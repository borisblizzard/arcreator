#==============================================================================
# Window_Ammo
#==============================================================================

class Window_Ammo < Window_Item
  
  def initialize(skill_id, help_window)
    @skill_id = skill_id
    super()
    @help_window = help_window
  end
  
  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    @data = []
    ary = CP.resort_items
    (1...ary.size).each {|i|
        if $game_party.item_number(ary[i].id) > 0 &&
            CP::Cache::Bullets.include?(ary[i].id)
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
    if $game_party.ammo_can_use?(@skill_id, item.id)
      bitmap = RPG::Cache.icon(item.icon_name)
      self.contents.font.color = normal_color
    else
      bitmap = RPG::Cache.desaturated(item.icon_name)
      self.contents.font.color = disabled_color
    end
    self.contents.blt(x+4, y+4, bitmap, Rect.new(0, 0, 24, 24))
    self.contents.draw_text(x + 24, y, 40, 32, $game_party.item_number(item.id).to_s, 2)
  end
  
  def update_help
    if self.item != nil
      if $game_party.ammo_can_use?(@skill_id, self.item.id)
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
  
end
