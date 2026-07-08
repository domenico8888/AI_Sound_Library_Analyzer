from .fxp_reader import analyze_fxp



PLUGIN_SIGNATURES = {

    "Serum": [
        "Serum",
        "Xfer"
    ],

    "Diva": [
        "DIVA",
        "u-he"
    ],

    "Massive": [
        "Massive",
        "Native Instruments"
    ]

}



def detect_plugin(file_path):


    analysis = analyze_fxp(file_path)


    text = " ".join(
        analysis["strings"]
    )


    for plugin, signatures in PLUGIN_SIGNATURES.items():


        score = 0


        for signature in signatures:

            if signature.lower() in text.lower():

                score += 1



        if score:

            return {

                "plugin": plugin,

                "confidence": score / len(signatures),

                "analysis": analysis

            }



    return {

        "plugin": "Unknown",

        "confidence": 0,

        "analysis": analysis

    }