# This snippet creates a class that contains the properties of any desired insert. The class is called Insert.
# The class is called by Insert(track number).property
import mixer

class insertInfo:
    def __init__(self, number):
        self.number = number
        self.name = mixer.getTrackName(number)
        self.volume = mixer.getTrackVolume(number)
        self.pan = mixer.getTrackPan(number)
        self.mute = mixer.isTrackMuted(number)
        self.arm = mixer.isTrackArmed(number)
        self.fxStatus = mixer.isTrackSlotsEnabled(number)