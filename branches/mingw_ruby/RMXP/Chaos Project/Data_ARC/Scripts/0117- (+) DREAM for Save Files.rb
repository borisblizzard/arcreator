#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=
# DREAM controller for Save Files by Blizzard
# Version: 3.0
# Type: Encryptor / Decryptor
# uses DREAM v4.0 or higher
# Date 22.7.2006
# Date v2.0: 25.1.2007
# Date v3.0: 19.8.2007
#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=

DREAM.initialize

#==============================================================================
# SaveFile_DREAM
#==============================================================================

class SaveFile_DREAM
  
  attr_reader :game_data
  attr_reader :game_frame
  attr_reader :_sys
  attr_reader :_swi
  attr_reader :_var
  attr_reader :_party
  attr_reader :_map
  attr_reader :_player
  attr_reader :_font
  
  def initialize
    @_party, @game_data = [], []
    @_sys = @_swi = @_var = @_map = @_player = 0
    if $game_party != nil
      $game_party.actors.each {|actor|
          @game_data.push([actor.character_name, actor.character_hue])}
    end
    @game_frame = Graphics.frame_count
  end  
        
  def encrypt_data(file)
    $game_system.save_count += 1
    $game_system.magic_number = $data_system.magic_number
    $game_troop.clear
    sys = [@game_data, @game_frame, $game_system, $game_switches,
        $game_variables, $game_self_switches, $game_screen, $game_actors,
        $game_party, $game_troop, $game_map.map_id, $game_player, $fontface]
    sys = DREAM.create_encryption_pattern(DREAM.dream4_encryption(sys), sys)
    DREAM.dat(file, sys)
    $game.contents.progress_bar($game.width-40, 1, 0)
    Graphics.update
  end
  
  def get_data(file)
    sys = DREAM.dat(file, true)
    if sys[0].is_a?(String) && sys[0].clone.sub!(/DREAM v4.x/) {} != nil
      res, sys = DREAM.read_encryption_pattern(sys)
      sys = DREAM.dream4_decryption(res, sys)
    else
      sys = DREAM.decode_old_dream(sys)
    end
    @game_data, @game_frame, @_sys, @_swi, @_var, @_party, @_map, @_player,
    @_font = sys[0], sys[1], sys[2], sys[3], sys[4], sys[8], sys[10], sys[11],
    sys[12]
  end
  
  def restore_game(file)
    sys = DREAM.dat(file, true)
    if sys[0].is_a?(String) && sys[0].clone.sub!(/DREAM v4.x/) {} != nil
      res, sys = DREAM.read_encryption_pattern(sys)
      sys = DREAM.dream4_decryption(res, sys)
    else
      sys = DREAM.decode_old_dream(sys)
    end
    sys.shift
    Graphics.frame_count, $game_system, $game_switches, $game_variables,
    $game_self_switches, $game_screen, $game_actors, $game_party, $game_troop,
    $game_map, $game_player, $fontface = sys
    $fontface = 'Geometrix' if $fontface == 'Comic Sans MS' || $fontface == 'Tahoma'
    $fontsize = ($fontface == 'Papyrus' ? 30 : 24)
    if $game_map.is_a?(Game_Map)
      map_id = $game_map.map_id
    else
      map_id, $game_map = $game_map, Game_Map.new
    end
    $game_map.setup(map_id)
    $game_player.center($game_player.x, $game_player.y)
    [$game_party, $game_player].each {|i| i.refresh}
    $game_troop = Game_Troop.new if $game_troop == nil
    $game.contents.progress_bar($game.width-40, 1, 0)
    Graphics.update
  end
  
end

#==============================================================================
# Bitmap
#==============================================================================

class Bitmap
  
  def progress_bar(width, fill_rate, type)
    case type
    when 0 then color1, color2 = Color.new(0, 80, 0), Color.new(0, 240, 0)
    when 1 then color1, color2 = Color.new(80, 0, 0), Color.new(240, 0, 0)
    when 2 then color1, color2 = Color.new(80, 80, 0), Color.new(240, 240, 0)
    end
    fill_rect(3, 40, width+2, 8, Color.new(255, 255, 255))
    fill_rect(4, 41, width, 6, Color.new(0, 0, 0))
    (0...(width * fill_rate).to_i).each {|i|
        red = color1.red + (color2.red - color1.red) * i / width
        green = color1.green + (color2.green - color1.green) * i / width
        blue = color1.blue + (color2.blue - color1.blue) * i / width
        fill_rect(4+i, 41, 1, 6, Color.new(red, green, blue))}
  end

end

#==============================================================================
# Scene_Save
#==============================================================================

