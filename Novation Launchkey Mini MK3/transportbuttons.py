import variables as var
import constants as cons
import midi
import transport
import ui

def TrBehavior(midiId, data1, data2):
    if midiId == midi.MIDI_CONTROLCHANGE:
            if data1 == cons.shift_DATA1:
                if data2 == 127:
                    var.SHIFT_STATUS = True
                    
                else:
                    var.SHIFT_STATUS = False
                    
            if data2 > 0:
                if data1 == cons.play_button:              # Play button behavior. It gets back to the start when stop signal is triggered (the same as the space bar action).
                    if transport.isPlaying():
                        if var.SHIFT_STATUS:                    # If Shift button is hold, then play button will trigger a pause signal instead of a stop one.
                            transport.start()
                            
                        else:
                            transport.stop()
                            
                            ui.setHintMsg("Playback stopped!")
                    else:
                        if var.SHIFT_STATUS:
                            transport.stop()
                            ui.setHintMsg("Playing position reseted!")
                        else:
                            if ui.isStartOnInputEnabled():
                                transport.start()
                                ui.setHintMsg("Waiting for input ...")
                            else:
                                transport.start()
                                ui.setHintMsg("Now playing!")
                        
                if data2 > 0:
                    if data1 == cons.record_button:        # Record button behavior.
                        if var.SHIFT_STATUS == False:
                        #print ("Record")
                            if transport.isRecording():
                                transport.record()
                                ui.setHintMsg("Recording is now unarmed!")
                            else:
                                transport.record()
                                ui.setHintMsg("Armed for recording!")

def Handler(midiId, data1):
    if midiId == midi.MIDI_CONTROLCHANGE:
        if var.SHIFT_STATUS:
            if data1 == cons.play_button:
                return False
        else:
            if data1 == cons.play_button or cons.record_button:
                return True