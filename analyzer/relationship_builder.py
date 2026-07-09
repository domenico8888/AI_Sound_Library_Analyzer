import json
import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


DATASET_FILE = (
    BASE_DIR /
    "output" /
    "assets_dataset.json"
)



# ----------------------------
# NORMALIZZAZIONE NOME
# ----------------------------

def normalize_name(name):

    name = name.lower()


    # togli estensione
    name = re.sub(
        r"\.(wav|mp3|aif|aiff|mid|midi|fxp|fxb|h2p|nksf)$",
        "",
        name
    )


    # togli bpm
    name = re.sub(
        r"\d+\s*bpm",
        "",
        name
    )


    # togli note musicali
    name = re.sub(
        r"\b[a-g](#|b)?m?\b",
        "",
        name
    )


    # solo lettere numeri
    name = re.sub(
        r"[^a-z0-9]+",
        " ",
        name
    )


    return name.strip()



# ----------------------------
# FAMILY ID
# ----------------------------

def create_family_id(name):

    normalized = normalize_name(
        name
    )


    words = normalized.split()


    # rimuoviamo parole generiche

    blacklist = [

        "wav",
        "audio",
        "preset",
        "patch",
        "sound"

    ]


    words=[

        w for w in words
        if w not in blacklist

    ]


    return "_".join(words)





# ----------------------------
# MATCH ASSET
# ----------------------------

def similarity_name(a,b):


    a=set(
        create_family_id(a).split("_")
    )


    b=set(
        create_family_id(b).split("_")
    )


    if not a or not b:
        return 0



    return len(
        a.intersection(b)
    ) / len(
        a.union(b)
    )






# ----------------------------
# BUILD RELATIONSHIPS
# ----------------------------

def build_relationships():


    print(
        "Caricamento dataset..."
    )


    with open(
        DATASET_FILE,
        "r",
        encoding="utf8"
    ) as f:

        assets=json.load(f)



    print(
        "Asset:",
        len(assets)
    )



    # assegna family

    for asset in assets:


        asset["family_id"] = create_family_id(
            asset["name"]
        )


        asset["related_assets"]=[]





    # confronto tutti contro tutti

    for i,asset in enumerate(assets):


        for other in assets[i+1:]:


            score=similarity_name(
                asset["name"],
                other["name"]
            )



            if score >= 0.5:


                asset["related_assets"].append({

                    "id":
                    other["id"],

                    "name":
                    other["name"],

                    "asset_type":
                    other["asset_type"],

                    "file":
                    other["files"].get(
                        "audio"
                    )
                    or
                    other["files"].get(
                        "midi"
                    )
                    or
                    other["files"].get(
                        "preset"
                    )

                })



                other["related_assets"].append({

                    "id":
                    asset["id"],

                    "name":
                    asset["name"],

                    "asset_type":
                    asset["asset_type"],

                    "file":
                    asset["files"].get(
                        "audio"
                    )
                    or
                    asset["files"].get(
                        "midi"
                    )
                    or
                    asset["files"].get(
                        "preset"
                    )

                })




    with open(
        DATASET_FILE,
        "w",
        encoding="utf8"
    ) as f:


        json.dump(
            assets,
            f,
            indent=4,
            ensure_ascii=False
        )



    print(
        "Relazioni create!"
    )




if __name__=="__main__":

    build_relationships()