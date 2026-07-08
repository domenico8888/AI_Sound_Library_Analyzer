import json
from pathlib import Path

from .plugin_detector import detect_plugin



def build_dataset(folder, output):


    dataset = []


    folder = Path(folder)



    for file in folder.rglob("*.fxp"):


        info = detect_plugin(file)


        dataset.append({

            "file": str(file),

            **info

        })



    with open(
        output,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            dataset,
            f,
            indent=4
        )


    return dataset