#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=
# Blizz-ABS by Blizzard
# Version: 1.0.9.3
# Type: Advanced Action Battle System
# Date 1.0.0.0: 19.04.2007
# Date 1.0.0.1: 30.04.2007
# Date 1.0.0.2: 17.07.2007
# Date 1.0.0.4: 25.07.2007
# Date 1.0.0.9: 25.07.2007
# Date 1.0.3.0: 29.07.2007
# Date 1.0.3.3: 30.07.2007
# Date 1.0.3.4: 05.08.2007
# Date 1.0.9.0: 05.09.2007
# Date 1.0.9.1: 06.09.2007
# Date 1.0.9.2: 07.09.2007
# Date 1.0.9.3: 11.09.2007
#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=
# 
# Explanation:
# 
#   This script will allow you to create games with an Action Battle System
#   (ABS) (i.e. Zelda). Action Battle System means real time battle on the map.
# 
#   If you don't read the Manual, you will not be able to use many of the great
#   features this ABS supports.
# 
#   You didn't get a Manual with the Blizz-ABS? Please e-mail me, tell me where
#   you got this script from and I will give you a download link to the manual.
#   Here is my e-mail:
#   boris_blizzard@yahoo.de
# 
# 
# Compatibility:
# 
#   80% compatible with SDK 1.x. 40% compatible with SDK 2.x. Compatible with
#   any CMS. Mostly is not compatible with any battle add-ons for the normal
#   turn based battle system. WILL corrupt your old save games. Incompatible
#   with the RGSS100J.dll.
# 
# 
# IMPORTANT:
# 
#   Any CMS is being overriden, so put this script UNDER the CMS script if you
#   are using a CMS script (CMS = Custom Menu System). This script overrides
#   Tons of Add-ons and goes under it.
# 
# 
# Special Thanks for testing to:
# 
#   - Leonharts
#   - modern algebra
#   - NAMKCOR
#   - Rune
#   - Irockman1
#   - blazinhandling
#   - Zeph
# 
# 
# If you find any bugs, please report them here:
# http://www.chaosproject.co.nr
#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=

#==============================================================================
# BlizzABS
#------------------------------------------------------------------------------
#  This is the master control, configuration, utility and battle process
#  module for Blizz-ABS.
#==============================================================================

