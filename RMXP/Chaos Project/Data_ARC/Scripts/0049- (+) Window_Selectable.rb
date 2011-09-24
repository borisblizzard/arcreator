#==============================================================================
# Window_Selectable
#==============================================================================

class Window_Selectable < Window_Base
  
  attr_reader :index
  attr_reader :help_window
  
  def initialize(x, y, width, height)
    super(x, y, width, height)
    @item_max = 1
    @column_max = 1
    @index = -1
  end
  
  def index=(index)
    @index = index
    update_help if self.active && @help_window != nil
    update_cursor_rect
  end
  
  def row_max
    return (@item_max + @column_max - 1) / @column_max
  end
  
  def top_row
    return self.oy / 32
  end
  
  def top_row=(row)
    row = 0 if row < 0
    row = row_max - 1 if row > row_max - 1
    self.oy = row * 32
  end
  
  def page_row_max
    return (self.height - 32) / 32
  end
  
  def page_item_max
    return page_row_max * @column_max
  end
  
  def help_window=(help_window)
    @help_window = help_window
    update_help if self.active && @help_window != nil
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
    y = @index / @column_max * 32 - self.oy
    self.cursor_rect.set(x, y, cursor_width, 32)
  end
  
  def update
    super
    if self.active && @item_max > 0 && @index >= 0
      if Input.repeat?($controls.down)
        if (@column_max == 1 && Input.trigger?($controls.down)) ||
            @index != @item_max - 1
          if @index < @item_max - @column_max
            $game_system.se_play($data_system.cursor_se)
            @index = (@index + @column_max) % @item_max
          elsif @index == @item_max - 1
            $game_system.se_play($data_system.cursor_se)
            @index = 0
          elsif (@index + @column_max) / @column_max < row_max
            $game_system.se_play($data_system.cursor_se)
            @index = @item_max - 1
          end
        end
      elsif Input.repeat?($controls.up)
        if (@column_max == 1 && Input.trigger?($controls.up)) ||
           @index >= @column_max
          $game_system.se_play($data_system.cursor_se)
          @index = (@index - @column_max + @item_max) % @item_max
        end
      elsif Input.repeat?($controls.right)
        if @column_max >= 2
          if @index < @item_max - 1
            $game_system.se_play($data_system.cursor_se)
            @index += 1
          elsif Input.trigger?($controls.right)
            $game_system.se_play($data_system.cursor_se)
            @index = 0
          end
        end
      elsif Input.repeat?($controls.left)
        if @column_max >= 2
          if @index > 0
            $game_system.se_play($data_system.cursor_se)
            @index -= 1
          elsif Input.trigger?($controls.left)
            $game_system.se_play($data_system.cursor_se)
            @index = @item_max - 1
          end
        end
      elsif Input.repeat?($controls.nex)
        if self.top_row + (self.page_row_max - 1) < (self.row_max - 1)
          $game_system.se_play($data_system.cursor_se)
          @index = @index + self.page_item_max
          item_max = @item_max - 1
          @index = item_max if @index > item_max
          self.top_row += self.page_row_max
        end
      elsif Input.repeat?($controls.prev)
        if self.top_row > 0
          $game_system.se_play($data_system.cursor_se)
          @index = @index - self.page_item_max
          @index = 0 if @index < 0
          self.top_row -= self.page_row_max
        end
      end
    end
    update_help if self.active && @help_window != nil
    update_cursor_rect
  end
  
end
