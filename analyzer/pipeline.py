from .scanner import scan_library

from .asset_builder import build_assets

from .asset_linker import link_assets

from .exporter import export_assets




def analyze_library(input_folder, output_file):


    sounds = scan_library(
        input_folder
    )



    assets = build_assets(
        sounds
    )



    assets = link_assets(
        assets
    )



    export_assets(
        assets,
        output_file
    )



    return assets