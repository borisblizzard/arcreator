#==============================================================================
# Scene_Load
#==============================================================================

class Scene_Load < Scene_File
  
  def initialize
    $fontface = 'Geometrix'
    $game_temp = Game_Temp.new if $game_temp == nil
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
    old_system = $game_system
    read_save_data(file)
    file.close
    old_system.se_play($data_system.load_se)
    $game_map.update
    $game_temp = Game_Temp.new
    $scene = Scene_Map.new
  end
  
  def on_cancel
    $game_system.se_play($data_system.cancel_se)
    $scene = Scene_Title.new
  end
  
end
