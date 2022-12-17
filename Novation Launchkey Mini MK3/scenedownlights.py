### Colors for Scene-down button
import device
import variables as var
import constants as cons
import colors

def Downbutton():
    if var.SCENE_SEL == "Mixer":
        if var.scmodes.get("MIXER_READYFOR") == "":
            device.midiOutMsg(0xb0, 0, cons.scenedown_DATA1, colors.EMPTYWHITE)
        elif var.scmodes.get("MIXER_READYFOR") == "Stop":
            device.midiOutMsg(0xb2, 0, cons.scenedown_DATA1, colors.STOP)
        elif var.scmodes.get("MIXER_READYFOR") == "Solo":
            device.midiOutMsg(0xb2, 0, cons.scenedown_DATA1, colors.SOLO)
        elif var.scmodes.get("MIXER_READYFOR") == "Mute":
            device.midiOutMsg(0xb2, 0, cons.scenedown_DATA1, colors.MUTE)
            
    elif var.SCENE_SEL == "Playlist":
        if var.scmodes.get("PLAYLIST_READYFOR") == "":
            device.midiOutMsg(0xb0, 0, cons.scenedown_DATA1, colors.EMPTYWHITE)
        elif var.scmodes.get("PLAYLIST_READYFOR") == "Stop":
            device.midiOutMsg(0xb2, 0, cons.scenedown_DATA1, colors.PLSTOP)
        elif var.scmodes.get("PLAYLIST_READYFOR") == "Solo":
            device.midiOutMsg(0xb2, 0, cons.scenedown_DATA1, colors.PLSOLO)
        elif var.scmodes.get("PLAYLIST_READYFOR") == "Mute":
            device.midiOutMsg(0xb2, 0, cons.scenedown_DATA1, colors.PLMUTE)
    
    elif var.SCENE_SEL == "Channel rack":
        if var.scmodes.get("CHANRACK_READYFOR") == "":
            device.midiOutMsg(0xb0, 0, cons.scenedown_DATA1, colors.EMPTYWHITE)
        elif var.scmodes.get("CHANRACK_READYFOR") == "Stop":
            device.midiOutMsg(0xb2, 0, cons.scenedown_DATA1, colors.CRSTOP)
        elif var.scmodes.get("CHANRACK_READYFOR") == "Solo":
            device.midiOutMsg(0xb2, 0, cons.scenedown_DATA1, colors.CRSOLO)
        elif var.scmodes.get("CHANRACK_READYFOR") == "Mute":
            device.midiOutMsg(0xb2, 0, cons.scenedown_DATA1, colors.CRMUTE)
    
    elif var.SCENE_SEL == "Piano roll":
        if var.scmodes.get("PIANOROLL_READYFOR") == "":
            device.midiOutMsg(0xb0, 0, cons.scenedown_DATA1, colors.EMPTYWHITE)
        elif var.scmodes.get("PIANOROLL_READYFOR") == "Stop":
            device.midiOutMsg(0xb2, 0, cons.scenedown_DATA1, colors.PRSTOP)
        elif var.scmodes.get("PIANOROLL_READYFOR") == "Solo":
            device.midiOutMsg(0xb2, 0, cons.scenedown_DATA1, colors.PRSOLO)
        elif var.scmodes.get("PIANOROLL_READYFOR") == "Mute":
            device.midiOutMsg(0xb2, 0, cons.scenedown_DATA1, colors.PRMUTE)
    
    elif var.SCENE_SEL == "Plugin":
        if var.scmodes.get("PLUGIN_READYFOR") == "":
            device.midiOutMsg(0xb0, 0, cons.scenedown_DATA1, colors.EMPTYWHITE)
        elif var.scmodes.get("PLUGIN_READYFOR") == "Stop":
            device.midiOutMsg(0xb2, 0, cons.scenedown_DATA1, colors.PRSTOP)
        elif var.scmodes.get("PLUGIN_READYFOR") == "Solo":
            device.midiOutMsg(0xb2, 0, cons.scenedown_DATA1, colors.PRSOLO)
        elif var.scmodes.get("PLUGIN_READYFOR") == "Mute":
            device.midiOutMsg(0xb2, 0, cons.scenedown_DATA1, colors.PRMUTE)
    
    elif var.SCENE_SEL == "Editor":
        if var.scmodes.get("EDITOR_READYFOR") == "":
            device.midiOutMsg(0xb0, 0, cons.scenedown_DATA1, colors.EMPTYWHITE)
        elif var.scmodes.get("EDITOR_READYFOR") == "Stop":
            device.midiOutMsg(0xb2, 0, cons.scenedown_DATA1, colors.STOP)
        elif var.scmodes.get("EDITOR_READYFOR") == "Solo":
            device.midiOutMsg(0xb2, 0, cons.scenedown_DATA1, colors.SOLO)
        elif var.scmodes.get("EDITOR_READYFOR") == "Mute":
            device.midiOutMsg(0xb2, 0, cons.scenedown_DATA1, colors.MUTE)

    else:
        device.midiOutMsg(0xb0, 0, cons.scenedown_DATA1, 0)