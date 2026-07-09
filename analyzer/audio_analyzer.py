import librosa
import numpy as np
import warnings


def hz_to_note(freq):

    if freq <= 0:
        return None

    midi = (
        69 +
        12 *
        np.log2(freq / 440)
    )

    note_names = [
        "C",
        "C#",
        "D",
        "D#",
        "E",
        "F",
        "F#",
        "G",
        "G#",
        "A",
        "A#",
        "B"
    ]

    note = note_names[
        int(round(midi)) % 12
    ]

    octave = (
        int(round(midi)) // 12
    ) - 1


    return {
        "hz": round(float(freq),2),
        "midi": round(float(midi),2),
        "note": f"{note}{octave}"
    }



def detect_pitch(y, sr):

    try:

        # per bass e synth
        # limitiamo la ricerca
        pitches, magnitudes = librosa.piptrack(
            y=y,
            sr=sr,
            fmin=35,
            fmax=500
        )


        candidates = []


        for t in range(
            pitches.shape[1]
        ):

            idx = magnitudes[:,t].argmax()

            pitch = pitches[idx,t]

            magnitude = magnitudes[idx,t]


            if (
                pitch > 35
                and magnitude > 0.05
            ):

                candidates.append(
                    pitch
                )



        if len(candidates) < 3:
            return None



        # mediana più stabile
        freq = np.median(
            candidates
        )


        return hz_to_note(
            freq
        )


    except Exception:

        return None




def analyze_audio(audio_path):

    features = {}


    try:


        # ======================
        # LOAD
        # ======================


        y, sr = librosa.load(
            audio_path,
            sr=None,
            mono=True
        )


        duration = librosa.get_duration(
            y=y,
            sr=sr
        )


        features["duration"] = round(
            float(duration),
            3
        )

        features["sample_rate"] = sr



        # ======================
        # PARAMETRI FFT
        # ======================


        signal_length = len(y)


        if signal_length < 1024:

            n_fft = 512

        else:

            n_fft = 2048



        hop_length = 512




        # ======================
        # RMS
        # ======================


        rms = librosa.feature.rms(
            y=y,
            frame_length=n_fft,
            hop_length=hop_length
        )


        rms_value = float(
            np.mean(rms)
        )


        features["rms_energy"] = round(
            rms_value,
            5
        )




        # ======================
        # SPECTRAL FEATURES
        # ======================


        centroid = librosa.feature.spectral_centroid(
            y=y,
            sr=sr,
            n_fft=n_fft,
            hop_length=hop_length
        )


        rolloff = librosa.feature.spectral_rolloff(
            y=y,
            sr=sr,
            n_fft=n_fft,
            hop_length=hop_length
        )


        bandwidth = librosa.feature.spectral_bandwidth(
            y=y,
            sr=sr,
            n_fft=n_fft,
            hop_length=hop_length
        )


        flatness = librosa.feature.spectral_flatness(
            y=y,
            n_fft=n_fft,
            hop_length=hop_length
        )


        features["spectral_centroid"] = round(
            float(np.mean(centroid)),
            2
        )


        features["spectral_rolloff"] = round(
            float(np.mean(rolloff)),
            2
        )


        features["spectral_bandwidth"] = round(
            float(np.mean(bandwidth)),
            2
        )


        features["spectral_flatness"] = round(
            float(np.mean(flatness)),
            6
        )




        # ======================
        # ZERO CROSSING
        # ======================


        zcr = librosa.feature.zero_crossing_rate(
            y,
            hop_length=hop_length
        )


        zcr_value = float(
            np.mean(zcr)
        )


        features["zero_crossing_rate"] = round(
            zcr_value,
            5
        )




        # ======================
        # MFCC
        # ======================


        mfcc = librosa.feature.mfcc(
            y=y,
            sr=sr,
            n_mfcc=13,
            n_fft=n_fft,
            hop_length=hop_length
        )


        mfcc_values = [

            round(float(x),3)

            for x in np.mean(
                mfcc,
                axis=1
            )

        ]


        features["mfcc"] = mfcc_values




        # ======================
        # CONTRAST
        # ======================


        try:

            contrast = librosa.feature.spectral_contrast(
                y=y,
                sr=sr,
                n_fft=n_fft,
                hop_length=hop_length
            )


            features["spectral_contrast"] = [

                round(float(x),3)

                for x in np.mean(
                    contrast,
                    axis=1
                )

            ]


        except:

            features["spectral_contrast"] = []





        # ======================
        # CHROMA
        # ======================


        try:

            chroma = librosa.feature.chroma_stft(
                y=y,
                sr=sr,
                n_fft=n_fft,
                hop_length=hop_length
            )


            features["chroma"] = [

                round(float(x),3)

                for x in np.mean(
                    chroma,
                    axis=1
                )

            ]

        except:

            features["chroma"] = []






        # ======================
        # PITCH
        # ======================


        pitch_data = detect_pitch(
            y,
            sr
        )


        features["pitch"] = pitch_data




        # ======================
        # TEMPO
        # ======================


        tempo = None


        if duration >= 3:


            try:

                with warnings.catch_warnings():

                    warnings.simplefilter(
                        "ignore"
                    )


                    tempo_value = librosa.feature.rhythm.tempo(
                        y=y,
                        sr=sr
                    )


                    if len(tempo_value):

                        tempo = float(
                            tempo_value[0]
                        )


            except:

                pass



        features["tempo"] = (

            round(tempo,2)

            if tempo

            else None

        )






        # ======================
        # AI EMBEDDING
        # ======================


        embedding = []


        embedding.extend(
            mfcc_values
        )


        embedding.extend([

            rms_value,

            np.mean(centroid),

            np.mean(rolloff),

            np.mean(bandwidth),

            np.mean(flatness),

            zcr_value,

            duration

        ])



        if pitch_data:

            embedding.append(
                pitch_data["midi"]
            )

        else:

            embedding.append(
                0.0
            )



        features["embedding"] = [

            round(float(x),5)

            for x in embedding

        ]



        return features



    except Exception as e:


        print(
            f"Errore analisi audio {audio_path}: {e}"
        )


        return {

            "duration":None,
            "sample_rate":None,
            "rms_energy":None,
            "mfcc":[],
            "pitch":None,
            "tempo":None,
            "embedding":[]

        }