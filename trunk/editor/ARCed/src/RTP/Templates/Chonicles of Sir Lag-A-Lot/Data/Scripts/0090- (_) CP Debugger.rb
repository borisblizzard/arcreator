#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=
# Chaos Project Debug System by Blizzard
# Version: 1.0b
# Type: Heavy Debug Utility
# Date: 25.8.2007
# Date v1.0b: 5.09.2007
#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=
# 
# Compatibility:
# 
#   99% compatible with SDK v1.x. 90% compatible with SDK v2.x. Can cause
#   incompatibility issues with following systems:
#   - exotic CBS-es
#   - exotic Skill Systems
#   - exotic Weapon Systems
#   - exotic Armor Systems
#   - exotic Item Systems
#   - exotic Party Changers
#   This script is being used by "The Legend of Lexima IV - Chaos Project" and
#   no incompatiblity issues are known with any of the large number of custom
#   systems and scripts this game has built in.
# 
# 
# Features:
# 
#   - new options in DEBUG menu (press F9 to open the DEBUG menu):
#     -> Manage Switches
#     -> Manage Variables
#     -> Manage Party
#     -> Manage System
#     -> Manage Actors
#     -> Manage Battle
#     -> Teleport
#     -> Easy Party Switcher
#     -> Save
#     -> Load
#     -> Return to DEBUG ROOM
#     -> Exit
#   - can be called from the map and from battle
#   - returns to the scene from where it was called
#   - supports "Easy Party Switcher" v2.1b and higher as enhancement
# 
# new in v1.0b:
#   - fixed glitch where skills would conflict with states
#   - fixed glitch where "Load" would be always displayed grayed out
#   - now beta
# 
# 
# Explanation:
# 
#   This script will allow you to use an enhanced debugging menu with many
#   useful options that even works in the battle without interrupting the
#   battle and resetting the Scene_Battle.
# 
# 
# Instructions:
# 
# - How to use:
#   
#   The Debug System can be called through pressing F9 either in battle or on
#   the map. This Debug_Scene only interrupts the calling scene and it is
#   possible that lag can appear in the Debug Scene. But upon exit, the calling
#   scene WILL NOT be restarted which means that battles will not be reseted
#   and can be continued as if nothing happened. Same goes for the map scene.
#   Note that changing HP/SP/states of actors will not be updated immediately
#   in the battle status window! If you change numeric variables you can hold
#   A, S and/or D to multiply the added/subtracted value by 10, 100 and/or 1000
#   which can result up to 1000000 if all three keys are being pressed while
#   changing the value of the variable. Each variable can be set to a value
#   from -99999999 to 99999999, regardless if those values are allowed
#   (i.e. actor has 99999 HP, even though his max HP are 8267). Same works for
#   actor class/weapon/armor IDs. "True" and "False" values are displayed as
#   "T" and "F" for more convenience. Items which can be set up in a special
#   menu are written in capital letters and have 'SP' as value. When you want
#   to change switches or variables you need to specifiy the range with
#   LEFT/RIGHT in the main debug screen. This is necessary to decrease lag as
#   drawing up to 5000 items (5000 is the max number of switches/variables you
#   can use) can crash the game, because of the "Script is hanging" error. Keep
#   in mind that you can quickly skip a couple of items on the list if you
#   press Q/W instead of UP/DOWN. 
#   
# - Configuration:
# 
#   Set DEBUG_ROOM_ID to the ID of your debug map to be able to use the option
#   "Return to DEBUG Room" so you can quickly return to a predefined map
#   without using the teleport command. You will be teleported to the center of
#   the Debug Room. If you set TELEPORT_POSITION to true you can set up the
#   position where you want to be teleported to when using the "Teleport"
#   in the debug screen. When using values out of range (like an actor's level
#   over 99 or under 0) the game may crash. If you want to prevent such a
#   crash in the Debug Menu, set PREVENT_CRASH to true. If you don't want to
#   get an error message at all, set SHOW_ERROR to false. Note that using
#   PREVENT_CRASH is not recommended as it could cover up possible bugs in this
#   or other scripts. The SAVE options are for custom save systems.
# 
# - Options:
#   
#   Manage Switches:
#     -> Turn switches on and off.
#   Manage Variables:
#     -> Change the value of variables. If you "access" a variable, you can
#        set up quickly very large positive and negative values.
#   Manage Party:
#     -> Allows changing of gold, steps, weapons, armors, items and any integer
#        and false/true variable used by other scripts.
#   Manage System:
#     -> Allows changing of any integer and false/true variable used by the
#        default and any other scripts.
#   Manage Actors:
#     -> Allows changing of any integer and false/true variable used by the
#        default and any other scripts. (i.e. hp, sp, sr, limit, etc)
#     -> When changing skills and/or states a special screen will appear.
#     -> When changine the weapon ID/armor IDs/class ID the window in the upper
#        right corner will display the current weapon/armor/class
#   Manage Battle:
#     -> This option is only available if the debug screen was called from
#        battle.
#     -> Allows quick winning, losing or aborting/escaping the battle. This
#        works for ANY battle, regardless of the limitations you have set up.
#     -> Allows access to enemy integer and false/true variables.
#     -> Changing special enemy states will call a special screen.
#   Teleport:
#     -> Allows quick teleportation to any map in your game.
#     -> You can set up the position if you set TELEPORT_POSITION to true in
#        the configuration. Otherwise you will be set at the center of the map.
#     -> WILL return to the map scene.
#   Easy Party Switcher:
#     -> If you are using Easy Party Switcher v2.x, you can call the scene from
#        here. Note that only v2.1b and higher will override the
#        "not_available" and "disabled_for_party" options. Otherwise this
#        option will be disabled. You can also use the EPS only for debug and
#        not in your game at all.
#     -> WILL return to the map scene.
#   Save:
#     -> Allows saving the game in case you're using a CMS without Saving
#        option.
#     -> WILL return to the map after exiting this scene.
#   Load:
#     -> Allows loading games in case you are using the DMS or a CMS without
#        Loading option. Will be disabled if you have no save file to load.
#     -> WILL return to the map after exiting this scene.
#   Return to DEBUG ROOM:
#     -> Allows quick teleport to a predefined map where you can set up events
#        for advanced testing. If DEBUG_ROOM_ID is 0, this option will be
#        disabled.
#     -> WILL return to the map scene.
#   Exit:
#     -> Returns to the scene where the debug screen was called from.
# 
# 
# If you find any bugs, please report them here:
# http://www.chaosproject.co.nr
#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# the ID of the map where you have set up various events for quick testing
DEBUG_ROOM_ID = 0
# set this value to true if you want to decide the coordinates where you want
# to be teleported when using the teleport command, othersise the position will
# be the center of the map by default
TELEPORT_POSITION = false
# set this option to true if you want to be able to set up values out of range
# without fearing a crash, an error message will appear
PREVENT_CRASH = true
# if you have set PREVENT_CRASH to true and want an error message to appear
SHOW_ERROR = true
# if you are using a custom save system
SAVE_NAME = 'Save'
SAVE_EXTENSION = 'rxdata'
SAVE_FILES_NUMBER = 4

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#==============================================================================
# Object
#==============================================================================

