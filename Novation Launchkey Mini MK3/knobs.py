# Constants for knobs (Novation calls them "pots" lmao). They take "MIDI velos" in the range 0-127.
knobs_midi_status = 191         # The same as transport_midi_status.
knobs = {}                      # This creates a dictionary containing knob mapping, in the order shown in the manual, in decimal format.
for x in range (1,9):
    knobs["knob{0}_DATA1".format(x)] = 20+x
locals().update(knobs)          # This creates variables for knob notes by unpacking the previous dictionary.