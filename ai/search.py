import faiss
import numpy as np
import json
from pathlib import Path



BASE_DIR=Path(__file__).resolve().parent.parent


INDEX_FILE=BASE_DIR/"output"/"faiss.index"

IDS_FILE=BASE_DIR/"output"/"embeddings_ids.npy"

ASSETS_FILE=BASE_DIR/"output"/"assets_dataset.json"



index=faiss.read_index(
    str(INDEX_FILE)
)



ids=np.load(
    IDS_FILE,
    allow_pickle=True
)



with open(
    ASSETS_FILE,
    "r",
    encoding="utf8"
) as f:

    assets=json.load(f)



asset_map={

    a["id"]:a

    for a in assets

}





def search_similar(
        embedding,
        category=None,
        subcategory=None,
        limit=10
):


    vector=np.array(
        [embedding],
        dtype="float32"
    )


    faiss.normalize_L2(
        vector
    )



    # cerchiamo molti candidati
    scores,indexes=index.search(
        vector,
        100
    )



    results=[]



    for score,idx in zip(
        scores[0],
        indexes[0]
    ):


        if idx==-1:
            continue



        asset_id=ids[idx]


        asset=asset_map.get(
            asset_id
        )


        if not asset:
            continue



        # elimina stesso file

        if np.array_equal(
            embedding,
            asset["audio_features"]["embedding"]
        ):

            continue



        # filtro categoria

        if category:

            if asset["category"] != category:
                continue



        if subcategory:

            if asset["subcategory"] != subcategory:
                continue



        results.append({

            "similarity":round(
                float(score),
                4
            ),

            "name":
                asset["name"],

            "category":
                asset["category"],

            "subcategory":
                asset["subcategory"],

            "duration":
                asset["audio_features"]["duration"],

            "file":
                asset["files"]["audio"]

        })



        if len(results)>=limit:
            break



    return results





if __name__=="__main__":


    test=assets[0]


    print("\nSUONO DI PARTENZA:")
    print(
        test["name"]
    )


    print(
        "\nSIMILI TROVATI:\n"
    )



    results=search_similar(

        test["audio_features"]["embedding"],

        category=test["category"],

        subcategory=test["subcategory"],

        limit=10

    )



    for r in results:

        print(r)