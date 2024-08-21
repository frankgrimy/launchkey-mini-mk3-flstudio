import specialmath as math2, variables as var, knobs
import plugins, channels, midi, ui

def Knobs(midiId, data1, data2):
    channumber = channels.selectedChannel()
    global handled
    handled = False

    if plugins.isValid(channumber) and plugins.getPluginName (channumber, -1) == "FLEX":
        if var.SCENE_SEL == "Channel rack" and var.KNOBSTATUS == "Device":
            if midiId == midi.MIDI_CONTROLCHANGE:
                if not var.SHIFT_STATUS:
                    for x in knobs.knobs.values():
                        if data1 == x:
                            plugins.setParamValue(math2.linnormalize(data2, 127, 1, 0), 10+x-21, channumber, -1)
                            handled = True

def Handled():
    return handled