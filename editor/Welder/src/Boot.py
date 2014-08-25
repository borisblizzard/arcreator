#!/usr/bin/env python
"""
Created on Sep 11, 2010

the main program module. load the wx libary and runs the application

Classes in this module
-----------------------
ARC_App - main application class
"""
import os
import sys
import types

import configparser

import importlib

import wx
from wx.lib.embeddedimage import PyEmbeddedImage
import wx.lib.agw.advancedsplash as AS
import wx.lib.inspection

import Welder
import Logo

def WelderImport(name):
    if Welder.IMPORT_MODE == "SOURCE":
        return importlib.import_module(name, package=None)
    elif Welder.IMPORT_MODE == "COMPIL":
        return importlib.import_module("Compiled." + name, package=None)
    else:
        return importlib.import_module(name, package=None)

Kernel = WelderImport('Kernel')
#Kernel = WelderImport('Kernel')
KM = Kernel.Manager
#KM = Kernel.Manager
#import Core


class Config(object):

    def __init__(self):
        self.sections = {}

    def has_section(self, key):
        return str(key).lower() in self.sections

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
            return ConfigSection()

    def get(self, key, item):
        if self.has_section(key):
            return self.get_section(key).get(item)
        else:
            return None

    def getint(self, key, item):
        if self.has_section(key):
            return int(self.get_section(key).get(item))
        else:
            return None

    def getlist(self, key, item, separator='|'):
        if self.has_section(key):
            return self.get_section(key).get(item).split(separator)
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
        return str(key).lower() in self.items

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
        local_Welder_path = os.path.join(Kernel.GlobalObjects.get_value("Program_Dir"), "Welder.cfg")
        print("[BOOT] CFG FILE: %s" % local_Welder_path)
        Welder_cfg = ConfigManager.PhraseCFGFile(local_Welder_path, dict={"INSTALLDIR": Kernel.GlobalObjects.get_value("Program_Dir"), "COMMONPROGRAMFILES": "%COMMONPROGRAMFILES%"})
        try:
            user_Welder_path = os.path.join(Kernel.GetConfigFolder(), "Welder.cfg")
            if os.path.exists(user_Welder_path):
                Welder_cfg = ConfigManager.PhraseCFGFile(user_Welder_path, Welder_cfg)
        except Exception:
            Kernel.Log("Failed to load user config", "[Main]", error=True)
        if "Welder_config" in Kernel.GlobalObjects:
            Kernel.GlobalObjects.set_value("Welder_config", Welder_cfg)
        else:
            Kernel.GlobalObjects.request_new_key("Welder_config", "CORE", Welder_cfg)
        #wx config
        wx_config = wx.FileConfig(appName="Welder", vendorName="arc@chaos-project.com", 
                                    localFilename=os.path.join(Kernel.GetConfigFolder(), "filehistory.cfg"))
        if "WX_config" in Kernel.GlobalObjects:
            Kernel.GlobalObjects.set_value("WX_config", wx_config)
        else:
            Kernel.GlobalObjects.request_new_key("WX_config", "CORE", wx_config)
        #default component config
        local_defaults_path = os.path.join(Kernel.GlobalObjects.get_value("Program_Dir"), "defaults.ini")
        template = Kernel.KernelConfig.build_from_file(local_defaults_path)
        try:
            user_defaults_path = os.path.join(Kernel.GetConfigFolder(), "user_defaults.ini")
            if os.path.exists(user_defaults_path):
                template = Kernel.KernelConfig.build_from_file(user_defaults_path, template)
        except Exception:
            Kernel.Log("Failed to load user component defaults", "[Main]", error=True)
        if "DefaultComponentTemplate" in Kernel.GlobalObjects:
            Kernel.GlobalObjects.set_value("DefaultComponentTemplate", template)
        else:
            Kernel.GlobalObjects.request_new_key("DefaultComponentTemplate", "CORE", template)

    @staticmethod
    def SaveConfig():
        user_Welder_path = os.path.join(Kernel.GetConfigFolder(), "Welder.cfg")
        ConfigManager.SaveCFGFile(user_Welder_path, Kernel.GlobalObjects.get_value("Welder_config"))
        Kernel.GlobalObjects.get_value("WX_config").Flush()
        user_defaults_path = os.path.join(Kernel.GetConfigFolder(), "user_defaults.ini")
        Kernel.KernelConfig.save_to_file(Kernel.KernelConfig.BuildFromKernel(), user_defaults_path)
    
    @staticmethod    
    def PhraseCFGFile(file_path, config=None, dict=None):
        if config is None:
            config = Config()
        configphraser = configparser.ConfigParser()
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
        config = configparser.ConfigParser()
        for section_name, section in config_obj.itersections():
            config.add_section(str(section_name))
            for name, value in section.items():
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
                            exec(compile(open(os.path.join(name, "__init__.py")).read(), os.path.join(name, "__init__.py"), 'exec'), globals())
                    #else:
                    #    execfile(os.path.join(name, "__init__.py"), globals())
            except Exception:
                ConfigManager.HandelErrorLoadingPlugin(name, plugin_path)
            
    @staticmethod
    def HandelErrorLoadingPlugin(name, plugin_path):
        Kernel.Log("Error Loading plugin %s from path %s" % (name, plugin_path), "[Main Loader]", error=True)

