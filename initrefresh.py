import device, ui
import variables as var

def Initialize():
    if device.isAssigned():
        print(""), print("Novation Launchkey Mini MK3 script by Frank Grimy (@frank.grimy)"), print("")
    try:
        device.midiOutMsg(159,0,12,127) # Set the controller in DAW mode, by sending the appropriate MIDI message.
    except:
        ui.setHintMsg("Can't connect to the controller. Check the Script output.")
        print("Can't connect to the controller. Have you set up the input and the output ports the same?")
    else:
        print("Connection established. DAW mode enabled.")
        print("MIDI port assigned to the controller:", end=" "), print(var.PORT), print("")
