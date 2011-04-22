#load standard libs
import os
import cPickle
#load 3d party libs
import numpy  
import wx
from wx import glcanvas  
import pyglet
from pyglet import gl
#load our libraries
import Core
import pygletwx
from cache import PygletCache as Cache

#Set up some global strings
rtppath = "%PROGRAMFILES%/Common Files/Enterbrain/RGSS/Standard"
RTP_Location = os.path.normpath(os.path.expandvars(rtppath))
Project_Location = ""

class EventStruct(object):
    '''
    A small data structure so that the Event Grid class can keep track 
    of changes on specific events and draw them if they have changed
    '''

    def __init__(self, x, y, tile_id, name, hue, direction, pattern):
        self.x = x
        self.y = y
        self.tile_id = tile_id
        self.name = name
        self.hue = hue
        self.direction = direction
        self.pattern = pattern
        
class EventGrid(object):
    '''
    A organizer class, organizes and updates the sprites for events and 
    their background when they are drawn in the editor
    '''
    def __init__(self, map, cache, tileset=""):
        #set properties
        self.map = map
        self.cache = cache
        self.tileset_name = tileset
        #setup the rendering batch and the oarding groups
        self.renderingBatch = pyglet.graphics.Batch()
        self.backgroundGroup = pyglet.graphics.OrderedGroup(1)
        self.spriteGroup = pyglet.graphics.OrderedGroup(2)
        #set up data containers
        self.events = {}
        self.sprites = {}
        #setup the outline image used for background sprites
        self.setupOutline()
        #update the sprites
        self.update()
        
    def setupOutline(self):
        '''
        draws an outline for the event adn stores it so that it can be uses in sprites later
        '''
        outlineEdgePattern = pyglet.image.SolidColorImagePattern((255, 255, 255, 255))
        eventOutline = outlineEdgePattern.create_image(24, 24).get_texture()
        outlineBackPattern = pyglet.image.SolidColorImagePattern((255, 255, 255, 80))
        background = outlineBackPattern.create_image(22, 22)
        eventOutline.blit_into(background, 1, 1, 0)
        self.eventOutline = eventOutline.get_image_data()
    
    def setEventGraphic(self, key):
        '''
        takes an event id as a key and updates the sprite graphic
        '''
        #get event
        event = self.events[key] 
        #if the graphic is a tile
        if event.tile_id >= 384:
            bitmap = self.cache.Tile(self.tileset_name, event.tile_id, event.hue, Project_Location)
            if not bitmap:
                bitmap = self.cache.Tile(self.tileset_name, event.tile_id, event.hue, RTP_Location)
            if bitmap:
                rect = (5, 5, 22, 22)
        #other wise the graphic is a sprite
        else:
            bitmap = self.cache.Character(event.name, event.hue, Project_Location)
            if not bitmap:
                bitmap = self.cache.Character(event.name, event.hue, RTP_Location)
            if bitmap:
                cw = bitmap.width / 4
                ch = bitmap.height / 4
                sx = event.pattern * cw
                sy = (event.direction - 2) / 2 * ch
                rect = (sx + (cw - 22) / 2, bitmap.height - sy - ch / 2 - 5, 22, 22)
        
        #draw a portion of the event graphic
        if bitmap:
            image = pyglet.image.create(32, 32).get_texture()
            reagion = bitmap.get_region(*rect)
            image.blit_into(reagion, 5, 5, 0)
            
        xpos = event.x * 32
        ypos = ((self.map.height - event.y) * 32) - 32
        if not self.sprites.has_key(key) or self.sprites[key][0] is None:
            sprite = None
            if bitmap: 
               sprite = pyglet.sprite.Sprite(image, x=xpos, y=ypos, batch=self.renderingBatch, group=self.spriteGroup)
            
            background = pyglet.sprite.Sprite(self.eventOutline, x=xpos + 4, y=ypos + 4, 
                                 batch=self.renderingBatch, group=self.backgroundGroup)
            
            self.sprites[key] = [sprite, background]
        else:
            if bitmap:
                self.sprites[key][0].image = image 
            else:
                self.sprites[key][0].delete()
                self.sprites[key][0] = None
            
    def updateEvent(self, key):
        '''
        compares graphically relevant data to stored versions of the data
        for each event and sets the graphic to be updated if the data has changed
        '''
        #get event
        flag = False
        mapEvent = self.map.events[key]
        graphic = self.map.events[key].pages[0].graphic
        if not self.events.has_key(key):
            event = EventStruct(mapEvent.x, mapEvent.y, graphic.tile_id, graphic.character_name,  
                                graphic.character_hue, graphic.direction, graphic.pattern)
            self.events[key] = event
            flag = True
        else:
            event = self.events[key]
            if event.x != mapEvent.x:
                event.x = mapEvent.x
            if event.y != mapEvent.x:
                event.y = mapEvent.y
            xpos = event.x * 32
            ypos = ((self.map.height - event.y) * 32) - 32
            if self.sprites.has_key(key):
                if self.sprites[key][0] is not None:
                    if self.sprites[key][0].x != xpos or self.sprites[key][0].y != ypos:
                        self.sprites[key][0].set_position(xpos, ypos)
                    if self.sprites[key][1].x != xpos or self.sprites[key][1].y != ypos:
                        self.sprites[key][1].set_position(xpos, ypos)
            if event.tile_id != graphic.tile_id:
                flag = True
                event.tile_id = graphic.tile_id
            if event.name != graphic.character_name:
                flag = True
                event.name = graphic.character_name
            if event.hue != graphic.character_hue:
                flag = True
                event.hue = graphic.character_hue
            if event.direction != graphic.direction:
                flag = True
                event.direction = graphic.direction
            if event.pattern != graphic.pattern:
                flag = True
                event.pattern = graphic.pattern 
        if flag:
            self.setEventGraphic(key)
        #test values that are drawn to see if the graphic (or position) need to be updated
    
    def update(self):
        '''
        loops through every event and removes sprites for events that have been deleted, 
        then calls the updateEvent method for the rest of the events
        '''
        removed = list(set(self.events.keys()) - set(self.map.events.keys()))
        for key in removed:
            for sprite in self.events[key]:
                if sprite is not None:
                    sprite.delete()
            del self.events[key]
        for key in self.map.events.iterkeys():
            self.updateEvent(key)
            
    def Draw(self):
        '''
        Draws the rendering batch and thus all the attached sprites
        '''
        self.renderingBatch.draw()
        
    def  __del__(self):
        '''
        to be sure that all sprites are deleated properly
        '''
        self.destroy()
        
    def destroy(self):
        '''
        destroys all the sprites
        '''
        for group in self.sprites.itervalues():
            for sprite in group:
                if sprite is not None:
                    sprite.delete()

