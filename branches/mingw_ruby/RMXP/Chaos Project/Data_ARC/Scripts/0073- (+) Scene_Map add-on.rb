#==============================================================================
# Window_Battle
#==============================================================================

class Window_Battle < Window_Selectable

  attr_reader   :fade_in
  attr_accessor :fade_out
  attr_accessor :mode
  
  def initialize
    super(80, 232, 480, 480)
    self.opacity = 0
    @mode = -1
    @item_max = 0
    bitmap = Bitmap.new(self.width - 32, self.height - 32)
    @cursor_width = bitmap.text_size('Yes').width + 24
    bitmap.dispose
    self.windowskin = RPG::Cache.windowskin('Black Death')
    @fade_in = true
    @fade_out = false
    self.height = 16
    self.z = 1100
  end
  
  def refresh
    self.contents = Bitmap.new(self.width - 32, self.height - 32)
    self.contents.font.name = $fontface
    self.contents.font.size = $fontsize
    self.contents.font.bold = true if $fontface == 'Papyrus'
    if @mode == 1
      self.contents.draw_text(20, 32, 96, 32, 'Yes')
      self.contents.draw_text(20, 64, 96, 32, 'No')
    end
    self.contents.draw_text(4, 0, self.width-40, 32, @text, 1)
  end
  
  def update
    super
    if @fade_in
      make_mode if @mode == -1
      if @mode == 3 || @mode == 4
        @fade_in = false
      else
        self.opacity = 160
        if (@mode == 1 && self.height >= 128) || (@mode != 1 && self.height >= 64)
          self.height = (@mode == 1 ? 128 : 64)
          @fade_in = false
          refresh
          update_cursor_rect
        else
          self.height += 16
          self.y -= 8
        end
      end
    elsif @fade_out
      unless self.contents == nil
        self.contents.dispose
        self.contents = nil
      end
      if self.opacity == 0
        self.height = 16
        @fade_out = false
        @fade_in = true if @mode < 3
        $game_temp.battle_calling = [false, false] if @mode == 3
        @index = -1
      elsif self.height <= 16
        self.width = @wn
        self.x = 320 - self.width / 2
        self.opacity = 0
      else
        self.height -= 16
        self.y += 8
      end
    elsif @mode <= 5
      if Input.trigger?($controls.confirm)
        $game_system.se_play($data_system.decision_se) if @index >= 0
        if @index == 0 || @mode == 5
          @mode = 4
        elsif @mode == 0 || @mode == 2
          @mode = 4
          @flag = false
        elsif @mode == 1
          make_mode(true)
          self.contents.dispose
          self.contents = Bitmap.new(1, 1)
          self.contents.dispose
          self.contents = nil
        end
        @fade_out = true
        @index = -1
        update_cursor_rect
      elsif Input.trigger?($controls.cancel)
        $game_system.se_play($data_system.cancel_se) if @index >= 0
        if @mode == 0 || @mode == 2
          @mode = 4
          @flag = false
        elsif @mode == 1
          make_mode(true)
          self.contents.dispose
          self.contents = Bitmap.new(1, 1)
          self.contents.dispose
          self.contents = nil
        end
        @fade_out = true
        @index = -1
        update_cursor_rect
      end
    end
  end
  
  def update_cursor_rect
    if @index < 0 || self.contents == nil
      self.cursor_rect.empty
    else
      self.cursor_rect.set(12, @index * 32 + 32, @cursor_width, 32)
    end
  end
  
  def make_mode(val = false)
    unless val
      flag = $game_party.actors.any? {|actor| actor.armor4_id == 108 ||
          actor.armor5_id == 108 || actor.armor6_id == 108}
      @mode = ((flag || rand(50) < 15) ? 1 : 0)
    end
    if @mode == 1 && $game_system.encounter_mode == 1 || val
      flag = $game_party.actors.any? {|actor| actor.armor4_id == 107 ||
          actor.armor5_id == 107 || actor.armor6_id == 107}
      if flag
        @mode = 3
        return
      end
      @mode = 3 - rand(3)/2
      return if @mode == 3
    elsif @mode == 1 && $game_system.encounter_mode == 2
      @mode = 5
    end
    case @mode
    when 0
      @index = -1
      @item_max = 1
      @text = 'Surprised by an enemy!'
    when 1
      @index = 0
      @item_max = 2
      @text = 'Encountered enemy! Engage into combat?'
    when 2
      @index = -1
      @item_max = 1
      @text = 'Failed to evade a fight!'
      if self.contents != nil
        bitmap = Bitmap.new(self.width - 32, self.height - 32)
        bitmap.font.name = $fontface
        bitmap.font.size = $fontsize
        @wn = bitmap.text_size(@text).width + 48
        bitmap.dispose
        return
      end
    when 5
      @index = -1
      @item_max = 1
      @text = 'Engaging into combat!'
    end
    bitmap = Bitmap.new(self.width - 32, (self.height - 32).abs)
    bitmap.font.name = $fontface
    bitmap.font.size = $fontsize
    self.width = @wn = bitmap.text_size(@text).width + 48
    self.x = 320 - self.width / 2
    bitmap.dispose
  end
  
end

#==============================================================================
# Scene_Map
#==============================================================================

class Scene_Map
  
  alias main_battle_later main
  def main
    @battle_window = Window_Battle.new
    main_battle_later
    @battle_window.dispose if @battle_window != nil
  end
  
  alias update_stop_later update
  def update
    if @message_window.timer > -1 && @message_window.timer_active &&
        @message_window.frames != 2 * Graphics.frame_count / Graphics.frame_rate
      if @message_window.timer == 0 || Input.trigger?($controls.confirm)
        @message_window.timer_active = false
        @message_window.terminate_message
      end
      @message_window.frames = 2 * Graphics.frame_count / Graphics.frame_rate
      @message_window.timer -= 1
    end
    update_stop_later
  end
  
end

#==============================================================================
# Tilemap
#==============================================================================

class Tilemap
  
  alias upd_fps_later update
  def update
    upd_fps_later if Graphics.frame_count % 2 == 0
    upd_fps_later
  end
  
end
