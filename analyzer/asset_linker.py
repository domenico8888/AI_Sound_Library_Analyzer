from pathlib import Path


def normalize_name(name):

    """
    Normalizza il nome per trovare corrispondenze
    tra preset, audio e midi.
    """

    name = Path(name).stem.lower()


    replacements = [
        "bs -",
        "ld -",
        "pl -",
        "ch -",
        "arp -",
        "fx -",
        "dr -"
    ]


    for item in replacements:
        name = name.replace(
            item,
            ""
        )


    name = (
        name
        .replace("_", " ")
        .replace("-", " ")
    )


    return " ".join(
        name.split()
    )




def calculate_similarity(name1, name2):

    """
    Similarità semplice dei nomi.
    """

    a = set(
        normalize_name(name1).split()
    )

    b = set(
        normalize_name(name2).split()
    )


    if not a or not b:
        return 0


    intersection = len(
        a.intersection(b)
    )


    union = len(
        a.union(b)
    )


    return round(
        intersection / union,
        3
    )





def link_assets(assets):

    """
    Collega preset, audio e midi
    appartenenti alla stessa famiglia.
    """


    for asset in assets:

        asset["related_assets"] = []



    for i, asset in enumerate(assets):


        for other in assets[i+1:]:


            if asset["asset_type"] == other["asset_type"]:
                continue



            similarity = calculate_similarity(
                asset["name"],
                other["name"]
            )


            if similarity >= 0.5:


                asset["related_assets"].append(
                    {
                        "id": other["id"],
                        "name": other["name"],
                        "type": other["asset_type"],
                        "similarity": similarity
                    }
                )


                other["related_assets"].append(
                    {
                        "id": asset["id"],
                        "name": asset["name"],
                        "type": asset["asset_type"],
                        "similarity": similarity
                    }
                )


    return assets