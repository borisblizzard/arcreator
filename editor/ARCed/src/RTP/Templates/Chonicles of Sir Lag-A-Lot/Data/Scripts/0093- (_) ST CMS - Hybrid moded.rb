#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=
# StormTronics CMS by Blizzard
# Version: 5.0b - Hybrid Edition
# Type: Enhanced Custom Menu System
# Date v5.0: 27.8.2007
# Date v5.0b: unreleased
#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=
# 
# Compatibility:
# 
#   97% compatible with SDK v1.x. 80% compatible with SDK v2.x. Glitchs with
#   Fukuyama's Caterpillar script (but not with mine). Designed only for 8
#   elements. WILL corrupt old savegames.
# 
# 
# Features:
# 
#   - completely animated and graphically optimized (lag-free)
#   - own set of windowskins, fonts and icons for every status change and
#     element
#   - saves all changed options together with the savefile
#   - menu commands "Item", "Equipment", "Skill", "Equip", "Status", "Options",
#     "Save", "Load", "Exit"
#   - Item submenu: "Items", "Sort" (by quantity or by alphabet), "Quest Items"
#   - Equipment submenu shows information about equippable items for the chosen
#     character, switch the character with LEFT and RIGHT
#   - Skill submenu shows available skills for use for the chosen character,
#     switch character with L and R, menu status window in background shows the
#     chosen character
#   - Equip submenu shows complete information about Status resistance/attack,
#     Element resistance/attack and complete character stat changing (has
#     even "max HP" and "max SP" available if you are using "Weapon/Armor HP/SP
#     Plus")
#   - Status screen with overall information about character status
#   - Options submenu with "BGM Volume", "SFX Volume", "Battle BGM",
#     "Battle Cam" (if using KGC's Pseudo 3D Battle Camera with my add-on for
#     disabling), "Bar Style", "Bar Opacity" (if you are using Gradient Bar
#     Styler), "Font" and "Windowskin" (both with preview)
#   - Standard Save, Load and Exit commands
#   - uses "Ultimate Font Override", so the font changes will affect RPG Maker
#     XP versions 1.00, 1.01, 1.02 and 1.03 (including Dyna Edition and
#     Postality Knights Edition Enhanced) and the font even gets saved with the
#     savedata
# 
# new in Hybrid Edition:
#   - supports either windowskin background or custom images:
#                >>>  All StormTronics CMS Editions in one!  <<<
#   - compatible with all my scripts (even DREAM v4.0)
#   - draws SR in the menu if CLRS was detected
#   - supports any number of party members
#   - removed some special add-ons, please get Tons of Add-ons if you want to
#     continue using them, ST CMS will recognize Tons v4.98b and higher
#   - more than 1500 code lines less than Nemesis Edition and almost 2000
#     code lines less than Metal-Plate Edition
#   - removes options from Options menu that are not / cannot being used at all
#   - possibility to use a different equip system
#   - doesn't need skin icons anymore, the icon is drawn from the skin directly
#   - improved windowskins from "The Legend of Lexima™ IV - Chaos Project"
# 
# 
# Instructions:
# 
#   Copy your character faces into a the folder called "Characters". The
#   facesets MUST have the same names as the character spritesets with a _face
#   added at the end. Also copy the windowskins and the icons. Don't forget to
#   include the font files used by the game in your game folder. Also change
#   the variable ID in the conditional branches if you use another variable
#   than 49.
# 
# 
# Configuration:
# 
#   CAM_AVAILABLE       - set to true if you use KGC 3DPBC
#   FACESETS            - set to true if you want to use facesets
#   BGM_Variable        - ID number of the variable for the Battle BGM changer
#   BGM_Lock            - ID number of the switch used to temporarily disable
#                         the option of changing the Battle BGM, for that, just
#                         turn the switch on and off to disable and enable this
#                         option
#   WEAPONS_AND_ARMORS  - set to false to not show weapons and armors in the
#                         Item screen
#   $quest_items        - add any item IDs that are supposed to be quest items,
#                         so the CMS can separate them
#   BATTLE_BGMS         - add any battle BGMs you are using
#   SKINS               - add any skin name you are using
#   SKINS               - add any font name you are using, be sure to include
#                         the font install files in your game release as some
#                         people may not have those fonts installed
#   SAVE_NAME           - name of your savefiles (usually "Save")
#   SAVE_EXTENSION      - extension of your savefiles (usually "rxdata")
#   SAVE_FILES_NUMBER   - number of savefiles you are using (usually 4)
#   MAP_BACKGROUND      - set to true to show map as background, otherwise
#                         if CMS_EDITION is not nil or false the
#                         "CMSFullscreen" image will be displayed
#   CUSTOM_EQUIP_SCENE  - set this to true if you want to use a different equip
#                         scene and make this CMS compatible even with exotic
#                         Equipment Systems
#   FONT_BACKGROUND_FIX - set this to true if you want dark font colors to be
#                         used in the menu, this comes in handy when the
#                         custom background images you use are bright
#   MIRROR              - flips all horizontal window positions
#   CMS_EDITION         - set this to false or nil if you want to use Nemesis
#                         Edition, set to folder name where in the Pictures/CMS
#                         the images should be loaded from if you want to use
#                         custom images as background
# 
#   The syntax $game_system.get_cam can be used by an event (Call script
#   command) to restore the user's setting of the KGC 3DPBC if a forced cam
#   control was initiated during an event.
# 
#   You can use $game_system.reset_battle_bgm to reset the battle BGM to the
#   player's menu setting if you have changed it for i.e. a boss fight via
#   event.
# 
# 
# FAQ:
# 
# - Problem:
#   I get an error that some icons can't be found. how do I solve this?
# 
# - Solution:
#   Copy the icons from the demo or download them and place the into the Icons
#   folder into another folder called "CMS". Done.
# 
# - Problem:
#   I still get an error.
# 
# - Solution:
#   Rename the icons. If your elements were renamed and don't have the standard
#   names, your icons need to be renamed as well. Same goes for status effects.
#   Also be sure to add new icons with new names if you have more than the
#   basic 8 elements and/or more than the basic 16 status effects in your
#   database.
# 
# - Question:
#   Can I use my own skins, icons, fonts, battle BGMs, etc...?
# 
# - Answer:
#   Of course. Only be sure to change the appropriate options in the script and
#   to use the appropriate names, so everything can function normally after
#   that.
# 
# - Question:
#   Can this CMS be connected with other scripts? If yes, how and how much work
#   is it?
# 
# - Answer:
#   Yes, it can. A little bit of scripting and enhancing the functions of the
#   CMS are needed if it is going to be connected with other scripts. How much
#   of additional work it can cause only depends how big the script merge is. A
#   simple changing of the battle menu to display status effects in icons
#   should take between 15~30 minutes of scripting and testing. Adding another
#   option into the Options menu should also take only 15~30 minutes of
#   scripting and testing. Even adding an entire series of new windows or
#   implementing another Scene into the menu also won't take more than 30
#   minutes, because the menu itself works with the "sub-scene" system, saving
#   this way RAM and CPU.
# 
# - Question:
#   What is the "sub-scene" system? Also I have tried other animated CMS-es.
#   Why is this one so lag-free?
# 
# - Answer:
#   It is lag-free just because of the "sub-scene" system. This system is also
#   used in the "Scene_Battle". It only creates windows and handels them when
#   they are needed or used, otherwise they get disposed or not created at all.
#   In this script this method is being used to a possible maximum.
# 
# - Question:
#   Is this for real? This CMS doesn't even have 3000 lines of code!
# 
# - Answer:
#   Actually not even 2500 if you don't count the instructions.
# 
# - Question:
#   How is such a large collection of features possible with so relatively few
#   lines of code?!
# 
# - Answer:
#   Smart coding. =P
# 
# 
# Additional scripts/snipplets/add-ons:
# 
#   - Ultimate Font Override v1.0b (by Blizzard)
#   - BGM/SFX Volume Control with volume correction v1.0b (by Blizzard)
#   - Map Name/Location v1.0b (by Blizzard)
#   - Elemental Vulnerability Graph v1.0b (by Blizzard)
#   - Battle BGM control v2.0b (by Blizzard)
#   - Options control layout and funcionality v4.0b (by Blizzard)
#   - CMS layout/funcionality v5.0b (by Blizzard)
#   - optimized code and delagged by "sub-scene" window handling (by Blizzard)
# 
#   If you experience the "Stack level too deep" error, you may already have
#   one of the scripts listed above and it conflicts with itself, because of
#   aliased recursive calling. Try removing script by script and testing
#   everything. Don't forget to backup you Scripts.rxdata before doing so.
#   Scripts.rxdata is a file that contains your current scripts and is located
#   in the Data folder of your game folder.
# 
# 
# If you find any bugs, please report them here:
# http://www.chaosproject.co.nr
#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# basic config
CAM_AVAILABLE = false
FACESETS = false
BGM_Variable = 49
BGM_Lock = 49
WEAPONS_AND_ARMORS = true
$quest_items = [5, 6, 7, 8, 11, 12, 13]
# custom game configs
BATTLE_BGMS = [
#             ['BGM_NAME', VOLUME, PITCH, 'DISPLAY_NAME']
              ['001-Battle01', 100, 100, 'BGM 1'],
              ['002-Battle02', 100, 100, 'BGM 2'],
              ['003-Battle03', 100, 100, 'BGM 3'],
              ['004-Battle04', 100, 100, 'BGM 4']
              ]
SKINS = ['Original', 'Heavy Gold', 'Hell Breath', 'Liquid Water',
         'Violent Violet', 'Ice Cool', 'Fatal Venom', 'Perfect Chaos',
         'Blizzard Master']
FONTS = ['Arial', 'Future', 'Comic Sans MS', 'Brush Script', 'Tahoma',
         'Times New Roman']
# save file options
SAVE_NAME = 'Save'
SAVE_EXTENSION = 'rxdata'
SAVE_FILES_NUMBER = 4
# extra options
MAP_BACKGROUND = true
CUSTOM_EQUIP_SCENE = false
FONT_BACKGROUND_FIX = false
MIRROR = true
CMS_EDITION = false # 'Metal-Plate'

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

CAM_Variable = 25 if CAM_AVAILABLE # change only if changed in the 3DPBC script

#==============================================================================
# Game_System
#==============================================================================

