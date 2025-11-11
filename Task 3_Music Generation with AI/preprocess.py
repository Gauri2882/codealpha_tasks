from music21 import converter, note, chord
import glob

notes = []

for file in glob.glob("maestro-v3.0.0/**/*.mid", recursive=True):
    midi = converter.parse(file)
    for element in midi.flat.notes:
        if isinstance(element, note.Note):
            notes.append(str(element.pitch))
        elif isinstance(element, chord.Chord):
            notes.append('.'.join(str(n) for n in element.normalOrder))
