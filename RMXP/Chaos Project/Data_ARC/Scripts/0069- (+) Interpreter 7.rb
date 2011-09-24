#==============================================================================
# Interpreter (7)
#==============================================================================

class Interpreter
  
  def command_331
    value = operate_value(@parameters[1], @parameters[2], @parameters[3])
    iterate_enemy(@parameters[0]) {|enemy|
        if enemy.hp > 0
          if @parameters[4] == false && enemy.hp + value <= 0
            enemy.hp = 1
          else
            enemy.hp += value
          end
        end}
    return true
  end
  
  def command_332
    value = operate_value(@parameters[1], @parameters[2], @parameters[3])
    iterate_enemy(@parameters[0]) {|enemy| enemy.sp += value}
    return true
  end
  
  def command_333
    iterate_enemy(@parameters[0]) {|enemy|
        enemy.immortal = false if $data_states[@parameters[2]].zero_hp
        if @parameters[1] == 0
          enemy.add_state(@parameters[2])
        else
          enemy.remove_state(@parameters[2])
        end}
    return true
  end
  
  def command_334
    iterate_enemy(@parameters[0]) {|enemy| enemy.recover_all}
    return true
  end
  
  def command_335
    enemy = $game_troop.enemies[@parameters[0]]
    enemy.hidden = false if enemy != nil
    return true
  end
  
  def command_336
    enemy = $game_troop.enemies[@parameters[0]]
    enemy.transform(@parameters[1]) if enemy != nil
    return true
  end
  
  def command_337
    iterate_battler(@parameters[0], @parameters[1]) {|battler|
        battler.animation_id = @parameters[2] if battler.exist?}
    return true
  end
  
  def command_338
    value = operate_value(0, @parameters[2], @parameters[3])
    iterate_battler(@parameters[0], @parameters[1]) {|battler|
        if battler.exist?
          battler.hp -= value
          if $game_temp.in_battle
            battler.damage = value
            battler.damage_pop = true
          end
        end}
    return true
  end
  
  def command_339
    return true unless $game_temp.in_battle
    return true if $game_temp.battle_turn == 0
    iterate_battler(@parameters[0], @parameters[1]) {|battler|
        if battler.exist?
          battler.current_action.kind = @parameters[2]
          if battler.current_action.kind == 0
            battler.current_action.basic = @parameters[3]
          else
            battler.current_action.skill_id = @parameters[3]
          end
          if @parameters[4] == -2
            if battler.is_a?(Game_Enemy)
              battler.current_action.decide_last_target_for_enemy
            else
              battler.current_action.decide_last_target_for_actor
            end
          elsif @parameters[4] == -1
            if battler.is_a?(Game_Enemy)
              battler.current_action.decide_random_target_for_enemy
            else
              battler.current_action.decide_random_target_for_actor
            end
          elsif @parameters[4] >= 0
            battler.current_action.target_index = @parameters[4]
          end
          battler.current_action.forcing = true
          if battler.current_action.valid? && @parameters[5] == 1
            $game_temp.forcing_battler = battler
            @index += 1
            return false
          end
        end}
    return true
  end
  
  def command_340
    $game_temp.battle_abort = true
    @index += 1
    return false
  end
  
  def command_351
    $game_temp.battle_abort = $game_temp.menu_calling =
        $game_temp.event_menu = true
    @index += 1
    return false
  end
  
  def command_352
    $game_temp.battle_abort = $game_temp.save_calling = true
    @index += 1
    return false
  end
  
  def command_353
    $game_temp.gameover = true
    return false
  end
  
  def command_354
    $game_temp.to_title = true
    return false
  end
  
  def command_355
    script = @list[@index].parameters[0] + "\n"
    loop do
      break if @list[@index+1].code != 655
      script += @list[@index+1].parameters[0] + "\n"
      @index += 1
    end
    eval(script)
    return true
  end
  
end
