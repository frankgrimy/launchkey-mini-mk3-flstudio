# Constants for pads in session mode.
pads_midi_status = 144 # MIDI first byte for every pad.

# Definitions for pads in session mode. They are divided by upper and lower rows.
# The keys are standarized names for pads, and the values are the MIDI data1 values (the second bit in MIDI node specification).

ses_upperpads = {}; ses_lowerpads = {}

for x in range (1,9):
    ses_upperpads["sespad{0}_DATA1".format(x)] = 95+x
    ses_lowerpads["sespad{0}_DATA1".format(x+8)] = 103+x+8

for x in (ses_upperpads, ses_lowerpads):
    locals().update(x)



# Definitions for pads in drum mode. They are divided by quarters.
# The keys are standarized names for pads, and the values are the MIDI data1 values (the second bit in MIDI node specification).

drum_pads = {} # Makes a dictionary with the pads.

# This fills the drum_pads dictionary for all the pads in drum mode.  
for x in range (0,4):
    drum_pads["drumpad{0}_DATA1".format(x+1)] = 40 + x # The first 4 pads are the upper left quarter.
    drum_pads["drumpad{0}_DATA1".format(x+5)] = 48 + x # The next 4 pads are the upper right quarter.
    drum_pads["drumpad{0}_DATA1".format(x+9)] = 36 + x # The next 4 pads are the lower left quarter.
    drum_pads["drumpad{0}_DATA1".format(x+13)] = 44 + x # The last 4 pads are the lower right quarter.