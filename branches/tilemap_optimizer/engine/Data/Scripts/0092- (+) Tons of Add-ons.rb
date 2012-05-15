#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=
# Tons of Add-ons by Blizzard
# Version: 5.0b
# Type: Add-on Collection Control Script
# Date v1.00b:  14.11.2006
# Date v1.10b:  17.11.2006
# Date v1.60b:   4.12.2006
# Date v1.62b:   6.12.2006
# Date v1.70b:  13.12.2006
# Date v1.87b:  12.01.2007
# Date v2.20b:  16.01.2007
# Date v2.30b:  22.01.2007
# Date v2.31b:  24.01.2007
# Date v2.40b:   1.02.2007
# Date v2.50b:   4.02.2007
# Date v2.70b:   7.02.2007
# Date v2.71b:  12.02.2007
# Date v2.80b:  17.02.2007
# Date v3.70b:  19.02.2007
# Date v3.71b:  23.02.2007
# Date v3.80b:   7.03.2007
# Date v4.00b:   7.03.2007
# Date v4.01b:   9.03.2007
# Date v4.02b:  11.03.2007
# Date v4.30b:  12.03.2007
# Date v4.32b:  18.03.2007
# Date v4.50b:  24.03.2007
# Date v4.70b:  30.04.2007
# Date v4.80b:   4.05.2007
# Date v4.81b:   8.05.2007
# Date v4.85b:   7.07.2007
# Date v4.86b:   8.08.2007
# Date v4.90b:  12.07.2007
# Date v4.91b:  14.07.2007
# Date v4.97b:  31.07.2007
# Date v4.98b:   7.08.2007
# Date v5.00b:  ??.0?.2007
#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=
# 
# VERY IMPORTANT NOTE:
# 
#   For any new add-on the version will increase by 0.1, for any update of the
#   collection or any update on an add-on the version will increase by 0.01.
#   Also from v3.71b on there is a recognition global variable available which
#   will make the Tons of Add-ons much more compatible with many of my scripts.
#   I noticed serious issues with several of my older scripts.
# 
# 
# Important note:
# 
#   All Add-ons are initially turned off in any later version than 1.87b! 
#   Also note that "Full Reflection System" is BELOW HP/SP Absorbtion, because
#   of incompatibility issues.
# 
# 
# Compatibility:
# 
#   80% compatible with SKD v1.x. 40% compatible with SDK v2.x. Some add-ons
#   will corrupt your old savegames. If you experience the "Stack level too
#   deep" error, you might already use one of these add-ons. All of these
#   add-ons here work with each other with a success rate of 99%. This add-on
#   collection itself WILL corrupt your old savegames. May cause
#   incompatibility issues with following systems:
#   - exotic CBS-ex
#   - exotic CMS-es
#   - skill learning systems
#   - exotic graphic systems on the map
#   - weapon/armor changing systems
# 
# 
# Featured add-ons so far:
# 
#   - 49 add-ons by Blizzard
#   - 1 add-on by Zan
#   = 50 add-ons altogether
# 
# Ideas:
# 
#   - Blizzard
#   - GuardianAngelX72
#   - BanisherOfEden
#   - italianstal1ion
#   - indinera
#   - Yami
#   - blazinhandle
#   - Arrow-1
#   - Dark Angel Sion
#   - Zan
#   - shahafyz57
#   - Echo
# 
# 
# Features:
# 
#   ----> Graphic (make your game look nice):
# - Better Tilemap update (will update autotiles faster)
# - Animated Title (have an animated title screen without .gifs)
# - Center Battler (they will be centered instead of lined next to each other)
# - HP/SP/EXP gradient/slant bars (including 7 styles, opacity and least lag)
# - Location Names (shows pictures or names of the location the player visits)
# - Black Fade (shows a black screen when changing the map or before battle)
# - Simple Shaded Text (draws a shadow behind your text)
# - Blizz-Art lagless HUD (Heads Up Display using either HP/SP/EXP or simple)
# - Screen Tremble (makes your screen shake vertically, too)
# - Animation Stack (shows animation of all inflicted status effects)
# - Simple Facesets (shows a face instead of the spriteset in the main menu)
# - Caterpillar (party members follow you on the map)
# - Arrow over Player (shows arrow over player's head if he's "behind")
# - Animated Battle Background (animates battle backgrounds)
# - Map as Battleback (map is the battle backgrounds)
# - Facesets for DSS (shows a face instead of the spriteset in the status menu)
# - Status Effects as Icons (displays status effects as icons)
# - Animated Battlers Non-Action BS (animates battlers in battle systems)
# 
#   ----> Utility (make your game more unique and better/help you during debug):
# - FPS Modulator (increase the fps rate up 3 times like in an emulator)
# - Speed Modulator (change the main character's speed on the map)
# - Blizz-ABSEAL (the best event anti-lag for maps ever)
# - Fullscreen? (asks the player at game start if he wishes to switch to full)
# - Death Toll (counts killed enemies and actor deaths)
# - Window_BattleResult (displays gained items in a different, but better way)
# - Unique Skill Commands (different name for the Skill command for each class)
# - Ultimate Font Override (will override the font from any RMXP version)
# - Heal at LvlUp (heals characters who level up)
# - Weapon/Armor HP/SP Plus (max HP and max SP can also be increased)
# - EQUAP Skills (equipment skills, equip to learn + AP system like FF9)
# - Picture Movie Scene (easily create picture based cutscenes)
# - Target 'em all! (make skills target all battlers)
# - Quick Passability Test (let's you debug maps faster and more convenient)
# - Dynamic Passability Minimap (never was a minimap so easy to use)
# - Enemy Status in Battle (displays enemies' HP, SP and state)
# - Different Difficulties (like "Easy", "Normal", "Hard")
# - Skill Separation System (like "White Magic", "Black Magic", "Technic", etc.)
# - Multi-Hit (make weapons/skills/enemies hit more than once)
# 
#   ----> Status Effect (non-standard status effects):
# - Zombie (Healing items will hurt and light attacks are effective)
# - Regen (progressive healing aka poison, but the other way)
# - Auto-Revive (or Auto-Life, will be automatically revived after dieing)
# - Fury Status (if a specific character dies, another one will become Fury)
# - Invincible Status (this status will nullify ANY DAMAGE done by enemies)
# - Half SP (this status will halve SP cost when skills are used)
# - 1 SP (this status will set SP cost to 1 for all skills)
# - Full Reflection System (finally a Reflect that actually DOES work)
# 
#   ----> Skill (non-standard skills):
# - Absorb HP/SP (with considering undead enemies)
# - Death Roulette (kills a random target)
# - Blue Magic Skill (can learn enemy's skills)
# - EMP Skill (paralyze machine enemies)
# - Demi Skill (deals damage equal to a percentage of the remaining HP)
# 
# 
# Version history:
# 
# v1.10b:
#   -> added Black Fade by Blizzard
# 
# v1.60b:
#   -> added Ultimate Font Override by Blizzard
#   -> added Simple Shaded Text by Blizzard
#   -> added Heal at LvlUp by Blizzard
#   -> added Fury Status by Blizzard
#   -> added Invincible Status by Blizzard
# 
# v1.62b:
#   -> upgraded Death Toll by Blizzard to v1.2b
# 
# v1.70b:
#   -> added Half SP by Blizzard
# 
# v1.87b:
#   -> added Blizz-Art lagless HUD by Blizzard
#   -> upgraded Animated Title by Blizzard to v1.33b
#   -> upgraded Centered Battlers by Blizzard to v2.1b
#   -> upgraded HP/SP/EXP bars by Blizzard to v4.11b
#   -> upgraded Speed Modulator by Blizzard to v1.01b
#   -> upgraded Regen Status Effect by Blizzard to v1.1b
#   -> upgraded Auto-Revive by Blizzard to v1.21b
#   -> updated FPS Modulator by Blizzard
# 
# v2.20b:
#   -> added Weapon/Armor HP/SP Plus by Blizzard
#   -> added Full Reflection System by Blizzard
#   -> added EQ Skills by Blizzard
#   -> added Picture Movie Scene by Blizzard
# 
# v2.30b:
#   -> added Screen Tremble by Blizzard
# 
# v2.31b:
#   -> updated Screen Tremble by Blizzard
#   -> updated Better Tilemap update by Blizzard
# 
# v2.40b:
#   -> added Animation Stack by Blizzard
#   -> upgraded Picture Movie Scene by Blizzard to v2.02b
#   -> updated Screen Tremble by Blizzard
# 
# v2.50b:
#   -> added Target 'em all! by Blizzard
#   -> upgraded Unique Skill Commands by Blizzard to v1.11b
# 
# v2.70b:
#   -> added Quick Passability Test by Blizzard
#   -> added Dynamic Passability Minimap by Blizzard
#   -> upgraded Picture Movie Scene by Blizzard to v2.03b
# 
# v2.71b:
#   -> upgraded Dynamic Passability Minimap by Blizzard to v1.01b
# 
# v2.80b:
#   -> added Enemy Status in Battle by Blizzard
# 
# v3.70b:
#   -> added Simple Facesets by Blizzard
#   -> changed EQ Skills by Blizzard to EQUAP Skills and upgraded to v3.0b
#   -> upgraded Unique Skill Commands by Blizzard to v1.2b
#   -> updated Center Battler by Blizzard
#   -> updated Weapon/Armor HP/SP Plus by Blizzard
#   -> added constant for recognition by other scripts to improve compatibility
#   -> Why suddenly v3.7b? 37 add-ons are featured so far!
# 
# v3.71b:
#   -> upgraded Simple Facesets by Blizzard to v1.01b
#   -> fixed a problem with the compatibility recognition
# 
# v3.80b:
#   -> added Caterpillar by Blizzard
# 
# v4.00b:
#   -> added Arrow over Player by Blizzard
#   -> added EMP Skill by Blizzard
#   -> upgraded Caterpillar by Blizzard to v1.01b
#   -> upgraded EQUAP Skills by Blizzard to v3.02b
# 
# v4.01b:
#   -> upgraded Black Fade by Blizzard to v1.1b
# 
# v4.02b:
#   -> upgraded Window_BattleResult by Blizzard to v1.1b
# 
# v4.30b:
#   -> added Animated Battle Background by Blizzard
#   -> added Map as Battleback by Blizzard
#   -> added 1 SP by Blizzard
#   -> upgraded HP/SP/EXP gradient/slant bars by Blizzard to v4.2b
#   -> upgraded Blizz-Art lagless HUD by Blizzard to v1.2b
#   -> upgraded Window_BattleResult by Blizzard to v1.1b
#   -> upgraded Weapon/Armor HP/SP Plus by Blizzard to v1.01b
#   -> upgraded Full Reflection System by Blizzard to v2.0b
#   -> upgraded EMP Skill by Blizzard to v1.01b
# 
# v4.32b:
#   -> upgraded Zombie Status Effect by Blizzard to v1.1b
#   -> updated Arrow over Player by Blizzard
# 
# v4.50b:
#   -> added Different Difficulties by Blizzard
#   -> added Skill Separation System by Blizzard
#   -> upgraded Half SP by Blizzard to v1.4b
#   -> upgraded 1 SP by Blizzard to v1.1b
#   -> updated Center Battler by Blizzard
#   -> updated Blizz-Art lagless HUD by Blizzard
#   -> updated Death Roulette by Blizzard
#   -> updated EMP Skill by Blizzard
# 
# v4.70b:
#   -> added Facesets for DSS by Zan
#   -> added Status Effects as Icons for DSS by Blizzard
#   -> now compatible with Blizz-ABS 1.0.0.1 and higher
# 
# v4.80b:
#   -> added Animated Battlers for DBS by Blizzard
#   -> fixed the HUD lag problem with Blizz-ABS 1.0.0.1 and higher
# 
# v4.81b:
#   -> updated Skill Separation System by Blizzard
# 
# v4.85b:
#   -> upgraded Weapon/Armor HP/SP Plus by Blizzard to v2.0
#   -> upgraded Location Names by Blizzard to v2.1b
#   -> upgraded Blizz-Art lagless HUD by Blizzard to v1.3b
#   -> improved overall coding of Tons of Add-ons and fixed incompatibility bugs
# 
# v4.86b:
#   -> upgraded Fullscreen? by Blizzard to v1.22b
# 
# v4.9b:
#   -> added Demi Skill by Blizzard
# 
# v4.91b:
#   -> upgraded HP/SP/EXP gradient/slant bars by Blizzard to v4.4b
# 
# v4.97b:
#   -> due to a bug Ultimate Font Override can't be turned on/off ingame now
#   -> upgraded Location Names by Blizzard to v2.11b
#   -> upgraded Arrow over Player by Blizzard to v1.01b
#   -> upgraded Weapon/Armor HP/SP Plus by Blizzard to v2.0b
#   -> upgraded Death Toll by Blizzard to v1.3b
#   -> updated ABSEAL by Blizzard
# 
# v4.98b:
#   -> upgraded Caterpillar by Blizzard to v2.0
# 
# v5.0b:
#   -> added Multi-Hit by Blizzard
#   -> upgraded Caterpillar by Blizzard to v2.0b
#   -> upgraded Animated Battle Background by Blizzard to v1.1b
#   -> upgraded Map as Battleback by Blizzard to v1.5b
#   -> upgraded 1 SP by Blizzard to v1.11b
#   -> renamed and upgraded Blizz-ABSEAL by Blizzard to v2.0
#   -> renamed and upgraded Animated Battlers for Non-Action BS by Blizzard to v1.3b
#   -> rewritten conditions using classic syntax to avoid RGSS conditioning bug
#   -> now compatible with RTAB v1.16 + Plug-ins
# 
# 
# Instructions:
# 
# - Explanation:
# 
#   Every Add-on has its own instructions. Please read and follow them.
# 
# - Configuration:
# 
#   Configure the part just below to define which add-ons you want to use and 
#   which not. The configuration is split into two part for reason, don't
#   change this. It will work fine if you leave it as it is.
# 
# - For scripters:
# 
#   If you have any ideas how to improve this collection, just say so. I will
#   add you into the credits of this add-on collection if you have an own
#   add-on. I will not add any add-ons made by somebody else than yourself, you
#   can't ask me for somebody else to add an add-on. The creator has to ask me
#   himself.
# 
# 
# Side note:
# 
#   These add-ons were mostly tested in a different enviroment or not at all.
# 
# 
# Useless facts:
# 
#   - Tons of Add-ons already exceeds many CMS-es and even several CBS-es in
#     number of lines of code.
#   - The version history of Tons of Add-ons has more lines than several
#     add-ons themselves in Tons of Add-ons.
#   - Chaos Project uses only about 60% of the Tons of Add-ons.
#   - A good code is a short code that does what it is supposed to, not the
#     "Microsoft" way where you have many actually redundant lines of code.
#     Simple, short and straight, nothing more than necessary, that's what
#     makes codes efficient!
#   - Russian Reversal on Croatian Blizzards:
#     "In Russia Blizzard makes his scripts SDK compatible with YOU!"
# 
# 
# If you find any bugs, please report them here:
# http://www.chaosproject.co.nr
#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                                                                             #
#   ###   ###  #   # #####  #   #### #   # ####   ###  #####  #   ###  #   #  #
#  #   # #   # ##  # #      #  #     #   # #   # #   #   #    #  #   # ##  #  #
#  #     #   # # # # ####   #  #  ## #   # ####  #   #   #    #  #   # # # #  #
#  #   # #   # #  ## #      #  #   # #   # #   # #####   #    #  #   # #  ##  #
#   ###   ###  #   # #      #   ####  ###  #   # #   #   #    #   ###  #   #  #
#                                                                             #
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

$tons_version = 5.0

module TONS_OF_ADDONS
  
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration 1
# 
# You can enable/disable any add-on here if you wish. Set the value to false
# to disable it. These features CANNOT be turned on/off during the game.
# 
# NAME_OF_THE_ADDON = true
# NAME_OF_THE_ADDON = false
# 
# where NAME_OF_THE_ADDON is the same variable as the one used below.
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
  # the graphic add-ons
  ANIMATED_TITLE                = false
  # the utility add-ons
  FULLSCREEN                    = true
  ULTIMATE_FONT_OVERRIDE        = true
  EQUAP_SKILLS                  = false
  DIFFICULTY                    = false
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration 1
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
  
end

#==============================================================================
# Game_System
#==============================================================================

class Game_System
  
  alias init_tons_of_addons_later initialize
  def initialize
    init_tons_of_addons_later
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration 2
# 
# You can enable/disable any add-on here if you wish. Set the value to true
# to disable it initially. To turn it on/off ingame, just use the Call script
# command with one of these syntaxes:
# 
# $game_system.NAME_OF_THE_ADDON = true
# $game_system.NAME_OF_THE_ADDON = false
# 
# where NAME_OF_THE_ADDON is the same variable as the one used below.
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    # the GRAPHIC add-ons
    @BETTER_TILEMAP_UPDATE      = true
    @CENTER_BATTLER             = false
    @BARS                       = true
    @LOCATION_NAMES             = true
    @BLACKFADE                  = true
    @SHADED_TEXT                = true
    @HUD                        = false
    @TREMBLE                    = false
    @ANIMATION_STACK            = false
    @FACESETS                   = false
    @CATERPILLAR                = false
    @ARROW_OVER_PLAYER          = false
    @ANIMATED_BATTLE_BACKGROUND = false
    @MAP_AS_BATTLEBACK          = false
    @FACESETS_DSS               = false
    @STATUS_ICONS               = false
    @ANIMATED_BATTLERS_DBS      = false
    # the UTILITY add-ons
    @FPS_MODULATOR              = false
    @SPEED_MODULATOR            = false
    @DEATH_TOLL                 = false
    @WINDOW_BATTLERESULT        = false
    @UNIQUE_SKILL_COMMANDS      = false
    @HEAL_AT_LVLUP              = false
    @HPSPPLUS                   = false
    @TARGET_EM_ALL              = false
    @QUICK_PASSABILITY_TEST     = false
    @MINIMAP                    = false
    @ENEMY_STATUS               = false
    @SKILL_SEPARATION           = false
    # the STATUS EFFECT add-ons
    @ZOMBIE_STATUS              = true
    @REGEN_STATUS               = true
    @AUTO_REVIVE                = true
    @FURY_STATUS                = true
    @INVINCIBLE_STATUS          = true
    @HALF_SP                    = true
    @_1_SP                      = true
    @REFLECT                    = true
    # the SKILL add-ons
    @ABSORB_HP_SP               = true
    @DEATH_ROULETTE             = true
    @BLUE_MAGIC_SKILL           = true
    @EMP_SKILL                  = true
    @DEMI_SKILL                 = true
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration 2
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
  end
  
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# I suggest you don't edit anything below this line except for the
# configuration of the add-ons.
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

  attr_accessor :BETTER_TILEMAP_UPDATE
  attr_accessor :CENTER_BATTLER
  attr_accessor :BARS
  attr_accessor :LOCATION_NAMES
  attr_accessor :BLACKFADE
  attr_accessor :SHADED_TEXT
  attr_accessor :HUD
  attr_accessor :TREMBLE
  attr_accessor :ANIMATION_STACK
  attr_accessor :FACESETS
  attr_accessor :CATERPILLAR
  attr_accessor :ARROW_OVER_PLAYER
  attr_accessor :ANIMATED_BATTLE_BACKGROUND
  attr_accessor :MAP_AS_BATTLEBACK
  attr_accessor :FACESETS_DSS
  attr_accessor :STATUS_ICONS
  attr_accessor :ANIMATED_BATTLERS_DBS
  attr_accessor :FPS_MODULATOR
  attr_accessor :SPEED_MODULATOR
  attr_accessor :DEATH_TOLL
  attr_accessor :WINDOW_BATTLERESULT
  attr_accessor :UNIQUE_SKILL_COMMANDS
  attr_accessor :HEAL_AT_LVLUP
  attr_accessor :HPSPPLUS
  attr_accessor :TARGET_EM_ALL
  attr_accessor :QUICK_PASSABILITY_TEST
  attr_accessor :MINIMAP
  attr_accessor :ENEMY_STATUS
  attr_accessor :SKILL_SEPARATION
  attr_accessor :ZOMBIE_STATUS
  attr_accessor :REGEN_STATUS
  attr_accessor :AUTO_REVIVE
  attr_accessor :FURY_STATUS
  attr_accessor :INVINCIBLE_STATUS
  attr_accessor :HALF_SP
  attr_accessor :_1_SP
  attr_accessor :REFLECT
  attr_accessor :ABSORB_HP_SP
  attr_accessor :DEATH_ROULETTE
  attr_accessor :BLUE_MAGIC_SKILL
  attr_accessor :EMP_SKILL
  attr_accessor :DEMI_SKILL
  
end

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                                                                             #
#                #### ####   ###  ####  #   #  #  ###  #####                  #
#               #     #   # #   # #   # #   #  # #   # #                      #
#               #  ## ####  #   # ####  #####  # #     #####                  #
#               #   # #   # ##### #     #   #  # #   #     #                  #
#                #### #   # #   # #     #   #  #  ###  #####                  #
#                                                                             #
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

#==============================================================================
# Better Tilemap update by Blizzard#
# Type: Map Graphic Improvement
# Version: 1.0b
# Date: 13.8.2006
# 
# new in 1.0b:
#   - changed method of updating
# 
#   This will add a little faster update of autotile frames to allow a more
#   natural feeling.
#==============================================================================

#==============================================================================
# Tilemap
#==============================================================================

class Tilemap
  
  alias upd_fps_later update
  def update
    if $game_system.BETTER_TILEMAP_UPDATE
      upd_fps_later if Graphics.frame_count % (Graphics.frame_rate / 5) == 0
    end
    upd_fps_later
  end
  
end

#==============================================================================
# Animated Title by Blizzard
# Version: 1.33b
# Type: Game Graphic Design Improvement
# Date: 17.3.2006
# Date v1.3: 26.5.2006
# Date v1.32b: 14.11.2006
# Date v1.33b: 12.1.2007
# 
# 
# v1.3 features:
#   - completely overworked and 99% SDK compatible
# 
# v1.32b features:
#   - slightly improved code
# 
# v1.33b features:
#   - slightly improved code
# 
# 
# Instructions:
# 
#   - if you want to change the delay between the frames change "DELAY"
#   - name the frames of your title pictures "title0", "title1" and so on.
#   - to change the number of frames, change the value of "PICS"
#   - be sure to set "title0" as your title screen in the database
#==============================================================================

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

DELAY = 20 # change the delay
PICS = 1 # number of pictures/frames

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#==============================================================================
# Scene_Title
#==============================================================================

class Scene_Title
  
  alias initialize_animated_title initialize
  def initialize
    initialize_animated_title
    @frame = @counter = 0
  end
  
  alias update_animated_title update
  def update
    if TONS_OF_ADDONS::ANIMATED_TITLE && PICS > 1
      @counter += 1
      if @counter == DELAY
        @counter = 0
        @frame = (@frame + 1) % PICS
        @sprite.bitmap = RPG::Cache.title("title#{@frame}")
        Graphics.transition
      end
    end
    update_animated_title
  end
  
end

#==============================================================================
# Centered Battlers by Blizzard
# Version: 2.1b
# Type: Battle Graphic Improvement
# Date: 14.11.2006
# Date v2.1b: 12.1.2007
# 
# new in v2.0b:
#   - new code is much more compatible and not merged into the Regen add-on
# 
# new in v2.1b:
#   - compatible with "Easy LvlUp Notifier"
#==============================================================================

#==============================================================================
# Sprite_Battler
#==============================================================================

