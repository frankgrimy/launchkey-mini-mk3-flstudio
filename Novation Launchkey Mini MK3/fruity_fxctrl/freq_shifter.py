import specialmath as math2, variables as var, knobs
import plugins, midi, ui

def Knobs(midiId, data1, data2):
    if var.SCENE_SEL == "Mixer" and var.KNOBSTATUS == "Device":
        if midiId == midi.MIDI_CONTROLCHANGE:
            if var.focusedPlugin[0] == "Frequency Shifter":
                if data1 == 21:
                    plugins.setParamValue(math2.linnormalize(data2,127,1,0), 2, var.focusedPlugin[1], var.focusedPlugin[2], 1) # Frequency
                elif data1 == 22:
                    plugins.setParamValue(math2.linnormalize(data2,127,1,0), 4, var.focusedPlugin[1], var.focusedPlugin[2], 1) # Left shape
                elif data1 == 23:
                    plugins.setParamValue(math2.linnormalize(data2,127,1,0), 5, var.focusedPlugin[1], var.focusedPlugin[2], 1) # Right shape
                elif data1 == 24:
                    plugins.setParamValue(math2.linnormalize(data2,127,1,0), 9, var.focusedPlugin[1], var.focusedPlugin[2], 1) # Start phase
                elif data1 == 25:
                    plugins.setParamValue(math2.linnormalize(data2,127,1,0), 3, var.focusedPlugin[1], var.focusedPlugin[2], 1) # L/R phase
                elif data1 == 26:
                    plugins.setParamValue(math2.linnormalize(data2,127,1,0), 6, var.focusedPlugin[1], var.focusedPlugin[2], 1) # Feedback
                elif data1 == 27:
                    plugins.setParamValue(math2.linnormalize(data2,127,1,0), 0, var.focusedPlugin[1], var.focusedPlugin[2], 1) # Mix
                elif data1 == 28:
                    plugins.setParamValue(math2.linnormalize(data2,127,1,0), 7, var.focusedPlugin[1], var.focusedPlugin[2], 1) # Stereo