class Object
  
  def get_internal(var)
    eval("return @#{var}")
  end
  
  def set_internal(var, val)
    eval("@#{var} = val")
  end
  
end

#==============================================================================
# Window_DebugInfo
#==============================================================================

class Window_DebugInfo < Window_Base
  
  def initialize
    super(400, 288, 240, 192)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.contents.font.name = 'Arial'
    self.contents.font.size = 24
    self.z, self.back_opacity = 10000, 224
  end
  
  def set_mode(mode)
    self.contents.clear
    self.contents.font.color = system_color
    case mode
    when -2
      self.contents.draw_text(4, 0, 200, 32, 'ENTER')
      self.contents.draw_text(4, 32, 200, 32, '← / →')
      self.contents.draw_text(4, 64, 200, 32, 'Hold A')
      self.contents.draw_text(4, 96, 200, 32, 'Hold S')
      self.contents.draw_text(4, 128, 200, 32, 'Hold D')
      self.contents.font.color = normal_color
      self.contents.draw_text(4, 0, 200, 32, 'Access', 2)
      self.contents.draw_text(4, 32, 200, 32, '-/+ 1', 2)
      self.contents.draw_text(4, 64, 200, 32, '× 10', 2)
      self.contents.draw_text(4, 96, 200, 32, '× 100', 2)
      self.contents.draw_text(4, 128, 200, 32, '× 1000', 2)
    when -1
      self.contents.draw_text(4, 0, 200, 32, '↑ / ↓')
      self.contents.draw_text(4, 32, 200, 32, '← / →')
      self.contents.draw_text(4, 64, 200, 32, 'ENTER')
      self.contents.font.color = normal_color
      self.contents.draw_text(4, 0, 200, 32, 'Choose', 2)
      self.contents.draw_text(4, 32, 200, 32, 'Range', 2)
      self.contents.draw_text(4, 64, 200, 32, 'Access', 2)
    when 0
      self.contents.draw_text(4, 0, 200, 32, '← / →')
      self.contents.font.color = normal_color
      self.contents.draw_text(4, 0, 200, 32, 'Trigger Switch', 2)
    when 1..3
      self.contents.draw_text(4, 0, 200, 32, '← / →')
      self.contents.draw_text(4, 32, 200, 32, 'Hold A')
      self.contents.draw_text(4, 64, 200, 32, 'Hold S')
      self.contents.draw_text(4, 96, 200, 32, 'Hold D')
      self.contents.font.color = normal_color
      self.contents.draw_text(4, 0, 200, 32, '-/+ 1', 2)
      self.contents.draw_text(4, 32, 200, 32, '× 10', 2)
      self.contents.draw_text(4, 64, 200, 32, '× 100', 2)
      self.contents.draw_text(4, 96, 200, 32, '× 1000', 2)
    when 4
      self.contents.draw_text(4, 0, 200, 32, 'ENTER')
      self.contents.font.color = normal_color
      self.contents.draw_text(4, 0, 200, 32, 'Access', 2)
    when 5
      self.contents.draw_text(4, 0, 200, 32, '← / →')
      self.contents.draw_text(4, 32, 200, 32, 'ENTER')
      self.contents.font.color = normal_color
      self.contents.draw_text(4, 0, 200, 32, 'Battle End', 2)
      self.contents.draw_text(4, 32, 200, 32, 'Access', 2)
    when 6
      self.contents.draw_text(4, 0, 200, 32, 'ENTER')
      self.contents.draw_text(4, 32, 200, 32, '← / →')
      self.contents.draw_text(4, 64, 200, 32, 'Hold A')
      self.contents.draw_text(4, 96, 200, 32, 'Hold S')
      self.contents.font.color = normal_color
      self.contents.draw_text(4, 0, 200, 32, 'Teleport', 2)
      self.contents.draw_text(4, 32, 200, 32, '-/+ 1', 2)
      self.contents.draw_text(4, 64, 200, 32, '× 10', 2)
      self.contents.draw_text(4, 96, 200, 32, '× 100', 2)
    when 7
      self.contents.draw_text(4, 0, 200, 32, '← / →')
      self.contents.draw_text(4, 32, 200, 32, 'Hold A')
      self.contents.draw_text(4, 64, 200, 32, 'Hold S')
      self.contents.font.color = normal_color
      self.contents.draw_text(4, 0, 200, 32, '-/+ 1', 2)
      self.contents.draw_text(4, 32, 200, 32, '× 10', 2)
      self.contents.draw_text(4, 64, 200, 32, '× 100', 2)
    when 8
      self.contents.draw_text(4, 0, 200, 32, '← / →')
      self.contents.font.color = normal_color
      self.contents.draw_text(4, 0, 200, 32, 'Add / Remove', 2)
    end
  end
  
