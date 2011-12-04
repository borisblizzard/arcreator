import sys, os, shutil


# Remove config is it exists
path = os.path.join(os.path.expandvars('%PROGRAMDATA%'), 'Chaos Project')
shutil.rmtree(path)

dirName = os.path.dirname(os.path.abspath(__file__))
editorDir = os.path.split(os.path.split(dirName)[0])[0]
editorDir = os.path.join(editorDir, 'ARCed', 'src')  
sys.path.append(editorDir)

import wx
import Database.Controls
from Database.ScriptEditor import ScriptEditor_Panel


import Main
Main.ConfigManager.LoadConfig()
import Kernel
from Kernel import Manager as KM

common = os.path.expandvars('%COMMONPROGRAMFILES%')
rtpDir = os.path.join(common, 'Enterbrain', 'RGSS', 'Standard')
Kernel.GlobalObjects.get_value("ARCed_config").get_section("RTPs").set('RMXP', rtpDir)
TEST_PATH = os.path.join(editorDir, "RTP", "Templates", "Default Project", "Default Project.arcproj")

projectloader = KM.get_component("ARCProjectLoader").object()
projectloader.load(TEST_PATH)
if Kernel.GlobalObjects.has_key("PROJECT"):
	Kernel.GlobalObjects.set_value("PROJECT", projectloader.getProject())
else:
	Kernel.GlobalObjects.request_new_key("PROJECT", "CORE", projectloader.getProject())
if Kernel.GlobalObjects.has_key("Title"):
	Kernel.GlobalObjects.set_value("Title", projectloader.getProject().getInfo("Title"))
else:
	Kernel.GlobalObjects.request_new_key("Title", "CORE", projectloader.getProject().getInfo("Title"))
if Kernel.GlobalObjects.has_key("CurrentProjectDir"):
	Kernel.GlobalObjects.set_value("CurrentProjectDir", os.path.dirname(TEST_PATH))
else:
	Kernel.GlobalObjects.request_new_key("CurrentProjectDir", "CORE", os.path.dirname(TEST_PATH))
if Kernel.GlobalObjects.has_key("ProjectOpen"):
	Kernel.GlobalObjects.set_value("ProjectOpen", True)
else:
	Kernel.GlobalObjects.request_new_key("ProjectOpen", "CORE", True)

app = wx.PySimpleApp( 0 )
frame = wx.Frame( None, wx.ID_ANY, 'ARCed Script Editor', size=(940,640) )
#frame.CreateStatusBar()
panel = ScriptEditor_Panel( frame )
frame.Centre( wx.BOTH )
frame.Show()
app.MainLoop()