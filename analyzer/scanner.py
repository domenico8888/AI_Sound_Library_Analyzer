from pathlib import Path
import hashlib

from .models import Sound, SoundMetadata


def generate_id(path):

    return hashlib.md5(
        str(path).encode()
    ).hexdigest()



def scan_library(folder):

    sounds = []


    for file in Path(folder).rglob("*"):

        if file.is_file():

            sound = Sound(

                id=generate_id(file),

                metadata=SoundMetadata(

                    filename=file.name,

                    extension=file.suffix.lower(),

                    path=str(file),

                    sound_type="unknown"

                )

            )


            sounds.append(sound)


    return sounds