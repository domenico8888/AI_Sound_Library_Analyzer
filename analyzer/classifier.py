AUDIO_EXTENSIONS = {
    ".wav",
    ".aiff",
    ".aif"
}


MIDI_EXTENSIONS = {
    ".mid",
    ".midi"
}


PRESET_EXTENSIONS = {
    ".fxp",
    ".h2p",
    ".vital"
}



def classify(sound):

    ext = sound.metadata.extension


    if ext in AUDIO_EXTENSIONS:

        sound.metadata.sound_type = "audio"


    elif ext in MIDI_EXTENSIONS:

        sound.metadata.sound_type = "midi"


    elif ext in PRESET_EXTENSIONS:

        sound.metadata.sound_type = "preset"


    return sound