from .scanner import scan_library
from .dataset_builder import build_dataset



def analyze_library(config):

    files = scan_library(
        config["library_path"],
        config["extensions"]
    )


    return files



def create_dataset(config):

    dataset = build_dataset(
        config["dataset"]["input_folder"],
        config["dataset"]["output"]
    )


    return dataset