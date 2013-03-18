SWITCHES = [51, 53, 65, 56, 58, 59, 61, 62, 68, 70, 73, 74, 80, 81, 82, 83, 84,
            87, 88, 89, 91, 92, 102, 104, 105, 106, 108]

#==============================================================================
# Window_Update
#==============================================================================

class Window_Update < Window_Base
  
  def initialize
    super(32, 32, 576, 416)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.contents.font.name = $fontface
    self.contents.font.size = $fontsize
    self.contents.font.bold = true if $fontface == 'Papyrus'    
    self.windowskin = RPG::Cache.windowskin('Original')
    refresh
  end
  
  def refresh(type = 'Initialized',
              version = "Press #{CP.controls_name($controls.confirm)}",
              to_version = 'continue', progress = 0, current = '')
    self.contents.clear
    save = 'Savegame Update Version: '
    self.contents.draw_text(0, 0, 544, 32, "#{save}#{CP.ver($version)}", 1)
    flag = (version == "Press #{CP.controls_name($controls.confirm)}")
    self.contents.update_bar(32, 128, 480, progress)
    self.contents.draw_text(0, 224, 544, 32, type, 1)
    text = version + ' to ' + to_version
    text = "Press #{CP.controls_name($controls.confirm)} to continue" if flag
    self.contents.draw_text(0, 256, 544, 32, text, 1)
    return if flag
    self.contents.draw_text(0, 288, 544, 32, "#{(progress/10.0).round}%", 1)
    self.contents.draw_text(0, self.height - 96, self.width - 32, 32, current, 1)
  end
  
end

#==============================================================================
# Bitmap
#==============================================================================

class Bitmap
  
  def update_bar(x, y, w, rate)
    fill_rect(x, y, w+4, 24, Color.new(0, 0, 0))
    fill_rect(x+1, y+1, w+2, 22, Color.new(255, 255, 255))
    fill_rect(x+2, y+2, w, 20, Color.new(0, 0, 0, 160))
    blt(x+2, y+2, CP::Cache.image('update_bar'), Rect.new(0, 0, rate*w/1000.0, 24))
  end
  
end

#==============================================================================
# Game_System
#==============================================================================

class Game_System
  
  attr_reader :version
  attr_reader :release

  alias init_update_later initialize
  def initialize
    init_update_later
    update_version
  end
  
  def update_version(version = $version, release = $release)
    @version, @release = version, release
    @version_history = [] if @version_history == nil
    @version_history.push(version)
  end
  
  def print_version
    p "#{@release} ver. #{@version} <= #{@version_history.inspect}"
  end
  
end

#==============================================================================
# Scene_Map
#==============================================================================

class Scene_Map
  
  alias main_savegame_update_later main
  def main
    if $game_system.version == $version && $game_system.release == $release
      main_savegame_update_later
    else
      $scene = Scene_Update.new
    end
  end
  
end

#==============================================================================
# Scene_Update
#==============================================================================

