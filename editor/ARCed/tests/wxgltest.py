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
        if not self.sprites.has_key(key) or self.sprites[key][0] == None:
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
                if self.sprites[key][0] != None:
                    if self.sprites[key][0].x != xpos or self.sprites[key][0].y != ypos:
                        self.sprites[key][0].set_position(xpos, ypos)
                    if self.sprites[key][1].x != xpos or self.sprites[key][1].y != ypos:
                        self.sprites[key][1].set_position(xpos + 4, ypos + 4)
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
                if sprite != None:
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
                if sprite != None:
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
        for x in xrange(shape[0]):
            for y in xrange(shape[1]):
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
        for x in xrange(shape[0]):
            for y in xrange(shape[1]):
                if self.sprites[x, y] == None:
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
        self.tiles = self.createTilemap()
    
    def UpdateDimmingSprite(self, width, height, scale):
        '''
        '''
        if width != self.dimmingSpriteWidth or height != self.dimmingSpriteHeight or scale != self.dimmingSprite.scale:
            self.dimmingSpriteWidth = width
            self.dimmingSpriteHeight = height
            if self.dimmingImagePatteren == None:
                self.dimmingImagePatteren = pyglet.image.SolidColorImagePattern((0, 0, 0, 255))
            self.dimmingImage = self.dimmingImagePatteren.create_image(width, height).get_texture()
            self.dimmingSprite = pyglet.sprite.Sprite(self.dimmingImage, 0, 0)
            self.dimmingSprite.opacity = 180
            self.dimmingSprite.scale = scale
            
    def setDimXY(self, x, y):
        '''
        '''
        if self.dimmingSprite != None:
            self.dimmingSprite.set_position(x, y)
            
    def createTilemap(self):
        '''
        '''
        shape = self.table._data.shape
        sprites = numpy.empty(shape, dtype=object)
        for x in xrange(shape[0]):
            for y in xrange(shape[1]):
                for z in xrange(shape[2]):
                    sprite = self.makeSprite(x, y, z)
                    sprites[x, y, z] = sprite
        return sprites

    def get_rendering_batch(self, z):
        if len(self.renderingBatches) < z:
            for i in xrange(len(self.renderingBatches), z + 1):
                self.renderingBatches.append(pyglet.graphics.Batch())
        return self.renderingBatches[z]

    def get_ordered_groups(self, z):
        if len(self.ordered_groups) < z:
            for i in xrange(len(self.ordered_groups), z + 1):
                self.ordered_groups.append(pyglet.graphics.OrderedGroup(i))
        return self.ordered_groups[z]


    
    def makeSprite(self, x, y, z):
        xpos = x * 32
        ypos = ((self.table._data.shape[1] - y) * 32) - 32
        sprite = pyglet.sprite.Sprite(self.blank_tile, xpos, ypos, 
                                      batch=self.get_rendering_batch(z), group=self.get_ordered_groups(z))
        return sprite
                       
    def update(self):
        '''
        checks for change in tile ids and updates the tilemap
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
        if tile == None:
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
            for z in xrange(self.table._data.shape[2]):
                self.SetLayerOpacity(z, 255)
        else:
            if self.LayerDimming:
                for z in xrange(self.table._data.shape[2]):
                    if z <= self.activeLayer:
                        self.SetLayerOpacity(z, 255)
                    else:
                        self.SetLayerOpacity(z, 80)
    
    def SetLayerDimming(self, bool):
        '''
        '''
        self.LayerDimming = bool
        if self.LayerDimming:
            for z in xrange(self.table._data.shape[2]):
                if z <= self.activeLayer:
                    self.SetLayerOpacity(z, 255)
                else:
                    self.SetLayerOpacity(z, 80)
        else:
            for z in xrange(self.table._data.shape[2]):
                self.SetLayerOpacity(z, 255)

    def HideOffScreenSprites(self, x, y, width, height):
        #get tiles on screen
        on_screen = set(self.tiles[x:x + width, y:y + height].flatten())
        not_on_screen = [x for x in self.tiles.flatten() if x not in on_screen]
        for tile in on_screen:
            tile.visable = True
        for tile in not_onscren:
            tile.visable = False
        
    def Draw(self):
        '''
        '''
        for z in xrange(len(self.renderingBatches)):
            if z == self.activeLayer and self.LayerDimming: #and z != 0
                if self.dimmingSprite != None:
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
        for x in xrange(shape[0]):
            for y in xrange(shape[1]):
                for z in xrange(shape[2]):
                    if self.tiles[x, y, z] != None:
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
    
    def __init__(self, map):
        #setup data
        self.map = map
        self.cornerSprites = []
        self.cornerRenderingBatch = pyglet.graphics.Batch()
        self.topRowSprites = []
        self.bottomRowSprites = []
        self.horizontalRenderingBatch = pyglet.graphics.Batch()
        self.leftRowSprites = []
        self.rightRowSprites = []
        self.verticalRenderingBatch = pyglet.graphics.Batch()
        self.TBCorners = []
        self.TBRenderingBatch = pyglet.graphics.Batch()
        self.LRCorners = []
        self.LRRenderingBatch = pyglet.graphics.Batch()
        self.sprites = []
        self.singleMode = False
        self.topLeftPos = [-1, -1]
        self.bottomRightPos = [-1, -1]
        #create images to use
        self.setupImages()
        #create the sprites
        self.setupSprites()
            
    def setupImages(self):
        #get out solid color patterns
        blackPattern = pyglet.image.SolidColorImagePattern((0, 0, 0, 255))
        whitePattern = pyglet.image.SolidColorImagePattern((255, 255, 255, 255))
        #create the single image
        self.singleImage = blackPattern.create_image(32, 32).get_texture()
        whiteInner = whitePattern.create_image(30, 30)
        self.singleImage.blit_into(whiteInner, 1, 1, 0)
        blackInner = blackPattern.create_image(26, 26)
        self.singleImage.blit_into(blackInner, 3, 3, 0)
        clearInner = pyglet.image.create(24, 24)
        self.singleImage.blit_into(clearInner, 4, 4, 0)
        #get the pieces to construct the other sprites from the single sprite
        TLCorner = self.singleImage.get_region(0, 16, 16, 16).get_image_data()
        BLCorner = self.singleImage.get_region(0, 0, 16, 16).get_image_data()
        TRCorner = self.singleImage.get_region(16, 16, 16, 16).get_image_data()
        BRCorner = self.singleImage.get_region(16, 0, 16, 16).get_image_data()
        striateBH = self.singleImage.get_region(8, 0, 16, 16).get_image_data()
        striateLV = self.singleImage.get_region(0, 8, 16, 16).get_image_data()
        striateTH = self.singleImage.get_region(8, 16, 16, 16).get_image_data()
        striateRV = self.singleImage.get_region(16, 8, 16, 16).get_image_data()
        #Top Left corner
        self.TLCorner = pyglet.image.create(32, 32).get_texture()
        self.TLCorner.blit_into(TLCorner, 0, 16, 0)
        self.TLCorner.blit_into(striateLV, 0, 0, 0)
        self.TLCorner.blit_into(striateTH, 16, 16, 0)
        #Bottom Left corner
        self.BLCorner = pyglet.image.create(32, 32).get_texture()
        self.BLCorner.blit_into(BLCorner, 0, 0, 0)
        self.BLCorner.blit_into(striateLV, 0, 16, 0)
        self.BLCorner.blit_into(striateBH, 16, 0, 0)
        #Top Right corner
        self.TRCorner = pyglet.image.create(32, 32).get_texture()
        self.TRCorner.blit_into(TRCorner, 16, 16, 0)
        self.TRCorner.blit_into(striateRV, 16, 0, 0)
        self.TRCorner.blit_into(striateTH, 0, 16, 0)
        #Bottom Right corner
        self.BRCorner = pyglet.image.create(32, 32).get_texture()
        self.BRCorner.blit_into(BRCorner, 16, 0, 0)
        self.BRCorner.blit_into(striateRV, 16, 16, 0)
        self.BRCorner.blit_into(striateBH, 0, 0, 0)
        #Left Vertical
        self.LeftV = pyglet.image.create(32, 32).get_texture()
        self.LeftV.blit_into(striateLV, 0, 0, 0)
        self.LeftV.blit_into(striateLV, 0, 16, 0)
        #Right Vertical
        self.RightV = pyglet.image.create(32, 32).get_texture()
        self.RightV.blit_into(striateRV, 16, 0, 0)
        self.RightV.blit_into(striateRV, 16, 16, 0)
        #Left Corners
        self.LeftC = pyglet.image.create(32, 32).get_texture()
        self.LeftC.blit_into(BLCorner, 0, 0, 0)
        self.LeftC.blit_into(TLCorner, 0, 16, 0)
        self.LeftC.blit_into(striateTH, 16, 16, 0)
        self.LeftC.blit_into(striateBH, 16, 0, 0)
        #Right Corners
        self.RightC = pyglet.image.create(32, 32).get_texture()
        self.RightC.blit_into(TRCorner, 16, 16, 0)
        self.RightC.blit_into(BRCorner, 16, 0, 0)
        self.RightC.blit_into(striateTH, 0, 16, 0)
        self.RightC.blit_into(striateBH, 0, 0, 0)
        #Top Corners
        self.TopC = pyglet.image.create(32, 32).get_texture()
        self.TopC.blit_into(TRCorner, 16, 16, 0)
        self.TopC.blit_into(TLCorner, 0, 16, 0)
        self.TopC.blit_into(striateLV, 0, 0, 0)
        self.TopC.blit_into(striateRV, 16, 0, 0)
        #Bottom Corners
        self.BottomC = pyglet.image.create(32, 32).get_texture()
        self.BottomC.blit_into(BLCorner, 0, 0, 0)
        self.BottomC.blit_into(BRCorner, 16, 0, 0)
        self.BottomC.blit_into(striateLV, 0, 16, 0)
        self.BottomC.blit_into(striateRV, 16, 16, 0)
        #Top Horizontal 
        self.TopH = pyglet.image.create(32, 32).get_texture()
        self.TopH.blit_into(striateTH, 0, 16, 0)
        self.TopH.blit_into(striateTH, 16, 16, 0)
        #Bottom Horizontal 
        self.BottomH = pyglet.image.create(32, 32).get_texture()
        self.BottomH.blit_into(striateBH, 0, 0, 0)
        self.BottomH.blit_into(striateBH, 16, 0, 0)
        
    def makeSprite(self, type, x=-1, y=-1):
        #correct range
        if type < 0:
            type = 0
        if type > 11:
            type = 11
        #create the right sprite
        if type == 0: # TLC
            sprite = pyglet.sprite.Sprite(self.TLCorner, x * 32, y * 32, batch=self.cornerRenderingBatch)
        elif type == 1: # TRC
            sprite = pyglet.sprite.Sprite(self.TRCorner, x * 32, y * 32, batch=self.cornerRenderingBatch)
        elif type == 2: # BLC
            sprite = pyglet.sprite.Sprite(self.BLCorner, x * 32, y * 32, batch=self.cornerRenderingBatch)
        elif type == 3: # BRC
            sprite = pyglet.sprite.Sprite(self.BRCorner, x * 32, y * 32, batch=self.cornerRenderingBatch)
        elif type == 4: # TH
            sprite = pyglet.sprite.Sprite(self.TopH, x * 32, y * 32, batch=self.horizontalRenderingBatch)
        elif type == 5: # BH
            sprite = pyglet.sprite.Sprite(self.BottomH, x * 32, y * 32, batch=self.horizontalRenderingBatch)
        elif type == 6: # LV
            sprite = pyglet.sprite.Sprite(self.LeftV, x * 32, y * 32, batch=self.verticalRenderingBatch)
        elif type == 7: # RV
            sprite = pyglet.sprite.Sprite(self.RightV, x * 32, y * 32, batch=self.verticalRenderingBatch)
        elif type == 8: # LC
            sprite = pyglet.sprite.Sprite(self.LeftC, x * 32, y * 32, batch=self.LRRenderingBatch)
        elif type == 9: # RC
            sprite = pyglet.sprite.Sprite(self.RightC, x * 32, y * 32, batch=self.LRRenderingBatch)
        elif type == 10: #TC
            sprite = pyglet.sprite.Sprite(self.TopC, x * 32, y * 32, batch=self.TBRenderingBatch)
        elif type == 11: #BC
            sprite = pyglet.sprite.Sprite(self.BottomC, x * 32, y * 32, batch=self.TBRenderingBatch)
        #add the sprite to the sprites array so we can keep track of it 
        self.sprites.append(sprite)
        # return the sprite
        return sprite
        
    def setupSprites(self):
        self.singleTileSprite = pyglet.sprite.Sprite(self.singleImage, -1, -1)
        self.sprites.append(self.singleTileSprite)
        #make corner sprites
        for type in xrange(4): 
            self.cornerSprites.append(self.makeSprite(type))
        #add a striate sprite for each side, the lists will expand or contract as needed
        #self.topRowSprites.append(self.makeSprite(4))
        #self.bottomRowSprites.append(self.makeSprite(5))
        #self.leftRowSprites.append(self.makeSprite(6))
        #self.rightRowSprites.append(self.makeSprite(7))
        #add the left right corners
        self.LRCorners.append(self.makeSprite(8))
        self.LRCorners.append(self.makeSprite(9))
        #add the top bottom corners
        self.TBCorners.append(self.makeSprite(10))
        self.TBCorners.append(self.makeSprite(11))
       
    def setTopLeft(self, x, y):
        self.topLeftPos[0] = x
        self.topLeftPos[1] = y
        
    def setBottomRight(self, x, y):
        self.bottomRightPos[0] = x
        self.bottomRightPos[1] = y   
        
    def update(self):
        '''
        updates the positions of the sprite used to represent the mouse cursor
        '''
        fourCornersFlag = False
        verticalFlag = False
        horizontalFlag = False
        LRFlag = False
        TBFlag = False
        width = self.bottomRightPos[0] - self.topLeftPos[0]
        height = self.bottomRightPos[1] - self.topLeftPos[1]
        if self.singleMode or (width == 0 and height == 0):
            #update the positions of the single tile sprite
            self.singleTileSprite.set_position(self.topLeftPos[0] * 32, 
                                               ((self.map.height - self.topLeftPos[1]) * 32) - 32)
        elif width != 0:
            if abs(width) > 1:
                horizontalFlag = True
            if height == 0:
                LRFlag = True
            else:
                fourCornersFlag = True
                if abs(height) > 1:
                    verticalFlag = True      
        elif height != 0:
            if abs(height) > 1:
                verticalFlag = True
            if width == 0:   
                TBFlag = True
            else: 
                fourCornersFlag = True
                if abs(width) > 1:
                    horizontalFlag = True 
        
        if width >= 0:
            TLx = self.topLeftPos[0]
            BRx = self.bottomRightPos[0]
        elif width < 0:
            TLx = self.bottomRightPos[0]
            BRx = self.topLeftPos[0]
        if height >= 0:
            TLy = self.map.height - self.topLeftPos[1]
            BRy = self.map.height - self.bottomRightPos[1]
        elif height < 0:
            TLy = self.map.height - self.bottomRightPos[1]
            BRy = self.map.height - self.topLeftPos[1]
                 
        if horizontalFlag:
#            
#            sprites = self.topRowSprites
#            self.topRowSprites = []
#            for sprite in sprites:
#                sprite.delete()
#                self.sprites.remove(sprite)
#            sprites = self.bottomRowSprites
#            self.bottomRowSprites = []
#            for sprite in sprites:
#                sprite.delete()
#                self.sprites.remove(sprite)
            #make sure that there is the right number of top row sprites
            if len(self.topRowSprites) < abs(width) - 1:
                for i in xrange(abs(width) - 1 - len(self.topRowSprites)):
                    self.topRowSprites.append(self.makeSprite(4))
            else:
                sprites = self.topRowSprites
                self.topRowSprites = sprites[:abs(width) - 1]
                for sprite in sprites[abs(width) - 1:]:
                    sprite.delete()
                    self.sprites.remove(sprite)
            #make sure that there is the right number of bottom row sprites
            if len(self.bottomRowSprites) < abs(width) - 1:
                for i in xrange(abs(width) - 1 - len(self.bottomRowSprites)):
                    self.bottomRowSprites.append(self.makeSprite(5))
            else:
                sprites = self.bottomRowSprites
                self.bottomRowSprites = sprites[:abs(width) - 1]
                for sprite in sprites[abs(width) - 1:]:
                    sprite.delete()
                    self.sprites.remove(sprite)
            #update the positions of the horizontal sprites
            for x in xrange(len(self.topRowSprites)):
                self.topRowSprites[x].set_position((TLx + x + 1) * 32, (TLy * 32) - 32)
                self.bottomRowSprites[x].set_position((TLx + x + 1) * 32, (BRy * 32) - 32)          
        if verticalFlag:
            sprites = self.leftRowSprites
#            self.leftRowSprites = []
#            for sprite in sprites:
#                sprite.delete()
#                self.sprites.remove(sprite)
#            sprites = self.rightRowSprites
#            self.rightRowSprites = []
#            for sprite in sprites:
#                sprite.delete()
#                self.sprites.remove(sprite)
            #make sure that there is the right number of left row sprites
            if len(self.leftRowSprites) < abs(height) - 1:
                for i in xrange(abs(height) - 1 - len(self.leftRowSprites)):
                    self.leftRowSprites.append(self.makeSprite(6))
            else:
                sprites = self.leftRowSprites
                self.leftRowSprites = sprites[:abs(height) - 1]
                for sprite in sprites[abs(height) - 1:]:
                    sprite.delete()
                    self.sprites.remove(sprite)
            #make sure that there is the right number of right row sprites
            if len(self.rightRowSprites) < abs(height) - 1:
                for i in xrange(abs(height) - 1 - len(self.rightRowSprites)):
                    self.rightRowSprites.append(self.makeSprite(7))
            else:
                sprites = self.rightRowSprites
                self.rightRowSprites = sprites[:abs(height) - 1]
                for sprite in sprites[abs(height) - 1:]:
                    sprite.delete()
                    self.sprites.remove(sprite)
            #update the positions vertical sprites
            for y in xrange(len(self.leftRowSprites)):
                self.leftRowSprites[y].set_position(TLx * 32, ((TLy - y - 1) * 32) - 32)
                self.rightRowSprites[y].set_position(BRx * 32, ((TLy - y - 1) * 32) - 32)
        if TBFlag:
            #update the position of the top Bottom corners
            self.TBCorners[0].set_position(TLx * 32, (TLy * 32) - 32)
            self.TBCorners[1].set_position(TLx * 32, (BRy * 32) - 32)
        if LRFlag:
            #update positions of left right corners
            self.LRCorners[0].set_position(TLx * 32, (TLy * 32) - 32)
            self.LRCorners[1].set_position(BRx * 32, (TLy * 32) - 32)
        if fourCornersFlag:
            #update the positions of the corners sprites
            # TL
            self.cornerSprites[0].set_position(TLx * 32, TLy * 32 - 32)
            # TR
            self.cornerSprites[1].set_position(BRx * 32, TLy * 32 - 32)
            # BL
            self.cornerSprites[2].set_position(TLx * 32, BRy * 32 - 32)
            # BR
            self.cornerSprites[3].set_position(BRx * 32, BRy * 32 - 32)
           
                        
    def Draw(self):
        '''
        draws the rendering batchs to render the mouse sprites to the screen 
        '''
        fourCornersFlag = False
        verticalFlag = False
        horizontalFlag = False
        LRFlag = False
        TBFlag = False
        width = self.bottomRightPos[0] - self.topLeftPos[0]
        height = self.bottomRightPos[1] - self.topLeftPos[1]
        if self.singleMode or (width == 0 and height == 0):
            #draw the single tile sprite
            self.singleTileSprite.draw()
        elif width != 0:
            if abs(width) > 1:
                horizontalFlag = True
            if height == 0:
                LRFlag = True
            else:
                fourCornersFlag = True
                if abs(height) > 1:
                    verticalFlag = True      
        elif height != 0:
            if abs(height) > 1:
                verticalFlag = True
            if width == 0:   
                TBFlag = True
            else: 
                fourCornersFlag = True
                if abs(width) > 1:
                    horizontalFlag = True 
                 
        if horizontalFlag:
            #draw the horizontal sprites
            self.horizontalRenderingBatch.draw()
        if verticalFlag:
            #draw the vertical sprites
            self.verticalRenderingBatch.draw() 
        if TBFlag:
            #draw the top and Bottom corners in two tiles
            self.TBRenderingBatch.draw()
        if LRFlag:
            #draw the left and right corners in two tiles
            self.LRRenderingBatch.draw()
        if fourCornersFlag:
            #draw the four corner sprites
            self.cornerRenderingBatch.draw()
        
    def  __del__(self):
        '''
        to be sure the sprites get deleted properly
        '''
        self.destroy()
        
    def destroy(self):
        '''
        delete all the sprites
        '''
        for sprite in self.sprites:
            if sprite != None:
                sprite.delete()

class MouseManager(object):
    
    def __init__(self, mapPanel, map, toolbar):
        self.map = map
        self.toolbar = toolbar
        self.mapPanel = mapPanel
        self.sprite = None
        self.topLeft = [-1, -1]
        self.bottomRight = [-1, -1]
        
    def setSprite(self, sprite):
        self.sprite = sprite
        
    def setTopLeft(self, x, y):
        if x != self.topLeft[0] or y != self.topLeft[1]:
            self.topLeft[0] = x
            self.topLeft[1] = y
            self.mapPanel.NeedRedraw = True
            if self.sprite != None:
                self.sprite.setTopLeft(x, y)
    
    def setBottomRight(self, x, y):
        if x != self.bottomRight[0] or y != self.bottomRight[1]:
            self.bottomRight[0] = x
            self.bottomRight[1] = y
            self.mapPanel.NeedRedraw = True
            if self.sprite != None:
                self.sprite.setBottomRight(x, y)
    
    def setSingleMode(self, value):
        if self.sprite != None:
            self.sprite.singleMode = value
        
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
        self.zoom = 1.0
        self.drawing = False
        self.ToolMouseMode = False
        
        self.MouseManager = MouseManager(self, self.map, self.toolbar)
        
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
        # mouse event
        self.canvas.Bind(wx.EVT_LEFT_DOWN, self.OnLeftButtonEvent)
        self.canvas.Bind(wx.EVT_LEFT_UP, self.OnLeftButtonEvent)
        self.canvas.Bind(wx.EVT_MOTION, self.OnLeftButtonEvent)
        # UI update
        self.Bind(wx.EVT_UPDATE_UI, self.Update) 

    def OnLeftButtonEvent(self, event):
        onEventLayer = (self.activeLayer == (self.map.data._data.shape[2] + 1))
        if not onEventLayer:
            if not self.drawing:
                self.SetTopLeftXY(event)
            self.SetBottomRightXY(event)
        if event.LeftDown():
            self.SetFocus()
            if onEventLayer:
                self.SetTopLeftXY(event)
            self.drawing = True
        elif event.LeftUp():
            self.drawing = False
            if self.drawing:
                self.commitBrush()
        if self.NeedRedraw:
            self.ForceRedraw()
        event.Skip()
        
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
        self.tilemap.UpdateDimmingSprite(int(size.width), int(size.height), 1/self.zoom)
        gl.glViewport(0, 0,  size.width,  size.height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(0,  size.width / self.zoom, 0,  size.height / self.zoom, -1, 1)
        x = (-self.GetScrollPos(wx.HORIZONTAL)) / self.zoom
        y = ((-(self.map.height * 32) + size.height / self.zoom) + self.GetScrollPos(wx.VERTICAL) / self.zoom)
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
        self.tileGrid = TileGrid(self.map)
        self.eventGrid = EventGrid(self.map, self.cache, tileset.tileset_name)
        self.mouseSprite = MouseSprite(self.map)
        self.MouseManager.setSprite(self.mouseSprite)
        self.SetActiveLayer(self.activeLayer, True)
        
    def update_object_resize(self, width, height):
        '''called when the window recieves only if opengl is initialized'''
        #update the scrollbar widths
        self.SetOrigin()
               
    def draw_objects(self):
        '''called in the middle of ondraw after the buffer has been cleared'''
        self.tilemap.update()
        self.tilemap.Draw()
        if self.activeLayer == (self.map.data._data.shape[2] + 1):
            self.tileGrid.Draw()
            self.eventGrid.update()
            self.eventGrid.Draw()
        self.mouseSprite.update()
        self.mouseSprite.Draw()
        
    def Update(self, event):
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
        print 'Scroll Top'
   
    def scroll_bottom(self, event):
        print 'Scroll Bottom'
        
    def OnScroll(self, orient, pos):
        size = self.GetVirtualSizeTuple()
        if orient == wx.HORIZONTAL:
            thumb = size[0]
            range_s = self.map.width * 32 * self.zoom
        elif orient == wx.VERTICAL:
            thumb = size[1]
            range_s = self.map.height * 32 * self.zoom
        self.SetOrigin()
        self.OnDraw()
        self.SetScrollbar(orient, pos, thumb, range_s, refresh=True)
        
    def SetActiveLayer(self, layer, init=False):
        #if the selected layer is the event layer
        self.tilemap.setDimXY(-self.translateX, -self.translateY)
        self.activeLayer = layer
        self.tilemap.SetActiveLayer(layer)
        if layer == (self.map.data._data.shape[2] + 1):
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
    
    def __init__(self, parent, map, style=wx.TB_HORIZONTAL | wx.NO_BORDER | wx.TB_FLAT):
        '''Toolbar for the map editor'''
        super(MapToolbar, self).__init__(parent, style=style)
        
        self.map = map
        self.mapwin = None
        self.layers = self.map.data._data.shape[2]
        self.layerChoiceIDs = {}
        self.layerSet = False
        self.zoomSet = False
        self.SetupToolIDs()
        self.SetupTools()
        self.BindToolEvents()
        
    def SetupTools(self):
        tsize = (16,16)
        new_bmp =  wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR, tsize)
        self.SetToolBitmapSize(tsize)
        self.SetToolSeparation(10)
        self.SetMargins((4, 4))
        #add layer tools
        #generate choice list 
        layerChoices = self.GenLayerChoices()
        self.layerChoice = wx.Choice(self, wx.ID_ANY, size=(-1, -1), choices=layerChoices)
        self.layerChoice.SetSelection(0)
        self.AddControl(self.layerChoice)
        #self.AddSeparator() 
        # a dimlayers choice box
        self.dimLayersCB = wx.CheckBox(self, label="Dim Layers")
        self.dimLayersCB.SetValue(True)
        self.AddControl(self.dimLayersCB)
        self.AddSeparator() 
        # a zoom slider
        zoomChoices = self.GenZoomChoices()
        self.zoomChoice = wx.Choice(self, wx.ID_ANY, size=(-1, -1), choices=zoomChoices)
        self.zoomChoice.SetSelection(1)
        self.AddControl(self.zoomChoice)
        self.Realize() 
        
    def GenLayerChoices(self):
        choices = []
        self.layerChoiceIDs = {}
        for z in xrange(self.map.data._data.shape[2]):
            choice = "Layer %s" % (z + 1)
            self.layerChoiceIDs[choice] = z
            choices.append(choice)
        self.layerChoiceIDs["Event Layer"] = self.map.data._data.shape[2] + 1
        choices.append("Event Layer")
        return choices
    
    def GenZoomChoices(self):
        choices = []
        self.zoomChoiceIDs = {}
        values = [['2x', 2.0], ['1x', 1.0], ['1/2x', 1.0/2.0], #['1/3x', 1.0/3.0], 
                 ['1/4x', 1.0/4.0], ]#['1/5x', 1.0/5.0]]
        for z in values:
            self.zoomChoiceIDs[z[0]] = z[1]
            choices.append(z[0])
        return choices

    def BindToolEvents(self):
        #layer choice
        self.Bind(wx.EVT_CHOICE, self.OnLayerChoice, self.layerChoice)
        self.Bind(wx.EVT_UPDATE_UI, self.UpdateLayerChoices, self.layerChoice)
        #dim layers box
        self.Bind(wx.EVT_CHECKBOX, self.OnDimLayersChoice, self.dimLayersCB)
        #zoom choice
        self.Bind(wx.EVT_CHOICE, self.OnZoomChoice, self.zoomChoice)
        self.Bind(wx.EVT_UPDATE_UI, self.UpdateZoomChoice, self.zoomChoice)
    
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
        if self.mapwin != None:
            self.mapwin.SetLayerDimming(event.IsChecked())
    
    def OnLayerChoice(self, event):
        self.layerSet = False
        if self.mapwin != None:
            self.layerSet = True
            layer = self.layerChoiceIDs[self.layerChoice.GetItems()[self.layerChoice.GetSelection()]]
            self.mapwin.SetActiveLayer(layer)
    
    def OnZoomChoice(self, event):
        self.zoomSet = False
        if self.mapwin != None:
            self.zoomSet = True
            zoom = self.zoomChoiceIDs[self.zoomChoice.GetItems()[self.zoomChoice.GetSelection()]]
            self.mapwin.SetZoom(zoom)
    
    def UpdateLayerChoices(self, event): 
        if not(self.layers == self.map.data._data.shape[2]):
            self.layers = self.map.data._data.shape[2]
            choices = self.GenLayerChoices()
            self.layerChoice.SetItems(choices)
        if (self.mapwin != None) and (not self.layerSet):
            self.layerSet = True
            selection = self.layerChoice.GetSelection()
            items = self.layerChoice.GetItems()
            layer = self.layerChoiceIDs[items[selection]]
            self.mapwin.SetActiveLayer(layer) 
            
    def UpdateZoomChoice(self, event): 
        if (self.mapwin != None) and (not self.zoomSet):
            self.zoomSet = True
            selection = self.zoomChoice.GetSelection()
            items = self.zoomChoice.GetItems()
            layer = self.zoomChoiceIDs[items[selection]]
            self.mapwin.SetZoom(layer) 
                
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