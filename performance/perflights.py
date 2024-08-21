import pads
from device import midiOutMsg
import colors
from playlist import liveDisplayZone, getLiveBlockColor, getLiveBlockStatus
from variables import perfPosition, perfPadsFour
from colPalette import *

# convertColor(getLiveBlockColor(track,pad-1))
#colPalette.convertColor(playlist.getLiveBlockColor(perfPosition[0]+1,perfPosition[1]))

def setLights():
    #print(perfPosition)
    #midiOutMsg(0x90,0,96 ,colors.ORANGE1)
    if not perfPadsFour:
        for i in pads.ses_upperpads.values():
            #print(getLiveBlockStatus(perfPosition[1], perfPosition[0]+i-96, 1))
            #print()
            if getLiveBlockStatus(perfPosition[1], perfPosition[0]+i-96, 1) > 0:
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
            if getLiveBlockStatus(perfPosition[1], perfPosition[0]+i-96, 1) > 0:
                midiOutMsg(0x90,0,i-96,convertColor(getLiveBlockColor(perfPosition[1], perfPosition[0]+i-96)))
            else:
                midiOutMsg(0x90,0,i-96, 0)
        for i in range(100, 105):
            if getLiveBlockStatus(perfPosition[1]+2, perfPosition[0]+i-100, 1) > 0:
                midiOutMsg(0x90,0,i-96,convertColor(getLiveBlockColor(perfPosition[1]+2, perfPosition[0]+i-100)))
            else:
                midiOutMsg(0x90,0,i-96, 0)
        for i in range(112, 116):
            if getLiveBlockStatus(perfPosition[1]+1, perfPosition[0]+i-112, 1) > 0:
                midiOutMsg(0x90,0,i-112,convertColor(getLiveBlockColor(perfPosition[1]+1, perfPosition[0]+i-112)))
            else:
                midiOutMsg(0x90,0,i-112, 0)
        for i in range(116, 120):
            if getLiveBlockStatus(perfPosition[1]+3, perfPosition[0]+i-112, 1) > 0:
                midiOutMsg(0x90,0,i-112,convertColor(getLiveBlockColor(perfPosition[1]+3, perfPosition[0]+i-112)))
            else:
                midiOutMsg(0x90,0,i-112, 0)

def liveZone(isPerma):
    if isPerma:
        liveDisplayZone(perfPosition[0],perfPosition[1], perfPosition[0]+8, perfPosition[1]+2)
    else:
        liveDisplayZone(perfPosition[0],perfPosition[1], perfPosition[0]+8, perfPosition[1]+2, 1000)