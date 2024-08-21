### UI Messages
import variables as var
import ui
uimixer = {
    "Stop": "Ready to arm mixer tracks!",
    "Solo": "Ready to solo mixer tracks!",
    "Mute": "Ready to mute mixer tracks!",
    ""    : "Special mixer controls disabled!"
}

uichanrack = {
    "Stop" : "Ready to step-sequence the selected channel! ",
    "Solo" : "Ready to solo channels!",
    "Mute" : "Ready to mute channels!",
    ""     : "Special Channel rack controls disabled"
}

uieditor = {
    "Stop": "Monitoring insert peaks",
    "Solo": "Not implemented (Solo)",
    "Mute": "Not implemented (Mute)",
    "": "Editing mode"
}

def SceneMsg(scenesel, mode):
    if scenesel == var.SCENE_SEL:
        for x,y in var.scmodes.items():
                if x == mode:
                    if scenesel == "Mixer":
                        for a,b in uimixer.items():
                            if y == a:
                                ui.setHintMsg(b)
                    elif scenesel == "Channel rack":
                        for a,b in uichanrack.items():
                            if y == a:
                                ui.setHintMsg(b)
                    elif scenesel == "Editor":
                        for a,b in uieditor.items():
                            if y == a:
                                ui.setHintMsg(b)