module BlizzABS
  
  #============================================================================
  # BlizzABS::Control
  #----------------------------------------------------------------------------
  #  This module provides in-game control configurations.
  #============================================================================
  
  module Control
    
    # using other controls instead of arrow keys
    CUSTOM_CONTROLS = false
    # RMXP default controls will be replaced completely with Blizz-ABS controls
    DISABLE_DEFAULT = true
    # you can skip this if you have set CUSTOM_CONTROLS to false
    # setup the controls as array, but with prefix and suffix "
    # i.e.: Let T and R be for cancel => CANCEL = "[Let['T'], Let['R']]"
    # for more info about read 1.1.1. of the manual
    UP       = "[Let['W']]" # move up
    LEFT     = "[Let['A']]" # move left
    DOWN     = "[Let['S']]" # move down
    RIGHT    = "[Let['D']]" # move right
    PREVPAGE = "[Let['Q']]" # previous page
    NEXTPAGE = "[Let['E']]" # next page
    CONFIRM  = "[Let['H']]" # confirm selections / pick up items
    CANCEL   = "[Let['F']]" # cancel selections
    ATTACK   = "[Let['K']]" # attacking
    DEFEND   = "[Let['L']]" # defending (hold)
    SKILL    = "[Let['J']]" # use skill
    ITEM     = "[Let['I']]" # use item
    SELECT   = "[Let['O']]" # change leader
    HUD      = "[Let['Z']]" # HUD on/off if enabled
    HOTKEY   = "[Let['X']]" # hotkey display on/off if enabled
    MINIMAP  = "[Let['C']]" # toggle minimap mode if enabled
    RUN      = "[Let['M']]" # running (hold)
    SNEAK    = "[Dot]"      # sneaking (hold)
    JUMP     = "[Comma]"    # jumping
    TURN     = "[Let['U']]" # turning around without moving (hold)
  end
  
  #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
  # BlizzABS::Config
  #----------------------------------------------------------------------------
  #  This module provides Blizz-ABS configurations.
  #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
  
  module Config
    
    # should party members follow the leader on the map
    CATERPILLAR = true
    # how many party member do you use
    MAX_PARTY = 1
    # include all actor IDs who are animated when standing
    ANIMATED_IDS = []
    # 0 -> 32 pixel tiles, 1 -> 16,  2 -> 8, 3 -> 4, 4 -> 2, 5 -> 1
    # careful anything higher than 1 will limit the max speed of char movement
    # 0 - max: 6, 1 - max: 6, 2 - max: 5, 3 - max: 4, 4 - max: 3, 5 - max: 2
    # I recommend using 2 if you have allies else you can use 3
    # note that this can also cause problems with running and sneaking
    PIXEL_MOVEMENT_RATE = 2
    # will make the force movement command ALWAYS work for 32 pixel tiles
    REPAIR_MOVEMENT = true
    # enable or disable moving in all 8 directions
    EIGHT_WAY_MOVEMENT = true
    # the normal moving speed (4 is default)
    NORMAL_SPEED = 4
    # the speed of running (set to 0 to disable)
    RUN_SPEED = 5
    # the speed of sneaking (set to 0 to disable)
    SNEAK_SPEED = 3
    # how many squares should the player jump (set to 0 to disable)
    JUMPING = 2
    # the terrain tag of tiles where the player can't jump over
    JUMP_TAG = 8
    # measured in map squares
    PERCEPTION_RANGE = 5
    # the terrain tag of "walls" (enemies can't see through walls, only hear)
    WALL_TAG = 8
    # turns HUD on or off
    HUD_ENABLED = true
    # 0, 1, or 2 (slightly different drawing method of the bars)
    HUD_TYPE = 0
    # 0 = upper left corner, 1 = upper right corner
    HUD_POSITION = 0
    # enables minimap
    MINIMAP = true
    # enables intelligent minimap to save map loading time
    INTELLIGENT_PASSABILTY = true
    # how much time will pass until an enemy respawns (0 for no respawn)
    RESPAWN_TIME = 0
    # the terrain tag of tiles where enemies can't respawn
    NO_ENEMY_TAG = 8
    # how many seconds will dropped stuff stay (0xFFFF for "infinite")
    ITEM_TIME = 60
    # sound played when picking up items ("NAME", VOLUME, PITCH)
    ITEM_PICKUP_SOUND_FILE = RPG::AudioFile.new('056-Right02', 80, 100)
    # makes enemies drop gold, specify an icon for display here
    DROP_GOLD = ''
    # map IDs where ABSEAL is disabled
    DISABLE_ANTI_LAG_IDS = []
    # strength of delag (1 is most powerful and not recommended)
    FACTOR = 2
    # stops update of events with no spriteset
    ABSEAL_AUTOKILL = true
    # restores the character's HP/SP/Status on Level Up
    HEAL_ON_LVLUP = true
    # displays LvUp on Level Up
    DISPLAY_LVLUP = true
    # animation ID of the animation shown when a player levels up
    LVLUP_ANIMATION_ID = 0
    # animation ID of the animation shown when an enemy is on the run
    FLEE_LOOP_ANIMATION_ID = 48
    # shows attack/skill/item animation
    ANIMATIONS = true
    # enables or disables the sprites during action of for actors
    ACTOR_ACTION_SPRITES = true
    # enables or disables the sprites during action of enemies
    ENEMY_ACTION_SPRITES = true
    # enables or disables the extra sprites for each weapon (actors only)
    WEAPON_SPRITES = true
    # enables or disables the sprites during running (player and allies)
    RUNNING_SPRITES = false
    # enables or disables the sprites during sneaking (player and allies)
    SNEAKING_SPRITES = false
    # enables or disables the sprites during sneaking (player and allies)
    JUMPING_SPRITES = false
    # small animations (set to true to size animations down to 50%)
    SMALL_ANIMATIONS = true
    # use also different tint colors for the pre-menu
    MENU_COLOR_TINT = 0
    # attack sprite (for actors), first row y offset if necessary
    ACTOR_SPRITE_Y_OFFSET = 112
    # attack sprite (for enemies), first row y offset if necessary
    ENEMY_SPRITE_Y_OFFSET = 0
    # 0 = never, 1 = no enemies, 2 = enemies dead, 3 = enemies within ABSEAL dead
    DISABLE_ABS_MODE = 1
    # [type, range], 0 = no data, 1 = in name, 2 = in description
    WEAPON_DATA_MODE = [2, 1]
    # [type, explode range, range] 0 = no data, 1 = in name, 2 = in description
    SKILL_DATA_MODE = [2, 2, 1]
    # [type, explode range, range] 0 = no data, 1 = in name, 2 = in description
    ITEM_DATA_MODE = [2, 2, 1]
  end
  
  #============================================================================
  # BlizzABS::Weapons
  #----------------------------------------------------------------------------
  #  This module provides weapon configurations.
  #============================================================================
  
  module Weapons
    
    #--------------------------------------------------------------------------
    # type
    #  id - weapon ID
    #  This method serves as database for weapon types.
    #  0 = sword / axe / claws / unarmed / etc. (damages in close front)
    #  1 = spear / lance (damages only in front)
    #  2 = flail (distant weapon, does not damage close enemies, front)
    #  3 = boomerang (returning projectile weapon, front)
    #  4 = bow and arrows / gun / shuriken (non-returning projectile, NO consumption)
    #  5 = bow and arrows / gun (non-returning projectile, consumes AMMUNITION)
    #  6 = shuriken (non-returning projectile, consumes ITSELF)
    #-------------------------------------------------------------------------- 
    def self.type(id)
      case id
      # START set up weapon types (when ID then return TYPE)
      when 1 then return 0 ## Rubber Sword
      when 2 then return 0 ## Leet Blade
      when 3 then return 3 ## Banana
      when 4 then return 5 ## Link's Bow
      when 5 then return 2 ## Rose Flail
      when 6 then return 6 ## Icicles
      # END
      end
      return 0
    end
    #--------------------------------------------------------------------------
    # range
    #  id - weapon ID
    #  This method serves as database for weapon ranges. All ranges are
    #  measured in map squares. Any decimal value WILL have its effect if
    #  pixel movement is being used.
    #-------------------------------------------------------------------------- 
    def self.range(id)
      case id
      # START set up weapon ranges (when ID then return RANGE)
      when 1 then return 1
      when 2 then return 1.2
      when 3 then return 4.5
      when 4 then return 5.7
      when 5 then return 4
      when 6 then return 5
      # END
      end
      return 1.0
    end
    #--------------------------------------------------------------------------
    # consume
    #  id - weapon ID
    #  Lets your weapons consume items to work. You must have the item assigned
    #  as your hot item for the weapon to work. One weapon can consumes
    #  different items. If you don't have any items left, the attack will fail.
    #  Allies' items for usage can be set up directly or over the AI menu.
    #-------------------------------------------------------------------------- 
    def self.consume(id)
      case id
      # START set up ammo consumption (when ID then return ID_ARRAY)
      when 4 then return [9, 10] ## can consume LOS Fork and/or Fire Arrows
      # END
      end
      return []
    end
  end
  
  #============================================================================
  # BlizzABS::Skills
  #----------------------------------------------------------------------------
  #  This module provides skill configurations.
  #============================================================================
  
  module Skills
    
    #--------------------------------------------------------------------------
    # type
    #  id - skill ID
    #  Lets you define how skills will be executed.
    #   0 = shooting skill (projectile skill, hits first target it encounters)
    #   1 = homing skill (projectile skill, finds a target you specify)
    #   2 = direct skill (hits the target instantly, you select the target)
    #   3 = beam skill (hits every target it goes through instantly)
    #  If a skill targets all enemies/allies, the skill will turn into:
    #   0 => thrusting skill (projectile skill, hits every target it goes through)
    #   1 => super homing skill (projectiles hit all targets in range)
    #   2 => shockwave skill (circular shockwave hits all targets in range)
    #   3 => fullscreen skill (targets all allies/enemies on the screen)
    #  Set the exploding range to 0 if you don't want anybody around to be
    #  affected by this skill. A skill explosion does not differ between ally
    #  and enemy. The animation ID can be skipped if no explosion range was
    #  defined.
    #-------------------------------------------------------------------------- 
    def self.type(id)
      case id
      # START set up skill types (when ID then return [TYPE, EXPLODING_RANGE, ANIMATION_ID])
      when 1 then return [2, 0]       ## Vitaly
      when 2 then return [0, 0]       ## Kugelblitz
      when 3 then return [0, 0]       ## Burner
      when 4 then return [1, 1.5, 24] ## Homing Fireball
      when 5 then return [2, 0]       ## Thor's Hammer
      when 6 then return [3, 0]       ## Holy Beam
      when 7 then return [0, 0]       ## Icicle
      when 8 then return [2, 0]       ## Raining Icicles
      when 9 then return [0, 0]       ## Stingshot
      when 10 then return [2, 0]      ## Evil Ghosts
      when 11 then return [3, 0]      ## Leet Skill
      # END
      end
      return [2, 0]
    end
    #--------------------------------------------------------------------------
    # range
    #  id - skill ID
    #  This method serves as database for skill ranges. All ranges are
    #  measured in map squares. Any decimal value WILL have its effect if
    #  pixel movement is being used. If the skill is a summon skill, this will
    #  define the time in seconds how long the summoned ally will prevail.
    #-------------------------------------------------------------------------- 
    def self.range(id)
      case id
      # START set up skill ranges (when ID then return RANGE)
      when 1 then return 2.5
      when 2 then return 5.5
      when 3 then return 6.5
      when 4 then return 5.5
      when 5 then return 6
      when 6 then return 4.5
      when 7 then return 6.5
      when 8 then return 2.5
      when 9 then return 2.5
      # END
      end
      return 1.0
    end
  end
  
  #============================================================================
  # BlizzABS::Items
  #----------------------------------------------------------------------------
  #  This module provides item configurations.
  #============================================================================
  
  module Items
    
    #--------------------------------------------------------------------------
    # type
    #  id - item ID
    #   0 = shooting item (projectile item, hits first target it encounters)
    #   1 = homing item (projectile item, finds a target you specify)
    #   2 = direct item (hits the target instantly, you select the target)
    #   3 = beam item (hits every target it goes through instantly)
    #  If a item targets all enemies/allies, the item will turn into:
    #   0 => thrusting item (projectile item, hits every target it goes through)
    #   1 => super homing item (projectiles hit all targets in range)
    #   2 => shockwave item (circular shockwave hits all targets in range)
    #   3 => fullscreen item (targets all allies/enemies on the screen)
    #  Set the exploding range to 0 if you don't want anybody around to be
    #  affected by this item. An item explosion does not differ between ally
    #  and enemy.
    #-------------------------------------------------------------------------- 
    def self.type(id)
      case id
      # START set up skill types (when ID then return [TYPE, EXPLODING_RANGE, ANIMATION_ID])
      when 1 then return [2, 0] ## actually all items are direct
      # END
      end
      return [2, 0]
    end
    #--------------------------------------------------------------------------
    # range
    #  id - item ID
    #  This method serves as database for item ranges. All ranges are
    #  measured in map squares. Any decimal value WILL have its effect if
    #  pixel movement is being used. If the item is a summon item, this will
    #  define the time in seconds how long the summoned ally will prevail.
    #-------------------------------------------------------------------------- 
    def self.range(id)
      case id
      # START set up item ranges (when ID then return RANGE)
      when 1 then return 5.5
      # END
      end
      return 5.5
    end
  end
  
  #============================================================================
  # BlizzABS::Enemies
  #----------------------------------------------------------------------------
  #  This module provides special enemy configurations.
  #============================================================================
  
  module Enemies
    
    #--------------------------------------------------------------------------
    # type
    #  id - enemy ID
    #  This method serves as database for enemy attack types.
    #  0 = damages in close front
    #  1 = damages only in front
    #  2 = distant weapon, does not damage close enemies, front
    #  3 = returning projectile weapon, front
    #  4 = projectile weapon
    #-------------------------------------------------------------------------- 
    def self.type(id)
      case id
      # START set up enemy attack types (when ID then return TYPE)
      when 1 then return 1  ## Zinger      - spear type
      when 2 then return 4  ## Cold Lunch  - shooter type
      when 5 then return 1  ## Batman      - spear type
      when 6 then return 3  ## Hot Lady    - boomerang type
      when 8 then return 1  ## Third Head  - spear type
      when 10 then return 1 ## Killerbunny - spear type
      when 11 then return 4 ## Lord Flamer - shooter type
      # END
      end
      return 0
    end
    #--------------------------------------------------------------------------
    # range
    #  id - enemy ID
    #  This method serves as database for enemy attack ranges. All ranges are
    #  measured in map squares. Any decimal value WILL have its effect if
    #  pixel movement is being used.
    #-------------------------------------------------------------------------- 
    def self.range(id)
      case id
      # START set up enemy attack ranges (when ID then return RANGE)
      when 2 then return 4.5
      when 6 then return 3.5
      when 8 then return 2.5
      when 9 then return 2.5
      when 11 then return 5.5
      # END
      end
      return 1.5
    end
    #--------------------------------------------------------------------------
    # enemy_set
    #  id - enemy ID
    #  Specify spritesets for enemy projectile attacks. Spritesets are
    #  auto-animated all the time.
    #-------------------------------------------------------------------------- 
    def self.enemy_set(id)
      case id
      # START set up enemy attack spritesets (when ID then return SPRITESET_NAME)
      when 2 then return 'icicle'       ## Cold Lunch shoots icicles
      when 6 then return 'flame'        ## Hot Lady throws a red boomerang
      when 11 then return 'fire burst'  ## Flamer throws those huge fireballs
      # END
      end
      return ''
    end
  end
  
  #============================================================================
  # BlizzABS::Cache
  #----------------------------------------------------------------------------
  #  This module holds a few bitmaps, so they don't need to be drawn each time
  #  which improves speed and reduces lag. It also holds damage sprites and
  #  Projectile Characters.
  #============================================================================
  
  module Cache
    
    #--------------------------------------------------------------------------
    # load
    #  Loads the cache images.
    #-------------------------------------------------------------------------- 
    def self.load
      # initialize
      @data = []
      # add image
      @data.push(self._green_arrow)
      # prevent "Script is hanging" error
      Graphics.update
      # add image
      @data.push(self._white_arrow)
      # prevent "Script is hanging" error
      Graphics.update
      # add image
      @data.push(self._arrow)
      # prevent "Script is hanging" error
      Graphics.update
      # add image
      @data.push(self._minimap_autotile)
      # prevent "Script is hanging" error
      Graphics.update
      # create damage sprite buffer and projectile buffer
      @damages, @projectiles = [], []
    end
    #--------------------------------------------------------------------------
    # damages
    #  Returns all currently displayed damage sprites.
    #--------------------------------------------------------------------------
    def self.damages
      return @damages
    end
    #--------------------------------------------------------------------------
    # projectiles
    #  Returns all currently active projectiles.
    #--------------------------------------------------------------------------
    def self.projectiles
      return @projectiles
    end
    #--------------------------------------------------------------------------
    # clean
    #  Cleans the cache from projectiles and damage sprites.
    #--------------------------------------------------------------------------
    def self.clean
      # disposes all damage sprites
      @damages.each {|ary| ary[0].dispose}
      # create new damage sprite buffer and new projectile buffer
      @damages, @projectiles = [], []
      # unfreeze all actor's actions
      BlizzABS.player.actors.each {|actor| actor.freeze_action = false}
    end
    #--------------------------------------------------------------------------
    # image
    #  index - index of the image in the cache
    #  Returns a copy of the image.
    #--------------------------------------------------------------------------
    def self.image(index)
      return @data[index].clone
    end
    #--------------------------------------------------------------------------
    # _green_arrow
    #  Creates the minimap icon for events.
    #--------------------------------------------------------------------------
    def self._green_arrow
      b = Bitmap.new(56, 14)
      c1 = Color.new(0, 0, 0)
      c2 = Color.new(255, 255, 255)
      c3 = Color.new(0, 255, 0)
      b.set_pixel(23, 0, c1)
      b.set_pixel(32, 0, c1)
      b.set_pixel(22, 1, c1)
      b.fill_rect(23, 1, 1, 12, c3)
      b.fill_rect(24, 1, 1, 12, c1)
      b.fill_rect(31, 1, 1, 12, c1)
      b.fill_rect(32, 1, 1, 12, c3)
      b.set_pixel(33, 1, c1)
      b.set_pixel(21, 2, c1)
      b.fill_rect(22, 2, 1, 10, c3)
      b.fill_rect(33, 2, 1, 10, c3)
      b.set_pixel(34, 2, c1)
      b.fill_rect(1, 3, 12, 1, c1)
      b.set_pixel(20, 3, c1)
      b.fill_rect(21, 3, 1, 8, c3)
      b.fill_rect(34, 3, 1, 8, c3)
      b.set_pixel(35, 3, c1)
      b.fill_rect(48, 3, 2, 1, c1)
      b.set_pixel(0, 4, c1)
      b.fill_rect(1, 4, 12, 1, c3)
      b.set_pixel(13, 4, c1)
      b.set_pixel(19, 4, c1)
      b.fill_rect(20, 4, 1, 6, c3)
      b.fill_rect(35, 4, 1, 6, c3)
      b.set_pixel(36, 4, c1)
      b.set_pixel(47, 4, c1)
      b.fill_rect(48, 4, 2, 6, c3)
      b.set_pixel(50, 4, c1)
      b.set_pixel(1, 5, c1)
      b.fill_rect(2, 5, 10, 1, c3)
      b.set_pixel(12, 5, c1)
      b.set_pixel(18, 5, c1)
      b.fill_rect(19, 5, 1, 4, c3)
      b.fill_rect(36, 5, 1, 4, c3)
      b.set_pixel(37, 5, c1)
      b.set_pixel(46, 5, c1)
      b.fill_rect(47, 5, 1, 5, c3)
      b.fill_rect(50, 5, 1, 5, c3)
      b.set_pixel(51, 5, c1)
      b.set_pixel(2, 6, c1)
      b.fill_rect(3, 6, 8, 1, c3)
      b.set_pixel(11, 6, c1)
      b.fill_rect(17, 6, 1, 2, c1)
      b.fill_rect(18, 6, 1, 2, c3)
      b.fill_rect(37, 6, 1, 2, c3)
      b.fill_rect(38, 6, 1, 2, c1)
      b.set_pixel(45, 6, c1)
      b.fill_rect(46, 6, 1, 4, c3)
      b.fill_rect(51, 6, 1, 4, c3)
      b.set_pixel(52, 6, c1)
      b.set_pixel(3, 7, c1)
      b.fill_rect(4, 7, 6, 1, c3)
      b.set_pixel(10, 7, c1)
      b.set_pixel(44, 7, c1)
      b.fill_rect(45, 7, 1, 3, c3)
      b.fill_rect(52, 7, 1, 3, c3)
      b.set_pixel(53, 7, c1)
      b.set_pixel(4, 8, c1)
      b.fill_rect(5, 8, 4, 1, c3)
      b.set_pixel(9, 8, c1)
      b.set_pixel(18, 8, c1)
      b.set_pixel(37, 8, c1)
      b.set_pixel(43, 8, c1)
      b.fill_rect(44, 8, 1, 2, c3)
      b.fill_rect(53, 8, 1, 2, c3)
      b.set_pixel(54, 8, c1)
      b.set_pixel(5, 9, c1)
      b.fill_rect(6, 9, 2, 1, c3)
      b.set_pixel(8, 9, c1)
      b.set_pixel(19, 9, c1)
      b.set_pixel(36, 9, c1)
      b.set_pixel(42, 9, c1)
      b.set_pixel(43, 9, c3)
      b.set_pixel(54, 9, c3)
      b.set_pixel(55, 9, c1)
      b.fill_rect(6, 10, 2, 1, c1)
      b.set_pixel(20, 10, c1)
      b.set_pixel(35, 10, c1)
      b.fill_rect(43, 10, 12, 1, c1)
      b.set_pixel(21, 11, c1)
      b.set_pixel(34, 11, c1)
      b.set_pixel(22, 12, c1)
      b.set_pixel(33, 12, c1)
      b.set_pixel(23, 13, c1)
      b.set_pixel(32, 13, c1)
      return b
    end
    #--------------------------------------------------------------------------
    # _white_arrow
    #  Creates the minimap icon for other events.
    #--------------------------------------------------------------------------
    def self._white_arrow
      b = Bitmap.new(56, 14)
      c1 = Color.new(0, 0, 0)
      c2 = Color.new(255, 255, 255)
      b.set_pixel(23, 0, c1)
      b.set_pixel(32, 0, c1)
      b.set_pixel(22, 1, c1)
      b.fill_rect(23, 1, 1, 12, c2)
      b.fill_rect(24, 1, 1, 12, c1)
      b.fill_rect(31, 1, 1, 12, c1)
      b.fill_rect(32, 1, 1, 12, c2)
      b.set_pixel(33, 1, c1)
      b.set_pixel(21, 2, c1)
      b.fill_rect(22, 2, 1, 10, c2)
      b.fill_rect(33, 2, 1, 10, c2)
      b.set_pixel(34, 2, c1)
      b.fill_rect(1, 3, 12, 1, c1)
      b.set_pixel(20, 3, c1)
      b.fill_rect(21, 3, 1, 8, c2)
      b.fill_rect(34, 3, 1, 8, c2)
      b.set_pixel(35, 3, c1)
      b.fill_rect(48, 3, 2, 1, c1)
      b.set_pixel(0, 4, c1)
      b.fill_rect(1, 4, 12, 1, c2)
      b.set_pixel(13, 4, c1)
      b.set_pixel(19, 4, c1)
      b.fill_rect(20, 4, 1, 6, c2)
      b.fill_rect(35, 4, 1, 6, c2)
      b.set_pixel(36, 4, c1)
      b.set_pixel(47, 4, c1)
      b.fill_rect(48, 4, 2, 6, c2)
      b.set_pixel(50, 4, c1)
      b.set_pixel(1, 5, c1)
      b.fill_rect(2, 5, 10, 1, c2)
      b.set_pixel(12, 5, c1)
      b.set_pixel(18, 5, c1)
      b.fill_rect(19, 5, 1, 4, c2)
      b.fill_rect(36, 5, 1, 4, c2)
      b.set_pixel(37, 5, c1)
      b.set_pixel(46, 5, c1)
      b.fill_rect(47, 5, 1, 5, c2)
      b.fill_rect(50, 5, 1, 5, c2)
      b.set_pixel(51, 5, c1)
      b.set_pixel(2, 6, c1)
      b.fill_rect(3, 6, 8, 1, c2)
      b.set_pixel(11, 6, c1)
      b.fill_rect(17, 6, 1, 2, c1)
      b.fill_rect(18, 6, 1, 2, c2)
      b.fill_rect(37, 6, 1, 2, c2)
      b.fill_rect(38, 6, 1, 2, c1)
      b.set_pixel(45, 6, c1)
      b.fill_rect(46, 6, 1, 4, c2)
      b.fill_rect(51, 6, 1, 4, c2)
      b.set_pixel(52, 6, c1)
      b.set_pixel(3, 7, c1)
      b.fill_rect(4, 7, 6, 1, c2)
      b.set_pixel(10, 7, c1)
      b.set_pixel(44, 7, c1)
      b.fill_rect(45, 7, 1, 3, c2)
      b.fill_rect(52, 7, 1, 3, c2)
      b.set_pixel(53, 7, c1)
      b.set_pixel(4, 8, c1)
      b.fill_rect(5, 8, 4, 1, c2)
      b.set_pixel(9, 8, c1)
      b.set_pixel(18, 8, c1)
      b.set_pixel(37, 8, c1)
      b.set_pixel(43, 8, c1)
      b.fill_rect(44, 8, 1, 2, c2)
      b.fill_rect(53, 8, 1, 2, c2)
      b.set_pixel(54, 8, c1)
      b.set_pixel(5, 9, c1)
      b.fill_rect(6, 9, 2, 1, c2)
      b.set_pixel(8, 9, c1)
      b.set_pixel(19, 9, c1)
      b.set_pixel(36, 9, c1)
      b.set_pixel(42, 9, c1)
      b.set_pixel(43, 9, c2)
      b.set_pixel(54, 9, c2)
      b.set_pixel(55, 9, c1)
      b.fill_rect(6, 10, 2, 1, c1)
      b.set_pixel(20, 10, c1)
      b.set_pixel(35, 10, c1)
      b.fill_rect(43, 10, 12, 1, c1)
      b.set_pixel(21, 11, c1)
      b.set_pixel(34, 11, c1)
      b.set_pixel(22, 12, c1)
      b.set_pixel(33, 12, c1)
      b.set_pixel(23, 13, c1)
      b.set_pixel(32, 13, c1)
      return b
    end
    #--------------------------------------------------------------------------
    # _arrow
    #  Creates the arrow displayed in the hotkey assignment menu.
    #--------------------------------------------------------------------------
    def self._arrow
      b = Bitmap.new(16, 9)
      c1 = Color.new(0, 0, 0)
      c2 = Color.new(255, 255, 255)
      c3 = Color.new(127, 127, 127)
      b.fill_rect(7, 0, 2, 1, c2)
      b.set_pixel(6, 1, c2)
      b.fill_rect(7, 1, 1, 7, c3)
      b.fill_rect(8, 1, 1, 7, c1)
      b.set_pixel(9, 1, c2)
      b.set_pixel(5, 2, c2)
      b.fill_rect(6, 2, 1, 6, c3)
      b.fill_rect(9, 2, 1, 6, c1)
      b.set_pixel(10, 2, c2)
      b.set_pixel(4, 3, c2)
      b.fill_rect(5, 3, 1, 5, c3)
      b.fill_rect(10, 3, 1, 5, c1)
      b.set_pixel(11, 3, c2)
      b.set_pixel(3, 4, c2)
      b.fill_rect(4, 4, 1, 4, c3)
      b.fill_rect(11, 4, 1, 4, c1)
      b.set_pixel(12, 4, c2)
      b.set_pixel(2, 5, c2)
      b.fill_rect(3, 5, 1, 3, c3)
      b.fill_rect(12, 5, 1, 3, c1)
      b.set_pixel(13, 5, c2)
      b.set_pixel(1, 6, c2)
      b.fill_rect(2, 6, 1, 2, c3)
      b.fill_rect(13, 6, 1, 2, c1)
      b.set_pixel(14, 6, c2)
      b.set_pixel(0, 7, c2)
      b.set_pixel(1, 7, c3)
      b.set_pixel(14, 7, c1)
      b.set_pixel(15, 7, c2)
      b.fill_rect(1, 8, 14, 1, c2)
      return b
    end
    #--------------------------------------------------------------------------
    # _minimap_autotile
    #  Creates the minimap autotile for passability.
    #--------------------------------------------------------------------------
    def self._minimap_autotile
      b = Bitmap.new(24, 32)
      c1 = Color.new(191, 191, 191)
      c2 = Color.new(255, 255, 255)
      b.fill_rect(2, 0, 4, 1, c2)
      b.set_pixel(1, 1, c2)
      b.fill_rect(2, 1, 4, 6, c1)
      b.set_pixel(6, 1, c2)
      b.fill_rect(0, 2, 1, 4, c2)
      b.fill_rect(1, 2, 1, 4, c1)
      b.fill_rect(6, 2, 1, 4, c1)
      b.fill_rect(7, 2, 1, 4, c2)
      b.set_pixel(1, 6, c2)
      b.set_pixel(6, 6, c2)
      b.fill_rect(2, 7, 4, 1, c2)
      b.fill_rect(7, 8, 10, 1, c2)
      b.set_pixel(6, 9, c2)
      b.fill_rect(7, 9, 10, 22, c1)
      b.set_pixel(17, 9, c2)
      b.set_pixel(5, 10, c2)
      b.fill_rect(6, 10, 1, 20, c1)
      b.fill_rect(17, 10, 1, 20, c1)
      b.set_pixel(18, 10, c2)
      b.set_pixel(4, 11, c2)
      b.fill_rect(5, 11, 1, 18, c1)
      b.fill_rect(18, 11, 1, 18, c1)
      b.set_pixel(19, 11, c2)
      b.set_pixel(3, 12, c2)
      b.fill_rect(4, 12, 1, 16, c1)
      b.fill_rect(19, 12, 1, 16, c1)
      b.set_pixel(20, 12, c2)
      b.set_pixel(2, 13, c2)
      b.fill_rect(3, 13, 1, 14, c1)
      b.fill_rect(20, 13, 1, 14, c1)
      b.set_pixel(21, 13, c2)
      b.set_pixel(1, 14, c2)
      b.fill_rect(2, 14, 1, 12, c1)
      b.fill_rect(21, 14, 1, 12, c1)
      b.set_pixel(22, 14, c2)
      b.fill_rect(0, 15, 1, 10, c2)
      b.fill_rect(1, 15, 1, 10, c1)
      b.fill_rect(22, 15, 1, 10, c1)
      b.fill_rect(23, 15, 1, 10, c2)
      b.set_pixel(1, 25, c2)
      b.set_pixel(22, 25, c2)
      b.set_pixel(2, 26, c2)
      b.set_pixel(21, 26, c2)
      b.set_pixel(3, 27, c2)
      b.set_pixel(20, 27, c2)
      b.set_pixel(4, 28, c2)
      b.set_pixel(19, 28, c2)
      b.set_pixel(5, 29, c2)
      b.set_pixel(18, 29, c2)
      b.set_pixel(6, 30, c2)
      b.set_pixel(17, 30, c2)
      b.fill_rect(7, 31, 10, 1, c2)
      return b
    end
  end
  
  #============================================================================
  # Player_Controller
  #----------------------------------------------------------------------------
  #  This class is a special controller that controls the party leader.
  #============================================================================
  
  class Player_Controller
    
    # Center screen x-coordinate * 4
    CX = (320 - 16) * 4
    # Center screen y-coordinate * 4
    CY = (240 - 16) * 4
    
    # set all accessable variables
    attr_accessor :normal_speed
    attr_accessor :actors
    #--------------------------------------------------------------------------
    # Initialization
    #--------------------------------------------------------------------------
    def initialize
      # set event trigger escape counter
      @evented = 0
      # set actor characters
      @actors = []
      # set memory jump
      @memory_jump = false
      # set normal speed
      @normal_speed = BlizzABS::Config::NORMAL_SPEED
    end
    #--------------------------------------------------------------------------
    # player
    #  This method is used to make the code easier to read.
    #--------------------------------------------------------------------------
    def player
      return @actors[0]
    end
    #--------------------------------------------------------------------------
    # update_control
    #  Processes player control.
    #--------------------------------------------------------------------------
    def update_control
      # get pixel movement rate
      pix = BlizzABS.pixel
      # reset move speed
      player.move_speed = @normal_speed
      # reset spriteset name
      player.character_name = player.character_name_org
      # if allowed to change speed
      unless $game_system.map_interpreter.running? ||
          player.move_route_forcing || $game_temp.message_window_showing
        # if run button works and running
        if Input.press?(Input::Run) && BlizzABS::Config::RUN_SPEED != 0
          # set running speed
          player.move_speed = BlizzABS::Config::RUN_SPEED
        # if sneak button works and sneaking
        elsif Input.press?(Input::Sneak) && BlizzABS::Config::SNEAK_SPEED != 0
          # set sneaking speed
          player.move_speed = BlizzABS::Config::SNEAK_SPEED
        end
      end
      # if battler exists and either dead or select triggered
      if player.battler != nil && (Input.trigger?(Input::Select) ||
          player.battler.dead?)
        # iterate "number of party members" times
        $game_party.actors.size.times {
            # change party leader
            $game_party.add_actor($game_party.actors.shift.id)
            # until finding one who's not dead
            break if $game_party.actors[0] != nil && !$game_party.actors[0].dead?}
        # center screen display on new player controlled character
        center(player.x, player.y, true)
        # enforce emptying moving buffer and add special command
        update_buffer(false)
      end 
      # update spriteset animation
      player.sprite_update
      # decrease event trigger escape counter if no interpreter running
      @evented -= 1 if @evented > 0 && !$game_system.map_interpreter.running?
      # if allowed to turn and pressed turning button or defending
      if ((player.defending && player.attacked == 0 &&
            player.in_action == 0) || Input.press?(Input::Turn)) &&
            !player.moving? && !$game_system.map_interpreter.running? &&
            !player.move_route_forcing && !$game_temp.message_window_showing
        # straighten
        player.straighten
        # depending on input turn
        case Input.dir4
        when 2 then player.turn_down
        when 4 then player.turn_left
        when 6 then player.turn_right
        when 8 then player.turn_up
        end
        # updates any attack action
        player.update_attacked
        # abort method
        return nil
      end
      # updates any attack action
      player.update_attacked
      # if acting
      if player.in_action > 0
        # decrease action counter if in_action is greater than 0
        player.in_action -= 1 if player.in_action > 0
        # return data
        return [player.moving?, player.real_x, player.real_y]
      end
      # if allowed to move
      unless $game_system.map_interpreter.running? ||
          player.move_route_forcing || $game_temp.message_window_showing
        # if jump button was pressed and not already jumping
        @memory_jump = true if Input.trigger?(Input::Jump) && !player.jumping?
        # if not moving
        unless player.moving?
          # get jumping range
          range = BlizzABS::Config::JUMPING
          # if jumping turned on and not jumping and jumped
          if range > 0 && !player.jumping? && @memory_jump
            # if sneaking or running is possible
            if BlizzABS::Config::RUN_SPEED > 0 || BlizzABS::Config::SNEAK_SPEED > 0
              # get difference between current speed and normal speed
              dplus = player.move_speed - @normal_speed
            else
              # difference is 0
              dplus = 0
            end
            # check input
            direction = ($game_system._8_way ? Input.dir8 : Input.dir4)
            # set jumping direction
            case direction
            when 1 then x, y = -1, 1
            when 2 then x, y = 0, 1
            when 3 then x, y = 1, 1
            when 4 then x, y = -1, 0
            when 6 then x, y = 1, 0
            when 7 then x, y = -1, -1
            when 8 then x, y = 0, -1
            when 9 then x, y = 1, -1
            else
              x, y = 0, 0
            end
            # jump into direction with considering running/sneaking
            player.jump(x*range + x*dplus, y*range + y*dplus, direction)
          elsif !player.jumping?
            # check input and attempt to move
            case ($game_system._8_way ? Input.dir8 : Input.dir4)
            when 1 then move(4) if !move(1) && !move(2)
            when 2 then move(2)
            when 3 then move(6) if !move(3) && !move(2)
            when 4 then move(4)
            when 6 then move(6)
            when 7 then move(4) if !move(7) && !move(8)
            when 8 then move(8)
            when 9 then move(6) if !move(9) && !move(8)
            end
          end
          # not jumping anymore
          @memory_jump = false
        end
      end
      # return data
      return [player.moving?, player.real_x, player.real_y]
    end
    #--------------------------------------------------------------------------
    # move
    #  dir - direction
    #  This method is used to make the code easier to read. It moves the player
    #--------------------------------------------------------------------------
    def move(dir)
      return case dir
      when 1 then player.move_lower_left
      when 2 then player.move_down
      when 3 then player.move_lower_right
      when 4 then player.move_left
      when 6 then player.move_right
      when 7 then player.move_upper_left
      when 8 then player.move_up
      when 9 then player.move_upper_right
      end
    end
    #--------------------------------------------------------------------------
    # update_move
    #  Processes player control.
    #--------------------------------------------------------------------------
    def update_move(data)
      # if control update was not aborted
      if data != nil
        # if moved down
        if player.real_y > data[2] && player.real_y - $game_map.display_y > CY
          # scroll screen down
          $game_map.scroll_down(player.real_y - data[2])
        end
        # if moved left
        if player.real_x < data[1] && player.real_x - $game_map.display_x < CX
          # scroll screen left
          $game_map.scroll_left(data[1] - player.real_x)
        end
        # if moved right
        if player.real_x > data[1] && player.real_x - $game_map.display_x > CX
          # scroll screen right
          $game_map.scroll_right(player.real_x - data[1])
        end
        # if moved up
        if player.real_y < data[2] && player.real_y - $game_map.display_y < CY
          # scroll screen up
          $game_map.scroll_up(data[2] - player.real_y)
        end
        # if not moving
        unless player.moving?
          # if was moving before and event escape expired and event not triggered
          if data[0] && @evented == 0 && check_event_trigger_here([1, 2])
            # set event trigger escape counter to one second
            @evented = 40
          end
          # if pressed C button
          if Input.trigger?(Input::C)
            # check event here
            check_event_trigger_here([0])
            # check event there
            check_event_trigger_there([0, 1, 2])
          end
        end
      end
      # update actors' characters
      update_actors
      # update ABS controls
      $game_system.controls.update
    end
    #--------------------------------------------------------------------------
    # update_buffer
    #  move - new command
    #  Updates the buffer of the last moving commands.
    #--------------------------------------------------------------------------
    def update_buffer(move)
      # empty each actor's buffer if new command requires so
      @actors.each {|actor| actor.buffer = []} if [nil, false].include?(move)
      # add new command or enforce emptying whether move is reset for each actor
      @actors.each {|actor| actor.update_buffer(move == 'reset' ? nil : move)}
    end
    #--------------------------------------------------------------------------
    # update_actors
    #  Updates all the actors on the map.
    #--------------------------------------------------------------------------
    def update_actors
      # update each other actor except the player
      @actors[1, @actors.size-1].each {|actor| actor.update}
      # set stopped animation flag if player's character is animated
      @step_anime = true if BlizzABS::Config::ANIMATED_IDS.include?(player.battler.id)
    end
    #--------------------------------------------------------------------------
    # refresh
    #  Refreshes the character.
    #--------------------------------------------------------------------------
    def refresh
      # test on changes in the inner structure of $game_party.actors
      if @actors.any? {|actor|
          actor.battler == nil && $game_party.actors[actor.index] != nil ||
          actor.battler != $game_party.actors[actor.index]}
        # store old array
        old = @actors
        # create new array
        @actors = []
        # add all characters with battlers
        old.each {|a| @actors[a.battler.index] = a unless a.battler == nil}
        # add all characters without battlers
        old.each {|a| @actors.push(a) if a.battler == nil}
        #  for each actor
        @actors.each {|a|
            # if no battler assigned, but in the party is a battler
            if a.battler == nil && $game_party.actors[a.index] != nil
              # assign battler
              a.battler = $game_party.actors[a.index]
            end}
      end
      # refresh each actor's character
      @actors.each {|actor| actor.refresh(true)}
      # set new $game_player character
      $game_player = player
    end
    #--------------------------------------------------------------------------
    # moveto
    #  x - x-coordinate
    #  y - y-coordinate
    #  Moves the player instantly to a postion, moves all actors and centers
    #  the screen upon the player.
    #--------------------------------------------------------------------------
    def moveto(x, y)
      # center screen upon player
      center(x, y)
      # empty movement command buffer
      update_buffer(nil)
      # move each actor to the same position
      (@actors - [player]).each {|actor| actor.moveto(x, y)}
    end
    #--------------------------------------------------------------------------
    # center
    #  x - x-coordinate
    #  y - y-coordinate
    #  Centers the screen upon the player. (pixel movement)
    #--------------------------------------------------------------------------
    def center(x, y, flag = false)
      # if flag or game was loaded
      if flag
        # resize coordinates
        x, y = x * 128 / BlizzABS.pixel, y * 128 / BlizzABS.pixel
      else
        # resize coordinates
        x, y = x * 128, y * 128
      end
      # get maximum coordinates of map
      max_x = ($game_map.width - 20) * 128
      max_y = ($game_map.height - 15) * 128
      # set new display coordinates
      $game_map.display_x = [0, [x - CX, max_x].min].max
      $game_map.display_y = [0, [y - CY, max_y].min].max
    end
    #--------------------------------------------------------------------------
    # check_event_trigger_here
    #  triggers - possible event triggers
    #  Checks if there are events to be triggered. (pixel movement)
    #--------------------------------------------------------------------------
    def check_event_trigger_here(triggers)
      # not started if already running
      return false if $game_system.map_interpreter.running?
      # get pixel movement rate
      pix = BlizzABS.pixel
      # initialize result
      result = false
      # iterate through all events
      $game_map.enemies(true).each {|event|
          # if coordinates fit and can be triggered and not jumping
          if event.x == (player.x+pix/2)/pix &&
             event.y == (player.y+pix/2)/pix &&
              triggers.include?(event.trigger) && !event.jumping? &&
              event.over_trigger?
            # start event
            event.start
            # events were started
            result = true
          end}
      # return result
      return result
    end
    #--------------------------------------------------------------------------
    # check_event_trigger_there
    #  triggers - possible event triggers
    #  Checks if there are events to be triggered. (pixel movement)
    #--------------------------------------------------------------------------
    def check_event_trigger_there(triggers)
      # not started if already running
      return false if $game_system.map_interpreter.running?
      # get pixel movement rate
      pix = BlizzABS.pixel
      # calculate new coordinates
      nx = player.x + (player.direction == 6 ? 1 : player.direction == 4 ? -1 : 0)*pix
      ny = player.y + (player.direction == 2 ? 1 : player.direction == 8 ? -1 : 0)*pix
      # initialize result
      result = false
      # iterate through all events
      $game_map.enemies(true).each {|event|
          # if coordinates fit and can be triggered and not jumping
          if event.x >= nx/pix && event.x <= (nx+pix-1)/pix &&
              event.y >= ny/pix && event.y <= (ny+pix-1)/pix &&
              triggers.include?(event.trigger) && !event.jumping? &&
              !event.over_trigger?
            # start event
            event.start
            # events were started
            result = true
          end}
      # if event was not started and counter
      if !result && $game_map.pixel_counter?(nx, ny)
        # change new coordinates
        nx += (direction == 6 ? 1 : direction == 4 ? -1 : 0)*pix
        ny += (direction == 2 ? 1 : direction == 8 ? -1 : 0)*pix
        # iterate through all events
        $game_map.enemies(true).each {|event|
            # if coordinates fit and can be triggered and not jumping
            if event.x >= nx/pix && event.x <= (nx+pix-1)/pix &&
                event.y >= ny/pix && event.y <= (ny+pix-1)/pix &&
                triggers.include?(event.trigger) && !event.jumping? &&
                !event.over_trigger?
              # start event
              event.start
              # events were started
              result = true
            end}
      end
      # return result
      return result
    end
    #--------------------------------------------------------------------------
    # check_event_trigger_touch
    #  x - x-coordinate
    #  y - y-coordinate
    #  Checks if there are events that were triggered by touch. (pixel movement)
    #--------------------------------------------------------------------------
    def check_event_trigger_touch(x, y)
      # not started if already running
      return false if $game_system.map_interpreter.running?
      # get pixel movement rate
      pix = BlizzABS.pixel
      # initialize result
      result = false
      # iterate through all events
      $game_map.enemies(true).each {|event|
          # if coordinates fit and can be triggered and not jumping
          if event.x >= x/pix && event.x <= (x+pix-1)/pix &&
              event.y >= y/pix && event.y <= (y+pix-1)/pix &&
              [1, 2].include?(event.trigger) && !event.jumping? &&
              !event.over_trigger?
            # start event
            event.start
            # events were started
            result = true
          end}
      # return result
      return result
    end
    
  end
  
  # version of Blizz-ABS
  VERSION = 1.093
  # edition of Blizz-ABS
  EDITION = 'Normal'
  # load player controller
  @player = BlizzABS::Player_Controller.new
  # create Blizz-ABS Cache
  BlizzABS::Cache.load
  # ensures compatibility with plugins (aka test if Blizz-ABS is there)
  $BlizzABS = true
  
  #--------------------------------------------------------------------------
  # player
  #  Returns the player controller instance.
  #-------------------------------------------------------------------------- 
  def self.player
    return @player
  end
  #--------------------------------------------------------------------------
  # pixel
  #  Safe method to retreive the pixel movement rate.
  #-------------------------------------------------------------------------- 
  def self.pixel
    return $game_system == nil ? 1 : 2 ** $game_system.pixel_rate
  end
  #--------------------------------------------------------------------------
  # animations_size_down
  #  Sizes down all the animations to 50%.
  #-------------------------------------------------------------------------- 
  def self.animations_size_down
    # iterate through all animations
    $data_animations[1, $data_animations.size-1].each {|animation|
      # iterate through all frames
      animation.frames.each {|frame|
        # iterate through all cells
        (0...frame.cell_data.xsize).each {|i|
            # if cell contains image
            if frame.cell_data[i, 0] != nil && frame.cell_data[i, 0] != -1
              # size down x position, y position and zoom by half
              (1..3).each {|j| frame.cell_data[i, j] /= 2}
            end}}}
  end
  #--------------------------------------------------------------------------
  # setup_minimap
  #  map - database map
  #  Returns a data hash with coordinates for the minimap drawing.
  #-------------------------------------------------------------------------- 
  def self.setup_passability(map)
    # set map for further use
    @map = map
    # initialize
    result = Table.new(@map.width, @map.height)
    # iterate through each element in the given in each horizontal lines
    (0...@map.height).each {|y| (0...@map.width).each {|x|
        # initialize value
        val = 0x00
        # add to value if virtually passable in each direction
        val |= 0x01 if self.passable?(x, y, 2) && self.passable?(x, y+1, 8)
        val |= 0x02 if self.passable?(x, y, 4) && self.passable?(x-1, y, 6)
        val |= 0x04 if self.passable?(x, y, 6) && self.passable?(x+1, y, 4)
        val |= 0x08 if self.passable?(x, y, 8) && self.passable?(x, y-1, 2)
        # add coordinate if passable anyhow
        result[x, y] = val if val != 0x00}}
    # remove map from memory
    @map = nil
    # return passable coordinates
    return result
  end
  #----------------------------------------------------------------------------
  # passable?
  #  x - x-coordinate
  #  y - y-coordinate
  #  d - direction
  #  Checks virtual passability for the minimap.
  #----------------------------------------------------------------------------
  def self.passable?(x, y, d)
    # "passable" if out of map border
    return true if x < 0 || x >= @map.width || y < 0 || y >= @map.height
    # set bit
    bit = (1 << (d / 2 - 1)) & 0x0f
    # iterate through all layers
    for i in [2, 1, 0]
      # get tile ID
      tile_id = @map.data[x, y, i]
      # if tile ID not valid
      if tile_id == nil
        # impassable
        return false
      # if obstacle bit is set
      elsif $data_tilesets[@map.tileset_id].passages[tile_id] & bit != 0
        # impassable
        return false
      # if obstacle bit is set in all directions
      elsif $data_tilesets[@map.tileset_id].passages[tile_id] & 0x0F == 0x0F
        # impassable
        return false
      # if priority is 0
      elsif $data_tilesets[@map.tileset_id].priorities[tile_id] == 0
        # passable
        return true
      end
    end
    # passable
    return true
  end
  #----------------------------------------------------------------------------
  # init_caterpillar
  #  This method serves for initialization of the caterpillar.
  #----------------------------------------------------------------------------
  def self.init_caterpillar
    # add player controlled character
    @player.actors = [$game_player]
    # if CATERPILLAR is active
    if Config::CATERPILLAR
      # MAX-PARTY size - 1 times create actor
      (1...Config::MAX_PARTY).each {|i| @player.actors.push(Map_Actor.new(i))}
    end
    # refresh the player's battler
    $game_player.battler = $game_party.actors[0]
    # if not very beginning of the game
    if $game_map.map_id != nil && $game_map.map_id > 0
      # move all actors to the player's position
      $game_player.moveto($game_player.x/BlizzABS.pixel, $game_player.y/BlizzABS.pixel)
    end
  end
  #----------------------------------------------------------------------------
  # attack_process
  #  ch - the character in action
  #  Processes ABS attack setup and handling for actors and enemies.
  #----------------------------------------------------------------------------
  def self.attack_process(ch)
    # determine whether actor or enemy for easier reference
    classe = (ch.is_a?(Map_Actor) ? Map_Enemy : Map_Actor)
    # get and correct attack range
    d = [(classe == Map_Enemy ? Weapons.range(ch.battler.weapon_id) :
        Enemies.range(ch.battler.id)), 1].max
    # temporary variable depending on whether actor or enemy
    type = (classe == Map_Enemy ? Weapons.type(ch.battler.weapon_id) :
        Enemies.type(ch.battler.id))
    # create affection area depending on attack type
    case type
    # sword attack
    when 0
      range = [ch.real_x + 64, ch.real_y + 64, d*128, ch.direction]
    # lance attack
    when 1
      # create affection area rectangle
      range = case ch.direction
      when 2 then Rect.new(ch.real_x, ch.real_y+64, 128, d*128)
      when 4 then Rect.new(ch.real_x+64-d*128, ch.real_y, d*128, 128)
      when 6 then Rect.new(ch.real_x+64, ch.real_y, d*128, 128)
      when 8 then Rect.new(ch.real_x, ch.real_y+64-d*128, 128, d*128)
      end
    # flail attack
    when 2
      # create affection area rectangle
      range = case ch.direction
      when 2 then Rect.new(ch.real_x, ch.real_y+64+d*64, 128, d*64)
      when 4 then Rect.new(ch.real_x+64-d*128, ch.real_y, d*64, 128)
      when 6 then Rect.new(ch.real_x+64+d*64, ch.real_y, d*64, 128)
      when 8 then Rect.new(ch.real_x, ch.real_y+64-d*128, 128, d*64)
      end
    # returning projectile attack
    when 3
      # if attacker is actor
      if classe == Map_Enemy
        # create returning projectile based on actor's weapon ID
        proj = Projectile.new($data_weapons[ch.battler.weapon_id].icon_name, ch,
            0, d, 0, classe, true)
      else
        # create returning projectile based on enemy's ID
        proj = Projectile.new(Enemies.enemy_set(ch.battler.id), ch, 0, d, 0,
            classe, true)
      end
    # projectile attack
    when 4
      # if attacker is actor
      if classe == Map_Enemy
        # create projectile based on actor's weapon ID
        proj = Projectile.new($data_weapons[ch.battler.weapon_id].icon_name, ch,
            0, d, 2, classe, true)
      else
        # create projectile based on enemy's ID
        proj = Projectile.new(Enemies.enemy_set(ch.battler.id), ch, 0, d, 2,
            classe, true)
      end
    # item consuming projectile
    when 5
      # temporary variable
      ids = Weapons.consume(ch.battler.weapon_id)
      # if currently equipped item can be consumed and item in inventory
      if ids.include?(ch.battler.item) &&
          $game_party.item_number(ch.battler.item) > 0
        # remove one item from inventory
        $game_party.lose_item(ch.battler.item, 1)
        # temporary variable
        item = $data_items[ch.battler.item]
        # create projectile from item with weapon attack effect
        proj = Projectile.new(item.icon_name, ch, item.id, d, 3, classe, true)
      else
        # ignore attack
        return false
      end
    # self consuming weapon
    when 6
      # temporary variable
      weapon = $data_weapons[ch.battler.weapon_id]
      # unequip last weapon if no more weapons in inventory
      ch.battler.equip(0, 0) if $game_party.weapon_number(weapon.id) == 0
      # remove one weapon from inventory
      $game_party.lose_weapon(weapon.id, 1)
      # self shooting weapon, create projectile from weapon
      proj = Projectile.new(weapon.icon_name, ch, weapon.id, d, 4, classe, true)
    end
    # if projectile fired
    if proj != nil
      # add projectile to buffer
      BlizzABS::Cache.projectiles.push(proj)
      # no enemies were directly attacked
      return false
    end
    # iterate through all battlers
    ($game_map.enemies + BlizzABS.player.actors).each {|battler|
        # if target can be hit considering all conditions
        if battler.is_a?(classe) && battler.battler != nil &&
            !battler.battler.dead? && self.intersection(range,
            Rect.new(battler.real_x, battler.real_y, 128, 128))
          # execute attack
          battler.attack_effect(ch, ch.battler)
        end}
    # enemies were attacked
    return true
  end
  #----------------------------------------------------------------------------
  # skillitem_process
  #  ch - the skill/item using character
  #  object - the skill or item that is being used
  #  Processes skill and item use in Blizz-ABS on the map. One method is used
  #  for both since the process is almost identical for both objects.
  #----------------------------------------------------------------------------
  def self.skillitem_process(ch, object)
    # determine whether skill or item for easier reference
    skill = (object.is_a?(RPG::Skill))
    # get and correct range
    d = [(skill ? Skills.range(object.id) : Items.range(object.id)), 1].max
    # determine skill/item type
    type = (skill ? Skills.type(object.id) : Items.type(object.id))
    # skill/item used (can happen to be a common event call) if no target scope
    return true if object.scope == 0
    # not used if summoning skill/item (this type is N/A in 1.0.9.x)
    return false if type[0] == 4
    # if targeting self
    if object.scope == 7
      # if skill
      if skill
        # execute skill upon user
        ch.skill_effect(ch, ch.battler, object)
      else
        # execute item upon user
        ch.item_effect(ch, ch.battler, object)
      end
      # skill/item used
      return true
    end
    # check scope and determine target class, ndead flag and all flag
    case object.scope
    when 1
      classe, ndead = (ch.is_a?(Map_Enemy) ? Map_Actor : Map_Enemy), true
      all = false
    when 2
      classe, ndead = (ch.is_a?(Map_Enemy) ? Map_Actor : Map_Enemy), true
      all = true
    when 3 then classe, ndead, all = ch.class, true, false
    when 4 then classe, ndead, all = ch.class, true, true
    when 5 then classe, ndead, all = ch.class, false, false
    when 6 then classe, ndead, all = ch.class, false, true
    end
    # selection only if player using selectable skill/item
    if ch == $game_player && ([1, 2].include?(type[0]) || type[0] == 3 &&
        [2, 4, 6].include?(object.scope))
      # temporary variable, selection skill/item
      handling = 0
    else
      # temporary variable, projectile skill/item or direct skill/item
      handling = (type[0] < 2 ? 1 : 2)
    end
    # execute preparations for skill/item use depending on handling
    case handling
    # selection
    when 0
      # create circle shape data
      range = [ch.real_x+64, ch.real_y+64, d*128, 0]
      # create fullscreen rectangle
      screen = Rect.new($game_map.display_x, $game_map.display_y, 2560, 1920)
      # initialize array for targets, available for selection
      available = []
      # iterate through all character sprites
      $scene.spriteset.character_sprites.each {|sprite|
          # temporary variable
          battler = sprite.character
          # if target can be hit
          if battler.is_a?(classe) && battler.battler != nil &&
              ndead ^ battler.battler.dead? && self.intersection(screen,
              Rect.new(battler.real_x+60, battler.real_y+60, 8, 8)) &&
              (type[0] == 3 && all || self.intersection(range,
              Rect.new(battler.real_x, battler.real_y, 128, 128)))
            # add sprite to selectable
            available.push(sprite)
          end}
      # no use if no selectable targets
      return false if available.size == 0
      # sort selectable targets by coordinates
      available.sort {|a, b| b.y > a.y ? 1 : b.y < a.y ? -1 : (b.x <=> a.x)}
      # setup select interuption
      $game_temp.select_data = [ch, object, available]
      # don't use skill/item yet
      return false
    # projectile
    when 1
      # decide process branch depending on skill type
      case type[0]
      # set normal or break-through projectile data
      when 0
        projectype, targets = (all ? (skill ? 6 : 10) : (skill ? 5 : 9)), [d]
      # direct skill/item
      when 1
        # create circle shape data
        range = [ch.real_x+64, ch.real_y+64, d*128, 0]
        # initialize targets
        targets = []
        # create fullscreen rectangle
        screen = Rect.new($game_map.display_x, $game_map.display_y, 2560, 1920)
        # iterate through all battlers
        ($game_map.enemies + BlizzABS.player.actors).each {|battler|
            # if target can be hit
            if battler.is_a?(classe) && battler.battler != nil &&
                ndead ^ battler.battler.dead? && self.intersection(screen,
                Rect.new(battler.real_x+60, battler.real_y+60, 8, 8)) &&
                self.intersection(range,
                Rect.new(battler.real_x, battler.real_y, 128, 128))
              # add to targets
              targets.push(battler)
            end}
        # set homing projectile type
        projectype = (skill ? 7 : 11)
      end
    # direct
    when 2
      # if direct skill or shockwave skill
      if type[0] == 2
        # create circle shape data
        range = [ch.real_x+64, ch.real_y+64, d*128, 0]
      # if beam skill
      elsif !all
        # determine affection area depending on facing direction for beam
        range = case ch.direction
        when 2 then Rect.new(ch.real_x, ch.real_y+64, 128, d*128)
        when 4 then Rect.new(ch.real_x+64-d*128, ch.real_y, d*128, 128)
        when 6 then Rect.new(ch.real_x+64, ch.real_y, d*128, 128)
        when 8 then Rect.new(ch.real_x, ch.real_y+64-d*128, 128, d*128)
        end
      end
      # create fullscreen rectangle
      screen = Rect.new($game_map.display_x, $game_map.display_y, 2560, 1920)
      # initialize targets
      targets = []
      # iterate through all battlers
      ($game_map.enemies + BlizzABS.player.actors).each {|battler|
          # if target can be hit
          if battler.is_a?(classe) && battler.battler != nil &&
              ndead ^ battler.battler.dead? && self.intersection(screen,
              Rect.new(battler.real_x+60, battler.real_y+60, 8, 8)) &&
              (type[0] == 3 && all || self.intersection(range,
              Rect.new(battler.real_x, battler.real_y, 128, 128)))
            # add to targets
            targets.push(battler)
          end}
    end
    # no use if no selectable targets
    return false if targets.size == 0
    # get a random target from all targets if not targeting all
    targets = [targets[rand(targets.size)]] unless all
    # if projectile data is available and projectile should be created
    if projectype != nil
      # iterate through all targets
      targets.each {|target|
          # create exploding projectile with provided data
          if type[1] > 0
            proj = Projectile.new(object.icon_name, ch, object.id, target,
                projectype, classe, ndead, type[1, 2])
          # create projectile with provided data
          else
            proj = Projectile.new(object.icon_name, ch, object.id, target,
                projectype, classe, ndead)
          end
          # add projectile to buffer
          BlizzABS::Cache.projectiles.push(proj)}
    # if skill
    elsif skill
      # execute skill effect upon all targets
      targets.each {|target| target.skill_effect(ch, ch.battler, object)}
    else
      # execute item effect upon all targets
      targets.each {|target| target.item_effect(ch, ch.battler, object)}
    end
    # skill/item use successful
    return true
  end
  #----------------------------------------------------------------------------
  # selectable
  #  battler - the map battler to be tested
  #  ndead   - ndead flag
  #  range   - range definition
  #  Serves the simplification of the code because of encapsulation of repeated
  #  condition checking.
  #----------------------------------------------------------------------------
  def self.selectable(battler, ndead, range, type)
    return ()
  end
  #----------------------------------------------------------------------------
  # intersection
  #  shape - either rectangle or a data array with circle data
  #  rect  - rectangle
  #  This method processes and test intersection of rectangles, a rectangle
  #  with a full circle and a rectangle with a fourth of a circle in which the
  #  user of an attack/skill/item is facing. The shapes get tested on whether
  #  at least one point of the rectangle is within the shape and if not, then
  #  this method checks whether the shape's characteristic lines determined by
  #  the center points and a few point on the borders intersect with the
  #  rectangle. This polygon intersection determination is a simplified
  #  version, sufficient for Blizz-ABS that needs less CPU time than a full
  #  determination algorithm.
  #----------------------------------------------------------------------------
  def self.intersection(shape, rect)
    # if both are rectangles return rectangle intersection result
    return self.rect_intersection(shape, rect) if shape.is_a?(Rect)
    # temporary variables
    x, y, r, d = shape
    # iterate through all of rectangle's points
    [rect.x, rect.x+rect.width-1].each {|i| [rect.y, rect.y+rect.height-1].each {|j|
        # if within special circle radius
        if Math.hypot(x-i, y-j) < r || Math.hypot(x-i-1, y-j) < r ||
            Math.hypot(x-i, y-j-1) < r || Math.hypot(x-i-1, y-j-1) < r
          case d
          when 2 then return true if j-y >= 0 && i-x <= j-y && x-i-1 <= j-y
          when 4 then return true if x-i-1 >= 0 && j-y <= x-i-1 && y-j-1 <= x-i-1
          when 6 then return true if i-x >= 0 && j-y <= i-x && y-j-1 <= i-x
          when 8 then return true if y-j-1 >= 0 && i-x <= y-j-1 && x-i-1 <= y-j-1
          else
            # full circle, intersection exists
            return true
          end
        end}}
    # initialize arrays
    rects, coos = [], []
    # radius line end coordinates and rectangles depending on which circle part
    case d
    when 2
      coos.push([x-1-(r/Math.sqrt(2)).to_i, y+(r/Math.sqrt(2)).to_i])
      coos.push([2*x-coos[0][0]-1, coos[0][1]])
      rects.push(Rect.new(x-1, y, 2, r))
    when 4
      coos.push([x-1-(r/Math.sqrt(2)).to_i, y-1-(r/Math.sqrt(2)).to_i])
      coos.push([coos[0][0], 2*y-coos[0][1]-1])
      rects.push(Rect.new(x-r-1, y-1, r, 2))
    when 6
      coos.push([x+(r/Math.sqrt(2)).to_i, y-1-(r/Math.sqrt(2)).to_i])
      coos.push([coos[0][0], 2*y-coos[0][1]-1])
      rects.push(Rect.new(x, y-1, r, 2))
    when 8
      coos.push([x-1-(r/Math.sqrt(2)).to_i, y-1-(r/Math.sqrt(2)).to_i])
      coos.push([2*x-coos[0][0]-1, coos[0][1]])
      rects.push(Rect.new(x-1, y-r-1, 2, r))
    else
      rects.push(Rect.new(x-1, y, 2, r), Rect.new(x-r-1, y-1, r, 2),
          Rect.new(x, y-1, r, 2), Rect.new(x-1, y-r-1, 2, r))
    end
    # intersection exists if intersecting with any of the radius rectangles
    return true if rects.any? {|rec| self.rect_intersection(rect, rec)}
    # iterate through rectangle's border lines
    [[rect.x, rect.y], [rect.x+rect.width-1, rect.y+rect.height-1]].each {|i|
      [[rect.x, rect.y+rect.height-1], [rect.x+rect.width-1, rect.y]].each {|j|
        # iterate through the characteristic lines
        coos.each {|c|
            # if borderline of rectangle intersects with diagonal radius line
            if self.line_intersection(i[0], i[1], j[0], j[1], c[0], c[1], x, y)
              # intersection exists
              return true
            end}}}
    # intersection does not exist
    return false
  end
  #----------------------------------------------------------------------------
  # rect_intersection
  #  r1 - first rectangle
  #  r2 - second rectangle
  #  This method quickly determines intersection of two rectangles. It is
  #  faster than the algorithm to determine line intersection as both
  #  rectangles are always rectangles with a rotation angle of 0, 90, 180 or
  #  270.
  #----------------------------------------------------------------------------
  def self.rect_intersection(r1, r2)
    return (r1.x + r1.width > r2.x && r1.x < r2.x + r2.width &&
            r1.y + r1.height > r2.y && r1.y < r2.y + r2.height)
  end
  #----------------------------------------------------------------------------
  # line_intersection
  #  x1 - x coordinate of the first line's first point
  #  y1 - y coordinate of the first line's first point
  #  x1 - x coordinate of the first line's second point
  #  y1 - y coordinate of the first line's second point
  #  x1 - x coordinate of the second line's first point
  #  y1 - y coordinate of the second line's first point
  #  x1 - x coordinate of the second line's second point
  #  y1 - y coordinate of the second line's second point
  #  This method uses a quick algorithm to test whether two lines intersect.
  #----------------------------------------------------------------------------
  def self.line_intersection(x1, y1, x2, y2, x3, y3, x4, y4)
    # calculate vector products
    d1 = (x3-x1)*(y4-y1) - (x4-x1)*(y3-y1)
    d2 = (x3-x2)*(y4-y2) - (x4-x2)*(y3-y2)
    d3 = (x1-x3)*(y2-y3) - (x2-x3)*(y1-y3)
    d4 = (x1-x4)*(y2-y4) - (x2-x4)*(y1-y4)
    # check vector product results
    if (d1 > 0 && d2 < 0 || d1 < 0 && d2 > 0) &&
        (d3 > 0 && d4 < 0 || d3 < 0 && d4 > 0)
      # intersection exists
      return true
    # if at least one point of one line lies on the other line
    elsif d1 == 0 && [x3, x4].min <= x1 && x1 <= [x3, x4].max &&
          [y3, y4].min <= y1 && y1 <= [y3, y4].max ||
          d2 == 0 && [x3, x4].min <= x2 && x2 <= [x3, x4].max &&
          [y3, y4].min <= y2 && y2 <= [y3, y4].max ||
          d3 == 0 && [x1, x2].min <= x3 && x3 <= [x1, x2].max &&
          [y1, y2].min <= y3 && y3 <= [y1, y2].max ||
          d4 == 0 && [x1, x2].min <= x4 && x4 <= [x1, x2].max &&
          [y1, y2].min <= y4 && y4 <= [y1, y2].max
      # intersection exists
      return true
    end
    # intersection does not exist
    return false
  end
      
