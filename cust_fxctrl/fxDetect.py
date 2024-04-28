import variables as var
import plugins, mixer

class pluginInfo():
    def OnRefresh(self):
        pluginCoords = mixer.getActiveEffectIndex()
        if pluginCoords != None:
            var.focusedPlugin[0] = plugins.getPluginName(pluginCoords[0], pluginCoords[1])
            var.focusedPlugin[1] = pluginCoords[0]
            var.focusedPlugin[2] = pluginCoords[1]
        elif pluginCoords == None:
            var.focusedPlugin[0] = ""
            var.focusedPlugin[1] = None
            var.focusedPlugin[2] = None
        #print(var.focusedPlugin) # Debugging purposes. Prints the plugin name and its coordinates in the mixer, to the console.

