#==============================================================================
# Window_Skill
#==============================================================================

class Window_Skill < Window_Selectable
  
  def initialize(actor, type)
    super(16, 108, 608, 196)
    @actor = actor
    @column_max = 6
    @type = type
    self.opacity = 160
    self.index = 0
    self.windowskin = RPG::Cache.windowskin('Black Death')
    refresh
  end
  
  def skill
    return @data[self.index]
  end
  
  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    @data = []
    @actor.skills.each {|id|
        skill = $data_skills[id]
        @data.push(skill) if skill.element_set.include?(@type + 19)}
    @item_max = @data.size
    if @item_max > 0
      self.contents = Bitmap.new(width - 32, row_max * 32 + 8)
      self.contents.font.name = $fontface
      self.contents.font.size = $fontsize
      self.contents.font.bold = true if $fontface == 'Papyrus'
      (0...@item_max).each {|i| draw_item(i)}
    end
  end
  
  def draw_item(index)
    skill = @data[index]
    x = index % 6 * 96 + 16
    y = index / 6 * 32
    if @actor.skill_can_use?(skill.id)
      bitmap = RPG::Cache.icon(skill.icon_name)
      self.contents.font.color = normal_color
    else
      bitmap = RPG::Cache.desaturated(skill.icon_name)
      self.contents.font.color = disabled_color
    end
    self.contents.blt(x+4, y+4, bitmap, Rect.new(0, 0, 24, 24))
    sp_cost = skill.sp_cost 
    sp_cost = (sp_cost / 2.0).ceil if @actor.states.include?(31) 
    unless sp_cost == 0
      self.contents.draw_text(x + 24, y, 44, 32, sp_cost.to_s, 2)
    end
  end
  
  def update_help
    if self.skill != nil
      if @actor.skill_can_use?(self.skill.id)
        color = Color.new(0, 255, 0)
      else
        color = disabled_color
      end
      sp_cost = self.skill.sp_cost 
      sp_cost = (sp_cost / 2.0).ceil if @actor.states.include?(31) 
      text = self.skill.name
      text += " (#{sp_cost} #{$data_system.words.sp})" unless sp_cost == 0
      @help_window.set_text(text, 1, color, self.skill.description)
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
    x = @index % @column_max * 96 + 4
    y = @index / @column_max * 32 - self.oy
    self.cursor_rect.set(x, y, 96, 32)
  end
  
end
