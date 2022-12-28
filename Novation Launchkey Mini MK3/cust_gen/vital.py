### Knob behavior for Vital VST.
import specialmath as math2, variables as var, knobs
import plugins, channels, midi, ui

def Knobs(midiId, data1, data2):
    channumber = channels.selectedChannel()
    global handled
    handled = ""
    
    if var.SCENE_SEL == "Channel rack":
        if var.KNOBSTATUS == "Device":
            if plugins.isValid(channumber, -1):
                if plugins.getPluginName(channumber, -1) == "Vital":
                    if midiId == midi.MIDI_CONTROLCHANGE:
                        if not var.SHIFT_STATUS:
                            for x in knobs.knobs.values():
                                if data1 in tuple(knobs.knobs.values())[0:4]:
                                    handled = True
                                    if data1 == x:
                                        if plugins.getParamName(211, channumber, -1) == "Macro 1":
                                            plugins.setParamValue(math2.linnormalize(data2,127,1,0),211+x-21,channumber,-1)
                                            ui.setHintMsg("(" + plugins.getPluginName(channumber, -1, 1) + ") " + "Controlling Macro " + str(x-20) + ": " + str(math2.truncate(plugins.getParamValue(211+x-21, channumber, -1)*100, 1)) + "%")
                                else:
                                    if data1 == x:
                                        handled = True
                                        if plugins.getParamName(48, channumber, -1) == "Envelope 1 Attack":
                                            if x-25 < 2:
                                                plugins.setParamValue(math2.linnormalize(data2,127,1,0),48+2*(x-25),channumber,-1)
                                                if x-25 == 0:
                                                    ui.setHintMsg("(" + plugins.getPluginName(channumber, -1, 1) + ") " + "Controlling Envelope 1 Attack")
                                                elif x-25 == 1:
                                                    ui.setHintMsg("(" + plugins.getPluginName(channumber, -1, 1) + ") " + "Controlling Envelope 1 Decay")
                                            if x-25 == 2:
                                                plugins.setParamValue(math2.linnormalize(data2,127,1,0),48+2*(x-25)+2,channumber,-1)
                                                ui.setHintMsg("(" + plugins.getPluginName(channumber, -1, 1) + ") " + "Controlling Envelope 1 Sustain")
                                            if x-25 == 3:
                                                plugins.setParamValue(math2.linnormalize(data2,127,1,0),48+2*(x-25)-2,channumber,-1)
                                                ui.setHintMsg("(" + plugins.getPluginName(channumber, -1, 1) + ") " + "Controlling Envelope 1 Release")
                        else:
                            handled = False
            else:
                handled = False
                pass
    
def Handled():
    return handled