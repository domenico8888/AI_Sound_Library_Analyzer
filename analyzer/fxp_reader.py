from pathlib import Path


def read_binary(file_path):

    file_path = Path(file_path)

    with open(file_path, "rb") as f:
        return f.read()



def extract_strings(data, min_length=4):

    strings = []

    current = []


    for byte in data:

        if 32 <= byte <= 126:

            current.append(chr(byte))

        else:

            if len(current) >= min_length:

                strings.append(
                    "".join(current)
                )

            current = []


    return strings



def analyze_fxp(file_path):

    data = read_binary(file_path)


    result = {

        "file": str(file_path),

        "size": len(data),

        "header": data[:16].hex(),

        "strings": extract_strings(data)

    }


    return result