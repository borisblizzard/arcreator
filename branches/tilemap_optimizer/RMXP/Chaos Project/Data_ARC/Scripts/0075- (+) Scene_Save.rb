#==============================================================================
# Scene_Save
#==============================================================================

class Scene_Save < Scene_File
  
  def initialize
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
    super('Which file do you wish to save to?')
  end
  
  def on_decision(file_index)
    filename = make_filename(file_index)
    $game_system.se_play($data_system.decision_se)
    file = File.open(filename, 'wb')
    write_save_data(file)
    file.close
    @filestatus_windows[file_index].reset
    @caution_window.refresh
    $game_system.se_play($data_system.save_se)
    Graphics.update
    Graphics.freeze
    Graphics.transition(30)
    if $game_temp.save_calling
      $game_temp.save_calling = false
      $scene = Scene_Map.new
    else
      $scene = Scene_Menu.new(0)
    end
  end
  
  def on_cancel
    $game_system.se_play($data_system.cancel_se)
    if $game_temp.save_calling
      $game_temp.save_calling = false
      $scene = Scene_Map.new
    else
      $scene = Scene_Menu.new(0)
    end
  end
  
end
