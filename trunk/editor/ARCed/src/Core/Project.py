'''
Created on Sep 12, 2010

Contains data for a open project

'''
import os
import sys
import time
import ConfigParser
import zipfile

import Kernel
from Kernel import Manager as KM

class Project(object):
    
    def __init__(self):
        self._data = {}
        self._deferred_data = {}
        self._info = {}
        self.project_path = ""
        self.load_func = None
        self.save_func = None
        
    def setLoadFunc(self, func):
        self.load_func = func
    
    def setSaveFunc(self, func):
        self.save_func = func
        
    def setProjectPath(self, path):
        self.project_path = path

    def getProjectPath(self):
        return self.project_path
        
    def setData(self, key, value, changed=True):
        if self._data.has_key(key):
            self._data[key][0] = changed
            self._data[key][1] = value
        else:
            self._data[key] = [changed, value]
    
    def getData(self, key):
        if self._data.has_key(key):
            return self._data[key][1]
        else:
            Kernel.Log("Warning: data key %s does not exist. Returned None" % key, "[Project]")
            return None
        
    def setDeferredData(self, key, value, changed=True):
        if self._deferred_data.has_key(key):
            self._deferred_data[key][0] = changed
            self._deferred_data[key][1] = value
        else:
            self._deferred_data[key] = [changed, value]
            
    def getDeferredData(self, key):
        if self._deferred_data.has_key(key):
            return self._deferred_data[key][1]
        else:
            try:
                self._deferred_data[key] = [False, self.load_func(os.path.dirname(self.project_path), key)]
                return self._deferred_data[key][1]
            except Exception:
                Kernel.Log("Warning: Deferred data '%s' does not exist. Returned None" % key, "[Project]")
                return None
    
    def setInfo(self, key, value, changed=True):
        if self._info.has_key(key.lower()):
            self._info[key.lower()][0] = changed
            self._info[key.lower()][1] = value
        else:
            self._info[key.lower()] = [changed, value]
        
    def getInfo(self, key):
        if self._info.has_key(key.lower()):
            return self._info[key.lower()][1]
        else:
            Kernel.Log("Warning: info key %s does not exist. Returned None" % key, "[Project]")
            return None
        
    def setChangedInfo(self, key, value):
        if self._info.has_key(key.lower()):
            self._info[key.lower()][0] = value
        else:
            Kernel.Log("Info key %s does not exist. change flag not set" % key, "[Project]")
    
    def getChangedInfo(self, key):
        if self._info.has_key(key.lower()):
            return self._info[key.lower()][0]
        else:
            return False
        
    def setChangedData(self, key, value):
        if self._data.has_key(key):
            self._data[key][0] = value
        else:
            Kernel.Log("Data key %s does not exist. changed flag not set" % key, "[Project]")
        
    def getChangedData(self, key):
        if self._data.has_key(key):
            return self._data[key][0]
        else:
            return False
        
    def setChangedDeferredData(self, key, value):
        if self._deferred_data.has_key(key):
            self._deferred_data[key][0] = value
        else:
            Kernel.Log("Deferred data key %s does not exist. changed flag not set" % key, "[Project]")
            
    def getChangedDeferredData(self, key):
        if self._deferred_data.has_key(key):
            return self._deferred_data[key][0]
        else:
            return False
        
    def getMapData(self, id_num):
        return self.getDeferredData("Map%03d" % id_num)
    
    def setMapData(self, id_num, value, changed=True):
        self.setDeferredData("Map%03d" % id_num, value, changed)
        
    def getChangedMapData(self, id_num):
        self.getChangedDeferredData("Map%03d" % id_num)
        
    def setChangedMapData(self, id_num, value):
        self.setChangedDeferredData("Map%03d" % id_num, value)

    def hasDataChanged(self):
        changed_flag = False
        for key, value in self._data.items():
            if value[0]:
                changed_flag = True
        for key, vlaue in self._deferred_data.items():
            if value[0]:
                changed_flag = True
        return changed_flag

    def hasInfoChanged(self):
        changed_flag = False
        for key, value in self._info.items():
            if value[0]:
                changed_flag = True
        return changed_flag


    def saveData(self, key):
        if (self.save_func != None) and callable(self.save_func):
            self.save_func(os.path.dirname(self.project_path), key, self.getData(key))
            self.setChangedData(key, False)
        else:
            Kernel.Log("Warning: no save function set for project. Data files NOT saved", "[Project]")
                
    def saveDeferredData(self, key):
        if (self.save_func != None) and callable(self.save_func):
            self.save_func(os.path.dirname(self.project_path), key, self.getDeferredData(key))
            self.setChangedDeferredData(key, False)
        else:
            Kernel.Log("Warning: no save function set for project. Data files NOT saved", "[Project]")

    def saveMapData(self, id_num):
        if (self.save_func != None) and callable(self.save_func):
            self.save_func(os.path.dirname(self.project_path), key, self.getDeferredData("Map%03d" % id_num))
            self.setChangedDeferredData("Map%03d" % id_num, False)
        else:
            Kernel.Log("Warning: no save function set for project. Data files NOT saved", "[Project]")

    def saveInfo(self):
        config = ConfigParser.ConfigParser()
        config.add_section("Project")
        for key, value in self._info.items():
            config.set("Project", str(key), str(value[1]))
        filename = os.path.normpath(self.project_path)
        config.add_section("Files")
        filelist = ""
        files = self._data.keys()
        i = 0
        for file_name in files:
            filelist += str(file_name)
            if not (i >= (len(files) - 1)):
                filelist += "|"
            i += 1
        config.set("Files", "List", filelist)
        f = open(filename, 'wb')
        config.write(f)
        f.close()

    def saveProject(self):
        for key in self._data:
            if self.getChangedData(key):
                self.saveData(key)
        for key in self._deferred_data:
            if self.getChangedDeferredData(key):
                self.saveDeferredData(key)
               
    def loadProject(self):
        if os.path.exists(self.project_path):
            self.Backup()
            config = ConfigParser.ConfigParser()
            config.read(os.path.normpath(self.project_path))
            infos = config.items("Project")
            for info in infos:
                self.setInfo(info[0], info[1], False)
            filelist = config.get("Files", "List")
            files = filelist.split("|")
            for file_name in files:
                if file_name != "":
                    if (self.load_func != None) and callable(self.load_func):
                        self.setData(file_name, self.load_func(os.path.dirname(self.project_path), file_name), False)
                    else:
                        self.setData(file_name, None, False)
                        Kernel.Log("Warning: no load function set for project. Data for %s set to None" % file_name, "[Project]")
        else:
            Kernel.Log("Warning: project path %s does not exist. Project not loaded." % self.project_path, "[Project]")
    
    def addFolderToZip(self, zip, dir, rel_path=""):
        dir = os.path.abspath(dir)
        dir = dir.encode('ascii') #convert path to ascii for ZipFile Method
        for file in os.listdir(dir):
            if os.path.isfile(file):
                zip.write(os.path.join(dir, file), os.path.join(rel_path, os.path.basename(file)), zipfile.ZIP_DEFLATED)
            elif os.path.isdir(file):
                    self.addFolderToZip(zip, os.path.join(dir, file), os.path.join(rel_path, os.path.basename(dir)))
    
    def Backup(self):
        filename = ""
        parts = os.path.basename(self.project_path).split(".")
        if len(parts) > 1:
            filename = ".".join(parts[:-1])
        elif len(parts) == 1:
            fielname = parts[0]
        curTime = time.strftime("__%Y_%m_%d_%H_%M")
        filename += curTime
        filename += ".zip"
        backupFolder = os.path.abspath(os.path.join(os.path.dirname(self.project_path), "Backups"))
        if not os.path.exists(backupFolder) or not os.path.isdir(backupFolder):
            os.makedirs(backupFolder)
        zipFilename = os.path.abspath(os.path.join(backupFolder, filename))
        zip = zipfile.ZipFile(zipFilename, "wb", zipfile.ZIP_DEFLATED)
        self.addFolderToZip(zip, os.path.abspath(os.path.join(os.path.dirname(self.project_path), "Data")))
        zip.close()
        return zipFilename

    def RestoreBackup(self, path):
        backup = self.Backup()
        if zipfile.is_zipfile(path):
            try:
                zip = zipfile.ZipFile(path, "rb", zipfile.ZIP_DEFLATED)
                local_path = os.path.abspath(os.path.dirname(self.project_path))
                for file in zip.namelist():
                    member = zip.getinfo(file)
                    if member.filename[0] == '/':
                        targetpath = os.path.join(local_path, member.filename[1:])
                    else:
                        targetpath = os.path.join(local_path, member.filename)
                    if os.path.normpath(os.path.join(local_path, file)) == os.path.abspath(targetpath):
                        if member.filename[-1] == '/':
                            if not os.path.isdir(targetpath):
                                os.mkdir(targetpath)
                            continue
                        zip.extract(file, local_path)
            except Exception:
                Kernel.Log("There was an error restoring the backup, your project data may be corrupted. A backup was made before the restore was attempted, this backup can be found at %s" % backup, "[Project]", True, True)
        else:
            Kernel.Log("Backup file is not a valid zip file", "[Project]", True)

                
