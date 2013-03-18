#==============================================================================
# Game_Map
#==============================================================================

#EX_X = 10
#EX_Y = 7
#EX_X = 20
#EX_Y = 14
EX_X = 11
EX_Y = 8

class Game_Map
  
  attr_accessor :tileset_name
  attr_accessor :autotile_names
  attr_accessor :panorama_name
  attr_accessor :panorama_hue
  attr_accessor :fog_name
  attr_accessor :fog_hue
  attr_accessor :fog_opacity
  attr_accessor :fog_blend_type
  attr_accessor :fog_zoom
  attr_accessor :fog_sx
  attr_accessor :fog_sy
  attr_accessor :battleback_name
  attr_accessor :display_x
  attr_accessor :display_y
  attr_accessor :need_refresh
  attr_reader   :passages
  attr_reader   :priorities
  attr_reader   :terrain_tags
  attr_reader   :events
  attr_reader   :fog_ox
  attr_reader   :fog_oy
  attr_reader   :fog_tone
  attr_reader   :map_id
  attr_reader   :virtual_passability
  
  def initialize
    @map_id = @display_x = @display_y = 0
  end
  
  def pass(x, y)
    @pass[[x, y]] = [] if @pass[[x, y]] == nil
    return @pass[[x, y]]
  end
  
  def setup(map_id)
    @map_id = map_id
    @map = load_data(sprintf('Data/Map%03d.rxdata', @map_id))
    tileset = $data_tilesets[@map.tileset_id]
    @tileset_name = tileset.tileset_name
    @autotile_names = tileset.autotile_names
    @panorama_name = tileset.panorama_name
    @panorama_hue = tileset.panorama_hue
    @fog_name = tileset.fog_name
    @fog_hue = tileset.fog_hue
    @fog_opacity = tileset.fog_opacity
    @fog_blend_type = tileset.fog_blend_type
    @fog_zoom = tileset.fog_zoom
    @fog_sx = tileset.fog_sx
    @fog_sy = tileset.fog_sy
    @battleback_name = tileset.battleback_name
    @passages = tileset.passages
    @priorities = tileset.priorities
    @terrain_tags = tileset.terrain_tags
    @display_x = @display_y = 0
    @need_refresh = false
    @events = {}
    @pass = {}
    @map.events.each_key {|i| @events[i] = Game_Event.new(@map_id, @map.events[i])}
    @common_events = {}
    (1...$data_common_events.size).each {|i| @common_events[i] = Game_CommonEvent.new(i)}
    @fog_ox = @fog_oy = 0
    @fog_tone, @fog_tone_target = Tone.new(0, 0, 0, 0), Tone.new(0, 0, 0, 0)
    @fog_tone_duration = @fog_opacity_duration = @fog_opacity_target = 0
    @scroll_direction, @scroll_rest, @scroll_speed = 2, 0, 4
    set_passability
    modify_map
  end
  
  def set_passability
    @virtual_passability = load_data('Data/MapData.cpx')[0][map_id]
  end
  
  def update_event(x, y, event)
    return unless event.is_a?(Game_Event)
    self.pass(x, y).delete(event)
    self.pass(event.x, event.y).push(event)
  end
  
  def modify_map
    return if @map_id != 28 && @map_id != 300
    if $game_temp.player_new_x == nil
      $game_temp.player_new_x = $data_system.start_x
    end
    if $game_temp.player_new_y == nil
      $game_temp.player_new_y = $data_system.start_y
    end
    minx = maxx = ox = $game_temp.player_new_x
    miny = maxy = oy = $game_temp.player_new_y
    unless tile_passable?(ox, oy, 2) || tile_passable?(ox, oy, 4) ||
        tile_passable?(ox, oy, 6) || tile_passable?(ox, oy, 8)
      return
    end
    if CP::Cache.world_map_data[[ox, oy, @map_id]] == nil
      check_table = Table.new(@map.width, @map.height)
      check_table[ox, oy] = 1
      pending = [[ox, oy]]
      while pending.size > 0
        x, y = pending.shift
        if check_table[x, y+1] == 0 && tile_passable?(x, y, 2)
          pending.push([x, y+1])
          maxy = y+1 if maxy < y+1
          check_table[x, y+1] = 1
        end
        if check_table[x-1, y] == 0 && tile_passable?(x, y, 4)
          pending.push([x-1, y])
          minx = x-1 if minx > x-1
          check_table[x-1, y] = 1
        end
        if check_table[x+1, y] == 0 && tile_passable?(x, y, 6)
          pending.push([x+1, y])
          maxx = x+1 if maxx < x+1
          check_table[x+1, y] = 1
        end
        if check_table[x, y-1] == 0 && tile_passable?(x, y, 8)
          pending.push([x, y-1])
          miny = y-1 if miny > y-1
          check_table[x, y-1] = 1
        end
      end
      minx -= EX_X - 1
      minx = 0 if minx < 0
      w = maxx - minx + EX_X
      width = @map.width - minx
      w = width if w > width
      miny -= EX_Y - 1
      miny = 0 if miny < 0
      h = maxy - miny + EX_Y
      height = @map.height - miny
      h = height if h > height
      CP::Cache.world_map_data[[ox, oy, @map_id]] = [minx, miny, w, h]
    else
      minx, miny, w, h = CP::Cache.world_map_data[[ox, oy, @map_id]]
    end
    @map.width, @map.height = w, h
    if CP::Cache.compressed_map[[minx, miny, w, h, @map_id]] == nil
      pass, map_data = @virtual_passability, @map.data
      @virtual_passability, @map.data = Table.new(w, h), Table.new(w, h, 3)
      (0...h).each {|y| (0...w).each {|x|
          @virtual_passability[x, y] = pass[x+minx, y+miny]
          (0..2).each {|i| @map.data[x, y, i] = map_data[x+minx, y+miny, i]}}}
      CP::Cache.compressed_map[[minx, miny, w, h, @map_id]] =
          [@map.data, @virtual_passability]
    else
      @map.data, @virtual_passability =
          CP::Cache.compressed_map[[minx, miny, w, h, @map_id]]
    end
    $game_variables[113], $game_variables[114] = minx, miny
    @events.each_value {|event|
        if self.valid?(event.x - minx, event.y - miny)
          event.moveto(event.x - minx, event.y - miny)
        elsif event.trigger == 3 || event.trigger == 4
          event.moveto(0, 0)
        else
          @events.delete(event.id)
        end}
    $game_temp.player_new_x -= minx
    $game_temp.player_new_y -= miny
  end
  
  def width
    return @map.width
  end
  
  def height
    return @map.height
  end
  
  def encounter_list
    return @map.encounter_list
  end
  
  def encounter_step
    return @map.encounter_step
  end
  
  def data
    return @map.data
  end
  
  def autoplay
    return if $game_switches[354]
    $game_system.bgm_play(@map.bgm) if @map.autoplay_bgm
    $game_system.bgs_play(@map.bgs) if @map.autoplay_bgs
  end
  
  def refresh
    if @map_id > 0
      @events.values.each {|event| event.refresh}
      @common_events.values.each{|common_event| common_event.refresh}
    end
    @need_refresh = false
  end
  
  def scroll_down(distance)
    @display_y = @display_y + distance
    height = (self.height - 15) * 128
    @display_y = height if @display_y > height
  end
  
  def scroll_left(distance)
    @display_x = @display_x - distance
    @display_x = 0 if @display_x < 0
  end
  
  def scroll_right(distance)
    @display_x = @display_x + distance
    width = (self.width - 20) * 128
    @display_x = width if @display_x > width
  end
  
  def scroll_up(distance)
    @display_y = @display_y - distance
    @display_y = 0 if @display_y < 0
  end
  
  def valid?(x, y)
    return (x >= 0 && x < width && y >= 0 && y < height)
  end
  
  def event_passable?(x, y, d, self_event = nil)
    bit = (1 << (d / 2 - 1)) & 0x0f
    (self.pass(x, y) - [self_event]).each {|event|
        if event.tile_id >= 0 && !event.through
          if @passages[event.tile_id] & bit != 0
            return false
          elsif @passages[event.tile_id] & 0x0f == 0x0f
            return false
          elsif @priorities[event.tile_id] == 0
            return true
          end
        end}
    return nil
  end
      
  def passable?(x, y, d, self_event = nil)
    return false unless valid?(x, y)
    bit = (1 << (d / 2 - 1)) & 0x0F
    result = event_passable?(x, y, d, self_event)
    return result if result != nil
    return tile_passable?(x, y, d)
  end
  
  def tile_passable?(x, y, d)
    return true if d == 0
    bit = (1 << (d / 2 - 1)) & 0x0F
    return ($game_map.virtual_passability[x, y] & bit != 0x00)
  end
  
  def bush?(x, y)
    if @map_id != 0
      CP::Cache::MapLayers.each {|i|
          if data[x, y, i] == nil
            return false
          elsif @passages[data[x, y, i]] & 0x40 == 0x40
            return true
          end}
    end
    return false
  end
  
  def counter?(x, y)
    if @map_id != 0
      CP::Cache::MapLayers.each {|i|
          if data[x, y, i] == nil
            return false
          elsif @passages[data[x, y, i]] & 0x80 == 0x80
            return true
          end}
    end
    return false
  end
  
  def terrain_tag(x, y)
    if @map_id != 0
      CP::Cache::MapLayers.each {|i|
          if data[x, y, i] == nil
            return 0
          elsif @terrain_tags[data[x, y, i]] > 0
            return @terrain_tags[data[x, y, i]]
          end}
    end
    return 0
  end
  
  def check_event(x, y)
    return (@pass[[x, y]].size > 0 ? @pass[[x, y]] : nil)
  end
  
  def start_scroll(direction, distance, speed)
    @scroll_direction = direction
    @scroll_rest = distance * 128
    @scroll_speed = speed
  end
  
  def scrolling?
    return @scroll_rest > 0
  end
  
  def start_fog_tone_change(tone, duration)
    @fog_tone_target = tone.clone
    @fog_tone_duration = duration
    @fog_tone = @fog_tone_target.clone if @fog_tone_duration == 0
  end
  
  def start_fog_opacity_change(opacity, duration)
    @fog_opacity_target = opacity * 1.0
    @fog_opacity_duration = duration
    @fog_opacity = @fog_opacity_target if @fog_opacity_duration == 0
  end
  
  def update
    refresh if $game_map.need_refresh
    if @scroll_rest > 0
      distance = 2 ** @scroll_speed
      case @scroll_direction
      when 2 then scroll_down(distance)
      when 4 then scroll_left(distance)
      when 6 then scroll_right(distance)
      when 8 then scroll_up(distance)
      end
      @scroll_rest -= distance
    end
    @events.each_value {|event| event.update}
    @common_events.each_value {|common_event| common_event.update}
    @fog_ox -= @fog_sx / 8.0
    @fog_oy -= @fog_sy / 8.0
    if @fog_tone_duration >= 1
      d = @fog_tone_duration
      target = @fog_tone_target
      @fog_tone.red = (@fog_tone.red * (d - 1) + target.red) / d
      @fog_tone.green = (@fog_tone.green * (d - 1) + target.green) / d
      @fog_tone.blue = (@fog_tone.blue * (d - 1) + target.blue) / d
      @fog_tone.gray = (@fog_tone.gray * (d - 1) + target.gray) / d
      @fog_tone_duration -= 1
    end
    if @fog_opacity_duration >= 1
      d = @fog_opacity_duration
      @fog_opacity = (@fog_opacity * (d - 1) + @fog_opacity_target) / d
      @fog_opacity_duration -= 1
    end
  end
  
end