class Sprite_Battler < RPG::Sprite 
    
  alias upd_center_battler_later update
  def update
    upd_center_battler_later
    if $game_system.CENTER_BATTLER && @battler != nil
      if @battler.is_a?(Game_Actor)
        self.x = case $game_party.actors.size
        when 1 then @battler.screen_x + 240
        when 2 then @battler.screen_x + 80 + @battler.index * 160
        when 3 then @battler.screen_x + 80
        when 4 then @battler.screen_x
        end
      elsif @battler.is_a?(Game_Enemy)
        self.x = @battler.screen_x
      end
      self.y = @battler.screen_y
      self.z = @battler.screen_z
    end
  end 
  
end

#==============================================================================
# Scene_Battle
#==============================================================================

class Scene_Battle
  
  alias upd_center_battler_later update
  def update
    if $game_system.CENTER_BATTLER && @lvlup_windows != nil
      for i in 0...@lvlup_windows.size
        @lvlup_windows[i].x = case $game_party.actors.size
        when 1 then 240
        when 2 then 80 + i * 320
        when 3 then 80 + i * 160
        when 4 then i * 160
        end
      end
    end
    upd_center_battler_later
  end
  
  alias phase3_setup_command_window_center_battler_later phase3_setup_command_window
  def phase3_setup_command_window
    phase3_setup_command_window_center_battler_later
    if $game_system.CENTER_BATTLER
      @actor_command_window.x = case $game_party.actors.size
      when 1 then 240
      when 2 then 80 + @actor_index * 320
      when 3 then 80 + @actor_index * 160
      when 4 then @actor_index * 160
      end
      @actor_command_window.index = 0
    end
  end

end

#==============================================================================
# Arrow_Actor
#==============================================================================

class Arrow_Actor < Arrow_Base
  
  alias upd_center_battler_later update
  def update
    upd_center_battler_later
    if $game_system.CENTER_BATTLER && self.actor != nil
      self.x = case $game_party.actors.size
      when 1 then 240 + self.actor.screen_x
      when 2 then 2 * self.actor.screen_x
      when 3 then 80 + self.actor.screen_x
      when 4 then self.actor.screen_x
      end
      self.y = self.actor.screen_y
    end
  end

end

#==============================================================================
# Window_BattleStatus
#==============================================================================

class Window_BattleStatus < Window_Base
  
  alias refresh_center_battler_later refresh
  def refresh
    unless $game_system.CENTER_BATTLER
      refresh_center_battler_later
      return
    end
    self.contents.clear
    @item_max = $game_party.actors.size
    for i in 0...$game_party.actors.size
      actor = $game_party.actors[i]
      actor_x = case $game_party.actors.size
      when 1 then 4 + 240
      when 2 then 4 + 80 + i * 320
      when 3 then 4 + 80 + i * 160
      when 4 then 4 + i * 160
      end
      draw_actor_name(actor, actor_x, 0)
      draw_actor_hp(actor, actor_x, 32, 120)
      draw_actor_sp(actor, actor_x, 64, 120)
      if @level_up_flags[i]
        self.contents.font.color = normal_color
        self.contents.draw_text(actor_x, 96, 120, 32, 'LEVEL UP!')
      else
        draw_actor_state(actor, actor_x, 96)
      end
    end
  end

end

#==============================================================================
# Blizz-Art Gradient Styler with HP/SP/EXP bars by Blizzard
# Version: 4.4b
# Type: Game Playability Improvement
# Date v4.0: 13.11.2006
# Date v4.11: 12.1.2007
# Date v4.2b: 12.3.2007
# Date v4.4b: 14.7.2007
# 
# v2.0+:
#   - 2 styles, better code
# v3.0+:
#   - 6 styles, far better code
# v4.0:
#   - 6 styles, overworked and extremely delagged, enjoy the most lagless
#     gradient/slant bar code ever
# v4.11:
#   - added instructions and a recognition constant for plugins
# v4.2b:
#   - improved code
# v4.4b:
#   - improved code, now 7 styles
# 
# 
# Instructions:
# 
#   You can change style and opacity by using the "Call script" event command.
#   Use one of of these syntaxes:
# 
#     $game_system.bar_style = X
#     $game_system.bar_opacity = Y
# 
#   X - number from 0 to 6 and is the ID number of the style
#   Y - number from 0 to 255 and indicates the opacity
#   
#   Values out of range will be corrected.
#==============================================================================

$Blizz_Art = true

#==============================================================================
# Game_System
#==============================================================================

class Game_System
  
  attr_accessor :bar_style
  attr_reader   :bar_opacity
  
  alias init_blizzart_later initialize
  def initialize
    init_blizzart_later
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration
# 
#   Configure this part manually if you have no "Options" controller for the
#   styles and the opacity. (style: 0~6, opacity: 0~255)
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    @bar_style = 5
    self.bar_opacity = 255
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
  end
  
  def bar_opacity=(alpha)
    @bar_opacity = [[alpha, 0].max, 255].min
  end
  
end

#==============================================================================
# Game_Actor 
#==============================================================================

class Game_Actor < Game_Battler 
  
  def now_exp 
    return @exp - @exp_list[@level] 
  end 
  
  def next_exp 
    return @exp_list[@level+1] > 0 ? @exp_list[@level+1] - @exp_list[@level] : 0
  end 
  
end

#==============================================================================
# Bitmap
#==============================================================================

class Bitmap

  def gradient_bar(x, y, w, color1, color2, color3, rate)
    return unless $game_system.BARS
    return if $game_system.bar_style < 0 || $game_system.bar_style > 6
    styles = [1, 3, 4, 5]
    offset = 5
    x += offset
    y += 26
    if styles.include?($game_system.bar_style)
      offset += 2
      w = w / 8 * 8
      y -= 1
      $game_system.bar_style == 5 ? y-= 2 : x += 1
    elsif $game_system.bar_style == 6
      offset += 2
      y -= 3
    end
    alpha = $game_system.bar_opacity
    if $game_system.bar_style < 5
      for i in 0...(offset+3)
        fill_rect(x-i, y+i-2, w+3, 1, Color.new(0, 0, 0))
      end
      for i in 0...(offset+1)
        fill_rect(x-i, y+i-1, w+1, 1, Color.new(255, 255, 255))
      end
      if $game_system.bar_style < 2
        for i in 0...(w+offset)
          red = color3.red * i / (w + offset)
          green = color3.green * i / (w + offset)
          blue = color3.blue * i / (w + offset)
          oy = i < offset ? offset-i : 0
          off = i < offset ? i : i > w ? w+offset-i : offset
          fill_rect(x+i-offset+1, y+oy-1, 1, off, Color.new(red, green, blue, alpha))
        end
        if (w*rate).to_i >= offset
          for i in 0...((w*rate).to_i+offset)
            red = color1.red + (color2.red-color1.red)*i/((w+offset)*rate)
            green = color1.green + (color2.green-color1.green)*i/((w+offset)*rate)
            blue = color1.blue + (color2.blue-color1.blue)*i/((w+offset)*rate)
            oy = i < offset ? offset-i : 0
            off = i < offset ? i : i > w*rate ? (w*rate).to_i+offset-i : offset
            fill_rect(x+i-offset+1, y+oy-1, 1, off, Color.new(red, green, blue, alpha))
          end
        else
          for i in 0...(w*rate).to_i
            for j in 0...offset
              red = color1.red + (color2.red-color1.red) * i / (w * rate)
              green = color1.green + (color2.green-color1.green) * i / (w * rate)
              blue = color1.blue + (color2.blue-color1.blue) * i / (w * rate)
              set_pixel(x+i-j+1, y+j-1, Color.new(red, green, blue, alpha))
            end
          end
        end
      else
        for i in 0...offset
          red = color3.red * i / offset
          green = color3.green * i / offset
          blue = color3.blue * i / offset
          fill_rect(x-i+1, y+i-1, w, 1, Color.new(red, green, blue, alpha))
          if $game_system.bar_style == 4
            if i < offset / 2
              red = color2.red * (i+1) / (offset/2) 
              green = color2.green * (i+1) / (offset/2)
              blue = color2.blue * (i+1) / (offset/2)
            else
              red = color2.red * (offset+1-i) / (offset/2 + 1)
              green = color2.green * (offset+1-i) / (offset/2 + 1)
              blue = color2.blue * (offset+1-i) / (offset/2 + 1) 
            end
          else
            red = color1.red + (color2.red-color1.red) * i / offset
            green = color1.green + (color2.green-color1.green) * i / offset
            blue = color1.blue + (color2.blue-color1.blue) * i / offset
          end
          fill_rect(x-i+1, y+i-1, w*rate, 1, Color.new(red, green, blue, alpha))
        end
      end
      if styles.include?($game_system.bar_style)
        for i in 0...w
          for j in 0...offset
            if styles.include?($game_system.bar_style) && i % 8 < 2
              set_pixel(x+i-j+1, y+j-1, Color.new(0, 0, 0, alpha))
            end
          end
        end
      end
    else
      fill_rect(x+1, y-3, w+2, 12, Color.new(255, 255, 255, alpha))
      for i in 0...10
        if i < 5
          red = color3.red * (i+1) / 5
          green = color3.green * (i+1) / 5
          blue = color3.blue * (i+1) / 5
        else
          red = color3.red * (11-i) / 6
          green = color3.green * (11-i) / 6
          blue = color3.blue * (11-i) / 6
        end
        fill_rect(x+2, y+i-2, w, 1, Color.new(red, green, blue, alpha))
        if i < 5
          red = color2.red * (i+1) / 5
          green = color2.green * (i+1) / 5
          blue = color2.blue * (i+1) / 5
        else
          red = color2.red * (11-i) / 6
          green = color2.green * (11-i) / 6
          blue = color2.blue * (11-i) / 6
        end
        fill_rect(x+2, y+i-2, w*rate, 1, Color.new(red, green, blue, alpha))
      end
      if styles.include?($game_system.bar_style)
        for i in 0...w/8
          fill_rect(x+2+i*8, y-2, 1, 10, Color.new(0, 0, 0, alpha))
          fill_rect(x+9+i*8, y-2, 1, 10, Color.new(0, 0, 0, alpha))
        end
      end
    end
  end
  
end

#==============================================================================
# Window_Base
#==============================================================================

class Window_Base < Window

  alias draw_actor_hp_blizzart_later draw_actor_hp
  def draw_actor_hp(actor, x, y, w = 148)
    if $game_system.BARS
      w -= 12
      rate = (actor.maxhp > 0 ? actor.hp.to_f / actor.maxhp : 0)
      if rate > 0.6
        color1 = Color.new(80 - 150 * (rate-0.6), 80, 50 * (rate-0.6), 192) 
        color2 = Color.new(240 - 450 * (rate-0.6), 240, 150 * (rate-0.6), 192) 
      elsif rate > 0.2 && rate <= 0.6
        color1 = Color.new(80, 200 * (rate-0.2), 0, 192) 
        color2 = Color.new(240, 600 * (rate-0.2), 0, 192) 
      elsif rate <= 0.2
        color1 = Color.new(400 * rate, 0, 0, 192) 
        color2 = Color.new(240, 0, 0, 192) 
      end
      color3 = Color.new(0, 80, 0, 192)
      self.contents.gradient_bar(x, y, w, color1, color2, color3, rate)
      if $scene.is_a?(Scene_Battle)
        draw_actor_hp_blizzart_later(actor, x, y, w)
      else
        draw_actor_hp_blizzart_later(actor, x, y)
      end
    else
      draw_actor_hp_blizzart_later(actor, x, y, w)
    end
  end

  alias draw_actor_sp_blizzart_later draw_actor_sp
  def draw_actor_sp(actor, x, y, w = 148)
    if $game_system.BARS
      w -= 12
      rate = (actor.maxsp > 0 ? actor.sp.to_f / actor.maxsp : 0)
      if rate > 0.4
        color1 = Color.new(60 - 66 * (rate-0.4), 20, 80, 192) 
        color2 = Color.new(180 - 200 * (rate-0.4), 60, 240, 192) 
      elsif rate <= 0.4
        color1 = Color.new(20 + 100 * rate, 50 * rate, 26 + 166 * rate, 192) 
        color2 = Color.new(60 + 300 * rate, 150 * rate, 80 + 400 * rate, 192) 
      end
      color3 = Color.new(0, 0, 80, 192) 
      self.contents.gradient_bar(x, y, w, color1, color2, color3, rate)
      if $scene.is_a?(Scene_Battle)
        draw_actor_sp_blizzart_later(actor, x, y, w)
      else
        draw_actor_sp_blizzart_later(actor, x, y)
      end
    else
      draw_actor_sp_blizzart_later(actor, x, y, w)
    end
  end

  alias draw_actor_exp_blizzart_later draw_actor_exp
  def draw_actor_exp(actor, x, y, w = 148)
    if $game_system.BARS
      w += 12
      rate = (actor.next_exp != 0 ? actor.now_exp.to_f / actor.next_exp : 1)
      if rate < 0.5
        color1 = Color.new(20 * rate, 60, 80, 192) 
        color2 = Color.new(60 * rate, 180, 240, 192) 
      elsif rate >= 0.5
        color1 = Color.new(20 + 120 * (rate-0.5), 60 + 40 * (rate-0.5), 80, 192)
        color2 = Color.new(60 + 360 * (rate-0.5), 180 + 120 * (rate-0.5), 240, 192)
      end
      color3 = Color.new(80, 80, 80, 192) 
      self.contents.gradient_bar(x, y, w, color1, color2, color3, rate)
    end
    draw_actor_exp_blizzart_later(actor, x, y)
  end
  
end

#==============================================================================
# Location Names with Pictures or Text by Blizzard
# Version: 2.11b
# Type: Game Playability Improvement
# Date: 14.11.2006
# Date v2.1b: 7.7.2007
# Date v2.11b: 30.7.2007
# 
# NOTE: This script WILL corrupt old savegames!
# 
# Instructions:
#   Connect map IDs with picture names. All pictures MUST be in the the Names
#   folder in your picture folder. If you don't have a picture, the map name
#   will be written out using the default text engine from RMXP. Please set up
#   the font you wish the text to be displayed in this case.
#==============================================================================

LOCATION_FONT = 'Arial'
LOCATION_SIZE = 32
LOCATION_BOLD = true
LOCATION_ITALIC = false
LOCATION_COLOR = Color.new(255, 255, 255) # Color.new(R, G, B, A)
DISPLAY_TIME = 5 # in seconds

#==============================================================================
# Game_System
#==============================================================================

class Game_System
  
  attr_accessor :map_name_id
  attr_accessor :name_timer
  
  alias init_names_later initialize
  def initialize
    init_names_later
    @map_name_id = 0
    @name_timer = 0
  end
  
end

#==============================================================================
# Name_Sprite
#==============================================================================

class Name_Sprite < Sprite
  
  attr_accessor :timer
  
  def initialize
    super
    if $game_system.map_name_id == $game_map.map_id
      @timer = $game_system.name_timer
    else
      @timer = 0
    end
    if @timer < 16
      self.opacity = @timer * 15
    elsif @timer > 16 + 20 * DISPLAY_TIME
      self.opacity = 255 - (@timer - 16 - 20 * DISPLAY_TIME)* 15
    end
    $game_system.map_name_id = $game_map.map_id
    self.z = 6000
    self.bitmap = get_image($game_map.map_id)
    self.bitmap == nil ? self.dispose : self.x = 640 - self.bitmap.width
  end
  
  def get_image(id)
    case id
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START of Database
# 
#   Use this template to configure this add-on:
# 
#     when ID then name = 'FILE_NAME'
#   
#   ID - map ID where the picture should be displayed
#   FILE_NAME - the file name of the picture file in the Pictures/Names folder
# 
#   If you don't have a picture and want the name displayed anyway, please use:
# 
#     when ID then name = nil
# 
#   Instead of an image normal text will be displayed in the chosen font.
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    when 10, 12, 13, 17, 20, 22, 23, 24, 25 then name = nil
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END of Database
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    else
      return nil
    end
    if name == nil
      bitmap = Bitmap.new(1, 1)
      bitmap.font.name = LOCATION_FONT
      bitmap.font.size = LOCATION_SIZE
      w = bitmap.text_size($game_map.name).width + 40
      bitmap.dispose
      bitmap = Bitmap.new(w, LOCATION_SIZE + 16)
      bitmap.font.name = LOCATION_FONT
      bitmap.font.size = LOCATION_SIZE
      bitmap.font.bold = LOCATION_BOLD
      bitmap.font.italic = LOCATION_ITALIC
      bitmap.font.color = LOCATION_COLOR
      bitmap.draw_text(0, 8, w, LOCATION_SIZE + 8, $game_map.name, 1)
    else
      bitmap = RPG::Cache.picture("Names\\#{name}")
    end
    return bitmap
  end
  
  def dispose
    $game_system.name_timer = @timer
    super
  end
  
end

#==============================================================================
# Spriteset_Map
#==============================================================================

class Spriteset_Map
  
  attr_accessor :name
  
  alias init_name_later initialize
  def initialize
    init_name_later
    @name = Name_Sprite.new if $game_system.LOCATION_NAMES
  end
  
  alias upd_name_later update
  def update
    if @name != nil 
      unless @name.disposed?
        @name.timer += 1
        @name.opacity += 15 if @name.timer < 16
        @name.opacity -= 15 if @name.timer > 16 + 20 * DISPLAY_TIME
        if @name.opacity == 0
          @name.dispose
          @name = nil
        end
      else
        @name = nil
      end
    end
    upd_name_later
  end
  
  alias dispose_name_later dispose
  def dispose
    dispose_name_later
    unless @name == nil
      $game_system.name_timer = @name.timer
      @name.dispose
    end
    @name = nil
  end
  
end

#============================================================================== 
# Scene_Title
#============================================================================== 

class Scene_Title

  alias main_location_later main
  def main
    $map_infos = ARC::Data.load('Data/MapInfos.arc')
    for key in $map_infos.keys
      $map_infos[key] = $map_infos[key].name
    end
    main_location_later
  end
  
end

#============================================================================== 
# Game_Map 
#============================================================================== 

class Game_Map
        
  def name
    return $map_infos[@map_id]
  end
   
end

#==============================================================================
# Black Fade by Blizzard
# Version: 1.1b
# Type: Graphical Improvement
# Date: 28.4.2006
# Date v1.1b: 9.3.2006
# 
# 
# new in 1.1b:
#   - optional setting for black fade before battle
# 
# Explanation:
# 
#   Replaces the standard fading between maps with a black screen. Note that
#   this add-on is much less compatible than other add-ons and therefore it
#   might cause problems.
#==============================================================================

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

MAP_FADE = true # execute black fade when changing maps
MAP_TRANSIT = 8 # how long does the transition take
MAP_BLACKTIME = 12 # how long does black screen stay
BATTLE_FADE = true # execute black fade when changing maps
BATTLE_TRANSIT = 20 # how long does the transition take
BATTLE_BLACKTIME = 12 # how long does black screen stay

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#==============================================================================
# Scene_Map
#==============================================================================

class Scene_Map
  
  alias main_player_black_fade_later main
  def main
    main_player_black_fade_later
    if $game_system.BLACKFADE && BATTLE_FADE && $scene.is_a?(Scene_Battle)
      if $data_system.battle_transition == ''
        Graphics.transition(BATTLE_TRANSIT)
      else
        Graphics.transition(BATTLE_TRANSIT, 'Graphics/Transitions/' +
          $data_system.battle_transition)
      end
      Graphics.freeze
      Graphics.transition(BATTLE_BLACKTIME)
      Graphics.freeze
    end
  end
  
  alias transfer_player_black_fade_later transfer_player
  def transfer_player
    unless $game_system.BLACKFADE && MAP_FADE
      transfer_player_black_fade_later
      return
    end
    $game_temp.player_transferring = false
    if $game_map.map_id != $game_temp.player_new_map_id
      $game_map.setup($game_temp.player_new_map_id)
    end
    $game_player.moveto($game_temp.player_new_x, $game_temp.player_new_y)
    case $game_temp.player_new_direction
    when 2 then $game_player.turn_down
    when 4 then $game_player.turn_left
    when 6 then $game_player.turn_right
    when 8 then $game_player.turn_up
    end
    $game_player.straighten
    $game_map.update
    Graphics.freeze if $game_temp.transition_processing # added
    @spriteset.dispose
    # added from here
    if $game_temp.transition_processing
      Graphics.transition(MAP_TRANSIT)
      Graphics.freeze
      Graphics.transition(MAP_BLACKTIME)
      Graphics.freeze
    end
    # to here
    @spriteset = Spriteset_Map.new
    if $game_temp.transition_processing
      $game_temp.transition_processing = false
      Graphics.transition(MAP_TRANSIT) # instead of 20 now MAP_TRANSIT
    end
    $game_map.autoplay
    Graphics.frame_reset
    Input.update
  end
  
end

#==============================================================================
# Simple Shaded Text by Blizzard
# Version: 1.0c
# Type: Text Readability Improvement
# Date: 2.7.2006
#==============================================================================

#==============================================================================
# Bitmap
#==============================================================================

class Bitmap
  
  alias draw_text_shaded_text_later draw_text
  def draw_text(x2, y2, w2 = 0, h2 = 0, text2 = '', a2 = 0)
    if x2.is_a?(Rect)
      x, y, w, h, text, a = x2.x, x2.y, x2.width, x2.height, y2, w2
    else
      x, y, w, h, text, a = x2, y2, w2, h2, text2, a2
    end
    if $game_system != nil && $game_system.SHADED_TEXT
      save_color = self.font.color.clone
      self.font.color = Color.new(0, 0, 0, 255)
      draw_text_shaded_text_later(x+1, y+1, w, h, text, a)
      self.font.color = save_color
    end
    draw_text_shaded_text_later(x, y, w, h, text, a)
  end
  
end

#==============================================================================
# Blizz-Art lagless HUD by Blizzard
# Version: 1.3b
# Type: Game Playability Improvement
# Date: 16.12.2006
# Date v1.1b: 12.1.2007
# Date v1.2b: 11.3.2007
# Date v1.3b: 7.7.2007
# 
# 
# IMPORTANT:
# 
#   The "not simple" method of using this add-on REQUIRES Blizz-Art Gradient
#   styler for HP/SP/EXP bars. Blizz-ABS disables this add-on automatically and
#   uses the Blizz-ABS HUD system.
# 
# 
# Instructions:
# 
#   This add-on will add a HUD into your game. Configure the part below. The
#   meanings of the variables are:
# 
#     SIMPLE       - set this to false to use Blizz-Art Gradient styler instead
#                    of the normal bars
#     FULL_DISPLAY - set to true to show the stats of all party members in the
#                    display (otherwise hold D and press Q/W to cycle through
#                    the actors)
#     TOP          - set this value to false and the HUD will appear on the
#                    bottom
# 
# Side-Note:
# 
#   This add-on comes BELOW the Gradient Styler. This HUD was made for an
#   infinite number of party members, but if using FULL_DISPLAY, only the first
#   4 members will be displayed.
#==============================================================================

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Start HUD Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

SIMPLE = true
FULL_DISPLAY = false
TOP = true
HUD_TYPE = 0 # 0, 1 or 2

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# End HUD Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#==============================================================================
# Game_System
#==============================================================================

class Game_System
  
  attr_accessor :index
  attr_accessor :bar_style unless FULL_DISPLAY
  attr_reader   :bar_opacity
  
  alias init_blizzart_hud_later initialize
  def initialize
    init_blizzart_hud_later
    @index = 0 unless FULL_DISPLAY
    unless $Blizz_Art
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration
# 
#   Configure this part manually if you have no "Options" controller for the
#   styles and the opacity. (style: 0~5, opacity: 0~255)
#   Note that this WILL be overriden if you use Blizz-Art Gradient Styler.
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
      @bar_style = 5
      self.bar_opacity = 255
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    end
  end
  
  def bar_opacity=(alpha)
    @bar_opacity = [[alpha, 0].max, 255].max
  end
  
end

#==============================================================================
# Bitmap
#==============================================================================

