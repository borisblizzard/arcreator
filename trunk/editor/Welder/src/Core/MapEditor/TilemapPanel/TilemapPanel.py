import math

import wx

import pyglet
pyglet.options['shadow_window'] = False
from pyglet import gl

import Kernel

from PyitectConsumes import PygletGLPanel
from PyitectConsumes import TilemapMouseManager
from PyitectConsumes import TilemapEventGrid
from PyitectConsumes import TilemapTileGrid
from PyitectConsumes import Tilemap
from PyitectConsumes import TilemapMouseSprite



class TilemapPanel(PygletGLPanel):

    def __init__(self, parent, map, tilesets, toolbar, id=wx.ID_ANY):
        super(TilemapPanel, self).__init__(parent, id, wx.DefaultPosition, wx.Size(800, 600),
                                           wx.VSCROLL | wx.HSCROLL | wx.SUNKEN_BORDER)

        # set data
        self.map = map
        self.tilesets = tilesets
        self.NeedRedraw = False
        self.activeLayer = 0
        self.toolbar = toolbar
        self.toolbar.mapwin = self
        self.translateX = 0
        self.translateY = 0
        self.onscreenwidth = 0
        self.onscreenheight = 0
        self.zoom = 1.0
        self.drawing = False
        self.ToolMouseMode = False

        self.MouseManager = TilemapMouseManager(self, self.map, self.toolbar)

        # set up scrollbars
        size = self.GetVirtualSizeTuple()
        width = self.map.width * 32
        height = self.map.height * 32
        self.SetScrollbar(wx.HORIZONTAL, 0, size[0], width, refresh=True)
        self.SetScrollbar(wx.VERTICAL, 0, size[1], height, refresh=True)

        # scrollbar event
        self.Bind(wx.EVT_SCROLLWIN_TOP, self.scroll_top)
        self.Bind(wx.EVT_SCROLLWIN_BOTTOM, self.scroll_bottom)
        self.Bind(wx.EVT_SCROLLWIN_LINEUP, self.scroll_lineup)
        self.Bind(wx.EVT_SCROLLWIN_LINEDOWN, self.scroll_linedown)
        self.Bind(wx.EVT_SCROLLWIN_PAGEUP, self.scroll_pageup)
        self.Bind(wx.EVT_SCROLLWIN_PAGEDOWN, self.scroll_pagedown)
        self.Bind(wx.EVT_SCROLLWIN_THUMBTRACK, self.update_scroll_pos)
        self.Bind(wx.EVT_SCROLLWIN_THUMBRELEASE, self.update_scroll_pos)
        # mouse event
        self.canvas.Bind(wx.EVT_LEFT_DOWN, self.OnLeftButtonEvent)
        self.canvas.Bind(wx.EVT_LEFT_UP, self.OnLeftButtonEvent)
        self.canvas.Bind(wx.EVT_MOTION, self.OnLeftButtonEvent)
        self.canvas.Bind(wx.EVT_LEFT_DCLICK, self.OnLeftButtonDEvent)
        # UI update
        self.Bind(wx.EVT_UPDATE_UI, self.update)

    def OnLeftButtonDEvent(self, event):
        if self.onEventLayer():
            mgr = Kernel.GlobalObjects["PanelManager"]
            x, y = self.ConvertEventCoords(event)
            event = self.FindEvent(x, y)
            if event:
                pass
            else:
                pass
            #mgr.dispatchPanel("MainActorsPanel", "Main Actors Panel")

    def FindEvent(self, x, y):
        for event in self.map.events:
            if event.x == x and event.y == y:
                return event
        return None

    def OnLeftButtonEvent(self, event):
        if not self.onEventLayer():
            if not self.drawing:
                self.SetTopLeftXY(event)
            self.SetBottomRightXY(event)
        if event.LeftDown():
            Kernel.System.fire_event("MapEditorMouseLeftDown", event)
            self.SetFocus()
            self.canvas.CaptureMouse()
            if self.onEventLayer():
                self.SetTopLeftXY(event)
            self.drawing = True
        elif event.LeftUp():
            self.canvas.ReleaseMouse()
            # if self.drawing:
            #    self.commitBrush()
            self.drawing = False
        if self.NeedRedraw:
            self.ForceRedraw()
        event.Skip()

    def onEventLayer(self):
        return (self.activeLayer == (self.map.data.getShape()[2] + 1))

    def SetTopLeftXY(self, event):
        x, y = self.ConvertEventCoords(event)
        x = x / int(32 * self.zoom)
        y = y / int(32 * self.zoom)
        self.MouseManager.setTopLeft(x, y)

    def SetBottomRightXY(self, event):
        x, y = self.ConvertEventCoords(event)
        x = x / int(32 * self.zoom)
        y = y / int(32 * self.zoom)
        self.MouseManager.setBottomRight(x, y)

    def ConvertEventCoords(self, event):
        scrollX = self.GetScrollPos(wx.HORIZONTAL)
        scrollY = self.GetScrollPos(wx.VERTICAL)
        newpos = [event.GetX() + scrollX, event.GetY() + scrollY]
        return newpos

    def SetOrigin(self):
        size = self.GetVirtualSizeTuple()
        self.SetScrollbar(wx.HORIZONTAL, self.GetScrollPos(wx.HORIZONTAL), size[0],
                          self.map.width * 32 * self.zoom, refresh=True)
        self.SetScrollbar(wx.VERTICAL, self.GetScrollPos(wx.VERTICAL), size[1],
                          self.map.height * 32 * self.zoom, refresh=True)
        size = self.GetGLExtents()
        if size.width <= 0:
            size.width = 1
        if size.height <= 0:
            size.height = 1
        self.tilemap.updateDimmingSprite(
            int(size.width) + 2, int(size.height) + 2, 1 / self.zoom)
        gl.glViewport(0, 0, size.width, size.height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(0, size.width / self.zoom, 0, size.height / self.zoom, -1, 1)
        x = (-self.GetScrollPos(wx.HORIZONTAL)) / self.zoom
        y = ((-(self.map.height * 32) + size.height / self.zoom) +
             self.GetScrollPos(wx.VERTICAL) / self.zoom)
        gl.glTranslatef(x, y, 0)
        self.translateX = -x + size.width / 2 / self.zoom
        self.translateY = -y + size.height / 2 / self.zoom
        self.onscreenwidth = int(size.width / self.zoom)
        self.onscreenheight = int(size.height / self.zoom)
        self.tilemap.setDimXY(self.translateX - 1, self.translateY + 1)
        gl.glMatrixMode(gl.GL_MODELVIEW)

    def create_objects(self):
        '''create opengl objects when opengl is initialized'''
        table = self.map.data
        self.cache = Kernel.System.load("RTPPygletCache")()
        tileset = self.tilesets[self.map.tileset_id]
        self.tilemap = Tilemap(
            self.cache, table, tileset.tileset_name, tileset.autotile_names)
        self.tileGrid = TilemapTileGrid(self.map)
        self.eventGrid = TilemapEventGrid(self.map, self.cache, tileset.tileset_name)
        self.mouseSprite = TilemapMouseSprite(self.map)
        self.MouseManager.setSprite(self.mouseSprite)
        self.SetActiveLayer(self.activeLayer, True)

    def update_object_resize(self, width, height):
        '''called when the window receives only if opengl is initialized'''
        # update the scrollbar widths
        self.SetOrigin()

    def draw_objects(self):
        '''called in the middle of ondraw after the buffer has been cleared'''
        self.tilemap.update()
        shape = self.map.data.getShape()
        x = math.ceil(self.GetScrollPos(wx.HORIZONTAL) / 32.0 / self.zoom) - 1
        if x < 0:
            x = 0
        if x > shape[0] - 1:
            x = shape[0] - 1
        y = math.ceil(self.GetScrollPos(wx.VERTICAL) / 32.0 / self.zoom) - 1
        if y < 0:
            y = 0
        if y > shape[1] - 1:
            y = shape[1] - 1
        width = math.ceil(self.onscreenwidth / 32.0) + 1
        if width > shape[0]:
            width = shape[0]
        height = math.ceil(self.onscreenheight / 32.0) + 1
        if height > shape[1]:
            height = shape[1]
        self.tilemap.Draw(x, y, width, height)
        if self.activeLayer == (shape[2] + 1):
            self.tileGrid.Draw(x, y, width, height)
            self.eventGrid.update()
            self.eventGrid.Draw()
        self.mouseSprite.update()
        self.mouseSprite.Draw()

    def update(self, event):
        self.PrepareGL()
        if self.NeedRedraw:
            self.OnDraw()
            self.NeedRedraw = False

    def ForceRedraw(self):
        self.PrepareGL()
        self.OnDraw()
        self.NeedRedraw = False

    def update_scroll_pos(self, event):
        self.OnScroll(event.GetOrientation(), event.GetPosition())
        event.Skip()

    def scroll_lineup(self, event):
        orient = event.GetOrientation()
        pos = self.GetScrollPos(orient)
        new_pos = pos - 1
        if new_pos < 0:
            new_pos = 0
        if new_pos > self.GetScrollRange(orient):
            new_pos = self.GetScrollRange(orient)
        self.OnScroll(orient, new_pos)

    def scroll_linedown(self, event):
        orient = event.GetOrientation()
        pos = self.GetScrollPos(orient)
        new_pos = pos + 1
        if new_pos < 0:
            new_pos = 0
        if new_pos > self.GetScrollRange(orient):
            new_pos = self.GetScrollRange(orient)
        self.OnScroll(orient, new_pos)

    def scroll_pageup(self, event):
        orient = event.GetOrientation()
        pos = self.GetScrollPos(orient)
        new_pos = pos - 32
        if new_pos < 0:
            new_pos = 0
        if new_pos > self.GetScrollRange(orient):
            new_pos = self.GetScrollRange(orient)
        self.OnScroll(orient, new_pos)

    def scroll_pagedown(self, event):
        orient = event.GetOrientation()
        pos = self.GetScrollPos(orient)
        new_pos = pos + 32
        if new_pos < 0:
            new_pos = 0
        if new_pos > self.GetScrollRange(orient):
            new_pos = self.GetScrollRange(orient)
        self.OnScroll(orient, new_pos)

    def scroll_top(self, event):
        print('Scroll Top')

    def scroll_bottom(self, event):
        print('Scroll Bottom')

    def OnScroll(self, orient, pos):
        size = self.GetVirtualSizeTuple()
        if orient == wx.HORIZONTAL:
            thumb = size[0]
            range_s = self.map.width * 32 * self.zoom
        elif orient == wx.VERTICAL:
            thumb = size[1]
            range_s = self.map.height * 32 * self.zoom
        self.PrepareGL()
        self.SetOrigin()
        self.OnDraw()
        self.SetScrollbar(orient, pos, thumb, range_s, refresh=True)

    def SetActiveLayer(self, layer, init=False):
        # if the selected layer is the event layer
        self.tilemap.setDimXY(self.translateX, self.translateY)
        self.activeLayer = layer
        self.tilemap.SetActiveLayer(layer)
        if layer == (self.map.data.getShape()[2] + 1):
            self.MouseManager.setSingleMode(True)
        else:
            self.MouseManager.setSingleMode(self.ToolMouseMode)
        if not init:
            self.OnDraw()

    def SetLayerDimming(self, bool):
        self.tilemap.SetLayerDimming(bool)
        self.SetOrigin()
        self.OnDraw()

    def SetZoom(self, value):
        self.zoom = value
        self.SetOrigin()
        self.OnDraw()