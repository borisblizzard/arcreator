'''
Created on Sep 12, 2010

Contains data for a open project

'''
import os
import sys
import time
import ConfigParser
import zipfile
import re

import Kernel
from Kernel import Manager as KM

class Project(object):
    
    def __init__(self):
        self._data = {}
        self._deferred_data = {}
        self._info = {}
        self.advanced_handlers = {}
        self.project_path = ""
        self.load_func = None
        self.save_func = None

    def addAdvancedHandler(self, handler, name):
        self.addFolderToZip[name] = handler

    def removeAdvancedHandler(self, name):
        del self.advanced_handlers[name]
        
    def testAdvancedHandlersLoad(self, key):
        for handler in self.advanced_handlers.itervalues():
            if handler.test():
                handler.loadData(key)
                handler.finalize()
                return True
            else:
                return False

    def testAdvancedHandlersSave(self, key):
        for handler in self.advanced_handlers.itervalues():
            if handler.test():
                handler.finalize()
                handler.saveData(key)
                return True
            else:
                return False

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

    def hasData(self, key):
        return self._data.has_key(key)
        
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
                if not self.testAdvancedHandlersLoad(key):
                    self._deferred_data[key] = [False, self.load_func(os.path.dirname(self.project_path), key)]
                return self._deferred_data[key][1]
            except StandardError:
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

    def hasInfo(self, key):
        return self._info.has_key(key.lower())
        
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
            Kernel.Protect(self.save_func)(os.path.dirname(self.project_path), key, self.getData(key))
            self.setChangedData(key, False)
        else:
            Kernel.Log("Warning: no save function set for project. Data files NOT saved", "[Project]")
                
    def saveDeferredData(self, key):
        if (self.save_func != None) and callable(self.save_func):
            Kernel.Protect(self.save_func)(os.path.dirname(self.project_path), key, self.getDeferredData(key))
            self.setChangedDeferredData(key, False)
        else:
            Kernel.Log("Warning: no save function set for project. Data files NOT saved", "[Project]")

    def saveMapData(self, id_num):
        if (self.save_func != None) and callable(self.save_func):
            self.save_func(os.path.dirname(self.project_path), "Map%03d" % id_num, self.getDeferredData("Map%03d" % id_num))
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

    def saveProject(self, all=False):
        for key in self._data:
            if all or self.getChangedData(key):
                if not self.testAdvancedHandlersSave(key):
                    self.saveData(key)
        for key in self._deferred_data:
            if all or self.getChangedDeferredData(key):
                if not self.testAdvancedHandlersSave(key):
                    self.saveDeferredData(key)
        self.saveInfo()
               
    def loadProject(self, backup=True):
        if os.path.exists(self.project_path):
            if backup: self.Backup()
            config = ConfigParser.ConfigParser()
            config.read(os.path.normpath(self.project_path))
            infos = config.items("Project")
            for info in infos:
                self.setInfo(info[0], info[1], False)
            filelist = config.get("Files", "List")
            files = filelist.split("|")
            for file_name in files:
                if file_name != "":
                    if not self.testAdvancedHandlersLoad(file_name):
                        if (self.load_func != None) and callable(self.load_func):
                            self.setData(file_name, Kernel.Protect(self.load_func)(os.path.dirname(self.project_path), file_name), False)
                        else:
                            self.setData(file_name, None, False)
                            Kernel.Log("Warning: no load function set for project. Data for %s set to None" % file_name, "[Project]")
        else:
            Kernel.Log("Warning: project path %s does not exist. Project not loaded." % self.project_path, "[Project]")
    
    def addFolderToZip(self, zip, dir, rel_path=""):
        dir = os.path.abspath(dir)
        dir = dir.encode('ascii') #convert path to ascii for ZipFile Method
        for file in os.listdir(dir):
            target = os.path.join(dir, file)
            if os.path.isfile(target):
                zip.write(target, os.path.join(rel_path, file), zipfile.ZIP_DEFLATED)
            elif os.path.isdir(target):
                self.addFolderToZip(zip, target, os.path.join(rel_path, os.path.basename(target)))
    
    def Backup(self):
        Kernel.StatusBar.BeginTask(3, "Making Project Backup")
        Kernel.StatusBar.UpdateTask(0, "Ensure Backup Path")
        filename = os.path.splitext(os.path.basename(self.project_path))[0]
        curTime = time.strftime("-%Y_%m_%d-%H_%M")
        filename += curTime
        filename += ".zip"
        backupFolder = os.path.abspath(os.path.join(os.path.dirname(self.project_path), "Backups"))
        if not os.path.exists(backupFolder) or not os.path.isdir(backupFolder):
            os.makedirs(backupFolder)
        zipFilename = os.path.abspath(os.path.join(backupFolder, filename))
        zip = zipfile.ZipFile(zipFilename, "w", zipfile.ZIP_DEFLATED)
        Kernel.StatusBar.UpdateTask(1, "Adding Data folder to Backup")
        self.addFolderToZip(zip, os.path.abspath(os.path.join(os.path.dirname(self.project_path), "Data")), "Data")
        zip.close()
        Kernel.StatusBar.UpdateTask(2, "Limiting the Number of Backups")
        self.LimitBackups(backupFolder)
        Kernel.StatusBar.UpdateTask(3, "Finished Backup")
        Kernel.StatusBar.EndTask()
        return zipFilename

    def FindBackupFiles(self, path):
        pattern = "%s-([0-9]+_[0-9]+_[0-9]+-[0-9]+_[0-9]+)" % os.path.splitext(os.path.basename(self.project_path))[0]
        namePattern = re.compile(pattern, re.IGNORECASE)
        files = []
        for file in os.listdir(path):
            match = namePattern.search(file)
            if match:
                filetime = time.mktime(time.strptime(match.group(1), "%Y_%m_%d-%H_%M"))
                files.append([os.path.join(path, file), filetime])
        return files

    def LimitBackups(self, path):
        backups = self.FindBackupFiles(path)
        backups.sort(key=lambda backup: backup[1])
        config = Kernel.GlobalObjects.get_value("ARCed_config")
        try:
            maxBackups = config.getint("Main", "MaxBackups")
        except:
            maxBackups = 10
            Kernel.Log("Invalid setting for MaxBackups in configuration", "[Project]", error=True)
        if len(backups) > maxBackups:
            for i in range(len(backups) - maxBackups):
                file = backups.pop(0)
                os.remove(file[0])

    def RestoreBackup(self, path):
        backup = self.Backup()
        if zipfile.is_zipfile(path):
            try:
                zip = zipfile.ZipFile(path, "r", zipfile.ZIP_DEFLATED)
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
            except StandardError:
                Kernel.Log("There was an error restoring the backup, your project data may be corrupted. A backup was made before the restore was attempted, this backup can be found at %s" % backup, "[Project]", True, True)
        else:
            Kernel.Log("Backup file is not a valid zip file", "[Project]", True)

