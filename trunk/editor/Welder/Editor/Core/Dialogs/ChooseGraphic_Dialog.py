import os

import wx
import PIL


import Kernel


from PyitectConsumes import RTPFunctions
from PyitectConsumes import RTPCache


from PyitectConsumes import ChooseGraphic_Dialog_Template


class ChooseGraphic_Dialog(ChooseGraphic_Dialog_Template):

    def __init__(self, parent, folder, current, hue):
        ChooseGraphic_Dialog_Template.__init__(self, parent)
        self.glCanvasGraphic.canvas.Bind(wx.EVT_LEFT_DOWN,
                                         Kernel.Protect(self.glCanvas_LeftMouse))
        #self.Centre( wx.BOTH )
        self.glCanvasGraphic.SetDrawMode(5)
        self.ImageList = ['(None)']
        self.ImageList.extend(
            RTPFunctions.GetFileList(os.path.join('Graphics', folder)))
        self.ImageIndex = 0
        if folder == 'Characters':
            self.cache = RTPCache.Character
        elif folder == 'Battlers':
            self.cache = RTPCache.Battler
        # TODO: Implement the rest...
        if current in self.ImageList:
            self.ImageIndex = self.ImageList.index(current)
        self.listBoxGraphics.AppendItems(self.ImageList)
        self.listBoxGraphics.SetSelection(self.ImageIndex)
        self.sliderHue.SetValue(hue)
        self.RefreshCanvas()

    def RefreshCanvas(self):
        if self.ImageIndex == 0:
            image = PIL.Image.new('RGBA', (32, 32))
        else:
            filename = self.ImageList[self.ImageIndex]
            hue = self.sliderHue.GetValue()
            image = self.cache(filename, hue)
        self.glCanvasGraphic.ChangeImage(image)
        del (image)

    def glCanvas_LeftMouse(self, event):

        print('LEFT DOWN')

    def listBoxGraphics_SelectionChanged(self, event):
        """Changes the image index and refreshes the canvas"""
        self.ImageIndex = event.GetSelection()
        self.RefreshCanvas()

    def sliderHue_Scrolled(self, event):
        """Refreshes the canvas and redraws with the selected hue rotation"""
        self.RefreshCanvas()
        RTPCache.CacheLimit()

    def GetSelection(self):
        """Returns the filename and hue that was selected by the user"""
        if self.ImageIndex == 0:
            return 0, 0
        return self.ImageList[self.ImageIndex], self.sliderHue.GetValue()

    def buttonOK_Clicked(self, event):
        """End the dialog and return wx.ID_OK"""
        self.EndModal(wx.ID_OK)

    def buttonCancel_Clicked(self, event):
        """End the dialog and return wx.ID_CANCEL"""
        self.EndModal(wx.ID_CANCEL)
