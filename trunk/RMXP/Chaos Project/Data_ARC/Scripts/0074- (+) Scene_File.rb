#==============================================================================
# Window_Base
#==============================================================================

class Window_Base < Window

  def draw_actor_exp_alt(actor, x, y)
    self.contents.font.color = system_color
    self.contents.draw_text(x, y, 64, 32, 'next')
    self.contents.font.color = normal_color
    self.contents.draw_text(x + 56, y, 84, 32, actor.next_rest_exp_s, 2)
  end

  alias draw_actor_exp_new2 draw_actor_exp_alt
  def draw_actor_exp_alt(actor, x, y, w = 148)
    w -= 12
    if actor.next_exp == 0
      rate = 1
    else
      rate = actor.now_exp.to_f / actor.next_exp
      if rate < 0
        rate = 0
      elsif rate > 1
        rate = 1
      end
    end
    if rate < 0.5
      color1 = Color.new(20 * rate, 60, 80, 192) 
      color2 = Color.new(60 * rate, 180, 240, 192) 
    elsif rate >= 0.5
      color1 = Color.new(20 + 120 * (rate-0.5), 60 + 40 * (rate-0.5), 80, 192) 
      color2 = Color.new(60 + 360 * (rate-0.5), 180 + 120 * (rate-0.5), 240, 192) 
    end
    color3 = Color.new(80, 80, 80, 192)
    self.contents.gradient_bar(x, y, w, color1, color2, color3, rate)
    draw_actor_exp_new2(actor, x, y)
  end

end

#==============================================================================
# Window_SaveFile
#==============================================================================

class Window_SaveFile < Window_Base
  
  attr_reader   :filename
  attr_reader   :selected
  
  def initialize(file_index, filename)
    super(0, 64 + file_index % 8 * 50, 96, 64)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.contents.font.name = $fontface
    self.contents.font.size = $fontsize
    self.contents.font.bold = true if self.contents.font.name == 'Papyrus'    
    self.z, self.opacity = 10000, 0
    @file_index = file_index
    @filename = CP.saves + "Chaos#{@file_index + 1}.cps"
    self.contents.draw_text(4, 0, width - 40, 32, "No. #{@file_index+1}", 1)
    @selected = false
  end
  
  def selected=(selected)
    @selected = selected
    update_cursor_rect
  end

  def update_cursor_rect
    if @selected
      self.cursor_rect.set(0, 0, self.width-32, 32)
    else
      self.cursor_rect.empty
    end
  end

end

#==============================================================================
# Window_FileStatus
#==============================================================================

class Window_FileStatus < Window_Base
    
  def refresh(flag = true)
    self.load if flag
    if @file_exist
      save_system = $game_system
      $game_system = @game_system
      save_party = $game_party
      $game_party = @game_party
      save_switches = $game_switches
      $game_switches = @game_switches
      self.contents.clear
      @item_max = @game_party.actors.size
      if @game_map.is_a?(Numeric)
        map_name = CP.map_name(@game_map, @game_switches)
      else
        map_name = CP.map_name(@game_map.map_id, @game_switches)
      end
      map_name.gsub!('/') {' '}
      if map_name.clone.gsub!('Hyperion') {''} == nil
        case @game_variables[23]
        when 1 then map_name += ' / Arthia'
        when 2 then map_name += ' / Kadro'
        end
      end
      self.contents.font.bold = true if self.contents.font.name == 'Papyrus'    
      @game_party.actors.each_index {|i|
          self.contents.font.color = normal_color
          draw_actor_face(@game_party.actors[i], 14, i*88+48)
          draw_actor_name2(@game_party.actors[i], 4, i*88+28, 100)
          draw_actor_level(@game_party.actors[i], 112, i*88+28)
          draw_actor_state(@game_party.actors[i], 172, i*88+28, 252, 0)
          draw_actor_hp(@game_party.actors[i], 112, i*88+52)
          draw_actor_sp(@game_party.actors[i], 272, i*88+52)
          draw_actor_sr(@game_party.actors[i], 112, i*88+80)
          draw_actor_exp_alt(@game_party.actors[i], 272, i*88+80)}
      @total_sec = 359999 if @total_sec > 359999
      hour = @total_sec / 60 / 60
      min = @total_sec / 60 % 60
      sec = @total_sec % 60
      time_string = @time_stamp.strftime('%d.%m.%Y %H:%M')
      time_string2 = sprintf('%02d:%02d:%02d', hour, min, sec)
      if map_name.clone.gsub!('Hyperion') {''} == nil &&
          map_name.clone.gsub!('Cravgon') {''} == nil &&
          map_name.clone.gsub!('Unknown Aircraft') {''} == nil &&
          map_name.clone.gsub!('Unbekanntes Flugschiff') {''} == nil &&
          map_name.clone.gsub!('Unknown Laboratory') {''} == nil &&
          map_name.clone.gsub!('Unbekanntes Labor') {''} == nil
        if @game_switches[26]
          time_string3 = 'Day'
        elsif @game_switches[27]
          time_string3 = 'Night'
        else
          time_string3 = ''
        end
      else
        time_string3 = ''
      end
      if @game_system.exp_rate == 4
        mode_text = '4×EXP'
        self.contents.font.color = text_color(3)
      elsif @game_system.exp_rate == 0.5
        mode_text = '0.5×EXP'
        self.contents.font.color = text_color(6)
      elsif @game_party.test_exerion
        mode_text = 'Exerion'
        self.contents.font.color = text_color(2)
      else
        mode_text = ''
      end
      save_font = self.contents.font.name
      self.contents.font.name = 'Geometrix'
      self.contents.draw_text(192, 318, 320, 32, mode_text, 2)
      self.contents.font.name = save_font
      self.contents.font.color = system_color
      self.contents.draw_text(192, 0, 320, 32, time_string, 2)
      self.contents.draw_text(192, 28, 320, 32, time_string2, 2)
      self.contents.draw_text(192, 56, 320, 32, time_string3, 2)
      self.contents.draw_text(0, 0, 320, 32, map_name, 0)
      self.contents.font.color = normal_color
      self.contents.font.name = 'EurostileExtended-Roman-DTC'
      self.contents.font.bold = true
      self.contents.font.size = 14
      if $game_system.release == 'Final Demo'
        $game_system.update_version($game_system.version, 'Demo')
      end
      self.contents.draw_text(0, 342, 512, 32, $game_system.release, 2)
      self.contents.draw_text(0, 356, 512, 32, CP.ver, 2)
      $game_system = save_system
      $game_party = save_party
      $game_switches = save_switches
    end
    Input.update
    @refreshed = true
  end

