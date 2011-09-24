#==============================================================================
# Game_Character (2)
#==============================================================================

class Game_Character
  
  attr_accessor :move_speed
  
  def update
    jumping? ? update_jump : (moving? ? update_move : update_stop)
    if @anime_count > 16 - @move_speed * 2
      if !@step_anime && @stop_count > 0
        @pattern = @original_pattern
      else
        @pattern = (@pattern + 1) % 4
      end
      @anime_count = 0
    end
    if @wait_count > 0
      @wait_count -= 1 
    elsif @move_route_forcing
      move_type_custom
    elsif !@starting && !lock? &&
        @stop_count >= (40 - @move_frequency * 2) * (6 - @move_frequency)
      case @move_type
      when 1 then move_type_random
      when 2 then move_type_toward_player
      when 3 then move_type_custom
      end
    end
  end
  
  def update_jump
    @jump_count -= 1
    @real_x = (@real_x * @jump_count + @x * 128) / (@jump_count + 1)
    @real_y = (@real_y * @jump_count + @y * 128) / (@jump_count + 1)
  end
  
  def update_move
    distance = 2 ** @move_speed
    x, y = @x * 128, @y * 128
    if y > @real_y
      @real_y = @real_y + distance
      @real_y = y if @real_y > y
    elsif y < @real_y
      @real_y = @real_y - distance
      @real_y = y if @real_y < y
    end
    if x > @real_x
      @real_x = @real_x + distance
      @real_x = x if @real_x > x
    elsif x < @real_x
      @real_x = @real_x - distance
      @real_x = x if @real_x < x
    end
    if @walk_anime
      @anime_count += 1.6
    elsif @step_anime
      @anime_count += 1
    end
  end
  
  def update_stop
    if @step_anime
      @anime_count += 1
    elsif @pattern != @original_pattern
      @anime_count += 1.5
    end
    @stop_count += 1 unless @starting || lock?
  end
  
  def move_type_random
    return if moving?
    case rand(6)
    when 0..3 then move_random
    when 4 then move_forward
    when 5 then @stop_count = 0
    end
  end
  
  def move_type_toward_player
    sx = @x - $game_player.x
    sy = @y - $game_player.y
    abs_sx = sx > 0 ? sx : -sx
    abs_sy = sy > 0 ? sy : -sy
    if sx + sy >= 20
      move_random
      return
    end
    case rand(6)
    when 0..3 then move_toward_player
    when 4 then move_random
    when 5 then move_forward
    end
  end
  
  def increase_steps
    @stop_count = 0
  end
  
  def move_type_custom
    return if jumping? || moving?
    while @move_route_index < @move_route.list.size
      index = @move_route_index if index == nil
      command = @move_route.list[@move_route_index]
      trace = CP.trace
      if trace != nil && trace[0] == self && command.code.between?(1, 4)
        reverse = command.clone
        reverse.code = 5 - command.code
        trace.push(reverse)
      end
      if command.code == 0
        if @move_route.repeat
          this_index, @move_route_index = @move_route_index, 0
          if @move_route.list.size > 1 &&
              (this_index + 1) % @move_route.list.size != index
            next
          else
            return
          end
        end
        if @move_route_forcing
          @move_route_forcing = false
          @move_route = @original_move_route
          @move_route_index = @original_move_route_index
          @original_move_route = nil
        end
        @stop_count = 0
        return
      end
      if command.code <= 14
        case command.code
        when 1 then move_down
        when 2 then move_left
        when 3 then move_right
        when 4 then move_up
        when 5 then move_lower_left
        when 6 then move_lower_right
        when 7 then move_upper_left
        when 8 then move_upper_right
        when 9 then move_random
        when 10 then move_toward_player
        when 11 then move_away_from_player
        when 12 then move_forward
        when 13 then move_backward
        when 14 then jump(command.parameters[0], command.parameters[1])
        end
        return if !@move_route.skippable && !moving? && !jumping?
        @move_route_index += 1
        return
      end
      if command.code == 15
        if @tracer && $game_system.gold_rate > 0.5
          @wait_count = command.parameters[0] * 4 - 1
        else
          @wait_count = command.parameters[0] * 2 - 1
        end
        @move_route_index += 1
        return
      end
      if command.code >= 16 && command.code <= 26
        case command.code
        when 16 then turn_down
        when 17 then turn_left
        when 18 then turn_right
        when 19 then turn_up
        when 20 then turn_right_90
        when 21 then turn_left_90
        when 22 then turn_180
        when 23 then turn_right_or_left_90
        when 24 then turn_random
        when 25 then turn_toward_player
        when 26 then turn_away_from_player
        end
        @move_route_index += 1
        (moving? || jumping?) ? return : next
      end
      if command.code >= 27
        case command.code
        when 27
          $game_switches[command.parameters[0]] = true
          $game_map.need_refresh = true
        when 28
          $game_switches[command.parameters[0]] = false
          $game_map.need_refresh = true
        when 29 then @move_speed = command.parameters[0]
        when 30 then @move_frequency = command.parameters[0]
        when 31 then @walk_anime = true
        when 32 then @walk_anime = false
        when 33 then @step_anime = true
        when 34 then @step_anime = false
        when 35 then @direction_fix = true
        when 36 then @direction_fix = false
        when 37 then @through = true
        when 38 then @through = false
        when 39 then @always_on_top = true
        when 40 then @always_on_top = false
        when 41
          @tile_id = 0
          @character_name = command.parameters[0]
          @character_hue = command.parameters[1]
          @original_direction = @direction = command.parameters[2]
          @original_pattern = @pattern = command.parameters[3]
        when 42 then @opacity = command.parameters[0]
        when 43 then @blend_type = command.parameters[0]
        when 44 then $game_system.se_play(command.parameters[0])
        when 45 then result = eval(command.parameters[0])
        end
        @move_route_index += 1
      end
    end
  end
  
  def set_graphic(character_name)
    @character_name = character_name
  end
  
end
