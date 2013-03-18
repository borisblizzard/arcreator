#==============================================================================
# Sprite_Timer
#==============================================================================

class Sprite_Timer < Sprite
  
  def initialize
    super
    self.bitmap = Bitmap.new(106, 64)
    self.bitmap.font.name = 'LED Real'
    self.bitmap.font.size = 36
    self.x, self.y = 616 - self.bitmap.width/2, self.bitmap.height/2
    self.ox, self.oy, self.z = self.bitmap.width/2, self.bitmap.height/2, 10000
    update
  end
  
  def dispose
    self.bitmap.dispose if self.bitmap != nil
    super
  end
  
  def update
    super
    self.visible = $game_system.timer_working
    if $game_system.timer_working || $game_switches[369]
      if $game_switches[367] || $game_switches[369]
        self.zoom_x = self.zoom_y = 1.0
      elsif $game_system.timer / Graphics.frame_rate < 10
        zoom = $game_system.timer % 10
        self.zoom_x = self.zoom_y = 1.0 + (zoom < 5 ? zoom : 10-zoom) * 0.06
      elsif $game_system.timer / Graphics.frame_rate < 60
        zoom = $game_system.timer % 20
        self.zoom_x = self.zoom_y = 1.0 + (zoom < 10 ? zoom : 20-zoom) * 0.03
      else
        self.zoom_x = self.zoom_y = 1.0
      end
    end
    if 2 * $game_system.timer / Graphics.frame_rate != @total_sec &&
        $game_system.timer >= 0 || $game_switches[369] &&
        Graphics.frame_count % (Graphics.frame_rate / 2) == 0
      self.bitmap.clear
      @total_sec = 2 * $game_system.timer / Graphics.frame_rate
      min = sprintf('%02d', @total_sec / 120)
      sec = sprintf('%02d', (@total_sec/2) % 60)
      if $game_switches[367] || $game_switches[369]
        if @total_sec < 1200 || $game_switches[369]
          self.bitmap.font.color.set(255, 255, 255)
        else
          self.bitmap.font.color.set(255, 255, 0)
        end
      elsif @total_sec < 20
        self.bitmap.font.color.set(255, 0, 0)
      elsif @total_sec < 120
        self.bitmap.font.color.set(255, 255, 0)
      else
        self.bitmap.font.color.set(255, 255, 255)
      end
      self.bitmap.draw_text_outline(self.bitmap.rect, min, 0)
      if (2 * $game_system.timer / Graphics.frame_rate) % 2 == 1 ||
          2 * $game_system.timer / Graphics.frame_rate == 0 ||
          $game_switches[369] &&
          Graphics.frame_count % Graphics.frame_rate / 20 == 0
        self.bitmap.draw_text_outline(self.bitmap.rect, ' :', 1)
      end
      self.bitmap.draw_text_outline(self.bitmap.rect, sec, 2)
    end
  end
  
end
