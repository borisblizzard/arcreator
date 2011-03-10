'''
Created on Jan 17, 2011

'''
import os
import sys

import wx



class ImportRMXPProjectDialog (wx.Dialog):

    def __init__(self, parent):

        #pre create
        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, title=u"Import RMXP Data", size=wx.DefaultSize,
                   style=wx.CLOSE_BOX | wx.DEFAULT_DIALOG_STYLE)
        #post create
        self.PostCreate(pre)

        self.cbdict = {}

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        self.Titletext = wx.StaticText(self, wx.ID_ANY,
                                       u"Import RPG Maker XP Data",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.Titletext.Wrap(-1)
        MainSizer.Add(self.Titletext, 0, wx.ALIGN_CENTER | wx.ALIGN_TOP | wx.ALL, 5)

        self.warningText = wx.StaticText(self, wx.ID_ANY,
                                         u"WARNING: Importing data will " \
                                         "overwrite\nany data of that type " \
                                         "already in the \nproject. If you " \
                                         "just created this project\nthen" \
                                         "this is nothing to worry about,\nBut " \
                                         "otherwise be extremely careful! ",
                                         wx.DefaultPosition, wx.DefaultSize,
                                         wx.ALIGN_CENTRE)
        self.warningText.Wrap(-1)
        self.warningText.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(),
                                         70, 90, 92, False, wx.EmptyString))
        self.warningText.SetForegroundColour(wx.Colour(255, 0, 0))

        MainSizer.Add(self.warningText, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        LocationSizer = wx.BoxSizer(wx.VERTICAL)

        self.locationText = wx.StaticText(self, wx.ID_ANY,
                                          u"RMXP Project Location:",
                                          wx.DefaultPosition, wx.DefaultSize,
                                          0)
        self.locationText.Wrap(-1)
        self.locationText.SetHelpText(u"The folder with the RMXP project " \
                                      "from which the data should be imported.")

        LocationSizer.Add(self.locationText, 0, wx.ALL, 5)

        locationCtrlBtnSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.locationTextCtrl = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, (300, -1),
                                             0)
        self.locationTextCtrl.SetHelpText(u"The folder with the RMXP project " \
                                          "from which the data should be imported.")

        locationCtrlBtnSizer.Add(self.locationTextCtrl, 1, wx.ALL, 5)

        self.locationBtn = wx.Button(self, wx.ID_ANY, u"...",
                                     wx.DefaultPosition, wx.Size(25, -1), 0)
        self.locationBtn.SetHelpText(u"Open a dialog to select the folder with " \
                                     "the RMXP project from which the data should " \
                                     "be imported.")

        locationCtrlBtnSizer.Add(self.locationBtn, 0, wx.ALL, 5)

        LocationSizer.Add(locationCtrlBtnSizer, 1, wx.EXPAND, 5)

        MainSizer.Add(LocationSizer, 0, wx.EXPAND, 5)

        self.allCb = wx.CheckBox(self, wx.ID_ANY, u"All", wx.DefaultPosition,
                                 wx.DefaultSize, 0)
        self.allCb.SetHelpText(u"Import all the data from the project.")
        self.allCb.SetValue(True)

        MainSizer.Add(self.allCb, 0, wx.ALL, 5)

        cBoxSizer = wx.GridSizer(2, 3, 0, 0)

        self.actorsCb = wx.CheckBox(self, wx.ID_ANY, u"Actors",
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.actorsCb.SetHelpText(u"Import Actors data.")
        self.cbdict["Actors"] = self.actorsCb

        cBoxSizer.Add(self.actorsCb, 0, wx.ALL, 5)

        self.classesCb = wx.CheckBox(self, wx.ID_ANY, u"Classes",
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.classesCb.SetHelpText(u"Import Classes data.")
        self.cbdict["Classes"] = self.classesCb

        cBoxSizer.Add(self.classesCb, 0, wx.ALL, 5)

        self.skillsCb = wx.CheckBox(self, wx.ID_ANY, u"Skills",
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.skillsCb.SetHelpText(u"Import Skills data.")
        self.cbdict["Skills"] = self.skillsCb

        cBoxSizer.Add(self.skillsCb, 0, wx.ALL, 5)

        self.itemsCb = wx.CheckBox(self, wx.ID_ANY, u"Items",
                                   wx.DefaultPosition, wx.DefaultSize, 0)
        self.itemsCb.SetHelpText(u"Import Items data.")
        self.cbdict["Items"] = self.itemsCb

        cBoxSizer.Add(self.itemsCb, 0, wx.ALL, 5)

        self.weaponsCb = wx.CheckBox(self, wx.ID_ANY, u"Weapons",
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.weaponsCb.SetHelpText(u"Import Weapons data.")
        self.cbdict["Weapons"] = self.weaponsCb

        cBoxSizer.Add(self.weaponsCb, 0, wx.ALL, 5)

        self.armorsCb = wx.CheckBox(self, wx.ID_ANY, u"Armors",
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.armorsCb.SetHelpText(u"Import Armors data.")
        self.cbdict["Armors"] = self.armorsCb

        cBoxSizer.Add(self.armorsCb, 0, wx.ALL, 5)

        self.enemiesCb = wx.CheckBox(self, wx.ID_ANY, u"Enemies",
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.enemiesCb.SetHelpText(u"Import Enemies data.")
        self.cbdict["Enemies"] = self.enemiesCb

        cBoxSizer.Add(self.enemiesCb, 0, wx.ALL, 5)

        self.troopsCb = wx.CheckBox(self, wx.ID_ANY, u"Troops",
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.troopsCb.SetHelpText(u"Import Troops data.")
        self.cbdict["Troops"] = self.troopsCb

        cBoxSizer.Add(self.troopsCb, 0, wx.ALL, 5)

        self.statesCb = wx.CheckBox(self, wx.ID_ANY, u"States",
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.statesCb.SetHelpText(u"Import States data.")
        self.cbdict["States"] = self.statesCb

        cBoxSizer.Add(self.statesCb, 0, wx.ALL, 5)

        self.animationscb = wx.CheckBox(self, wx.ID_ANY, u"Animations",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        self.animationscb.SetHelpText(u"Import Animations data.")
        self.cbdict["Animations"] = self.animationscb

        cBoxSizer.Add(self.animationscb, 0, wx.ALL, 5)

        self.tilesetsCb = wx.CheckBox(self, wx.ID_ANY, u"Tilesets",
                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.tilesetsCb.SetHelpText(u"Import Tilesets data.")
        self.cbdict["Tilesets"] = self.tilesetsCb

        cBoxSizer.Add(self.tilesetsCb, 0, wx.ALL, 5)

        self.commoneventsCb = wx.CheckBox(self, wx.ID_ANY, u"Common Events",
                                          wx.DefaultPosition, wx.DefaultSize,
                                          0)
        self.commoneventsCb.SetHelpText(u"Import Common Events data.")
        self.cbdict["Common Events"] = self.commoneventsCb

        cBoxSizer.Add(self.commoneventsCb, 0, wx.ALL, 5)

        self.systemCb = wx.CheckBox(self, wx.ID_ANY, u"System",
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.systemCb.SetHelpText(u"Import System data.")
        self.cbdict["System"] = self.systemCb

        cBoxSizer.Add(self.systemCb, 0, wx.ALL, 5)

        self.mapsCb = wx.CheckBox(self, wx.ID_ANY, u"Maps",
                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.mapsCb.SetHelpText(u"Import Maps data. Because of the way maps are \
                                internally linked to \ntheir info file it makes \
                                little sense to import individual maps. If you \
                                wish\nto Import individual maps it is best to \
                                copy and paste them from \nanother project.\n")
        self.cbdict["Maps"] = self.mapsCb

        cBoxSizer.Add(self.mapsCb, 0, wx.ALL, 5)

        MainSizer.Add(cBoxSizer, 1, wx.EXPAND, 5)

        BtnSizer = wx.StdDialogButtonSizer()
        self.BtnOK = wx.Button(self, wx.ID_OK)
        BtnSizer.AddButton(self.BtnOK)
        self.BtnCancel = wx.Button(self, wx.ID_CANCEL)
        BtnSizer.AddButton(self.BtnCancel)
        if wx.Platform != "__WXMSW__":
            self.ButtonContextHelp = wx.ContextHelpButton(self)
            BtnSizer.AddButton(self.ButtonContextHelp)
        BtnSizer.Realize();
        MainSizer.Add(BtnSizer, 0, wx.EXPAND, 5)

        self.SetSizer(MainSizer)
        self.Layout()
        self.Fit()

        self.Centre(wx.BOTH)

        self.BindEvents()

    def BindEvents(self):
        for value in self.cbdict.itervalues():
            self.Bind(wx.EVT_UPDATE_UI, self.uiupdate, value)
        self.Bind(wx.EVT_BUTTON, self.OnLocationBtn, self.locationBtn)
        self.Bind(wx.EVT_BUTTON, self.OnOk, self.BtnOK)

    def uiupdate(self, event):
        event.Enable(not self.allCb.GetValue())
        event.Check(self.allCb.GetValue())

    def OnLocationBtn(self, event):
        defaultpath = os.path.expandvars(self.locationTextCtrl.GetValue())
        if defaultpath == "" or not os.path.exists(defaultpath):
            defaultpath = (os.path.join(wx.StandardPaths.Get().
                           GetDocumentsDir(), "RPGXP"))
        dlg = wx.DirDialog(self, "Select the RMXP Project Location:",
                           defaultPath=defaultpath,
                           style=wx.DD_DEFAULT_STYLE
                           | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            self.locationTextCtrl.SetValue(dlg.GetPath())
        dlg.Destroy()

    def GetFilesList(self):
        list = []
        if self.allCb.GetValue():
            list.append("all")
        else:
            for key, value in self.cbdict:
                if value.GetValue():
                    list.append(key)
        return list

    def GetLocation(self):
        return self.locationTextCtrl.GetValue()

    def OnOk(self, event):
        result = self.checkdata()
        if result:
            event.Skip()

    def checkdata(self):
        string = os.path.expandvars(self.locationTextCtrl.GetValue())
        if not os.path.exists(string) and not os.path.isdir(string):
            caption = "RPG Maker PY"
            message = "Please provide a valid path to the project location"
            dlg = wx.MessageDialog(self, message, caption,
                                   style=wx.OK | wx.CENTRE
                                   | wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            return False
        checkpath = os.path.join(string, "Game.rxproj")
        if not os.path.exists(checkpath):
            caption = "RPG Maker PY"
            message = "Please provide a path where a RMXP project file " \
                      "can be found"
            dlg = wx.MessageDialog(self, message, caption,
                                   style=wx.OK | wx.CENTRE
                                   | wx.ICON_EXCLAMATION)
            dlg.ShowModal()
            return False
        return True


class ExportRMXPProjectDialog (wx.Dialog):

    def __init__(self, parent):

        #pre create
        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, title=u"Export RMXP Data", size=wx.DefaultSize,
                   style=wx.CLOSE_BOX | wx.DEFAULT_DIALOG_STYLE)
        #post create
        self.PostCreate(pre)

        self.cbdict = {}

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        self.Titletext = wx.StaticText(self, wx.ID_ANY,
                                       u"Export RPG Maker XP Data",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.Titletext.Wrap(-1)
        MainSizer.Add(self.Titletext, 0, wx.ALIGN_CENTER | wx.ALIGN_TOP | wx.ALL, 5)

        LocationSizer = wx.BoxSizer(wx.VERTICAL)

        self.locationText = wx.StaticText(self, wx.ID_ANY,
                                          u"Target Location:",
                                          wx.DefaultPosition, wx.DefaultSize,
                                          0)
        self.locationText.Wrap(-1)
        self.locationText.SetHelpText(u"The folder you wish to export data to")

        LocationSizer.Add(self.locationText, 0, wx.ALL, 5)

        locationCtrlBtnSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.locationTextCtrl = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, (300, -1),
                                             0)
        self.locationTextCtrl.SetHelpText(u"The folder you wish to export data to")

        locationCtrlBtnSizer.Add(self.locationTextCtrl, 1, wx.ALL, 5)

        self.locationBtn = wx.Button(self, wx.ID_ANY, u"...",
                                     wx.DefaultPosition, wx.Size(25, -1), 0)
        self.locationBtn.SetHelpText(u"Open a dialog to select the folder " \
                                     "you wish to export data to")

        locationCtrlBtnSizer.Add(self.locationBtn, 0, wx.ALL, 5)

        LocationSizer.Add(locationCtrlBtnSizer, 1, wx.EXPAND, 5)

        MainSizer.Add(LocationSizer, 0, wx.EXPAND, 5)

        self.allCb = wx.CheckBox(self, wx.ID_ANY, u"All", wx.DefaultPosition,
                                 wx.DefaultSize, 0)
        self.allCb.SetHelpText(u"Export all the data from the project.")
        self.allCb.SetValue(True)

        MainSizer.Add(self.allCb, 0, wx.ALL, 5)

        cBoxSizer = wx.GridSizer(2, 3, 0, 0)

        self.actorsCb = wx.CheckBox(self, wx.ID_ANY, u"Actors",
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.actorsCb.SetHelpText(u"Export Actors data.")
        self.cbdict["Actors"] = self.actorsCb

        cBoxSizer.Add(self.actorsCb, 0, wx.ALL, 5)

        self.classesCb = wx.CheckBox(self, wx.ID_ANY, u"Classes",
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.classesCb.SetHelpText(u"Export Classes data.")
        self.cbdict["Classes"] = self.classesCb

        cBoxSizer.Add(self.classesCb, 0, wx.ALL, 5)

        self.skillsCb = wx.CheckBox(self, wx.ID_ANY, u"Skills",
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.skillsCb.SetHelpText(u"Export Skills data.")
        self.cbdict["Skills"] = self.skillsCb

        cBoxSizer.Add(self.skillsCb, 0, wx.ALL, 5)

        self.itemsCb = wx.CheckBox(self, wx.ID_ANY, u"Items",
                                   wx.DefaultPosition, wx.DefaultSize, 0)
        self.itemsCb.SetHelpText(u"Export Items data.")
        self.cbdict["Items"] = self.itemsCb

        cBoxSizer.Add(self.itemsCb, 0, wx.ALL, 5)

        self.weaponsCb = wx.CheckBox(self, wx.ID_ANY, u"Weapons",
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.weaponsCb.SetHelpText(u"Export Weapons data.")
        self.cbdict["Weapons"] = self.weaponsCb

        cBoxSizer.Add(self.weaponsCb, 0, wx.ALL, 5)

        self.armorsCb = wx.CheckBox(self, wx.ID_ANY, u"Armors",
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.armorsCb.SetHelpText(u"Export Armors data.")
        self.cbdict["Armors"] = self.armorsCb

        cBoxSizer.Add(self.armorsCb, 0, wx.ALL, 5)

        self.enemiesCb = wx.CheckBox(self, wx.ID_ANY, u"Enemies",
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.enemiesCb.SetHelpText(u"Export Enemies data.")
        self.cbdict["Enemies"] = self.enemiesCb

        cBoxSizer.Add(self.enemiesCb, 0, wx.ALL, 5)

        self.troopsCb = wx.CheckBox(self, wx.ID_ANY, u"Troops",
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.troopsCb.SetHelpText(u"Export Troops data.")
        self.cbdict["Troops"] = self.troopsCb

        cBoxSizer.Add(self.troopsCb, 0, wx.ALL, 5)

        self.statesCb = wx.CheckBox(self, wx.ID_ANY, u"States",
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.statesCb.SetHelpText(u"Export States data.")
        self.cbdict["States"] = self.statesCb

        cBoxSizer.Add(self.statesCb, 0, wx.ALL, 5)

        self.animationscb = wx.CheckBox(self, wx.ID_ANY, u"Animations",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        self.animationscb.SetHelpText(u"Export Animations data.")
        self.cbdict["Animations"] = self.animationscb

        cBoxSizer.Add(self.animationscb, 0, wx.ALL, 5)

        self.tilesetsCb = wx.CheckBox(self, wx.ID_ANY, u"Tilesets",
                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.tilesetsCb.SetHelpText(u"Export Tilesets data.")
        self.cbdict["Tilesets"] = self.tilesetsCb

        cBoxSizer.Add(self.tilesetsCb, 0, wx.ALL, 5)

        self.commoneventsCb = wx.CheckBox(self, wx.ID_ANY, u"Common Events",
                                          wx.DefaultPosition, wx.DefaultSize,
                                          0)
        self.commoneventsCb.SetHelpText(u"Export Common Events data.")
        self.cbdict["Common Events"] = self.commoneventsCb

        cBoxSizer.Add(self.commoneventsCb, 0, wx.ALL, 5)

        self.systemCb = wx.CheckBox(self, wx.ID_ANY, u"System",
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.systemCb.SetHelpText(u"Export System data.")
        self.cbdict["System"] = self.systemCb

        cBoxSizer.Add(self.systemCb, 0, wx.ALL, 5)

        self.mapsCb = wx.CheckBox(self, wx.ID_ANY, u"Maps",
                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.mapsCb.SetHelpText(u"Export Maps data.")

        self.cbdict["Maps"] = self.mapsCb

        cBoxSizer.Add(self.mapsCb, 0, wx.ALL, 5)

        MainSizer.Add(cBoxSizer, 1, wx.EXPAND, 5)

        BtnSizer = wx.StdDialogButtonSizer()
        self.BtnOK = wx.Button(self, wx.ID_OK)
        BtnSizer.AddButton(self.BtnOK)
        self.BtnCancel = wx.Button(self, wx.ID_CANCEL)
        BtnSizer.AddButton(self.BtnCancel)
        if wx.Platform != "__WXMSW__":
            self.ButtonContextHelp = wx.ContextHelpButton(self)
            BtnSizer.AddButton(self.ButtonContextHelp)
        BtnSizer.Realize();
        MainSizer.Add(BtnSizer, 0, wx.EXPAND, 5)

        self.SetSizer(MainSizer)
        self.Layout()
        self.Fit()

        self.Centre(wx.BOTH)

        self.BindEvents()

    def BindEvents(self):
        for value in self.cbdict.itervalues():
            self.Bind(wx.EVT_UPDATE_UI, self.uiupdate, value)
        self.Bind(wx.EVT_BUTTON, self.OnLocationBtn, self.locationBtn)
        self.Bind(wx.EVT_BUTTON, self.OnOk, self.BtnOK)

    def uiupdate(self, event):
        event.Enable(not self.allCb.GetValue())
        event.Check(self.allCb.GetValue())

    def OnLocationBtn(self, event):
        defaultpath = os.path.expandvars(self.locationTextCtrl.GetValue())
        if defaultpath == "" or not os.path.exists(defaultpath):
            defaultpath = (os.path.join(wx.StandardPaths.Get().
                           GetDocumentsDir(), "RPGXP"))
        dlg = wx.DirDialog(self, "Select the Target Location:",
                           defaultPath=defaultpath,
                           style=wx.DD_DEFAULT_STYLE
                           | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            self.locationTextCtrl.SetValue(dlg.GetPath())
        dlg.Destroy()

    def GetFilesList(self):
        list = []
        if self.allCb.GetValue():
            list.append("all")
        else:
            for key, value in self.cbdict:
                if value.GetValue():
                    list.append(key)
        return list

    def GetLocation(self):
        return self.locationTextCtrl.GetValue()

    def OnOk(self, event):
        result = self.checkdata()
        if result:
            event.Skip()

    def checkdata(self):
        string = os.path.expandvars(self.locationTextCtrl.GetValue())
        if not os.path.exists(string) and not os.path.isdir(string):
            caption = "RPG Maker PY"
            message = "Please provide a valid path to the export location"
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
    #import Core

    provider = wx.SimpleHelpProvider()
    wx.HelpProvider.Set(provider)


    app = wx.PySimpleApp()
    frame = ImportRMXPProjectDialog(None)
    frame.Show()
    app.MainLoop()
