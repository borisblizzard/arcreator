'''
Created on Sep 11, 2010

the main program module. load the wx libary and runs the application

Classes in this module
-----------------------
ARC_App - main application class
'''
import os
import sys

import ConfigParser

import wx
try:
    dirName = os.path.dirname(os.path.abspath(__file__))
except:
    dirName = os.path.dirname(os.path.abspath(sys.argv[0]))
sys.path.append(os.path.split(dirName)[0])

import Kernel
from Kernel import Manager as KM
import Core


class ARC_App(wx.App):

    def OnInit(self):
        self.SetAppName("ARCed")
        self.SetupData()
        self.LoadConponentDefaults()
        global MainWindow
        MainWindow = KM.get_component("EditorMainWindow").object
        self.frame = MainWindow(None, wx.ID_ANY, 'ARCed')
        self.frame.Show(True)
        self.SetTopWindow(self.frame)

        wx.InitAllImageHandlers()

        self.keepGoing = True
        return True

    def SetupData(self):
        config = ConfigParser.ConfigParser()
        path = os.path.join(dirName, "ARC.cfg")
        config.read(path)
        Kernel.GlobalObjects.set_value("ARCconfig", config)
        
    def LoadPlugins(self):
        local_path  = Kernel.GlobalObjects.get_value("Program_Dir")
        plugin_path = os.path.join(local_path, "plugins")
        if not os.path.exists(plugin_path) and not os.path.isdir(plugin_path):
            os.mkdir(plugin_path)
        names = os.listdir(plugin_path)
        for name in names:
            try:
                if os.path.exists(name):
                    if os.path.isdir(name):
                        if os.path.exists(os.path.join(name, "__init__.py")) and not os.path.isdir(os.path.join(name, "__init__.py")):
                            execfile(os.path.join(name, "__init__.py"), globals())
                    else:
                        execfile(os.path.join(name, "__init__.py"), globals())
            except Exception:
                self.HandelErrorLoadingPlugin(name, plugin_path)
            
    def HandelErrorLoadingPlugin(self, name, plugin_path):
        pass

    def LoadConponentDefaults(self):
        template = Kernel.ConfigLoader.build_from_file(os.path.join(dirName,
                                                      "defaults.ini"))
        template = Kernel.ConfigLoader.build_from_file(os.path.join(dirName,
                                                      "userdefaults.ini"),
                                                      template)
        Kernel.ConfigLoader.load(template)
        Kernel.GlobalObjects.set_value("LoadedComponentDefaultsTemplate", template)


if __name__ == '__main__':

    provider = wx.SimpleHelpProvider()
    wx.HelpProvider.Set(provider)

    
    redirect = True
    
    app = ARC_App(redirect)
    #dlg = wx.MessageDialog(None, "test", "test2",
    #                               style=wx.OK | wx.CENTRE
    #                               | wx.ICON_EXCLAMATION)
    #dlg.ShowModal()
    app.MainLoop()
