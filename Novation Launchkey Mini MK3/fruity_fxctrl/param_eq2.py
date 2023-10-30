import specialmath as math2, variables as var, knobs
import plugins, midi, ui

def Knobs(midiId, data1, data2):
    if var.SCENE_SEL == "Mixer" and var.KNOBSTATUS == "Device":
        if midiId == midi.MIDI_CONTROLCHANGE:
            if var.focusedPlugin[0] == "Fruity parametric EQ 2":
                if not var.SHIFT_STATUS:
                    if data1 == 28:
                        plugins.setParamValue(math2.linnormalize(data2,127,1,0), 35, var.focusedPlugin[1], var.focusedPlugin[2], 1)
                        ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" + ") " +
                                      "Controlling Main level (" + plugins.getParamValueString(35, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")
                    else:
                        for i in range(21, 28):
                            if data1 == i:
                                plugins.setParamValue(math2.linnormalize(data2,127,1,0), i-21, var.focusedPlugin[1], var.focusedPlugin[2], 1) # Band gain
                                ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" + ") " +
                                            "Controlling Band " + str(i-20) + " Gain (" + plugins.getParamValueString(i-21, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")

                elif var.SHIFT_STATUS:
                    for i in range(21,28):
                        if data1 == i:
                            plugins.setParamValue(math2.linnormalize(data2,127,1,0), i-14, var.focusedPlugin[1], var.focusedPlugin[2], 1) # Band freq
                            ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" + ") " +
                                        "Controlling Band " + str(i-20) + " Freq (" + plugins.getParamValueString(i-14, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")