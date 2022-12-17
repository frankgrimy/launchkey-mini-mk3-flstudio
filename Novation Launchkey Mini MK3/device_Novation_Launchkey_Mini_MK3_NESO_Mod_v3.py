#   name=Novation Launchkey Mini MK3 (NESO Mod) v2022.12.171
#   url=https://forum.image-line.com/viewtopic.php?f=1994&t=260133
#   supportedDevices=MIDIIN2 (Launchkey Mini MK3 MID,Launchkey Mini MK3 DAW Port

import midi, device, transport, mixer, general, ui, playlist, channels, plugins
from mxr.mirectangle import Rectangle
import pads, knobs, mixerlowpads, sceneup, browse, handlers
import variables as var, constants as cons, drumpads as drum, stepsequencer as step, panvol as pv, scenedown as scdown
import uimessages as uimsg, scenedownlights as downlight, upperpadslights as uplights, initrefresh as initrfsh, padknobmodes as pkm
import upperpadsactions as upact, crlowpads as crlp, transportbuttons as trns
#from cust_gen import vital, pigments3, surge
from cust_gen import *
from fruity_gen import *

import pl.controls as plctrl
import mxr.embdeq
from editors.shortcuts import *
from time import time
#from mxr.levelmon import peakMonitor
apiver4script=23

def OnInit():           # Set up "DAW mode" in the controller after linking the script to the controller. RTFM to know why is this important!
    if general.getVersion() >= apiver4script:
        initrfsh.Initialize()
        cons.startTime = time()
    else:
        print("")
        print ("This script might not be supported in this FL Studio version.")
        print ("Please upgrade to version 20.9.2 (build 2963 for Windows, or MacOS equivalent) or higher."), print("")
        print("Scripting API version needed:", end=" "), print(apiver4script)
        print("Scripting API version installed:", end=" "), print(general.getVersion())
        print("")
        print("Attempting to start anyway...")
        initrfsh.Initialize()
    
    if device.isAssigned():
        device.midiOutMsg(0xBF, 0, 0x09, 0x01)

def OnIdle():
    uplights.Padlights()
    var.currentTime = time()
    #global FOCUS_STATUS
    if ui.getFocused(0):
        var.FOCUS_STATUS = "Mixer"
    elif ui.getFocused(1):
        var.FOCUS_STATUS = "Channel rack"
    elif ui.getFocused(2):
        var.FOCUS_STATUS = "Playlist"
    elif ui.getFocused(3):
        var.FOCUS_STATUS = "Piano roll"
    elif ui.getFocused(4):
        var.FOCUS_STATUS = "Browser"
    elif ui.getFocused(5):
        var.FOCUS_STATUS = "Plugin"
    
### Colors for Scene Down button
    if not var.SHIFT_STATUS:
        downlight.Downbutton()

### Colors for Scene-up button
    sceneup.UpColorsIdle()

### Lower pads colors for Mixer mode!
    mixerlowpads.LowerLights()

### Lower pads colors for Channel rack mode!
    crlp.LowerLights()

### Step-sequencer lights
    step.SeqLights()

### Playlist track mute state
    #plctrl.MuteLights()
    
    ShortLights()
    peakMonitor()

def OnDeInit():         # Gets back to Standalone mode after exiting FL Studio.
    if device.isAssigned():
        device.midiOutMsg(0xBF, 0, 0x73, 0x00)
        device.midiOutMsg(159,0,12,0)
        print("Connection disabled. Back to Standalone mode.")
        print("")



def OnMidiMsg(event):
    sceneup.UpPushed(event.midiId, event.data1, event.data2)
    trns.TrBehavior(event.midiId, event.data1, event.data2)
    browse.Arrowkeys(event.midiId, event.data1, event.data2)
    
    pkm.KnobModes(event.midiId, event.data1, event.data2)
    pkm.PadModes(event.midiId, event.data1, event.data2)
    
    #if  channels.getChannelType(channels.channelNumber()) == 2:
    vital.Knobs(event.midiId, event.data1, event.data2)
    pigments3.Knobs(event.midiId, event.data1, event.data2)
    surge.Knobs(event.midiId, event.data1, event.data2)
    cardinal.Knobs(event.midiId, event.data1, event.data2)
    massive.Knobs(event.midiId, event.data1, event.data2)

    flex.Knobs(event.midiId, event.data1, event.data2)
    sytrus.Knobs(event.midiId, event.data1, event.data2)
    harmor.Knobs(event.midiId, event.data1, event.data2)
    midiout.Knobs(event.midiId, event.data1, event.data2)
    
    plctrl.MuteTracks(event.data1, event.data2)
    

    mxr.embdeq.setMixerEQGain(event.data1, mixer.trackNumber(),0,event.data2)
    