class Game_System
  
  attr_accessor :bgm_volume
  attr_accessor :sfx_volume
  attr_accessor :cam
  attr_reader   :fontname
  attr_reader   :fontsize
  
  alias init_storm_cms_later initialize
  def initialize
    init_storm_cms_later
    @bgm_volume = @sfx_volume = 100
    @cam = 0
    self.fontname = 'Arial'
    self.fontsize = 24
  end
  
  def fontname=(name)
    Font.default_name = $defaultfonttype = $fontface = @fontname = name
  end
    
  def fontsize=(size)
    Font.default_size = $defaultfontsize = $fontsize = @fontsize = size
  end
  
  def get_cam
    $game_variables[CAM_Variable] = @cam
    return # if an event calls this method the "return" is HIGHLY neccesary!
  end
    
  def reset_battle_bgm
    bgm = BATTLE_BGMS[$game_variables[BGM_Variable]]
    $game_system.battle_bgm = RPG::AudioFile.new(bgm[0], bgm[1], bgm[2])
    return # if an event calls this method the "return" is HIGHLY neccesary!
  end
  
  if $dream_music
  def bgm_play(bgm)
    @playing_bgm = bgm
    if bgm != nil && bgm.name != ''
      vol = correction(@bgm_volume)
      dream_ed = bgm.clone
      dream_ed.volume = dream_ed.volume * vol / 100
      DREAM.play_encrypted_audio('Audio/BGM/', dream_ed, 0)
    else
      Audio.bgm_stop
    end
    Graphics.frame_reset
  end
  
  def bgs_play(bgs)
    @playing_bgs = bgs
    if bgs != nil && bgs.name != ''
      vol = correction(@sfx_volume)
      dream_ed = bgs.clone
      dream_ed.volume = dream_ed.volume * vol / 100
      DREAM.play_encrypted_audio('Audio/BGS/', dream_ed, 1)
    else
      Audio.bgs_stop
    end
    Graphics.frame_reset
  end
  
  def me_play(me)
    if me != nil && me.name != ''
      vol = correction(@bgm_volume)
      dream_ed = me.clone
      dream_ed.volume = dream_ed.volume * vol / 100
      DREAM.play_encrypted_audio('Audio/ME/', dream_ed, 2)
    else
      Audio.me_stop
    end
    Graphics.frame_reset
  end
  
  def se_play(se)
    if se != nil && se.name != ''
      vol = correction(@sfx_volume)
      dream_ed = se.clone
      dream_ed.volume = dream_ed.volume * vol / 100
      DREAM.play_encrypted_audio('Audio/SE/', dream_ed, 3)
    end
  end
  else
  def bgm_play(bgm)
    @playing_bgm = bgm
    if bgm != nil && bgm.name != ''
      vol = correction(@bgm_volume)
      Audio.bgm_play('Audio/BGM/' + bgm.name , bgm.volume * vol / 100, bgm.pitch)
    else
      Audio.bgm_stop
    end
    Graphics.frame_reset
  end
  
  def bgs_play(bgs)
    @playing_bgs = bgs
    if bgs != nil && bgs.name != ''
      vol = correction(@sfx_volume)
      Audio.bgs_play('Audio/BGS/' + bgs.name, bgs.volume * vol / 100, bgs.pitch)
    else
      Audio.bgs_stop
    end
    Graphics.frame_reset
  end
  
  def me_play(me)
    if me != nil && me.name != ''
      vol = correction(@bgm_volume)
      Audio.me_play('Audio/ME/' + me.name, me.volume * vol / 100, me.pitch)
    else
      Audio.me_stop
    end
    Graphics.frame_reset
  end

  def se_play(se)
    if se != nil && se.name != ''
      vol = correction(@sfx_volume)
      Audio.se_play('Audio/SE/' + se.name, se.volume * vol / 100, se.pitch)
    end
  end
  end
  
  def correction(volume)
    case volume
    when 100 then return 100
    when 95 then return 97
    when 90 then return 95
    when 85 then return 92
    when 80 then return 90
    when 75 then return 87
    when 70 then return 85
    when 65 then return 82
    when 60 then return 80
    when 55 then return 77
    when 50 then return 75
    when 45 then return 72
    when 40 then return 70
    when 35 then return 65
    when 30 then return 60
    when 25 then return 55
    when 20 then return 50
    when 15 then return 40
    when 10 then return 35
    when 5 then return 25
    end
    return 0
  end
  
end

#============================================================================== 
# Game_Actor 
#============================================================================== 

class Game_Actor < Game_Battler 
  
  def now_exp 
    return (@exp-@exp_list[@level])
  end 
  
  def next_exp 
    return (@exp_list[@level+1] > 0 ? @exp_list[@level+1]-@exp_list[@level] : 0)
  end 
  
  def test_equip(equip_type, id)
    case equip_type
    when 0 then old_id, @weapon_id = @weapon_id, id
    when 1 then old_id, @armor1_id = @armor1_id, id
    when 2 then old_id, @armor2_id = @armor2_id, id
    when 3 then old_id, @armor3_id = @armor3_id, id
    when 4 then old_id, @armor4_id = @armor4_id, id
    end
    tested = [self.maxhp, self.maxsp, self.atk, self.pdef, self.mdef, self.str,
              self.dex, self.agi, self.int, self.eva]
    case equip_type
    when 0 then @weapon_id = old_id
    when 1 then @armor1_id = old_id
    when 2 then @armor2_id = old_id
    when 3 then @armor3_id = old_id
    when 4 then @armor4_id = old_id
    end
    return tested
  end
  
end 

#============================================================================== 
# Scene_Title
#============================================================================== 

class Scene_Title

  alias main_storm_cms_later main
  def main
    $map_infos = load_data('Data/MapInfos.rxdata')
    $map_infos.keys.each {|key| $map_infos[key] = $map_infos[key].name}
    main_storm_cms_later
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
# Bitmap
#==============================================================================

class Bitmap

  if $tons_version == nil || $tons_version < 3.71
  alias init_ultimate_font_override_later initialize
  def initialize(w, h = nil)
    if w.is_a?(Numeric) && h.is_a?(Numeric)
      init_ultimate_font_override_later(w, h)
    else
      init_ultimate_font_override_later(w)
    end
    if $game_system != nil && $game_system.fontname != nil &&
        !$scene.is_a?(Scene_Title)
      self.font.name = $game_system.fontname
      self.font.size = $game_system.fontsize
    else
      self.font.name = 'Arial'
      self.font.size = 24
    end
  end
  
  if !$crls || !BAR_STYLES
  def gradient_bar(x, y, w, color1, color2, color3, rate)
    offset = 5
    x += offset
    y += 26
    (0...offset+3).each {|i| fill_rect(x-i, y+i-2, w+3, 1, Color.new(0, 0, 0))}
    (0...offset+1).each {|i| fill_rect(x-i, y+i-1, w+1, 1, Color.new(255, 255, 255))}
    (0...w+offset).each {|i|
        red = color3.red * i / (w + offset)
        green = color3.green * i / (w + offset)
        blue = color3.blue * i / (w + offset)
        oy = i < offset ? offset-i : 0
        off = i < offset ? i : i > w ? w+offset-i : offset
        fill_rect(x+i-offset+1, y+oy-1, 1, off, Color.new(red, green, blue))}
    if (w*rate).to_i >= offset
      (0...(w*rate).to_i+offset).each {|i|
          red = color1.red + (color2.red-color1.red)*i/((w+offset)*rate)
          green = color1.green + (color2.green-color1.green)*i/((w+offset)*rate)
          blue = color1.blue + (color2.blue-color1.blue)*i/((w+offset)*rate)
          oy = i < offset ? offset-i : 0
          off = i < offset ? i : i > w*rate ? (w*rate).to_i+offset-i : offset
          fill_rect(x+i-offset+1, y+oy-1, 1, off, Color.new(red, green, blue))}
    else
      (0...(w*rate).to_i).each {|i|
          (0...offset-1).each {|j|
              red = color1.red + (color2.red-color1.red) * i / (w * rate)
              green = color1.green + (color2.green-color1.green) * i / (w * rate)
              blue = color1.blue + (color2.blue-color1.blue) * i / (w * rate)
              set_pixel(x+i-j+1, y+j-1, Color.new(red, green, blue))}}
    end
  end
  end
  end
  
end

#============================================================================== 
# Window_Base 
#============================================================================== 