class Bitmap
  
  def gradient_bar_simple(x, y, w, color1, color2, rate)
    w = w / 8 * 8
    alpha = $game_system.bar_opacity
    case HUD_TYPE
    when 0 then fill_rect(x + 1, y, w + 2, 14, Color.new(255, 255, 255, 192))
    when 1 then fill_rect(x + 1, y, w + 2, 14, Color.new(255, 255, 255, 0))
    end
    for i in 1..6
      color = Color.new(color2.red*i/6, color2.green*i/6, color2.blue*i/6, alpha)
      fill_rect(x + 2, y + i, w, 14 - i * 2, color)
      color = Color.new(color1.red*i/6, color1.green*i/6, color1.blue*i/6, alpha)
      fill_rect(x + 2, y + i, w * rate, 14 - i * 2, color)
    end
  end
  
  unless $Blizz_Art
  alias draw_text_shaded_text_later draw_text
  def draw_text(x2, y2, w2 = 0, h2 = 0, text2 = '', a2 = 0)
    if x2.is_a?(Rect)
      x, y, w, h, text, a = x2.x, x2.y, x2.width, x2.height, y2, w2
    else
      x, y, w, h, text, a = x2, y2, w2, h2, text2, a2
    end
    save_color = self.font.color.clone
    self.font.color = Color.new(0, 0, 0, 255)
    draw_text_shaded_text_later(x+1, y+1, w, h, text, a)
    self.font.color = save_color
    draw_text_shaded_text_later(x, y, w, h, text, a)
  end
  end

  def draw_text_full(x2, y2, w2 = 0, h2 = 0, text2 = '', a2 = 0)
    if x2.is_a?(Rect)
      x, y, w, h, text, a = x2.x, x2.y, x2.width, x2.height, y2, w2
    else
      x, y, w, h, text, a = x2, y2, w2, h2, text2, a2
    end
    save_color = self.font.color.clone
    self.font.color = Color.new(0, 0, 0, 255)
    draw_text_shaded_text_later(x+1, y+1, w, h, text, a)
    draw_text_shaded_text_later(x-1, y+1, w, h, text, a)
    draw_text_shaded_text_later(x-1, y-1, w, h, text, a)
    draw_text_shaded_text_later(x+1, y-1, w, h, text, a)
    self.font.color = save_color
    draw_text_shaded_text_later(x, y, w, h, text, a)
  end
  
end

#==============================================================================
# Window_Base
#==============================================================================

class Window_Base < Window

  def draw_actor_exp_alt(actor, x, y)
    self.contents.font.color = system_color
    self.contents.draw_text(x, y, 64, 32, 'next')
    self.contents.font.color = normal_color
    self.contents.draw_text(x + 56, y, 84, 32, actor.next_rest_exp_s, 2)
  end
  
  alias draw_actor_exp_alt_blizzart_hud_later draw_actor_exp_alt
  def draw_actor_exp_alt(actor, x, y, w = 148)
    w -= 12
    rate = (actor.next_exp != 0 ? actor.now_exp.to_f / actor.next_exp : 1)
    if rate < 0.5
      color1 = Color.new(20 * rate, 60, 80, 192)
      color2 = Color.new(60 * rate, 180, 240, 192)
    elsif rate >= 0.5
      color1 = Color.new(20 + 120 * (rate-0.5), 60 + 40 * (rate-0.5), 80, 192)
      color2 = Color.new(60 + 360 * (rate-0.5), 180 + 120 * (rate-0.5), 240, 192)
    end
    color3 = Color.new(80, 80, 80, 192)
    self.contents.gradient_bar(x, y, w, color1, color2, color3, rate)
    draw_actor_exp_alt_blizzart_hud_later(actor, x, y)
  end

  def draw_actor_hp_hud(actor, x, y, w = 148)
    rate = (actor.maxhp > 0 ? actor.hp.to_f / actor.maxhp : 0)
    if rate > 0.6
      color1 = Color.new(240 - 450 * (rate-0.6), 240, 150 * (rate-0.6), 192) 
    elsif rate > 0.2 && rate <= 0.6
      color1 = Color.new(240, 600 * (rate-0.2), 0, 192) 
    elsif rate <= 0.2
      color1 = Color.new(240, 0, 0, 192)
    end
    color2 = Color.new(0, 80, 0, 192)
    self.contents.gradient_bar_simple(x + 32, y, w - 48, color1, color2, rate)
    y -= 9
    self.contents.font.color = system_color
    self.contents.draw_text_full(x, y, 32, 32, $data_system.words.hp)
    hp_x = x + w - 122
    self.contents.font.color = actor.hp == 0 ? knockout_color :
      actor.hp <= actor.maxhp / 4 ? crisis_color : normal_color
    self.contents.draw_text_full(hp_x, y, 48, 32, actor.hp.to_s, 2)
    self.contents.font.color = normal_color
    self.contents.draw_text_full(hp_x + 48, y, 12, 32, '/', 1)
    self.contents.draw_text_full(hp_x + 60, y, 48, 32, actor.maxhp.to_s)
    self.contents.font.color.alpha = 255
  end
  
  def draw_actor_sp_hud(actor, x, y, w = 148)
    rate = (actor.maxsp > 0 ? actor.sp.to_f / actor.maxsp : 0)
    if rate > 0.4
      color1 = Color.new(180 - 200 * (rate-0.4), 60, 240, 192) 
    elsif rate <= 0.4
      color1 = Color.new(60 + 300 * rate, 150 * rate, 80 + 400 * rate, 192) 
    end
    color2 = Color.new(0, 0, 80, 192) 
    self.contents.gradient_bar_simple(x + 32, y, w - 48, color1, color2, rate)
    y -= 9
    self.contents.font.color = system_color
    self.contents.draw_text_full(x, y, 32, 32, $data_system.words.sp)
    sp_x = x + w - 122
    self.contents.font.color = actor.sp == 0 ? knockout_color :
      actor.sp <= actor.maxhp / 4 ? crisis_color : normal_color
    self.contents.draw_text_full(sp_x, y, 48, 32, actor.sp.to_s, 2)
    self.contents.font.color = normal_color
    self.contents.draw_text_full(sp_x + 48, y, 12, 32, '/', 1)
    self.contents.draw_text_full(sp_x + 60, y, 48, 32, actor.maxsp.to_s)
  end
  
  def draw_actor_exp_hud(actor, x, y, w = 148)
    rate = (actor.next_exp != 0 ? actor.now_exp.to_f / actor.next_exp : 1)
    if rate < 0.5
      color1 = Color.new(60 * rate, 180, 240, 192) 
    elsif rate >= 0.5
      color1 = Color.new(60 + 360 * (rate-0.5), 180 + 120 * (rate-0.5), 240, 192) 
    end
    color2 = Color.new(80, 80, 80, 192)
    self.contents.gradient_bar_simple(x + 32, y, w - 48, color1, color2, rate)
    y -= 9
    self.contents.font.color = system_color
    self.contents.draw_text_full(x, y, 80, 32, 'next')
    self.contents.font.color = normal_color
    self.contents.draw_text_full(x + 56, y, 84, 32, actor.next_rest_exp_s, 2)
    self.contents.font.color.alpha = 255
  end
  
end

#============================================================================== 
# Game_Actor 
#============================================================================== 

class Game_Actor < Game_Battler 
  
  def now_exp
    return @exp - @exp_list[@level] 
  end 
  
  def next_exp
    return @exp_list[@level+1] > 0 ? @exp_list[@level+1] - @exp_list[@level] : 0 
  end
  
end

#==============================================================================
# Hud
#==============================================================================

class Hud < Window_Base
  
  def initialize
    super(-12, -16, 192, 112)
    self.opacity = 0
    unless TOP
      self.y += 400
      self.y -= 16 unless SIMPLE
    end
    self.height += 32 unless SIMPLE
    self.z = 5000
    refresh
  end
  
  def refresh
    self.contents.clear if self.contents != nil
    self.width = FULL_DISPLAY ? 32 + 160 * $game_party.actors.size : 192
    self.contents = Bitmap.new(self.width - 32, self.height - 32)
    self.contents.font.name = 'Arial'
    self.contents.font.size = 16
    self.contents.font.bold = true
    @names, @levels, @hps, @sps, @exps = [], [], [], [], []
    for i in 0...$game_party.actors.size
      actor = $game_party.actors[(FULL_DISPLAY ? i : $game_system.index)]
      self.contents.font.italic = true
      self.contents.font.size += 2
      self.contents.font.color = system_color
      self.contents.draw_text(i*160, -8, 152, 32, actor.name, 1)
      self.contents.font.italic = false
      if SIMPLE
        self.contents.font.size -= 2
        draw_actor_hp_hud(actor, i*160, 16, 160)
        draw_actor_sp_hud(actor, i*160, 32, 160)
        draw_actor_exp_hud(actor, i*160, 48, 160)
      else
        draw_actor_hp(actor, i*160, 8, 160)
        draw_actor_sp(actor, i*160, 32, 160)
        draw_actor_exp_alt(actor, i*160, 56, 160)
        self.contents.font.size -= 2
      end
    end
    text = "#{$data_system.words.gold}: #{$game_party.gold}"
    self.contents.font.color = Color.new(255, 255, 0)
    self.contents.draw_text(0, (SIMPLE ? 56 : 84), 152, 32, text)
    for actor in $game_party.actors
      @names.push(actor.name)
      @levels.push(actor.level)
      @hps.push(actor.hp)
      @sps.push(actor.sp)
      @exps.push(actor.exp)
    end
    @gold = $game_party.gold
  end
  
  def test_changes
    return true if $game_party.gold != @gold
    if FULL_DISPLAY
      for i in 0...$game_party.actors.size
        actor = $game_party.actors[i]
        if actor.name != @names[i] || actor.level != @levels[i] ||
            actor.hp != @hps[i] || actor.sp != @sps[i]
          return true
        end
      end
    else
      actor = $game_party.actors[$game_system.index]
      if actor.name != @names[$game_system.index] ||
          actor.level != @levels[$game_system.index] ||
          actor.hp != @hps[$game_system.index] ||
          actor.sp != @sps[$game_system.index]
        return true
      end
    end
    return false
  end
  
end

#==============================================================================
# Scene_Map
#==============================================================================

class Scene_Map
  
  alias main_blizzart_hud_later main
  def main
    if $BlizzABS != true || BlizzABS::VERSION < 1.001
      @hud = Hud.new if $game_system.HUD
    end
    main_blizzart_hud_later
    @hud.dispose if @hud != nil
  end
  
  alias upd_blizzart_hud_later update
  def update
    if $BlizzABS != true || BlizzABS::VERSION < 1.001
      if $game_system.HUD
        @hud = Hud.new if @hud == nil
      else
        @hud.dispose if @hud != nil
        @hud = nil
      end
      if @hud != nil
        if Input.press?(Input::Z) && Input.trigger?(Input::L)
          $game_system.index += $game_party.actors.size - 1
          $game_system.index %= $game_party.actors.size
          @hud.refresh
        elsif Input.press?(Input::Z) && Input.trigger?(Input::R)
          $game_system.index += 1
          $game_system.index %= $game_party.actors.size
          @hud.refresh
        elsif @hud.test_changes
          @hud.refresh
        end
      end
    end
    upd_blizzart_hud_later
  end
  
end

#==============================================================================
# Screen Tremble by Blizzard
# Version: 1.0c
# Type: Game Experience Improvement
# Date: 22.1.2007
# Date v1.0b: 24.1.2007
# 
# 
# new in 1.0b:
#   - improved code and better method of shaking the screen apart
# 
# new in 1.0c:
#   - improved code and better method of shaking the screen apart
# 
# 
# Compatibility:
# 
#   98% compatible with SDK v1.x. 90% compatible with SDK v2.x. WILL corrupt
#   old savegames. Might glitch with exotic CBS-es or exotic Map modifications.
# 
# 
# Explanation:
#
#   This add-on will add an advanced feature of screen shaking:
#   Vertical shaking!
# 
# 
# Configuration:
# 
#   Change TREMBLE_SWITCH to a switch ID number. Turn this switch on to enable
#   vertical screen-shaking. You MUST have screen shaking turned on. This
#   add-on will not work if no screen shaking is activated at all. You can't
#   have only vertical screen shaking.
#==============================================================================

TREMBLE_SWITCH = 189

#==============================================================================
# Game_Screen
#==============================================================================

class Game_Screen
  
  attr_reader :tremble
  
  alias init_tremble_later initialize
  def initialize
    init_tremble_later
    @tremble = 0
    @tremble_power = 0
    @tremble_direction = 1
  end
  
  alias upd_tremble_later update
  def update
    upd_tremble_later
    if $game_system.TREMBLE && $game_switches[TREMBLE_SWITCH] &&
        (@shake_duration >= 1 || @tremble != 0)
      delta = (@tremble_power * (@shake_speed + 1) * @tremble_direction) / 10.0
      if @shake_duration <= 1 && @tremble * (@tremble + delta) < 0
        @tremble = 0
      else
        @tremble += delta
      end
      @tremble_direction = -1 if @tremble > @tremble_power * 1.5
      @tremble_direction = 1 if @tremble < -@tremble_power * 1.5
      @shake_duration -= 1 if @shake_duration >= 1
    end
  end

  alias start_tremble start_shake
  def start_shake(power, speed, duration)
    start_tremble(power, speed, duration)
    @tremble_power = power * 8 / 7 if $game_switches[TREMBLE_SWITCH]
  end
  
end

#==============================================================================
# Spriteset_Map
#==============================================================================

class Spriteset_Map
  
  alias upd_tremble_later update
  def update
    @viewport1.oy = ($game_switches[TREMBLE_SWITCH] ? $game_screen.tremble : 0)
    upd_tremble_later
  end

end

#==============================================================================
# Spriteset_Battle
#==============================================================================

class Spriteset_Battle
  
  alias upd_tremble_later update
  def update
    @viewport1.oy = ($game_switches[TREMBLE_SWITCH] ? $game_screen.tremble : 0)
    upd_tremble_later
  end

end

#==============================================================================
# Animation Stack by Blizzard
# Version: 1.0
# Type: Battle Graphic Improvement
# Date: 1.2.2007
# 
# This add-on will make the display of all status effect animations possible.
# 
# LOOPS - set this value to the number of how many time an animation should
#         loop before the next one is being displayed
#==============================================================================

LOOPS = 3

#==============================================================================
# Game_Battler
#==============================================================================

class Game_Battler
  
  alias init_anima_stack_later initialize
  def initialize
    init_anima_stack_later
    @anima_count = 0
    @anima_index = 0
  end
  
  alias state_animation_id_anima_stack_later state_animation_id
  def state_animation_id
    if $game_system.ANIMATION_STACK
      if @states.size == 0
        @anima_count = @anima_index = 0
        return 0
      end
      size = 0
      loop do
        @anima_index %= @states.size
        state = $data_states[@states[@anima_index]]
        break unless $data_animations[state.animation_id] == nil
        @anima_index += 1
        size += 1
        return 0 if size == @states.size
      end
      state = $data_states[@states[@anima_index]]
      if @anima_count > 2*LOOPS*$data_animations[state.animation_id].frame_max
        @anima_count = 0
        @anima_index += 1
      else
        @anima_count += 1
      end
      return state.animation_id
    end
    return state_animation_id_anima_stack_later
  end
  
end

#==============================================================================
# Simple Facesets by Blizzard
# Version: 1.01b
# Type: Menu Graphic Alteration
# Date: 18.2.2007
# 
# 
# Explanation:
# 
#   This litte add-on will change the spritesets in the main menu to facesets
#   or any other pictures you might be using. Name the pictures exactly like
#   the spritesets and add _face to their name. Put them into the "Characters"
#   folder. Size is not fixed, the script will put it into the correct place,
#   it's up to you to find the right size.
# 
# Note:
# 
#   This might not be compatible with exotic CMS-es.
#==============================================================================

FACE_HUE = false # set it to true to apply the same hue as the spriteset

#==============================================================================
# Window_Base
#==============================================================================

class Window_Base < Window
  
  alias draw_actor_graphic_faces_later draw_actor_graphic
  def draw_actor_graphic(actor, x, y)
    if $game_system.FACESETS && self.is_a?(Window_MenuStatus)
      if actor != nil && actor.character_name != ''
        draw_actor_face(actor, x, y)
      end
    else
      draw_actor_graphic_faces_later(actor, x, y)
    end
  end
  
  def draw_actor_face(actor, x, y)
    hue = (FACE_HUE ? actor.character_hue : 0)
    bitmap = RPG::Cache.character("#{actor.character_name}_face", hue)
    src_rect = Rect.new(0, 0, bitmap.width, bitmap.height)
    self.contents.blt(x-bitmap.width/2, y-bitmap.height/2, bitmap, src_rect)
  end

end

#==============================================================================
# Caterpillar by Blizzard
# Version: 2.0b
# Type: Game Experience Improvement
# Date: 7.3.2007
# Date v1.01b: 7.3.2007
# Date v2.0: 7.8.2007
# Date v2.0b: 8.8.2007
# 
# 
# new in 1.01b:
#   - now events can't go through your party members anymore
# 
# new in 2.0:
#   - completely overworked and improved
# 
# new in 2.0b:
#   - improved coding and made it work more convenient
#   - fixed a few glitches
#   - added DEAD_DISPLAY option
# 
# 
# Compatibility:
# 
#   93% compatible with SDK v1.x. 60% compatible with SDK v2.x. You might
#   experience problems with pixel movement scripts or map graphic manipulating
#   scripts. Blizz-ABS disables this add-on automatically and uses the
#   Blizz-ABS Caterpillar system.
# 
# 
# Features:
# 
#   - your party members follow you on the map
#   - less code than other caterpillar scripts
#   - use $game_player.update_buffer('reset') if you need all party members to
#     gather around the player
#==============================================================================

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# max number of party members
MAX_PARTY = 4
# actor IDs where the actor is animated even when not walking
ANIMATED_IDS = []
# 0 - shows all characters; 1 - shows "ghosts"; 2 - removes from caterpillar
DEAD_DISPLAY = 0

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#==============================================================================
# Game_Character
#==============================================================================
    
class Game_Character
  
  alias passable_caterpillar_later? passable?
  def passable?(x, y, d)
    result = passable_caterpillar_later?(x, y, d)
    return result if $BlizzABS && BlizzABS::VERSION >= 1.001
    return result if self.is_a?(Game_Player) || self.is_a?(Game_Member)
    new_x = x + (d == 6 ? 1 : d == 4 ? -1 : 0)
    new_y = y + (d == 2 ? 1 : d == 8 ? -1 : 0)
    for member in $game_player.members
      if member.character_name != '' && member.x == new_x && member.y == new_y
        return false
      end
    end
    return result 
  end
  
end

#==============================================================================
# Game_Player
#==============================================================================
    
class Game_Player < Game_Character
  
  attr_reader :members
  attr_reader :move_speed
  
  alias init_caterpillar_later initialize
  def initialize
    init_caterpillar_later
    @members = []
    1.upto(MAX_PARTY-1) {|i| @members.push(Game_Member.new(i))}
  end
  
  alias upd_caterpillar_later update
  def update
    upd_caterpillar_later
    refresh if DEAD_DISPLAY > 0
    @members.each {|member| member.update}
    @step_anime = (ANIMATED_IDS.include?(actor.id))
  end
  
  alias straighten_caterpillar_later straighten
  def straighten
    straighten_caterpillar_later
    @members.each {|member| member.straighten}
  end
  
  alias refresh_caterpillar refresh
  def refresh
    act = $game_party.actors[0]
    $game_party.actors[0] = actor
    refresh_caterpillar
    $game_party.actors[0] = act
    if actor.dead? && DEAD_DISPLAY == 1
      @opacity = Graphics.frame_count % 2 * 255
      @blend_type = 1
    end
  end
  
  def actor
    if DEAD_DISPLAY > 0
      for actor in $game_party.actors
        return actor unless actor.dead?
      end
    end
    return $game_party.actors[0]
  end
  
  def update_buffer(next_move)
    if next_move == nil
      @members.each {|member| member.buffer = []}
    else 
      @members.each {|member| member.update_buffer(
          next_move == 'reset' ? nil : next_move)}
    end
  end
  
  alias move_down_caterpillar_later move_down
  def move_down(turn_enabled = true)
    update_buffer(2) if passable?(@x, @y, 2)
    move_down_caterpillar_later
  end
  
  alias move_left_caterpillar_later move_left
  def move_left(turn_enabled = true)
    update_buffer(4) if passable?(@x, @y, 4)
    move_left_caterpillar_later
  end
  
  alias move_right_caterpillar_later move_right
  def move_right(turn_enabled = true)
    update_buffer(6) if passable?(@x, @y, 6)
    move_right_caterpillar_later
  end
  
  alias move_up_caterpillar_later move_up
  def move_up(turn_enabled = true)
    update_buffer(8) if passable?(@x, @y, 8)
    move_up_caterpillar_later
  end
  
  alias move_lower_left_caterpillar_later move_lower_left
  def move_lower_left
    if passable?(@x, @y, 2) && passable?(@x, @y + 1, 4) ||
       passable?(@x, @y, 4) && passable?(@x - 1, @y, 2)
      update_buffer(1)
    end
    move_lower_left_caterpillar_later
  end
  
  alias move_lower_right_caterpillar_later move_lower_right
  def move_lower_right
    if passable?(@x, @y, 2) && passable?(@x, @y + 1, 6) ||
       passable?(@x, @y, 6) && passable?(@x + 1, @y, 2)
      update_buffer(3)
    end
    move_lower_right_caterpillar_later
  end
  
  alias move_upper_left_caterpillar_later move_upper_left
  def move_upper_left
    if passable?(@x, @y, 8) && passable?(@x, @y - 1, 4) ||
       passable?(@x, @y, 4) && passable?(@x - 1, @y, 8)
      update_buffer(7)
    end
    move_upper_left_caterpillar_later
  end
  
  alias move_upper_right_caterpillar_later move_upper_right
  def move_upper_right
    if passable?(@x, @y, 8) && passable?(@x, @y - 1, 6) ||
       passable?(@x, @y, 6) && passable?(@x + 1, @y, 8)
      update_buffer(9)
    end
    move_upper_right_caterpillar_later
  end
  
  alias jump_caterpillar_later jump
  def jump(x_plus, y_plus)
    if (x_plus != 0 || y_plus != 0) && passable?(@x + x_plus, @y + y_plus, 0)
      update_buffer([x_plus, y_plus])
    end
    jump_caterpillar_later(x_plus, y_plus)
  end
  
  alias moveto_caterpillar moveto
  def moveto(x, y)
    update_buffer(nil)
    moveto_caterpillar(x, y)
    for member in @members
      member.moveto(x, y)
      case @direction
      when 2 then member.turn_down
      when 4 then member.turn_left
      when 6 then member.turn_right
      when 8 then member.turn_up
      end
    end
  end
  
end
  
#==============================================================================
# Game_Member
#==============================================================================

