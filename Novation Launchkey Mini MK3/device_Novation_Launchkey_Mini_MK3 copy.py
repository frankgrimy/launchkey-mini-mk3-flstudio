#   name=Novation Launchkey Mini MK3 (by Frank Grimy) v1.4.0
#   url=https://forum.image-line.com/viewtopic.php?f=1994&t=260133
#   supportedDevices=MIDIIN2 (Launchkey Mini MK3 MID,Launchkey Mini MK3 DAW Port

# Import list
import midi, mixer, ui, channels
from mxr.mirectangle import Rectangle
import pads, knobs, mixerlowpads, sceneup, browse, handlers
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
apiver4script=23 # Scripting API version compatible with this script.

def OnInit():
    Startup.OnInit()

def OnDeInit():
    QuitFL.OnDeInit()


def OnIdle(): # Functionality that runs in the background. This lets the script to give feedback to the user in real time and in context.
    uplights.Padlights() # Upper pads + transport lighting.
    var.currentTime = time() # Sets the current time for the script.
    WindowFocus() # Detects the focused window in FL Studio.
    
### Colors for Scene Down button
    downlight.Downbutton()

### Colors for Scene-up button
    sceneup.UpColorsIdle()

### Lower pads colors for Mixer mode!
    mixerlowpads.LowerLights()

### Lower pads colors for Channel rack mode!
    crlp.LowerLights()

### Step-sequencer lights
    #step.SeqLights()

### Playlist track mute state
    #plctrl.MuteLights()
    
    ShortLights() # Lights for shortcuts in Editor mode.
    peakMonitor() # Peak meter monitor (Editor mode).


def OnMidiMsg(event): # Functionality to integrate buttons, pads and knobs operations (CC). This data is passed to FL Studio, and it does stuff with it.
    sceneup.UpPushed(event.midiId, event.data1, event.data2) # Scene-up button behavior.
    trns.TrBehavior(event.midiId, event.data1, event.data2) # Transport buttons behavior.
    browse.Arrowkeys(event.midiId, event.data1, event.data2) # Arrow keys behavior (Shift + Arrow buttons).
    
    pkm.KnobModes(event.midiId, event.data1, event.data2) # Knob modes (Shift + Device/Volume/Pan/Custom pads). Defines variable KNOBSTATUS and prints a hint in FL Studio.
    pkm.PadModes(event.midiId, event.data1, event.data2) # Pad modes (Shift + Session/Drum/Custom pads). Defines variable PADSTATUS and prints a hint in FL Studio.
    
    
    # Knob integrations for plugins.
    ## Generators
    ### Third-party plugins 
    vital.Knobs(event.midiId, event.data1, event.data2) 
    pigments3.Knobs(event.midiId, event.data1, event.data2)
    surge.Knobs(event.midiId, event.data1, event.data2)
    cardinal.Knobs(event.midiId, event.data1, event.data2)
    massive.Knobs(event.midiId, event.data1, event.data2)

    ### FL Studio native plugins
    flex.Knobs(event.midiId, event.data1, event.data2)
    sytrus.Knobs(event.midiId, event.data1, event.data2)
    harmor.Knobs(event.midiId, event.data1, event.data2)
    midiout.Knobs(event.midiId, event.data1, event.data2)
    
    mxr.embdeq.setMixerEQGain(event.data1, mixer.trackNumber(),0,event.data2) # Mixer embedded EQ controls.
    
    #plctrl.MuteTracks(event.data1, event.data2) # Non-functional playlist mute tracks.
    step.SeqLights()


def OnNoteOn(padhit): # Functionality to integrate pads operations (Note On). This data is passed to FL Studio, and it does stuff with it.
    
    if not var.PADSTATUS == "Drum": # If the pad mode is not "Drum", then the upper pads will provide macros and shortcuts.
        upact.UpperPads(padhit.midiId, padhit.data1, padhit.data2) ### Upper pads behavior
        step.Sequencer(padhit.midiId, padhit.data1, padhit.data2)  ### Step-sequencer in low pads.
        
        if padhit.midiId == midi.MIDI_NOTEON:            
            if "MIXER_READYFOR" in var.scmodes:
                mxr = mixerlowpads.LowPads (padhit.data1, padhit.data2, var.scmodes.get("MIXER_READYFOR"))
                mxr.LowerPadsControls() # Mixer mode lower pads behavior.

        crlp.LowerPadsControls(padhit.data1, padhit.data2, var.scmodes.get("CHANRACK_READYFOR")) # Channel rack mode lower pads behavior.

    # Pads in Drum mode.
    if var.PADSTATUS == "Drum":
        drumpads = drum.DrumData(padhit.data1, padhit.data2, pads.drum_pads)
        drumpads.DrumLights()
    
    Shortcuts(padhit.midiId, padhit.data1, padhit.data2) # Integrate messages to provide shortcuts in Editor mode.
    #velocityCurves(padhit.midiId, padhit.data1, padhit.data2)

    padhit.handled = handlers.PadHandler(padhit.midiId, padhit.data1) # If a pad is integrated, then FL Studio will show a yellow icon.

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
      
    scene.handled = handlers.SceneHandler(scene.midiId, scene.data1) # If a CC is integrated, then FL Studio will show a yellow icon.
    sceneup.UpBehavior(scene.midiId, scene.data1, scene.data2) # Up button behavior.
    sceneup.UpColorsPush(scene.midiId, scene.data1) # Up button colors.

    # Mixer rectangle indicator.
    if var.SCENE_SEL == "Mixer":
        if scene.data1 and scene.data2:
            Rectangle()
