import os
import sys
import math

import wx
from wx import glcanvas


import pyglet
from pyglet import gl

import rabbyt

import numpy

from Boot import WelderImport

Kernel = WelderImport('Kernel')
KM = Kernel.Manager

if hasattr(sys, 'frozen'):
    dirName = sys.executable
else:
    try:
        dirName = os.path.dirname(os.path.abspath(__file__))
    except:
        dirName = os.path.dirname(os.path.abspath(sys.argv[0]))

if not os.path.isdir(dirName):
    LOCAL_PATH = os.path.split(dirName)[0]
else:
    LOCAL_PATH = dirName


if __name__ == '__main__':

    app = wx.App(redirect=False)

    if Kernel.GlobalObjects.has_key("Program_Dir"):
        Kernel.GlobalObjects.set_value("Program_Dir", LOCAL_PATH)
    else:
        Kernel.GlobalObjects.request_new_key("Program_Dir", "CORE", LOCAL_PATH)

    print "[BOOT] Programming Running in %s" % dirName
    print "[BOOT] LOCAL PATH: %s" % LOCAL_PATH
    print "[BOOT] CONFIG PATH: %s" % Kernel.GetConfigFolder()

    import Boot
    from Boot import WelderImport
    Boot.ConfigManager.LoadConfig()

    Core = WelderImport('Core')
    Core.late_bind()

    EventPanel = Core.EventEditor.EventPanel.EventPanel

    class TestFrame(wx.Frame):

        def __init__(self, parent, id, title, pos=wx.DefaultPosition,
                     size=wx.Size(800, 800), style=wx.DEFAULT_FRAME_STYLE,
                     name='frame'):
            super(TestFrame, self).__init__(parent, id, title, pos, size, style, name)

            self.mainsizer = wx.BoxSizer(wx.HORIZONTAL)

            self.load_project()
            project = Kernel.GlobalObjects.get_value("PROJECT")
            #---------------------------------
            #self.map = project.getMapData(46)
            #---------------------------------
            self.map = project.getMapData(1)
            self.events = self.map.events

            self.tilesets = project.getData("Tilesets")
            #---------------------------------
            #self.EventEditorPanel = EventPanel(self, self.events[7])
            #---------------------------------
            # Test Event IDs 1 through 6
            # 1 = First Page of Event Commands
            # 2 = Change Variable commands
            # 3 = Conditional Branches
            # 4 = Second Page of Event Commands
            # 5 = Non-Actor/Enemy altering Commands
            # 6 = Actor/Enemy altering Commands
            self.EventEditorPanel = EventPanel(self, self.events[3]) 

            self.mainsizer.Add(self.EventEditorPanel, 1, wx.EXPAND, 0)
            self.SetSizer(self.mainsizer)
            self.Layout()

        def load_project(self):
            #config = Kernel.GlobalObjects.get_value("Welder_config")
            #path = config.get("RTPs", "core")
            RTP_PATH = Kernel.GlobalObjects.get_value("Welder_config").get_section("RTPs").get('Standard')
            print "[EVENT TEST] RTP PATH: %s" % RTP_PATH
            #---------------------------------
            #TEST_PATH = os.path.join(Kernel.normConfigPath(RTP_PATH), "Templates", "Chronicles of Sir Lag-A-Lot", "Chronicles of Sir Lag-A-Lot.arcproj")
            #---------------------------------
            TEST_PATH = os.path.join(Kernel.normConfigPath(RTP_PATH), "Templates", "EventTest", "EventTest.arcproj")
            print TEST_PATH
            #get a project loader
            projectloader = KM.get_component("ARCProjectLoader").object()
            projectloader.load(TEST_PATH)
            #place the project in the global namespace
            if Kernel.GlobalObjects.has_key("PROJECT"):
                Kernel.GlobalObjects.set_value("PROJECT", projectloader.getProject())
            else:
                Kernel.GlobalObjects.request_new_key("PROJECT", "CORE", projectloader.getProject())
            #set the Project Title
            if Kernel.GlobalObjects.has_key("Title"):
                Kernel.GlobalObjects.set_value("Title", projectloader.getProject().getInfo("Title"))
            else:
                Kernel.GlobalObjects.request_new_key("Title", "CORE", projectloader.getProject().getInfo("Title"))
            #set the current project directory
            if Kernel.GlobalObjects.has_key("CurrentProjectDir"):
                Kernel.GlobalObjects.set_value("CurrentProjectDir", os.path.dirname(TEST_PATH))
            else:
                Kernel.GlobalObjects.request_new_key("CurrentProjectDir", "CORE", os.path.dirname(TEST_PATH))
            #set that there is an open project
            if Kernel.GlobalObjects.has_key("ProjectOpen"):
                Kernel.GlobalObjects.set_value("ProjectOpen", True)
            else:
                Kernel.GlobalObjects.request_new_key("ProjectOpen", "CORE", True)

    provider = wx.SimpleHelpProvider()
    wx.HelpProvider.Set(provider)
       
    
    frame = TestFrame(None, wx.ID_ANY, 'Event Test')
    frame.Show()

    app.MainLoop()
    app.Destroy()