from pathlib import Path

from .metadata_parser import (
    parse_preset_name,
    parse_audio_path
)

from .asset_metadata import extract_metadata

from .audio_analyzer import analyze_audio

from .midi_analyzer import analyze_midi

from .music_metadata import normalize_key



PLUGIN_BY_FOLDER = {

    "Serum Presets": "Serum",

    "Diva Presets": "Diva"

}



def detect_plugin(path):

    path = Path(path)

    for part in path.parts:

        if part in PLUGIN_BY_FOLDER:

            return PLUGIN_BY_FOLDER[part]


    return None




def build_assets(sounds):

    assets = []


    for sound in sounds:


        path = Path(
            sound.metadata.path
        )


        metadata = extract_metadata(path)


        asset = {


            "id": sound.id,


            "name": sound.metadata.filename,


            "asset_type": sound.metadata.sound_type,


            "category": None,


            "subcategory": None,


            "plugin": None,


            "metadata": metadata,


            "audio_features": {},


            "midi_features": {},


            "files": {

                "audio": None,

                "midi": None,

                "preset": None

            }

        }



        # -----------------------
        # KEY NORMALIZATION
        # -----------------------

        asset["metadata"]["key_normalized"] = normalize_key(

            asset["metadata"].get("key")

        )



        file_type = sound.metadata.sound_type




        # =====================
        # PRESET
        # =====================

        if file_type == "preset":


            asset["files"]["preset"] = str(path)


            asset["plugin"] = detect_plugin(path)



            preset_metadata = parse_preset_name(
                sound.metadata.filename
            )


            asset["category"] = preset_metadata["category"]


            asset["name"] = preset_metadata["name"]





        # =====================
        # AUDIO
        # =====================

        elif file_type == "audio":


            asset["files"]["audio"] = str(path)



            audio_metadata = parse_audio_path(path)


            asset["category"] = audio_metadata["category"]


            asset["subcategory"] = audio_metadata["subcategory"]



            asset["audio_features"] = analyze_audio(
                path
            )






        # =====================
        # MIDI
        # =====================

        elif file_type == "midi":


            asset["files"]["midi"] = str(path)



            midi_features = analyze_midi(
                path
            )



            midi_features["tempo"] = {


                "midi_bpm": midi_features.get(
                    "bpm_detected"
                ),


                "metadata_bpm": asset["metadata"].get(
                    "bpm"
                ),


                "effective_bpm": (

                    asset["metadata"].get("bpm")

                    or

                    midi_features.get("bpm_detected")

                )

            }



            asset["midi_features"] = midi_features




        assets.append(asset)



    return assets