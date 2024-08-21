# Novation Launchkey Mini MK3 integration script for FL Studio

This script aims to integrate [Novation Launchkey Mini MK3](https://novationmusic.com/es/keys/launchkey-mini) using FL Studio [MIDI Scripting Device API](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm) based in Python. It is intended to provide the user __macro-driven functionality__ reducing the need to interact with a computer keyboard.
Despite this, the script tries to preserve the _performance_ capabilities that the controller provides, letting the user to link parameters to the knobs.

This script should be compatible with the latest FL Studio version, for both Windows and MacOS (and might even work with Linux/Wine).

![Launchkey Mini MK3 front image](./Info/Launchkey%20Mini%20MK3.png)

&nbsp;

## Installation

Download the code and copy the _Novation Launchkey Mini MK3_ folder in FL Studio [__User Data Folder__](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/envsettings_files.htm#userdata)/Settings/Hardware.

For Windows, if you haven't modified FL Studio's default User Data Folder, you can copy this address and access it from the File Explorer address bar:
> %USERPROFILE%\Documents\Image-Line\FL Studio\Settings\Hardware

## Configuration

Have in mind that this device __has two MIDI input/output pairs__. One controls the _Standalone (MIDI) mode_ (which lets you to use the keyboard) and the other control the __DAW mode__ (the responsible for the most functions this script offers).
Also, according to your OS and/or other settings, the device naming might differ.

After copying the script, you now have to set up FL Studio.

1. Connect your device to your computer and start FL Studio.
2. Go to FL Studio [MIDI settings](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/envsettings_midi.htm).
3. Configure the ports so each MIDI IN/OUT pairs are set to the same port. Note that in the screenshot below, the DAW mode pair is set to use __MIDI port 10__, while the Standalone mode uses MIDI port 20.
4. Select the DAW MIDI port in the Input list and choose the script ___Novation Launchkey Mini MK3 (by Frank Grimy)___ from the __Controller type__ dropdown list,
5. (Optional) Set the Standalone MIDI device to use the __(generic controller)__. This will let you use the MIDI keyboard as usual.
6. (Optional) Enable _Send master sync_ option for the DAW output device. This makes FL Studio send a MIDI clock signal to the controller, that syncs its lighting to the BPM of the current project.

If you did it all good, the device pads might change colors and you'll be ready to enjoy the script.

For reference, there's a screenshot below that resumes the settings, so you can compare with.

![Suggested MIDI settings](./Info/Suggested%20MIDI%20settings.png)

## Functions manual

Please read the [Manual](./Info/MANUAL.md).

## Supported plugins

### Generators

Image-Line plugins:

- [FLEX](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/FLEX.htm)
- [Harmor](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Harmor.htm)
- [Sytrus](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Sytrus.htm)
- [__MIDI Out__](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/MIDI%20Out.htm)

Third-party plugins:

- [Cardinal](https://github.com/DISTRHO/Cardinal)
- [Massive](https://www.native-instruments.com/en/products/komplete/synths/massive/)
- [Pigments 3](https://www.arturia.com/products/software-instruments/pigments/overview)
- [Surge XT](https://surge-synthesizer.github.io/)
- [Vital](https://vital.audio/)

### Effects

Image-Line plugins:

- [Control Surface](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Control%20Surface.htm): only the first 8 parameters per instance
- [Frequency Shifter](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Frequency%20Shifter.htm)
- [Fruity Limiter](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Fruity%20Limiter.htm)
- [Fruity Love Philter](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Fruity%20Love%20Philter.htm): only X-Y modulation
- [Fruity Parametric EQ 2](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Fruity%20Parametric%20EQ%202.htm): by default controls the seven bands cutoff and global gain. Hold [SHIFT] to control the bandwidth.

Third-party plugins:

- [Kilohearts Gain](https://kilohearts.com/products/gain)
- [Fabfilter Pro-L 2](https://www.fabfilter.com/products/pro-l-2-limiter-plug-in)