class TileGrid(object):
    '''
    A container and organizer class. maintains sprites that form a transparent 
    grid over the tilemap when in the event mode
    '''
    def __init__(self, map):
        #store the map
        self.map = map
        #create an image for the sprites
        self.grid_image = pyglet.image.create(32, 32)
        #get a rendering batch to draw the grid quickly
        self.renderingBatch = pyglet.graphics.Batch()
        #setup the grid image
        self.setupGridImage()
        #create all the sprites in the grid and store them in a numpy array of dtype object
        self.sprites = self.createGrid()
        
    def setupGridImage(self):
        '''
        draws the black outline around the edge of the tile 
        '''
        self.black_pattern = pyglet.image.SolidColorImagePattern((0, 0, 0, 255))
        self.grid_image = self.black_pattern.create_image(32, 32).get_texture()
        self.cut_pattern = pyglet.image.create(30, 30)
        self.grid_image.blit_into(self.cut_pattern, 1, 1, 0)
                
    def createGrid(self):
        '''
        loops through the maps x and y to create all the necessary sprites
        '''
        shape = (self.map.width, self.map.height)
        sprites = numpy.empty(shape, dtype=object)
        for x in range(shape[0]):
            for y in range(shape[1]):
                sprite = self.makeSprite(x, y)
                sprites[x, y] = sprite
        return sprites
    
    def makeSprite(self, x, y):
        xpos = x * 32
        ypos = ((self.map.height - y) * 32) - 32
        sprite = pyglet.sprite.Sprite(self.grid_image, xpos, ypos, 
                                      batch=self.renderingBatch,)
        sprite.opacity = 80
        return sprite
                                
    def update(self):
        '''
        updates the sprites in the grid so that if the map size changes the grid changes too
        '''
        #if it isn;t the same size as the map
        shape = (self.map.width, self.map.height)
        if self.sprites.shape != shape:
            self.resize(*shape)
                
    def Draw(self):
        '''
        draws the rendering batch and thus all the attached sprites
        '''
        self.renderingBatch.draw()
        
    def  __del__(self):
        '''
        to be sure the sprites get deleted properly
        '''
        self.destroy()
        
    def destroy(self):
        '''
        delete all the sprites
        '''
        for sprite in self.sprites.flatten():
            sprite.delete()
            
    def resize(self, xsize=1, ysize=1):
        '''
        '''
        newdata = numpy.empty((xsize, ysize), dtype=object)
        shape = self.sprites.shape
        mask = [0, 0, 0]
        if xsize >= shape[0]:
            mask[0] = shape[0]
        else:
            mask[0] = xsize
        if ysize >= shape[1]:
            mask[1] = shape[1]
        else:
            mask[1] = ysize
        newdata[:mask[0], :mask[1]] = self.sprites[:mask[0], :mask[1]]
        self.sprites = newdata
        shape = self.sprites.shape
        for x in range(shape[0]):
            for y in range(shape[1]):
                if self.sprites[x, y] is None:
                    self.sprites[x, y] = self.makeSprite(x, y)
                else:
                    xpos = x * 32
                    ypos = ((self.map.height - y) * 32) - 32
                    self.sprites[x, y].set_position(xpos, ypos)
                
