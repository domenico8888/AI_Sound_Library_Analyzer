from .scanner import scan_library
from .asset_builder import build_assets
from .exporter import export_json



def analyze_library(input_folder, output_file):

    sounds = scan_library(
        input_folder
    )

    assets = build_assets(
        sounds
    )

    export_json(
        assets,
        output_file
    )

    return assets