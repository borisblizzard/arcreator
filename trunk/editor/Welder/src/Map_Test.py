import os
import sys
import math

import wx
from wx import glcanvas

import pyglet
from pyglet import gl

import rabbyt

import numpy



import Kernel


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

    if "Program_Dir" in Kernel.GlobalObjects:
        Kernel.GlobalObjects.set_value("Program_Dir", LOCAL_PATH)
    else:
        Kernel.GlobalObjects.request_new_key("Program_Dir", "CORE", LOCAL_PATH)

    print("[BOOT] Programming Running in %s" % dirName)
    print("[BOOT] LOCAL PATH: %s" % LOCAL_PATH)
    print("[BOOT] CONFIG PATH: %s" % Kernel.GetConfigFolder())

    import Boot
    
    Boot.ConfigManager.LoadConfig()

    
    Core.late_bind()

    MapPanel = Core.MapEditor.MapEditorPanel.MapPanel

    if "Program_Dir" in Kernel.GlobalObjects:
        Kernel.GlobalObjects.set_value("Program_Dir", LOCAL_PATH)
    else:
        Kernel.GlobalObjects.request_new_key("Program_Dir", "CORE", LOCAL_PATH)

    class TestFrame(wx.Frame):
        '''A simple class for using OpenGL with wxPython.'''

        def __init__(self, parent, id, title, pos=wx.DefaultPosition,
                     size=wx.Size(800, 600), style=wx.DEFAULT_FRAME_STYLE,
                     name='frame'):
            super(TestFrame, self).__init__(parent, id, title, pos, size, style, name)
        
            self.mainsizer = wx.BoxSizer(wx.HORIZONTAL)
            #self.GLPanel1 = TestGlPanel(self)
            #self.mainsizer.Add(self.GLPanel1, 1, wx.EXPAND, 5)
            #self.GLPanel2 = TestGlPanel(self, wx.ID_ANY, (20, 20))
            #self.mainsizer.Add(self.GLPanel2, 1, wx.EXPAND, 5)
            
            self.load_project()
            project = Kernel.GlobalObjects.get_value("PROJECT")
            self.map = project.getMapData(8)
            self.tilesets = project.getData("Tilesets")
        
            self.MapEditorPanel = MapPanel(self, self.map, self.tilesets)
            self.mainsizer.Add(self.MapEditorPanel, 1, wx.EXPAND, 0)
        
            self.SetSizer(self.mainsizer)
            self.Layout()

        
        def load_project(self):
            #config = Kernel.GlobalObjects.get_value("Welder_config")
            #path = config.get("RTPs", "core")
            RTP_PATH = Kernel.GlobalObjects.get_value("Welder_config").get_section("RTPs").get('Standard')
            TEST_PATH = os.path.join(RTP_PATH, "Templates", "Chronicles of Sir Lag-A-Lot", "Chronicles of Sir Lag-A-Lot.arcproj")
            print(TEST_PATH)
            #get a project loader
            projectloader = Kernel.System.load(ARCProjectLoader)()
            projectloader.load(TEST_PATH)
            #place the project in the global namespace
            if "PROJECT" in Kernel.GlobalObjects:
                Kernel.GlobalObjects.set_value("PROJECT", projectloader.getProject())
            else:
                Kernel.GlobalObjects.request_new_key("PROJECT", "CORE", projectloader.getProject())
            #set the Project Title
            if "Title" in Kernel.GlobalObjects:
                Kernel.GlobalObjects.set_value("Title", projectloader.getProject().getInfo("Title"))
            else:
                Kernel.GlobalObjects.request_new_key("Title", "CORE", projectloader.getProject().getInfo("Title"))
            #set the current project directory
            if "CurrentProjectDir" in Kernel.GlobalObjects:
                Kernel.GlobalObjects.set_value("CurrentProjectDir", os.path.dirname(TEST_PATH))
            else:
                Kernel.GlobalObjects.request_new_key("CurrentProjectDir", "CORE", os.path.dirname(TEST_PATH))
            #set that there is an open project
            if "ProjectOpen" in Kernel.GlobalObjects:
                Kernel.GlobalObjects.set_value("ProjectOpen", True)
            else:
                Kernel.GlobalObjects.request_new_key("ProjectOpen", "CORE", True)

    

    app = wx.App(redirect=False)
    frame = TestFrame(None, wx.ID_ANY, 'Map Test')
    frame.Show()

    app.MainLoop()
    app.Destroy()