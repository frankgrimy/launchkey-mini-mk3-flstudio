import specialmath as math2, variables as var, knobs
import plugins, channels, midi, ui
def Knobs(midiId, data1, data2):
    channumber = channels.selectedChannel()
    global handled
    handled = False

    if var.SCENE_SEL == "Channel rack" and var.KNOBSTATUS == "Device" and plugins.isValid(channumber):
        if plugins.getPluginName (channumber, -1) == "Sytrus":
            if midiId == midi.MIDI_CONTROLCHANGE:
                if not var.SHIFT_STATUS:
                    if data1 == 21:
                        handled = True
                        if plugins.getParamName(18, channumber, -1) == "Main - Modulation X":
                            plugins.setParamValue(math2.linnormalize(data2, 127, 1, 0), 18, channumber, -1)
                    elif data1 == 22:
                        handled = True
                        if plugins.getParamName(19, channumber, -1) == "Main - Modulation Y":
                            plugins.setParamValue(math2.linnormalize(data2, 127, 1, 0), 19, channumber, -1)


def Handled():
    return handled