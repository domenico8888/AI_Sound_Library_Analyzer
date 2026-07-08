from pathlib import Path

from .metadata_parser import (
    parse_preset_name,
    parse_audio_path
)



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


        asset = {

            "id": sound.id,

            "name": sound.metadata.filename,

            "asset_type": sound.metadata.sound_type,

            "category": None,

            "subcategory": None,

            "plugin": None,

            "files": {

                "audio": None,

                "midi": None,

                "preset": None

            }

        }



        file_type = sound.metadata.sound_type



        # =====================
        # PRESET
        # =====================

        if file_type == "preset":


            asset["files"]["preset"] = str(path)


            asset["plugin"] = detect_plugin(path)


            metadata = parse_preset_name(
                sound.metadata.filename
            )


            asset["category"] = metadata["category"]


            asset["name"] = metadata["name"]




        # =====================
        # AUDIO
        # =====================

        elif file_type == "audio":


            asset["files"]["audio"] = str(path)


            metadata = parse_audio_path(path)


            asset["category"] = metadata["category"]

            asset["subcategory"] = metadata["subcategory"]




        # =====================
        # MIDI
        # =====================

        elif file_type == "midi":


            asset["files"]["midi"] = str(path)



        assets.append(asset)



    return assets