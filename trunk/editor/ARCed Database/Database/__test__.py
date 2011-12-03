import wx
import Database.Controls
from Database.ScriptEditor import ScriptEditor_Panel

#--------------------------------------------------------------------------------------
# TEST
#--------------------------------------------------------------------------------------

app = wx.PySimpleApp( 0 )
frame = wx.Frame( None, wx.ID_ANY, 'ARCed Script Editor', size=(840,630) )
#frame.CreateStatusBar()
panel = ScriptEditor_Panel( frame )
frame.Centre( wx.BOTH )
frame.Show()
app.MainLoop()