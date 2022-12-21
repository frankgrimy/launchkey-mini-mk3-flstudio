### Editor + Monitor config
import midi
import pads
import variables as var
import transport
from ui import setHintMsg
from general import undo, undoUp
from device import midiOutMsg, midiOutSysex as sysex
import colors
from time import time, time_ns
from mxr import levelmon
from mixer import trackNumber as number, getTrackPeaks as peaks, isTrackMuted as muted, trackCount as count


def Shortcuts(midiId, data1, data2): ### This is a fast implementation of the editor window.
    if var.SCENE_SEL == "Editor":
        if not var.scmodes.get("EDITOR_READYFOR"):
            if midiId == midi.MIDI_NOTEON:
                if data2:
                    #global shortpress,shortdata
                    var.shortpress = True
                    var.shortdata = data1 # data1 is the pad number
                    if data1 == pads.sespad9_DATA1:
                        transport.globalTransport(midi.FPT_Menu, 1)
                        setHintMsg("Menu for focused window")
                    
                    elif data1 == pads.sespad10_DATA1:
                        transport.globalTransport(midi.FPT_Cut, 1)
                        setHintMsg("Cut to clipboard")
                    
                    elif data1 == pads.sespad11_DATA1:
                        transport.globalTransport(midi.FPT_Copy, 1)
                        setHintMsg("Copy to clipboard")
                    
                    elif data1 == pads.sespad12_DATA1:
                        transport.globalTransport(midi.FPT_Paste, 1)
                        setHintMsg("Paste from clipboard")
                    
                    elif data1 == pads.sespad13_DATA1:
                        undo()
                        #transport.globalTransport(midi.FPT_Undo, 1)
                        #setHintMsg("Undo/redo")
                        
                    elif data1 == pads.sespad14_DATA1:
                        undoUp()
                        #transport.globalTransport(midi.FPT_UndoUp, 1)
                        #setHintMsg("Keep undoing")
                    elif data1 == pads.sespad15_DATA1 and data2 > 0:
                        transport.globalTransport(midi.FPT_Snap, 1)
                        setHintMsg("Snap toggled")
                    elif data1 == pads.sespad16_DATA1:
                        transport.globalTransport(midi.FPT_AddMarker, 1)
                        setHintMsg("Marker added at playback position")
                else:
                    var.shortpress = False
        #elif var.scmodes.get("EDITOR_READYFOR") == "Stop":
        #    print("a")


def ShortLights(): 
    if var.SCENE_SEL == "Editor": 
        if not var.scmodes.get("EDITOR_READYFOR"):
            if var.shortpress:
                if var.shortdata == pads.sespad9_DATA1:
                    midiOutMsg(0x90, 0, var.shortdata, colors.MENU1)

                elif var.shortdata == pads.sespad10_DATA1 or var.shortdata == pads.sespad11_DATA1 or var.shortdata == pads.sespad12_DATA1:
                    midiOutMsg(0x90, 0, var.shortdata, colors.CCP1)
                
                elif var.shortdata == pads.sespad13_DATA1 or var.shortdata == pads.sespad14_DATA1:
                    midiOutMsg(0x90, 0, var.shortdata, colors.UNRE1)
                elif var.shortdata == pads.sespad15_DATA1:
                    midiOutMsg(0x90, 0, var.shortdata, colors.SNAP1)
                elif var.shortdata == pads.sespad16_DATA1:
                    midiOutMsg(0x90, 0, var.shortdata, colors.MARKER1)

            else:
                midiOutMsg(0x92, 0, pads.sespad9_DATA1, colors.MENU)
                midiOutMsg(0x92, 0, pads.sespad10_DATA1, colors.CCP)
                midiOutMsg(0x92, 0, pads.sespad11_DATA1, colors.CCP)
                midiOutMsg(0x92, 0, pads.sespad12_DATA1, colors.CCP)
                midiOutMsg(0x92, 0, pads.sespad13_DATA1, colors.UNRE)
                midiOutMsg(0x92, 0, pads.sespad14_DATA1, colors.UNRE)
                midiOutMsg(0x92, 0, pads.sespad15_DATA1, colors.SNAP)
                midiOutMsg(0x92, 0, pads.sespad16_DATA1, colors.MARKER)
        elif var.scmodes.get("EDITOR_READYFOR") not in ("Stop","Solo"):
            midiOutMsg(0x92, 0, pads.sespad9_DATA1, 0)
            midiOutMsg(0x92, 0, pads.sespad10_DATA1, 0)
            midiOutMsg(0x92, 0, pads.sespad11_DATA1, 0)
            midiOutMsg(0x92, 0, pads.sespad12_DATA1, 0)
            midiOutMsg(0x92, 0, pads.sespad13_DATA1, 0)
            midiOutMsg(0x92, 0, pads.sespad14_DATA1, 0)

#def MonitorLights(level):
#    if var.SCENE_SEL == "Editor" and var.scmodes.get("EDITOR_READYFOR") == "Stop":
#        if level 

