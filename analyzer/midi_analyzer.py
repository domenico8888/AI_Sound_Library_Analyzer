import pretty_midi



def midi_note_name(note_number):

    names = [

        "C","C#","D","D#",
        "E","F","F#","G",
        "G#","A","A#","B"

    ]


    octave = (note_number // 12) - 1


    return f"{names[note_number % 12]}{octave}"




def detect_register(min_pitch, max_pitch):

    avg = (min_pitch + max_pitch) / 2


    if avg < 48:

        return "low"


    elif avg < 60:

        return "low-mid"


    elif avg < 72:

        return "mid"


    elif avg < 84:

        return "high-mid"


    return "high"





def analyze_midi(path):

    try:


        midi = pretty_midi.PrettyMIDI(
            str(path)
        )



        tempos = midi.get_tempo_changes()


        bpm = None


        if len(tempos[1]):

            bpm = float(
                round(
                    tempos[1][0],
                    2
                )
            )



        notes = []


        tracks = []



        for instrument in midi.instruments:


            track_notes = []


            for note in instrument.notes:


                item = {

                    "pitch": int(note.pitch),

                    "note": midi_note_name(
                        note.pitch
                    ),

                    "start": round(
                        note.start,
                        4
                    ),

                    "end": round(
                        note.end,
                        4
                    ),

                    "duration": round(
                        note.end-note.start,
                        4
                    ),

                    "velocity": int(
                        note.velocity
                    )

                }


                notes.append(note)


                track_notes.append(item)



            tracks.append({

                "name": instrument.name,

                "program": int(
                    instrument.program
                ),

                "is_drum": instrument.is_drum,

                "notes_count": len(track_notes),

                "notes": track_notes

            })




        pitches = [

            n.pitch

            for n in notes

        ]



        pitch_range = None

        register = None



        if pitches:


            pitch_range = {

                "min": {

                    "midi": int(min(pitches)),

                    "note": midi_note_name(
                        min(pitches)
                    )

                },

                "max": {

                    "midi": int(max(pitches)),

                    "note": midi_note_name(
                        max(pitches)
                    )

                }

            }


            register = detect_register(

                min(pitches),

                max(pitches)

            )




        duration = midi.get_end_time()



        musical_features = {


            "bars": None,


            "beats": None,


            "note_density": round(

                len(notes) / duration,

                2

            ) if duration else 0,


            "average_note_duration": round(

                sum(
                    n.end-n.start
                    for n in notes
                )
                /
                len(notes),

                4

            ) if notes else 0,


            "register": register

        }




        return {


            "duration_seconds": round(
                duration,
                3
            ),


            "tracks_count": len(
                midi.instruments
            ),


            "notes_count": len(notes),


            "bpm_detected": bpm,


            "pitch_range": pitch_range,


            "musical_features": musical_features,


            "tracks": tracks

        }



    except Exception as e:


        return {

            "error": str(e)

        }