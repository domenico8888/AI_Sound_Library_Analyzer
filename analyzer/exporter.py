import json



def export_json(objects, output_file):

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            objects,
            f,
            indent=4,
            ensure_ascii=False
        )