#==============================================================================
# Interpreter (5)
#==============================================================================

class Interpreter
  
  def command_201
    return true if $game_temp.in_battle
    if $game_temp.player_transferring || $game_temp.message_window_showing ||
        $game_temp.transition_processing
      return false
    end
    $game_temp.player_transferring = true
    if @parameters[0] == 0
      $game_temp.player_new_map_id = @parameters[1]
      $game_temp.player_new_x = @parameters[2]
      $game_temp.player_new_y = @parameters[3]
      $game_temp.player_new_direction = @parameters[4]
    else
      $game_temp.player_new_map_id = $game_variables[@parameters[1]]
      $game_temp.player_new_x = $game_variables[@parameters[2]]
      $game_temp.player_new_y = $game_variables[@parameters[3]]
      $game_temp.player_new_direction = @parameters[4]
    end
    @index += 1
    if @parameters[5] == 0
      Graphics.freeze
      $game_temp.transition_processing = true
      $game_temp.transition_name = ''
    end
    return false
  end
  
  def command_202
    return true if $game_temp.in_battle
    character = get_character(@parameters[0])
    return true if character == nil
    if @parameters[1] == 0
      character.moveto(@parameters[2], @parameters[3])
    elsif @parameters[1] == 1
      character.moveto($game_variables[@parameters[2]],
          $game_variables[@parameters[3]])
    else
      old_x, old_y = character.x, character.y
      character2 = get_character(@parameters[2])
      if character2 != nil
        character.moveto(character2.x, character2.y)
        character2.moveto(old_x, old_y)
      end
    end
    case @parameters[4]
    when 2 then character.turn_down
    when 4 then character.turn_left
    when 6 then character.turn_right
    when 8 then character.turn_up
    end
    return true
  end
  
  def command_203
    return true if $game_temp.in_battle
    return false if $game_map.scrolling?
    $game_map.start_scroll(@parameters[0], @parameters[1], @parameters[2])
    return true
  end
  
  def command_204
    case @parameters[0]
    when 0
      $game_map.panorama_name = @parameters[1]
      $game_map.panorama_hue = @parameters[2]
    when 1
      $game_map.fog_name = @parameters[1]
      $game_map.fog_hue = @parameters[2]
      $game_map.fog_opacity = @parameters[3]
      $game_map.fog_blend_type = @parameters[4]
      $game_map.fog_zoom = @parameters[5]
      $game_map.fog_sx = @parameters[6]
      $game_map.fog_sy = @parameters[7]
    when 2
      $game_map.battleback_name = @parameters[1]
      $game_temp.battleback_name = @parameters[1]
    end
    return true
  end
  
  def command_205
    $game_map.start_fog_tone_change(@parameters[0], @parameters[1] * 2)
    return true
  end
  
  def command_206
    $game_map.start_fog_opacity_change(@parameters[0], @parameters[1] * 2)
    return true
  end
  
  def command_207
    character = get_character(@parameters[0])
    return true if character == nil
    character.animation_id = @parameters[1]
    return true
  end
  
  def command_208
    $game_player.transparent = (@parameters[0] == 0)
    return true
  end
  
  def command_209
    character = get_character(@parameters[0])
    return true if character == nil
    character.force_move_route(@parameters[1])
    return true
  end
  
  def command_210
    @move_route_waiting = true unless $game_temp.in_battle
    return true
  end
  
  def command_221
    return false if $game_temp.message_window_showing
    Graphics.freeze
    return true
  end
  
  def command_222
    return false if $game_temp.transition_processing
    $game_temp.transition_processing = true
    $game_temp.transition_name = @parameters[0]
    @index += 1
    return false
  end
  
  def command_223
    $game_screen.start_tone_change(@parameters[0], @parameters[1] * 2)
    return true
  end
  
  def command_224
    $game_screen.start_flash(@parameters[0], @parameters[1] * 2)
    return true
  end
  
  def command_225
    $game_screen.start_shake(@parameters[0], @parameters[1], @parameters[2] * 2)
    return true
  end
  
  def command_231
    number = @parameters[0] + ($game_temp.in_battle ? 50 : 0)
    if @parameters[3] == 0
      x, y = @parameters[4, 2]
    else
      x, y = $game_variables[@parameters[4]], $game_variables[@parameters[5]]
    end
    $game_screen.pictures[number].show(@parameters[1], @parameters[2],
        x, y, @parameters[6], @parameters[7], @parameters[8], @parameters[9])
    return true
  end
  
  def command_232
    number = @parameters[0] + ($game_temp.in_battle ? 50 : 0)
    if @parameters[3] == 0
      x, y = @parameters[4, 2]
    else
      x, y = $game_variables[@parameters[4]], $game_variables[@parameters[5]]
    end
    $game_screen.pictures[number].move(@parameters[1] * 2, @parameters[2],
        x, y, @parameters[6], @parameters[7], @parameters[8], @parameters[9])
    return true
  end
  
  def command_233
    number = @parameters[0] + ($game_temp.in_battle ? 50 : 0)
    $game_screen.pictures[number].rotate(@parameters[1])
    return true
  end
  
  def command_234
    number = @parameters[0] + ($game_temp.in_battle ? 50 : 0)
    $game_screen.pictures[number].start_tone_change(@parameters[1],
        @parameters[2] * 2)
    return true
  end
  
  def command_235
    number = @parameters[0] + ($game_temp.in_battle ? 50 : 0)
    $game_screen.pictures[number].erase
    return true
  end
  
  def command_236
    $game_screen.weather(@parameters[0], @parameters[1], @parameters[2])
    return true
  end
  
  def command_241
    $game_system.bgm_play(@parameters[0])
    return true
  end
  
  def command_242
    $game_system.bgm_fade(@parameters[0])
    return true
  end
  
  def command_245
    $game_system.bgs_play(@parameters[0])
    return true
  end
  
  def command_246
    value = @parameters[0]
    value = 0 if value == 60
    $game_system.bgs_fade(value)
    return true
  end
  
  def command_247
    $game_system.bgm_memorize
    $game_system.bgs_memorize
    return true
  end
  
  def command_248
    $game_system.bgm_restore
    $game_system.bgs_restore
    return true
  end
  
  def command_249
    $game_system.me_play(@parameters[0])
    return true
  end
  
  def command_250
    $game_system.se_play(@parameters[0])
    return true
  end
  
  def command_251
    Audio.se_stop
    return true
  end
  
end
