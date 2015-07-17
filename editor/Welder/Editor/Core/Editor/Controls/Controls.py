'''
Created on Jan 17, 2011

'''

import wx

import Kernel


class MainStatusBar(wx.StatusBar):

    def __init__(self, parent):
        wx.StatusBar.__init__(self, parent, -1)

        # set the number of fields
        self.SetFieldsCount(4)
        # field 1 is the progressbar
        # field 2 is a spacer
        # field 3 is extra status text
        # field 4 is main status text
        # set the relative widths of the fields
        self.SetStatusWidths([-3, -3, -5, -5])
        # set default text
        self.SetStatusText("Welder - Advanced RPG Creator Editor", 3)
        self.SetStatusText("Idle", 2)
        # create the Progress Bar
        self.progressBar = wx.Gauge(
            self,
            wx.ID_ANY,
            10,
            pos=wx.DefaultPos,
            size=wx.DefaultSize,
            style=wx.GA_HORIZONTAL | wx.GA_SMOOTH
        )
        self.progressBar.Show(False)
        self.Bind(wx.EVT_UPDATE_UI, self.updateUIProgressBar, self.progressBar)

        self.sizeChanged = False
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_IDLE, self.OnIdle)

        # set self as the statusbar
        Kernel.StatusBar.SetStatusBar(self)

    def updateUIProgressBar(self, evt):
        self.updateProgressBarShow()

    def updateProgressBarShow(self):
        if Kernel.StatusBar.TaskRunning:
            self.progressBar.Show(True)
        else:
            self.progressBar.Show(False)

    def SetMainStatus(self, text):
        self.SetStatusText(text, 3)

    def SetExtraStatus(self, text):
        self.SetStatusText(text, 2)

    def updateProgress(self, step):
        self.progressBar.SetValue(step)

    def PulseProgress(self):
        self.progressBar.Pulse()

    def SetProgressRange(self, range):
        self.progressBar.SetRange(range)

    def GetMainStatus(self):
        return self.SetStatusText(3)

    def GetExtraStatus(self):
        return self.GetStatusText(2)

    def GetProgress(self):
        return self.progressBar.GetValue()

    def GetProgressRange(self):
        return self.progressBar.GetRange()

    def OnSize(self, evt):
        self.Reposition()  # for normal size events
        self.sizeChanged = True

    def OnIdle(self, evt):
        if self.sizeChanged:
            self.Reposition()

    # reposition the checkbox
    def Reposition(self):
        rect = self.GetFieldRect(0)
        self.progressBar.SetPosition((rect.x + 2, rect.y + 2))
        self.progressBar.SetSize((rect.width - 4, rect.height - 4))
        self.sizeChanged = False
