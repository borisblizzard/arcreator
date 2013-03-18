#==============================================================================
# Scene_Battle (4)
#==============================================================================

NO_CONFUSION_IDS = [109, 110, 112, 142, 196, 217, 218, 233, 343, 422]

class Scene_Battle
  
  def start_phase4(tried_escape = false)
    @skill = @item = nil
    $game_party.actors.each {|actor|
        if actor.confused?
          decide_confusion_action(actor)
        elsif (actor.armor4_id == 177 || actor.armor5_id == 177 ||
            actor.armor6_id == 177)
          actor.current_action.repeating = true
        end}
    disrupt = []
    unless tried_escape
      $game_party.actors.each_index {|i|
          actor = $game_party.actors[i]
          @last_actions[i] = actor.current_action.clone}
      $game_party.actors.each {|actor|
          if actor.current_action.kind == 0 && actor.current_action.basic == 1
            index = actor.current_action.target_index
            covered = $game_party.actors[index]
            if covered != actor
              if !covered.coverable?
                actor.current_action.decide_cover_target
                next if actor.current_action.clear?
                covered = $game_party.actors[actor.current_action.target_index]
              end
              covered.guarded_by.push(actor)
            end
          end}
      $game_party.actors.each {|actor|
          if actor.meta == 17 && actor.movable? && rand(100) < 25
            disrupt.push(actor)
          end}
    end
    @phase = 4
    $game_temp.battle_turn += 1
    $data_troops[@troop_id].pages.each_index {|index|
        page = $data_troops[@troop_id].pages[index]
        $game_temp.battle_event_flags[index] = false if page.span == 1}
    @actor_index = -1
    @active_battler = nil
    @help_window.visible = @party_command_window.active =
    @party_command_window.visible = @actor_command_window.active =
    @actor_command_window.visible = false
    $game_temp.battle_main_phase = true
    $game_troop.enemies.each {|enemy| enemy.make_action}
    disruptable = $game_troop.enemies.find_all {|enemy|
        enemy.exist? && !enemy.current_action.forcing && !enemy.boss}
    disrupting = []
    disrupted = disruptable.clone
    while disrupt.size > 0 && disruptable.size > 0
      i, j = rand(disrupt.size), rand(disruptable.size)
      disrupt[i].disrupting = disruptable[j]
      disrupting.push(disrupt[i])
      disrupt[i] = disruptable[j] = nil
      disrupt.compact!
      disruptable.compact!
    end
    @disrupted_texts = []
    $game_troop.enemies.each {|enemy| disrupting.each {|actor|
        if actor.disrupting == enemy
          enemy.current_action.clear
          name = enemy.name
          name += (name[name.size-1, 1] == 's' ? '\'' : '\'s')
          text = " (#{disrupted.index(enemy)+1}) action got canceled by "
          @disrupted_texts.push(name + text + actor.name)
          break
        end}}
    make_action_orders
    $game_party.actors.each {|actor| actor.disrupting = nil}
    @phase4_step, @wait_count = 1, 10
  end
  
  def make_action_orders
    @action_battlers, battlers, priority_battlers = [], [], []
    ($game_party.actors + $game_troop.enemies).each {|battler|
        if battler.current_action.kind == 0 && battler.current_action.basic == 1 ||
            battler.current_action.kind == 5
          priority_battlers.push(battler)
        else
          battlers.push(battler)
          if battler.current_action.repeating
            battler.current_action.repeating = false
            @action_battlers.push(battler)
          end
        end}
    while battlers.size > 0
      next_battlers = []
      max = 0
      battlers.each {|battler| max = battler.agi if max < battler.agi}
      battlers.each_index {|i|
          if battlers[i].agi == max
            next_battlers.push(battlers[i])
            battlers[i] = nil
          end}
      battlers.compact!
      if next_battlers.size > 1
        r_battlers, next_battlers = next_battlers, []
        while r_battlers.size > 0
          i = rand(r_battlers.size)
          next_battlers.push(r_battlers[i])
          r_battlers.delete_at(i)
        end
      end
      @action_battlers += next_battlers
    end
    @action_battlers.sort! {|a, b| b.agi - a.agi}
    priority_battlers.reverse.each {|battler| @action_battlers.unshift(battler)}
  end
  
  def update_phase4
    if @trigger != nil
      @trigger.dispose
      @trigger = nil
    end
    if @disrupted_texts.size > 0 && @wait_count <= 0
      @help_window.set_text(@disrupted_texts.shift, 1, Color.new(0, 255, 0))
      @wait_count = 80
    else
      case @phase4_step
      when 1 then update_phase4_step1
      when 2 then update_phase4_step2
      when 3 then update_phase4_step3
      when 4 then update_phase4_step4
      when 5 then update_phase4_step5
      when 6 then update_phase4_step6
      when 9 then update_phase4_step4_2
      end
    end
  end
  
  def update_phase4_step2
    unless @active_battler.current_action.forcing
      if @active_battler.restriction == 2
        @active_battler.current_action.kind = 0
        @active_battler.current_action.basic = 0
      end
      if @active_battler.restriction == 4
        $game_temp.forcing_battler = nil
        @active_battler.current_action.clear
        @active_battler.remove_state(2) if @active_battler.states.include?(2)
        @phase4_step = 1
        return
      end
    end
    @target_battlers = []
    if @active_battler.current_action.fail != nil
      make_fail_action_result
      @phase4_step = 1
    else
      case @active_battler.current_action.kind
      when 0 then make_basic_action_result
      when 1 then make_skill_action_result
      when 2 then make_item_action_result
      when 3 then make_rage_action_result
      when 4 then make_uf_action_result
      when 5 then make_despair_action_result
      when 9 then make_meta_action_result
      end
    end
    @phase4_step = 3 if @phase4_step == 2
  end
  
  def decide_confusion_action(battler)
    kinds = [0, 3]
    kinds.push(1) if battler.can_use_any_skill?
    kinds.push(2) if $game_party.can_use_any_item?
    battler.current_action.kind = kinds[rand(kinds.size)]
    case battler.current_action.kind
    when 0
      if rand(2) == 0
        battler.current_action.basic = 0
      else
        battler.current_action.basic = 1
        set_target_battlers_confused(-1)
      end
    when 1
      ids = []
      battler.skills.each {|id| ids.push(id) if battler.skill_can_use?(id)}
      ids -= NO_CONFUSION_IDS
      battler.current_action.skill_id = ids[rand(ids.size)]
    when 2
      ids = []
      $game_party.items.each_key {|id|
          if $game_party.item_can_use?(id) &&
              !(CP::Cache::Trade | CP::Cache::Quest | CP::Cache::Bullets).include?(id)
            ids.push(id) 
          end}
      battler.current_action.item_id = ids[rand(ids.size)]
    when 3
      ids, reqs = [], []
      (0...7).each {|i|
          weapon = (i == 0)
          equip = nil
          case i
          when 0 then equip = $data_weapons[battler.weapon_id]
          when 1
            if CP::Cache::Lucius.include?(battler.id)
              equip = $data_weapons[battler.armor1_id]
              weapon = true
            else
              equip = $data_armors[battler.armor1_id]
            end
          when 2 then equip = $data_armors[battler.armor2_id]
          when 3 then equip = $data_armors[battler.armor3_id]
          when 4 then equip = $data_armors[battler.armor4_id]
          when 5 then equip = $data_armors[battler.armor5_id]
          when 6 then equip = $data_armors[battler.armor6_id]
          end
          id = (equip == nil ? 0 : equip.id)
          id = (weapon ? CP.sr_weapons(id) : CP.sr_armors(id, battler, i))
          ids.push(id) if (id != 0 && battler.sr_can_use?(id))}
      ids -= NO_CONFUSION_IDS
      id = (ids + [0])[rand(ids.size+1)]
      if id == 0
        battler.current_action.kind = 5
      else
        battler.current_action.skill_id = id
      end
    end
  end
  
  def set_target_battlers_confused(scope = nil)
    case scope
    when -1
      @target_battlers = [$game_party.random_target_actor_con]
    when 1, 3
      if rand(2) == 0
        @target_battlers = [$game_party.random_target_actor]
      else
        @target_battlers = [$game_troop.random_target_enemy]
      end
    when 2, 4
      if rand(2) == 0
        @target_battlers = $game_party.actors.find_all {|actor| actor.exist?}
      else
        @target_battlers = $game_troop.enemies.find_all {|enemy| enemy.exist?}
      end
    when 5
      @target_battlers.push($game_party.random_target_actor_con)
    when 6
      @target_battlers = $game_party.actors.clone
    when 7
      @target_battlers = [@active_battler]
    when 8
      @target_battlers = ($game_party.actors +
          $game_troop.enemies).find_all {|battler| battler.exist?}
    when 9
      if rand(2) == 0
        @target_battlers = $game_party.actors.clone
      else
        @target_battlers = $game_troop.enemies.find_all {|enemy| enemy.exist?}
      end
    when 10
      @target_battlers = ($game_party.actors +
          $game_troop.enemies).find_all {|battler| battler.exist?}
      @target_battlers = [@target_battlers[rand(@target_battlers.size)]]
    end
    @target_battlers.compact!
  end
  
  def set_target_battlers(scope)
    if @active_battler.confused?
      set_target_battlers_confused(scope)
    elsif @active_battler.is_a?(Game_Enemy)
      case scope
      when 1
        index = @active_battler.current_action.target_index
        @target_battlers.push($game_party.smooth_target_actor(index))
      when 2
        @target_battlers = $game_party.actors.find_all {|actor| actor.exist?}
      when 3
        index = @active_battler.current_action.target_index
        @target_battlers.push($game_troop.smooth_target_enemy(index))
      when 4
        @target_battlers = $game_troop.enemies.find_all {|enemy| enemy.exist?}
      when 5
        index = @active_battler.current_action.target_index
        enemy = $game_troop.enemies[index]
        @target_battlers.push(enemy) if enemy != nil && enemy.hp0?
      when 6
        @target_battlers = $game_troop.enemies.find_all {|enemy| enemy.hp0?}
      when 7
        @target_battlers.push(@active_battler)
      when 8
        @target_battlers = ($game_party.actors +
            $game_troop.enemies).find_all {|battler| battler.exist?}
      when 9
        @target_battlers = $game_troop.enemies.find_all {|enemy| enemy.exist?}
      when 10
        @target_battlers = ($game_party.actors +
            $game_troop.enemies).find_all {|battler| battler.exist?}
        @target_battlers = [@target_battlers[rand(@target_battlers.size)]]
      end
    elsif @active_battler.is_a?(Game_Actor)
      case scope
      when 1
        index = @active_battler.current_action.target_index
        @target_battlers.push($game_troop.smooth_target_enemy(index))
      when 2
        @target_battlers = $game_troop.enemies.find_all {|enemy| enemy.exist?}
      when 3
        index = @active_battler.current_action.target_index
        @target_battlers.push($game_party.smooth_target_actor(index))
      when 4
        @target_battlers = $game_party.actors.find_all {|actor| actor.exist?}
      when 5
        index = @active_battler.current_action.target_index
        actor = $game_party.actors[index]
        @target_battlers.push(actor) if actor != nil && actor.hp0?
      when 6
        @target_battlers = $game_party.actors.find_all {|actor| actor.hp0?}
      when 7
        @target_battlers.push(@active_battler)
      when 8
        @target_battlers = ($game_party.actors +
            $game_troop.enemies).find_all {|battler| battler.exist?}
      when 9
        @target_battlers = $game_party.actors.clone
      when 10
        @target_battlers = ($game_party.actors +
            $game_troop.enemies).find_all {|battler| battler.exist?}
        @target_battlers = [@target_battlers[rand(@target_battlers.size)]]
      end
    end
  end
  
  def make_basic_action_result
    if @active_battler.current_action.basic == 0
      make_attack_action_result
    elsif @active_battler.current_action.basic == 1
      make_defend_action_result
    elsif @active_battler.current_action.basic == 2 &&
        @active_battler.is_a?(Game_Enemy)
      make_escape_action_result
    elsif @active_battler.current_action.basic == 3
      make_nothing_action_result
    end
  end
  
  def make_attack_action_result
    @animation1_id = @active_battler.animation1_id
    @animation2_id = @active_battler.animation2_id
    if @active_battler.confused?
      set_target_battlers_confused(1)
      target = @target_battlers[0]
    elsif @active_battler.is_a?(Game_Enemy)
      if @active_battler.restriction == 2
        target = $game_party.random_target_actor
      else
        index = @active_battler.current_action.target_index
        target = $game_party.smooth_target_actor(index)
      end
    elsif @active_battler.is_a?(Game_Actor)
      if @active_battler.restriction == 2
        target = $game_troop.random_target_enemy
      else
        index = @active_battler.current_action.target_index
        target = $game_troop.smooth_target_enemy(index)
      end
    end
    @target_battlers = [target]
    target.attack_effect(@active_battler)
  end
  
  def make_defend_action_result
    if @active_battler.is_a?(Game_Actor)
      cover = $game_party.actors[@active_battler.current_action.target_index]
    elsif @active_battler.is_a?(Game_Enemy)
      cover = @active_battler
    end
    if @active_battler == cover
      @help_window.set_text("#{@active_battler.name} defends", 1)
    else
      @help_window.set_text("#{@active_battler.name} covers #{cover.name}", 1)
    end
  end
  
  def make_escape_action_result
    @help_window.set_text('Absconding', 1)
    @active_battler.escape
  end
  
  def make_nothing_action_result
    $game_temp.forcing_battler = nil
    @phase4_step = 1
  end
  
  def make_skill_action_result
    @skill = $data_skills[@active_battler.current_action.skill_id]
    ammo = true
    if @active_battler.is_a?(Game_Actor) &&
        CP.gun_database(@active_battler.armor1_id).include?(@skill.id)
      ammo = $game_party.ammo_can_use?(@skill.id, @ammo.id)
    end
    unless @active_battler.current_action.forcing ||
        @active_battler.skill_can_use?(@skill.id) && ammo
      @active_battler.current_action.fail = 1
      make_fail_action_result
      $game_temp.forcing_battler = nil
      @phase4_step = 1
      return false
    end
    if @active_battler.states.include?(31) 
      @active_battler.sp -= (@skill.sp_cost / 2.0).ceil
    else 
      @active_battler.sp -= @skill.sp_cost 
    end
    @status_window.refresh
    if @active_battler.is_a?(Game_Actor) &&
        CP.gun_database(@active_battler.armor1_id).include?(@skill.id)
      $game_party.lose_item(@ammo.id, CP.ammo_req(@skill.id))
      @skill = @skill.clone
      @skill.element_set |= @ammo.element_set
      @skill.plus_state_set |= @ammo.plus_state_set
      @skill.minus_state_set |= @ammo.minus_state_set
      if @ammo.animation1_id != 0
        @skill.animation1_id = [@skill.animation1_id, @ammo.animation1_id]
      end
      if @ammo.animation2_id != 0
        @skill.animation2_id = [@skill.animation2_id, @ammo.animation2_id]
      end
      @skill.pdef_f -= @ammo.pdef_f
      w_text = ' with '
      @help_window.set_text(@skill.name + w_text + @ammo.name, 1)
    else
      @help_window.set_text(@skill.name, 1)
    end
    @animation1_id, @animation2_id = @skill.animation1_id, @skill.animation2_id
    @common_event_id = @skill.common_event_id
    set_target_battlers(@skill.scope)
    if @skill.id != 381
      @target_battlers.each {|target| target.skill_effect(@active_battler, @skill)}
    else
      @target_battlers -= $game_party.actors
    end
    return true
  end
  
  def make_item_action_result
    @item = $data_items[@active_battler.current_action.item_id]
    unless $game_party.item_can_use?(@item.id)
      @active_battler.current_action.fail = 2
      make_fail_action_result
      @phase4_step = 1
      return false
    end
    $game_party.lose_item(@item.id, 1) if @item.consumable
    @help_window.set_text(@item.name, 1)
    @animation1_id, @animation2_id = @item.animation1_id, @item.animation2_id
    @common_event_id = @item.common_event_id
    index = @active_battler.current_action.target_index
    target = $game_party.smooth_target_actor(index)
    set_target_battlers(@item.scope)
    @target_battlers.each {|target| target.item_effect(@item)}
    return true
  end
  
  def make_despair_action_result
    if @active_battler.current_action.kind == 5
      @help_window.set_text("#{@active_battler.name} despairs", 1)
    end
  end
  
  def make_fail_action_result
    text = ''
    case @active_battler.current_action.fail
    when 1
      skill = $data_skills[@active_battler.current_action.skill_id]
      if skill != nil
        (19..24).each {|i|
            if skill.element_set.include?(i)
              text = "#{@active_battler.name} failed to use #{$data_system.elements[i]} \"#{skill.name}\""
              break
            end}
        text = "#{@active_battler.name} failed to use \"#{skill.name}\"" if text == ''
      end
    when 2
      item = $data_items[@active_battler.current_action.item_id]
      text = "#{@active_battler.name} failed to use \"#{item.name}\"" if item != nil
    when 3
      skill = $data_skills[@active_battler.current_action.skill_id]
      text = "#{@active_battler.name} failed to use Soul Rage \"#{skill.name}\"" if skill != nil
    when 4
      skill = $data_skills[@active_battler.current_action.skill_id]
      text = "#{@active_battler.name} failed to use Meta Limit \"#{skill.name}\"" if skill != nil
    when 5
      skill = $data_skills[@active_battler.current_action.skill_id]
      if skill != nil
        text = "Failed to use Unity Force \"#{skill.name}\""
      end
    else
      text = 'Action failed'
    end
    unless text == ''
      @help_window.set_text(text, 1, Color.new(255, 255, 255, 192))
      @wait_count = 80
    end
  end
  
  def update_phase4_step3
    if @animation1_id == 0
      @active_battler.white_flash = true
      @wait_count = 50 if @active_battler.current_action.fail != nil
    else
      @active_battler.animation_id = @animation1_id
      @active_battler.animation_hit = true
    end
    @phase4_step = 4
  end
  
  def update_phase4_step4
    if @animation2_id.is_a?(Array)
      id = @animation2_id.shift
      @phase4_step = 9
    else
      id = @animation2_id
    end
    @target_battlers.each {|target|
        target.animation_id = id
        target.animation_hit = (target.damage != 'Missed')}
    @wait_count = 1
    @phase4_step = 5 unless @phase4_step == 9
  end
  
  def update_phase4_step4_2
    id = @animation2_id.shift
    @target_battlers.each {|target|
        target.animation_id = id
        target.animation_hit = (target.damage != 'Missed')}
    @wait_count, @phase4_step = 1, (@animation2_id.size > 0 ? 9 : 5)
  end
  
  def update_phase4_step5
    @help_window.visible = false
    if @skill != nil && @skill.id == 381
      return_in_time
    else
      @target_battlers.each {|target|
          if target.damage != nil
            if @active_battler.is_a?(Game_Actor) &&
                target.damage.is_a?(Numeric) &&
                CP::Cache::MainParty.any? {|i|
                    $game_party.actors.include?($game_actors[i])}
              $game_system.total_damage += target.damage
              if $game_system.max_damage < target.damage
                $game_system.max_damage = target.damage
              end
            end
            target.damage_pop = true
            @status_window.refresh if target.absorb_post_process(@active_battler)
          end}
      if $game_troop.enemies[0].id == 87 && $game_troop.enemies[0].hp <= 0
        $game_troop.enemies[1].hp = 0
      end
    end
    @status_window.refresh
    @skill, @phase4_step = nil, 6
  end
  
  def update_phase4_step6
    $game_temp.forcing_battler = nil
    $game_variables[162] = @active_battler.index
    if @common_event_id > 0
      common_event = $data_common_events[@common_event_id]
      $game_system.battle_interpreter.setup(common_event.list, 0)
    end
    @active_battler.damage_pop = false
    @active_battler.damage, @phase4_step = nil, 1
  end
  
end
