import json
from pathlib import Path



def export_json(objects, filename):

    data = [

        obj.to_dict()

        for obj in objects

    ]


    Path(filename).parent.mkdir(
        exist_ok=True
    )


    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:


        json.dump(

            data,

            f,

            indent=4,

            ensure_ascii=False

        )