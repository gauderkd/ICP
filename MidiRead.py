import midi  # Uses python-midi module: https://github.com/vishnubob/python-midi
# To install in python3, run:
# pip install git+https://github.com/vishnubob/python-midi@feature/python3
from ICP import *

# This file will loop through the first track of a midi file and allow processing on each note.
# Midi files often have multiple tracks layered together. This is especially important to perceive chords.
# So we will need to write a program that parses through all the tracks and combines them.
# Maybe retains that "2d" verticality and chords

pattern = midi.read_midifile('Prelude4.mid')
midiFile = pattern[1][1:-1]  # Extract all midi events, minus meta events
meta = pattern[1][0]
nEvents = len(midiFile)


progression = 0
for i, event in enumerate(midiFile):
    type = event.name  # note on or note off
    pitch = event.get_pitch()  #pitch
    velocity = event.get_velocity()  #velocity
    tick = event.tick  # timing?
    progression += tick
    note = midiToNote(pitch)

    if type == 'Note On':
        next_event = midiFile[i+1]
        duration = next_event.tick + tick
        print(progression, note, duration)