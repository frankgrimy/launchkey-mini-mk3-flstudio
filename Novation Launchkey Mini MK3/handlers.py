### Handlers. Set events as handled.
#from transportbuttons import Handler
import variables as var, constants as cons, knobs
import midi
#from cust_gen import *
import cust_gen
#from fruity_gen import flex, sytrus, harmor
#from fruity_gen import *
import fruity_gen
from mxr import embdeq

def PadHandler(midiId, data1):          # Specific handler for pads.
    handled = ""
    if midiId == midi.MIDI_NOTEON:
        if not var.PADSTATUS == "Drum":
            handled = True
    
    return bool(handled)

def SceneHandler(midiId, data1):
    handled = ""
    customsynths = []
    for i in cust_gen.__all__:
        customsynths.append("cust_gen." + i + ".Handled")
    
    fruitysynths = []
    for i in fruity_gen.__all__:
        fruitysynths.append("fruity_gen." + i + ".Handled")

    if midiId == (midi.MIDI_CONTROLCHANGE):
        if not var.SHIFT_STATUS:
            if data1 in knobs.knobs.values():
                if var.KNOBSTATUS in ("Volume", "Pan"):
                    handled = True
                else:
                    handled = False
            else:
                handled = True
            
        else:
            if data1 == cons.shift_DATA1 or cons.play_button:
                if not data1 == cons.record_button:
                    if not data1 in knobs.knobs.values():
                        handled = True
                    else:
                        handled = False
                else:
                    handled = False
        
        for i in customsynths + fruitysynths:
            if eval(i):
                handled = True
        if embdeq.Handled():
        #elif embdeq.Handled():
            handled = True
    
    return handled