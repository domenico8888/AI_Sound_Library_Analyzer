from pathlib import Path
from .plugin_detector import detect_plugin


def scan_library(folder, extensions):

    folder = Path(folder)

    results = []


    audio_extensions = set(
        extensions["audio"]
    )

    midi_extensions = set(
        extensions["midi"]
    )

    preset_extensions = set(
        extensions["preset"]
    )



    for file in folder.rglob("*"):

        if not file.is_file():
            continue


        ext = file.suffix.lower()



        if ext in audio_extensions:

            results.append({
                "path": str(file),
                "type": "audio"
            })


        elif ext in midi_extensions:

            results.append({
                "path": str(file),
                "type": "midi"
            })



        elif ext in preset_extensions:

            plugin_info = detect_plugin(file)

            results.append({

                "path": str(file),

                "type": "preset",

                **plugin_info

            })


    return results