import specialmath as math2, variables as var, knobs
import plugins, midi, ui

def Knobs(midiId: int, data1: int, data2: int):
    if var.SCENE_SEL == "Mixer" and var.KNOBSTATUS == "Device":
        if midiId == midi.MIDI_CONTROLCHANGE:
            if var.focusedPlugin[0] == "Fruity Limiter":
                if not var.SHIFT_STATUS:
                    if data1 == 21:
                        plugins.setParamValue(math2.linnormalize(data2,127,1,0), 0, var.focusedPlugin[1], var.focusedPlugin[2], 1)
                        ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" + ") " +
                                    "Controlling Gain (" + plugins.getParamValueString(0, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")
                    elif data1 == 22:
                        plugins.setParamValue(math2.linnormalize(data2,127,1,0), 1, var.focusedPlugin[1], var.focusedPlugin[2], 1)
                        ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" + ") " +
                                    "Controlling saturation (" + plugins.getParamValueString(1, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")
                    elif data1 == 23:
                        plugins.setParamValue(math2.linnormalize(data2,127,1,0), 2, var.focusedPlugin[1], var.focusedPlugin[2], 1)
                        ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" + ") " +
                                    "Controlling Ceiling (" + plugins.getParamValueString(2, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")
                    elif data1 == 24:
                        plugins.setParamValue(math2.linnormalize(data2,127,1,0), 3, var.focusedPlugin[1], var.focusedPlugin[2], 1)
                        ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" + ") " +
                                    "Controlling Lim attack time (" + plugins.getParamValueString(3, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")
                    elif data1 == 25:
                        plugins.setParamValue(math2.linnormalize(data2,127,1,0), 5, var.focusedPlugin[1], var.focusedPlugin[2], 1)
                        ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" + ") " +
                                    "Controlling Lim release time (" + plugins.getParamValueString(5, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")
                    elif data1 == 26:
                        plugins.setParamValue(math2.linnormalize(data2,127,1,0), 7, var.focusedPlugin[1], var.focusedPlugin[2], 1)
                        ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" + ") " +
                                    "Controlling Lim peak window (" + plugins.getParamValueString(7, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")
                        
                elif var.SHIFT_STATUS:
                    if data1 == 21:
                        plugins.setParamValue(math2.linnormalize(data2,127,1,0), 0, var.focusedPlugin[1], var.focusedPlugin[2], 1)
                        ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" + ") " +
                                    "Controlling Gain (" + plugins.getParamValueString(0, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")
                    elif data1 == 22:
                        plugins.setParamValue(math2.linnormalize(data2,127,1,0), 1, var.focusedPlugin[1], var.focusedPlugin[2], 1)
                        ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" + ") " +
                                    "Controlling saturation (" + plugins.getParamValueString(1, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")
                    elif data1 == 23:
                        plugins.setParamValue(math2.linnormalize(data2,127,1,0), 8, var.focusedPlugin[1], var.focusedPlugin[2], 1)
                        ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" + ") " +
                                    "Controlling Comp threshold (" + plugins.getParamValueString(8, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")
                    elif data1 == 24:
                        plugins.setParamValue(math2.linnormalize(data2,127,1,0), 10, var.focusedPlugin[1], var.focusedPlugin[2], 1)
                        ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" + ") " +
                                    "Controlling Comp ratio (" + plugins.getParamValueString(10, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")
                    elif data1 == 25:
                        plugins.setParamValue(math2.linnormalize(data2,127,1,0), 9, var.focusedPlugin[1], var.focusedPlugin[2], 1)
                        ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" + ") " +
                                    "Controlling Comp knee (" + plugins.getParamValueString(9, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")
                    elif data1 == 26:
                        plugins.setParamValue(math2.linnormalize(data2,127,1,0), 11, var.focusedPlugin[1], var.focusedPlugin[2], 1)
                        ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" + ") " +
                                    "Controlling Comp attack time (" + plugins.getParamValueString(11, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")
                    elif data1 == 27:
                        plugins.setParamValue(math2.linnormalize(data2,127,1,0), 12, var.focusedPlugin[1], var.focusedPlugin[2], 1)
                        ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" + ") " +
                                    "Controlling Comp release time (" + plugins.getParamValueString(12, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")
                    elif data1 == 28:
                        plugins.setParamValue(math2.linnormalize(data2,127,1,0), 14, var.focusedPlugin[1], var.focusedPlugin[2], 1)
                        ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" + ") " +
                                    "Controlling Comp RMS window (" + plugins.getParamValueString(14, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")