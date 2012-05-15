#==============================================================================
# Scene_Battle (3)
#==============================================================================

class Scene_Battle
  
  def start_phase3
    @phase = 3
    @actor_index = -1
    @active_battler = nil
    $game_party.reset_slip_damage
    $game_troop.reset_slip_damage
    phase3_next_actor
  end
  
  def phase3_next_actor
    begin
      @active_battler.blink = false if @active_battler != nil
      if @actor_index == $game_party.actors.size-1
        start_phase4
        return
      end
      @actor_index += 1
      @active_battler = $game_party.actors[@actor_index]
      @active_battler.blink = true
    end until @active_battler.inputable?
    phase3_setup_command_window
  end
  
  def phase3_prior_actor
    begin
      @active_battler.blink = false if @active_battler != nil
      if @actor_index == 0
        start_phase2(2)
        return
      end
      @actor_index -= 1
      @active_battler = $game_party.actors[@actor_index]
      @active_battler.blink = true
    end until @active_battler.inputable?
    phase3_setup_command_window
  end
  
  def update_phase3
    if @enemy_arrows.size > 0
      update_phase3_enemy_select
    elsif @actor_arrows.size > 0
      update_phase3_actor_select
    elsif @skill_window != nil
      update_phase3_skill_select
    elsif @item_window != nil
      update_phase3_item_select
    elsif @actor_command_window.active
      update_phase3_basic_command
    elsif @ability_command_windows.any? {|win| win.active}
      update_phase3_ability_select
    elsif @rage_command_window != nil && @rage_command_window.active
      update_phase3_rage_select
    end
  end
  
  def update_phase3_basic_command
    if Input.trigger?($controls.cancel)
      $game_system.se_play($data_system.cancel_se)
      phase3_prior_actor
    elsif Input.trigger?($controls.confirm)
      $game_system.se_play($data_system.decision_se)
      case @actor_command_window.index
      when 0
        @active_battler.current_action.kind = 0
        @active_battler.current_action.basic = 0
        start_enemy_select
      when 1
        @active_battler.current_action.kind = 1
        start_ability_select
      when 2
        @active_battler.current_action.kind = 0
        @active_battler.current_action.basic = 1
        start_actor_select
      when 3
        @active_battler.current_action.kind = 2
        start_item_select
      when 4
        @active_battler.current_action.kind = 3
        start_rage_select
      when 5
        @active_battler.current_action.kind = 9
        start_meta_select
      end
    end
  end
  
  def update_phase3_skill_select
    if @ammo_window != nil
      @ammo_window.visible = true
      @ammo_window.update
      if Input.trigger?($controls.cancel)
        $game_system.se_play($data_system.cancel_se)
        @ammo_window.dispose
        @ammo_window = nil
        @skill_window.visible = true
      elsif Input.trigger?($controls.confirm)
        @ammo = @ammo_window.item
        if @ammo == nil || !$game_party.ammo_can_use?(@skill.id, @ammo.id)
          $game_system.se_play($data_system.buzzer_se)
          return
        end
        $game_system.se_play($data_system.decision_se)
        @ammo_window.visible = false
        case @skill.scope
        when 1 then start_enemy_select
        when 2 then start_enemy_select_all
        when 3, 5 then start_actor_select
        when 4, 6, 9 then start_actor_select_all
        when 7 then start_self_select
        when 8, 10 then start_select_all
        else
          end_skill_select
          phase3_next_actor
        end
      end
      return
    end
    @skill_window.visible = true
    @skill_window.update
    if Input.trigger?($controls.cancel)
      $game_system.se_play($data_system.cancel_se)
      end_skill_select_back
    elsif Input.trigger?($controls.confirm)
      @skill = @skill_window.skill
      if @skill == nil || !@active_battler.skill_can_use?(@skill.id)
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      $game_system.se_play($data_system.decision_se)
      @active_battler.current_action.skill_id = @skill.id
      @skill_window.visible = false
      ids = CP.gun_database(@active_battler.armor1_id)
      if ids.include?(@skill.id)
        @ammo_window = Window_Ammo.new(@skill.id, @help_window)
      else
        case @skill.scope
        when 1 then start_enemy_select
        when 2 then start_enemy_select_all
        when 3, 5 then start_actor_select
        when 4, 6, 9 then start_actor_select_all
        when 7 then start_self_select
        when 8, 10 then start_select_all
        else
          end_skill_select
          phase3_next_actor
        end
      end
    end
  end
  
  def update_phase3_item_select
    @item_window.visible = true
    @item_window.update
    if Input.trigger?($controls.cancel)
      $game_system.se_play($data_system.cancel_se)
      end_item_select
    elsif Input.trigger?($controls.confirm)
      @item = @item_window.item
      unless $game_party.item_can_use?(@item.id)
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      $game_system.se_play($data_system.decision_se)
      @active_battler.current_action.item_id = @item.id
      @item_window.visible = false
      case @item.scope
      when 1 then start_enemy_select
      when 2 then start_enemy_select_all
      when 3, 5 then start_actor_select
      when 4, 6, 9 then start_actor_select_all
      when 7 then start_self_select
      when 8, 10 then start_select_all
      else
        end_item_select
        phase3_next_actor
      end
    end
  end
  
  def update_phase3_enemy_select
    @enemy_arrows.each {|arrow| arrow.update(@select_type)}
    if Input.trigger?($controls.cancel)
      $game_system.se_play($data_system.cancel_se)
      end_enemy_select
    elsif Input.trigger?($controls.confirm)
      $game_system.se_play($data_system.decision_se)
      @active_battler.current_action.target_index = @enemy_arrows[0].index
      end_enemy_select
      end_skill_select if @skill_window != nil
      end_item_select if @item_window != nil
      phase3_next_actor
    end
  end
  
  def update_phase3_actor_select
    @actor_arrows.each {|arrow| arrow.update(@select_type)}
    if Input.trigger?($controls.cancel)
      $game_system.se_play($data_system.cancel_se)
      end_actor_select
    elsif Input.trigger?($controls.confirm)
      $game_system.se_play($data_system.decision_se)
      @active_battler.current_action.target_index = @actor_arrows[0].index
      end_actor_select
      end_skill_select if @skill_window != nil
      end_item_select if @item_window != nil
      phase3_next_actor
    end
  end
  
  def start_enemy_select
    @enemy_arrows.push(Arrow_Enemy.new(@spriteset.viewport1))
    @actor_command_window.active = @actor_command_window.visible = false
    @enemy_arrows[0].help_window = @help_window
    @select_type = true
  end
  
  def start_enemy_select_all
    enemies = get_valid_enemies
    enemies.each {|enemy|
        arrow = Arrow_Enemy.new(@spriteset.viewport1)
        arrow.index = enemy.index
        @enemy_arrows.push(arrow)}
    @actor_command_window.active = @actor_command_window.visible = false
    @help_window.set_text('All enemies', 1)
    @select_type = false
  end
  
  def end_enemy_select
    @enemy_arrows.each {|arrow| arrow.dispose}
    @enemy_arrows = []
    if @actor_command_window.index == 0 || @actor_command_window.index == 5
      @help_window.visible = false
      @actor_command_window.active = @actor_command_window.visible = true
    end
  end
  
  def start_actor_select
    @actor_arrows.push(Arrow_Actor.new(@spriteset.viewport2))
    @actor_command_window.active = @actor_command_window.visible = false
    @actor_arrows[0].help_window = @help_window
    @actor_arrows[0].index = @actor_index
    @select_type = true
  end
  
  def start_actor_select_all
    $game_party.actors.each {|actor|
        arrow = Arrow_Actor.new(@spriteset.viewport1)
        arrow.index = actor.index
        @actor_arrows.push(arrow)}
    @actor_command_window.active = @actor_command_window.visible = false
    @help_window.set_text('All allies', 1)
    @select_type = false
  end
  
  def start_self_select
    start_actor_select
    @select_type = false
  end
  
  def end_actor_select
    @actor_arrows.each {|arrow| arrow.dispose}
    @actor_arrows = []
    if @active_battler.current_action.kind == 0 &&
        @active_battler.current_action.basic == 1 ||
        @active_battler.current_action.kind == 9
      @actor_command_window.active = @actor_command_window.visible = true
    end
  end
  
  def start_select_all
    enemies = get_valid_enemies
    enemies.each {|enemy|
        arrow = Arrow_Enemy.new(@spriteset.viewport1)
        arrow.index = enemy.index
        @enemy_arrows.push(arrow)}
    $game_party.actors.each {|actor|
        arrow = Arrow_Actor.new(@spriteset.viewport1)
        arrow.index = actor.index
        @enemy_arrows.push(arrow)}
    @actor_command_window.active = @actor_command_window.visible = false
    @help_window.set_text('All', 1)
    @select_type = false
  end
  
  def start_ability_select
    @ability_command_windows[@active_battler.index].active =
    @ability_command_windows[@active_battler.index].visible = true
    @actor_command_window.active = @actor_command_window.visible = false
  end
  
  def start_skill_select
    @skill_window = Window_Skill.new(@active_battler,
        @ability_command_windows[@active_battler.index].type)
    @skill_window.help_window = @help_window
    @ability_command_windows[@active_battler.index].active =
    @ability_command_windows[@active_battler.index].visible = false
  end
  
  def end_skill_select_back
    if @ammo_window != nil
      @ammo_window.dispose
      @ammo_window = nil
    end
    @skill_window.dispose
    @skill_window = nil
    @ability_command_windows[@active_battler.index].active =
    @ability_command_windows[@active_battler.index].visible = true
  end
  
  def end_skill_select
    if @ammo_window != nil
      @ammo_window.dispose
      @ammo_window = nil
    end
    @skill_window.dispose
    @skill_window = nil
    @actor_command_window.active = @actor_command_window.visible = true
  end
  
  def end_skill_select_next
    @ability_command_windows[@active_battler.index].active =
    @ability_command_windows[@active_battler.index].visible = false
    @actor_command_window.active = @actor_command_window.visible = true
  end
  
  def update_phase3_ability_select
    if Input.trigger?($controls.cancel)
      $game_system.se_play($data_system.cancel_se)
      end_skill_select_next
    elsif Input.trigger?($controls.confirm)
      $game_system.se_play($data_system.decision_se)
      start_skill_select
    end
  end
  
  def start_item_select
    @item_window = Window_Item.new
    @item_window.help_window = @help_window
    @actor_command_window.active = @actor_command_window.visible = false
  end
  
  def end_item_select
    @item_window.dispose
    @item_window = nil
    @help_window.visible = false
    @actor_command_window.active = @actor_command_window.visible = true
  end
  
end
