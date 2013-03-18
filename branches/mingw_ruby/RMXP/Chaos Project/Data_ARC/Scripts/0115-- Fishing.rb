#==============================================================================
# Game_Party
#==============================================================================

class Game_Party
  
  def check_items
    data = []
    (1...$data_items.size).each {|i|
        if !(CP::Cache::Trade | CP::Cache::Quest).include?(i) && item_number(i) > 0
          data.push($data_items[i]) if $data_items[i].price > 0
        end}
    (1...$data_weapons.size).each {|i|
        if weapon_number(i) > 0 && $data_weapons[i].price > 0
          data.push($data_weapons[i])
        end}
    (1...$data_armors.size).each {|i|
        if armor_number(i) > 0 && $data_armors[i].price > 0
          data.push($data_armors[i])
        end}
    return (data.size == 0)
  end
  
  def test_exerion
    return (weapon_number(53) > 0 || @actors.any? {|actor| actor.weapon_id == 53 ||
        CP::Cache::Lucius.include?(actor.id) && actor.armor1_id == 53})
  end
  
end

#==============================================================================
# Game_Player
#==============================================================================

class Game_Player
  
  attr_accessor :fishing
  attr_accessor :caught_fish
  
  alias init_fishing_later initialize
  def initialize
    init_fishing_later
    @fishing = false
    @caught_fish = [0.0, 0]
  end
  
  alias passable_fishing_later? passable?
  def passable?(x, y, d)
    new_x = x + (d == 6 ? 1 : d == 4 ? -1 : 0)
    new_y = y + (d == 2 ? 1 : d == 8 ? -1 : 0)
    if $game_map.map_id == 290 && $game_switches[31] &&
        $game_map.terrain_tag(new_x, new_y) == 1
      $game_system.se_play($data_system.decision_se)
      @fishing = true
      self.straighten
      return false
    end
    return passable_fishing_later?(x, y, d)
  end

end

#==============================================================================
# Window_FishBar
#==============================================================================

