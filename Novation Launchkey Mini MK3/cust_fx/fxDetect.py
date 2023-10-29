import variables as var
import plugins, mixer

class pluginInfo():
    def OnRefresh(self):
        pluginCoords = mixer.getActiveEffectIndex()
        if pluginCoords != None:
            """print(plugins.getPluginName(pluginCoords[0], pluginCoords[1]) + " (" + \
                  (plugins.getParamName(0, pluginCoords[0], pluginCoords[1])) + \
                    ", Value: " + str(plugins.getParamValueString(0, pluginCoords[0], pluginCoords[1])) + ")" )"""
            var.focusedPlugin[0] = plugins.getPluginName(pluginCoords[0], pluginCoords[1])
            var.focusedPlugin[1] = pluginCoords[0]
            var.focusedPlugin[2] = pluginCoords[1]
            print(var.focusedPlugin)
        elif pluginCoords == None:
            var.focusedPlugin[0] = ""
            var.focusedPlugin[1] = None
            var.focusedPlugin[2] = None
            print(var.focusedPlugin)

