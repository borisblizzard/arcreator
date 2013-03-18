#==============================================================================
# Sprite_Battler
#==============================================================================

class Sprite_Animation < RPG::Sprite
  
  def initialize(loop_id, viewport = nil)
    super(viewport)
    self.bitmap = Bitmap.new(1, 1)
    self.x, self.y, self.z = 320, 240, 2000
    loop_animation($data_animations[loop_id])
  end
  
end

#==============================================================================
# Window_Horizontal
#==============================================================================

class Window_Horizontal < Window_Base
  
  attr_reader :commands
  
  def initialize(w, commands)
    super(0, 0, 3 * w + 32, 64)
    @item_max = commands.size
    @commands = commands
    if @item_max > 0
      self.contents = Bitmap.new((@item_max + 4) * w, height - 32)
    else
      self.contents = Bitmap.new(32, height - 32)
    end
    @dir = 0
    self.contents.font.name, self.contents.font.size = 'Brush Script', 26
    self.opacity = self.index = 0
    refresh
  end
  
  def refresh
    self.contents.clear
    (0...@item_max+4).each {|i| draw_item(i, (i + @item_max - 2) % @item_max)}
  end
  
  def get_command
    return @commands[(@index + @item_max) % @item_max]
  end
  
  def draw_item(i, index, color = nil)
    rect = Rect.new((self.width - 32)/3 * i, 0, (self.width - 32)/3, 32)
    self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
    if color.is_a?(Color)
      self.contents.font.color = color
    else
      self.contents.font.color = case @commands[index]
      when 'And again!' then text_color(3)
      when 'Warrior' then text_color(6)
      when 'Exerion' then text_color(2)
      when 'Controls' then text_color(9)
      when 'Credits' then Color.new(0, 255, 96)
      else
        normal_color
      end
    end
    self.contents.draw_text_outline(rect, @commands[index], 1)
  end
  
  def disable_item(index)
    draw_item((index + 2) % @item_max, index, disabled_color)
    draw_item((index + 2) % @item_max + @item_max, index, disabled_color)
    draw_item((index + 2) % @item_max + @item_max*2, index, disabled_color)
  end
  
  def size
    return @commands.size
  end
  
  def update
    super
    if moving?
      case @dir.abs
      when 1 then self.ox -= 5 * @dir.sgn
      when 2 then self.ox -= 10 * @dir.sgn
      when 3 then self.ox -= 20 * @dir.sgn
      when 4 then self.ox -= 45 * @dir.sgn
      when 5 then self.ox -= 45 * @dir.sgn
      when 6 then self.ox -= 20 * @dir.sgn
      when 7 then self.ox -= 10 * @dir.sgn
      when 8 then self.ox -= 5 * @dir.sgn
      end
      @dir -= @dir.sgn
    end
    if !moving? && self.active && @item_max > 0
      if Input.repeat?($controls.right)
        $game_system.se_play($data_system.cursor_se)
        @index = @index % @item_max + 1
        if self.ox == (@item_max + 1)* (self.width - 32)/3
          self.ox -= @item_max * (self.width - 32)/3
          @index = 1
        end
        @dir = -8
      elsif Input.repeat?($controls.left)
        $game_system.se_play($data_system.cursor_se)
        @index = (@index + @item_max - 2) % @item_max + 1
        if self.ox == (self.width - 32)/3
          self.ox += @item_max * (self.width - 32)/3
          @index = @item_max - 1
        end
        @dir = 8
      end
    end
    update_cursor_rect
  end
  
  def moving?
    return (@dir != 0)
  end
      
  def index=(index)
    @index = index
    self.ox = (index + 1) * (self.width - 32)/3
    update_help if self.active && @help_window != nil
    update_cursor_rect
  end
  
  def update_cursor_rect
    self.cursor_rect.set((self.width - 32)/3, 0, (self.width - 32)/3, 32)
  end
  
end

#==============================================================================
# Scene_Title
#==============================================================================

