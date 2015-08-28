import wx

import Kernel


class MapEditorToolbar(wx.ToolBar):

    def __init__(self, parent, map, style=wx.TB_HORIZONTAL | wx.NO_BORDER | wx.TB_FLAT):
        '''Toolbar for the map editor'''
        super(MapEditorToolbar, self).__init__(parent, style=style)

        self.map = map
        self.mapwin = None
        self.layers = self.map.data.getShape()[2]
        self.layerChoiceIDs = {}
        self.layerSet = False
        self.zoomSet = False
        self.SetupToolIDs()
        self.SetupTools()
        self.BindToolEvents()

    def SetupTools(self):
        tsize = (16, 16)
        new_bmp = wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR, tsize)
        self.SetToolBitmapSize(tsize)
        self.SetToolSeparation(10)
        self.SetMargins((4, 4))
        # add layer tools
        # generate choice list
        layerChoices = self.GenLayerChoices()
        self.layerChoice = wx.Choice(
            self, wx.ID_ANY, size=(-1, -1), choices=layerChoices)
        self.layerChoice.SetSelection(0)
        self.AddControl(self.layerChoice)
        # self.AddSeparator()
        # a dimlayers choice box
        self.dimLayersCB = wx.CheckBox(self, label="Dim Layers")
        self.dimLayersCB.SetValue(True)
        self.AddControl(self.dimLayersCB)
        self.AddSeparator()
        # a zoom slider
        zoomChoices = self.GenZoomChoices()
        self.zoomChoice = wx.Choice(
            self, wx.ID_ANY, size=(-1, -1), choices=zoomChoices)
        self.zoomChoice.SetSelection(1)
        self.AddControl(self.zoomChoice)
        self.Realize()

    def GenLayerChoices(self):
        choices = []
        self.layerChoiceIDs = {}
        for z in range(self.map.data.getShape()[2]):
            choice = "Layer %s" % (z + 1)
            self.layerChoiceIDs[choice] = z
            choices.append(choice)
        self.layerChoiceIDs["Event Layer"] = self.map.data.getShape()[2] + 1
        choices.append("Event Layer")
        return choices

    def GenZoomChoices(self):
        choices = []
        self.zoomChoiceIDs = {}
        values = [['2x', 2.0], ['1x', 1.0], ['1/2x', 1.0 / 2.0],  # ['1/3x', 1.0/3.0],
                  ['1/4x', 1.0 / 4.0], ]  # ['1/5x', 1.0/5.0]]
        for z in values:
            self.zoomChoiceIDs[z[0]] = z[1]
            choices.append(z[0])
        return choices

    def BindToolEvents(self):
        # layer choice
        self.Bind(wx.EVT_CHOICE, self.OnLayerChoice, self.layerChoice)
        self.Bind(wx.EVT_UPDATE_UI, self.updateLayerChoices, self.layerChoice)
        # dim layers box
        self.Bind(wx.EVT_CHECKBOX, self.OnDimLayersChoice, self.dimLayersCB)
        # zoom choice
        self.Bind(wx.EVT_CHOICE, self.OnZoomChoice, self.zoomChoice)
        self.Bind(wx.EVT_UPDATE_UI, self.updateZoomChoice, self.zoomChoice)

    def SetupToolIDs(self):
        self.EventLayerID = 4
        self.PenID = 5
        self.RecID = 6
        self.ElipID = 7
        self.BucketID = 8
        self.SelectID = 9

    def OnDimLayersChoice(self, event):
        if self.mapwin is not None:
            self.mapwin.SetLayerDimming(event.IsChecked())

    def OnLayerChoice(self, event):
        self.layerSet = False
        if self.mapwin is not None:
            self.layerSet = True
            layer = self.layerChoiceIDs[
                self.layerChoice.GetItems()[self.layerChoice.GetSelection()]]
            self.mapwin.SetActiveLayer(layer)

    def OnZoomChoice(self, event):
        self.zoomSet = False
        if self.mapwin is not None:
            self.zoomSet = True
            zoom = self.zoomChoiceIDs[
                self.zoomChoice.GetItems()[self.zoomChoice.GetSelection()]]
            self.mapwin.SetZoom(zoom)

    def updateLayerChoices(self, event):
        if not(self.layers == self.map.data.getShape()[2]):
            self.layers = self.map.data.getShape()[2]
            choices = self.GenLayerChoices()
            self.layerChoice.SetItems(choices)
        if (self.mapwin is not None) and (not self.layerSet):
            self.layerSet = True
            selection = self.layerChoice.GetSelection()
            items = self.layerChoice.GetItems()
            layer = self.layerChoiceIDs[items[selection]]
            self.mapwin.SetActiveLayer(layer)

    def updateZoomChoice(self, event):
        if (self.mapwin is not None) and (not self.zoomSet):
            self.zoomSet = True
            selection = self.zoomChoice.GetSelection()
            items = self.zoomChoice.GetItems()
            layer = self.zoomChoiceIDs[items[selection]]
            self.mapwin.SetZoom(layer)