class Window_FishBar < Window_Base
  
  attr_accessor :lost_fish
  attr_reader   :caught_fish
  attr_reader   :got_fish
  attr_reader   :fill
  attr_reader   :rate
  
  def initialize(indicator_window, info_window)
    super(0, 0, 316, 96)
    self.x = 640 - self.width - 16
    self.contents = Bitmap.new(width - 32, height - 32)
    self.contents.font.name = $fontface
    self.contents.font.bold = true if $fontface == 'Papyrus'    
    self.opacity = 0
    get_fish
    @got_fish = @lost_fish = false
    @caught_fish = [0.0, 0, false]
    @fish_length = 0.0
    @fish_pulling = @fish_weight = @fill = @shock = 0
    @rate = 1000
    @sec = Graphics.frame_count / Graphics.frame_rate
    @indicator_window = indicator_window
    @indicator_window.update(1000, self.x, self.width - 36)
    @info_window = info_window
    self.reset
  end
  
  def refresh
    self.contents.clear
    self.contents.gradient_bar_alt3(80, @fill/1000.0, @rate/1000.0)
    @current_fish = $game_player.caught_fish
    text = "Current catch:  #{@current_fish[0]}cm  #{@current_fish[1]}g"
    self.contents.draw_text(0, 32, self.width - 32, 32, text)
  end
  
  def update
    super
    result = false
    if @lost_fish || @caught_fish[2]
      if !@info_window.visible
        @info_window.visible = true
        @info_window.set_fish(@lost_fish, @caught_fish)
        @info_window.refresh
      end
      check = @info_window.update
      if check == 0
        self.reset
        result = true
      elsif check == 1
        $game_player.fishing = false
        self.reset
        result = true
      end
    elsif @got_fish
      if @fish_pulling > 0
        if Input.trigger?($controls.leximus)
          self.rate -= 200 * @fish_power/@rod_power
          self.fill -= 25
          @shock = 2
          $game_system.se_play(RPG::AudioFile.new('032-Switch01', 70, 100))
        else
          self.fill += 10
          if @shock > 0
            @shock -= 1
          $game_system.se_play(RPG::AudioFile.new('032-Switch01', 70, 100))
          else
            self.rate += 5
          end
          if Graphics.frame_count % 2 == 0
          $game_system.se_play(RPG::AudioFile.new('032-Switch01', 70, 100))
          end
        end
        @fish_pulling -= 1
        @fish_pulling = -(rand(17) + 8) if @fish_pulling == 0
      else
        if Input.trigger?($controls.leximus)
          self.rate += 5
          self.fill -= 50
          @shock = 2
          $game_system.se_play(RPG::AudioFile.new('032-Switch01', 70, 100))
        else
          if @shock > 0
            @shock -= 1
            $game_system.se_play(RPG::AudioFile.new('032-Switch01', 70, 100))
          else
            self.rate += 10
          end
        end
        @fish_pulling += 1 if @fish_pulling < 0
        @fish_pulling = rand(17) + 3 if @fish_pulling == 0 && rand(20) == 0
      end
      @indicator_window.update(@fill, self.x + 80, self.width - 116)
      refresh
      lose_fish if @fill == 1000 || @rate == 0
      catch_fish if @fill == 0
    elsif @sec != Graphics.frame_count / Graphics.frame_rate
      @sec = Graphics.frame_count / Graphics.frame_rate
      self.got_fish if rand(100) < 10
    end
    return result
  end
  
  def lose_fish
    @got_fish, @lost_fish = false, true
    @caught_fish = [0.0, 0, false]
  end
  
  def catch_fish
    @got_fish = false
    @caught_fish = [@fish_length, @fish_weight, true]
  end
  
  def reset
    $game_player.caught_fish = [@caught_fish[0], @caught_fish[1]] if @caught_fish[2]
    @caught_fish = [0.0, 0, false]
    @got_fish = @lost_fish = false
    @fish_pulling = @fish_weight = @fill = 0
    @fish_length = 0.0
    @rate = 1000
    refresh
    @indicator_window.update(1000, self.x + 80, self.width - 116)
    @info_window.visible = false
    @info_window.index = -1
  end
  
  def got_fish
    $game_variables[9] += 1
    case @fish_types
    when 0
      a = rand(250) + 50
      b = a*2
      @fish_length = a/10 + (a%10)/10.0
      @fish_weight = b
      @fish_power = a/2
    when 1
      a = rand(250) + 250
      b = a*3
      @fish_length = a/10 + (a%10)/10.0
      @fish_weight = b
      @fish_power = a
    when 2
      if rand(100) < 15
        a = rand(250) + rand(300) + 1450
        b = a*(a > 1700 ? 12 : 9)
      else
        a = rand(700) + 750
        b = a * 5
      end
      @fish_length = a / 10 + (a % 10) / 10.0
      @fish_weight = b
      @fish_power = a
    end
    @fill = rand(400) + 300
    @got_fish = true
    @fish_pulling = rand(8) + 2
  end
  
  def get_fish
    actor = $game_party.actors[0]
    if [actor.armor4_id, actor.armor5_id, actor.armor6_id].include?(97)
      @fish_types, @rod_power = 2, 900
    elsif [actor.armor4_id, actor.armor5_id, actor.armor6_id].include?(96)
      @fish_types, @rod_power = 1, 350
    elsif [actor.armor4_id, actor.armor5_id, actor.armor6_id].include?(94)
      @fish_types, @rod_power = 0, 100
    end
  end
  
  def fill=(val)
    if val < 0
      @fill = 0
    elsif val > 1000
      @fill = 1000
    else
      @fill = val
    end
  end
  
  def rate=(val)
    if val < 0
      @rate = 0
    elsif val > 1000
      @rate = 1000
    else
      @rate = val
    end
  end
  
  alias disp_fishing_later dispose
  def dispose
    [@indicator_window, @info_window].each {|win| win.dispose}
    @indicator_window = @info_window = nil
    $game_player.caught_fish = [0.0, 0] if !$game_variables[31]
    disp_fishing_later
  end
  
  def update_cursor_rect
    if @index < 0
      self.cursor_rect.empty
      return
    end
    row = @index / @column_max
    self.top_row = row if row < top_row
    self.top_row = row - (page_row_max - 1) if row > top_row + (page_row_max - 1)
    cursor_width = (self.width - 32)/ @column_max
    x = @index % @column_max * (cursor_width + 32)
    y = @index / @column_max * 32 - self.oy + 32
    self.cursor_rect.set(x, y, cursor_width, 32)
  end
  
end

#==============================================================================
# FishIcon
#==============================================================================