class Scene_Update
  
  def main
    if $game_system.release == nil
      raise 'Fatal error. The version of the savegame cannot be updated. Chaos' +
      ' Project will leave the savegame unchanged and exit.'
    elsif $game_system.version < $version && $game_system.release == $release ||
        CP::Cache::Releases[$game_system.release] < CP::Cache::Releases[$release]
      @update_window = Window_Update.new
      Graphics.transition(10)
      loop do
        Graphics.update
        Input.update
        if Input.trigger?($controls.confirm)
          $game_system.se_play($data_system.decision_se)
          break
        end
      end
      if CP::Cache::Releases[$game_system.release] < 2
        update_final_demo
        if CP::Cache::Releases[$release] >= 2
          $game_system.update_version(0.0)
          update_full_game
        end
      elsif CP::Cache::Releases[$game_system.release] >= 2
        update_full_game
      end
      @update_window.refresh('Update successful',
          "Press #{CP.controls_name($controls.confirm)}",
          CP.ver($version), 1000)
      $game_system.se_play($data_system.save_se)
      loop do
        Graphics.update
        Input.update
        if Input.trigger?($controls.confirm)
          $game_system.se_play($data_system.decision_se)
          break
        end
      end
      Graphics.freeze
      $game_system.update_version
      @update_window.dispose
    elsif $game_system.version > $version && $game_system.release == $release ||
        CP::Cache::Releases[$game_system.release] > CP::Cache::Releases[$release]
      p 'Fatal error. This savegame was saved with a newer version/release' +
      ' of Lexima 4 than the one you are running ' +
      'right now. A "downgrade" is not possible.'
      raise "Savegame: #{CP.ver}    " +
      "Savegame release:  #{$game_system.release}    " +
      "Game: #{CP.ver($version)}    Game release:  #{$release}"
    else
      p 'An error has occured while comparing the versions and releases' +
      ' of the game and the savegame. Savegame cannot be updated. It is' +
      ' possible that the savegame version/release is newer than the game.'
      raise "Savegame: #{CP.ver}    " +
      "Savegame release:  #{$game_system.release}    " +
      "Game: #{CP.ver($version)}    Game release:  #{$release}"
    end
    $scene = Scene_Map.new
  end
  
  def update_full_game
    ver = $game_system.version
    ver = update_fg_1(ver) if ver < 1.000
    ver = update_fg_2(ver) if ver < 1.020
    ver = update_fg_3(ver) if ver < 1.103
    ver = update_fg_4(ver) if ver < 1.200
    ver = update_fg_5(ver) if ver < 1.220
  end
  
  def update_fg_5(tver)
    vver = 1.220
    nver, cver = CP.ver(vver), CP.ver(tver)
    @update_window.refresh('Finished', cver, nver, 1000, 'Version Update')
    screen
    return vver
  end
  
  def update_fg_4(tver)
    vver = 1.200
    nver, cver = CP.ver(vver), CP.ver(tver)
    @update_window.refresh('Correcting save position', cver, nver, 0, 'Updating Map')
    screen
    if $game_map.map_id == 538
      $game_player.moveto($game_player.x, $game_player.y + 1)
    end
    @update_window.refresh('Finished', cver, nver, 1000, 'Updating Map')
    screen
    return vver
  end
  
  def update_fg_3(tver)
    vver = 1.103
    nver, cver = CP.ver(vver), CP.ver(tver)
    @update_window.refresh('Finished', cver, nver, 1000, 'Version Update')
    screen
    return vver
  end
  
  def update_fg_2(tver)
    vver = 1.020
    nver, cver = CP.ver(vver), CP.ver(tver)
    @update_window.refresh('Changing quest outcome', cver, nver, 0, 'Updating Party')
    screen
    if $game_variables[8] == 5 && !$game_self_switches[[794, 7, 'A']]
      $game_party.gain_item(56, 1)
    end
    @update_window.refresh('Finished', cver, nver, 1000, 'Updating Party')
    screen
    return vver
  end
  
  def update_fg_1(tver)
    vver = 1.000
    nver, cver = CP.ver(vver), CP.ver(tver)
    (0..4).each {|i|
        @update_window.refresh('Setting new BGM format', cver, nver, i*100, 'Updating System')
        screen
        $game_system.unlock_bgm(i)}
    @update_window.refresh('Creating unique game ID', cver, nver, 500, 'Updating System')
    screen
    $game_variables[CP::Cache::GameID] = rand(1000000)
    @update_window.refresh('Reseting Custom Menu Mode', cver, nver, 600, 'Updating System')
    screen
    $game_system.menu_mode = 0
    @update_window.refresh('Setting new BGM format', cver, nver, 700, 'Updating System')
    screen
    if $game_system.battle_bgm.name == '28 - Fight 2'
      $game_system.battle_bgm.name = '28 - Fight 2 (Serious Sam Soundtrack)'
    end
    @update_window.refresh('Unlocking new BGM', cver, nver, 800, 'Updating System')
    screen
    $game_system.unlock_bgm(6) if $game_system.bgm_list.include?(5)
    @update_window.refresh('Unlocking new BGM', cver, nver, 900, 'Updating System')
    screen
    $game_system.unlock_bgm(5)
    @update_window.refresh('Changing BGM', cver, nver, 950, 'Updating System')
    screen
    unless $game_switches[BGM_Lock]
      change = Interpreter.new(0, false)
      change.setup($data_common_events[13].list, 13)
      change.setup_starting_event
      change.update
    end
    @update_window.refresh('Finished', cver, nver, 1000, 'Updating System')
    screen
    @update_window.refresh('Setting Switches', cver, nver, 0, 'Updating Switches')
    screen
    if $game_switches[280] || $game_variables[116] >= 9
      $game_self_switches[[515, 11, 'A']] = true
    end
    @update_window.refresh('Setting Switches', cver, nver, 100, 'Updating Switches')
    screen
    $game_switches[356] = true if $game_self_switches[[184, 23, 'A']]
    @update_window.refresh('Setting Switches', cver, nver, 200, 'Updating Switches')
    screen
    if $game_self_switches[[109, 32, 'A']]
      $game_self_switches[[109, 32, 'A']] = nil
      $game_self_switches[[724, 32, 'A']] = true
    end
    @update_window.refresh('Setting Switches', cver, nver, 300, 'Updating Switches')
    screen
    if $game_self_switches[[109, 33, 'A']]
      $game_self_switches[[109, 33, 'A']] = nil
      $game_self_switches[[723, 33, 'A']] = true
    end
    @update_window.refresh('Setting Switches', cver, nver, 400, 'Updating Switches')
    screen
    if $game_self_switches[[109, 27, 'A']]
      $game_self_switches[[109, 27, 'A']] = nil
      $game_self_switches[[725, 27, 'A']] = true
    end
    @update_window.refresh('Setting Switches', cver, nver, 500, 'Updating Switches')
    screen
    if $game_self_switches[[109, 31, 'A']]
      $game_self_switches[[109, 31, 'A']] = nil
      $game_self_switches[[725, 31, 'A']] = true
    end
    @update_window.refresh('Setting Switches', cver, nver, 600, 'Updating Switches')
    screen
    if $game_self_switches[[109, 13, 'A']]
      $game_self_switches[[109, 13, 'A']] = nil
      $game_self_switches[[726, 13, 'A']] = true
    end
    @update_window.refresh('Setting Switches', cver, nver, 700, 'Updating Switches')
    screen
    if $game_self_switches[[109, 34, 'A']]
      $game_self_switches[[109, 34, 'A']] = nil
      $game_self_switches[[727, 34, 'A']] = true
    end
    @update_window.refresh('Setting Switches', cver, nver, 800, 'Updating Switches')
    screen
    if $game_self_switches[[109, 59, 'A']]
      $game_self_switches[[109, 59, 'A']] = nil
      $game_self_switches[[727, 59, 'A']] = true
    end
    @update_window.refresh('Fixing Switches', cver, nver, 900, 'Updating Switches')
    screen
    $game_switches[424] = true
    @update_window.refresh('Finished', cver, nver, 1000, 'Updating Switches')
    screen
    @update_window.refresh('Correcting save position', cver, nver, 0, 'Updating Map')
    screen
    if $game_map.map_id == 49
      $game_player.moveto($game_player.x - 4, $game_player.y + 14)
    end
    @update_window.refresh('Correcting save position', cver, nver, 500, 'Updating Map')
    screen
    if $game_map.map_id == 109
      $game_player.moveto($game_player.x - 80, $game_player.y - 44)
    end
    @update_window.refresh('Finished', cver, nver, 1000, 'Updating Map')
    screen
    @update_window.refresh('Adding Items', cver, nver, 0, 'Updating Party')
    screen
    $game_party.gain_item(151, 1)
    @update_window.refresh('Finished', cver, nver, 1000, 'Updating Party')
    screen
    (1...$data_actors.size).each {|i|
        @update_window.refresh('Updating EXP List', cver, nver, (i-1)*1000/($data_actors.size-1), 'Updating Actors')
        Graphics.update
        $game_actors[i].make_exp_list
        $game_actors[i].fix_class
        $game_actors[i].exp += 0}
    @update_window.refresh('Finished', cver, nver, 1000, 'Updating Actors')
    screen
    return vver
  end
  
  def update_final_demo
    ver = $game_system.version
    ver = update_fd_1(ver) if ver < 1.042
    ver = update_fd_2(ver) if ver < 1.050
    ver = update_fd_3(ver) if ver < 1.051
    ver = update_fd_4(ver) if ver < 1.200
    ver = update_fd_5(ver) if ver < 1.600
    ver = update_fd_6(ver) if ver < 1.650
  end
  
  def update_fd_6(tver)
    vver = 1.650
    nver, cver = CP.ver(vver), CP.ver(tver)
    @update_window.refresh('Finished', cver, nver, 1000, 'Version Update')
    screen
    return vver
  end
  
  def update_fd_5(tver)
    vver = 1.600
    nver, cver = CP.ver(vver), CP.ver(tver)
    characters = [$game_player] | $game_map.events.values
    characters.each_index {|i|
        if i % 3 == 0
          @update_window.refresh('Setting Character Animation', cver, nver, i*1000/characters.size, 'Updating Characters')
          Graphics.update
        end
        characters[i].loop_id = 0}
    screen
    @update_window.refresh('Finished', cver, nver, 1000, 'Updating Characters')
    screen
    (1...$data_actors.size).each {|i|
        @update_window.refresh('Setting Battler Variables', cver, nver, (i-1)*333/($data_actors.size-1), 'Updating Actors')
        Graphics.update
        $game_actors[i].anima_index = $game_actors[i].anima_count = 0}
    screen
    (1...$data_actors.size).each {|i|
        @update_window.refresh('Setting Repeat Action', cver, nver, 333 + (i-1)*334/($data_actors.size-1), 'Updating Actors')
        Graphics.update
        $game_actors[i].def_mode = 0}
    screen
    (1...$data_actors.size).each {|i|
        @update_window.refresh('Updating EXP List', cver, nver, 667 + (i-1)*333/($data_actors.size-1), 'Updating Actors')
        Graphics.update
        $game_actors[i].make_exp_list
        $game_actors[i].fix_class
        $game_actors[i].exp += 0}
    @update_window.refresh('Finished', cver, nver, 1000, 'Updating Actors')
    screen
    @update_window.refresh('Setting new BGM format', cver, nver, 0, 'Updating System')
    screen
    if $game_system.battle_bgm.name == 'Astral Projection - Chaos ' +
        '(Bizzare Contact RMX, Blizzard Edit for CP - NW)'
      $game_system.battle_bgm.name = 'Astral Projection - Chaos ' +
          '(Bizzare Contact RMX, Blizzard Mix for CP)'
    elsif $game_system.battle_bgm.name == 'Astral Projection - Nilaya ' +
        '(Melicia RMX, Blizzard Edit for CP - NW)'
      $game_system.battle_bgm.name = 'Astral Projection - Nilaya ' +
          '(Melicia RMX, Blizzard Mix for CP)'
    end
    @update_window.refresh('Setting new BGM format', cver, nver, 250, 'Updating System')
    screen
    if $game_variables[BGM] > 1
      $game_variables[BGM] += 1
      unless $game_switches[BGM_Lock]
        change = Interpreter.new(0, false)
        change.setup($data_common_events[13].list, 13)
        change.setup_starting_event
        change.update
      end
    end
    @update_window.refresh('Fixing windowskin', cver, nver, 500, 'Updating System')
    screen
    if $game_system.windowskin_name == 'Black Death'
      $game_system.windowskin_name = 'Original'
    end
    @update_window.refresh('Fixing counter', cver, nver, 750, 'Updating System')
    screen
    $game_system.max_damage = 0
    @update_window.refresh('Finished', cver, nver, 1000, 'Updating System')
    screen
    if $game_variables[82] != 0
      $game_switches[204] = true if $game_variables[82] <= 12
      max = SWITCHES.size
    elsif $game_variables[79] > 0
      max = SWITCHES.size-5
    elsif $game_variables[28] > 0
      max = 3
    else
      max = 0
    end
    (0...max).each {|i|
        @update_window.refresh('Fixing Box switches', cver, nver, i*1000/(max+1), 'Updating Switches')
        Graphics.update
        $game_switches[SWITCHES[i]] = (!$game_switches[SWITCHES[i]])}
    @update_window.refresh('Finished', cver, nver, max*1000/((max+1)), 'Updating Switches')
    screen
    $game_switches[192] = true if $game_variables[7] == 0
    $game_switches[200], $game_switches[201] = false, true
    @update_window.refresh('Finished', cver, nver, 1000, 'Updating Switches')
    screen
    @update_window.refresh('Creating new Caterpillar', cver, nver, 0, 'Updating Caterpillar')
    screen
    $game_party.characters = nil
    $game_player.members = []
    (1...4).each {|i|
        @update_window.refresh('Creating new Caterpillar', cver, nver, (i-1)*333, 'Updating Caterpillar')
        screen
        member = Game_Member.new(i)
        member.moveto($game_player.x, $game_player.y)
        $game_player.members.push(member)}
    @update_window.refresh('Finished', cver, nver, 1000, 'Updating Caterpillar')
    screen
    return vver
  end
  
  def update_fd_4(tver)
    vver = 1.200
    nver, cver = CP.ver(vver), CP.ver(tver)
    @update_window.refresh('Adding Menu Mode', cver, nver, 0, 'Updating System')
    screen
    $game_system.menu_mode = 0
    @update_window.refresh('Adding Custom Menu Mode', cver, nver, 250, 'Updating System')
    screen
    $game_system.ex_mode = 0
    @update_window.refresh('Setting black font flag', cver, nver, 500, 'Updating System')
    screen
    $game_system.black_back = false
    @update_window.refresh('Setting Unity Force Mode', cver, nver, 750, 'Updating System')
    screen
    $game_system.uf_mode = false
    @update_window.refresh('Finished', cver, nver, 1000, 'Updating System')
    screen
    @update_window.refresh('Setting Cover', cver, nver, 0, 'Updating Characters')
    screen
    (1...$data_actors.size).each {|i| $game_actors[i].guarded_by = []}
    @update_window.refresh('Finished', cver, nver, 1000, 'Updating Characters')
    screen
    return vver
  end
  
  def update_fd_3(tver)
    vver = 1.051
    nver, cver = CP.ver(vver), CP.ver(tver)
    @update_window.refresh('Fixing screen control', cver, nver, 0, 'Updating Screen')
    screen
    $game_screen.init_tremble
    @update_window.refresh('Finished', cver, nver, 1000, 'Updating Screen')
    screen
    return vver
  end
  
  def update_fd_2(tver)
    vver = 1.050
    nver, cver = CP.ver(vver), CP.ver(tver)
    @update_window.refresh('Fixing counter', cver, nver, 0, 'Updating System')
    screen
    $game_system.fights = 0
    @update_window.refresh('Finished', cver, nver, 1000, 'Updating System')
    screen
    return vver
  end
  
  def update_fd_1(tver)
    vver = 1.042
    nver, cver = CP.ver(vver), CP.ver(tver)
    @update_window.refresh('Adding Unity Force', cver, nver, 0, 'Updating Party')
    screen
    $game_party.ufs = []
    @update_window.refresh('Adding basic Unity Forces', cver, nver, 250, 'Updating Party')
    screen
    $game_party.ufs.push(223)
    @update_window.refresh('Adding basic Unity Forces', cver, nver, 500, 'Updating Party')
    screen
    $game_party.ufs.push(224) if $game_system.beasts.include?(41)
    @update_window.refresh('Adding basic Unity Forces', cver, nver, 750, 'Updating Party')
    screen
    $game_party.gain_item(81, 1) if $game_variables[81] >= 9
    @update_window.refresh('Finished', cver, nver, 1000, 'Updating Party')
    screen
    @update_window.refresh('Fixing abilities', cver, nver, 0, 'Updating Characters')
    screen
    $game_actors[9].forget_skill(110)
    @update_window.refresh('Finished', cver, nver, 1000, 'Updating Characters')
    screen
    @update_window.refresh('Fixing switches', cver, nver, 0, 'Updating Switches')
    screen
    $game_switches[54] = (!$game_switches[54])
    @update_window.refresh('Fixing switches', cver, nver, 500, 'Updating Switches')
    screen
    $game_switches[52] = ($game_variables[26] < 6)
    @update_window.refresh('Finished', cver, nver, 1000, 'Updating Switches')
    screen
    return vver
  end
  
  def update_fd_0000_to_0000
    test_update
    return $version
  end
  
  def test_update
    (0...100).each {||
        @update_window.refresh('Testing Update...', '0.0.0.0', '0.0.0.0', i*10, 'Test')
        Graphics.update}
  end
  
  def screen(frames = 8)
    frames.times{Graphics.update}
  end
  
end
