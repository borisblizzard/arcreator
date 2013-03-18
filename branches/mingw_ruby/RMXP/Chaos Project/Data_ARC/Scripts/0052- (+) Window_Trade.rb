#==============================================================================
# Window_Trade
#==============================================================================

class Window_Trade < Window_Base
  
  def initialize(override = false)
    super(0, 0, 192, 64)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.contents.font.name = $fontface
    self.contents.font.size = $fontsize
    self.contents.font.bold = true if $fontface == 'Papyrus'
    @override = override
    refresh
  end
  
  def refresh
    self.contents.clear
    if !@override && $game_variables[107].is_a?(Array)
      cx = 0
      $game_variables[107].each {|id|
          w = contents.text_size($data_items[id].name).width
          cx = w if cx < w}
      self.width = cx/32*32 + 128
      self.height = ($game_variables[107].size+1)*32
      self.contents.dispose
      self.contents = Bitmap.new(width - 32, height - 32)
      if $scene.is_a?(Scene_Shop)
        self.contents.fill_rect(0, 0, width, height, Color.new(0, 0, 0, 160))
      end
      self.contents.font.size = $fontsize
      $game_variables[107].each_index {|i|
          id = $game_variables[107][i]
          self.contents.font.color = system_color
          self.contents.font.name = 'Arial'
          self.contents.font.bold = false
          self.contents.draw_text(self.width-cx-56, i*32 + 2, 16, 32, '×')
          self.contents.font.name = $fontface
          self.contents.font.bold = true if $fontface == 'Papyrus'
          self.contents.draw_text(self.width-cx-40, i*32, cx+4, 32, $data_items[id].name)
          self.contents.font.color = normal_color
          self.contents.draw_text(self.width-cx-100, i*32, 40, 32, $game_party.item_number(id).to_s, 2)}
    elsif !@override && $game_variables[107] > 0
      cx = contents.text_size($data_items[$game_variables[107]].name).width
      self.width = cx/32*32 + 128
      self.contents.dispose
      self.contents = Bitmap.new(width - 32, height - 32)
      if $scene.is_a?(Scene_Shop)
        self.contents.fill_rect(0, 0, width, height, Color.new(0, 0, 0, 160))
      end
      self.contents.font.color = system_color
      self.contents.font.size = $fontsize
      self.contents.font.name = 'Arial'
      self.contents.font.bold = false
      self.contents.draw_text(self.width-cx-56, 2, 16, 32, '×')
      self.contents.font.name = $fontface
      self.contents.font.bold = true if $fontface == 'Papyrus'
      self.contents.draw_text(self.width-cx-40, 0, cx+4, 32, $data_items[$game_variables[107]].name)
      self.contents.font.color = normal_color
      self.contents.draw_text(self.width-cx-100, 0, 40, 32, $game_party.item_number($game_variables[107]).to_s, 2)
    else
      if $scene.is_a?(Scene_Shop)
        self.contents.fill_rect(0, 0, width, height, Color.new(0, 0, 0, 160))
      end
      cx = contents.text_size($data_system.words.gold).width
      self.contents.font.color = system_color
      self.contents.draw_text(156-cx, 0, cx, 32, $data_system.words.gold, 2)
      self.contents.font.color = normal_color
      self.contents.draw_text(0, 0, 152-cx, 32, $game_party.gold.to_s, 2)
    end
  end
  
end
