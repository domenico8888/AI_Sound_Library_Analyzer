import json
import os
import numpy as np

from sklearn.preprocessing import StandardScaler
import joblib



def build_embedding_database(
        json_path,
        output_dir="database"
):

    """
    Costruisce il database vettoriale
    partendo dal JSON della libreria analizzata
    """

    os.makedirs(
        output_dir,
        exist_ok=True
    )


    # ============================
    # CARICA JSON
    # ============================

    with open(
        json_path,
        "r",
        encoding="utf-8"
    ) as f:

        assets = json.load(f)



    vectors = []
    metadata = []



    # ============================
    # ESTRAZIONE EMBEDDING
    # ============================

    for asset in assets:


        audio_features = asset.get(
            "audio_features"
        )


        if not audio_features:
            continue


        embedding = audio_features.get(
            "embedding"
        )


        if not embedding:
            continue



        vectors.append(
            embedding
        )


        metadata.append({

            "id": asset.get(
                "id"
            ),

            "name": asset.get(
                "name"
            ),

            "category": asset.get(
                "category"
            ),

            "subcategory": asset.get(
                "subcategory"
            ),

            "plugin": asset.get(
                "plugin"
            ),

            "path": asset.get(
                "files",
                {}
            ).get(
                "audio"
            )

        })



    if len(vectors) == 0:

        raise Exception(
            "Nessun embedding trovato"
        )



    X = np.array(
        vectors,
        dtype=np.float32
    )



    print(
        f"Embedding caricati: {X.shape}"
    )



    # ============================
    # NORMALIZZAZIONE
    # ============================

    scaler = StandardScaler()


    X_scaled = scaler.fit_transform(
        X
    )



    # ============================
    # SALVATAGGIO
    # ============================


    np.save(
        os.path.join(
            output_dir,
            "embeddings.npy"
        ),
        X_scaled
    )



    with open(
        os.path.join(
            output_dir,
            "metadata.json"
        ),
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            metadata,
            f,
            indent=4,
            ensure_ascii=False
        )



    joblib.dump(
        scaler,
        os.path.join(
            output_dir,
            "scaler.pkl"
        )
    )


    print(
        "Database embedding creato!"
    )


    return X_scaled, metadata