end
  
#==============================================================================
# Window_DebugInfo
#==============================================================================

class Window_DebugStatus < Window_Base
  
  def initialize(battler = nil)
    super(400, 0, 240, 288)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.contents.font.name = 'Arial'
    self.contents.font.size = 24
    refresh(battler)
    self.z, self.back_opacity = 10000, 224
  end
  
  def refresh(battler = nil)
    self.contents.clear
    if battler.is_a?(Array)
      self.visible = true
      case battler[0]
      when 0 then data = $data_classes
      when 1 then data = $data_weapons
      when 2 then data = $data_armors
      end
      min = [[battler[1]-4, 0].max, data.size-8].min
      max = [min+7, data.size-1].min
      (min..max).each {|i|
        self.contents.font.color =
            (i == battler[1] ? normal_color : disabled_color)
        self.contents.draw_text(4, (i-min)*32, 200, 32, (data[i] == nil ?
            '--------' : data[i].name))}
    elsif battler != nil
      self.visible = true
      draw_actor_name(battler, 4, 0)
      self.contents.font.color = system_color
      self.contents.draw_text(4, 32, 200, 32, "Battler ID: #{battler.id}")
      draw_actor_hp(battler, 4, 64, 200)
      draw_actor_sp(battler, 4, 96, 200)
      draw_actor_state(battler, 4, 128, 200)
      if battler.is_a?(Game_Actor)
        self.contents.font.color = system_color
        if battler.index
          self.contents.draw_text(4, 224, 176, 32, 'Party Index:')
          self.contents.font.color = normal_color
          self.contents.draw_text(4, 224, 200, 32, battler.index.to_s, 2)
        else
          self.contents.draw_text(4, 224, 176, 32, 'Not in Party')
        end
        draw_actor_level(battler, 4, 160)
        draw_actor_exp(battler, 4, 192)
      elsif battler.is_a?(Game_Enemy)
        self.contents.font.color = system_color
        self.contents.draw_text(4, 160, 160, 32, 'Hidden:')
        self.contents.draw_text(4, 192, 160, 32, 'Immortal:')
        self.contents.draw_text(4, 224, 160, 32, 'Member Index:')
        self.contents.font.color = normal_color
        self.contents.draw_text(4, 160, 200, 32, battler.hidden ? 'Yes' : 'No', 2)
        self.contents.draw_text(4, 192, 200, 32, battler.immortal ? 'Yes' : 'No', 2)
        self.contents.draw_text(4, 224, 200, 32, battler.index.to_s, 2)
      end
    else
      self.visible = false
    end
  end
  
end
  
#==============================================================================
# Window_DebugArray
#==============================================================================

class Window_DebugArray < Window_Selectable
  
  attr_reader :battler
  
  def initialize(battler, ary)
    super(0, 64, 400, 416)
    @type = (ary[1].is_a?(RPG::Skill) ? 0 : 1)
    @battler, @ary, @triggers = battler, ary[1, ary.size-1], []
    input = (@type == 0 ? @battler.skills : @battler.states)
    (1...ary.size).each {|i| @triggers.push(input.include?(i))}
    @item_max = @ary.size
    self.contents = Bitmap.new(width - 32, @item_max*32)
    self.contents.font.name = 'Arial'
    self.contents.font.size = 24
    refresh
    self.z, self.index, self.back_opacity = 10000, 0, 224
  end
  
  def refresh
    self.contents.clear
    (0...@item_max).each {|i| draw_item(i)}
  end
  
  def update
    super
    if Input.repeat?(Input::RIGHT) || Input.repeat?(Input::LEFT)
      $game_system.se_play($data_system.cursor_se)
      @triggers[index] = !@triggers[index]
      draw_item(index)
      if @type == 1
        @ary[index].plus_state_set.each {|i|
            @triggers[i-1] = true
            draw_item(i-1)}
        @ary[index].minus_state_set.each {|i|
            @triggers[i-1] = false
            draw_item(i-1)}
      end
    end
  end
  
  def draw_item(i)
    self.contents.fill_rect(0, i*32, 368, 32, Color.new(0, 0, 0, 0))
    self.contents.draw_text(4, i*32, 360, 32, sprintf('%03d', @ary[i].id))
    if @type == 0
      icon = RPG::Cache.icon(@ary[i].icon_name)
      self.contents.blt(48, i*32+4, icon, Rect.new(0, 0, 24, 24))
      self.contents.draw_text(80, i*32, 284, 32, @ary[i].name)
    else
      self.contents.draw_text(48, i*32, 320, 32, @ary[i].name)
    end
    self.contents.draw_text(4, i*32, 360, 32, (@triggers[i] ? 'Yes' : 'No'), 2)
  end
  
  def dispose
    new = []
    (0...@triggers.size).each {|i| new.push(i+1) if @triggers[i]}
    if @type == 0
      (@battler.skills - new).each {|i| @battler.forget_skill(i)}
      (new - @battler.skills).each {|i| @battler.learn_skill(i)}
    else
      (@battler.states - new).each {|i| @battler.remove_state(i)}
      (new - @battler.states).each {|i| @battler.add_state(i)}
    end
    super
  end
  
end
  
#==============================================================================
# Window_DebugParty
#==============================================================================

