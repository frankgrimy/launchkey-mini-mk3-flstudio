import specialmath as math2, variables as var, knobs
import plugins, midi, ui

def Knobs(midiId, data1, data2):
    if var.SCENE_SEL == "Mixer" and var.KNOBSTATUS == "Device":
        if midiId == midi.MIDI_CONTROLCHANGE:
            if var.focusedPlugin[0] == "kHs Gain":
                if data1 == 21:
                    plugins.setParamValue(math2.linnormalize(data2,127,1,0), 1, var.focusedPlugin[1], var.focusedPlugin[2], 1) # Gain
                    ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" 
                                          + ") " + "Controlling Gain (" + plugins.getParamValueString(1, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")
                elif data1 == 22:
                    plugins.setParamValue(math2.linnormalize(data2,127,1,0), 2, var.focusedPlugin[1], var.focusedPlugin[2]) # Mode
                    ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" + ") " +
                                  "Controlling Mode (" + plugins.getParamValueString(2, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")