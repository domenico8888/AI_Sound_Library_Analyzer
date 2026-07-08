import json

from analyzer.config_loader import load_config
from analyzer.pipeline import (
    analyze_library,
    create_dataset
)



config = load_config()



mode = config.get(
    "mode",
    "analyze"
)



if mode == "analyze":


    result = analyze_library(
        config
    )


    output = config["output_file"]



elif mode == "dataset":


    result = create_dataset(
        config
    )


    output = config["dataset"]["output"]



else:

    raise ValueError(
        f"Modalità sconosciuta: {mode}"
    )



with open(
    output,
    "w",
    encoding="utf-8"
) as file:


    json.dump(
        result,
        file,
        indent=4
    )


print(
    f"Completato: {output}"
)