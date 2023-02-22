#   name=Novation Launchkey Mini MK3 (by Frank Grimy)(STRIPPED)
#   url=https://forum.image-line.com/viewtopic.php?f=1994&t=260133
#   supportedDevices=MIDIIN2 (Launchkey Mini MK3 MID,Launchkey Mini MK3 DAW Port

# Import list
import midi, mixer, channels
from mxr.mirectangle import Rectangle
import pads, knobs, mixerlowpads, browse, handlers
import variables as var, constants as cons, drumpads as drum, stepsequencer as step, panvol as pv, scenedown as scdown
import uimessages as uimsg, scenedownlights as downlight, upperpadslights as uplights, padknobmodes as pkm
import upperpadsactions as upact, crlowpads as crlp, transportbuttons as trns
from cust_gen import *
from fruity_gen import *

import mxr.embdeq
from editors.shortcuts import *
from time import time
from deinit import QuitFL
from initialize import Startup
from windowfocus import WindowFocus
from sceneup import UpColor, UpColorsIdle
from time import time, sleep

apiver4script=23 # Scripting API version compatible with this script.

def OnInit():
    Startup.OnInit()

def OnDeInit():
    QuitFL.OnDeInit()

def OnIdle():
    var.currentTime = time() # Keep track of time

# # Button
# def OnMidiMsg(event):
#     if event.data1 == cons.sceneup_DATA1: # If the desired button is pressed...
#         pushtime = None # Timestamp for the button press
#         while event.data2: # While the button is pressed...
#             # timestamp for the last event
#             pushtime = time() # Create a timestamp for the button press
#             if pushtime - var.currentTime > 0.5: # If the button is pressed for more than 1 second...
#                 print("Long press detected") # Print a message to the console
#                 break # Break the loop
#             else:
#                 if event.data2:
#                     sleep(0.1)
#                     continue
#                 else:
#                     print("Short press detected")
#                     break

# def OnMidiMsg(event):
#     if event.data1 == cons.sceneup_DATA1: # If the desired button is pressed...
#         pushtime = None # Timestamp for the button press
#         while True: # While the button is pressed...
#             if event.data2:
#                 pushtime = time() # Create a timestamp for the button press
#                 if pushtime - var.currentTime > 0.5: # If the button is pressed for more than 1 second...
#                     print("Long press detected") # Print a message to the console
#                     break # Break the loop
#                 else:
#                     if event.data2:
#                         sleep(0.1)
#                         continue
#                     else:
#                         print("Short press detected")
#                         break

pushTime = 0
relTime = 0
class HoldButton():
    def OnIdle(event):
        global pushTime, relTime
        # isPushed = False
        # isReleased = False
        # pushTime = None
        # relTime = None
        # # if event.data2:
        # #     pushTime = time()
        # #     if event.data1 == cons.sceneup_DATA1:
        # #         print("Button is held")
        # #         print(str(pushTime) + " " + str(var.currentTime) + " " + str(pushTime - var.currentTime))
        # #     else:
        # #         print("Button is not held")
        # if event.data1 == cons.sceneup_DATA1:
        #     while True:
        #         if event.data2:
        #             isPushed = True
        #             pushTime = time()
        #             if pushTime - var.currentTime > 0.5:
        #                 sleep(0.1)
        #                 print("Long press detected")
        #                 break
        #         elif not event.data2 and isPushed:
        #             isReleased = True
        #             relTime = time()
        #             print(relTime-pushTime)
        #             if relTime - pushTime < 0.5:
        #                 print("Short press detected")
        #                 sleep(0.1)
        #                 break
        #         else:
        #             break
        # pushTime = None
        # relTime = None
        if event.data1 == cons.sceneup_DATA1:
            if event.data2:
                pushTime = time()
                # print("Push: ", pushTime, "Release: ", relTime)
            elif not event.data2:
                relTime = time()
                # print("Push: ", pushTime, "Release: ", relTime)
            if relTime - pushTime > 0.25 and pushTime != 0 and relTime != 0:
                print("Long press detected")
                pushTime = 0
                relTime = 0
            elif relTime - pushTime <= 0.25 and pushTime != 0 and relTime != 0:
                print("Short press detected")
                pushTime = 0
                relTime = 0
            else:
                pass



def OnMidiMsg(event):
    HoldButton.OnIdle(event)
