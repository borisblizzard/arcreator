#==============================================================================
# Window_Command
#==============================================================================

class Window_Command < Window_Selectable
  
  attr_reader :commands
  
  def initialize(width, commands, height = nil)
    if height == nil
      super(0, 0, width, commands.size * 32 + 32)
    else
      super(0, 0, width, height)
    end
    @item_max = commands.size
    @commands = commands
    if @item_max > 0
      self.contents = Bitmap.new(width - 32, @item_max * 32)
    else
      self.contents = Bitmap.new(width - 32, 32)
    end
    self.contents.font.name = $fontface
    self.contents.font.size = $fontsize
    self.contents.font.bold = true if $fontface == 'Papyrus'
    refresh
    self.index = 0
  end
  
  def set_title_commands(com)
    if $scene.is_a?(Scene_Title)
      @commands = com
      refresh
    end
  end
  
  def refresh
    self.contents.clear
    (0...@item_max).each {|i| draw_item(i, normal_color)}
  end
  
  def draw_item(index, color)
    rect = Rect.new(4, 32 * index, self.contents.width - 8, 32)
    self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
    self.contents.font.color = color
    if $scene.is_a?(Scene_Title)
      self.contents.draw_text(rect, @commands[index], 1)
    elsif $scene.is_a?(Scene_Gameover)
      self.contents.draw_text_outline(rect, @commands[index], 1)
    elsif $scene.is_a?(Scene_Roulette)
      self.contents.draw_text_outline(rect, @commands[index], 2)
    else
      self.contents.draw_text(rect, @commands[index])
    end  
  end
  
  def disable_item(index)
    draw_item(index, disabled_color)
  end
  
  def size
    return @commands.size
  end
  
end