class ARCSplashScreen(AS.AdvancedSplash):
    def __init__(self):
        #get the splashscreen logo
        #bmp = bitmap = wx.Bitmap(os.path.join(Kernel.GlobalObjects.get_value("Program_Dir"), "arc-logo.png"), wx.BITMAP_TYPE_PNG)
        bmp = Logo.getlogoBitmap()
        shadow = wx.WHITE
        AS.AdvancedSplash.__init__(self, None, bitmap=bmp,
                                   agwStyle=AS.AS_NOTIMEOUT| 
                                   AS.AS_CENTER_ON_SCREEN|
                                   AS.AS_SHADOW_BITMAP,
                                   shadowcolour=shadow)      

    def Do_Setup(self):
        #load up the editor
        #load the configuration
        try:
            ConfigManager.LoadConfig()
        except:
            Kernel.Log("Error Loading Configuration", "[Main]", True, True)
            #sadly there is a tone of thing that won't work if the configuration didn't load properly so we have to exit
            wx.Exit()
        #import the core and register it
        try:
            WelderImport('Core').late_bind()
        except:
            Kernel.Log("Error Loading Core", "[Main]", True, True)
            #we can't recover from this so exit out
            wx.Exit()

        #load plugins
        #ConfigManager.LoadPlugins()
        #apply the default component template
        try:
            template = Kernel.GlobalObjects.get_value("DefaultComponentTemplate")
            Kernel.KernelConfig.load(template)
        except:
            #even if this fails we should be good to go, plugins probably won;t work though
            Kernel.Log("Error Applying the Default Component Template, Plugins may not work", "[Main]", True, True)
            
        # ok were all set up. bring up the main window and close the splash screen
        self.ShowMain()
        #lets start up PyXAL so we can use it
        self.BindPyXAL()
        self.fc = wx.FutureCall(1000, self.Close)

    def Close(self):
        self.Hide()
        self.Destroy()
        
    

    def ShowMain(self):
        MainWindow = KM.get_component("EditorMainWindow").object
        self.frame = MainWindow(None, wx.ID_ANY, 'Welder')
        self.frame.Show(True)

    def BindPyXAL(self):
        PyXAL = KM.get_component("PyXAL").object
        if PyXAL is not None:
            PyXAL.Init(self.frame.GetHandle(), True)
        
        #wx.lib.inspection.InspectionTool().Show()

class ARC_App(wx.App):

    def OnInit(self):
        self.SetAppName("Welder")

        self.SplashScreen = ARCSplashScreen()
        self.SplashScreen.Show()
        self.fc = wx.CallLater(10, Kernel.Protect(self.SplashScreen.Do_Setup, exit_on_fail=True))

        self.keepGoing = True
        return True

def Run(programDir):
    if "Program_Dir" in Kernel.GlobalObjects:
        Kernel.GlobalObjects.set_value("Program_Dir", programDir)
    else:
        Kernel.GlobalObjects.request_new_key("Program_Dir", "CORE", programDir)

    print("[BOOT] Programming Running in %s" % programDir)
    
    provider = wx.SimpleHelpProvider()
    wx.HelpProvider.Set(provider)

    app = ARC_App(False)
    #start up the app, we wont be comming back till the app is closed
    app.MainLoop()
    # we want to clean up PyXAL as much as we can, it's dead now anyway as the window it was bound to is gone
    try:
        PyXAL = KM.get_component("PyXAL").object
        if PyXAL is not None:
            PyXAL.Destroy()
    except:
        Kernel.Log("Error destroying PyXAL Binding", "[Main]", error=True)
    #lets try to save the user's current config before we leave
    try:
        ConfigManager.SaveConfig()
    except:
        Kernel.Log("Error saving Configs", "[Main]", error=True)
