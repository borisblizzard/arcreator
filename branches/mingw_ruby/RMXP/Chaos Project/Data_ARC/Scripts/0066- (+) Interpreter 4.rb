#==============================================================================
# Interpreter (4)
#==============================================================================

class Interpreter
  
  def command_121
    (@parameters[0]..@parameters[1]).each {|i|
        $game_switches[i] = (@parameters[2] == 0)}
    $game_map.need_refresh = true
    return true
  end
  
  def command_122
    value = 0
    case @parameters[3]
    when 0 then value = @parameters[4]
    when 1 then value = $game_variables[@parameters[4]]
    when 2 then value = @parameters[4] + rand(@parameters[5] - @parameters[4] + 1)
    when 3 then value = $game_party.item_number(@parameters[4])
    when 4
      actor = $game_actors[@parameters[4]]
      if actor != nil
        case @parameters[5]
        when 0 then value = actor.level
        when 1 then value = actor.exp
        when 2 then value = actor.hp
        when 3 then value = actor.sp
        when 4 then value = actor.maxhp
        when 5 then value = actor.maxsp
        when 6 then value = actor.str
        when 7 then value = actor.dex
        when 8 then value = actor.agi
        when 9 then value = actor.int
        when 10 then value = actor.atk
        when 11 then value = actor.pdef
        when 12 then value = actor.mdef
        when 13 then value = actor.eva
        end
      end
    when 5
      enemy = $game_troop.enemies[@parameters[4]]
      if enemy != nil
        case @parameters[5]
        when 0 then value = enemy.hp
        when 1 then value = enemy.sp
        when 2 then value = enemy.maxhp
        when 3 then value = enemy.maxsp
        when 4 then value = enemy.str
        when 5 then value = enemy.dex
        when 6 then value = enemy.agi
        when 7 then value = enemy.int
        when 8 then value = enemy.atk
        when 9 then value = enemy.pdef
        when 10 then value = enemy.mdef
        when 11 then value = enemy.eva
        end
      end
    when 6
      character = get_character(@parameters[4])
      if character != nil
        case @parameters[5]
        when 0 then value = character.x
        when 1 then value = character.y
        when 2 then value = character.direction
        when 3 then value = character.screen_x
        when 4 then value = character.screen_y
        when 5 then value = character.terrain_tag
        end
      end
    when 7
      case @parameters[4]
      when 0 then value = $game_map.map_id
      when 1 then value = $game_party.actors.size
      when 2 then value = $game_party.gold
      when 3 then value = $game_party.steps
      when 4 then value = Graphics.frame_count / Graphics.frame_rate
      when 5 then value = $game_system.timer / Graphics.frame_rate
      when 6 then value = $game_system.save_count
      end
    end
    (@parameters[0]..@parameters[1]).each {|i|
        case @parameters[2]
        when 0 then $game_variables[i] = value
        when 1 then $game_variables[i] += value
        when 2 then $game_variables[i] -= value
        when 3 then $game_variables[i] *= value
        when 4 then $game_variables[i] /= value if value != 0
        when 5 then $game_variables[i] %= value if value != 0
        end
        $game_variables[i] = 99999999 if $game_variables[i] > 99999999
        $game_variables[i] = -99999999 if $game_variables[i] < -99999999}
    $game_map.need_refresh = true
    return true
  end
  
  def command_123
    if @event_id > 0
      key = [$game_map.map_id, @event_id, @parameters[0]]
      $game_self_switches[key] = (@parameters[1] == 0)
    end
    $game_map.need_refresh = true
    return true
  end
  
  def command_124
    if @parameters[0] == 0
      $game_system.timer = @parameters[1] * Graphics.frame_rate
      $game_system.timer_working = true
    end
    $game_system.timer_working = false if @parameters[0] == 1
    return true
  end
  
  def command_125
    value = operate_value(@parameters[0], @parameters[1], @parameters[2])
    $game_party.gain_gold(value)
    return true
  end
  
  def command_126
    value = operate_value(@parameters[1], @parameters[2], @parameters[3])
    $game_party.gain_item(@parameters[0], value)
    return true
  end
  
  def command_127
    value = operate_value(@parameters[1], @parameters[2], @parameters[3])
    $game_party.gain_weapon(@parameters[0], value)
    return true
  end
  
  def command_128
    value = operate_value(@parameters[1], @parameters[2], @parameters[3])
    $game_party.gain_armor(@parameters[0], value)
    return true
  end
  
  def command_129
    actor = $game_actors[@parameters[0]]
    if actor != nil
      if @parameters[1] == 0
        $game_actors[@parameters[0]].setup(@parameters[0]) if @parameters[2] == 1
        $game_party.add_actor(@parameters[0])
      else
        $game_party.remove_actor(@parameters[0])
      end
    end
    return true
  end
  
  def command_131
    $game_system.windowskin_name = @parameters[0]
    return true
  end
  
  def command_132
    $game_system.battle_bgm = @parameters[0]
    return true
  end
  
  def command_133
    $game_system.battle_end_me = @parameters[0]
    return true
  end
  
  def command_134
    $game_system.save_disabled = (@parameters[0] == 0)
    return true
  end
  
  def command_135
    $game_system.menu_disabled = (@parameters[0] == 0)
    return true
  end
  
  def command_136
    if $game_system.encounter_disabled != (@parameters[0] == 0)
      $game_system.encounter_disabled = (@parameters[0] == 0)
      $game_player.make_encounter_count
    end
    return true
  end
  
end
