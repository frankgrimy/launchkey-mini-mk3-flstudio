import specialmath as math2, variables as var, knobs
import plugins, channels, midi, ui

def Knobs(midiId, data1, data2):
    channumber = channels.selectedChannel()
    global handled
    handled = False

    if var.SCENE_SEL == "Channel rack" and var.KNOBSTATUS == "Device" and plugins.isValid(channumber):
        if plugins.getPluginName (channumber, -1) in ("Surge", "Surge XT"):
            if midiId == midi.MIDI_CONTROLCHANGE:
                if not var.SHIFT_STATUS:
                    for x in knobs.knobs.values():
                        if data1 == x:
                            plugins.setParamValue(math2.linnormalize(data2, 127, 1, 0), x-21, channumber, -1)
                            handled = True
                            ui.setHintMsg("(" + plugins.getPluginName(channumber, -1, 1) + ") " + "Controlling Macro " + str(x-20) + " (" + (plugins.getParamName(x-21, channumber, -1)[4:]) + ")" + ": " + str(math2.truncate(plugins.getParamValue(x-21, channumber, -1)*100, 1)) + "%" )
def Handled():
    return handled