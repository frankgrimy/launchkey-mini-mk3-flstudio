from general import getVersion
import constants as cons
from time import time
from device import isAssigned, midiOutMsg
from ui import setHintMsg
from variables import PORT
from playlist import getPerformanceModeState
import variables as var


def Initialize():
    if isAssigned():
        print(""), print("Novation Launchkey Mini MK3 script by Frank Grimy (@frank.grimy)"), print("")
    try:
        midiOutMsg(159,0,12,127) # Set the controller in DAW mode, by sending the appropriate MIDI message.
    except:
        setHintMsg("Can't connect to the controller. Check the Script output.")
        print("Can't connect to the controller. Have you set up the input and the output ports the same?")
    else:
        print("Connection established. DAW mode enabled.")
        print("MIDI port assigned to the controller:", end=" "), print(PORT), print("")


class Init():
    def OnInit(self):
        if getVersion() >= cons.apiver4script:
            Initialize()
            cons.startTime = time()
        else:
            print("")
            print ("This script might not be supported in this FL Studio version.")
            print ("Please upgrade to version 20.9.2 (build 2963 for Windows, or MacOS equivalent) or higher."), print("")
            print("Scripting API version needed:", end=" "), print(cons.apiver4script)
            print("Scripting API version installed:", end=" "), print(getVersion())
            print("")
            print("Attempting to start anyway...")
            Initialize()

        if isAssigned():
            midiOutMsg(0xBF, 0, 0x09, 0x01) # Set the knobs default target to Volume.
            var.isPerformance = getPerformanceModeState()
                
Startup = Init()