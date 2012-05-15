#==============================================================================
# Game_System
#==============================================================================

class Game_System
  
  attr_accessor :reserve_party
  attr_accessor :mine_table
  
  alias init_ice_temple_later initialize
  def initialize
    init_ice_temple_later
    @reserve_party = []
  end
  
end

#==============================================================================
# Points
#==============================================================================

class Points < Sprite
  
  attr_reader :points
  attr_reader :game
  attr_reader :player
  
  def initialize(index = -1)
    super()
    if $game_switches[31]
      if index < 0
        self.x, self.y, @game, w, h = 16, 16, 0, 64, 32
      else
        case index
        when 0 then self.x, self.y, @player = 224, 128, 14
        when 1 then self.x, self.y, @player = 224, 224, 5
        when 2 then self.x, self.y, @player = 224, 320, 9
        when 3 then self.x, self.y, @player = 352, 128, 10
        when 4 then self.x, self.y, @player = 352, 224, 19
        when 5 then self.x, self.y, @player = 352, 320, 20
        end
        w, h, @game = 64, 32, 1
      end
      self.bitmap = Bitmap.new(w, h)
      self.bitmap.font.name = $fontface
      self.bitmap.font.bold = true if $fontface == 'Papyrus'    
      @points = 0
    end
    self.z = 2000
    refresh
  end
  
  def refresh
    self.bitmap.clear
    case @game
    when 0
      text = "#{$game_variables[14]} Hits"
      self.bitmap.draw_text_outline(0, 0, self.bitmap.width, 32, text, 2)
      @points = $game_variables[14]
      $game_system.kill_arshes = @points if $game_system.kill_arshes < @points
    when 1
      self.bitmap.draw_text_outline(0, 0, 64, 32, $game_variables[@player].to_s, 1)
      @points = $game_variables[@player]
    end
  end
  
end

#==============================================================================
# IceIndicator
#==============================================================================

class IceIndicator < Sprite
  
  def initialize
    super
    self.x, self.y, self.ox = 320, 27, 3
    self.bitmap = Bitmap.new(6, 16)
    self.bitmap.blt(0, 0, CP::Cache.image('ice_indicator'), Rect.new(0, 0, 16, 32))
  end
  
  def update
    if $game_player.terrain_tag == 0
      self.x = 320 unless $game_system.map_interpreter.running?
    elsif $game_player.terrain_tag == 1
      var = rand(7) + 3
      if $game_player.moving? && self.x <= 440 && self.x >= 200
        self.x += var unless $game_temp.message_window_showing
      elsif !$game_player.moving? && self.x <= 440 && self.x >= 200
        self.x -= var unless $game_temp.message_window_showing
      end
    end
  end
  
end

#==============================================================================
# Bitmap
#==============================================================================

class Bitmap
  
  def mirror
    b = self.clone
    self.clear
    (0...self.width).each {|x| (0...self.height).each {|y|
        set_pixel(self.width-x-1, y, b.get_pixel(x, y))}}
    b.dispose
  end
  
  def invert
    (0...self.width).each {|x| (0...self.height).each {|y| invert_pixel(x, y)}}
  end
  
  def invert_pixel(x, y)
    c = get_pixel(x, y)
    return if c.alpha == 0
    if c.red > c.green
      if c.red > c.blue
        max = c.red
        min = (c.blue < c.green ? c.blue : c.green)
      else
        max = c.blue
        min = (c.red < c.green ? c.red : c.green)
      end
    elsif c.green > c.blue
      max = c.green
      min = (c.blue < c.red ? c.blue : c.red)
    else
      max = c.blue
      min = (c.red < c.green ? c.red : c.green)
    end
    med = (max + min) / 2
    if med > 128
      c.red, c.green, c.blue = 128-med/2, 383-med*3/2, 383-med*3/2
    else
      c.red, c.green, c.blue = 255-med*3/2, 255-med/2, 255-med/2
    end
    set_pixel(x, y, c)
  end
  
end

#==============================================================================
# Scene_Map
#==============================================================================

class Scene_Map
  
  attr_accessor :points_window
  attr_accessor :bar
  attr_accessor :indicator
  attr_accessor :fbar_window
  attr_accessor :init_points
  
  alias main_minigame_later main
  def main
    main_minigame_later
    if @bar != nil
      @bar.dispose
      @indicator.dispose
      @bar = nil
      @indicator = nil
    end
    if @fbar_window != nil
      @fbar_window.dispose
      @fbar_window = nil
    end
  end
  
  alias update_minigame_later update
  def update
    check_switches
    update_minigame_later
  end
  
  def check_switches
    if $game_switches[31]
      if @init_points
        if @points_window != nil
          if @points_window.is_a?(Array)
            game = @points_window[0].game
          else
            game = @points_window.game
          end
          case game
          when 0
            @points_window.refresh if @points_window.points != $game_variables[14]
          when 1
            @points_window.each {|win|
                win.refresh if win.points != $game_variables[win.player]}
          end
        end
        @indicator.update if @bar != nil
      else
        case $game_map.map_id
        when 186
          @points_window = Points.new
          @init_points = true
        when 188
          @points_window = []
          (0...6).each {|i| @points_window.push(Points.new(i))}
          @init_points = true
        when 249
          @bar = Sprite.new
          @bar.x, @bar.y, @bar.bitmap = 199, 30, Bitmap.new(242, 10)
          @bar.bitmap.blt(0, 0, CP::Cache.image('ice_bar'), Rect.new(0, 0, 242, 10))
          @indicator = IceIndicator.new
          @init_points = true
        when 290
          @fbar_window = Window_FishBar.new(FishIcon.new, Window_FishInfo.new)
          @init_points = true
        end
      end
    else
      remove_points
    end
  end
  
  def remove_points
    if @points_window != nil
      if @points_window.is_a?(Array)
        @points_window.each {|win| win.dispose}
      else
        @points_window.dispose
      end
      @points_window = nil
    end
    if @bar != nil
      @bar.dispose
      @indicator.dispose
      @bar = @indicator = nil
    end
    if @fbar_window != nil
      @fbar_window.dispose
      @fbar_window = nil
    end
    @init_points = nil
  end
    
    
end
