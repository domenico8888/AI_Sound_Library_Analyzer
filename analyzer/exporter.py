import json



def export_assets(assets, output_file):


    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:


        json.dump(
            assets,
            f,
            indent=4,
            ensure_ascii=False
        )