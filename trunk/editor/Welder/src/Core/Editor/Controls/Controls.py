'''
Created on Jan 17, 2011

'''

import wx


import wx.lib.agw.aui as aui
    


# this is for if we need to use pygame ever
#===============================================================================
# #do stuff to use pygame with out a window
# os.environ["SDL_VIDEODRIVER"] = "dummy"
# if 1:
#    #some platforms might need to init the display for some parts of pygame.
#    import pygame
#    pygame.init()
#    screen = pygame.display.set_mode((1, 1))
#===============================================================================

import Kernel


class MainStatusBar(wx.StatusBar):
    def __init__(self, parent):
        wx.StatusBar.__init__(self, parent, -1)

        #set the number of fields
        self.SetFieldsCount(4)
        #field 1 is the progressbar
        #field 2 is a spacer
        #field 3 is extra status text
        #field 4 is main status text
        #set the relative widths of the fields
        self.SetStatusWidths([-3, -3, -5, -5])
        #set default text
        self.SetStatusText("Welder - Advanced RPG Creator Editor", 3)
        self.SetStatusText("Idle", 2)
        #create the Progress Bar
        self.progressBar = wx.Gauge(self, -1, 10, pos=(-1, -1), size=(-1, -1), style=wx.GA_HORIZONTAL|wx.GA_SMOOTH)
        self.progressBar.Show(False)
        self.Bind(wx.EVT_UPDATE_UI, self.UpdateUIProgressBar, self.progressBar)

        self.sizeChanged = False
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_IDLE, self.OnIdle)

        #set self as the statusbar
        Kernel.StatusBar.SetStatusBar(self)

    def UpdateUIProgressBar(self, evt):
        self.UpdateProgressBarShow()

    def UpdateProgressBarShow(self):
        if Kernel.StatusBar.TaskRunning:
            self.progressBar.Show(True)
        else:
            self.progressBar.Show(False)

    def SetMainStatus(self, text):
        self.SetStatusText(text, 3)

    def SetExtraStatus(self, text):
        self.SetStatusText(text, 2)

    def UpdateProgress(self, step):
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
        self.progressBar.SetPosition((rect.x+2, rect.y+2))
        self.progressBar.SetSize((rect.width-4, rect.height-4))
        self.sizeChanged = False

class MapTreeCtrl(wx.TreeCtrl):
    def __init__(self, parent, id, pos, size, edit=False):
        style = wx.TR_DEFAULT_STYLE | wx.NO_BORDER | wx.TR_HAS_BUTTONS
        self.edit = edit
        if self.edit:
            style |= wx.TR_EDIT_LABELS | wx.WANTS_CHARS
        wx.TreeCtrl.__init__(self, parent, id, pos, size, style)
        self.parent = parent
        KM.get_event("RefreshProject").register(self.Refresh_Map_List)
        IconManager = KM.get_component("IconManager").object
        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(IconManager.getBitmap("project_icon"))
        imglist.Add(IconManager.getBitmap("map_icon"))
        self.AssignImageList(imglist)

        root = self.AddRoot("Advanced RPG Creator Project", 0)
        items = []
        self.maps = {}
        self.struct = {0 : []}

        self.Expand(root)

        self.Bind(wx.EVT_WINDOW_DESTROY, self.onClose, self)

    def buildStruct(self):
        project = Kernel.GlobalObjects.get_value("PROJECT")
        mapinfos = project.getData("MapInfos")
        self.struct = {0 : []}
        stack = []
        for key, value in mapinfos.items():
            self.struct[key] = []
            if value.parent_id in self.struct:
                self.struct[value.parent_id].append(key)
            else:
                stack.append([key, value])
        while len(stack) > 0:
            key, value = stack.pop()
            if value.parent_id in self.struct:
                self.struct[value.parent_id].append(key)
            else:
                stack.append([key, value])
        self.sortStruct()

    def sortStruct(self):
        project = Kernel.GlobalObjects.get_value("PROJECT")
        mapinfos = project.getData("MapInfos")
        def chmp(key):
            return mapinfos[key].order
        for key in self.struct:
            self.struct[key].sort(key=chmp, reverse=True)

    def Refresh_Map_List(self):
        #get the roject
        project = Kernel.GlobalObjects.get_value("PROJECT")
        #get the map infos
        mapinfos = project.getData("MapInfos")
        #clear the list
        self.DeleteAllItems()
        #set up the mapping
        self.maps = {}
        #add project root
        root = self.AddRoot(str(project.getInfo("Title")), 0)
        #creat a stack
        stack = []
        #build a sorted scruct to build the list off of
        self.buildStruct()
        #add the top level maps
        for key in self.struct[0]:
            self.maps[key] = self.AppendItem(root, mapinfos[key].name, 1, data=wx.TreeItemData([key, mapinfos[key].name]))
        #now loop through the struct and add the maps
        for key in self.struct:
            if key == 0 or mapinfos[key].parent_id == 0:
                #skip the top level maps as they have already been added
                continue
            if key not in self.maps:
                self.maps[key] = self.AppendItem(self.maps[mapinfos[key].parent_id], mapinfos[key].name, 1, data=wx.TreeItemData([key, mapinfos[key].name]))
            for id in self.struct[key]:
                if mapinfos[id].parent_id in self.maps:
                    self.maps[id] = self.AppendItem(self.maps[mapinfos[id].parent_id], mapinfos[id].name, 1, data=wx.TreeItemData([id, mapinfos[id].name]))
                else:
                    stack.append([id, mapinfos[id]])
        while len(stack) > 0:
            key, value = stack.pop()
            if value.parent_id in self.maps:
                self.maps[key] = self.AppendItem(self.maps[value.parent_id], value.name, 1, data=wx.TreeItemData([key, value.name]))
            else:
                stack.append([key, value])
        self.Expand(root)

    def onClose(self, event):
        KM.get_event("RefreshProject").unregister(self.Refresh_Map_List)
        event.Skip()