class Window_Base < Window
  
  alias st_cms_hybrid_hack_init initialize
  def initialize(xx, yy, w, h)
    st_cms_hybrid_hack_init(xx, yy, w, h)
    if CMS_EDITION && @background != nil
      @backsprite = Sprite.new
      @backsprite.bitmap = RPG::Cache.picture("CMS/#{CMS_EDITION}/#{@background}")
      self.opacity, @backsprite.x, @backsprite.y = 0, self.x, self.y
    end
  end
  
  alias st_cms_hybrid_hack_x_ x=
  def x=(xx)
    st_cms_hybrid_hack_x_($scene.is_a?(Scene_Menu) && MIRROR ? 640-width-xx : xx)
    @backsprite.x = xx unless @backsprite == nil || @backsprite.disposed?
  end
  
  alias st_cms_hybrid_hack_y_ y=
  def y=(yy)
    st_cms_hybrid_hack_y_(yy)
    @backsprite.y = yy unless @backsprite == nil || @backsprite.disposed?
  end
  
  alias st_cms_hybrid_hack_x x
  def x
    xx = st_cms_hybrid_hack_x
    return ($scene.is_a?(Scene_Menu) && MIRROR ? 640-width-xx : xx)
  end
  
  alias st_cms_hybrid_hack_z z=
  def z=(z)
    st_cms_hybrid_hack_z(z)
    @backsprite.z = z unless @backsprite == nil || @backsprite.disposed?
  end
  
  alias st_cms_hybrid_hack_width width=
  def width=(w)
    self.x += w-width if $scene.is_a?(Scene_Menu) && MIRROR
    st_cms_hybrid_hack_width(w)
  end
  
  alias st_cms_hybrid_hack_visible visible=
  def visible=(expr)
    st_cms_hybrid_hack_visible(expr)
    @backsprite.visible = expr unless @backsprite == nil || @backsprite.disposed?
  end
  
  alias disp_sprite_later dispose
  def dispose
    @backsprite.dispose unless @backsprite == nil || @backsprite.disposed?
    disp_sprite_later
  end
  
  alias st_cms_hybrid_hack_normal_color normal_color
  def normal_color
    if $scene.is_a?(Scene_Menu) && FONT_BACKGROUND_FIX
      return Color.new(0, 0, 0)
    else
      return st_cms_hybrid_hack_normal_color
    end
  end

  alias st_cms_hybrid_hack_system_color system_color
  def system_color
    if $scene.is_a?(Scene_Menu) && FONT_BACKGROUND_FIX
      return Color.new(160, 0, 255)
    else
      return st_cms_hybrid_hack_system_color
    end
  end

  alias st_cms_hybrid_hack_disabled_color disabled_color
  def disabled_color
    if $scene.is_a?(Scene_Menu) && FONT_BACKGROUND_FIX
      return Color.new(96, 96, 96)
    else
      return st_cms_hybrid_hack_disabled_color
    end
  end
  
  alias st_cms_hybrid_hack_crisis_color crisis_color
  def crisis_color
    if $scene.is_a?(Scene_Menu) && FONT_BACKGROUND_FIX
      return Color.new(192, 192, 0)
    else
      return st_cms_hybrid_hack_crisis_color
    end
  end
  
  alias draw_actor_graphic_st_cms_later draw_actor_graphic
  def draw_actor_graphic(actor, x, y)
    if actor != nil && actor.character_name != ''
      if self.is_a?(Window_CMSMenuStatus) && FACESETS
        bitmap = RPG::Cache.character("#{actor.character_name}_face", actor.character_hue)
        x -= bitmap.width / 2
        y -= bitmap.height
        draw_actor_face_st_cms(actor, x, y)
      else
        draw_actor_graphic_st_cms_later(actor, x, y)
      end
    end
  end

  def draw_actor_face_st_cms(actor, x, y)
    if $tons_version == nil || $tons_version < 3.71 || !FACE_HUE
      hue = 0
    else
      hue = (FACE_HUE ? actor.character_hue : 0)
    end
    bitmap = RPG::Cache.character("#{actor.character_name}_face", hue)
    src_rect = Rect.new(0, 0, bitmap.width, bitmap.height)
    self.contents.blt(x, y, bitmap, src_rect)
  end
  
  def draw_actor_battler(actor, x, y)
    if actor != nil && actor.battler_name != ''
      bitmap = RPG::Cache.battler(actor.battler_name, actor.battler_hue)
      cw = bitmap.width
      ch = bitmap.height
      src_rect = Rect.new(0, 0, cw,ch)
      self.contents.blt(x - cw / 2, y - ch, bitmap, src_rect)
    end
  end
  
  def draw_actor_exp(actor, x, y, width = 144)
    self.contents.font.color = system_color
    self.contents.draw_text(x, y, 48, 32, 'EXP')
    if actor.exp_s.to_i > 999999
      w = self.contents.text_size('999999').width
    else
      w = self.contents.text_size(actor.exp_s).width
    end
    if actor.next_exp_s.to_i > 999999
      w2 = self.contents.text_size('999999').width
    else
      w2 = self.contents.text_size(actor.next_exp_s).width
    end
    self.contents.font.color = normal_color
    self.contents.draw_text(x + 108 - w2, y, w2, 32, actor.exp_s, 2)
    self.contents.draw_text(x + 108, y, 12, 32, '/', 1)
    self.contents.draw_text(x + 120, y, w2, 32, actor.next_exp_s)
  end
  
  def draw_actor_exp_alt(actor, x, y)
    self.contents.font.color = system_color
    self.contents.draw_text(x, y, 64, 32, 'next')
    self.contents.font.color = normal_color
    self.contents.draw_text(x + 56, y, 84, 32, actor.next_rest_exp_s, 2)
  end

  def draw_actor_name2(actor, x, y, w, a)
    self.contents.font.color = normal_color
    self.contents.draw_text(x, y, w, 32, actor.name, a)
  end
  
  def up_color
    return Color.new(0, 255, 0)
  end
 
  def down_color
    return Color.new(255, 0, 0)
  end
  
  alias draw_actor_parameter_st_cms_later draw_actor_parameter
  def draw_actor_parameter(actor, x, y, type)
    if type == 7
      self.contents.font.color = system_color
      self.contents.draw_text(x, y, 120, 32, 'Evasion')
      self.contents.font.color = normal_color
      self.contents.draw_text(x + 120, y, 36, 32, actor.eva.to_s, 2)
    else
      draw_actor_parameter_st_cms_later(actor, x, y, type)
    end
  end
  
  if $Blizz_Art
  alias draw_actor_exp_blizzart_later draw_actor_exp
  def draw_actor_exp(actor, x, y, w = 148)
    if $game_system.BARS
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
    end
    draw_actor_exp_blizzart_later(actor, x, y)
  end
  
  alias draw_actor_exp_new2 draw_actor_exp_alt
  def draw_actor_exp_alt(actor, x, y, w = 148)
    w -= 12
    rate = (actor.next_exp != 0 ? actor.now_exp.to_f / actor.next_exp : 1)
    if rate < 0.5
      color1 = Color.new(20 * rate, 60, 80)
      color2 = Color.new(60 * rate, 180, 240)
    elsif rate >= 0.5
      color1 = Color.new(20 + 120 * (rate-0.5), 60 + 40 * (rate-0.5), 80)
      color2 = Color.new(60 + 360 * (rate-0.5), 180 + 120 * (rate-0.5), 240)
    end
    color3 = Color.new(80, 80, 80, 192)
    self.contents.gradient_bar(x, y, w, color1, color2, color3, rate)
    draw_actor_exp_new2(actor, x, y)
  end
  end

end

#==============================================================================
# Window_CMSCommand
#==============================================================================

class Window_CMSCommand < Window_Command
  
  attr_reader :continue
  
  def initialize(index, continue)
    @background = 'CMSCommand'
    commands = [$data_system.words.item, 'Equipment', $data_system.words.equip,
        $data_system.words.skill, 'Status', 'Options', 'Save', 'Load', 'Exit']
    super(180, commands)
    @continue, self.index, self.x, self.y, self.z = continue, index, 972, 0, 999
  end
  
  def draw_item(i, color)
    self.contents.fill_rect(0, i*32, 148, 32, Color.new(0, 0, 0, 0))
    bitmap = RPG::Cache.icon("CMS/commandmenu#{i}")
    opacity = (color == normal_color ? 255 : 128)
    self.contents.blt(4, 4 + i*32, bitmap, Rect.new(0, 0, 24, 24), opacity)
    self.contents.font.color = color
    self.contents.draw_text(32, i*32, 148, 32, @commands[i])
  end
  
end

#==============================================================================
# Window_CMSChooseItem
#==============================================================================

class Window_CMSChooseItem < Window_Selectable
  
  def initialize
    @background = 'CMSHelp'
    super(0, -576, 640, 64)
    @commands = ['Items', 'Sort', 'Quest Items']
    @item_max = @column_max = @commands.size
    self.contents = Bitmap.new(width - 32, 32)
    refresh
    self.active, self.z, self.index = true, 2900, 0
  end
  
  def refresh
    self.contents.clear
    (0...@item_max).each {|i| draw_item(i, normal_color)}
  end
  
  def draw_item(i, color)
    self.contents.font.color = color
    self.contents.fill_rect(8 + 212*i, 0, 164, 32, Color.new(0, 0, 0, 0))
    self.contents.draw_text(8 + 212*i, 0, 164, 32, @commands[i], 1)
  end
  
end

#==============================================================================
# Window_CMSOptions
#==============================================================================

class Window_CMSOptions < Window_Selectable

  attr_accessor :current_font
  attr_reader   :current_skin
  attr_reader   :skin_name
  attr_reader   :font_name
  
  def initialize
    @background = 'CMSFullscreen'
    super(0, 512, 640, 480)
    @commands = ['BGM Volume', 'SFX Volume']
    self.contents = Bitmap.new(width - 32, height - 32)
    self.z, self.index = 2999, 0
    @item_max = @commands.size
    refresh
  end
  
  def get_option
    return @commands[index]
  end
  
  def refresh
    self.contents.clear
    self.contents.font.name = $game_system.fontname
    (0...@item_max).each {|i|
        self.contents.font.color = normal_color
        self.contents.fill_rect(24, 16 + i*36, 192, 32, Color.new(0, 0, 0, 0))
        self.contents.draw_text(24, 16 + i*36, 192, 32, @commands[i])
        draw_arrows(288, 4 + i*36)
        case @commands[i]
        when 'BGM Volume' then draw_volume(288, 4 + i*36)
        when 'SFX Volume' then draw_volume(288, 4 + i*36, true)
        end}
  end
      
  def draw_arrows(x, y)
    self.contents.draw_text(x - 32, y + 13, 32, 32, '<<')
    self.contents.draw_text(x + 249, y + 13, 32, 32, '>>')
  end
  
  def draw_volume(x, y, mode = false, width = 224)
    volume = (mode ? $game_system.sfx_volume.to_f : $game_system.bgm_volume.to_f)
    vol = volume.to_f / 100
    color1 = Color.new(20, 40, 80, 192)
    color2 = Color.new(60, 120, 240, 192)
    color3 = Color.new(0, 0, 80, 192)
    if $Blizz_Art 
      old = $game_system.bar_opacity
      $game_system.bar_opacity = 255
    end
    self.contents.gradient_bar(x, y, width, color1, color2, color3, vol)
    $game_system.bar_opacity = old if $Blizz_Art
  end
  
  def update_cursor_rect
    if self.index < 0
      self.cursor_rect.empty
    else
      self.cursor_rect.set(16, @index*36 + 16, 128, 32)
    end
  end
  
end

#==============================================================================
# Window_CMSTarget
#==============================================================================

class Window_CMSTarget < Window_Base
  
  attr_reader :index
  attr_reader :actor
  attr_reader :dir
  
  def initialize(actor, mode = false)
    @background = 'CMSTarget'
    super(-304, 64, 256, 104)
    self.contents = Bitmap.new(width - 32, height - 32)
    @actor, @item_max = actor, 1
    self.y += actor.index*104 unless mode
    self.z = 3999
    self.index = -1
    refresh
  end
  
  def index=(i)
    @index = i
    update_cursor_rect
  end
  
  def refresh
    self.contents.clear
    draw_actor_name(@actor, 4, -4)
    draw_actor_state(@actor, 100, -4, 112)
    draw_actor_hp(@actor, 44, 16)
    draw_actor_sp(@actor, 44, 38)
  end
  
  def update_actor(actor)
    @actor = actor
    refresh
  end
  
  def dir=(val)
    self.y -= val*40
    @dir = val
  end
  
  def update(i = @actor.index - 1)
    unless self.index == -2
      if @actor.index == i
        self.index = 0 if self.index == -1
      else
        self.index = -1 if self.index == 0
      end
    end
    self.y = 64+@actor.index*104 unless self.active
    @dir = 0 if (self.y-64) / 104 * 104 == self.y-64
    super()
    update_cursor_rect
  end
  
  def update_cursor_rect
    if !self.active || self.index == -1
      self.cursor_rect.empty
    elsif self.index >= 0
      self.cursor_rect.set(0, @index * 96, 224, 72)
    elsif self.index == -2
      self.cursor_rect.set(0, 0, 224, 72)
    end
  end
  
end

#==============================================================================
# Window_Help
#==============================================================================

