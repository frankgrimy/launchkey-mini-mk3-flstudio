import mixer, ui, variables as var

def Rectangle(): # Display rectangle on mixer.
    mxr = mixer.trackNumber() 
    count = mixer.trackCount() 
    if var.FOCUS_STATUS == "Mixer":
        if mxr <= count - 9:
            ui.miDisplayRect(mxr, mxr+7, 500)
        else:
            if mxr < 126:
                ui.miDisplayRect(mxr, count-2, 500)
