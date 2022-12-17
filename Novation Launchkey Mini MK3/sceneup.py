### Behavior and lights for Scene-up button

import constants as cons
import variables as var
import colors
import midi
import ui
import device

### Scene selector.
def UpBehavior(midiId, data1, data2):
    if midiId == midi.MIDI_CONTROLCHANGE:
        if not var.SHIFT_STATUS:
            if data1 == cons.sceneup_DATA1:
                if data2 > 0:
                    """
                    if var.SCENE_SEL == "Mixer":
                        var.SCENE_SEL = "Playlist"
                        ui.setHintMsg("Controls in Playlist mode!")
                    elif var.SCENE_SEL == "Playlist":
                        var.SCENE_SEL = "Channel rack"
                        ui.setHintMsg("Controls in Channel rack mode!")
                    elif var.SCENE_SEL == "Channel rack":
                        var.SCENE_SEL = "Piano roll"
                        ui.setHintMsg("Controls in Piano roll mode!")
                    elif var.SCENE_SEL == "Piano roll":
                        var.SCENE_SEL = "Editor"
                        ui.setHintMsg("Controls in Editor mode!")
                    elif var.SCENE_SEL == "Editor":
                        var.SCENE_SEL = "Mixer"
                        ui.setHintMsg("Controls in Mixer mode!")
                    """
                    if var.SCENE_SEL == "Mixer":
                        var.SCENE_SEL = "Channel rack"
                        ui.setHintMsg("Controls in Channel rack mode!")
                    elif var.SCENE_SEL == "Channel rack":
                        var.SCENE_SEL = "Editor"
                        ui.setHintMsg("Controls in Editor mode!")
                    elif var.SCENE_SEL == "Editor":
                        var.SCENE_SEL = "Mixer"
                        ui.setHintMsg("Controls in Mixer mode!")
            #if data1:
                return 1

### Colors on push.
def UpColorsPush(midiId, data1):
    if not var.SHIFT_STATUS:
        if midiId == midi.MIDI_CONTROLCHANGE:
            if data1 == cons.sceneup_DATA1:
                if var.SCENEUP_STATUS:
                    if var.SCENE_SEL == "Mixer":
                        device.midiOutMsg(0xb0, 0, 0x68, colors.MIXER)
                    elif var.SCENE_SEL == "Playlist":
                        device.midiOutMsg(0xb0, 0, 0x68, colors.PLAYLIST)
                    elif var.SCENE_SEL == "Channel rack":
                        device.midiOutMsg(0xb0, 0, 0x68, colors.CHAN_RACK)
                    elif var.SCENE_SEL == "Piano roll":
                        device.midiOutMsg(0xb0, 0, 0x68, colors.PIANO_ROLL)
                    elif var.SCENE_SEL == "Editor":
                        device.midiOutMsg(0xb0, 0, 0x68, colors.EDITOR)

### Colors on idle state.
def UpColorsIdle():
    if not var.SHIFT_STATUS:
        if not var.SCENEUP_STATUS:
            if var.SCENE_SEL == "Mixer":
                device.midiOutMsg(0xb2, 0, cons.sceneup_DATA1, colors.MIXER)
            if var.SCENE_SEL == "Playlist":
                device.midiOutMsg(0xb2, 0, cons.sceneup_DATA1, colors.PLAYLIST)
            if var.SCENE_SEL == "Channel rack":
                device.midiOutMsg(0xb2, 0, cons.sceneup_DATA1, colors.CHAN_RACK)
            if var.SCENE_SEL == "Piano roll":
                device.midiOutMsg(0xb2, 0, cons.sceneup_DATA1, colors.PIANO_ROLL)
            if var.SCENE_SEL == "Editor":
                device.midiOutMsg(0xb2, 0, cons.sceneup_DATA1, colors.EDITOR)

### Push-release state.
def UpPushed(midiId, data1, data2):
    if midiId == midi.MIDI_CONTROLCHANGE:
        if data1 == cons.sceneup_DATA1:
            if data2:
                var.SCENEUP_STATUS=1
            else:
                var.SCENEUP_STATUS=0