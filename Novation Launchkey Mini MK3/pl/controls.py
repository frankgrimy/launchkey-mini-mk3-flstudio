import colors, pads, variables as var
import device, ui, playlist

mutemap = {}
notmuted = True
def MuteTracks(data1, data2): # Toggle tracks mute state.
    if data1 == pads.ses_lowerpads["sespad9_DATA1"] and data2 > 0:
        if var.SCENE_SEL == "Playlist":
            if not var.scmodes.get("PLAYLIST_READYFOR") == "Stop":
                if var.scmodes.get("PLAYLIST_READYFOR") == "Mute":
                    global notmuted
                    if notmuted == False:
                        notmuted = True
                    elif notmuted:
                        notmuted = False
                    
                    if notmuted:
                        device.midiOutMsg(0x90, 0, pads.sespad9_DATA1, colors.GREEN1)
                    elif not notmuted:
                        device.midiOutMsg(0x90, 0, pads.sespad9_DATA1, colors.PLMUTE)

                """n = 1                   
                while n <= playlist.trackCount():
                #for x in range (1, playlist.trackCount()):
                    #mutemap[x] = bool(playlist.isTrackMuted(x))
                    while not playlist.isTrackMuteLock(x):
                #for x in range (1, 11):
                    #if not playlist.isTrackMuteLock(x):
                        if playlist.isTrackMuted(x) == notmuted:
                        #if mutemap.get(x) == bool(notmuted):
                            print("A")
                            #playlist.muteTrack(x)
                """
                n = 1
                while n < playlist.trackCount():
                    if playlist.isTrackMuteLock(n):
                    #if True:
                        if playlist.isTrackMuted(n) == bool(notmuted):
                            playlist.soloTrack(n)
                            playlist.muteTrack(n)
                            print(n)
                            print(notmuted)
                        break
                    else:
                        playlist.soloTrack(1)
                        playlist.muteTrack(1)
                    n += 1
