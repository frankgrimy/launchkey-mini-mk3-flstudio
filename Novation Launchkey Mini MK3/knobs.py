# Constants for knobs (Novation calls them "pots"). They take "MIDI velos" in the range 0-127.
knobs_midi_status = 191         # MIDI first byte for every knob.

knobs = {} # Makes a dictionary with the knobs.
for x in range (21,29):
    knobs["knob{0}_DATA1".format(x-20)] = x