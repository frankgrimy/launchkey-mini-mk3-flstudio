### Change the modes for the pads (session, drum or custom).
import midi
import constants as cons
import colors
import ui
import device
import pads
import variables as var

def PadModes(midiId, data1, data2):
    if midiId == midi.MIDI_CONTROLCHANGE:
        if data1 == cons.dedpad_DATA1:
                if data2 == cons.sessionpad_DATA2:
                    #global PADSTATUS
                    var.PADSTATUS = "Session"
                    ui.setHintMsg("Pads are now in SESSION mode!")
                elif data2 == cons.drumpad_DATA2:
                    var.PADSTATUS = "Drum"
                    ui.setHintMsg("Pads are now in DRUM mode!")
                    for x in pads.drum_pads.values():
                        device.midiOutMsg(0x99, 0, x, colors.EMPTYWHITE)
                    
                elif data2 == cons.custompad_DATA2:
                    var.PADSTATUS = "Custom"
                    ui.setHintMsg("Pads are now in CUSTOM mode!")

def KnobModes(midiId, data1, data2):
    if data1 == cons.dedknob_DATA1:
        if data2 == cons.volumepad_knob_DATA2:
            #global KNOBSTATUS
            var.KNOBSTATUS = "Volume"
            #print(KNOBSTATUS)
            ui.setHintMsg("Knobs now control VOLUME!")
        elif data2 == cons.panpad_knob_DATA2:
            var.KNOBSTATUS = "Pan"
            #print(KNOBSTATUS)
            ui.setHintMsg("Knobs now control PANNING!")
        elif data2 == cons.devicepad_knob_DATA2:
            var.KNOBSTATUS = "Device"
            #print(KNOBSTATUS)
            ui.setHintMsg("Knobs are now in DEVICE MODE!")
        elif data2 == cons.sendspad_knob_DATA2:    
            var.KNOBSTATUS = "Sends"
            ui.setHintMsg("Knobs now control SENDS!")
            #print(KNOBSTATUS)
        elif data2 == cons.custompad_knob_DATA2:
            var.KNOBSTATUS = "Custom"
            #print(KNOBSTATUS)
            ui.setHintMsg("Knobs are now in FREE MODE!")