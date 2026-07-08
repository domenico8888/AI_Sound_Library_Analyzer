import json

from analyzer.pipeline import analyze_library



with open(
    "config.json"
) as f:

    config=json.load(f)



if config["mode"] == "analyze":


    analyze_library(

        config["dataset"]["input_folder"],

        config["dataset"]["analysis_output"]

    )


    print(
        "Analysis completed"
    )