class Window_Help < Window_Base
  
  alias init_storm_cms_later initialize
  def initialize
    @background = 'CMSHelp' if $scene.is_a?(Scene_Menu)
    init_storm_cms_later
    refresh
  end
  
  def refresh
    self.contents.font.name = $game_system.fontname
  end
  
end

#==============================================================================
# Window_CMSItem
#==============================================================================

class Window_CMSItem < Window_Selectable

  def initialize
    @background = 'CMSItem'
    super(256, -512, 384, 416)
    self.active, self.visible, self.z, self.index = false, false, 2999, -1
    refresh
  end

  def data
    return @data[self.index]
  end
  
  def draw_item(i)
    number = case @data[i]
    when RPG::Item then $game_party.item_number(@data[i].id)
    when RPG::Weapon then $game_party.weapon_number(@data[i].id)
    when RPG::Armor then $game_party.armor_number(@data[i].id)
    end
    if @data[i].is_a?(RPG::Item) && $game_party.item_can_use?(@data[i].id) ||
        @mode == nil
      self.contents.font.color = normal_color
    else
      self.contents.font.color = disabled_color
    end
    self.contents.fill_rect(4, i*32, 352, 32, Color.new(0, 0, 0, 0))
    bitmap = RPG::Cache.icon(@data[i].icon_name)
    opacity = self.contents.font.color == normal_color ? 255 : 128
    self.contents.blt(4, i*32 + 4, bitmap, Rect.new(0, 0, 24, 24), opacity)
    self.contents.draw_text(32, i*32, 212, 32, @data[i].name, 0)
    self.contents.draw_text(308, i*32, 16, 32, ':', 1)
    self.contents.draw_text(324, i*32, 24, 32, number.to_s, 2)
  end

  def update_help
    @help_window.set_text(data == nil ? '' : data.description)
  end
  
end

#==============================================================================
# Window_NormalItem
#==============================================================================

class Window_NormalItem < Window_CMSItem
  
  attr_accessor :mode
  
  def initialize
    @mode = 0
    super
    self.visible = true
  end
  
  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    data1, data2, data3 = [], [], []
    (1...$data_items.size).each {|i|
        if $game_party.item_number(i) > 0 && !$quest_items.include?(i)
          data1.push($data_items[i])
        end}
    if WEAPONS_AND_ARMORS
      (1...$data_weapons.size).each {|i|
          data2.push($data_weapons[i]) if $game_party.weapon_number(i) > 0}
      (1...$data_armors.size).each {|i|
          data3.push($data_armors[i]) if $game_party.armor_number(i) > 0}
    end
    if [1, 2].include?(@mode)
      data1.sort! {|a, b|
          $game_party.item_number(a.id) <=> $game_party.item_number(b.id)}
      data2.sort! {|a, b|
          $game_party.weapon_number(a.id) <=> $game_party.weapon_number(b.id)}
      data3.sort! {|a, b|
          $game_party.armor_number(a.id) <=> $game_party.armor_number(b.id)}
      [data1, data2, data3].each {|ary| ary.reverse!} if @mode == 2
    elsif [3, 4].include?(@mode)
      [data1, data2, data3].each {|ary| ary.sort! {|a, b| a.name <=> b.name}}
      [data1, data2, data3].each {|ary| ary.reverse!} if @mode == 4
    end
    @data = data1 + data2 + data3  
    @item_max = @data.size
    self.contents = Bitmap.new(width - 32, @item_max * 32) if @item_max > 0
    (0...@item_max).each {|i| draw_item(i)}
  end
  
end

#==============================================================================
# Window_QuestItem
#==============================================================================

class Window_QuestItem < Window_CMSItem
  
  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    @data = []
    (1...$data_items.size).each {|i|
        if $game_party.item_number(i) > 0 && $quest_items.include?(i)
          @data.push($data_items[i])
        end}
    @item_max = @data.size
    self.contents = Bitmap.new(width - 32, @item_max * 32) if @item_max > 0
    (0...@item_max).each {|i| draw_item(i)}
  end

end

#==============================================================================
# Window_EquipmentItem
#==============================================================================

class Window_EquipmentItem < Window_CMSItem

  attr_accessor :item_max
  
  def initialize(actor)
    @actor = actor
    super()
    self.x, self.y, self.z, self.index = 256, -548, 2999, 0
    self.active = self.visible = true
  end

  def update_actor(actor)
    @actor = actor
    refresh
  end
  
  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    @data = []
    (1...$data_weapons.size).each {|i|
        @data.push($data_weapons[i]) if $game_party.weapon_number(i) > 0}
    (1...$data_armors.size).each {|i|
        @data.push($data_armors[i]) if $game_party.armor_number(i) > 0}
    @item_max = @data.size
    self.contents = Bitmap.new(width - 32, @item_max * 32) if @item_max > 0
    (0...@item_max).each {|i| draw_item(i)}
  end

  def draw_item(i)
    case @data[i]
    when RPG::Weapon
      if @actor.equippable?($data_weapons[@data[i].id])
        self.contents.font.color = normal_color
      else
        self.contents.font.color = disabled_color
      end
      number = $game_party.weapon_number(@data[i].id)
    when RPG::Armor
      if @actor.equippable?($data_armors[@data[i].id])
        self.contents.font.color = normal_color
      else
        self.contents.font.color = disabled_color
      end
      number = $game_party.armor_number(@data[i].id)
    end
    self.contents.fill_rect(4, i*32, 352, 32, Color.new(0, 0, 0, 0))
    bitmap = RPG::Cache.icon(@data[i].icon_name)
    opacity = self.contents.font.color == normal_color ? 255 : 128
    self.contents.blt(4, 4 + i*32, bitmap, Rect.new(0, 0, 24, 24), opacity)
    self.contents.draw_text(32, i*32, 212, 32, @data[i].name, 0)
    self.contents.draw_text(308, i*32, 16, 32, ':', 1)
    self.contents.draw_text(324, i*32, 24, 32, number.to_s, 2)
  end

end

#==============================================================================
# Window_CMSSkill
#==============================================================================

class Window_CMSSkill < Window_CMSItem
  
  def initialize(actor)
    @actor = actor
    super()
    self.x, self.y, self.z, self.index = -512, 64, 2999, 0
    self.active = self.visible = true
  end

  def update_actor(actor)
    @actor = actor
    refresh
  end

  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    @data = []
    @actor.skills.each {|id| @data.push($data_skills[id])}
    @item_max = @data.size
    self.contents = Bitmap.new(width - 32, @item_max * 32) if @item_max > 0
    (0...@item_max).each {|i| draw_item(i)}
  end

  def draw_item(i)
    self.contents.fill_rect(4, i*32, 352, 32, Color.new(0, 0, 0, 0))
    if @actor.skill_can_use?(@data[i].id)
      self.contents.font.color = normal_color
    else
      self.contents.font.color = disabled_color
    end
    bitmap = RPG::Cache.icon(@data[i].icon_name)
    opacity = self.contents.font.color == normal_color ? 255 : 128
    self.contents.blt(4, 4 + i*32, bitmap, Rect.new(0, 0, 24, 24), opacity)
    self.contents.draw_text(32, i*32, 204, 32, @data[i].name, 0)
    if @data[i].sp_cost > 0
      if $tons_version != nil && $tons_version >= 4.98
        if $game_system._1_SP && @actor.states.include?(ONE_SP_ID)
          sp_cost = 1
        elsif $game_system.HALF_SP && @actor.states.include?(HALF_SP_ID)
          sp_cost = (@data[i].sp_cost/2.0).ceil
        end
      end
      sp_cost = @data[i].sp_cost if sp_cost == nil
      self.contents.draw_text(292, i*32, 48, 32, sp_cost.to_s, 2)
    end
  end

end

#==============================================================================
# Window_CMSEquipLeft
#==============================================================================

class Window_CMSEquipLeft < Window_Base
  
  attr_accessor :mode
  attr_accessor :current
  attr_accessor :changed
  
  def initialize(actor)
    @background = 'CMSEquipLeft'
    super(640, 64, 288, 416)
    self.contents = Bitmap.new(width - 32, height - 32)
    @current = @changed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    @elements, @states, @actor, @mode, self.z = [], [], actor, 0, 2999
    refresh
  end
  
  def update_actor(actor)
    @actor = actor
    refresh
  end
  
  def draw_actor_hp(actor, x, y, width = 144)
    self.contents.font.color = system_color
    self.contents.draw_text(x, y, 96, 32, "max #{$data_system.words.hp}")
    self.contents.font.color = normal_color
    self.contents.draw_text(x + 108, y, 48, 32, actor.maxhp.to_s, 2)
  end
    
  def draw_actor_sp(actor, x, y, width = 144)
    self.contents.font.color = system_color
    self.contents.draw_text(x, y, 96, 32, "max #{$data_system.words.sp}")
    self.contents.font.color = normal_color
    self.contents.draw_text(x + 108, y, 48, 32, actor.maxsp.to_s, 2)
  end
    
  def refresh
    self.contents.clear
    draw_actor_name(@actor, 4, 0)
    draw_actor_level(@actor, 180, 0)
    draw_actor_hp(@actor, 4, 28)
    draw_actor_sp(@actor, 4, 52)
    (0..7).each {|i| draw_actor_parameter(@actor, 4, 76 + i*24, i)}
    if @mode == 0
      self.contents.font.color = up_color
      self.contents.draw_text(4, 276, 200, 32, 'Elemental attack:')
      self.contents.draw_text(4, 324, 200, 32, 'Status attack:')
    elsif @mode == 1
      self.contents.font.color = up_color
      self.contents.draw_text(4, 276, 200, 32, 'Elemental resistance:')
      self.contents.draw_text(4, 324, 200, 32, 'Status resistance:')
    end
    self.contents.font.color = normal_color
    draw_elements(4, 300)
    draw_states(4, 348)
    @current.each_index {|i|
        val = @current[i] - @changed[i]
        if val != 0
          self.contents.font.color = system_color
          self.contents.draw_text(162, 28+i*24, 40, 32, '»»', 1)
          self.contents.font.color = (val > 0 ? down_color : up_color)
          self.contents.draw_text(204, 28+i*24, 48, 32, @changed[i].abs.to_s, 2)
        end}
  end
  
  def set_new_parameters(elements, states)
    @elements, @states = elements, states
    refresh
  end
  
  def draw_elements(x, y)
    @elements.each_index {|i|
        icon = RPG::Cache.icon("CMS/elm_#{$data_system.elements[@elements[i]].downcase}")
        self.contents.blt(x + i*28, y + 4, icon, Rect.new(0, 0, 24, 24))}
  end
  
  def draw_states(x, y)
    @states.each_index {|i|
        icon = RPG::Cache.icon("CMS/stat_#{$data_states[@states[i]].name.downcase}")
        self.contents.blt(x + i*28, y + 4, icon, Rect.new(0, 0, 24, 24))}
  end
  
