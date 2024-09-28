import pads
from device import midiOutMsg
from playlist import liveDisplayZone, getLiveBlockColor, getLiveBlockStatus
from variables import perfPosition, perfPadsFour, isPlaying
from colPalette import *

# convertColor(getLiveBlockColor(track,pad-1))
#colPalette.convertColor(playlist.getLiveBlockColor(perfPosition[0]+1,perfPosition[1]))

def setLights():
    if not perfPadsFour:
        for i in pads.ses_upperpads.values():
            #print(getLiveBlockStatus(perfPosition[1], perfPosition[0]+i-96, 1))
            blockStatus = getLiveBlockStatus(perfPosition[1], perfPosition[0]+i-96, 1)
            if blockStatus:
                if blockStatus == 3:
                    midiOutMsg(0x92,0,i,convertColor(getLiveBlockColor(perfPosition[1], perfPosition[0]+i-96)))
                else:
                    midiOutMsg(0x90,0,i,convertColor(getLiveBlockColor(perfPosition[1], perfPosition[0]+i-96)))
            else:
                midiOutMsg(0x90,0,i, 0)
        for i in pads.ses_lowerpads.values():
            if getLiveBlockStatus(perfPosition[1]+1, perfPosition[0]+i-112, 1) > 0:
                midiOutMsg(0x90,0,i,convertColor(getLiveBlockColor(perfPosition[1]+1, perfPosition[0]+i-112)))
            else:
                midiOutMsg(0x90,0,i, 0)
    else:
        for i in range(96, 100):
            blockStatus = getLiveBlockStatus(perfPosition[1], perfPosition[0]+i-96, 0)
            if blockStatus:
                if blockStatus in (5,7):
                    midiOutMsg(0x92,0,i,convertColor(getLiveBlockColor(perfPosition[1], perfPosition[0]+i-96)))
                else:
                    midiOutMsg(0x90,0,i,convertColor(getLiveBlockColor(perfPosition[1], perfPosition[0]+i-96)))
            else:
                midiOutMsg(0x90,0,i, 0)
        
        
        for i in range(100, 104):
            blockStatus = getLiveBlockStatus(perfPosition[1]+2, perfPosition[0]+i-100, 0)
            if blockStatus:
                if blockStatus in (5,7):
                    midiOutMsg(0x92,0,i,convertColor(getLiveBlockColor(perfPosition[1]+2, perfPosition[0]+i-100)))
                else:
                    midiOutMsg(0x90,0,i,convertColor(getLiveBlockColor(perfPosition[1]+2, perfPosition[0]+i-100)))
            else:
                midiOutMsg(0x90,0,i, 0)
        
        
        for i in range(112, 116):
            blockStatus = getLiveBlockStatus(perfPosition[1]+1, perfPosition[0]+i-112, 0)
            if blockStatus:
                if blockStatus in (5,7):
                    midiOutMsg(0x92,0,i,convertColor(getLiveBlockColor(perfPosition[1]+1, perfPosition[0]+i-112)))
                else:
                    midiOutMsg(0x90,0,i,convertColor(getLiveBlockColor(perfPosition[1]+1, perfPosition[0]+i-112)))
            else:
                midiOutMsg(0x90,0,i, 0)
        
        
        for i in range(116, 120):
            blockStatus = getLiveBlockStatus(perfPosition[1]+1, perfPosition[0]+i-112, 0)
            if blockStatus:
                if blockStatus in (5,7):
                    midiOutMsg(0x92,0,i,convertColor(getLiveBlockColor(perfPosition[1]+3, perfPosition[0]+i-116)))
                else:
                    midiOutMsg(0x90,0,i,convertColor(getLiveBlockColor(perfPosition[1]+3, perfPosition[0]+i-116)))
            else:
                midiOutMsg(0x90,0,i, 0)


def liveZone(isPerma):
    if not perfPadsFour:
        if isPerma:
            liveDisplayZone(perfPosition[0],perfPosition[1], perfPosition[0]+8, perfPosition[1]+2)
        else:
            liveDisplayZone(perfPosition[0],perfPosition[1], perfPosition[0]+8, perfPosition[1]+2, 1000)
    else:
        if isPerma:
            liveDisplayZone(perfPosition[0],perfPosition[1], perfPosition[0]+4, perfPosition[1]+4)
        else:
            liveDisplayZone(perfPosition[0],perfPosition[1], perfPosition[0]+4, perfPosition[1]+4, 1000)