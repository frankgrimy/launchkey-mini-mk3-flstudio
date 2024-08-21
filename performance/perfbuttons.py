import device
import playlist
import pads
import variables as var #perfPosition, SHIFT_STATUS
from performance.perflights import liveZone
import colors
import colPalette as col

def trigger(padhit):
  if padhit.data2: print(f"Pad {padhit.data1} pressed")

  if not var.perfPadsFour:
    if padhit.data2:
      for i in pads.ses_upperpads.values():
        if padhit.data1 == i:
          # playlist.triggerLiveClip(track,pad-1,2)
          playlist.triggerLiveClip(var.perfPosition[1],i+var.perfPosition[0]-96,2)
          device.midiOutMsg(0x90,0,i, colors.ORANGE1)
      for i in pads.ses_lowerpads.values():
        if padhit.data1 == i:
          playlist.triggerLiveClip(var.perfPosition[1]+1,i+var.perfPosition[0]-112,2)
          device.midiOutMsg(0x90,0,i, colors.ORANGE1)
    elif not padhit.data2:
      for i in pads.ses_upperpads.values():
        if padhit.data1 == i:
          playlist.triggerLiveClip(var.perfPosition[1],i+var.perfPosition[0]-96,0)
          # Check if there is a clip in the selected pad and then color it if it is.
          if playlist.getLiveBlockStatus(var.perfPosition[1], var.perfPosition[0]+i-96, 1) > 0:
            device.midiOutMsg(0x90,0,i, col.perfColorNumber(var.perfPosition[1], var.perfPosition[0]+i-96))
          else:
            device.midiOutMsg(0x90,0,i, 0)
      for i in pads.ses_lowerpads.values():
        if padhit.data1 == i:
          playlist.triggerLiveClip(var.perfPosition[1]+1,i+var.perfPosition[0]-112,0)
          # Check if there is a clip in the selected pad and then color it if it is.
          if playlist.getLiveBlockStatus(var.perfPosition[1]+1, var.perfPosition[0]+i-112, 1) > 0:
            device.midiOutMsg(0x90,0,i, col.perfColorNumber(var.perfPosition[1]+1, var.perfPosition[0]+i-112))
          else:
            device.midiOutMsg(0x90,0,i, 0)
  else:
    if padhit.data2:
      for i in range(96, 100):
        if padhit.data1 == i:
          playlist.triggerLiveClip(var.perfPosition[1],i+var.perfPosition[0]-96,2)
          device.midiOutMsg(0x90,0,i-96, colors.ORANGE1)
      for i in range(100, 105):
        if padhit.data1 == i:
          playlist.triggerLiveClip(var.perfPosition[1]+2,i+var.perfPosition[0]-100,2)
          device.midiOutMsg(0x90,0,i-96, colors.ORANGE1)
      for i in range(112, 116):
        if padhit.data1 == i:
          playlist.triggerLiveClip(var.perfPosition[1]+1,i+var.perfPosition[0]-112,2)
          device.midiOutMsg(0x90,0,i-112, colors.ORANGE1)
      for i in range(116, 120):
        if padhit.data1 == i:
          playlist.triggerLiveClip(var.perfPosition[1]+3,i+var.perfPosition[0]-112,2)
          device.midiOutMsg(0x90,0,i-112, colors.ORANGE1)

      


  padhit.handled = True

def displayPos(event):
  if event.midiId == 176:
    #if var.SHIFT_STATUS:
      if event.data1 == 104:
        event.handled = True
        if event.data2:
          if var.perfPosition[1] > 1: # Limit the movement to the top
            var.perfPosition[1] -= 1 # Go up
        
      elif event.data1 == 105:
        event.handled = True
        if event.data2:
          var.perfPosition[1] += 1 # Go down
      
      elif event.data1 == 103:
        event.handled = True
        if event.data2:
          if var.perfPosition[0] > 0: # Limit the movement to the left
            var.perfPosition[0] -= 8

      elif event.data1 == 102:  # Go right
        event.handled = True
        if event.data2:
          var.perfPosition[0] += 8
      liveZone(0) # Performance mode position highlight.
  