class Scene_Title
  
  attr_accessor :intro_fade
  
  CHEATS = ['THISISTOOHARD', 'ISTHATALLYOUGOT', 'IWISHIHADEXERION']
  CHEATS.each_index {|i| CHEATS[i] = CHEATS[i].scan(/./)}
  
  def main
    $data_system = load_data('Data/System.rxdata')
    $fontface, $fontsize = 'Geometrix', 24
    $game_system = Game_System.new
    $game_system.bgm_play($data_system.title_bgm)
    Audio.bgm_play('Audio/BGM/E Nomine - Schwarze Sonne (Blizzard Mix for CP Theme)', 85, 100)
    $game_system.windowskin_name = 'GameOver'
    @sprite = Sprite.new
    @sprite.bitmap = RPG::Cache.title($data_system.title_name).clone
    @sprite_mask = Sprite.new
    @sprite_mask.bitmap = RPG::Cache.title("#{$data_system.title_name}_masker").clone
    @sprite_mask.z = 1000
    @cheat_codes = []
    CHEATS.size.times {|i| @cheat_codes.push(0)}
    @command_window = Window_Horizontal.new(160, self.get_commands)
    @command_window.back_opacity = 160
    @command_window.x = 320 - @command_window.width/2
    @command_window.y = 352
    @continue = (CP::Cache::SaveGames.any? {|i| FileTest.exist?(CP.saves + "Chaos#{i+1}.cps")})
    if @continue
      @command_window.index = @command_window.size - 4
    else
      @command_window.disable_item(@command_window.size - 4)
    end
    Audio.me_stop
    Audio.bgs_stop
    @version = Sprite.new
    @version.bitmap = Bitmap.new(320, 32)
    @version.x, @version.y, @version.z = 316, 456, 2000
    @version.bitmap.font.name = 'EurostileExtended-Roman-DTC'
    @version.bitmap.font.bold = true
    @version.bitmap.font.size = 14
    @version.bitmap.draw_text(0, 0, 320, 32, "#{$release}: #{CP.ver($version)}", 2)
    $data_animations = load_data('Data/Animations.rxdata')
    Graphics.transition(@intro_fade ? 10 : 20)
    @anima = Sprite_Animation.new(52)
    loop do
      Graphics.update
      Input.update
      update
      break if $scene != self || @game != nil
    end
    Graphics.freeze
    [@command_window, @sprite, @sprite_mask, @version, @anima].each {|object|
        object.dispose}
    if $scene != nil
      CP.init_game
      if @game != nil
        init_game
        case @game
        when 0..3 then command_newgame
        end
      end
    end
  end
  
  def get_commands
    commands = []
    commands.push('New Game')
    commands.push('And again!') if $unlocks[0] > 0
    commands.push('Warrior') if $unlocks[0] > 1
    commands.push('Exerion') if $unlocks[0] > 2
    commands.push('Continue', 'Controls', 'Credits', 'Exit')
    return commands
  end
  
  def update
    @command_window.update
    @anima.update
    check_cheat
    return if @command_window.moving?
    if Input.trigger?($controls.confirm)
      case @command_window.get_command
      when 'New Game' then game(0)
      when 'And again!' then game(1)
      when 'Warrior' then game(2)
      when 'Exerion' then game(3)
      when 'Continue' then command_continue
      when 'Controls' then command_option
      when 'Credits' then command_credits
      when 'Exit' then command_shutdown
      end
    end
  end
  
  def game(i)
    $game_system.se_play($data_system.decision_se)
    @game = i
  end
  
  def init_game(flag = true)
    $fontface = 'Geometrix'
    $fontsize = 24
    Graphics.frame_count = 0
    $game_temp          = Game_Temp.new
    $game_system        = Game_System.new
    $game_switches      = Game_Switches.new
    $game_variables     = Game_Variables.new
    $game_self_switches = Game_SelfSwitches.new
    $game_screen        = Game_Screen.new
    $game_actors        = Game_Actors.new
    $game_party         = Game_Party.new
    $game_troop         = Game_Troop.new
    $game_map           = Game_Map.new
    $game_player        = Game_Player.new
    $game_variables[CP::Cache::GameID] = rand(1000000)
    if flag
      $game_party.setup_starting_members
      $scene = Scene_Map.new
      $game_system.windowskin_name = 'Original'
    end
  end
  
  def command_newgame
    case @game
    when 1 then $game_system.exp_rate = $game_system.gold_rate = 4
    when 2 then $game_system.exp_rate = $game_system.gold_rate = 0.5
    when 3 then $game_system.exerion = true
    end
    $game_map.setup($data_system.start_map_id)
    $game_player.moveto($data_system.start_x, $data_system.start_y)
    $game_player.refresh
    $game_map.autoplay
    $game_map.update
  end
  
  def command_continue
    unless @continue
      $game_system.se_play($data_system.buzzer_se)
      return
    end
    $game_system.se_play($data_system.decision_se)
    $scene = Scene_Load.new
  end
  
  def command_option
    $game_system.se_play($data_system.decision_se)
    $scene = Scene_Controls.new
  end
  
  def command_credits
    $game_system.se_play($data_system.decision_se)
    $scene = Scene_Credits.new
  end
  
  def command_shutdown
    $game_system.se_play($data_system.decision_se)
    Audio.bgm_fade(800)
    Audio.bgs_fade(800)
    Audio.me_fade(800)
    $scene = nil
  end
  
  def battle_test
    $data_actors        = load_data('Data/BT_Actors.rxdata')
    $data_classes       = load_data('Data/BT_Classes.rxdata')
    $data_skills        = load_data('Data/BT_Skills.rxdata')
    $data_items         = load_data('Data/BT_Items.rxdata')
    $data_weapons       = load_data('Data/BT_Weapons.rxdata')
    $data_armors        = load_data('Data/BT_Armors.rxdata')
    $data_enemies       = load_data('Data/Enemies.rxdata')
    $data_troops        = load_data('Data/BT_Troops.rxdata')
    $data_states        = load_data('Data/BT_States.rxdata')
    $data_animations    = load_data('Data/BT_Animations.rxdata')
    $data_tilesets      = load_data('Data/BT_Tilesets.rxdata')
    $data_common_events = load_data('Data/BT_CommonEvents.rxdata')
    $data_system        = load_data('Data/BT_System.rxdata')
    ($data_actors - [nil]).each {|actor| actor.generate_parameters}
    init_game(false)
    $game_party.setup_battle_test_members
    $game_temp.battle_troop_id = $data_system.test_troop_id
    $game_temp.battle_can_escape = true
    $game_map.battleback_name = $data_system.battleback_name
    $game_system.se_play($data_system.battle_start_se)
    $game_system.bgm_play($game_system.battle_bgm)
    $scene = Scene_Battle.new
  end
  
  def check_cheat
    @cheat_codes.each_index {|i|
        if Input.trigger?(Input::Let[CHEATS[i][@cheat_codes[i]]])
          @cheat_codes[i] += 1
        elsif Input.Anykey
          @cheat_codes[i] = (Input.trigger?(Input::Let[CHEATS[i][0]]) ? 1 : 0)
        end}
    ($unlocks[0]...3).to_a.reverse.each {|i|
        if @cheat_codes[i] == CHEATS[i].size
          Audio.se_play('Audio/SE/056-Right02', 80, 100)
          CP.unlock(i + 1)
          Graphics.freeze
          Audio.bgm_fade(800)
          $scene = Scene_Stormtronics.new
          return
        end}
  end
      
end