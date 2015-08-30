'''
Created on Jan 18, 2011

'''
import os
import wx

import welder_kernel as kernel

from PyitectConsumes import NewProject_Dialog, ARCProjectCreator, ARCProjectLoader, ARCProjectSaver


def NewProject(mainwindow):
    # handle an already open project
    if "ProjectOpen" in kernel.GlobalObjects and (kernel.GlobalObjects["ProjectOpen"] == True) and "PROJECT" in kernel.GlobalObjects:
        current_project = kernel.GlobalObjects["PROJECT"]
        if current_project.hasDataChanged() or current_project.hasInfoChanged():
            message = "There are unsaved changes in the currently open project Do you want to save these chagnes?"
        else:
            message = "Do you want to save the currently open project?"
        caption = "There is already an open project"
        dlg = wx.MessageDialog(mainwindow, message, caption, style=wx.YES_NO |
                               wx.YES_DEFAULT)
        result = dlg.ShowModal()
        if result == wx.YES:
            kernel.Syatem.load("SaveProjectHandler")()
    # pull the dialog for the newproject
    dlg = NewProject_Dialog(mainwindow)
    result = dlg.ShowModal()
    if result == wx.ID_OK:
        # lets create the project
        template, name, folder = dlg.getdata()
        path = os.path.join(folder, "%s.arcproj" % os.path.basename(folder))
        projectcreator = ARCProjectCreator()
        kernel.StatusBar.BeginTask(2, "Creating Project")
        projectcreator.Create(path, name, template)
        kernel.StatusBar.updateTask(1, "Finished Creating Project")
        # place the project in the global namespace
        if "PROJECT" in kernel.GlobalObjects:
            kernel.GlobalObjects["PROJECT"] = projectcreator.getProject()
        else:
            kernel.GlobalObjects.newKey("PROJECT", "CORE", projectcreator.getProject())
        # set the project title
        if "Title" in kernel.GlobalObjects:
            kernel.GlobalObjects["Title"] = name
        else:
            kernel.GlobalObjects.newKey("Title", "CORE", name)
        # set the current project directory
        if "CurrentProjectDir" in kernel.GlobalObjects:
            kernel.GlobalObjects["CurrentProjectDir"] = path
        else:
            kernel.GlobalObjects.newKey("CurrentProjectDir", "CORE", path)
        # set that there is an open project
        if "ProjectOpen" in kernel.GlobalObjects:
            kernel.GlobalObjects["ProjectOpen"] = True
        else:
            kernel.GlobalObjects.newKey("ProjectOpen", "CORE", True)
        # refresh the interface on project data change
        kernel.StatusBar.updateTask(1, "Refreshing Interface")
        kernel.System.fire_event("RefreshProject")
        kernel.StatusBar.EndTask()
    dlg.Destroy()


