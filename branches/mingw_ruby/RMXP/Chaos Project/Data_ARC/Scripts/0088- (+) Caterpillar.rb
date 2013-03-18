#==============================================================================
# Caterpillar by Blizzard
# Version: 2.0
# Date: 7.3.2007
# Date v1.01b: 7.3.2007
# Date v2.0: 7.8.2007
#==============================================================================

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# actor IDs where the actor is animated even when not walking
ANIMATED_IDS = [2]

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#==============================================================================
# Game_Character
#==============================================================================
    
class Game_Character
  
  alias passable_caterpillar_later? passable?
  def passable?(x, y, d)
    result = passable_caterpillar_later?(x, y, d)
    return result if self.is_a?(Game_Player) || self.is_a?(Game_Member)
    new_x = x + (d == 6 ? 1 : d == 4 ? -1 : 0)
    new_y = y + (d == 2 ? 1 : d == 8 ? -1 : 0)
    unless @through
      $game_player.members.each {|member|
          if member.character_name != '' && member.x == new_x && member.y == new_y
            return false
          end}
    end
    return result 
  end
  
end

#==============================================================================
# Game_Player
#==============================================================================
    
class Game_Player < Game_Character
  
  attr_accessor :members
  attr_accessor :move_speed
  
  alias init_caterpillar_later initialize
  def initialize
    init_caterpillar_later
    @members = []
    (1..3).each {|i| @members.push(Game_Member.new(i))}
  end
  
  alias straighten_caterpillar_later straighten
  def straighten
    straighten_caterpillar_later
    @members.each {|member| member.straighten}
  end
  
  alias refresh_caterpillar_later refresh
  def refresh
    refresh_caterpillar_later
    @members.each {|member| member.refresh} if @members != nil
  end
  
  alias upd_caterpillar_later update
  def update
    upd_caterpillar_later
    @members.each {|member| member.update}
    @step_anime = true if ANIMATED_IDS.include?($game_party.actors[0].id)
  end
  
  def update_buffer(next_move)
    if next_move == nil
      @members.each {|member| member.buffer = [] unless member.lock}
    else 
      @members.each {|member| member.update_buffer(
          next_move == 'reset' ? nil : next_move)}
    end
  end
  
  alias move_down_caterpillar_later move_down
  def move_down(turn_enabled = true)
    update_buffer(2) if passable?(@x, @y, 2)
    move_down_caterpillar_later
  end
  
  alias move_left_caterpillar_later move_left
  def move_left(turn_enabled = true)
    update_buffer(4) if passable?(@x, @y, 4)
    move_left_caterpillar_later
  end
  
  alias move_right_caterpillar_later move_right
  def move_right(turn_enabled = true)
    update_buffer(6) if passable?(@x, @y, 6)
    move_right_caterpillar_later
  end
  
  alias move_up_caterpillar_later move_up
  def move_up(turn_enabled = true)
    update_buffer(8) if passable?(@x, @y, 8)
    move_up_caterpillar_later
  end
  
  alias move_lower_left_caterpillar_later move_lower_left
  def move_lower_left
    if (passable?(@x, @y, 2) && passable?(@x, @y + 1, 4)) ||
       (passable?(@x, @y, 4) && passable?(@x - 1, @y, 2))
      update_buffer(1)
    end
    move_lower_left_caterpillar_later
  end
  
  alias move_lower_right_caterpillar_later move_lower_right
  def move_lower_right
    if (passable?(@x, @y, 2) && passable?(@x, @y + 1, 6)) ||
       (passable?(@x, @y, 6) && passable?(@x + 1, @y, 2))
      update_buffer(3)
    end
    move_lower_right_caterpillar_later
  end
  
  alias move_upper_left_caterpillar_later move_upper_left
  def move_upper_left
    if (passable?(@x, @y, 8) && passable?(@x, @y - 1, 4)) ||
       (passable?(@x, @y, 4) && passable?(@x - 1, @y, 8))
      update_buffer(7)
    end
    move_upper_left_caterpillar_later
  end
  
  alias move_upper_right_caterpillar_later move_upper_right
  def move_upper_right
    if (passable?(@x, @y, 8) && passable?(@x, @y - 1, 6)) ||
       (passable?(@x, @y, 6) && passable?(@x + 1, @y, 8))
      update_buffer(9)
    end
    move_upper_right_caterpillar_later
  end
  
  alias jump_caterpillar_later jump
  def jump(x_plus, y_plus)
    if (x_plus != 0 || y_plus != 0) && passable?(@x + x_plus, @y + y_plus, 0)
      update_buffer([x_plus, y_plus])
    end
    jump_caterpillar_later(x_plus, y_plus)
  end
  
  alias moveto_caterpillar moveto
  def moveto(x, y)
    moveto_caterpillar(x, y)
    update_buffer(nil)
    @members.each {|member| member.moveto(x, y)}
    case $game_player.direction
    when 2 then turn_down
    when 4 then turn_left
    when 6 then turn_right
    when 8 then turn_up
    end
  end
  
end
  
#==============================================================================
# Game_Member
#==============================================================================

class Game_Member < Game_Character
  
  attr_accessor :buffer
  attr_accessor :lock
  
  def initialize(index)
    super()
    @index, @force_movement, @buffer, @through = index, 0, [], true
  end
  
  def moveto(x, y)
    super(x, y) unless @lock
  end
  
  def name
    if $game_party.actors[@index] == nil
      if $game_party.actors[@index - 1] != nil && $game_switches[366]
        return 'Luvian King'
      end
      return ''
    end
    return $game_party.actors[@index].name
  end
  
  def refresh
    return if $game_switches[194]
    if $game_party.actors[@index] == nil
      if $game_party.actors[@index - 1] != nil && $game_switches[366]
        @character_name = '042-King01'
      else
        @character_name = ''
      end
      @character_hue = 0
      return
    end
    @character_name = $game_party.actors[@index].character_name
    @character_hue = $game_party.actors[@index].character_hue
    @opacity, @blend_type = 255, 0
  end
  
  def update
    refresh
    unless $game_switches[167]
      @transparent = $game_player.transparent
      @blend_type = $game_player.blend_type
      @opacity = $game_player.opacity
    end
    @move_speed = $game_player.move_speed
    if !moving? && (@buffer.size > @index || @force_movement > 0)
      if @buffer.size > 0
        move = @buffer.shift
        if move.is_a?(Array)
          jump(move[0], move[1])
        else
          case move
          when 1 then move_lower_left
          when 2 then move_down(true)
          when 3 then move_lower_right
          when 4 then move_left(true)
          when 6 then move_right(true)
          when 7 then move_upper_left
          when 8 then move_up(true)
          when 9 then move_upper_right
          end
        end
        @force_movement -= 1 if @force_movement > 0
      end
    end
    super
    @step_anime = (ANIMATED_IDS.include?($game_party.actors[@index].id))
  end
  
  def update_buffer(next_move)
    if next_move == nil
      @force_movement = @buffer.size
    else
      @buffer.push(next_move)
      @force_movement = @buffer.size if next_move.is_a?(Array)
    end
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
              $game_variables[149] = @index
              event.catch
              return true
            end}
      end
    end
    return false
  end
  
  def screen_z(height = 0)
    return (super + 8 - @index)
  end
  
end

#==============================================================================
# Spriteset_Map
#==============================================================================

class Spriteset_Map
  
  alias init_blizzabs_later initialize
  def initialize
    init_blizzabs_later
    $game_player.members.each {|member|
        sprite = Sprite_Character.new(@viewport1, member)
        sprite.update
        @character_sprites.push(sprite)}
  end
  
end
