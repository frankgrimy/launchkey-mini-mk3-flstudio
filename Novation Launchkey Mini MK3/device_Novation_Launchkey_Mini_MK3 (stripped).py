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
from sceneup import UpMidi, UpColor, UpColorsIdle
from time import time

apiver4script=23 # Scripting API version compatible with this script.

def OnInit():
    Startup.OnInit()

def OnDeInit():
    QuitFL.OnDeInit()

def OnIdle():
    var.currentTime = time()

# Up button
def OnMidiMsg(event):
    if event.data1 == cons.sceneup_DATA1:
        nowtime = None
        while event.data2:
            # timestamp for the last event
            nowtime = time()
            if nowtime - var.currentTime > 1:
                print("yay")
                break
            else:
                continue
