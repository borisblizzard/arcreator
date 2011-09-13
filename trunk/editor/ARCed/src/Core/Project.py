'''
Created on Sep 12, 2010

Contains data for a open project

'''
import os
import sys
import ConfigParser

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
        for file in files:
            filelist += str(file)
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
        for file in files:
            if file != "":
                self.setData(file, load_func(os.path.dirname(path), file))