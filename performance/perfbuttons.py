import device
import playlist
import pads
import variables as var #perfPosition, SHIFT_STATUS
from performance.perflights import liveZone, setLights
import colors
import colPalette as col

def trigger(padhit):
  #if padhit.data2: print(f"Pad {padhit.data1} pressed")

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
    for i in range(96, 100):
      if padhit.data1 == i:
        playTrack(padhit.data2, var.perfPosition[1], var.perfPosition[0]+i-96, i)
        # if padhit.data2:          
        #   playTrack(var.perfPosition[1], var.perfPosition[0]+i-96)
        #   device.midiOutMsg(0x90,0,i, colors.ORANGE1)
        # else:
        #     setLights()
    
    for i in range(100, 104):
      if padhit.data1 == i:
        playTrack(padhit.data2, var.perfPosition[1]+2, var.perfPosition[0]+i-100, i)
    
    for i in range(112, 116):
      if padhit.data1 == i:
        playTrack(padhit.data2, var.perfPosition[1]+1, var.perfPosition[0]+i-112, i)
    
    for i in range(116, 120):
      if padhit.data1 == i:
        playTrack(padhit.data2, var.perfPosition[1]+3, var.perfPosition[0]+i-116, i)

    # for i in range(100, 105):
    #   if padhit.data1 == i:
    #     if padhit.data2:
    #       #print(playlist.getLiveBlockStatus(var.perfPosition[1]+2, var.perfPosition[0]+i-100,0))
          
    #       playTrack(var.perfPosition[1]+2, var.perfPosition[0]+i-100)
    #       #playlist.triggerLiveClip(var.perfPosition[1]+2,i+var.perfPosition[0]-100,2)
    #       device.midiOutMsg(0x90,0,i, colors.ORANGE1)
    #     else:
    #         setLights()
    # for i in range(112, 116):
    #   if padhit.data1 == i:
    #     if padhit.data2:
    #       #print(playlist.getLiveBlockStatus(var.perfPosition[1]+1, var.perfPosition[0]+i-112,0))
          
    #       playTrack(var.perfPosition[1]+1, var.perfPosition[0]+i-112)
    #       #playlist.triggerLiveClip(var.perfPosition[1]+1,i+var.perfPosition[0]-112,2)
    #       device.midiOutMsg(0x90,0,i, colors.ORANGE1)
    #     else:
    #         setLights()
    # for i in range(116, 120):
    #   if padhit.data1 == i:
    #     if padhit.data2:
    #       #print(playlist.getLiveBlockStatus(var.perfPosition[1]+3, var.perfPosition[0]+i-116,0))
          
    #       playTrack(var.perfPosition[1]+3, var.perfPosition[0]+i-116)
    #       #playlist.triggerLiveClip(var.perfPosition[1]+3,i+var.perfPosition[0]-116,2)
    #       device.midiOutMsg(0x90,0,i, colors.ORANGE1)
    #     else:
    #         setLights()
  padhit.handled = True

def playTrack(data2,track, pad, contPad): # Play the selected track and pad, based on its conditions.
  trackLoop = playlist.getLiveLoopMode(track) # Get the loop mode of the selected track (row).
  #0: Stay
  #1: One Shot
  #2: March and warp
  #3: March and stay
  #4: March and stop
  #5: Random
  #6: ExRandom (avoid previous)

  blockStatus = playlist.getLiveBlockStatus(track, pad, 0) # Get the status of the selected pad.
  #0: Empty
  #1: Filled
  #2: Scheduled
  #3: Playing
  #print(f"Block status: {blockStatus}")

  pressMode = playlist.getLiveTriggerMode(track) # Press/trigger mode of the selected track.
  #0: Retrigger
  #1: Hold and stop
  #2: Hold and motion
  #3: Latch
  print(f"Track loop mode: {trackLoop}    " + f"Block status: {blockStatus}    "+ f"Press mode: {pressMode}")
  
  if trackLoop == 0: # Stay
    if pressMode == 1: # Hold and stop
      #if blockStatus:
        if data2:
          playlist.triggerLiveClip(track, pad, 2)
          #device.midiOutMsg(0x90,0,contPad, colors.ORANGE1)
        else:
          playlist.triggerLiveClip(track, -1, 2)
          #device.midiOutMsg(0x90,0,contPad, 0)

  elif trackLoop == 1: # One Shot
    if data2:
      if blockStatus:
          playlist.triggerLiveClip(track, pad, 2)
          device.midiOutMsg(0x90,0,contPad, colors.ORANGE1)
    #else:
    #  setLights()
  
  elif trackLoop == 2: # March and warp
    if data2:
      if blockStatus:
          playlist.triggerLiveClip(track, pad, 2)
          device.midiOutMsg(0x90,0,contPad, colors.ORANGE1)
    #else:
    #  setLights()
  



def displayPos(event):
  if not var.perfPadsFour:
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
        liveZone(1) # Performance mode position highlight.
  
  else:
    if event.midiId == 176:
      #if var.SHIFT_STATUS:
        if event.data1 == 104:
          event.handled = True
          if event.data2:
            if var.perfPosition[1] > 4: # Limit the movement to the top
              var.perfPosition[1] -= 4
            
        elif event.data1 == 105:
          event.handled = True
          if event.data2:
            var.perfPosition[1] += 4 # Go down
          
        elif event.data1 == 103:
          event.handled = True
          if event.data2:
            if var.perfPosition[0] > 3: # Limit the movement to the left
              var.perfPosition[0] -= 4
              
        elif event.data1 == 102:  # Go right
          event.handled = True
          if event.data2:
            var.perfPosition[0] += 4
        liveZone(1)