class AdvancedDataHandler(object):

    def __init__(self, project):
        self.project = project
        self.names = []

    def test(self, name):
        for test_name in self.names:
            if test_name.lower() == name.lower():
                return True
        return False

    def loadData(self, name):
        pass

    def saveData(self, name):
        pass

    def finalize(self):
        pass

    def getPath(self, name):
        dir_name = self.getDir(name)
        path = os.path.join(dir_name, name + ".arc")
        return path

    def getDir(self, name):
        dir_name = os.path.join(self.project.getProjectPath(), "Data")
        return dir_name
                

class ARCProjectCreator(object):
    
    def __init__(self):
        self.project = None
        
    def Create(self, path, title, template):
        #create a project object
        self.project = KM.get_component("ARCProjectHolder").object()
        if template[0]:
            #load the template
            self.project.setProjectPath(template[1])
            self.project.setLoadFunc(KM.get_component("ARCProjectLoadFunction").object)
            self.project.loadProject(backup=False)
            mapinfos = self.project.getData("MapInfos")
            for key in mapinfos:
                self.project.getMapData(key)
        else:
            #set initial info
            self.project.setData("Actors", [], False)
            self.project.setData("Classes", [], False)
            self.project.setData("Skills", [], False)
            self.project.setData("Items", [], False)
            self.project.setData("Weapons", [], False)
            self.project.setData("Armors", [], False)
            self.project.setData("Enemies", [], False)
            self.project.setData("States", [], False)
            self.project.setData("Animations", [], False)
            self.project.setData("Troops", [], False)
            self.project.setData("Tilesets", [], False)
            self.project.setData("CommonEvents", [], False)
            self.project.setData("System", [], False)
            self.project.setData("MapInfos", {}, False)
            self.project.setData("MapData", {}, False)
        #set the title
        self.project.setInfo("Title", title)
        self.project.setChangedInfo("Title", False)
        #set the save function
        self.project.setSaveFunc(KM.get_component("ARCProjectSaveFunction").object)
        #set the project path
        self.project.setProjectPath(path)
        #save the project
        self.project.saveProject(all=True)

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

