# Channel rack lower pads functions
import colors
import pads
import variables as var
import channels
import device
import ui
import colPalette as col

def LowerLights():
    chan = channels.selectedChannel()
    if var.SCENE_SEL == "Channel rack" and not var.scmodes.get("CHANRACK_READYFOR") == "Stop":
        for x in pads.ses_lowerpads.values():
            if chan+x-112 < channels.channelCount():
                if channels.isChannelSolo(chan+x-112):
                    device.midiOutMsg(0x92, 0, x, colors.CRSOLO)
                elif channels.isChannelMuted(chan+x-112):
                    device.midiOutMsg(0x92, 0, x, colors.CRMUTE)
                elif var.scmodes.get("CHANRACK_READYFOR") == "Solo" and not channels.isChannelSolo(chan+x-112):
                    device.midiOutMsg(0x90, 0, x, colors.GREEN1)
                elif var.scmodes.get("CHANRACK_READYFOR") == "Mute" and not channels.isChannelSolo(chan+x-112):
                    device.midiOutMsg(0x90, 0, x, colors.GREEN1)
                elif var.scmodes.get("CHANRACK_READYFOR") == "":
                    device.midiOutMsg(0x90, 0, x, col.channelColorNumber(chan+x-112)) # Colored pads according to the channel color.
            else: device.midiOutMsg(0x90, 0, x, 0)

def LowerPadsControls(data1, data2, CRMODE):
    chan = channels.selectedChannel()
    for x,y in pads.ses_lowerpads.items():
        if data1 == pads.ses_lowerpads[x] and data2:
            if CRMODE == "Solo":
                if chan+y-112 < channels.channelCount():
                    channels.soloChannel(chan+y-112)
                    if channels.isChannelSolo(chan+y-112):
                        ui.setHintMsg("Channel " + str(chan+y-112) + " SOLOED! (" + channels.getChannelName(chan+y-112)+ ")")
                    else:
                        ui.setHintMsg("Channel " + str(chan+y-112) + " UN-SOLOED! (" + channels.getChannelName(chan+y-112)+ ")")
                else:
                    ui.setHintMsg("Can't solo non-existing channels!")
                
            elif CRMODE == "Mute":
                if chan+y-112 < channels.channelCount():
                    channels.muteChannel(chan+y-112)
                    if channels.isChannelMuted(chan+y-112):
                        ui.setHintMsg("Channel " + str(chan+y-112) + " MUTED! (" + channels.getChannelName(chan+y-112)+ ")")
                    else:
                        ui.setHintMsg("Channel " + str(chan+y-112) + " UNMUTED! (" + channels.getChannelName(chan+y-112)+ ")")
                else:
                    ui.setHintMsg("Can't mute non-existing channels!")