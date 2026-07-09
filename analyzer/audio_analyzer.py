import librosa
import numpy as np
import warnings


def analyze_audio(audio_path):

    features = {}

    try:

        # ============================
        # LOAD AUDIO
        # ============================

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



        # ============================
        # FFT DINAMICO
        # ============================

        signal_length = len(y)


        if signal_length < 512:
            n_fft = 256

        elif signal_length < 1024:
            n_fft = 512

        else:
            n_fft = 2048



        # ============================
        # RMS ENERGY
        # ============================

        rms = librosa.feature.rms(
            y=y
        )


        rms_value = float(
            np.mean(rms)
        )


        features["rms_energy"] = round(
            rms_value,
            5
        )



        # ============================
        # SPECTRAL CENTROID
        # ============================

        centroid = librosa.feature.spectral_centroid(
            y=y,
            sr=sr,
            n_fft=n_fft
        )


        centroid_value = float(
            np.mean(centroid)
        )


        features["spectral_centroid"] = round(
            centroid_value,
            2
        )



        # ============================
        # SPECTRAL ROLLOFF
        # ============================

        rolloff = librosa.feature.spectral_rolloff(
            y=y,
            sr=sr,
            n_fft=n_fft
        )


        rolloff_value = float(
            np.mean(rolloff)
        )


        features["spectral_rolloff"] = round(
            rolloff_value,
            2
        )



        # ============================
        # SPECTRAL BANDWIDTH
        # ============================

        bandwidth = librosa.feature.spectral_bandwidth(
            y=y,
            sr=sr,
            n_fft=n_fft
        )


        bandwidth_value = float(
            np.mean(bandwidth)
        )


        features["spectral_bandwidth"] = round(
            bandwidth_value,
            2
        )



        # ============================
        # SPECTRAL CONTRAST
        # ============================

        contrast = librosa.feature.spectral_contrast(
            y=y,
            sr=sr,
            n_fft=n_fft
        )


        contrast_values = [
            float(x)
            for x in np.mean(
                contrast,
                axis=1
            )
        ]


        features["spectral_contrast"] = [
            round(x,3)
            for x in contrast_values
        ]



        # ============================
        # CHROMA
        # ============================

        chroma = librosa.feature.chroma_stft(
            y=y,
            sr=sr,
            n_fft=n_fft
        )


        chroma_values = [
            float(x)
            for x in np.mean(
                chroma,
                axis=1
            )
        ]


        features["chroma"] = [
            round(x,3)
            for x in chroma_values
        ]



        # ============================
        # ZERO CROSSING RATE
        # ============================

        zcr = librosa.feature.zero_crossing_rate(
            y
        )


        zcr_value = float(
            np.mean(zcr)
        )


        features["zero_crossing_rate"] = round(
            zcr_value,
            5
        )



        # ============================
        # MFCC
        # ============================

        mfcc = librosa.feature.mfcc(
            y=y,
            sr=sr,
            n_mfcc=13,
            n_fft=n_fft
        )


        mfcc_values = [
            round(float(x),3)
            for x in np.mean(
                mfcc,
                axis=1
            )
        ]


        features["mfcc"] = mfcc_values



        # ============================
        # PITCH
        # ============================

        pitch_data = None


        try:

            pitches, magnitudes = librosa.piptrack(
                y=y,
                sr=sr,
                fmin=30,
                fmax=1000
            )


            pitch_values = []


            for t in range(
                pitches.shape[1]
            ):

                index = magnitudes[:,t].argmax()

                pitch = pitches[index,t]


                if pitch > 0:

                    pitch_values.append(
                        pitch
                    )



            if len(pitch_values) > 5:


                freq = np.percentile(
                    pitch_values,
                    20
                )


                midi = (
                    69 +
                    12 *
                    np.log2(
                        freq / 440
                    )
                )


                note_names = [
                    "C","C#","D",
                    "D#","E","F",
                    "F#","G","G#",
                    "A","A#","B"
                ]


                note = note_names[
                    int(round(midi)) % 12
                ]


                octave = (
                    int(round(midi)) // 12
                ) - 1



                pitch_data = {

                    "hz": round(
                        float(freq),
                        2
                    ),

                    "midi": round(
                        float(midi),
                        2
                    ),

                    "note": f"{note}{octave}"

                }


        except Exception:

            pitch_data = None



        features["pitch"] = pitch_data



        # ============================
        # TEMPO
        # ============================

        tempo = None


        if duration >= 3:

            try:

                with warnings.catch_warnings():

                    warnings.simplefilter(
                        "ignore"
                    )

                    tempo_value = (
                        librosa.feature.rhythm.tempo(
                            y=y,
                            sr=sr
                        )
                    )


                    if len(tempo_value):

                        tempo = float(
                            tempo_value[0]
                        )


            except Exception:

                tempo = None



        features["tempo"] = (
            round(tempo,2)
            if tempo
            else None
        )



        # ============================
        # AI EMBEDDING
        # ============================

        embedding = []


        # MFCC
        embedding.extend(
            [
                float(x)
                for x in mfcc_values
            ]
        )


        # Spectral features
        embedding.extend([

            rms_value,

            centroid_value,

            rolloff_value,

            bandwidth_value,

            zcr_value,

            duration

        ])


        # Contrast

        embedding.extend(
            contrast_values
        )


        # Chroma

        embedding.extend(
            chroma_values
        )


        # Pitch

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



    except Exception as e:


        print(
            f"Errore analisi audio {audio_path}: {e}"
        )


        return {

            "duration": None,
            "sample_rate": None,
            "tempo": None,
            "rms_energy": None,
            "spectral_centroid": None,
            "spectral_rolloff": None,
            "spectral_bandwidth": None,
            "zero_crossing_rate": None,
            "mfcc": [],
            "pitch": None,
            "embedding": []

        }



    return features