def OpenProject(mainwindow, filehistory, path=""):
    kernel.System.fire_event("OpenProject")
    # handle an already open project
    if "ProjectOpen" in kernel.GlobalObjects and kernel.GlobalObjects["ProjectOpen"] and "PROJECT" in kernel.GlobalObjects:
        current_project = kernel.GlobalObjects["PROJECT"]
        if current_project.hasDataChanged() or current_project.hasInfoChanged():
            message = "There are unsaved changes in the currently open project Do you want to save these changes?"
        else:
            message = "Do you want to save the currently open project?"
        caption = "There is already an open project"
        dlg = wx.MessageDialog(mainwindow, message, caption, style=wx.YES_NO |
                               wx.YES_DEFAULT)
        result = dlg.ShowModal()
        if result == wx.YES:
            kernel.Syatem.load("SaveProjectHandler")()
    # now lets open a project
    if path == "":
        # if we open the project through file history we alrady have a path
        # otherwise lets get a path to a project file
        wildcard = "Welder Project File (*.arcproj)|*.arcproj"
        defaultpath = (os.path.join(wx.StandardPaths.Get().GetDocumentsDir(),
                                    "ARC"))
        dlg = wx.FileDialog(mainwindow, message="Choose a file",
                            defaultDir=defaultpath,
                            defaultFile="",
                            wildcard=wildcard,
                            style=wx.FD_OPEN | wx.FD_CHANGE_DIR
                            )
        if dlg.ShowModal() == wx.ID_OK:
            # we got a path lets save it
            path = str(os.path.normpath(dlg.GetPath()))
            # and add it to the file history
            filehistory.AddFileToHistory(path)
        else:
            # they pressed cancel on the dialog? then lets exit with out
            # loading a project
            return

    if "CurrentProjectDir" in kernel.GlobalObjects:
        kernel.GlobalObjects["CurrentProjectDir"] = path
    # get a project loader
    projectloader = ARCProjectLoader()
    # this might take a while lets say we busy
    kernel.StatusBar.BeginTask(2, "Loading Project")
    projectloader.load(path)
    # ok done loading, that was the longest part of it
    kernel.StatusBar.updateTask(1, "Finished Loading Project")
    # place the project in the global namespace
    if "PROJECT" in kernel.GlobalObjects:
        kernel.GlobalObjects["PROJECT"] = projectloader.getProject()
    else:
        kernel.GlobalObjects.newKey("PROJECT", "CORE", projectloader.getProject())
    # set the Project Title
    if "Title" in kernel.GlobalObjects:
        kernel.GlobalObjects[
            "Title"] = projectloader.getProject().getInfo("Title")
    else:
        kernel.GlobalObjects.newKey("Title", "CORE", projectloader.getProject().getInfo("Title"))
    # set the current project directory
    if "CurrentProjectDir" in kernel.GlobalObjects:
        kernel.GlobalObjects["CurrentProjectDir"] = os.path.dirname(path)
    else:
        kernel.GlobalObjects.newKey("CurrentProjectDir", "CORE", os.path.dirname(path))
    # set that there is an open project
    if "ProjectOpen" in kernel.GlobalObjects:
        kernel.GlobalObjects["ProjectOpen"] = True
    else:
        kernel.GlobalObjects.newKey("ProjectOpen", "CORE", True)
    # refresh the interface on project data change
    kernel.StatusBar.updateTask(1, "Refreshing Interface")
    kernel.System.fire_event("RefreshProject")
    kernel.StatusBar.EndTask()


def SaveProject():
    kernel.System.fire_event("SaveProject")
    if "PROJECT" in kernel.GlobalObjects and (kernel.GlobalObjects["PROJECT"] is not None):
        project = kernel.GlobalObjects["PROJECT"]
        if "CurrentProjectDir" in kernel.GlobalObjects and not (kernel.GlobalObjects["CurrentProjectDir"] == ""):
            path = kernel.GlobalObjects["CurrentProjectDir"]
        else:
            path = os.path.join(
                wx.StandardPaths.Get().GetDocumentsDir(), "ARC", "TEMP_No_project_dirrectory_save")
        projectsaver = ARCProjectSaver(project)
        # this might take a while lets say we busy
        kernel.StatusBar.BeginTask(1, "Saving Project")
        projectsaver.save(path)
        kernel.StatusBar.updateTask(1, "Finished Saving")
        # ok done saving, that was the longest part of it
        kernel.System.fire_event("RefreshProject")
        kernel.StatusBar.EndTask()
    else:
        kernel.Log(
            "No current project, project not saved", "[Save Project Handeler]")


def SaveProjectAS(mainwindow, filehistory):
    kernel.System.fire_event("SaveProject")
    if "PROJECT" in kernel.GlobalObjects and (kernel.GlobalObjects["PROJECT"] is not None):
        project = kernel.GlobalObjects["PROJECT"]
        defaultpath = (os.path.join(wx.StandardPaths.Get().GetDocumentsDir(),
                                    "ARC"))
        dlg = wx.DirDialog(mainwindow, "Choose a Location:",
                           defaultPath=defaultpath,
                           style=wx.DD_DEFAULT_STYLE
                           | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            location = dlg.GetPath()
            path = os.path.join(location, "Project.arcproj")
            filehistory.AddFileToHistory(path)
            projectsaver = ARCProjectSaver()
            # this might take a while lets say we busy
            kernel.StatusBar.BeginTask(1, "Saving Project")
            projectsaver.save(path)
            # ok done saving, that was the longest part of it
            kernel.StatusBar.updateTask(1, "Finished Saving")
            # set the current project directory
            if "CurrentProjectDir" in kernel.GlobalObjects:
                kernel.GlobalObjects[
                    "CurrentProjectDir"] = os.path.dirname(path)
            else:
                kernel.GlobalObjects.newKey("CurrentProjectDir", "CORE", os.path.dirname(path))
            kernel.StatusBar.EndTask()
    else:
        kernel.Log(
            "No current project, project not saved", "[Save AS Project Handeler]")