class ARCProjectCreator(object):
    
    def __init__(self):
        self.project = None
        
    def Create(self, path, title):
        #create a project object
        self.project = KM.get_component("ARCProjectHolder").object()
        #set initial info
        self.project.setInfo("Title", title)
        self.project.setChangedInfo("Title", False)
        self.project.setData("Actors", [])
        self.project.setChangedData("Actors", False)
        self.project.setData("Classes", [])
        self.project.setChangedData("Classes", False)
        self.project.setData("Skills", [])
        self.project.setChangedData("Skills", False)
        self.project.setData("Items", [])
        self.project.setChangedData("Items", False)
        self.project.setData("Weapons", [])
        self.project.setChangedData("Weapons", False)
        self.project.setData("Armors", [])
        self.project.setChangedData("Armors", False)
        self.project.setData("States", [])
        self.project.setChangedData("States", False)
        self.project.setData("Animations", [])
        self.project.setChangedData("Animations", False)
        self.project.setData("Troops", [])
        self.project.setChangedData("Troops", False)
        self.project.setData("Tilesets", [])
        self.project.setChangedData("Tilesets", False)
        self.project.setData("CommonEvents", [])
        self.project.setChangedData("CommonEvents", False)
        self.project.setData("System", [])
        self.project.setChangedData("System", False)
        self.project.setData("MapInfos", {})
        self.project.setChangedData("MapInfos", False)
        #set the save function
        self.project.setSaveFunc(KM.get_component("ARCProjectSaveFunction").object)
        #set the project path
        self.project.setProjectPath(path)
        #save the project
        self.project.saveProject()

    def getProject(self):
        return self.project

    def setProject(self, project):
        self.project = project
                   