def peakMonitor():
    if var.SCENE_SEL == "Editor":
        if var.scmodes.get("EDITOR_READYFOR") == "Stop":
            if not muted(number()):
                peak = peaks(number(),2)
                #print(peak)

                if peak < 0.02:
                    midiOutMsg(0x90, 0, pads.sespad9_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad10_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad11_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad12_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad13_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad14_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad15_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad16_DATA1, 0x0)
                elif peak < 0.15:
                    midiOutMsg(0x90, 0, pads.sespad9_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad10_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad11_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad12_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad13_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad14_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad15_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad16_DATA1, 0x0)
                elif peak < 0.25:
                    midiOutMsg(0x90, 0, pads.sespad9_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad10_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad11_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad12_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad13_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad14_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad15_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad16_DATA1, 0x0)
                elif peak < 0.45:
                    midiOutMsg(0x90, 0, pads.sespad9_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad10_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad11_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad12_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad13_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad14_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad15_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad16_DATA1, 0x0)
                elif peak < 0.55:
                    midiOutMsg(0x90, 0, pads.sespad9_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad10_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad11_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad12_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad13_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad14_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad15_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad16_DATA1, 0x0)
                elif peak < 0.80:
                    midiOutMsg(0x90, 0, pads.sespad9_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad10_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad11_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad12_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad13_DATA1, colors.LEVMID)
                    midiOutMsg(0x90, 0, pads.sespad14_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad15_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad16_DATA1, 0x0)
                elif peak < 0.85:
                    midiOutMsg(0x90, 0, pads.sespad9_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad10_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad11_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad12_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad13_DATA1, colors.LEVMID)
                    midiOutMsg(0x90, 0, pads.sespad14_DATA1, colors.LEVMID)
                    midiOutMsg(0x90, 0, pads.sespad15_DATA1, 0x0)
                    midiOutMsg(0x90, 0, pads.sespad16_DATA1, 0x0)
                elif peak < 0.90:
                    midiOutMsg(0x90, 0, pads.sespad9_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad10_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad11_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad12_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad13_DATA1, colors.LEVMID)
                    midiOutMsg(0x90, 0, pads.sespad14_DATA1, colors.LEVMID)
                    midiOutMsg(0x90, 0, pads.sespad15_DATA1, colors.LEVHI)
                    midiOutMsg(0x90, 0, pads.sespad16_DATA1, 0x0)
                elif peak < 1:
                    midiOutMsg(0x90, 0, pads.sespad9_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad10_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad11_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad12_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad13_DATA1, colors.LEVMID)
                    midiOutMsg(0x90, 0, pads.sespad14_DATA1, colors.LEVMID)
                    midiOutMsg(0x90, 0, pads.sespad15_DATA1, colors.LEVHI)
                    midiOutMsg(0x90, 0, pads.sespad16_DATA1, colors.LEVHI)
                elif peak >1:
                    midiOutMsg(0x90, 0, pads.sespad9_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad10_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad11_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad12_DATA1, colors.LEVLOW)
                    midiOutMsg(0x90, 0, pads.sespad13_DATA1, colors.LEVMID)
                    midiOutMsg(0x90, 0, pads.sespad14_DATA1, colors.LEVMID)
                    midiOutMsg(0x90, 0, pads.sespad15_DATA1, colors.LEVHI)
                    midiOutMsg(0x90, 0, pads.sespad16_DATA1, colors.LEVCLIP)
            else:
                midiOutMsg(0x90, 0, pads.sespad9_DATA1, 0x0)
                midiOutMsg(0x90, 0, pads.sespad10_DATA1, 0x0)
                midiOutMsg(0x90, 0, pads.sespad11_DATA1, 0x0)
                midiOutMsg(0x90, 0, pads.sespad12_DATA1, 0x0)
                midiOutMsg(0x90, 0, pads.sespad13_DATA1, 0x0)
                midiOutMsg(0x90, 0, pads.sespad14_DATA1, 0x0)
                midiOutMsg(0x90, 0, pads.sespad15_DATA1, 0x0)
                midiOutMsg(0x90, 0, pads.sespad16_DATA1, 0x0)


"""def velocityCurves(midiId, data1, data2): 
    if var.SCENE_SEL == "Editor" and var.scmodes.get("EDITOR_READYFOR") == "Solo":
        if midiId == 0x90:
            if data1 == pads.sespad9_DATA1 and data2 > 0:
                if var.keysVelo == 1:
                    var.keysVelo = 2
                    midiOutMsg(0x90, 0, pads.sespad9_DATA1, colors.LEVHI)
                    sysex()
                elif var.keysVelo == 2:
                    var.keysVelo = 3
                    midiOutMsg(0x90, 0, pads.sespad9_DATA1, colors.LEVCLIP)
                elif var.keysVelo == 3:
                    var.keysVelo = 0
                    midiOutMsg(0x90, 0, pads.sespad9_DATA1, colors.LEVLOW)
                elif var.keysVelo == 0:
                    var.keysVelo = 1
                    midiOutMsg(0x90, 0, pads.sespad9_DATA1, colors.LEVMID)
            elif data1 == pads.sespad10_DATA1 and data2 > 0:
                if var.padsVelo == 1:
                    var.padsVelo = 2
                    midiOutMsg(0x90, 0, pads.sespad10_DATA1, colors.LEVHI)
                elif var.padsVelo == 2:
                    var.padsVelo = 3
                    midiOutMsg(0x90, 0, pads.sespad10_DATA1, colors.LEVCLIP)
                elif var.padsVelo == 3:
                    var.padsVelo = 0
                    midiOutMsg(0x90, 0, pads.sespad10_DATA1, colors.LEVLOW)
                elif var.padsVelo == 0:
                    var.padsVelo = 1
                    midiOutMsg(0x90, 0, pads.sespad10_DATA1, colors.LEVMID)"""	