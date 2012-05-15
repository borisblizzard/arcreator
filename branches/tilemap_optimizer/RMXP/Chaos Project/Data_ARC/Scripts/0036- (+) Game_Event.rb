#==============================================================================
# Game_Event
#==============================================================================

class Game_Event < Game_Character
  
  attr_reader :trigger
  attr_reader :list
  attr_reader :starting
  attr_reader :message
  attr_reader :event
  attr_reader :lowest
  attr_reader :tracer
  
  def initialize(map_id, event)
    @lowest = (event.name[0, 5] == 'TileY' || event.name[1, 5] == 'TileY' || 
        event.name[0, 5] == 'DoorY')
    @tracer = (event.name[0, 6] == 'Tracer')
    @mirror_offset = (event.name[0, 4] == 'Door')
    super()
    @map_id, @event, @id, @erased, @starting, @through =
        map_id, event, event.id, false, false, true
    moveto(@event.x, @event.y)
    refresh
    @no_ceal = (event.name.clone.gsub!('\\eal') {''} != nil)
    event.name.gsub!('\\eal') {''}
    event.name = 'EV' + sprintf('%03d', @id) if event.name == ''
    @move_speed -= 1 if @tracer && $game_system.gold_rate > 0.5
  end
  
  def screen_z(height = 0)
    return (@lowest ? 1 : super(height))
  end
  
  def name
    return (@name == nil ? @event.name : @name)
  end
  
  def name=(val)
    @name = val
  end
  
  def clear_starting
    @starting = false
  end
  
  def over_trigger?
    return ((@character_name == '' || @through) && $game_map.passable?(@x, @y, 0))
  end
  
  def start
    @starting = true if @list.size > 1
  end
  
  def erase
    @erased = true
    refresh
  end
  
  def refresh
    new_page = nil
    unless @erased
      @event.pages.reverse.each {|page|
          c = page.condition
          next if c.switch1_valid && !$game_switches[c.switch1_id]
          next if c.switch2_valid && !$game_switches[c.switch2_id]
          next if c.variable_valid && $game_variables[c.variable_id] < c.variable_value
          if c.self_switch_valid
            key = [@map_id, @event.id, c.self_switch_ch]
            next if $game_self_switches[key] != true
          end
          new_page = page
          break}
    end
    return if new_page == @page
    @page = new_page
    clear_starting
    if @page == nil
      @character_name = ''
      @tile_id = @character_hue = @move_type = 0
      @through = true
      @trigger = @list = @interpreter = nil
      return
    end
    if @event.name[0, 5] == 'Bunny' && $game_switches[403]
      @lowest, @loop_id = true, 166
    end
    @tile_id = @page.graphic.tile_id
    @character_name = @page.graphic.character_name
    @character_hue = @page.graphic.character_hue
    if @original_direction != @page.graphic.direction
      @original_direction = @direction = @page.graphic.direction
      @prelock_direction = 0
    end
    if @original_pattern != @page.graphic.pattern
      @original_pattern = @pattern = @page.graphic.pattern
    end
    @opacity, @blend_type = @page.graphic.opacity, @page.graphic.blend_type
    @move_type, @move_speed = @page.move_type, @page.move_speed
    @move_frequency, @move_route = @page.move_frequency, @page.move_route
    @move_route_index, @move_route_forcing = 0, false
    @walk_anime, @step_anime = @page.walk_anime, @page.step_anime
    @direction_fix, @always_on_top = @page.direction_fix, @page.always_on_top
    @through, @trigger = @page.through, @page.trigger
    @list = @page.list
    @interpreter = (@trigger == 4 ? Interpreter.new : nil)
    check_event_trigger_auto
  end
  
  def check_event_trigger_touch(x, y)
    if @tracer && !$game_switches[328]
      actors = [$game_player] + $game_player.members
      actors.each_index {|i|
          if x == actors[i].x && y == actors[i].y
            last_direction_fix, @direction_fix = @direction_fix, false
            turn_toward(actors[i])
            @direction_fix = last_direction_fix
            $game_variables[149] = i
            catch
          end}
    elsif @trigger == 2 && @x == $game_player.x && @y == $game_player.y
      start if !jumping? && !over_trigger?
    end
  end
  
  def check_event_trigger_auto
    if @trigger == 3 || @trigger == 2 && @x == $game_player.x &&
        @y == $game_player.y && !jumping? && over_trigger?
      start
    end
  end
  
  def update
    super
    check_event_trigger_auto
    if @interpreter != nil
      @interpreter.setup(@list, @event.id) unless @interpreter.running?
      @interpreter.update
    end
  end
  
  def passable?(x, y, d)
    nx = x + (d == 6 ? 1 : d == 4 ? -1 : 0)
    ny = y + (d == 2 ? 1 : d == 8 ? -1 : 0)
    return @through if $game_map.terrain_tag(nx, ny) == CP::Cache::NoEventTag
    return super
  end
  
end
