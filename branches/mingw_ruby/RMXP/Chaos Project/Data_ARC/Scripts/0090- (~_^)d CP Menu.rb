#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=
# StormTronics Hybrid by Blizzard
# Version: 6.4b - Hybrid Edition DX
# Type: Enhanced Custom Menu System
# Scene_Menu with complete menu control
#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=

INSIDE_DARK, INSIDE, OUTSIDE = 32, 29, 28

#==============================================================================
# module RPG
# module Cache
#==============================================================================

module RPG::Cache
  
  def self.custom_back(add)
    self.load_bitmap('', "custom_#{add}")
  end
  
end

#==============================================================================
# Scene_Menu
#==============================================================================

ADD_SKINS = ['MaxRed']
LIGHT_MODES = [0]
ONE_PIC_MODES = []
MODES = ['Metal-Plate', 'Classic']

class Scene_Menu
  
  attr_reader :windowskin
  
  def initialize(menu_index = 0, actor_index = 0, equip_index = 0)
    @menu_index, @actor_index, @equip_index = menu_index, actor_index, equip_index
    @viewport1 = Viewport.new(0, 0, 640, 480)
    test_ex_mode
  end
  
  def test_ex_mode
    tmp = $game_system.ex_mode
    i = 0
    loop do
      if $game_system.test_custom(i+1)
        i += 1
      else
        $game_system.ex_mode = i
        break
      end
    end
    if tmp > $game_system.ex_mode
      $game_system.menu_mode = 0
      $game_system.black_back = false
      return false
    end
    return true
  end

  def main
    @actor = $game_party.actors[@actor_index]
    @background = Plane.new
    @background.bitmap = RPG::Cache.picture('background')
    @windowskin = $game_system.windowskin_name.clone
    if $game_system.menu_mode != MODES.size - 1
      if $game_system.menu_mode >= MODES.size
        if $game_system.black_back
          $game_system.windowskin_name = 'MaxRed'
        else
          $game_system.windowskin_name = 'GameOver'
        end
      else
        $game_system.windowskin_name = ADD_SKINS[$game_system.menu_mode]
        $game_system.black_back = LIGHT_MODES.include?($game_system.menu_mode)
      end
    end
    continue = (CP::Cache::SaveGames.any? {|i| FileTest.exist?(CP.saves + "Chaos#{i+1}.cps")})
    @command_window = Window_HybridCommand.new(@menu_index, continue)
    (0..4).each {|i| @command_window.disable_item(i)} if $game_party.actors.size == 0
    if $game_switches[TELEPORT_Lock] || $game_variables[CITY] == 0 ||
        $game_temp.event_menu
      @command_window.disable_item(6)
    end
    @command_window.disable_item(7) if !@command_window.continue
    @info_window = Window_HybridInfo.new
    @status_windows = []
    (0...$game_party.actors.size).each {|i|
        @status_windows.push(Window_HybridMenuStatus.new($game_party.actors[i], i))}
    @help_window = Window_Help.new
    @help_window.active = false
    @help_window.x, @help_window.y, @help_window.z = 0, -368, 2999
    @info = Info_Sprite.new
    Graphics.transition
    loop do
      Graphics.update
      Input.update
      update
      break if @scene != nil
    end
    @info.dispose
    loop do
      Graphics.update
      ([@command_window, @info_window] + @status_windows).each {|win| win.update}
      @background.ox += 1
      @background.oy -= 1
      move_da_outro
      break if @status_windows[0].x <= -512
    end
    Graphics.freeze
    $game_map.refresh
    (@status_windows + [@background, @command_window, @info_window, @help_window,
    @sort_window, @playerstatus_window, @left_window, @skill_window,
    @target_window, @end_window, @item_choose_window, @rage_window,
    @ragestatus_window, @help_window2, @options_window,
    @teleport_window]).each {|obj| obj.dispose if obj != nil}
    $game_system.windowskin_name = @windowskin
    if @scene.is_a?(Scene_Title) || @scene == false
      Graphics.transition(25)
      Graphics.freeze
    else
      Graphics.transition
      Graphics.freeze
    end
    $game_temp.event_menu = nil
    $scene = @scene
  end
  
  def update
    @background.ox += 1
    @background.oy -= 1
    $game_system.update
    @info.update
    @info_window.update
    @help_window.update
    move_da_main if @status_windows[@status_windows.size-1].x < 0
    move_da_status if @playerstatus_window != nil && @playerstatus_window.y > 0
    move_da_equip if @left_window != nil && @left_window.x > 0
    move_da_skill if @skill_window != nil && @skill_window.x < 256
    move_da_target if @target_window != nil && @target_window.x < 0
    move_da_items if @item_choose_window != nil && @item_choose_window.y < 0
    move_da_sort if @sort_window != nil && @sort_window.y < 64
    move_da_rage if @rage_window != nil && @rage_window.y < 224
    move_da_options if @options_window != nil && @options_window.y > 0
    move_da_explain if @window != nil && @window.y > 0
    move_da_teleport if @teleport_window != nil && @teleport_window.x > 460
    move_da_end if @end_window != nil && @end_window.y > 320
    if @moved
      @moved = false
    elsif @rage_window != nil
      @rage_window.update
      update_rage
    elsif @command_window.active
      @command_window.update
      @status_windows.each {|win|
          win.index = ((win.active && @actor_index == win.actor.index) ? 0 : -1)
          win.update}
      @info.index = @command_window.index
      update_command
    elsif @status_windows[0].active
      @status_windows.each {|win|
          win.index = ((win.active && @actor_index == win.actor.index) ? 0 : -1)
          win.update}
      update_status
    elsif @item_choose_window != nil
      items_refresh
      if @item_choose_window.active
        @item_choose_window.update
        @info.index = @item_choose_window.index
        update_items_choose
      elsif @sort_window != nil && @sort_window.active
        @sort_window.update
        @info.index = @sort_window.index
        update_sort
      elsif @items_window1 != nil && @items_window1.active ||
            @items_window2 != nil && @items_window2.active ||
            @items_window3 != nil && @items_window3.active
        [@items_window1, @items_window2, @items_window3].each {|win| win.update}
        update_item
      elsif @target_window != nil && @target_window.active
        @target_window.update
        update_item_target 
      end
    elsif @skill_window != nil && @skill_window.active
      @skill_window.update
      update_skill
    elsif @target_window != nil && @target_window.active
      @target_window.update
      update_skill_target
    elsif @right_window != nil
      @left_window.update
      if @right_window.active
        @right_window.update
        update_right_equip
      elsif @item_window != nil && @item_window.active
        @item_window.update
        update_eitem
      end
    elsif @playerstatus_window != nil && @playerstatus_window.active
      @playerstatus_window.update
      @info.index = @playerstatus_window.index
      update_playerstatus
    elsif @options_window != nil && @options_window.active
      if @window != nil
        update_explain
      else
        @options_window.update
        @info.index = @options_window.index
        update_options
      end
    elsif @teleport_window != nil && @teleport_window.active
      @teleport_window.update
      update_teleport
    elsif @end_window != nil
      @end_window.update
      @info.index = @end_window.index
      update_end
    end
  end
  
  def equip_refresh
    if @item_window.active
      item = @item_window.data
      last_hp, last_sp = @actor.hp, @actor.sp
      @left_window.current = [@actor.maxhp, @actor.maxsp, @actor.atk,
          @actor.pdef, @actor.mdef, @actor.str, @actor.dex, @actor.agi,
          @actor.int, @actor.eva]
      @left_window.changed = @actor.test_equip(@right_window.index, item == nil ? 0 : item.id)
      @actor.hp, @actor.sp = last_hp, last_sp
    else
      item = @right_window.data
      @left_window.current = @left_window.changed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    end
    elements = (item.is_a?(RPG::Weapon) ? item.element_set :
        (item.is_a?(RPG::Armor) ? item.guard_element_set : []))
    states = (item.is_a?(RPG::Weapon) ? item.plus_state_set :
        (item.is_a?(RPG::Armor) ? item.guard_state_set : []))
    @left_window.set_new_parameters(elements, states)
    @left_window.refresh
  end
  
  def element_states_refresh
    item = @right_window.data
    elements = (item.is_a?(RPG::Weapon) ? item.element_set :
        (item.is_a?(RPG::Armor) ? item.guard_element_set : []))
    states = (item.is_a?(RPG::Weapon) ? item.plus_state_set :
        (item.is_a?(RPG::Armor) ? item.guard_state_set : []))
    @left_window.set_new_parameters(elements, states)
    @left_window.element_states_refresh
  end
  
  def move_windows(wins, border, mdiff, lead, xy, acc = false)
    if acc
      diff = ((xy ? lead.x : lead.y)-border).abs
    else
      diff = ((xy ? lead.x : lead.y)-border).abs / 2
    end
    if diff < 1
      diff = 1
    elsif diff > mdiff
      diff = mdiff
    end
    wins[0].each {|win| win.x += diff if win != nil}
    wins[1].each {|win| win.x -= diff if win != nil}
    wins[2].each {|win| win.y += diff if win != nil}
    wins[3].each {|win| win.y -= diff if win != nil}
    @moved = true
  end
  
  def move_da_main
    if @status_windows[@status_windows.size-1].x < 0
      if @status_windows[0].x < 0
        lead = @status_windows[0]
        x_plus = [@status_windows[0]]
        x_minus = [@command_window]
        y_minus = [@info_window]
        move_windows([x_plus, x_minus, [], y_minus], 0, 128, lead, true)
      end
      (1...@status_windows.size).each {|i|
          if @status_windows[i].x < 0
            lead = @status_windows[i]
            x_plus = [@status_windows[i]]
            move_windows([x_plus, [], [], []], 0, 128, lead, true)
          end}
    end
  end
  
  def move_da_outro
    lead = @status_windows[0]
    x_plus = [@command_window, @teleport_window]
    x_minus = @status_windows + [@target_window, @skill_window, @help_window]
    y_plus = [@info_window]
    y_minus = [@item_choose_window, @items_window1, @items_window3,
        @items_window2, @help_window]
    move_windows([x_plus, x_minus, y_plus, y_minus], 0, 128, lead, true, true)
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
  
  def move_da_target(win = @target_window)
    move_windows([[@target_window], [], [], []], 0, 32, win, true)
  end
  
  def move_da_items(win = @item_choose_window)
    y_plus = [@item_choose_window, @items_window1, @items_window2,
        @items_window3, @help_window]
    move_windows([[], [], y_plus, []], 0, 64, win, false)
  end
  
  def move_da_rage(win = @rage_window)
    y_plus = [@rage_window, @help_window, @help_window2, @ragestatus_window]
    move_windows([[], [], y_plus, []], 224, 64, win, false)
  end
  
  def move_da_options(win = @options_window)
    move_windows([[], [], [], [win]], 0, 64, win, false)
  end
  
  def move_da_end(win = @end_window)
    move_windows([[], [], [], [win]], 320, 32, win, false)
  end
  
  def move_da_explain(win = @window)
    move_windows([[], [], [], [win, @helpinfo_window]], 0, 64, win, false)
  end
  
  def move_da_teleport(win = @teleport_window)
    move_windows([[], [win], [], []], 460, 64, win, true)
  end  
  
  def update_command
    if Input.trigger?($controls.cancel)
      $game_system.se_play($data_system.cancel_se)
      @scene = Scene_Map.new
    elsif Input.trigger?($controls.confirm)
      if $game_party.actors.size == 0 && @command_window.index < 4
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      case @command_window.index
      when 0
        @info.set(1, 0)
        @item_choose_window = Window_HybridChooseItem.new
        @items_window1 = Window_NormalItem.new
        @items_window2 = Window_EquipmentItem.new
        @items_window3 = Window_QuestItem.new
        @items_window1.help_window = @items_window2.help_window =
            @items_window3.help_window = @help_window
        $game_system.se_play($data_system.decision_se)
        @command_window.active = false
        @item_choose_window.active = true
        @help_window.x = 0
        @help_window.y = -576
        @help_window.set_text('')
        @items_window1.visible = @items_window2.visible =
            @items_window3.visible = true
        @help_window.visible = false
        @help_window.update
        items_refresh
      when 1..4
        @info.set(-1, 0)
        $game_system.se_play($data_system.decision_se)
        @command_window.active = false
        @status_windows.each {|win| win.active = true}
        @actor_index = 0
      when 5
        @info.set(6, 0)
        @options_window = Window_HybridOptions.new
        $game_system.se_play($data_system.decision_se)
        @command_window.active = false
        @options_window.index = 0
      when 6
        if $game_switches[TELEPORT_Lock] || $game_variables[CITY] == 0 ||
            $game_temp.event_menu
          $game_system.se_play($data_system.buzzer_se)
          return
        end
        @info.set(-1, 0)
        @teleport_window = Window_HybridTeleport.new
        $game_system.se_play($data_system.decision_se)
        @command_window.active = false
        @teleport_window.index = 0
      when 7
        @info.set(8, 0)
        if @command_window.continue
          $game_system.se_play($data_system.decision_se)
          @scene = Scene_NewLoad.new
          Graphics.transition(0)
        else
          $game_system.se_play($data_system.buzzer_se)
        end
      when 8
        @info.set(9, 0)
        $game_system.se_play($data_system.decision_se)
        @command_window.active = false
        @end_window = Window_HybridEndCommand.new
      end
    end
  end
  
  def update_status
    @actor = $game_party.actors[@actor_index]
    if Input.trigger?($controls.cancel)
      @info.set(0, @command_window.index)
      $game_system.se_play($data_system.cancel_se)
      @status_windows.each {|win| win.active = false}
      @command_window.active = true
      @actor_index = -1
    elsif Input.trigger?($controls.confirm)
      case @command_window.index
      when 1
        @left_window = Window_HybridEquipLeft.new(@actor)
        @right_window = Window_HybridEquipRight.new(@actor)
        @right_window.help_window = @help_window
        @item_windows = []
        (0..4).each {|i| win = Window_HybridEquipItem.new(@actor, 4-i)
            win.help_window = @help_window
            @item_windows.unshift(win)}
        @item_window = @item_windows[0]
        @item_window.visible = true
        $game_system.se_play($data_system.decision_se)
        @help_window.y = 0
        @help_window.x = 640
        @status_windows.each {|win| win.active = false}
        @help_window.update
        @info.rage_window = @right_window
        equip_refresh
        @info.set(12, 0)
      when 2
        if @actor.restriction >= 2
          $game_system.se_play($data_system.buzzer_se)
          return
        end
        @skill_window = Window_HybridSkill.new(@actor)
        @skill_window.help_window = @help_window
        $game_system.se_play($data_system.decision_se)
        @help_window.active = true
        @help_window.y = 0
        @help_window.x = -768
        @status_windows.each {|win| win.active = false}
        @help_window.update
      when 3
        @help_window2 = Window_Help.new(true, 64)
        @rage_window = Window_HybridSoulRage.new(@actor, @help_window2)
        @rage_window.help_window = @help_window
        @ragestatus_window = Window_HybridRageStatus.new(@actor)
        $game_system.se_play($data_system.decision_se)
        @status_windows.each {|win| win.active = false}
        @help_window.active = true
        @help_window.x = 0
        @help_window.y = -512
        @help_window2.active = true
        @help_window2.x = 0
        @help_window2.y = -448
        @help_window2.z = 2999
        @rage_window.visible = @rage_window.active = true
        @help_window.update
        @help_window2.update
      when 4
        @info.set(5, 0)
        @actor = $game_party.actors[@actor_index]
        $game_system.se_play($data_system.decision_se)
        @playerstatus_window = Window_HybridStatus.new(@actor)
        @playerstatus_window.active = true
        @playerstatus_window.x = 0
        @status_windows.each {|win| win.active = false}
        @help_window.update
      end
    elsif Input.trigger?($controls.down)
      $game_system.se_play($data_system.cursor_se)
      @status_windows[@actor_index].index = -1
      @actor_index = (@actor_index+1) % $game_party.actors.size
      @status_windows[@actor_index].index = 0
    elsif Input.trigger?($controls.up)
      $game_system.se_play($data_system.cursor_se)
      @status_windows[@actor_index].index = -1
      @actor_index = (@actor_index+$game_party.actors.size-1) % $game_party.actors.size
      @status_windows[@actor_index].index = 0
    end
  end
  
  def update_items_choose
    if Input.trigger?($controls.cancel)
      @info.set(0, 0)
      @item_choose_window.dispose
      @items_window1.dispose
      @items_window2.dispose
      @items_window3.dispose
      @item_choose_window = @items_window1 = @items_window2 = @items_window3 = nil
      $game_system.se_play($data_system.cancel_se)
      @help_window.x, @help_window.y = 0, -612
      @help_window.visible = @command_window.active = true
    elsif Input.trigger?($controls.confirm)
      items_refresh
      case @item_choose_window.index
      when 0
        @info.set(-1, 0)
        $game_system.se_play($data_system.decision_se)
        @item_choose_window.active = @item_choose_window.visible = false
        @items_window1.active = @help_window.active = @help_window.visible = true
        @help_window.update
        @items_window1.index = 0
      when 1
        @info.set(11, 0)
        @sort_window = Window_HybridSortCommand.new
        $game_system.se_play($data_system.decision_se)
        @sort_window.active = true
        @item_choose_window.active = false
      when 2
        $game_system.se_play($data_system.decision_se)
        @item_choose_window.active = @item_choose_window.visible = false
        @items_window2.active = @help_window.active = @help_window.visible = true
        @info.rage_window = @items_window2
        @help_window.update
        @items_window2.index = 0
        @info.set(12, 0)
      when 3
        @info.set(-1, 0)
        $game_system.se_play($data_system.decision_se)
        @item_choose_window.active = @item_choose_window.visible = false
        @items_window3.active = @help_window.active = @help_window.visible = true
        @help_window.update
        @items_window3.index = 0
      end
    end
  end
  
  def update_sort
    if Input.trigger?($controls.cancel)
      @info.set(1, 1)
      @sort_window.dispose
      @sort_window = @info.rage_window = nil
      @item_choose_window.active = true
      $game_system.se_play($data_system.cancel_se)
    elsif Input.trigger?($controls.confirm)
      $game_system.se_play($data_system.decision_se)
      temp = @sort_window.index * @sort_window.index
      @items_window1.mode = @items_window2.mode = case @sort_window.index
      when 0 then 0
      when 1 then (@items_window1.mode == 1 ? 2 : 1)
      when 2 then (@items_window1.mode == 3 ? 4 : 3)
      end
      @items_window1.refresh
      @items_window2.refresh
    end
  end
  
  def items_refresh
    index = @item_choose_window.index
    @items_window1.visible = (index == 0 || index == 1)
    @items_window2.visible = (index == 2)
    @items_window3.visible = (index == 3)
  end
    
  def update_rage
    if Input.trigger?($controls.cancel)
      @info.set(0, 1)
      @rage_window.dispose
      @ragestatus_window.dispose
      @help_window2.dispose
      @rage_window = @ragestatus_window = @help_window2 = nil
      $game_system.se_play($data_system.cancel_se)
      @status_windows.each {|win| win.index = -1; win.update; win.active = false}
      @actor_index = -1
      @command_window.active, @help_window.active = true, false
      @help_window.x, @help_window.y = 0, -612
    elsif Input.trigger?($controls.right)
      $game_system.se_play($data_system.cursor_se)
      @status_windows[@actor_index].index = -1
      @actor_index = (@actor_index+1) % $game_party.actors.size
      @status_windows[@actor_index].index = 0
      @rage_window.update_actor($game_party.actors[@actor_index])
      @ragestatus_window.update_actor($game_party.actors[@actor_index])
    elsif Input.trigger?($controls.left)
      $game_system.se_play($data_system.cursor_se)
      @status_windows[@actor_index].index = -1
      @actor_index = (@actor_index+$game_party.actors.size-1) % $game_party.actors.size
      @status_windows[@actor_index].index = 0
      @rage_window.update_actor($game_party.actors[@actor_index])
      @ragestatus_window.update_actor($game_party.actors[@actor_index])
    end
  end
  
  def update_item
    if Input.trigger?($controls.cancel)
      @info.set(1, @item_choose_window.index)
      $game_system.se_play($data_system.cancel_se)
      @item_choose_window.active = @item_choose_window.visible = true
      @help_window.set_text('')
      @items_window1.active = @items_window2.active = @items_window3.active =
          @help_window.active = @help_window.visible = false
      @items_window1.index = @items_window2.index = @items_window3.index = -1
      @info.rage_window = nil
    elsif Input.trigger?($controls.confirm)
      if @item_choose_window.index == 0
        @item = @items_window1.data
        if !@item.is_a?(RPG::Item) || !$game_party.item_can_use?(@item.id)
          $game_system.se_play($data_system.buzzer_se)
          return
        end
      elsif @item_choose_window.index == 2
        return
      elsif @item_choose_window.index == 3
        @item = @items_window3.data
        if !@item.is_a?(RPG::Item) || !$game_party.item_can_use?(@item.id)
          $game_system.se_play($data_system.buzzer_se)
          return
        end
      end
      @target_window = Window_HybridTarget.new($game_party.actors[0])
      $game_system.se_play($data_system.decision_se)
      if @item.scope >= 3
        @items_window1.active = false
        @target_window.visible = @target_window.active = true
        @target_window.index = ((@item.scope == 4 || @item.scope == 6) ? -1 : 0)
      elsif @item.common_event_id > 0
        $game_temp.common_event_id = @item.common_event_id
        $game_system.se_play(@item.menu_se)
        if @item.consumable
          $game_party.lose_item(@item.id, 1)
          @items_window1.draw_item(@items_window1.index)
        end
        @scene = Scene_Map.new
      end
    elsif Input.repeat?($controls.up) || Input.repeat?($controls.down)
      @info.refresh
    end
  end
  
  def update_item_target
    if Input.trigger?($controls.cancel)
      @target_window.dispose
      @target_window = nil
      $game_system.se_play($data_system.cancel_se)
      @items_window1.refresh unless $game_party.item_can_use?(@item.id)
      @items_window1.active = true
    elsif Input.trigger?($controls.confirm)
      if $game_party.item_number(@item.id) == 0
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      if @target_window.index == -1
        used = false
        $game_party.actors.each {|actor| used |= actor.item_effect(@item)}
      elsif @target_window.index >= 0
        other_target = $game_party.actors[@target_window.index]
        used = other_target.item_effect(@item)
      end
      if used
        $game_system.se_play(@item.menu_se)
        if @item.consumable
          $game_party.lose_item(@item.id, 1)
          @items_window1.draw_item(@items_window1.index)
        end
        @target_window.refresh
        @status_windows.each {|win| win.refresh}
        if $game_party.all_dead?
          @scene = Scene_Gameover.new
        elsif @item.common_event_id > 0
          $game_temp.common_event_id = @item.common_event_id
          @scene = Scene_Map.new
        end
      else
        $game_system.se_play($data_system.buzzer_se)
      end
    end
  end

  def update_skill
    if Input.trigger?($controls.cancel)
      @info.set(0, 2)
      @skill_window.dispose
      @skill_window = nil
      $game_system.se_play($data_system.cancel_se)
      @help_window.active, @help_window.x, @help_window.y = false, 0, -768
      @status_windows.each {|win| win.index = -1; win.update; win.active = false}
      @command_window.active = true
      @actor_index = -1
    elsif Input.trigger?($controls.confirm)
      @skill = @skill_window.data
      if @skill == nil || !@actor.skill_can_use?(@skill.id)
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      @target_window = Window_HybridTarget.new($game_party.actors[0])
      $game_system.se_play($data_system.decision_se)
      if @skill.scope >= 3
        @skill_window.active = false
        @target_window.visible = @target_window.active = true
        @target_window.index = ((@skill.scope == 4 || @skill.scope == 6) ? -1 : 0)
      elsif @skill.common_event_id > 0
        $game_temp.common_event_id = @skill.common_event_id
        $game_system.se_play(@skill.menu_se)
        @actor.sp -= (@skill.sp_cost/(@actor.states.include?(31) ? 2.0 : 1)).ceil
        @status_windows.each {|win| win.refresh}
        @skill_window.refresh
        @target_window.refresh
        @scene = Scene_Map.new
      end
    elsif Input.trigger?($controls.right)
      $game_system.se_play($data_system.cursor_se)
      @status_windows[@actor_index].index = -1
      @actor_index = (@actor_index+1) % $game_party.actors.size
      @status_windows[@actor_index].index = 0
      @actor = $game_party.actors[@actor_index]
      @skill_window.update_actor(@actor)
      @skill_window.index = 0
    elsif Input.trigger?($controls.left)
      $game_system.se_play($data_system.cursor_se)
      @status_windows[@actor_index].index = -1
      @actor_index = (@actor_index+$game_party.actors.size-1) % $game_party.actors.size
      @status_windows[@actor_index].index = 0
      @actor = $game_party.actors[@actor_index]
      @skill_window.update_actor(@actor)
      @skill_window.index = 0
    end
  end
  
  def update_skill_target
    if Input.trigger?($controls.cancel)
      @target_window.dispose
      @target_window = nil
      $game_system.se_play($data_system.cancel_se)
      @skill_window.active = true
    elsif Input.trigger?($controls.confirm)
      if !@actor.skill_can_use?(@skill.id)
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      if @target_window.index == -1
        used = false
        $game_party.actors.each {|actor| used |= actor.skill_effect(@actor, @skill)}
      else
        other_target = $game_party.actors[@target_window.index]
        used = other_target.skill_effect(@actor, @skill)
      end
      if used
        $game_system.se_play(@skill.menu_se)
        if @actor.states.include?(31)
          @actor.sp -= (@skill.sp_cost / 2.0).ceil
        else
          @actor.sp -= @skill.sp_cost
        end
        @target_window.refresh
        @status_windows.each {|win| win.refresh}
        @skill_window.refresh
        @target_window.refresh
        if $game_party.all_dead?
          @scene = Scene_Gameover.new
        elsif @skill.common_event_id > 0
          $game_temp.common_event_id = @skill.common_event_id
          @scene = Scene_Map.new
        end
      else
        $game_system.se_play($data_system.buzzer_se)
      end
    end
  end
  
  def update_right_equip
    update_equipitem_visibility
    if Input.trigger?($controls.cancel)
      @info.set(0, 3)
      ([@left_window, @right_window] + @item_windows).each {|win| win.dispose}
      @left_window = @right_window = @item_window = @item_windows =
          @info.rage_window = nil
      $game_system.se_play($data_system.cancel_se)
      @help_window.active, @help_window.x, @help_window.y = false, 660, 0
      @status_windows.each {|win| win.index = -1; win.update; win.active = false}
      @command_window.active = true
      @actor_index = -1
    elsif Input.trigger?($controls.confirm)
      if @actor.equip_fix?(@right_window.index)
        $game_system.se_play($data_system.buzzer_se)
      else
        $game_system.se_play($data_system.decision_se)
        @right_window.active = false
        @item_window.active = true
        @item_window.index = 0
        @info.rage_window = @item_window
        equip_refresh
        @info.refresh
      end
    elsif Input.trigger?($controls.right)
      $game_system.se_play($data_system.cursor_se)
      @status_windows[@actor_index].index = -1
      @actor_index = (@actor_index+1) % $game_party.actors.size
      @status_windows[@actor_index].index = 0
      @actor = $game_party.actors[@actor_index]
      @right_window.update_actor(@actor)
      @left_window.update_actor(@actor)
      @item_windows.each {|win| win.update_actor(@actor)}
      equip_refresh
      update_equipitem_visibility
      @info.refresh
    elsif Input.trigger?($controls.left)
      $game_system.se_play($data_system.cursor_se)
      @status_windows[@actor_index].index = -1
      @actor_index = (@actor_index+$game_party.actors.size-1) % $game_party.actors.size
      @status_windows[@actor_index].index = 0
      @actor = $game_party.actors[@actor_index]
      @right_window.update_actor(@actor)
      @left_window.update_actor(@actor)
      @item_windows.each {|win| win.update_actor(@actor)}
      equip_refresh
      update_equipitem_visibility
      @info.refresh
    elsif Input.repeat?($controls.up) || Input.repeat?($controls.down)
      element_states_refresh
      @info.refresh
    end
  end

  def update_equipitem_visibility
    if CP::Cache::Lucius.include?(@right_window.actor.id)
      @item_windows[0].visible = (@right_window.index <= 1)
      @item_windows[1].visible = false
    else
      @item_windows[0].visible = (@right_window.index == 0)
      @item_windows[1].visible = (@right_window.index == 1)
    end
    @item_windows[2].visible = (@right_window.index == 2)
    @item_windows[3].visible = (@right_window.index == 3)
    @item_windows[4].visible = (@right_window.index >= 4)
    @item_windows.each {|win| @item_window = win if win.visible}
    newmode = @right_window.index
    newmode = 1 if newmode > 1
    if @right_window.index == 1 && CP::Cache::Lucius.include?(@right_window.actor.id)
      newmode = 0
    end
    if newmode != @left_window.mode
      @left_window.mode = newmode
      @left_window.element_states_refresh
    end
  end
  
  def update_eitem
    if Input.trigger?($controls.cancel)
      $game_system.se_play($data_system.cancel_se)
      @right_window.active = true
      @item_window.active = false
      @item_window.index = -1
      @info.rage_window = @right_window
      equip_refresh
      @info.refresh
    elsif Input.trigger?($controls.confirm)
      $game_system.se_play($data_system.equip_se)
      item = @item_window.data
      @actor.equip(@right_window.index, item == nil ? 0 : item.id)
      @right_window.active = true
      @item_window.active = false
      @item_window.index = -1
      @right_window.refresh
      @item_window.refresh
      @status_windows.each {|win| win.refresh}
      @info.rage_window = @right_window
      equip_refresh
      @info.refresh
    elsif Input.repeat?($controls.up) || Input.repeat?($controls.down) ||
        Input.repeat?($controls.prev) || Input.repeat?($controls.nex)
      equip_refresh
      @info.refresh
    end
  end
  
  def update_playerstatus
    if Input.trigger?($controls.cancel)
      @info.set(0, 4)
      $game_system.se_play($data_system.cancel_se)
      @playerstatus_window.active = false
      @playerstatus_window.y = 528
      @command_window.active = true
      @actor_index = -1
      @status_windows.each {|win| win.index = -1; win.update; win.active = false}
      @playerstatus_window.dispose
      @playerstatus_window = nil
    elsif Input.trigger?($controls.right)
      $game_system.se_play($data_system.cursor_se)
      @status_windows[@actor_index].index = -1
      @actor_index = (@actor_index+1) % $game_party.actors.size
      @status_windows[@actor_index].index = 0
      @actor = $game_party.actors[@actor_index]
      @playerstatus_window.update_actor(@actor)
    elsif Input.trigger?($controls.left)
      $game_system.se_play($data_system.cursor_se)
      @status_windows[@actor_index].index = -1
      @actor_index = (@actor_index+$game_party.actors.size-1) % $game_party.actors.size
      @status_windows[@actor_index].index = 0
      @actor = $game_party.actors[@actor_index]
      @playerstatus_window.update_actor(@actor)
    end
  end
  
  def update_options
    if Input.trigger?($controls.cancel)
      @info.set(0, 5)
      @options_window.dispose
      @options_window = nil
      $game_system.se_play($data_system.cancel_se)
      @command_window.active = true
      return
    end
    case @options_window.index
    when 0
      if Input.repeat?($controls.right)
        $game_system.bgm_volume += 5
        $game_system.bgm_volume = 100 if $game_system.bgm_volume > 100
        $game_system.bgm_play($game_system.bgm_memorize)
        @options_window.refresh(@options_window.index)
      elsif Input.repeat?($controls.left)
        $game_system.bgm_volume -= 5
        $game_system.bgm_volume = 0 if $game_system.bgm_volume < 0
        $game_system.bgm_play($game_system.bgm_memorize)
        @options_window.refresh(@options_window.index)
      end
    when 1
      if Input.repeat?($controls.right)
        $game_system.sfx_volume += 5
        if $game_system.sfx_volume > 100
          $game_system.sfx_volume = 100
        else
          $game_system.se_play($data_system.cursor_se)
        end
        $game_system.bgs_play($game_system.bgs_memorize)
        @options_window.refresh(@options_window.index)
      end
      if Input.repeat?($controls.left)
        $game_system.sfx_volume -= 5
        $game_system.sfx_volume = 0 if $game_system.sfx_volume < 0
        $game_system.se_play($data_system.cursor_se)
        $game_system.bgm_play($game_system.bgm_memorize)
        @options_window.refresh(@options_window.index)
      end
    when 2
      if Input.repeat?($controls.left) || Input.repeat?($controls.right) || Input.repeat?($controls.confirm)
        $game_system.se_play($data_system.decision_se)
        tmp, $game_system.black_back = $game_system.black_back, false
        if test_ex_mode
          if Input.repeat?($controls.right) || Input.repeat?($controls.confirm)
            $game_system.menu_mode += 1
            $game_system.menu_mode %= MODES.size + $game_system.ex_mode
          elsif Input.repeat?($controls.left)
            $game_system.menu_mode += MODES.size + $game_system.ex_mode - 1
            $game_system.menu_mode %= MODES.size + $game_system.ex_mode
          end
        end
        @command_window.cache_sprite
        @info_window.cache_sprite
        @status_windows.each {|win| win.cache_sprite}
        @help_window.cache_sprite
        @options_window.cache_sprite
        if $game_system.menu_mode == MODES.size - 1
          $game_system.windowskin_name = @windowskin
        else
          unless ['MaxRed', 'GameOver'].include?($game_system.windowskin_name)
            @windowskin = $game_system.windowskin_name
          end
          if $game_system.menu_mode >= MODES.size
            tmp2 = $game_system.black_back
            if $game_system.black_back
              $game_system.windowskin_name = 'MaxRed'
            else
              $game_system.windowskin_name = 'GameOver'
            end
          else
            $game_system.windowskin_name = ADD_SKINS[$game_system.menu_mode]
            $game_system.black_back = LIGHT_MODES.include?($game_system.menu_mode)
          end
        end
        @command_window.setup_skin
        @info_window.setup_skin
        @status_windows.each {|win|
            win.setup_skin
            win.index = ((win.active && @actor_index == win.actor.index) ? 0 : -1)
            win.update}
        @help_window.setup_skin
        @options_window.setup_skin
        if tmp != $game_system.black_back
          @command_window.refresh
          @info_window.refresh
          @status_windows.each {|win| win.refresh}
          @help_window.refresh
          @options_window.refresh
          if $game_switches[TELEPORT_Lock] || $game_variables[CITY] == 0
            @command_window.disable_item(6)
          end
          @command_window.disable_item(7) if !@command_window.continue
        else
          @options_window.refresh(@options_window.index)
        end
      end
    when 3
      if Input.repeat?($controls.left) || Input.repeat?($controls.right) || Input.repeat?($controls.confirm)
        if $game_switches[BGM_Lock] || $game_temp.event_menu
          $game_system.se_play($data_system.buzzer_se)
        else
          $game_system.se_play($data_system.decision_se)
          i = $game_system.bgm_list.index($game_variables[BGM])
          if Input.repeat?($controls.left)
            i = (i + $game_system.bgm_list.size - 1) % $game_system.bgm_list.size
          elsif Input.repeat?($controls.right) || Input.repeat?($controls.confirm)
            i = (i + 1) % $game_system.bgm_list.size
          end
          $game_variables[BGM] = $game_system.bgm_list[i]
          interpreter = Interpreter.new(0, false)
          interpreter.setup($data_common_events[13].list, 13)
          interpreter.setup_starting_event
          interpreter.update
          @options_window.refresh(@options_window.index)
        end
      end
    when 4
      if Input.repeat?($controls.left) || Input.repeat?($controls.right) || Input.repeat?($controls.confirm)
        $game_system.se_play($data_system.decision_se)
        $game_system.cam += 1
        $game_system.cam %= 2
        $game_system.get_cam
        @options_window.refresh(@options_window.index)
      end
    when 5
      if Input.repeat?($controls.right) || Input.repeat?($controls.confirm)
        $game_system.se_play($data_system.decision_se)
        $game_system.encounter_mode = ($game_system.encounter_mode + 1) % 3
        @options_window.refresh(@options_window.index)
      elsif Input.repeat?($controls.left)
        $game_system.se_play($data_system.decision_se)
        $game_system.encounter_mode = ($game_system.encounter_mode + 3 - 1) % 3
        @options_window.refresh(@options_window.index)
      end
    when 6
      if Input.repeat?($controls.left) || Input.repeat?($controls.right) || Input.repeat?($controls.confirm)
        $game_system.se_play($data_system.decision_se)
        $game_system.uf_mode = (!$game_system.uf_mode)
        @options_window.refresh(@options_window.index)
      end
    when 7
      if Input.repeat?($controls.left)
        if $game_system.bar_opacity == 0
          $game_system.se_play($data_system.buzzer_se)
        else
          $game_system.bar_style = ($game_system.bar_style + 6) % 7
          $game_system.se_play($data_system.decision_se)
          [0, 1, @options_window.index].each {|i| @options_window.refresh(i)}
          @status_windows.each {|win| win.refresh}
        end
      elsif Input.repeat?($controls.right)
        if $game_system.bar_opacity == 0
          $game_system.se_play($data_system.buzzer_se)
        else
          $game_system.bar_style = ($game_system.bar_style + 1) % 7
          $game_system.se_play($data_system.decision_se)
          [0, 1, @options_window.index].each {|i| @options_window.refresh(i)}
          @status_windows.each {|win| win.refresh}
        end
      end
    when 8
      if Input.repeat?($controls.left)
        $game_system.se_play($data_system.decision_se)
        $game_system.bar_opacity -= 64
        @options_window.refresh(@options_window.index)
        @options_window.refresh(@options_window.index-1)
        @status_windows.each {|win| win.refresh}
      elsif Input.repeat?($controls.right)
        $game_system.se_play($data_system.decision_se)
        $game_system.bar_opacity += 64
        @options_window.refresh(@options_window.index)
        @options_window.refresh(@options_window.index-1)
        @status_windows.each {|win| win.refresh}
      end
    when 9
      if Input.repeat?($controls.left)
        $game_system.se_play($data_system.cursor_se)
        @options_window.current_font += CP::Cache::Fonts.size-1
        @options_window.current_font %= CP::Cache::Fonts.size
        @options_window.refresh(@options_window.index)
      elsif Input.repeat?($controls.right)
        $game_system.se_play($data_system.cursor_se)
        @options_window.current_font += 1
        @options_window.current_font %= CP::Cache::Fonts.size
        @options_window.refresh(@options_window.index)
      elsif Input.repeat?($controls.confirm)
        $game_system.se_play($data_system.decision_se)
        $fontface = @options_window.font_name
        $fontsize = ($fontface == 'Papyrus' ? 30 : 24)
        ([@command_window, @info_window, @help_window, @options_window] +
            @status_windows).each {|win|
                win.contents.font.bold = ($fontface == 'Papyrus')}
        ([@info, @command_window, @info_window, @help_window, @options_window] + 
            @status_windows).each {|win| win.refresh}
        if $game_switches[TELEPORT_Lock] || $game_variables[CITY] == 0
          @command_window.disable_item(6)
        end
        @command_window.disable_item(7) if !@command_window.continue
      end
    when 10
      if Input.repeat?($controls.left)
        $game_system.se_play($data_system.cursor_se)
        @options_window.current_skin += CP::Cache::Skins.size - 1
        @options_window.current_skin %= CP::Cache::Skins.size
        if !$game_switches[200] &&
              @options_window.current_skin == CP::Cache::Skins.size-1
          @options_window.current_skin -= 1
        end
        @options_window.refresh(@options_window.index)
      elsif Input.repeat?($controls.right)
        $game_system.se_play($data_system.cursor_se)
        @options_window.current_skin += 1
        @options_window.current_skin %= CP::Cache::Skins.size
        if !$game_switches[200] &&
            @options_window.current_skin == CP::Cache::Skins.size-1
          @options_window.current_skin = 0
        end
        @options_window.refresh(@options_window.index)
      elsif Input.repeat?($controls.confirm)
        $game_system.se_play($data_system.decision_se)
        @windowskin = @options_window.skin_name
        if $game_system.menu_mode == MODES.size - 1
          $game_system.windowskin_name = @windowskin
        end
        ([@command_window, @info_window, @help_window, @options_window] + 
            @status_windows).each {|win| win.setup_skin}
      end
    when 11
      if Input.repeat?($controls.confirm)
        $game_system.se_play($data_system.decision_se)
        @window = Window_HybridExplain.new
        @helpinfo_window = Window_Help.new(false)
        @helpinfo_window.x, @helpinfo_window.y, @helpinfo_window.z = 0, 542, 24999
        @window.help_window = @helpinfo_window
        @helpinfo_window.opacity = 0
        @window.refresh
      end
    end
  end
  
  def update_explain
    if Input.trigger?($controls.cancel)
      $game_system.se_play($data_system.cancel_se)
      [@window, @helpinfo_window].each {|win| win.dispose}
      @window = @helpinfo_window = nil
    else
      @window.update
    end
  end
  
  def update_teleport
    if Input.trigger?($controls.cancel)
      @info.set(0, 6)
      @teleport_window.dispose
      @teleport_window = nil
      $game_system.se_play($data_system.cancel_se)
      @command_window.active = true
    elsif Input.trigger?($controls.confirm)
      if $game_party.item_number(139) == 0
        $game_party.actors.each {|actor|
            actor.hp = actor.hp/3 + 1 if actor.hp > 0
            actor.sp -= (actor.maxsp/2).ceil if actor.hp > 0}
      end
      if CP::Cache::SilenceMaps.include?($game_map.map_id)
        $game_party.actors.each {|actor| actor.remove_state(5)}
      elsif CP::Cache::HeatstrikeMaps.include?($game_map.map_id)
        $game_party.actors.each {|actor| actor.remove_state(51)}
        $game_party.actors.each {|actor| actor.remove_state(54)}
      end
      $game_temp.player_transferring = true
      Audio.bgm_stop
      $game_system.se_play(RPG::AudioFile.new('Teleporting', 80, 100))
      $game_temp.player_new_direction = 2
      $game_switches[INSIDE_DARK] = $game_switches[INSIDE] = false
      $game_switches[OUTSIDE] = true
      if $game_variables[PLANET] == 2
        if !$game_switches[379] && @teleport_window.index == 7
          data = [711, 0, 0]
        else
          if @teleport_window.index >= 7
            $game_ddns.turn_on
            $game_ddns.go_inside
          end
          data = CP::Cache::Teleports[@teleport_window.index + 9]
        end
      else
        data = CP::Cache::Teleports[@teleport_window.index]
      end
      $game_temp.player_new_map_id = data[0]
      $game_temp.player_new_x, $game_temp.player_new_y = data[1], data[2]
      $game_temp.transition_processing = true
      $game_temp.transition_name = ''
      $game_system.encounter_disabled = false
      @scene = Scene_Map.new
    end
  end
  
  def update_end
    if Input.trigger?($controls.cancel)
      @info.set(0, 8)
      @end_window.dispose
      @end_window = nil
      $game_system.se_play($data_system.cancel_se)
      @command_window.active = true
    elsif Input.trigger?($controls.confirm)
      case @end_window.index
      when 0 
        @info.set(0, 8)
        $game_system.se_play($data_system.cancel_se)
        @command_window.active = true
      when 1 
        Graphics.freeze
        $game_system.se_play($data_system.decision_se)
        Audio.bgm_fade(800)
        Audio.bgs_fade(800)
        Audio.me_fade(800)
        @scene = Scene_Title.new
      when 2 
        Graphics.freeze
        $game_system.se_play($data_system.decision_se)
        Audio.bgm_fade(800)
        Audio.bgs_fade(800)
        Audio.me_fade(800)
        @scene = false
      end
      @end_window.dispose
      @end_window = nil
    end
  end
  
end

#==============================================================================
# Scene_NewLoad
#==============================================================================

class Scene_NewLoad < Scene_File
  
  def initialize
    $game_temp.last_file_index = 0
    latest_time = Time.at(0)
    CP::Cache::SaveGames.each {|i|
        filename = make_filename(i)
        if FileTest.exist?(filename)
          file = File.open(filename, 'r')
          if file.mtime > latest_time
            latest_time = file.mtime
            $game_temp.last_file_index = i
          end
          file.close
        end}
    super('Which file do you wish to load from?')
  end

  def on_decision(file_index)
    filename = make_filename(file_index)
    unless FileTest.exist?(filename) && @filestatus_windows[file_index].file_exist
      $game_system.se_play($data_system.buzzer_se)
      return
    end
    $game_system.se_play($data_system.decision_se)
    file = File.open(filename, 'rb')
    read_save_data(file)
    file.close
    $game_system.se_play($data_system.load_se)
    $game_map.update
    $scene = Scene_Map.new
  end

  def on_cancel
    $game_system.se_play($data_system.cancel_se)
    $scene = Scene_Menu.new(7)
  end

end
