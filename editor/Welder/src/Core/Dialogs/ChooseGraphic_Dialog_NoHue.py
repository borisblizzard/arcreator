import os

import wx
import PIL


import Kernel


RTPFunctions = Core.Cache.RTPFunctions
PILCache = Core.Cache.PILCache


from PyitectConsumes import ChooseGraphic_Dialog_NoHue_Template


class ChooseGraphic_Dialog_NoHue(ChooseGraphic_Dialog_NoHue_Template):

    def __init__(self, parent, folder, current):
        ChooseGraphic_Dialog_NoHue_Template.__init__(self, parent)
        self.glCanvasGraphic.canvas.Bind(wx.EVT_LEFT_DOWN,
                                         Kernel.Protect(self.glCanvas_LeftMouse))
        #self.Centre( wx.BOTH )
        self.glCanvasGraphic.SetDrawMode(5)
        self.ImageList = ['(None)']
        self.ImageList.extend(
            RTPFunctions.GetFileList(os.path.join('Graphics', folder)))
        self.ImageIndex = 0
        if folder == 'Icons':
            self.cache = PILCache.Icon
        elif folder == 'Panoramas':
            self.cache = PILCache.Panorama
        # TODO: Implement the rest...
        if current in self.ImageList:
            self.ImageIndex = self.ImageList.index(current)
        self.listBoxGraphics.AppendItems(self.ImageList)
        self.listBoxGraphics.SetSelection(self.ImageIndex)
        self.RefreshCanvas()

    def RefreshCanvas(self):
        if self.ImageIndex == 0:
            image = PIL.Image.new('RGBA', (32, 32))
        else:
            filename = self.ImageList[self.ImageIndex]
            image = self.cache(filename)
        self.glCanvasGraphic.ChangeImage(image)
        del (image)

    def glCanvas_LeftMouse(self, event):

        print('LEFT DOWN')

    def listBoxGraphics_SelectionChanged(self, event):
        """Changes the image index and refreshes the canvas"""
        self.ImageIndex = event.GetSelection()
        self.RefreshCanvas()

    def GetSelection(self):
        """Returns the filename that was selected by the user"""
        if self.ImageIndex == 0:
            return None
        return self.ImageList[self.ImageIndex]

    def buttonOK_Clicked(self, event):
        """End the dialog and return wx.ID_OK"""
        self.EndModal(wx.ID_OK)

    def buttonCancel_Clicked(self, event):
        """End the dialog and return wx.ID_CANCEL"""
        self.EndModal(wx.ID_CANCEL)
