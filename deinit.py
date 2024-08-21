# Run when the controller is disconnected from FL Studio
import device

class DeInit():
    def OnDeInit(self):
        if device.isAssigned():
            device.midiOutMsg(0xBF, 0, 0x73, 0x00)
            device.midiOutMsg(159,0,12,0)
            print("Connection disabled. Back to Standalone mode.\n")

QuitFL = DeInit()