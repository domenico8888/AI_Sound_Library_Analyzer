from pathlib import Path
import re


CATEGORY_MAP = {

    "BS": "Bass",
    "LD": "Lead",
    "CH": "Chord",
    "PL": "Pluck",
    "PD": "Pad",
    "FX": "FX",
    "AR": "Arpeggio"

}



def parse_preset_name(filename):

    name = filename.rsplit(".", 1)[0]

    result = {

        "category": None,

        "name": name

    }


    match = re.match(
        r"([A-Z]{2})\s*-\s*(.*)",
        name
    )


    if match:

        prefix = match.group(1)

        result["category"] = CATEGORY_MAP.get(
            prefix,
            "Unknown"
        )

        result["name"] = match.group(2)


    return result



# ==========================
# AUDIO METADATA
# ==========================


AUDIO_CATEGORY_MAP = {

    "Bass Shots": {
        "category": "Bass",
        "subcategory": "Shot"
    },

    "Bass Loops": {
        "category": "Bass",
        "subcategory": "Loop"
    },

    "Synth Shots": {
        "category": "Synth",
        "subcategory": "Shot"
    },

    "Kicks": {
        "category": "Drum",
        "subcategory": "Kick"
    },

    "Snares": {
        "category": "Drum",
        "subcategory": "Snare"
    },

    "Claps": {
        "category": "Drum",
        "subcategory": "Clap"
    },

    "Percussion": {
        "category": "Drum",
        "subcategory": "Percussion"
    },

    "Perc Loops": {
        "category": "Drum",
        "subcategory": "Perc Loop"
    },

    "Hat Loops": {
        "category": "Drum",
        "subcategory": "Hat Loop"
    },

    "Open Hats": {
        "category": "Drum",
        "subcategory": "Open Hat"
    },

    "Closed Hats": {
        "category": "Drum",
        "subcategory": "Closed Hat"
    },

    "Toms": {
        "category": "Drum",
        "subcategory": "Tom"
    },

    "Rims": {
        "category": "Drum",
        "subcategory": "Rim"
    },

    "Shakers": {
        "category": "Drum",
        "subcategory": "Shaker"
    },

    "Hooks": {
        "category": "Musical",
        "subcategory": "Hook"
    },

    "Adlibs": {
        "category": "Vocal",
        "subcategory": "Adlib"
    },

    "Spoken Words": {
        "category": "Vocal",
        "subcategory": "Spoken"
    },

    "MiscFX": {
        "category": "FX",
        "subcategory": "Misc"
    },

    "Impacts": {
        "category": "FX",
        "subcategory": "Impact"
    },

    "Uplifters": {
        "category": "FX",
        "subcategory": "Uplifter"
    },

    "Downlifters": {
        "category": "FX",
        "subcategory": "Downlifter"
    },

    "Ambience": {
        "category": "Atmosphere",
        "subcategory": "Ambience"
    },

    "Fills": {
        "category": "Drum",
        "subcategory": "Fill"
    },
    "Shaker Loops": {
        "category": "Drum",
        "subcategory": "Shaker Loop"
    },
    "Crashes": {
        "category": "Drum",
        "subcategory": "Crash"
    },

    "Minimal Loops": {
        "category": "Drum",
        "subcategory": "Minimal Loop"
    },

    "Top Loops": {
        "category": "Drum",
        "subcategory": "Top Loop"
    },

    "Loops": {
        "category": "Loop",
        "subcategory": None
    }

}



def parse_audio_path(path):

    parts = Path(path).parts


    for folder, metadata in AUDIO_CATEGORY_MAP.items():

        if folder in parts:

            return metadata


    return {

        "category": None,

        "subcategory": None

    }