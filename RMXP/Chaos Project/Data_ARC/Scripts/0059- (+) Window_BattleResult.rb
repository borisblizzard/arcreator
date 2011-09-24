#==============================================================================
# Window_BattleResult
#==============================================================================

class Window_BattleResult < Window_Base

  def initialize(exp, gold, treasures)
    @exp, @gold, @treasures = exp, gold, get_treasures(treasures)
    super(160, 0, 320, @treasures[0].size*32 + 64)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.contents.font.name = $fontface
    self.contents.font.size = $fontsize
    self.contents.font.bold = true if $fontface == 'Papyrus'    
    self.y = 160-height/2
    self.back_opacity = 160
    self.visible = false
    self.z = 9999
    refresh
  end
  
  def refresh
    self.contents.clear
    gold, x = @gold, 4
    cx = contents.text_size('Found').width
    self.contents.font.color = system_color
    self.contents.draw_text(x, 0, cx, 32, 'Found')
    x += cx + 4
    gold = 'no' if @gold == 0
    cx = contents.text_size(gold.to_s).width
    self.contents.font.color = normal_color
    self.contents.draw_text(x, 0, cx, 32, gold.to_s)
    x += cx + 4
    self.contents.font.color = system_color
    self.contents.draw_text(x, 0, 128, 32, $data_system.words.gold)
    @treasures[0].each_index {|i|
        draw_item(@treasures[0][i], 4, (i+1)*32, @treasures[1][i])}
  end
  
  def get_treasures(treasures)
    items, weapons, armors, stuff, qua = [], [], [], [], []
    treasures.each {|i|
        case i
        when RPG::Item then items.push(i)
        when RPG::Weapon then weapons.push(i)
        when RPG::Armor then armors.push(i)
        end}
    items.each {|i|
        if stuff.include?(i)
          qua[stuff.index(i)] += 1
        else
          stuff.push(i)
          qua.push(1)
        end}
    weapons.each {|i|
        if stuff.include?(i)
          qua[stuff.index(i)] += 1
        else
          stuff.push(i)
          qua.push(1)
        end}
    armors.each {|i|
        if stuff.include?(i)
          qua[stuff.index(i)] += 1
        else
          stuff.push(i)
          qua.push(1)
        end}
    return [stuff, qua]
  end
    
  def draw_item(item, x, y, qua = 1)
    return if item == nil
    w1 = self.contents.text_size('0').width
    save_font = self.contents.font.name
    self.contents.font.name = 'Arial'
    w2 = self.contents.text_size('× ').width
    self.contents.font.name = save_font
    x += w1 + w2 + 4
    bitmap = RPG::Cache.icon(item.icon_name)
    self.contents.font.color = system_color
    save_font = self.contents.font.name
    self.contents.font.name = 'Arial'
    self.contents.font.bold = false
    self.contents.draw_text(w1 + 8, y + 2, w2, 32, '×')
    self.contents.font.name = save_font
    self.contents.font.bold = true if save_font == 'Papyrus'
    self.contents.blt(x, y + 4, bitmap, Rect.new(0, 0, 24, 24))
    self.contents.font.color = normal_color
    self.contents.draw_text(4, y, w1, 32, qua.to_s, 2)
    self.contents.draw_text(x + 28, y, 212, 32, item.name)
  end
  
end
