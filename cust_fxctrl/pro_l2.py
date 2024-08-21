import specialmath as math2, variables as var, knobs
import plugins, midi, ui

def Knobs(midiId, data1, data2):
    if var.SCENE_SEL == "Mixer" and var.KNOBSTATUS == "Device":
        if not var.SHIFT_STATUS:
            if midiId == midi.MIDI_CONTROLCHANGE:
                if var.focusedPlugin[0] == "Pro-L 2":
                    if data1 == tuple(knobs.knobs.values())[0]:
                        if plugins.getParamName(0, var.focusedPlugin[1], var.focusedPlugin[2]) == "Gain":
                            plugins.setParamValue(math2.linnormalize(data2,127,1,0), 0, var.focusedPlugin[1], var.focusedPlugin[2], 1)
                            ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" 
                                          + ") " + "Controlling Gain (" + plugins.getParamValueString(0, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")
                    
                    elif data1 == tuple(knobs.knobs.values())[1]:
                        if plugins.getParamName(2, var.focusedPlugin[1], var.focusedPlugin[2]) == "Lookahead":
                            plugins.setParamValue(math2.linnormalize(data2,127,1,0), 2, var.focusedPlugin[1], var.focusedPlugin[2])
                            ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" 
                                          + ") " + "Controlling Lookahead (" + plugins.getParamValueString(2, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")
                    
                    elif data1 == tuple(knobs.knobs.values())[2]:
                        if plugins.getParamName(3, var.focusedPlugin[1], var.focusedPlugin[2]) == "Attack":
                            plugins.setParamValue(math2.linnormalize(data2,127,1,0), 3, var.focusedPlugin[1], var.focusedPlugin[2])
                            ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" 
                                          + ") " + "Controlling Attack (" + plugins.getParamValueString(3, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")
                            
                    elif data1 == tuple(knobs.knobs.values())[3]:
                        if plugins.getParamName(4, var.focusedPlugin[1], var.focusedPlugin[2]) == "Release":
                            plugins.setParamValue(math2.linnormalize(data2,127,1,0), 4, var.focusedPlugin[1], var.focusedPlugin[2])
                            ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" 
                                          + ") " + "Controlling Release (" + plugins.getParamValueString(4, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")
                            
                    elif data1 == tuple(knobs.knobs.values())[4]:
                        if plugins.getParamName(5, var.focusedPlugin[1], var.focusedPlugin[2]) == "Channel Link Transients":
                            plugins.setParamValue(math2.linnormalize(data2,256,1,0), 5, var.focusedPlugin[1], var.focusedPlugin[2])
                            ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" 
                                          + ") " + "Controlling Channel Link Transients (" + plugins.getParamValueString(5, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")
                            
                    elif data1 == tuple(knobs.knobs.values())[5]:
                        if plugins.getParamName(6, var.focusedPlugin[1], var.focusedPlugin[2]) == "Channel Link Release":
                            plugins.setParamValue(math2.linnormalize(data2,256,1,0), 6, var.focusedPlugin[1], var.focusedPlugin[2])
                            ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" 
                                          + ") " + "Controlling Channel Link Release (" + plugins.getParamValueString(6, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")
                        
                    elif data1 == tuple(knobs.knobs.values())[6]:
                        if plugins.getParamName(18, var.focusedPlugin[1], var.focusedPlugin[2]) == "Output Level":
                            plugins.setParamValue(math2.linnormalize(data2,127,1,0), 18, var.focusedPlugin[1], var.focusedPlugin[2], 1)
                            ui.setHintMsg("(" + var.focusedPlugin[0] + " [" + str(var.focusedPlugin[1]+1) + "," + str(var.focusedPlugin[2]+1) + "]" 
                                          + ") " + "Controlling Output Level (" + plugins.getParamValueString(18, var.focusedPlugin[1], var.focusedPlugin[2]) + ")")