### Scene-down behavior and colors
import constants as cons
import variables as var
class SceneDown():
    def __init__(self, data1, data2, mode):
        self.data1 = data1
        self.data2 = data2
        #self.scene = scene
        self.mode = mode
    
    def Selection(self): ### Set the DOWN pad to Stop, Solo or Mute.
        if self.data1 == cons.scenedown_DATA1:
            if self.data2>0:
                    for x,y in var.scmodes.items():
                        #print (x, y)
                        if x == self.mode:
                            if y == "":
                                var.scmodes.update({self.mode: "Stop"})
                            elif y == "Stop":
                                var.scmodes.update({self.mode: "Solo"})
                            elif y == "Solo":
                                var.scmodes.update({self.mode: "Mute"})
                            elif y == "Mute":
                                var.scmodes.update({self.mode: ""})
                            #print (x,y)
            return 1

    def DownAction(self):
        if self.data1 == cons.scenedown_DATA1:
            if self.data2:
                for x, y in var.scmodes.items():
                    if x == self.mode:
                        if y == "Stop":
                            return "Stop"
                        elif y == "Solo":
                            return "Solo"
                        elif y == "Mute":
                            return "Mute"
                        elif y == "":
                            return ""