class Game_Member < Game_Character
  
  attr_accessor :buffer
  
  def initialize(index)
    super()
    @index = index
    @force_movement = 0
    @buffer = []
    @through = true
  end
  
  def refresh
    unless $game_system.CATERPILLAR && actor != nil
      @character_name = ''
      @character_hue = 0
      return
    end
    @character_name = actor.character_name
    @character_hue = actor.character_hue
    if actor.dead? && DEAD_DISPLAY == 1
      @opacity = Graphics.frame_count % 2 * 255
      @blend_type = 1
    else
      @opacity = 255
      @blend_type = 0
    end
  end
  
  def actor
    case DEAD_DISPLAY
    when 0
      return $game_party.actors[@index]
    when 1
      alive = 0
      $game_party.actors.each {|actor| alive += 1 unless actor.dead?}
      if @index >= alive
        ind = @index - alive
        for i in 0...$game_party.actors.size
          ind -= 1 if $game_party.actors[i].dead?
          return $game_party.actors[i] if ind < 0
        end
      else
        ind = @index
        for i in 0...$game_party.actors.size
          ind -= 1 unless $game_party.actors[i].dead?
          return $game_party.actors[i] if ind < 0
        end
      end
      return nil
    when 2
      ind = @index
      for i in 0...$game_party.actors.size
        ind -= 1 unless $game_party.actors[i].dead?
        return $game_party.actors[i] if ind < 0
      end
    end
    return nil
  end
  
  def update
    refresh
    @transparent = $game_player.transparent
    @move_speed = $game_player.move_speed
    unless moving? || @buffer.size <= @index && @force_movement <= 0
      if @buffer.size > 0
        move = @buffer.shift
        if move.is_a?(Array)
          jump(move[0], move[1])
        else
          case move
          when 1 then move_lower_left
          when 2 then move_down(true)
          when 3 then move_lower_right
          when 4 then move_left(true)
          when 6 then move_right(true)
          when 7 then move_upper_left
          when 8 then move_up(true)
          when 9 then move_upper_right
          end
        end
        @force_movement -= 1 if @force_movement > 0
      end
    end
    super
    @step_anime = (ANIMATED_IDS.include?($game_party.actors[@index].id))
  end
  
  def update_buffer(next_move)
    if next_move == nil
      @force_movement = @buffer.size
    else
      @buffer.push(next_move)
      @force_movement = @buffer.size if next_move.is_a?(Array)
    end
  end
  
  def check_event_trigger_touch(x, y) # don't remove this, it's necessary...
  end
  
  def screen_z(height = 0)
    return (super - @index)
  end
  
end

#==============================================================================
# Spriteset_Map
#==============================================================================

class Spriteset_Map
  
  alias init_caterpillar_later initialize
  def initialize
    init_caterpillar_later
    return if $BlizzABS && BlizzABS::VERSION >= 1.001
    for member in $game_player.members
      sprite = Sprite_Character.new(@viewport1, member)
      sprite.update
      @character_sprites.push(sprite)
    end
  end
  
end

#==============================================================================
# Scene_Map
#==============================================================================

class Scene_Map
  
  alias transfer_player_caterpillar_later transfer_player
  def transfer_player
    transfer_player_caterpillar_later
    return if $BlizzABS
    case $game_temp.player_new_direction
    when 2 then $game_player.members.each {|member| member.turn_down}
    when 4 then $game_player.members.each {|member| member.turn_left}
    when 6 then $game_player.members.each {|member| member.turn_right}
    when 8 then $game_player.members.each {|member| member.turn_up}
    end
  end
  
end

#==============================================================================
# Arrow over Player by Blizzard
# Version: 1.01b
# Type: Game Playability Improvement
# Date: 7.3.2007
# Date v1.01b: 30.7.2007
# 
# 
# new in 1.01b:
#   - shows arrow if tile has higher priority AND isn't completely transparent
#   - slightly faster arrow drawing due to half-optimized code
# 
# Explanation:
# 
#   This add-on will show an arrow over the player's head if he's behind a tile
#   with a higher priority that isn't completely transparent.
#==============================================================================

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

INNER_COLOR = Color.new(0, 0, 0, 128)
OUTER_COLOR = Color.new(255, 255, 255, 192)

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#==============================================================================
# Spriteset_Map
#==============================================================================

class Spriteset_Map
  
  alias init_arrow_over_player_later initialize
  def initialize
    if $game_system.ARROW_OVER_PLAYER
      @arrow = Sprite.new
      @arrow.bitmap = Bitmap.new(16, 9)
      @arrow.bitmap.fill_rect(1, 0, 14, 1, OUTER_COLOR)
      @arrow.bitmap.set_pixel(0, 1, OUTER_COLOR)
      @arrow.bitmap.fill_rect(1, 1, 7, 1, INNER_COLOR)
      @arrow.bitmap.fill_rect(8, 1, 7, 1, INNER_COLOR)
      @arrow.bitmap.set_pixel(15, 1, OUTER_COLOR)
      @arrow.bitmap.set_pixel(1, 2, OUTER_COLOR)
      @arrow.bitmap.fill_rect(2, 2, 6, 1, INNER_COLOR)
      @arrow.bitmap.fill_rect(8, 2, 6, 1, INNER_COLOR)
      @arrow.bitmap.set_pixel(14, 2, OUTER_COLOR)
      @arrow.bitmap.set_pixel(2, 3, OUTER_COLOR)
      @arrow.bitmap.fill_rect(3, 3, 5, 1, INNER_COLOR)
      @arrow.bitmap.fill_rect(8, 3, 5, 1, INNER_COLOR)
      @arrow.bitmap.set_pixel(13, 3, OUTER_COLOR)
      @arrow.bitmap.set_pixel(3, 4, OUTER_COLOR)
      @arrow.bitmap.fill_rect(4, 4, 4, 1, INNER_COLOR)
      @arrow.bitmap.fill_rect(8, 4, 4, 1, INNER_COLOR)
      @arrow.bitmap.set_pixel(12, 4, OUTER_COLOR)
      @arrow.bitmap.set_pixel(4, 5, OUTER_COLOR)
      @arrow.bitmap.fill_rect(5, 5, 3, 1, INNER_COLOR)
      @arrow.bitmap.fill_rect(8, 5, 3, 1, INNER_COLOR)
      @arrow.bitmap.set_pixel(11, 5, OUTER_COLOR)
      @arrow.bitmap.set_pixel(5, 6, OUTER_COLOR)
      @arrow.bitmap.fill_rect(6, 6, 2, 1, INNER_COLOR)
      @arrow.bitmap.fill_rect(8, 6, 2, 1, INNER_COLOR)
      @arrow.bitmap.set_pixel(10, 6, OUTER_COLOR)
      @arrow.bitmap.set_pixel(6, 7, OUTER_COLOR)
      @arrow.bitmap.set_pixel(7, 7, INNER_COLOR)
      @arrow.bitmap.set_pixel(8, 7, INNER_COLOR)
      @arrow.bitmap.set_pixel(9, 7, OUTER_COLOR)
      @arrow.bitmap.fill_rect(7, 8, 2, 1, OUTER_COLOR)
      @arrow.visible = false
      @arrow.z = 5000
      @arrow.ox = 8
      @arrow_mode = true
    end
    init_arrow_over_player_later
  end
  
  alias upd_arrow_over_player_later update
  def update
    upd_arrow_over_player_later
    if $game_system.ARROW_OVER_PLAYER
      @arrow.x = $game_player.screen_x
      @arrow.y = $game_player.screen_y - 56
      @arrow.visible = false
      for n in 0..2
        tile_id = $game_map.data[$game_player.x, $game_player.y-1, n]
        if tile_id != nil && tile_id != 0 && $game_map.priorities[tile_id] > 1
          tile = RPG::Cache.tile($game_map.tileset_name, tile_id, 0)
          if tile_id < 384
            @arrow.visible = true
          else
            for i in 0...32
              for j in 0...32
                unless tile.get_pixel(i, j).alpha == 0
                  @arrow.visible = true
                  break
                end
              end
            end
          end
        end
      end
      if @arrow_mode
        @arrow.oy += 1
        @arrow_mode = (@arrow.oy < 4)
      else
        @arrow.oy -= 1
        @arrow_mode = (@arrow.oy <= -4)
      end
    end
  end
  
  alias disp_arrow_over_player_later dispose
  def dispose
    disp_arrow_over_player_later
    @arrow.dispose if $game_system.ARROW_OVER_PLAYER
  end
  
end

#==============================================================================
# Animated Battle Background by Blizzard
# Version: 1.1b
# Type: Game Graphic Design Improvement
# Date: 12.3.2007
# Date v1.1b: 12.8.2007
# 
# new in 1.1b
#   - shorter code, increased performance and increased compatiblity
# 
# 
# Explanation:
# 
#   This will animate battle backgrounds. To animate them, you MUST HAVE the
#   appropriate picture files. You can name them however you like, but you need
#   to give them numbers. Every other frame than the first has to have a number
#   higher than the one before. If one number is skipped, the animation will
#   loop until it reaches the highest number available before the skipped
#   number.
# 
# Examples:
# 
#   1)
#   Temple.png
#   Temple1.png
#   Temple2.png
#   Temple3.png
#   - all frames will be shown
# 
#   2)
#   Temple.png
#   Temple1.png
#   Temple3.png
#   Temple4.png
#   - only the 1st and 2nd frame will be shown
# 
#   3)
#   Temple.png
#   Temple3.png
#   Temple4.png
#   Temple5.png
#   - no animation at all
#==============================================================================

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# how many REAL frames that should be skipped before updating the background,
# note that using anything below 8 is not recommended and that using low values
# can increase lag dramatically
SPEED = 8

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#==============================================================================
# Spriteset_Battle
#==============================================================================

class Spriteset_Battle
  
  alias init_animated_battle_background_later initialize
  def initialize
    if $game_system.ANIMATED_BATTLE_BACKGROUND &&
        !$game_system.MAP_AS_BATTLEBACK
      setup_battleback
    end
    init_animated_battle_background_later
  end
  
  alias upd_animated_battle_background_later update
  def update
    if $game_system.ANIMATED_BATTLE_BACKGROUND &&
        !$game_system.MAP_AS_BATTLEBACK
      setup_battleback if @origin_name != $game_temp.battleback_name
      @frame = (@frame + 1) % @max_frame if Graphics.frame_count % SPEED == 0
      $game_temp.battleback_name = @origin_name + (@frame > 0 ? @frame.to_s : '')
      upd_animated_battle_background_later
      $game_temp.battleback_name = @origin_name
    else
      upd_animated_battle_background_later
    end
  end
  
  def setup_battleback
    @origin_name = $game_temp.battleback_name
    @frame = 0
    @max_frame = 1
    loop do
      name = @origin_name + @max_frame.to_s
      if FileTest.exist?("Graphics/Battlebacks/#{name}.jpg") ||
         FileTest.exist?("Graphics/Battlebacks/#{name}.png")
        @max_frame += 1
      else
        break
      end
    end
  end

end

#==============================================================================
# Map as Battleback by Blizzard
# Version: 1.5b
# Type: Game Design Alteration
# Date: 11.3.2007
# Date v1.5b: 12.8.2007
# 
# 
# new in 1.5b:
#   - shortened code and increased performance
# 
# Explanation:
# 
#   This will make the map to be the battle background. Note that this add-on
#   will automatically turn off Animated Battle Backgrounds.
#==============================================================================

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# include any class definitions which you don't want to see on the background
REMOVE_CLASSES = [Game_Player, Game_Member]

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#==============================================================================
# Spriteset_Map
#==============================================================================

class Spriteset_Map

  def delete_characters
    for i in 0...@character_sprites.size
      if REMOVE_CLASSES.include?(@character_sprites[i].character.class)
        @character_sprites[i].dispose
        @character_sprites[i] = nil
      end
    end
    @character_sprites.compact!
  end
  
end

#==============================================================================
# Spriteset_Battle
#==============================================================================

class Spriteset_Battle
  
  alias init_map_as_battleback_later initialize
  def initialize
    if $game_system.MAP_AS_BATTLEBACK
      @map_battleback = Spriteset_Map.new
      @map_battleback.delete_characters if REMOVE_CLASSES.size > 0
      init_map_as_battleback_later
      @battleback_sprite.dispose
      @battleback_sprite = nil
    else
      init_map_as_battleback_later
    end
  end
  
  alias disp_map_as_battleback_later dispose
  def dispose
    @battleback_sprite = Sprite.new if @battleback_sprite == nil
    @map_battleback.dispose if @map_battleback != nil
    disp_map_as_battleback_later
  end
  
end

#==============================================================================
# Facesets for Default Status Screen (DSS) by Zan
# Version: 1.01
# Type: Menu Layout Alteration
# Date: 2.4.2007
# 
# This works just like Simple Facesets, except it applies to the status screen.
# In case you didn't look at that section, here are the incredibly complicated
# rules:
# Ready?
# You have to have pictures in your "Characters" folder for each of your
# characters. The pictures have to have the same name as the character's
# spriteset, with "_face" added on. That's it.
# 
# Note:
# This script is currently set for *my* pictures, which are 108x108 pixels. To
# change it around for different-sized pictures, change the value of FACE_X and
# FACE_Y in the Config settings.
# 
# Another note:
# Not compatible with any CMS that changes drastically the status scene or does
# not use the default status window.
#==============================================================================
 
#==============================================================================
# Config
#==============================================================================

FACE_X = 15 # set the x coordinate offset (higher value -> righter position)
FACE_Y = -30 # set the y coordinate offset (higher value -> lower position)
 
FACE_HUE = false # set it to true to apply the same hue as the spriteset
 
#==============================================================================
# Window_Base
#==============================================================================
 
class Window_Status < Window_Base
  
  alias draw_actor_graphic_faces_when draw_actor_graphic
  def draw_actor_graphic(actor, x, y)
    if $game_system.FACESETS_DSS && self.is_a?(Window_Status)
      if actor != nil && actor.character_name != ''
        draw_actor_face(actor, x, y)
      end
    else
      draw_actor_graphic_faces_when(actor, x, y)
    end
  end
  
  def draw_actor_face(actor, x, y)
    hue = (FACE_HUE ? actor.character_hue : 0)
    bitmap = RPG::Cache.character("#{actor.character_name}_face", hue)
    src_rect = Rect.new(0, 0, bitmap.width, bitmap.height)
    self.contents.blt((x-bitmap.width/2)+FACE_X, (y-bitmap.height/2)+FACE_Y,
        bitmap, src_rect)
  end
 
end

#==============================================================================
# Status Effects as Icons by Blizzard
# Version: 1.0
# Type: Game Design Improvement
# Date: 30.4.2007
# 
# 
#   This add-on will modify your game so no status text is displayed, but icons
#   instead. Note that you need to use default icon size of 24x24. Import the
#   icons into the default icon folder and name them like the status effects
#   with "stat_" before and type everything in lowcase.
#   In SPECIAL_EFFECTS include all the IDs from status effects that will
#   override the usual icon display and force the display of their name in the
#   default way of displaying.
# 
# Example:
# 
#   status effect name: "Painful Distortion"
#   icon file name:     "stat_painful distortion.png"
#==============================================================================
 
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

SPECIAL_EFFECTS = []

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
 
#==============================================================================
# Window_Base
#==============================================================================
 
class Window_Base < Window
  
  alias draw_actor_state_icons_later draw_actor_state
  def draw_actor_state(actor, x, y, width = 120)
    if $game_system.STATUS_ICONS
      if actor != nil
        for state in actor.states
          if SPECIAL_EFFECTS.include?(state)
            text = "[#{$data_states[state].name}]"
            self.contents.font.color = actor.dead? ? knockout_color : normal_color
            self.contents.draw_text(x, y, width, 32, text)
            return
          end
        end
        for i in 0...actor.states.size
          w = i * 28
          break if w > width
          icon = RPG::Cache.icon("stat_#{$data_states[actor.states[i]].name.downcase}")
          self.contents.blt(x + 2 + w, y + 4, icon, Rect.new(0, 0, 24, 24))
        end
      end
    else
      draw_actor_state_icons_later(actor, x, y, width)
    end
  end
  
end

#==============================================================================
# Window_Help
#==============================================================================
 
class Window_Help < Window_Base
  
  alias set_enemy_state_icons_later set_enemy
  def set_enemy(enemy)
    if !$game_system.STATUS_ICONS || $game_system.ENEMY_STATUS
      set_enemy_state_icons_later(enemy)
      return
    end
    text = enemy.name
    if enemy.states.size > 0
      w = self.contents.text_size(text).width
      if enemy.states.size * 28 + w > self.contents.width
        width = self.contents.width/self.contents.text_size(' ').width
      else
        width = enemy.states.size*28/self.contents.text_size(' ').width
      end
      for i in 0...width
        text += " "
      end
      if @text != text || @align != 1
        for state in enemy.states
          if SPECIAL_EFFECTS.include?(state)
            text = "#{enemy.name}  [#{$data_states[state].name}]"
            set_text(text, 1)
            return
          end
        end
        set_text(text, 1)
        x = self.contents.width/2 - w/2
        for i in 0...enemy.states.size
          w = i * 28
          break if x + 2 + w > self.contents.width
          icon = RPG::Cache.icon("stat_#{$data_states[enemy.states[i]].name.downcase}")
          self.contents.blt(x + 2 + w, 4, icon, Rect.new(0, 0, 24, 24))
        end
      end
    else
      set_text(text, 1)
    end
  end

end

#==============================================================================
# Animated Battlers for Non-Action BS by Blizzard
# Version: 1.3b
# Type: Battle Graphic Improvement
# Date: 5.5.2007
# Date v1.3b: 13.8.2007
# 
# 
# new in 1.3b:
#   - fixed the flicking glitch that appeared when a battler was dying
#   - improved coding, now executed over Sprite_Battler instead of
#     Spriteset_Battle and due to that increased compatibility and shorter code
# 
# 
# Compatibility:
# 
#   95% compatible with SDK v1.x. 70% compatible with SDK v2.x. Not compatible
#   exotic action CBS-es that need special battler animation.
# 
# 
# Explanation:
# 
#   This will animate battlers in the default battle system. To animate them,
#   you MUST HAVE the appropriate picture files. You can name them however you
#   like, but you need to give them numbers. Every other frame than the first
#   has to have a number higher than the one before. If one number is skipped,
#   the animation will loop until it reaches the highest number available
#   before the skipped number. Not that this works for actors AND for enemies.
# 
# Examples:
# 
#   1)
#   Arshes.png
#   Arshes1.png
#   Arshes2.png
#   Arshes3.png
#   - all frames will be shown
# 
#   2)
#   Arshes.png
#   Arshes1.png
#   Arshes3.png
#   Arshes4.png
#   - only the 1st and 2nd frame will be shown
# 
#   3)
#   Arshes.png
#   Arshes3.png
#   Arshes4.png
#   Arshes5.png
#   - no animation at all
#==============================================================================

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# how many REAL frames that should be skipped before updating the battlers,
# note that using anything below 2 is not recommended and that using low values
# can increase lag dramatically
B_SPEED = 4

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#==============================================================================
# Game_Battler
#==============================================================================

class Game_Battler
  
  attr_accessor :frame
  attr_accessor :max_frame
  attr_accessor :origin_name
  attr_accessor :battler_name
  
end

#==============================================================================
# Sprite_Battler
#==============================================================================

class Sprite_Battler < RPG::Sprite
  
  alias upd_animated_battlers_dbs_later update
  def update
    if $game_system.ANIMATED_BATTLERS_NON_ACTION_BS && @battler != nil
      setup_battler if @battler.origin_name != @battler.battler_name
      if Graphics.frame_count % B_SPEED == 0
        @battler.frame = (@battler.frame + 1) % @battler.max_frame
      end
      if @frame != @battler.frame
        @frame = @battler.frame
        name = @battler.origin_name
        name += @frame.to_s if @frame > 0
        self.bitmap = RPG::Cache.battler(name, @battler.battler_hue)
        @width = bitmap.width
        @height = bitmap.height
        self.ox = @width / 2
        self.oy = @height
      end
    end
    upd_animated_battlers_dbs_later
  end
  
  def setup_battler
    @battler.origin_name = @battler.battler_name
    @battler.frame = @frame = 0
    @battler.max_frame = 1
    loop do
      name = @battler.origin_name + @battler.max_frame.to_s
      if FileTest.exist?("Graphics/Battlers/#{name}.jpg") ||
         FileTest.exist?("Graphics/Battlers/#{name}.png")
        @battler.max_frame += 1
      else
        break
      end
    end
  end
  
end

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                                                                             #
#                   #   # #####  #  #      #  ##### #   #                     #
#                   #   #   #    #  #      #    #    # #                      #
#                   #   #   #    #  #      #    #     #                       #
#                   #   #   #    #  #      #    #     #                       #
#                    ###    #    #  #####  #    #     #                       #
#                                                                             #
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

#==============================================================================
# FPS Modulator by Blizzard
# Version: 1.0b
# Type: Debug Utility
# Date: 12.2.2006
# 
#   Holding SHIFT and pressing Q/W will allow you to speed up the game like in
#   an emulator up to 3 times (sorry, RMXP doesn't allow more). Remove the
#   triple commented lines (###) to allow this feature even in the normal game,
#   not only the Debug mode.
#==============================================================================

#==============================================================================
# Scene_Map
#==============================================================================

class Scene_Map
  
  alias update_fps_later update
  def update
    if $game_system.FPS_MODULATOR
      if $DEBUG ### 
        if Input.press?(Input::A) && Input.press?(Input::R)
          Graphics.frame_rate += 40
          return
        elsif Input.press?(Input::A) && Input.trigger?(Input::L)
          Graphics.frame_rate -= 40 unless Graphics.frame_rate == 40
          return
        end
      end ###
    end
    update_fps_later
  end

end

#==============================================================================
# Speed Modulator by Blizzard
# Version: 1.01b
# Type: Debug Utility
# Date: 12.2.2006
# Date v1.01: 12.1.2007
# 
#   Pressing Q/W will allow you to speed up the main character. Pressing SHIFT
#   will reset his speed immediately. Remove the triple commented lines (###)
#   to allow this feature even in the normal game, not only the Debug mode.
#==============================================================================

#==============================================================================
# Game_Player
#==============================================================================

class Game_Player
  
  alias upd_speed_later update
  def update
    if $game_system.SPEED_MODULATOR
      if $DEBUG ###
        if Input.trigger?(Input::A)
          @move_speed = 4
          return
        elsif !Input.press?(Input::A) && !Input.press?(Input::X) &&
            Input.trigger?(Input::R)
          @move_speed += 1 unless @move_speed == 6
          return
        elsif !Input.press?(Input::A) && !Input.press?(Input::X) &&
            Input.trigger?(Input::L)
          @move_speed -= 1 unless @move_speed == 1
          return
        end
      end ###
    end
    upd_speed_later
  end
  
end

#==============================================================================
# FullScreen? by Blizzard
# Version: 1.22b
# Type: Game Experience Improvement
# Date: 14.11.2006
# Date v1.22b: 8.7.2006
# 
# new in v1.21b:
#   - better code, easier to use
# 
# new in v1.22b:
#   - fixes a conflict with SDK v2.2
#==============================================================================

#==============================================================================
# Window_Command
#==============================================================================

class Window_FullScreen < Window_Selectable

  def initialize(width, commands)
    super(0, 0, width, commands.size * 32 + 64)
    @item_max = commands.size
    @commands = commands
    self.contents = Bitmap.new(width - 32, @item_max * 32 + 32)
    if $fontface != nil
      self.contents.font.name = $fontface
      self.contents.font.size = $fontsize
    elsif $defaultfonttype != nil
      self.contents.font.name = $defaultfonttype
      self.contents.font.size = $defaultfontsize
    end
    refresh
    self.index = 0
  end

  def refresh
    self.contents.clear
    qu = 'Switch to fullscreen?'
    self.contents.draw_text(0, 0, width - 32, 32, qu, 1)
    for i in 0...@item_max
      draw_item(i, normal_color)
    end
  end

  def draw_item(index, color)
    rect = Rect.new(4, 32+32 * index, self.contents.width - 8, 32)
    rect2 = Rect.new(4+1, 32+32 * index+1, self.contents.width - 8, 32)
    self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
    self.contents.font.color = color
    self.contents.draw_text(rect, @commands[index], 1)
  end
  
  def update_cursor_rect
    if @index < 0
      self.cursor_rect.empty
      return
    end
    row = @index / @column_max
    self.top_row = row if row < self.top_row
    if row > self.top_row + (self.page_row_max - 1)
      self.top_row = row - (self.page_row_max - 1)
    end
    cursor_width = 64
    x = (self.contents.width - cursor_width) / 2
    y = @index / @column_max * 32 - self.oy
    self.cursor_rect.set(x, y + 32, cursor_width, 32)
  end

