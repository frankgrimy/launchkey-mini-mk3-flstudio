### Editor + Monitor config
import midi
import pads
import variables as var
import transport
from ui import setHintMsg
from general import undo, undoUp
from device import midiOutMsg
import colors
from time import time, time_ns
from mxr import levelmon
from mixer import trackNumber as number, getTrackPeaks as peaks, isTrackMuted as muted

def Shortcuts(midiId, data1, data2): ### This is a fast implementation of the editor window.
    if var.SCENE_SEL == "Editor":
        if not var.scmodes.get("EDITOR_READYFOR"):
            if midiId == midi.MIDI_NOTEON:
                if data2:
                    #global shortpress,shortdata
                    var.shortpress = True
                    var.shortdata = data1
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
                    """
                    if data1 == pads.sespad15_DATA1:
                        if data2:
                            presstime = time()
                            var.repeatqueue["sespad15_DATA1"] = presstime
                        else:
                            var.repeatqueue["sespad15_DATA1"] = None
                    """
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

            else:
                midiOutMsg(0x92, 0, pads.sespad9_DATA1, colors.MENU)
                midiOutMsg(0x92, 0, pads.sespad10_DATA1, colors.CCP)
                midiOutMsg(0x92, 0, pads.sespad11_DATA1, colors.CCP)
                midiOutMsg(0x92, 0, pads.sespad12_DATA1, colors.CCP)
                midiOutMsg(0x92, 0, pads.sespad13_DATA1, colors.UNRE)
                midiOutMsg(0x92, 0, pads.sespad14_DATA1, colors.UNRE)
                midiOutMsg(0x92, 0, pads.sespad15_DATA1, 0)
                midiOutMsg(0x92, 0, pads.sespad16_DATA1, 0)
        elif var.scmodes.get("EDITOR_READYFOR") != "Stop":
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
