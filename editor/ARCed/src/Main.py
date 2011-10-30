'''
Created on Sep 11, 2010

the main program module. load the wx libary and runs the application

Classes in this module
-----------------------
ARC_App - main application class
'''
import os
import sys
import types

import ConfigParser

import wx
from wx.lib.embeddedimage import PyEmbeddedImage
import wx.lib.agw.advancedsplash as AS

if hasattr(sys, 'frozen'): 
    dirName = sys.executable
else:
    try:
        dirName = os.path.dirname(os.path.abspath(__file__))
    except:
        dirName = os.path.dirname(os.path.abspath(sys.argv[0]))
sys.path.append(os.path.split(dirName)[0])
print dirName

import Kernel
from Kernel import Manager as KM
#import Core

import Logo


class Config(object):

    def __init__(self):
        self.sections = {}

    def has_section(self, key):
        return self.sections.has_key(str(key).lower())

    def add_section(self, key):
        if not self.has_section(key):
            self.sections[str(key).lower()] = ConfigSection()
        else:
            Kernel.Log("Config Section '%s' already exists" % key, "[Config]")

    def get_section(self, key):
        if self.has_section(key):
            return self.sections[str(key).lower()]
        else:
            Kernel.Log("No config section '%s'" % key, "[Config]")
            return  ConfigSection()

    def get(self, key, item):
        if self.has_section(key):
            return self.get_section(key).get(item)
        else:
            return None

    def set(self, key, item, value):
        if self.has_section(key):
            self.get_section(key).set(item, value)

    def itersections(self):
        for section in self.sections:
            yield section, self.sections[section]



class ConfigSection(object):

    def __init__(self):
        self.items = {}

    def has_item(self, key):
        return self.items.has_key(str(key).lower())

    def set(self, key, value):
        self.items[str(key).lower()] = str(value)

    def get(self, key):
        if self.has_item(key):
            return self.items[str(key).lower()]
        else:
            return None

    def iteritems(self):
        for item in self.items:
            yield item, self.items[item]

class ConfigManager(object):

    @staticmethod
    def LoadConfig():
        #main Config
        local_arced_path = os.path.join(dirName, "ARCed.cfg")
        user_arced_path = os.path.join(Kernel.GetConfigFolder(), "ARCed.cfg")
        arced_cfg = ConfigManager.PhraseCFGFile(local_arced_path, dict={"INSTALLDIR": dirName, "PROGRAMFILES": "%PROGRAMFILES%"})
        arced_cfg = ConfigManager.PhraseCFGFile(user_arced_path, arced_cfg)
        if Kernel.GlobalObjects.has_key("ARCed_config"):
            Kernel.GlobalObjects.set_value("ARCed_config", arced_cfg)
        else:
            Kernel.GlobalObjects.request_new_key("ARCed_config", "CORE", arced_cfg)
        #wx config
        wx_config = wx.FileConfig(appName="ARCed", vendorName="arc@chaos-project.com", 
                                    localFilename=os.path.join(Kernel.GetConfigFolder(), "filehistory.cfg"))
        if Kernel.GlobalObjects.has_key("WX_config"):
            Kernel.GlobalObjects.set_value("WX_config", wx_config)
        else:
            Kernel.GlobalObjects.request_new_key("WX_config", "CORE", wx_config)
        #default component config
        local_defaults_path = os.path.join(dirName, "defaults.ini")
        user_defaults_path = os.path.join(Kernel.GetConfigFolder(), "user_defaults.ini")
        template = Kernel.KernelConfig.build_from_file(local_defaults_path)
        if os.path.exists(user_defaults_path):
            template = Kernel.KernelConfig.build_from_file(user_defaults_path, template)
        Kernel.KernelConfig.load(template)
        if Kernel.GlobalObjects.has_key("DefaultComponentTemplate"):
            Kernel.GlobalObjects.set_value("DefaultComponentTemplate", template)
        else:
            Kernel.GlobalObjects.request_new_key("DefaultComponentTemplate", "CORE", template)

    @staticmethod
    def SaveConfig():
        user_arced_path = os.path.join(Kernel.GetConfigFolder(), "ARCed.cfg")
        ConfigManager.SaveCFGFile(user_arced_path, Kernel.GlobalObjects.get_value("ARCed_config"))
        Kernel.GlobalObjects.get_value("WX_config").Flush()
        user_defaults_path = os.path.join(Kernel.GetConfigFolder(), "user_defaults.ini")
        Kernel.KernelConfig.save_to_file(Kernel.KernelConfig.BuildFromKernel(), user_defaults_path)
    
    @staticmethod    
    def PhraseCFGFile(file_path, config=None, dict=None):
        if config is None:
            config = Config()
        configphraser = ConfigParser.ConfigParser()
        configphraser.read(file_path)
        for section in configphraser.sections():
            if not config.has_section(section):
                config.add_section(section)
            for item, value in configphraser.items(section, True):
                if dict is None:
                    config.set(section, item, value)
                else:
                    config.set(section, item, value % dict)
        return config

    @staticmethod
    def SaveCFGFile(file_path, config_obj):
        config = ConfigParser.ConfigParser()
        for section_name, section in config_obj.itersections():
            config.add_section(str(section_name))
            for name, value in section.iteritems():
                config.set(str(section_name), str(name), str(value))
        f = open(file_path, "wb")
        config.write(f)
        f.close()

    @staticmethod
    def LoadPlugins():
        plugin_path = Kernel.GetPluginFolder()
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
                ConfigManager.HandelErrorLoadingPlugin(name, plugin_path)
            
    @staticmethod
    def HandelErrorLoadingPlugin(name, plugin_path):
        Kernel.Log("Error Loading plugin %s from path %s" % (name, plugin_path), "[Main Loader]", error=True)



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
        #import the core and regester it
        try:
            import Core
        except:
            Kernel.Log("Error Loading Core", "[Main]", True, True)
            wx.Exit()
        #load the configuration
        try:
            ConfigManager.LoadConfig()
        except:
            Kernel.Log("Error Loading Configuration", "[Main]", True, True)
        #ConfigManager.LoadPlugins()
        self.ShowMain()
        self.fc = wx.FutureCall(1000, self.Close)

    def Close(self):
        self.Hide()
        self.Destroy()
        
    

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
        self.fc = wx.FutureCall(10, Kernel.Protect(self.SplashScreen.Do_Setup))

        self.keepGoing = True
        return True

   


if __name__ == '__main__':

    provider = wx.SimpleHelpProvider()
    wx.HelpProvider.Set(provider)

    
    redirect = False
    
    app = ARC_App(redirect)
    app.MainLoop()
    try:
        ConfigManager.SaveConfig()
    except:
        Kernel.Log("Error saving Configs", "[Main]", error=True)
