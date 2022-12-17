import midi
import device
import colors

class DrumData:
    def __init__(self, DATA1, DATA2, *drumpad_map):
        self.DATA1 = DATA1
        self.DATA2 = DATA2
        self.drumpad_map = drumpad_map[0]

    def DrumLights(self):
        
        for x, y in self.drumpad_map.items():
            if self.DATA1 == self.drumpad_map[x]:
                if self.DATA2:
                    device.midiOutMsg(0x99, 0, y, colors.ORANGE1)
                else:
                    device.midiOutMsg(0x99, 0, y, colors.EMPTYWHITE)

