from pathlib import Path
import re



def extract_source_folder(path):

    parts = Path(path).parts

    if len(parts) >= 2:
        return parts[-2]

    return None



def extract_bpm(filename):

    match = re.search(
        r"\((\d+)\s*BPM\)",
        filename,
        re.IGNORECASE
    )

    if match:
        return int(match.group(1))

    return None



def extract_key(filename):

    keys = [
        "Cmin",
        "C#min",
        "Dmin",
        "D#min",
        "Emin",
        "Fmin",
        "F#min",
        "Gmin",
        "G#min",
        "Amin",
        "A#min",
        "Bmin",
        "Cmaj",
        "C#maj",
        "Dmaj",
        "D#maj",
        "Emaj",
        "Fmaj",
        "F#maj",
        "Gmaj",
        "G#maj",
        "Amaj",
        "A#maj",
        "Bmaj"
    ]


    for key in keys:

        if key.lower() in filename.lower():

            return key


    return None



def extract_metadata(path):

    filename = Path(path).name


    return {

        "source_folder": extract_source_folder(path),

        "bpm": extract_bpm(filename),

        "key": extract_key(filename)

    }