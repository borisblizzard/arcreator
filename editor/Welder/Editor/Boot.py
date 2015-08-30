#!/usr/bin/env python
"""
The main Boot code,
shows a splash screen during load
loads genral and plugin configuration
builds the plugin system
loads the main window
"""
import site
import sys
import os

# process .pth files
paths = sys.path[:]
for path in paths:
    if os.path.isdir(path):
        print("Processing site Dirs", path)
        site.addsitedir(path)

import os
import json
import yaml
import warnings
from pathlib import Path


import wx

import welder_kernel as kernel

import wx.lib.inspection


class ARCSplashScreen(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Welder",
                          style=wx.FRAME_SHAPED | wx.NO_BORDER)

        self.hasShape = False
        self.delta = wx.Point(0, 0)

        icon = Path(kernel.GlobalObjects["Program_Dir"], 'icon.ico')
        ico = wx.Icon(str(icon), wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)

        # Load the image
        splash = Path(kernel.GlobalObjects["Program_Dir"], 'splash.png')
        image = wx.Image(str(splash), wx.BITMAP_TYPE_PNG)
        self.bmp = wx.Bitmap(image)

        self.SetClientSize((self.bmp.GetWidth(), self.bmp.GetHeight()))
        self.CenterOnScreen()

        dc = wx.ClientDC(self)
        self.Paint(dc)

        self.SetWindowShape()

        textctl_size = (self.bmp.GetWidth() // 2 + 32,
                        self.bmp.GetHeight() // 4 - 32)
        textctl_pos = (16, self.bmp.GetHeight() / 4 * 3 + 8)

        gauge_size = (self.bmp.GetWidth() // 2 + 32, 14)
        gauge_pos = (16, self.bmp.GetHeight() - 20)

        self.logctl = wx.TextCtrl(
            self, wx.ID_ANY, "", textctl_pos, textctl_size,
            wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_DONTWRAP)

        self.gaugectl = wx.Gauge(
            self, wx.ID_ANY, 100, gauge_pos, gauge_size, wx.GA_HORIZONTAL)
        self.gaugectl.Pulse()

        self.logctl.SetSize(textctl_size)
        self.logctl.SetPosition(textctl_pos)

        self.gaugectl.SetSize(gauge_size)
        self.gaugectl.SetPosition(gauge_pos)

        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnMouseMove)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_WINDOW_CREATE, self.SetWindowShape)
        self.Bind(wx.EVT_CLOSE, self.OnClose, self)

    def SetWindowShape(self, evt=None):
        r = wx.Region(self.bmp)
        self.hasShape = self.SetShape(r)

    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        self.Paint(dc)

    def Paint(self, dc):

        dc.DrawBitmap(self.bmp, 0, 0, True)

        string1 = "Version: %s" % kernel.VERSION
        string2 = "\n %s %s (%s)" % (kernel.COPYRIGHT,
                                     kernel.AUTHOR,
                                     kernel.EMAIL)

        dc.SetFont(wx.Font(wx.FontInfo(9)))
        dc.SetTextBackground(wx.Colour(0, 0, 0))
        dc.SetTextForeground(wx.Colour(255, 255, 255))

        text_size1 = dc.GetFullMultiLineTextExtent(string2)
        text_x = self.bmp.GetWidth() - text_size1[0] - 2
        text_y = self.bmp.GetHeight() - text_size1[1] - 2

        dc.DrawText(string2, text_x, text_y)

        text_size2 = dc.GetFullMultiLineTextExtent(string1)
        text_x = self.bmp.GetWidth() - text_size2[0] - 2
        text_y = self.bmp.GetHeight() - text_size2[1] - text_size1[2] - 2

        dc.DrawText(string1, text_x, text_y)

    def OnLeftDown(self, evt):
        self.CaptureMouse()
        pos = self.ClientToScreen(evt.GetPosition())
        origin = self.GetPosition()
        self.delta = wx.Point(pos.x - origin.x, pos.y - origin.y)

    def OnMouseMove(self, evt):
        if evt.Dragging() and evt.LeftIsDown():
            pos = self.ClientToScreen(evt.GetPosition())
            newPos = (pos.x - self.delta.x, pos.y - self.delta.y)
            self.Move(newPos)

    def OnLeftUp(self, evt):
        if self.HasCapture():
            self.ReleaseMouse()

    def getWXConfig(self):
        wx_config = wx.FileConfig(
            appName="Welder",
            vendorName="arc@chaos-project.com",
            localFilename=os.path.join(kernel.GetConfigFolder(),
                                       "filehistory.cfg"))
        if "WX_config" in kernel.GlobalObjects:
            kernel.GlobalObjects["WX_config"] = wx_config
        else:
            kernel.GlobalObjects.newKey("WX_config", "CORE", wx_config)

    def getPluginConfig(self):
        try:
            programpath = Path(
                kernel.GlobalObjects["Program_Dir"], "plugins.cfg")
            userpath = Path(kernel.GetConfigFolder(), "plugins.cfg")

            if programpath.exists():
                with programpath.open() as f:
                    kernel.PluginCFG.updateProgram(yaml.load(f))
            if userpath.exists():
                with userpath.open() as f:
                    kernel.PluginCFG.updateUser(yaml.load(f))
        except:
            # we can theoreticly continue even with out plugin defaults, log
            # and continue
            kernel.Log("Error Loading Plugin Configuration",
                       "[Main]", True, True)

    def getGenralConfig(self):
        try:
            programpath = Path(
                kernel.GlobalObjects["Program_Dir"], "welder.cfg")
            userpath = Path(kernel.GetConfigFolder(), "welder.cfg")

            if programpath.exists():
                with programpath.open() as f:
                    kernel.Config.updateProgram(yaml.load(f))
            if userpath.exists():
                with userpath.open() as f:
                    try:
                        kernel.Config.updateUser(yaml.load(f))
                    except:
                        kernel.Log(
                            "Can not load user welder configuration",
                            "[BOOT]",
                            inform=True,
                            error=True)
        except:
            kernel.Log("Error Loading Configuration", "[Main]", True, True)
            # sadly there is also a ton of things that won't work if the genral
            # configuration didn't load properly so we have to exit
            wx.Exit()

    def buildPluginSystem(self):
        try:
            # build the system setting up the plugin configuration
            kernel.buildSystem(kernel.PluginCFG.getUnified())

            # bind some plugin system informative events
            # to the kernel Log
            kernel.System.bind_event('plugin_found', self.onPluginFound)
            kernel.System.bind_event('plugin_loaded', self.onPluginLoad)
            kernel.System.bind_event('component_loaded', self.onComponentLoad)

            # search the Core for all Core plugins
            kernel.System.search(str(
                Path(kernel.GlobalObjects["Program_Dir"], "Core")))
            # kernel.System.plugins curently contains all plugins found inside
            # the Core, we want to enable all of these
            corePlugs = [
                kernel.System.plugins[n][v]
                for n in kernel.System.plugins
                for v in kernel.System.plugins[n]]
            kernel.System.enable_plugins(corePlugs)

            # search the user Plugin folder for plugins
            kernel.System.search(kernel.GetPluginFolder())
            # the new plugins can be filtered according to the
            # user's white & black lists in the config
            # TODO impliment user plugin enabeling
        except:
            kernel.Log("Error Loading Plugins", "[Main]", True, True)
            # we can't recover from this so exit out
            wx.Exit()

    def Do_Setup(self):
        # load up the editor

        self.getWXConfig()

        # load the plugin configuration
        self.getPluginConfig()

        # load the genral configuration
        self.getGenralConfig()

        # build the plugin system
        self.buildPluginSystem()

        # filter out the pyitect warnings about defaults, we dont really care
        warnings.filterwarnings('ignore', module="pyitect")

        # ok first bind our close method to a system event to be fired when the
        # main editor is fully loaded
        kernel.System.bind_event("EditorReady", self.Close)

        # load up the main editor component and show the window
        MainWindow = kernel.System.load("EditorMainWindow")
        editor = MainWindow(None, wx.ID_ANY, 'Welder')
        if "EditorMainWindow" in kernel.GlobalObjects:
            kernel.GlobalObjects["EditorMainWindow"] = editor
        else:
            kernel.GlobalObjects.newKey("EditorMainWindow", "CORE", editor)

    def OnClose(self, event):
        # unbind events, we dont want them called with the window destroied
        kernel.System.unbind_event('plugin_found', self.onPluginFound)
        kernel.System.unbind_event('plugin_loaded', self.onPluginLoad)
        kernel.System.unbind_event('component_loaded', self.onComponentLoad)
        event.Skip()

    def onPluginFound(self, path, plugin):
        self.log("Plugin '%s' found at '%s'" % (plugin, path))

    def onPluginLoad(self, plugin, plugin_required, component_needed):
        self.log(
            "Plugin '%s' was loaded by plugin '%s' "
            "during a request for the '%s' component"
            % (plugin, plugin_required, component_needed))

    def onComponentLoad(self, component, plugin_required, plugin_loaded):
        self.log(
            "Component '%s' loaded, required by plugin '%s', "
            "loaded from plugin '%s'"
            % (component, plugin_required, plugin_loaded))

    def log(self, message):
        self.logctl.AppendText(message + "\n")
        self.gaugectl.Pulse()
        wx.SafeYield()

    def Bindpyxal(self):
        pyxal = kernel.System.load("pyxal")
        if pyxal is not None:
            pyxal.Init(self.frame.GetHandle(), True)

        # wx.lib.inspection.InspectionTool().Show()


