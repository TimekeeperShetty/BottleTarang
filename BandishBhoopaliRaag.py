from midiutil import MIDIFile
from mingus.core import notes

note_progression = ["C", "E", "D", "E", "C", "A", "C", "D", 
                     "E", "D", "E", "G", "E", "D", "E", "E", "G", "E", "D", "E", "G",
                     "A", "C", "A", "G", "E", "D", "C", "A",
                     "E", "E", "E", "G", "G", "C", "A", "C", "C", "C", "C",
                     "C", "D", "C", "C", "A", "A", "A", "C", "C", "D", "D",
                     "C", "D", "E", "C", "A", "G", "G",
                     "E", "E", "E", "D", "E", "G", "A", "C",
                     "G", "A", "C", "A", "G", "E", "D", "C", "A"]

NOTES = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
OCTAVES = list(range(11))
NOTES_IN_OCTAVE = len(NOTES)

errors = {
    'notes': 'Bad input, please refer this spec-\n'
}


def swap_accidentals(note):
    if note == 'Db':
        return 'C#'
    if note == 'D#':
        return 'Eb'
    if note == 'E#':
        return 'F'
    if note == 'Gb':
        return 'F#'
    if note == 'G#':
        return 'Ab'
    if note == 'A#':
        return 'Bb'
    if note == 'B#':
        return 'C'

    return note


def note_to_number(note: str, octave: int) -> int:
    note = swap_accidentals(note)
    assert note in NOTES, errors['notes']
    assert octave in OCTAVES, errors['notes']

    note = NOTES.index(note)
    note += (NOTES_IN_OCTAVE * octave)

    assert 0 <= note <= 127, errors['notes']

    return note


track = 0
channel = 0
time = 0  # In beats
duration = 0.5  # In beats
tempo = 80  # In BPM
volume = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
# automatically)
MyMIDI.addTempo(track, time, tempo)


OCTAVE = 3
pitch = note_to_number(note_progression[0], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[1], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[2], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[3], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[4], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
OCTAVE = 2

pitch = note_to_number(note_progression[5], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
OCTAVE = 3

pitch = note_to_number(note_progression[6], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[7], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
duration = 1.5

pitch = note_to_number(note_progression[8], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
duration = 0.5

pitch = note_to_number(note_progression[9], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[10], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[11], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[12], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[13], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[14], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[15], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
duration = 1

pitch = note_to_number(note_progression[16], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
duration = 0.5

pitch = note_to_number(note_progression[17], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[18], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[19], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[20], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[21], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
OCTAVE = 4

pitch = note_to_number(note_progression[22], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
OCTAVE = 3

pitch = note_to_number(note_progression[23], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[24], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[25], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[26], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[27], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
OCTAVE = 2

pitch = note_to_number(note_progression[28], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
OCTAVE = 3 

pitch = note_to_number(note_progression[0], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[1], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[2], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[3], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[4], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
OCTAVE = 2

pitch = note_to_number(note_progression[5], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
OCTAVE = 3

pitch = note_to_number(note_progression[6], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[7], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
duration = 1.5

pitch = note_to_number(note_progression[8], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
duration = 0.5

pitch = note_to_number(note_progression[9], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[10], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[11], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[12], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[13], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
duration = 1

pitch = note_to_number(note_progression[29], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
duration = 0.5

pitch = note_to_number(note_progression[30], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[31], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[32], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[33], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
OCTAVE = 4

pitch = note_to_number(note_progression[34], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
OCTAVE = 3

pitch = note_to_number(note_progression[35], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
OCTAVE = 4 

pitch = note_to_number(note_progression[36], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[37], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[38], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[39], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[40], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[41], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[42], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[43], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
OCTAVE = 3
duration = 1 

pitch = note_to_number(note_progression[44], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
duration = 0.5

pitch = note_to_number(note_progression[45], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[46], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
OCTAVE = 4

pitch = note_to_number(note_progression[47], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[48], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[49], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[50], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[51], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[52], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[53], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
duration = 1

pitch = note_to_number(note_progression[54], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
duration = 0.5
OCTAVE = 3

pitch = note_to_number(note_progression[55], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[56], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[57], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[58], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[59], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[60], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[61], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[62], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[63], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[64], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
OCTAVE = 4

pitch = note_to_number(note_progression[65], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
duration = 0.25
OCTAVE = 3

pitch = note_to_number(note_progression[66], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[67], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
OCTAVE = 4
duration = 0.5

pitch = note_to_number(note_progression[68], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
OCTAVE = 3

pitch = note_to_number(note_progression[69], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[70], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[71], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[72], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[73], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
OCTAVE = 2

pitch = note_to_number(note_progression[74], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
OCTAVE = 3

pitch = note_to_number(note_progression[0], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[1], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[2], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[3], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[4], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
OCTAVE = 2

pitch = note_to_number(note_progression[5], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
OCTAVE = 3

pitch = note_to_number(note_progression[6], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[7], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
duration = 1.5

pitch = note_to_number(note_progression[8], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
duration = 0.5

pitch = note_to_number(note_progression[9], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[10], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[11], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration

pitch = note_to_number(note_progression[12], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
time = time + duration
duration = 2

pitch = note_to_number(note_progression[13], OCTAVE)
MyMIDI.addNote(track, channel, pitch, time, duration, volume)

with open("BhoopaliRaagBandish.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)