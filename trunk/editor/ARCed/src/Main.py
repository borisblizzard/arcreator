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
from wx.lib.embeddedimage import PyEmbeddedImage
import wx.lib.agw.advancedsplash as AS
try:
    dirName = os.path.dirname(os.path.abspath(__file__))
except:
    dirName = os.path.dirname(os.path.abspath(sys.argv[0]))
sys.path.append(os.path.split(dirName)[0])

import Kernel
from Kernel import Manager as KM
#import Core

import Logo


class ARCSplashScreen(AS.AdvancedSplash):
    def __init__(self):
        #get the splashscreen logo
        #bmp = bitmap = wx.Bitmap(os.path.join(dirName, "arc-logo.png"), wx.BITMAP_TYPE_PNG)
        bmp = Logo.getlogoImage().ConvertToBitmap()
        shadow = wx.WHITE
        AS.AdvancedSplash.__init__(self, None, bitmap=bmp,
                                   agwStyle=AS.AS_NOTIMEOUT| 
                                   AS.AS_CENTER_ON_SCREEN|
                                   AS.AS_SHADOW_BITMAP,
                                   shadowcolour=shadow)      

    def Do_Setup(self):
        #load up the editor
        import Core
        self.SetupData()
        self.LoadConponentDefaults()
        #self.LoadPlugins()
        self.ShowMain()
        self.fc = wx.FutureCall(1000, self.Close)

    def Close(self):
        self.Hide()
        self.Destroy()
        
    def SetupData(self):
        config = ConfigParser.ConfigParser()
        path = os.path.join(dirName, "ARC.cfg")
        config.read(path)
        Kernel.GlobalObjects.set_value("ARCconfig", config)

        programconfig = wx.FileConfig(appName="ARCed", vendorName="arc@chaos-project.com", 
                                    localFilename=os.path.join(Kernel.GetConfigFolder(), "ARCed.cfg"))
        if Kernel.GlobalObjects.has_key("programconfig"):
            Kernel.GlobalObjects.set_value("programconfig", programconfig)
        else:
            Kernel.GlobalObjects.request_new_key("programconfig", "CORE", programconfig)
        
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
        Kernel.Log("Error Loading plugin %s from path %s" % (name, plugin_path), "[Main Loader]", error=True)

    def LoadConponentDefaults(self):
        template = Kernel.ConfigLoader.build_from_file(os.path.join(dirName, "defaults.ini"))
        Kernel.ConfigLoader.load(template)
        if Kernel.GlobalObjects.has_key("LoadedComponentDefaultsTemplate"):
            Kernel.GlobalObjects.set_value("LoadedComponentDefaultsTemplate", template)
        else:
            Kernel.GlobalObjects.request_new_key("LoadedComponentDefaultsTemplate", "CORE", template)

    def ShowMain(self):
        MainWindow = KM.get_component("EditorMainWindow").object
        self.frame = MainWindow(None, wx.ID_ANY, 'ARCed')
        self.frame.Show(True)

class ARC_App(wx.App):

    def OnInit(self):
        self.SetAppName("ARCed")

        wx.InitAllImageHandlers()

        self.SplashScreen = ARCSplashScreen()
        self.SplashScreen.Show()
        self.fc = wx.FutureCall(10, self.SplashScreen.Do_Setup)

        self.keepGoing = True
        return True

   


if __name__ == '__main__':

    provider = wx.SimpleHelpProvider()
    wx.HelpProvider.Set(provider)

    
    redirect = False
    
    app = ARC_App(redirect)
    app.MainLoop()
