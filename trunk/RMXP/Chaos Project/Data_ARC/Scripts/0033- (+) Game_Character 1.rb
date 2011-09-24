#==============================================================================
# Game_Character (1)
#==============================================================================

class Game_Character
  
  attr_reader   :id
  attr_reader   :x
  attr_reader   :y
  attr_reader   :real_x
  attr_reader   :real_y
  attr_reader   :tile_id
  attr_reader   :character_name
  attr_accessor :character_hue
  attr_reader   :opacity
  attr_reader   :blend_type
  attr_reader   :pattern
  attr_reader   :move_route_forcing
  attr_reader   :through
  attr_reader   :mirror_offset
  attr_accessor :direction
  attr_accessor :animation_id
  attr_accessor :transparent
  attr_accessor :loop_id
  attr_accessor :always_on_top
  attr_accessor :direction_fix
  
  def initialize
    @id = @x = @y = @real_x = @real_y = @tile_id = 0
    @character_name, @character_hue = '', 0
    @opacity, @blend_type, @direction, @pattern = 255, 0, 2, 0
    @move_route_forcing = @through = @transparent = false
    @animation_id, @original_direction, @original_pattern = 0, 2, 0
    @move_type, @move_speed, @move_frequency, @move_route = 0, 4, 6, nil
    @move_route_index, @original_move_route = 0, nil
    @original_move_route_index = 0
    @walk_anime = true
    @step_anime = @direction_fix = @always_on_top = @locked = false
    @anime_count = @stop_count = @jump_count = @jump_peak = @wait_count =
    @prelock_direction = @loop_id = 0
  end
  
  def moving?
    return (@real_x != @x * 128 || @real_y != @y * 128)
  end
  
  def jumping?
    return (@jump_count > 0)
  end
  
  def straighten
    @pattern = 0 if @walk_anime || @step_anime
    @anime_count = @prelock_direction = 0
  end
  
  def force_move_route(move_route)
    if @original_move_route == nil
      @original_move_route = @move_route
      @original_move_route_index = @move_route_index
    end
    @move_route = move_route
    @move_route_forcing = true
    @move_route_index = @prelock_direction = @wait_count = 0
    move_type_custom
  end
  
  def passable?(x, y, d)
    new_x = x + (d == 6 ? 1 : d == 4 ? -1 : 0)
    new_y = y + (d == 2 ? 1 : d == 8 ? -1 : 0)
    return false unless $game_map.valid?(new_x, new_y)
    return true if @through
    return false if $game_switches[328]
    return false unless $game_map.passable?(x, y, d, self)
    result = $game_map.event_passable?(new_x, new_y, 10-d)
    return false if result == false
    $game_map.pass(new_x, new_y).each {|event|
        unless event.through
          return false if self != $game_player || event.character_name != ''
        end}
    if $game_player.x == new_x && $game_player.y == new_y
      return false if !$game_player.through && @character_name != ''
    end
    return true
  end
  
  def lock
    return if @locked
    @prelock_direction = @direction
    turn_toward_player
    @locked = true
  end
  
  def lock?
    return @locked
  end
  
  def unlock
    return unless @locked
    @locked = false
    @direction = @prelock_direction if !@direction_fix && @prelock_direction != 0
  end
  
  def moveto(x, y)
    old_x, old_y = @x, @y
    @x = x % $game_map.width
    @y = y % $game_map.height
    @real_x = @x * 128
    @real_y = @y * 128
    @prelock_direction = 0
    $game_map.update_event(old_x, old_y, self)
  end
  
  def screen_x
    return (@real_x - $game_map.display_x + 3) / 4 + 16
  end
  
  def screen_y
    y = (@real_y - $game_map.display_y + 3) / 4 + 32
    n = @jump_count - @jump_peak
    return y - (@jump_peak * @jump_peak - n * n) / 2
  end
  
  def screen_z(height = 0)
    z = (@real_y - $game_map.display_y + 3) / 4 + 32
    if @tile_id > 0
      return z+$game_map.priorities[@tile_id]*32+(@always_on_top ? 500 : 0)
    else
      h = (height > 32 ? 31 : (height < 0 ? height : 0))
      return z+h-8+(@always_on_top ? 500 : 0)
    end
  end
  
  def bush_depth
    return 0 if @tile_id > 0 || @always_on_top
    return ((@jump_count == 0 && $game_map.bush?(@x, @y)) ? 12 : 0)
  end
  
  def terrain_tag
    return $game_map.terrain_tag(@x, @y)
  end
  
end
