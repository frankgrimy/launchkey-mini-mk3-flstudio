### Step sequencer lights and behavior.
import midi
import device
import ui
import channels
import colors
#import sys
import variables as var
import pads
#import midi

class HorPos:
    #def __init__(self, SCENE_SEL, channumber, DATA1, DATA2, *drumpad_map):
    def __init__(self, DATA1, DATA2, distance):
        #self.SCENE_SEL = SCENE_SEL
        #self.channumber = channumber
        self.DATA1 = DATA1
        self.DATA2 = DATA2
        self.distance = distance
        #self.drumpad_map = drumpad_map
    

    def Move(self):
        POS = 0
        if self.DATA1 and self.DATA2>0:
            POS = POS + self.distance
            return (POS)

def Sequencer(midiID, data1, data2):        ### It's run with MIDI events
    crRight = HorPos(data1, data2, 8)
    crLeft = HorPos(data1, data2, -8)

    if midiID == midi.MIDI_NOTEON or midiID == midi.MIDI_CONTROLCHANGE:
        if var.SCENE_SEL == "Channel rack" and var.scmodes.get("CHANRACK_READYFOR") == "Stop":
            if data1 == pads.sespad8_DATA1 and data2:
                var.crRectPos = var.crRectPos + int(crRight.Move() or 0)
                ui.setHintMsg("Moving the frame to the right!")
            
            elif data1 == pads.sespad7_DATA1 and data2:
                    if var.crRectPos >=8:
                        var.crRectPos = var.crRectPos + int(crLeft.Move() or 0)
                        ui.setHintMsg("Moving the frame to the left!")
                    else:
                        ui.setHintMsg("Can't move to the left any further!")
            
            ui.crDisplayRect(var.crRectPos, channels.selectedChannel(), 8, 1, 2500)
        
        for x,y in pads.ses_lowerpads.items():
            if var.SCENE_SEL == "Channel rack" and var.scmodes.get("CHANRACK_READYFOR") == "Stop":
                if data1 == pads.ses_lowerpads[x] and data2:
                    if channels.getGridBit(channels.selectedChannel(), var.crRectPos+y-112):
                        channels.setGridBit(channels.selectedChannel(), var.crRectPos+y-112, 0)
                    else:
                        channels.setGridBit(channels.selectedChannel(), var.crRectPos+y-112, 1)


def SeqLights():        ### It's run On idle
    if var.SCENE_SEL == "Channel rack":
        if var.scmodes.get("CHANRACK_READYFOR") == "Stop":
            for x,y in pads.ses_lowerpads.items():
                if channels.getGridBit(channels.selectedChannel(), var.crRectPos+y-112):
                    device.midiOutMsg(0x92, 0, pads.ses_lowerpads[x], colors.CRSTOP)
                else:
                    device.midiOutMsg(0x90, 0, pads.ses_lowerpads[x], colors.EMPTYWHITE)