import json
import numpy as np
import faiss
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


ASSETS_FILE = BASE_DIR / "output" / "assets_dataset.json"

INDEX_FILE = BASE_DIR / "output" / "faiss.index"

IDS_FILE = BASE_DIR / "output" / "embeddings_ids.npy"



def build_index():

    print("Caricamento dataset...")


    with open(
        ASSETS_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        assets=json.load(f)



    embeddings=[]
    ids=[]



    for asset in assets:


        audio=asset.get(
            "audio_features"
        )


        if not audio:
            continue



        emb=audio.get(
            "embedding"
        )


        if emb:


            embeddings.append(
                emb
            )

            ids.append(
                asset["id"]
            )



    matrix=np.array(
        embeddings,
        dtype="float32"
    )



    print(
        "Embedding caricati:",
        matrix.shape
    )



    # normalizzazione
    faiss.normalize_L2(
        matrix
    )



    dim=matrix.shape[1]


    index=faiss.IndexFlatIP(
        dim
    )


    index.add(
        matrix
    )



    faiss.write_index(
        index,
        str(INDEX_FILE)
    )



    np.save(
        IDS_FILE,
        ids
    )



    print(
        "Indice FAISS creato!"
    )



if __name__=="__main__":

    build_index()