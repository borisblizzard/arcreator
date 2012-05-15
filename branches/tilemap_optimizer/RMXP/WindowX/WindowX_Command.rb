#==============================================================================
# WindowX_Command
#==============================================================================

class WindowX_Command < WindowX_Selectable
  
  attr_reader :align
  
  def initialize(x, y, width, height, commands, icons = [])
    super(x, y, width, height)
    @item_max = [commands.size, icons.size].max
    @commands = commands
    @enabled = Array.new(@item_max, true)
    @icons = icons
    @space_left = 2
    @space_right = 2
    @icon_space = 2
    @align = 0
    @clamp_cursor_rect = false
    self.contents = Bitmap.new(width, height)
    refresh
    self.index = -1
    self.active = false
  end
  
  def refresh
    self.contents.clear
    @item_max.times {|i| draw_item(i)}
  end
  
  def align=(value)
    @align = value
    refresh
  end
  
  def get_draw_rect(index = @index, clamp_cursor_rect = @clamp_cursor_rect)
    rect = super
    if clamp_cursor_rect
      rect.x += @space_left
      draw_w = self.get_draw_width(index)
      case @align
      when 1 then rect.x += (rect.width - draw_w) / 2
      when 2 then rect.x += rect.width - draw_w
      end
      rect.width = draw_w
    end
    return rect
  end
  
  def get_draw_width(index = @index)
    draw_w = @space_left + @space_right
    if @icons != nil && @icons[index] != nil
      draw_w += self.get_icon(index).width + @icon_space
    end
    if @commands != nil && @commands[index] != nil
      draw_w += self.contents.text_size(@commands[index]).width
    end
    return draw_w
  end
  
  def get_icon(index)
    return RPG::Cache.icon(@icons[index]) if @icons[index][0, 1] != ':'
    return RPG::Cache.icon(@icons[index][1, @icons[index].size - 1]).desaturate
  end
  
  def draw_item(index)
    self.contents.fill_rect(self.get_draw_rect(index), BLANK_COLOR)
    self.contents.font.color = (@enabled[index] ? normal_color : disabled_color)
    rect = self.get_draw_rect(index)
    if @icons != nil && @icons[index] != nil
      icon = self.get_icon(index)
      icon_y = rect.y + (@row_height - icon.height) / 2
      self.contents.blt(rect.x, icon_y, icon, ICON_RECT)
      rect.x += icon.width + @icon_space
    end
    if @commands != nil && @commands[index] != nil
      self.contents.draw_text(rect, @commands[index], @align)
    end
  end
  
  def disable_item(index)
    if @enabled[index]
      @enabled[index] = false
      draw_item(index)
    end
  end
  
  def enable_item(index)
    if !@enabled[index]
      @enabled[index] = true
      draw_item(index)
    end
  end
  
  def enabled?(index = @index)
    return @enabled[index]
  end
  
  def set_commands(commands, icons = [])
    @item_max = [commands.size, icons.size].max
    @commands = commands
    @icons = icons
    @enabled = Array.new(@item_max, true)
    refresh
  end
  
end
