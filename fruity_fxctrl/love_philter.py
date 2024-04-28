import specialmath as math2, variables as var, knobs
import plugins, midi, ui

def Knobs(midiId, data1, data2):
    if var.SCENE_SEL == "Mixer" and var.KNOBSTATUS == "Device":
        if not var.SHIFT_STATUS:
            if midiId == midi.MIDI_CONTROLCHANGE:
                if var.focusedPlugin[0] == "Fruity Love Philter":
                    if data1 == 21:
                        plugins.setParamValue(math2.linnormalize(data2,127,1,0), 6, var.focusedPlugin[1], var.focusedPlugin[2], 1) # Mod X
                        ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" + ") " +
                                    "Controlling Mod X (" + plugins.getParamValueString(6, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")
                    elif data1 == 22:
                        plugins.setParamValue(math2.linnormalize(data2,127,1,0), 7, var.focusedPlugin[1], var.focusedPlugin[2], 1) # Mod Y
                        ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" + ") " +
                                    "Controlling Mod Y (" + plugins.getParamValueString(7, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")