end
  
#==============================================================================
# Window_CMSEquipRight
#==============================================================================

class Window_CMSEquipRight < Window_Selectable

  def initialize(actor)
    @background = 'CMSEquipRight'
    super(928, 64, 352, 192)
    self.contents = Bitmap.new(width - 32, height - 32)
    @actor, self.active, self.z, self.index = actor, true, 2999, 0
    refresh
  end

  def data
    return @data[self.index]
  end
  
  def update_actor(actor)
    @actor = actor
    refresh
  end

  def refresh
    self.contents.clear
    @data = []
    @data.push($data_weapons[@actor.weapon_id])
    @data.push($data_armors[@actor.armor1_id])
    @data.push($data_armors[@actor.armor2_id])
    @data.push($data_armors[@actor.armor3_id])
    @data.push($data_armors[@actor.armor4_id])
    @item_max = @data.size
    self.contents.font.color = system_color
    self.contents.draw_text(4, 32 * 0, 120, 32, $data_system.words.weapon)
    self.contents.draw_text(4, 32 * 1, 120, 32, $data_system.words.armor1)
    self.contents.draw_text(4, 32 * 2, 120, 32, $data_system.words.armor2)
    self.contents.draw_text(4, 32 * 3, 120, 32, $data_system.words.armor3)
    self.contents.draw_text(4, 32 * 4, 120, 32, $data_system.words.armor4)
    (0...5).each {|i| draw_item_name(@data[i], 120, 32 * i)}
  end

  def update_help
    @help_window.set_text(data == nil ? '' : data.description)
  end
  
end

#==============================================================================
# Window_CMSEquipItem
#==============================================================================

class Window_CMSEquipItem < Window_Selectable

  def initialize(actor, equip_type)
    @background = 'CMSEquipItem'
    super(928, 256, 352, 224)
    self.active = self.visible = false
    @actor, @equip_type, self.z, self.index = actor, equip_type, 3000, -1
    refresh
  end

  def data
    return @data[self.index]
  end

  def update_actor(actor, equip_type)
   @actor = actor
   @equip_type = equip_type
   refresh
 end
  
  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    @data = []
    if @equip_type == 0
      weapon_set = $data_classes[@actor.class_id].weapon_set
      (1...$data_weapons.size).each {|i|
          if $game_party.weapon_number(i) > 0 && weapon_set.include?(i)
            @data.push($data_weapons[i])
          end}
    else
      armor_set = $data_classes[@actor.class_id].armor_set
      (1...$data_armors.size).each {|i|
          if $game_party.armor_number(i) > 0 && armor_set.include?(i)
            @data.push($data_armors[i]) if $data_armors[i].kind == @equip_type-1
          end}
    end
    @data.push(nil)
    @item_max = @data.size
    self.contents = Bitmap.new(width - 32, @item_max * 32)
    (0...@item_max-1).each {|i| draw_item(i)}
    self.contents.font.color = system_color
    self.contents.draw_text(4, (@item_max-1)*32, 100, 32, '[Unequip]')
  end

  def draw_item(i)
    number = case @data[i]
    when RPG::Weapon then $game_party.weapon_number(@data[i].id)
    when RPG::Armor then $game_party.armor_number(@data[i].id)
    end
    self.contents.font.color = normal_color
    bitmap = RPG::Cache.icon(@data[i].icon_name)
    self.contents.blt(4, 4 + i*32, bitmap, Rect.new(0, 0, 24, 24))
    self.contents.draw_text(32, i*32, 212, 32, @data[i].name, 0)
    self.contents.draw_text(212, i*32, 16, 32, ':', 1)
    self.contents.draw_text(228, i*32, 24, 32, number.to_s, 2)
  end

  def update_help
    @help_window.set_text(data == nil ? '' : data.description)
  end
  
end

#==============================================================================
# Window_CMSStatus
#==============================================================================

class Window_CMSStatus < Window_Base

  def initialize(actor)
    @background = 'CMSFullscreen'
    super(0, 512, 640, 480)
    self.contents = Bitmap.new(width - 32, height - 32)
    @actor, self.active, self.z = actor, true, 2999
    refresh
  end

  def refresh
    self.contents.clear
    self.contents.font.color = normal_color
    self.contents.draw_text(224, 0, 120, 32, @actor.name, 1)
    draw_actor_battler(@actor, 284, 232)
    draw_actor_class(@actor, 400, 32)
    draw_actor_level(@actor, 400, 0)
    draw_actor_state(@actor, 400, 64, 168)
    draw_actor_hp(@actor, 400, 92, 172)
    draw_actor_sp(@actor, 400, 122, 172)
    if $crls
      if DRAW_BAR
        draw_actor_sr_with_bar(@actor, 400, 152, 172)
      else
        draw_actor_sr(@actor, 400, 152, 172)
      end
      draw_actor_exp(@actor, 400, 182, 172)
    else
      draw_actor_exp(@actor, 400, 152, 172)
    end
    (0..7).each {|i| draw_actor_parameter(@actor, 4, i*28, i)}
    self.contents.font.color = system_color
    self.contents.draw_text(84, 244, 96, 32, 'Equipment')
    self.contents.draw_text(4, 276, 96, 32, $data_system.words.weapon)
    self.contents.draw_text(4, 308, 96, 32, $data_system.words.armor1)
    self.contents.draw_text(4, 340, 96, 32, $data_system.words.armor2)
    self.contents.draw_text(4, 372, 96, 32, $data_system.words.armor3)
    self.contents.draw_text(4, 404, 96, 32, $data_system.words.armor4)
    equips = [$data_weapons[@actor.weapon_id], $data_armors[@actor.armor1_id],
        $data_armors[@actor.armor2_id], $data_armors[@actor.armor3_id],
        $data_armors[@actor.armor4_id]]
    equips.each_index {|i|
        if @actor.equippable?(equips[i])
          draw_item_name(equips[i], 108, 276 + i*32)
        else
          self.contents.font.color = (i == 0 ? knockout_color : crisis_color)
          self.contents.draw_text(108, 276 + i*32, 192, 32, 'Nothing equipped')
        end}
  end
  
  def update_actor(actor)
    @actor = actor
    refresh
  end
  
end

#==============================================================================
# Window_CMSSortCommand
#==============================================================================

class Window_CMSSortCommand < Window_Command

  def initialize
    @background = 'CMSMini'
    super(180, ['Standard', 'by quantity', 'by alphabet'])
    self.x, self.y, self.z = 224, -128, 9999
  end
  
end

#==============================================================================
# Window_CMSEndCommand
#==============================================================================

class Window_CMSEndCommand < Window_Command

  def initialize
    @background = 'CMSMini'
    super(180, ['Back to game', 'Back to title', 'Exit game'])
    self.x, self.y, self.z = 460, 524, 3999
  end
  
end

#==============================================================================
# Window_CMSInfo
#==============================================================================

class Window_CMSInfo < Window_Base

  def initialize
    @background = 'CMSInfo'
    super(0, 0, 180, 160)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.active, self.x, self.y, self.z = false, 460, 832, 1999
    refresh
  end

  def refresh
    self.contents.clear
    self.contents.font.name = $game_system.fontname
    @double_sec = Graphics.frame_count * 2 / Graphics.frame_rate
    total_sec = @double_sec / 2
    hour, min, sec = total_sec / 60 / 60, total_sec / 60 % 60, total_sec % 60
    if @double_sec % 2 == 1
      text = sprintf('%02d %02d %02d', hour, min, sec)
    else
      text = sprintf('%02d:%02d:%02d', hour, min, sec)
    end
    self.contents.font.color = system_color
    cx = contents.text_size($data_system.words.gold).width
    self.contents.draw_text(148-cx, 32, cx, 32, $data_system.words.gold, 2)
    self.contents.draw_text(0, 64, 148, 32, 'Location:')
    self.contents.font.color = normal_color
    self.contents.draw_text(0, 0, 148, 32, text, 1)
    self.contents.draw_text(0, 32, 144-cx, 32, $game_party.gold.to_s, 2)
    self.contents.draw_text(0, 96, 148, 32, $game_map.name, 2)
  end
  
  def update
    super
    refresh if Graphics.frame_count * 2 / Graphics.frame_rate != @double_sec
  end
  
end

#==============================================================================
# Window_CMSMenuStatus
#==============================================================================

class Window_CMSMenuStatus < Window_Base
  
  attr_reader :index
  attr_reader :actor
  attr_reader :dir
  
  def initialize(actor)
    @background = 'CMSMenuStatus'
    super(0, 0, 460, 120)
    self.contents = Bitmap.new(width - 32, height - 32)
    @actor = actor
    @dir = 0
    refresh
    self.active = false
    self.index = -1
    self.x, self.y, self.z = -512, @actor.index * 120, 999
  end
  
  def index=(i)
    @index = i
    update_cursor_rect
  end
  
  def refresh
    self.contents.clear
    self.contents.font.name = $game_system.fontname
    self.contents.font.color = normal_color
    draw_actor_graphic(@actor, 56, 80)
    draw_actor_name2(@actor, 8, 0, 88, 1)
    draw_actor_level(@actor, 104, 0)
    draw_actor_state(@actor, 168, 0, 252)
    draw_actor_hp(@actor, 104, 28)
    draw_actor_sp(@actor, 272, 28)
    draw_actor_exp_alt(@actor, 272, 56)
    if $crls
      if DRAW_BAR
        draw_actor_sr_with_bar(@actor, 104, 56)
      else
        draw_actor_sr(@actor, 104, 56)
      end
    end
  end
  
  def dir=(val)
    self.y -= val*56
    @dir = val
  end
  
  def update(i = @actor.index - 1)
    if @actor.index == i
      self.index = 0 if self.index == -1
    else
      self.index = -1 if self.index == 0
    end
    self.y = @actor.index*120 unless self.active
    @dir = 0 if self.y / 120 * 120 == self.y
    super()
  end
  
  def update_cursor_rect
    if @index < 0
      self.cursor_rect.empty
    else
      self.cursor_rect.set(0, 0, width - 32, height - 32)
    end
  end
  
end

#==============================================================================
# Scene_Menu
#==============================================================================

