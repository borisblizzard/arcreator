#==============================================================================
# ** Window_HCommand
#------------------------------------------------------------------------------
#  This window deals with general command choices, but the display is
#  horizontal.
#==============================================================================

class Window_HCommand < Window_Command
  
  def initialize(width, commands)
    super(commands.size * width + 32, commands, 64)
    @column_max = commands.size
    self.contents.dispose
    self.contents = Bitmap.new(self.width - 32, self.height - 32)
    refresh
    update_cursor_rect
  end
  
  def refresh
    self.contents.clear
    (0...@item_max).each {|i| draw_item(i, normal_color)}
  end
  
  def draw_item(i, color)
    self.contents.font.color = color
    w = (self.width - 32) / @column_max
    x = i % @column_max * w
    rect = Rect.new(x, 0, self.contents.width / @column_max, 32)
    self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
    self.contents.draw_text(rect, @commands[i], 1)
  end
  
  def update_cursor_rect
    if @index < 0
      self.cursor_rect.empty
      return
    end
    row = @index / @column_max
    self.top_row = row if row < self.top_row
    if row > self.top_row + (self.page_row_max - 1)
      self.top_row = row - (self.page_row_max - 1)
    end
    cursor_width = (self.width - 32) / @column_max
    x = @index % @column_max * cursor_width
    self.cursor_rect.set(x, 0, cursor_width, 32)
  end
  
end

#==============================================================================
# ** Window_H2Command
#------------------------------------------------------------------------------
#  This window deals with general command choices, but the display is
#  horizontal.
#==============================================================================

class Window_H2Command < Window_HCommand
  
  def draw_item(i, color)
    self.contents.font.color = color
    w = (self.width - 32) / @column_max
    x = i % @column_max * w
    rect = Rect.new(x, 0, self.contents.width / @column_max, 32)
    self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
    self.contents.draw_text_outline(rect, @commands[i], 1)
  end
  
end
