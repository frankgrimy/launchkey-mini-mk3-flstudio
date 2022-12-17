# Constants for "boolean" buttons (which only take MIDI velocities values 0 and 127,
# for OFF and ON respectively).

    #Transport buttons
transport_midi_status = 191     # Status for transport buttons.
transport_midi_id = 176
play_button = 115                 # MIDI note for play button.
record_button = 117               # MIDI note for record button.
annex_STATUS = 176              # Status for shift, scene-up and scene-down buttons.
shift_DATA1 = 108                # MIDI note for shift button.
sceneup_DATA1 = 104              # MIDI note for scene-up button.
scenedown_DATA1 = 105            # MIDI note for scene-down button.
sceneleft_DATA1 = 103
sceneright_DATA1 = 102


# Dedicated pad constants (triggered with Shift + orange pads).
dedpad_STATUS = 144             # It is a MIDI control change parameter.
dedpad_DATA1 = 3
sessionpad_DATA2 = 2
drumpad_DATA2 = 1
custompad_DATA2 = 5

# Dedicated knob constants (triggered with Shift + cyan pads)
dedknob_STATUS = 176
dedknob_DATA1 = 9
devicepad_knob_DATA2 = 2
volumepad_knob_DATA2 = 1
panpad_knob_DATA2 = 3
sendspad_knob_DATA2 = 4
custompad_knob_DATA2 = 6


modes = {
    "Mixer":"MIXER_READYFOR",
    "Playlist": "PLAYLIST_READYFOR",
    "Channel rack": "CHANRACK_READYFOR",
    "Piano roll": "PIANOROLL_READYFOR",
    "Plugin": "PLUGIN_READYFOR",
    'Monitor': 'MONITOR_READYFOR',
    'Editor': 'EDITOR_READYFOR'}
    

startTime = None

monitor = {
    'PAD1': '0',
    'PAD2': '0',
    'PAD3': '0',
    'PAD4': '0',
    'PAD5': '0',
    'PAD6': '0',
    'PAD7': '0',
    'PAD8': '0'
}
