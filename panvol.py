### Panning and volume controls for Mixer and Channel Rack scenes.
from specialmath import truncate as trnc
from mixer import setTrackPan, setTrackVolume
from channels import setChannelPan, setChannelVolume
from ui import setHintMsg

class PanVol:
    def __init__(self, data1, data2, pos, count, scenetype, *knobmap):
        self.data1 = data1
        self.data2 = data2
        self.pos = pos
        self.count = count
        self.knobmap = knobmap[0]
        self.scenetype = scenetype
    
    def Pan(self):
        for x, y in self.knobmap.items():
            if self.data1 == self.knobmap[x]:
                if self.scenetype == "Mixer":
                    if self.pos+y-21 < self.count-1:
                        setTrackPan(*(self.pos+y-21, trnc((self.data2*2/127)-1 , 2)))
                        return 1
                    else:
                        if self.pos+y-21 == self.count-1:
                            setHintMsg("You can't pan the Current insert")
                            return 0
                        else:
                            setHintMsg("The insert you're trying to pan doesn't exist!")
                            return 0
                        

                elif self.scenetype == "Channel rack":
                    if self.pos+y-21 < self.count:
                        setChannelPan(*(self.pos+y-21, trnc((self.data2*2/127)-1 , 2)))
                        return 1
                    else:
                        setHintMsg("The channel you're trying to pan doesn't exist!")
                        return 0
    
    def Vol(self):
        for x,y in self.knobmap.items():
            if self.data1 == self.knobmap[x]:
                if self.scenetype == "Mixer":
                    if self.pos+y-21 < self.count-1:
                        setTrackVolume(*(self.pos+y-21, (self.data2/127)*0.8))
                        return 1
                    else:
                        if self.pos+y-21 == self.count-1:
                            setHintMsg("You can't level the Current insert")
                            return 0
                        else: 
                            setHintMsg("The insert you're trying to level doesn't exist!")
                            return 0
                
                elif self.scenetype == "Channel rack":
                    if self.pos+y-21 < self.count:
                        setChannelVolume(*(self.pos+y-21, self.data2*0.78125/127))
                        return 1
                    else:
                        setHintMsg("The channel you're trying to level doesn't exist!")
                        return 0