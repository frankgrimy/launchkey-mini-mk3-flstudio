import variables as var
from playlist import getPerformanceModeState

def setPerfMode():
    var.isPerformance = getPerformanceModeState()