end
  
#==============================================================================
# Scene_Title
#==============================================================================

class Scene_Title
  
  alias main_fullscreen? main
  def main
    if TONS_OF_ADDONS::FULLSCREEN
      unless $game_started 
        Graphics.freeze
        $data_system = ARC::Data.load('Data/System.arc')
        $game_system = Game_System.new
        @window = Window_FullScreen.new(320, ['Yes' ,'No'])
        @window.x = 320 - @window.width / 2
        @window.y = 240 - @window.height / 2
        @window.opacity = 0
        Graphics.transition(10)
        loop do
          Graphics.update
          Input.update
          @window.update
          update_window
          break if $game_started
        end
        Graphics.freeze
        @window.dispose
        @window = nil
        Graphics.transition(10)
        Graphics.freeze
      end
    else
      $game_started = true
    end
    main_fullscreen?
  end
  
  def update_window
    if Input.trigger?(Input::C)
      if @window.index == 0
        $game_system.se_play($data_system.decision_se)
        keybd = Win32API.new 'user32.dll', 'keybd_event', ['i', 'i', 'l', 'l'], 'v'
        keybd.call 0xA4, 0, 0, 0
        keybd.call 13, 0, 0, 0
        keybd.call 13, 0, 2, 0
        keybd.call 0xA4, 0, 2, 0
      else
        $game_system.se_play($data_system.cancel_se)
      end
      $game_started = true
    elsif Input.trigger?(Input::B)
      $game_system.se_play($data_system.cancel_se)
      $game_started = true
    end
  end

end

#==============================================================================
# Death Toll by Blizzard
# Version: 1.3b
# Type: Playing Statistics Addition
# Date: 10.10.2006
# Date v1.2b: 6.12.2006
# Date v1.3b: 31.7.2007
# 
# 
# Instructions:
# 
#   Set ID to the variable ID you want to use to store the number of killed
#   enemies. To show the number just use in a message \v[X] where X is the same
#   number as you set ID.
# 
# new in 1.2b:
#   Counts now actor deaths, too. The numbers are stored in the variables with
#   the ID "DT_ID + actor's ID", so i.e. for DT_ID = 26, variable number 26
#   will contain killed enemies, number 27 will contain the deaths of actor
#   with ID 1, number 28 will contain the deaths of actor with ID 2, etc.
# 
# new in 1.3b:
#   Fixed a possible conflict with Chaos Rage Limit System.
#==============================================================================

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

DT_ID = 26 # variable ID

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#==============================================================================
# Scene_Battle
#==============================================================================

class Scene_Battle

  alias main_dt_later main
  def main
    @td_flag = 0
    main_dt_later
  end
  
  alias upd_dt_later update
  def update
    @td_flag = $game_troop.enemies.size if @td_flag == 0
    upd_dt_later
  end
  
  alias battle_end_td_later battle_end
  def battle_end(result)
    battle_end_td_later(result)
    if $game_system.DEATH_TOLL
      count = 0
      for enemy in $game_troop.enemies
        count += 1 unless enemy.exist? || enemy.hidden
      end
      $game_variables[DT_ID] += @td_flag - count
    end
  end

end

#==============================================================================
# Game_Actor
#==============================================================================

class Game_Battler
  
  alias hp_is_equal_to_td_later hp=
  def hp=(val)
    hp_is_equal_to_td_later(val)
    if val <= 0 && $game_system.DEATH_TOLL && self.is_a?(Game_Actor)
      $game_variables[DT_ID + self.id] += 1
    end
  end
  
end
    
#==============================================================================
# Window_BattleResult Add-on by Blizzard
# Version: 1.1b
# Type: Game Playability Improvement
# Date: 27.8.2006
# Date v1.1b: 11.3.2007
# 
# 
# new in 1.1b:
#   - now fully compatible with Easy LvlUp Notifier 1.3b and higher
# 
# 
# Compatibility:
# 
#   99% compatible with SDK v1.x. 60% compatible with SDK v2.x. 99% chance of
#   full compatibility with everything else.
# 
# 
# Features:
# 
#   - instead of displaying each item seperatedly, it displays now item and
#     quantity
#==============================================================================

#==============================================================================
# Window_BattleResult
#==============================================================================

class Window_BattleResult < Window_Base

  alias init_result_addon_later initialize
  def initialize(exp, gold, treasures)
    if $game_system.WINDOW_BATTLERESULT
      @exp, @gold = exp, gold
      set_treasures(treasures)
      super(160, 0, 320, @treasures[0].size * 32 + 64)
      self.contents = Bitmap.new(width - 32, height - 32)
      if $fontface != nil
        self.contents.font.name = $fontface
      elsif $defaultfonttype != nil
        self.contents.font.name = $defaultfonttype
      end
      self.y = 160 - height / 2
      self.back_opacity = 160
      self.visible = false
      refresh
    else
      init_result_addon_later(exp, gold, treasures)
    end
  end
  
  alias refresh_result_addon_later refresh
  def refresh
    if $game_system.WINDOW_BATTLERESULT
      self.contents.clear
      x = 4
      if $easy_lvlup_notifier
        self.contents.font.color = system_color
        cx = contents.text_size('Gained').width
        self.contents.draw_text(x, 0, cx, 32, 'Gained')
        x += cx + 4
      else
        self.contents.font.color = normal_color
        cx = contents.text_size(@exp.to_s).width
        self.contents.draw_text(x, 0, cx, 32, @exp.to_s)
        x += cx + 4
        self.contents.font.color = system_color
        cx = contents.text_size('EXP').width
        self.contents.draw_text(x, 0, 64, 32, 'EXP')
        x += cx + 16
      end
      self.contents.font.color = normal_color
      cx = contents.text_size(@gold.to_s).width
      self.contents.draw_text(x, 0, cx, 32, @gold.to_s)
      x += cx + 4
      self.contents.font.color = system_color
      self.contents.draw_text(x, 0, 128, 32, $data_system.words.gold)
      for i in 0...@treasures.size
        draw_item(@treasures[0][i], 4, (i+1)*32, @treasures[1][i])
      end
    else
      refresh_result_addon_later
    end
  end
  
  def set_treasures(treasures)
    items = []
    weapons = []
    armors = []
    stuff = []
    qua = []
    for i in treasures
      items.push(i.id) if i.is_a?(RPG::Item)
      weapons.push(i.id) if i.is_a?(RPG::Weapon)
      armors.push(i.id) if i.is_a?(RPG::Armor)
    end
    for id in items
      if stuff.include?($data_items[id])
        qua[stuff.index($data_items[id])] += 1
      else
        stuff.push($data_items[id])
        qua.push(1)
      end
    end
    for id in weapons
      if stuff.include?($data_weapons[id])
        qua[stuff.index($data_weapons[id])] += 1
      else
        stuff.push($data_weapons[id])
        qua.push(1)
      end
    end
    for id in armors
      if stuff.include?($data_armors[id])
        qua[stuff.index($data_armors[id])] += 1
      else
        stuff.push($data_armors[id])
        qua.push(1)
      end
    end
    @treasures = []
    @treasures.push(stuff)
    @treasures.push(qua)
  end
    
  def draw_item(item, x, y, qua = 1)
    if item != nil
      w1 = self.contents.text_size('0').width
      w2 = self.contents.text_size('x ').width
      x += w1 + w2 + 4
      bitmap = RPG::Cache.icon(item.icon_name)
      self.contents.font.color = normal_color
      self.contents.draw_text(4, y, w1, 32, qua.to_s, 2)
      self.contents.font.color = system_color
      self.contents.draw_text(w1 + 8, y, w2, 32, 'x')
      self.contents.blt(x, y + 4, bitmap, Rect.new(0, 0, 24, 24))
      self.contents.font.color = normal_color
      self.contents.draw_text(x + 28, y, 212, 32, item.name)
    end
  end
  
end

#==============================================================================
# Unique Skill Commands by Blizzard
# Version: 1.2b
# Type: Actor Individuality Improvement
# Date: 14.11.2006
# 
# new in 1.2b:
#   Now corresponding to the Actor ID instead of the class ID && only
#   refreshes the window if neccessary.
#==============================================================================

#==============================================================================
# Window_Command
#==============================================================================

class Window_Command
  
  attr_accessor :actor
  
  def setup_command_name
    if $game_system.UNIQUE_SKILL_COMMANDS && @actor != nil
      old_command = @commands[1]
      @commands[1] = case @actor.id
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Database
#
# Just like usual in all of my scripts and add-on the template is:
# when X then 'COMMAND'
# X - class ID on the database
# COMMAND - the unique skill command for the appropriate class
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
      when 1 then 'Technic'
      when 2 then 'Lancetech'
      when 3 then 'Powers'
      when 4 then 'Skills'
      when 5 then 'Arrowmagic'
      when 6 then 'Ammo'
      when 7 then 'White Magic'
      when 8 then 'Magic'
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Database
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
      end
      refresh if old_command != @commands[1]
    end
  end
  
end

#==============================================================================
# Scene_Battle
#==============================================================================

class Scene_Battle
  
  alias phase3_setup_command_window_unique_command_later phase3_setup_command_window
  def phase3_setup_command_window
    phase3_setup_command_window_unique_command_later
    @actor_command_window.actor = @active_battler
    @actor_command_window.setup_command_name
  end
  
end

#==============================================================================
# Ultimate Font Override by Blizzard
# Version: 1.01b
# Type: Project-Script Compatibility Improvement
# Date: 19.10.2006
# Date v1.01b: 30.7.2007
# 
#   You can change the font/fontsize with the "Call script" event command or
#   directly through a script by using these methods:
# 
#     $game_system.fontname = "FONTNAME"
#     $game_system.fontsize = FONTSIZE
# 
#   It will override the font from any RMXP version. It is also possible to
#   change the font during the game. It will be saved, too.
#==============================================================================

#==============================================================================
# Game_System
#==============================================================================

class Game_System
  
  attr_reader :fontname
  attr_reader :fontsize
  
  alias init_ultimate_font_override_later initialize
  def initialize
    init_ultimate_font_override_later
    self.fontname = 'Arial'
    self.fontsize = 24
  end
  
  def fontname=(name)
    $defaultfonttype = $fontface = @fontname = name
  end
    
  def fontsize=(size)
    $defaultfontsize = $fontsize = @fontsize = size
  end
  
end

#==============================================================================
# Bitmap
#==============================================================================

class Bitmap

  alias init_font_override_later initialize
  def initialize(w, h = nil)
    if w.is_a?(Numeric) && h.is_a?(Numeric)
      init_font_override_later(w, h)
    else
      init_font_override_later(w)
    end
    if TONS_OF_ADDONS::ULTIMATE_FONT_OVERRIDE
      if $game_system != nil && $game_system.fontname != nil &&
          !$scene.is_a?(Scene_Title)
        self.font.name = $game_system.fontname
        self.font.size = $game_system.fontsize
      else
        self.font.name = 'Arial'
        self.font.size = 24
      end
    end
  end
  
end

#==============================================================================
# Heal at LvlUp by Blizzard
# Version: 1.0b
# Type: Game Alteration
# Date: 4.12.2006
# 
# 
# Compatibility:
# 
#   90% compatible with SDK v1.x. 40% compatible with SDK v2.x. Might not work
#   with exotic CBS-es or exotic Status displays during battle.
#==============================================================================

#==============================================================================
# Window_BattleStatus
#==============================================================================

class Window_BattleStatus < Window_Base
  
  alias refesh_heal_at_lvlup_later refresh
  def refresh
    if $game_system.HEAL_AT_LVLUP
      for i in 0...$game_party.actors.size
        if @level_up_flags[i]
          $game_party.actors[i].hp = $game_party.actors[i].maxhp
          $game_party.actors[i].sp = $game_party.actors[i].maxsp
        end
      end
    end
    refesh_heal_at_lvlup_later
  end
  
end

#==============================================================================
# Weapon/Armor HP/SP Plus by Blizzard
# Version: 2.0b
# Type: Weapon/Armor Attribute Alteration
# Date: 18.8.2006
# Date v1.01b: 12.3.2007
# Date v2.0: 15.5.2007
# Date v2.0b: 30.7.2007
# 
# 
# Compatibility:
# 
#   95% compatible with SDK v1.x. 50% compatible with SDK v2.x. May cause
#   slight incompatibility issues with CBS-es, but can be made compatible
#   easily. Can cause imcompatibility issues with other weapon/armor changing
#   scripts and custom equipments scripts.
# 
# 
# Features:
# 
#   - uses static (i.e. 500 HP more) or dynamic (i.e. 30% HP more) increasements
#   - easy to set up
#   - does NOT change any rxdata files
#   - this script comes UNDER SDK SCRIPTS if you use any
# 
# new in v2.0:
#   - completely overworked and changed code for better compatibility
# 
# new in v2.0b:
#   - fixed a bug that appeared because of a typing mistake
# 
# 
# Instructions:
# 
# - Explanation:
# 
#   This script will add the option for Weapons/Armors to have HP/SP pluses
#   while equipped just like the usual STR, DEX, INT etc. pluses.
# 
# - Configuration
# 
#   Find the phrase saying "START" (CTRL+F) to find the database parts. Use the
#   following template to configure your database:
# 
#     when ID then return [EXPR, VAL]
# 
#   ID   - Weapon/Armor ID in the normal database
#   EXPR - set to false if you want "static" increasement or true if you want
#          "dynamic" increasement
#   VAL  - if you use static increasement, set this value to any integer you
#          want (i.e. 100, -500, 831 etc.) to increase the HP/SP, otherwise set
#          it to any decimal value of the final HP/SP (i.e. 1.2 = 20% more,
#          2.3 = 130% more, 0.7 = 30% less)
# 
#   VAL can be a signed integer (static increasement) OR a decimal number
#   greater than 0 (dynamic increasement). Change MAX_HP and MAX_SP to
#   different values if you use another max HP and/or max SP limit than 9999.
# 
# 
# Side Note:
# 
#   It took more to write the instructions than to write and test script
#   itself.
# 
# 
# If you find any bugs, please report them here:
# http://www.chaosproject.co.nr
#==============================================================================

MAX_HP = 9999 # change if needed, 9999 is standard
MAX_SP = 9999 # change if needed, 9999 is standard

#==============================================================================
# Game_System
#==============================================================================

class Game_System
  
  def weapon_hp_plus(id)
    case id
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Weapon HP plus Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    when 1 then return [false, 350]
    when 5 then return [true, 1.2]
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Weapon HP plus Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    else
      return [false, 0]
    end
  end
  
  def weapon_sp_plus(id)
    case id
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Weapon SP plus Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    when 25 then return [false, 500]
    when 29 then return [true, 1.5]
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Weapon SP plus Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    else
      return [false, 0]
    end
  end
  
  def armor_hp_plus(id)
    case id
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Armor HP plus Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    when 1 then return [true, 1.1]
    when 5 then return [true, 0.5]
    when 13 then return [false, 90]
    when 17 then return [false, -450]
    when 9 then return [true, 1.3]
    when 21 then return [true, 1.3]
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Armor HP plus Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    else
      return [false, 0]
    end
  end
  
  def armor_sp_plus(id)
    case id
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Armor SP plus Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    when 9 then return [true, 1.3]
    when 21 then return [true, 1.3]
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Armor SP plus Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    else
      return [false, 0]
    end
  end
  
end

#==============================================================================
# Game_Battler
#==============================================================================

class Game_Battler
  
  alias maxsp_hpsp_add_on_later maxsp
  def maxsp
    val = [MAX_SP, maxsp_hpsp_add_on_later].min
    @sp = val if @sp > val
    return val
  end
  
end

#==============================================================================
# Game_Actor
#==============================================================================

class Game_Actor < Game_Battler
  
  alias maxhp_hpsp_add_on_later maxhp
  def maxhp
    return maxhp_hpsp_add_on_later unless $game_system.HPSPPLUS
    val = [MAX_HP, maxhp_hpsp_add_on_later].min
    @hp = val if @hp > val
    return val
  end
  
  alias base_maxhp_hpsp_add_on_later base_maxhp
  def base_maxhp
    return base_maxhp_hpsp_add_on_later unless $game_system.HPSPPLUS
    plus = 0
    multi = 1.0
    if @weapon_id != 0
      result = $game_system.weapon_hp_plus(@weapon_id)
      result[0] ? (multi *= result[1]) : (plus += result[1])
    end
    for id in [@armor1_id, @armor2_id, @armor3_id, @armor4_id]
      if id != 0
        result = $game_system.armor_hp_plus(id)
        result[0] ? (multi *= result[1]) : (plus += result[1])
      end
    end
    return (multi * (plus + base_maxhp_hpsp_add_on_later)).to_i
  end
  
  alias base_maxsp_hpsp_add_on_later base_maxsp
  def base_maxsp
    return base_maxsp_hpsp_add_on_later unless $game_system.HPSPPLUS
    plus = 0
    multi = 1.0
    if @weapon_id != 0
      result = $game_system.weapon_sp_plus(@weapon_id)
      result[0] ? (multi *= result[1]) : (plus += result[1])
    end
    for id in [@armor1_id, @armor2_id, @armor3_id, @armor4_id]
      if id != 0
        result = $game_system.armor_sp_plus(id)
        result[0] ? (multi *= result[1]) : (plus += result[1])
      end
    end
    return (multi * (plus + base_maxsp_hpsp_add_on_later)).to_i
  end
  
end

#==============================================================================
# EQUAP Skills by Blizzard
# Version: 3.02b
# Type: Skill System
# Date: 28.05.2006
# Date v2.0: 13.06.2006
# Date v2.02b: 16.1.2007
# Date v3.0b: 19.2.2007
# Date v3.02b: 7.3.2007
# 
# 
# Explanation:
# 
#   This add-on will allow you to bound skills to equipment. Equip it and you
#   learn the skill, unequip it and you will forget it. The AP system allows to
#   gain AP for skills and learn the permanently if the max AP for the skill
#   are gathered. (This system is a very similar one to FF9's AP Skill System.)
# 
# 
# v2.0:
#   - fixed bug, that appeared, when more equipment parts had the same skill
#   - new multi-skill support
# 
# v2.02b:
#   - improved coding a little bit
# 
# v3.0b:
#   - completely overworked and added optional AP system (similar to FF9)
#     (I want to mention here I made this especially for blazinhandle =) )
# 
# v3.02b:
#   - fixed bugs
# 
# 
# Compatibility:
# 
#   99% compatible with SDK v1.x. 60% compatible with SDK v2.x. WILL cause
#   incompatibility with custom equipment scripts but there are instructions
#   how to configure the script. Please note, that this script depends on the
#   layout of your Equip Screen and needs to be put UNDER a CMS script if you
#   are using one. Also there needs to be something changed if you are using
#   another script, that uses dummy elements. Add your dummy element IDs to the
#   triple commented array (###). WILL corrupt your old savegames. Might not
#   work with some CMS-es.
# 
# 
# Instructions:
# 
# - Configuration:
# 
#   Press CRTL+SHIFT+F and type into the window one of the following:
# 
#     Start EQ Database
#     Start MAXAP Database
#     Start GAINAP Database
# 
#   You can jump now to the database directly. There are more instructions.
#   Also change EQUAP_ELEMENT = XXX, where XXX is the ID number of the dummy
#   element, that determines, which skill is bound to the equipment. Be sure to
#   give that element every EQ skill or the system WILL glitch.
# 
# - Merge with a Custom Equipment System:
#   
#   The lines, that need to be edited are double commented with ##. If you are no 
#   at least a bit of experienced scripter, it may be better to ask somebody else
#   to perform the edit for you. Please note, that the person, who is going to
#   edit this script needs the custom equipment script for reference.
# 
# 
# NOTE:
# 
#   DO NOT USE EQUAP SKILLS AS NORMAL SKILLS! THE SYSTEM WORKS WITH TEMPORARY
#   LEARNING AND FORGETTING THE EQUAP SKILL. IF YOU LET YOUR CHARACTER LEARN AN
#   EQUAP SKILL BY NORMAL MEANS, HE WILL FORGET IT AFTER HE UNEQUIPS THE
#   APPROPRIATE EQUIPMENT!
# 
# 
# If you find any bugs, please report them here:
# http://www.chaosproject.co.nr/
#==============================================================================

if TONS_OF_ADDONS::EQUAP_SKILLS

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Start EQUAP General Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

$EQUAP_ELEMENT = 17 # your EQ element ID
if $DUMMY_ELEMENTS == nil
  $DUMMY_ELEMENTS = [$EQUAP_ELEMENT] ### add more dummy elements if you have any
else
  $DUMMY_ELEMENTS.push($EQUAP_ELEMENT)
end
DISPLAY_AP_GAIN = true # uses a modified Battle Result to display gained AP
DISPLAY_AP_REQ = true # show CURRENT_AP/NEEDED_AP in the skill's name
GAIN_DEAD = false # dead actor also gain AP, no matter what

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# End EQUAP General Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#==============================================================================
# Game_System
#==============================================================================

class Game_System
  
  def maxap(id)
    case id
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Start of MAXAP Database
#
#   Here you can define the APs needed to learn a skill. If you add no skills
#   here the AP system is automatically disabled. Configure it like this
#   template:
# 
#     when SKILL_ID then return MAXAP
# 
#   SKILL_ID - the ID of the skill that will be learned with AP
#   MAXAP    - how many AP are required to learn the skill
# 
# Note:
# 
#   Don't forget to assign your AP skills to equipment in the EQ Database below.
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    when 1 then return 0
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# End of MAXAP Database
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    end
    return 0
  end
  
  def gainap(id)
    case id
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Start of GAINAP Database
#
#   Here you can define how many AP you will get from enemy troops. Configure
#   it like this template:
# 
#     when TROOP_ID then return GAINAP
# 
#   TROOP_ID - the ID of the enemy troop
#   GAINAP   - how many AP will the player get from this troop.
# 
# Note:
# 
#   This will automatically be disabled if there are no AP skills.
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    when 1 then return 2
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# End of MAXAP Database
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    end
    return 0
  end
  
  def eq_database(ids)
    skill_ids = []
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Start of EQ Database
#
#   This is your equipment database. To add one or more new EQUAP skills to a
#   weapon is very simple. Add another "when"-branch in the script snipplet
#   below (they have comments next to it). Configure it like this template:
# 
#     when WEAPON_ID
#       @skill_ids.push(EQUAP_SKILL_ID1)
#       @skill_ids.push(EQUAP_SKILL_ID2)
# 
#   The same works for armors:
# 
#     when ARMOR_ID
#       @skill_ids.push(EQUAP_SKILL_ID1)
#       @skill_ids.push(EQUAP_SKILL_ID2)
# 
#   Please note, that you need to configure this for every equipment part
#   separately. That means you need to set it seperately for shields, armors,
#   helmets and accessories. This also goes for custom equipment additions.
# 
#   The lines are commented below so you should have no problems with the script.
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    case ids[0]
    when 6 # weapon ID
      skill_ids.push(10) # EQUAP skill ID
      skill_ids.push(11) # EQUAP skill ID
    when 10 # weapon ID
      skill_ids.push(8) # EQUAP skill ID
      skill_ids.push(12) # EQUAP skill ID
    end
    case ids[1]
    when 1 # armor1 ID
      skill_ids.push(1) # EQUAP skill ID
      skill_ids.push(25) # EQUAP skill ID
    when 19 # armor1 ID
      skill_ids.push(25) # EQUAP skill ID
    end
    case ids[2]
    when 5 # armor2 ID
      skill_ids.push(15) # EQUAP skill ID
    when 18 # armor2 ID
      skill_ids.push(27) # EQUAP skill ID
    end
    case ids[3]
    when 13 # armor3 ID
      skill_ids.push(2) # EQUAP skill ID
      skill_ids.push(25) # EQUAP skill ID
    when 3 # armor3 ID
      skill_ids.push(7) # EQUAP skill ID
      skill_ids.push(4) # EQUAP skill ID
    end
    case ids[4] ## add more ids if you are using a custom number of equip parts
    when 29 # armor4 ID
      skill_ids.push(10) # EQUAP skill ID
    when 8 # armor4 ID
      skill_ids.push(32) # EQUAP skill ID
      skill_ids.push(29) # EQUAP skill ID
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# End of EQ Database
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    end
    return skill_ids
  end
    
