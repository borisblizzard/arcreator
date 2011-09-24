#==============================================================================
# Window_Item
#==============================================================================

class Window_Item < Window_Selectable
  
  def initialize
    super(16, 108, 608, 196)
    @column_max = 6
    self.opacity = 160
    self.index = 0
    self.windowskin = RPG::Cache.windowskin('Black Death')
    refresh
  end
  
  def item
    return @data[self.index]
  end
  
  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    @data = []
    ary = CP.resort_items
    (1...ary.size).each {|i|
        if $game_party.item_can_use?(ary[i].id) &&
            !(CP::Cache::Trade | CP::Cache::Quest | CP::Cache::Bullets).include?(ary[i].id)
          @data.push(ary[i]) 
        end}
    @item_max = @data.size
    if @item_max > 0
      self.contents = Bitmap.new(width - 32, row_max * 32 + 8)
      self.contents.font.name = $fontface
      if $fontface == 'Papyrus'
        self.contents.font.bold = true
        self.contents.font.size = 28
      else
        self.contents.font.size = 22
      end
      (0...@item_max).each {|i| draw_item(i)}
    end
  end
  
  def draw_item(index)
    item = @data[index]
    x, y = index % 6 * 96 + 16, index / 6 * 32
    if $game_party.item_can_use?(item.id)
      bitmap = RPG::Cache.icon(item.icon_name)
      self.contents.font.color = normal_color
    else
      bitmap = RPG::Cache.desaturated(item.icon_name)
      self.contents.font.color = disabled_color
    end
    self.contents.blt(x+4, y+4, bitmap, Rect.new(0, 0, 24, 24))
    self.contents.draw_text(x + 16, y, 48, 32, $game_party.item_number(item.id).to_s, 2)
  end
  
  def update_help
    if self.item != nil
      if $game_party.item_can_use?(self.item.id)
        color = normal_color
      else
        color = disabled_color
      end
      text = "#{self.item.name} (#{$game_party.item_number(self.item.id)})"
      @help_window.set_text(text, 1, color, self.item.description)
    else
      @help_window.set_text('')
    end
  end
  
  def update_cursor_rect
    if @index < 0
      self.cursor_rect.empty
      return
    end
    row = @index / @column_max
    self.top_row = row if row < top_row
    self.top_row = row - (page_row_max - 1) if row > top_row + (page_row_max - 1)
    x = @index % @column_max * 96 + 8
    y = @index / @column_max * 32 - self.oy
    self.cursor_rect.set(x, y, 88, 32)
  end
  
end