class FishIcon < Sprite
  
  def initialize
    super
    self.bitmap = RPG::Cache.picture('fish_icon')
    self.z, self.y = 9999, 16
  end
  
  def update(fill, x, width)
    self.x = x + width * fill / 1000
  end
  
end

#==============================================================================
# Window_FishInfo
#==============================================================================

class Window_FishInfo < Window_Selectable
  
  def initialize
    super(64, 176, 512, 128)
    create_bitmap
    @cursor_width = self.contents.text_size('Yes').width + 16
    self.visible = false
    self.opacity = 160
  end
  
  def create_bitmap
    self.contents = Bitmap.new(self.width - 32, self.height - 32)
    self.contents.font.name = $fontface
    self.contents.font.size = $fontsize
    self.contents.font.bold = true if $fontface == 'Papyrus'    
  end
  
  def refresh
    if @lost
      text = 'Fish got away. Continue?'
    else
      d1, d2 = "#{@catch_data[0]}cm", "#{@catch_data[1]}g"
      $game_system.caught = [@catch_data[0], @catch_data[1]]
      text = "Caught fish is #{d1} and #{d2}. Continue?"
    end
    self.width = self.contents.text_size(text).width + 48
    self.x = 320 - self.width / 2
    self.contents.dispose
    create_bitmap
    self.contents.draw_text(4, 0, self.width - 40, 32, text, 1)
    self.contents.draw_text(12, 32, 96, 32, 'Yes')
    self.contents.draw_text(12, 64, 96, 32, 'No')
    @index, @item_max = 0, 2
  end
  
  def set_fish(lost, catch_data)
    @lost, @catch_data = lost, catch_data
  end
  
  def update
    super
    if Input.trigger?($controls.confirm)
      $game_system.se_play($data_system.decision_se)
      return @index
    elsif Input.trigger?($controls.cancel)
      $game_system.se_play($data_system.cancel_se)
      return 1
    end
    return nil
  end
  
  def update_cursor_rect
    if @index < 0 || self.contents == nil
      self.cursor_rect.empty
    else
      self.cursor_rect.set(4, @index * 32 + 32, @cursor_width, 32)
    end
  end
  
end

#==============================================================================
# Bitmap
#==============================================================================

class Bitmap

  def gradient_bar_alt3(x, fill = 1.0, rate = 1.0)
    if rate > 0.6
      c1 = Color.new(240 - 450 * (rate-0.6), 240, 150 * (rate-0.6), 192)
      c2 = Color.new(80 - 150 * (rate-0.6), 80, 50 * (rate-0.6), 192)
    elsif rate > 0.2 && rate <= 0.6
      c1 = Color.new(240, 600 * (rate-0.2), 0, 192)
      c2 = Color.new(80, 200 * (rate-0.2), 0, 192)
    elsif rate <= 0.2
      c1 = Color.new(240, 0, 0, 192)
      c2 = Color.new(80 + 160 * (0.2 - rate), 0, 0, 192)
    end
    r1, g1, b1, r2, g2, b2 = c1.red, c1.green, c1.blue, c2.red, c2.green, c2.blue
    fill_rect(x, 13, 204, 11, Color.new(0, 0, 0, 255))
    fill_rect(x+1, 14, 202, 9, Color.new(255, 255, 255, 255))
    fill_rect(x+2, 14, 200, 8, Color.new(0, 0, 0, 160))
    (0...(200*fill).to_i).each {|i|
        r = (r1-r2)*i / (200*fill)+r2
        g = (g1-g2)*i / (200*fill)+g2
        b = (b1-b2)*i / (200*fill)+b2
        fill_rect(x+i+2, 14, 1, 8, Color.new(r, g, b, 255))}
  end
  
end

#==============================================================================
# Scene_Map
#==============================================================================

class Scene_Map
  
  alias upd_fishing_later update
  def update
    if $game_player.fishing
      result = @fbar_window.update
      $game_map.update
      $game_system.map_interpreter.update
      $game_system.update
      $game_screen.update
      @spriteset.update
      @message_window.update
      if !result && Input.trigger?($controls.cancel)
        $game_system.se_play($data_system.cancel_se)
        $game_player.fishing = false 
        @fbar_window.reset
      end
    else
      upd_fishing_later
    end
  end
  
end