class Scene_Save < Scene_File
  
  def write_save_data(file)
    code = SaveFile_DREAM.new
    CP.make_game_text(false)
    code.encrypt_data(file)
    4.times {Graphics.update}
    $game.dispose
    $game = nil
  end
  
  alias on_decision_DREAM_later on_decision
  def on_decision(file_index)
    filename = make_filename(file_index)
    if FileTest.exist?(filename) && FileTest.size(filename) > 10
      FileUtils.copy(filename, filename + '.bkup')
    end
    on_decision_DREAM_later(file_index)
  end
  
end

#==============================================================================
# Scene_Load
#==============================================================================

class Scene_Load < Scene_File
  
  def read_save_data(file)
    code = SaveFile_DREAM.new
    CP.make_game_text
    code.restore_game(file)
  end

end

#==============================================================================
# Scene_NewLoad
#==============================================================================

class Scene_NewLoad < Scene_File
  
  def read_save_data(file)
    code = SaveFile_DREAM.new
    CP.make_game_text
    code.restore_game(file)
  end

end

#==============================================================================
# Scene_NewLoad
#==============================================================================

class Scene_GameoverLoad < Scene_File
  
  def read_save_data(file)
    code = SaveFile_DREAM.new
    CP.make_game_text
    code.restore_game(file)
  end

end

#==============================================================================
# Window_FileStatus
#==============================================================================

class Window_FileStatus < Window_Base
  
  attr_reader :file_exist
  attr_reader :refreshed
  
  def initialize(file_index, filename)
    super(0, 64, 544, 416)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.x, self.y, self.z = 96, 64, 10000
    self.contents.font.name = $fontface
    self.contents.font.size = $fontsize
    self.contents.font.bold = true if $fontface == 'Papyrus'    
    @refreshed = @selected = false
    self.opacity = @map_infos = 0
    @file_index = file_index
    @filename = CP.saves + "Chaos#{@file_index + 1}.cps"
    @time_stamp = Time.at(0)
    @file_exist = FileTest.exist?(@filename)
  end
  
  def load
    if @file_exist
      file = File.open(@filename, 'r')
      @time_stamp = file.mtime
      code = SaveFile_DREAM.new
      self.contents.font.size = 22
      text = 'Loading file...'
      w = contents.text_size(text).width + 4
      x = self.contents.width / 2 - w / 2
      y = self.contents.height / 2 - 16
      self.contents.draw_text(x, y, w, 32, text)
      Graphics.update
      begin
        code.get_data(file)
        @characters = code.game_data
        @frame_count = code.game_frame
        @game_system = code._sys
        @game_switches = code._swi
        @game_variables = code._var
        @game_map = code._map
        @game_party = code._party
        @map_infos = (@game_map.is_a?(Numeric) ? @game_map : @game_map.map_id)
        self.windowskin = RPG::Cache.windowskin(@game_system.windowskin_name)
        self.contents.font.name = code._font
        if self.contents.font.name == 'Comic Sans MS' ||
            self.contents.font.name == 'Tahoma'
          self.contents.font.name = 'Geometrix'
        end
        @total_sec = @frame_count / Graphics.frame_rate
        self.opacity = 255
        if self.contents.font.name == 'Papyrus'
          self.contents.font.size = 28
          self.contents.font.bold = true
        else
          self.contents.font.size = 22
          self.contents.font.bold = false
        end
      rescue
        self.contents.clear
        self.contents.font.size = 22
        text = 'Corrupted save data'
        w = contents.text_size(text).width + 4
        x = self.contents.width / 2 - w / 2
        y = self.contents.height / 2 - 16
        self.contents.font.color = Color.new(255, 0, 0)
        self.contents.draw_text(x, y, w, 32, text)
        self.opacity = 0
        @file_exist = false
      end
      file.close
    else
      self.contents.font.size = 22
      text = 'No saved data'
      w = contents.text_size(text).width + 4
      x = self.contents.width / 2 - w / 2
      y = self.contents.height / 2 - 16
      self.contents.draw_text(x, y, w, 32, text)
      self.opacity = 0
    end
  end
  
  def reset
    @file_exist = true
    @time_stamp = Time.now
    @frame_count = Graphics.frame_count
    @game_system = $game_system
    @game_switches = $game_switches
    @game_variables = $game_variables
    @game_map = $game_map
    @game_party = $game_party
    @map_infos = (@game_map.is_a?(Numeric) ? @game_map : @game_map.map_id)
    self.windowskin = RPG::Cache.windowskin(@game_system.windowskin_name)
    self.contents.font.name = $fontface
    @total_sec = @frame_count / Graphics.frame_rate
    self.opacity = 255
    if self.contents.font.name == 'Papyrus'
      self.contents.font.size = 28
      self.contents.font.bold = true
    else
      self.contents.font.size = 22
      self.contents.font.bold = false
    end
    refresh(false)
  end
  
end
