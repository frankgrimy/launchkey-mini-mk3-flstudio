### Behavior and lights for Scene-up button

import constants as cons
import variables as var
import colors
import midi
import ui
import device
from time import time

# ### Scene selector.
# def UpBehavior(midiId, data1, data2):
#     if midiId == midi.MIDI_CONTROLCHANGE:
#         if not var.SHIFT_STATUS:
#             if data1 == cons.sceneup_DATA1:
#                 if data2 > 0:
#                     """
#                     if var.SCENE_SEL == "Mixer":
#                         var.SCENE_SEL = "Playlist"
#                         ui.setHintMsg("Controls in Playlist mode!")
#                     elif var.SCENE_SEL == "Playlist":
#                         var.SCENE_SEL = "Channel rack"
#                         ui.setHintMsg("Controls in Channel rack mode!")
#                     elif var.SCENE_SEL == "Channel rack":
#                         var.SCENE_SEL = "Piano roll"
#                         ui.setHintMsg("Controls in Piano roll mode!")
#                     elif var.SCENE_SEL == "Piano roll":
#                         var.SCENE_SEL = "Editor"
#                         ui.setHintMsg("Controls in Editor mode!")
#                     elif var.SCENE_SEL == "Editor":
#                         var.SCENE_SEL = "Mixer"
#                         ui.setHintMsg("Controls in Mixer mode!")
#                     """
#                     if var.SCENE_SEL == "Mixer":
#                         var.SCENE_SEL = "Channel rack"
#                         ui.setHintMsg("Controls in Channel rack mode!")
#                     elif var.SCENE_SEL == "Channel rack":
#                         var.SCENE_SEL = "Editor"
#                         ui.setHintMsg("Controls in Editor mode!")
#                     elif var.SCENE_SEL == "Editor":
#                         var.SCENE_SEL = "Mixer"
#                         ui.setHintMsg("Controls in Mixer mode!")
#             #if data1:
#                 return 1

### Scene selector.
def UpBehavior(direction):
        if not var.SHIFT_STATUS:
            if not direction:
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
            elif direction:
                if var.SCENE_SEL == "Mixer":
                    var.SCENE_SEL = "Editor"
                    ui.setHintMsg("Controls in Editor mode!")
                elif var.SCENE_SEL == "Channel rack":
                    var.SCENE_SEL = "Mixer"
                    ui.setHintMsg("Controls in Mixer mode!")
                elif var.SCENE_SEL == "Editor":
                    var.SCENE_SEL = "Channel rack"
                    ui.setHintMsg("Controls in Channel rack mode!")
                
            #if data1:
            return 1

### Colors on push.
def UpColorsPush():
    if not var.SHIFT_STATUS:
        if var.isPushed:
        # if midiId == midi.MIDI_CONTROLCHANGE:
        #     if data1 == cons.sceneup_DATA1:
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
def UpPushed(status):
    if status:
            var.SCENEUP_STATUS=1
    elif not status:
        var.SCENEUP_STATUS=0


class SceneUpColor(): # Controls up button colors on idle.
    def OnIdle(self):
        UpColorsIdle()

UpColor = SceneUpColor()

# class SceneUpMidi(): # Controls up button behavior at/after push.
#     def OnMidiMsg(self, midiId, data1, data2):
#         nowtime = None
#         while data2:
#             nowtime = time()
#             if nowtime - var.currentTime > 1:
#                 print("1 second press")
#                 break
#             else:
#                 print("pressing")
#                 continue

#     # def OnMidiMsg(midiId, data1, data2):
#     #     UpBehavior(midiId, data1, data2)
#     #     UpPushed(midiId, data1, data2)
#     #     UpColorsPush(midiId, data1)


# class SceneUpMidi(): # Controls up button behavior at/after push.
#     def OnIdle(midiId, data1, data2):
#         if data1 == cons.sceneup_DATA1:
#             internalMidiId = midiId
#             internalData1 = data1
#             if data2:
#                 internalData2 = data2
#                 var.pushTime = time()
#                 # print("Push: ", pushTime, "Release: ", releaseTime)
#             elif not data2:
#                 var.releaseTime = time()
#                 internalData2 = data2
#                 # print("Push: ", pushTime, "Release: ", releaseTime)
#             if var.releaseTime - var.pushTime > 0.5 and var.pushTime != 0 and var.releaseTime != 0:
#                 # print("Long press detected")
#                 var.pushTime = 0
#                 var.releaseTime = 0
#             elif var.releaseTime - var.pushTime <= 0.5 and var.pushTime != 0 and var.releaseTime != 0:
#                 print("Short press detected")
#                 print(internalData1, internalData2)
#                 UpBehavior(internalMidiId, internalData1, internalData2)
#                 UpPushed(internalMidiId, internalData1, internalData2)
#                 UpColorsPush(internalMidiId, internalData1)
#                 var.pushTime = 0
#                 var.releaseTime = 0
#             else:
#                 pass


#UpMidi = SceneUpMidi()

# def SceneUpMidi(event, timeDelta):
#     if event.midiId == midi.MIDI_CONTROLCHANGE:
#         if event.data1 == cons.sceneup_DATA1:
#             if event.data2:
#                 var.pushTime = time()
#                 UpPushed(1)
#                 UpColorsPush()
#             elif not event.data2:
#                 var.releaseTime = time()
#                 UpPushed(0)
#                 if var.releaseTime - var.pushTime < timeDelta and var.pushTime != 0 and var.releaseTime != 0:
#                     var.pushTime = 0
#                     var.releaseTime = 0
#                     UpBehavior(0)
#                 elif var.releaseTime - var.pushTime >= timeDelta and var.pushTime != 0 and var.releaseTime != 0:
#                     UpBehavior(1)
#                     #UpPushed(event.midiId, event.data1, event.data2)
#                     var.pushTime = 0
#                     var.releaseTime = 0
#                 else:
#                     pass

def SceneUpMidi(event):
    if event.midiId == midi.MIDI_CONTROLCHANGE:
        if event.data1 == cons.sceneup_DATA1:
            if event.data2:
                var.isPushed = 1
                UpPushed(1)  
                if not var.pushTime:
                    var.pushTime = time() # Set pushTime to the time the button was pushed.
            else:    
                #var.pushTime = 0 # Reset pushTime to 0.
                UpPushed(0)
                var.isPushed = 0
    
    


