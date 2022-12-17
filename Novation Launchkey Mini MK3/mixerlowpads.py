### Colors and UI messages for lower pads in Mixer mode
import variables as var
import pads
import mixer
import device
import colors
import ui

def LowerLights():
    if var.SCENE_SEL == "Mixer":
            for x in pads.ses_lowerpads.values():
                if mixer.trackNumber()+x-112 < mixer.trackCount()-1:
                    
                    if mixer.isTrackArmed(mixer.trackNumber()+x-112):
                        device.midiOutMsg(0x92, 0, x, colors.STOP)
                    elif mixer.isTrackSolo(mixer.trackNumber()+x-112):
                        device.midiOutMsg(0x92, 0, x, colors.SOLO)
                    elif mixer.isTrackMuted(mixer.trackNumber()+x-112):
                        device.midiOutMsg(0x92, 0, x, colors.MUTE)

                    elif var.MIXER_READYFOR == "Solo" and not mixer.isTrackSolo(mixer.trackNumber()+x-112):
                        device.midiOutMsg(0x90, 0, x, colors.GREEN1)
                    elif var.MIXER_READYFOR == "Mute" and not mixer.isTrackSolo(mixer.trackNumber()+x-112):
                        device.midiOutMsg(0x90, 0, x, colors.GREEN1)
                    else:
                        device.midiOutMsg(0x90, 0, x, colors.GREEN1)
                
                else: device.midiOutMsg(0x90, 0, x, 0)

class LowPads:
    def __init__(self, DATA1, DATA2, MIXERMODE):
        self.DATA1 = DATA1
        self.DATA2 = DATA2
        self.MIXERMODE = MIXERMODE
    
        
    def LowerPadsControls(self):
        for x,y in pads.ses_lowerpads.items():
            if self.DATA1 == pads.ses_lowerpads[x]:
                if self.DATA2:
                    if self.MIXERMODE == "Stop":
                        if mixer.trackNumber()+y-112 < mixer.trackCount()-1:
                            mixer.armTrack(mixer.trackNumber()+y-112)
                            if mixer.isTrackArmed(mixer.trackNumber()+y-112):
                                ui.setHintMsg("Insert " + str(mixer.trackNumber()+y-112) + " ARMED for recording! (" + mixer.getTrackName(mixer.trackNumber()+y-112)+ ")")
                            else:
                                ui.setHintMsg("Insert " + str(mixer.trackNumber()+y-112) + " UNARMED for recording! (" + mixer.getTrackName(mixer.trackNumber()+y-112)+ ")")
                        else:
                            if mixer.trackNumber()+y-112 == mixer.trackCount()-1:
                                ui.setHintMsg("Can't arm the Current insert!")
                            else:
                                ui.setHintMsg("Can't arm non-existing inserts!")

                    elif self.MIXERMODE == "Solo":
                        if mixer.trackNumber()+y-112 < mixer.trackCount()-1:
                            mixer.soloTrack(mixer.trackNumber()+y-112)
                            if mixer.isTrackSolo(mixer.trackNumber()+y-112):
                                ui.setHintMsg("Insert " + str(mixer.trackNumber()+y-112) + " SOLOED! (" + mixer.getTrackName(mixer.trackNumber()+y-112)+ ")")
                            else:
                                ui.setHintMsg("Insert " + str(mixer.trackNumber()+y-112) + " UN-SOLOED! (" + mixer.getTrackName(mixer.trackNumber()+y-112)+ ")")
                        else:
                            if mixer.trackNumber()+y-112 == mixer.trackCount()-1:
                                ui.setHintMsg("Can't solo the Current insert!")
                            else:
                                ui.setHintMsg("Can't solo non-existing inserts!")
                    
                    elif self.MIXERMODE == "Mute":
                        if mixer.trackNumber()+y-112 < mixer.trackCount()-1:
                            if mixer.isTrackMuted(mixer.trackNumber()+y-112):
                                ui.setHintMsg("Insert " + str(mixer.trackNumber()+y-112) + " UNMUTED! (" + mixer.getTrackName(mixer.trackNumber()+y-112)+ ")")
                            else:
                                ui.setHintMsg("Insert " + str(mixer.trackNumber()+y-112) + " MUTED! (" + mixer.getTrackName(mixer.trackNumber()+y-112)+ ")")
                            mixer.muteTrack(mixer.trackNumber()+y-112)
                        else:
                            if mixer.trackNumber()+y-112 == mixer.trackCount()-1:
                                ui.setHintMsg("Can't mute the Current insert!")
                            else:
                                ui.setHintMsg("Can't mute non-existing inserts!")
                        