#def OnProgramChange(event):
#    print (str(hex(event.midiId)) + " " + str(event.data1))

def OnNoteOn(padhit):
    if not var.PADSTATUS == "Drum":
        upact.UpperPads(padhit.midiId, padhit.data1, padhit.data2) ### Upper pads behavior
        step.Sequencer(padhit.midiId, padhit.data1, padhit.data2)  ### Step-sequencer in low pads.
    
    if not var.PADSTATUS == "Drum":
        if padhit.midiId == midi.MIDI_NOTEON:            
            if "MIXER_READYFOR" in var.scmodes:
                mxr = mixerlowpads.LowPads (padhit.data1, padhit.data2, var.scmodes.get("MIXER_READYFOR"))
                mxr.LowerPadsControls()

    if not var.PADSTATUS == "Drum":
        crlp.LowerPadsControls(padhit.data1, padhit.data2, var.scmodes.get("CHANRACK_READYFOR"))

    if var.PADSTATUS == "Drum":
        upperpads = drum.DrumData(padhit.data1, padhit.data2, pads.drum_upperpads)
        lowerpads = drum.DrumData(padhit.data1, padhit.data2, pads.drum_lowerpads)
        upperpads.DrumLights()
        lowerpads.DrumLights()
    Shortcuts(padhit.midiId, padhit.data1, padhit.data2)

    padhit.handled = handlers.PadHandler(padhit.midiId, padhit.data1)

def OnControlChange(scene):
    if not var.SHIFT_STATUS:
            for x,y in cons.modes.items():
                if var.SCENE_SEL == x:
                    x = scdown.SceneDown(scene.data1, scene.data2, y)
                    x.Selection()
           
            if scene.data1 == cons.scenedown_DATA1 and scene.data2:
                for x,y in cons.modes.items():
                   uimsg.SceneMsg(x,y)
                        
        ### KNOB BEHAVIOR
    if not var.SHIFT_STATUS:
        if var.KNOBSTATUS != "Custom":  
        ### Knobs behavior in Mixer mode.
            if var.SCENE_SEL == "Mixer":

            ### Panning controls in mixer mode.
                if var.KNOBSTATUS =="Pan":
                    mixermod = pv.PanVol(scene.data1, scene.data2, mixer.trackNumber(), mixer.trackCount(), var.SCENE_SEL, knobs.knobs)
                    mixermod.Pan()
                    
            ### Volume controls in mixer mode.
                elif var.KNOBSTATUS == "Volume":
                    mixermod = pv.PanVol(scene.data1, scene.data2, mixer.trackNumber(), mixer.trackCount(), var.SCENE_SEL, knobs.knobs)
                    mixermod.Vol()
                    
        ### Knobs behavior in Channel rack mode.
            elif var.SCENE_SEL=="Channel rack":               
            ### Panning controls in Channel rack mode.
                if var.KNOBSTATUS =="Pan":
                    channel = pv.PanVol(scene.data1, scene.data2, channels.selectedChannel(), channels.channelCount(), var.SCENE_SEL, knobs.knobs)
                    channel.Pan()         

            ### Volume controls in Channel rack mode.
                if var.KNOBSTATUS =="Volume":
                    channel = pv.PanVol(scene.data1, scene.data2, channels.selectedChannel(), channels.channelCount(), var.SCENE_SEL, knobs.knobs)
                    channel.Vol()
      
    scene.handled = handlers.SceneHandler(scene.midiId, scene.data1)
    sceneup.UpBehavior(scene.midiId, scene.data1, scene.data2)
    sceneup.UpColorsPush(scene.midiId, scene.data1)

    if var.SCENE_SEL == "Mixer":
        if scene.data1 and scene.data2:
            Rectangle()