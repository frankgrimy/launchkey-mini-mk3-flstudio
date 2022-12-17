# Constants for pads in session mode.
pads_midi_status = 144

ses_upperpads = {}                 # This creates a dictionary for the upper pads, as shown in the manual. I'll count from left to right.
for y in range (1,9):
    ses_upperpads["sespad{0}_DATA1".format(y)] = 95+y
locals().update(ses_upperpads)     # Unpacks upper pads from the dictionary.

ses_lowerpads = {}                 # This creates a dictionary for the lower pads, as shown in the manual. I'll count from left to right.
for z in range (9,17):
    ses_lowerpads["sespad{0}_DATA1".format(z)] = 103+z
locals().update(ses_lowerpads)     # Unpacks lower pads from the dictionary.

# Constants for pads in drum mode. They are divided by quarters
drum_upperpads = {
    "drumpad1_DATA1":40,
    "drumpad2_DATA1":41,
    "drumpad3_DATA1":42,
    "drumpad4_DATA1":43,
    "drumpad5_DATA1":48,
    "drumpad6_DATA1":49,
    "drumpad7_DATA1":50,
    "drumpad8_DATA1":51
}
locals().update(drum_upperpads)

drum_lowerpads = {
    "drumpad9_DATA1":36,
    "drumpad10_DATA1":37,
    "drumpad11_DATA1":38,
    "drumpad12_DATA1":39,
    "drumpad13_DATA1":44,
    "drumpad14_DATA1":45,
    "drumpad15_DATA1":46,
    "drumpad16_DATA1":47    
}
locals().update(drum_lowerpads)