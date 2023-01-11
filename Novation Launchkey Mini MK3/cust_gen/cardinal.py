### Knob behavior for Cardinal VST Synth (https://github.com/DISTRHO/Cardinal)
import specialmath as math2, variables as var, knobs
import plugins, channels, midi, ui

def Knobs(midiId, data1, data2):
    channumber = channels.selectedChannel()
    global handled
    handled = False

    if plugins.isValid(channumber) and plugins.getPluginName(channumber, -1) == "Cardinal Synth":
        if var.SCENE_SEL == "Channel rack" and var.KNOBSTATUS == "Device":
            if midiId == midi.MIDI_CONTROLCHANGE:
                if not var.SHIFT_STATUS:
                    if data1 in tuple(knobs.knobs.values())[0:9]:
                        handled = True
                        if plugins.getParamName(2080, channumber, -1) == "Parameter 1":
                            plugins.setParamValue(math2.linnormalize(data2,127,1,0), 2080+data1-21, channumber, -1)
                            if data1 in tuple(knobs.knobs.values())[0:9]:
                                ui.setHintMsg("(" + plugins.getPluginName(channumber, -1, 1) + ") " + "Controlling Parameter " + str(data1-20))
                    
def Handled():
    return handled