import re


def normalize_key(key):

    if not key:
        return {
            "root": None,
            "scale": None
        }


    key = key.strip()


    match = re.match(
        r"([A-Ga-g][#b]?)(.*)",
        key
    )


    if not match:

        return {
            "root": key,
            "scale": None
        }


    root = match.group(1).upper()

    scale_part = match.group(2).lower()



    if "min" in scale_part or "minor" in scale_part:

        scale = "minor"

    elif "maj" in scale_part or "major" in scale_part:

        scale = "major"

    else:

        scale = None



    return {

        "root": root,

        "scale": scale

    }