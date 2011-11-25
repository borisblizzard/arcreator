import wx
from ExpGrid_Dialog import ExpGrid_Dialog
from Core.RMXP import RGSS1_RPG as RPG



app = wx.PySimpleApp( 0 )
#frame = wx.Frame( None, wx.ID_ANY, 'Configuration Manager', size=(400,300) )
#panel = MyPanel( frame )
#frame.CenterOnScreen()
#frame.Show()
actor = RPG.Actor()
dlg = ExpGrid_Dialog(None, actor)
dlg.ShowModal()
app.MainLoop()