class Tilemap(object):
    
    def __init__(self, table, cache, tileset="", autotiles=[]):
        self.cache = cache
        self.table = table
        self.tile_ids = numpy.zeros(self.table._data.shape)
        self.renderingBatches = []
        self.sprites = []
        self.blank_tile = pyglet.image.create(32, 32)
        self.dimmingImagePatteren = None
        self.dimmingImage = None
        self.dimmingSprite = None
        self.dimmingSpriteWidth = 0
        self.dimmingSpriteHeight = 0
        self.activeLayer = 0
        self.LayerDimming = True
        self.x = self.oldx = self.y = self.oldy = 0
        self.autotile_names = autotiles
        self.tileset_name = tileset
        self.ordered_groups = []
        for i in range(self.table._data.shape[2]):
            self.ordered_groups.append(pyglet.graphics.OrderedGroup(i))
            self.renderingBatches.append(pyglet.graphics.Batch())
        self.tiles = self.createTilemap()
    
    def UpdateDimmingSprite(self, width, height):
        '''
        '''
        if width != self.dimmingSpriteWidth or height != self.dimmingSpriteHeight:
            self.dimmingSpriteWidth = width
            self.dimmingSpriteHeight = height
            if self.dimmingImagePatteren is None:
                self.dimmingImagePatteren = pyglet.image.SolidColorImagePattern((0, 0, 0, 255))
            self.dimmingImage = self.dimmingImagePatteren.create_image(width, height).get_texture()
            self.dimmingSprite = pyglet.sprite.Sprite(self.dimmingImage, 0, 0)
            self.dimmingSprite.opacity = 180
            
    def setDimXY(self, x, y):
        '''
        '''
        if self.dimmingSprite is not None:
            self.dimmingSprite.set_position(x, y)
            
    def createTilemap(self):
        '''
        '''
        shape = self.table._data.shape
        sprites = numpy.empty(shape, dtype=object)
        for x in range(shape[0]):
            for y in range(shape[1]):
                for z in range(shape[2]):
                    sprite = self.makeSprite(x, y, z)
                    sprites[x, y, z] = sprite
        return sprites
    
    def makeSprite(self, x, y, z):
        xpos = x * 32
        ypos = ((self.table._data.shape[1] - y) * 32) - 32
        sprite = pyglet.sprite.Sprite(self.blank_tile, xpos, ypos, 
                                      batch=self.renderingBatches[z], group=self.ordered_groups[z])
        return sprite
                       
    def update(self):
        '''
        '''
        #if the arn't the same size
        if self.tile_ids.shape != self.table._data.shape:
            self.resize(*self.table._data.shape)
        #find the tiles who's ids have changed
        indexes = numpy.argwhere(self.table._data != self.tile_ids)
        #we have the idexes of the tiles we need to update so copy 
        #the changed data over so we don;t have to update again
        self.tile_ids[:] = self.table._data[:]
        for index in indexes:
            self.set_image(tuple(index), self.tile_ids[tuple(index)])
         
    def set_image(self, index, id):
        '''
        '''
        tile = self.tiles[index]
        #if for some reason the sprite does not exist (ie. the map was resized) make it
        if tile is None:
            x, y, z = index
            tile = self.makeSprite(x, y, z)
            self.tiles[index] = tile
            
        flag = False
        #get the tile bitmap
        if id < 384:
            if id <= 47:
                bitmap = self.blank_tile
            else:
                #get the filename
                autotile = self.autotile_names[int(id) / 48 - 1]
                #get the right pattern
                pattern = id % 48
                #collect the tile form the cache checking the local project folder
                #and the system RTP folder
                bitmap = self.cache.AutotilePattern(autotile, pattern, RTP_Location)
                if not bitmap:
                    bitmap = self.cache.AutotilePattern(autotile, pattern, RTP_Location)
                if not bitmap:
                    flag = True
                    print "could not get autotile"
                    bitmap = self.blank_tile
        #normal tile
        else:
            #get the tile bitmap
            bitmap = self.cache.Tile(self.tileset_name, id, 0, RTP_Location)
            if not bitmap:
                bitmap = self.cache.Tile(self.tileset_name, id, 0, RTP_Location)
            if not bitmap:
                flag = True
                print "could not get tile"
                bitmap = self.blank_tile
        #draw the tile to the surface
        tile.image = bitmap
        
    def translate(self, x, y):
        '''
        '''
        for sprite in self.tiles.flatten():
            sprite.set_position(sprite.x + x, sprite.y + y)
            
    def SetLayerOpacity(self, layer, opacity):
        '''
        '''
        layer = self.tiles[:, :, layer]
        for sprite in layer.flatten():
            sprite.opacity = opacity
            
    def SetActiveLayer(self, layer):
        '''
        '''
        self.activeLayer = layer
        if layer == (self.table._data.shape[2] + 1):
            for z in range(self.table._data.shape[2]):
                self.SetLayerOpacity(z, 255)
        else:
            if self.LayerDimming:
                for z in range(self.table._data.shape[2]):
                    if z <= self.activeLayer:
                        self.SetLayerOpacity(z, 255)
                    else:
                        self.SetLayerOpacity(z, 80)
    
    def SetLayerDimming(self, bool):
        '''
        '''
        self.LayerDimming = bool
        if self.LayerDimming:
            for z in range(self.table._data.shape[2]):
                if z <= self.activeLayer:
                    self.SetLayerOpacity(z, 255)
                else:
                    self.SetLayerOpacity(z, 80)
        else:
            for z in range(self.table._data.shape[2]):
                self.SetLayerOpacity(z, 255)
        
    def Draw(self):
        '''
        '''
        for z in range(len(self.renderingBatches)):
            if z == self.activeLayer and self.LayerDimming: #and z != 0
                if self.dimmingSprite is not None:
                    self.dimmingSprite.draw()
            self.renderingBatches[z].draw()
            
    def  __del__(self):
        '''
        '''
        self.destroy()
        
    def destroy(self):
        '''
        '''
        for sprite in self.tiles.flatten():
            sprite.delete()  
        
    def resize(self, xsize=1, ysize=1, zsize=1):
        '''
        '''
        newdata = numpy.empty((xsize, ysize, zsize), dtype=object)
        shape = self.tiles.shape
        mask = [0, 0, 0]
        if xsize >= shape[0]:
            mask[0] = shape[0]
        else:
            mask[0] = xsize
        if ysize >= shape[1]:
            mask[1] = shape[1]
        else:
            mask[1] = ysize
        if zsize >= shape[2]:
            mask[2] = shape[2]
        else:
            mask[2] = zsize  
        newdata[:mask[0], :mask[1], :mask[2]] = self.tiles[:mask[0], :mask[1], :mask[2]]
        self.tiles = newdata
        shape = self.tiles.shape
        for x in range(shape[0]):
            for y in range(shape[1]):
                for z in range(shape[2]):
                    if self.tiles[x, y, z] is not None:
                        xpos = x * 32
                        ypos = ((self.map.height - y) * 32) - 32
                        self.tiles[x, y, z].set_position(xpos, ypos)
        newdata = numpy.zeros((xsize, ysize, zsize))
        shape = self.tile_ids.shape
        mask = [0, 0, 0]
        if xsize >= shape[0]:
            mask[0] = shape[0]
        else:
            mask[0] = xsize
        if ysize >= shape[1]:
            mask[1] = shape[1]
        else:
            mask[1] = ysize
        if ysize >= shape[2]:
            mask[2] = shape[2]
        else:
            mask[2] = zsize  
        newdata[:mask[0], :mask[1], :mask[2]] = self.tile_ids[:mask[0], :mask[1], :mask[2]]
        self.tile_ids = newdata     
               
