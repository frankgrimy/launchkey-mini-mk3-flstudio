### Upper pads lights
import ui
import device
import pads
import colors
import variables as var
import transport

def Padlights():
    if ui.isMetronomeEnabled():     # Metronome pad lighting at start. Useful if your default template starts with metronome ON.
            device.midiOutMsg(0x92,0,0x61,0x09)
    else:
        device.midiOutMsg(0x90,0,0x61,70)

    if transport.getLoopMode():     # Looping mode pad lighting at start. Useful if your default template starts at Pattern mode. 
        device.midiOutMsg(0x92,0,pads.sespad1_DATA1,0x15)
    else:
        device.midiOutMsg(0x92,0,pads.sespad1_DATA1,0x09)

    if ui.isStartOnInputEnabled():
        device.midiOutMsg(0x90,0,0x62,0x09)
    else:
        device.midiOutMsg(0x90,0,0x62,70)

    if ui.isPrecountEnabled():
        device.midiOutMsg(0x90,0,0x63,0x09)
    else:
        device.midiOutMsg(0x90,0,0x63,70)

    if ui.getVisible(2):
        device.midiOutMsg(0x92,0,pads.sespad5_DATA1,colors.ORANGE2)
    else:
        device.midiOutMsg(0x90,0,pads.sespad5_DATA1,70)

    if ui.getVisible(1):
        device.midiOutMsg(0x92,0,pads.sespad6_DATA1,colors.ORANGE2)
    else:
        device.midiOutMsg(0x90,0,pads.sespad6_DATA1,70)

    if not (var.SCENE_SEL== "Channel rack" and var.scmodes.get("CHANRACK_READYFOR") == "Stop"):
        if ui.getVisible(3):
            device.midiOutMsg(0x92,0,pads.sespad7_DATA1,colors.ORANGE2)
        else:
            device.midiOutMsg(0x90,0,pads.sespad7_DATA1,70)
    else:
        device.midiOutMsg(0x92,0,pads.sespad7_DATA1,colors.crRectSel)


    if not (var.SCENE_SEL== "Channel rack" and var.scmodes.get("CHANRACK_READYFOR") == "Stop"):
        if ui.getVisible(0):
            device.midiOutMsg(0x92,0,pads.sespad8_DATA1,colors.ORANGE2)
        else:
            device.midiOutMsg(0x90,0,pads.sespad8_DATA1,70)
    else:
        device.midiOutMsg(0x92,0,pads.sespad8_DATA1,colors.crRectSel)


    if transport.isPlaying():
        device.midiOutMsg(0xb2,0, 0x73, 0x03)
    else:
        device.midiOutMsg(0xb1,0, 0x73, 0x7f)

    if transport.isRecording():
        device.midiOutMsg(0xb2, 0, 0x75, 0x03)
    else:
        device.midiOutMsg(0xbf, 0, 0x75, 0x00)