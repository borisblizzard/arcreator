'''
Created on Sep 12, 2010

Contains data for a open project

'''
import os
import sys
import ConfigParser
import ARC_Data

import Kernel
from Kernel import Manager as KM

class Project(object):
    
    def __init__(self):
        self._data = {}
        self._info = {}
        
    def setData(self, key, value):
        self._data[key] = value
    
    def getData(self, key):
        if self._data.has_key(key):
            return self._data[key]
        else:
            return None
    
    def setInfo(self, key, value):
        self._info[key] = value
        
    def getInfo(self, key):
        if self._info.has_key(key):
            return self._info[key]
        else:
            return None

    def saveProject(self, path, save_func):
        config = ConfigParser.ConfigParser()
        config.add_section("Project")
        for key, value in self._info.items():
            config.set("Project", str(key), str(value))
        filename = os.path.normpath(path)
        config.add_section("Files")
        filelist = ""
        files = self._data.keys()
        i = 0
        for file_name in files:
            filelist += str(file_name)
            if i >= (len(files) - 1):
                filelist += "|"
            i += 1
        config.set("Files", "List", filelist)
        f = open(filename, 'wb')
        config.write(f)
        f.close()
        for key, value in self._data.items():
            save_func(os.path.dirname(path), key, value)
    
    def loadProject(self, path, load_func):
        config = ConfigParser.ConfigParser()
        config.read(os.path.normpath(path))
        infos = config.items("Project")
        for info in infos:
            self.setInfo(info[0], info[1])
        filelist = config.get("Files", "List")
        files = filelist.split("|")
        for file_name in files:
            if file_name != "":
                self.setData(file_name, load_func(os.path.dirname(path), file_name))
                
class ARCProjectCreator(object):
    
    def __init__(self):
        self.project = None
        
    def Create(self, path, title, saveas=False):
        self.project = KM.get_component("ARCProjectHolder").object()
        self.project.setInfo("Title", title)
        self.project.setData("Actors", [])
        self.project.setData("Classes", [])
        self.project.setData("Skills", [])
        self.project.setData("Items", [])
        self.project.setData("Weapons", [])
        self.project.setData("Armors", [])
        self.project.setData("Troops", [])
        self.project.setData("Tilesets", [])
        self.project.setData("CommonEvents", [])
        self.project.setData("System", [])
        self.project.setData("MapInfos", [])
        if Kernel.GlobalObjects.has_key("PROJECT"):
            Kernel.GlobalObjects.set_value("PROJECT", self.project)
        else:
            Kernel.GlobalObjects.request_new_key("PROJECT", "CORE", self.project)
        self.project.saveProject(path, KM.get_component("ARCProjectSaveFunction"))
        if not saveas:
            KM.raise_event("CoreEventRefreshProject")
            
            
def ARCProjectSaveFunction(dir_name, filename, obj):
    path = os.path.join(dir_name, "Data", filename + ".arc")
    f = open(path, "wb")
    redirects = {}
    KM.raise_event("CoreEventARCRedirectClassPathsOnSave", redirects)
    ARC_Data.ARC_Data.dump(f, obj, redirects)
    f.close()
    
def ARCProjectLoadFunction(dir_name, filename):
    path = os.path.join(dir_name, "Data", filename + ".arc")
    f = open(path, "rb")
    redirects = {}
    KM.raise_event("CoreEventARCRedirectClassPathsOnSave", redirects)
    extended_namespace = {}
    KM.raise_event("CoreEventARCExtendNamespaceOnLoad", extended_namespace)
    obj = ARC_Data.ARC_Data.load(f, redirects, extended_namespace)
    f.close()
    return obj
    