class MouseSprite(object):
    
    def __init__(self):
        pass
    
class TilemapPanel(pygletwx.GLPanel):

    def __init__(self, parent, map, tilesets, toolbar, id=wx.ID_ANY):
        super(TilemapPanel, self).__init__(parent, id, wx.DefaultPosition, wx.Size(800, 600), 
              wx.VSCROLL | wx.HSCROLL)
        
        #set data
        self.map = map
        self.tilesets = tilesets
        self.NeedRedraw = False
        self.activeLayer = 0
        self.toolbar = toolbar
        self.toolbar.mapwin = self
        self.translateX = 0
        self.translateY = 0
        
        #set up scrollbars
        size = self.GetVirtualSizeTuple()
        width = self.map.width * 32
        height = self.map.height * 32
        self.SetScrollbar(wx.HORIZONTAL, 0, size[0], width, refresh=True)
        self.SetScrollbar(wx.VERTICAL, 0, size[1], height, refresh=True)
        
        #scrollbar event
        self.Bind(wx.EVT_SCROLLWIN_TOP, self.scroll_top)
        self.Bind(wx.EVT_SCROLLWIN_BOTTOM, self.scroll_bottom)
        self.Bind(wx.EVT_SCROLLWIN_LINEUP, self.scroll_lineup)
        self.Bind(wx.EVT_SCROLLWIN_LINEDOWN, self.scroll_linedown)
        self.Bind(wx.EVT_SCROLLWIN_PAGEUP, self.scroll_pageup)
        self.Bind(wx.EVT_SCROLLWIN_PAGEDOWN, self.scroll_pagedown)
        self.Bind(wx.EVT_SCROLLWIN_THUMBTRACK, self.update_scroll_pos)
        self.Bind(wx.EVT_SCROLLWIN_THUMBRELEASE, self.update_scroll_pos)
        # mouse eent
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftButtonEvent)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftButtonEvent)
        self.Bind(wx.EVT_MOTION, self.OnLeftButtonEvent)
        # UI update
        self.Bind(wx.EVT_UPDATE_UI, self.Update) 

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

        # draw the mouse
        
        
    def SetMouseXY(self, event):
        x, y = self.ConvertEventCoords(event)
        x = x / int(32 * self.zoom)
        y = y / int(32 * self.zoom)
        self.mouse_x, self.mouse_y = x, y

    def ConvertEventCoords(self, event):
        newpos = self.CalcUnscrolledPosition(event.GetX(), event.GetY())
        return newpos
            
    def SetOrigin(self):
        size = self.GetGLExtents()
        gl.glViewport(0, 0,  size.width,  size.height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(0,  size.width, 0,  size.height, -1, 1)
        x = -self.GetScrollPos(wx.HORIZONTAL)
        y = -(self.map.height * 32) + size.height + self.GetScrollPos(wx.VERTICAL)
        gl.glTranslatef(x, y, 0)
        self.translateX = x
        self.translateY = y
        self.tilemap.setDimXY(-x, -y)
        gl.glMatrixMode(gl.GL_MODELVIEW)
    
    def create_objects(self):
        '''create opengl objects when opengl is initialized'''
        table = self.map.data
        tileset = self.tilesets[self.map.tileset_id]
        self.cache = Cache()
        self.tilemap = Tilemap(table, self.cache, tileset.tileset_name, tileset.autotile_names)
        self.SetActiveLayer(self.activeLayer)
        self.tileGrid = TileGrid(self.map)
        self.eventGrid = EventGrid(self.map, self.cache, tileset.tileset_name)
        
    def update_object_resize(self, width, height):
        '''called when the window recieves only if opengl is initialized'''
        #update the scrollbar widths
        self.tilemap.UpdateDimmingSprite(width, height)
        self.SetOrigin()
        size = self.GetVirtualSizeTuple()
        self.SetScrollbar(wx.HORIZONTAL, self.GetScrollPos(wx.HORIZONTAL), size[0], 
                          self.map.width * 32, refresh=True)
        self.SetScrollbar(wx.VERTICAL, self.GetScrollPos(wx.VERTICAL), size[1], 
                          self.map.height * 32, refresh=True)
               
    def draw_objects(self):
        '''called in the middle of ondraw after the buffer has been cleared'''
        self.tilemap.update()
        self.tilemap.Draw()
        if self.activeLayer == (self.map.data._data.shape[2] + 1):
            self.tileGrid.Draw()
            self.eventGrid.update()
            self.eventGrid.Draw()
        
    def Update(self, event):
        self.PrepareGL() 
        if self.NeedRedraw:
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
        print 'Scroll Top'
   
    def scroll_bottom(self, event):
        print 'Scroll Bottom'
        
    def OnScroll(self, orient, pos):
        size = self.GetVirtualSizeTuple()
        if orient == wx.HORIZONTAL:
            thumb = size[0]
            range = self.map.width * 32
        elif orient == wx.VERTICAL:
            thumb = size[1]
            range = self.map.height * 32
        self.SetOrigin()
        self.OnDraw()
        self.SetScrollbar(orient, pos, thumb, range, refresh=True)
        
    def SetActiveLayer(self, layer):
        #if the selected layer is the event layer
        self.tilemap.setDimXY(-self.translateX, -self.translateY)
        self.activeLayer = layer
        self.tilemap.SetActiveLayer(layer)
        self.OnDraw()
    
    def SetLayerDimming(self, bool):
        self.tilemap.SetLayerDimming(bool)
        self.OnDraw()

class MapPanel(wx.Panel):
    
    def __init__(self, parent, map, tilesets,  id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0):
        '''lays out a toolbar and the map window'''
        super(MapPanel, self).__init__(parent, id, pos, size, style)
        #set data
        self.map = map
        self.tilesets = tilesets
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        #toolbar
        self.Create_Toolbar()
        #map
        self.mapwin = TilemapPanel(self, self.map, self.tilesets, self.toolbar)
        self.sizer.Add(self.mapwin, 1, wx.EXPAND)
        #set the sizer and layout the panel
        self.SetSizer(self.sizer)
        self.Layout()
           
    def Create_Toolbar(self):
        '''creates the toolbar and adds tools'''
        self.toolbar = MapToolbar(self, self.map)
        self.sizer.Add(self.toolbar, 0, wx.EXPAND)
               
class MapToolbar(wx.ToolBar):
    
    def __init__(self, parent, map, style=0):
        '''Toolbar for the map editor'''
        super(MapToolbar, self).__init__(parent, style=style)
        
        self.map = map
        self.mapwin = None
        self.layers = self.map.data._data.shape[2]
        self.layerChoiceIDs = {}
        self.layerSet = False
        self.SetupToolIDs()
        self.SetupTools()
        self.BindToolEvents()
        
    def SetupTools(self):
        tsize = (16,16)
        new_bmp =  wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR, tsize)
        self.SetToolBitmapSize(tsize)
        #add layer tools
        #generate choice list 
        layerChoices = self.GenLayerChoices()
        self.layerChoice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition,
                                    wx.DefaultSize, layerChoices, 0)
        self.layerChoice.SetSelection(0)
        self.AddControl(self.layerChoice)
        self.AddSeparator() 
        # a dimlayers choice box
        self.dimLayersCB = wx.CheckBox(self, label="Dim Layers")
        self.dimLayersCB.SetValue(True)
        self.AddControl(self.dimLayersCB)
        self.AddSeparator() 
        
        self.Realize() 
         
    def GenLayerChoices(self):
        choices = []
        self.layerChoiceIDs = {}
        for z in range(self.map.data._data.shape[2]):
            choice = "Layer %s" % (z + 1)
            self.layerChoiceIDs[choice] = z
            choices.append(choice)
        self.layerChoiceIDs["Event Layer"] = self.map.data._data.shape[2] + 1
        choices.append("Event Layer")
        return choices

    def BindToolEvents(self):
        #layer choice
        self.Bind(wx.EVT_CHOICE, self.OnLayerChoice, self.layerChoice)
        self.Bind(wx.EVT_UPDATE_UI, self.UpdateLayerChoices, self.layerChoice)
        #dim layers box
        self.Bind(wx.EVT_CHECKBOX, self.OnDimLayersChoice, self.dimLayersCB)
    
    def SetupToolIDs(self):
        self.layer1ID = 1
        self.layer2ID = 2
        self.layer3ID = 3
        self.layer4ID = 4
        self.PenID = 5
        self.RecID = 6
        self.ElipID = 7
        self.BucketID = 8
        self.SelectID = 9
                
    def OnDimLayersChoice(self, event):
        if self.mapwin is not None:
            self.mapwin.SetLayerDimming(event.IsChecked())
    
    def OnLayerChoice(self, event):
        self.layerSet = False
        if self.mapwin is not None:
            self.layerSet = True
            layer = self.layerChoiceIDs[self.layerChoice.GetItems()[self.layerChoice.GetSelection()]]
            self.mapwin.SetActiveLayer(layer)
    
    def UpdateLayerChoices(self, event): 
        if not(self.layers == self.map.data._data.shape[2]):
            self.layers = self.map.data._data.shape[2]
            choices = self.GenLayerChoices()
            self.layerChoice.SetItems(choices)
        if (self.mapwin is not None) and (not self.layerSet):
            self.layerSet = True
            selection = self.layerChoice.GetSelection()
            items = self.layerChoice.GetItems()
            layer = self.layerChoiceIDs[items[selection]]
            self.mapwin.SetActiveLayer(layer) 
            
        
    
