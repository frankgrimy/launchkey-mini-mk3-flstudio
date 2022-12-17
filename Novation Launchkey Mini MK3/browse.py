### Behavior and colors for scene buttons while browsing.
import variables as var
import constants as cons
import midi, device, ui, transport

def Arrowkeys(midiId, data1, data2):
    if midiId == midi.MIDI_CONTROLCHANGE:
        if data1 == cons.shift_DATA1:
            if data2 == 127:
                var.SHIFT_STATUS = True
                #return True
            else:
                var.SHIFT_STATUS = False
                #return True
        """if data2 == 0:                          # Set the buttons release as handled. They have no assigned behavior at release, but setting this status avoids DAW "unhandled" behavior.
            if data1 == cons.record_button:
                #return True
            elif data1 == cons.play_button:
                #return True
            elif data1 == cons.shift_DATA1:
                #return True
            else:
                #return False
        """
    if midiId == midi.MIDI_CONTROLCHANGE:
        if var.SHIFT_STATUS:
            device.midiOutMsg(0xb2, 0, 0x69, 0x35)
            device.midiOutMsg(0xb2, 0, 0x68, 0x35)
            device.midiOutMsg(0xb2, 0, 0x66, 0x01)
            device.midiOutMsg(0xb2, 0, 0x67, 0x01)
            if data1 == cons.scenedown_DATA1:
                if data2 > 0:
                    if var.FOCUS_STATUS == "Mixer":
                            ui.down()
                            device.midiOutMsg(0xbf, 0 , 0x69, 0x7f)
                            ui.setHintMsg("Skipping 4 mixer tracks")
                    elif var.FOCUS_STATUS == "Browser" or "Channel rack":
                            ui.next()
                            device.midiOutMsg(0xbf, 0 , 0x69, 0x7f)
                            ui.setHintMsg("Focus moving down")
            elif data1 == cons.sceneup_DATA1:
                if data2 > 0:
                    if var.FOCUS_STATUS == "Mixer":
                        ui.up()
                        device.midiOutMsg(0xbf, 0 , 0x68, 0x7f)
                        ui.setHintMsg("Returning 4 mixer tracks")
                    elif var.FOCUS_STATUS == "Browser" or "Channel rack":
                        ui.previous()
                        device.midiOutMsg(0xbf, 0 , 0x68, 0x7f)
                        ui.setHintMsg("Focus moving up")
            elif data1 == cons.sceneleft_DATA1:
                if data2 > 0:
                    if var.FOCUS_STATUS == "Browser":
                        transport.globalTransport(midi.FPT_Left, 1)
                        device.midiOutMsg(0xbf, 0, 0x67, 0x7f)
                        ui.setHintMsg("Back to parent folder")
                    elif var.FOCUS_STATUS == "Mixer":
                        ui.previous()
                        device.midiOutMsg(0xbf, 0, 0x67, 0x7f)
            elif data1 == cons.sceneright_DATA1:
                if data2 > 0:
                    if var.FOCUS_STATUS == "Browser":
                        transport.globalTransport(midi.FPT_Right, 1)
                        ui.setHintMsg("Getting into folder / Playing sample")
                        device.midiOutMsg(0xbf, 0, 0x66, 0x7f)
                    elif var.FOCUS_STATUS == "Mixer":
                        ui.next()
                        device.midiOutMsg(0xbf, 0, 0x66, 0x7f)
        else:
            device.midiOutMsg(0xbf, 0 , 0x67, 0x00)
            device.midiOutMsg(0xb2, 0 , 0x66, 0x00)

