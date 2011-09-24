#==============================================================================
# Game_Player
#==============================================================================

class Game_Player < Game_Character
  
  CENTER_X = (320 - 16) * 4
  CENTER_Y = (240 - 16) * 4
  
  attr_reader :encounter_count
  
  def passable?(x, y, d)
    new_x = x + (d == 6 ? 1 : d == 4 ? -1 : 0)
    new_y = y + (d == 2 ? 1 : d == 8 ? -1 : 0)
    return false unless $game_map.valid?(new_x, new_y)
    return super
  end
  
  def name
    return $game_party.actors[0].name
  end
  
  def center(x, y)
    return if $game_switches[401]
    $game_map.display_x = x * 128 - CENTER_X
    max_x = ($game_map.width - 20) * 128
    if $game_map.display_x < 0
      $game_map.display_x = 0
    elsif $game_map.display_x > max_x
      $game_map.display_x = max_x
    end
    $game_map.display_y = y * 128 - CENTER_Y
    max_y = ($game_map.height - 15) * 128
    if $game_map.display_y < 0
      $game_map.display_y = 0
    elsif $game_map.display_y > max_y
      $game_map.display_y = max_y
    end
  end
  
  def moveto(x, y)
    super
    center(x, y)
    make_encounter_count
  end
  
  def move_caterpillar(x, y)
    xs, ys = x - $game_player.x, y - $game_player.y
    $game_player.members.each {|m| m.lock = true}
    $game_player.moveto(x, y)
    $game_player.members.each {|m|
        m.lock = nil
        m.moveto(m.x + xs, m.y + ys)}
    center(x, y)
    make_encounter_count
  end
  
  def increase_steps
    super
    unless @move_route_forcing
      $game_party.increase_steps
      $game_party.check_map_slip_damage if $game_party.steps % 2 == 0
    end
  end
  
  def make_encounter_count
    if $game_map.map_id != 0
      n = $game_map.encounter_step
      @encounter_count = rand(n - 5) + rand(n - 5) + 10
    end
  end
  
  def refresh
    return if $game_switches[194]
    if $game_party.actors.size == 0
      @character_name, @character_hue = '', 0
      return
    end
    @character_name = $game_party.actors[0].character_name
    @character_hue = $game_party.actors[0].character_hue
    @opacity, @blend_type = 255, 0
  end
  
  def check_event_trigger_here(triggers)
    return false if $game_system.map_interpreter.running? || $game_switches[167]
    result = false
    $game_map.pass(@x, @y).each {|event|
        if !event.jumping? && triggers.include?(event.trigger) &&
            event.over_trigger?
          event.start
          result = true
        end}
    return result
  end
  
  def check_event_trigger_there(triggers)
    return false if $game_system.map_interpreter.running? || $game_switches[167]
    result = false
    new_x = @x + (@direction == 6 ? 1 : @direction == 4 ? -1 : 0)
    new_y = @y + (@direction == 2 ? 1 : @direction == 8 ? -1 : 0)
    $game_map.pass(new_x, new_y).each {|event|
        if !event.jumping? && triggers.include?(event.trigger) &&
            !event.over_trigger?
          event.start
          result = true
        end}
    if !result && $game_map.counter?(new_x, new_y)
      new_x += (@direction == 6 ? 1 : @direction == 4 ? -1 : 0)
      new_y += (@direction == 2 ? 1 : @direction == 8 ? -1 : 0)
      $game_map.pass(new_x, new_y).each {|event|
          if !event.jumping? && triggers.include?(event.trigger) &&
              !event.over_trigger?
            event.start
            result = true
          end}
    end
    return result
  end
  
  def check_event_trigger_touch(x, y)
    if !$game_switches[328]
      tracers = $game_map.pass(x, y).find_all {|e| e.is_a?(Game_Event) && e.tracer}
      if tracers.size > 0
        tracers.each {|event|
            if x == event.x && y == event.y
              last_direction_fix, event.direction_fix = event.direction_fix, false
              event.turn_toward(self)
              event.direction_fix = last_direction_fix
              $game_variables[149] = 0
              event.catch
              return true
            end}
      end
    end
    return false if $game_system.map_interpreter.running? || $game_switches[167]
    result = false
    $game_map.pass(x, y).each {|event|
        if !event.jumping? && (event.trigger == 1 || event.trigger == 2) &&
            !event.over_trigger?
          event.start
          result = true
        end}
    return result
  end
  
  def update
    last_moving = moving?
    if @members != nil
      @members.each {|member| member.always_on_top = @always_on_top}
    end
    unless moving? || @move_route_forcing ||
           $game_system.map_interpreter.running? ||
           $game_temp.message_window_showing &&
           $game_system.message_walking
      case Input.dir4
      when 2 then move_down
      when 4 then move_left
      when 6 then move_right
      when 8 then move_up
      end
    end
    last_real_x, last_real_y = @real_x, @real_y
    super
    if !$game_switches[274]
      if @real_y > last_real_y && @real_y - $game_map.display_y > CENTER_Y
        $game_map.scroll_down(@real_y - last_real_y)
      end
      if @real_x < last_real_x && @real_x - $game_map.display_x < CENTER_X
        $game_map.scroll_left(last_real_x - @real_x)
      end
      if @real_x > last_real_x && @real_x - $game_map.display_x > CENTER_X
        $game_map.scroll_right(@real_x - last_real_x)
      end
      if @real_y < last_real_y && @real_y - $game_map.display_y < CENTER_Y
        $game_map.scroll_up(last_real_y - @real_y)
      end
    end
    unless moving?
      if last_moving
        result = check_event_trigger_here([1, 2])
        update_encounter_count(result)
      end
      if Input.trigger?($controls.confirm)
        check_event_trigger_here([0])
        check_event_trigger_there([0, 1])
      end
    end
  end
    
  def update_encounter_count(result)
    if !result && !$game_system.encounter_disabled && @encounter_count > 0
      @encounter_count -= 1
    end
  end
  
  def screen_z(height = 0)
    return super(height) + 8
  end
  
end