end
  
#==============================================================================
# Game_Battler
#==============================================================================

class Game_Battler
  
  def elements_correct(elements)
    multiplier = size = 0
    for i in elements
      unless $DUMMY_ELEMENTS.include?(i)
        multiplier += self.element_rate(i)
        size += 1
      end
    end
    return (size == 0 ? 100 : multiplier/size)
  end
  
end

#==============================================================================
# Game_Actor
#==============================================================================

class Game_Actor < Game_Battler
  
  alias setup_equap_later setup
  def setup(id)
    setup_equap_later(id)
    if $ap_enabled
      @ap = {}
      for id in 1...$data_skills.size
        @ap[id] = 0 if $game_system.maxap(id) != 0
      end
    end
    test_equap
  end
  
  def add_ap(val)
    if $ap_enabled
      for key in @ap.keys
        if @skills.include?(key)
          max = $game_system.maxap(key)
          @ap[key] = self.ap(key) + val
          @ap[key] = max if @ap[key] > max
          @ap[key] = 0 if @ap[key] < 0
        end
      end
    end
  end
  
  def ap(id)
    return (!$ap_enabled ? 0 : @ap[id] == nil ? 0 : @ap[id])
  end
  
  alias equip_equap_later equip
  def equip(equip_type, id)
    equip_equap_later(equip_type, id)
    test_equap
  end
  
  def test_equap
    ids = []
    ids.push(@weapon_id) ## this part here needs to be edited if a custom
    ids.push(@armor1_id) ## number of equipment parts is used. In that case it
    ids.push(@armor2_id) ## is enough to add more of these commands here. Also
    ids.push(@armor3_id) ## be sure to use the correct names for the IDs like
    ids.push(@armor4_id) ## i.e. "armor3_id"
    skill_ids = $game_system.eq_database(ids)
    for id in 1...$data_skills.size
      if $data_skills[id].element_set.include?($EQUAP_ELEMENT) &&
          (!$ap_enabled || self.ap(id) < $game_system.maxap(id))
        forget_skill(id)
      end
    end
    for id in skill_ids
      learn_skill(id)
    end
  end
  
end

#==============================================================================
# Game_Troop
#==============================================================================

class Game_Troop
  
  attr_reader :id
  
  alias setup_equap_later setup
  def setup(troop_id)
    setup_equap_later(troop_id)
    @id = troop_id if $ap_enabled
  end
  
end

#==============================================================================
# Window_BattleResult
#==============================================================================

class Window_BattleResult
  
  def refresh_extra(aps)
    self.contents.fill_rect(0, 0, self.width, 32, Color.new(0, 0, 0, 0))
    x = 4
    self.contents.font.color = normal_color
    cx = contents.text_size(@exp.to_s).width
    self.contents.draw_text(x, 0, cx, 32, @exp.to_s)
    x += cx + 4
    self.contents.font.color = system_color
    cx = contents.text_size('EXP').width
    self.contents.draw_text(x, 0, 64, 32, 'EXP')
    x += cx + 16
    self.contents.font.color = normal_color
    cx = contents.text_size(@gold.to_s).width
    self.contents.draw_text(x, 0, cx, 32, @gold.to_s)
    x += cx + 4
    self.contents.font.color = system_color
    cx = contents.text_size($data_system.words.gold).width
    self.contents.draw_text(x, 0, 128, 32, $data_system.words.gold)
    x += cx + 16
    self.contents.font.color = normal_color
    cx = contents.text_size(aps.to_s).width
    self.contents.draw_text(x, 0, cx, 32, aps.to_s)
    x += cx + 4
    self.contents.font.color = system_color
    self.contents.draw_text(x, 0, 128, 32, 'AP')
  end

end

#==============================================================================
# Window_Skill
#==============================================================================

class Window_Skill
  
  alias draw_item_equap_later draw_item
  def draw_item(index)
    skill = @data[index]
    aps = $game_system.maxap(skill.id)
    if DISPLAY_AP_REQ && aps != 0 && !$scene.is_a?(Scene_Battle)
      if @actor.skill_can_use?(skill.id)
        self.contents.font.color = normal_color
      else
        self.contents.font.color = disabled_color
      end
      x = 4 + index % 2 * (288 + 32)
      y = index / 2 * 32
      rect = Rect.new(x, y, self.width / @column_max - 32, 32)
      self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
      bitmap = RPG::Cache.icon(skill.icon_name)
      opacity = self.contents.font.color == normal_color ? 255 : 128
      self.contents.blt(x, y + 4, bitmap, Rect.new(0, 0, 24, 24), opacity)
      text = "#{skill.name} (#{@actor.ap(skill.id)}/#{aps})"
      self.contents.draw_text(x + 28, y, 204, 32, text, 0)
      self.contents.draw_text(x + 232, y, 48, 32, skill.sp_cost.to_s, 2)
    else    
      draw_item_equap_later(index)
    end
  end
  
end

#==============================================================================
# Scene_Battle
#==============================================================================

class Scene_Battle
  
  alias start_phase5_equap_later start_phase5
  def start_phase5
    start_phase5_equap_later
    if $ap_enabled && DISPLAY_AP_GAIN
      aps = $game_system.gainap($game_troop.id)
      @result_window.refresh_extra(aps)
      for actor in $game_party.actors
        actor.add_ap(aps) if GAIN_DEAD || !actor.dead?
      end
    end
  end
  
end

#==============================================================================
# AP enabled test
#==============================================================================

sys = Game_System.new
skills = ARC::Data.load('Data/Skills.arc')
skills.delete(nil)
$ap_enabled = false
for skill in skills
  if sys.maxap(skill.id) != 0
    $ap_enabled = true
    break
  end
end
sys = nil
skills = nil

end

#==============================================================================
# Picture Movie Scene by Blizzard
# Version: 2.03b
# Type: Scene Creation Utility
# Date: 3.11.2006
# 
# 
# Compatibility:
# 
#   100% compatible with SDK v1.x. 90% compatible with SDK v2.x.
# 
# Complexity:
#   - very low
# 
# Special knowledge REQUIRED:
#   - reading long and boring instructions
#   - using the "Call script" event command
# 
# Special knowledge RECOMMENED:
#   - REALLY using the "Call script" event command
# 
# 
# Explanation:
# 
#   This script will allow you to create picture scenes for different purposes.
#   You can create Credits, Intros or just picture (comic) movies.
# 
# 
# Instructions:
# 
#   Use following syntax to call this script:
# 
#     $scene = Scene_Pictures.new('STRING', DELAY, BDELAY, EXIT, 'FILE', RETURN)
# 
#   STRING     - name of the pictures to be loaded
#   DELAY      - time of displaying pictures
#   BLACKDELAY - time delay of displaying between the pictures
#   EXIT       - allow exiting (true by default) the scene by pressing ESC/ENTER
#   FILE       - the name of the music file to be played (none by default)
#   RETURN     - to which scene to return when done (Scene_Map is default)
# 
#   All your pictures must be named like STRING and put into a new folder
#   called Scene inside the Pictures folder with the order number attached.
# 
# Examples:
# 
# 1)
#   $scene = Scene_Pictures.new('animat', 5, 1, false)
# 
#   A scene will be created where the first picture is located in:
#   Graphics/Pictures/Scene/animat1.png
#   The next will be
#   Graphics/Pictures/Scene/animat2.png
#   It will display pictures as long as there are some.
#   The scene can't be interrupted.
# 
# 2)
#   $scene = Scene_Pictures.new('i_n_t_r_o_', 5, 1, true, nil, Scene_Title.new)
# 
#   Graphics/Pictures/Scene/i_n_t_r_o_1.png will be the first.
#   Graphics/Pictures/Scene/i_n_t_r_o_2.png will be the next after that.
#   It can be interrupted and will start the title scene after finishing.
# 
# 3)
#   $scene = Scene_Pictures.new('credits', 5, 1)
# 
#   Graphics/Pictures/Scene/credits1.png will be the first.
#   Graphics/Pictures/Scene/credits2.png will be the next after that.
# 
# 
# Side notes:
# 
#   If you want to use this scene an intro before the Title, you have to apply
#   the syntax mentioned above in the Main script. Just change the
#   $scene = Scene_Title.new
#   to the desired syntax and don't forget to set its returning to Scene_Title.
#   All your BGMs should be in the Audio/BGM folder
# 
# 
# If you find any bugs, please report them here:
# http://www.chaosproject.co.nr
#==============================================================================

#==============================================================================
# Scene_Pictures
#==============================================================================

class Scene_Pictures

  def initialize(pics, del, hold, int = true, file = nil, scene = Scene_Map.new)
    $game_system = Game_System.new if $game_system == nil
    @names = pics
    @delay = del
    @hold = hold
    @int = int
    @file = file
    @next_scene = scene
  end

  def main
    $scene = @next_scene
    @next_scene = nil
    Graphics.transition
    Graphics.freeze
    delaying(true)
    Audio.bgm_stop
    if @file != nil
      Audio.bgm_play("Audio/BGM/#{@file}", 100, 100)
      @file = nil
    end
    i = 1
    loop do
      break if there_are_no_more_files(@names + i.to_s)
      @pic = RPG::Sprite.new
      @pic.bitmap = RPG::Cache.picture("Scene/#{@names}#{i}")
      @pic.x = 320 - @pic.bitmap.width/2
      @pic.y = 240 - @pic.bitmap.height/2
      Graphics.transition(12)
      break if delaying
      Graphics.freeze
      @pic.dispose
      @pic = nil
      Graphics.transition(12)
      break if delaying(true)
      Graphics.freeze
      i += 1
    end
    unless @pic == nil || @pic.disposed?
      @pic.dispose 
      Graphics.transition(12)
    else
      Graphics.transition(4)
    end
    delaying(true)
    Audio.bgm_fade(800)
    Graphics.freeze
  end

  def delaying(just_hold = false)
    for i in 0...(just_hold ? @hold : @delay)*40
      Graphics.update
      if @int
        Input.update
        return true if Input.press?(Input::C) || Input.press?(Input::B)
      end
    end
    return false
  end
  
  def there_are_no_more_files(name)
    return (!FileTest.exist?("Graphics/Pictures/Scene/#{name}.png") &&
            !FileTest.exist?("Graphics/Pictures/Scene/#{name}.jpg"))
  end
  
end

#==============================================================================
# Target 'em all! by Blizzard
# Version: 1.0b
# Type: Skill Enhancement
# Date: 27.9.2006
# 
# 
#   This add-ons will allow you to create skills that can target all enemies
#   and all party members. Include all such skill IDs in the FULL_TARGET_IDS
#   array and separate them with commas. Note that you should make the skill
#   target all enemies/all party members/etc. to avoid the cursor being
#   displayed.
#==============================================================================

FULL_TARGET_IDS = []

#==============================================================================
# Scene_Battle
#==============================================================================

class Scene_Battle
  
  alias make_skill_action_result_target_all_later make_skill_action_result
  def make_skill_action_result
    if $game_system.TARGET_EM_ALL &&
        FULL_TARGET_IDS.include?(@active_battler.current_action.skill_id)
      @target_battlers = []
      for enemy in $game_troop.enemies
        @target_battlers.push(enemy) if enemy.exist?
      end
      for actor in $game_party.actors
        @target_battlers.push(actor) unless actor.dead?
      end
    end
    make_skill_action_result_target_all_later
  end

end

#==============================================================================
# Quick Passability Test by Blizzard
# Version: 1.0b
# Type: Debug Utility
# Date: 7.2.2007
# 
# 
# Important:
# 
#   This add-ons ONLY works in Debug mode/Testplay mode and is mainly
#   considered for debugging maps faster.
# 
# 
# Instructions:
# 
#   This will put a mask on your map that shows the passability. Trigger on/off
#   the mask by pressing F6. You can define the color the passable part should
#   have by changing the TILE_COLOR constant. Use this template:
# 
#   TILE_COLOR = Color.new(R, G, B, A)
# 
#   R - red
#   G - green
#   B - blue
#   A - alpha (opacity)
# 
#   Every value needs to be set to a number between 0~255. Alpha over 128 is
#   not recommended. This will only work with the map, events are not
#   considered. This add-on will not work if the map's width * maps's height is
#   bigger than 19200, because the sprite would take up too much RAM and your
#   operating system would freeze and crash the game.
#==============================================================================

TILE_COLOR = Color.new(255, 64, 0, 96)

#==============================================================================
# Game_Map
#==============================================================================

$quick_pass = true

class Game_Map
  
  attr_reader :passables
  
  alias setup_minimap_later setup
  def setup(map_id)
    setup_minimap_later(map_id)
    setup_passability_net(true)
  end
  
  def setup_passability_net(force_flag = false)
    if @passables == nil || @passables == [] || force_flag
      @passables = []
      s1 = $game_system.minimap_w / $game_map.width
      s2 = $game_system.minimap_h / $game_map.height
      if $DEBUG && $game_system.QUICK_PASSABILITY_TEST &&
          width * height <= 19200 || $game_system.MINIMAP && s1 != 0 && s2 != 0
        for i in 0...$game_map.height
          Graphics.update if $game_map.width * $game_map.height >= 19200
          for j in 0...$game_map.width
            if $game_map.virtual_passable?(j, i, 2) || $game_map.virtual_passable?(j, i, 4) ||
                $game_map.virtual_passable?(j, i, 6) || $game_map.virtual_passable?(j, i, 8)
              @passables.push([j, i])
            end
          end
        end
      end
    end
  end
  
  def virtual_passable?(x, y, d)
    return false unless valid?(x, y)
    bit = (1 << (d / 2 - 1)) & 0x0f
    for i in [2, 1, 0]
      tile_id = data[x, y, i]
      if tile_id == nil then return false
      elsif @passages[tile_id] & bit != 0 then return false
      elsif @passages[tile_id] & 0x0f == 0x0f then return false
      elsif @priorities[tile_id] == 0 then return true
      end
    end
    return true
  end
  
end

#==============================================================================
# Scene_Map
#==============================================================================

class Scene_Map
  
  alias main_quick_passability_later main
  def main
    main_quick_passability_later
    @passable.dispose if @passable != nil
  end
  
  alias upd_quick_passability_later update
  def update
    upd_quick_passability_later
    if $DEBUG && $game_system.QUICK_PASSABILITY_TEST
      if @passable != nil
        if Input.trigger?(Input::F6)
          @passable.dispose
          @passable = nil
        else
          @passable.x = -$game_map.display_x/4
          @passable.y = -$game_map.display_y/4
        end
      elsif Input.trigger?(Input::F6)
        @passable = create_passable_help
        unless @passable == nil
          @passable.x = -$game_map.display_x/4
          @passable.y = -$game_map.display_y/4
        end
      end
    end
  end
  
  def create_passable_help
    coos = $game_map.passables
    if coos != [] && $game_map.width * $game_map.height <= 19200
      passable = RPG::Sprite.new
      passable.bitmap = Bitmap.new($game_map.width*32, $game_map.height*32)
      for i in 0...coos.size
        passable.bitmap.fill_rect(coos[i][0]*32, coos[i][1]*32, 32, 32, TILE_COLOR)
      end
      passable.z = 10000
      return passable
    end
  end
  
end

#==============================================================================
# Dynamic Passability Minimap by Blizzard
# Version: 1.01b
# Type: Game Playability Improvement
# Date: 7.2.2007
# 
# 
# Compatibility:
# 
#   95% compatible with SDK v1.x. 60% compatible with SDK v2.x. This add-on
#   NEEDS "Quick Passability Test" by Blizzard. WILL corrupt your old
#   savegames. Might not work with special map add-ons. Does NOT work with
#   pixel-movement without changing the code.
# 
# 
# Why this minimap script better is than any other (aka features):
# 
#   - simple display to avoid lag
#   - custom size, position and opacity, changeable even during the game
#   - no bitmaps, no pictures to import, only plain script
# 
# 
# Explanation:
# 
#   This add-on will draw a real-time minimap on the specified X and Y
#   coordinate on your screen. It will show the player, events that do NOT have
#   a comment in their code that says "no_minimap", that are not parallel
#   process and that are not auto-start and that are not erased yet. Events
#   with a teleport/transfer player command will be shown in a different color.
#   Any event with and comment with "special" in their code will be also
#   displayed differently. Blizz-ABS disables this add-on automatically and
#   uses the more enhanced built-in Blizz-ABS Minimap.
# 
# 
# Instructions:
# 
#   You can trigger the minimap visible/invisible with F5 during the game.
#   Set up the starting configuration below. The colors follow a template of:
# 
#     WHAT_COLOR = Color.new(R, G, B)
# 
#   R - red
#   G - green
#   B - blue
# 
#   Change the colors of the dots on the map as you prefer it.
# 
#   PLAYER_COLOR    - the player on the minimap
#   EVENT_COLOR     - any event on the minimap that is not erased, is not
#                     auto-start, is not parallel process and does not have a
#                     comment in its code with the word "no_minimap"
#   TELEPORT_COLOR  - any event like the one above, but that has a teleport/
#                     transfer_player command
#   SPECIAL_COLOR   - any event with a comment with the word "special"
#   MINIMAP_X       - default X of the minimap on the screen
#   MINIMAP_Y       - default Y of the minimap on the screen
#   MINIMAP_WIDTH   - default maximal allowed width of the minimap
#   MINIMAP_HEIGHT  - default maximal allowed height of the minimap
#   MINIMAP_OPACITY - default opacity of the minimap on the screen
# 
#   You have the possibility to change the minimap's size, coordinates and
#   opacity during the game process. The command you need to type in into a
#   "Call Script" command window are:
# 
#     $game_system.mini_coos(X, Y)
#     $game_system.mini_size(W, H)
#     $game_system.mini_opaq(A)
# 
#   X - new X
#   Y - new Y
#   W - new width
#   H - new height
#   A - new opacity
# 
#   Any changes will be applied instantly. Note that you don't need to use ALL
#   commands.
# 
# 
# Note:
# 
#   Changing X, Y and opacity during the game will result in just moving the
#   sprite. The minimap will not work if the maximal allowed size is smaller
#   than the map size. (i.e. if your minimap is 160x120, maps like 170x130,
#   180x15 or 20x140 will not work.)
#==============================================================================

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Start Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

PLAYER_COLOR = Color.new(0, 255, 0)
EVENT_COLOR = Color.new(0, 128, 255)
TELEPORT_COLOR = Color.new(255, 255, 0)
SPECIAL_COLOR = Color.new(255, 0, 0)
MINIMAP_X = 0
MINIMAP_Y = 0
MINIMAP_WIDTH = 160
MINIMAP_HEIGHT = 160
MINIMAP_OPACITY = 160

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# End Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if $quick_pass != true
  p 'Attention! Minimap is missing a vital add-on! Application will now close!'
  exit
end

#==============================================================================
# Game_System
#==============================================================================

class Game_System
  
  attr_reader   :minimap_x
  attr_reader   :minimap_y
  attr_reader   :minimap_w
  attr_reader   :minimap_h
  attr_reader   :minimap_a
  attr_accessor :minimap_visible
  
  alias init_minimap_later initialize
  def initialize
    init_minimap_later
    @minimap_visible = false
    @minimap_x = [[MINIMAP_X, 0].max, 640].min
    @minimap_y = [[MINIMAP_Y, 0].max, 480].min
    @minimap_w = [[MINIMAP_WIDTH, 0].max, 640].min
    @minimap_h = [[MINIMAP_HEIGHT, 0].max, 480].min
    @minimap_a = [[MINIMAP_OPACITY, 0].max, 255].min
  end
  
  def mini_coos(x, y)
    @minimap_x = [[x, 0].max, 640].min
    @minimap_y = [[y, 0].max, 480].min
  end
  
  def mini_size(w, h)
    @minimap_w = [[w, 0].max, 640].min
    @minimap_h = [[h, 0].max, 480].min
    $game_map.setup_passability_net
  end
  
  def mini_opaq(a)
    @minimap_a = [[a, 0].max, 255].min
  end
  
end

#==============================================================================
# Game_Event
#==============================================================================

class Game_Event < Game_Character
  
  attr_reader :erased
  
  def conditions
    for page in @event.pages.reverse
      c = page.condition
      next if c.switch1_valid && !$game_switches[c.switch1_id]
      next if c.switch2_valid && !$game_switches[c.switch2_id]
      if c.variable_valid
        next if $game_variables[c.variable_id] < c.variable_value
      end
      if c.self_switch_valid
        key = [@map_id, @event.id, c.self_switch_ch]
        next if $game_self_switches[key] != true
      end
      return true
    end
    return false
  end
  
end
  
#==============================================================================
# Mini_Map
#==============================================================================

class Mini_Map < RPG::Sprite
  
  def initialize(viewport = nil)
    super
    self.z = 10100
    create_minimap
  end
  
  def create_minimap
    coos = $game_map.passables
    @w = $game_system.minimap_w
    @h = $game_system.minimap_h
    s = [@w / $game_map.width, @h / $game_map.height]
    @size = (s[0] > s[1] ? s[1] : s[0])
    if @size > 0
      self.bitmap = Bitmap.new(@size*$game_map.width, @size*$game_map.height)
      self.bitmap.fill_rect(0, 0, @w, @h, Color.new(0, 0, 0))
      color = Color.new(128, 128, 128, 255)
      for coo in coos
        self.bitmap.fill_rect(coo[0]*@size, coo[1]*@size, @size, @size, color)
      end
      @events = get_events
      create_sevents
      update
    else
      self.dispose
    end
  end
  
  def update
    super
    ev = get_events
    if ev != @events
      @events = ev
      destroy_sevents
      create_sevents
    end
    self.x = $game_system.minimap_x
    self.y = $game_system.minimap_y
    self.opacity = $game_system.minimap_a
    for i in 0...@sevents.size
      @sevents[i].x = @events[i].x * @size + self.x
      @sevents[i].y = @events[i].y * @size + self.y
      @sevents[i].opacity = $game_system.minimap_a
    end
    if @w != $game_system.minimap_w || @h != $game_system.minimap_h
      self.bitmap.dispose
      destroy_sevents
      create_minimap
    end
  end
  
  def create_sevents
    @sevents = []
    for i in 0...@events.size
      sprite = RPG::Sprite.new
      sprite.bitmap = Bitmap.new(@size, @size)
      if @events[i].is_a?(Game_Player)
        color = PLAYER_COLOR
      elsif event_comment(@events[i], 'special')
        color = SPECIAL_COLOR
      elsif @events[i].list != nil
        color = EVENT_COLOR
        for j in @events[i].list
          if j.code == 201
            color = TELEPORT_COLOR
            break
          end
        end
      else
        color = EVENT_COLOR
      end
      sprite.bitmap.fill_rect(0, 0, @size, @size, color)
      sprite.z = 10200
      @sevents.push(sprite)
    end
  end
    
  def destroy_sevents
    @sevents.each {|i| i.dispose}
    @sevents = nil
  end
  
  def get_events
    events = [$game_player]
    for event in $game_map.events.values
      if !event.erased && ![3, 4].include?(event.trigger) &&
          !event_comment(event, 'no_minimap') && event.conditions
        events.push(event)
      end
    end
    return events
  end
  
  def event_comment(event, comment)
    return false unless event.list.is_a?(Array)
    for command in event.list
      return true if command.code == 108 && command.parameters[0] == comment
    end
    return false
  end
  
  def dispose
    destroy_sevents if @sevents != nil
    super
  end
  
