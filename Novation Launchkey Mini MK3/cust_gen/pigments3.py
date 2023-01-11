### Knob behavior for Arturia Pigments 3 VST
import specialmath as math2, variables as var, knobs
import plugins, channels, midi, ui

def Knobs(midiId, data1, data2):
    channumber = channels.selectedChannel()
    global handled
    handled = False

    if plugins.isValid(channumber) and plugins.getPluginName(channumber, -1) == "Pigments":
        if var.SCENE_SEL == "Channel rack" and var.KNOBSTATUS == "Device":
            if midiId == midi.MIDI_CONTROLCHANGE:
                if not var.SHIFT_STATUS:
                    if data1 in tuple(knobs.knobs.values())[0:9]:
                        handled = True
                        if plugins.getParamName(1, channumber, -1) == "Macro 1":
                            plugins.setParamValue(math2.linnormalize(data2,127,1,0), 1+data1-21, channumber, -1)
                            if data1 in tuple(knobs.knobs.values())[0:4]:
                                ui.setHintMsg("(" + plugins.getPluginName(channumber, -1, 1) + ") " + "Controlling Macro " + str(data1-20))
                            
                            elif data1 in tuple(knobs.knobs.values())[4:9]:
                                env = ("Envelope Attack", "Envelope Decay", "Envelope Sustain", "Envelope Release")
                                ui.setHintMsg("(" + plugins.getPluginName(channumber, -1, 1) + ") " + "Controlling " + env[data1-25])
                    
def Handled():
    return handled