#   name=Novation Launchkey Mini MK3 (by Frank Grimy) v1.4.1
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

from cust_fxctrl import *
import fruity_fxctrl
from fruity_fxctrl import *

#import mxr.embdeq
from editors.shortcuts import *
from time import time
from deinit import QuitFL
from initialize import Startup
from windowfocus import WindowFocus
from sceneup import SceneUpMidi, UpColorsPush, UpColorsIdle
from longPress import Hold
#import plugins


def OnInit():
    Startup.OnInit()

def OnDeInit():
    QuitFL.OnDeInit()


def OnIdle(): # Functionality that runs in the background. This lets the script to give feedback to the user in real time and in context.
    var.currentTime = time() # Sets the current time for the script.
    Hold(0.250) # Detects if the Scene-up button is being held, during 250 milliseconds.
    UpColorsPush()
    uplights.Padlights() # Upper pads + transport lighting.
    WindowFocus() # Detects the focused window in FL Studio.
    
### Colors for Scene Down button
    downlight.Downbutton()

### Colors for Scene-up button
    UpColorsIdle()

### Lower pads colors for Mixer mode!
    mixerlowpads.LowerLights()

### Lower pads colors for Channel rack mode!
    crlp.LowerLights()

### Step-sequencer lights
    step.SeqLights()

### Playlist track mute state
    #plctrl.MuteLights()
    
    ShortLights() # Lights for shortcuts in Editor mode.
    peakMonitor() # Peak meter monitor (Editor mode).

    var.isPlaying = transport.isPlaying() # Detects if FL Studio is playing.


def OnMidiMsg(event): # Functionality to integrate buttons, pads and knobs operations (CC). This data is passed to FL Studio, and it does stuff with it.
    """if event.data2:
        pluginCoords = mixer.getActiveEffectIndex() # This prints the coordinates of the active effect in the mixer (tuple).
        if pluginCoords:
            print(plugins.getParamCount(pluginCoords[0], pluginCoords[1])) # This prints the name of the active effect in the mixer."""
    
    SceneUpMidi(event)
    trns.TrBehavior(event.midiId, event.data1, event.data2) # Transport buttons behavior.
    browse.Arrowkeys(event.midiId, event.data1, event.data2) # Arrow keys behavior (Shift + Arrow buttons).
    
    pkm.KnobModes(event.midiId, event.data1, event.data2) # Knob modes (Shift + Device/Volume/Pan/Custom pads). Defines variable KNOBSTATUS and prints a hint in FL Studio.
    pkm.PadModes(event.midiId, event.data1, event.data2) # Pad modes (Shift + Session/Drum/Custom pads). Defines variable PADSTATUS and prints a hint in FL Studio.
    
    
    # Knob integrations for plugins.
    ## Generators
    ### Third-party plugins 
    for i in ("vital", "pigments3", "surge", "cardinal", "massive", "phaseplant"):
        eval(i).Knobs(event.midiId, event.data1, event.data2)

    ### FL Studio native generator plugins
    for i in ("flex",
              "sytrus",
              "harmor",
              "midiout"):
        eval(i).Knobs(event.midiId, event.data1, event.data2)

    ## Effects
    ### Third-party plugins
    for i in ("pro_l2",
              "khs_gain"):
        eval(i).Knobs(event.midiId, event.data1, event.data2)
    
    ### FL Studio native effect plugins
    for i in ("freq_shifter",
              "love_philter",
              "param_eq2",
              "fruity_limiter",
              "control_surface"):
        if i in dir(fruity_fxctrl):
            eval(i).Knobs(event.midiId, event.data1, event.data2)
    
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
    #sceneup.UpBehavior(scene.midiId, scene.data1, scene.data2) # Up button behavior.
    #sceneup.UpColorsPush(scene.midiId, scene.data1) # Up button colors.

    # Mixer rectangle indicator.
    if var.SCENE_SEL == "Mixer":
        if scene.data1 and scene.data2:
            Rectangle()

def OnRefresh(HW_Dirty_LEDs):
        fxDetect.pluginInfo().OnRefresh() # Sets var.focusedPlugin to the active effect in the mixer, including its coordinates.