end

#==============================================================================
# Scene_Map
#==============================================================================

class Scene_Map
  
  alias main_minimap_later main
  def main
    @minimap = Mini_Map.new if $game_system.minimap_visible
    main_minimap_later
    @minimap.dispose if @minimap != nil
  end
  
  alias upd_minimap_later update
  def update
    upd_minimap_later
    return if $BlizzABS && BlizzABS::VERSION >= 1.030
    if $game_system.MINIMAP
      if @minimap != nil
        if Input.trigger?(Input::F5)
          @minimap.dispose
          @minimap = nil
          $game_system.minimap_visible = false
        else
          @minimap.update
        end
      elsif Input.trigger?(Input::F5)
        @minimap = Mini_Map.new
        if @minimap.disposed?
          $game_system.minimap_visible = false
          @minimap = nil
        else
          $game_system.minimap_visible = true
        end
      end
    end
  end
  
  alias transfer_player_minimap_later transfer_player
  def transfer_player
    if $game_system.minimap_visible
      @minimap.dispose
      @minimap = nil
    end
    transfer_player_minimap_later
    @minimap = Mini_Map.new if $game_system.minimap_visible
    if @minimap != nil && @minimap.disposed?
      @minimap = nil
      $game_system.minimap_visible = false
    end
  end
  
end

#==============================================================================
# Enemy Status in Battle by Blizzard
# Version: 1.0b
# Type: Information Display Alteration
# Date: 17.2.2007
# 
# 
# Compatibility:
# 
#   99% compatible with SDK v1.x. 80% compatible with SDK v2.x. Might cause
#   incompatibility issues with exotic CBS-es, CMS-es and custom enemy status
#   displays.
# 
# 
# Explanation:
# 
#   This add-on will not only show enemies' names, but even HP, SP and status
#   in the help window during battle.
#==============================================================================

#==============================================================================
# Window_Help
#==============================================================================

class Window_Help < Window_Base
  
  alias set_enemy_status_later set_enemy
  def set_enemy(enemy)
    $game_system.ENEMY_STATUS ? set_actor(enemy) : set_enemy_status_later(enemy)
  end
  
end

#==============================================================================
# Skill Separation System (SSS) by Blizzard
# Version: 1.0b
# Type: Game Playability Improvement
# Date: 22.3.2007
# 
# new in 1.0b:
#   - beta release, it should work without bugs now
# 
# 
# Explanation:
# 
#   Every of your skills will be categorized. You can put the same skill in
#   more categories. You can define category names and element dummies below.
#==============================================================================

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# your skill set dummy elements
SKILL_SETS = [9, 10, 11, 12, 13, 14, 15, 16]
# names of skill sets
SKILL_SET_NAMES = ['White Magic', 'Black Magic', 'Blue Magic', 'Technic',
                    'Special Attack', 'Psy', 'Magitech', 'Overlution']
# the X offset of the drawing (try changing it to see what it does and adjust
# it how you want it to be, of course you can use negative numbers)
$x_off = 50

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if $DUMMY_ELEMENTS != nil
  $DUMMY_ELEMENTS |= SKILL_SETS
else
  $DUMMY_ELEMENTS = SKILL_SETS.clone
end

#==============================================================================
# Game_Battler
#==============================================================================

class Game_Battler
  
  def elements_correct(elements)
    multiplier = size = 0
    for i in elements
      unless $DUMMY_ELEMENTS.include?(i)
        multiplier += self.element_rate(i)
        size += 1
      end
    end
    return (size == 0 ? 100 : multiplier/size)
  end
  
end

#==============================================================================
# Window_Skill
#==============================================================================

class Window_Skill < Window_Selectable
  
  alias init_sss_later initialize
  def initialize(actor)
    if $game_system.SKILL_SEPARATION
      super(0, 128, 640, 384)
      @skill_ids = []
      SKILL_SETS.size.times{@skill_ids.push([0])}
      @column_max = 1
      @actor = actor
      @index = 0
      @alt_index = []
      SKILL_SETS.size.times{@alt_index.push(0)}
      refresh
      if $game_temp.in_battle
        self.y = 64
        self.height = 256
        self.back_opacity = 160
      end
    else
      init_sss_later(actor)
    end
  end
  
  alias refresh_sss_later refresh
  def refresh
    if $game_system.SKILL_SEPARATION
      if self.contents != nil
        self.contents.dispose
        self.contents = nil
      end
      if @actor != nil
        for id in @actor.skills
          for i in 0...SKILL_SETS.size
            if $data_skills[id].element_set.include?(SKILL_SETS[i])
              @skill_ids[i].push(id)
            end
          end
        end
        for i in 0...SKILL_SETS.size
          @skill_ids[i].delete(0) if @skill_ids[i].size > 1
        end
        @item_max = SKILL_SETS.size
        self.contents = Bitmap.new(width - 32, row_max * 32)
        if $fontface != nil
          self.contents.font.name = $fontface
        elsif $defaultfonttype != nil
          self.contents.font.name = $defaultfonttype
        end
        self.contents.font.size = 24
        for i in 0...SKILL_SETS.size
          draw_item(i)
        end
      end
    else
      refresh_sss_later
    end
  end
  
  alias draw_item_sss_later draw_item
  def draw_item(index)
    if $game_system.SKILL_SEPARATION
      y = index * 32
      rect = Rect.new(0, y, self.width / @column_max - 32, 32)
      self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
      id = @skill_ids[index][@alt_index[index]]
      skill = $data_skills[id] if id != 0
      if skill != nil
        if @actor.skill_can_use?(skill.id)
          self.contents.font.color = normal_color
        else
          self.contents.font.color = disabled_color
        end
        bitmap = RPG::Cache.icon(skill.icon_name)
        opacity = self.contents.font.color == normal_color ? 255 : 128
        self.contents.blt(200+$x_off, y+4, bitmap, Rect.new(0, 0, 24, 24), opacity)
        self.contents.draw_text(228+$x_off, y, 204, 32, skill.name, 0)
        self.contents.draw_text(516, y, 64, 32, skill.sp_cost.to_s, 2)
        if @skill_ids[index].size > 1
          self.contents.draw_text(184+$x_off, y, 32, 32, '«')
          self.contents.draw_text(564, y, 32, 32, '»', 2)
        end
      else
        self.contents.font.color = disabled_color
        self.contents.draw_text(228+$x_off, y, 204, 32, 'not available')
      end
      if id == 0
        color = disabled_color
      elsif @actor.skill_can_use?(id)
        color = normal_color
      else
        color = disabled_color
      end
      if SKILL_SET_NAMES[index] == nil
        self.contents.draw_text(4, y, 288, 32, "Undefined name #{index}")
      else
        self.contents.draw_text(4, y, 288, 32, SKILL_SET_NAMES[index])
      end
    else
      draw_item_sss_later(index)
    end
  end
  
  alias upd_sss_later update
  def update
    upd_sss_later
    if $game_system.SKILL_SEPARATION
      size, old_index = @skill_ids[@index].size, @alt_index[@index]
      if Input.repeat?(Input::RIGHT)
        @alt_index[@index] = (@alt_index[@index] + 1) % size
        if old_index != @alt_index[@index]
          $game_system.se_play($data_system.cursor_se)
          draw_item(@index)
        else
          $game_system.se_play($data_system.buzzer_se)
        end
      elsif Input.repeat?(Input::LEFT)
        @alt_index[@index] = (@alt_index[@index] + size - 1) % size
        if old_index != @alt_index[@index]
          $game_system.se_play($data_system.cursor_se)
          draw_item(@index)
        else
          $game_system.se_play($data_system.buzzer_se)
        end
      end
    end
  end
  
  alias skill_sss_later skill
  def skill
    return skill_sss_later unless $game_system.SKILL_SEPARATION
    id = @skill_ids[@index][@alt_index[@index]]
    return $data_skills[id] if id != 0
  end
  
end

#==============================================================================
# Multi-Hit by Blizzard
# Version: 1.0
# Type: Weapon/Skill/Enemy Enhancement
# Date: 12.8.2007
# 
# 
# Compatibility:
# 
#   90% compatible with SDK 1.x. 60% compatible with SDK 2.x. Might be
#   incompatible with exotic skills and/or CBS-es. Compatible with CRLS 5.1b or
#   higher.
# 
# 
# Explanation:
# 
#   This add-on will allow that skills and weapons attack more than once.
# 
# 
# Configuration:
# 
#   There are 3 configurations. Configuration 1 is for weapons, Configuration 2
#   is for skills and Configuration 3 is for normal enemy attacks. Use
#   following template to set up how many hits should be done:
# 
#     when ID then return HITS
# 
#   ID   - ID of weapon, skill or enemy, depending on the configuration number
#   HITS - number of hits
#==============================================================================

#==============================================================================
# Game_System
#==============================================================================

class Game_System
  
  def weapon_hits(id)
    case id
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration 1
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    when 1 then return 3
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration 1
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    end
    return 1
  end
  
  def skill_hits(id)
    case id
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration 2
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    when 58 then return 2
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration 2
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    end
    return 1
  end
  
  def enemy_hits(id)
    case id
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration 3
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    when 1 then return 3
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration 3
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    end
    return 1
  end
  
end

#==============================================================================
# Scene_Battle
#==============================================================================

class Scene_Battle
  
  alias update_phase4_step1_multi_hit_later update_phase4_step1
  def update_phase4_step1
    update_phase4_step1_multi_hit_later
    @repeat = [1, 1, 0]
    if $game_system.MULTI_HIT
      @skill_use_flag = false
      if @active_battler != nil
        if @active_battler.current_action.kind == 0
          if @active_battler.current_action.basic == 0
            if @active_battler.is_a?(Game_Actor)
              hits = $game_system.weapon_hits(@active_battler.weapon_id)
            elsif @active_battler.is_a?(Game_Enemy)
              hits = $game_system.enemy_hits(@active_battler.id)
            end
            @repeat = [1, 1, 2]
          end
        else
          @repeat[2] = 3
        end
      end
    end
  end
  
  alias update_phase4_step2_multi_hit_later update_phase4_step2
  def update_phase4_step2
    update_phase4_step2_multi_hit_later
    if $game_system.MULTI_HIT && @repeat[2] == 3
      hits = $game_system.skill_hits(@skill.id)
      @repeat = [hits, hits+1, 4]
    end
  end
  
  alias update_phase4_step5_multi_hit_later update_phase4_step5
  def update_phase4_step5
    update_phase4_step5_multi_hit_later
    if $game_system.MULTI_HIT
      @phase4_step = 2 if @repeat[0] > 1 && @repeat[2] > 0
      @repeat[0] -= 1
    end
  end
  
  alias make_skill_action_result_multi_hit_later make_skill_action_result
  def make_skill_action_result
    make_skill_action_result_multi_hit_later
    if @repeat[0] != @repeat[1] || @repeat[2] != 3
      if $game_system._1_SP && @active_battler.states.include?(ONE_SP_ID)
        @active_battler.sp += [1, @skill.sp_cost].min
      elsif $game_system.HALF_SP && @active_battler.states.include?(HALF_SP_ID)
        @active_battler.sp += (@skill.sp_cost/2.0).ceil
      else
        @active_battler.sp += @skill.sp_cost
      end
      @status_window.refresh
    end
  end
  
end

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                                                                             #
#  ##### #####  ###  ##### #   # #####    ##### ##### ##### #####  ###  ##### #
#  #       #   #   #   #   #   # #        #     #     #     #     #   #   #   #
#  #####   #   #   #   #   #   # #####    ####  ####  ####  ####  #       #   #
#      #   #   #####   #   #   #     #    #     #     #     #     #   #   #   #
#  #####   #   #   #   #    ###  #####    ##### #     #     #####  ###    #   #
#                                                                             #
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

#==============================================================================
# Zombie Status Effect by Blizzard
# Version: 1.1b
# Type: Game Experience Improvement
# Date: 26.9.2006
# Date v1.1b: 18.3.2007
# 
# new in 1.1b:
#   - working itself without you needing to do anything except the
#     configuration
#   - actual code
#   - works with attacks and items now as well
# 
# 
# Configuration:
# 
#   ZOMBIE_ID        - the ID of the Zombie status effect
#   LIGHT_ELEMENT_ID - the ID of the light element
#   ZOMBIE_POWER     - how much stronger should light attacks be
#==============================================================================

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

ZOMBIE_ID = 23
LIGHT_ELEMENT_ID = 7
ZOMBIE_POWER = 1.5

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#==============================================================================
# Game_Battler
#==============================================================================

class Game_Battler
  
  alias skill_effect_zombie_later skill_effect
  def skill_effect(user, skill)
    last_hp = self.hp
    last_sr = self.sr if $crls && self.is_a?(Game_Actor)
    result = skill_effect_zombie_later(user, skill)
    if $game_system.ZOMBIE_STATUS && result && @states.include?(ZOMBIE_ID)
      self.sr = last_sr if $crls && self.is_a?(Game_Actor)
      if self.damage.is_a?(Numeric) && self.damage < 0
        self.damage = -self.damage 
        self.hp = last_hp - self.damage
      end
      if skill.element_set.include?(LIGHT_ELEMENT_ID)
        self.damage = (self.damage * ZOMBIE_POWER).to_i
        self.hp = last_hp - self.damage
      end
    end
    return result
  end
  
  alias attack_effect_zombie_later attack_effect
  def attack_effect(attacker)
    last_hp = self.hp
    last_sr = self.sr if $crls && self.is_a?(Game_Actor)
    result = attack_effect_zombie_later(attacker)
    if $game_system.ZOMBIE_STATUS && result && @states.include?(ZOMBIE_ID)
      self.sr = last_sr if $crls && self.is_a?(Game_Actor)
      if self.damage.is_a?(Numeric) && self.damage < 0
        self.damage = -self.damage 
        self.hp = last_hp - self.damage
      end
      if skill.element_set.include?(LIGHT_ELEMENT_ID)
        self.damage = (self.damage * ZOMBIE_POWER).to_i
        self.hp = last_hp - self.damage
      end
    end
    return result
  end
  
  alias item_effect_zombie_later item_effect
  def item_effect(item)
    last_hp = self.hp
    last_sr = self.sr if $crls && self.is_a?(Game_Actor)
    result = item_effect_zombie_later(item)
    if $game_system.ZOMBIE_STATUS && result && @states.include?(ZOMBIE_ID)
      self.sr = last_sr if $crls && self.is_a?(Game_Actor)
      if self.damage.is_a?(Numeric) && self.damage < 0
        self.damage = -self.damage 
        self.hp = last_hp - self.damage
      end
      if skill.element_set.include?(LIGHT_ELEMENT_ID)
        self.damage = (self.damage * ZOMBIE_POWER).to_i
        self.hp = last_hp - self.damage
      end
    end
    return result
  end
  
end

#==============================================================================
# Regen Status Effect by Blizzard
# Version: 1.1b
# Type: Game Experience Improvement
# Date: 4.5.2006
# Date v1.1b: 12.1.2007
# 
# new in 1.1b:
#   - fixed glitches, improved code and made it possible to have Regen and
#     Poison at the same time (they nullificate each other on the map, but not
#     in battle)
#==============================================================================

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

REGEN_ID = 18 # set this to the status effect ID that will be Regen

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#==============================================================================
# Game_Party
#==============================================================================

class Game_Party
  
  alias check_map_slip_damage_regen_later check_map_slip_damage
  def check_map_slip_damage
    check_map_slip_damage_regen_later
    if $game_system.REGEN_STATUS
      for actor in @actors
        if actor.hp > 0 && actor.states.include?(REGEN_ID)
          actor.hp += [actor.maxhp / 100, 1].max
        end
      end
    end
  end
  
end

#==============================================================================
# Game_Battler
#==============================================================================

class Game_Battler

  alias slip_damage_regen_later? slip_damage?
  def slip_damage?
    if $game_system.REGEN_STATUS
      return true if @states.include?(REGEN_ID) && !$scene.is_a?(Scene_Map)
    end
    return slip_damage_regen_later?
  end
  
  alias slip_damage_effect_regen_later slip_damage_effect
  def slip_damage_effect
    if $game_system.REGEN_STATUS
      if !@states.include?(REGEN_ID) && slip_damage?
        slip_damage_effect_regen_later
      elsif @states.include?(REGEN_ID)
        dam = -self.maxhp / 10
        if dam.abs > 0
          amp = [dam.abs * 15 / 100, 1].max
          dam -= rand(amp+1) + rand(amp+1) - amp
        end
        self.hp -= dam
        self.damage = 0 if self.damage == nil
        self.damage += dam
      end
    else
      slip_damage_effect_regen_later
    end
  end

end

#==============================================================================
# Auto-Revive by Blizzard
# Version: 1.21b
# Type: Game Experience Improvement
# Date: 5.6.2006
# Date v1.2b: 14.11.2006
# Date v1.21b: 12.1.2007
# 
# new in 1.2b
#   - less and better code, much more compatible, easier to use
# 
# new in 1.21b
#   - removed an obsolete constant
#==============================================================================

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

AUTO_REVIVE_ID = 19 # ID of the status effect
REVIVE_ANIMATION_ID = 25 # ID of the Revive animation
REVIVE_TEXT = 'Auto-Revive!' # Text displayed

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#==============================================================================
# Game_Party
#==============================================================================

class Game_Party

  alias all_dead_autorevive_later? all_dead?
  def all_dead?
    return all_dead_autorevive_later? unless $game_system.AUTO_REVIVE
    for actor in @actors
      return false if actor.states.include?(AUTO_REVIVE_ID)
    end
    return all_dead_autorevive_later?
  end

end

#==============================================================================
# Sprite
#==============================================================================

class RPG::Sprite
  
  alias damage_regen_later damage
  def damage(damage, critical)
    if damage == REVIVE_TEXT
      dispose_damage
      bitmap = Bitmap.new(160, 48)
      bitmap.font.name = 'Arial Black'
      bitmap.font.size = 32
      bitmap.font.color.set(0, 0, 0) 
      bitmap.draw_text(-1, 12-1, 160, 36, REVIVE_TEXT, 1)
      bitmap.draw_text(-1, 12+1, 160, 36, REVIVE_TEXT, 1)
      bitmap.draw_text(1, 12-1, 160, 36, REVIVE_TEXT, 1)
      bitmap.draw_text(1, 12+1, 160, 36, REVIVE_TEXT, 1)
      bitmap.font.color.set(0, 192, 255)
      bitmap.font.size = 32
      bitmap.draw_text(0, 12, 160, 36, REVIVE_TEXT, 1)
      @_damage_sprite = ::Sprite.new(self.viewport) 
      @_damage_sprite.bitmap = bitmap 
      @_damage_sprite.ox = 80 
      @_damage_sprite.oy = 20 
      @_damage_sprite.x = self.x 
      @_damage_sprite.y = self.y - self.oy / 2 
      @_damage_sprite.z = 3000 
      @_damage_duration = 40 
    else
      damage_regen_later(damage, critical)
    end
  end 

end

#==============================================================================
# Scene_Battle
#==============================================================================

class Scene_Battle

  alias judge_autorevive_later judge
  def judge
    if $game_system.AUTO_REVIVE
      for actor in $game_party.actors
        if actor.states.include?(AUTO_REVIVE_ID) && actor.hp == 0
          actor.hp += actor.maxhp / 5
          actor.remove_state(AUTO_REVIVE_ID)
          actor.remove_state(1)
          actor.animation_id = REVIVE_ANIMATION_ID
          actor.damage = REVIVE_TEXT
          actor.damage_pop = true
          @status_window.refresh
        end
      end
    end
    return judge_autorevive_later
  end

end

#==============================================================================
# Fury Status by Blizzard
# Version: 1.0b
# Type: Game Experience Improvement
# Date: 10.10.2006
# 
# 
# Compatibility:
# 
#   99% compatible with SDK v1.x. 70% compatible with SDK v2.x. Could cause
#   problems with exotic CBS-es.
# 
# 
# Instructions:
# 
# - Explanation:
# 
#   This add-on will make specific characters get inflicted with the status
#   effect called "Fury" if another specific character gets killed during battle.
#   Also make the status effect end after the battle is over.
# 
# - Configuration:
# 
#   Configure your database further below like this template:
# 
#     when X then return Y
# 
#   X - ID of the dead character
#   Y - ID of the character who will inflicted with Fury.
#   
#   Set FURY_ID to the status effect ID.
# 
# If you find any bugs, please report them here:
# http://www.chaosproject.co.nr/
#==============================================================================

FURY_ID = 23

#==============================================================================
# Scene_Battle
#==============================================================================

class Scene_Battle
  
  alias upd_fury_later update
  def update
    if $game_system.FURY_STATUS
      ids = []
      for actor in $game_party.actors
        ids.push(database(actor.id)) if actor.dead?
      end
      for actor in $game_party.actors
        actor.remove_state(FURY_ID)
      end
      for id in ids
        if $game_actors[id] != nil && $game_party.actors.include?($game_actors[id])
          $game_actors[id].add_state(FURY_ID) unless $game_actors[id].dead?
        end
      end
    end
    upd_fury_later
  end
  
  def database(id)
    case id
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Fury Database
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    when 1 then return 2
    when 2 then return 7
    when 7 then return 8
    when 8 then return 1
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Fury Database
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    else
      return 0
    end
  end
  
end
  
#==============================================================================
# Invincible Status by Blizzard
# Version: 1.0b
# Type: Game Experience Improvement
# Date: 4.12.2006
# 
# 
# Compatibility:
# 
#   99% compatible with SDK v1.x. 70% compatible with SDK v2.x. Could cause
#   problems with exotic CBS-es.
# 
# 
# Instructions:
# 
# - Explanation:
# 
#   This add-on will allow having a status effect that makes a character
#   invincible. Set INVINCIBLE_ID to the status effect ID.
#==============================================================================

INVINCIBLE_ID = 17

#==============================================================================
# Game_Battler
#==============================================================================

class Game_Battler

  alias hp_actor_invincible_later hp=
  def hp=(val)
    if $game_system.INVINCIBLE_STATUS
      return if @states.include?(INVINCIBLE_ID) && val < @hp
    end
    hp_actor_invincible_later(val)
  end
  
  def damage=(val)
    @damage = val
    if $game_system.INVINCIBLE_STATUS && val.is_a?(Numeric)
      @damage = 0 if @states.include?(INVINCIBLE_ID) && val > 0
    end
  end

end

#==============================================================================
# Half SP by Blizzard
# Version: 1.4b
# Type: Game Experience Improvement
# Date: 8.4.2006
# Date v1.3b: 13.12.2006
# Date v1.31b: 12.3.2007
# Date v1.4b: 24.3.2007
# 
# new in v1.3b:
#   - totally overworked and improved code
# 
# new in v1.31b:
#   - fixed a glitch
# 
# new in 1.4b:
#   - compatible with Skill Separation System
# 
# 
# Compatibility:
# 
#   99% compatible with SDK v1.x. 70% compatible with SDK v2.x. Should be 100%
#   compatible with everything else. Can cause incompatibility issues with
#   exotic CBS-es and exotic CMS-es, but only if different Skills Windows are
#   used. There is a high chance that this problem can be solved by renaming
#   the defined class "Window_Skill" just below into the name of the class your
#   CBS/CMS is using. The exact line is triple commented with ###. To avoid
#   problems with manual setting the SP, use negative value of the maximum
#   possible SP and to set it to zero and afterwards increase it to the desired
#   value. (sp = -maxsp; sp = X)
# 
# 
# Explanation:
# 
#   This add-on will allow having a status effect that halves SP consumption
#   during usage of skills. Set HALF_SP_ID to the status effect ID.
#==============================================================================