class Scene_Menu
  
  def initialize(menu_index = 0)
    @menu_index = menu_index
    @actor_index = @target_index = -1
    @viewport1 = Viewport.new(0, 0, 640, 480)
    @moved = false
  end

  def main
    if MAP_BACKGROUND
      @spriteset = Spriteset_Map.new
    elsif CMS_EDITION
      @spriteset = Sprite.new
      @spriteset.bitmap = RPG::Cache.picture("CMS/#{CMS_EDITION}/CMSFullscreen")
    end
    continue = false
    (1..SAVE_FILES_NUMBER).each {|i| 
        continue = true if FileTest.exist?("#{SAVE_NAME}#{i}.#{SAVE_EXTENSION}")}
    @command_window = Window_CMSCommand.new(@menu_index, continue)
    (0...5).each {|i| @command_window.disable_item(i)} if $game_party.actors.size == 0
    @command_window.disable_item(6) if $game_system.save_disabled
    @command_window.disable_item(7) unless @command_window.continue
    @info_window = Window_CMSInfo.new
    @status_windows, @target_windows = [], []
    $game_party.actors.each {|actor|
        @status_windows.push(Window_CMSMenuStatus.new(actor))}
    @help_window = Window_Help.new
    @help_window.x, @help_window.y, @help_window.z = 0, -368, 9999
    Graphics.transition
    loop do
      Graphics.update
      Input.update
      update
      break if @scene != nil || $scene != self
    end
    loop do
      Graphics.update
      (@status_windows + [@command_window, @info_window]).each {|win| win.update}
      move_da_outro
      break if @status_windows[0].x <= - 512
    end
    Graphics.freeze
    (@status_windows + @target_windows + [@command_window, @info_window,
        @help_window, @spriteset]).each {|obj| obj.dispose if obj != nil}
    del_sort if @sort_window != nil
    del_status if @playerstatus_window != nil
    del_equip if @left_window != nil
    del_skill if @skill_window != nil
    del_end if @end_window != nil
    del_items if @item_choose_window != nil
    del_items if @equips_window != nil
    del_options if @options_window != nil
    if @scene.is_a?(Scene_Title)
      Graphics.transition(25)
      Graphics.freeze
    end
    $scene = @scene
  end
  
  def equip_refresh
    if @item_window.active
      item = @item_window.data
      last_hp = @actor.hp
      last_sp = @actor.sp
      @left_window.current = [@actor.maxhp, @actor.maxsp, @actor.atk,
          @actor.pdef, @actor.mdef, @actor.str, @actor.dex, @actor.agi,
          @actor.int, @actor.eva]
      @left_window.changed = @actor.test_equip(@right_window.index, item == nil ? 0 : item.id)
      elements = (item.is_a?(RPG::Weapon) ? item.element_set :
          (item.is_a?(RPG::Armor) ? item.guard_element_set : []))
      states = (item.is_a?(RPG::Weapon) ? item.plus_state_set :
          (item.is_a?(RPG::Armor) ? item.guard_state_set : []))
      @actor.hp = last_hp
      @actor.sp = last_sp
      @left_window.set_new_parameters(elements, states)
    else
      @left_window.current = @left_window.changed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
      @left_window.set_new_parameters([], [])
    end
  end
  
  def del_sort
    @sort_window.dispose
    @sort_window = nil
  end
  
  def del_status
    @playerstatus_window.dispose
    @playerstatus_window = nil
  end
  
  def del_equip
    @left_window.dispose
    @right_window.dispose
    @item_windows.each {|win| win.dispose}
    @left_window = @right_window = @item_window = @item_windows = nil
  end
  
  def del_skill
    @skill_window.dispose
    @skill_window = nil
  end
  
  def del_target
    @target_windows.each {|win| win.dispose}
    @target_windows = []
  end

  def del_end
    @end_window.dispose
    @end_window = nil
  end
  
  def del_items
    @items_window1.dispose
    @items_window1 = nil
    @items_window2.dispose
    @items_window2 = nil
    @item_choose_window.dispose
    @item_choose_window = nil
  end
  
  def del_equipment
    @equips_window.dispose
    @equips_window = nil
    del_target
  end
  
  def del_options
    @options_window.dispose
    @options_window = nil
  end
  
  def update
    @status_windows.each {|win| win.update(@actor_index)}
    @target_windows.each {|win| win.update(@target_index)}
    @info_window.update
    unless @status_windows[0].x < 0 || @status_windows[0].dir != 0 ||
        @target_windows[0] != nil && @target_windows[0].dir != 0
      @command_window.update# if @command_window.active
      [@help_window, @equips_window, @item_choose_window, @sort_window,
      @skill_window, @left_window, @right_window, @playerstatus_window,
      @options_window, @end_window].each {|win| win.update if win != nil}
    end
    move_da_main if @status_windows[0].x < 0
    move_da_selection if @status_windows[0].dir != 0
    move_da_targeting if @target_windows[0] != nil && @target_windows[0].dir != 0
    move_da_status if @playerstatus_window != nil && @playerstatus_window.y > 0
    move_da_equip if @left_window != nil && @left_window.x > 0
    move_da_skill if @skill_window != nil && @skill_window.x < 256
    move_da_target if @target_windows[0] != nil && @target_windows[0].x < 0
    move_da_items if @item_choose_window != nil && @item_choose_window.y < 0
    move_da_sort if @sort_window != nil && @sort_window.y < 64
    move_da_equipment if @equips_window != nil && @equips_window.y < 64
    move_da_options if @options_window != nil && @options_window.y > 0
    move_da_end if @end_window != nil && @end_window.y > 336
    if @moved
      @moved = false
      return
    end
    if @equips_window != nil
      update_equipment
    elsif @command_window.active
      update_command
    elsif @status_windows[0].active
      update_status
    elsif @item_choose_window != nil
      if @item_choose_window.active
        items_refresh
        update_items_choose
      elsif @sort_window != nil && @sort_window.active
        update_sort
      elsif @items_window1 != nil && @items_window1.active
        @items_window1.update
        update_item
      elsif @items_window2 != nil && @items_window2.active
        @items_window2.update
        update_item
      elsif @target_windows[0] != nil && @target_windows[0].active
        update_item_target
      end
    elsif @skill_window != nil && @skill_window.active
      update_skill
    elsif @target_windows[0] != nil && @target_windows[0].active
      update_skill_target
    elsif @right_window != nil
      if @right_window.active
        update_right_equip
      elsif @item_window != nil && @item_window.active
        @item_window.update
        update_eitem
      end
    elsif @playerstatus_window != nil && @playerstatus_window.active
      update_playerstatus
    elsif @options_window != nil && @options_window.active
      update_options
    elsif @end_window != nil
      update_end
    end
  end
  
  def move_windows(wins, border, mdiff, lead, xy, acc = false)
    if acc
      diff = [[((xy ? lead.x : lead.y)-border).abs, mdiff].min, 1].max
    else
      diff = [[((xy ? lead.x : lead.y)-border).abs/2, mdiff].min, 1].max
    end
    wins[0].each {|win| win.x += diff if win != nil}
    wins[1].each {|win| win.x -= diff if win != nil}
    wins[2].each {|win| win.y += diff if win != nil}
    wins[3].each {|win| win.y -= diff if win != nil}
    @moved = true
  end
  
  def move_da_main
    lead = @status_windows[0]
    x_plus = @status_windows
    x_minus = [@command_window]
    y_minus = [@info_window]
    move_windows([x_plus, x_minus, [], y_minus], 0, 128, lead, true)
  end
  
  def move_da_outro
    lead = @status_windows[0]
    x_plus = [@command_window]
    x_minus = @status_windows + @target_windows + [@skill_window, @help_window]
    y_plus = [@info_window]
    y_minus = [@item_choose_window, @items_window1, @items_window2, @help_window]
    move_windows([x_plus, x_minus, y_plus, y_minus], 0, 128, lead, true, true)
  end
  
  def move_da_selection(lead = @status_windows[@actor_index])
    if lead.dir == 1
      move_windows([[], [], [], @status_windows], 360, 32, lead, false)
    else
      move_windows([[], [], @status_windows, []], 0, 32, lead, false)
    end
  end
  
  def move_da_targeting(lead = @target_windows[@target_index])
    if lead.dir == 1
      move_windows([[], [], [], @target_windows], 376, 32, lead, false)
    else
      move_windows([[], [], @target_windows, []], 64, 32, lead, false)
    end
  end
  
  def move_da_sort(win = @sort_window)
    move_windows([[], [], [win], []], 64, 32, win, false)
  end
  
  def move_da_status(win = @playerstatus_window)
    move_windows([[], [], [], [win]], 0, 64, win, false)
  end

  def move_da_equip(win = @left_window)
    x_minus = [@left_window, @right_window, @help_window] + @item_windows
    move_windows([[], x_minus, [], []], 0, 64, win, true)
  end  
    
  def move_da_skill(win = @skill_window)
    x_plus = [@skill_window, @help_window]
    move_windows([x_plus, [], [], []], 256, 64, win, true)
  end
  
  def move_da_target(win = @target_windows[0])
    move_windows([@target_windows, [], [], []], 0, 32, win, true)
  end
  
  def move_da_items(win = @item_choose_window)
    y_plus = [@item_choose_window, @items_window1, @items_window2, @help_window]
    move_windows([[], [], y_plus, []], 0, 64, win, false)
  end
  
  def move_da_equipment(win = @equips_window)
    y_plus = [@equips_window, @help_window]
    move_windows([[], [], y_plus, []], 64, 64, win, false)
  end
  
  def move_da_options(win = @options_window)
    move_windows([[], [], [], [win]], 0, 64, win, false)
  end
  
  def move_da_end(win = @end_window)
    move_windows([[], [], [], [win]], 336, 64, win, false)
  end
  
  def update_command
    if Input.trigger?(Input::B)
      $game_system.se_play($data_system.cancel_se)
      @scene = Scene_Map.new
    elsif Input.trigger?(Input::C)
      if $game_party.actors.size == 0 && @command_window.index < 5
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      case @command_window.index
      when 0
        $game_system.se_play($data_system.decision_se)
        @item_choose_window = Window_CMSChooseItem.new
        @items_window1 = Window_NormalItem.new
        @items_window2 = Window_QuestItem.new
        @items_window1.help_window = @items_window2.help_window = @help_window
        @command_window.active = false
        @help_window.x, @help_window.y = 0, -576
        @help_window.set_text('')
        @help_window.visible = false
        items_refresh
      when 1..4
        $game_system.se_play($data_system.decision_se)
        @command_window.active = false
        @status_windows.each {|win| win.active = true}
        @actor_index = 0
      when 5
        $game_system.se_play($data_system.decision_se)
        @options_window = Window_CMSOptions.new
        @command_window.active = false
      when 6
        if $game_system.save_disabled
          $game_system.se_play($data_system.buzzer_se)
        else
          $game_system.se_play($data_system.decision_se)
          @scene = Scene_CMSSave.new
          Graphics.transition(0)
        end
      when 7
        if @command_window.continue
          $game_system.se_play($data_system.decision_se)
          @scene = Scene_CMSLoad.new
          Graphics.transition(0)
        else
          $game_system.se_play($data_system.buzzer_se)
        end
      when 8
        $game_system.se_play($data_system.decision_se)
        @command_window.active = false
        @end_window = Window_CMSEndCommand.new
      end
    end
  end
  
  def update_status
    @actor = $game_party.actors[@actor_index]
    if Input.trigger?(Input::B)
      $game_system.se_play($data_system.cancel_se)
      @status_windows.each {|win| win.active, win.index = false, -1}
      @actor_index = -1
      @command_window.active = true
    elsif Input.trigger?(Input::C)
      case @command_window.index
      when 1
        $game_system.se_play($data_system.decision_se)
        @equips_window = Window_EquipmentItem.new(@actor)
        @equips_window.help_window = @help_window
        @target_windows.push(Window_CMSTarget.new(@actor, true))
        @status_windows.each {|win| win.active = false}
        @help_window.visible = true
        @help_window.x, @help_window.y = 0, -612
      when 2
        $game_system.se_play($data_system.decision_se)
        if CUSTOM_EQUIP_SCENE
          @scene = Scene_Equip.new(@actor_index)
        else
          @left_window = Window_CMSEquipLeft.new(@actor)
          @right_window = Window_CMSEquipRight.new(@actor)
          @right_window.help_window = @help_window
          @item_windows = []
          (0..4).each {|i| win = Window_CMSEquipItem.new(@actor, 4-i)
              win.help_window = @help_window
              @item_windows.unshift(win)}
          @item_windows[0].visible = @help_window.visible = true
          @help_window.x, @help_window.y = 640, 0
          @status_windows.each {|win| win.active = false}
        end
      when 3
        if @actor.restriction >= 2
          $game_system.se_play($data_system.buzzer_se)
        else
          $game_system.se_play($data_system.decision_se)
          @skill_window = Window_CMSSkill.new(@actor)
          @skill_window.help_window = @help_window
          @help_window.visible = true
          @help_window.x, @help_window.y = -768, 0
          @status_windows.each {|win| win.active = false}
        end
      when 4
        $game_system.se_play($data_system.decision_se)
        @playerstatus_window = Window_CMSStatus.new(@actor)
        @status_windows.each {|win| win.active = false}
      end
    elsif Input.repeat?(Input::DOWN)
      $game_system.se_play($data_system.cursor_se)
      @actor_index = (@actor_index+1) % $game_party.actors.size
      if @status_windows[@actor_index].y < 0
        @status_windows.each {|win| win.y += ($game_party.actors.size-4)*120}
      elsif @status_windows[@actor_index].y >= 480
        @status_windows.each {|win| win.dir = 1}
      end
    elsif Input.repeat?(Input::UP)
      $game_system.se_play($data_system.cursor_se)
      @actor_index += $game_party.actors.size-1
      @actor_index %= $game_party.actors.size
      if @status_windows[@actor_index].y < 0
        @status_windows.each {|win| win.dir = -1}
      elsif @status_windows[@actor_index].y >= 480
        @status_windows.each {|win| win.y -= ($game_party.actors.size-4)*120}
      end
    end
  end
  
  def update_items_choose
    if Input.trigger?(Input::B)
      del_items
      $game_system.se_play($data_system.cancel_se)
      @command_window.active, @help_window.x, @help_window.y = true, 0, -612
    elsif Input.trigger?(Input::C)
      items_refresh
      @item_choose_window.active = false
      $game_system.se_play($data_system.decision_se)
      case @item_choose_window.index
      when 0
        @items_window1.active = @help_window.visible = true
        @items_window1.index = 0
      when 1
        @sort_window = Window_CMSSortCommand.new
      when 2
        @items_window2.active = @help_window.visible = true
        @items_window2.index = 0
      end
    end
  end
  
  def update_sort
    if Input.trigger?(Input::B)
      del_sort
      @item_choose_window.active = true
      $game_system.se_play($data_system.cancel_se)
    elsif Input.trigger?(Input::C)
      $game_system.se_play($data_system.decision_se)
      @items_window1.mode = case @sort_window.index
      when 0 then @sort_window.index
      when 1 then @items_window1.mode == 1 ? 2 : 1
      when 2 then @items_window1.mode == 3 ? 4 : 3
      end
      @items_window1.refresh
    end
  end
  
  def items_refresh
    index = @item_choose_window.index
    @items_window1.visible = [0, 1].include?(index)
    @items_window2.visible = (index == 2)
  end
    
  def update_equipment
    if Input.trigger?(Input::B)
      del_equipment
      $game_system.se_play($data_system.cancel_se)
      @actor_index = -1
      @command_window.active = true
      @help_window.visible = false
      @help_window.x, @help_window.y = 0, -612
    elsif Input.trigger?(Input::RIGHT) || Input.trigger?(Input::LEFT)
      $game_system.se_play($data_system.cursor_se)
      if Input.trigger?(Input::RIGHT)
        @actor_index = (@actor_index+1) % $game_party.actors.size
      elsif Input.trigger?(Input::LEFT)
        @actor_index += $game_party.actors.size-1
        @actor_index %= $game_party.actors.size
      end
      @target_windows[0].update_actor($game_party.actors[@actor_index])
      @equips_window.update_actor($game_party.actors[@actor_index])
      unless @equips_window.item_max > @equips_window.index
        @equips_window.index = 0
      end
    end
  end
  
  def update_item
    if Input.trigger?(Input::B)
      $game_system.se_play($data_system.cancel_se)
      @item_choose_window.active = true
      @help_window.set_text('')
      @items_window1.active = @items_window2.active = @help_window.visible = false
      @items_window1.index = @items_window2.index = -1
    elsif Input.trigger?(Input::C)
      win = (@item_choose_window.index == 0 ? @items_window1 : @items_window2)
      @item = win.data
      unless @item.is_a?(RPG::Item) && $game_party.item_can_use?(@item.id)
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      $game_party.actors.each_index {|i|
          @target_windows.push(Window_CMSTarget.new($game_party.actors[i]))}
      @target_index = 0
      $game_system.se_play($data_system.decision_se)
      if @item.scope.between?(3, 6)
        win.active = false
        @target_windows.each {|win| win.active = true}
        if [4, 6].include?(@item.scope)
          @target_windows.each {|win| win.index = -2}
        else
          @target_windows[@target_index].index = 0
        end
      elsif @item.common_event_id > 0
        $game_temp.common_event_id = @item.common_event_id
        $game_system.se_play(@item.menu_se)
        if @item.consumable
          $game_party.lose_item(@item.id, 1)
          win.draw_item(win.index)
        end
        (@status_windows + @target_windows).each {|win| win.refresh}
        @items_window1.refresh
        @items_window2.refresh
        @scene = Scene_Map.new
      elsif @skill.scope == 7
        $game_system.se_play($data_system.buzzer_se)
      end
    end
  end
  
  def update_item_target
    if Input.trigger?(Input::B)
      del_target
      $game_system.se_play($data_system.cancel_se)
      @target_index = -1
      @items_window1.refresh unless $game_party.item_can_use?(@item.id)
      @items_window1.active = true
    elsif Input.trigger?(Input::C)
      if $game_party.item_number(@item.id) == 0
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      if @target_windows[0].index == -2
        used = false
        $game_party.actors.each {|actor| used |= actor.item_effect(@item)}
      elsif @target_index >= 0
        used = $game_party.actors[@target_index].item_effect(@item)
      end
      if used
        $game_system.se_play(@item.menu_se)
        if @item.consumable
          $game_party.lose_item(@item.id, 1)
          @items_window1.draw_item(@items_window1.index)
        end
        (@status_windows + @target_windows).each {|win| win.refresh}
        if $game_party.all_dead?
          @scene = Scene_Gameover.new
        elsif @item.common_event_id > 0
          $game_temp.common_event_id = @item.common_event_id
          @scene = Scene_Map.new
        end
      else
        $game_system.se_play($data_system.buzzer_se)
      end
    else
      update_target
    end
  end
  
  def update_target
    return if @target_windows[0] == nil || @target_windows[0].index == -2
    if Input.repeat?(Input::DOWN)
      $game_system.se_play($data_system.cursor_se)
      @target_index = (@target_index+1) % $game_party.actors.size
      if @target_windows[@target_index].y < 64
        @target_windows.each {|win| win.y += ($game_party.actors.size-4)*104}
      elsif @target_windows[@target_index].y >= 480
        @target_windows.each {|win| win.dir = 1}
      end
    elsif Input.repeat?(Input::UP)
      $game_system.se_play($data_system.cursor_se)
      @target_index += $game_party.actors.size-1
      @target_index %= $game_party.actors.size
      if @target_windows[@target_index].y < 64
        @target_windows.each {|win| win.dir = -1}
      elsif @target_windows[@target_index].y >= 480
        @target_windows.each {|win| win.y -= ($game_party.actors.size-4)*104}
      end
    end
  end

  def update_skill
    if Input.trigger?(Input::B)
      del_skill
      $game_system.se_play($data_system.cancel_se)
      @help_window.x, @help_window.y = 0, -768
      @help_window.visible = false
      @command_window.active = true
      @actor_index = @target_index = -1
    elsif Input.trigger?(Input::C)
      @skill = @skill_window.data
      if @skill == nil || !@actor.skill_can_use?(@skill.id)
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      $game_party.actors.each_index {|i|
          @target_windows.push(Window_CMSTarget.new($game_party.actors[i]))}
      @target_index = 0
      $game_system.se_play($data_system.decision_se)
      if @skill.scope.between?(3, 6)
        @skill_window.active = false
        @target_windows.each {|win| win.visible = win.active = true}
        if [4, 6].include?(@skill.scope)
          @target_windows.each {|win| win.index = -2}
        else
          @target_windows[@target_index].index = 0
        end
      elsif @skill.common_event_id > 0
        $game_temp.common_event_id = @skill.common_event_id
        $game_system.se_play(@skill.menu_se)
        @actor.sp -= @skill.sp_cost
        (@status_windows + @target_windows).each {|win| win.refresh}
        @skill_window.refresh
        @scene = Scene_Map.new
      elsif @skill.scope == 7
        $game_system.se_play($data_system.buzzer_se)
      end
    elsif Input.trigger?(Input::R) || Input.trigger?(Input::L)
      $game_system.se_play($data_system.cursor_se)
      if Input.trigger?(Input::R)
        @actor_index = (@actor_index+1) % $game_party.actors.size
      elsif Input.trigger?(Input::L)
        @actor_index += $game_party.actors.size-1
        @actor_index %= $game_party.actors.size
      end
      @actor = $game_party.actors[@actor_index]
      @skill_window.update_actor(@actor)
      @skill_window.index = 0
    end
  end
  
  def update_skill_target
    if Input.trigger?(Input::B)
      del_target
      $game_system.se_play($data_system.cancel_se)
      @skill_window.active = true
      @target_index = -1
    elsif Input.trigger?(Input::C)
      unless @actor.skill_can_use?(@skill.id)
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      if @target_windows[0].index == -2
        used = false
        $game_party.actors.each {|actor| used |= actor.skill_effect(@actor, @skill)}
      else
        used = $game_party.actors[@target_index].skill_effect(@actor, @skill)
      end
      if used
        $game_system.se_play(@skill.menu_se)
        @actor.sp -= @skill.sp_cost
        (@status_windows + @target_windows).each {|win| win.refresh}
        @skill_window.refresh
        if $game_party.all_dead?
          @scene = Scene_Gameover.new
        elsif @skill.common_event_id > 0
          $game_temp.common_event_id = @skill.common_event_id
          @scene = Scene_Map.new
        end
      else
        $game_system.se_play($data_system.buzzer_se)
      end
    else
      update_target
    end
  end
  
  def update_right_equip
    @item_windows.each_index {|i|
        @item_windows[i].visible = (@right_window.index == i)}
    @item_window = @item_windows[@right_window.index]
    newmode = [@right_window.index, 1].min
    if newmode != @left_window.mode
      @left_window.mode = newmode
      @left_window.refresh
    end
    if Input.trigger?(Input::B)
      del_equip
      $game_system.se_play($data_system.cancel_se)
      @help_window.x, @help_window.y = 660, 0
      @command_window.active = true
      @actor_index = -1
    elsif Input.trigger?(Input::C)
      if @actor.equip_fix?(@right_window.index)
        $game_system.se_play($data_system.buzzer_se)
      else
        $game_system.se_play($data_system.decision_se)
        @right_window.active = false
        @item_window.active, @item_window.index = true, 0
        equip_refresh
      end
    elsif Input.trigger?(Input::R) || Input.trigger?(Input::L)
      $game_system.se_play($data_system.cursor_se)
      if Input.trigger?(Input::R)
        @actor_index = (@actor_index+1) % $game_party.actors.size
      elsif Input.trigger?(Input::L)
        @actor_index += $game_party.actors.size-1
        @actor_index %= $game_party.actors.size
      end
      @actor = $game_party.actors[@actor_index]
      @right_window.update_actor(@actor)
      @left_window.update_actor(@actor)
      @item_windows.each_index {|i| @item_windows[i].update_actor(@actor, i)}
    end
  end

  def update_eitem
    if Input.trigger?(Input::B)
      $game_system.se_play($data_system.cancel_se)
      @right_window.active = true
      @item_window.active, @item_window.index = false, -1
      equip_refresh
    elsif Input.trigger?(Input::C)
      $game_system.se_play($data_system.equip_se)
      item = @item_window.data
      @actor.equip(@right_window.index, item == nil ? 0 : item.id)
      @right_window.active = true
      @item_window.active, @item_window.index = false, -1
      @right_window.refresh
      @item_window.refresh
      (@item_windows + @status_windows).each {|win| win.refresh}
      equip_refresh
    elsif Input.repeat?(Input::UP) || Input.repeat?(Input::DOWN) ||
        Input.repeat?(Input::R) || Input.repeat?(Input::L)
      equip_refresh
    end
  end
  
  def update_playerstatus
    if Input.trigger?(Input::B)
      $game_system.se_play($data_system.cancel_se)
      @command_window.active = true
      @actor_index = -1
      del_status
    elsif Input.trigger?(Input::R) || Input.trigger?(Input::RIGHT) ||
        Input.trigger?(Input::L) || Input.trigger?(Input::LEFT)
      $game_system.se_play($data_system.cursor_se)
      if Input.trigger?(Input::R) || Input.trigger?(Input::RIGHT)
        @actor_index = (@actor_index+1) % $game_party.actors.size
      elsif Input.trigger?(Input::L) || Input.trigger?(Input::LEFT)
        @actor_index += $game_party.actors.size-1
        @actor_index %= $game_party.actors.size
      end
      @actor = $game_party.actors[@actor_index]
      @playerstatus_window.update_actor(@actor)
    end
  end
  
  def update_options
    if Input.trigger?(Input::B)
      del_options
      $game_system.se_play($data_system.cancel_se)
      @command_window.active = true
      return
    end
    case @options_window.get_option
    when 'BGM Volume'
      if Input.repeat?(Input::RIGHT)
        $game_system.bgm_volume += 5
        $game_system.bgm_volume = 100 if $game_system.bgm_volume > 100
        $game_system.bgm_play($game_system.bgm_memorize)
        @options_window.refresh
      elsif Input.repeat?(Input::LEFT)
        $game_system.bgm_volume -= 5
        $game_system.bgm_volume = 0 if $game_system.bgm_volume < 0
        $game_system.bgm_play($game_system.bgm_memorize)
        @options_window.refresh
      end
    when 'SFX Volume'
      if Input.repeat?(Input::RIGHT)
        $game_system.sfx_volume += 5
        if $game_system.sfx_volume > 100
          $game_system.sfx_volume = 100
        else
          $game_system.se_play($data_system.cursor_se)
        end
        @options_window.refresh
      elsif Input.repeat?(Input::LEFT)
        $game_system.sfx_volume -= 5
        $game_system.sfx_volume = 0 if $game_system.sfx_volume < 0
        $game_system.se_play($data_system.cursor_se)
        @options_window.refresh
      end
    when 'Battle BGM'
      if Input.repeat?(Input::LEFT) || Input.repeat?(Input::RIGHT) ||
          Input.repeat?(Input::C)
        if $game_switches[BGM_Lock] || BATTLE_BGMS.size <= 1
          $game_system.se_play($data_system.buzzer_se)
        else
          $game_system.se_play($data_system.decision_se)
          ind = $game_variables[BGM_Variable]
          if Input.repeat?(Input::RIGHT) || Input.repeat?(Input::C)
            ind = (ind+1) % BATTLE_BGMS.size
          elsif Input.repeat?(Input::LEFT)
            ind = (ind+BATTLE_BGMS.size-1) % BATTLE_BGMS.size
          end
          $game_variables[BGM_Variable] = ind
          $game_system.reset_battle_bgm
          @options_window.refresh
        end
      end
    when 'Battle Cam'
      if Input.repeat?(Input::LEFT) || Input.repeat?(Input::RIGHT) ||
          Input.repeat?(Input::C)
        if CAM_AVAILABLE
          $game_system.se_play($data_system.decision_se)
          $game_system.cam = ($game_system.cam+1) % 2
          $game_system.get_cam
          @options_window.refresh
        else
          $game_system.se_play($data_system.buzzer_se)
        end
      end
    when 'Bar Style'
      if Input.repeat?(Input::RIGHT)
        if $game_system.bar_opacity == 0
          $game_system.se_play($data_system.buzzer_se)
        else
          $game_system.bar_style = ($game_system.bar_style + 1) % 7
          $game_system.se_play($data_system.decision_se)
          @options_window.refresh
          @status_windows.each {|win| win.refresh}
        end
      elsif Input.repeat?(Input::LEFT)
        if $game_system.bar_opacity == 0
          $game_system.se_play($data_system.buzzer_se)
        else
          $game_system.bar_style = ($game_system.bar_style + 6) % 7
          $game_system.se_play($data_system.decision_se)
          @options_window.refresh
          @status_windows.each {|win| win.refresh}
        end
      end
    when 'Bar Opacity'
      if Input.repeat?(Input::LEFT) || Input.repeat?(Input::RIGHT)
        $game_system.se_play($data_system.decision_se)
        $game_system.bar_opacity += (Input.repeat?(Input::RIGHT) ? 64 : -64)
        @options_window.refresh
        @status_windows.each {|win| win.refresh}
      end
    when 'Font'
      if Input.repeat?(Input::RIGHT)
        $game_system.se_play($data_system.decision_se)
        @options_window.current_font += 1
        @options_window.current_font %= FONTS.size
        @options_window.refresh
      elsif Input.repeat?(Input::LEFT)
        $game_system.se_play($data_system.decision_se)
        @options_window.current_font += FONTS.size - 1
        @options_window.current_font %= FONTS.size
        @options_window.refresh
      elsif Input.repeat?(Input::C)
        $game_system.se_play($data_system.decision_se)
        $game_system.fontname = @options_window.font_name
        @command_window.refresh
        @info_window.refresh
        @status_windows.each {|win| win.refresh}
        @help_window.refresh
        @options_window.refresh
        (0...5).each {|i| @command_window.disable_item(i)} if $game_party.actors.size == 0
        @command_window.disable_item(6) if $game_system.save_disabled
        @command_window.disable_item(7) unless @command_window.continue
      end
    when 'Windowskin'
      if Input.repeat?(Input::RIGHT)
        $game_system.se_play($data_system.decision_se)
        @options_window.current_skin += 1
        @options_window.current_skin %= SKINS.size
        @options_window.refresh
      elsif Input.repeat?(Input::LEFT)
        $game_system.se_play($data_system.decision_se)
        @options_window.current_skin += SKINS.size - 1
        @options_window.current_skin %= SKINS.size
        @options_window.refresh
      elsif Input.repeat?(Input::C)
        $game_system.se_play($data_system.decision_se)
        $game_system.windowskin_name = @options_window.skin_name
      end
    end
  end
  
  def update_end
    if Input.trigger?(Input::B) || Input.trigger?(Input::C) &&
        @end_window.index == 0
      $game_system.se_play($data_system.cancel_se)
      @command_window.active = true
      del_end
    elsif Input.trigger?(Input::C)
      Graphics.freeze
      $game_system.se_play($data_system.decision_se)
      Audio.bgm_fade(800)
      Audio.bgs_fade(800)
      Audio.me_fade(800)
      @end_window.index == 1 ? @scene = Scene_Title.new : $scene = nil
      del_end
    end
  end

end

#==============================================================================
# Scene_CMSSave
#==============================================================================

class Scene_CMSSave < Scene_Save
  
  def on_cancel
    $game_system.se_play($data_system.cancel_se)
    $scene = Scene_Menu.new(6)
  end
  
end

#==============================================================================
# Scene_CMSLoad
#==============================================================================

class Scene_CMSLoad < Scene_Load
  
  def on_cancel
    $game_system.se_play($data_system.cancel_se)
    $scene = Scene_Menu.new(7)
  end
  
end