class Window_DebugParty < Window_Selectable
  
  def initialize(ary)
    super(0, 64, 400, 416)
    @type = (ary[1].is_a?(RPG::Item) ? 0 : (ary[1].is_a?(RPG::Weapon) ? 1 : 2))
    @ary = ary[1, ary.size-1]
    @item_max = @ary.size
    self.contents = Bitmap.new(width - 32, @item_max*32)
    self.contents.font.name = 'Arial'
    self.contents.font.size = 24
    refresh
    self.z, self.index, self.back_opacity = 10000, 0, 224
  end
  
  def refresh
    self.contents.clear
    (0...@item_max).each {|i| draw_item(i)}
  end
  
  def update
    super
    val = 1
    val *= 10 if Input.press?(Input::X)
    val *= 100 if Input.press?(Input::Y)
    if Input.repeat?(Input::RIGHT)
      old_value = new_value = 0
      case @type
      when 0
        old_value = $game_party.item_number(index + 1)
        $game_party.gain_item(index+1, val)
        new_value = $game_party.item_number(index + 1)
      when 1
        old_value = $game_party.weapon_number(index + 1)
        $game_party.gain_weapon(index+1, val)
        new_value = $game_party.weapon_number(index + 1)
      when 2
        old_value = $game_party.armor_number(index + 1)
        $game_party.gain_armor(index+1, val)
        new_value = $game_party.armor_number(index + 1)
      end
      if old_value != new_value
        $game_system.se_play($data_system.cursor_se)
        draw_item(index)
      else
        $game_system.se_play($data_system.buzzer_se)
      end
    elsif Input.repeat?(Input::LEFT)
      old_value = new_value = 0
      case @type
      when 0
        old_value = $game_party.item_number(index + 1)
        $game_party.lose_item(index+1, val)
        new_value = $game_party.item_number(index + 1)
      when 1
        old_value = $game_party.weapon_number(index + 1)
        $game_party.lose_weapon(index+1, val)
        new_value = $game_party.weapon_number(index + 1)
      when 2
        old_value = $game_party.armor_number(index + 1)
        $game_party.lose_armor(index+1, val)
        new_value = $game_party.armor_number(index + 1)
      end
      if old_value != new_value
        $game_system.se_play($data_system.cursor_se)
        draw_item(index)
      else
        $game_system.se_play($data_system.buzzer_se)
      end
    end
  end
  
  def draw_item(i)
    self.contents.fill_rect(0, i*32, 368, 32, Color.new(0, 0, 0, 0))
    self.contents.draw_text(4, i*32, 360, 32, sprintf('%03d', @ary[i].id))
    icon = RPG::Cache.icon(@ary[i].icon_name)
    self.contents.blt(48, i*32+4, icon, Rect.new(0, 0, 24, 24))
    self.contents.draw_text(80, i*32, 284, 32, @ary[i].name)
    number = case @type
    when 0 then $game_party.item_number(i+1).to_s
    when 1 then $game_party.weapon_number(i+1).to_s
    when 2 then $game_party.armor_number(i+1).to_s
    end
    self.contents.draw_text(4, i*32, 360, 32, number, 2)
  end
  
end
  
#==============================================================================
# Window_DebugList
#==============================================================================

class Window_DebugBattler < Window_Selectable
  
  attr_reader :battler
  
  def initialize(battler, status_window)
    super(0, 64, 400, 416)
    @status_window, @battler, @commands = status_window, battler, []
    dont_show = ['actor_id', 'animation_hit', 'animation_id', 'battler_hue',
      'blink', 'character_hue', 'critical', 'damage_pop', 'enemy_id', 'name',
      'member_index', 'state_changed', 'troop_id', 'white_flash']
    @battler.instance_variables.each {|item|
        value = @battler.get_internal(item[1, item.size-1])
        if (value.is_a?(Integer) || value.is_a?(FalseClass) ||
            value.is_a?(TrueClass)) && !dont_show.include?(item[1, item.size-1])
          @commands.push(item[1, item.size-1])
        end}
    @commands.push('SKILLS') if @battler.is_a?(Game_Actor)
    @commands.push('STATES')
    @commands.sort!
    @item_max = @commands.size
    self.contents = Bitmap.new(width - 32, @item_max * 32)
    self.contents.font.name = 'Arial'
    self.contents.font.size = 24
    refresh
    self.active, self.z, self.index, self.back_opacity = true, 10000, 0, 224
  end
  
  def refresh
    self.contents.clear
    (0...@item_max).each {|i| draw_instance_variable(i)}
  end
  
  def special?
    return case @commands[index]
    when 'SKILLS' then 0
    when 'STATES' then 1
    end
  end
  
  def update(old_index = index)
    super()
    value = @battler.get_internal(@commands[index])
    if old_index != index
      case @commands[index][0, 5]
      when 'class' then @status_window.refresh([0, value])
      when 'weapo' then @status_window.refresh([1, value])
      when 'armor' then @status_window.refresh([2, value])
      else
        @status_window.refresh(@battler)
      end
    end
    if value.is_a?(Integer)
      val = 1
      val *= 10 if Input.press?(Input::X)
      val *= 100 if Input.press?(Input::Y)
      val *= 1000 if Input.press?(Input::Z)
      if Input.repeat?(Input::LEFT)
        case @commands[index][0, 5]
        when 'class'
          value = (value+$data_classes.size-val) % $data_classes.size
          new = [0, value]
        when 'weapo'
          value = (value+$data_weapons.size-val) % $data_weapons.size
          new = [1, value]
        when 'armor'
          value = (value+$data_armors.size-val) % $data_armors.size
          new = [2, value]
        else
          value -= val
          new = @battler
        end
      elsif Input.repeat?(Input::RIGHT)
        case @commands[index][0, 5]
        when 'class'
          value = (value+val) % $data_classes.size
          new = [0, value]
        when 'weapo'
          value = (value+val) % $data_weapons.size
          new = [1, value]
        when 'armor'
          value = (value+val) % $data_armors.size
          new = [2, value]
        else
          value += val
          new = @battler
        end
      end
      if new != nil
        $game_system.se_play($data_system.cursor_se)
        @battler.set_internal(@commands[index], value)
        @status_window.refresh(new)
        draw_instance_variable(index)
      end
    elsif (value == true || value == false) &&
        (Input.repeat?(Input::LEFT) || Input.repeat?(Input::RIGHT))
      $game_system.se_play($data_system.cursor_se)
      @battler.set_internal(@commands[index], !value)
      @status_window.refresh(@battler)
      draw_instance_variable(index)
    end
  end
  
  def draw_instance_variable(i)
    self.contents.fill_rect(4, i*32, 368, 32, Color.new(0, 0, 0, 0))
    self.contents.draw_text(4, i*32, 280, 32, @commands[i])
    value = @battler.get_internal(@commands[i])
    value = case value
    when true then 'T'
    when false then 'F'
    when nil then 'SP'
    else
      value.to_s
    end
    self.contents.draw_text(244, i*32, 120, 32, value, 2)
  end
  
