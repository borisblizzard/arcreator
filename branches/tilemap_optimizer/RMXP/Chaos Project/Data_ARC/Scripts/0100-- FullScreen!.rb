#==============================================================================
# Scene_Stormtronics
#==============================================================================

class Window_Command < Window_Selectable

  alias init initialize
  def initialize(width, commands, height = nil)
    if $scene.is_a?(Scene_Stormtronics)
      if height == nil
        super(0, 0, width, commands.size * 32 + 64)
      else
        super(0, 0, width, height)
      end
      @item_max = commands.size
      @commands = commands
      self.contents = Bitmap.new(width - 32, @item_max * 32 + 32)
      self.contents.font.name = $fontface
      self.contents.font.size = $fontsize
      self.contents.font.bold = true if $fontface == 'Papyrus'
      refresh
      self.index = 0
      return
    end
    init(width, commands, height)
  end

  alias ref refresh
  def refresh(mode = false)
    if $scene.is_a?(Scene_Stormtronics)
      self.contents.clear
      unless mode
        self.contents.draw_text_outline(0, 0, width - 32, 32,
            'Switch to fullscreen?', 1)
      end
      (0...@item_max).each {|i| draw_itemX(i, normal_color)}
      return
    end
    ref
  end

  def draw_itemX(index, color)
    rect = Rect.new(4, 32+32 * index, self.contents.width - 8, 32)
    self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
    self.contents.font.color = color
    self.contents.draw_text_outline(rect, @commands[index], 1)
  end
  
  alias cur update_cursor_rect
  def update_cursor_rect
    if $scene.is_a?(Scene_Stormtronics)
      if @index < 0
        self.cursor_rect.empty
        return
      end
      row = @index / @column_max
      self.top_row = row if row < top_row
      self.top_row = row - (page_row_max - 1) if row > top_row + (page_row_max - 1)
      cursor_width = 64
      x = (self.contents.width - cursor_width) / 2
      y = @index / @column_max * 32 - self.oy
      self.cursor_rect.set(x, y + 32, cursor_width, 32)
      return
    end
    cur
  end

end
  
#==============================================================================
# Scene_Stormtronics
#==============================================================================

class Scene_Stormtronics
  
  alias main_fullscreen_later main
  def main
    unless $game_started
      Graphics.freeze
      $game_system = Game_System.new
      $game_system.windowskin_name = 'GameOver'
      @window = Window_Command.new(320, ['Yes' ,'No'])
      @window.x = 320 - @window.width / 2
      @window.y = 240 - @window.height / 2
      @window.opacity = 0
      @sprite = Sprite.new
      @sprite.bitmap = Bitmap.new(640, 32)
      @sprite.y = 360
      @sprite.bitmap.font.size = 22
      @sprite.bitmap.draw_text(0, 0, 640, 32, 'Game controls are in the readme file!', 1)
      Graphics.transition(10)
      loop do
        Graphics.update
        Input.update
        @window.update
        update_window
        break if update_window
      end
      Graphics.freeze
      @window.dispose
      @sprite.dispose if @sprite != nil
      @window = @sprite = nil
      Graphics.transition(10)
      $game_system.windowskin_name = 'Original'
      $game_started = true
    end
    main_fullscreen_later
  end
  
  def update_window
    if Input.trigger?($controls.confirm)
      $game_system.se_play($data_system.decision_se)
      if @window.index == 0
        keybd = Win32API.new('user32.dll', 'keybd_event', ['i', 'i', 'l', 'l'], 'v')
        keybd.call 0xA4, 0, 0, 0
        keybd.call 13, 0, 0, 0
        keybd.call 13, 0, 2, 0
        keybd.call 0xA4, 0, 2, 0
      end
      return true
    elsif Input.trigger?($controls.cancel)
      $game_system.se_play($data_system.cancel_se)
      return true
    end
    return false
  end
  
end
