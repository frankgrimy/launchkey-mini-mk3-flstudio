### Knob behavior for Massive synth (https://www.native-instruments.com/en/products/komplete/synths/massive/)
import specialmath as math2, variables as var, knobs
import plugins, channels, midi, ui

def Knobs(midiId, data1, data2):
    channumber = channels.selectedChannel()
    global handled
    handled = False

    if plugins.isValid(channumber) and plugins.getPluginName (channumber, -1) == "Massive":
        if var.SCENE_SEL == "Channel rack" and var.KNOBSTATUS == "Device":
            if midiId == midi.MIDI_CONTROLCHANGE:
                if not var.SHIFT_STATUS:
                    for x in knobs.knobs.values():
                        if data1 == x:
                            plugins.setParamValue(math2.linnormalize(data2, 127, 1, 0), x-20, channumber, -1)
                            handled = True
                            ui.setHintMsg("(" + plugins.getPluginName(channumber, -1, 1) + ") " + "Controlling Macro " + str(x-20) + " (" + plugins.getParamName(x-20, channumber, -1) + ")")

def Handled():
    return handled