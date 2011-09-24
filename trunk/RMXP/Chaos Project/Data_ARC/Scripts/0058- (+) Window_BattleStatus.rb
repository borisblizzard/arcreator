#==============================================================================
# Window_BattleStatus
#==============================================================================

class Window_BattleStatus < Window_Base
  
  def initialize
    super(0, 320, 640, 160)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.contents.font.name = $fontface
    self.contents.font.size = 16
    self.contents.font.bold = true if $fontface == 'Papyrus'    
    refresh
  end
  
  def dispose
    super
  end
  
  def refresh
    self.contents.clear
    @item_max = $game_party.actors.size
    $game_party.actors.each_index {|i|
        save_font = self.contents.font.name
        self.contents.font.name = 'EurostileExtended-Roman-DTC'
        self.contents.font.bold = true
        actor = $game_party.actors[i]
        actor_x = case $game_party.actors.size
        when 1 then 4 + 240
        when 2 then 4 + 80 + i * 320
        when 3 then 4 + 80 + i * 160
        when 4 then 4 + i * 160
        end
        draw_actor_name2(actor, actor_x-10, -12, 128)
        self.contents.font.bold = true
        self.contents.font.size = 16
        draw_actor_hp(actor, actor_x, 14, 120)
        draw_actor_sp(actor, actor_x, 42, 120)
        draw_actor_sr(actor, actor_x, 70, 120)
        self.contents.font.bold = false unless save_font == 'Papyrus'
        self.contents.font.name = save_font 
        self.contents.font.color = normal_color
        size = ($fontface == 'Papyrus' ? 12 : 6)
        self.contents.font.size += size
        draw_actor_state(actor, actor_x, 100, 112)
        self.contents.font.size -= size}
  end
  
  def update
    super
    if $game_temp.battle_main_phase
      self.contents_opacity -= 12 if self.contents_opacity > 128
    else
      self.contents_opacity += 12 if self.contents_opacity < 255
    end
  end
  
end