def ARCProjectSaveFunction(dir_name, filename, obj):
    dir_path = os.path.join(dir_name, "Data")
    path = os.path.join(dir_path, filename + ".arc")
    if (not os.path.exists(dir_path)) or (not os.path.isdir(dir_path)):
        os.makedirs(dir_path)
    try:
        f = open(path, "wb")
        redirects = {}
        KM.raise_event("CoreEventARCRedirectClassPathsOnSave", redirects)
        save_func = KM.get_component("ARCDataDumpFunction").object
        save_func(f, obj, redirects)
        f.close()
    except IOError:
        Kernel.Log("IO Error encountered Saving file %s" % path, "[ARC Save Function]", True)
    
def ARCProjectLoadFunction(dir_name, filename):
    path = os.path.join(dir_name, "Data", filename + ".arc")
    if os.path.exists(path) and (not os.path.isdir(path)):
        try:
            f = open(path, "rb")
            redirects = {}
            KM.raise_event("CoreEventARCRedirectClassPathsOnLoad", redirects)
            extended_namespace = {}
            KM.raise_event("CoreEventARCExtendNamespaceOnLoad", extended_namespace)
            load_func = KM.get_component("ARCDataLoadFunction").object
            obj = load_func(f, redirects, extended_namespace)
            f.close()
            return obj
        except IOError:
            Kernel.Log("IO Error encountered Loading file %s Returned None" % path, "[ARC Load Function]", True)
            return None
        
    else:
        Kernel.Log("Warning: file %s does not exist. Returned None" % path, "[ARC Load Function]")
        return None
    

class ARCProjectSaver(object):

    def __init__(self, project):
        self.project = project

    def save(self, path=""):
        if not path == "":
            self.project.setProjectPath(path)
        self.project.setSaveFunc(KM.get_component("ARCProjectSaveFunction").object)
        self.project.saveProject()

    def getProject(self):
        return self.project

    def setProject(self, project):
        self.project = project

class ARCProjectLoader(object):

    def __init__(self):
        self.project = KM.get_component("ARCProjectHolder").object()

    def load(self, path):
        self.project.setProjectPath(path)
        self.project.setLoadFunc(KM.get_component("ARCProjectLoadFunction").object)
        self.project.loadProject()
        

    def getProject(self):
        return self.project

    def setProject(self, project):
        self.project = project

