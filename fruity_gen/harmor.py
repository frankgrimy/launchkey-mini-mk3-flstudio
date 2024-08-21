import specialmath as math2, variables as var, knobs
import plugins, channels, midi, ui
def Knobs(midiId, data1, data2):
    channumber = channels.selectedChannel()
    global handled
    handled = False

    if plugins.isValid(channumber) and plugins.getPluginName (channumber, -1) == "Harmor":
        if var.SCENE_SEL == "Channel rack" and var.KNOBSTATUS == "Device":
            if midiId == midi.MIDI_CONTROLCHANGE:
                if not var.SHIFT_STATUS:
                    if data1 == 21:
                        handled = True
                        if plugins.getParamName(772, channumber, -1) == "Modulation X":
                            plugins.setParamValue(math2.linnormalize(data2, 127, 1, 0), 772, channumber, -1)
                    elif data1 == 22:
                        handled = True
                        if plugins.getParamName(773, channumber, -1) == "Modulation Y":
                            plugins.setParamValue(math2.linnormalize(data2, 127, 1, 0), 773, channumber, -1)
                    elif data1 == 23:
                        handled = True
                        if plugins.getParamName(774, channumber, -1) == "Modulation Z":
                            plugins.setParamValue(math2.linnormalize(data2, 127, 1, 0), 774, channumber, -1)


def Handled():
    return handled