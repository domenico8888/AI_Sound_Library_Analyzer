from .scanner import scan_library
from .dataset_builder import build_dataset
from .classifier import classify
from .exporter import export_json


def analyze_library(input_folder,output_file):


    sounds = scan_library(
        input_folder
    )


    sounds = [

        classify(sound)

        for sound in sounds

    ]


    export_json(
        sounds,
        output_file
    )


    return sounds

def create_dataset(config):

    dataset = build_dataset(
        config["dataset"]["input_folder"],
        config["dataset"]["output"]
    )


    return dataset