end

#==============================================================================
# Window_DebugList
#==============================================================================

class Window_DebugList < Window_Selectable
  
  attr_reader :type
  attr_reader :battle_mode
  attr_reader :swi
  attr_reader :var
  attr_reader :map
  
  def initialize(type, other = nil)
    super(0, 64, 400, 416)
    $battle, @commands, @type = 0, [], type
    case type
    when Array
      @commands, @swi, @var, @type = other, type[1], type[2], 7
    when 0
      @type = type + other[type] - 1
      (@type+1...[@type+101, $data_system.switches.size].min).each {|i|
          @commands.push($data_system.switches[i])}
    when 1
      @type = type + other[type] - 1
      (@type...[@type+100, $data_system.variables.size].min).each {|i|
          @commands.push($data_system.variables[i])}
    when 2
      @object = $game_party
      @object.instance_variables.sort.each {|item|
          value = @object.get_internal(item[1, item.size-1])
          if value.is_a?(Integer) || value.is_a?(FalseClass) ||
              value.is_a?(TrueClass)
            @commands.push(item[1, item.size-1])
          end}
      @commands.push('ITEMS', 'WEAPONS', 'ARMORS')
      @commands.sort!
    when 3
      @object = $game_system
      @object.instance_variables.sort.each {|item|
          value = @object.get_internal(item[1, item.size-1])
          if value.is_a?(Integer) || value.is_a?(FalseClass) ||
              value.is_a?(TrueClass)
            @commands.push(item[1, item.size-1])
          end}
      @commands.sort!
    when 4
      (1...$data_actors.size).each {|i| @commands.push($game_actors[i].name)}
      @status_window = other
      @status_window.refresh($game_actors[1])
    when 5
      @commands.push('Manipulate Battle')
      $game_troop.enemies.each {|enemy| @commands.push(enemy.name)}
      @status_window = other
      @status_window.refresh
    when 6
      @map_data = load_data('Data/MapInfos.rxdata')
      @commands = ['Map doesn\'t exist']
      @commands.push('X coordinate', 'Y coordinate') if TELEPORT_POSITION
      @map = [0, 0, 0]
      self.height = @commands.size*32 + 32
    end
    @item_max = @commands.size
    self.contents = Bitmap.new(width - 32, @item_max * 32)
    self.contents.font.name, self.contents.font.size = 'Arial', 24
    refresh
    self.z, self.index, self.back_opacity = 10000, 0, 224
  end
  
  def refresh
    self.contents.clear
    case @type % 100
    when 0 then (0...@item_max).each {|i| draw_switch(i)}
    when 1 then (0...@item_max).each {|i| draw_variable(i)}
    when 2..3 then (0...@item_max).each {|i| draw_instance_variable(i)}
    when 4..5, 7 then (0...@item_max).each {|i| draw_item(i)}
    when 6 then (0...@item_max).each {|i| draw_map(i, disabled_color)}
    end
    if @type == 5
      draw_battle
    elsif @type == 7
      draw_main(0)
      draw_main(1)
    end
  end
  
  def special?
    return case @commands[index]
    when 'ITEMS' then 1
    when 'WEAPONS' then 2
    when 'ARMORS' then 3
    end
  end
  
  def update(old_index = index)
    super()
    case @type % 100
    when 0
      if Input.trigger?(Input::LEFT) || Input.trigger?(Input::RIGHT)
        $game_system.se_play($data_system.decision_se)
        $game_switches[index+@type+1] = !$game_switches[index+@type+1]
        draw_switch(index)
      end
    when 1
      val = 1
      val *= 10 if Input.press?(Input::X)
      val *= 100 if Input.press?(Input::Y)
      val *= 1000 if Input.press?(Input::Z)
      if Input.repeat?(Input::LEFT)
        if $game_variables[index+@type] > -99999999
          $game_system.se_play($data_system.cursor_se)
          $game_variables[index+@type] =
              [$game_variables[index+@type] - val, -99999999].max
          draw_variable(index)
        else
          $game_system.se_play($data_system.buzzer_se)
        end
      elsif Input.repeat?(Input::RIGHT)
        if $game_variables[index+@type] < 99999999
          $game_system.se_play($data_system.cursor_se)
          $game_variables[index+@type] =
              [$game_variables[index+@type] + val, 99999999].min
          draw_variable(index)
        else
          $game_system.se_play($data_system.buzzer_se)
        end
      end
    when 2..3
      value = @object.get_internal(@commands[index])
      if value.is_a?(Integer)
        val = 1
        val *= 10 if Input.press?(Input::X)
        val *= 100 if Input.press?(Input::Y)
        val *= 1000 if Input.press?(Input::Z)
        if Input.repeat?(Input::LEFT)
          $game_system.se_play($data_system.cursor_se)
          value = @object.get_internal(@commands[index])
          @object.set_internal(@commands[index], value - val)
          draw_instance_variable(index)
        elsif Input.repeat?(Input::RIGHT)
          $game_system.se_play($data_system.cursor_se)
          value = @object.get_internal(@commands[index])
          @object.set_internal(@commands[index], value + val)
          draw_instance_variable(index)
        end
      elsif (value == true || value == false) &&
          (Input.repeat?(Input::LEFT) || Input.repeat?(Input::RIGHT))
        $game_system.se_play($data_system.cursor_se)
        value = @object.get_internal(@commands[index])
        @object.set_internal(@commands[index], !value)
        draw_instance_variable(index)
      end
    when 4
      @status_window.refresh($game_actors[index+1]) if old_index != index
      if Input.trigger?(Input::C)
        $game_system.se_play($data_system.decision_se)
      end
    when 5
      if old_index != index
        @status_window.refresh(index == 0 ? nil : $game_troop.enemies[index-1])
      end
      if index == 0
        mode = $battle
        if Input.repeat?(Input::RIGHT)
          $battle = ($battle + 1) % 4
        elsif Input.repeat?(Input::LEFT)
          $battle = ($battle + 3) % 4
        end
        if mode != $battle
          $game_system.se_play($data_system.cursor_se)
          draw_item(0)
          draw_battle
        end
      elsif Input.trigger?(Input::C)
        $game_system.se_play($data_system.decision_se)
      end
    when 6
      val = 1
      val *= 10 if Input.press?(Input::X)
      val *= 100 if Input.press?(Input::Y)
      if index == 0
        old_map = @map[0]
        if Input.repeat?(Input::RIGHT)
          @map[0] = (@map[0]+val) % 1000
        elsif Input.repeat?(Input::LEFT)
          @map[0] = (@map[0]+1000-val) % 1000
        end
        if old_map != @map[0]
          $game_system.se_play($data_system.cursor_se)
          if @map_data.keys.include?(@map[0])
            @loaded = load_data(sprintf('Data/Map%03d.rxdata', @map[0]))
            @commands[0] = @map_data[@map[0]].name
            draw_map(0)
            if TELEPORT_POSITION
              @map[1] = [@loaded.width, @map[1]].min
              @map[2] = [@loaded.height, @map[2]].min
              draw_map(1)
              draw_map(2)
            end
          else
            @loaded = nil
            @commands[0] = 'Map doesn\'t exist'
            draw_map(0, disabled_color)
            if TELEPORT_POSITION
              draw_map(1, disabled_color)
              draw_map(2, disabled_color)
            end
          end
        end
      elsif @loaded != nil
        limit = (index == 1 ? @loaded.width : @loaded.height)
        old_map = @map[index]
        if Input.repeat?(Input::RIGHT)
          @map[index] = (@map[index]+val) % limit
        elsif Input.repeat?(Input::LEFT)
          @map[index] = (@map[index]+limit-val) % limit
        end
        if old_map != @map[index]
          $game_system.se_play($data_system.cursor_se)
          draw_map(index)
        end
      elsif Input.repeat?(Input::RIGHT) || Input.repeat?(Input::LEFT)
        $game_system.se_play($data_system.buzzer_se)
      end
    when 7
      if index == 0
        val = @swi
        if Input.repeat?(Input::RIGHT)
          if $data_system.switches.size > 101
            @swi = (@swi + 100) % (($data_system.switches.size+98)/100*100)
          else
            $game_system.se_play($data_system.buzzer_se)
          end
        elsif Input.repeat?(Input::LEFT)
          if $data_system.switches.size > 100
            size = ($data_system.switches.size+98)/100*100
            @swi = (@swi+size-100) % size
          else
            $game_system.se_play($data_system.buzzer_se)
          end
        end
        if val != @swi
          $game_system.se_play($data_system.cursor_se)
          draw_item(0)
          draw_main(0)
        end
      elsif index == 1
        val = @var
        if Input.repeat?(Input::RIGHT)
          if $data_system.variables.size > 101
            @var = (@var + 100) % (($data_system.variables.size+98)/100*100)
          else
            $game_system.se_play($data_system.buzzer_se)
          end
        elsif Input.repeat?(Input::LEFT)
          if $data_system.variables.size > 100
            size = ($data_system.variables.size+98)/100*100
            @var = (@var+size-100) % size
          else
            $game_system.se_play($data_system.buzzer_se)
          end
        end
        if val != @var
          $game_system.se_play($data_system.cursor_se)
          draw_item(1)
          draw_main(1)
        end
      end
    end
  end
  
  def battler
    if @type == 4
      return $game_actors[index+1]
    elsif @type == 5 && index > 0
      return $game_troop.enemies[index-1]
    end
    return nil
  end
  
  def draw_switch(i)
    self.contents.fill_rect(4, i*32, 368, 32, Color.new(0, 0, 0, 0))
    self.contents.draw_text(4, i*32, 320, 32, "[#{sprintf('%04d', i+@type+1)}] #{@commands[i]}")
    self.contents.draw_text(324, i*32, 40, 32, $game_switches[i+@type+1] ? 'ON' : 'OFF', 2)
  end
  
  def draw_variable(i)
    self.contents.fill_rect(4, i*32, 368, 32, Color.new(0, 0, 0, 0))
    self.contents.draw_text(4, i*32, 240, 32, "[#{sprintf('%04d', i+@type)}] #{@commands[i]}")
    self.contents.draw_text(244, i*32, 120, 32, $game_variables[i+@type].to_s, 2)
  end
  
  def draw_instance_variable(i)
    self.contents.fill_rect(4, i*32, 368, 32, Color.new(0, 0, 0, 0))
    self.contents.draw_text(4, i*32, 280, 32, @commands[i])
    value = @object.get_internal(@commands[i])
    value = case value
    when true then 'T'
    when false then 'F'
    when nil then 'SP'
    else
      value.to_s
    end
    self.contents.draw_text(244, i*32, 120, 32, value, 2)
  end
  
  def draw_battle
    text = case $battle
    when 0 then ': Nothing'
    when 1 then ': Win'
    when 2 then ': Lose'
    when 3 then ': Abort/Escape'
    end
    self.contents.draw_text(244, 0, 200, 32, text)
  end
    
  def draw_item(i)
    self.contents.fill_rect(0, i*32, 368, 32, Color.new(0, 0, 0, 0))
    self.contents.draw_text(4, i*32, 360, 32, @commands[i])
  end
  
  def draw_map(i, color = normal_color)
    self.contents.fill_rect(0, i*32, 368, 32, Color.new(0, 0, 0, 0))
    self.contents.font.color = color
    self.contents.draw_text(4, i*32, 360, 32, @commands[i])
    self.contents.font.color = normal_color if i == 0
    self.contents.draw_text(4, i*32, 360, 32, @map[i].to_s, 2)
  end
  
  def draw_main(i)
    if i == 0
      text1 = sprintf('%04d', @swi)
      text2 = sprintf('%04d', [@swi+99, $data_system.switches.size-1].min)
    else
      text1 = sprintf('%04d', @var)
      text2 = sprintf('%04d', [@var+99, $data_system.variables.size-1].min)
    end
    self.contents.draw_text(4, i*32, 360, 32, "[#{text1}] - [#{text2}]", 2)
  end
  
  def disable_item(i)
    self.contents.font.color = disabled_color
    draw_item(i)
    self.contents.font.color = normal_color
  end
  
