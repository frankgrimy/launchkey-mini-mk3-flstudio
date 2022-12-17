import variables as var
import mixer, general, midi
import specialmath as math2
import knobs

def setMixerEQGain(data1, track, band, data2):   #band 0..2, value -1..1
    global handled
    handled = ""
    if var.KNOBSTATUS == "Device" and var.SCENE_SEL == "Mixer":
        if not var.SHIFT_STATUS:
            if data1 in knobs.knobs.values():
                if data1-21 <=2:
                    #value = round((data2*3600/127)-1800)
                    value = round(1800*((data2*2/127)-1)**3)
                    """if math2.truncate(((data2*36/127)-18), 1) in (0.1,-0.1):
                        value = 0
                        print(value)
                    else:
                        value = round(100*math2.truncate(((data2*36/127)-18), 1))
                        print(value)
                    """#print(round(data2*18))
                    general.processRECEvent(midi.REC_Mixer_EQ_Gain+(data1-21)+mixer.getTrackPluginId(track, 0), value, midi.REC_UpdateControl | midi.REC_UpdateValue | midi.REC_ShowHint)
                    handled = True
                    #general.processRECEvent(midi.REC_Mixer_EQ_Gain+band+mixer.getTrackPluginId(chan, 0), round(value*1800), midi.REC_UpdateControl | midi.REC_UpdateValue | midi.REC_ShowHint)
                elif 3 <= data1-21 <= 5:
                    value = round((data2/127)*65535)
                    #def setMixerEQFrequency(chan, band, value):   #band 0..2, value 0..1
                    general.processRECEvent(midi.REC_Mixer_EQ_Freq+(data1-24)+mixer.getTrackPluginId(track, 0), value, midi.REC_UpdateControl | midi.REC_UpdateValue | midi.REC_ShowHint)
                    handled = True
                else:
                    handled = False
            
def Handled():
    return handled
            