end

# if using intelligent minimap mode
if BlizzABS::Config::INTELLIGENT_PASSABILTY && $DEBUG
  # load tileset data
  $data_tilesets = load_data('Data/Tilesets.rxdata')
  # get current map states
  new_data = load_data('Data/MapInfos.rxdata')
  # if first time intelligent passability is being used
  if !File.exist?('Data/Map_Data.abs')
    # initialize
    data, dates = {}, {}
    # all map IDs
    ids = new_data.keys.sort
  else
    # get passability data and "modified time" data from old data file
    data, dates = load_data('Data/Map_Data.abs')
    # iterate through all current map IDs
    new_data.keys.sort.each {|id|
        # if game not encrypted
        if File.exist?(sprintf('Data/Map%03d.rxdata', id))
          # open map file for reading
          file = File.open(sprintf('Data/Map%03d.rxdata', id), 'r')
          # remove map ID if map was edited
          [data, dates].each {|_hash| _hash.delete(id)} if dates[id] != file.mtime
          # close file
          file.close
        end}
    # iterate through all map IDs that were deleted
    (data.keys-new_data.keys).sort.each {|id|
        # remove map ID
        [data, dates].each {|hash| hash.delete(id)}}
    # get all map IDs that need to be updated
    ids = (new_data.keys-data.keys).sort
  end
  # open new file
  file = File.open('Data/Map_Data.abs', 'wb')
  # iterate through all IDs
  ids.each {|id|
      # load map
      map = load_data(sprintf('Data/Map%03d.rxdata', id))
      # create one map data pack
      data[id] = BlizzABS.setup_passability(map)
      # if game not encrypted
      if File.exist?(sprintf('Data/Map%03d.rxdata', id))
        # open map file for reading
        f = File.open(sprintf('Data/Map%03d.rxdata', id), 'r')
        # get map file modified time
        dates[id] = f.mtime
        # close file
        f.close
      end
      # prevent "Script is hanging" error
      Graphics.update}
  # save all data to file
  Marshal.dump([data, dates], file)
  # save and close file
  file.close
  # remove variables from memory completely
  file = f = data = map = $data_tilesets = nil
end