end

#==============================================================================
# Scene_Map
#==============================================================================

class Scene_Map
  
  alias upd_cp_debugger_later update
  def update
    upd_cp_debugger_later
    if $scene.is_a?(Scene_Debug)
      $scene = self
      scene = SceneSub_Debug.new
      Graphics.freeze
      scene.main
      Graphics.transition
    end
  end
  
end

#==============================================================================
# Scene_Battle
#==============================================================================

class Scene_Battle
  
  alias upd_cp_debugger_later update
  def update
    if $DEBUG && Input.trigger?(Input::F9)
      $game_system.se_play($data_system.decision_se)
      scene = SceneSub_Debug.new
      Graphics.freeze
      scene.main
      Graphics.transition
      if $battle != nil
        case $battle
        when 1..2
          battlers = ($battle == 1 ? $game_troop.enemies : $game_party.actors)
          battlers.each {|battler| battler.hp = 0 if battler.exist?}
          @party_command_window.active = @party_command_window.visible =
          @actor_command_window.active = @actor_command_window.visible = false
          @active_battler.blink = false unless @active_battler == nil
          @spriteset.update
          start_phase1
        when 3 then $game_temp.battle_abort = true
        end
        $battle = nil
      end
    else
      upd_cp_debugger_later
    end
  end
  
