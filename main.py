from analyzer.pipeline import analyze_library


if __name__ == "__main__":

    input_folder = "libraries/The Producer School - Motion"

    output_file = "output/assets_dataset.json"

    assets = analyze_library(
        input_folder,
        output_file
    )

    print(
        f"Analizzati {len(assets)} asset"
    )