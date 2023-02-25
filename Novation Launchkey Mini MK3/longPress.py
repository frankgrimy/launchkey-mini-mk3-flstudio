import variables as var
from time import time
from sceneup import UpBehavior

def Hold(timeDelta):
    if var.pushTime:
        var.holdTime = time() - var.pushTime
        if var.holdTime > timeDelta:
            UpBehavior(1)
            var.pushTime = 0
        elif not var.isPushed:
            UpBehavior(0)
            var.pushTime = 0

        
    

    
    #     elif var.holdTime <= timeDelta:
    #         if var.isPushed:
    #             pass
    

        # if var.holdTime > timeDelta and var.isPushed:
        #     if not var.isLongPress:
        #         var.isLongPress = 1
        #     if var.isLongPress:
        #         print("Long press detected")
        #         UpBehavior(1)
        #         var.pushTime = 0
        #         var.isLongPress = 0
        # elif var.holdTime <= timeDelta and var.isPushed:
        #     print ("Short press detected")
        #     UpBehavior(0)
        #     var.pushTime = 0
        #     var.isLongPress = 0 
        # elif var.holdTime <= timeDelta and not var.isPushed:
        #     var.pushTime = 0
        #     var.isLongPress = 0

"""var.pushtime: el instante en que se pulsó el botón
var.isPushed: si el botón está pulsado o no
var.holdTime: el tiempo que se ha mantenido pulsado el botón
var.isLongPress: si el botón se ha mantenido pulsado más de timeDelta segundos o no"""