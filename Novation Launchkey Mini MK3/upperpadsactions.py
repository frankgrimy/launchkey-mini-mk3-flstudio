### Actions for the upper pads.
import variables as var
import constants as cons
import pads
import colors
import device
import midi
import transport
import ui

def UpperPads(midiId, data1, data2):
    if not var.PADSTATUS == "Drum":
        if midiId == midi.MIDI_NOTEON:
            #handled = True
            if data1 == pads.sespad1_DATA1:
                if data2 > 0:
                    if transport.getLoopMode():
                        transport.setLoopMode()
                        ui.setHintMsg("Pattern mode")
                    else:
                        transport.setLoopMode()
                        ui.setHintMsg("Song mode")
            if data1 == pads.sespad2_DATA1:
                if data2 > 0:
                    if ui.isMetronomeEnabled():
                        #print("Metro OFF")
                        transport.globalTransport(midi.FPT_Metronome, 1)
                        ui.setHintMsg("Metronome OFF")
                    else:
                        #print("Metro ON")
                        transport.globalTransport(midi.FPT_Metronome, 1)
                        ui.setHintMsg("Metronome ON")
            if data1 == pads.sespad3_DATA1:
                if data2 > 0:
                    if ui.isStartOnInputEnabled():
                        transport.globalTransport(midi.FPT_WaitForInput, 1)
                        device.midiOutMsg(0x90,0,0x62,70)
                        ui.setHintMsg("Start on input OFF")
                    else:
                        transport.globalTransport(midi.FPT_WaitForInput, 1)
                        device.midiOutMsg(0x90,0,0x62,0x09)
                        ui.setHintMsg("Start on input ON")
            if data1 == pads.sespad4_DATA1:
                if data2 > 0:
                    if ui.isPrecountEnabled():
                        transport.globalTransport(midi.FPT_CountDown, 1)
                        device.midiOutMsg(0x90,0,0x63,70)
                        ui.setHintMsg("Countdown before recording OFF")
                    else:
                        transport.globalTransport(midi.FPT_CountDown, 1)
                        device.midiOutMsg(0x90,0,0x63,0x09)
                        ui.setHintMsg("Countdown before recording ON")
            if data1 == pads.sespad5_DATA1:
                if data2 > 0:
                    if ui.getVisible(2):
                        if ui.getFocused(2):
                            ui.hideWindow(2)
                            ui.setHintMsg("Playlist closed!")
                            device.midiOutMsg(0x90,0,pads.sespad5_DATA1,70)
                        else:
                            ui.setFocused(2)
                            ui.setHintMsg("Playlist focused!")
                    else:
                        ui.showWindow(2)
                        ui.setHintMsg("Playlist open!")
                        device.midiOutMsg(0x92,0,pads.sespad5_DATA1,colors.ORANGE2)
            if data1 == pads.sespad6_DATA1:
                if data2 > 0:
                    if ui.getVisible(1):
                        ui.hideWindow(1)
                        ui.setHintMsg("Channel rack closed!")
                        device.midiOutMsg(0x90,0,pads.sespad6_DATA1,70)
                    else:
                        ui.showWindow(1)
                        ui.setHintMsg("Channel rack open!")
                        device.midiOutMsg(0x92,0,pads.sespad6_DATA1,colors.ORANGE2)

            if data1 == pads.sespad7_DATA1:
                if data2 > 0:
                    if not (var.SCENE_SEL== "Channel rack" and var.scmodes.get("CHANRACK_READYFOR") == "Stop"):
                        if ui.getVisible(3):
                            ui.hideWindow(3)
                            ui.setHintMsg("Piano roll closed!")
                        else:
                            ui.showWindow(3)
                            ui.setHintMsg("Piano roll open!")
                    
            if data1 == pads.sespad8_DATA1:
                if data2 > 0:
                    if not (var.SCENE_SEL== "Channel rack" and var.scmodes.get("CHANRACK_READYFOR") == "Stop"):
                        if ui.getVisible(0):
                            if ui.getFocused(0):
                                ui.hideWindow(0)
                                ui.setHintMsg("Mixer closed!")
                            else:
                                ui.setFocused(0)
                                ui.setHintMsg("Mixer focused!")
                        else:
                            ui.showWindow(0)
                            ui.setHintMsg("Mixer open!")