end

#==============================================================================
# SceneSub_Debug
#==============================================================================

class SceneSub_Debug
  
  def main
    @mem_index, @extra = [0, 0, 0], [1, 1]
    @commands = ['Manage Switches', 'Manage Variables', 'Manage Party',
                'Manage System', 'Manage Actors', 'Manage Battle',
                'Teleport', 'Easy Party Switcher', 'Save', 'Load',
                'Return to DEBUG ROOM', 'Exit']
    @continue = (1..SAVE_FILES_NUMBER).any? {|i|
        FileTest.exist?("#{SAVE_NAME}#{i}.#{SAVE_EXTENSION}")}
    make_debug_window
    @help_window = Window_Help.new
    @help_window.width = 400
    @help_window.contents.dispose
    @help_window.contents = Bitmap.new(368, 32)
    @help_window.set_text('Debug Main Menu', 1)
    @help_window.z, @help_window.back_opacity = 10000, 224
    @info_window = Window_DebugInfo.new
    @info_window.set_mode(-1)
    @list = true
    Graphics.transition
    loop do
      Graphics.update
      Input.update
      if PREVENT_CRASH
        begin
          update
        rescue
          if SHOW_ERROR
            p 'Error detected! Set the value back.'
            p "Original Error Message:  #{$!}"
          end
        end
      else
        update
      end
      break if @abort
    end
    Graphics.freeze
    [@debug_window, @control_window, @battler_window, @help_window,
        @info_window].each {|win| win.dispose if win != nil}
    $battle = nil if $battle == 0
    $scene.transfer_player if $game_temp.transition_processing
  end
  
  def make_debug_window
    @debug_window = Window_DebugList.new([7] + @extra, @commands)
    @debug_window.disable_item(5) unless $game_temp.in_battle
    @debug_window.disable_item(7) unless $easy_party_switcher
    @debug_window.disable_item(9) unless @continue
    @debug_window.disable_item(10) if DEBUG_ROOM_ID == 0
    @debug_window.index = @mem_index[0]
  end
  
  def remove_debug_window
    @extra = [@debug_window.swi, @debug_window.var]
    @info_window.set_mode(@debug_window.index)
    @help_window.set_text(@commands[@debug_window.index], 1)
    @mem_index[0] = @debug_window.index
    @debug_window.dispose
    @debug_window = nil
  end
        
  def update
    if @hash_window != nil
      @hash_window.update
      if Input.trigger?(Input::B)
        $game_system.se_play($data_system.cancel_se)
        @control_window = Window_DebugList.new(@mem_index[0], @status_window)
        @control_window.index = @mem_index[1]
        @control_window.update(-1)
        @info_window.set_mode(@mem_index[0])
        @help_window.set_text(@commands[@mem_index[0]], 1)
        @hash_window.dispose
        @hash_window = nil
      end
    elsif @array_window != nil
      @array_window.update
      if Input.trigger?(Input::B)
        $game_system.se_play($data_system.cancel_se)
        @battler_window = Window_DebugBattler.new(@array_window.battler,
            @status_window)
        @battler_window.index = @mem_index[2]
        @help_window.set_text(@array_window.battler.name, 1)
        @info_window.set_mode(-2)
        @status_window.visible = true
        @array_window.dispose
        @array_window = nil
        @status_window.refresh(@battler_window.battler)
      end
    elsif @battler_window != nil
      @battler_window.update
      if Input.trigger?(Input::B)
        $game_system.se_play($data_system.cancel_se)
        @control_window = Window_DebugList.new(@mem_index[0], @status_window)
        @control_window.index = @mem_index[1]
        @control_window.update(-1)
        @info_window.set_mode(@mem_index[0])
        @help_window.set_text(@commands[@mem_index[0]], 1)
        @battler_window.dispose
        @battler_window = nil
      elsif Input.trigger?(Input::C)
        case @battler_window.special?
        when 0 then ary = [$data_skills, ' - Skills']
        when 1 then ary = [$data_states, ' - States']
        end
        if ary != nil
          $game_system.se_play($data_system.decision_se)
          @array_window = Window_DebugArray.new(@battler_window.battler, ary[0])
          @mem_index[2] = @battler_window.index
          @status_window.visible = false
          @help_window.set_text(@battler_window.battler.name + ary[1], 1)
          @info_window.set_mode(8)
          @battler_window.dispose
          @battler_window = nil
        end
      end
    elsif @control_window != nil
      @control_window.update
      if Input.trigger?(Input::C) && @mem_index[0] == 6
        $game_system.se_play($data_system.decision_se)
        @abort = true
        $game_temp.player_new_map_id = @control_window.map[0]
        $game_temp.player_transferring = true
        $game_temp.transition_processing = true
        if TELEPORT_POSITION
          $game_temp.player_new_x = @control_window.map[1]
          $game_temp.player_new_y = @control_window.map[2]
        else
          map = load_data(sprintf('Data/Map%03d.rxdata', @control_window.map[0]))
          $game_temp.player_new_x = map.width/2
          $game_temp.player_new_y = map.height/2
        end
        $scene = Scene_Map.new unless $scene.is_a?(Scene_Map)
      elsif Input.trigger?(Input::C) && @mem_index[0] == 2
        case @control_window.special?
        when 1 then ary = [$data_items, 'Party - Items']
        when 2 then ary = [$data_weapons, 'Party - Weapons']
        when 3 then ary = [$data_armors, 'Party - Armors']
        end
        if ary != nil
          $game_system.se_play($data_system.decision_se)
          @hash_window = Window_DebugParty.new(ary[0])
          @mem_index[1] = @control_window.index
          @help_window.set_text(ary[1], 1)
          @info_window.set_mode(7)
          @control_window.dispose
          @control_window = nil
        end
      elsif Input.trigger?(Input::C) && @control_window.battler != nil
        @battler_window = Window_DebugBattler.new(@control_window.battler,
            @status_window)
        @battler_window.update(-1)
        @mem_index[1] = @control_window.index
        @help_window.set_text(@control_window.battler.name, 1)
        @info_window.set_mode(-2)
        @control_window.dispose
        @control_window = nil
      elsif Input.trigger?(Input::B)
        $game_system.se_play($data_system.cancel_se)
        @control_window.dispose
        @control_window = nil
        if @status_window != nil
          @status_window.dispose
          @status_window = nil
        end
        @help_window.set_text('Debug Main Menu', 1)
        @info_window.set_mode(-1)
        make_debug_window
      end
    else
      @debug_window.update
      if Input.trigger?(Input::B) || Input.trigger?(Input::C) && @debug_window.index == 11
        $game_system.se_play($data_system.cancel_se)
        @abort = true
      elsif Input.trigger?(Input::C)
        case @debug_window.index
        when 0..1
          $game_system.se_play($data_system.decision_se)
          @extra = [@debug_window.swi, @debug_window.var]
          @control_window = Window_DebugList.new(@debug_window.index, @extra)
          remove_debug_window
        when 2, 3, 6
          $game_system.se_play($data_system.decision_se)
          @control_window = Window_DebugList.new(@debug_window.index)
          remove_debug_window
        when 4
          $game_system.se_play($data_system.decision_se)
          @status_window = Window_DebugStatus.new
          @control_window = Window_DebugList.new(@debug_window.index, @status_window)
          remove_debug_window
        when 5
          if $game_temp.in_battle
            $game_system.se_play($data_system.decision_se)
            @status_window = Window_DebugStatus.new
            @control_window = Window_DebugList.new(@debug_window.index, @status_window)
            remove_debug_window
          else
            $game_system.se_play($data_system.buzzer_se)
          end
        when 7
          if $easy_party_switcher
            $game_system.se_play($data_system.decision_se)
            @abort = true
            $scene = Scene_PartySwitcher.new(10)
          else
            $game_system.se_play($data_system.buzzer_se)
          end
        when 8
          $game_system.se_play($data_system.decision_se)
          $game_temp.save_calling = true
          @abort = true
          $scene = Scene_Save.new
        when 9
          if @continue
            $game_system.se_play($data_system.decision_se)
            @abort = true
            $scene = Scene_Load.new
          else
            $game_system.se_play($data_system.buzzer_se)
          end
        when 10
          if DEBUG_ROOM_ID != 0
            $game_system.se_play($data_system.decision_se)
            @abort = true
            map = load_data(sprintf('Data/Map%03d.rxdata', DEBUG_ROOM_ID))
            $game_temp.player_new_map_id = DEBUG_ROOM_ID
            $game_temp.player_new_x = map.width/2
            $game_temp.player_new_y = map.height/2
            $game_temp.player_transferring = true
            $game_temp.transition_processing = true
            $scene = Scene_Map.new unless $scene.is_a?(Scene_Map)
          else
            $game_system.se_play($data_system.buzzer_se)
          end
        end
      end
    end
  end
  
end
