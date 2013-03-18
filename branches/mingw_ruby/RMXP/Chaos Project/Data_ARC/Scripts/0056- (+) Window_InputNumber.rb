#==============================================================================
# Window_InputNumber
#==============================================================================

class Window_InputNumber < Window_Base
  
  def initialize(digits_max, transparent = true)
    @digits_max, @transparent = digits_max, transparent
    @max = 10 ** @digits_max - 1
    if $game_switches[522]
      @max = 100 - $game_party.item_number($game_variables[105])
    end
    @number = 0
    dummy_bitmap = Bitmap.new(32, 32)
    @cursor_width = dummy_bitmap.text_size('0').width + 2
    dummy_bitmap.dispose
    super(0, 0, @cursor_width * @digits_max + 32, 64)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.contents.font.name = $fontface
    self.contents.font.size = $fontsize
    self.contents.font.bold = true if $fontface == 'Papyrus'
    self.z += 9999
    self.opacity = 0
    reset
  end
  
  def reset
    @index = @digits_max - 1
    update_cursor_rect
    @number = 0
    refresh
  end
    
  def number
    return @number
  end
  
  def number=(number)
    if number < 0
      @number = 0
    elsif number > @max
      @number = @max
    else
      @number = number
    end
    refresh
  end
  
  def update_cursor_rect
    self.cursor_rect.set(@index * @cursor_width - 1, 0, @cursor_width + 1, 32)
  end
  
  def update
    super
    if Input.repeat?($controls.up)
      $game_system.se_play($data_system.cursor_se)
      n = 10 ** (@digits_max - 1 - @index)
      self.number += n
    elsif Input.repeat?($controls.down)
      $game_system.se_play($data_system.cursor_se)
      n = 10 ** (@digits_max - 1 - @index)
      self.number -= n
    elsif Input.repeat?($controls.right) && @digits_max >= 2
      $game_system.se_play($data_system.cursor_se)
      @index = (@index + 1) % @digits_max
    elsif Input.repeat?($controls.left) && @digits_max >= 2
      $game_system.se_play($data_system.cursor_se)
      @index = (@index + @digits_max - 1) % @digits_max
    end
    update_cursor_rect
  end
  
  def refresh
    self.contents.clear
    self.contents.font.color = normal_color
    s = sprintf('%0*d', @digits_max, @number)
    (0...@digits_max).each {|i|
        if @transparent
          self.contents.draw_text_outline(i * @cursor_width, 0, 32, 32, s[i, 1])
        else
          self.contents.draw_text(i * @cursor_width, 0, 32, 32, s[i, 1])
        end}
  end
  
end
