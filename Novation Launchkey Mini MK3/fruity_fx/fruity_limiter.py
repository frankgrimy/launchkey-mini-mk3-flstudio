### Knob behavior for Fruity Limiter
import specialmath as math2, variables as var, knobs
import plugins, mixer, midi, ui

def Knobs(midiId, data1, data2):
    insert = mixer.trackNumber()
    global handled
    handled = ""

    if var.SCENE_SEL == "Mixer" and var.KNOBSTATUS == "Device":
        if ui.getFocusedFormID == "fruity limiter ID":
            if midiId == midi.MIDI_CONTROLCHANGE:
                if not var.SHIFT_STATUS:
                    if data1 in knobs.knobs.values():
                        if data1 == tuple(knobs.knobs.values())[0]:
                            handled = True
                            if plugins.getParamName(0, insert , fruityId) == "Gain":
                                plugins.setParamValue(math2.truncate(math2.linearize(data1, 0, -1, 127, 1, 0), 2), 0, fruityId)