# How to use this script

For reference, there's an image of the controller below.

![Launchkey Mini MK3 front image](Launchkey%20Mini%20MK3.png)

&nbsp;

## Introduction

After [installing](README.md#installation) and [configuring](README.md#configuration) the script, your controller should be ready to use.

You'll be greeted with the __Mixer mode__ by default.

&nbsp;

## __Arp__, __Fixed Chord__ and __Transport__ functionality

The Novation Launchkey Mini MK3 controller has two features available through the [Standalone mode](README.md#configuration); the __Arp__ and the __Fixed Chord__.
These functions are not affected by the script, and are available whenever you want. Read the device manual for more information.

The __Transport__ functionality is also available, and can be accessed by pressing the __[Play]__ and __[Record]__ buttons.
About the __[Play]__ button, it will start the song if it's stopped, and stop it if it's playing. If you press __[Shift]__ + __[Play]__ while playback, the song will pause, remembering the pause position. If you press __[Shift]__ + __[Play]__ while paused, the play position will be reset to the beginning of the playback frame.

&nbsp;

## __Basic controls__

The basic controls are available in all modes, and provide access to many functions within FL Studio.  
These controls are accesible by the upper row of pads. Below are the available controls.

1. __Toggle Song/Pattern mode__: The first pad lets you to toggle between the __Song__ and the __pattern mode__. The Song mode is indicated by a green light, and the pattern mode by a orange light.
2. __Toggle metronome__: The second pad lets you toggle the metronome __on__ (orange light) or __off__ (white light).
3. __Toggle start on input__: The third pad lets you toggle the __start on input__ option. When this option is enabled, the song will start playing only if you press a key on your keyboard.
4. __Toggle countdown before recording__: The fourth pad lets you toggle the __countdown before recording__ option. When this option is enabled, the song will start recording after a series of countdown metronome ticks.
5. __Open/focus/close playlist__: The fifth pad lets you open the playlist window, or focus it if it's already open. If the playlist is already focused, pressing this pad will close it.
6. __Open/close channel rack__: The sixth pad lets you open the channel rack window, or close it if it's already open.
7. __Open/close piano roll__: The seventh pad lets you open the piano roll window, or close it if it's already open.
8. __Open/focus/close mixer__: The eighth pad lets you open the mixer window, or focus it if it's already open. If the mixer is already focused, pressing this pad will close it.

&nbsp;

## __Browsing__

The arrow buttons in the controller are meant to work as traditional arrow keys. Depending on the context, you will be able to move different stuff.
You can move through the __browser__ by using the __[Shift]__ + __[Up/Down/Left/Right]__ buttons, and even play samples. Currently, this functionality is available only for the [__Standard layout__](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/browser.htm#Browser_Tab_Menu).

&nbsp;

## __Modes__, __submodes__ and __knobs__

Modes provide contextual controls for the controller. That means that the pads and knobs will have different functions depending on the mode selected.

You can change the mode by pressing the __[>]__ button, which will cycle through the available modes. The current mode is indicated by the color of the button.

Also, the [Stop/Solo/Mute] buttons will cycle through the available submodes for the current mode. For simplicity, this button will be referred as __[SSM]__.

About the __knobs__, they will be used to control parameters of the current mode. Their target parameters can be selected by pressing the __[Shift]__ button and pressing one of the cyan pads. Depending on the context, the knobs will control different parameters.

The __[Shift]__ + __[Custom]__ combination will let you assign any parameter to the knobs, but they are universal and are only 8 in total, independent of the mode selected.

Below is a detailed list of the available modes and submodes.

&nbsp;

### __Mixer mode__

The mixer mode is based on a __frame__ of 8 tracks in the mixer, showed with a red rectangle, which can be moved by __focusing the mixer__ and pressing the __[Shift]__ + __[Left/Right]__.

This mode is indicated by the <span style="color:green">green</span> color in the <span style="color:green">__[>]__</span> button.

<u>Pads in mixer mode</u>

<span style="color:green">__[>] Mixer__</span>: Lets you control options of the mixer.

1. <span style="color:white">__[SSM] Special controls disabled (default)__</span>: Pads will only show the status of the tracks. Arm tracks will be lit in <span style="color:blue">blue</span>, active tracks in <span style="color:green">green</span> and muted tracks in <span style="color:red">red</span>.
2. <span style="color:blue">__[SSM] Arm mixer tracks__</span>: Pads will let you arm-unarm tracks.
3. <span style="color:green">__[SSM] Solo mixer tracks__</span>: Pads will let you solo-unsolo tracks.
4. <span style="color:red">__Mixer (mute)__</span>: Lets you mute-unmute tracks.

<u>Knobs in mixer mode</u>

- __[Shift]__ + __[Volume]__ pad: the knobs will control the volume of each track in the frame.
- __[Shift]__ + __[Pan]__ pad: the knobs will control the pan of each track in the frame.
- __[Shift]__ + __[Device]__ pad: the knobs will control the __embedded parametric EQ__ of the selected track.
    1. Knob 1: low band gain.
    2. Knob 2: mid band gain.
    3. Knob 3: high band gain.
    4. Knob 4: low band frequency.
    5. Knob 5: mid band frequency.
    6. Knob 6: high band frequency.

&nbsp;

### __Channel rack mode__

The channel rack mode is based on a __frame__ of a range between the selected channel and the next 7 channels (if any) in the channel rack (8 tracks in total). You can change the selected channel (and therefore the frame) by pressing __[Shift]__ + __[Up/Down]__.

This mode is indicated by the <span style="color:red">red</span> color in the <span style="color:red">__[>]__</span> button.

<u>Pads in channel rack mode</u>

1. <span style="color:white">__[SSM] Special controls disabled (default)__</span>: Pads will only show the status of the channels. Active tracks will be lit in <span style="color:green">green</span> and muted tracks in <span style="color:red">red</span>.
2. <span style="color:pink">__[SSM] Step-sequencer__</span>: Pads will let you control the step-sequencer of the selected channel. The pads will show the status of the steps (on/off) of the __active frame__. The frame can be moved left and right by pressing pads 8 and 9 (cyan ones).
3. <span style="color:green">__[SSM] Solo channels (default)__</span>: Pads will let you solo-unsolo channels.
4. <span style="color:red">__[SSM] Mute__</span>: Lets you mute-unmute channels.

<u>Knobs in channel rack mode</u>

- __[Shift]__ + __[Volume]__ pad: the knobs will control the volume of each channel in the frame.
- __[Shift]__ + __[Pan]__ pad: the knobs will control the pan of each channel in the frame.
- __[Shift]__ + __[Device]__ pad: the knobs will control __macros and parameters__ for some plugins. The list of supported plugins is [available here](README.md#supported-plugins).

&nbsp;

### __Editor mode__

The editor mode provides more macros for general use. It is indicated by the <span style="color:blue">blue</span> color in the <span style="color:blue">__[>]__</span> button.

<u>Pads in editor mode</u>

1. <span style="color:white">__[SSM] Macro row 1 (default)__</span>: Pads will let you control different macros:
   - <span style="color:blue">__Pad 9__</span>: Contextual menu.
   - <span style="color:yellow">__Pad 10-12__</span>: Cut, copy and paste, respectively.
   - <span style="color:pink">__Pad 13__</span>: Undo/redo (equivalent to pressing Ctrl + Z).
   - <span style="color:orange">__Pad 14__</span>: Undo up (equivalent to pressing Ctrl + Alt + Z).
2. <span style="color:blue">__[SSM] Peak monitor__</span>: cool eyecandy monitor for the selected mixer track.