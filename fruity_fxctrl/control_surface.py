import specialmath as math2, variables as var, knobs
import plugins, midi, ui

def Knobs(midiId: int, data1: int, data2: int):
    if var.SCENE_SEL == "Mixer" and var.KNOBSTATUS == "Device":
        if midiId == midi.MIDI_CONTROLCHANGE:
            if var.focusedPlugin[0] == "Control Surface":
                if not var.SHIFT_STATUS:
                    for i in range(21, 29):
                        if data1 == i:
                            plugins.setParamValue(math2.linnormalize(data2,127,1,0), i-21, var.focusedPlugin[1], var.focusedPlugin[2])
                            ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" + ") " +
                                        "Controlling " + plugins.getParamName(i-21, var.focusedPlugin[1], var.focusedPlugin[2]) + " (" +
                                        str(math2.truncate(plugins.getParamValue(i-21, var.focusedPlugin[1], var.focusedPlugin[2]), 2)) + ")")