class ARC_App(wx.App):

    def OnInit(self):
        self.SetAppName("Welder")

        self.SplashScreen = ARCSplashScreen()
        self.SplashScreen.Show()
        self.fc = wx.CallLater(
            1, kernel.Protect(self.SplashScreen.Do_Setup, exit_on_fail=True))

        self.keepGoing = True
        return True


def Run(programDir, argv):
    if "ARGV" in kernel.GlobalObjects:
        kernel.GlobalObjects["ARGV"] = argv
    else:
        kernel.GlobalObjects.newKey("ARGV", "CORE", argv)

    if "Program_Dir" in kernel.GlobalObjects:
        kernel.GlobalObjects["Program_Dir"] = programDir
    else:
        kernel.GlobalObjects.newKey("Program_Dir", "CORE", programDir)

    print("[BOOT] Programming running in %s" % programDir)
    print("[BOOT] Running with arguments: %s" % argv)

    provider = wx.SimpleHelpProvider()
    wx.HelpProvider.Set(provider)

    app = ARC_App(False)
    # start up the app, we wont be comming back till the app is closed
    app.MainLoop()

    kernel.GlobalObjects["WX_config"].Flush()
    # we want to clean up pyxal as much as we can
    # it's dead now anyway as the window it was bound to is gone
    # try:
    #     pyxal = kernel.System.load("pyxal")
    #     if pyxal is not None:
    #         pyxal.Destroy()
    # except:
    #     kernel.Log("Error destroying pyxal Binding", "[Main]", error=True)
    # lets try to save the user's current config before we leave
    # try:
    #     ConfigManager.SaveConfig()
    # except:
    #     kernel.Log("Error saving Configs", "[Main]", error=True)