end

#==============================================================================
# Window_Caution
#==============================================================================

class Window_Caution < Window_Base

  def initialize(w, h)
    x, y = 320 - w/2, 240 - h/2
    super(x, y, w, h)
    self.contents = Bitmap.new(w - 32, h - 32)
    self.contents.font.name = 'Geometrix'
    self.visible = false
    self.opacity = 192
    self.z = 15000
    self.windowskin = RPG::Cache.windowskin('Black Death')
  end

  def refresh
    self.contents.clear
    self.visible = true
    text = 'Data successfully saved.'
    self.width = self.contents.text_size(text).width + 40
    self.contents.dispose
    self.contents = Bitmap.new(self.width - 32, self.height - 32)
    self.x = 320 - self.width / 2
    self.contents.font.color = normal_color
    self.contents.draw_text(0, 0, width-32, 32, text, 1)
  end
  
end

#==============================================================================
# Scene_File
#==============================================================================

class Scene_File
  
  def initialize(help_text)
    @help_text = help_text
  end
  
  def main
    save_sys = $game_system
    @caution_window = Window_Caution.new(160, 64)
    @filestatus_windows = []
    @savefile_windows = []
    @dummy_window = Window_Base.new(0, 64, 96, 416)
    @dummy_window.z = 10000
    CP::Cache::SaveGames.each {|i|
        @filestatus_windows.push(Window_FileStatus.new(i, make_filename(i)))
        @savefile_windows.push(Window_SaveFile.new(i, make_filename(i)))}
    @help_window = Window_Help.new
    @help_window.set_text(@help_text)
    @help_window.z = 10000
    @file_index = $game_temp.last_file_index
    @savefile_windows[@file_index].selected = true
    CP::Cache::SaveGames.each {|i| @filestatus_windows[i].visible = (@file_index == i)}
    Graphics.transition
    loop do
      Graphics.update
      Input.update
      update
      Audio.bgs_stop if self.is_a?(Scene_Load)
      break if $scene != self
    end
    if save_sys != $game_system && $game != nil
      20.times {Graphics.update}
      $game.dispose
      $game = nil
    end
    Graphics.freeze
    @help_window.dispose
    (@savefile_windows | @filestatus_windows).each {|i| i.dispose}
    @caution_window.dispose
    @dummy_window.dispose
    if save_sys != $game_system
      if $game != nil
        $game.dispose
        $game = nil
      end
      if $game_system.exp_rate == 4
        CP.unlock(1)
      elsif $game_system.exp_rate == 0.5
        CP.unlock(2)
      elsif $game_party != nil && $game_party.test_exerion
        CP.unlock(3)
      end
      Audio.bgm_fade(1000)
      Graphics.transition(20)
      Graphics.freeze
      Graphics.transition(40)
      Graphics.freeze
      $game_system.bgm_play($game_system.playing_bgm)
      $game_system.bgs_play($game_system.playing_bgs)
    elsif !$scene.is_a?(Scene_Title) && !$scene.is_a?(Scene_Gameover)
      Graphics.transition
      Graphics.freeze
    end
  end
  
  def update
    CP::Cache::SaveGames.each {|i| @filestatus_windows[i].visible = (@file_index == i)}
    unless @filestatus_windows[@file_index].refreshed
      @filestatus_windows[@file_index].refresh
    end
    @help_window.update
    @savefile_windows.each {|win| win.update}
    if Input.trigger?($controls.confirm)
      on_decision(@file_index)
      $game_temp.last_file_index = @file_index
    elsif Input.trigger?($controls.cancel)
      $game_system = Game_System.new if $game_system == nil
      on_cancel
    elsif Input.repeat?($controls.down)
      if Input.trigger?($controls.down) || @file_index < 7
        $game_system.se_play($data_system.cursor_se)
        @savefile_windows[@file_index].selected = false
        @file_index = (@file_index + 1) % 8
        @savefile_windows[@file_index].selected = true
      end
    elsif Input.repeat?($controls.up)
      if Input.trigger?($controls.up) || @file_index > 0
        $game_system.se_play($data_system.cursor_se)
        @savefile_windows[@file_index].selected = false
        @file_index = (@file_index + 7) % 8
        @savefile_windows[@file_index].selected = true
      end
    end
  end
  
  def make_filename(file_index)
    return CP.saves + "Chaos#{file_index + 1}.cps"
  end
  
end
