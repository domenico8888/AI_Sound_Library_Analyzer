import json
from pathlib import Path



CONFIG_FILE = "config.json"



def load_config():

    config_path = Path(CONFIG_FILE)


    if not config_path.exists():

        raise FileNotFoundError(
            "config.json non trovato"
        )


    with open(
        config_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)