class TestFrame(wx.Frame):
    '''A simple class for using OpenGL with wxPython.'''

    def __init__(self, parent, id, title, pos=wx.DefaultPosition,
                 size=wx.Size(800, 600), style=wx.DEFAULT_FRAME_STYLE,
                 name='frame'):
        super(TestFrame, self).__init__(parent, id, title, pos, size, style, name)
        
        self.mainsizer = wx.BoxSizer(wx.HORIZONTAL)
        #self.GLPanel1 = TestGlPanel(self)
        #self.mainsizer.Add(self.GLPanel1, 1, wx.EXPAND, 5)
        #self.GLPanel2 = TestGlPanel(self, wx.ID_ANY, (20, 20))
        #self.mainsizer.Add(self.GLPanel2, 1, wx.EXPAND, 5)
        
        self.map = self.load_data('data/Map001.xppy')
        self.tilesets = self.load_data('data/Tilesets.xppy')
        
        self.MapEditorPanel = MapPanel(self, self.map, self.tilesets)
        self.mainsizer.Add(self.MapEditorPanel, 1, wx.EXPAND, 5)
        
        self.SetSizer(self.mainsizer)
        self.Layout()

        
    def load_data(self, filename):
        f = open(os.path.normpath(filename), 'rb')
        data = cPickle.load(f)
        f.close()
        return data

    

app = wx.App(redirect=False)
frame = TestFrame(None, wx.ID_ANY, 'GL Window')
frame.Show()

app.MainLoop()
app.Destroy()