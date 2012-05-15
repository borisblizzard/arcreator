#==============================================================================
# Game_Character (3)
#==============================================================================

class Game_Character
  
  def move_in_direction(direction)
    case direction
    when 1 then move_lower_left
    when 2 then move_down
    when 3 then move_lower_right
    when 4 then move_left
    when 6 then move_right
    when 7 then move_upper_left
    when 8 then move_up
    when 9 then move_upper_right
    end
  end
  
  def move_down(turn_enabled = true)
    turn_down if turn_enabled
    if passable?(@x, @y, 2)
      turn_down
      @y += 1
      $game_map.update_event(@x, @y-1, self)
      increase_steps
    else
      check_event_trigger_touch(@x, @y+1)
    end
  end
  
  def move_left(turn_enabled = true)
    turn_left if turn_enabled
    if passable?(@x, @y, 4)
      turn_left
      @x -= 1
      $game_map.update_event(@x+1, @y, self)
      increase_steps
    else
      check_event_trigger_touch(@x-1, @y)
    end
  end
  
  def move_right(turn_enabled = true)
    turn_right if turn_enabled
    if passable?(@x, @y, 6)
      turn_right
      @x += 1
      $game_map.update_event(@x-1, @y, self)
      increase_steps
    else
      check_event_trigger_touch(@x+1, @y)
    end
  end
  
  def move_up(turn_enabled = true)
    turn_up if turn_enabled
    if passable?(@x, @y, 8)
      turn_up
      @y -= 1
      $game_map.update_event(@x, @y+1, self)
      increase_steps
    else
      check_event_trigger_touch(@x, @y-1)
    end
  end
  
  def move_lower_left
    unless self.direction_fix
      @direction = (@direction == 6 ? 4 : @direction == 8 ? 2 : @direction)
    end
    if (passable?(@x, @y, 2) && passable?(@x, @y + 1, 4)) ||
        (passable?(@x, @y, 4) && passable?(@x - 1, @y, 2))
      @x -= 1
      @y += 1
      $game_map.update_event(@x+1, @y-1, self)
      increase_steps
    end
  end
  
  def move_lower_right
    unless self.direction_fix
      @direction = (@direction == 4 ? 6 : @direction == 8 ? 2 : @direction)
    end
    if (passable?(@x, @y, 2) && passable?(@x, @y + 1, 6)) ||
        (passable?(@x, @y, 6) && passable?(@x + 1, @y, 2))
      @x += 1
      @y += 1
      $game_map.update_event(@x-1, @y-1, self)
      increase_steps
    end
  end
  
  def move_upper_left
    unless self.direction_fix
      @direction = (@direction == 6 ? 4 : @direction == 2 ? 8 : @direction)
    end
    if (passable?(@x, @y, 8) && passable?(@x, @y - 1, 4)) ||
        (passable?(@x, @y, 4) && passable?(@x - 1, @y, 8))
      @x -= 1
      @y -= 1
      $game_map.update_event(@x+1, @y+1, self)
      increase_steps
    end
  end
  
  def move_upper_right
    unless self.direction_fix
      @direction = (@direction == 4 ? 6 : @direction == 2 ? 8 : @direction)
    end
    if (passable?(@x, @y, 8) && passable?(@x, @y - 1, 6)) ||
        (passable?(@x, @y, 6) && passable?(@x + 1, @y, 8))
      @x += 1
      @y -= 1
      $game_map.update_event(@x-1, @y+1, self)
      increase_steps
    end
  end
  
  def move_random
    case rand(4)
    when 0 then move_down(false)
    when 1 then move_left(false)
    when 2 then move_right(false)
    when 3 then move_up(false)
    end
  end
  
  def move_toward_player
    sx = @x - $game_player.x
    sy = @y - $game_player.y
    return if sx == 0 && sy == 0
    rand(2) == 0 ? sx.abs += 1 : sy.abs += 1 if sx.abs == sy.abs
    if sx.abs > sy.abs
      sx > 0 ? move_left : move_right
      sy > 0 ? move_up : move_down if !moving? && sy != 0
    else
      sy > 0 ? move_up : move_down
      sx > 0 ? move_left : move_right if !moving? && sx != 0
    end
  end
  
  def move_away_from_player
    sx = @x - $game_player.x
    sy = @y - $game_player.y
    return if sx == 0 && sy == 0
    rand(2) == 0 ? sx.abs += 1 : sy.abs += 1 if sx.abs == sy.abs
    if sx.abs > sy.abs
      sx > 0 ? move_right : move_left
      sy > 0 ? move_down : move_up if !moving? && sy != 0
    else
      sy > 0 ? move_down : move_up
      sx > 0 ? move_right : move_left if !moving? && sx != 0
    end
  end
  
  def move_forward
    case @direction
    when 2 then move_down(false)
    when 4 then move_left(false)
    when 6 then move_right(false)
    when 8 then move_up(false)
    end
  end
  
  def move_backward
    last_direction_fix, @direction_fix = @direction_fix, true
    case @direction
    when 2 then move_up(false)
    when 4 then move_right(false)
    when 6 then move_left(false)
    when 8 then move_down(false)
    end
    @direction_fix = last_direction_fix
  end
  
  def jump(x_plus, y_plus)
    if x_plus != 0 || y_plus != 0
      if x_plus.abs > y_plus.abs
        x_plus < 0 ? turn_left : turn_right
      else
        y_plus < 0 ? turn_up : turn_down
      end
    end
    if (x_plus == 0 && y_plus == 0) || passable?(@x + x_plus, @y + y_plus, 0)
      straighten
      @x, @y = @x + x_plus, @y + y_plus
      distance = Math.sqrt(x_plus * x_plus + y_plus * y_plus).round
      @jump_peak = 10 + distance - @move_speed
      @jump_count = @jump_peak * 2
      @stop_count = 0
    end
  end
  
  def turn_down
    @direction, @stop_count = 2, 0 unless self.direction_fix
  end
  
  def turn_left
    @direction, @stop_count = 4, 0 unless self.direction_fix
  end
  
  def turn_right
    @direction, @stop_count = 6, 0 unless self.direction_fix
  end
  
  def turn_up
    @direction, @stop_count = 8, 0 unless self.direction_fix
  end
  
  def turn_right_90
    case @direction
    when 2 then turn_left
    when 4 then turn_up
    when 6 then turn_down
    when 8 then turn_right
    end
  end
  
  def turn_left_90
    case @direction
    when 2 then turn_right
    when 4 then turn_down
    when 6 then turn_up
    when 8 then turn_left
    end
  end
  
  def turn_180
    case @direction
    when 2 then turn_up
    when 4 then turn_right
    when 6 then turn_left
    when 8 then turn_down
    end
  end
  
  def turn_right_or_left_90
    rand(2) == 0 ? turn_right_90 : turn_left_90
  end
  
  def turn_random
    case rand(4)
    when 0 then turn_up
    when 1 then turn_right
    when 2 then turn_left
    when 3 then turn_down
    end
  end
  
  def turn_toward_player
    turn_toward($game_player)
  end
  
  def turn_away_from_player
    turn_away_from($game_player)
  end
  
  def turn_toward(character)
    sx, sy = @x - character.x, @y - character.y
    return if sx == 0 && sy == 0
    if sx.abs > sy.abs
      sx > 0 ? turn_left : turn_right
    else
      sy > 0 ? turn_up : turn_down
    end
  end
  
  def turn_away_from(character)
    sx, sy = @x - character.x, @y - character.y
    return if sx == 0 && sy == 0
    if sx.abs > sy.abs
      sx > 0 ? turn_right : turn_left
    else
      sy > 0 ? turn_down : turn_up
    end
  end
  
end
