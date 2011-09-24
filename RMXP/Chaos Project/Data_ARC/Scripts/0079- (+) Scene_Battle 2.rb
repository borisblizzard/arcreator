#==============================================================================
# Scene_Battle (2)
#==============================================================================

class Scene_Battle
  
  def start_phase1
    @phase = 1
    $game_party.clear_actions
    setup_battle_event
  end
  
  def update_phase1
    start_phase2(1) unless judge
  end
  
  def start_phase2(flag = 0)
    prepare_next_phase2(flag) if flag == 0 || flag == 1
    @phase, @actor_index, @active_battler = 2, -1, nil
    @party_command_window.active = @party_command_window.visible = true
    @party_command_window.refresh
    @party_command_window.reset
    @actor_command_window.active = @actor_command_window.visible =
        $game_temp.battle_main_phase = false
    $game_party.clear_actions
    start_phase4 unless $game_party.inputable?
  end
  
  def prepare_next_phase2(flag)
    @uf_overload = rand(3)
    if flag == 0
      ($game_party.actors + $game_troop.enemies).each {|battler|
          battler.remove_states_auto}
    end
    $data_troops[@troop_id].pages.each_index {|index|
        page = $data_troops[@troop_id].pages[index]
        $game_temp.battle_event_flags[index] = false if page.span == 1}
    setup_battle_event
    @status_window.refresh
    save_time
  end
  
  def update_phase2
    if Input.trigger?($controls.confirm)
      case @party_command_window.index
      when 0
        $game_system.se_play($data_system.decision_se)
        start_phase3
      when 1
        unless $game_party.uf_can_use?(-1)
          $game_system.se_play($data_system.buzzer_se)
          return
        end
        $game_system.se_play($data_system.decision_se)
        start_phase_uf
      when 2
        unless $game_temp.battle_can_escape
          $game_system.se_play($data_system.buzzer_se)
          return
        end
        $game_system.se_play($data_system.decision_se)
        update_phase2_escape
      when 3
        $game_system.se_play($data_system.decision_se)
        $game_party.actors.each_index {|i|
            if $game_party.actors[i].movable?
              repeat_action(i)
            else
              $game_party.actors[i].current_action.clear
              if $game_party.actors[i].states.include?(2)
                $game_party.actors[i].remove_state(2)
              end
            end}
        start_phase4
      end
    end
  end
  
  def repeat_action(i)
    actor, action = $game_party.actors[i], @last_actions[i]
    action.fail = nil
    if action.clear?
      case actor.def_mode
      when 1
        action.kind = 0
        action.basic = 0
        action.target_index = 0
      when 2
        action.kind = 0
        action.basic = 1
        action.target_index = i
      when 3
        action.kind = 5
      end
    elsif action.skill? &&
        (!actor.skill_can_use?(action.skill_id) ||
        CP.gun_database(actor.armor1_id).include?(action.skill_id) &&
        !$game_party.ammo_can_use?(action.skill_id, @ammo.id))
      case actor.def_mode
      when 0
        action.fail = 1
      when 1
        action.kind = action.basic = 0
        action.decide_random_target_for_actor
      when 2
        action.kind = 0
        action.basic = 1
        action.target_index = i
      when 3
        action.kind = 5
      end
    elsif action.item? &&
        !$game_party.item_can_use?(action.item_id)
      case actor.def_mode
      when 0
        action.fail = 2
      when 1
        action.kind = action.basic = 0
        action.decide_random_target_for_actor
      when 2
        action.kind = 0
        action.basic = 1
        action.target_index = i
      when 3
        action.kind = 5
      end
    elsif action.sr? && !actor.sr_can_use?(action.skill_id)
      case actor.def_mode
      when 0
        action.fail = 3
      when 1
        action.kind = action.basic = 0
        action.decide_random_target_for_actor
      when 2
        action.kind = 0
        action.basic = 1
        action.target_index = i
      when 3
        action.kind = 5
      end
    elsif action.meta? && actor.sr < 900
      case actor.def_mode
      when 0
        action.fail = 4
      when 1
        action.kind = action.basic = 0
        action.decide_random_target_for_actor
      when 2
        action.kind = 0
        action.basic = 1
        action.target_index = i
      when 3
        action.kind = 5
      end
    end
    actor.current_action = action
  end
  
  def update_phase2_escape
    enemies_agi = enemies_number = 0
    $game_troop.enemies.each {|enemy|
        if enemy.exist?
          enemies_agi += enemy.agi if enemy.restriction < 4
          enemies_number += 1
        end}
    enemies_agi /= enemies_number.to_f if enemies_number > 0
    actors_agi = actors_number = 0
    $game_party.actors.each {|actor|
        if actor.exist? && actor.restriction < 4
          actors_agi += actor.agi
          actors_number += 1
        end}
    actors_agi /= actors_number.to_f if actors_number > 0
    success = false
    if enemies_number > 0 && enemies_agi > 0
      success |= rand(100) < 50 * actors_agi / enemies_agi
      success |= rand(100) < 50 * actors_agi / enemies_agi
    elsif actors_number > 0
      success = true
    end
    if success
      @levels.each_index {|i|
          $game_party.actors[i].level = @levels[i][0]
          $game_party.actors[i].all_exp = @levels[i][1]}
      $game_system.se_play($data_system.escape_se)
      @escaped = true
      @party_command_window.active = @party_command_window.visible =
          @actor_command_window.active = @actor_command_window.visible = false
      start_phase5
    else
      $game_party.clear_actions
      start_phase4(true)
    end
  end
  
  def start_phase5
    @levels.each_index {|i|
        $game_party.actors[i].level = @levels[i][0]
        $game_party.actors[i].all_exp = @levels[i][1]}
    @phase = 5
    unless @escaped || ($game_system.playing_bgm != nil &&
        $game_temp.map_bgm != nil &&
        $game_system.playing_bgm.name == $game_temp.map_bgm.name)
      $game_system.me_play($game_system.battle_end_me)
    end
    $game_system.bgm_play($game_temp.map_bgm)
    exp = gold = 0
    treasures = []
    unless @escaped
      $game_troop.enemies.each {|enemy|
          unless enemy.hidden || !enemy.dead?
            gold += enemy.gold * $game_party.gold_factor
            factor = enemy.treasure_prob * $game_party.item_factor
            if rand(100) < factor
              treasures.push($data_items[enemy.item_id]) if enemy.item_id > 0
              treasures.push($data_weapons[enemy.weapon_id]) if enemy.weapon_id > 0
              treasures.push($data_armors[enemy.armor_id]) if enemy.armor_id > 0
            end
          end}
      treasures.each {|item|
          case item
          when RPG::Item then $game_party.gain_item(item.id, 1)
          when RPG::Weapon then $game_party.gain_weapon(item.id, 1)
          when RPG::Armor then $game_party.gain_armor(item.id, 1)
          end}
      gold = gold * (9000000 + rand(2000001)) / 10000000
      $game_party.gain_gold(gold)
    end
    $game_troop.enemies.each {|enemy| exp += enemy.exp if enemy.dead? && !enemy.hidden}
    dead = 0
    $game_party.actors.each_index {|i| dead += 1 if $game_party.actors[i].cant_get_exp?}
    exp = exp * $game_party.actors.size / ($game_party.actors.size - dead)
    $game_party.actors.each {|actor|
        unless actor.cant_get_exp?
          if !CP::Cache::NoExtraEXP.include?($game_troop.id)
            actor.exp += exp * actor.exp_factor / 100000
            actor.exp += exp * actor.exp_factor / 100000 if actor.armor4_id == 78
            actor.exp += exp * actor.exp_factor / 100000 if actor.armor5_id == 78
            actor.exp += exp * actor.exp_factor / 100000 if actor.armor6_id == 78
          else
            actor.exp += exp
            actor.exp += exp if actor.armor4_id == 78
            actor.exp += exp if actor.armor5_id == 78
            actor.exp += exp if actor.armor6_id == 78
          end
        end}
    @result_window = Window_BattleResult.new(exp, gold, treasures)
    @result_window.visible = false if @escaped
    @phase5_wait_count = 100
  end
  
end
