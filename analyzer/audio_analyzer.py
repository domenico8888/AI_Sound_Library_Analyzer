import librosa
import numpy as np



def analyze_audio(path):

    try:

        y, sr = librosa.load(
            path,
            sr=None
        )


        duration = librosa.get_duration(
            y=y,
            sr=sr
        )


        tempo = None


        # Il BPM ha senso soprattutto per loop e sample più lunghi
        if duration >= 1.0:

            estimated_tempo, _ = librosa.beat.beat_track(
                y=y,
                sr=sr
            )

            tempo = round(
                float(np.mean(estimated_tempo)),
                2
            )



        rms = librosa.feature.rms(
            y=y
        )


        spectral_centroid = librosa.feature.spectral_centroid(
            y=y,
            sr=sr
        )


        zero_crossing = librosa.feature.zero_crossing_rate(
            y
        )


        mfcc = librosa.feature.mfcc(
            y=y,
            sr=sr,
            n_mfcc=13
        )


        return {

            "duration": round(
                float(duration),
                3
            ),


            "sample_rate": sr,


            "tempo": tempo,


            "rms_energy": round(
                float(np.mean(rms)),
                5
            ),


            "spectral_centroid": round(
                float(np.mean(spectral_centroid)),
                2
            ),


            "zero_crossing_rate": round(
                float(np.mean(zero_crossing)),
                5
            ),


            "mfcc": [

                round(
                    float(x),
                    3
                )

                for x in np.mean(
                    mfcc,
                    axis=1
                )

            ]

        }


    except Exception as e:


        return {

            "error": str(e)

        }