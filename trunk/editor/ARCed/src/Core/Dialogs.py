'''
Created on Jan 16, 2011


'''
import os
import sys
import ConfigParser

import wx

import Kernel
from Kernel import Manager as KM


class NewProjectDialog(wx.Dialog):

    def __init__(self, parent):
        #pre create
        #(500, 170)
        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, title="New ARCed Project", size=wx.DefaultSize,
                   style=wx.CLOSE_BOX | wx.DEFAULT_DIALOG_STYLE)
        #post create
        self.PostCreate(pre)

        #set up properties
        self.name = ""
        self.location = (os.path.join(wx.StandardPaths.Get().
                         GetDocumentsDir(), "ARC"))
        if not os.path.exists(self.location) and not os.path.isdir(self.location):
            os.mkdir(self.location)
        founddir = False
        dirname = "Project"
        startnum = 0
        while not founddir:
            startnum += 1
            dername = "Project" + str(startnum)
            pathtocheck = os.path.join(self.location, dername)
            if not os.path.exists(pathtocheck) and not os.path.isdir(pathtocheck):
                founddir = True
                dirname = dername
        self.location = os.path.join(self.location, dirname)
        self.type = ""
        self.internaltextchange = False

        #layout the dialog
        self.LayoutDialog()

    def LayoutDialog(self):
        #layout the dialog
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        DialogSizer = wx.BoxSizer(wx.VERTICAL)

        TopSizer = wx.BoxSizer(wx.HORIZONTAL)

        nameSizer = wx.BoxSizer(wx.VERTICAL)

        staticBox = wx.StaticBox(self, wx.ID_ANY, label="Type", name="Type")
        templatesizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.templateRadiobt = wx.RadioButton(self, wx.ID_ANY, 'From Template', style=wx.RB_GROUP)
        templatesizer.Add(self.templateRadiobt, 0, wx.ALL, 5)

        RTPFunctions = KM.get_component("ARCRTPFunctions").object
        templatefiles = RTPFunctions.GetTemplateList()
        templates = {}
        templateList = []
        for file in templatefiles:
            name = self.getTemplateProjectName(file)
            templates[name] = file
            templateList.append(name)

        index = 0
        for name in templateList:
            if "default".lower() in name.lower():
                index = templateList.index(name)
                break
        
        self.TemplateChoice = wx.Choice(self, wx.ID_ANY, choices=[])
        self.TemplateChoice.Append(templateList[index], templates[templateList[index]]) 

        for i in range(len(templateList)):
            if i == index: continue
            self.TemplateChoice.Append(templateList[i], templates[templateList[i]]) 
        self.TemplateChoice.Select(0)

        templatesizer.Add(self.TemplateChoice, 0, wx.ALL, 5)

        self.BlankProjectRadiobt = wx.RadioButton(self, wx.ID_ANY, 'Blank Project')

        TypeSizer = wx.StaticBoxSizer(staticBox, wx.VERTICAL)
        TypeSizer.Add(templatesizer, 1, wx.ALL|wx.EXPAND, 0)
        TypeSizer.Add(self.BlankProjectRadiobt, 1, wx.ALL|wx.EXPAND, 5)

        TopSizer.Add(TypeSizer, 0, wx.ALL|wx.EXPAND, 5)

        self.nameText = wx.StaticText(self, wx.ID_ANY, "Project Name:",
                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.nameText.Wrap(-1)
        self.nameText.SetHelpText("The name of the project.")

        nameSizer.Add(self.nameText, 1, wx.ALL|wx.EXPAND, 5)

        self.nameTextCtrl = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                        wx.DefaultPosition, (350, -1), 0)
        self.nameTextCtrl.SetHelpText("The name of the project.")

        nameSizer.Add(self.nameTextCtrl, 0, wx.ALL|wx.EXPAND, 5)

        TopSizer.Add(nameSizer, 5, wx.ALL|wx.EXPAND, 5)

        DialogSizer.Add(TopSizer, 1, wx.ALL|wx.EXPAND, 5)

        BottomSizer = wx.BoxSizer(wx.HORIZONTAL)

        folderSizer = wx.BoxSizer(wx.VERTICAL)

        self.folderText = wx.StaticText(self, wx.ID_ANY, "Project Folder:",
                                           wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.folderText.Wrap(-1)
        self.folderText.SetHelpText("The name of the folder the project will " \
                                      "be created in.")

        folderSizer.Add(self.folderText, 0, wx.ALL, 5)

        self.folderTextCtrl = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.folderTextCtrl.SetHelpText("The name of the folder the project will " \
                                      "be created in.")
        self.folderTextCtrl.SetValue(os.path.split(self.location)[1])

        folderSizer.Add(self.folderTextCtrl, 0, wx.ALL, 5)

        BottomSizer.Add(folderSizer, 0, wx.EXPAND, 5)

        locationSizer = wx.BoxSizer(wx.VERTICAL)

        self.locationText = wx.StaticText(self, wx.ID_ANY, "Project Location:",
                                           wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.locationText.Wrap(-1)
        self.locationText.SetHelpText("The location in which the project will " \
                                      "be created.")

        locationSizer.Add(self.locationText, 0, wx.ALL, 5)

        locationCtrlBtnSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.locationTextCtrl = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, (300, -1), 0)
        self.locationTextCtrl.SetHelpText("The location in which the project " \
                                         "will be created.")
        self.locationTextCtrl.SetValue(self.location)

        locationCtrlBtnSizer.Add(self.locationTextCtrl, 4, wx.ALL, 5)

        self.folderBtn = wx.Button(self, wx.ID_ANY, "...", wx.DefaultPosition,
                                   (25, -1), 0)
        self.folderBtn.SetHelpText("Open a dialog to select the folder.")

        locationCtrlBtnSizer.Add(self.folderBtn, 0, wx.ALL, 5)

        locationSizer.Add(locationCtrlBtnSizer, 1, wx.EXPAND, 5)

        BottomSizer.Add(locationSizer, 5, wx.EXPAND, 5)

        DialogSizer.Add(BottomSizer, 1, wx.EXPAND, 5)

        MainSizer.Add(DialogSizer, 1, wx.EXPAND, 5)

        ButtonSizer = wx.StdDialogButtonSizer()
        self.ButtonOK = wx.Button(self, wx.ID_OK)
        ButtonSizer.AddButton(self.ButtonOK)
        self.ButtonCancel = wx.Button(self, wx.ID_CANCEL)
        ButtonSizer.AddButton(self.ButtonCancel)
        if wx.Platform != "__WXMSW__":
            self.ButtonContextHelp = wx.ContextHelpButton(self)
            ButtonSizer.AddButton(self.ButtonContextHelp)
        ButtonSizer.Realize();
        MainSizer.Add(ButtonSizer, 0, wx.EXPAND, 5)

        self.SetSizer(MainSizer)
        self.Layout()
        self.Fit()

        self.Centre(wx.BOTH)

        #bind events
        self.Bind(wx.EVT_TEXT, self.NameChanged, self.nameTextCtrl)
        self.Bind(wx.EVT_TEXT, self.LocationChanged, self.locationTextCtrl)
        self.Bind(wx.EVT_TEXT, self.FolderChanged, self.folderTextCtrl)
        self.Bind(wx.EVT_BUTTON, self.OnOk, self.ButtonOK)
        self.Bind(wx.EVT_BUTTON, self.OnFolder, self.folderBtn)

    def getTemplateProjectName(self, path):
        config = ConfigParser.ConfigParser()
        config.read(os.path.normpath(path))
        title = config.get("Project", "Title")
        return title

    def NameChanged(self, event):
        self.name = event.GetString()

    def FolderChanged(self, event):
        self.folder = event.GetString()
        if not self.internaltextchange:
            self.location = os.path.join(os.path.split(self.location)[0], self.folder)
            self.internaltextchange = True
            self.locationTextCtrl.SetValue(self.location)
            self.internaltextchange = False

    def LocationChanged(self, event):
        self.location = event.GetString()
        if not self.internaltextchange:
            self.folder = os.path.split(self.location)[1]
            self.internaltextchange = True
            self.folderTextCtrl.SetValue(self.folder)
            self.internaltextchange = False

    def OnFolder(self, event):
        defaultpath = os.path.expandvars(self.location)
        if defaultpath == "" or not os.path.exists(defaultpath):
            defaultpath = (os.path.join(wx.StandardPaths.Get().
                           GetDocumentsDir(), "ARC"))
        dlg = wx.DirDialog(self, "Choose a Location:",
                           defaultPath=defaultpath,
                           style=wx.DD_DEFAULT_STYLE
                           | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            self.location = dlg.GetPath()
            self.internaltextchange = True
            self.locationTextCtrl.SetValue(self.location)
            self.folder = os.path.split(self.location)[1]
            self.folderTextCtrl.SetValue(self.folder)
            self.internaltextchange = False
        dlg.Destroy()

    def OnOk(self, event):
        result = self.checkdata()
        if result:
            event.Skip()

    def getdata(self):
        template = (False, "")
        if self.templateRadiobt.GetValue():
            template = (True, self.TemplateChoice.GetClientData(self.TemplateChoice.GetSelection()))
        return (template, self.name, self.location)

    def checkdata(self):
        if self.name.strip() == "":
            caption = "ARCed"
            message = "The project name can't be left blank"
            dlg = wx.MessageDialog(self, message, caption,
                                   style=wx.OK | wx.CENTRE
                                   | wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            return False
        string = os.path.split(os.path.expandvars(self.location))[0]
        if not os.path.exists(string) and not os.path.isdir(string):
            caption = "ARCed"
            message = "Please provide a valid path to the project parent directory."
            dlg = wx.MessageDialog(self, message, caption,
                                   style=wx.OK | wx.CENTRE
                                   | wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            return False
        string = os.path.expandvars(self.location)
        if not os.path.exists(string) and not os.path.isdir(string):
            try:
                os.mkdir(string)
            except Exception:
                caption = "ARCed"
                message = "Failed to make Project folder, please provide a " \
                          "valid folder name."
                dlg = wx.MessageDialog(self, message, caption,
                                       style=wx.OK | wx.CENTRE
                                       | wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                return False
        return True




#=======================================================================
# NOTE: the below is for testing purposes only
#=======================================================================

if __name__ == '__main__':
    import Core

    provider = wx.SimpleHelpProvider()
    wx.HelpProvider.Set(provider)


    app = wx.PySimpleApp()
    frame = NewProjectDialog(None)
    frame.Show()
    app.MainLoop()
