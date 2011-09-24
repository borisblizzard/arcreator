#==============================================================================
# Game_Player
#==============================================================================

class Game_Player
  
  alias upd_guards update
  def update
    if $game_switches[329]
      if Input.press?($controls.leximus)
        $game_switches[330], @move_speed = true, 3
      else
        $game_switches[330], @move_speed = false, 4
      end
    end
    upd_guards
  end
  
end

#==============================================================================
# Game_Event
#==============================================================================

class Game_Event
  
  alias upd_guards update
  def update
    upd_guards
    if !$game_switches[329] || !@tracer ||
        $game_system.map_interpreter.running? ||
        $game_temp.message_window_showing
      return
    end
    return if $game_switches[328]
    perception = ([$game_player] + $game_player.members).find_all {|c|
        Math.hypot(c.x-@x, c.y-@y) < 4.3}
    return if perception.size == 0
    unless $game_switches[330]
      heard = perception.find_all {|c| c.moving?}
      if heard.size > 0
        last_direction_fix, @direction_fix = @direction_fix, false
        turn_toward(heard[0])
        @direction_fix = last_direction_fix
      end
    end
    perception = perception.find_all {|c|
        self.can_see_char?(c.x, c.y) && !self.wall?(c.x, c.y)}
    if perception.size > 0
      if perception[0] == $game_player
        $game_variables[149] = 0
      else
        $game_variables[149] = $game_player.members.index(perception[0]) + 1
      end
      catch
    end
  end
  
  def catch
    $game_temp.animator = @event.name
    $game_switches[328] = $game_map.need_refresh = true
  end
  
  def direction_fix
    return (@direction_fix || $game_switches[328])
  end
  
  def wall?(x, y)
    dx, dy = x-@x, y-@y
    if dx != 0 && dx.abs > dy.abs
      return ((0..dx.abs).any? {|i| CP::Cache::WallTag ==
          $game_map.terrain_tag(@x+dx.sgn*i, @y+(i.to_f*dy/dx).round)})
    elsif dy != 0 && dy.abs > dx.abs
      return ((0..dy.abs).any? {|i| CP::Cache::WallTag ==
          $game_map.terrain_tag(@x+(i.to_f*dx/dy).round, @y+dy.sgn*i)})
    elsif dy.abs == dx.abs
      return ((0..dy.abs).any? {|i| CP::Cache::WallTag ==
          $game_map.terrain_tag(@x+dx.sgn*i, @y+dy.sgn*i)})
    end
    return false
  end
  
  def can_see_char?(x, y)
    dx, dy = x-@x, y-@y
    return case @direction
    when 2 then (dy >= 0 && dx.abs <= dy.abs)
    when 4 then (dx <= 0 && dx.abs >= dy.abs)
    when 6 then (dx >= 0 && dx.abs >= dy.abs)
    when 8 then (dy <= 0 && dx.abs <= dy.abs)
    else
      false
    end
  end
    
end