HALF_SP_ID = 22

#==============================================================================
# Game_Battler
#==============================================================================

class Game_Battler
  
  alias sp_actor_halfsp_later sp=
  def sp=(val)
    if val < self.sp && $game_system.HALF_SP && @states.include?(HALF_SP_ID)
      val += (self.sp - val) / 2
    end
    sp_actor_halfsp_later(val)
  end
  
  alias skill_can_use_halfsp_later? skill_can_use?
  def skill_can_use?(skill_id)
    if $game_system.HALF_SP && self.states.include?(HALF_SP_ID)
      return false if ($data_skills[skill_id].sp_cost/2.0).ceil > self.sp
    end
    return skill_can_use_halfsp_later?(skill_id)
  end
  
end

#==============================================================================
# Window_Skill
#==============================================================================

class Window_Skill < Window_Selectable ###
  
  alias draw_item_halfsp_later draw_item
  def draw_item(index)
    draw_item_halfsp_later(index)
    if $game_system.HALF_SP && @actor.states.include?(HALF_SP_ID)
      if $game_system.SKILL_SEPARATION
        y = index * 32
        rect = Rect.new(0, y, self.width / @column_max - 32, 32)
        self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
        id = @skill_ids[index][@alt_index[index]]
        skill = $data_skills[id] if id != 0
        if skill != nil
          if @actor.skill_can_use?(skill.id)
            self.contents.font.color = normal_color
          else
            self.contents.font.color = disabled_color
          end
          bitmap = RPG::Cache.icon(skill.icon_name)
          opacity = self.contents.font.color == normal_color ? 255 : 128
          self.contents.blt(200+$x_off, y+4, bitmap, Rect.new(0, 0, 24, 24), opacity)
          self.contents.draw_text(228+$x_off, y, 204, 32, skill.name, 0)
          self.contents.draw_text(516, y, 64, 32, (skill.sp_cost/2.0).ceil.to_s, 2)
          if @skill_ids[index].size > 1
            self.contents.draw_text(184+$x_off, y, 32, 32, '«')
            self.contents.draw_text(564, y, 32, 32, '»', 2)
          end
        else
          self.contents.font.color = disabled_color
          self.contents.draw_text(228+$x_off, y, 204, 32, 'not available')
        end
        if id == 0
          color = disabled_color
        elsif @actor.skill_can_use?(id)
          color = normal_color
        else
          color = disabled_color
        end
        if SKILL_SET_NAMES[index] == nil
          self.contents.draw_text(4, y, 288, 32, 'Undefined name')
        else
          self.contents.draw_text(4, y, 288, 32, SKILL_SET_NAMES[index])
        end
      else
        skill = @data[index]
        if @actor.skill_can_use?(skill.id)
          self.contents.font.color = normal_color
        else
          self.contents.font.color = disabled_color
        end
        sp_cost = (skill.sp_cost / 2.0).ceil
        x = 4 + index % 2 * (288 + 32)
        y = index / 2 * 32
        rect = Rect.new(x + 232, y, 48, 32)
        self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
        self.contents.draw_text(x + 232, y, 48, 32, sp_cost.to_s, 2)
      end
    end
  end

end

#==============================================================================
# 1 SP by Blizzard
# Version: 1.11b
# Type: Game Experience Improvement
# Date: 12.3.2007
# Date v1.1b: 24.3.2007
# Date v1.11b: 26.8.2007
# 
# new in 1.1b:
#   - compatible with Skill Separation System
# 
# new in 1.11b:
#   - fixed bug where 0-SP skills couldn't be used if 1 SP was on
# 
# 
# Compatibility:
# 
#   99% compatible with SDK v1.x. 70% compatible with SDK v2.x. Should be 100%
#   compatible with everything else. Can cause incompatibility issues with
#   exotic CBS-es and exotic CMS-es, but only if different Skills Windows are
#   used. There is a high chance that this problem can be solved by renaming
#   the defined class "Window_Skill" just below into the name of the class your
#   CBS/CMS is using. The exact line is triple commented with ###. To avoid
#   problems with manual setting the SP, use any negative value to set it to
#   zero and afterwards increase it to the desired value. (sp = -1; sp = X)
# 
# 
# Explanation:
# 
#   This add-on will allow having a status effect that sets SP consumption to 1
#   during usage of skills. Set ONE_SP_ID to the status effect ID.
#==============================================================================

ONE_SP_ID = 20

#==============================================================================
# Game_Battler
#==============================================================================

class Game_Battler
  
  alias sp_actor_1_sp_later sp=
  def sp=(val)
    if $game_system._1_SP && val >= 0
      val = self.sp - 1 if val < self.sp && @states.include?(ONE_SP_ID)
    end
    sp_actor_1_sp_later(val)
  end
  
  alias skill_can_use_1_sp_later? skill_can_use?
  def skill_can_use?(skill_id)
    if $game_system._1_SP && self.states.include?(ONE_SP_ID)
      return false if self.sp == 0 && $data_skills.sp_cost > 0
    end
    return skill_can_use_1_sp_later?(skill_id)
  end
  
end

#==============================================================================
# Window_Skill
#==============================================================================

class Window_Skill < Window_Selectable ###
  
  alias draw_item_1_sp_later draw_item
  def draw_item(index)
    draw_item_1_sp_later(index)
    if $game_system._1_SP && @actor.states.include?(ONE_SP_ID)
      if $game_system.SKILL_SEPARATION
        y = index * 32
        rect = Rect.new(0, y, self.width / @column_max - 32, 32)
        self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
        id = @skill_ids[index][@alt_index[index]]
        skill = $data_skills[id] if id != 0
        if skill != nil
          if @actor.skill_can_use?(skill.id)
            self.contents.font.color = normal_color
          else
            self.contents.font.color = disabled_color
          end
          bitmap = RPG::Cache.icon(skill.icon_name)
          opacity = self.contents.font.color == normal_color ? 255 : 128
          self.contents.blt(200+$x_off, y+4, bitmap, Rect.new(0, 0, 24, 24), opacity)
          self.contents.draw_text(228+$x_off, y, 204, 32, skill.name, 0)
          self.contents.draw_text(516, y, 64, 32, [1, skill.sp_cost].min.to_s, 2)
          if @skill_ids[index].size > 1
            self.contents.draw_text(184+$x_off, y, 32, 32, '«')
            self.contents.draw_text(564, y, 32, 32, '»', 2)
          end
        else
          self.contents.font.color = disabled_color
          self.contents.draw_text(228+$x_off, y, 204, 32, 'not available')
        end
        if id == 0
          color = disabled_color
        elsif @actor.skill_can_use?(id)
          color = normal_color
        else
          color = disabled_color
        end
        if SKILL_SET_NAMES[index] == nil
          self.contents.draw_text(4, y, 288, 32, 'Undefined name')
        else
          self.contents.draw_text(4, y, 288, 32, SKILL_SET_NAMES[index])
        end
      else
        skill = @data[index]
        if @actor.skill_can_use?(skill.id)
          self.contents.font.color = normal_color
        else
          self.contents.font.color = disabled_color
        end
        x = 4 + index % 2 * (288 + 32)
        y = index / 2 * 32
        rect = Rect.new(x + 232, y, 48, 32)
        self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
        self.contents.draw_text(x + 232, y, 48, 32, [1, skill.sp_cost].min.to_s, 2)
      end
    end
  end

end

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#                                                                             #
#                         ##### #   #  #  #     #                             #
#                         #     #  #   #  #     #                             #
#                         ##### ###    #  #     #                             #
#                             # #  #   #  #     #                             #
#                         ##### #   #  #  ##### #####                         #
#                                                                             #
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

#==============================================================================
# Absorbing SP and HP by Blizzard
# Version: 1.7b
# Type: Enhanced Skill
# Date: 8.5.2006
# Date v1.7b: 14.11.2006
# 
# new in v1.7b:
#   - overworked code, fixed bugs and glitches, added "undead SP"
# 
#   Just include all the skill IDs that are supposed to steal HP/SP. You can
#   also define undead enemies who will (due to common belief...) revert the HP
#   absorb effect. Also you may add any IDs of enemies who use the same undead
#   effect, but on SP, add the IDs into UNDEAD_SP. Note that you can make
#   enemies who only are "undead" for HP stealing, SP stealing or even both.
#==============================================================================

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

SKILL_IDS_HP = [90] # add any Skill IDs and separate them with commas
SKILL_IDS_SP = [91] # add any Skill IDs and separate them with commas
UNDEAD_IDS = [1] # add IDS and separate them with commas
UNDEAD_SP = [32] # add IDS and separate them with commas

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#==============================================================================
# Game_Battler
#==============================================================================

class Game_Battler
  
  alias skill_effect_hpsp_absorb_later skill_effect
  def skill_effect(user, skill)
    @flag = false
    last_hp = self.hp
    last_sr = self.sr if $crls && self.is_a?(Game_Actor)
    result = skill_effect_hpsp_absorb_later(user, skill)
    if $game_system.ABSORB_HP_SP
      if SKILL_IDS_SP.include?(skill.id) && self.damage.is_a?(Numeric)
        self.hp = last_hp
        self.sr = last_sr if $crls && self.is_a?(Game_Actor)
        if self.is_a?(Game_Enemy) && UNDEAD_SP.include?(self.id)
          self.damage = -self.damage
        end
        if self.sp >= self.damage
          self.sp -= self.damage
        else
          self.damage = self.sp
          self.sp = 0
        end
      elsif SKILL_IDS_HP.include?(skill.id) && self.damage.is_a?(Numeric)
        self.hp = last_hp
        self.sr = last_sr if $crls && self.is_a?(Game_Actor)
        if self.is_a?(Game_Enemy) && UNDEAD_IDS.include?(self.id)
          self.damage = -self.damage
        end
        if self.hp >= self.damage
          self.hp -= self.damage
        else
          self.damage = self.hp
          self.hp = 0
        end
      end
    end
    return result
  end
  
end

#==============================================================================
# Scene_Battle
#==============================================================================

class Scene_Battle

  alias update_phase4_step5_hpsp_absorb_later update_phase4_step5
  def update_phase4_step5
    if $game_system.ABSORB_HP_SP
      @help_window.visible = false
      @status_window.refresh
      damages = 0
      for target in @target_battlers
        if target.damage != nil
          target.damage_pop = true
          damages += target.damage if target.damage.is_a?(Numeric)
        end
      end
      @status_window.refresh if check_absorb(@active_battler, 
          @active_battler.current_action.skill_id, damages)
      @skill = nil
      @phase4_step = 6
    else
      update_phase4_step5_hpsp_absorb_later
    end
  end

  def check_absorb(user, id, damage)
    if (SKILL_IDS_HP | SKILL_IDS_SP).include?(id)
      user.hp += damage if SKILL_IDS_HP.include?(id)
      user.sp += damage if SKILL_IDS_SP.include?(id)
      user.damage = -damage
      user.damage_pop = true
      return true
    end
    return false
  end
    
end

#==============================================================================
# Full Reflection System by Blizzard
# Version: 2.0b
# Type: Game Experience Improvement
# Date: 5.9.2006
# Date v1.4: 16.1.2007
# Date v2.0b: 12.3.2007
# 
# 
# new in v1.4:
# 
#   - overworked code and fixed all the glitches
#   - the power comes back X times stronger if it is reflected from X battlers
#     (ie. like in the Final Fantasy series)
#   - spells now get reflected to anybody from the enemy party, not only the
#     user (makes it possible to split damage from the FF feature mentioned
#     above)
#   - added a fix so it works with HP/SP Absorb
# 
# new in v2.0b:
# 
#   - completely overworked and fixed
# 
# 
# Compatibility:
# 
#   97% compatible with SDK v1.x. 60% compatible with SDK v2.x. You might
#   experience problems with exotic CBS-es.
# 
# 
# Configuration:
# 
#   Make a status effect and call it "Reflect". Remember the ID number. Now
#   make an animation that should be displayed when reflecting magic.
# 
#     REFLECT_ID        - the ID of the reflect status
#     REFLECT_ANIMATION - the ID of animation displayed when magic is being
#                         reflecting
#     BREAK_REFLECT     - IDs of skills that go through Reflection no matter
#                         what
#     MISS_DAMAGE       - what is displayed in your game if somebody gets
#                         missed (usually 'Miss')
# 
# Note:
# 
#   A magical skill is considered a skill that has a either INT-F greater than
#   zero or MDEF-F greater than zero. Please note that skills that can disable
#   the reflection status break through the reflection automatically.
# 
# 
# Important note:
# 
#   It is better if you don't use sounds and screen/target flashing in the
#   animation for the reflecting effect.
#==============================================================================

REFLECT_ID = 21
REFLECT_ANIMATION = 103
BREAK_REFLECT = []
MISS_DAMAGE = 'Miss'

#==============================================================================
# Game_Battler
#==============================================================================

class Game_Battler
  
  alias skill_effect_reflect_later skill_effect
  def skill_effect(user, skill, reflect = false)
    if !$game_system.REFLECT || reflect || !test_reflection(skill)
      return skill_effect_reflect_later(user, skill)
    end
    return false
  end
  
  def test_reflection(skill)
    return ((skill.int_f > 0 || skill.mdef_f > 0) &&
        @states.include?(REFLECT_ID) && !BREAK_REFLECT.include?(skill.id) &&
        !skill.minus_state_set.include?(REFLECT_ID))
  end
  
end

#==============================================================================
# Scene_Battle
#==============================================================================

class Scene_Battle
  
  alias main_reflect_later main
  def main
    @old_targets = []
    main_reflect_later
  end
  
  alias set_target_battlers_reflect_later set_target_battlers
  def set_target_battlers(scope, override = false)
    if $game_system.REFLECT && !BREAK_REFLECT.include?(@skill.id) &&
        !override && @active_battler.current_action.kind == 1
      return []
    end
    return set_target_battlers_reflect_later(scope)
  end
  
  alias make_skill_action_result_reflect_later make_skill_action_result
  def make_skill_action_result
    make_skill_action_result_reflect_later
    if $game_system.REFLECT && !BREAK_REFLECT.include?(@skill.id)
      set_target_battlers(@skill.scope, true)
      for i in 0...@target_battlers.size
        if @skill != nil && @active_battler.current_action.kind == 1 &&
            @target_battlers[i].test_reflection(@skill)
          new_target = swap_targets(@target_battlers[i], @active_battler)
          if @target_battlers[i] != new_target
            @old_targets.push(@target_battlers[i])
            @target_battlers[i] = new_target
          end
        end
      end
      for target in @target_battlers
        dam = (target.damage.is_a?(Numeric) ? target.damage : 0)
        target.skill_effect(@active_battler, @skill, true)
        target.damage += dam if target.damage.is_a?(Numeric)
        target.animation_hit = (target.damage != MISS_DAMAGE)
      end
    end
  end
  
  alias update_phase4_step4_reflect_later update_phase4_step4
  def update_phase4_step4
    if $game_system.REFLECT
      for target in @old_targets
        target.animation_id = REFLECT_ANIMATION
      end
      @old_targets = []
    end
    update_phase4_step4_reflect_later
  end
  
  def swap_targets(battler1, battler2)
    if battler1.is_a?(Game_Enemy) && battler2.is_a?(Game_Enemy)
      actors = []
      for actor in $game_party.actors
        actors.push(actor) if actor.exist?
      end
      battler3 = actors[rand(actors.size)]
    elsif battler1.is_a?(Game_Actor) && battler2.is_a?(Game_Actor)
      enemies = []
      for enemy in $game_troop.enemies
        enemies.push(enemy) if enemy.exist?
      end
      battler3 = enemies[rand(enemies.size)]
    elsif battler1.is_a?(Game_Enemy) && battler2.is_a?(Game_Actor)
      actors = []
      for actor in $game_party.actors
        actors.push(actor) if actor.exist?
      end
      battler3 = actors[rand(actors.size)]
    elsif battler1.is_a?(Game_Actor) && battler2.is_a?(Game_Enemy)
      enemies = []
      for enemy in $game_troop.enemies
        enemies.push(enemy) if enemy.exist?
      end
      battler3 = enemies[rand(enemies.size)]
    else
      battler3 = battler2
    end
    if SKILL_IDS_HP != nil && SKILL_IDS_SP != nil &&
        SKILL_IDS_HP.include?(@skill) || SKILL_IDS_SP.include?(@skill)
      loop do
        break if battler2 != battler3
        if battler2.is_a?(Game_Actor)
          actors = []
          for actor in $game_party.actors
            actors.push(actor) if actor.exist?
          end
          battler3 = actors[rand(actors.size)]
        elsif battler2.is_a?(Game_Enemy)
          enemies = []
          for enemy in $game_troop.enemies
            enemies.push(enemy) if enemy.exist?
          end
          battler3 = enemies[rand(enemies.size)]
        end
      end
    end
    return battler3
  end
  
end

#==============================================================================
# Death Roulette by Blizzard
# Version: 1.0
# Type: Enhanced Skill
# Date: 7.8.2006
# 
# 
#   This skill will kill a random target: hero or enemy. To make somebody
#   immune to this skill, just set the immunity to the Death Status effect to
#   F. Make the skill target nobody.
#==============================================================================

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

DEATH_ROULETTE_IDS = [666] # add any Skill IDs and separate them with commas
DEAD_ID = 1 # the Status effect ID of the "dead" Status effect

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#==============================================================================
# Scene_Battle
#==============================================================================

class Scene_Battle
  
  alias make_skill_action_result_death_roulette_later make_skill_action_result
  def make_skill_action_result
    if $game_system.DEATH_ROULETTE &&
        DEATH_ROULETTE_IDS.include?(@active_battler.current_action.skill_id)
      roulette = []
      for enemy in $game_troop.enemies
        roulette.push(enemy) if enemy.exist?
      end
      for actor in $game_party.actors
        roulette.push(actor) unless actor.dead?
      end
      @target_battlers = [roulette[rand(roulette.size)]]
      @target_battlers = [$game_party.actors[0]]
      make_skill_action_result_death_roulette_later
      immune = @target_battlers[0].state_ranks[DEAD_ID]
      if [0, 6].include?(immune)
        @target_battlers[0].damage = 'Can\'t kill'
      else
        @target_battlers[0].hp = 0
        @target_battlers[0].damage = 'Dead!'
      end
    else
      make_skill_action_result_death_roulette_later
    end
  end
    
end

#==============================================================================
# Blue Magic via skill by Blizzard
# Version: 1.0
# Type: Enhanced Skill
# Date: 14.11.2006
# 
# 
#   This actor will learn one of the enemy's skills. Making this skill target
#   all enemies, ONLY ONE SKILL WILL BE LEARNED FROM A RANDOM ENEMY! Make the
#   skill do no damage to the enemy and use the hit rate to determine the
#   success chance of the skill.
#==============================================================================

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

BLUE_MAGIC_IDS = [92] # add any Skill IDs and separate them with commas

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#==============================================================================
# Scene_Battle
#==============================================================================

class Scene_Battle
  
  alias make_skill_action_result_blue_later make_skill_action_result
  def make_skill_action_result
    make_skill_action_result_blue_later
    if $game_system.BLUE_MAGIC_SKILL
      if BLUE_MAGIC_IDS.include?(@active_battler.current_action.skill_id)
        @target_battlers.each {|target| target.damage = nil}
        target = @target_battlers[rand(@target_battlers.size)]
        if target.is_a?(Game_Enemy)
          if rand(100) < $data_skills[@active_battler.current_action.skill_id].hit
            ids = []
            for action in target.actions
              ids.push(action.skill_id) if action.kind == 1
            end
            if ids.size > 0
              skill = $data_skills[ids[rand(ids.size)]]
              if @active_battler.skills.include?(skill.id)
                target.damage = "#{skill.name} known"
              else
                @active_battler.learn_skill(skill.id)
                target.damage = "#{skill.name} learned"
              end
            else
              target.damage = 'None available'
            end
          else
            target.damage = 'Miss'
          end
        end
      end
    end
  end
    
end

#==============================================================================
# EMP Skill by Blizzard
# Version: 1.01b
# Type: Enhanced Skill
# Date: 7.3.2007
# Date v1.01b: 12.3.2007
# 
# new in v1.01b:
#   - fixed an incompatiblity bug with Reflect
# 
# 
# Explanation:
# 
#   This skill paralyzes all enemies that are machines. 
# 
# 
# Configuration:
# 
#   Give your enemies the element with ID $MACHINE_ELEMENT and set it to "A" if
#   you want the skill to affect that enemy. Set the PARA_ID to the Status
#   element ID you want to inflict (basically it's paralyze, but you don't have
#   to use paralyze...). Set EMP_ID to the skill ID. Set EMP_DAMAGE to the text
#   displayed when an enemy is shut down (set it to "" for none).
#==============================================================================

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

EMP_ID = 95
PARA_ID = 8
EMP_DAMAGE = 'Shut Down!'
$MACHINE_ELEMENT = 10
if $DUMMY_ELEMENTS == nil
  $DUMMY_ELEMENTS = [$MACHINE_ELEMENT] ### add more dummy elements if you have any
else
  $DUMMY_ELEMENTS.push($MACHINE_ELEMENT)
end

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#==============================================================================
# Game_Battler
#==============================================================================

class Game_Battler
  
  def elements_correct(elements)
    multiplier = size = 0
    for i in elements
      unless $DUMMY_ELEMENTS.include?(i)
        multiplier += self.element_rate(i)
        size += 1
      end
    end
    return (size == 0 ? 100 : multiplier/size)
  end
  
end

#==============================================================================
# Game_Enemy
#==============================================================================

class Game_Enemy < Game_Battler
  
  alias skill_effect_emp_skill_later skill_effect
  def skill_effect(user, skill, flag = false)
    if $game_system.EMP_SKILL && skill.id == EMP_ID && self.is_a?(Game_Enemy) &&
        $data_enemies[self.id].element_ranks[$MACHINE_ELEMENT] == 1
      self.add_state(PARA_ID)
      self.damage = EMP_DAMAGE
      return true
    end
    return skill_effect_emp_skill_later(user, skill, flag)
  end
  
end

#==============================================================================
# Demi Skill by Blizzard
# Version: 1.0b
# Type: Enhanced Skill
# Date: 12.7.2007
# 
# 
# Explanation:
# 
#   This skill deals damage equal to a percentage of the remaining HP.
# 
# 
# Configuration:
# 
#   Scroll down to START Demi Database and create Demi skills. This system work
#   on both sides, both enemies and actors can use it.
#==============================================================================

#==============================================================================
# Game_System
#==============================================================================

class Game_System
  
  def demi_database(id)
    case id
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Demi Database
# 
#   Use following template to create Demi skills:
# 
#     when ID then return RATE
# 
#   ID   - ID of the skill in the database
#   RATE - percentage of how much of the remaining HP should be taken away
# 
# Example:
# 
#   when 88 then return 25
#   Skill with ID 88 will do damage equal to 25% of the enemies' remaining HP.
# 
#   Note that using values equal to or greater than 100 will kill instantly.
#   Negative values will heal instead.
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    when 88 then return 25
    when 89 then return 50
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Demi Database
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    end
    return 0
  end
  
end

#==============================================================================
# Game_Battler
#==============================================================================

class Game_Enemy < Game_Battler
  
  alias skill_effect_demi_skill_later skill_effect
  def skill_effect(user, skill, flag = false)
    last_hp = self.hp
    last_sr = self.sr if $crls && self.is_a?(Game_Actor)
    result = skill_effect_demi_skill_later(user, skill, flag)
    if $game_system.DEMI_SKILL
      rate = $game_system.demi_database(skill.id)
      if result && rate > 0
        self.sr = last_sr if $crls && self.is_a?(Game_Actor)
        self.damage = last_hp * rate / 100
        self.hp = last_hp - self.damage
      end
    end
    return result
  end
  
end