class WxRMXPMapWindow(wx.ScrolledWindow):
    Autotiles = [
                [[27, 28, 33, 34], [5, 28, 33, 34], [27, 6, 33, 34],
                 [5, 6, 33, 34], [27, 28, 33, 12], [5, 28, 33, 12],
                 [27, 6, 33, 12], [5, 6, 33, 12] ],
                [[27, 28, 11, 34], [5, 28, 11, 34], [27, 6, 11, 34],
                 [5, 6, 11, 34], [27, 28, 11, 12], [5, 28, 11, 12],
                 [27, 6, 11, 12], [5, 6, 11, 12] ],
                [[25, 26, 31, 32], [25, 6, 31, 32], [25, 26, 31, 12],
                 [25, 6, 31, 12], [15, 16, 21, 22], [15, 16, 21, 12],
                 [15, 16, 11, 22], [15, 16, 11, 12] ],
                [[29, 30, 35, 36], [29, 30, 11, 36], [5, 30, 35, 36],
                 [5, 30, 11, 36], [39, 40, 45, 46], [5, 40, 45, 46],
                 [39, 6, 45, 46], [5, 6, 45, 46] ],
                [[25, 30, 31, 36], [15, 16, 45, 46], [13, 14, 19, 20],
                 [13, 14, 19, 12], [17, 18, 23, 24], [17, 18, 11, 24],
                 [41, 42, 47, 48], [5, 42, 47, 48] ],
                [[37, 38, 43, 44], [37, 6, 43, 44], [13, 18, 19, 24],
                 [13, 14, 43, 44], [37, 42, 43, 48], [17, 18, 47, 48],
                 [13, 18, 43, 48], [1, 2, 7, 8] ]
                ]
    Layer1 = 0
    Layer2 = 1
    Layer3 = 2
    LayerE = 3
    LayerP = 4

    LayerTransparencyFactor = 0.5


    def __init__(self, parent, id= -1, size=wx.DefaultSize, map_id=0):
        '''
        
        @param parent: the parent window
        @param id: the window id
        @param size: the size of the window
        @param map_id: the id of the map to open
        '''
        wx.ScrolledWindow.__init__(self, parent, id, (0, 0), size=size, style=wx.SUNKEN_BORDER)
        # get plugin components
        self.RPG = KM.get_component("RPG", "RMXP").object
        self.Table = KM.get_component("Table", "RMXP").object
        self.Project = Kernel.Global.Project
        self.Cache = KM.get_component("WxCache", "RMXP").object
        #init data
        self.map_id = 0
        self.map = self.RPG.Map(20, 15)
        self.width = self.map.width
        self.height = self.map.height
        self.data = self.Table(self.width, self.height, 3)
        self.tileset_id = self.map.tileset_id
        self.events = {}
        self.zoom = 1.0
        self.active = 0
        self.old_active = 0
        self.mode = 0
        self.old_mode = 0
        self.tileset = self.Project.getTilesets()[self.tileset_id]
        self.autotile_names = []
        self.tileset_name = ""
        self.tileset_passages = self.Table()
        self.autotiles_b = []
        #layer buffers
        self.layer1 = wx.EmptyBitmapRGBA(32 * self.map.width, 32 * self.map.height) #layer1
        self.layer2 = wx.EmptyBitmapRGBA(32 * self.map.width, 32 * self.map.height) #layer2
        self.layer3 = wx.EmptyBitmapRGBA(32 * self.map.width, 32 * self.map.height) #layer3
        self.layer4 = wx.EmptyBitmapRGBA(32 * self.map.width, 32 * self.map.height) #layerEvents
        self.layer5 = wx.EmptyBitmapRGBA(32 * self.map.width, 32 * self.map.height) #layerBrush
        self.layer6 = wx.EmptyBitmapRGBA(32 * self.map.width, 32 * self.map.height) #layerMouse
        self.layerP = wx.EmptyBitmapRGBA(32 * self.map.width, 32 * self.map.height) #layerPreview
        sz = self.GetClientSize()
        sz.width = max(1, sz.width)
        sz.height = max(1, sz.height)
        self._buffer = wx.EmptyBitmap(sz.width, sz.height, 32)
        self.setup(map_id)
        #bind events
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftButtonEvent)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftButtonEvent)
        self.Bind(wx.EVT_MOTION, self.OnLeftButtonEvent)

    def OnLeftButtonEvent(self, event):
        if self.mode != self.LayerE:
            self.SetMouseXY(event)
        if event.LeftDown():
            self.SetFocus()
            self.SetMouseXY(event)
            self.CaptureMouse()
            self.drawing = True

        elif event.Dragging() and self.drawing:
            self.buildBrush()

        elif event.LeftUp():
            self.ReleaseMouse()
            if self.drawing:
                self.commitBrush()

        dc = wx.BufferedDC(None, self._buffer)
        gc = wx.GraphicsContext.Create(dc)
        self.DoDrawing(gc, self.init)

        # refresh it
        self.Refresh(eraseBackground=False)

    def buildBrush(self):
        pass

    def commitBrush(self):
        pass

    def setup(self, id):
        self.init = True
        self.map_id = id
        self.map = self.Project.getMap(self.map_id)
        self.width = self.map.width
        self.height = self.map.height
        self.data = self.Table(self.width, self.height, 3)
        self.tileset_id = self.map.tileset_id
        self.events = self.map.events
        self.mouse_x = self.old_mouse_x = self.mouse_y = self.old_mouse_y = 0
        self.last_mouse_x = self.last_mouse_y = 0
        self.zoom = 1.0
        self.old_zoom = 1
        self.active = 0
        self.old_active = 0
        self.mode = 0
        self.old_mode = 0
        self.tileset = self.Project.getTilesets()[self.tileset_id]
        self.autotile_names = []
        self.tileset_name = ""
        self.tileset_passages = self.Table()
        self.autotiles_b = [None] * 7
        self.layer1 = wx.EmptyBitmapRGBA(32 * self.map.width, 32 *
                                         self.map.height) #layer1
        self.layer2 = wx.EmptyBitmapRGBA(32 * self.map.width, 32 *
                                         self.map.height) #layer2
        self.layer3 = wx.EmptyBitmapRGBA(32 * self.map.width, 32 *
                                         self.map.height) #layer3
        self.layer4 = wx.EmptyBitmapRGBA(32 * self.map.width, 32 *
                                         self.map.height) #layerEvents
        self.layer5 = wx.EmptyBitmapRGBA(32 * self.map.width, 32 *
                                         self.map.height) #layerBrush
        self.layer6 = wx.EmptyBitmapRGBA(32 * self.map.width, 32 *
                                         self.map.height) #layerMouse
        self.layerP = wx.EmptyBitmapRGBA(32 * self.map.width, 32 *
                                         self.map.height) #layerPreview
        self._dimlayer = wx.EmptyBitmapRGBA(32 * self.map.width, 32 *
                                            self.map.height)
        self.InitBuffer()
        self.SetVirtualSize((((self.map.width) * 32) * self.zoom,
                             ((self.map.height) * 32) * self.zoom))
        self.SetScrollRate(1, 1)

    def SetMouseXY(self, event):
        x, y = self.ConvertEventCoords(event)
        x = x / int(32 * self.zoom)
        y = y / int(32 * self.zoom)
        self.mouse_x, self.mouse_y = x, y

    def ConvertEventCoords(self, event):
        newpos = self.CalcUnscrolledPosition(event.GetX(), event.GetY())
        return newpos

    def needRedraw(self):
        # set flags
        flag = False
        layer1flag = False
        layer2flag = False
        layer3flag = False
        layerEflag = False
        previewflag = False
        mouseflag = False
        brushflag = False
        #test width and height
        if self.width != self.map.width:
            self.width = self.map.width
            flag = True
        if self.height != self.map.height:
            self.height = self.map.height
            flag = True
        #test tileset & autotiles
        if self.tileset_id != self.map.tileset_id:
            self.tileset_id = self.map.tileset_id
            flag = True
        if self.autotile_names != self.tileset.autotile_names:
            self.autotile_names = self.tileset.autotile_names[:]
            self.load_autotiles()
            flag = True
        if self.tileset_name != self.tileset.tileset_name:
            self.tileset_name = self.tileset.tileset_name
            flag = True
        #test data
        eq = self.data._data != self.map.data._data
        layerflags = eq.reshape(-1, 3).any(axis=0)
        layer1flag = layerflags[0]
        layer2flag = layerflags[1]
        layer3flag = layerflags[2]
        if layerflags.any():
            self.data._data[:] = self.map.data._data
        #test events
        if self.map_id in self.Project.Event_redraw_flags:
            if self.Project.Event_redraw_flags[self.map_id]:
                layerEflag = True
        #test active
        if self.old_active != self.active:
            self.old_active = self.active
            layerEflag = True
        # test mouse
        if (self.old_mouse_x != self.mouse_x) or (self.old_mouse_y != self.mouse_y):
            self.old_mouse_x = self.mouse_x
            self.old_mouse_y = self.mouse_y
            mouseflag = True
        #test brush 
        if False:
            brushflag = True

        return (flag, layer1flag, layer2flag, layer3flag, layerEflag, previewflag, mouseflag, brushflag)

    def InitBuffer(self):
        self._buffer = wx.EmptyBitmap(self.map.width * 32,
                                      self.map.height * 32, 32)
        dc = wx.MemoryDC(self._buffer)
        dc.SetBackground(wx.Brush(wx.NullColor))
        dc.Clear()
        gc = wx.GraphicsContext.Create(dc)
        self.DoDrawing(gc, True)

    def OnPaint(self, event):
        #prepare dc and the draw to it
        dc = wx.BufferedPaintDC(self, self._buffer, wx.BUFFER_VIRTUAL_AREA)
        #gc = wx.GraphicsContext.Create(dc)
        #self.DoDrawing(gc, self.init)

    def DoDrawing(self, dc, init=False):
        flag, layer1flag, layer2flag, layer3flag, layerEflag, previewflag, mouseflag, brushflag = self.needRedraw()
        self.init = False
        if flag:
            self.draw_dimlayer()
        if flag or layer1flag:
            self.drawlayer1()
        if flag or layer2flag:
            self.drawlayer2()
        if flag or layer3flag:
            self.drawlayer3()
        if flag or layerEflag:
            self.draw_events()
        if flag or previewflag:
            self.draw_preview
        if flag or mouseflag:
            self.draw_mouse()
        if flag or brushflag:
            self.draw_brush
        dc.SetPen(wx.Pen(wx.Colour(0, 0, 0, 255), 1))
        dc.SetBrush(wx.Brush(wx.Colour(0, 0, 0, 255)))
        #combine the layers onto the primary dc
        newWidth = self.layer1.GetWidth() * self.zoom
        newHeight = self.layer1.GetHeight() * self.zoom
        if self.mode == self.LayerP:
            if previewflag != True or init != True:
                return
            size = self.layerP.GetSize()
            dc.DrawRectangle(0, 0, size.width * self.zoom, size.height * self.zoom)
            imagelayerP = self.layerP.ConvertToImage()
            imagelayerP.Rescale(newWidth, newHeight, wx.IMAGE_QUALITY_HIGH)
            layerP = imagelayerP.ConvertToBitmap()
            dc.DrawBitmap(layerP, 0, 0, size.width * self.zoom, size.height)
        elif self.mode == self.Layer1:
            if (layer1flag != True and layer2flag != True and layer3flag !=
                True and layerEflag != True) and init != True and mouseflag != True:
                return
            dc.DrawRectangle(0, 0, self.layer1.GetWidth() * self.zoom, self.layer1.GetWidth() * self.zoom)
            #layer 1
            imagelayer1 = self.layer1.ConvertToImage()
            imagelayer1.Rescale(newWidth, newHeight, wx.IMAGE_QUALITY_HIGH)
            layer1 = imagelayer1.ConvertToBitmap()
            dc.DrawBitmap(layer1, 0, 0, newWidth, newHeight)
            #brush layer
            imagelayer5 = self.layer5.ConvertToImage()
            imagelayer5.Rescale(newWidth, newHeight, wx.IMAGE_QUALITY_HIGH)
            layer5 = imagelayer5.ConvertToBitmap()
            dc.DrawBitmap(layer5, 0, 0, newWidth, newHeight)
            #layer 2
            imagelayer2 = self.layer2.ConvertToImage()
            imagelayer2.Rescale(newWidth, newHeight, wx.IMAGE_QUALITY_HIGH)
            imagelayer2.AdjustChannels(1.0, 1.0, 1.0, self.LayerTransparencyFactor)
            layer2 = imagelayer2.ConvertToBitmap()
            dc.DrawBitmap(layer2, 0, 0, newWidth, newHeight)
            #layer 3
            imagelayer3 = self.layer3.ConvertToImage()
            imagelayer3.Rescale(newWidth, newHeight, wx.IMAGE_QUALITY_HIGH)
            imagelayer3.AdjustChannels(1.0, 1.0, 1.0, self.LayerTransparencyFactor)
            layer3 = imagelayer3.ConvertToBitmap()
            dc.DrawBitmap(layer3, 0, 0, newWidth, newHeight)
            #event layer
            imagelayerE = self.layer4.ConvertToImage()
            imagelayerE.Rescale(newWidth, newHeight, wx.IMAGE_QUALITY_HIGH)
            imagelayerE.AdjustChannels(1.0, 1.0, 1.0, self.LayerTransparencyFactor)
            layerE = imagelayerE.ConvertToBitmap()
            dc.DrawBitmap(layerE, 0, 0, newWidth, newHeight)
            #mouse
            imagelayer6 = self.layer6.ConvertToImage()
            imagelayer6.Rescale(newWidth, newHeight, wx.IMAGE_QUALITY_HIGH)
            layer6 = imagelayer6.ConvertToBitmap()
            dc.DrawBitmap(layer6, 0, 0, newWidth, newHeight)

        elif self.mode == self.Layer2:
            if (layer1flag != True and layer2flag != True and layer3flag !=
                True and layerEflag != True) and init != True and mouseflag != True:
                return
            dc.DrawRectangle(0, 0, self.layer1.GetWidth() * self.zoom, self.layer1.GetWidth() * self.zoom)
            #layer 1
            imagelayer1 = self.layer1.ConvertToImage()
            imagelayer1.Rescale(newWidth, newHeight, wx.IMAGE_QUALITY_HIGH)
            layer1 = imagelayer1.ConvertToBitmap()
            dc.DrawBitmap(layer1, 0, 0, newWidth, newHeight)
            #dimlayers
            dc.DrawBitmap(self._dimlayer, 0, 0, newWidth, newHeight)
            #layer 2
            imagelayer2 = self.layer2.ConvertToImage()
            imagelayer2.Rescale(newWidth, newHeight, wx.IMAGE_QUALITY_HIGH)
            layer2 = imagelayer2.ConvertToBitmap()
            dc.DrawBitmap(layer2, 0, 0, newWidth, newHeight)
            #brush layer
            imagelayer5 = self.layer5.ConvertToImage()
            imagelayer5.Rescale(newWidth, newHeight, wx.IMAGE_QUALITY_HIGH)
            layer5 = imagelayer5.ConvertToBitmap()
            dc.DrawBitmap(layer5, 0, 0, newWidth, newHeight)
            #layer 3
            imagelayer3 = self.layer3.ConvertToImage()
            imagelayer3.Rescale(newWidth, newHeight, wx.IMAGE_QUALITY_HIGH)
            imagelayer3.AdjustChannels(1.0, 1.0, 1.0, self.LayerTransparencyFactor)
            layer3 = imagelayer3.ConvertToBitmap()
            dc.DrawBitmap(layer3, 0, 0, newWidth, newHeight)
            #event layer
            imagelayerE = self.layer4.ConvertToImage()
            imagelayerE.Rescale(newWidth, newHeight, wx.IMAGE_QUALITY_HIGH)
            imagelayerE.AdjustChannels(1.0, 1.0, 1.0, self.LayerTransparencyFactor)
            layerE = imagelayerE.ConvertToBitmap()
            dc.DrawBitmap(layerE, 0, 0, newWidth, newHeight)
            #mouse
            imagelayer6 = self.layer6.ConverToImage()
            imagelayer6.Rescale(newWidth, newHeight, wx.IMAGE_QUALITY_HIGH)
            layer6 = imagelayer6.ConvertToBitmap()
            dc.DrawBitmap(layer6, 0, 0, newWidth, newHeight)
        elif self.mode == self.Layer3:
            if (layer1flag != True and layer2flag != True and layer3flag !=
                True and layerEflag != True) and init != True and mouseflag != True:
                return
            dc.DrawRectangle(0, 0, self.layer1.GetWidth() * self.zoom, self.layer1.GetWidth() * self.zoom)
            #layer 1
            imagelayer1 = self.layer1.ConvertToImage()
            imagelayer1.Rescale(newWidth, newHeight, wx.IMAGE_QUALITY_HIGH)
            layer1 = imagelayer1.ConvertToBitmap()
            dc.DrawBitmap(layer1, 0, 0, newWidth, newHeight)
            #layer 2
            imagelayer2 = self.layer2.ConvertToImage()
            imagelayer2.Rescale(newWidth, newHeight, wx.IMAGE_QUALITY_HIGH)
            layer2 = imagelayer2.ConvertToBitmap()
            dc.DrawBitmap(layer2, 0, 0, newWidth, newHeight)
            #dimlayers
            dc.DrawBitmap(self._dimlayer, 0, 0, newWidth, newHeight)
            #layer 3
            imagelayer3 = self.layer3.ConvertToImage()
            imagelayer3.Rescale(newWidth, newHeight, wx.IMAGE_QUALITY_HIGH)
            layer3 = imagelayer3.ConvertToBitmap()
            dc.DrawBitmap(layer3, 0, 0, newWidth, newHeight)
            #brush layer
            imagelayer5 = self.layer5.ConvertToImage()
            imagelayer5.Rescale(newWidth, newHeight, wx.IMAGE_QUALITY_HIGH)
            layer5 = imagelayer5.ConvertToBitmap()
            dc.DrawBitmap(layer5, 0, 0, newWidth, newHeight)
            #event layer
            imagelayerE = self.layer4.ConvertToImage()
            imagelayerE.Rescale(newWidth, newHeight, wx.IMAGE_QUALITY_HIGH)
            imagelayerE.AdjustChannels(1.0, 1.0, 1.0, self.LayerTransparencyFactor)
            layerE = imagelayerE.ConvertToBitmap()
            dc.DrawBitmap(layerE, 0, 0, newWidth, newHeight)
            #mouse
            imagelayer6 = self.layer6.ConverToImage()
            imagelayer6.Rescale(newWidth, newHeight, wx.IMAGE_QUALITY_HIGH)
            layer6 = imagelayer6.ConvertToBitmap()
            dc.DrawBitmap(layer6, 0, 0, newWidth, newHeight)
        elif self.mode == self.LayerE:
            if (layer1flag != True and layer2flag != True and layer3flag !=
                True and layerEflag != True) and init != True and mouseflag != True:
                return
            dc.DrawRectangle(0, 0, self.layer1.GetWidth() * self.zoom, self.layer1.GetWidth() * self.zoom)
            #layer 1
            imagelayer1 = self.layer1.ConvertToImage()
            imagelayer1.Rescale(newWidth, newHeight, wx.IMAGE_QUALITY_HIGH)
            layer1 = imagelayer1.ConvertToBitmap()
            dc.DrawBitmap(layer1, 0, 0, newWidth, newHeight)
            #layer 2
            imagelayer2 = self.layer2.ConvertToImage()
            imagelayer2.Rescale(newWidth, newHeight, wx.IMAGE_QUALITY_HIGH)
            layer2 = imagelayer2.ConvertToBitmap()
            dc.DrawBitmap(layer2, 0, 0, newWidth, newHeight)
            #layer 3
            imagelayer3 = self.layer3.ConvertToImage()
            imagelayer3.Rescale(newWidth, newHeight, wx.IMAGE_QUALITY_HIGH)
            layer3 = imagelayer3.ConvertToBitmap()
            dc.DrawBitmap(layer3, 0, 0, newWidth, newHeight)
            #event layer
            dc.DrawBitmap(self.layer4, 0, 0, self.layer4.GetWidth(), self.layer4.GetHeight())
            path = dc.CreatePath()
            path.AddRectangle(0, 0, 31, 31)
            dc.SetPen(wx.Pen(wx.Colour(0, 0, 0, 80), 1))
            dc.SetBrush(wx.Brush(wx.Colour(0, 0, 0, 255)))
            for x in range(0, self.map.width - 1):
                # Passes Through Z Coordinates
                for y in range(0, self.map.height - 1):
                    dc.PushState()             # save current translation/scale/other state 
                    dc.Scale(self.zoom, self.zoom)
                    dc.Translate(x * 32 * self.zoom, y * 32 * self.zoom)
                    dc.StrokePath(path)
                    dc.PopState()              # restore saved state

    def load_autotiles(self):
        for i in range(7):
            autotile_name = self.autotile_names[i]
            self.autotiles_b[i] = self.Cache.Autotile(autotile_name, self.Project.Location)
            if not self.autotiles_b[i]:
                self.autotiles_b[i] = self.Cache.Autotile(autotile_name, self.Project.RTP_Location)
            if not self.autotiles_b[i]:
                self.autotiles_b[i] = wx.EmptyBitmapRGBA(32 * 3, 32 * 4)

    def draw_brush(self):
        if (self.layer5.GetWidth() != self.map.width * 32) or (self.layer5.GetHeight() != self.map.width * 32):
            self.layer5 = wx.EmptyBitmapRGBA(32 * self.map.width, 32 * self.map.height)

    def draw_dimlayer(self):
        if (self._dimlayer.GetWidth() != self.map.width * 32) or (self._dimlayer.GetHeight() != self.map.width * 32):
            self._dimlayer = wx.EmptyBitmapRGBA(32 * self.map.width, 32 * self.map.height)
        dc = wx.MemoryDC()
        dc.SelectObject(self._dimlayer)
        dc.SetBackground(wx.Brush(wx.Colour(0, 0, 0, 80)))
        dc.Clear()
        dc.SelectObject(wx.NullBitmap)

    def draw_mouse(self):
        if (self.layer6.GetWidth() != self.map.width * 32) or (self.layer6.GetHeight() != self.map.width * 32):
            self.layer6 = wx.EmptyBitmapRGBA(32 * self.map.width, 32 * self.map.height)
        dc = wx.MemoryDC()
        dc.SelectObject(self.layer6)
        dc.SetBackground(wx.Brush(wx.Colour(255, 255, 255, 0), wx.TRANSPARENT))
        dc.Clear()
        gc = wx.GraphicsContext.Create(dc)
        path = gc.CreatePath()
        path.AddRectangle(0, 0, 31, 31)
        path.AddRectangle(3, 3, 25, 25)
        gc.SetPen(wx.Pen("black", 1))
        gc.SetBrush(wx.Brush("white"))
        gc.PushState()             # save current translation/scale/other state 
        gc.Translate(self.mouse_x * 32, self.mouse_y * 32)
        gc.DrawPath(path)
        gc.PopState()              # restore saved state
        dc.SelectObject(wx.NullBitmap)

    def draw_preview(self):
        if (self.layerP.GetWidth() != self.map.width * 32) or (self.layerP.GetHeight() != self.map.width * 32):
            self.layerP = wx.EmptyBitmapRGBA(32 * self.map.width, 32 * self.map.height)
        if self.mode == self.LayerP:
            dc = wx.MemoryDC()
            dc.SelectObject(self.layerP)
            dc.SetBackground(wx.Brush(wx.Colour(255, 255, 255, 0), wx.TRANSPARENT))
            dc.Clear()
            tileset = self.Cache.Tileset(self.tileset_name, self.Project.Location)
            if not tileset:
                tileset = self.Cache.Tileset(self.tileset_name, self.Project.RTP_Location)
            if not tileset:
                tileset = wx.EmptyBitmapRGBA(32 * 6, 32)
            for p in range(0, 5):
                # Passes Through Layers
                for z in range(0, 2):
                    # Passes Through X Coordinates
                    for x in range(0, self.map.width - 1):
                        # Passes Through Z Coordinates
                        for y in range(0, self.map.height - 1):
                            # Collects Tile ID
                            id = self.data[x, y, z]
                            # if not 0 tile
                            if id != 0:
                                # If Priority Matches
                                if p == self.tileset.Priorities[id]:
                                    # Cap Priority to Layer 3
                                    if p > 2:
                                        p = 2
                                    # Draw Tile
                                    if id < 384:
                                        if self.autotiles[id / 48 - 1].GetWidth() / 96 > 1:
                                            autotile = self.autotiles_b[id / 48 - 1]
                                            tile_id = id % 48
                                            bitmap = wx.EmptyBitmapRGBA(32, 32)
                                            # Collects Auto-Tile Tile Layout
                                            tiles = self.Autotiles[tile_id / 8][tile_id % 8]
                                            dc_at = wx.MemoryDC()
                                            dc_at.SelectObject(bitmap)
                                            for i in range(4):
                                                tile_position = tiles[i] - 1
                                                src_rect = wx.Rect(tile_position % 6 * 16, tile_position / 6 * 16, 16, 16)
                                                sub_at_bitmap = autotile.GetSubBitmap(src_rect)
                                                dc_at.DrawBitmap(sub_at_bitmap, i % 2 * 16, i / 2 * 16, True)
                                            dc_at.SelectObject(wx.NullBitmap)
                                            t_x = x * 32
                                            t_y = y * 32
                                            dc.DrawBitmap(bitmap, t_x, t_y, True)
                                    else:
                                        rect = wx.Rect((id - 384) % 8 * 32, (id - 384) / 8 * 32, 32, 32)
                                        sub_bitmap = tileset.GetSubBitmap(rect)
                                        dc.DrawBitmap(sub_bitmap, x * 32, y * 32, True)
            dc.SelectObject(wx.NullBitmap)

    def draw_events(self):
        if (self.layer4.GetWidth() != self.map.width * 32) or (self.layer4.GetHeight() != self.map.width * 32):
            self.layer4 = wx.EmptyBitmapRGBA(32 * self.map.width, 32 * self.map.height)
        dc = wx.MemoryDC()
        dc.SelectObject(self.layer4)
        dc.SetBackground(wx.Brush(wx.Colour(255, 255, 255, 0), wx.TRANSPARENT))
        dc.Clear()
        gc = wx.GraphicsContext.Create(dc)
        path = gc.CreatePath()
        gc.SetPen(wx.Pen("white", 1))
        gc.SetBrush(wx.Brush(wx.Colour(255, 255, 255, 80)))
        path.AddRectangle(4, 4, 23, 23)
        for key in self.events.keys():
            event = self.events[key]
            eventGraphic = self.events[key].pages[0].graphic
            if eventGraphic.tile_id >= 384:
                temp_bitmap = self.Cache.Tile(self.tileset_name, eventGraphic.tile_id,
                                              eventGraphic.character_hue, self.Project.Location)
                if not temp_bitmap:
                    temp_bitmap = self.Cache.Tile(self.tileset_name, eventGraphic.tile_id,
                                                  eventGraphic.character_hue, self.Project.RTP_Location)
                if not temp_bitmap:
                    temp_bitmap = wx.EmptyBitmapRGBA(32, 32)
                rect = wx.Rect(5, 5, 22, 22)
                bitmap = temp_bitmap.GetSubBitmap(rect)
            else:
                temp_bitmap = self.Cache.Character(eventGraphic.character_name,
                                                   eventGraphic.character_hue, self.Project.Location)
                if not temp_bitmap:
                    temp_bitmap = self.Cache.Character(eventGraphic.character_name, eventGraphic.character_hue,
                                                       self.Project.RTP_Location)
                if not temp_bitmap:
                    temp_bitmap = wx.EmptyBitmapRGBA(32 * 4, 32 * 4)
                cw = temp_bitmap.GetWidth() / 4
                ch = temp_bitmap.GetHeight() / 4
                sx = eventGraphic.pattern * cw
                sy = (eventGraphic.direction - 2) / 2 * ch
                rect = wx.Rect(sx + 5, sy + 5, 22, 22)
                bitmap = temp_bitmap.GetSubBitmap(rect)
            bitmapSize = bitmap.GetSize()
            gc.PushState()             # save current translation/scale/other state 
            gc.Translate(event.x * 32, event.y * 32)
            gc.DrawPath(path)
            gc.PopState()              # restore saved state
            gc.DrawBitmap(bitmap, event.x * 32 + 5, event.y * 32 + 5, bitmapSize.width, bitmapSize.height)
        dc.SelectObject(wx.NullBitmap)

    def drawlayer1(self):
        if (self.layer1.GetWidth() != self.map.width * 32) or (self.layer1.GetHeight() != self.map.width * 32):
            self.layer1 = wx.EmptyBitmapRGBA(32 * self.map.width, 32 * self.map.height)
        dc = wx.MemoryDC()
        dc.SelectObject(self.layer1)
        dc.SetBackground(wx.Brush(wx.Colour(255, 255, 255, 0), wx.TRANSPARENT))
        dc.Clear()
        dc = wx.GCDC(dc)
        emptybitmap = False
        tileset = self.Cache.Tileset(self.tileset_name, self.Project.Location)
        if not tileset:
            tileset = self.Cache.Tileset(self.tileset_name, self.Project.RTP_Location)
        if not tileset:
            tileset = wx.EmptyBitmapRGBA(32 * 8, 32)
            emptybitmap = True
        for x in range(self.map.width):
            for y in range(self.map.height):
                id = int(self.data[x, y, 0])
                if id != 0:
                    if id < 384:
                        if self.autotiles_b[id / 48 - 1].GetWidth() / 96 >= 1:
                            autotile = self.autotiles_b[id / 48 - 1]
                            tile_id = id % 48
                            # Collects Auto-Tile Tile Layout
                            tiles = self.Autotiles[tile_id / 8][tile_id % 8]
                            t_x = x * 32
                            t_y = y * 32
                            for i in range(4):
                                tile_position = tiles[i] - 1
                                src_rect = wx.Rect(tile_position % 6 * 16, tile_position / 6 * 16, 16, 16)
                                sub_at_bitmap = autotile.GetSubBitmap(src_rect)
                                dc.DrawBitmap(sub_at_bitmap, t_x + (i % 2 * 16),
                                              t_y + (i / 2 * 16), True)
                    else:
                        rect = wx.Rect((id - 384) % 8 * 32, (id - 384) / 8 * 32, 32, 32)
                        if emptybitmap and tileset.GetHeight() < (rect.GetY() + 32):
                            tileset = wx.EmptyBitmap(32 * 8, rect.GetY() + 32)
                        sub_bitmap = tileset.GetSubBitmap(rect)
                        dc.DrawBitmap(sub_bitmap, x * 32, y * 32, True)

    def drawlayer2(self):
        if (self.layer2.GetWidth() != self.map.width * 32) or (self.layer2.GetHeight() != self.map.width * 32):
            self.layer2 = wx.EmptyBitmapRGBA(32 * self.map.width, 32 * self.map.height)
        dc = wx.MemoryDC()
        dc.SelectObject(self.layer2)
        dc.SetBackground(wx.Brush(wx.Colour(255, 255, 255, 0), wx.TRANSPARENT))
        dc.Clear()
        dc = wx.GCDC(dc)
        emptybitmap = False
        tileset = self.Cache.Tileset(self.tileset_name, self.Project.Location)
        if not tileset:
            tileset = self.Cache.Tileset(self.tileset_name, self.Project.RTP_Location)
        if not tileset:
            tileset = wx.EmptyBitmapRGBA(32 * 8, 32)
            emptybitmap = True
        for x in range(self.map.width):
            for y in range(self.map.height):
                id = int(self.data[x, y, 1])
                if id != 0:
                    if id < 384:
                        if self.autotiles_b[id / 48 - 1].GetWidth() / 96 >= 1:
                            autotile = self.autotiles_b[id / 48 - 1]
                            tile_id = id % 48
                            # Collects Auto-Tile Tile Layout
                            tiles = self.Autotiles[tile_id / 8][tile_id % 8]
                            t_x = x * 32
                            t_y = y * 32
                            for i in range(4):
                                tile_position = tiles[i] - 1
                                src_rect = wx.Rect(tile_position % 6 * 16, tile_position / 6 * 16, 16, 16)
                                sub_at_bitmap = autotile.GetSubBitmap(src_rect)
                                dc.DrawBitmap(sub_at_bitmap, t_x + (i % 2 * 16),
                                              t_y + (i / 2 * 16), True)
                    else:
                        rect = wx.Rect((id - 384) % 8 * 32, (id - 384) / 8 * 32, 32, 32)
                        if emptybitmap and tileset.GetHeight() < (rect.GetY() + 32):
                            tileset = wx.EmptyBitmap(32 * 8, rect.GetY() + 32)
                        sub_bitmap = tileset.GetSubBitmap(rect)
                        dc.DrawBitmap(sub_bitmap, x * 32, y * 32, True)

    def drawlayer3(self):
        if (self.layer3.GetWidth() != self.map.width * 32) or (self.layer3.GetHeight() != self.map.width * 32):
            self.layer3 = wx.EmptyBitmapRGBA(32 * self.map.width, 32 * self.map.height)
        dc = wx.MemoryDC()
        dc.SelectObject(self.layer3)
        dc.SetBackground(wx.Brush(wx.Colour(255, 255, 255, 0), wx.TRANSPARENT))
        dc.Clear()
        dc = wx.GCDC(dc)
        emptybitmap = False
        tileset = self.Cache.Tileset(self.tileset_name, self.Project.Location)
        if not tileset:
            tileset = self.Cache.Tileset(self.tileset_name, self.Project.RTP_Location)
        if not tileset:
            tileset = wx.EmptyBitmapRGBA(32 * 8, 32)
            emptybitmap = True
        for x in range(self.map.width):
            for y in range(self.map.height):
                id = int(self.data[x, y, 2])
                if id != 0:
                    if id < 384:
                        if self.autotiles_b[id / 48 - 1].GetWidth() / 96 >= 1:
                            autotile = self.autotiles_b[id / 48 - 1]
                            tile_id = id % 48
                            # Collects Auto-Tile Tile Layout
                            tiles = self.Autotiles[tile_id / 8][tile_id % 8]
                            t_x = x * 32
                            t_y = y * 32
                            for i in range(4):
                                tile_position = tiles[i] - 1
                                src_rect = wx.Rect(tile_position % 6 * 16, tile_position / 6 * 16, 16, 16)
                                sub_at_bitmap = autotile.GetSubBitmap(src_rect)
                                dc.DrawBitmap(sub_at_bitmap, t_x + (i % 2 * 16),
                                              t_y + (i / 2 * 16), True)
                    else:
                        rect = wx.Rect((id - 384) % 8 * 32, (id - 384) / 8 * 32, 32, 32)
                        if emptybitmap and tileset.GetHeight() < (rect.GetY() + 32):
                            tileset = wx.EmptyBitmap(32 * 8, rect.GetY() + 32)
                        sub_bitmap = tileset.GetSubBitmap(rect)
                        dc.DrawBitmap(sub_bitmap, x * 32, y * 32, True)

class WxRMXPMapPanel(wx.Panel):
    def __init__(self, parent, style):
        wx.Panel.__init__(self, parent)

        #set up Sizer
        box = wx.BoxSizer(wx.VERTICAL)

        #set up notebook
        self.notebook = aui.AuiNotebook(self, -1, wx.Point(0, 0),
                                        wx.Size(430, 200), agwStyle=style)

        #add ctrls to sizer
        box.Add(self.notebook, 1, wx.ALL | wx.EXPAND)
        #set sizer
        self.SetSizerAndFit(box)

    def add_page(self, map_id, name):
            editor = WxRMXPMapWindow(self, map_id=map_id)
            self.notebook.AddPage(editor, name)




