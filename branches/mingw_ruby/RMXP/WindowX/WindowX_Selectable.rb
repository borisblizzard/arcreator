#==============================================================================
# WindowX_Selectable
#==============================================================================

class WindowX_Selectable < WindowX_Base
  
  attr_reader :index
  
  def initialize(x, y, width, height)
    super
    @item_max = 1
    @index = -1
    @row_height = 32
    @row_space = 0
    @column_max = 1
    @column_space = 0
  end
  
  def index=(index)
    @index = index
    update_cursor_rect
  end
  
  def row_max
    return (@item_max + @column_max - 1) / @column_max
  end
  
  def top_row
    return self.oy / @row_height
  end
  
  def top_row=(row)
    if row < 0
      row = 0
    elsif row > row_max - 1
      row = row_max - 1
    end
    self.oy = row * @row_height
  end
  
  def page_row_max
    return (self.height - self.pad_vertical) / @row_height
  end
  
  def page_item_max
    return page_row_max * @column_max
  end
  
  def update_cursor_rect
    if @index < 0
      self.cursor_rect.empty
      return
    end
    row = @index / @column_max
    if row < self.top_row
      self.top_row = row
    elsif row > self.top_row + (self.page_row_max - 1)
      self.top_row = row - (self.page_row_max - 1)
    end
    rect = self.get_draw_rect
    rect.y -= self.oy
    self.cursor_rect.set(rect.x, rect.y, rect.width, rect.height)
  end
  
  def get_draw_rect(index = @index, clamp_cursor_rect = false)
    column = index % @column_max
    row = index / @column_max
    w = (self.width - self.pad_horizontal - @column_space * (@column_max - 1)) / @column_max
    x = column * (w + @column_space)
    y = row * (@row_height + @row_space)
    return Rect.new(x, y, w, @row_height)
  end
  
  def update
    super
    if self.active && @item_max > 0 && @index >= 0
      if Input.repeat?(Input::DOWN)
        if (@column_max == 1 && Input.trigger?(Input::DOWN)) || @index < @item_max - @column_max
          $game_system.se_play($data_system.cursor_se)
          @index = (@index + @column_max) % @item_max
        end
      elsif Input.repeat?(Input::UP)
        if (@column_max == 1 && Input.trigger?(Input::UP)) || @index >= @column_max
          $game_system.se_play($data_system.cursor_se)
          @index = (@index - @column_max + @item_max) % @item_max
        end
      elsif Input.repeat?(Input::RIGHT)
        if @column_max >= 2 && @index < @item_max - 1
          $game_system.se_play($data_system.cursor_se)
          @index += 1
        end
      elsif Input.repeat?(Input::LEFT)
        if @column_max >= 2 && @index > 0
          $game_system.se_play($data_system.cursor_se)
          @index -= 1
        end
      elsif Input.repeat?(Input::R)
        if self.top_row + (self.page_row_max - 1) < (self.row_max - 1)
          $game_system.se_play($data_system.cursor_se)
          @index = [@index + self.page_item_max, @item_max - 1].min
          self.top_row += self.page_row_max
        end
      elsif Input.repeat?(Input::L)
        if self.top_row > 0
          $game_system.se_play($data_system.cursor_se)
          @index = [@index - self.page_item_max, 0].max
          self.top_row -= self.page_row_max
        end
      end
    end
    update_cursor_rect
  end
  
end
