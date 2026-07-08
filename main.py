import json

from analyzer.pipeline import analyze_library
from analyzer.dataset_builder import build_dataset



with open("config.json", encoding="utf-8") as f:

    config = json.load(f)



mode = config.get("mode")



if mode == "analyze":


    analyze_library(

        config["dataset"]["input_folder"],

        config["dataset"]["analysis_output"]

    )


    print(
        "Analysis completed"
    )



elif mode == "dataset":


    build_dataset(

        config["dataset"]["analysis_output"],

        config["dataset"]["dataset_output"]

    )


    print(
        "Dataset generated"
    )



else:


    raise ValueError(
        f"Unknown mode: {mode}"
    )