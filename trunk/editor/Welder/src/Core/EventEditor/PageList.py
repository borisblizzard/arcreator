
from Boot import WelderImport

Kernel = WelderImport('Kernel')
KM = Kernel.Manager

import wx


class EventListCtrl(wx.HtmlListBox):

    __KNOWN_FILLER = []

    def __init__(self, parent, list):
        wx.HtmlListBox.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_MULTIPLE)
        self.list = list
        self.strip_filler()
        self.SetItemCount(len(self.list))

    def strip_filler(self):
        for command in list(self.list):
            if command.code in self.__KNOWN_FILLER:
                self.list.remove(command)

    def OnGetItem(self, n):
        EventCommandFormater = KM.get_component("EventCommandFormater").object
        html = EventCommandFormater.format(self.list[n])
        return html

    def OnGetItemMarkup(self, n):
        html = self.OnGetItem(n)
        body = '<font face="Courier New" size="3">%s</font>' % html
        return body
