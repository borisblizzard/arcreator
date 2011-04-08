'''
Created on Jan 17, 2011

'''

import os
import sys

import wx

try:
    from agw import aui
except ImportError: # if it's not there locally, try the wxPython lib.
    import wx.lib.agw.aui as aui

import Kernel
from Kernel import Manager as KM

class MainToolbar(object):
    def __init__(self, toolbar, mainwindow):
        self.toolbar = toolbar
        self.mainwindow = mainwindow

        self.toolbar.SetToolBitmapSize(wx.Size(16, 16))

        #get bitmaps
        newbmp = wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR, (16, 16))
        openbmp = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, (16, 16))
        savebmp = wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR, (16, 16))
        undobmp = wx.ArtProvider.GetBitmap(wx.ART_UNDO, wx.ART_TOOLBAR, (16, 16))
        redobmp = wx.ArtProvider.GetBitmap(wx.ART_REDO, wx.ART_TOOLBAR, (16, 16))
        copybmp = wx.ArtProvider.GetBitmap(wx.ART_COPY, wx.ART_TOOLBAR, (16, 16))
        cutbmp = wx.ArtProvider.GetBitmap(wx.ART_CUT, wx.ART_TOOLBAR, (16, 16))
        pastebmp = wx.ArtProvider.GetBitmap(wx.ART_PASTE, wx.ART_TOOLBAR, (16, 16))
        #set up ids
        self.newid = wx.NewId()
        self.openid = wx.NewId()
        self.saveid = wx.NewId()
        self.redoid = wx.NewId()
        self.undoid = wx.NewId()
        self.copyid = wx.NewId()
        self.cutid = wx.NewId()
        self.pasteid = wx.NewId()
        #add the tools
        self.toolbar.AddSimpleTool(self.newid, "New", newbmp,
                                   "Create a new project")
        self.toolbar.AddSimpleTool(self.openid, "Open", openbmp,
                                   "Open a RMPY Project")
        self.toolbar.AddSimpleTool(self.saveid, "Save", savebmp,
                                   "Save the current Project")
        self.toolbar.AddSeparator()
        self.toolbar.AddSimpleTool(self.undoid, "Undo", undobmp,
                                   "Undo last action")
        self.toolbar.AddSimpleTool(self.redoid, "Redo", redobmp,
                                   "Redo last action")
        self.toolbar.AddSeparator()
        self.toolbar.AddSimpleTool(self.cutid, "Cut", cutbmp,
                           "Cut selection and copy to the clipboard")
        self.toolbar.AddSimpleTool(self.copyid, "Copy", copybmp,
                           "Copy selection to the clipboard")
        self.toolbar.AddSimpleTool(self.pasteid, "Paste", pastebmp,
                           "Paste data from the clipboard")
        self.toolbar.Realize()

        self.toolbar.Bind(wx.EVT_TOOL, self.OnNew, id=self.newid)
        self.toolbar.Bind(wx.EVT_TOOL, self.OnOpen, id=self.openid)
        self.toolbar.Bind(wx.EVT_TOOL, self.OnSave, id=self.saveid)
        self.toolbar.Bind(wx.EVT_UPDATE_UI, self.uiupdate, id=self.saveid)

        self.toolbar.Bind(wx.EVT_TOOL, self.OnUndo, id=self.undoid)
        self.toolbar.Bind(wx.EVT_TOOL, self.OnRedo, id=self.redoid)

        self.toolbar.Bind(wx.EVT_TOOL, self.OnCut, id=self.cutid)
        self.toolbar.Bind(wx.EVT_TOOL, self.OnCopy, id=self.copyid)
        self.toolbar.Bind(wx.EVT_TOOL, self.OnPaste, id=self.pasteid)

    def OnNew(self, event):
        newproject = KM.get_component("NewProjectHandler").object
        newproject(self.mainwindow)
        Kernel.Global.FileHistory.Save(Kernel.Global.programconfig) #@UndefinedVariable

    def OnOpen(self, event):
        openproject = KM.get_component("OpenProjectHandler").object
        openproject(self.mainwindow, Kernel.Global.FileHistory)
        Kernel.Global.FileHistory.Save(Kernel.Global.programconfig) #@UndefinedVariable

    def OnSave(self, event):
        saveproject = KM.get_component("SaveProjectHandler").object
        saveproject(self.mainwindow)
        Kernel.Global.FileHistory.Save(Kernel.Global.programconfig) #@UndefinedVariable

    def OnUndo(self, event):
        pass

    def OnRedo(self, event):
        pass

    def OnCopy(self, event):
        pass

    def OnCut(self, event):
        pass

    def OnPaste(self, event):
        pass

    def uiupdate(self, event):
        if Kernel.Global.ProjectOpen:
            event.Enable(True)
        else:
            event.Enable(False)

class MainStatusBar(wx.StatusBar):
    def __init__(self, parent):
        wx.StatusBar.__init__(self, parent, -1)
