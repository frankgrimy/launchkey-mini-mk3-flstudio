import device

PORT=device.getPortNumber()     # Save controller's assigned port as the PORT variable. May be useful.
#AUTO_SWITCH_TO_CONTROLLED_PARAMETER = True

"""
Remember that MIDI info require three bytes (which is the same as three hexadecimal pairs, e.g. AA BB CC;
or three base ten numbers, e.g. 170 187 204) in order to transmit a message understandable by a
MIDI host (in this case, FL Studio).
The first byte communicates the MIDI status (STATUS), the kind of message sent (note on/off, pad on/off, knob rotation, etc).
The second one indicates aditional MIDI info 1 (DATA1). The controller's pads, knobs and buttons are identified
by this method, since every one of these are mapped to an unique STATUS-DATA1 bytes combination.
You can find those mappings in Novation Launchkey MK3 Programmer's reference manual, or using a
MIDI monitoring tool (like Pocket MIDI).
The third byte indicates the MIDI info 2 (DATA2), a value between 0 and 127, that can be interpreted as the status
of the note, pad, knob or button triggered at a time. On keystrokes and pads, it indicates the MIDI velocity,
for knobs it indicates the degree of rotation, and for buttons it indicates if it's held down (value 127),
or if it's released (value 0).

By the way, most of the functions handled by FL Studio need decimal values in order to operate correctly,
but you can use Python's hexadecimal notation to represent those values.
For example, if an operation here requires the decimal number 170, this one can be expressed as the
hexadecimal value 0xAA. This comes in handy since the Programming Manual provided by Novation for their
Launchkey MK3 device series show those values in both ways, but sometimes it preffers one above the other.

On other side, fortunately, Launchkey Mini MK3 makes almost no use of SysEx messages (just when the Host device queries
device info, when it triggers the original boot animation [or even a custom one 🌈], or when setting the
status for special buttons [as Arp or Fixed Chord]).

The next sections define specific bytes that might act as those AAs, BBs or CCs, for each pad, knob or button.

"""

SHIFT_STATUS = False
FOCUS_STATUS = 0
MIXER_READYFOR = ""
PLAYLIST_READYFOR = ""
CHANRACK_READYFOR = ""
PIANOROLL_READYFOR = ""
WAITFORINPUT = ""
KNOBSTATUS = ""
PADSTATUS = ""
SCENE_SEL = "Mixer"
#SCENE_SEL = "Playlist"
SCENEUP_STATUS=""


crRectPos = 0


#sespad1_DATA1 = 96

scmodes = {"MIXER_READYFOR":"","PLAYLIST_READYFOR":"", "CHANRACK_READYFOR":"", "PIANOROLL_READYFOR":"", "EDITOR_READYFOR":"", 'MONITOR_READYFOR':''}

# For shortcut lights in Editor mode.
shortpress = ""
shortdata = ""


currentTime = None


repeatqueue = {}
repeatok = {}

