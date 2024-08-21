from ui import getFocused
import variables as var

def WindowFocus():
    if getFocused(0):
        var.FOCUS_STATUS = "Mixer"
    elif getFocused(1):
        var.FOCUS_STATUS = "Channel rack"
    elif getFocused(2):
        var.FOCUS_STATUS = "Playlist"
    elif getFocused(3):
        var.FOCUS_STATUS = "Piano roll"
    elif getFocused(4):
        var.FOCUS_STATUS = "Browser"
    elif getFocused(5):
        var.FOCUS_STATUS = "Plugin"