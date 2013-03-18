#==============================================================================
# Scene_Gameover
#==============================================================================

class Scene_Gameover
  
  def initialize(skip = false)
    @skip = skip
  end
  
  def main
    @sprite = Sprite.new
    @sprite.bitmap = RPG::Cache.gameover($data_system.gameover_name)
    unless @skip
      Audio.bgm_fade(800)
      Audio.bgs_fade(800)
      $game_system.me_play($data_system.gameover_me)
      Graphics.transition(200, 'Graphics/Gameovers/' + $data_system.gameover_name)
      loop do
        Graphics.update
        Input.update
        break if Input.trigger?($controls.confirm)
      end
      Graphics.freeze
    end
    $game_system.windowskin_name = 'MaxRed'
    $fontface = 'Geometrix'
    $fontsize = 24
    @command_window = Window_Command.new(200, ['Load', 'Back to title', 'Exit'])
    @command_window.x = 320 - @command_window.width / 2
    @command_window.y = 240 - @command_window.height / 2
    @continue = ((0...7).any? {|i| FileTest.exist?(CP.saves + "Chaos#{i+1}.cps")})
    @continue ? @command_window.index = 0 : @command_window.disable_item(0)
    Graphics.transition
    loop do
      Graphics.update
      Input.update
      update
      break if $scene != self
    end
    Graphics.freeze
    @command_window.dispose
    @sprite.dispose
    if $scene.is_a?(Scene_Title)
      Graphics.transition(20)
      Graphics.freeze
    end
  end

  def update
    @command_window.update
    if Input.trigger?($controls.confirm)
      case @command_window.index
      when 0 then command_continue
      when 1 then command_to_title
      when 2 then command_quit
      end
    end
  end

  def command_continue
    unless @continue
      $game_system.se_play($data_system.buzzer_se)
      return
    end
    $game_system.se_play($data_system.decision_se)
    $scene = Scene_GameoverLoad.new
  end

  def command_to_title
    $game_system.se_play($data_system.decision_se)
    Audio.me_stop
    $scene = Scene_Title.new
  end 

  def command_quit
    $game_system.se_play($data_system.decision_se)
    Audio.bgm_fade(800)
    Audio.bgs_fade(800)
    Audio.me_fade(800)
    $scene = nil
  end
  
end

#==============================================================================
# Scene_GameoverLoad
#==============================================================================

class Scene_GameoverLoad < Scene_File

  def initialize
    $game_temp = Game_Temp.new
    $game_temp.last_file_index = 0
    latest_time = Time.at(0)
    CP::Cache::SaveGames.each {|i|
        filename = make_filename(i)
        if FileTest.exist?(filename)
          file = File.open(filename, 'r')
          if file.mtime > latest_time
            latest_time = file.mtime
            $game_temp.last_file_index = i
          end
          file.close
        end}
    super('Which file do you wish to load from?')
  end
  
  def on_decision(file_index)
    filename = make_filename(file_index)
    unless FileTest.exist?(filename) && @filestatus_windows[file_index].file_exist
      $game_system.se_play($data_system.buzzer_se)
      return
    end
    $game_system.se_play($data_system.decision_se)
    file = File.open(filename, 'rb')
    read_save_data(file)
    file.close
    $game_system.se_play($data_system.load_se)
    Audio.me_stop
    $game_map.update
    $scene = Scene_Map.new
  end

  def on_cancel
    $game_system.se_play($data_system.cancel_se)
    $scene = Scene_Gameover.new(true)
  end

end
