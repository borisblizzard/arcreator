'''
Created on Sep 11, 2010

the main program module. load the wx libary and runs the application

Classes in this module
-----------------------
RMPY_App - main application class
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



class RMPY_App(wx.App):

    def OnInit(self):
        self.SetupData()
        self.LoadConponentDefaults()
        global MainWindow
        MainWindow = KM.get_component("EditorMainWindow").object
        self.frame = MainWindow(None, wx.ID_ANY, 'RPG Maker PY')
        self.frame.Show(True)
        self.SetTopWindow(self.frame)

        wx.InitAllImageHandlers()

        self.keepGoing = True
        return True

    def SetupData(self):
        config = ConfigParser.ConfigParser()
        path = os.path.join(dirName, "RMPY.cfg")
        config.read(path)
        Kernel.Global.RMPYconfig = config

    def LoadConponentDefaults(self):
        template = Kernel.ConfigLoader.build_from_file(os.path.join(dirName,
                                                      "defaults.ini"))
        template = Kernel.ConfigLoader.build_from_file(os.path.join(dirName,
                                                      "userdefaults.ini"),
                                                      template)
        Kernel.ConfigLoader.load(template)
        Kernel.Global.LoadedComponentDefaultsTemplate = template


if __name__ == '__main__':

    provider = wx.SimpleHelpProvider()
    wx.HelpProvider.Set(provider)

    app = RMPY_App(False)
    app.MainLoop()
