# Novation Launchkey Mini MK3 integration script for FL Studio

This script aims to integrate [Novation Launchkey Mini MK3](https://novationmusic.com/es/keys/launchkey-mini) using FL Studio [MIDI Scripting Device API](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm) based in Python. It is intended to provide the user __macro-driven functionality__ reducing the need to interact with a computer keyboard.
Despite this, the script tries to preserve the _performance_ capabilities that the controller provides, letting the user to link parameters to the knobs.

This script should be compatible with the latest FL Studio version, for both Windows and MacOS (and might even work with Linux/Wine).

![Launchkey Mini MK3 front image](Launchkey%20Mini%20MK3.png)

&nbsp;

## Installation

Download the code and copy the _Novation Launchkey Mini MK3_ folder in FL Studio [__User Data Folder__](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/envsettings_files.htm#userdata)/Settings/Hardware.

For Windows, you can copy this address and access it from the File Explorer address bar:
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

![Suggested MIDI settings](Suggested%20MIDI%20settings.png)
