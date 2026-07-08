from pathlib import Path
import hashlib

from .models import Sound, SoundMetadata


# estensioni che vogliamo analizzare
SUPPORTED_EXTENSIONS = {

    ".wav",
    ".aif",
    ".aiff",

    ".mid",
    ".midi",

    ".fxp",
    ".fst",
    ".h2p"

}


def generate_id(path):

    return hashlib.md5(
        str(path).encode()
    ).hexdigest()



def detect_sound_type(extension):

    if extension in {
        ".wav",
        ".aif",
        ".aiff"
    }:
        return "audio"


    if extension in {
        ".mid",
        ".midi"
    }:
        return "midi"


    if extension in {
        ".fxp",
        ".fst",
        ".h2p"
    }:
        return "preset"


    return "unknown"



def scan_library(folder):

    sounds = []


    for file in Path(folder).rglob("*"):


        # ignora cartelle
        if not file.is_file():
            continue


        # ignora file nascosti macOS
        if file.name.startswith("."):
            continue


        extension = file.suffix.lower()


        # ignora file non musicali
        if extension not in SUPPORTED_EXTENSIONS:
            continue



        sound = Sound(

            id=generate_id(file),

            metadata=SoundMetadata(

                filename=file.name,

                extension=extension,

                path=str(file),

                sound_type=detect_sound_type(extension)

            )

        )


        sounds.append(sound)


    return sounds