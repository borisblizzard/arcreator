#==============================================================================
# ** Game_Temp
#------------------------------------------------------------------------------
#  This class handles temporary data that is not included with save data.
#  Refer to "$game_temp" for the instance of this class.
#==============================================================================

class Game_Temp
  #--------------------------------------------------------------------------
  # * Public Instance Variables
  #--------------------------------------------------------------------------
  attr_accessor :map_bgm                  # map music (for battle memory)
  attr_accessor :message_text             # message text
  attr_accessor :message_proc             # message callback (Proc)
  attr_accessor :choice_start             # show choices: opening line
  attr_accessor :choice_max               # show choices: number of items
  attr_accessor :choice_cancel_type       # show choices: cancel
  attr_accessor :choice_proc              # show choices: callback (Proc)
  attr_accessor :num_input_start          # input number: opening line
  attr_accessor :num_input_variable_id    # input number: variable ID
  attr_accessor :num_input_digits_max     # input number: digit amount
  attr_accessor :message_window_showing   # message window showing
  attr_accessor :common_event_id          # common event ID
  attr_accessor :in_battle                # in-battle flag
  attr_accessor :battle_calling           # battle calling flag
  attr_accessor :battle_troop_id          # battle troop ID
  attr_accessor :battle_can_escape        # battle flag: escape possible
  attr_accessor :battle_can_lose          # battle flag: losing possible
  attr_accessor :battle_proc              # battle callback (Proc)
  attr_accessor :battle_turn              # number of battle turns
  attr_accessor :battle_event_flags       # battle event flags: completed
  attr_accessor :battle_abort             # battle flag: interrupt
  attr_accessor :battle_main_phase        # battle flag: main phase
  attr_accessor :battleback_name          # battleback file name
  attr_accessor :forcing_battler          # battler being forced into action
  attr_accessor :shop_calling             # shop calling flag
  attr_accessor :shop_goods               # list of shop goods
  attr_accessor :name_calling             # name input: calling flag
  attr_accessor :name_actor_id            # name input: actor ID
  attr_accessor :name_max_char            # name input: max character count
  attr_accessor :menu_calling             # menu calling flag
  attr_accessor :menu_beep                # menu: play sound effect flag
  attr_accessor :save_calling             # save calling flag
  attr_accessor :debug_calling            # debug calling flag
  attr_accessor :player_transferring      # player place movement flag
  attr_accessor :player_new_map_id        # player destination: map ID
  attr_accessor :player_new_x             # player destination: x-coordinate
  attr_accessor :player_new_y             # player destination: y-coordinate
  attr_accessor :player_new_direction     # player destination: direction
  attr_accessor :transition_processing    # transition processing flag
  attr_accessor :transition_name          # transition file name
  attr_accessor :gameover                 # game over flag
  attr_accessor :to_title                 # return to title screen flag
  attr_accessor :last_file_index          # last save file no.
  attr_accessor :debug_top_row            # debug screen: for saving conditions
  attr_accessor :debug_index              # debug screen: for saving conditions
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    @map_bgm = nil
    @message_text = nil
    @message_proc = nil
    @choice_start = 99
    @choice_max = 0
    @choice_cancel_type = 0
    @choice_proc = nil
    @num_input_start = 99
    @num_input_variable_id = 0
    @num_input_digits_max = 0
    @message_window_showing = false
    @common_event_id = 0
    @in_battle = false
    @battle_calling = false
    @battle_troop_id = 0
    @battle_can_escape = false
    @battle_can_lose = false
    @battle_proc = nil
    @battle_turn = 0
    @battle_event_flags = {}
    @battle_abort = false
    @battle_main_phase = false
    @battleback_name = ''
    @forcing_battler = nil
    @shop_calling = false
    @shop_id = 0
    @name_calling = false
    @name_actor_id = 0
    @name_max_char = 0
    @menu_calling = false
    @menu_beep = false
    @save_calling = false
    @debug_calling = false
    @player_transferring = false
    @player_new_map_id = 0
    @player_new_x = 0
    @player_new_y = 0
    @player_new_direction = 0
    @transition_processing = false
    @transition_name = ""
    @gameover = false
    @to_title = false
    @last_file_index = 0
    @debug_top_row = 0
    @debug_index = 0
  end
end
#==============================================================================
# ** Game_System
#------------------------------------------------------------------------------
#  This class handles data surrounding the system. Backround music, etc.
#  is managed here as well. Refer to "$game_system" for the instance of 
#  this class.
#==============================================================================

class Game_System
  #--------------------------------------------------------------------------
  # * Public Instance Variables
  #--------------------------------------------------------------------------
  attr_reader   :map_interpreter          # map event interpreter
  attr_reader   :battle_interpreter       # battle event interpreter
  attr_accessor :timer                    # timer
  attr_accessor :timer_working            # timer working flag
  attr_accessor :save_disabled            # save forbidden
  attr_accessor :menu_disabled            # menu forbidden
  attr_accessor :encounter_disabled       # encounter forbidden
  attr_accessor :message_position         # text option: positioning
  attr_accessor :message_frame            # text option: window frame
  attr_accessor :save_count               # save count
  attr_accessor :magic_number             # magic number
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    @map_interpreter = Interpreter.new(0, true)
    @battle_interpreter = Interpreter.new(0, false)
    @timer = 0
    @timer_working = false
    @save_disabled = false
    @menu_disabled = false
    @encounter_disabled = false
    @message_position = 2
    @message_frame = 0
    @save_count = 0
    @magic_number = 0
  end
  #--------------------------------------------------------------------------
  # * Play Background Music
  #     bgm : background music to be played
  #--------------------------------------------------------------------------
  def bgm_play(bgm)
    @playing_bgm = bgm
    if bgm != nil and bgm.name != ""
      Audio.bgm_play("Audio/BGM/" + bgm.name, bgm.volume, bgm.pitch)
    else
      Audio.bgm_stop
    end
    Graphics.frame_reset
  end
  #--------------------------------------------------------------------------
  # * Stop Background Music
  #--------------------------------------------------------------------------
  def bgm_stop
    Audio.bgm_stop
  end
  #--------------------------------------------------------------------------
  # * Fade Out Background Music
  #     time : fade-out time (in seconds)
  #--------------------------------------------------------------------------
  def bgm_fade(time)
    @playing_bgm = nil
    Audio.bgm_fade(time * 1000)
  end
  #--------------------------------------------------------------------------
  # * Background Music Memory
  #--------------------------------------------------------------------------
  def bgm_memorize
    @memorized_bgm = @playing_bgm
  end
  #--------------------------------------------------------------------------
  # * Restore Background Music
  #--------------------------------------------------------------------------
  def bgm_restore
    bgm_play(@memorized_bgm)
  end
  #--------------------------------------------------------------------------
  # * Play Background Sound
  #     bgs : background sound to be played
  #--------------------------------------------------------------------------
  def bgs_play(bgs)
    @playing_bgs = bgs
    if bgs != nil and bgs.name != ""
      Audio.bgs_play("Audio/BGS/" + bgs.name, bgs.volume, bgs.pitch)
    else
      Audio.bgs_stop
    end
    Graphics.frame_reset
  end
  #--------------------------------------------------------------------------
  # * Fade Out Background Sound
  #     time : fade-out time (in seconds)
  #--------------------------------------------------------------------------
  def bgs_fade(time)
    @playing_bgs = nil
    Audio.bgs_fade(time * 1000)
  end
  #--------------------------------------------------------------------------
  # * Background Sound Memory
  #--------------------------------------------------------------------------
  def bgs_memorize
    @memorized_bgs = @playing_bgs
  end
  #--------------------------------------------------------------------------
  # * Restore Background Sound
  #--------------------------------------------------------------------------
  def bgs_restore
    bgs_play(@memorized_bgs)
  end
  #--------------------------------------------------------------------------
  # * Play Music Effect
  #     me : music effect to be played
  #--------------------------------------------------------------------------
  def me_play(me)
    if me != nil and me.name != ""
      Audio.me_play("Audio/ME/" + me.name, me.volume, me.pitch)
    else
      Audio.me_stop
    end
    Graphics.frame_reset
  end
  #--------------------------------------------------------------------------
  # * Play Sound Effect
  #     se : sound effect to be played
  #--------------------------------------------------------------------------
  def se_play(se)
    if se != nil and se.name != ""
      Audio.se_play("Audio/SE/" + se.name, se.volume, se.pitch)
    end
  end
  #--------------------------------------------------------------------------
  # * Stop Sound Effect
  #--------------------------------------------------------------------------
  def se_stop
    Audio.se_stop
  end
  #--------------------------------------------------------------------------
  # * Get Playing Background Music
  #--------------------------------------------------------------------------
  def playing_bgm
    return @playing_bgm
  end
  #--------------------------------------------------------------------------
  # * Get Playing Background Sound
  #--------------------------------------------------------------------------
  def playing_bgs
    return @playing_bgs
  end
  #--------------------------------------------------------------------------
  # * Get Windowskin File Name
  #--------------------------------------------------------------------------
  def windowskin_name
    if @windowskin_name == nil
      return $data_system.windowskin_name
    else
      return @windowskin_name
    end
  end
  #--------------------------------------------------------------------------
  # * Set Windowskin File Name
  #     windowskin_name : new windowskin file name
  #--------------------------------------------------------------------------
  def windowskin_name=(windowskin_name)
    @windowskin_name = windowskin_name
  end
  #--------------------------------------------------------------------------
  # * Get Battle Background Music
  #--------------------------------------------------------------------------
  def battle_bgm
    if @battle_bgm == nil
      return $data_system.battle_bgm
    else
      return @battle_bgm
    end
  end
  #--------------------------------------------------------------------------
  # * Set Battle Background Music
  #     battle_bgm : new battle background music
  #--------------------------------------------------------------------------
  def battle_bgm=(battle_bgm)
    @battle_bgm = battle_bgm
  end
  #--------------------------------------------------------------------------
  # * Get Background Music for Battle Ending
  #--------------------------------------------------------------------------
  def battle_end_me
    if @battle_end_me == nil
      return $data_system.battle_end_me
    else
      return @battle_end_me
    end
  end
  #--------------------------------------------------------------------------
  # * Set Background Music for Battle Ending
  #     battle_end_me : new battle ending background music
  #--------------------------------------------------------------------------
  def battle_end_me=(battle_end_me)
    @battle_end_me = battle_end_me
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # reduce timer by 1
    if @timer_working and @timer > 0
      @timer -= 1
    end
  end
end
#==============================================================================
# ** Game_Switches
#------------------------------------------------------------------------------
#  This class handles switches. It's a wrapper for the built-in class "Array."
#  Refer to "$game_switches" for the instance of this class.
#==============================================================================

class Game_Switches
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    @data = []
  end
  #--------------------------------------------------------------------------
  # * Get Switch
  #     switch_id : switch ID
  #--------------------------------------------------------------------------
  def [](switch_id)
    if switch_id <= 5000 and @data[switch_id] != nil
      return @data[switch_id]
    else
      return false
    end
  end
  #--------------------------------------------------------------------------
  # * Set Switch
  #     switch_id : switch ID
  #     value     : ON (true) / OFF (false)
  #--------------------------------------------------------------------------
  def []=(switch_id, value)
    if switch_id <= 5000
      @data[switch_id] = value
    end
  end
end
#==============================================================================
# ** Game_Variables
#------------------------------------------------------------------------------
#  This class handles variables. It's a wrapper for the built-in class "Array."
#  Refer to "$game_variables" for the instance of this class.
#==============================================================================

class Game_Variables
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    @data = []
  end
  #--------------------------------------------------------------------------
  # * Get Variable
  #     variable_id : variable ID
  #--------------------------------------------------------------------------
  def [](variable_id)
    if variable_id <= 5000 and @data[variable_id] != nil
      return @data[variable_id]
    else
      return 0
    end
  end
  #--------------------------------------------------------------------------
  # * Set Variable
  #     variable_id : variable ID
  #     value       : the variable's value
  #--------------------------------------------------------------------------
  def []=(variable_id, value)
    if variable_id <= 5000
      @data[variable_id] = value
    end
  end
end
#==============================================================================
# ** Game_SelfSwitches
#------------------------------------------------------------------------------
#  This class handles self switches. It's a wrapper for the built-in class
#  "Hash." Refer to "$game_self_switches" for the instance of this class.
#==============================================================================

class Game_SelfSwitches
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    @data = {}
  end
  #--------------------------------------------------------------------------
  # * Get Self Switch 
  #     key : key
  #--------------------------------------------------------------------------
  def [](key)
    return @data[key] == true ? true : false
  end
  #--------------------------------------------------------------------------
  # * Set Self Switch
  #     key   : key
  #     value : ON (true) / OFF (false)
  #--------------------------------------------------------------------------
  def []=(key, value)
    @data[key] = value
  end
end
#==============================================================================
# ** Game_Screen
#------------------------------------------------------------------------------
#  This class handles screen maintenance data, such as change in color tone,
#  flashing, etc. Refer to "$game_screen" for the instance of this class.
#==============================================================================

class Game_Screen
  #--------------------------------------------------------------------------
  # * Public Instance Variables
  #--------------------------------------------------------------------------
  attr_reader   :tone                     # color tone
  attr_reader   :flash_color              # flash color
  attr_reader   :shake                    # shake positioning
  attr_reader   :pictures                 # pictures
  attr_reader   :weather_type             # weather type
  attr_reader   :weather_max              # max number of weather sprites
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    @tone = Tone.new(0, 0, 0, 0)
    @tone_target = Tone.new(0, 0, 0, 0)
    @tone_duration = 0
    @flash_color = Color.new(0, 0, 0, 0)
    @flash_duration = 0
    @shake_power = 0
    @shake_speed = 0
    @shake_duration = 0
    @shake_direction = 1
    @shake = 0
    @pictures = [nil]
    for i in 1..100
      @pictures.push(Game_Picture.new(i))
    end
    @weather_type = 0
    @weather_max = 0.0
    @weather_type_target = 0
    @weather_max_target = 0.0
    @weather_duration = 0
  end
  #--------------------------------------------------------------------------
  # * Start Changing Color Tone
  #     tone : color tone
  #     duration : time
  #--------------------------------------------------------------------------
  def start_tone_change(tone, duration)
    @tone_target = tone.clone
    @tone_duration = duration
    if @tone_duration == 0
      @tone = @tone_target.clone
    end
  end
  #--------------------------------------------------------------------------
  # * Start Flashing
  #     color : color
  #     duration : time
  #--------------------------------------------------------------------------
  def start_flash(color, duration)
    @flash_color = color.clone
    @flash_duration = duration
  end
  #--------------------------------------------------------------------------
  # * Start Shaking
  #     power : strength
  #     speed : speed
  #     duration : time
  #--------------------------------------------------------------------------
  def start_shake(power, speed, duration)
    @shake_power = power
    @shake_speed = speed
    @shake_duration = duration
  end
  #--------------------------------------------------------------------------
  # * Set Weather
  #     type : type
  #     power : strength
  #     duration : time
  #--------------------------------------------------------------------------
  def weather(type, power, duration)
    @weather_type_target = type
    if @weather_type_target != 0
      @weather_type = @weather_type_target
    end
    if @weather_type_target == 0
      @weather_max_target = 0.0
    else
      @weather_max_target = (power + 1) * 4.0
    end
    @weather_duration = duration
    if @weather_duration == 0
      @weather_type = @weather_type_target
      @weather_max = @weather_max_target
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    if @tone_duration >= 1
      d = @tone_duration
      @tone.red = (@tone.red * (d - 1) + @tone_target.red) / d
      @tone.green = (@tone.green * (d - 1) + @tone_target.green) / d
      @tone.blue = (@tone.blue * (d - 1) + @tone_target.blue) / d
      @tone.gray = (@tone.gray * (d - 1) + @tone_target.gray) / d
      @tone_duration -= 1
    end
    if @flash_duration >= 1
      d = @flash_duration
      @flash_color.alpha = @flash_color.alpha * (d - 1) / d
      @flash_duration -= 1
    end
    if @shake_duration >= 1 or @shake != 0
      delta = (@shake_power * @shake_speed * @shake_direction) / 10.0
      if @shake_duration <= 1 and @shake * (@shake + delta) < 0
        @shake = 0
      else
        @shake += delta
      end
      if @shake > @shake_power * 2
        @shake_direction = -1
      end
      if @shake < - @shake_power * 2
        @shake_direction = 1
      end
      if @shake_duration >= 1
        @shake_duration -= 1
      end
    end
    if @weather_duration >= 1
      d = @weather_duration
      @weather_max = (@weather_max * (d - 1) + @weather_max_target) / d
      @weather_duration -= 1
      if @weather_duration == 0
        @weather_type = @weather_type_target
      end
    end
    if $game_temp.in_battle
      for i in 51..100
        @pictures[i].update
      end
    else
      for i in 1..50
        @pictures[i].update
      end
    end
  end
end
#==============================================================================
# ** Game_Picture
#------------------------------------------------------------------------------
#  This class handles the picture. It's used within the Game_Screen class
#  ($game_screen).
#==============================================================================

class Game_Picture
  #--------------------------------------------------------------------------
  # * Public Instance Variables
  #--------------------------------------------------------------------------
  attr_reader   :number                   # picture number
  attr_reader   :name                     # file name
  attr_reader   :origin                   # starting point
  attr_reader   :x                        # x-coordinate
  attr_reader   :y                        # y-coordinate
  attr_reader   :zoom_x                   # x directional zoom rate
  attr_reader   :zoom_y                   # y directional zoom rate
  attr_reader   :opacity                  # opacity level
  attr_reader   :blend_type               # blend method
  attr_reader   :tone                     # color tone
  attr_reader   :angle                    # rotation angle
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     number : picture number
  #--------------------------------------------------------------------------
  def initialize(number)
    @number = number
    @name = ""
    @origin = 0
    @x = 0.0
    @y = 0.0
    @zoom_x = 100.0
    @zoom_y = 100.0
    @opacity = 255.0
    @blend_type = 1
    @duration = 0
    @target_x = @x
    @target_y = @y
    @target_zoom_x = @zoom_x
    @target_zoom_y = @zoom_y
    @target_opacity = @opacity
    @tone = Tone.new(0, 0, 0, 0)
    @tone_target = Tone.new(0, 0, 0, 0)
    @tone_duration = 0
    @angle = 0
    @rotate_speed = 0
  end
  #--------------------------------------------------------------------------
  # * Show Picture
  #     name       : file name
  #     origin     : starting point
  #     x          : x-coordinate
  #     y          : y-coordinate
  #     zoom_x     : x directional zoom rate
  #     zoom_y     : y directional zoom rate
  #     opacity    : opacity level
  #     blend_type : blend method
  #--------------------------------------------------------------------------
  def show(name, origin, x, y, zoom_x, zoom_y, opacity, blend_type)
    @name = name
    @origin = origin
    @x = x.to_f
    @y = y.to_f
    @zoom_x = zoom_x.to_f
    @zoom_y = zoom_y.to_f
    @opacity = opacity.to_f
    @blend_type = blend_type
    @duration = 0
    @target_x = @x
    @target_y = @y
    @target_zoom_x = @zoom_x
    @target_zoom_y = @zoom_y
    @target_opacity = @opacity
    @tone = Tone.new(0, 0, 0, 0)
    @tone_target = Tone.new(0, 0, 0, 0)
    @tone_duration = 0
    @angle = 0
    @rotate_speed = 0
  end
  #--------------------------------------------------------------------------
  # * Move Picture
  #     duration   : time
  #     origin     : starting point
  #     x          : x-coordinate
  #     y          : y-coordinate
  #     zoom_x     : x directional zoom rate
  #     zoom_y     : y directional zoom rate
  #     opacity    : opacity level
  #     blend_type : blend method
  #--------------------------------------------------------------------------
  def move(duration, origin, x, y, zoom_x, zoom_y, opacity, blend_type)
    @duration = duration
    @origin = origin
    @target_x = x.to_f
    @target_y = y.to_f
    @target_zoom_x = zoom_x.to_f
    @target_zoom_y = zoom_y.to_f
    @target_opacity = opacity.to_f
    @blend_type = blend_type
  end
  #--------------------------------------------------------------------------
  # * Change Rotation Speed
  #     speed : rotation speed
  #--------------------------------------------------------------------------
  def rotate(speed)
    @rotate_speed = speed
  end
  #--------------------------------------------------------------------------
  # * Start Change of Color Tone
  #     tone     : color tone
  #     duration : time
  #--------------------------------------------------------------------------
  def start_tone_change(tone, duration)
    @tone_target = tone.clone
    @tone_duration = duration
    if @tone_duration == 0
      @tone = @tone_target.clone
    end
  end
  #--------------------------------------------------------------------------
  # * Erase Picture
  #--------------------------------------------------------------------------
  def erase
    @name = ""
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    if @duration >= 1
      d = @duration
      @x = (@x * (d - 1) + @target_x) / d
      @y = (@y * (d - 1) + @target_y) / d
      @zoom_x = (@zoom_x * (d - 1) + @target_zoom_x) / d
      @zoom_y = (@zoom_y * (d - 1) + @target_zoom_y) / d
      @opacity = (@opacity * (d - 1) + @target_opacity) / d
      @duration -= 1
    end
    if @tone_duration >= 1
      d = @tone_duration
      @tone.red = (@tone.red * (d - 1) + @tone_target.red) / d
      @tone.green = (@tone.green * (d - 1) + @tone_target.green) / d
      @tone.blue = (@tone.blue * (d - 1) + @tone_target.blue) / d
      @tone.gray = (@tone.gray * (d - 1) + @tone_target.gray) / d
      @tone_duration -= 1
    end
    if @rotate_speed != 0
      @angle += @rotate_speed / 2.0
      while @angle < 0
        @angle += 360
      end
      @angle %= 360
    end
  end
end
#==============================================================================
# ** Game_Battler (part 1)
#------------------------------------------------------------------------------
#  This class deals with battlers. It's used as a superclass for the Game_Actor
#  and Game_Enemy classes.
#==============================================================================

class Game_Battler
  #--------------------------------------------------------------------------
  # * Public Instance Variables
  #--------------------------------------------------------------------------
  attr_reader   :battler_name             # battler file name
  attr_reader   :battler_hue              # battler hue
  attr_reader   :hp                       # HP
  attr_reader   :sp                       # SP
  attr_reader   :states                   # states
  attr_accessor :hidden                   # hidden flag
  attr_accessor :immortal                 # immortal flag
  attr_accessor :damage_pop               # damage display flag
  attr_accessor :damage                   # damage value
  attr_accessor :critical                 # critical flag
  attr_accessor :animation_id             # animation ID
  attr_accessor :animation_hit            # animation hit flag
  attr_accessor :white_flash              # white flash flag
  attr_accessor :blink                    # blink flag
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    @battler_name = ""
    @battler_hue = 0
    @hp = 0
    @sp = 0
    @states = []
    @states_turn = {}
    @maxhp_plus = 0
    @maxsp_plus = 0
    @str_plus = 0
    @dex_plus = 0
    @agi_plus = 0
    @int_plus = 0
    @hidden = false
    @immortal = false
    @damage_pop = false
    @damage = nil
    @critical = false
    @animation_id = 0
    @animation_hit = false
    @white_flash = false
    @blink = false
    @current_action = Game_BattleAction.new
  end
  #--------------------------------------------------------------------------
  # * Get Maximum HP
  #--------------------------------------------------------------------------
  def maxhp
    n = [[base_maxhp + @maxhp_plus, 1].max, 999999].min
    for i in @states
      n *= $data_states[i].maxhp_rate / 100.0
    end
    n = [[Integer(n), 1].max, 999999].min
    return n
  end
  #--------------------------------------------------------------------------
  # * Get Maximum SP
  #--------------------------------------------------------------------------
  def maxsp
    n = [[base_maxsp + @maxsp_plus, 0].max, 9999].min
    for i in @states
      n *= $data_states[i].maxsp_rate / 100.0
    end
    n = [[Integer(n), 0].max, 9999].min
    return n
  end
  #--------------------------------------------------------------------------
  # * Get Strength (STR)
  #--------------------------------------------------------------------------
  def str
    n = [[base_str + @str_plus, 1].max, 999].min
    for i in @states
      n *= $data_states[i].str_rate / 100.0
    end
    n = [[Integer(n), 1].max, 999].min
    return n
  end
  #--------------------------------------------------------------------------
  # * Get Dexterity (DEX)
  #--------------------------------------------------------------------------
  def dex
    n = [[base_dex + @dex_plus, 1].max, 999].min
    for i in @states
      n *= $data_states[i].dex_rate / 100.0
    end
    n = [[Integer(n), 1].max, 999].min
    return n
  end
  #--------------------------------------------------------------------------
  # * Get Agility (AGI)
  #--------------------------------------------------------------------------
  def agi
    n = [[base_agi + @agi_plus, 1].max, 999].min
    for i in @states
      n *= $data_states[i].agi_rate / 100.0
    end
    n = [[Integer(n), 1].max, 999].min
    return n
  end
  #--------------------------------------------------------------------------
  # * Get Intelligence (INT)
  #--------------------------------------------------------------------------
  def int
    n = [[base_int + @int_plus, 1].max, 999].min
    for i in @states
      n *= $data_states[i].int_rate / 100.0
    end
    n = [[Integer(n), 1].max, 999].min
    return n
  end
  #--------------------------------------------------------------------------
  # * Set Maximum HP
  #     maxhp : new maximum HP
  #--------------------------------------------------------------------------
  def maxhp=(maxhp)
    @maxhp_plus += maxhp - self.maxhp
    @maxhp_plus = [[@maxhp_plus, -9999].max, 9999].min
    @hp = [@hp, self.maxhp].min
  end
  #--------------------------------------------------------------------------
  # * Set Maximum SP
  #     maxsp : new maximum SP
  #--------------------------------------------------------------------------
  def maxsp=(maxsp)
    @maxsp_plus += maxsp - self.maxsp
    @maxsp_plus = [[@maxsp_plus, -9999].max, 9999].min
    @sp = [@sp, self.maxsp].min
  end
  #--------------------------------------------------------------------------
  # * Set Strength (STR)
  #     str : new Strength (STR)
  #--------------------------------------------------------------------------
  def str=(str)
    @str_plus += str - self.str
    @str_plus = [[@str_plus, -999].max, 999].min
  end
  #--------------------------------------------------------------------------
  # * Set Dexterity (DEX)
  #     dex : new Dexterity (DEX)
  #--------------------------------------------------------------------------
  def dex=(dex)
    @dex_plus += dex - self.dex
    @dex_plus = [[@dex_plus, -999].max, 999].min
  end
  #--------------------------------------------------------------------------
  # * Set Agility (AGI)
  #     agi : new Agility (AGI)
  #--------------------------------------------------------------------------
  def agi=(agi)
    @agi_plus += agi - self.agi
    @agi_plus = [[@agi_plus, -999].max, 999].min
  end
  #--------------------------------------------------------------------------
  # * Set Intelligence (INT)
  #     int : new Intelligence (INT)
  #--------------------------------------------------------------------------
  def int=(int)
    @int_plus += int - self.int
    @int_plus = [[@int_plus, -999].max, 999].min
  end
  #--------------------------------------------------------------------------
  # * Get Hit Rate
  #--------------------------------------------------------------------------
  def hit
    n = 100
    for i in @states
      n *= $data_states[i].hit_rate / 100.0
    end
    return Integer(n)
  end
  #--------------------------------------------------------------------------
  # * Get Attack Power
  #--------------------------------------------------------------------------
  def atk
    n = base_atk
    for i in @states
      n *= $data_states[i].atk_rate / 100.0
    end
    return Integer(n)
  end
  #--------------------------------------------------------------------------
  # * Get Physical Defense Power
  #--------------------------------------------------------------------------
  def pdef
    n = base_pdef
    for i in @states
      n *= $data_states[i].pdef_rate / 100.0
    end
    return Integer(n)
  end
  #--------------------------------------------------------------------------
  # * Get Magic Defense Power
  #--------------------------------------------------------------------------
  def mdef
    n = base_mdef
    for i in @states
      n *= $data_states[i].mdef_rate / 100.0
    end
    return Integer(n)
  end
  #--------------------------------------------------------------------------
  # * Get Evasion Correction
  #--------------------------------------------------------------------------
  def eva
    n = base_eva
    for i in @states
      n += $data_states[i].eva
    end
    return n
  end
  #--------------------------------------------------------------------------
  # * Change HP
  #     hp : new HP
  #--------------------------------------------------------------------------
  def hp=(hp)
    @hp = [[hp, maxhp].min, 0].max
    # add or exclude incapacitation
    for i in 1...$data_states.size
      if $data_states[i].zero_hp
        if self.dead?
          add_state(i)
        else
          remove_state(i)
        end
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Change SP
  #     sp : new SP
  #--------------------------------------------------------------------------
  def sp=(sp)
    @sp = [[sp, maxsp].min, 0].max
  end
  #--------------------------------------------------------------------------
  # * Recover All
  #--------------------------------------------------------------------------
  def recover_all
    @hp = maxhp
    @sp = maxsp
    for i in @states.clone
      remove_state(i)
    end
  end
  #--------------------------------------------------------------------------
  # * Get Current Action
  #--------------------------------------------------------------------------
  def current_action
    return @current_action
  end
  #--------------------------------------------------------------------------
  # * Determine Action Speed
  #--------------------------------------------------------------------------
  def make_action_speed
    @current_action.speed = agi + rand(10 + agi / 4)
  end
  #--------------------------------------------------------------------------
  # * Decide Incapacitation
  #--------------------------------------------------------------------------
  def dead?
    return (@hp == 0 and not @immortal)
  end
  #--------------------------------------------------------------------------
  # * Decide Existance
  #--------------------------------------------------------------------------
  def exist?
    return (not @hidden and (@hp > 0 or @immortal))
  end
  #--------------------------------------------------------------------------
  # * Decide HP 0
  #--------------------------------------------------------------------------
  def hp0?
    return (not @hidden and @hp == 0)
  end
  #--------------------------------------------------------------------------
  # * Decide if Command is Inputable
  #--------------------------------------------------------------------------
  def inputable?
    return (not @hidden and restriction <= 1)
  end
  #--------------------------------------------------------------------------
  # * Decide if Action is Possible
  #--------------------------------------------------------------------------
  def movable?
    return (not @hidden and restriction < 4)
  end
  #--------------------------------------------------------------------------
  # * Decide if Guarding
  #--------------------------------------------------------------------------
  def guarding?
    return (@current_action.kind == 0 and @current_action.basic == 1)
  end
  #--------------------------------------------------------------------------
  # * Decide if Resting
  #--------------------------------------------------------------------------
  def resting?
    return (@current_action.kind == 0 and @current_action.basic == 3)
  end
end
#==============================================================================
# ** Game_Battler (part 2)
#------------------------------------------------------------------------------
#  This class deals with battlers. It's used as a superclass for the Game_Actor
#  and Game_Enemy classes.
#==============================================================================

class Game_Battler
  #--------------------------------------------------------------------------
  # * Check State
  #     state_id : state ID
  #--------------------------------------------------------------------------
  def state?(state_id)
    # Return true if the applicable state is added.
    return @states.include?(state_id)
  end
  #--------------------------------------------------------------------------
  # * Determine if a state is full or not.
  #     state_id : state ID
  #--------------------------------------------------------------------------
  def state_full?(state_id)
    # Return false if the applicable state is not added.
    unless self.state?(state_id)
      return false
    end
    # Return true if the number of maintenance turns is -1 (auto state).
    if @states_turn[state_id] == -1
      return true
    end
    # Return true if the number of maintenance turns is equal to the
    # lowest number of natural removal turns.
    return @states_turn[state_id] == $data_states[state_id].hold_turn
  end
  #--------------------------------------------------------------------------
  # * Add State
  #     state_id : state ID
  #     force    : forcefully added flag (used to deal with auto state)
  #--------------------------------------------------------------------------
  def add_state(state_id, force = false)
    # For an ineffective state
    if $data_states[state_id] == nil
      # End Method
      return
    end
    # If not forcefully added
    unless force
      # A state loop already in existance
      for i in @states
        # If a new state is included in the state change (-) of an existing
        # state, and that state is not included in the state change (-) of
        # a new state (example: an attempt to add poison during dead)
        if $data_states[i].minus_state_set.include?(state_id) and
           not $data_states[state_id].minus_state_set.include?(i)
          # End Method
          return
        end
      end
    end
    # If this state is not added
    unless state?(state_id)
      # Add state ID to @states array
      @states.push(state_id)
      # If option [regarded as HP 0]is effective
      if $data_states[state_id].zero_hp
        # Change HP to 0
        @hp = 0
      end
      # All state loops
      for i in 1...$data_states.size
        # Dealing with a state change (+)
        if $data_states[state_id].plus_state_set.include?(i)
          add_state(i)
        end
        # Dealing with a state change (-)
        if $data_states[state_id].minus_state_set.include?(i)
          remove_state(i)
        end
      end
      # line change to a large rating order (if value is the same, then a
      # strong restriction order)
      @states.sort! do |a, b|
        state_a = $data_states[a]
        state_b = $data_states[b]
        if state_a.rating > state_b.rating
          -1
        elsif state_a.rating < state_b.rating
          +1
        elsif state_a.restriction > state_b.restriction
          -1
        elsif state_a.restriction < state_b.restriction
          +1
        else
          a <=> b
        end
      end
    end
    # If added forcefully
    if force
      # Set the natural removal's lowest number of turns to -1
      @states_turn[state_id] = -1
    end
    # If not added forcefully
    unless  @states_turn[state_id] == -1
      # Set the natural removal's lowest number of turns
      @states_turn[state_id] = $data_states[state_id].hold_turn
    end
    # If unable to move
    unless movable?
      # Clear action
      @current_action.clear
    end
    # Check the maximum value of HP and SP
    @hp = [@hp, self.maxhp].min
    @sp = [@sp, self.maxsp].min
  end
  #--------------------------------------------------------------------------
  # * Remove State
  #     state_id : state ID
  #     force    : forcefully removed flag (used to deal with auto state)
  #--------------------------------------------------------------------------
  def remove_state(state_id, force = false)
    # If this state is added
    if state?(state_id)
      # If a forcefully added state is not forcefully removed
      if @states_turn[state_id] == -1 and not force
        # End Method
        return
      end
      # If current HP is at 0 and options are effective [regarded as HP 0]
      if @hp == 0 and $data_states[state_id].zero_hp
        # Determine if there's another state [regarded as HP 0] or not
        zero_hp = false
        for i in @states
          if i != state_id and $data_states[i].zero_hp
            zero_hp = true
          end
        end
        # Change HP to 1 if OK to remove incapacitation.
        if zero_hp == false
          @hp = 1
        end
      end
      # Delete state ID from @states and @states_turn hash array
      @states.delete(state_id)
      @states_turn.delete(state_id)
    end
    # Check maximum value for HP and SP
    @hp = [@hp, self.maxhp].min
    @sp = [@sp, self.maxsp].min
  end
  #--------------------------------------------------------------------------
  # * Get State Animation ID
  #--------------------------------------------------------------------------
  def state_animation_id
    # If no states are added
    if @states.size == 0
      return 0
    end
    # Return state animation ID with maximum rating
    return $data_states[@states[0]].animation_id
  end
  #--------------------------------------------------------------------------
  # * Get Restriction
  #--------------------------------------------------------------------------
  def restriction
    restriction_max = 0
    # Get maximum restriction from currently added states
    for i in @states
      if $data_states[i].restriction >= restriction_max
        restriction_max = $data_states[i].restriction
      end
    end
    return restriction_max
  end
  #--------------------------------------------------------------------------
  # * Determine [Can't Get EXP] States
  #--------------------------------------------------------------------------
  def cant_get_exp?
    for i in @states
      if $data_states[i].cant_get_exp
        return true
      end
    end
    return false
  end
  #--------------------------------------------------------------------------
  # * Determine [Can't Evade] States
  #--------------------------------------------------------------------------
  def cant_evade?
    for i in @states
      if $data_states[i].cant_evade
        return true
      end
    end
    return false
  end
  #--------------------------------------------------------------------------
  # * Determine [Slip Damage] States
  #--------------------------------------------------------------------------
  def slip_damage?
    for i in @states
      if $data_states[i].slip_damage
        return true
      end
    end
    return false
  end
  #--------------------------------------------------------------------------
  # * Remove Battle States (called up during end of battle)
  #--------------------------------------------------------------------------
  def remove_states_battle
    for i in @states.clone
      if $data_states[i].battle_only
        remove_state(i)
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Natural Removal of States (called up each turn)
  #--------------------------------------------------------------------------
  def remove_states_auto
    for i in @states_turn.keys.clone
      if @states_turn[i] > 0
        @states_turn[i] -= 1
      elsif rand(100) < $data_states[i].auto_release_prob
        remove_state(i)
      end
    end
  end
  #--------------------------------------------------------------------------
  # * State Removed by Shock (called up each time physical damage occurs)
  #--------------------------------------------------------------------------
  def remove_states_shock
    for i in @states.clone
      if rand(100) < $data_states[i].shock_release_prob
        remove_state(i)
      end
    end
  end
  #--------------------------------------------------------------------------
  # * State Change (+) Application
  #     plus_state_set  : State Change (+)
  #--------------------------------------------------------------------------
  def states_plus(plus_state_set)
    # Clear effective flag
    effective = false
    # Loop (added state)
    for i in plus_state_set
      # If this state is not guarded
      unless self.state_guard?(i)
        # Set effective flag if this state is not full
        effective |= self.state_full?(i) == false
        # If states offer [no resistance]
        if $data_states[i].nonresistance
          # Set state change flag
          @state_changed = true
          # Add a state
          add_state(i)
        # If this state is not full
        elsif self.state_full?(i) == false
          # Convert state effectiveness to probability,
          # compare to random numbers
          if rand(100) < [0,100,80,60,40,20,0][self.state_ranks[i]]
            # Set state change flag
            @state_changed = true
            # Add a state
            add_state(i)
          end
        end
      end
    end
    # End Method
    return effective
  end
  #--------------------------------------------------------------------------
  # * Apply State Change (-)
  #     minus_state_set : state change (-)
  #--------------------------------------------------------------------------
  def states_minus(minus_state_set)
    # Clear effective flag
    effective = false
    # Loop (state to be removed)
    for i in minus_state_set
      # Set effective flag if this state is added
      effective |= self.state?(i)
      # Set a state change flag
      @state_changed = true
      # Remove state
      remove_state(i)
    end
    # End Method
    return effective
  end
end
#==============================================================================
# ** Game_Battler (part 3)
#------------------------------------------------------------------------------
#  This class deals with battlers. It's used as a superclass for the Game_Actor
#  and Game_Enemy classes.
#==============================================================================

class Game_Battler
  #--------------------------------------------------------------------------
  # * Determine Usable Skills
  #     skill_id : skill ID
  #--------------------------------------------------------------------------
  def skill_can_use?(skill_id)
    # If there's not enough SP, the skill cannot be used.
    if $data_skills[skill_id].sp_cost > self.sp
      return false
    end
    # Unusable if incapacitated
    if dead?
      return false
    end
    # If silent, only physical skills can be used
    if $data_skills[skill_id].atk_f == 0 and self.restriction == 1
      return false
    end
    # Get usable time
    occasion = $data_skills[skill_id].occasion
    # If in battle
    if $game_temp.in_battle
      # Usable with [Normal] and [Only Battle]
      return (occasion == 0 or occasion == 1)
    # If not in battle
    else
      # Usable with [Normal] and [Only Menu]
      return (occasion == 0 or occasion == 2)
    end
  end
  #--------------------------------------------------------------------------
  # * Applying Normal Attack Effects
  #     attacker : battler
  #--------------------------------------------------------------------------
  def attack_effect(attacker)
    # Clear critical flag
    self.critical = false
    # First hit detection
    hit_result = (rand(100) < attacker.hit)
    # If hit occurs
    if hit_result == true
      # Calculate basic damage
      atk = [attacker.atk - self.pdef / 2, 0].max
      self.damage = atk * (20 + attacker.str) / 20
      # Element correction
      self.damage *= elements_correct(attacker.element_set)
      self.damage /= 100
      # If damage value is strictly positive
      if self.damage > 0
        # Critical correction
        if rand(100) < 4 * attacker.dex / self.agi
          self.damage *= 2
          self.critical = true
        end
        # Guard correction
        if self.guarding?
          self.damage /= 2
        end
      end
      # Dispersion
      if self.damage.abs > 0
        amp = [self.damage.abs * 15 / 100, 1].max
        self.damage += rand(amp+1) + rand(amp+1) - amp
      end
      # Second hit detection
      eva = 8 * self.agi / attacker.dex + self.eva
      hit = self.damage < 0 ? 100 : 100 - eva
      hit = self.cant_evade? ? 100 : hit
      hit_result = (rand(100) < hit)
    end
    # If hit occurs
    if hit_result == true
      # State Removed by Shock
      remove_states_shock
      # Substract damage from HP
      self.hp -= self.damage
      # State change
      @state_changed = false
      states_plus(attacker.plus_state_set)
      states_minus(attacker.minus_state_set)
    # When missing
    else
      # Set damage to "Miss"
      self.damage = "Miss"
      # Clear critical flag
      self.critical = false
    end
    # End Method
    return true
  end
  #--------------------------------------------------------------------------
  # * Apply Skill Effects
  #     user  : the one using skills (battler)
  #     skill : skill
  #--------------------------------------------------------------------------
  def skill_effect(user, skill)
    # Clear critical flag
    self.critical = false
    # If skill scope is for ally with 1 or more HP, and your own HP = 0,
    # or skill scope is for ally with 0, and your own HP = 1 or more
    if ((skill.scope == 3 or skill.scope == 4) and self.hp == 0) or
       ((skill.scope == 5 or skill.scope == 6) and self.hp >= 1)
      # End Method
      return false
    end
    # Clear effective flag
    effective = false
    # Set effective flag if common ID is effective
    effective |= skill.common_event_id > 0
    # First hit detection
    hit = skill.hit
    if skill.atk_f > 0
      hit *= user.hit / 100
    end
    hit_result = (rand(100) < hit)
    # Set effective flag if skill is uncertain
    effective |= hit < 100
    # If hit occurs
    if hit_result == true
      # Calculate power
      power = skill.power + user.atk * skill.atk_f / 100
      if power > 0
        power -= self.pdef * skill.pdef_f / 200
        power -= self.mdef * skill.mdef_f / 200
        power = [power, 0].max
      end
      # Calculate rate
      rate = 20
      rate += (user.str * skill.str_f / 100)
      rate += (user.dex * skill.dex_f / 100)
      rate += (user.agi * skill.agi_f / 100)
      rate += (user.int * skill.int_f / 100)
      # Calculate basic damage
      self.damage = power * rate / 20
      # Element correction
      self.damage *= elements_correct(skill.element_set)
      self.damage /= 100
      # If damage value is strictly positive
      if self.damage > 0
        # Guard correction
        if self.guarding?
          self.damage /= 2
        end
      end
      # Dispersion
      if skill.variance > 0 and self.damage.abs > 0
        amp = [self.damage.abs * skill.variance / 100, 1].max
        self.damage += rand(amp+1) + rand(amp+1) - amp
      end
      # Second hit detection
      eva = 8 * self.agi / user.dex + self.eva
      hit = self.damage < 0 ? 100 : 100 - eva * skill.eva_f / 100
      hit = self.cant_evade? ? 100 : hit
      hit_result = (rand(100) < hit)
      # Set effective flag if skill is uncertain
      effective |= hit < 100
    end
    # If hit occurs
    if hit_result == true
      # If physical attack has power other than 0
      if skill.power != 0 and skill.atk_f > 0
        # State Removed by Shock
        remove_states_shock
        # Set to effective flag
        effective = true
      end
      # Substract damage from HP
      last_hp = self.hp
      self.hp -= self.damage
      effective |= self.hp != last_hp
      # State change
      @state_changed = false
      effective |= states_plus(skill.plus_state_set)
      effective |= states_minus(skill.minus_state_set)
      # If power is 0
      if skill.power == 0
        # Set damage to an empty string
        self.damage = ""
        # If state is unchanged
        unless @state_changed
          # Set damage to "Miss"
          self.damage = "Miss"
        end
      end
    # If miss occurs
    else
      # Set damage to "Miss"
      self.damage = "Miss"
    end
    # If not in battle
    unless $game_temp.in_battle
      # Set damage to nil
      self.damage = nil
    end
    # End Method
    return effective
  end
  #--------------------------------------------------------------------------
  # * Application of Item Effects
  #     item : item
  #--------------------------------------------------------------------------
  def item_effect(item)
    # Clear critical flag
    self.critical = false
    # If item scope is for ally with 1 or more HP, and your own HP = 0,
    # or item scope is for ally with 0 HP, and your own HP = 1 or more
    if ((item.scope == 3 or item.scope == 4) and self.hp == 0) or
       ((item.scope == 5 or item.scope == 6) and self.hp >= 1)
      # End Method
      return false
    end
    # Clear effective flag
    effective = false
    # Set effective flag if common ID is effective
    effective |= item.common_event_id > 0
    # Determine hit
    hit_result = (rand(100) < item.hit)
    # Set effective flag is skill is uncertain
    effective |= item.hit < 100
    # If hit occurs
    if hit_result == true
      # Calculate amount of recovery
      recover_hp = maxhp * item.recover_hp_rate / 100 + item.recover_hp
      recover_sp = maxsp * item.recover_sp_rate / 100 + item.recover_sp
      if recover_hp < 0
        recover_hp += self.pdef * item.pdef_f / 20
        recover_hp += self.mdef * item.mdef_f / 20
        recover_hp = [recover_hp, 0].min
      end
      # Element correction
      recover_hp *= elements_correct(item.element_set)
      recover_hp /= 100
      recover_sp *= elements_correct(item.element_set)
      recover_sp /= 100
      # Dispersion
      if item.variance > 0 and recover_hp.abs > 0
        amp = [recover_hp.abs * item.variance / 100, 1].max
        recover_hp += rand(amp+1) + rand(amp+1) - amp
      end
      if item.variance > 0 and recover_sp.abs > 0
        amp = [recover_sp.abs * item.variance / 100, 1].max
        recover_sp += rand(amp+1) + rand(amp+1) - amp
      end
      # If recovery code is negative
      if recover_hp < 0
        # Guard correction
        if self.guarding?
          recover_hp /= 2
        end
      end
      # Set damage value and reverse HP recovery amount
      self.damage = -recover_hp
      # HP and SP recovery
      last_hp = self.hp
      last_sp = self.sp
      self.hp += recover_hp
      self.sp += recover_sp
      effective |= self.hp != last_hp
      effective |= self.sp != last_sp
      # State change
      @state_changed = false
      effective |= states_plus(item.plus_state_set)
      effective |= states_minus(item.minus_state_set)
      # If parameter value increase is effective
      if item.parameter_type > 0 and item.parameter_points != 0
        # Branch by parameter
        case item.parameter_type
        when 1  # Max HP
          @maxhp_plus += item.parameter_points
        when 2  # Max SP
          @maxsp_plus += item.parameter_points
        when 3  # Strength
          @str_plus += item.parameter_points
        when 4  # Dexterity
          @dex_plus += item.parameter_points
        when 5  # Agility
          @agi_plus += item.parameter_points
        when 6  # Intelligence
          @int_plus += item.parameter_points
        end
        # Set to effective flag
        effective = true
      end
      # If HP recovery rate and recovery amount are 0
      if item.recover_hp_rate == 0 and item.recover_hp == 0
        # Set damage to empty string
        self.damage = ""
        # If SP recovery rate / recovery amount are 0, and parameter increase
        # value is ineffective.
        if item.recover_sp_rate == 0 and item.recover_sp == 0 and
           (item.parameter_type == 0 or item.parameter_points == 0)
          # If state is unchanged
          unless @state_changed
            # Set damage to "Miss"
            self.damage = "Miss"
          end
        end
      end
    # If miss occurs
    else
      # Set damage to "Miss"
      self.damage = "Miss"
    end
    # If not in battle
    unless $game_temp.in_battle
      # Set damage to nil
      self.damage = nil
    end
    # End Method
    return effective
  end
  #--------------------------------------------------------------------------
  # * Application of Slip Damage Effects
  #--------------------------------------------------------------------------
  def slip_damage_effect
    # Set damage
    self.damage = self.maxhp / 10
    # Dispersion
    if self.damage.abs > 0
      amp = [self.damage.abs * 15 / 100, 1].max
      self.damage += rand(amp+1) + rand(amp+1) - amp
    end
    # Subtract damage from HP
    self.hp -= self.damage
    # End Method
    return true
  end
  #--------------------------------------------------------------------------
  # * Calculating Element Correction
  #     element_set : element
  #--------------------------------------------------------------------------
  def elements_correct(element_set)
    # If not an element
    if element_set == []
      # Return 100
      return 100
    end
    # Return the weakest object among the elements given
    # * "element_rate" method is defined by Game_Actor and Game_Enemy classes,
    #    which inherit from this class.
    weakest = -100
    for i in element_set
      weakest = [weakest, self.element_rate(i)].max
    end
    return weakest
  end
end
#==============================================================================
# ** Game_BattleAction
#------------------------------------------------------------------------------
#  This class handles actions in battle. It's used within the Game_Battler 
#  class.
#==============================================================================

class Game_BattleAction
  #--------------------------------------------------------------------------
  # * Public Instance Variables
  #--------------------------------------------------------------------------
  attr_accessor :speed                    # speed
  attr_accessor :kind                     # kind (basic / skill / item)
  attr_accessor :basic                    # basic (attack / guard / escape)
  attr_accessor :skill_id                 # skill ID
  attr_accessor :item_id                  # item ID
  attr_accessor :target_index             # target index
  attr_accessor :forcing                  # forced flag
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    clear
  end
  #--------------------------------------------------------------------------
  # * Clear
  #--------------------------------------------------------------------------
  def clear
    @speed = 0
    @kind = 0
    @basic = 3
    @skill_id = 0
    @item_id = 0
    @target_index = -1
    @forcing = false
  end
  #--------------------------------------------------------------------------
  # * Determine Validity
  #--------------------------------------------------------------------------
  def valid?
    return (not (@kind == 0 and @basic == 3))
  end
  #--------------------------------------------------------------------------
  # * Determine if for One Ally
  #--------------------------------------------------------------------------
  def for_one_friend?
    # If kind = skill, and effect scope is for ally (including 0 HP)
    if @kind == 1 and [3, 5].include?($data_skills[@skill_id].scope)
      return true
    end
    # If kind = item, and effect scope is for ally (including 0 HP)
    if @kind == 2 and [3, 5].include?($data_items[@item_id].scope)
      return true
    end
    return false
  end
  #--------------------------------------------------------------------------
  # * Determine if for One Ally (HP 0)
  #--------------------------------------------------------------------------
  def for_one_friend_hp0?
    # If kind = skill, and effect scope is for ally (only 0 HP)
    if @kind == 1 and [5].include?($data_skills[@skill_id].scope)
      return true
    end
    # If kind = item, and effect scope is for ally (only 0 HP)
    if @kind == 2 and [5].include?($data_items[@item_id].scope)
      return true
    end
    return false
  end
  #--------------------------------------------------------------------------
  # * Random Target (for Actor)
  #--------------------------------------------------------------------------
  def decide_random_target_for_actor
    # Diverge with effect scope
    if for_one_friend_hp0?
      battler = $game_party.random_target_actor_hp0
    elsif for_one_friend?
      battler = $game_party.random_target_actor
    else
      battler = $game_troop.random_target_enemy
    end
    # If a target exists, get an index, and if a target doesn't exist,
    # clear the action
    if battler != nil
      @target_index = battler.index
    else
      clear
    end
  end
  #--------------------------------------------------------------------------
  # * Random Target (for Enemy)
  #--------------------------------------------------------------------------
  def decide_random_target_for_enemy
    # Diverge with effect scope
    if for_one_friend_hp0?
      battler = $game_troop.random_target_enemy_hp0
    elsif for_one_friend?
      battler = $game_troop.random_target_enemy
    else
      battler = $game_party.random_target_actor
    end
    # If a target exists, get an index, and if a target doesn't exist,
    # clear the action
    if battler != nil
      @target_index = battler.index
    else
      clear
    end
  end
  #--------------------------------------------------------------------------
  # * Last Target (for Actor)
  #--------------------------------------------------------------------------
  def decide_last_target_for_actor
    # If effect scope is ally, then it's an actor, anything else is an enemy
    if @target_index == -1
      battler = nil
    elsif for_one_friend?
      battler = $game_party.actors[@target_index]
    else
      battler = $game_troop.enemies[@target_index]
    end
    # Clear action if no target exists
    if battler == nil or not battler.exist?
      clear
    end
  end
  #--------------------------------------------------------------------------
  # * Last Target (for Enemy)
  #--------------------------------------------------------------------------
  def decide_last_target_for_enemy
    # If effect scope is ally, then it's an enemy, anything else is an actor
    if @target_index == -1
      battler = nil
    elsif for_one_friend?
      battler = $game_troop.enemies[@target_index]
    else
      battler = $game_party.actors[@target_index]
    end
    # Clear action if no target exists
    if battler == nil or not battler.exist?
      clear
    end
  end
end
#==============================================================================
# ** Game_Actor
#------------------------------------------------------------------------------
#  This class handles the actor. It's used within the Game_Actors class
#  ($game_actors) and refers to the Game_Party class ($game_party).
#==============================================================================

class Game_Actor < Game_Battler
  #--------------------------------------------------------------------------
  # * Public Instance Variables
  #--------------------------------------------------------------------------
  attr_reader   :name                     # name
  attr_reader   :character_name           # character file name
  attr_reader   :character_hue            # character hue
  attr_reader   :class_id                 # class ID
  attr_reader   :weapon_id                # weapon ID
  attr_reader   :armor1_id                # shield ID
  attr_reader   :armor2_id                # helmet ID
  attr_reader   :armor3_id                # body armor ID
  attr_reader   :armor4_id                # accessory ID
  attr_reader   :level                    # level
  attr_reader   :exp                      # EXP
  attr_reader   :skills                   # skills
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     actor_id : actor ID
  #--------------------------------------------------------------------------
  def initialize(actor_id)
    super()
    setup(actor_id)
  end
  #--------------------------------------------------------------------------
  # * Setup
  #     actor_id : actor ID
  #--------------------------------------------------------------------------
  def setup(actor_id)
    actor = $data_actors[actor_id]
    @actor_id = actor_id
    @name = actor.name
    @character_name = actor.character_name
    @character_hue = actor.character_hue
    @battler_name = actor.battler_name
    @battler_hue = actor.battler_hue
    @class_id = actor.class_id
    @weapon_id = actor.weapon_id
    @armor1_id = actor.armor1_id
    @armor2_id = actor.armor2_id
    @armor3_id = actor.armor3_id
    @armor4_id = actor.armor4_id
    @level = actor.initial_level
    @exp_list = Array.new(101)
    make_exp_list
    @exp = @exp_list[@level]
    @skills = []
    @hp = maxhp
    @sp = maxsp
    @states = []
    @states_turn = {}
    @maxhp_plus = 0
    @maxsp_plus = 0
    @str_plus = 0
    @dex_plus = 0
    @agi_plus = 0
    @int_plus = 0
    # Learn skill
    for i in 1..@level
      for j in $data_classes[@class_id].learnings
        if j.level == i
          learn_skill(j.skill_id)
        end
      end
    end
    # Update auto state
    update_auto_state(nil, $data_armors[@armor1_id])
    update_auto_state(nil, $data_armors[@armor2_id])
    update_auto_state(nil, $data_armors[@armor3_id])
    update_auto_state(nil, $data_armors[@armor4_id])
  end
  #--------------------------------------------------------------------------
  # * Get Actor ID
  #--------------------------------------------------------------------------
  def id
    return @actor_id
  end
  #--------------------------------------------------------------------------
  # * Get Index
  #--------------------------------------------------------------------------
  def index
    return $game_party.actors.index(self)
  end
  #--------------------------------------------------------------------------
  # * Calculate EXP
  #--------------------------------------------------------------------------
  def make_exp_list
    actor = $data_actors[@actor_id]
    @exp_list[1] = 0
    pow_i = 2.4 + actor.exp_inflation / 100.0
    for i in 2..100
      if i > actor.final_level
        @exp_list[i] = 0
      else
        n = actor.exp_basis * ((i + 3) ** pow_i) / (5 ** pow_i)
        @exp_list[i] = @exp_list[i-1] + Integer(n)
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Get Element Revision Value
  #     element_id : element ID
  #--------------------------------------------------------------------------
  def element_rate(element_id)
    # Get values corresponding to element effectiveness
    table = [0,200,150,100,50,0,-100]
    result = table[$data_classes[@class_id].element_ranks[element_id]]
    # If this element is protected by armor, then it's reduced by half
    for i in [@armor1_id, @armor2_id, @armor3_id, @armor4_id]
      armor = $data_armors[i]
      if armor != nil and armor.guard_element_set.include?(element_id)
        result /= 2
      end
    end
    # If this element is protected by states, then it's reduced by half
    for i in @states
      if $data_states[i].guard_element_set.include?(element_id)
        result /= 2
      end
    end
    # End Method
    return result
  end
  #--------------------------------------------------------------------------
  # * Get State Effectiveness
  #--------------------------------------------------------------------------
  def state_ranks
    return $data_classes[@class_id].state_ranks
  end
  #--------------------------------------------------------------------------
  # * Determine State Guard
  #     state_id : state ID
  #--------------------------------------------------------------------------
  def state_guard?(state_id)
    for i in [@armor1_id, @armor2_id, @armor3_id, @armor4_id]
      armor = $data_armors[i]
      if armor != nil
        if armor.guard_state_set.include?(state_id)
          return true
        end
      end
    end
    return false
  end
  #--------------------------------------------------------------------------
  # * Get Normal Attack Element
  #--------------------------------------------------------------------------
  def element_set
    weapon = $data_weapons[@weapon_id]
    return weapon != nil ? weapon.element_set : []
  end
  #--------------------------------------------------------------------------
  # * Get Normal Attack State Change (+)
  #--------------------------------------------------------------------------
  def plus_state_set
    weapon = $data_weapons[@weapon_id]
    return weapon != nil ? weapon.plus_state_set : []
  end
  #--------------------------------------------------------------------------
  # * Get Normal Attack State Change (-)
  #--------------------------------------------------------------------------
  def minus_state_set
    weapon = $data_weapons[@weapon_id]
    return weapon != nil ? weapon.minus_state_set : []
  end
  #--------------------------------------------------------------------------
  # * Get Maximum HP
  #--------------------------------------------------------------------------
  def maxhp
    n = [[base_maxhp + @maxhp_plus, 1].max, 9999].min
    for i in @states
      n *= $data_states[i].maxhp_rate / 100.0
    end
    n = [[Integer(n), 1].max, 9999].min
    return n
  end
  #--------------------------------------------------------------------------
  # * Get Basic Maximum HP
  #--------------------------------------------------------------------------
  def base_maxhp
    return $data_actors[@actor_id].parameters[0, @level]
  end
  #--------------------------------------------------------------------------
  # * Get Basic Maximum SP
  #--------------------------------------------------------------------------
  def base_maxsp
    return $data_actors[@actor_id].parameters[1, @level]
  end
  #--------------------------------------------------------------------------
  # * Get Basic Strength
  #--------------------------------------------------------------------------
  def base_str
    n = $data_actors[@actor_id].parameters[2, @level]
    weapon = $data_weapons[@weapon_id]
    armor1 = $data_armors[@armor1_id]
    armor2 = $data_armors[@armor2_id]
    armor3 = $data_armors[@armor3_id]
    armor4 = $data_armors[@armor4_id]
    n += weapon != nil ? weapon.str_plus : 0
    n += armor1 != nil ? armor1.str_plus : 0
    n += armor2 != nil ? armor2.str_plus : 0
    n += armor3 != nil ? armor3.str_plus : 0
    n += armor4 != nil ? armor4.str_plus : 0
    return [[n, 1].max, 999].min
  end
  #--------------------------------------------------------------------------
  # * Get Basic Dexterity
  #--------------------------------------------------------------------------
  def base_dex
    n = $data_actors[@actor_id].parameters[3, @level]
    weapon = $data_weapons[@weapon_id]
    armor1 = $data_armors[@armor1_id]
    armor2 = $data_armors[@armor2_id]
    armor3 = $data_armors[@armor3_id]
    armor4 = $data_armors[@armor4_id]
    n += weapon != nil ? weapon.dex_plus : 0
    n += armor1 != nil ? armor1.dex_plus : 0
    n += armor2 != nil ? armor2.dex_plus : 0
    n += armor3 != nil ? armor3.dex_plus : 0
    n += armor4 != nil ? armor4.dex_plus : 0
    return [[n, 1].max, 999].min
  end
  #--------------------------------------------------------------------------
  # * Get Basic Agility
  #--------------------------------------------------------------------------
  def base_agi
    n = $data_actors[@actor_id].parameters[4, @level]
    weapon = $data_weapons[@weapon_id]
    armor1 = $data_armors[@armor1_id]
    armor2 = $data_armors[@armor2_id]
    armor3 = $data_armors[@armor3_id]
    armor4 = $data_armors[@armor4_id]
    n += weapon != nil ? weapon.agi_plus : 0
    n += armor1 != nil ? armor1.agi_plus : 0
    n += armor2 != nil ? armor2.agi_plus : 0
    n += armor3 != nil ? armor3.agi_plus : 0
    n += armor4 != nil ? armor4.agi_plus : 0
    return [[n, 1].max, 999].min
  end
  #--------------------------------------------------------------------------
  # * Get Basic Intelligence
  #--------------------------------------------------------------------------
  def base_int
    n = $data_actors[@actor_id].parameters[5, @level]
    weapon = $data_weapons[@weapon_id]
    armor1 = $data_armors[@armor1_id]
    armor2 = $data_armors[@armor2_id]
    armor3 = $data_armors[@armor3_id]
    armor4 = $data_armors[@armor4_id]
    n += weapon != nil ? weapon.int_plus : 0
    n += armor1 != nil ? armor1.int_plus : 0
    n += armor2 != nil ? armor2.int_plus : 0
    n += armor3 != nil ? armor3.int_plus : 0
    n += armor4 != nil ? armor4.int_plus : 0
    return [[n, 1].max, 999].min
  end
  #--------------------------------------------------------------------------
  # * Get Basic Attack Power
  #--------------------------------------------------------------------------
  def base_atk
    weapon = $data_weapons[@weapon_id]
    return weapon != nil ? weapon.atk : 0
  end
  #--------------------------------------------------------------------------
  # * Get Basic Physical Defense
  #--------------------------------------------------------------------------
  def base_pdef
    weapon = $data_weapons[@weapon_id]
    armor1 = $data_armors[@armor1_id]
    armor2 = $data_armors[@armor2_id]
    armor3 = $data_armors[@armor3_id]
    armor4 = $data_armors[@armor4_id]
    pdef1 = weapon != nil ? weapon.pdef : 0
    pdef2 = armor1 != nil ? armor1.pdef : 0
    pdef3 = armor2 != nil ? armor2.pdef : 0
    pdef4 = armor3 != nil ? armor3.pdef : 0
    pdef5 = armor4 != nil ? armor4.pdef : 0
    return pdef1 + pdef2 + pdef3 + pdef4 + pdef5
  end
  #--------------------------------------------------------------------------
  # * Get Basic Magic Defense
  #--------------------------------------------------------------------------
  def base_mdef
    weapon = $data_weapons[@weapon_id]
    armor1 = $data_armors[@armor1_id]
    armor2 = $data_armors[@armor2_id]
    armor3 = $data_armors[@armor3_id]
    armor4 = $data_armors[@armor4_id]
    mdef1 = weapon != nil ? weapon.mdef : 0
    mdef2 = armor1 != nil ? armor1.mdef : 0
    mdef3 = armor2 != nil ? armor2.mdef : 0
    mdef4 = armor3 != nil ? armor3.mdef : 0
    mdef5 = armor4 != nil ? armor4.mdef : 0
    return mdef1 + mdef2 + mdef3 + mdef4 + mdef5
  end
  #--------------------------------------------------------------------------
  # * Get Basic Evasion Correction
  #--------------------------------------------------------------------------
  def base_eva
    armor1 = $data_armors[@armor1_id]
    armor2 = $data_armors[@armor2_id]
    armor3 = $data_armors[@armor3_id]
    armor4 = $data_armors[@armor4_id]
    eva1 = armor1 != nil ? armor1.eva : 0
    eva2 = armor2 != nil ? armor2.eva : 0
    eva3 = armor3 != nil ? armor3.eva : 0
    eva4 = armor4 != nil ? armor4.eva : 0
    return eva1 + eva2 + eva3 + eva4
  end
  #--------------------------------------------------------------------------
  # * Get Offensive Animation ID for Normal Attacks
  #--------------------------------------------------------------------------
  def animation1_id
    weapon = $data_weapons[@weapon_id]
    return weapon != nil ? weapon.animation1_id : 0
  end
  #--------------------------------------------------------------------------
  # * Get Target Animation ID for Normal Attacks
  #--------------------------------------------------------------------------
  def animation2_id
    weapon = $data_weapons[@weapon_id]
    return weapon != nil ? weapon.animation2_id : 0
  end
  #--------------------------------------------------------------------------
  # * Get Class Name
  #--------------------------------------------------------------------------
  def class_name
    return $data_classes[@class_id].name
  end
  #--------------------------------------------------------------------------
  # * Get EXP String
  #--------------------------------------------------------------------------
  def exp_s
    return @exp_list[@level+1] > 0 ? @exp.to_s : "-------"
  end
  #--------------------------------------------------------------------------
  # * Get Next Level EXP String
  #--------------------------------------------------------------------------
  def next_exp_s
    return @exp_list[@level+1] > 0 ? @exp_list[@level+1].to_s : "-------"
  end
  #--------------------------------------------------------------------------
  # * Get Until Next Level EXP String
  #--------------------------------------------------------------------------
  def next_rest_exp_s
    return @exp_list[@level+1] > 0 ?
      (@exp_list[@level+1] - @exp).to_s : "-------"
  end
  #--------------------------------------------------------------------------
  # * Update Auto State
  #     old_armor : unequipped armor
  #     new_armor : equipped armor
  #--------------------------------------------------------------------------
  def update_auto_state(old_armor, new_armor)
    # Forcefully remove unequipped armor's auto state
    if old_armor != nil and old_armor.auto_state_id != 0
      remove_state(old_armor.auto_state_id, true)
    end
    # Forcefully add unequipped armor's auto state
    if new_armor != nil and new_armor.auto_state_id != 0
      add_state(new_armor.auto_state_id, true)
    end
  end
  #--------------------------------------------------------------------------
  # * Determine Fixed Equipment
  #     equip_type : type of equipment
  #--------------------------------------------------------------------------
  def equip_fix?(equip_type)
    case equip_type
    when 0  # Weapon
      return $data_actors[@actor_id].weapon_fix
    when 1  # Shield
      return $data_actors[@actor_id].armor1_fix
    when 2  # Head
      return $data_actors[@actor_id].armor2_fix
    when 3  # Body
      return $data_actors[@actor_id].armor3_fix
    when 4  # Accessory
      return $data_actors[@actor_id].armor4_fix
    end
    return false
  end
  #--------------------------------------------------------------------------
  # * Change Equipment
  #     equip_type : type of equipment
  #     id    : weapon or armor ID (If 0, remove equipment)
  #--------------------------------------------------------------------------
  def equip(equip_type, id)
    case equip_type
    when 0  # Weapon
      if id == 0 or $game_party.weapon_number(id) > 0
        $game_party.gain_weapon(@weapon_id, 1)
        @weapon_id = id
        $game_party.lose_weapon(id, 1)
      end
    when 1  # Shield
      if id == 0 or $game_party.armor_number(id) > 0
        update_auto_state($data_armors[@armor1_id], $data_armors[id])
        $game_party.gain_armor(@armor1_id, 1)
        @armor1_id = id
        $game_party.lose_armor(id, 1)
      end
    when 2  # Head
      if id == 0 or $game_party.armor_number(id) > 0
        update_auto_state($data_armors[@armor2_id], $data_armors[id])
        $game_party.gain_armor(@armor2_id, 1)
        @armor2_id = id
        $game_party.lose_armor(id, 1)
      end
    when 3  # Body
      if id == 0 or $game_party.armor_number(id) > 0
        update_auto_state($data_armors[@armor3_id], $data_armors[id])
        $game_party.gain_armor(@armor3_id, 1)
        @armor3_id = id
        $game_party.lose_armor(id, 1)
      end
    when 4  # Accessory
      if id == 0 or $game_party.armor_number(id) > 0
        update_auto_state($data_armors[@armor4_id], $data_armors[id])
        $game_party.gain_armor(@armor4_id, 1)
        @armor4_id = id
        $game_party.lose_armor(id, 1)
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Determine if Equippable
  #     item : item
  #--------------------------------------------------------------------------
  def equippable?(item)
    # If weapon
    if item.is_a?(RPG::Weapon)
      # If included among equippable weapons in current class
      if $data_classes[@class_id].weapon_set.include?(item.id)
        return true
      end
    end
    # If armor
    if item.is_a?(RPG::Armor)
      # If included among equippable armor in current class
      if $data_classes[@class_id].armor_set.include?(item.id)
        return true
      end
    end
    return false
  end
  #--------------------------------------------------------------------------
  # * Change EXP
  #     exp : new EXP
  #--------------------------------------------------------------------------
  def exp=(exp)
    @exp = [[exp, 9999999].min, 0].max
    # Level up
    while @exp >= @exp_list[@level+1] and @exp_list[@level+1] > 0
      @level += 1
      # Learn skill
      for j in $data_classes[@class_id].learnings
        if j.level == @level
          learn_skill(j.skill_id)
        end
      end
    end
    # Level down
    while @exp < @exp_list[@level]
      @level -= 1
    end
    # Correction if exceeding current max HP and max SP
    @hp = [@hp, self.maxhp].min
    @sp = [@sp, self.maxsp].min
  end
  #--------------------------------------------------------------------------
  # * Change Level
  #     level : new level
  #--------------------------------------------------------------------------
  def level=(level)
    # Check up and down limits
    level = [[level, $data_actors[@actor_id].final_level].min, 1].max
    # Change EXP
    self.exp = @exp_list[level]
  end
  #--------------------------------------------------------------------------
  # * Learn Skill
  #     skill_id : skill ID
  #--------------------------------------------------------------------------
  def learn_skill(skill_id)
    if skill_id > 0 and not skill_learn?(skill_id)
      @skills.push(skill_id)
      @skills.sort!
    end
  end
  #--------------------------------------------------------------------------
  # * Forget Skill
  #     skill_id : skill ID
  #--------------------------------------------------------------------------
  def forget_skill(skill_id)
    @skills.delete(skill_id)
  end
  #--------------------------------------------------------------------------
  # * Determine if Finished Learning Skill
  #     skill_id : skill ID
  #--------------------------------------------------------------------------
  def skill_learn?(skill_id)
    return @skills.include?(skill_id)
  end
  #--------------------------------------------------------------------------
  # * Determine if Skill can be Used
  #     skill_id : skill ID
  #--------------------------------------------------------------------------
  def skill_can_use?(skill_id)
    if not skill_learn?(skill_id)
      return false
    end
    return super
  end
  #--------------------------------------------------------------------------
  # * Change Name
  #     name : new name
  #--------------------------------------------------------------------------
  def name=(name)
    @name = name
  end
  #--------------------------------------------------------------------------
  # * Change Class ID
  #     class_id : new class ID
  #--------------------------------------------------------------------------
  def class_id=(class_id)
    if $data_classes[class_id] != nil
      @class_id = class_id
      # Remove items that are no longer equippable
      unless equippable?($data_weapons[@weapon_id])
        equip(0, 0)
      end
      unless equippable?($data_armors[@armor1_id])
        equip(1, 0)
      end
      unless equippable?($data_armors[@armor2_id])
        equip(2, 0)
      end
      unless equippable?($data_armors[@armor3_id])
        equip(3, 0)
      end
      unless equippable?($data_armors[@armor4_id])
        equip(4, 0)
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Change Graphics
  #     character_name : new character file name
  #     character_hue  : new character hue
  #     battler_name   : new battler file name
  #     battler_hue    : new battler hue
  #--------------------------------------------------------------------------
  def set_graphic(character_name, character_hue, battler_name, battler_hue)
    @character_name = character_name
    @character_hue = character_hue
    @battler_name = battler_name
    @battler_hue = battler_hue
  end
  #--------------------------------------------------------------------------
  # * Get Battle Screen X-Coordinate
  #--------------------------------------------------------------------------
  def screen_x
    # Return after calculating x-coordinate by order of members in party
    if self.index != nil
      return self.index * 160 + 80
    else
      return 0
    end
  end
  #--------------------------------------------------------------------------
  # * Get Battle Screen Y-Coordinate
  #--------------------------------------------------------------------------
  def screen_y
    return 464
  end
  #--------------------------------------------------------------------------
  # * Get Battle Screen Z-Coordinate
  #--------------------------------------------------------------------------
  def screen_z
    # Return after calculating z-coordinate by order of members in party
    if self.index != nil
      return 4 - self.index
    else
      return 0
    end
  end
end
#==============================================================================
# ** Game_Enemy
#------------------------------------------------------------------------------
#  This class handles enemies. It's used within the Game_Troop class
#  ($game_troop).
#==============================================================================

class Game_Enemy < Game_Battler
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     troop_id     : troop ID
  #     member_index : troop member index
  #--------------------------------------------------------------------------
  def initialize(troop_id, member_index)
    super()
    @troop_id = troop_id
    @member_index = member_index
    troop = $data_troops[@troop_id]
    @enemy_id = troop.members[@member_index].enemy_id
    enemy = $data_enemies[@enemy_id]
    @battler_name = enemy.battler_name
    @battler_hue = enemy.battler_hue
    @hp = maxhp
    @sp = maxsp
    @hidden = troop.members[@member_index].hidden
    @immortal = troop.members[@member_index].immortal
  end
  #--------------------------------------------------------------------------
  # * Get Enemy ID
  #--------------------------------------------------------------------------
  def id
    return @enemy_id
  end
  #--------------------------------------------------------------------------
  # * Get Index
  #--------------------------------------------------------------------------
  def index
    return @member_index
  end
  #--------------------------------------------------------------------------
  # * Get Name
  #--------------------------------------------------------------------------
  def name
    return $data_enemies[@enemy_id].name
  end
  #--------------------------------------------------------------------------
  # * Get Basic Maximum HP
  #--------------------------------------------------------------------------
  def base_maxhp
    return $data_enemies[@enemy_id].maxhp
  end
  #--------------------------------------------------------------------------
  # * Get Basic Maximum SP
  #--------------------------------------------------------------------------
  def base_maxsp
    return $data_enemies[@enemy_id].maxsp
  end
  #--------------------------------------------------------------------------
  # * Get Basic Strength
  #--------------------------------------------------------------------------
  def base_str
    return $data_enemies[@enemy_id].str
  end
  #--------------------------------------------------------------------------
  # * Get Basic Dexterity
  #--------------------------------------------------------------------------
  def base_dex
    return $data_enemies[@enemy_id].dex
  end
  #--------------------------------------------------------------------------
  # * Get Basic Agility
  #--------------------------------------------------------------------------
  def base_agi
    return $data_enemies[@enemy_id].agi
  end
  #--------------------------------------------------------------------------
  # * Get Basic Intelligence
  #--------------------------------------------------------------------------
  def base_int
    return $data_enemies[@enemy_id].int
  end
  #--------------------------------------------------------------------------
  # * Get Basic Attack Power
  #--------------------------------------------------------------------------
  def base_atk
    return $data_enemies[@enemy_id].atk
  end
  #--------------------------------------------------------------------------
  # * Get Basic Physical Defense
  #--------------------------------------------------------------------------
  def base_pdef
    return $data_enemies[@enemy_id].pdef
  end
  #--------------------------------------------------------------------------
  # * Get Basic Magic Defense
  #--------------------------------------------------------------------------
  def base_mdef
    return $data_enemies[@enemy_id].mdef
  end
  #--------------------------------------------------------------------------
  # * Get Basic Evasion
  #--------------------------------------------------------------------------
  def base_eva
    return $data_enemies[@enemy_id].eva
  end
  #--------------------------------------------------------------------------
  # * Get Offensive Animation ID for Normal Attack
  #--------------------------------------------------------------------------
  def animation1_id
    return $data_enemies[@enemy_id].animation1_id
  end
  #--------------------------------------------------------------------------
  # * Get Target Animation ID for Normal Attack
  #--------------------------------------------------------------------------
  def animation2_id
    return $data_enemies[@enemy_id].animation2_id
  end
  #--------------------------------------------------------------------------
  # * Get Element Revision Value
  #     element_id : Element ID
  #--------------------------------------------------------------------------
  def element_rate(element_id)
    # Get a numerical value corresponding to element effectiveness
    table = [0,200,150,100,50,0,-100]
    result = table[$data_enemies[@enemy_id].element_ranks[element_id]]
    # If protected by state, this element is reduced by half
    for i in @states
      if $data_states[i].guard_element_set.include?(element_id)
        result /= 2
      end
    end
    # End Method
    return result
  end
  #--------------------------------------------------------------------------
  # * Get State Effectiveness
  #--------------------------------------------------------------------------
  def state_ranks
    return $data_enemies[@enemy_id].state_ranks
  end
  #--------------------------------------------------------------------------
  # * Determine State Guard
  #     state_id : state ID
  #--------------------------------------------------------------------------
  def state_guard?(state_id)
    return false
  end
  #--------------------------------------------------------------------------
  # * Get Normal Attack Element
  #--------------------------------------------------------------------------
  def element_set
    return []
  end
  #--------------------------------------------------------------------------
  # * Get Normal Attack State Change (+)
  #--------------------------------------------------------------------------
  def plus_state_set
    return []
  end
  #--------------------------------------------------------------------------
  # * Get Normal Attack State Change (-)
  #--------------------------------------------------------------------------
  def minus_state_set
    return []
  end
  #--------------------------------------------------------------------------
  # * Aquire Actions
  #--------------------------------------------------------------------------
  def actions
    return $data_enemies[@enemy_id].actions
  end
  #--------------------------------------------------------------------------
  # * Get EXP
  #--------------------------------------------------------------------------
  def exp
    return $data_enemies[@enemy_id].exp
  end
  #--------------------------------------------------------------------------
  # * Get Gold
  #--------------------------------------------------------------------------
  def gold
    return $data_enemies[@enemy_id].gold
  end
  #--------------------------------------------------------------------------
  # * Get Item ID
  #--------------------------------------------------------------------------
  def item_id
    return $data_enemies[@enemy_id].item_id
  end
  #--------------------------------------------------------------------------
  # * Get Weapon ID
  #--------------------------------------------------------------------------
  def weapon_id
    return $data_enemies[@enemy_id].weapon_id
  end
  #--------------------------------------------------------------------------
  # * Get Armor ID
  #--------------------------------------------------------------------------
  def armor_id
    return $data_enemies[@enemy_id].armor_id
  end
  #--------------------------------------------------------------------------
  # * Get Treasure Appearance Probability
  #--------------------------------------------------------------------------
  def treasure_prob
    return $data_enemies[@enemy_id].treasure_prob
  end
  #--------------------------------------------------------------------------
  # * Get Battle Screen X-Coordinate
  #--------------------------------------------------------------------------
  def screen_x
    return $data_troops[@troop_id].members[@member_index].x
  end
  #--------------------------------------------------------------------------
  # * Get Battle Screen Y-Coordinate
  #--------------------------------------------------------------------------
  def screen_y
    return $data_troops[@troop_id].members[@member_index].y
  end
  #--------------------------------------------------------------------------
  # * Get Battle Screen Z-Coordinate
  #--------------------------------------------------------------------------
  def screen_z
    return screen_y
  end
  #--------------------------------------------------------------------------
  # * Escape
  #--------------------------------------------------------------------------
  def escape
    # Set hidden flag
    @hidden = true
    # Clear current action
    self.current_action.clear
  end
  #--------------------------------------------------------------------------
  # * Transform
  #     enemy_id : ID of enemy to be transformed
  #--------------------------------------------------------------------------
  def transform(enemy_id)
    # Change enemy ID
    @enemy_id = enemy_id
    # Change battler graphics
    @battler_name = $data_enemies[@enemy_id].battler_name
    @battler_hue = $data_enemies[@enemy_id].battler_hue
    # Remake action
    make_action
  end
  #--------------------------------------------------------------------------
  # * Make Action
  #--------------------------------------------------------------------------
  def make_action
    # Clear current action
    self.current_action.clear
    # If unable to move
    unless self.movable?
      # End Method
      return
    end
    # Extract current effective actions
    available_actions = []
    rating_max = 0
    for action in self.actions
      # Confirm turn conditions
      n = $game_temp.battle_turn
      a = action.condition_turn_a
      b = action.condition_turn_b
      if (b == 0 and n != a) or
         (b > 0 and (n < 1 or n < a or n % b != a % b))
        next
      end
      # Confirm HP conditions
      if self.hp * 100.0 / self.maxhp > action.condition_hp
        next
      end
      # Confirm level conditions
      if $game_party.max_level < action.condition_level
        next
      end
      # Confirm switch conditions
      switch_id = action.condition_switch_id
      if switch_id > 0 and $game_switches[switch_id] == false
        next
      end
      # Add this action to applicable conditions
      available_actions.push(action)
      if action.rating > rating_max
        rating_max = action.rating
      end
    end
    # Calculate total with max rating value at 3 (exclude 0 or less)
    ratings_total = 0
    for action in available_actions
      if action.rating > rating_max - 3
        ratings_total += action.rating - (rating_max - 3)
      end
    end
    # If ratings total isn't 0
    if ratings_total > 0
      # Create random numbers
      value = rand(ratings_total)
      # Set things that correspond to created random numbers as current action
      for action in available_actions
        if action.rating > rating_max - 3
          if value < action.rating - (rating_max - 3)
            self.current_action.kind = action.kind
            self.current_action.basic = action.basic
            self.current_action.skill_id = action.skill_id
            self.current_action.decide_random_target_for_enemy
            return
          else
            value -= action.rating - (rating_max - 3)
          end
        end
      end
    end
  end
end
#==============================================================================
# ** Game_Actors
#------------------------------------------------------------------------------
#  This class handles the actor array. Refer to "$game_actors" for each
#  instance of this class.
#==============================================================================

class Game_Actors
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    @data = []
  end
  #--------------------------------------------------------------------------
  # * Get Actor
  #     actor_id : actor ID
  #--------------------------------------------------------------------------
  def [](actor_id)
    if actor_id > 999 or $data_actors[actor_id] == nil
      return nil
    end
    if @data[actor_id] == nil
      @data[actor_id] = Game_Actor.new(actor_id)
    end
    return @data[actor_id]
  end
end
#==============================================================================
# ** Game_Party
#------------------------------------------------------------------------------
#  This class handles the party. It includes information on amount of gold 
#  and items. Refer to "$game_party" for the instance of this class.
#==============================================================================

class Game_Party
  #--------------------------------------------------------------------------
  # * Public Instance Variables
  #--------------------------------------------------------------------------
  attr_reader   :actors                   # actors
  attr_reader   :gold                     # amount of gold
  attr_reader   :steps                    # number of steps
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    # Create actor array
    @actors = []
    # Initialize amount of gold and steps
    @gold = 0
    @steps = 0
    # Create amount in possession hash for items, weapons, and armor
    @items = {}
    @weapons = {}
    @armors = {}
  end
  #--------------------------------------------------------------------------
  # * Initial Party Setup
  #--------------------------------------------------------------------------
  def setup_starting_members
    @actors = []
    for i in $data_system.party_members
      @actors.push($game_actors[i])
    end
  end
  #--------------------------------------------------------------------------
  # * Battle Test Party Setup
  #--------------------------------------------------------------------------
  def setup_battle_test_members
    @actors = []
    for battler in $data_system.test_battlers
      actor = $game_actors[battler.actor_id]
      actor.level = battler.level
      gain_weapon(battler.weapon_id, 1)
      gain_armor(battler.armor1_id, 1)
      gain_armor(battler.armor2_id, 1)
      gain_armor(battler.armor3_id, 1)
      gain_armor(battler.armor4_id, 1)
      actor.equip(0, battler.weapon_id)
      actor.equip(1, battler.armor1_id)
      actor.equip(2, battler.armor2_id)
      actor.equip(3, battler.armor3_id)
      actor.equip(4, battler.armor4_id)
      actor.recover_all
      @actors.push(actor)
    end
    @items = {}
    for i in 1...$data_items.size
      if $data_items[i].name != ""
        occasion = $data_items[i].occasion
        if occasion == 0 or occasion == 1
          @items[i] = 99
        end
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Refresh Party Members
  #--------------------------------------------------------------------------
  def refresh
    # Actor objects split from $game_actors right after loading game data
    # Avoid this problem by resetting the actors each time data is loaded.
    new_actors = []
    for i in 0...@actors.size
      if $data_actors[@actors[i].id] != nil
        new_actors.push($game_actors[@actors[i].id])
      end
    end
    @actors = new_actors
  end
  #--------------------------------------------------------------------------
  # * Getting Maximum Level
  #--------------------------------------------------------------------------
  def max_level
    # If 0 members are in the party
    if @actors.size == 0
      return 0
    end
    # Initialize local variable: level
    level = 0
    # Get maximum level of party members
    for actor in @actors
      if level < actor.level
        level = actor.level
      end
    end
    return level
  end
  #--------------------------------------------------------------------------
  # * Add an Actor
  #     actor_id : actor ID
  #--------------------------------------------------------------------------
  def add_actor(actor_id)
    # Get actor
    actor = $game_actors[actor_id]
    # If the party has less than 4 members and this actor is not in the party
    if @actors.size < 4 and not @actors.include?(actor)
      # Add actor
      @actors.push(actor)
      # Refresh player
      $game_player.refresh
    end
  end
  #--------------------------------------------------------------------------
  # * Remove Actor
  #     actor_id : actor ID
  #--------------------------------------------------------------------------
  def remove_actor(actor_id)
    # Delete actor
    @actors.delete($game_actors[actor_id])
    # Refresh player
    $game_player.refresh
  end
  #--------------------------------------------------------------------------
  # * Gain Gold (or lose)
  #     n : amount of gold
  #--------------------------------------------------------------------------
  def gain_gold(n)
    @gold = [[@gold + n, 0].max, 9999999].min
  end
  #--------------------------------------------------------------------------
  # * Lose Gold
  #     n : amount of gold
  #--------------------------------------------------------------------------
  def lose_gold(n)
    # Reverse the numerical value and call it gain_gold
    gain_gold(-n)
  end
  #--------------------------------------------------------------------------
  # * Increase Steps
  #--------------------------------------------------------------------------
  def increase_steps
    @steps = [@steps + 1, 9999999].min
  end
  #--------------------------------------------------------------------------
  # * Get Number of Items Possessed
  #     item_id : item ID
  #--------------------------------------------------------------------------
  def item_number(item_id)
    # If quantity data is in the hash, use it. If not, return 0
    return @items.include?(item_id) ? @items[item_id] : 0
  end
  #--------------------------------------------------------------------------
  # * Get Number of Weapons Possessed
  #     weapon_id : weapon ID
  #--------------------------------------------------------------------------
  def weapon_number(weapon_id)
    # If quantity data is in the hash, use it. If not, return 0
    return @weapons.include?(weapon_id) ? @weapons[weapon_id] : 0
  end
  #--------------------------------------------------------------------------
  # * Get Amount of Armor Possessed
  #     armor_id : armor ID
  #--------------------------------------------------------------------------
  def armor_number(armor_id)
    # If quantity data is in the hash, use it. If not, return 0
    return @armors.include?(armor_id) ? @armors[armor_id] : 0
  end
  #--------------------------------------------------------------------------
  # * Gain Items (or lose)
  #     item_id : item ID
  #     n       : quantity
  #--------------------------------------------------------------------------
  def gain_item(item_id, n)
    # Update quantity data in the hash.
    if item_id > 0
      @items[item_id] = [[item_number(item_id) + n, 0].max, 99].min
    end
  end
  #--------------------------------------------------------------------------
  # * Gain Weapons (or lose)
  #     weapon_id : weapon ID
  #     n         : quantity
  #--------------------------------------------------------------------------
  def gain_weapon(weapon_id, n)
    # Update quantity data in the hash.
    if weapon_id > 0
      @weapons[weapon_id] = [[weapon_number(weapon_id) + n, 0].max, 99].min
    end
  end
  #--------------------------------------------------------------------------
  # * Gain Armor (or lose)
  #     armor_id : armor ID
  #     n        : quantity
  #--------------------------------------------------------------------------
  def gain_armor(armor_id, n)
    # Update quantity data in the hash.
    if armor_id > 0
      @armors[armor_id] = [[armor_number(armor_id) + n, 0].max, 99].min
    end
  end
  #--------------------------------------------------------------------------
  # * Lose Items
  #     item_id : item ID
  #     n       : quantity
  #--------------------------------------------------------------------------
  def lose_item(item_id, n)
    # Reverse the numerical value and call it gain_item
    gain_item(item_id, -n)
  end
  #--------------------------------------------------------------------------
  # * Lose Weapons
  #     weapon_id : weapon ID
  #     n         : quantity
  #--------------------------------------------------------------------------
  def lose_weapon(weapon_id, n)
    # Reverse the numerical value and call it gain_weapon
    gain_weapon(weapon_id, -n)
  end
  #--------------------------------------------------------------------------
  # * Lose Armor
  #     armor_id : armor ID
  #     n        : quantity
  #--------------------------------------------------------------------------
  def lose_armor(armor_id, n)
    # Reverse the numerical value and call it gain_armor
    gain_armor(armor_id, -n)
  end
  #--------------------------------------------------------------------------
  # * Determine if Item is Usable
  #     item_id : item ID
  #--------------------------------------------------------------------------
  def item_can_use?(item_id)
    # If item quantity is 0
    if item_number(item_id) == 0
      # Unusable
      return false
    end
    # Get usable time
    occasion = $data_items[item_id].occasion
    # If in battle
    if $game_temp.in_battle
      # If useable time is 0 (normal) or 1 (only battle) it's usable
      return (occasion == 0 or occasion == 1)
    end
    # If useable time is 0 (normal) or 2 (only menu) it's usable
    return (occasion == 0 or occasion == 2)
  end
  #--------------------------------------------------------------------------
  # * Clear All Member Actions
  #--------------------------------------------------------------------------
  def clear_actions
    # Clear All Member Actions
    for actor in @actors
      actor.current_action.clear
    end
  end
  #--------------------------------------------------------------------------
  # * Determine if Command is Inputable
  #--------------------------------------------------------------------------
  def inputable?
    # Return true if input is possible for one person as well
    for actor in @actors
      if actor.inputable?
        return true
      end
    end
    return false
  end
  #--------------------------------------------------------------------------
  # * Determine Everyone is Dead
  #--------------------------------------------------------------------------
  def all_dead?
    # If number of party members is 0
    if $game_party.actors.size == 0
      return false
    end
    # If an actor is in the party with 0 or more HP
    for actor in @actors
      if actor.hp > 0
        return false
      end
    end
    # All members dead
    return true
  end
  #--------------------------------------------------------------------------
  # * Slip Damage Check (for map)
  #--------------------------------------------------------------------------
  def check_map_slip_damage
    for actor in @actors
      if actor.hp > 0 and actor.slip_damage?
        actor.hp -= [actor.maxhp / 100, 1].max
        if actor.hp == 0
          $game_system.se_play($data_system.actor_collapse_se)
        end
        $game_screen.start_flash(Color.new(255,0,0,128), 4)
        $game_temp.gameover = $game_party.all_dead?
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Random Selection of Target Actor
  #     hp0 : limited to actors with 0 HP
  #--------------------------------------------------------------------------
  def random_target_actor(hp0 = false)
    # Initialize roulette
    roulette = []
    # Loop
    for actor in @actors
      # If it fits the conditions
      if (not hp0 and actor.exist?) or (hp0 and actor.hp0?)
        # Get actor class [position]
        position = $data_classes[actor.class_id].position
        # Front guard: n = 4; Mid guard: n = 3; Rear guard: n = 2
        n = 4 - position
        # Add actor to roulette n times
        n.times do
          roulette.push(actor)
        end
      end
    end
    # If roulette size is 0
    if roulette.size == 0
      return nil
    end
    # Spin the roulette, choose an actor
    return roulette[rand(roulette.size)]
  end
  #--------------------------------------------------------------------------
  # * Random Selection of Target Actor (HP 0)
  #--------------------------------------------------------------------------
  def random_target_actor_hp0
    return random_target_actor(true)
  end
  #--------------------------------------------------------------------------
  # * Smooth Selection of Target Actor
  #     actor_index : actor index
  #--------------------------------------------------------------------------
  def smooth_target_actor(actor_index)
    # Get an actor
    actor = @actors[actor_index]
    # If an actor exists
    if actor != nil and actor.exist?
      return actor
    end
    # Loop
    for actor in @actors
      # If an actor exists
      if actor.exist?
        return actor
      end
    end
  end
end
#==============================================================================
# ** Game_Troop
#------------------------------------------------------------------------------
#  This class deals with troops. Refer to "$game_troop" for the instance of
#  this class.
#==============================================================================

class Game_Troop
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    # Create enemy array
    @enemies = []
  end
  #--------------------------------------------------------------------------
  # * Get Enemies
  #--------------------------------------------------------------------------
  def enemies
    return @enemies
  end
  #--------------------------------------------------------------------------
  # * Setup
  #     troop_id : troop ID
  #--------------------------------------------------------------------------
  def setup(troop_id)
    # Set array of enemies who are set as troops
    @enemies = []
    troop = $data_troops[troop_id]
    for i in 0...troop.members.size
      enemy = $data_enemies[troop.members[i].enemy_id]
      if enemy != nil
        @enemies.push(Game_Enemy.new(troop_id, i))
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Random Selection of a Target Enemy
  #     hp0 : limited to enemies with 0 HP
  #--------------------------------------------------------------------------
  def random_target_enemy(hp0 = false)
    # Initialize roulette
    roulette = []
    # Loop
    for enemy in @enemies
      # If it fits the conditions
      if (not hp0 and enemy.exist?) or (hp0 and enemy.hp0?)
        # Add an enemy to the roulette
        roulette.push(enemy)
      end
    end
    # If roulette size is 0
    if roulette.size == 0
      return nil
    end
    # Spin the roulette, choose an enemy
    return roulette[rand(roulette.size)]
  end
  #--------------------------------------------------------------------------
  # * Random Selection of a Target Enemy (HP 0)
  #--------------------------------------------------------------------------
  def random_target_enemy_hp0
    return random_target_enemy(true)
  end
  #--------------------------------------------------------------------------
  # * Smooth Selection of a Target Enemy
  #     enemy_index : enemy index
  #--------------------------------------------------------------------------
  def smooth_target_enemy(enemy_index)
    # Get an enemy
    enemy = @enemies[enemy_index]
    # If an enemy exists
    if enemy != nil and enemy.exist?
      return enemy
    end
    # Loop
    for enemy in @enemies
      # If an enemy exists
      if enemy.exist?
        return enemy
      end
    end
  end
end
#==============================================================================
# ** Game_Map
#------------------------------------------------------------------------------
#  This class handles the map. It includes scrolling and passable determining
#  functions. Refer to "$game_map" for the instance of this class.
#==============================================================================

class Game_Map
  #--------------------------------------------------------------------------
  # * Public Instance Variables
  #--------------------------------------------------------------------------
  attr_accessor :tileset_name             # tileset file name
  attr_accessor :autotile_names           # autotile file name
  attr_accessor :panorama_name            # panorama file name
  attr_accessor :panorama_hue             # panorama hue
  attr_accessor :fog_name                 # fog file name
  attr_accessor :fog_hue                  # fog hue
  attr_accessor :fog_opacity              # fog opacity level
  attr_accessor :fog_blend_type           # fog blending method
  attr_accessor :fog_zoom                 # fog zoom rate
  attr_accessor :fog_sx                   # fog sx
  attr_accessor :fog_sy                   # fog sy
  attr_accessor :battleback_name          # battleback file name
  attr_accessor :display_x                # display x-coordinate * 128
  attr_accessor :display_y                # display y-coordinate * 128
  attr_accessor :need_refresh             # refresh request flag
  attr_reader   :passages                 # passage table
  attr_reader   :priorities               # prioroty table
  attr_reader   :terrain_tags             # terrain tag table
  attr_reader   :events                   # events
  attr_reader   :fog_ox                   # fog x-coordinate starting point
  attr_reader   :fog_oy                   # fog y-coordinate starting point
  attr_reader   :fog_tone                 # fog color tone
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    @map_id = 0
    @display_x = 0
    @display_y = 0
  end
  #--------------------------------------------------------------------------
  # * Setup
  #     map_id : map ID
  #--------------------------------------------------------------------------
  def setup(map_id)
    # Put map ID in @map_id memory
    @map_id = map_id
    # Load map from file and set @map
    @map = load_data(sprintf("Data/Map%03d.rxdata", @map_id))
    # set tile set information in opening instance variables
    tileset = $data_tilesets[@map.tileset_id]
    @tileset_name = tileset.tileset_name
    @autotile_names = tileset.autotile_names
    @panorama_name = tileset.panorama_name
    @panorama_hue = tileset.panorama_hue
    @fog_name = tileset.fog_name
    @fog_hue = tileset.fog_hue
    @fog_opacity = tileset.fog_opacity
    @fog_blend_type = tileset.fog_blend_type
    @fog_zoom = tileset.fog_zoom
    @fog_sx = tileset.fog_sx
    @fog_sy = tileset.fog_sy
    @battleback_name = tileset.battleback_name
    @passages = tileset.passages
    @priorities = tileset.priorities
    @terrain_tags = tileset.terrain_tags
    # Initialize displayed coordinates
    @display_x = 0
    @display_y = 0
    # Clear refresh request flag
    @need_refresh = false
    # Set map event data
    @events = {}
    for i in @map.events.keys
      @events[i] = Game_Event.new(@map_id, @map.events[i])
    end
    # Set common event data
    @common_events = {}
    for i in 1...$data_common_events.size
      @common_events[i] = Game_CommonEvent.new(i)
    end
    # Initialize all fog information
    @fog_ox = 0
    @fog_oy = 0
    @fog_tone = Tone.new(0, 0, 0, 0)
    @fog_tone_target = Tone.new(0, 0, 0, 0)
    @fog_tone_duration = 0
    @fog_opacity_duration = 0
    @fog_opacity_target = 0
    # Initialize scroll information
    @scroll_direction = 2
    @scroll_rest = 0
    @scroll_speed = 4
  end
  #--------------------------------------------------------------------------
  # * Get Map ID
  #--------------------------------------------------------------------------
  def map_id
    return @map_id
  end
  #--------------------------------------------------------------------------
  # * Get Width
  #--------------------------------------------------------------------------
  def width
    return @map.width
  end
  #--------------------------------------------------------------------------
  # * Get Height
  #--------------------------------------------------------------------------
  def height
    return @map.height
  end
  #--------------------------------------------------------------------------
  # * Get Encounter List
  #--------------------------------------------------------------------------
  def encounter_list
    return @map.encounter_list
  end
  #--------------------------------------------------------------------------
  # * Get Encounter Steps
  #--------------------------------------------------------------------------
  def encounter_step
    return @map.encounter_step
  end
  #--------------------------------------------------------------------------
  # * Get Map Data
  #--------------------------------------------------------------------------
  def data
    return @map.data
  end
  #--------------------------------------------------------------------------
  # * Automatically Change Background Music and Backround Sound
  #--------------------------------------------------------------------------
  def autoplay
    if @map.autoplay_bgm
      $game_system.bgm_play(@map.bgm)
    end
    if @map.autoplay_bgs
      $game_system.bgs_play(@map.bgs)
    end
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    # If map ID is effective
    if @map_id > 0
      # Refresh all map events
      for event in @events.values
        event.refresh
      end
      # Refresh all common events
      for common_event in @common_events.values
        common_event.refresh
      end
    end
    # Clear refresh request flag
    @need_refresh = false
  end
  #--------------------------------------------------------------------------
  # * Scroll Down
  #     distance : scroll distance
  #--------------------------------------------------------------------------
  def scroll_down(distance)
    @display_y = [@display_y + distance, (self.height - 15) * 128].min
  end
  #--------------------------------------------------------------------------
  # * Scroll Left
  #     distance : scroll distance
  #--------------------------------------------------------------------------
  def scroll_left(distance)
    @display_x = [@display_x - distance, 0].max
  end
  #--------------------------------------------------------------------------
  # * Scroll Right
  #     distance : scroll distance
  #--------------------------------------------------------------------------
  def scroll_right(distance)
    @display_x = [@display_x + distance, (self.width - 20) * 128].min
  end
  #--------------------------------------------------------------------------
  # * Scroll Up
  #     distance : scroll distance
  #--------------------------------------------------------------------------
  def scroll_up(distance)
    @display_y = [@display_y - distance, 0].max
  end
  #--------------------------------------------------------------------------
  # * Determine Valid Coordinates
  #     x          : x-coordinate
  #     y          : y-coordinate
  #--------------------------------------------------------------------------
  def valid?(x, y)
    return (x >= 0 and x < width and y >= 0 and y < height)
  end
  #--------------------------------------------------------------------------
  # * Determine if Passable
  #     x          : x-coordinate
  #     y          : y-coordinate
  #     d          : direction (0,2,4,6,8,10)
  #                  *  0,10 = determine if all directions are impassable
  #     self_event : Self (If event is determined passable)
  #--------------------------------------------------------------------------
  def passable?(x, y, d, self_event = nil)
    # If coordinates given are outside of the map
    unless valid?(x, y)
      # impassable
      return false
    end
    # Change direction (0,2,4,6,8,10) to obstacle bit (0,1,2,4,8,0)
    bit = (1 << (d / 2 - 1)) & 0x0f
    # Loop in all events
    for event in events.values
      # If tiles other than self are consistent with coordinates
      if event.tile_id >= 0 and event != self_event and
         event.x == x and event.y == y and not event.through
        # If obstacle bit is set
        if @passages[event.tile_id] & bit != 0
          # impassable
          return false
        # If obstacle bit is set in all directions
        elsif @passages[event.tile_id] & 0x0f == 0x0f
          # impassable
          return false
        # If priorities other than that are 0
        elsif @priorities[event.tile_id] == 0
          # passable
          return true
        end
      end
    end
    # Loop searches in order from top of layer
    for i in [2, 1, 0]
      # Get tile ID
      tile_id = data[x, y, i]
      # Tile ID acquistion failure
      if tile_id == nil
        # impassable
        return false
      # If obstacle bit is set
      elsif @passages[tile_id] & bit != 0
        # impassable
        return false
      # If obstacle bit is set in all directions
      elsif @passages[tile_id] & 0x0f == 0x0f
        # impassable
        return false
      # If priorities other than that are 0
      elsif @priorities[tile_id] == 0
        # passable
        return true
      end
    end
    # passable
    return true
  end
  #--------------------------------------------------------------------------
  # * Determine Thicket
  #     x          : x-coordinate
  #     y          : y-coordinate
  #--------------------------------------------------------------------------
  def bush?(x, y)
    if @map_id != 0
      for i in [2, 1, 0]
        tile_id = data[x, y, i]
        if tile_id == nil
          return false
        elsif @passages[tile_id] & 0x40 == 0x40
          return true
        end
      end
    end
    return false
  end
  #--------------------------------------------------------------------------
  # * Determine Counter
  #     x          : x-coordinate
  #     y          : y-coordinate
  #--------------------------------------------------------------------------
  def counter?(x, y)
    if @map_id != 0
      for i in [2, 1, 0]
        tile_id = data[x, y, i]
        if tile_id == nil
          return false
        elsif @passages[tile_id] & 0x80 == 0x80
          return true
        end
      end
    end
    return false
  end
  #--------------------------------------------------------------------------
  # * Get Terrain Tag
  #     x          : x-coordinate
  #     y          : y-coordinate
  #--------------------------------------------------------------------------
  def terrain_tag(x, y)
    if @map_id != 0
      for i in [2, 1, 0]
        tile_id = data[x, y, i]
        if tile_id == nil
          return 0
        elsif @terrain_tags[tile_id] > 0
          return @terrain_tags[tile_id]
        end
      end
    end
    return 0
  end
  #--------------------------------------------------------------------------
  # * Get Designated Position Event ID
  #     x          : x-coordinate
  #     y          : y-coordinate
  #--------------------------------------------------------------------------
  def check_event(x, y)
    for event in $game_map.events.values
      if event.x == x and event.y == y
        return event.id
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Start Scroll
  #     direction : scroll direction
  #     distance  : scroll distance
  #     speed     : scroll speed
  #--------------------------------------------------------------------------
  def start_scroll(direction, distance, speed)
    @scroll_direction = direction
    @scroll_rest = distance * 128
    @scroll_speed = speed
  end
  #--------------------------------------------------------------------------
  # * Determine if Scrolling
  #--------------------------------------------------------------------------
  def scrolling?
    return @scroll_rest > 0
  end
  #--------------------------------------------------------------------------
  # * Start Changing Fog Color Tone
  #     tone     : color tone
  #     duration : time
  #--------------------------------------------------------------------------
  def start_fog_tone_change(tone, duration)
    @fog_tone_target = tone.clone
    @fog_tone_duration = duration
    if @fog_tone_duration == 0
      @fog_tone = @fog_tone_target.clone
    end
  end
  #--------------------------------------------------------------------------
  # * Start Changing Fog Opacity Level
  #     opacity  : opacity level
  #     duration : time
  #--------------------------------------------------------------------------
  def start_fog_opacity_change(opacity, duration)
    @fog_opacity_target = opacity * 1.0
    @fog_opacity_duration = duration
    if @fog_opacity_duration == 0
      @fog_opacity = @fog_opacity_target
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # Refresh map if necessary
    if $game_map.need_refresh
      refresh
    end
    # If scrolling
    if @scroll_rest > 0
      # Change from scroll speed to distance in map coordinates
      distance = 2 ** @scroll_speed
      # Execute scrolling
      case @scroll_direction
      when 2  # Down
        scroll_down(distance)
      when 4  # Left
        scroll_left(distance)
      when 6  # Right
        scroll_right(distance)
      when 8  # Up
        scroll_up(distance)
      end
      # Subtract distance scrolled
      @scroll_rest -= distance
    end
    # Update map event
    for event in @events.values
      event.update
    end
    # Update common event
    for common_event in @common_events.values
      common_event.update
    end
    # Manage fog scrolling
    @fog_ox -= @fog_sx / 8.0
    @fog_oy -= @fog_sy / 8.0
    # Manage change in fog color tone
    if @fog_tone_duration >= 1
      d = @fog_tone_duration
      target = @fog_tone_target
      @fog_tone.red = (@fog_tone.red * (d - 1) + target.red) / d
      @fog_tone.green = (@fog_tone.green * (d - 1) + target.green) / d
      @fog_tone.blue = (@fog_tone.blue * (d - 1) + target.blue) / d
      @fog_tone.gray = (@fog_tone.gray * (d - 1) + target.gray) / d
      @fog_tone_duration -= 1
    end
    # Manage change in fog opacity level
    if @fog_opacity_duration >= 1
      d = @fog_opacity_duration
      @fog_opacity = (@fog_opacity * (d - 1) + @fog_opacity_target) / d
      @fog_opacity_duration -= 1
    end
  end
end
#==============================================================================
# ** Game_CommonEvent
#------------------------------------------------------------------------------
#  This class handles common events. It includes execution of parallel process
#  event. This class is used within the Game_Map class ($game_map).
#==============================================================================

class Game_CommonEvent
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     common_event_id : common event ID
  #--------------------------------------------------------------------------
  def initialize(common_event_id)
    @common_event_id = common_event_id
    @interpreter = nil
    refresh
  end
  #--------------------------------------------------------------------------
  # * Get Name
  #--------------------------------------------------------------------------
  def name
    return $data_common_events[@common_event_id].name
  end
  #--------------------------------------------------------------------------
  # * Get Trigger
  #--------------------------------------------------------------------------
  def trigger
    return $data_common_events[@common_event_id].trigger
  end
  #--------------------------------------------------------------------------
  # * Get Condition Switch ID
  #--------------------------------------------------------------------------
  def switch_id
    return $data_common_events[@common_event_id].switch_id
  end
  #--------------------------------------------------------------------------
  # * Get List of Event Commands
  #--------------------------------------------------------------------------
  def list
    return $data_common_events[@common_event_id].list
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    # Create an interpreter for parallel process if necessary
    if self.trigger == 2 and $game_switches[self.switch_id] == true
      if @interpreter == nil
        @interpreter = Interpreter.new
      end
    else
      @interpreter = nil
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # If parallel process is valid
    if @interpreter != nil
      # If not running
      unless @interpreter.running?
        # Set up event
        @interpreter.setup(self.list, 0)
      end
      # Update interpreter
      @interpreter.update
    end
  end
end
#==============================================================================
# ** Game_Character (part 1)
#------------------------------------------------------------------------------
#  This class deals with characters. It's used as a superclass for the
#  Game_Player and Game_Event classes.
#==============================================================================

class Game_Character
  #--------------------------------------------------------------------------
  # * Public Instance Variables
  #--------------------------------------------------------------------------
  attr_reader   :id                       # ID
  attr_reader   :x                        # map x-coordinate (logical)
  attr_reader   :y                        # map y-coordinate (logical)
  attr_reader   :real_x                   # map x-coordinate (real * 128)
  attr_reader   :real_y                   # map y-coordinate (real * 128)
  attr_reader   :tile_id                  # tile ID (invalid if 0)
  attr_reader   :character_name           # character file name
  attr_reader   :character_hue            # character hue
  attr_reader   :opacity                  # opacity level
  attr_reader   :blend_type               # blending method
  attr_reader   :direction                # direction
  attr_reader   :pattern                  # pattern
  attr_reader   :move_route_forcing       # forced move route flag
  attr_reader   :through                  # through
  attr_accessor :animation_id             # animation ID
  attr_accessor :transparent              # transparent flag
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    @id = 0
    @x = 0
    @y = 0
    @real_x = 0
    @real_y = 0
    @tile_id = 0
    @character_name = ""
    @character_hue = 0
    @opacity = 255
    @blend_type = 0
    @direction = 2
    @pattern = 0
    @move_route_forcing = false
    @through = false
    @animation_id = 0
    @transparent = false
    @original_direction = 2
    @original_pattern = 0
    @move_type = 0
    @move_speed = 4
    @move_frequency = 6
    @move_route = nil
    @move_route_index = 0
    @original_move_route = nil
    @original_move_route_index = 0
    @walk_anime = true
    @step_anime = false
    @direction_fix = false
    @always_on_top = false
    @anime_count = 0
    @stop_count = 0
    @jump_count = 0
    @jump_peak = 0
    @wait_count = 0
    @locked = false
    @prelock_direction = 0
  end
  #--------------------------------------------------------------------------
  # * Determine if Moving
  #--------------------------------------------------------------------------
  def moving?
    # If logical coordinates differ from real coordinates,
    # movement is occurring.
    return (@real_x != @x * 128 or @real_y != @y * 128)
  end
  #--------------------------------------------------------------------------
  # * Determine if Jumping
  #--------------------------------------------------------------------------
  def jumping?
    # A jump is occurring if jump count is larger than 0
    return @jump_count > 0
  end
  #--------------------------------------------------------------------------
  # * Straighten Position
  #--------------------------------------------------------------------------
  def straighten
    # If moving animation or stop animation is ON
    if @walk_anime or @step_anime
      # Set pattern to 0
      @pattern = 0
    end
    # Clear animation count
    @anime_count = 0
    # Clear prelock direction
    @prelock_direction = 0
  end
  #--------------------------------------------------------------------------
  # * Force Move Route
  #     move_route : new move route
  #--------------------------------------------------------------------------
  def force_move_route(move_route)
    # Save original move route
    if @original_move_route == nil
      @original_move_route = @move_route
      @original_move_route_index = @move_route_index
    end
    # Change move route
    @move_route = move_route
    @move_route_index = 0
    # Set forced move route flag
    @move_route_forcing = true
    # Clear prelock direction
    @prelock_direction = 0
    # Clear wait count
    @wait_count = 0
    # Move cutsom
    move_type_custom
  end
  #--------------------------------------------------------------------------
  # * Determine if Passable
  #     x : x-coordinate
  #     y : y-coordinate
  #     d : direction (0,2,4,6,8)
  #         * 0 = Determines if all directions are impassable (for jumping)
  #--------------------------------------------------------------------------
  def passable?(x, y, d)
    # Get new coordinates
    new_x = x + (d == 6 ? 1 : d == 4 ? -1 : 0)
    new_y = y + (d == 2 ? 1 : d == 8 ? -1 : 0)
    # If coordinates are outside of map
    unless $game_map.valid?(new_x, new_y)
      # impassable
      return false
    end
    # If through is ON
    if @through
      # passable
      return true
    end
    # If unable to leave first move tile in designated direction
    unless $game_map.passable?(x, y, d, self)
      # impassable
      return false
    end
    # If unable to enter move tile in designated direction
    unless $game_map.passable?(new_x, new_y, 10 - d)
      # impassable
      return false
    end
    # Loop all events
    for event in $game_map.events.values
      # If event coordinates are consistent with move destination
      if event.x == new_x and event.y == new_y
        # If through is OFF
        unless event.through
          # If self is event
          if self != $game_player
            # impassable
            return false
          end
          # With self as the player and partner graphic as character
          if event.character_name != ""
            # impassable
            return false
          end
        end
      end
    end
    # If player coordinates are consistent with move destination
    if $game_player.x == new_x and $game_player.y == new_y
      # If through is OFF
      unless $game_player.through
        # If your own graphic is the character
        if @character_name != ""
          # impassable
          return false
        end
      end
    end
    # passable
    return true
  end
  #--------------------------------------------------------------------------
  # * Lock
  #--------------------------------------------------------------------------
  def lock
    # If already locked
    if @locked
      # End method
      return
    end
    # Save prelock direction
    @prelock_direction = @direction
    # Turn toward player
    turn_toward_player
    # Set locked flag
    @locked = true
  end
  #--------------------------------------------------------------------------
  # * Determine if Locked
  #--------------------------------------------------------------------------
  def lock?
    return @locked
  end
  #--------------------------------------------------------------------------
  # * Unlock
  #--------------------------------------------------------------------------
  def unlock
    # If not locked
    unless @locked
      # End method
      return
    end
    # Clear locked flag
    @locked = false
    # If direction is not fixed
    unless @direction_fix
      # If prelock direction is saved
      if @prelock_direction != 0
        # Restore prelock direction
        @direction = @prelock_direction
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Move to Designated Position
  #     x : x-coordinate
  #     y : y-coordinate
  #--------------------------------------------------------------------------
  def moveto(x, y)
    @x = x % $game_map.width
    @y = y % $game_map.height
    @real_x = @x * 128
    @real_y = @y * 128
    @prelock_direction = 0
  end
  #--------------------------------------------------------------------------
  # * Get Screen X-Coordinates
  #--------------------------------------------------------------------------
  def screen_x
    # Get screen coordinates from real coordinates and map display position
    return (@real_x - $game_map.display_x + 3) / 4 + 16
  end
  #--------------------------------------------------------------------------
  # * Get Screen Y-Coordinates
  #--------------------------------------------------------------------------
  def screen_y
    # Get screen coordinates from real coordinates and map display position
    y = (@real_y - $game_map.display_y + 3) / 4 + 32
    # Make y-coordinate smaller via jump count
    if @jump_count >= @jump_peak
      n = @jump_count - @jump_peak
    else
      n = @jump_peak - @jump_count
    end
    return y - (@jump_peak * @jump_peak - n * n) / 2
  end
  #--------------------------------------------------------------------------
  # * Get Screen Z-Coordinates
  #     height : character height
  #--------------------------------------------------------------------------
  def screen_z(height = 0)
    # If display flag on closest surface is ON
    if @always_on_top
      # 999, unconditional
      return 999
    end
    # Get screen coordinates from real coordinates and map display position
    z = (@real_y - $game_map.display_y + 3) / 4 + 32
    # If tile
    if @tile_id > 0
      # Add tile priority * 32
      return z + $game_map.priorities[@tile_id] * 32
    # If character
    else
      # If height exceeds 32, then add 31
      return z + ((height > 32) ? 31 : 0)
    end
  end
  #--------------------------------------------------------------------------
  # * Get Thicket Depth
  #--------------------------------------------------------------------------
  def bush_depth
    # If tile, or if display flag on the closest surface is ON
    if @tile_id > 0 or @always_on_top
      return 0
    end
    # If element tile other than jumping, then 12; anything else = 0
    if @jump_count == 0 and $game_map.bush?(@x, @y)
      return 12
    else
      return 0
    end
  end
  #--------------------------------------------------------------------------
  # * Get Terrain Tag
  #--------------------------------------------------------------------------
  def terrain_tag
    return $game_map.terrain_tag(@x, @y)
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # Branch with jumping, moving, and stopping
    if jumping?
      update_jump
    elsif moving?
      update_move
    else
      update_stop
    end
    # If animation count exceeds maximum value
    # * Maximum value is move speed * 1 taken from basic value 18
    if @anime_count > 18 - @move_speed * 2
      # If stop animation is OFF when stopping
      if not @step_anime and @stop_count > 0
        # Return to original pattern
        @pattern = @original_pattern
      # If stop animation is ON when moving
      else
        # Update pattern
        @pattern = (@pattern + 1) % 4
      end
      # Clear animation count
      @anime_count = 0
    end
    # If waiting
    if @wait_count > 0
      # Reduce wait count
      @wait_count -= 1
      return
    end
    # If move route is forced
    if @move_route_forcing
      # Custom move
      move_type_custom
      return
    end
    # When waiting for event execution or locked
    if @starting or lock?
      # Not moving by self
      return
    end
    # If stop count exceeds a certain value (computed from move frequency)
    if @stop_count > (40 - @move_frequency * 2) * (6 - @move_frequency)
      # Branch by move type
      case @move_type
      when 1  # Random
        move_type_random
      when 2  # Approach
        move_type_toward_player
      when 3  # Custom
        move_type_custom
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (jump)
  #--------------------------------------------------------------------------
  def update_jump
    # Reduce jump count by 1
    @jump_count -= 1
    # Calculate new coordinates
    @real_x = (@real_x * @jump_count + @x * 128) / (@jump_count + 1)
    @real_y = (@real_y * @jump_count + @y * 128) / (@jump_count + 1)
  end
  #--------------------------------------------------------------------------
  # * Update frame (move)
  #--------------------------------------------------------------------------
  def update_move
    # Convert map coordinates from map move speed into move distance
    distance = 2 ** @move_speed
    # If logical coordinates are further down than real coordinates
    if @y * 128 > @real_y
      # Move down
      @real_y = [@real_y + distance, @y * 128].min
    end
    # If logical coordinates are more to the left than real coordinates
    if @x * 128 < @real_x
      # Move left
      @real_x = [@real_x - distance, @x * 128].max
    end
    # If logical coordinates are more to the right than real coordinates
    if @x * 128 > @real_x
      # Move right
      @real_x = [@real_x + distance, @x * 128].min
    end
    # If logical coordinates are further up than real coordinates
    if @y * 128 < @real_y
      # Move up
      @real_y = [@real_y - distance, @y * 128].max
    end
    # If move animation is ON
    if @walk_anime
      # Increase animation count by 1.5
      @anime_count += 1.5
    # If move animation is OFF, and stop animation is ON
    elsif @step_anime
      # Increase animation count by 1
      @anime_count += 1
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (stop)
  #--------------------------------------------------------------------------
  def update_stop
    # If stop animation is ON
    if @step_anime
      # Increase animation count by 1
      @anime_count += 1
    # If stop animation is OFF, but current pattern is different from original
    elsif @pattern != @original_pattern
      # Increase animation count by 1.5
      @anime_count += 1.5
    end
    # When waiting for event execution, or not locked
    # * If lock deals with event execution coming to a halt
    unless @starting or lock?
      # Increase stop count by 1
      @stop_count += 1
    end
  end
  #--------------------------------------------------------------------------
  # * Move Type : Random
  #--------------------------------------------------------------------------
  def move_type_random
    # Branch by random numbers 0-5
    case rand(6)
    when 0..3  # Random
      move_random
    when 4  # 1 step forward
      move_forward
    when 5  # Temporary stop
      @stop_count = 0
    end
  end
  #--------------------------------------------------------------------------
  # * Move Type : Approach
  #--------------------------------------------------------------------------
  def move_type_toward_player
    # Get difference in player coordinates
    sx = @x - $game_player.x
    sy = @y - $game_player.y
    # Get absolute value of difference
    abs_sx = sx > 0 ? sx : -sx
    abs_sy = sy > 0 ? sy : -sy
    # If separated by 20 or more tiles matching up horizontally and vertically
    if sx + sy >= 20
      # Random
      move_random
      return
    end
    # Branch by random numbers 0-5
    case rand(6)
    when 0..3  # Approach player
      move_toward_player
    when 4  # random
      move_random
    when 5  # 1 step forward
      move_forward
    end
  end
  #--------------------------------------------------------------------------
  # * Move Type : Custom
  #--------------------------------------------------------------------------
  def move_type_custom
    # Interrupt if not stopping
    if jumping? or moving?
      return
    end
    # Loop until finally arriving at move command list
    while @move_route_index < @move_route.list.size
      # Acquiring move command
      command = @move_route.list[@move_route_index]
      # If command code is 0 (last part of list)
      if command.code == 0
        # If [repeat action] option is ON
        if @move_route.repeat
          # First return to the move route index
          @move_route_index = 0
        end
        # If [repeat action] option is OFF
        unless @move_route.repeat
          # If move route is forcing
          if @move_route_forcing and not @move_route.repeat
            # Release forced move route
            @move_route_forcing = false
            # Restore original move route
            @move_route = @original_move_route
            @move_route_index = @original_move_route_index
            @original_move_route = nil
          end
          # Clear stop count
          @stop_count = 0
        end
        return
      end
      # During move command (from move down to jump)
      if command.code <= 14
        # Branch by command code
        case command.code
        when 1  # Move down
          move_down
        when 2  # Move left
          move_left
        when 3  # Move right
          move_right
        when 4  # Move up
          move_up
        when 5  # Move lower left
          move_lower_left
        when 6  # Move lower right
          move_lower_right
        when 7  # Move upper left
          move_upper_left
        when 8  # Move upper right
          move_upper_right
        when 9  # Move at random
          move_random
        when 10  # Move toward player
          move_toward_player
        when 11  # Move away from player
          move_away_from_player
        when 12  # 1 step forward
          move_forward
        when 13  # 1 step backward
          move_backward
        when 14  # Jump
          jump(command.parameters[0], command.parameters[1])
        end
        # If movement failure occurs when [Ignore if can't move] option is OFF
        if not @move_route.skippable and not moving? and not jumping?
          return
        end
        @move_route_index += 1
        return
      end
      # If waiting
      if command.code == 15
        # Set wait count
        @wait_count = command.parameters[0] * 2 - 1
        @move_route_index += 1
        return
      end
      # If direction change command
      if command.code >= 16 and command.code <= 26
        # Branch by command code
        case command.code
        when 16  # Turn down
          turn_down
        when 17  # Turn left
          turn_left
        when 18  # Turn right
          turn_right
        when 19  # Turn up
          turn_up
        when 20  # Turn 90° right
          turn_right_90
        when 21  # Turn 90° left
          turn_left_90
        when 22  # Turn 180°
          turn_180
        when 23  # Turn 90° right or left
          turn_right_or_left_90
        when 24  # Turn at Random
          turn_random
        when 25  # Turn toward player
          turn_toward_player
        when 26  # Turn away from player
          turn_away_from_player
        end
        @move_route_index += 1
        return
      end
      # If other command
      if command.code >= 27
        # Branch by command code
        case command.code
        when 27  # Switch ON
          $game_switches[command.parameters[0]] = true
          $game_map.need_refresh = true
        when 28  # Switch OFF
          $game_switches[command.parameters[0]] = false
          $game_map.need_refresh = true
        when 29  # Change speed
          @move_speed = command.parameters[0]
        when 30  # Change freq
          @move_frequency = command.parameters[0]
        when 31  # Move animation ON
          @walk_anime = true
        when 32  # Move animation OFF
          @walk_anime = false
        when 33  # Stop animation ON
          @step_anime = true
        when 34  # Stop animation OFF
          @step_anime = false
        when 35  # Direction fix ON
          @direction_fix = true
        when 36  # Direction fix OFF
          @direction_fix = false
        when 37  # Through ON
          @through = true
        when 38  # Through OFF
          @through = false
        when 39  # Always on top ON
          @always_on_top = true
        when 40  # Always on top OFF
          @always_on_top = false
        when 41  # Change Graphic
          @tile_id = 0
          @character_name = command.parameters[0]
          @character_hue = command.parameters[1]
          if @original_direction != command.parameters[2]
            @direction = command.parameters[2]
            @original_direction = @direction
            @prelock_direction = 0
          end
          if @original_pattern != command.parameters[3]
            @pattern = command.parameters[3]
            @original_pattern = @pattern
          end
        when 42  # Change Opacity
          @opacity = command.parameters[0]
        when 43  # Change Blending
          @blend_type = command.parameters[0]
        when 44  # Play SE
          $game_system.se_play(command.parameters[0])
        when 45  # Script
          begin
            eval(command.parameters[0])
          rescue
          end
        end
        @move_route_index += 1
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Increase Steps
  #--------------------------------------------------------------------------
  def increase_steps
    # Clear stop count
    @stop_count = 0
  end
  #--------------------------------------------------------------------------
  # * Move Down
  #     turn_enabled : a flag permits direction change on that spot
  #--------------------------------------------------------------------------
  def move_down(turn_enabled = true)
    # Turn down
    if turn_enabled
      turn_down
    end
    # If passable
    if passable?(@x, @y, 2)
      # Turn down
      turn_down
      # Update coordinates
      @y += 1
      # Increase steps
      increase_steps
    # If impassable
    else
      # Determine if touch event is triggered
      check_event_trigger_touch(@x, @y+1)
    end
  end
  #--------------------------------------------------------------------------
  # * Move Left
  #     turn_enabled : a flag permits direction change on that spot
  #--------------------------------------------------------------------------
  def move_left(turn_enabled = true)
    # Turn left
    if turn_enabled
      turn_left
    end
    # If passable
    if passable?(@x, @y, 4)
      # Turn left
      turn_left
      # Update coordinates
      @x -= 1
      # Increase steps
      increase_steps
    # If impassable
    else
      # Determine if touch event is triggered
      check_event_trigger_touch(@x-1, @y)
    end
  end
  #--------------------------------------------------------------------------
  # * Move Right
  #     turn_enabled : a flag permits direction change on that spot
  #--------------------------------------------------------------------------
  def move_right(turn_enabled = true)
    # Turn right
    if turn_enabled
      turn_right
    end
    # If passable
    if passable?(@x, @y, 6)
      # Turn right
      turn_right
      # Update coordinates
      @x += 1
      # Increase steps
      increase_steps
    # If impassable
    else
      # Determine if touch event is triggered
      check_event_trigger_touch(@x+1, @y)
    end
  end
  #--------------------------------------------------------------------------
  # * Move up
  #     turn_enabled : a flag permits direction change on that spot
  #--------------------------------------------------------------------------
  def move_up(turn_enabled = true)
    # Turn up
    if turn_enabled
      turn_up
    end
    # If passable
    if passable?(@x, @y, 8)
      # Turn up
      turn_up
      # Update coordinates
      @y -= 1
      # Increase steps
      increase_steps
    # If impassable
    else
      # Determine if touch event is triggered
      check_event_trigger_touch(@x, @y-1)
    end
  end
  #--------------------------------------------------------------------------
  # * Move Lower Left
  #--------------------------------------------------------------------------
  def move_lower_left
    # If no direction fix
    unless @direction_fix
      # Face down is facing right or up
      @direction = (@direction == 6 ? 4 : @direction == 8 ? 2 : @direction)
    end
    # When a down to left or a left to down course is passable
    if (passable?(@x, @y, 2) and passable?(@x, @y + 1, 4)) or
       (passable?(@x, @y, 4) and passable?(@x - 1, @y, 2))
      # Update coordinates
      @x -= 1
      @y += 1
      # Increase steps
      increase_steps
    end
  end
  #--------------------------------------------------------------------------
  # * Move Lower Right
  #--------------------------------------------------------------------------
  def move_lower_right
    # If no direction fix
    unless @direction_fix
      # Face right if facing left, and face down if facing up
      @direction = (@direction == 4 ? 6 : @direction == 8 ? 2 : @direction)
    end
    # When a down to right or a right to down course is passable
    if (passable?(@x, @y, 2) and passable?(@x, @y + 1, 6)) or
       (passable?(@x, @y, 6) and passable?(@x + 1, @y, 2))
      # Update coordinates
      @x += 1
      @y += 1
      # Increase steps
      increase_steps
    end
  end
  #--------------------------------------------------------------------------
  # * Move Upper Left
  #--------------------------------------------------------------------------
  def move_upper_left
    # If no direction fix
    unless @direction_fix
      # Face left if facing right, and face up if facing down
      @direction = (@direction == 6 ? 4 : @direction == 2 ? 8 : @direction)
    end
    # When an up to left or a left to up course is passable
    if (passable?(@x, @y, 8) and passable?(@x, @y - 1, 4)) or
       (passable?(@x, @y, 4) and passable?(@x - 1, @y, 8))
      # Update coordinates
      @x -= 1
      @y -= 1
      # Increase steps
      increase_steps
    end
  end
  #--------------------------------------------------------------------------
  # * Move Upper Right
  #--------------------------------------------------------------------------
  def move_upper_right
    # If no direction fix
    unless @direction_fix
      # Face right if facing left, and face up if facing down
      @direction = (@direction == 4 ? 6 : @direction == 2 ? 8 : @direction)
    end
    # When an up to right or a right to up course is passable
    if (passable?(@x, @y, 8) and passable?(@x, @y - 1, 6)) or
       (passable?(@x, @y, 6) and passable?(@x + 1, @y, 8))
      # Update coordinates
      @x += 1
      @y -= 1
      # Increase steps
      increase_steps
    end
  end
  #--------------------------------------------------------------------------
  # * Move at Random
  #--------------------------------------------------------------------------
  def move_random
    case rand(4)
    when 0  # Move down
      move_down(false)
    when 1  # Move left
      move_left(false)
    when 2  # Move right
      move_right(false)
    when 3  # Move up
      move_up(false)
    end
  end
  #--------------------------------------------------------------------------
  # * Move toward Player
  #--------------------------------------------------------------------------
  def move_toward_player
    # Get difference in player coordinates
    sx = @x - $game_player.x
    sy = @y - $game_player.y
    # If coordinates are equal
    if sx == 0 and sy == 0
      return
    end
    # Get absolute value of difference
    abs_sx = sx.abs
    abs_sy = sy.abs
    # If horizontal and vertical distances are equal
    if abs_sx == abs_sy
      # Increase one of them randomly by 1
      rand(2) == 0 ? abs_sx += 1 : abs_sy += 1
    end
    # If horizontal distance is longer
    if abs_sx > abs_sy
      # Move towards player, prioritize left and right directions
      sx > 0 ? move_left : move_right
      if not moving? and sy != 0
        sy > 0 ? move_up : move_down
      end
    # If vertical distance is longer
    else
      # Move towards player, prioritize up and down directions
      sy > 0 ? move_up : move_down
      if not moving? and sx != 0
        sx > 0 ? move_left : move_right
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Move away from Player
  #--------------------------------------------------------------------------
  def move_away_from_player
    # Get difference in player coordinates
    sx = @x - $game_player.x
    sy = @y - $game_player.y
    # If coordinates are equal
    if sx == 0 and sy == 0
      return
    end
    # Get absolute value of difference
    abs_sx = sx.abs
    abs_sy = sy.abs
    # If horizontal and vertical distances are equal
    if abs_sx == abs_sy
      # Increase one of them randomly by 1
      rand(2) == 0 ? abs_sx += 1 : abs_sy += 1
    end
    # If horizontal distance is longer
    if abs_sx > abs_sy
      # Move away from player, prioritize left and right directions
      sx > 0 ? move_right : move_left
      if not moving? and sy != 0
        sy > 0 ? move_down : move_up
      end
    # If vertical distance is longer
    else
      # Move away from player, prioritize up and down directions
      sy > 0 ? move_down : move_up
      if not moving? and sx != 0
        sx > 0 ? move_right : move_left
      end
    end
  end
  #--------------------------------------------------------------------------
  # * 1 Step Forward
  #--------------------------------------------------------------------------
  def move_forward
    case @direction
    when 2
      move_down(false)
    when 4
      move_left(false)
    when 6
      move_right(false)
    when 8
      move_up(false)
    end
  end
  #--------------------------------------------------------------------------
  # * 1 Step Backward
  #--------------------------------------------------------------------------
  def move_backward
    # Remember direction fix situation
    last_direction_fix = @direction_fix
    # Force directino fix
    @direction_fix = true
    # Branch by direction
    case @direction
    when 2  # Down
      move_up(false)
    when 4  # Left
      move_right(false)
    when 6  # Right
      move_left(false)
    when 8  # Up
      move_down(false)
    end
    # Return direction fix situation back to normal
    @direction_fix = last_direction_fix
  end
  #--------------------------------------------------------------------------
  # * Jump
  #     x_plus : x-coordinate plus value
  #     y_plus : y-coordinate plus value
  #--------------------------------------------------------------------------
  def jump(x_plus, y_plus)
    # If plus value is not (0,0)
    if x_plus != 0 or y_plus != 0
      # If horizontal distnace is longer
      if x_plus.abs > y_plus.abs
        # Change direction to left or right
        x_plus < 0 ? turn_left : turn_right
      # If vertical distance is longer, or equal
      else
        # Change direction to up or down
        y_plus < 0 ? turn_up : turn_down
      end
    end
    # Calculate new coordinates
    new_x = @x + x_plus
    new_y = @y + y_plus
    # If plus value is (0,0) or jump destination is passable
    if (x_plus == 0 and y_plus == 0) or passable?(new_x, new_y, 0)
      # Straighten position
      straighten
      # Update coordinates
      @x = new_x
      @y = new_y
      # Calculate distance
      distance = Math.sqrt(x_plus * x_plus + y_plus * y_plus).round
      # Set jump count
      @jump_peak = 10 + distance - @move_speed
      @jump_count = @jump_peak * 2
      # Clear stop count
      @stop_count = 0
    end
  end
  #--------------------------------------------------------------------------
  # * Turn Down
  #--------------------------------------------------------------------------
  def turn_down
    unless @direction_fix
      @direction = 2
      @stop_count = 0
    end
  end
  #--------------------------------------------------------------------------
  # * Turn Left
  #--------------------------------------------------------------------------
  def turn_left
    unless @direction_fix
      @direction = 4
      @stop_count = 0
    end
  end
  #--------------------------------------------------------------------------
  # * Turn Right
  #--------------------------------------------------------------------------
  def turn_right
    unless @direction_fix
      @direction = 6
      @stop_count = 0
    end
  end
  #--------------------------------------------------------------------------
  # * Turn Up
  #--------------------------------------------------------------------------
  def turn_up
    unless @direction_fix
      @direction = 8
      @stop_count = 0
    end
  end
  #--------------------------------------------------------------------------
  # * Turn 90° Right
  #--------------------------------------------------------------------------
  def turn_right_90
    case @direction
    when 2
      turn_left
    when 4
      turn_up
    when 6
      turn_down
    when 8
      turn_right
    end
  end
  #--------------------------------------------------------------------------
  # * Turn 90° Left
  #--------------------------------------------------------------------------
  def turn_left_90
    case @direction
    when 2
      turn_right
    when 4
      turn_down
    when 6
      turn_up
    when 8
      turn_left
    end
  end
  #--------------------------------------------------------------------------
  # * Turn 180°
  #--------------------------------------------------------------------------
  def turn_180
    case @direction
    when 2
      turn_up
    when 4
      turn_right
    when 6
      turn_left
    when 8
      turn_down
    end
  end
  #--------------------------------------------------------------------------
  # * Turn 90° Right or Left
  #--------------------------------------------------------------------------
  def turn_right_or_left_90
    if rand(2) == 0
      turn_right_90
    else
      turn_left_90
    end
  end
  #--------------------------------------------------------------------------
  # * Turn at Random
  #--------------------------------------------------------------------------
  def turn_random
    case rand(4)
    when 0
      turn_up
    when 1
      turn_right
    when 2
      turn_left
    when 3
      turn_down
    end
  end
  #--------------------------------------------------------------------------
  # * Turn Towards Player
  #--------------------------------------------------------------------------
  def turn_toward_player
    # Get difference in player coordinates
    sx = @x - $game_player.x
    sy = @y - $game_player.y
    # If coordinates are equal
    if sx == 0 and sy == 0
      return
    end
    # If horizontal distance is longer
    if sx.abs > sy.abs
      # Turn to the right or left towards player
      sx > 0 ? turn_left : turn_right
    # If vertical distance is longer
    else
      # Turn up or down towards player
      sy > 0 ? turn_up : turn_down
    end
  end
  #--------------------------------------------------------------------------
  # * Turn Away from Player
  #--------------------------------------------------------------------------
  def turn_away_from_player
    # Get difference in player coordinates
    sx = @x - $game_player.x
    sy = @y - $game_player.y
    # If coordinates are equal
    if sx == 0 and sy == 0
      return
    end
    # If horizontal distance is longer
    if sx.abs > sy.abs
      # Turn to the right or left away from player
      sx > 0 ? turn_right : turn_left
    # If vertical distance is longer
    else
      # Turn up or down away from player
      sy > 0 ? turn_down : turn_up
    end
  end
end
#==============================================================================
# ** Game_Event
#------------------------------------------------------------------------------
#  This class deals with events. It handles functions including event page 
#  switching via condition determinants, and running parallel process events.
#  It's used within the Game_Map class.
#==============================================================================

class Game_Event < Game_Character
  #--------------------------------------------------------------------------
  # * Public Instance Variables
  #--------------------------------------------------------------------------
  attr_reader   :trigger                  # trigger
  attr_reader   :list                     # list of event commands
  attr_reader   :starting                 # starting flag
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     map_id : map ID
  #     event  : event (RPG::Event)
  #--------------------------------------------------------------------------
  def initialize(map_id, event)
    super()
    @map_id = map_id
    @event = event
    @id = @event.id
    @erased = false
    @starting = false
    @through = true
    # Move to starting position
    moveto(@event.x, @event.y)
    refresh
  end
  #--------------------------------------------------------------------------
  # * Clear Starting Flag
  #--------------------------------------------------------------------------
  def clear_starting
    @starting = false
  end
  #--------------------------------------------------------------------------
  # * Determine if Over Trigger
  #    (whether or not same position is starting condition)
  #--------------------------------------------------------------------------
  def over_trigger?
    # If not through situation with character as graphic
    if @character_name != "" and not @through
      # Starting determinant is face
      return false
    end
    # If this position on the map is impassable
    unless $game_map.passable?(@x, @y, 0)
      # Starting determinant is face
      return false
    end
    # Starting determinant is same position
    return true
  end
  #--------------------------------------------------------------------------
  # * Start Event
  #--------------------------------------------------------------------------
  def start
    # If list of event commands is not empty
    if @list.size > 1
      @starting = true
    end
  end
  #--------------------------------------------------------------------------
  # * Temporarily Erase
  #--------------------------------------------------------------------------
  def erase
    @erased = true
    refresh
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    # Initialize local variable: new_page
    new_page = nil
    # If not temporarily erased
    unless @erased
      # Check in order of large event pages
      for page in @event.pages.reverse
        # Make possible referrence for event condition with c
        c = page.condition
        # Switch 1 condition confirmation
        if c.switch1_valid
          if $game_switches[c.switch1_id] == false
            next
          end
        end
        # Switch 2 condition confirmation
        if c.switch2_valid
          if $game_switches[c.switch2_id] == false
            next
          end
        end
        # Variable condition confirmation
        if c.variable_valid
          if $game_variables[c.variable_id] < c.variable_value
            next
          end
        end
        # Self switch condition confirmation
        if c.self_switch_valid
          key = [@map_id, @event.id, c.self_switch_ch]
          if $game_self_switches[key] != true
            next
          end
        end
        # Set local variable: new_page
        new_page = page
        # Remove loop
        break
      end
    end
    # If event page is the same as last time
    if new_page == @page
      # End method
      return
    end
    # Set @page as current event page
    @page = new_page
    # Clear starting flag
    clear_starting
    # If no page fulfills conditions
    if @page == nil
      # Set each instance variable
      @tile_id = 0
      @character_name = ""
      @character_hue = 0
      @move_type = 0
      @through = true
      @trigger = nil
      @list = nil
      @interpreter = nil
      # End method
      return
    end
    # Set each instance variable
    @tile_id = @page.graphic.tile_id
    @character_name = @page.graphic.character_name
    @character_hue = @page.graphic.character_hue
    if @original_direction != @page.graphic.direction
      @direction = @page.graphic.direction
      @original_direction = @direction
      @prelock_direction = 0
    end
    if @original_pattern != @page.graphic.pattern
      @pattern = @page.graphic.pattern
      @original_pattern = @pattern
    end
    @opacity = @page.graphic.opacity
    @blend_type = @page.graphic.blend_type
    @move_type = @page.move_type
    @move_speed = @page.move_speed
    @move_frequency = @page.move_frequency
    @move_route = @page.move_route
    @move_route_index = 0
    @move_route_forcing = false
    @walk_anime = @page.walk_anime
    @step_anime = @page.step_anime
    @direction_fix = @page.direction_fix
    @through = @page.through
    @always_on_top = @page.always_on_top
    @trigger = @page.trigger
    @list = @page.list
    @interpreter = nil
    # If trigger is [parallel process]
    if @trigger == 4
      # Create parallel process interpreter
      @interpreter = Interpreter.new
    end
    # Auto event start determinant
    check_event_trigger_auto
  end
  #--------------------------------------------------------------------------
  # * Touch Event Starting Determinant
  #--------------------------------------------------------------------------
  def check_event_trigger_touch(x, y)
    # If event is running
    if $game_system.map_interpreter.running?
      return
    end
    # If trigger is [touch from event] and consistent with player coordinates
    if @trigger == 2 and x == $game_player.x and y == $game_player.y
      # If starting determinant other than jumping is front event
      if not jumping? and not over_trigger?
        start
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Automatic Event Starting Determinant
  #--------------------------------------------------------------------------
  def check_event_trigger_auto
    # If trigger is [touch from event] and consistent with player coordinates
    if @trigger == 2 and @x == $game_player.x and @y == $game_player.y
      # If starting determinant other than jumping is same position event
      if not jumping? and over_trigger?
        start
      end
    end
    # If trigger is [auto run]
    if @trigger == 3
      start
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    super
    # Automatic event starting determinant
    check_event_trigger_auto
    # If parallel process is valid
    if @interpreter != nil
      # If not running
      unless @interpreter.running?
        # Set up event
        @interpreter.setup(@list, @event.id)
      end
      # Update interpreter
      @interpreter.update
    end
  end
end
#==============================================================================
# ** Game_Player
#------------------------------------------------------------------------------
#  This class handles the player. Its functions include event starting
#  determinants and map scrolling. Refer to "$game_player" for the one
#  instance of this class.
#==============================================================================

class Game_Player < Game_Character
  #--------------------------------------------------------------------------
  # * Invariables
  #--------------------------------------------------------------------------
  CENTER_X = (320 - 16) * 4   # Center screen x-coordinate * 4
  CENTER_Y = (240 - 16) * 4   # Center screen y-coordinate * 4
  #--------------------------------------------------------------------------
  # * Passable Determinants
  #     x : x-coordinate
  #     y : y-coordinate
  #     d : direction (0,2,4,6,8)
  #         * 0 = Determines if all directions are impassable (for jumping)
  #--------------------------------------------------------------------------
  def passable?(x, y, d)
    # Get new coordinates
    new_x = x + (d == 6 ? 1 : d == 4 ? -1 : 0)
    new_y = y + (d == 2 ? 1 : d == 8 ? -1 : 0)
    # If coordinates are outside of map
    unless $game_map.valid?(new_x, new_y)
      # Impassable
      return false
    end
    # If debug mode is ON and ctrl key was pressed
    if $DEBUG and Input.press?(Input::CTRL)
      # Passable
      return true
    end
    super
  end
  #--------------------------------------------------------------------------
  # * Set Map Display Position to Center of Screen
  #--------------------------------------------------------------------------
  def center(x, y)
    max_x = ($game_map.width - 20) * 128
    max_y = ($game_map.height - 15) * 128
    $game_map.display_x = [0, [x * 128 - CENTER_X, max_x].min].max
    $game_map.display_y = [0, [y * 128 - CENTER_Y, max_y].min].max
  end
  #--------------------------------------------------------------------------
  # * Move to Designated Position
  #     x : x-coordinate
  #     y : y-coordinate
  #--------------------------------------------------------------------------
  def moveto(x, y)
    super
    # Centering
    center(x, y)
    # Make encounter count
    make_encounter_count
  end
  #--------------------------------------------------------------------------
  # * Increaase Steps
  #--------------------------------------------------------------------------
  def increase_steps
    super
    # If move route is not forcing
    unless @move_route_forcing
      # Increase steps
      $game_party.increase_steps
      # Number of steps are an even number
      if $game_party.steps % 2 == 0
        # Slip damage check
        $game_party.check_map_slip_damage
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Get Encounter Count
  #--------------------------------------------------------------------------
  def encounter_count
    return @encounter_count
  end
  #--------------------------------------------------------------------------
  # * Make Encounter Count
  #--------------------------------------------------------------------------
  def make_encounter_count
    # Image of two dice rolling
    if $game_map.map_id != 0
      n = $game_map.encounter_step
      @encounter_count = rand(n) + rand(n) + 1
    end
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    # If party members = 0
    if $game_party.actors.size == 0
      # Clear character file name and hue
      @character_name = ""
      @character_hue = 0
      # End method
      return
    end
    # Get lead actor
    actor = $game_party.actors[0]
    # Set character file name and hue
    @character_name = actor.character_name
    @character_hue = actor.character_hue
    # Initialize opacity level and blending method
    @opacity = 255
    @blend_type = 0
  end
  #--------------------------------------------------------------------------
  # * Same Position Starting Determinant
  #--------------------------------------------------------------------------
  def check_event_trigger_here(triggers)
    result = false
    # If event is running
    if $game_system.map_interpreter.running?
      return result
    end
    # All event loops
    for event in $game_map.events.values
      # If event coordinates and triggers are consistent
      if event.x == @x and event.y == @y and triggers.include?(event.trigger)
        # If starting determinant is same position event (other than jumping)
        if not event.jumping? and event.over_trigger?
          event.start
          result = true
        end
      end
    end
    return result
  end
  #--------------------------------------------------------------------------
  # * Front Envent Starting Determinant
  #--------------------------------------------------------------------------
  def check_event_trigger_there(triggers)
    result = false
    # If event is running
    if $game_system.map_interpreter.running?
      return result
    end
    # Calculate front event coordinates
    new_x = @x + (@direction == 6 ? 1 : @direction == 4 ? -1 : 0)
    new_y = @y + (@direction == 2 ? 1 : @direction == 8 ? -1 : 0)
    # All event loops
    for event in $game_map.events.values
      # If event coordinates and triggers are consistent
      if event.x == new_x and event.y == new_y and
         triggers.include?(event.trigger)
        # If starting determinant is front event (other than jumping)
        if not event.jumping? and not event.over_trigger?
          event.start
          result = true
        end
      end
    end
    # If fitting event is not found
    if result == false
      # If front tile is a counter
      if $game_map.counter?(new_x, new_y)
        # Calculate 1 tile inside coordinates
        new_x += (@direction == 6 ? 1 : @direction == 4 ? -1 : 0)
        new_y += (@direction == 2 ? 1 : @direction == 8 ? -1 : 0)
        # All event loops
        for event in $game_map.events.values
          # If event coordinates and triggers are consistent
          if event.x == new_x and event.y == new_y and
             triggers.include?(event.trigger)
            # If starting determinant is front event (other than jumping)
            if not event.jumping? and not event.over_trigger?
              event.start
              result = true
            end
          end
        end
      end
    end
    return result
  end
  #--------------------------------------------------------------------------
  # * Touch Event Starting Determinant
  #--------------------------------------------------------------------------
  def check_event_trigger_touch(x, y)
    result = false
    # If event is running
    if $game_system.map_interpreter.running?
      return result
    end
    # All event loops
    for event in $game_map.events.values
      # If event coordinates and triggers are consistent
      if event.x == x and event.y == y and [1,2].include?(event.trigger)
        # If starting determinant is front event (other than jumping)
        if not event.jumping? and not event.over_trigger?
          event.start
          result = true
        end
      end
    end
    return result
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # Remember whether or not moving in local variables
    last_moving = moving?
    # If moving, event running, move route forcing, and message window
    # display are all not occurring
    unless moving? or $game_system.map_interpreter.running? or
           @move_route_forcing or $game_temp.message_window_showing
      # Move player in the direction the directional button is being pressed
      case Input.dir4
      when 2
        move_down
      when 4
        move_left
      when 6
        move_right
      when 8
        move_up
      end
    end
    # Remember coordinates in local variables
    last_real_x = @real_x
    last_real_y = @real_y
    super
    # If character moves down and is positioned lower than the center
    # of the screen
    if @real_y > last_real_y and @real_y - $game_map.display_y > CENTER_Y
      # Scroll map down
      $game_map.scroll_down(@real_y - last_real_y)
    end
    # If character moves left and is positioned more let on-screen than
    # center
    if @real_x < last_real_x and @real_x - $game_map.display_x < CENTER_X
      # Scroll map left
      $game_map.scroll_left(last_real_x - @real_x)
    end
    # If character moves right and is positioned more right on-screen than
    # center
    if @real_x > last_real_x and @real_x - $game_map.display_x > CENTER_X
      # Scroll map right
      $game_map.scroll_right(@real_x - last_real_x)
    end
    # If character moves up and is positioned higher than the center
    # of the screen
    if @real_y < last_real_y and @real_y - $game_map.display_y < CENTER_Y
      # Scroll map up
      $game_map.scroll_up(last_real_y - @real_y)
    end
    # If not moving
    unless moving?
      # If player was moving last time
      if last_moving
        # Event determinant is via touch of same position event
        result = check_event_trigger_here([1,2])
        # If event which started does not exist
        if result == false
          # Disregard if debug mode is ON and ctrl key was pressed
          unless $DEBUG and Input.press?(Input::CTRL)
            # Encounter countdown
            if @encounter_count > 0
              @encounter_count -= 1
            end
          end
        end
      end
      # If C button was pressed
      if Input.trigger?(Input::C)
        # Same position and front event determinant
        check_event_trigger_here([0])
        check_event_trigger_there([0,1,2])
      end
    end
  end
end
#==============================================================================
# ** Sprite_Character
#------------------------------------------------------------------------------
#  This sprite is used to display the character.It observes the Game_Character
#  class and automatically changes sprite conditions.
#==============================================================================

class Sprite_Character < RPG::Sprite
  #--------------------------------------------------------------------------
  # * Public Instance Variables
  #--------------------------------------------------------------------------
  attr_accessor :character                # character
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     viewport  : viewport
  #     character : character (Game_Character)
  #--------------------------------------------------------------------------
  def initialize(viewport, character = nil)
    super(viewport)
    @character = character
    update
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    super
    # If tile ID, file name, or hue are different from current ones
    if @tile_id != @character.tile_id or
       @character_name != @character.character_name or
       @character_hue != @character.character_hue
      # Remember tile ID, file name, and hue
      @tile_id = @character.tile_id
      @character_name = @character.character_name
      @character_hue = @character.character_hue
      # If tile ID value is valid
      if @tile_id >= 384
        self.bitmap = RPG::Cache.tile($game_map.tileset_name,
          @tile_id, @character.character_hue)
        self.src_rect.set(0, 0, 32, 32)
        self.ox = 16
        self.oy = 32
      # If tile ID value is invalid
      else
        self.bitmap = RPG::Cache.character(@character.character_name,
          @character.character_hue)
        @cw = bitmap.width / 4
        @ch = bitmap.height / 4
        self.ox = @cw / 2
        self.oy = @ch
      end
    end
    # Set visible situation
    self.visible = (not @character.transparent)
    # If graphic is character
    if @tile_id == 0
      # Set rectangular transfer
      sx = @character.pattern * @cw
      sy = (@character.direction - 2) / 2 * @ch
      self.src_rect.set(sx, sy, @cw, @ch)
    end
    # Set sprite coordinates
    self.x = @character.screen_x
    self.y = @character.screen_y
    self.z = @character.screen_z(@ch)
    # Set opacity level, blend method, and bush depth
    self.opacity = @character.opacity
    self.blend_type = @character.blend_type
    self.bush_depth = @character.bush_depth
    # Animation
    if @character.animation_id != 0
      animation = $data_animations[@character.animation_id]
      animation(animation, true)
      @character.animation_id = 0
    end
  end
end
#==============================================================================
# ** Sprite_Battler
#------------------------------------------------------------------------------
#  This sprite is used to display the battler.It observes the Game_Character
#  class and automatically changes sprite conditions.
#==============================================================================

class Sprite_Battler < RPG::Sprite
  #--------------------------------------------------------------------------
  # * Public Instance Variables
  #--------------------------------------------------------------------------
  attr_accessor :battler                  # battler
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     viewport : viewport
  #     battler  : battler (Game_Battler)
  #--------------------------------------------------------------------------
  def initialize(viewport, battler = nil)
    super(viewport)
    @battler = battler
    @battler_visible = false
  end
  #--------------------------------------------------------------------------
  # * Dispose
  #--------------------------------------------------------------------------
  def dispose
    if self.bitmap != nil
      self.bitmap.dispose
    end
    super
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    super
    # If battler is nil
    if @battler == nil
      self.bitmap = nil
      loop_animation(nil)
      return
    end
    # If file name or hue are different than current ones
    if @battler.battler_name != @battler_name or
       @battler.battler_hue != @battler_hue
      # Get and set bitmap
      @battler_name = @battler.battler_name
      @battler_hue = @battler.battler_hue
      self.bitmap = RPG::Cache.battler(@battler_name, @battler_hue)
      @width = bitmap.width
      @height = bitmap.height
      self.ox = @width / 2
      self.oy = @height
      # Change opacity level to 0 when dead or hidden
      if @battler.dead? or @battler.hidden
        self.opacity = 0
      end
    end
    # If animation ID is different than current one
    if @battler.damage == nil and
       @battler.state_animation_id != @state_animation_id
      @state_animation_id = @battler.state_animation_id
      loop_animation($data_animations[@state_animation_id])
    end
    # If actor which should be displayed
    if @battler.is_a?(Game_Actor) and @battler_visible
      # Bring opacity level down a bit when not in main phase
      if $game_temp.battle_main_phase
        self.opacity += 3 if self.opacity < 255
      else
        self.opacity -= 3 if self.opacity > 207
      end
    end
    # Blink
    if @battler.blink
      blink_on
    else
      blink_off
    end
    # If invisible
    unless @battler_visible
      # Appear
      if not @battler.hidden and not @battler.dead? and
         (@battler.damage == nil or @battler.damage_pop)
        appear
        @battler_visible = true
      end
    end
    # If visible
    if @battler_visible
      # Escape
      if @battler.hidden
        $game_system.se_play($data_system.escape_se)
        escape
        @battler_visible = false
      end
      # White flash
      if @battler.white_flash
        whiten
        @battler.white_flash = false
      end
      # Animation
      if @battler.animation_id != 0
        animation = $data_animations[@battler.animation_id]
        animation(animation, @battler.animation_hit)
        @battler.animation_id = 0
      end
      # Damage
      if @battler.damage_pop
        damage(@battler.damage, @battler.critical)
        @battler.damage = nil
        @battler.critical = false
        @battler.damage_pop = false
      end
      # Collapse
      if @battler.damage == nil and @battler.dead?
        if @battler.is_a?(Game_Enemy)
          $game_system.se_play($data_system.enemy_collapse_se)
        else
          $game_system.se_play($data_system.actor_collapse_se)
        end
        collapse
        @battler_visible = false
      end
    end
    # Set sprite coordinates
    self.x = @battler.screen_x
    self.y = @battler.screen_y
    self.z = @battler.screen_z
  end
end
#==============================================================================
# ** Sprite_Picture
#------------------------------------------------------------------------------
#  This sprite is used to display the picture.It observes the Game_Character
#  class and automatically changes sprite conditions.
#==============================================================================

class Sprite_Picture < Sprite
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     viewport : viewport
  #     picture  : picture (Game_Picture)
  #--------------------------------------------------------------------------
  def initialize(viewport, picture)
    super(viewport)
    @picture = picture
    update
  end
  #--------------------------------------------------------------------------
  # * Dispose
  #--------------------------------------------------------------------------
  def dispose
    if self.bitmap != nil
      self.bitmap.dispose
    end
    super
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    super
    # If picture file name is different from current one
    if @picture_name != @picture.name
      # Remember file name to instance variables
      @picture_name = @picture.name
      # If file name is not empty
      if @picture_name != ""
        # Get picture graphic
        self.bitmap = RPG::Cache.picture(@picture_name)
      end
    end
    # If file name is empty
    if @picture_name == ""
      # Set sprite to invisible
      self.visible = false
      return
    end
    # Set sprite to visible
    self.visible = true
    # Set transfer starting point
    if @picture.origin == 0
      self.ox = 0
      self.oy = 0
    else
      self.ox = self.bitmap.width / 2
      self.oy = self.bitmap.height / 2
    end
    # Set sprite coordinates
    self.x = @picture.x
    self.y = @picture.y
    self.z = @picture.number
    # Set zoom rate, opacity level, and blend method
    self.zoom_x = @picture.zoom_x / 100.0
    self.zoom_y = @picture.zoom_y / 100.0
    self.opacity = @picture.opacity
    self.blend_type = @picture.blend_type
    # Set rotation angle and color tone
    self.angle = @picture.angle
    self.tone = @picture.tone
  end
end
#==============================================================================
# ** Sprite_Timer
#------------------------------------------------------------------------------
#  This sprite is used to display the timer.It observes the $game_system
#  class and automatically changes sprite conditions.
#==============================================================================

class Sprite_Timer < Sprite
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    super
    self.bitmap = Bitmap.new(88, 48)
    self.bitmap.font.name = "Arial"
    self.bitmap.font.size = 32
    self.x = 640 - self.bitmap.width
    self.y = 0
    self.z = 500
    update
  end
  #--------------------------------------------------------------------------
  # * Dispose
  #--------------------------------------------------------------------------
  def dispose
    if self.bitmap != nil
      self.bitmap.dispose
    end
    super
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    super
    # Set timer to visible if working
    self.visible = $game_system.timer_working
    # If timer needs to be redrawn
    if $game_system.timer / Graphics.frame_rate != @total_sec
      # Clear window contents
      self.bitmap.clear
      # Calculate total number of seconds
      @total_sec = $game_system.timer / Graphics.frame_rate
      # Make a string for displaying the timer
      min = @total_sec / 60
      sec = @total_sec % 60
      text = sprintf("%02d:%02d", min, sec)
      # Draw timer
      self.bitmap.font.color.set(255, 255, 255)
      self.bitmap.draw_text(self.bitmap.rect, text, 1)
    end
  end
end
#==============================================================================
# ** Spriteset_Map
#------------------------------------------------------------------------------
#  This class brings together map screen sprites, tilemaps, etc.
#  It's used within the Scene_Map class.
#==============================================================================

class Spriteset_Map
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    # Make viewports
    @viewport1 = Viewport.new(0, 0, 640, 480)
    @viewport2 = Viewport.new(0, 0, 640, 480)
    @viewport3 = Viewport.new(0, 0, 640, 480)
    @viewport2.z = 200
    @viewport3.z = 5000
    # Make tilemap
    @tilemap = Tilemap.new(@viewport1)
    @tilemap.tileset = RPG::Cache.tileset($game_map.tileset_name)
    for i in 0..6
      autotile_name = $game_map.autotile_names[i]
      @tilemap.autotiles[i] = RPG::Cache.autotile(autotile_name)
    end
    @tilemap.map_data = $game_map.data
    @tilemap.priorities = $game_map.priorities
    # Make panorama plane
    @panorama = Plane.new(@viewport1)
    @panorama.z = -1000
    # Make fog plane
    @fog = Plane.new(@viewport1)
    @fog.z = 3000
    # Make character sprites
    @character_sprites = []
    for i in $game_map.events.keys.sort
      sprite = Sprite_Character.new(@viewport1, $game_map.events[i])
      @character_sprites.push(sprite)
    end
    @character_sprites.push(Sprite_Character.new(@viewport1, $game_player))
    # Make weather
    @weather = RPG::Weather.new(@viewport1)
    # Make picture sprites
    @picture_sprites = []
    for i in 1..50
      @picture_sprites.push(Sprite_Picture.new(@viewport2,
        $game_screen.pictures[i]))
    end
    # Make timer sprite
    @timer_sprite = Sprite_Timer.new
    # Frame update
    update
  end
  #--------------------------------------------------------------------------
  # * Dispose
  #--------------------------------------------------------------------------
  def dispose
    # Dispose of tilemap
    @tilemap.tileset.dispose
    for i in 0..6
      @tilemap.autotiles[i].dispose
    end
    @tilemap.dispose
    # Dispose of panorama plane
    @panorama.dispose
    # Dispose of fog plane
    @fog.dispose
    # Dispose of character sprites
    for sprite in @character_sprites
      sprite.dispose
    end
    # Dispose of weather
    @weather.dispose
    # Dispose of picture sprites
    for sprite in @picture_sprites
      sprite.dispose
    end
    # Dispose of timer sprite
    @timer_sprite.dispose
    # Dispose of viewports
    @viewport1.dispose
    @viewport2.dispose
    @viewport3.dispose
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # If panorama is different from current one
    if @panorama_name != $game_map.panorama_name or
       @panorama_hue != $game_map.panorama_hue
      @panorama_name = $game_map.panorama_name
      @panorama_hue = $game_map.panorama_hue
      if @panorama.bitmap != nil
        @panorama.bitmap.dispose
        @panorama.bitmap = nil
      end
      if @panorama_name != ""
        @panorama.bitmap = RPG::Cache.panorama(@panorama_name, @panorama_hue)
      end
      Graphics.frame_reset
    end
    # If fog is different than current fog
    if @fog_name != $game_map.fog_name or @fog_hue != $game_map.fog_hue
      @fog_name = $game_map.fog_name
      @fog_hue = $game_map.fog_hue
      if @fog.bitmap != nil
        @fog.bitmap.dispose
        @fog.bitmap = nil
      end
      if @fog_name != ""
        @fog.bitmap = RPG::Cache.fog(@fog_name, @fog_hue)
      end
      Graphics.frame_reset
    end
    # Update tilemap
    @tilemap.ox = $game_map.display_x / 4
    @tilemap.oy = $game_map.display_y / 4
    @tilemap.update
    # Update panorama plane
    @panorama.ox = $game_map.display_x / 8
    @panorama.oy = $game_map.display_y / 8
    # Update fog plane
    @fog.zoom_x = $game_map.fog_zoom / 100.0
    @fog.zoom_y = $game_map.fog_zoom / 100.0
    @fog.opacity = $game_map.fog_opacity
    @fog.blend_type = $game_map.fog_blend_type
    @fog.ox = $game_map.display_x / 4 + $game_map.fog_ox
    @fog.oy = $game_map.display_y / 4 + $game_map.fog_oy
    @fog.tone = $game_map.fog_tone
    # Update character sprites
    for sprite in @character_sprites
      sprite.update
    end
    # Update weather graphic
    @weather.type = $game_screen.weather_type
    @weather.max = $game_screen.weather_max
    @weather.ox = $game_map.display_x / 4
    @weather.oy = $game_map.display_y / 4
    @weather.update
    # Update picture sprites
    for sprite in @picture_sprites
      sprite.update
    end
    # Update timer sprite
    @timer_sprite.update
    # Set screen color tone and shake position
    @viewport1.tone = $game_screen.tone
    @viewport1.ox = $game_screen.shake
    # Set screen flash color
    @viewport3.color = $game_screen.flash_color
    # Update viewports
    @viewport1.update
    @viewport3.update
  end
end
#==============================================================================
# ** Spriteset_Battle
#------------------------------------------------------------------------------
#  This class brings together battle screen sprites. It's used within
#  the Scene_Battle class.
#==============================================================================

class Spriteset_Battle
  #--------------------------------------------------------------------------
  # * Public Instance Variables
  #--------------------------------------------------------------------------
  attr_reader   :viewport1                # enemy viewport
  attr_reader   :viewport2                # actor viewport
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    # Make viewports
    @viewport1 = Viewport.new(0, 0, 640, 320)
    @viewport2 = Viewport.new(0, 0, 640, 480)
    @viewport3 = Viewport.new(0, 0, 640, 480)
    @viewport4 = Viewport.new(0, 0, 640, 480)
    @viewport2.z = 101
    @viewport3.z = 200
    @viewport4.z = 5000
    # Make battleback sprite
    @battleback_sprite = Sprite.new(@viewport1)
    # Make enemy sprites
    @enemy_sprites = []
    for enemy in $game_troop.enemies.reverse
      @enemy_sprites.push(Sprite_Battler.new(@viewport1, enemy))
    end
    # Make actor sprites
    @actor_sprites = []
    @actor_sprites.push(Sprite_Battler.new(@viewport2))
    @actor_sprites.push(Sprite_Battler.new(@viewport2))
    @actor_sprites.push(Sprite_Battler.new(@viewport2))
    @actor_sprites.push(Sprite_Battler.new(@viewport2))
    # Make weather
    @weather = RPG::Weather.new(@viewport1)
    # Make picture sprites
    @picture_sprites = []
    for i in 51..100
      @picture_sprites.push(Sprite_Picture.new(@viewport3,
        $game_screen.pictures[i]))
    end
    # Make timer sprite
    @timer_sprite = Sprite_Timer.new
    # Frame update
    update
  end
  #--------------------------------------------------------------------------
  # * Dispose
  #--------------------------------------------------------------------------
  def dispose
    # If battleback bit map exists, dispose of it
    if @battleback_sprite.bitmap != nil
      @battleback_sprite.bitmap.dispose
    end
    # Dispose of battleback sprite
    @battleback_sprite.dispose
    # Dispose of enemy sprites and actor sprites
    for sprite in @enemy_sprites + @actor_sprites
      sprite.dispose
    end
    # Dispose of weather
    @weather.dispose
    # Dispose of picture sprites
    for sprite in @picture_sprites
      sprite.dispose
    end
    # Dispose of timer sprite
    @timer_sprite.dispose
    # Dispose of viewports
    @viewport1.dispose
    @viewport2.dispose
    @viewport3.dispose
    @viewport4.dispose
  end
  #--------------------------------------------------------------------------
  # * Determine if Effects are Displayed
  #--------------------------------------------------------------------------
  def effect?
    # Return true if even 1 effect is being displayed
    for sprite in @enemy_sprites + @actor_sprites
      return true if sprite.effect?
    end
    return false
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # Update actor sprite contents (corresponds with actor switching)
    @actor_sprites[0].battler = $game_party.actors[0]
    @actor_sprites[1].battler = $game_party.actors[1]
    @actor_sprites[2].battler = $game_party.actors[2]
    @actor_sprites[3].battler = $game_party.actors[3]
    # If battleback file name is different from current one
    if @battleback_name != $game_temp.battleback_name
      @battleback_name = $game_temp.battleback_name
      if @battleback_sprite.bitmap != nil
        @battleback_sprite.bitmap.dispose
      end
      @battleback_sprite.bitmap = RPG::Cache.battleback(@battleback_name)
      @battleback_sprite.src_rect.set(0, 0, 640, 320)
    end
    # Update battler sprites
    for sprite in @enemy_sprites + @actor_sprites
      sprite.update
    end
    # Update weather graphic
    @weather.type = $game_screen.weather_type
    @weather.max = $game_screen.weather_max
    @weather.update
    # Update picture sprites
    for sprite in @picture_sprites
      sprite.update
    end
    # Update timer sprite
    @timer_sprite.update
    # Set screen color tone and shake position
    @viewport1.tone = $game_screen.tone
    @viewport1.ox = $game_screen.shake
    # Set screen flash color
    @viewport4.color = $game_screen.flash_color
    # Update viewports
    @viewport1.update
    @viewport2.update
    @viewport4.update
  end
end
#==============================================================================
# ** Window_Base
#------------------------------------------------------------------------------
#  This class is for all in-game windows.
#==============================================================================

class Window_Base < Window
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     x      : window x-coordinate
  #     y      : window y-coordinate
  #     width  : window width
  #     height : window height
  #--------------------------------------------------------------------------
  def initialize(x, y, width, height)
    super()
    @windowskin_name = $game_system.windowskin_name
    self.windowskin = RPG::Cache.windowskin(@windowskin_name)
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.z = 100
  end
  #--------------------------------------------------------------------------
  # * Dispose
  #--------------------------------------------------------------------------
  def dispose
    # Dispose if window contents bit map is set
    if self.contents != nil
      self.contents.dispose
    end
    super
  end
  #--------------------------------------------------------------------------
  # * Get Text Color
  #     n : text color number (0-7)
  #--------------------------------------------------------------------------
  def text_color(n)
    case n
    when 0
      return Color.new(255, 255, 255, 255)
    when 1
      return Color.new(128, 128, 255, 255)
    when 2
      return Color.new(255, 128, 128, 255)
    when 3
      return Color.new(128, 255, 128, 255)
    when 4
      return Color.new(128, 255, 255, 255)
    when 5
      return Color.new(255, 128, 255, 255)
    when 6
      return Color.new(255, 255, 128, 255)
    when 7
      return Color.new(192, 192, 192, 255)
    else
      normal_color
    end
  end
  #--------------------------------------------------------------------------
  # * Get Normal Text Color
  #--------------------------------------------------------------------------
  def normal_color
    return Color.new(255, 255, 255, 255)
  end
  #--------------------------------------------------------------------------
  # * Get Disabled Text Color
  #--------------------------------------------------------------------------
  def disabled_color
    return Color.new(255, 255, 255, 128)
  end
  #--------------------------------------------------------------------------
  # * Get System Text Color
  #--------------------------------------------------------------------------
  def system_color
    return Color.new(192, 224, 255, 255)
  end
  #--------------------------------------------------------------------------
  # * Get Crisis Text Color
  #--------------------------------------------------------------------------
  def crisis_color
    return Color.new(255, 255, 64, 255)
  end
  #--------------------------------------------------------------------------
  # * Get Knockout Text Color
  #--------------------------------------------------------------------------
  def knockout_color
    return Color.new(255, 64, 0)
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    super
    # Reset if windowskin was changed
    if $game_system.windowskin_name != @windowskin_name
      @windowskin_name = $game_system.windowskin_name
      self.windowskin = RPG::Cache.windowskin(@windowskin_name)
    end
  end
  #--------------------------------------------------------------------------
  # * Draw Graphic
  #     actor : actor
  #     x     : draw spot x-coordinate
  #     y     : draw spot y-coordinate
  #--------------------------------------------------------------------------
  def draw_actor_graphic(actor, x, y)
    bitmap = RPG::Cache.character(actor.character_name, actor.character_hue)
    cw = bitmap.width / 4
    ch = bitmap.height / 4
    src_rect = Rect.new(0, 0, cw, ch)
    self.contents.blt(x - cw / 2, y - ch, bitmap, src_rect)
  end
  #--------------------------------------------------------------------------
  # * Draw Name
  #     actor : actor
  #     x     : draw spot x-coordinate
  #     y     : draw spot y-coordinate
  #--------------------------------------------------------------------------
  def draw_actor_name(actor, x, y)
    self.contents.font.color = normal_color
    self.contents.draw_text(x, y, 120, 32, actor.name)
  end
  #--------------------------------------------------------------------------
  # * Draw Class
  #     actor : actor
  #     x     : draw spot x-coordinate
  #     y     : draw spot y-coordinate
  #--------------------------------------------------------------------------
  def draw_actor_class(actor, x, y)
    self.contents.font.color = normal_color
    self.contents.draw_text(x, y, 236, 32, actor.class_name)
  end
  #--------------------------------------------------------------------------
  # * Draw Level
  #     actor : actor
  #     x     : draw spot x-coordinate
  #     y     : draw spot y-coordinate
  #--------------------------------------------------------------------------
  def draw_actor_level(actor, x, y)
    self.contents.font.color = system_color
    self.contents.draw_text(x, y, 32, 32, "Lv")
    self.contents.font.color = normal_color
    self.contents.draw_text(x + 32, y, 24, 32, actor.level.to_s, 2)
  end
  #--------------------------------------------------------------------------
  # * Make State Text String for Drawing
  #     actor       : actor
  #     width       : draw spot width
  #     need_normal : Whether or not [normal] is needed (true / false)
  #--------------------------------------------------------------------------
  def make_battler_state_text(battler, width, need_normal)
    # Get width of brackets
    brackets_width = self.contents.text_size("[]").width
    # Make text string for state names
    text = ""
    for i in battler.states
      if $data_states[i].rating >= 1
        if text == ""
          text = $data_states[i].name
        else
          new_text = text + "/" + $data_states[i].name
          text_width = self.contents.text_size(new_text).width
          if text_width > width - brackets_width
            break
          end
          text = new_text
        end
      end
    end
    # If text string for state names is empty, make it [normal]
    if text == ""
      if need_normal
        text = "[Normal]"
      end
    else
      # Attach brackets
      text = "[" + text + "]"
    end
    # Return completed text string
    return text
  end
  #--------------------------------------------------------------------------
  # * Draw State
  #     actor : actor
  #     x     : draw spot x-coordinate
  #     y     : draw spot y-coordinate
  #     width : draw spot width
  #--------------------------------------------------------------------------
  def draw_actor_state(actor, x, y, width = 120)
    text = make_battler_state_text(actor, width, true)
    self.contents.font.color = actor.hp == 0 ? knockout_color : normal_color
    self.contents.draw_text(x, y, width, 32, text)
  end
  #--------------------------------------------------------------------------
  # * Draw EXP
  #     actor : actor
  #     x     : draw spot x-coordinate
  #     y     : draw spot y-coordinate
  #--------------------------------------------------------------------------
  def draw_actor_exp(actor, x, y)
    self.contents.font.color = system_color
    self.contents.draw_text(x, y, 24, 32, "E")
    self.contents.font.color = normal_color
    self.contents.draw_text(x + 24, y, 84, 32, actor.exp_s, 2)
    self.contents.draw_text(x + 108, y, 12, 32, "/", 1)
    self.contents.draw_text(x + 120, y, 84, 32, actor.next_exp_s)
  end
  #--------------------------------------------------------------------------
  # * Draw HP
  #     actor : actor
  #     x     : draw spot x-coordinate
  #     y     : draw spot y-coordinate
  #     width : draw spot width
  #--------------------------------------------------------------------------
  def draw_actor_hp(actor, x, y, width = 144)
    # Draw "HP" text string
    self.contents.font.color = system_color
    self.contents.draw_text(x, y, 32, 32, $data_system.words.hp)
    # Calculate if there is draw space for MaxHP
    if width - 32 >= 108
      hp_x = x + width - 108
      flag = true
    elsif width - 32 >= 48
      hp_x = x + width - 48
      flag = false
    end
    # Draw HP
    self.contents.font.color = actor.hp == 0 ? knockout_color :
      actor.hp <= actor.maxhp / 4 ? crisis_color : normal_color
    self.contents.draw_text(hp_x, y, 48, 32, actor.hp.to_s, 2)
    # Draw MaxHP
    if flag
      self.contents.font.color = normal_color
      self.contents.draw_text(hp_x + 48, y, 12, 32, "/", 1)
      self.contents.draw_text(hp_x + 60, y, 48, 32, actor.maxhp.to_s)
    end
  end
  #--------------------------------------------------------------------------
  # * Draw SP
  #     actor : actor
  #     x     : draw spot x-coordinate
  #     y     : draw spot y-coordinate
  #     width : draw spot width
  #--------------------------------------------------------------------------
  def draw_actor_sp(actor, x, y, width = 144)
    # Draw "SP" text string
    self.contents.font.color = system_color
    self.contents.draw_text(x, y, 32, 32, $data_system.words.sp)
    # Calculate if there is draw space for MaxHP
    if width - 32 >= 108
      sp_x = x + width - 108
      flag = true
    elsif width - 32 >= 48
      sp_x = x + width - 48
      flag = false
    end
    # Draw SP
    self.contents.font.color = actor.sp == 0 ? knockout_color :
      actor.sp <= actor.maxsp / 4 ? crisis_color : normal_color
    self.contents.draw_text(sp_x, y, 48, 32, actor.sp.to_s, 2)
    # Draw MaxSP
    if flag
      self.contents.font.color = normal_color
      self.contents.draw_text(sp_x + 48, y, 12, 32, "/", 1)
      self.contents.draw_text(sp_x + 60, y, 48, 32, actor.maxsp.to_s)
    end
  end
  #--------------------------------------------------------------------------
  # * Draw Parameter
  #     actor : actor
  #     x     : draw spot x-coordinate
  #     y     : draw spot y-coordinate
  #     type  : parameter type (0-6)
  #--------------------------------------------------------------------------
  def draw_actor_parameter(actor, x, y, type)
    case type
    when 0
      parameter_name = $data_system.words.atk
      parameter_value = actor.atk
    when 1
      parameter_name = $data_system.words.pdef
      parameter_value = actor.pdef
    when 2
      parameter_name = $data_system.words.mdef
      parameter_value = actor.mdef
    when 3
      parameter_name = $data_system.words.str
      parameter_value = actor.str
    when 4
      parameter_name = $data_system.words.dex
      parameter_value = actor.dex
    when 5
      parameter_name = $data_system.words.agi
      parameter_value = actor.agi
    when 6
      parameter_name = $data_system.words.int
      parameter_value = actor.int
    end
    self.contents.font.color = system_color
    self.contents.draw_text(x, y, 120, 32, parameter_name)
    self.contents.font.color = normal_color
    self.contents.draw_text(x + 120, y, 36, 32, parameter_value.to_s, 2)
  end
  #--------------------------------------------------------------------------
  # * Draw Item Name
  #     item : item
  #     x    : draw spot x-coordinate
  #     y    : draw spot y-coordinate
  #--------------------------------------------------------------------------
  def draw_item_name(item, x, y)
    if item == nil
      return
    end
    bitmap = RPG::Cache.icon(item.icon_name)
    self.contents.blt(x, y + 4, bitmap, Rect.new(0, 0, 24, 24))
    self.contents.font.color = normal_color
    self.contents.draw_text(x + 28, y, 212, 32, item.name)
  end
end
#==============================================================================
# ** Window_Selectable
#------------------------------------------------------------------------------
#  This window class contains cursor movement and scroll functions.
#==============================================================================

class Window_Selectable < Window_Base
  #--------------------------------------------------------------------------
  # * Public Instance Variables
  #--------------------------------------------------------------------------
  attr_reader   :index                    # cursor position
  attr_reader   :help_window              # help window
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     x      : window x-coordinate
  #     y      : window y-coordinate
  #     width  : window width
  #     height : window height
  #--------------------------------------------------------------------------
  def initialize(x, y, width, height)
    super(x, y, width, height)
    @item_max = 1
    @column_max = 1
    @index = -1
  end
  #--------------------------------------------------------------------------
  # * Set Cursor Position
  #     index : new cursor position
  #--------------------------------------------------------------------------
  def index=(index)
    @index = index
    # Update Help Text (update_help is defined by the subclasses)
    if self.active and @help_window != nil
      update_help
    end
    # Update cursor rectangle
    update_cursor_rect
  end
  #--------------------------------------------------------------------------
  # * Get Row Count
  #--------------------------------------------------------------------------
  def row_max
    # Compute rows from number of items and columns
    return (@item_max + @column_max - 1) / @column_max
  end
  #--------------------------------------------------------------------------
  # * Get Top Row
  #--------------------------------------------------------------------------
  def top_row
    # Divide y-coordinate of window contents transfer origin by 1 row
    # height of 32
    return self.oy / 32
  end
  #--------------------------------------------------------------------------
  # * Set Top Row
  #     row : row shown on top
  #--------------------------------------------------------------------------
  def top_row=(row)
    # If row is less than 0, change it to 0
    if row < 0
      row = 0
    end
    # If row exceeds row_max - 1, change it to row_max - 1
    if row > row_max - 1
      row = row_max - 1
    end
    # Multiply 1 row height by 32 for y-coordinate of window contents
    # transfer origin
    self.oy = row * 32
  end
  #--------------------------------------------------------------------------
  # * Get Number of Rows Displayable on 1 Page
  #--------------------------------------------------------------------------
  def page_row_max
    # Subtract a frame height of 32 from the window height, and divide it by
    # 1 row height of 32
    return (self.height - 32) / 32
  end
  #--------------------------------------------------------------------------
  # * Get Number of Items Displayable on 1 Page
  #--------------------------------------------------------------------------
  def page_item_max
    # Multiply row count (page_row_max) times column count (@column_max)
    return page_row_max * @column_max
  end
  #--------------------------------------------------------------------------
  # * Set Help Window
  #     help_window : new help window
  #--------------------------------------------------------------------------
  def help_window=(help_window)
    @help_window = help_window
    # Update help text (update_help is defined by the subclasses)
    if self.active and @help_window != nil
      update_help
    end
  end
  #--------------------------------------------------------------------------
  # * Update Cursor Rectangle
  #--------------------------------------------------------------------------
  def update_cursor_rect
    # If cursor position is less than 0
    if @index < 0
      self.cursor_rect.empty
      return
    end
    # Get current row
    row = @index / @column_max
    # If current row is before top row
    if row < self.top_row
      # Scroll so that current row becomes top row
      self.top_row = row
    end
    # If current row is more to back than back row
    if row > self.top_row + (self.page_row_max - 1)
      # Scroll so that current row becomes back row
      self.top_row = row - (self.page_row_max - 1)
    end
    # Calculate cursor width
    cursor_width = self.width / @column_max - 32
    # Calculate cursor coordinates
    x = @index % @column_max * (cursor_width + 32)
    y = @index / @column_max * 32 - self.oy
    # Update cursor rectangle
    self.cursor_rect.set(x, y, cursor_width, 32)
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    super
    # If cursor is movable
    if self.active and @item_max > 0 and @index >= 0
      # If pressing down on the directional buttons
      if Input.repeat?(Input::DOWN)
        # If column count is 1 and directional button was pressed down with no
        # repeat, or if cursor position is more to the front than
        # (item count - column count)
        if (@column_max == 1 and Input.trigger?(Input::DOWN)) or
           @index < @item_max - @column_max
          # Move cursor down
          $game_system.se_play($data_system.cursor_se)
          @index = (@index + @column_max) % @item_max
        end
      end
      # If the up directional button was pressed
      if Input.repeat?(Input::UP)
        # If column count is 1 and directional button was pressed up with no
        # repeat, or if cursor position is more to the back than column count
        if (@column_max == 1 and Input.trigger?(Input::UP)) or
           @index >= @column_max
          # Move cursor up
          $game_system.se_play($data_system.cursor_se)
          @index = (@index - @column_max + @item_max) % @item_max
        end
      end
      # If the right directional button was pressed
      if Input.repeat?(Input::RIGHT)
        # If column count is 2 or more, and cursor position is closer to front
        # than (item count -1)
        if @column_max >= 2 and @index < @item_max - 1
          # Move cursor right
          $game_system.se_play($data_system.cursor_se)
          @index += 1
        end
      end
      # If the left directional button was pressed
      if Input.repeat?(Input::LEFT)
        # If column count is 2 or more, and cursor position is more back than 0
        if @column_max >= 2 and @index > 0
          # Move cursor left
          $game_system.se_play($data_system.cursor_se)
          @index -= 1
        end
      end
      # If R button was pressed
      if Input.repeat?(Input::R)
        # If bottom row being displayed is more to front than bottom data row
        if self.top_row + (self.page_row_max - 1) < (self.row_max - 1)
          # Move cursor 1 page back
          $game_system.se_play($data_system.cursor_se)
          @index = [@index + self.page_item_max, @item_max - 1].min
          self.top_row += self.page_row_max
        end
      end
      # If L button was pressed
      if Input.repeat?(Input::L)
        # If top row being displayed is more to back than 0
        if self.top_row > 0
          # Move cursor 1 page forward
          $game_system.se_play($data_system.cursor_se)
          @index = [@index - self.page_item_max, 0].max
          self.top_row -= self.page_row_max
        end
      end
    end
    # Update help text (update_help is defined by the subclasses)
    if self.active and @help_window != nil
      update_help
    end
    # Update cursor rectangle
    update_cursor_rect
  end
end
#==============================================================================
# ** Window_Command
#------------------------------------------------------------------------------
#  This window deals with general command choices.
#==============================================================================

class Window_Command < Window_Selectable
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     width    : window width
  #     commands : command text string array
  #--------------------------------------------------------------------------
  def initialize(width, commands)
    # Compute window height from command quantity
    super(0, 0, width, commands.size * 32 + 32)
    @item_max = commands.size
    @commands = commands
    self.contents = Bitmap.new(width - 32, @item_max * 32)
    refresh
    self.index = 0
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    self.contents.clear
    for i in 0...@item_max
      draw_item(i, normal_color)
    end
  end
  #--------------------------------------------------------------------------
  # * Draw Item
  #     index : item number
  #     color : text color
  #--------------------------------------------------------------------------
  def draw_item(index, color)
    self.contents.font.color = color
    rect = Rect.new(4, 32 * index, self.contents.width - 8, 32)
    self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
    self.contents.draw_text(rect, @commands[index])
  end
  #--------------------------------------------------------------------------
  # * Disable Item
  #     index : item number
  #--------------------------------------------------------------------------
  def disable_item(index)
    draw_item(index, disabled_color)
  end
end
#==============================================================================
# ** Window_Help
#------------------------------------------------------------------------------
#  This window shows skill and item explanations along with actor status.
#==============================================================================

class Window_Help < Window_Base
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    super(0, 0, 640, 64)
    self.contents = Bitmap.new(width - 32, height - 32)
  end
  #--------------------------------------------------------------------------
  # * Set Text
  #  text  : text string displayed in window
  #  align : alignment (0..flush left, 1..center, 2..flush right)
  #--------------------------------------------------------------------------
  def set_text(text, align = 0)
    # If at least one part of text and alignment differ from last time
    if text != @text or align != @align
      # Redraw text
      self.contents.clear
      self.contents.font.color = normal_color
      self.contents.draw_text(4, 0, self.width - 40, 32, text, align)
      @text = text
      @align = align
      @actor = nil
    end
    self.visible = true
  end
  #--------------------------------------------------------------------------
  # * Set Actor
  #     actor : status displaying actor
  #--------------------------------------------------------------------------
  def set_actor(actor)
    if actor != @actor
      self.contents.clear
      draw_actor_name(actor, 4, 0)
      draw_actor_state(actor, 140, 0)
      draw_actor_hp(actor, 284, 0)
      draw_actor_sp(actor, 460, 0)
      @actor = actor
      @text = nil
      self.visible = true
    end
  end
  #--------------------------------------------------------------------------
  # * Set Enemy
  #     enemy : name and status displaying enemy
  #--------------------------------------------------------------------------
  def set_enemy(enemy)
    text = enemy.name
    state_text = make_battler_state_text(enemy, 112, false)
    if state_text != ""
      text += "  " + state_text
    end
    set_text(text, 1)
  end
end
#==============================================================================
# ** Window_Gold
#------------------------------------------------------------------------------
#  This window displays amount of gold.
#==============================================================================

class Window_Gold < Window_Base
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    super(0, 0, 160, 64)
    self.contents = Bitmap.new(width - 32, height - 32)
    refresh
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    self.contents.clear
    cx = contents.text_size($data_system.words.gold).width
    self.contents.font.color = normal_color
    self.contents.draw_text(4, 0, 120-cx-2, 32, $game_party.gold.to_s, 2)
    self.contents.font.color = system_color
    self.contents.draw_text(124-cx, 0, cx, 32, $data_system.words.gold, 2)
  end
end
#==============================================================================
# ** Window_PlayTime
#------------------------------------------------------------------------------
#  This window displays play time on the menu screen.
#==============================================================================

class Window_PlayTime < Window_Base
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    super(0, 0, 160, 96)
    self.contents = Bitmap.new(width - 32, height - 32)
    refresh
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    self.contents.clear
    self.contents.font.color = system_color
    self.contents.draw_text(4, 0, 120, 32, "Play Time")
    @total_sec = Graphics.frame_count / Graphics.frame_rate
    hour = @total_sec / 60 / 60
    min = @total_sec / 60 % 60
    sec = @total_sec % 60
    text = sprintf("%02d:%02d:%02d", hour, min, sec)
    self.contents.font.color = normal_color
    self.contents.draw_text(4, 32, 120, 32, text, 2)
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    super
    if Graphics.frame_count / Graphics.frame_rate != @total_sec
      refresh
    end
  end
end
#==============================================================================
# ** Window_Steps
#------------------------------------------------------------------------------
#  This window displays step count on the menu screen.
#==============================================================================

class Window_Steps < Window_Base
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    super(0, 0, 160, 96)
    self.contents = Bitmap.new(width - 32, height - 32)
    refresh
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    self.contents.clear
    self.contents.font.color = system_color
    self.contents.draw_text(4, 0, 120, 32, "Step Count")
    self.contents.font.color = normal_color
    self.contents.draw_text(4, 32, 120, 32, $game_party.steps.to_s, 2)
  end
end
#==============================================================================
# ** Window_MenuStatus
#------------------------------------------------------------------------------
#  This window displays party member status on the menu screen.
#==============================================================================

class Window_MenuStatus < Window_Selectable
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    super(0, 0, 480, 480)
    self.contents = Bitmap.new(width - 32, height - 32)
    refresh
    self.active = false
    self.index = -1
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    self.contents.clear
    @item_max = $game_party.actors.size
    for i in 0...$game_party.actors.size
      x = 64
      y = i * 116
      actor = $game_party.actors[i]
      draw_actor_graphic(actor, x - 40, y + 80)
      draw_actor_name(actor, x, y)
      draw_actor_class(actor, x + 144, y)
      draw_actor_level(actor, x, y + 32)
      draw_actor_state(actor, x + 90, y + 32)
      draw_actor_exp(actor, x, y + 64)
      draw_actor_hp(actor, x + 236, y + 32)
      draw_actor_sp(actor, x + 236, y + 64)
    end
  end
  #--------------------------------------------------------------------------
  # * Cursor Rectangle Update
  #--------------------------------------------------------------------------
  def update_cursor_rect
    if @index < 0
      self.cursor_rect.empty
    else
      self.cursor_rect.set(0, @index * 116, self.width - 32, 96)
    end
  end
end
#==============================================================================
# ** Window_Item
#------------------------------------------------------------------------------
#  This window displays items in possession on the item and battle screens.
#==============================================================================

class Window_Item < Window_Selectable
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    super(0, 64, 640, 416)
    @column_max = 2
    refresh
    self.index = 0
    # If in battle, move window to center of screen
    # and make it semi-transparent
    if $game_temp.in_battle
      self.y = 64
      self.height = 256
      self.back_opacity = 160
    end
  end
  #--------------------------------------------------------------------------
  # * Get Item
  #--------------------------------------------------------------------------
  def item
    return @data[self.index]
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    @data = []
    # Add item
    for i in 1...$data_items.size
      if $game_party.item_number(i) > 0
        @data.push($data_items[i])
      end
    end
    # Also add weapons and items if outside of battle
    unless $game_temp.in_battle
      for i in 1...$data_weapons.size
        if $game_party.weapon_number(i) > 0
          @data.push($data_weapons[i])
        end
      end
      for i in 1...$data_armors.size
        if $game_party.armor_number(i) > 0
          @data.push($data_armors[i])
        end
      end
    end
    # If item count is not 0, make a bit map and draw all items
    @item_max = @data.size
    if @item_max > 0
      self.contents = Bitmap.new(width - 32, row_max * 32)
      for i in 0...@item_max
        draw_item(i)
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Draw Item
  #     index : item number
  #--------------------------------------------------------------------------
  def draw_item(index)
    item = @data[index]
    case item
    when RPG::Item
      number = $game_party.item_number(item.id)
    when RPG::Weapon
      number = $game_party.weapon_number(item.id)
    when RPG::Armor
      number = $game_party.armor_number(item.id)
    end
    if item.is_a?(RPG::Item) and
       $game_party.item_can_use?(item.id)
      self.contents.font.color = normal_color
    else
      self.contents.font.color = disabled_color
    end
    x = 4 + index % 2 * (288 + 32)
    y = index / 2 * 32
    rect = Rect.new(x, y, self.width / @column_max - 32, 32)
    self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
    bitmap = RPG::Cache.icon(item.icon_name)
    opacity = self.contents.font.color == normal_color ? 255 : 128
    self.contents.blt(x, y + 4, bitmap, Rect.new(0, 0, 24, 24), opacity)
    self.contents.draw_text(x + 28, y, 212, 32, item.name, 0)
    self.contents.draw_text(x + 240, y, 16, 32, ":", 1)
    self.contents.draw_text(x + 256, y, 24, 32, number.to_s, 2)
  end
  #--------------------------------------------------------------------------
  # * Help Text Update
  #--------------------------------------------------------------------------
  def update_help
    @help_window.set_text(self.item == nil ? "" : self.item.description)
  end
end
#==============================================================================
# ** Window_Skill
#------------------------------------------------------------------------------
#  This window displays usable skills on the skill and battle screens.
#==============================================================================

class Window_Skill < Window_Selectable
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     actor : actor
  #--------------------------------------------------------------------------
  def initialize(actor)
    super(0, 128, 640, 352)
    @actor = actor
    @column_max = 2
    refresh
    self.index = 0
    # If in battle, move window to center of screen
    # and make it semi-transparent
    if $game_temp.in_battle
      self.y = 64
      self.height = 256
      self.back_opacity = 160
    end
  end
  #--------------------------------------------------------------------------
  # * Acquiring Skill
  #--------------------------------------------------------------------------
  def skill
    return @data[self.index]
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    @data = []
    for i in 0...@actor.skills.size
      skill = $data_skills[@actor.skills[i]]
      if skill != nil
        @data.push(skill)
      end
    end
    # If item count is not 0, make a bit map and draw all items
    @item_max = @data.size
    if @item_max > 0
      self.contents = Bitmap.new(width - 32, row_max * 32)
      for i in 0...@item_max
        draw_item(i)
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Draw Item
  #     index : item number
  #--------------------------------------------------------------------------
  def draw_item(index)
    skill = @data[index]
    if @actor.skill_can_use?(skill.id)
      self.contents.font.color = normal_color
    else
      self.contents.font.color = disabled_color
    end
    x = 4 + index % 2 * (288 + 32)
    y = index / 2 * 32
    rect = Rect.new(x, y, self.width / @column_max - 32, 32)
    self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
    bitmap = RPG::Cache.icon(skill.icon_name)
    opacity = self.contents.font.color == normal_color ? 255 : 128
    self.contents.blt(x, y + 4, bitmap, Rect.new(0, 0, 24, 24), opacity)
    self.contents.draw_text(x + 28, y, 204, 32, skill.name, 0)
    self.contents.draw_text(x + 232, y, 48, 32, skill.sp_cost.to_s, 2)
  end
  #--------------------------------------------------------------------------
  # * Help Text Update
  #--------------------------------------------------------------------------
  def update_help
    @help_window.set_text(self.skill == nil ? "" : self.skill.description)
  end
end
#==============================================================================
# ** Window_SkillStatus
#------------------------------------------------------------------------------
#  This window displays the skill user's status on the skill screen.
#==============================================================================

class Window_SkillStatus < Window_Base
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     actor : actor
  #--------------------------------------------------------------------------
  def initialize(actor)
    super(0, 64, 640, 64)
    self.contents = Bitmap.new(width - 32, height - 32)
    @actor = actor
    refresh
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    self.contents.clear
    draw_actor_name(@actor, 4, 0)
    draw_actor_state(@actor, 140, 0)
    draw_actor_hp(@actor, 284, 0)
    draw_actor_sp(@actor, 460, 0)
  end
end
#==============================================================================
# ** Window_Target
#------------------------------------------------------------------------------
#  This window selects a use target for the actor on item and skill screens.
#==============================================================================

class Window_Target < Window_Selectable
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    super(0, 0, 336, 480)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.z += 10
    @item_max = $game_party.actors.size
    refresh
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    self.contents.clear
    for i in 0...$game_party.actors.size
      x = 4
      y = i * 116
      actor = $game_party.actors[i]
      draw_actor_name(actor, x, y)
      draw_actor_class(actor, x + 144, y)
      draw_actor_level(actor, x + 8, y + 32)
      draw_actor_state(actor, x + 8, y + 64)
      draw_actor_hp(actor, x + 152, y + 32)
      draw_actor_sp(actor, x + 152, y + 64)
    end
  end
  #--------------------------------------------------------------------------
  # * Cursor Rectangle Update
  #--------------------------------------------------------------------------
  def update_cursor_rect
    # Cursor position -1 = all choices, -2 or lower = independent choice
    # (meaning the user's own choice)
    if @index <= -2
      self.cursor_rect.set(0, (@index + 10) * 116, self.width - 32, 96)
    elsif @index == -1
      self.cursor_rect.set(0, 0, self.width - 32, @item_max * 116 - 20)
    else
      self.cursor_rect.set(0, @index * 116, self.width - 32, 96)
    end
  end
end
#==============================================================================
# ** Window_EquipLeft
#------------------------------------------------------------------------------
#  This window displays actor parameter changes on the equipment screen.
#==============================================================================

class Window_EquipLeft < Window_Base
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     actor : actor
  #--------------------------------------------------------------------------
  def initialize(actor)
    super(0, 64, 272, 192)
    self.contents = Bitmap.new(width - 32, height - 32)
    @actor = actor
    refresh
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    self.contents.clear
    draw_actor_name(@actor, 4, 0)
    draw_actor_level(@actor, 4, 32)
    draw_actor_parameter(@actor, 4, 64, 0)
    draw_actor_parameter(@actor, 4, 96, 1)
    draw_actor_parameter(@actor, 4, 128, 2)
    if @new_atk != nil
      self.contents.font.color = system_color
      self.contents.draw_text(160, 64, 40, 32, "->", 1)
      self.contents.font.color = normal_color
      self.contents.draw_text(200, 64, 36, 32, @new_atk.to_s, 2)
    end
    if @new_pdef != nil
      self.contents.font.color = system_color
      self.contents.draw_text(160, 96, 40, 32, "->", 1)
      self.contents.font.color = normal_color
      self.contents.draw_text(200, 96, 36, 32, @new_pdef.to_s, 2)
    end
    if @new_mdef != nil
      self.contents.font.color = system_color
      self.contents.draw_text(160, 128, 40, 32, "->", 1)
      self.contents.font.color = normal_color
      self.contents.draw_text(200, 128, 36, 32, @new_mdef.to_s, 2)
    end
  end
  #--------------------------------------------------------------------------
  # * Set parameters after changing equipment
  #     new_atk  : attack power after changing equipment
  #     new_pdef : physical defense after changing equipment
  #     new_mdef : magic defense after changing equipment
  #--------------------------------------------------------------------------
  def set_new_parameters(new_atk, new_pdef, new_mdef)
    if @new_atk != new_atk or @new_pdef != new_pdef or @new_mdef != new_mdef
      @new_atk = new_atk
      @new_pdef = new_pdef
      @new_mdef = new_mdef
      refresh
    end
  end
end
#==============================================================================
# ** Window_EquipRight
#------------------------------------------------------------------------------
#  This window displays items the actor is currently equipped with on the
#  equipment screen.
#==============================================================================

class Window_EquipRight < Window_Selectable
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     actor : actor
  #--------------------------------------------------------------------------
  def initialize(actor)
    super(272, 64, 368, 192)
    self.contents = Bitmap.new(width - 32, height - 32)
    @actor = actor
    refresh
    self.index = 0
  end
  #--------------------------------------------------------------------------
  # * Item Acquisition
  #--------------------------------------------------------------------------
  def item
    return @data[self.index]
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    self.contents.clear
    @data = []
    @data.push($data_weapons[@actor.weapon_id])
    @data.push($data_armors[@actor.armor1_id])
    @data.push($data_armors[@actor.armor2_id])
    @data.push($data_armors[@actor.armor3_id])
    @data.push($data_armors[@actor.armor4_id])
    @item_max = @data.size
    self.contents.font.color = system_color
    self.contents.draw_text(4, 32 * 0, 92, 32, $data_system.words.weapon)
    self.contents.draw_text(4, 32 * 1, 92, 32, $data_system.words.armor1)
    self.contents.draw_text(4, 32 * 2, 92, 32, $data_system.words.armor2)
    self.contents.draw_text(4, 32 * 3, 92, 32, $data_system.words.armor3)
    self.contents.draw_text(5, 32 * 4, 92, 32, $data_system.words.armor4)
    draw_item_name(@data[0], 92, 32 * 0)
    draw_item_name(@data[1], 92, 32 * 1)
    draw_item_name(@data[2], 92, 32 * 2)
    draw_item_name(@data[3], 92, 32 * 3)
    draw_item_name(@data[4], 92, 32 * 4)
  end
  #--------------------------------------------------------------------------
  # * Help Text Update
  #--------------------------------------------------------------------------
  def update_help
    @help_window.set_text(self.item == nil ? "" : self.item.description)
  end
end
#==============================================================================
# ** Window_EquipItem
#------------------------------------------------------------------------------
#  This window displays choices when opting to change equipment on the
#  equipment screen.
#==============================================================================

class Window_EquipItem < Window_Selectable
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     actor      : actor
  #     equip_type : equip region (0-3)
  #--------------------------------------------------------------------------
  def initialize(actor, equip_type)
    super(0, 256, 640, 224)
    @actor = actor
    @equip_type = equip_type
    @column_max = 2
    refresh
    self.active = false
    self.index = -1
  end
  #--------------------------------------------------------------------------
  # * Item Acquisition
  #--------------------------------------------------------------------------
  def item
    return @data[self.index]
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    @data = []
    # Add equippable weapons
    if @equip_type == 0
      weapon_set = $data_classes[@actor.class_id].weapon_set
      for i in 1...$data_weapons.size
        if $game_party.weapon_number(i) > 0 and weapon_set.include?(i)
          @data.push($data_weapons[i])
        end
      end
    end
    # Add equippable armor
    if @equip_type != 0
      armor_set = $data_classes[@actor.class_id].armor_set
      for i in 1...$data_armors.size
        if $game_party.armor_number(i) > 0 and armor_set.include?(i)
          if $data_armors[i].kind == @equip_type-1
            @data.push($data_armors[i])
          end
        end
      end
    end
    # Add blank page
    @data.push(nil)
    # Make a bit map and draw all items
    @item_max = @data.size
    self.contents = Bitmap.new(width - 32, row_max * 32)
    for i in 0...@item_max-1
      draw_item(i)
    end
  end
  #--------------------------------------------------------------------------
  # * Draw Item
  #     index : item number
  #--------------------------------------------------------------------------
  def draw_item(index)
    item = @data[index]
    x = 4 + index % 2 * (288 + 32)
    y = index / 2 * 32
    case item
    when RPG::Weapon
      number = $game_party.weapon_number(item.id)
    when RPG::Armor
      number = $game_party.armor_number(item.id)
    end
    bitmap = RPG::Cache.icon(item.icon_name)
    self.contents.blt(x, y + 4, bitmap, Rect.new(0, 0, 24, 24))
    self.contents.font.color = normal_color
    self.contents.draw_text(x + 28, y, 212, 32, item.name, 0)
    self.contents.draw_text(x + 240, y, 16, 32, ":", 1)
    self.contents.draw_text(x + 256, y, 24, 32, number.to_s, 2)
  end
  #--------------------------------------------------------------------------
  # * Help Text Update
  #--------------------------------------------------------------------------
  def update_help
    @help_window.set_text(self.item == nil ? "" : self.item.description)
  end
end
#==============================================================================
# ** Window_Status
#------------------------------------------------------------------------------
#  This window displays full status specs on the status screen.
#==============================================================================

class Window_Status < Window_Base
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     actor : actor
  #--------------------------------------------------------------------------
  def initialize(actor)
    super(0, 0, 640, 480)
    self.contents = Bitmap.new(width - 32, height - 32)
    @actor = actor
    refresh
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    self.contents.clear
    draw_actor_graphic(@actor, 40, 112)
    draw_actor_name(@actor, 4, 0)
    draw_actor_class(@actor, 4 + 144, 0)
    draw_actor_level(@actor, 96, 32)
    draw_actor_state(@actor, 96, 64)
    draw_actor_hp(@actor, 96, 112, 172)
    draw_actor_sp(@actor, 96, 144, 172)
    draw_actor_parameter(@actor, 96, 192, 0)
    draw_actor_parameter(@actor, 96, 224, 1)
    draw_actor_parameter(@actor, 96, 256, 2)
    draw_actor_parameter(@actor, 96, 304, 3)
    draw_actor_parameter(@actor, 96, 336, 4)
    draw_actor_parameter(@actor, 96, 368, 5)
    draw_actor_parameter(@actor, 96, 400, 6)
    self.contents.font.color = system_color
    self.contents.draw_text(320, 48, 80, 32, "EXP")
    self.contents.draw_text(320, 80, 80, 32, "NEXT")
    self.contents.font.color = normal_color
    self.contents.draw_text(320 + 80, 48, 84, 32, @actor.exp_s, 2)
    self.contents.draw_text(320 + 80, 80, 84, 32, @actor.next_rest_exp_s, 2)
    self.contents.font.color = system_color
    self.contents.draw_text(320, 160, 96, 32, "equipment")
    draw_item_name($data_weapons[@actor.weapon_id], 320 + 16, 208)
    draw_item_name($data_armors[@actor.armor1_id], 320 + 16, 256)
    draw_item_name($data_armors[@actor.armor2_id], 320 + 16, 304)
    draw_item_name($data_armors[@actor.armor3_id], 320 + 16, 352)
    draw_item_name($data_armors[@actor.armor4_id], 320 + 16, 400)
  end
  def dummy
    self.contents.font.color = system_color
    self.contents.draw_text(320, 112, 96, 32, $data_system.words.weapon)
    self.contents.draw_text(320, 176, 96, 32, $data_system.words.armor1)
    self.contents.draw_text(320, 240, 96, 32, $data_system.words.armor2)
    self.contents.draw_text(320, 304, 96, 32, $data_system.words.armor3)
    self.contents.draw_text(320, 368, 96, 32, $data_system.words.armor4)
    draw_item_name($data_weapons[@actor.weapon_id], 320 + 24, 144)
    draw_item_name($data_armors[@actor.armor1_id], 320 + 24, 208)
    draw_item_name($data_armors[@actor.armor2_id], 320 + 24, 272)
    draw_item_name($data_armors[@actor.armor3_id], 320 + 24, 336)
    draw_item_name($data_armors[@actor.armor4_id], 320 + 24, 400)
  end
end
#==============================================================================
# ** Window_SaveFile
#------------------------------------------------------------------------------
#  This window displays save files on the save and load screens.
#==============================================================================

class Window_SaveFile < Window_Base
  #--------------------------------------------------------------------------
  # * Public Instance Variables
  #--------------------------------------------------------------------------
  attr_reader   :filename                 # file name
  attr_reader   :selected                 # selected
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     file_index : save file index (0-3)
  #     filename   : file name
  #--------------------------------------------------------------------------
  def initialize(file_index, filename)
    super(0, 64 + file_index % 4 * 104, 640, 104)
    self.contents = Bitmap.new(width - 32, height - 32)
    @file_index = file_index
    @filename = "Save#{@file_index + 1}.rxdata"
    @time_stamp = Time.at(0)
    @file_exist = FileTest.exist?(@filename)
    if @file_exist
      file = File.open(@filename, "r")
      @time_stamp = file.mtime
      @characters = Marshal.load(file)
      @frame_count = Marshal.load(file)
      @game_system = Marshal.load(file)
      @game_switches = Marshal.load(file)
      @game_variables = Marshal.load(file)
      @total_sec = @frame_count / Graphics.frame_rate
      file.close
    end
    refresh
    @selected = false
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    self.contents.clear
    # Draw file number
    self.contents.font.color = normal_color
    name = "File#{@file_index + 1}"
    self.contents.draw_text(4, 0, 600, 32, name)
    @name_width = contents.text_size(name).width
    # If save file exists
    if @file_exist
      # Draw character
      for i in 0...@characters.size
        bitmap = RPG::Cache.character(@characters[i][0], @characters[i][1])
        cw = bitmap.rect.width / 4
        ch = bitmap.rect.height / 4
        src_rect = Rect.new(0, 0, cw, ch)
        x = 300 - @characters.size * 32 + i * 64 - cw / 2
        self.contents.blt(x, 68 - ch, bitmap, src_rect)
      end
      # Draw play time
      hour = @total_sec / 60 / 60
      min = @total_sec / 60 % 60
      sec = @total_sec % 60
      time_string = sprintf("%02d:%02d:%02d", hour, min, sec)
      self.contents.font.color = normal_color
      self.contents.draw_text(4, 8, 600, 32, time_string, 2)
      # Draw timestamp
      self.contents.font.color = normal_color
      time_string = @time_stamp.strftime("%Y/%m/%d %H:%M")
      self.contents.draw_text(4, 40, 600, 32, time_string, 2)
    end
  end
  #--------------------------------------------------------------------------
  # * Set Selected
  #     selected : new selected (true = selected, false = unselected)
  #--------------------------------------------------------------------------
  def selected=(selected)
    @selected = selected
    update_cursor_rect
  end
  #--------------------------------------------------------------------------
  # * Cursor Rectangle Update
  #--------------------------------------------------------------------------
  def update_cursor_rect
    if @selected
      self.cursor_rect.set(0, 0, @name_width + 8, 32)
    else
      self.cursor_rect.empty
    end
  end
end
#==============================================================================
# ** Window_ShopCommand
#------------------------------------------------------------------------------
#  This window is used to choose your business on the shop screen.
#==============================================================================

class Window_ShopCommand < Window_Selectable
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    super(0, 64, 480, 64)
    self.contents = Bitmap.new(width - 32, height - 32)
    @item_max = 3
    @column_max = 3
    @commands = ["Buy", "Sell", "Exit"]
    refresh
    self.index = 0
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    self.contents.clear
    for i in 0...@item_max
      draw_item(i)
    end
  end
  #--------------------------------------------------------------------------
  # * Draw Item
  #     index : item number
  #--------------------------------------------------------------------------
  def draw_item(index)
    x = 4 + index * 160
    self.contents.draw_text(x, 0, 128, 32, @commands[index])
  end
end
#==============================================================================
# ** Window_ShopBuy
#------------------------------------------------------------------------------
#  This window displays buyable goods on the shop screen.
#==============================================================================

class Window_ShopBuy < Window_Selectable
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     shop_goods : goods
  #--------------------------------------------------------------------------
  def initialize(shop_goods)
    super(0, 128, 368, 352)
    @shop_goods = shop_goods
    refresh
    self.index = 0
  end
  #--------------------------------------------------------------------------
  # * Item Acquisition
  #--------------------------------------------------------------------------
  def item
    return @data[self.index]
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    @data = []
    for goods_item in @shop_goods
      case goods_item[0]
      when 0
        item = $data_items[goods_item[1]]
      when 1
        item = $data_weapons[goods_item[1]]
      when 2
        item = $data_armors[goods_item[1]]
      end
      if item != nil
        @data.push(item)
      end
    end
    # If item count is not 0, make a bit map and draw all items
    @item_max = @data.size
    if @item_max > 0
      self.contents = Bitmap.new(width - 32, row_max * 32)
      for i in 0...@item_max
        draw_item(i)
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Draw Item
  #     index : item number
  #--------------------------------------------------------------------------
  def draw_item(index)
    item = @data[index]
    # Get items in possession
    case item
    when RPG::Item
      number = $game_party.item_number(item.id)
    when RPG::Weapon
      number = $game_party.weapon_number(item.id)
    when RPG::Armor
      number = $game_party.armor_number(item.id)
    end
    # If price is less than money in possession, and amount in possession is
    # not 99, then set to normal text color. Otherwise set to disabled color
    if item.price <= $game_party.gold and number < 99
      self.contents.font.color = normal_color
    else
      self.contents.font.color = disabled_color
    end
    x = 4
    y = index * 32
    rect = Rect.new(x, y, self.width - 32, 32)
    self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
    bitmap = RPG::Cache.icon(item.icon_name)
    opacity = self.contents.font.color == normal_color ? 255 : 128
    self.contents.blt(x, y + 4, bitmap, Rect.new(0, 0, 24, 24), opacity)
    self.contents.draw_text(x + 28, y, 212, 32, item.name, 0)
    self.contents.draw_text(x + 240, y, 88, 32, item.price.to_s, 2)
  end
  #--------------------------------------------------------------------------
  # * Help Text Update
  #--------------------------------------------------------------------------
  def update_help
    @help_window.set_text(self.item == nil ? "" : self.item.description)
  end
end
#==============================================================================
# ** Window_ShopSell
#------------------------------------------------------------------------------
#  This window displays items in possession for selling on the shop screen.
#==============================================================================

class Window_ShopSell < Window_Selectable
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    super(0, 128, 640, 352)
    @column_max = 2
    refresh
    self.index = 0
  end
  #--------------------------------------------------------------------------
  # * Getting Items
  #--------------------------------------------------------------------------
  def item
    return @data[self.index]
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    @data = []
    for i in 1...$data_items.size
      if $game_party.item_number(i) > 0
        @data.push($data_items[i])
      end
    end
    for i in 1...$data_weapons.size
      if $game_party.weapon_number(i) > 0
        @data.push($data_weapons[i])
      end
    end
    for i in 1...$data_armors.size
      if $game_party.armor_number(i) > 0
        @data.push($data_armors[i])
      end
    end
    # If item count is not 0, make a bitmap and draw all items
    @item_max = @data.size
    if @item_max > 0
      self.contents = Bitmap.new(width - 32, row_max * 32)
      for i in 0...@item_max
        draw_item(i)
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Draw Item
  #     index : item number
  #--------------------------------------------------------------------------
  def draw_item(index)
    item = @data[index]
    case item
    when RPG::Item
      number = $game_party.item_number(item.id)
    when RPG::Weapon
      number = $game_party.weapon_number(item.id)
    when RPG::Armor
      number = $game_party.armor_number(item.id)
    end
    # If items are sellable, set to valid text color. If not, set to invalid
    # text color.
    if item.price > 0
      self.contents.font.color = normal_color
    else
      self.contents.font.color = disabled_color
    end
    x = 4 + index % 2 * (288 + 32)
    y = index / 2 * 32
    rect = Rect.new(x, y, self.width / @column_max - 32, 32)
    self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
    bitmap = RPG::Cache.icon(item.icon_name)
    opacity = self.contents.font.color == normal_color ? 255 : 128
    self.contents.blt(x, y + 4, bitmap, Rect.new(0, 0, 24, 24), opacity)
    self.contents.draw_text(x + 28, y, 212, 32, item.name, 0)
    self.contents.draw_text(x + 240, y, 16, 32, ":", 1)
    self.contents.draw_text(x + 256, y, 24, 32, number.to_s, 2)
  end
  #--------------------------------------------------------------------------
  # * Help Text Update
  #--------------------------------------------------------------------------
  def update_help
    @help_window.set_text(self.item == nil ? "" : self.item.description)
  end
end
#==============================================================================
# ** Window_ShopNumber
#------------------------------------------------------------------------------
#  This window is for inputting quantity of items to buy or sell on the
#  shop screen.
#==============================================================================

class Window_ShopNumber < Window_Base
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    super(0, 128, 368, 352)
    self.contents = Bitmap.new(width - 32, height - 32)
    @item = nil
    @max = 1
    @price = 0
    @number = 1
  end
  #--------------------------------------------------------------------------
  # * Set Items, Max Quantity, and Price
  #--------------------------------------------------------------------------
  def set(item, max, price)
    @item = item
    @max = max
    @price = price
    @number = 1
    refresh
  end
  #--------------------------------------------------------------------------
  # * Set Inputted Quantity
  #--------------------------------------------------------------------------
  def number
    return @number
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    self.contents.clear
    draw_item_name(@item, 4, 96)
    self.contents.font.color = normal_color
    self.contents.draw_text(272, 96, 32, 32, "×")
    self.contents.draw_text(308, 96, 24, 32, @number.to_s, 2)
    self.cursor_rect.set(304, 96, 32, 32)
    # Draw total price and currency units
    domination = $data_system.words.gold
    cx = contents.text_size(domination).width
    total_price = @price * @number
    self.contents.font.color = normal_color
    self.contents.draw_text(4, 160, 328-cx-2, 32, total_price.to_s, 2)
    self.contents.font.color = system_color
    self.contents.draw_text(332-cx, 160, cx, 32, domination, 2)
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    super
    if self.active
      # Cursor right (+1)
      if Input.repeat?(Input::RIGHT) and @number < @max
        $game_system.se_play($data_system.cursor_se)
        @number += 1
        refresh
      end
      # Cursor left (-1)
      if Input.repeat?(Input::LEFT) and @number > 1
        $game_system.se_play($data_system.cursor_se)
        @number -= 1
        refresh
      end
      # Cursdr up (+10)
      if Input.repeat?(Input::UP) and @number < @max
        $game_system.se_play($data_system.cursor_se)
        @number = [@number + 10, @max].min
        refresh
      end
      # Cursor down (-10)
      if Input.repeat?(Input::DOWN) and @number > 1
        $game_system.se_play($data_system.cursor_se)
        @number = [@number - 10, 1].max
        refresh
      end
    end
  end
end
#==============================================================================
# ** Window_ShopStatus
#------------------------------------------------------------------------------
#  This window displays number of items in possession and the actor's equipment
#  on the shop screen.
#==============================================================================

class Window_ShopStatus < Window_Base
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    super(368, 128, 272, 352)
    self.contents = Bitmap.new(width - 32, height - 32)
    @item = nil
    refresh
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    self.contents.clear
    if @item == nil
      return
    end
    case @item
    when RPG::Item
      number = $game_party.item_number(@item.id)
    when RPG::Weapon
      number = $game_party.weapon_number(@item.id)
    when RPG::Armor
      number = $game_party.armor_number(@item.id)
    end
    self.contents.font.color = system_color
    self.contents.draw_text(4, 0, 200, 32, "number in possession")
    self.contents.font.color = normal_color
    self.contents.draw_text(204, 0, 32, 32, number.to_s, 2)
    if @item.is_a?(RPG::Item)
      return
    end
    # Equipment adding information
    for i in 0...$game_party.actors.size
      # Get actor
      actor = $game_party.actors[i]
      # If equippable, then set to normal text color. If not, set to
      # invalid text color.
      if actor.equippable?(@item)
        self.contents.font.color = normal_color
      else
        self.contents.font.color = disabled_color
      end
      # Draw actor's name
      self.contents.draw_text(4, 64 + 64 * i, 120, 32, actor.name)
      # Get current equipment
      if @item.is_a?(RPG::Weapon)
        item1 = $data_weapons[actor.weapon_id]
      elsif @item.kind == 0
        item1 = $data_armors[actor.armor1_id]
      elsif @item.kind == 1
        item1 = $data_armors[actor.armor2_id]
      elsif @item.kind == 2
        item1 = $data_armors[actor.armor3_id]
      else
        item1 = $data_armors[actor.armor4_id]
      end
      # If equippable
      if actor.equippable?(@item)
        # If weapon
        if @item.is_a?(RPG::Weapon)
          atk1 = item1 != nil ? item1.atk : 0
          atk2 = @item != nil ? @item.atk : 0
          change = atk2 - atk1
        end
        # If armor
        if @item.is_a?(RPG::Armor)
          pdef1 = item1 != nil ? item1.pdef : 0
          mdef1 = item1 != nil ? item1.mdef : 0
          pdef2 = @item != nil ? @item.pdef : 0
          mdef2 = @item != nil ? @item.mdef : 0
          change = pdef2 - pdef1 + mdef2 - mdef1
        end
        # Draw parameter change values
        self.contents.draw_text(124, 64 + 64 * i, 112, 32,
          sprintf("%+d", change), 2)
      end
      # Draw item
      if item1 != nil
        x = 4
        y = 64 + 64 * i + 32
        bitmap = RPG::Cache.icon(item1.icon_name)
        opacity = self.contents.font.color == normal_color ? 255 : 128
        self.contents.blt(x, y + 4, bitmap, Rect.new(0, 0, 24, 24), opacity)
        self.contents.draw_text(x + 28, y, 212, 32, item1.name)
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Set Item
  #     item : new item
  #--------------------------------------------------------------------------
  def item=(item)
    if @item != item
      @item = item
      refresh
    end
  end
end
#==============================================================================
# ** Window_NameEdit
#------------------------------------------------------------------------------
#  This window is used to edit your name on the input name screen.
#==============================================================================

class Window_NameEdit < Window_Base
  #--------------------------------------------------------------------------
  # * Public Instance Variables
  #--------------------------------------------------------------------------
  attr_reader   :name                     # name
  attr_reader   :index                    # cursor position
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     actor    : actor
  #     max_char : maximum number of characters
  #--------------------------------------------------------------------------
  def initialize(actor, max_char)
    super(0, 0, 640, 128)
    self.contents = Bitmap.new(width - 32, height - 32)
    @actor = actor
    @name = actor.name
    @max_char = max_char
    # Fit name within maximum number of characters
    name_array = @name.split(//)[0...@max_char]
    @name = ""
    for i in 0...name_array.size
      @name += name_array[i]
    end
    @default_name = @name
    @index = name_array.size
    refresh
    update_cursor_rect
  end
  #--------------------------------------------------------------------------
  # * Return to Default Name
  #--------------------------------------------------------------------------
  def restore_default
    @name = @default_name
    @index = @name.split(//).size
    refresh
    update_cursor_rect
  end
  #--------------------------------------------------------------------------
  # * Add Character
  #     character : text character to be added
  #--------------------------------------------------------------------------
  def add(character)
    if @index < @max_char and character != ""
      @name += character
      @index += 1
      refresh
      update_cursor_rect
    end
  end
  #--------------------------------------------------------------------------
  # * Delete Character
  #--------------------------------------------------------------------------
  def back
    if @index > 0
      # Delete 1 text character
      name_array = @name.split(//)
      @name = ""
      for i in 0...name_array.size-1
        @name += name_array[i]
      end
      @index -= 1
      refresh
      update_cursor_rect
    end
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    self.contents.clear
    # Draw name
    name_array = @name.split(//)
    for i in 0...@max_char
      c = name_array[i]
      if c == nil
        c = "＿"
      end
      x = 320 - @max_char * 14 + i * 28
      self.contents.draw_text(x, 32, 28, 32, c, 1)
    end
    # Draw graphic
    draw_actor_graphic(@actor, 320 - @max_char * 14 - 40, 80)
  end
  #--------------------------------------------------------------------------
  # * Cursor Rectangle Update
  #--------------------------------------------------------------------------
  def update_cursor_rect
    x = 320 - @max_char * 14 + @index * 28
    self.cursor_rect.set(x, 32, 28, 32)
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    super
    update_cursor_rect
  end
end
#==============================================================================
# ** Window_NameInput
#------------------------------------------------------------------------------
#  This window is used to select text characters on the input name screen.
#==============================================================================

class Window_NameInput < Window_Base
  CHARACTER_TABLE =
  [
    "A","B","C","D","E",
    "F","G","H","I","J",
    "K","L","M","N","O",
    "P","Q","R","S","T",
    "U","V","W","X","Y",
    "Z"," "," "," "," ",
    "+","-","*","/","!",
    "1","2","3","4","5",
    "" ,"" ,"" ,"" ,"" ,
    "a","b","c","d","e",
    "f","g","h","i","j",
    "k","l","m","n","o",
    "p","q","r","s","t",
    "u","v","w","x","y",
    "z"," "," "," "," ",
    "#","$","%","&","@",
    "6","7","8","9","0",
    "" ,"" ,"" ,"" ,"" ,
  ]
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    super(0, 128, 640, 352)
    self.contents = Bitmap.new(width - 32, height - 32)
    @index = 0
    refresh
    update_cursor_rect
  end
  #--------------------------------------------------------------------------
  # * Text Character Acquisition
  #--------------------------------------------------------------------------
  def character
    return CHARACTER_TABLE[@index]
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    self.contents.clear
    for i in 0...90
      x = 140 + i / 5 / 9 * 180 + i % 5 * 32
      y = i / 5 % 9 * 32
      self.contents.draw_text(x, y, 32, 32, CHARACTER_TABLE[i], 1)
    end
    self.contents.draw_text(428, 9 * 32, 48, 32, "OK", 1)
  end
  #--------------------------------------------------------------------------
  # * Cursor Rectangle Update
  #--------------------------------------------------------------------------
  def update_cursor_rect
    # If cursor is positioned on [OK]
    if @index >= 90
      self.cursor_rect.set(428, 9 * 32, 48, 32)
    # If cursor is positioned on anything other than [OK]
    else
      x = 140 + @index / 5 / 9 * 180 + @index % 5 * 32
      y = @index / 5 % 9 * 32
      self.cursor_rect.set(x, y, 32, 32)
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    super
    # If cursor is positioned on [OK]
    if @index >= 90
      # Cursor down
      if Input.trigger?(Input::DOWN)
        $game_system.se_play($data_system.cursor_se)
        @index -= 90
      end
      # Cursor up
      if Input.repeat?(Input::UP)
        $game_system.se_play($data_system.cursor_se)
        @index -= 90 - 40
      end
    # If cursor is positioned on anything other than [OK]
    else
      # If right directional button is pushed
      if Input.repeat?(Input::RIGHT)
        # If directional button pressed down is not a repeat, or
        # cursor is not positioned on the right edge
        if Input.trigger?(Input::RIGHT) or
           @index / 45 < 3 or @index % 5 < 4
          # Move cursor to right
          $game_system.se_play($data_system.cursor_se)
          if @index % 5 < 4
            @index += 1
          else
            @index += 45 - 4
          end
          if @index >= 90
            @index -= 90
          end
        end
      end
      # If left directional button is pushed
      if Input.repeat?(Input::LEFT)
        # If directional button pressed down is not a repeat, or
        # cursor is not positioned on the left edge
        if Input.trigger?(Input::LEFT) or
           @index / 45 > 0 or @index % 5 > 0
          # Move cursor to left
          $game_system.se_play($data_system.cursor_se)
          if @index % 5 > 0
            @index -= 1
          else
            @index -= 45 - 4
          end
          if @index < 0
            @index += 90
          end
        end
      end
      # If down directional button is pushed
      if Input.repeat?(Input::DOWN)
        # Move cursor down
        $game_system.se_play($data_system.cursor_se)
        if @index % 45 < 40
          @index += 5
        else
          @index += 90 - 40
        end
      end
      # If up directional button is pushed
      if Input.repeat?(Input::UP)
        # If directional button pressed down is not a repeat, or
        # cursor is not positioned on the upper edge
        if Input.trigger?(Input::UP) or @index % 45 >= 5
          # Move cursor up
          $game_system.se_play($data_system.cursor_se)
          if @index % 45 >= 5
            @index -= 5
          else
            @index += 90
          end
        end
      end
      # If L or R button was pressed
      if Input.repeat?(Input::L) or Input.repeat?(Input::R)
        # Move capital / small
        $game_system.se_play($data_system.cursor_se)
        if @index < 45
          @index += 45
        else
          @index -= 45
        end
      end
    end
    update_cursor_rect
  end
end
#==============================================================================
# ** Window_InputNumber
#------------------------------------------------------------------------------
#  This window is for inputting numbers, and is used within the
#  message window.
#==============================================================================

class Window_InputNumber < Window_Base
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     digits_max : digit count
  #--------------------------------------------------------------------------
  def initialize(digits_max)
    @digits_max = digits_max
    @number = 0
    # Calculate cursor width from number width (0-9 equal width and postulate)
    dummy_bitmap = Bitmap.new(32, 32)
    @cursor_width = dummy_bitmap.text_size("0").width + 8
    dummy_bitmap.dispose
    super(0, 0, @cursor_width * @digits_max + 32, 64)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.z += 9999
    self.opacity = 0
    @index = 0
    refresh
    update_cursor_rect
  end
  #--------------------------------------------------------------------------
  # * Get Number
  #--------------------------------------------------------------------------
  def number
    return @number
  end
  #--------------------------------------------------------------------------
  # * Set Number
  #     number : new number
  #--------------------------------------------------------------------------
  def number=(number)
    @number = [[number, 0].max, 10 ** @digits_max - 1].min
    refresh
  end
  #--------------------------------------------------------------------------
  # * Cursor Rectangle Update
  #--------------------------------------------------------------------------
  def update_cursor_rect
    self.cursor_rect.set(@index * @cursor_width, 0, @cursor_width, 32)
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    super
    # If up or down directional button was pressed
    if Input.repeat?(Input::UP) or Input.repeat?(Input::DOWN)
      $game_system.se_play($data_system.cursor_se)
      # Get current place number and change it to 0
      place = 10 ** (@digits_max - 1 - @index)
      n = @number / place % 10
      @number -= n * place
      # If up add 1, if down substract 1
      n = (n + 1) % 10 if Input.repeat?(Input::UP)
      n = (n + 9) % 10 if Input.repeat?(Input::DOWN)
      # Reset current place number
      @number += n * place
      refresh
    end
    # Cursor right
    if Input.repeat?(Input::RIGHT)
      if @digits_max >= 2
        $game_system.se_play($data_system.cursor_se)
        @index = (@index + 1) % @digits_max
      end
    end
    # Cursor left
    if Input.repeat?(Input::LEFT)
      if @digits_max >= 2
        $game_system.se_play($data_system.cursor_se)
        @index = (@index + @digits_max - 1) % @digits_max
      end
    end
    update_cursor_rect
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    self.contents.clear
    self.contents.font.color = normal_color
    s = sprintf("%0*d", @digits_max, @number)
    for i in 0...@digits_max
      self.contents.draw_text(i * @cursor_width + 4, 0, 32, 32, s[i,1])
    end
  end
end
#==============================================================================
# ** Window_Message
#------------------------------------------------------------------------------
#  This message window is used to display text.
#==============================================================================

class Window_Message < Window_Selectable
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    super(80, 304, 480, 160)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.visible = false
    self.z = 9998
    @fade_in = false
    @fade_out = false
    @contents_showing = false
    @cursor_width = 0
    self.active = false
    self.index = -1
  end
  #--------------------------------------------------------------------------
  # * Dispose
  #--------------------------------------------------------------------------
  def dispose
    terminate_message
    $game_temp.message_window_showing = false
    if @input_number_window != nil
      @input_number_window.dispose
    end
    super
  end
  #--------------------------------------------------------------------------
  # * Terminate Message
  #--------------------------------------------------------------------------
  def terminate_message
    self.active = false
    self.pause = false
    self.index = -1
    self.contents.clear
    # Clear showing flag
    @contents_showing = false
    # Call message callback
    if $game_temp.message_proc != nil
      $game_temp.message_proc.call
    end
    # Clear variables related to text, choices, and number input
    $game_temp.message_text = nil
    $game_temp.message_proc = nil
    $game_temp.choice_start = 99
    $game_temp.choice_max = 0
    $game_temp.choice_cancel_type = 0
    $game_temp.choice_proc = nil
    $game_temp.num_input_start = 99
    $game_temp.num_input_variable_id = 0
    $game_temp.num_input_digits_max = 0
    # Open gold window
    if @gold_window != nil
      @gold_window.dispose
      @gold_window = nil
    end
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    self.contents.clear
    self.contents.font.color = normal_color
    x = y = 0
    @cursor_width = 0
    # Indent if choice
    if $game_temp.choice_start == 0
      x = 8
    end
    # If waiting for a message to be displayed
    if $game_temp.message_text != nil
      text = $game_temp.message_text
      # Control text processing
      begin
        last_text = text.clone
        text.gsub!(/\\[Vv]\[([0-9]+)\]/) { $game_variables[$1.to_i] }
      end until text == last_text
      text.gsub!(/\\[Nn]\[([0-9]+)\]/) do
        $game_actors[$1.to_i] != nil ? $game_actors[$1.to_i].name : ""
      end
      # Change "\\\\" to "\000" for convenience
      text.gsub!(/\\\\/) { "\000" }
      # Change "\\C" to "\001" and "\\G" to "\002"
      text.gsub!(/\\[Cc]\[([0-9]+)\]/) { "\001[#{$1}]" }
      text.gsub!(/\\[Gg]/) { "\002" }
      # Get 1 text character in c (loop until unable to get text)
      while ((c = text.slice!(/./m)) != nil)
        # If \\
        if c == "\000"
          # Return to original text
          c = "\\"
        end
        # If \C[n]
        if c == "\001"
          # Change text color
          text.sub!(/\[([0-9]+)\]/, "")
          color = $1.to_i
          if color >= 0 and color <= 7
            self.contents.font.color = text_color(color)
          end
          # go to next text
          next
        end
        # If \G
        if c == "\002"
          # Make gold window
          if @gold_window == nil
            @gold_window = Window_Gold.new
            @gold_window.x = 560 - @gold_window.width
            if $game_temp.in_battle
              @gold_window.y = 192
            else
              @gold_window.y = self.y >= 128 ? 32 : 384
            end
            @gold_window.opacity = self.opacity
            @gold_window.back_opacity = self.back_opacity
          end
          # go to next text
          next
        end
        # If new line text
        if c == "\n"
          # Update cursor width if choice
          if y >= $game_temp.choice_start
            @cursor_width = [@cursor_width, x].max
          end
          # Add 1 to y
          y += 1
          x = 0
          # Indent if choice
          if y >= $game_temp.choice_start
            x = 8
          end
          # go to next text
          next
        end
        # Draw text
        self.contents.draw_text(4 + x, 32 * y, 40, 32, c)
        # Add x to drawn text width
        x += self.contents.text_size(c).width
      end
    end
    # If choice
    if $game_temp.choice_max > 0
      @item_max = $game_temp.choice_max
      self.active = true
      self.index = 0
    end
    # If number input
    if $game_temp.num_input_variable_id > 0
      digits_max = $game_temp.num_input_digits_max
      number = $game_variables[$game_temp.num_input_variable_id]
      @input_number_window = Window_InputNumber.new(digits_max)
      @input_number_window.number = number
      @input_number_window.x = self.x + 8
      @input_number_window.y = self.y + $game_temp.num_input_start * 32
    end
  end
  #--------------------------------------------------------------------------
  # * Set Window Position and Opacity Level
  #--------------------------------------------------------------------------
  def reset_window
    if $game_temp.in_battle
      self.y = 16
    else
      case $game_system.message_position
      when 0  # up
        self.y = 16
      when 1  # middle
        self.y = 160
      when 2  # down
        self.y = 304
      end
    end
    if $game_system.message_frame == 0
      self.opacity = 255
    else
      self.opacity = 0
    end
    self.back_opacity = 160
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    super
    # If fade in
    if @fade_in
      self.contents_opacity += 24
      if @input_number_window != nil
        @input_number_window.contents_opacity += 24
      end
      if self.contents_opacity == 255
        @fade_in = false
      end
      return
    end
    # If inputting number
    if @input_number_window != nil
      @input_number_window.update
      # Confirm
      if Input.trigger?(Input::C)
        $game_system.se_play($data_system.decision_se)
        $game_variables[$game_temp.num_input_variable_id] =
          @input_number_window.number
        $game_map.need_refresh = true
        # Dispose of number input window
        @input_number_window.dispose
        @input_number_window = nil
        terminate_message
      end
      return
    end
    # If message is being displayed
    if @contents_showing
      # If choice isn't being displayed, show pause sign
      if $game_temp.choice_max == 0
        self.pause = true
      end
      # Cancel
      if Input.trigger?(Input::B)
        if $game_temp.choice_max > 0 and $game_temp.choice_cancel_type > 0
          $game_system.se_play($data_system.cancel_se)
          $game_temp.choice_proc.call($game_temp.choice_cancel_type - 1)
          terminate_message
        end
      end
      # Confirm
      if Input.repeat?(Input::C)
        if $game_temp.choice_max > 0
          $game_system.se_play($data_system.decision_se)
          $game_temp.choice_proc.call(self.index)
        end
        terminate_message
      end
      return
    end
    # If display wait message or choice exists when not fading out
    if @fade_out == false and $game_temp.message_text != nil
      @contents_showing = true
      $game_temp.message_window_showing = true
      reset_window
      refresh
      Graphics.frame_reset
      self.visible = true
      self.contents_opacity = 0
      if @input_number_window != nil
        @input_number_window.contents_opacity = 0
      end
      @fade_in = true
      return
    end
    # If message which should be displayed is not shown, but window is visible
    if self.visible
      @fade_out = true
      self.opacity -= 48
      if self.opacity == 0
        self.visible = false
        @fade_out = false
        $game_temp.message_window_showing = false
      end
      return
    end
  end
  #--------------------------------------------------------------------------
  # * Cursor Rectangle Update
  #--------------------------------------------------------------------------
  def update_cursor_rect
    if @index >= 0
      n = $game_temp.choice_start + @index
      self.cursor_rect.set(8, n * 32, @cursor_width, 32)
    else
      self.cursor_rect.empty
    end
  end
end
#==============================================================================
# ** Window_PartyCommand
#------------------------------------------------------------------------------
#  This window is used to select whether to fight or escape on the battle
#  screen.
#==============================================================================

class Window_PartyCommand < Window_Selectable
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    super(0, 0, 640, 64)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.back_opacity = 160
    @commands = ["Fight", "Escape"]
    @item_max = 2
    @column_max = 2
    draw_item(0, normal_color)
    draw_item(1, $game_temp.battle_can_escape ? normal_color : disabled_color)
    self.active = false
    self.visible = false
    self.index = 0
  end
  #--------------------------------------------------------------------------
  # * Draw Item
  #     index : item number
  #     color : text character color
  #--------------------------------------------------------------------------
  def draw_item(index, color)
    self.contents.font.color = color
    rect = Rect.new(160 + index * 160 + 4, 0, 128 - 10, 32)
    self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
    self.contents.draw_text(rect, @commands[index], 1)
  end
  #--------------------------------------------------------------------------
  # * Cursor Rectangle Update
  #--------------------------------------------------------------------------
  def update_cursor_rect
    self.cursor_rect.set(160 + index * 160, 0, 128, 32)
  end
end
#==============================================================================
# ** Window_BattleStatus
#------------------------------------------------------------------------------
#  This window displays the status of all party members on the battle screen.
#==============================================================================

class Window_BattleStatus < Window_Base
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    super(0, 320, 640, 160)
    self.contents = Bitmap.new(width - 32, height - 32)
    @level_up_flags = [false, false, false, false]
    refresh
  end
  #--------------------------------------------------------------------------
  # * Dispose
  #--------------------------------------------------------------------------
  def dispose
    super
  end
  #--------------------------------------------------------------------------
  # * Set Level Up Flag
  #     actor_index : actor index
  #--------------------------------------------------------------------------
  def level_up(actor_index)
    @level_up_flags[actor_index] = true
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    self.contents.clear
    @item_max = $game_party.actors.size
    for i in 0...$game_party.actors.size
      actor = $game_party.actors[i]
      actor_x = i * 160 + 4
      draw_actor_name(actor, actor_x, 0)
      draw_actor_hp(actor, actor_x, 32, 120)
      draw_actor_sp(actor, actor_x, 64, 120)
      if @level_up_flags[i]
        self.contents.font.color = normal_color
        self.contents.draw_text(actor_x, 96, 120, 32, "LEVEL UP!")
      else
        draw_actor_state(actor, actor_x, 96)
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    super
    # Slightly lower opacity level during main phase
    if $game_temp.battle_main_phase
      self.contents_opacity -= 4 if self.contents_opacity > 191
    else
      self.contents_opacity += 4 if self.contents_opacity < 255
    end
  end
end
#==============================================================================
# ** Window_BattleResult
#------------------------------------------------------------------------------
#  This window displays amount of gold and EXP acquired at the end of a battle.
#==============================================================================

class Window_BattleResult < Window_Base
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     exp       : EXP
  #     gold      : amount of gold
  #     treasures : treasures
  #--------------------------------------------------------------------------
  def initialize(exp, gold, treasures)
    @exp = exp
    @gold = gold
    @treasures = treasures
    super(160, 0, 320, @treasures.size * 32 + 64)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.y = 160 - height / 2
    self.back_opacity = 160
    self.visible = false
    refresh
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    self.contents.clear
    x = 4
    self.contents.font.color = normal_color
    cx = contents.text_size(@exp.to_s).width
    self.contents.draw_text(x, 0, cx, 32, @exp.to_s)
    x += cx + 4
    self.contents.font.color = system_color
    cx = contents.text_size("EXP").width
    self.contents.draw_text(x, 0, 64, 32, "EXP")
    x += cx + 16
    self.contents.font.color = normal_color
    cx = contents.text_size(@gold.to_s).width
    self.contents.draw_text(x, 0, cx, 32, @gold.to_s)
    x += cx + 4
    self.contents.font.color = system_color
    self.contents.draw_text(x, 0, 128, 32, $data_system.words.gold)
    y = 32
    for item in @treasures
      draw_item_name(item, 4, y)
      y += 32
    end
  end
end
#==============================================================================
# ** Window_DebugLeft
#------------------------------------------------------------------------------
#  This window designates switch and variable blocks on the debug screen.
#==============================================================================

class Window_DebugLeft < Window_Selectable
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    super(0, 0, 192, 480)
    self.index = 0
    refresh
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    @switch_max = ($data_system.switches.size - 1 + 9) / 10
    @variable_max = ($data_system.variables.size - 1 + 9) / 10
    @item_max = @switch_max + @variable_max
    self.contents = Bitmap.new(width - 32, @item_max * 32)
    for i in 0...@switch_max
      text = sprintf("S [%04d-%04d]", i*10+1, i*10+10)
      self.contents.draw_text(4, i * 32, 152, 32, text)
    end
    for i in 0...@variable_max
      text = sprintf("V [%04d-%04d]", i*10+1, i*10+10)
      self.contents.draw_text(4, (@switch_max + i) * 32, 152, 32, text)
    end
  end
  #--------------------------------------------------------------------------
  # * Get Mode
  #--------------------------------------------------------------------------
  def mode
    if self.index < @switch_max
      return 0
    else
      return 1
    end
  end
  #--------------------------------------------------------------------------
  # * Get ID Shown on Top
  #--------------------------------------------------------------------------
  def top_id
    if self.index < @switch_max
      return self.index * 10 + 1
    else
      return (self.index - @switch_max) * 10 + 1
    end
  end
end
#==============================================================================
# ** Window_DebugRight
#------------------------------------------------------------------------------
#  This window displays switches and variables separately on the debug screen.
#==============================================================================

class Window_DebugRight < Window_Selectable
  #--------------------------------------------------------------------------
  # * Public Instance Variables
  #--------------------------------------------------------------------------
  attr_reader   :mode                     # mode (0: switch, 1: variable)
  attr_reader   :top_id                   # ID shown on top
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    super(192, 0, 448, 352)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.index = -1
    self.active = false
    @item_max = 10
    @mode = 0
    @top_id = 1
    refresh
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    self.contents.clear
    for i in 0..9
      if @mode == 0
        name = $data_system.switches[@top_id+i]
        status = $game_switches[@top_id+i] ? "[ON]" : "[OFF]"
      else
        name = $data_system.variables[@top_id+i]
        status = $game_variables[@top_id+i].to_s
      end
      if name == nil
        name = ''
      end
      id_text = sprintf("%04d:", @top_id+i)
      width = self.contents.text_size(id_text).width
      self.contents.draw_text(4, i * 32, width, 32, id_text)
      self.contents.draw_text(12 + width, i * 32, 296 - width, 32, name)
      self.contents.draw_text(312, i * 32, 100, 32, status, 2)
    end
  end
  #--------------------------------------------------------------------------
  # * Set Mode
  #     id : new mode
  #--------------------------------------------------------------------------
  def mode=(mode)
    if @mode != mode
      @mode = mode
      refresh
    end
  end
  #--------------------------------------------------------------------------
  # * Set ID Shown on Top
  #     id : new ID
  #--------------------------------------------------------------------------
  def top_id=(id)
    if @top_id != id
      @top_id = id
      refresh
    end
  end
end
#==============================================================================
# ** Arrow_Base
#------------------------------------------------------------------------------
#  This sprite is used as an arrow cursor for the battle screen. This class
#  is used as a superclass for the Arrow_Enemy and Arrow_Actor classes.
#==============================================================================

class Arrow_Base < Sprite
  #--------------------------------------------------------------------------
  # * Public Instance Variables
  #--------------------------------------------------------------------------
  attr_reader   :index                    # cursor position
  attr_reader   :help_window              # help window
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     viewport : viewport
  #--------------------------------------------------------------------------
  def initialize(viewport)
    super(viewport)
    self.bitmap = RPG::Cache.windowskin($game_system.windowskin_name)
    self.ox = 16
    self.oy = 64
    self.z = 2500
    @blink_count = 0
    @index = 0
    @help_window = nil
    update
  end
  #--------------------------------------------------------------------------
  # * Set Cursor Position
  #     index : new cursor position
  #--------------------------------------------------------------------------
  def index=(index)
    @index = index
    update
  end
  #--------------------------------------------------------------------------
  # * Set Help Window
  #     help_window : new help window
  #--------------------------------------------------------------------------
  def help_window=(help_window)
    @help_window = help_window
    # Update help text (update_help is defined by the subclasses)
    if @help_window != nil
      update_help
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # Update blink count
    @blink_count = (@blink_count + 1) % 8
    # Set forwarding origin rectangle
    if @blink_count < 4
      self.src_rect.set(128, 96, 32, 32)
    else
      self.src_rect.set(160, 96, 32, 32)
    end
    # Update help text (update_help is defined by the subclasses)
    if @help_window != nil
      update_help
    end
  end
end
#==============================================================================
# ** Arrow_Enemy
#------------------------------------------------------------------------------
#  This arrow cursor is used to choose enemies. This class inherits from the 
#  Arrow_Base class.
#==============================================================================

class Arrow_Enemy < Arrow_Base
  #--------------------------------------------------------------------------
  # * Get Enemy Indicated by Cursor
  #--------------------------------------------------------------------------
  def enemy
    return $game_troop.enemies[@index]
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    super
    # Skip if indicating a nonexistant enemy
    $game_troop.enemies.size.times do
      break if self.enemy.exist?
      @index += 1
      @index %= $game_troop.enemies.size
    end
    # Cursor right
    if Input.repeat?(Input::RIGHT)
      $game_system.se_play($data_system.cursor_se)
      $game_troop.enemies.size.times do
        @index += 1
        @index %= $game_troop.enemies.size
        break if self.enemy.exist?
      end
    end
    # Cursor left
    if Input.repeat?(Input::LEFT)
      $game_system.se_play($data_system.cursor_se)
      $game_troop.enemies.size.times do
        @index += $game_troop.enemies.size - 1
        @index %= $game_troop.enemies.size
        break if self.enemy.exist?
      end
    end
    # Set sprite coordinates
    if self.enemy != nil
      self.x = self.enemy.screen_x
      self.y = self.enemy.screen_y
    end
  end
  #--------------------------------------------------------------------------
  # * Help Text Update
  #--------------------------------------------------------------------------
  def update_help
    # Display enemy name and state in the help window
    @help_window.set_enemy(self.enemy)
  end
end
#==============================================================================
# ** Arrow_Actor
#------------------------------------------------------------------------------
#  This arrow cursor is used to choose an actor. This class inherits from the
#  Arrow_Base class.
#==============================================================================

class Arrow_Actor < Arrow_Base
  #--------------------------------------------------------------------------
  # * Get Actor Indicated by Cursor
  #--------------------------------------------------------------------------
  def actor
    return $game_party.actors[@index]
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    super
    # Cursor right
    if Input.repeat?(Input::RIGHT)
      $game_system.se_play($data_system.cursor_se)
      @index += 1
      @index %= $game_party.actors.size
    end
    # Cursor left
    if Input.repeat?(Input::LEFT)
      $game_system.se_play($data_system.cursor_se)
      @index += $game_party.actors.size - 1
      @index %= $game_party.actors.size
    end
    # Set sprite coordinates
    if self.actor != nil
      self.x = self.actor.screen_x
      self.y = self.actor.screen_y
    end
  end
  #--------------------------------------------------------------------------
  # * Help Text Update
  #--------------------------------------------------------------------------
  def update_help
    # Display actor status in help window
    @help_window.set_actor(self.actor)
  end
end
#==============================================================================
# ** Interpreter 
#------------------------------------------------------------------------------
#  This interpreter runs event commands. This class is used within the
#  Game_System class and the Game_Event class.
#==============================================================================

class Interpreter
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     depth : nest depth
  #     main  : main flag
  #--------------------------------------------------------------------------
  def initialize(depth = 0, main = false)
    @depth = depth
    @main = main
    # Depth goes up to level 100
    if depth > 100
      print("Common event call has exceeded maximum limit.")
      exit
    end
    # Clear inner situation of interpreter
    clear
  end
  #--------------------------------------------------------------------------
  # * Clear
  #--------------------------------------------------------------------------
  def clear
    @map_id = 0                       # map ID when starting up
    @event_id = 0                     # event ID
    @message_waiting = false          # waiting for message to end
    @move_route_waiting = false       # waiting for move completion
    @button_input_variable_id = 0     # button input variable ID
    @wait_count = 0                   # wait count
    @child_interpreter = nil          # child interpreter
    @branch = {}                      # branch data
  end
  #--------------------------------------------------------------------------
  # * Event Setup
  #     list     : list of event commands
  #     event_id : event ID
  #--------------------------------------------------------------------------
  def setup(list, event_id)
    # Clear inner situation of interpreter
    clear
    # Remember map ID
    @map_id = $game_map.map_id
    # Remember event ID
    @event_id = event_id
    # Remember list of event commands
    @list = list
    # Initialize index
    @index = 0
    # Clear branch data hash
    @branch.clear
  end
  #--------------------------------------------------------------------------
  # * Determine if Running
  #--------------------------------------------------------------------------
  def running?
    return @list != nil
  end
  #--------------------------------------------------------------------------
  # * Starting Event Setup
  #--------------------------------------------------------------------------
  def setup_starting_event
    # Refresh map if necessary
    if $game_map.need_refresh
      $game_map.refresh
    end
    # If common event call is reserved
    if $game_temp.common_event_id > 0
      # Set up event
      setup($data_common_events[$game_temp.common_event_id].list, 0)
      # Release reservation
      $game_temp.common_event_id = 0
      return
    end
    # Loop (map events)
    for event in $game_map.events.values
      # If running event is found
      if event.starting
        # If not auto run
        if event.trigger < 3
          # Clear starting flag
          event.clear_starting
          # Lock
          event.lock
        end
        # Set up event
        setup(event.list, event.id)
        return
      end
    end
    # Loop (common events)
    for common_event in $data_common_events.compact
      # If trigger is auto run, and condition switch is ON
      if common_event.trigger == 1 and
         $game_switches[common_event.switch_id] == true
        # Set up event
        setup(common_event.list, 0)
        return
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # Initialize loop count
    @loop_count = 0
    # Loop
    loop do
      # Add 1 to loop count
      @loop_count += 1
      # If 100 event commands ran
      if @loop_count > 100
        # Call Graphics.update for freeze prevention
        Graphics.update
        @loop_count = 0
      end
      # If map is different than event startup time
      if $game_map.map_id != @map_id
        # Change event ID to 0
        @event_id = 0
      end
      # If a child interpreter exists
      if @child_interpreter != nil
        # Update child interpreter
        @child_interpreter.update
        # If child interpreter is finished running
        unless @child_interpreter.running?
          # Delete child interpreter
          @child_interpreter = nil
        end
        # If child interpreter still exists
        if @child_interpreter != nil
          return
        end
      end
      # If waiting for message to end
      if @message_waiting
        return
      end
      # If waiting for move to end
      if @move_route_waiting
        # If player is forcing move route
        if $game_player.move_route_forcing
          return
        end
        # Loop (map events)
        for event in $game_map.events.values
          # If this event is forcing move route
          if event.move_route_forcing
            return
          end
        end
        # Clear move end waiting flag
        @move_route_waiting = false
      end
      # If waiting for button input
      if @button_input_variable_id > 0
        # Run button input processing
        input_button
        return
      end
      # If waiting
      if @wait_count > 0
        # Decrease wait count
        @wait_count -= 1
        return
      end
      # If an action forcing battler exists
      if $game_temp.forcing_battler != nil
        return
      end
      # If a call flag is set for each type of screen
      if $game_temp.battle_calling or
         $game_temp.shop_calling or
         $game_temp.name_calling or
         $game_temp.menu_calling or
         $game_temp.save_calling or
         $game_temp.gameover
        return
      end
      # If list of event commands is empty
      if @list == nil
        # If main map event
        if @main
          # Set up starting event
          setup_starting_event
        end
        # If nothing was set up
        if @list == nil
          return
        end
      end
      # If return value is false when trying to execute event command
      if execute_command == false
        return
      end
      # Advance index
      @index += 1
    end
  end
  #--------------------------------------------------------------------------
  # * Button Input
  #--------------------------------------------------------------------------
  def input_button
    # Determine pressed button
    n = 0
    for i in 1..18
      if Input.trigger?(i)
        n = i
      end
    end
    # If button was pressed
    if n > 0
      # Change value of variables
      $game_variables[@button_input_variable_id] = n
      $game_map.need_refresh = true
      # End button input
      @button_input_variable_id = 0
    end
  end
  #--------------------------------------------------------------------------
  # * Setup Choices
  #--------------------------------------------------------------------------
  def setup_choices(parameters)
    # Set choice item count to choice_max
    $game_temp.choice_max = parameters[0].size
    # Set choice to message_text
    for text in parameters[0]
      $game_temp.message_text += text + "\n"
    end
    # Set cancel processing
    $game_temp.choice_cancel_type = parameters[1]
    # Set callback
    current_indent = @list[@index].indent
    $game_temp.choice_proc = Proc.new { |n| @branch[current_indent] = n }
  end
  #--------------------------------------------------------------------------
  # * Actor Iterator (consider all party members)
  #     parameter : if 1 or more, ID; if 0, all
  #--------------------------------------------------------------------------
  def iterate_actor(parameter)
    # If entire party
    if parameter == 0
      # Loop for entire party
      for actor in $game_party.actors
        # Evaluate block
        yield actor
      end
    # If single actor
    else
      # Get actor
      actor = $game_actors[parameter]
      # Evaluate block
      yield actor if actor != nil
    end
  end
  #--------------------------------------------------------------------------
  # * Enemy Iterator (consider all troop members)
  #     parameter : If 0 or above, index; if -1, all
  #--------------------------------------------------------------------------
  def iterate_enemy(parameter)
    # If entire troop
    if parameter == -1
      # Loop for entire troop
      for enemy in $game_troop.enemies
        # Evaluate block
        yield enemy
      end
    # If single enemy
    else
      # Get enemy
      enemy = $game_troop.enemies[parameter]
      # Evaluate block
      yield enemy if enemy != nil
    end
  end
  #--------------------------------------------------------------------------
  # * Battler Iterator (consider entire troop and entire party)
  #     parameter1 : If 0, enemy; if 1, actor
  #     parameter2 : If 0 or above, index; if -1, all
  #--------------------------------------------------------------------------
  def iterate_battler(parameter1, parameter2)
    # If enemy
    if parameter1 == 0
      # Call enemy iterator
      iterate_enemy(parameter2) do |enemy|
        yield enemy
      end
    # If actor
    else
      # If entire party
      if parameter2 == -1
        # Loop for entire party
        for actor in $game_party.actors
          # Evaluate block
          yield actor
        end
      # If single actor (N exposed)
      else
        # Get actor
        actor = $game_party.actors[parameter2]
        # Evaluate block
        yield actor if actor != nil
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Event Command Execution
  #--------------------------------------------------------------------------
  def execute_command
    # If last to arrive for list of event commands
    if @index >= @list.size - 1
      # End event
      command_end
      # Continue
      return true
    end
    # Make event command parameters available for reference via @parameters
    @parameters = @list[@index].parameters
    # Branch by command code
    case @list[@index].code
    when 101  # Show Text
      return command_101
    when 102  # Show Choices
      return command_102
    when 402  # When [**]
      return command_402
    when 403  # When Cancel
      return command_403
    when 103  # Input Number
      return command_103
    when 104  # Change Text Options
      return command_104
    when 105  # Button Input Processing
      return command_105
    when 106  # Wait
      return command_106
    when 111  # Conditional Branch
      return command_111
    when 411  # Else
      return command_411
    when 112  # Loop
      return command_112
    when 413  # Repeat Above
      return command_413
    when 113  # Break Loop
      return command_113
    when 115  # Exit Event Processing
      return command_115
    when 116  # Erase Event
      return command_116
    when 117  # Call Common Event
      return command_117
    when 118  # Label
      return command_118
    when 119  # Jump to Label
      return command_119
    when 121  # Control Switches
      return command_121
    when 122  # Control Variables
      return command_122
    when 123  # Control Self Switch
      return command_123
    when 124  # Control Timer
      return command_124
    when 125  # Change Gold
      return command_125
    when 126  # Change Items
      return command_126
    when 127  # Change Weapons
      return command_127
    when 128  # Change Armor
      return command_128
    when 129  # Change Party Member
      return command_129
    when 131  # Change Windowskin
      return command_131
    when 132  # Change Battle BGM
      return command_132
    when 133  # Change Battle End ME
      return command_133
    when 134  # Change Save Access
      return command_134
    when 135  # Change Menu Access
      return command_135
    when 136  # Change Encounter
      return command_136
    when 201  # Transfer Player
      return command_201
    when 202  # Set Event Location
      return command_202
    when 203  # Scroll Map
      return command_203
    when 204  # Change Map Settings
      return command_204
    when 205  # Change Fog Color Tone
      return command_205
    when 206  # Change Fog Opacity
      return command_206
    when 207  # Show Animation
      return command_207
    when 208  # Change Transparent Flag
      return command_208
    when 209  # Set Move Route
      return command_209
    when 210  # Wait for Move's Completion
      return command_210
    when 221  # Prepare for Transition
      return command_221
    when 222  # Execute Transition
      return command_222
    when 223  # Change Screen Color Tone
      return command_223
    when 224  # Screen Flash
      return command_224
    when 225  # Screen Shake
      return command_225
    when 231  # Show Picture
      return command_231
    when 232  # Move Picture
      return command_232
    when 233  # Rotate Picture
      return command_233
    when 234  # Change Picture Color Tone
      return command_234
    when 235  # Erase Picture
      return command_235
    when 236  # Set Weather Effects
      return command_236
    when 241  # Play BGM
      return command_241
    when 242  # Fade Out BGM
      return command_242
    when 245  # Play BGS
      return command_245
    when 246  # Fade Out BGS
      return command_246
    when 247  # Memorize BGM/BGS
      return command_247
    when 248  # Restore BGM/BGS
      return command_248
    when 249  # Play ME
      return command_249
    when 250  # Play SE
      return command_250
    when 251  # Stop SE
      return command_251
    when 301  # Battle Processing
      return command_301
    when 601  # If Win
      return command_601
    when 602  # If Escape
      return command_602
    when 603  # If Lose
      return command_603
    when 302  # Shop Processing
      return command_302
    when 303  # Name Input Processing
      return command_303
    when 311  # Change HP
      return command_311
    when 312  # Change SP
      return command_312
    when 313  # Change State
      return command_313
    when 314  # Recover All
      return command_314
    when 315  # Change EXP
      return command_315
    when 316  # Change Level
      return command_316
    when 317  # Change Parameters
      return command_317
    when 318  # Change Skills
      return command_318
    when 319  # Change Equipment
      return command_319
    when 320  # Change Actor Name
      return command_320
    when 321  # Change Actor Class
      return command_321
    when 322  # Change Actor Graphic
      return command_322
    when 331  # Change Enemy HP
      return command_331
    when 332  # Change Enemy SP
      return command_332
    when 333  # Change Enemy State
      return command_333
    when 334  # Enemy Recover All
      return command_334
    when 335  # Enemy Appearance
      return command_335
    when 336  # Enemy Transform
      return command_336
    when 337  # Show Battle Animation
      return command_337
    when 338  # Deal Damage
      return command_338
    when 339  # Force Action
      return command_339
    when 340  # Abort Battle
      return command_340
    when 351  # Call Menu Screen
      return command_351
    when 352  # Call Save Screen
      return command_352
    when 353  # Game Over
      return command_353
    when 354  # Return to Title Screen
      return command_354
    when 355  # Script
      return command_355
    else      # Other
      return true
    end
  end
  #--------------------------------------------------------------------------
  # * End Event
  #--------------------------------------------------------------------------
  def command_end
    # Clear list of event commands
    @list = nil
    # If main map event and event ID are valid
    if @main and @event_id > 0
      # Unlock event
      $game_map.events[@event_id].unlock
    end
  end
  #--------------------------------------------------------------------------
  # * Command Skip
  #--------------------------------------------------------------------------
  def command_skip
    # Get indent
    indent = @list[@index].indent
    # Loop
    loop do
      # If next event command is at the same level as indent
      if @list[@index+1].indent == indent
        # Continue
        return true
      end
      # Advance index
      @index += 1
    end
  end
  #--------------------------------------------------------------------------
  # * Get Character
  #     parameter : parameter
  #--------------------------------------------------------------------------
  def get_character(parameter)
    # Branch by parameter
    case parameter
    when -1  # player
      return $game_player
    when 0  # this event
      events = $game_map.events
      return events == nil ? nil : events[@event_id]
    else  # specific event
      events = $game_map.events
      return events == nil ? nil : events[parameter]
    end
  end
  #--------------------------------------------------------------------------
  # * Calculate Operated Value
  #     operation    : operation
  #     operand_type : operand type (0: invariable 1: variable)
  #     operand      : operand (number or variable ID)
  #--------------------------------------------------------------------------
  def operate_value(operation, operand_type, operand)
    # Get operand
    if operand_type == 0
      value = operand
    else
      value = $game_variables[operand]
    end
    # Reverse sign of integer if operation is [decrease]
    if operation == 1
      value = -value
    end
    # Return value
    return value
  end
  #--------------------------------------------------------------------------
  # * Show Text
  #--------------------------------------------------------------------------
  def command_101
    # If other text has been set to message_text
    if $game_temp.message_text != nil
      # End
      return false
    end
    # Set message end waiting flag and callback
    @message_waiting = true
    $game_temp.message_proc = Proc.new { @message_waiting = false }
    # Set message text on first line
    $game_temp.message_text = @list[@index].parameters[0] + "\n"
    line_count = 1
    # Loop
    loop do
      # If next event command text is on the second line or after
      if @list[@index+1].code == 401
        # Add the second line or after to message_text
        $game_temp.message_text += @list[@index+1].parameters[0] + "\n"
        line_count += 1
      # If event command is not on the second line or after
      else
        # If next event command is show choices
        if @list[@index+1].code == 102
          # If choices fit on screen
          if @list[@index+1].parameters[0].size <= 4 - line_count
            # Advance index
            @index += 1
            # Choices setup
            $game_temp.choice_start = line_count
            setup_choices(@list[@index].parameters)
          end
        # If next event command is input number
        elsif @list[@index+1].code == 103
          # If number input window fits on screen
          if line_count < 4
            # Advance index
            @index += 1
            # Number input setup
            $game_temp.num_input_start = line_count
            $game_temp.num_input_variable_id = @list[@index].parameters[0]
            $game_temp.num_input_digits_max = @list[@index].parameters[1]
          end
        end
        # Continue
        return true
      end
      # Advance index
      @index += 1
    end
  end
  #--------------------------------------------------------------------------
  # * Show Choices
  #--------------------------------------------------------------------------
  def command_102
    # If text has been set to message_text
    if $game_temp.message_text != nil
      # End
      return false
    end
    # Set message end waiting flag and callback
    @message_waiting = true
    $game_temp.message_proc = Proc.new { @message_waiting = false }
    # Choices setup
    $game_temp.message_text = ""
    $game_temp.choice_start = 0
    setup_choices(@parameters)
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * When [**]
  #--------------------------------------------------------------------------
  def command_402
    # If fitting choices are selected
    if @branch[@list[@index].indent] == @parameters[0]
      # Delete branch data
      @branch.delete(@list[@index].indent)
      # Continue
      return true
    end
    # If it doesn't meet the condition: command skip
    return command_skip
  end
  #--------------------------------------------------------------------------
  # * When Cancel
  #--------------------------------------------------------------------------
  def command_403
    # If choices are cancelled
    if @branch[@list[@index].indent] == 4
      # Delete branch data
      @branch.delete(@list[@index].indent)
      # Continue
      return true
    end
    # If it doen't meet the condition: command skip
    return command_skip
  end
  #--------------------------------------------------------------------------
  # * Input Number
  #--------------------------------------------------------------------------
  def command_103
    # If text has been set to message_text
    if $game_temp.message_text != nil
      # End
      return false
    end
    # Set message end waiting flag and callback
    @message_waiting = true
    $game_temp.message_proc = Proc.new { @message_waiting = false }
    # Number input setup
    $game_temp.message_text = ""
    $game_temp.num_input_start = 0
    $game_temp.num_input_variable_id = @parameters[0]
    $game_temp.num_input_digits_max = @parameters[1]
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Text Options
  #--------------------------------------------------------------------------
  def command_104
    # If message is showing
    if $game_temp.message_window_showing
      # End
      return false
    end
    # Change each option
    $game_system.message_position = @parameters[0]
    $game_system.message_frame = @parameters[1]
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Button Input Processing
  #--------------------------------------------------------------------------
  def command_105
    # Set variable ID for button input
    @button_input_variable_id = @parameters[0]
    # Advance index
    @index += 1
    # End
    return false
  end
  #--------------------------------------------------------------------------
  # * Wait
  #--------------------------------------------------------------------------
  def command_106
    # Set wait count
    @wait_count = @parameters[0] * 2
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Conditional Branch
  #--------------------------------------------------------------------------
  def command_111
    # Initialize local variable: result
    result = false
    case @parameters[0]
    when 0  # switch
      result = ($game_switches[@parameters[1]] == (@parameters[2] == 0))
    when 1  # variable
      value1 = $game_variables[@parameters[1]]
      if @parameters[2] == 0
        value2 = @parameters[3]
      else
        value2 = $game_variables[@parameters[3]]
      end
      case @parameters[4]
      when 0  # value1 is equal to value2
        result = (value1 == value2)
      when 1  # value1 is greater than or equal to value2
        result = (value1 >= value2)
      when 2  # value1 is less than or equal to value2
        result = (value1 <= value2)
      when 3  # value1 is greater than value2
        result = (value1 > value2)
      when 4  # value1 is less than value2
        result = (value1 < value2)
      when 5  # value1 is not equal to value2
        result = (value1 != value2)
      end
    when 2  # self switch
      if @event_id > 0
        key = [$game_map.map_id, @event_id, @parameters[1]]
        if @parameters[2] == 0
          result = ($game_self_switches[key] == true)
        else
          result = ($game_self_switches[key] != true)
        end
      end
    when 3  # timer
      if $game_system.timer_working
        sec = $game_system.timer / Graphics.frame_rate
        if @parameters[2] == 0
          result = (sec >= @parameters[1])
        else
          result = (sec <= @parameters[1])
        end
      end
    when 4  # actor
      actor = $game_actors[@parameters[1]]
      if actor != nil
        case @parameters[2]
        when 0  # in party
          result = ($game_party.actors.include?(actor))
        when 1  # name
          result = (actor.name == @parameters[3])
        when 2  # skill
          result = (actor.skill_learn?(@parameters[3]))
        when 3  # weapon
          result = (actor.weapon_id == @parameters[3])
        when 4  # armor
          result = (actor.armor1_id == @parameters[3] or
                    actor.armor2_id == @parameters[3] or
                    actor.armor3_id == @parameters[3] or
                    actor.armor4_id == @parameters[3])
        when 5  # state
          result = (actor.state?(@parameters[3]))
        end
      end
    when 5  # enemy
      enemy = $game_troop.enemies[@parameters[1]]
      if enemy != nil
        case @parameters[2]
        when 0  # appear
          result = (enemy.exist?)
        when 1  # state
          result = (enemy.state?(@parameters[3]))
        end
      end
    when 6  # character
      character = get_character(@parameters[1])
      if character != nil
        result = (character.direction == @parameters[2])
      end
    when 7  # gold
      if @parameters[2] == 0
        result = ($game_party.gold >= @parameters[1])
      else
        result = ($game_party.gold <= @parameters[1])
      end
    when 8  # item
      result = ($game_party.item_number(@parameters[1]) > 0)
    when 9  # weapon
      result = ($game_party.weapon_number(@parameters[1]) > 0)
    when 10  # armor
      result = ($game_party.armor_number(@parameters[1]) > 0)
    when 11  # button
      result = (Input.press?(@parameters[1]))
    when 12  # script
      begin
        eval(@parameters[1])
      rescue
      end
      result = true
    end
    # Store determinant results in hash
    @branch[@list[@index].indent] = result
    # If determinant results are true
    if @branch[@list[@index].indent] == true
      # Delete branch data
      @branch.delete(@list[@index].indent)
      # Continue
      return true
    end
    # If it doesn't meet the conditions: command skip
    return command_skip
  end
  #--------------------------------------------------------------------------
  # * Else
  #--------------------------------------------------------------------------
  def command_411
    # If determinant results are false
    if @branch[@list[@index].indent] == false
      # Delete branch data
      @branch.delete(@list[@index].indent)
      # Continue
      return true
    end
    # If it doesn't meet the conditions: command skip
    return command_skip
  end
  #--------------------------------------------------------------------------
  # * Loop
  #--------------------------------------------------------------------------
  def command_112
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Repeat Above
  #--------------------------------------------------------------------------
  def command_413
    # Get indent
    indent = @list[@index].indent
    # Loop
    loop do
      # Return index
      @index -= 1
      # If this event command is the same level as indent
      if @list[@index].indent == indent
        # Continue
        return true
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Break Loop
  #--------------------------------------------------------------------------
  def command_113
    # Get indent
    indent = @list[@index].indent
    # Copy index to temporary variables
    temp_index = @index
    # Loop
    loop do
      # Advance index
      temp_index += 1
      # If a fitting loop was not found
      if temp_index >= @list.size-1
        # Continue
        return true
      end
      # If this event command is [repeat above] and indent is shallow
      if @list[temp_index].code == 413 and @list[temp_index].indent < indent
        # Update index
        @index = temp_index
        # Continue
        return true
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Exit Event Processing
  #--------------------------------------------------------------------------
  def command_115
    # End event
    command_end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Erase Event
  #--------------------------------------------------------------------------
  def command_116
    # If event ID is valid
    if @event_id > 0
      # Erase event
      $game_map.events[@event_id].erase
    end
    # Advance index
    @index += 1
    # End
    return false
  end
  #--------------------------------------------------------------------------
  # * Call Common Event
  #--------------------------------------------------------------------------
  def command_117
    # Get common event
    common_event = $data_common_events[@parameters[0]]
    # If common event is valid
    if common_event != nil
      # Make child interpreter
      @child_interpreter = Interpreter.new(@depth + 1)
      @child_interpreter.setup(common_event.list, @event_id)
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Label
  #--------------------------------------------------------------------------
  def command_118
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Jump to Label
  #--------------------------------------------------------------------------
  def command_119
    # Get label name
    label_name = @parameters[0]
    # Initialize temporary variables
    temp_index = 0
    # Loop
    loop do
      # If a fitting label was not found
      if temp_index >= @list.size-1
        # Continue
        return true
      end
      # If this event command is a designated label name
      if @list[temp_index].code == 118 and
         @list[temp_index].parameters[0] == label_name
        # Update index
        @index = temp_index
        # Continue
        return true
      end
      # Advance index
      temp_index += 1
    end
  end
  #--------------------------------------------------------------------------
  # * Control Switches
  #--------------------------------------------------------------------------
  def command_121
    # Loop for group control
    for i in @parameters[0] .. @parameters[1]
      # Change switch
      $game_switches[i] = (@parameters[2] == 0)
    end
    # Refresh map
    $game_map.need_refresh = true
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Control Variables
  #--------------------------------------------------------------------------
  def command_122
    # Initialize value
    value = 0
    # Branch with operand
    case @parameters[3]
    when 0  # invariable
      value = @parameters[4]
    when 1  # variable
      value = $game_variables[@parameters[4]]
    when 2  # random number
      value = @parameters[4] + rand(@parameters[5] - @parameters[4] + 1)
    when 3  # item
      value = $game_party.item_number(@parameters[4])
    when 4  # actor
      actor = $game_actors[@parameters[4]]
      if actor != nil
        case @parameters[5]
        when 0  # level
          value = actor.level
        when 1  # EXP
          value = actor.exp
        when 2  # HP
          value = actor.hp
        when 3  # SP
          value = actor.sp
        when 4  # MaxHP
          value = actor.maxhp
        when 5  # MaxSP
          value = actor.maxsp
        when 6  # strength
          value = actor.str
        when 7  # dexterity
          value = actor.dex
        when 8  # agility
          value = actor.agi
        when 9  # intelligence
          value = actor.int
        when 10  # attack power
          value = actor.atk
        when 11  # physical defense
          value = actor.pdef
        when 12  # magic defense
          value = actor.mdef
        when 13  # evasion
          value = actor.eva
        end
      end
    when 5  # enemy
      enemy = $game_troop.enemies[@parameters[4]]
      if enemy != nil
        case @parameters[5]
        when 0  # HP
          value = enemy.hp
        when 1  # SP
          value = enemy.sp
        when 2  # MaxHP
          value = enemy.maxhp
        when 3  # MaxSP
          value = enemy.maxsp
        when 4  # strength
          value = enemy.str
        when 5  # dexterity
          value = enemy.dex
        when 6  # agility
          value = enemy.agi
        when 7  # intelligence
          value = enemy.int
        when 8  # attack power
          value = enemy.atk
        when 9  # physical defense
          value = enemy.pdef
        when 10  # magic defense
          value = enemy.mdef
        when 11  # evasion correction
          value = enemy.eva
        end
      end
    when 6  # character
      character = get_character(@parameters[4])
      if character != nil
        case @parameters[5]
        when 0  # x-coordinate
          value = character.x
        when 1  # y-coordinate
          value = character.y
        when 2  # direction
          value = character.direction
        when 3  # screen x-coordinate
          value = character.screen_x
        when 4  # screen y-coordinate
          value = character.screen_y
        when 5  # terrain tag
          value = character.terrain_tag
        end
      end
    when 7  # other
      case @parameters[4]
      when 0  # map ID
        value = $game_map.map_id
      when 1  # number of party members
        value = $game_party.actors.size
      when 2  # gold
        value = $game_party.gold
      when 3  # steps
        value = $game_party.steps
      when 4  # play time
        value = Graphics.frame_count / Graphics.frame_rate
      when 5  # timer
        value = $game_system.timer / Graphics.frame_rate
      when 6  # save count
        value = $game_system.save_count
      end
    end
    # Loop for group control
    for i in @parameters[0] .. @parameters[1]
      # Branch with control
      case @parameters[2]
      when 0  # substitute
        $game_variables[i] = value
      when 1  # add
        $game_variables[i] += value
      when 2  # subtract
        $game_variables[i] -= value
      when 3  # multiply
        $game_variables[i] *= value
      when 4  # divide
        if value != 0
          $game_variables[i] /= value
        end
      when 5  # remainder
        if value != 0
          $game_variables[i] %= value
        end
      end
      # Maximum limit check
      if $game_variables[i] > 99999999
        $game_variables[i] = 99999999
      end
      # Minimum limit check
      if $game_variables[i] < -99999999
        $game_variables[i] = -99999999
      end
    end
    # Refresh map
    $game_map.need_refresh = true
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Control Self Switch
  #--------------------------------------------------------------------------
  def command_123
    # If event ID is valid
    if @event_id > 0
      # Make a self switch key
      key = [$game_map.map_id, @event_id, @parameters[0]]
      # Change self switches
      $game_self_switches[key] = (@parameters[1] == 0)
    end
    # Refresh map
    $game_map.need_refresh = true
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Control Timer
  #--------------------------------------------------------------------------
  def command_124
    # If started
    if @parameters[0] == 0
      $game_system.timer = @parameters[1] * Graphics.frame_rate
      $game_system.timer_working = true
    end
    # If stopped
    if @parameters[0] == 1
      $game_system.timer_working = false
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Gold
  #--------------------------------------------------------------------------
  def command_125
    # Get value to operate
    value = operate_value(@parameters[0], @parameters[1], @parameters[2])
    # Increase / decrease amount of gold
    $game_party.gain_gold(value)
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Items
  #--------------------------------------------------------------------------
  def command_126
    # Get value to operate
    value = operate_value(@parameters[1], @parameters[2], @parameters[3])
    # Increase / decrease items
    $game_party.gain_item(@parameters[0], value)
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Weapons
  #--------------------------------------------------------------------------
  def command_127
    # Get value to operate
    value = operate_value(@parameters[1], @parameters[2], @parameters[3])
    # Increase / decrease weapons
    $game_party.gain_weapon(@parameters[0], value)
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Armor
  #--------------------------------------------------------------------------
  def command_128
    # Get value to operate
    value = operate_value(@parameters[1], @parameters[2], @parameters[3])
    # Increase / decrease armor
    $game_party.gain_armor(@parameters[0], value)
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Party Member
  #--------------------------------------------------------------------------
  def command_129
    # Get actor
    actor = $game_actors[@parameters[0]]
    # If actor is valid
    if actor != nil
      # Branch with control
      if @parameters[1] == 0
        if @parameters[2] == 1
          $game_actors[@parameters[0]].setup(@parameters[0])
        end
        $game_party.add_actor(@parameters[0])
      else
        $game_party.remove_actor(@parameters[0])
      end
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Windowskin
  #--------------------------------------------------------------------------
  def command_131
    # Change windowskin file name
    $game_system.windowskin_name = @parameters[0]
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Battle BGM
  #--------------------------------------------------------------------------
  def command_132
    # Change battle BGM
    $game_system.battle_bgm = @parameters[0]
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Battle End ME
  #--------------------------------------------------------------------------
  def command_133
    # Change battle end ME
    $game_system.battle_end_me = @parameters[0]
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Save Access
  #--------------------------------------------------------------------------
  def command_134
    # Change save access flag
    $game_system.save_disabled = (@parameters[0] == 0)
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Menu Access
  #--------------------------------------------------------------------------
  def command_135
    # Change menu access flag
    $game_system.menu_disabled = (@parameters[0] == 0)
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Encounter
  #--------------------------------------------------------------------------
  def command_136
    # Change encounter flag
    $game_system.encounter_disabled = (@parameters[0] == 0)
    # Make encounter count
    $game_player.make_encounter_count
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Transfer Player
  #--------------------------------------------------------------------------
  def command_201
    # If in battle
    if $game_temp.in_battle
      # Continue
      return true
    end
    # If transferring player, showing message, or processing transition
    if $game_temp.player_transferring or
       $game_temp.message_window_showing or
       $game_temp.transition_processing
      # End
      return false
    end
    # Set transferring player flag
    $game_temp.player_transferring = true
    # If appointment method is [direct appointment]
    if @parameters[0] == 0
      # Set player move destination
      $game_temp.player_new_map_id = @parameters[1]
      $game_temp.player_new_x = @parameters[2]
      $game_temp.player_new_y = @parameters[3]
      $game_temp.player_new_direction = @parameters[4]
    # If appointment method is [appoint with variables]
    else
      # Set player move destination
      $game_temp.player_new_map_id = $game_variables[@parameters[1]]
      $game_temp.player_new_x = $game_variables[@parameters[2]]
      $game_temp.player_new_y = $game_variables[@parameters[3]]
      $game_temp.player_new_direction = @parameters[4]
    end
    # Advance index
    @index += 1
    # If fade is set
    if @parameters[5] == 0
      # Prepare for transition
      Graphics.freeze
      # Set transition processing flag
      $game_temp.transition_processing = true
      $game_temp.transition_name = ""
    end
    # End
    return false
  end
  #--------------------------------------------------------------------------
  # * Set Event Location
  #--------------------------------------------------------------------------
  def command_202
    # If in battle
    if $game_temp.in_battle
      # Continue
      return true
    end
    # Get character
    character = get_character(@parameters[0])
    # If no character exists
    if character == nil
      # Continue
      return true
    end
    # If appointment method is [direct appointment]
    if @parameters[1] == 0
      # Set character position
      character.moveto(@parameters[2], @parameters[3])
    # If appointment method is [appoint with variables]
    elsif @parameters[1] == 1
      # Set character position
      character.moveto($game_variables[@parameters[2]],
        $game_variables[@parameters[3]])
    # If appointment method is [exchange with another event]
    else
      old_x = character.x
      old_y = character.y
      character2 = get_character(@parameters[2])
      if character2 != nil
        character.moveto(character2.x, character2.y)
        character2.moveto(old_x, old_y)
      end
    end
    # Set character direction
    case @parameters[4]
    when 8  # up
      character.turn_up
    when 6  # right
      character.turn_right
    when 2  # down
      character.turn_down
    when 4  # left
      character.turn_left
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Scroll Map
  #--------------------------------------------------------------------------
  def command_203
    # If in battle
    if $game_temp.in_battle
      # Continue
      return true
    end
    # If already scrolling
    if $game_map.scrolling?
      # End
      return false
    end
    # Start scroll
    $game_map.start_scroll(@parameters[0], @parameters[1], @parameters[2])
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Map Settings
  #--------------------------------------------------------------------------
  def command_204
    case @parameters[0]
    when 0  # panorama
      $game_map.panorama_name = @parameters[1]
      $game_map.panorama_hue = @parameters[2]
    when 1  # fog
      $game_map.fog_name = @parameters[1]
      $game_map.fog_hue = @parameters[2]
      $game_map.fog_opacity = @parameters[3]
      $game_map.fog_blend_type = @parameters[4]
      $game_map.fog_zoom = @parameters[5]
      $game_map.fog_sx = @parameters[6]
      $game_map.fog_sy = @parameters[7]
    when 2  # battleback
      $game_map.battleback_name = @parameters[1]
      $game_temp.battleback_name = @parameters[1]
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Fog Color Tone
  #--------------------------------------------------------------------------
  def command_205
    # Start color tone change
    $game_map.start_fog_tone_change(@parameters[0], @parameters[1] * 2)
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Fog Opacity
  #--------------------------------------------------------------------------
  def command_206
    # Start opacity level change
    $game_map.start_fog_opacity_change(@parameters[0], @parameters[1] * 2)
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Show Animation
  #--------------------------------------------------------------------------
  def command_207
    # Get character
    character = get_character(@parameters[0])
    # If no character exists
    if character == nil
      # Continue
      return true
    end
    # Set animation ID
    character.animation_id = @parameters[1]
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Transparent Flag
  #--------------------------------------------------------------------------
  def command_208
    # Change player transparent flag
    $game_player.transparent = (@parameters[0] == 0)
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Set Move Route
  #--------------------------------------------------------------------------
  def command_209
    # Get character
    character = get_character(@parameters[0])
    # If no character exists
    if character == nil
      # Continue
      return true
    end
    # Force move route
    character.force_move_route(@parameters[1])
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Wait for Move's Completion
  #--------------------------------------------------------------------------
  def command_210
    # If not in battle
    unless $game_temp.in_battle
      # Set move route completion waiting flag
      @move_route_waiting = true
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Prepare for Transition
  #--------------------------------------------------------------------------
  def command_221
    # If showing message window
    if $game_temp.message_window_showing
      # End
      return false
    end
    # Prepare for transition
    Graphics.freeze
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Execute Transition
  #--------------------------------------------------------------------------
  def command_222
    # If transition processing flag is already set
    if $game_temp.transition_processing
      # End
      return false
    end
    # Set transition processing flag
    $game_temp.transition_processing = true
    $game_temp.transition_name = @parameters[0]
    # Advance index
    @index += 1
    # End
    return false
  end
  #--------------------------------------------------------------------------
  # * Change Screen Color Tone
  #--------------------------------------------------------------------------
  def command_223
    # Start changing color tone
    $game_screen.start_tone_change(@parameters[0], @parameters[1] * 2)
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Screen Flash
  #--------------------------------------------------------------------------
  def command_224
    # Start flash
    $game_screen.start_flash(@parameters[0], @parameters[1] * 2)
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Screen Shake
  #--------------------------------------------------------------------------
  def command_225
    # Start shake
    $game_screen.start_shake(@parameters[0], @parameters[1],
      @parameters[2] * 2)
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Show Picture
  #--------------------------------------------------------------------------
  def command_231
    # Get picture number
    number = @parameters[0] + ($game_temp.in_battle ? 50 : 0)
    # If appointment method is [direct appointment]
    if @parameters[3] == 0
      x = @parameters[4]
      y = @parameters[5]
    # If appointment method is [appoint with variables]
    else
      x = $game_variables[@parameters[4]]
      y = $game_variables[@parameters[5]]
    end
    # Show picture
    $game_screen.pictures[number].show(@parameters[1], @parameters[2],
      x, y, @parameters[6], @parameters[7], @parameters[8], @parameters[9])
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Move Picture
  #--------------------------------------------------------------------------
  def command_232
    # Get picture number
    number = @parameters[0] + ($game_temp.in_battle ? 50 : 0)
    # If appointment method is [direct appointment]
    if @parameters[3] == 0
      x = @parameters[4]
      y = @parameters[5]
    # If appointment method is [appoint with variables]
    else
      x = $game_variables[@parameters[4]]
      y = $game_variables[@parameters[5]]
    end
    # Move picture
    $game_screen.pictures[number].move(@parameters[1] * 2, @parameters[2],
      x, y, @parameters[6], @parameters[7], @parameters[8], @parameters[9])
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Rotate Picture
  #--------------------------------------------------------------------------
  def command_233
    # Get picture number
    number = @parameters[0] + ($game_temp.in_battle ? 50 : 0)
    # Set rotation speed
    $game_screen.pictures[number].rotate(@parameters[1])
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Picture Color Tone
  #--------------------------------------------------------------------------
  def command_234
    # Get picture number
    number = @parameters[0] + ($game_temp.in_battle ? 50 : 0)
    # Start changing color tone
    $game_screen.pictures[number].start_tone_change(@parameters[1],
      @parameters[2] * 2)
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Erase Picture
  #--------------------------------------------------------------------------
  def command_235
    # Get picture number
    number = @parameters[0] + ($game_temp.in_battle ? 50 : 0)
    # Erase picture
    $game_screen.pictures[number].erase
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Set Weather Effects
  #--------------------------------------------------------------------------
  def command_236
    # Set Weather Effects
    $game_screen.weather(@parameters[0], @parameters[1], @parameters[2])
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Play BGM
  #--------------------------------------------------------------------------
  def command_241
    # Play BGM
    $game_system.bgm_play(@parameters[0])
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Fade Out BGM
  #--------------------------------------------------------------------------
  def command_242
    # Fade out BGM
    $game_system.bgm_fade(@parameters[0])
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Play BGS
  #--------------------------------------------------------------------------
  def command_245
    # Play BGS
    $game_system.bgs_play(@parameters[0])
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Fade Out BGS
  #--------------------------------------------------------------------------
  def command_246
    # Fade out BGS
    $game_system.bgs_fade(@parameters[0])
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Memorize BGM/BGS
  #--------------------------------------------------------------------------
  def command_247
    # Memorize BGM/BGS
    $game_system.bgm_memorize
    $game_system.bgs_memorize
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Restore BGM/BGS
  #--------------------------------------------------------------------------
  def command_248
    # Restore BGM/BGS
    $game_system.bgm_restore
    $game_system.bgs_restore
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Play ME
  #--------------------------------------------------------------------------
  def command_249
    # Play ME
    $game_system.me_play(@parameters[0])
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Play SE
  #--------------------------------------------------------------------------
  def command_250
    # Play SE
    $game_system.se_play(@parameters[0])
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Stop SE
  #--------------------------------------------------------------------------
  def command_251
    # Stop SE
    Audio.se_stop
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Battle Processing
  #--------------------------------------------------------------------------
  def command_301
    # If not invalid troops
    if $data_troops[@parameters[0]] != nil
      # Set battle abort flag
      $game_temp.battle_abort = true
      # Set battle calling flag
      $game_temp.battle_calling = true
      $game_temp.battle_troop_id = @parameters[0]
      $game_temp.battle_can_escape = @parameters[1]
      $game_temp.battle_can_lose = @parameters[2]
      # Set callback
      current_indent = @list[@index].indent
      $game_temp.battle_proc = Proc.new { |n| @branch[current_indent] = n }
    end
    # Advance index
    @index += 1
    # End
    return false
  end
  #--------------------------------------------------------------------------
  # * If Win
  #--------------------------------------------------------------------------
  def command_601
    # When battle results = win
    if @branch[@list[@index].indent] == 0
      # Delete branch data
      @branch.delete(@list[@index].indent)
      # Continue
      return true
    end
    # If it doesn't meet conditions: command skip
    return command_skip
  end
  #--------------------------------------------------------------------------
  # * If Escape
  #--------------------------------------------------------------------------
  def command_602
    # If battle results = escape
    if @branch[@list[@index].indent] == 1
      # Delete branch data
      @branch.delete(@list[@index].indent)
      # Continue
      return true
    end
    # If it doesn't meet conditions: command skip
    return command_skip
  end
  #--------------------------------------------------------------------------
  # * If Lose
  #--------------------------------------------------------------------------
  def command_603
    # If battle results = lose
    if @branch[@list[@index].indent] == 2
      # Delete branch data
      @branch.delete(@list[@index].indent)
      # Continue
      return true
    end
    # If it doesn't meet conditions: command skip
    return command_skip
  end
  #--------------------------------------------------------------------------
  # * Shop Processing
  #--------------------------------------------------------------------------
  def command_302
    # Set battle abort flag
    $game_temp.battle_abort = true
    # Set shop calling flag
    $game_temp.shop_calling = true
    # Set goods list on new item
    $game_temp.shop_goods = [@parameters]
    # Loop
    loop do
      # Advance index
      @index += 1
      # If next event command has shop on second line or after
      if @list[@index].code == 605
        # Add goods list to new item
        $game_temp.shop_goods.push(@list[@index].parameters)
      # If event command does not have shop on second line or after
      else
        # End
        return false
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Name Input Processing
  #--------------------------------------------------------------------------
  def command_303
    # If not invalid actors
    if $data_actors[@parameters[0]] != nil
      # Set battle abort flag
      $game_temp.battle_abort = true
      # Set name input calling flag
      $game_temp.name_calling = true
      $game_temp.name_actor_id = @parameters[0]
      $game_temp.name_max_char = @parameters[1]
    end
    # Advance index
    @index += 1
    # End
    return false
  end
  #--------------------------------------------------------------------------
  # * Change HP
  #--------------------------------------------------------------------------
  def command_311
    # Get operate value
    value = operate_value(@parameters[1], @parameters[2], @parameters[3])
    # Process with iterator
    iterate_actor(@parameters[0]) do |actor|
      # If HP are not 0
      if actor.hp > 0
        # Change HP (if death is not permitted, make HP 1)
        if @parameters[4] == false and actor.hp + value <= 0
          actor.hp = 1
        else
          actor.hp += value
        end
      end
    end
    # Determine game over
    $game_temp.gameover = $game_party.all_dead?
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change SP
  #--------------------------------------------------------------------------
  def command_312
    # Get operate value
    value = operate_value(@parameters[1], @parameters[2], @parameters[3])
    # Process with iterator
    iterate_actor(@parameters[0]) do |actor|
      # Change actor SP
      actor.sp += value
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change State
  #--------------------------------------------------------------------------
  def command_313
    # Process with iterator
    iterate_actor(@parameters[0]) do |actor|
      # Change state
      if @parameters[1] == 0
        actor.add_state(@parameters[2])
      else
        actor.remove_state(@parameters[2])
      end
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Recover All
  #--------------------------------------------------------------------------
  def command_314
    # Process with iterator
    iterate_actor(@parameters[0]) do |actor|
      # Recover all for actor
      actor.recover_all
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change EXP
  #--------------------------------------------------------------------------
  def command_315
    # Get operate value
    value = operate_value(@parameters[1], @parameters[2], @parameters[3])
    # Process with iterator
    iterate_actor(@parameters[0]) do |actor|
      # Change actor EXP
      actor.exp += value
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Level
  #--------------------------------------------------------------------------
  def command_316
    # Get operate value
    value = operate_value(@parameters[1], @parameters[2], @parameters[3])
    # Process with iterator
    iterate_actor(@parameters[0]) do |actor|
      # Change actor level
      actor.level += value
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Parameters
  #--------------------------------------------------------------------------
  def command_317
    # Get operate value
    value = operate_value(@parameters[2], @parameters[3], @parameters[4])
    # Get actor
    actor = $game_actors[@parameters[0]]
    # Change parameters
    if actor != nil
      case @parameters[1]
      when 0  # MaxHP
        actor.maxhp += value
      when 1  # MaxSP
        actor.maxsp += value
      when 2  # strength
        actor.str += value
      when 3  # dexterity
        actor.dex += value
      when 4  # agility
        actor.agi += value
      when 5  # intelligence
        actor.int += value
      end
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Skills
  #--------------------------------------------------------------------------
  def command_318
    # Get actor
    actor = $game_actors[@parameters[0]]
    # Change skill
    if actor != nil
      if @parameters[1] == 0
        actor.learn_skill(@parameters[2])
      else
        actor.forget_skill(@parameters[2])
      end
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Equipment
  #--------------------------------------------------------------------------
  def command_319
    # Get actor
    actor = $game_actors[@parameters[0]]
    # Change Equipment
    if actor != nil
      actor.equip(@parameters[1], @parameters[2])
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Actor Name
  #--------------------------------------------------------------------------
  def command_320
    # Get actor
    actor = $game_actors[@parameters[0]]
    # Change name
    if actor != nil
      actor.name = @parameters[1]
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Actor Class
  #--------------------------------------------------------------------------
  def command_321
    # Get actor
    actor = $game_actors[@parameters[0]]
    # Change class
    if actor != nil
      actor.class_id = @parameters[1]
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Actor Graphic
  #--------------------------------------------------------------------------
  def command_322
    # Get actor
    actor = $game_actors[@parameters[0]]
    # Change graphic
    if actor != nil
      actor.set_graphic(@parameters[1], @parameters[2],
        @parameters[3], @parameters[4])
    end
    # Refresh player
    $game_player.refresh
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Enemy HP
  #--------------------------------------------------------------------------
  def command_331
    # Get operate value
    value = operate_value(@parameters[1], @parameters[2], @parameters[3])
    # Process with iterator
    iterate_enemy(@parameters[0]) do |enemy|
      # If HP is not 0
      if enemy.hp > 0
        # Change HP (if death is not permitted then change HP to 1)
        if @parameters[4] == false and enemy.hp + value <= 0
          enemy.hp = 1
        else
          enemy.hp += value
        end
      end
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Enemy SP
  #--------------------------------------------------------------------------
  def command_332
    # Get operate value
    value = operate_value(@parameters[1], @parameters[2], @parameters[3])
    # Process with iterator
    iterate_enemy(@parameters[0]) do |enemy|
      # Change SP
      enemy.sp += value
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Change Enemy State
  #--------------------------------------------------------------------------
  def command_333
    # Process with iterator
    iterate_enemy(@parameters[0]) do |enemy|
      # If [regard HP 0] state option is valid
      if $data_states[@parameters[2]].zero_hp
        # Clear immortal flag
        enemy.immortal = false
      end
      # Change
      if @parameters[1] == 0
        enemy.add_state(@parameters[2])
      else
        enemy.remove_state(@parameters[2])
      end
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Enemy Recover All
  #--------------------------------------------------------------------------
  def command_334
    # Process with iterator
    iterate_enemy(@parameters[0]) do |enemy|
      # Recover all
      enemy.recover_all
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Enemy Appearance
  #--------------------------------------------------------------------------
  def command_335
    # Get enemy
    enemy = $game_troop.enemies[@parameters[0]]
    # Clear hidden flag
    if enemy != nil
      enemy.hidden = false
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Enemy Transform
  #--------------------------------------------------------------------------
  def command_336
    # Get enemy
    enemy = $game_troop.enemies[@parameters[0]]
    # Transform processing
    if enemy != nil
      enemy.transform(@parameters[1])
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Show Battle Animation
  #--------------------------------------------------------------------------
  def command_337
    # Process with iterator
    iterate_battler(@parameters[0], @parameters[1]) do |battler|
      # If battler exists
      if battler.exist?
        # Set animation ID
        battler.animation_id = @parameters[2]
      end
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Deal Damage
  #--------------------------------------------------------------------------
  def command_338
    # Get operate value
    value = operate_value(0, @parameters[2], @parameters[3])
    # Process with iterator
    iterate_battler(@parameters[0], @parameters[1]) do |battler|
      # If battler exists
      if battler.exist?
        # Change HP
        battler.hp -= value
        # If in battle
        if $game_temp.in_battle
          # Set damage
          battler.damage = value
          battler.damage_pop = true
        end
      end
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Force Action
  #--------------------------------------------------------------------------
  def command_339
    # Ignore if not in battle
    unless $game_temp.in_battle
      return true
    end
    # Ignore if number of turns = 0
    if $game_temp.battle_turn == 0
      return true
    end
    # Process with iterator (For convenience, this process won't be repeated)
    iterate_battler(@parameters[0], @parameters[1]) do |battler|
      # If battler exists
      if battler.exist?
        # Set action
        battler.current_action.kind = @parameters[2]
        if battler.current_action.kind == 0
          battler.current_action.basic = @parameters[3]
        else
          battler.current_action.skill_id = @parameters[3]
        end
        # Set action target
        if @parameters[4] == -2
          if battler.is_a?(Game_Enemy)
            battler.current_action.decide_last_target_for_enemy
          else
            battler.current_action.decide_last_target_for_actor
          end
        elsif @parameters[4] == -1
          if battler.is_a?(Game_Enemy)
            battler.current_action.decide_random_target_for_enemy
          else
            battler.current_action.decide_random_target_for_actor
          end
        elsif @parameters[4] >= 0
          battler.current_action.target_index = @parameters[4]
        end
        # Set force flag
        battler.current_action.forcing = true
        # If action is valid and [run now]
        if battler.current_action.valid? and @parameters[5] == 1
          # Set battler being forced into action
          $game_temp.forcing_battler = battler
          # Advance index
          @index += 1
          # End
          return false
        end
      end
    end
    # Continue
    return true
  end
  #--------------------------------------------------------------------------
  # * Abort Battle
  #--------------------------------------------------------------------------
  def command_340
    # Set battle abort flag
    $game_temp.battle_abort = true
    # Advance index
    @index += 1
    # End
    return false
  end
  #--------------------------------------------------------------------------
  # * Call Menu Screen
  #--------------------------------------------------------------------------
  def command_351
    # Set battle abort flag
    $game_temp.battle_abort = true
    # Set menu calling flag
    $game_temp.menu_calling = true
    # Advance index
    @index += 1
    # End
    return false
  end
  #--------------------------------------------------------------------------
  # * Call Save Screen
  #--------------------------------------------------------------------------
  def command_352
    # Set battle abort flag
    $game_temp.battle_abort = true
    # Set save calling flag
    $game_temp.save_calling = true
    # Advance index
    @index += 1
    # End
    return false
  end
  #--------------------------------------------------------------------------
  # * Game Over
  #--------------------------------------------------------------------------
  def command_353
    # Set game over flag
    $game_temp.gameover = true
    # End
    return false
  end
  #--------------------------------------------------------------------------
  # * Return to Title Screen
  #--------------------------------------------------------------------------
  def command_354
    # Set return to title screen flag
    $game_temp.to_title = true
    # End
    return false
  end
  #--------------------------------------------------------------------------
  # * Script
  #--------------------------------------------------------------------------
  def command_355
    # Set first line to script
    script = @list[@index].parameters[0] + "\n"
    # Loop
    loop do
      # If next event command is second line of script or after
      if @list[@index+1].code == 655
        # Add second line or after to script
        script += @list[@index+1].parameters[0] + "\n"
      # If event command is not second line or after
      else
        # Abort loop
        break
      end
      # Advance index
      @index += 1
    end
    # Evaluation
    begin
      eval(script)
    rescue
    end
    # Continue
    return true
  end
end
#==============================================================================
# ** Scene_Title
#------------------------------------------------------------------------------
#  This class performs title screen processing.
#==============================================================================

class Scene_Title
  #--------------------------------------------------------------------------
  # * Main Processing
  #--------------------------------------------------------------------------
  def main
    # If battle test
    if $BTEST
      battle_test
      return
    end
    # Load database
    $data_actors        = load_data("Data/Actors.rxdata")
    $data_classes       = load_data("Data/Classes.rxdata")
    $data_skills        = load_data("Data/Skills.rxdata")
    $data_items         = load_data("Data/Items.rxdata")
    $data_weapons       = load_data("Data/Weapons.rxdata")
    $data_armors        = load_data("Data/Armors.rxdata")
    $data_enemies       = load_data("Data/Enemies.rxdata")
    $data_troops        = load_data("Data/Troops.rxdata")
    $data_states        = load_data("Data/States.rxdata")
    $data_animations    = load_data("Data/Animations.rxdata")
    $data_tilesets      = load_data("Data/Tilesets.rxdata")
    $data_common_events = load_data("Data/CommonEvents.rxdata")
    $data_system        = load_data("Data/System.rxdata")
    # Make system object
    $game_system = Game_System.new
    # Make title graphic
    @sprite = Sprite.new
    @sprite.bitmap = RPG::Cache.title($data_system.title_name)
    # Make command window
    s1 = "New Game"
    s2 = "Continue"
    s3 = "Shutdown"
    @command_window = Window_Command.new(192, [s1, s2, s3])
    @command_window.back_opacity = 160
    @command_window.x = 320 - @command_window.width / 2
    @command_window.y = 288
    # Continue enabled determinant
    # Check if at least one save file exists
    # If enabled, make @continue_enabled true; if disabled, make it false
    @continue_enabled = false
    for i in 0..3
      if FileTest.exist?("Save#{i+1}.rxdata")
        @continue_enabled = true
      end
    end
    # If continue is enabled, move cursor to "Continue"
    # If disabled, display "Continue" text in gray
    if @continue_enabled
      @command_window.index = 1
    else
      @command_window.disable_item(1)
    end
    # Play title BGM
    $game_system.bgm_play($data_system.title_bgm)
    # Stop playing ME and BGS
    Audio.me_stop
    Audio.bgs_stop
    # Execute transition
    Graphics.transition
    # Main loop
    loop do
      # Update game screen
      Graphics.update
      # Update input information
      Input.update
      # Frame update
      update
      # Abort loop if screen is changed
      if $scene != self
        break
      end
    end
    # Prepare for transition
    Graphics.freeze
    # Dispose of command window
    @command_window.dispose
    # Dispose of title graphic
    @sprite.bitmap.dispose
    @sprite.dispose
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # Update command window
    @command_window.update
    if Input.trigger?(Input::A)
      if @command_window.windowskin == nil
        @command_window.windowskin = RPG::Cache.windowskin($game_system.windowskin_name)
        @command_window.contents = RPG::Cache.windowskin($game_system.windowskin_name)
      else
        @command_window.windowskin = nil
        @command_window.contents = nil
      end
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # Branch by command window cursor position
      case @command_window.index
      when 0  # New game
        command_new_game
      when 1  # Continue
        command_continue
      when 2  # Shutdown
        command_shutdown
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Command: New Game
  #--------------------------------------------------------------------------
  def command_new_game
    # Play decision SE
    $game_system.se_play($data_system.decision_se)
    # Stop BGM
    Audio.bgm_stop
    # Reset frame count for measuring play time
    Graphics.frame_count = 0
    # Make each type of game object
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
    # Set up initial party
    $game_party.setup_starting_members
    # Set up initial map position
    $game_map.setup($data_system.start_map_id)
    # Move player to initial position
    $game_player.moveto($data_system.start_x, $data_system.start_y)
    # Refresh player
    $game_player.refresh
    # Run automatic change for BGM and BGS set with map
    $game_map.autoplay
    # Update map (run parallel process event)
    $game_map.update
    # Switch to map screen
    $scene = Scene_Map.new
  end
  #--------------------------------------------------------------------------
  # * Command: Continue
  #--------------------------------------------------------------------------
  def command_continue
    # If continue is disabled
    unless @continue_enabled
      # Play buzzer SE
      $game_system.se_play($data_system.buzzer_se)
      return
    end
    # Play decision SE
    $game_system.se_play($data_system.decision_se)
    # Switch to load screen
    $scene = Scene_Load.new
  end
  #--------------------------------------------------------------------------
  # * Command: Shutdown
  #--------------------------------------------------------------------------
  def command_shutdown
    # Play decision SE
    $game_system.se_play($data_system.decision_se)
    # Fade out BGM, BGS, and ME
    Audio.bgm_fade(800)
    Audio.bgs_fade(800)
    Audio.me_fade(800)
    # Shutdown
    $scene = nil
  end
  #--------------------------------------------------------------------------
  # * Battle Test
  #--------------------------------------------------------------------------
  def battle_test
    # Load database (for battle test)
    $data_actors        = load_data("Data/BT_Actors.rxdata")
    $data_classes       = load_data("Data/BT_Classes.rxdata")
    $data_skills        = load_data("Data/BT_Skills.rxdata")
    $data_items         = load_data("Data/BT_Items.rxdata")
    $data_weapons       = load_data("Data/BT_Weapons.rxdata")
    $data_armors        = load_data("Data/BT_Armors.rxdata")
    $data_enemies       = load_data("Data/BT_Enemies.rxdata")
    $data_troops        = load_data("Data/BT_Troops.rxdata")
    $data_states        = load_data("Data/BT_States.rxdata")
    $data_animations    = load_data("Data/BT_Animations.rxdata")
    $data_tilesets      = load_data("Data/BT_Tilesets.rxdata")
    $data_common_events = load_data("Data/BT_CommonEvents.rxdata")
    $data_system        = load_data("Data/BT_System.rxdata")
    # Reset frame count for measuring play time
    Graphics.frame_count = 0
    # Make each game object
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
    # Set up party for battle test
    $game_party.setup_battle_test_members
    # Set troop ID, can escape flag, and battleback
    $game_temp.battle_troop_id = $data_system.test_troop_id
    $game_temp.battle_can_escape = true
    $game_map.battleback_name = $data_system.battleback_name
    # Play battle start SE
    $game_system.se_play($data_system.battle_start_se)
    # Play battle BGM
    $game_system.bgm_play($game_system.battle_bgm)
    # Switch to battle screen
    $scene = Scene_Battle.new
  end
end
#==============================================================================
# ** Scene_Map
#------------------------------------------------------------------------------
#  This class performs map screen processing.
#==============================================================================

class Scene_Map
  #--------------------------------------------------------------------------
  # * Main Processing
  #--------------------------------------------------------------------------
  def main
    # Make sprite set
    @spriteset = Spriteset_Map.new
    # Make message window
    @message_window = Window_Message.new
    # Transition run
    Graphics.transition
    # Main loop
    loop do
      # Update game screen
      Graphics.update
      # Update input information
      Input.update
      # Frame update
      update
      # Abort loop if screen is changed
      if $scene != self
        break
      end
    end
    # Prepare for transition
    Graphics.freeze
    # Dispose of sprite set
    @spriteset.dispose
    # Dispose of message window
    @message_window.dispose
    # If switching to title screen
    if $scene.is_a?(Scene_Title)
      # Fade out screen
      Graphics.transition
      Graphics.freeze
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # Loop
    loop do
      # Update map, interpreter, and player order
      # (this update order is important for when conditions are fulfilled 
      # to run any event, and the player isn't provided the opportunity to
      # move in an instant)
      $game_map.update
      $game_system.map_interpreter.update
      $game_player.update
      # Update system (timer), screen
      $game_system.update
      $game_screen.update
      # Abort loop if player isn't place moving
      unless $game_temp.player_transferring
        break
      end
      # Run place move
      transfer_player
      # Abort loop if transition processing
      if $game_temp.transition_processing
        break
      end
    end
    # Update sprite set
    @spriteset.update
    # Update message window
    @message_window.update
    # If game over
    if $game_temp.gameover
      # Switch to game over screen
      $scene = Scene_Gameover.new
      return
    end
    # If returning to title screen
    if $game_temp.to_title
      # Change to title screen
      $scene = Scene_Title.new
      return
    end
    # If transition processing
    if $game_temp.transition_processing
      # Clear transition processing flag
      $game_temp.transition_processing = false
      # Execute transition
      if $game_temp.transition_name == ""
        Graphics.transition(20)
      else
        Graphics.transition(40, "Graphics/Transitions/" +
          $game_temp.transition_name)
      end
    end
    # If showing message window
    if $game_temp.message_window_showing
      return
    end
    # If encounter list isn't empty, and encounter count is 0
    if $game_player.encounter_count == 0 and $game_map.encounter_list != []
      # If event is running or encounter is not forbidden
      unless $game_system.map_interpreter.running? or
             $game_system.encounter_disabled
        # Confirm troop
        n = rand($game_map.encounter_list.size)
        troop_id = $game_map.encounter_list[n]
        # If troop is valid
        if $data_troops[troop_id] != nil
          # Set battle calling flag
          $game_temp.battle_calling = true
          $game_temp.battle_troop_id = troop_id
          $game_temp.battle_can_escape = true
          $game_temp.battle_can_lose = false
          $game_temp.battle_proc = nil
        end
      end
    end
    # If B button was pressed
    if Input.trigger?(Input::B)
      # If event is running, or menu is not forbidden
      unless $game_system.map_interpreter.running? or
             $game_system.menu_disabled
        # Set menu calling flag or beep flag
        $game_temp.menu_calling = true
        $game_temp.menu_beep = true
      end
    end
    # If debug mode is ON and F9 key was pressed
    if $DEBUG and Input.press?(Input::F9)
      # Set debug calling flag
      $game_temp.debug_calling = true
    end
    # If player is not moving
    unless $game_player.moving?
      # Run calling of each screen
      if $game_temp.battle_calling
        call_battle
      elsif $game_temp.shop_calling
        call_shop
      elsif $game_temp.name_calling
        call_name
      elsif $game_temp.menu_calling
        call_menu
      elsif $game_temp.save_calling
        call_save
      elsif $game_temp.debug_calling
        call_debug
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Battle Call
  #--------------------------------------------------------------------------
  def call_battle
    # Clear battle calling flag
    $game_temp.battle_calling = false
    # Clear menu calling flag
    $game_temp.menu_calling = false
    $game_temp.menu_beep = false
    # Make encounter count
    $game_player.make_encounter_count
    # Memorize map BGM and stop BGM
    $game_temp.map_bgm = $game_system.playing_bgm
    $game_system.bgm_stop
    # Play battle start SE
    $game_system.se_play($data_system.battle_start_se)
    # Play battle BGM
    $game_system.bgm_play($game_system.battle_bgm)
    # Straighten player position
    $game_player.straighten
    # Switch to battle screen
    $scene = Scene_Battle.new
  end
  #--------------------------------------------------------------------------
  # * Shop Call
  #--------------------------------------------------------------------------
  def call_shop
    # Clear shop call flag
    $game_temp.shop_calling = false
    # Straighten player position
    $game_player.straighten
    # Switch to shop screen
    $scene = Scene_Shop.new
  end
  #--------------------------------------------------------------------------
  # * Name Input Call
  #--------------------------------------------------------------------------
  def call_name
    # Clear name input call flag
    $game_temp.name_calling = false
    # Straighten player position
    $game_player.straighten
    # Switch to name input screen
    $scene = Scene_Name.new
  end
  #--------------------------------------------------------------------------
  # * Menu Call
  #--------------------------------------------------------------------------
  def call_menu
    # Clear menu call flag
    $game_temp.menu_calling = false
    # If menu beep flag is set
    if $game_temp.menu_beep
      # Play decision SE
      $game_system.se_play($data_system.decision_se)
      # Clear menu beep flag
      $game_temp.menu_beep = false
    end
    # Straighten player position
    $game_player.straighten
    # Switch to menu screen
    $scene = Scene_Menu.new
  end
  #--------------------------------------------------------------------------
  # * Save Call
  #--------------------------------------------------------------------------
  def call_save
    # Straighten player position
    $game_player.straighten
    # Switch to save screen
    $scene = Scene_Save.new
  end
  #--------------------------------------------------------------------------
  # * Debug Call
  #--------------------------------------------------------------------------
  def call_debug
    # Clear debug call flag
    $game_temp.debug_calling = false
    # Play decision SE
    $game_system.se_play($data_system.decision_se)
    # Straighten player position
    $game_player.straighten
    # Switch to debug screen
    $scene = Scene_Debug.new
  end
  #--------------------------------------------------------------------------
  # * Player Place Move
  #--------------------------------------------------------------------------
  def transfer_player
    # Clear player place move call flag
    $game_temp.player_transferring = false
    # If move destination is different than current map
    if $game_map.map_id != $game_temp.player_new_map_id
      # Set up a new map
      $game_map.setup($game_temp.player_new_map_id)
    end
    # Set up player position
    $game_player.moveto($game_temp.player_new_x, $game_temp.player_new_y)
    # Set player direction
    case $game_temp.player_new_direction
    when 2  # down
      $game_player.turn_down
    when 4  # left
      $game_player.turn_left
    when 6  # right
      $game_player.turn_right
    when 8  # up
      $game_player.turn_up
    end
    # Straighten player position
    $game_player.straighten
    # Update map (run parallel process event)
    $game_map.update
    # Remake sprite set
    @spriteset.dispose
    @spriteset = Spriteset_Map.new
    # If processing transition
    if $game_temp.transition_processing
      # Clear transition processing flag
      $game_temp.transition_processing = false
      # Execute transition
      Graphics.transition(20)
    end
    # Run automatic change for BGM and BGS set on the map
    $game_map.autoplay
    # Frame reset
    Graphics.frame_reset
    # Update input information
    Input.update
  end
end
#==============================================================================
# ** Scene_Menu
#------------------------------------------------------------------------------
#  This class performs menu screen processing.
#==============================================================================

class Scene_Menu
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     menu_index : command cursor's initial position
  #--------------------------------------------------------------------------
  def initialize(menu_index = 0)
    @menu_index = menu_index
  end
  #--------------------------------------------------------------------------
  # * Main Processing
  #--------------------------------------------------------------------------
  def main
    # Make command window
    s1 = $data_system.words.item
    s2 = $data_system.words.skill
    s3 = $data_system.words.equip
    s4 = "Status"
    s5 = "Save"
    s6 = "End Game"
    @command_window = Window_Command.new(160, [s1, s2, s3, s4, s5, s6])
    @command_window.index = @menu_index
    # If number of party members is 0
    if $game_party.actors.size == 0
      # Disable items, skills, equipment, and status
      @command_window.disable_item(0)
      @command_window.disable_item(1)
      @command_window.disable_item(2)
      @command_window.disable_item(3)
    end
    # If save is forbidden
    if $game_system.save_disabled
      # Disable save
      @command_window.disable_item(4)
    end
    # Make play time window
    @playtime_window = Window_PlayTime.new
    @playtime_window.x = 0
    @playtime_window.y = 224
    # Make steps window
    @steps_window = Window_Steps.new
    @steps_window.x = 0
    @steps_window.y = 320
    # Make gold window
    @gold_window = Window_Gold.new
    @gold_window.x = 0
    @gold_window.y = 416
    # Make status window
    @status_window = Window_MenuStatus.new
    @status_window.x = 160
    @status_window.y = 0
    # Execute transition
    Graphics.transition
    # Main loop
    loop do
      # Update game screen
      Graphics.update
      # Update input information
      Input.update
      # Frame update
      update
      # Abort loop if screen is changed
      if $scene != self
        break
      end
    end
    # Prepare for transition
    Graphics.freeze
    # Dispose of windows
    @command_window.dispose
    @playtime_window.dispose
    @steps_window.dispose
    @gold_window.dispose
    @status_window.dispose
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # Update windows
    @command_window.update
    @playtime_window.update
    @steps_window.update
    @gold_window.update
    @status_window.update
    # If command window is active: call update_command
    if @command_window.active
      update_command
      return
    end
    # If status window is active: call update_status
    if @status_window.active
      update_status
      return
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (when command window is active)
  #--------------------------------------------------------------------------
  def update_command
    # If B button was pressed
    if Input.trigger?(Input::B)
      # Play cancel SE
      $game_system.se_play($data_system.cancel_se)
      # Switch to map screen
      $scene = Scene_Map.new
      return
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # If command other than save or end game, and party members = 0
      if $game_party.actors.size == 0 and @command_window.index < 4
        # Play buzzer SE
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      # Branch by command window cursor position
      case @command_window.index
      when 0  # item
        # Play decision SE
        $game_system.se_play($data_system.decision_se)
        # Switch to item screen
        $scene = Scene_Item.new
      when 1  # skill
        # Play decision SE
        $game_system.se_play($data_system.decision_se)
        # Make status window active
        @command_window.active = false
        @status_window.active = true
        @status_window.index = 0
      when 2  # equipment
        # Play decision SE
        $game_system.se_play($data_system.decision_se)
        # Make status window active
        @command_window.active = false
        @status_window.active = true
        @status_window.index = 0
      when 3  # status
        # Play decision SE
        $game_system.se_play($data_system.decision_se)
        # Make status window active
        @command_window.active = false
        @status_window.active = true
        @status_window.index = 0
      when 4  # save
        # If saving is forbidden
        if $game_system.save_disabled
          # Play buzzer SE
          $game_system.se_play($data_system.buzzer_se)
          return
        end
        # Play decision SE
        $game_system.se_play($data_system.decision_se)
        # Switch to save screen
        $scene = Scene_Save.new
      when 5  # end game
        # Play decision SE
        $game_system.se_play($data_system.decision_se)
        # Switch to end game screen
        $scene = Scene_End.new
      end
      return
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (when status window is active)
  #--------------------------------------------------------------------------
  def update_status
    # If B button was pressed
    if Input.trigger?(Input::B)
      # Play cancel SE
      $game_system.se_play($data_system.cancel_se)
      # Make command window active
      @command_window.active = true
      @status_window.active = false
      @status_window.index = -1
      return
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # Branch by command window cursor position
      case @command_window.index
      when 1  # skill
        # If this actor's action limit is 2 or more
        if $game_party.actors[@status_window.index].restriction >= 2
          # Play buzzer SE
          $game_system.se_play($data_system.buzzer_se)
          return
        end
        # Play decision SE
        $game_system.se_play($data_system.decision_se)
        # Switch to skill screen
        $scene = Scene_Skill.new(@status_window.index)
      when 2  # equipment
        # Play decision SE
        $game_system.se_play($data_system.decision_se)
        # Switch to equipment screen
        $scene = Scene_Equip.new(@status_window.index)
      when 3  # status
        # Play decision SE
        $game_system.se_play($data_system.decision_se)
        # Switch to status screen
        $scene = Scene_Status.new(@status_window.index)
      end
      return
    end
  end
end
#==============================================================================
# ** Scene_Item
#------------------------------------------------------------------------------
#  This class performs item screen processing.
#==============================================================================

class Scene_Item
  #--------------------------------------------------------------------------
  # * Main Processing
  #--------------------------------------------------------------------------
  def main
    # Make help window, item window
    @help_window = Window_Help.new
    @item_window = Window_Item.new
    # Associate help window
    @item_window.help_window = @help_window
    # Make target window (set to invisible / inactive)
    @target_window = Window_Target.new
    @target_window.visible = false
    @target_window.active = false
    # Execute transition
    Graphics.transition
    # Main loop
    loop do
      # Update game screen
      Graphics.update
      # Update input information
      Input.update
      # Frame update
      update
      # Abort loop if screen is changed
      if $scene != self
        break
      end
    end
    # Prepare for transition
    Graphics.freeze
    # Dispose of windows
    @help_window.dispose
    @item_window.dispose
    @target_window.dispose
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # Update windows
    @help_window.update
    @item_window.update
    @target_window.update
    # If item window is active: call update_item
    if @item_window.active
      update_item
      return
    end
    # If target window is active: call update_target
    if @target_window.active
      update_target
      return
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (when item window is active)
  #--------------------------------------------------------------------------
  def update_item
    # If B button was pressed
    if Input.trigger?(Input::B)
      # Play cancel SE
      $game_system.se_play($data_system.cancel_se)
      # Switch to menu screen
      $scene = Scene_Menu.new(0)
      return
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # Get currently selected data on the item window
      @item = @item_window.item
      # If not a use item
      unless @item.is_a?(RPG::Item)
        # Play buzzer SE
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      # If it can't be used
      unless $game_party.item_can_use?(@item.id)
        # Play buzzer SE
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      # Play decision SE
      $game_system.se_play($data_system.decision_se)
      # If effect scope is an ally
      if @item.scope >= 3
        # Activate target window
        @item_window.active = false
        @target_window.x = (@item_window.index + 1) % 2 * 304
        @target_window.visible = true
        @target_window.active = true
        # Set cursor position to effect scope (single / all)
        if @item.scope == 4 || @item.scope == 6
          @target_window.index = -1
        else
          @target_window.index = 0
        end
      # If effect scope is other than an ally
      else
        # If command event ID is valid
        if @item.common_event_id > 0
          # Command event call reservation
          $game_temp.common_event_id = @item.common_event_id
          # Play item use SE
          $game_system.se_play(@item.menu_se)
          # If consumable
          if @item.consumable
            # Decrease used items by 1
            $game_party.lose_item(@item.id, 1)
            # Draw item window item
            @item_window.draw_item(@item_window.index)
          end
          # Switch to map screen
          $scene = Scene_Map.new
          return
        end
      end
      return
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (when target window is active)
  #--------------------------------------------------------------------------
  def update_target
    # If B button was pressed
    if Input.trigger?(Input::B)
      # Play cancel SE
      $game_system.se_play($data_system.cancel_se)
      # If unable to use because items ran out
      unless $game_party.item_can_use?(@item.id)
        # Remake item window contents
        @item_window.refresh
      end
      # Erase target window
      @item_window.active = true
      @target_window.visible = false
      @target_window.active = false
      return
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # If items are used up
      if $game_party.item_number(@item.id) == 0
        # Play buzzer SE
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      # If target is all
      if @target_window.index == -1
        # Apply item effects to entire party
        used = false
        for i in $game_party.actors
          used |= i.item_effect(@item)
        end
      end
      # If single target
      if @target_window.index >= 0
        # Apply item use effects to target actor
        target = $game_party.actors[@target_window.index]
        used = target.item_effect(@item)
      end
      # If an item was used
      if used
        # Play item use SE
        $game_system.se_play(@item.menu_se)
        # If consumable
        if @item.consumable
          # Decrease used items by 1
          $game_party.lose_item(@item.id, 1)
          # Redraw item window item
          @item_window.draw_item(@item_window.index)
        end
        # Remake target window contents
        @target_window.refresh
        # If all party members are dead
        if $game_party.all_dead?
          # Switch to game over screen
          $scene = Scene_Gameover.new
          return
        end
        # If common event ID is valid
        if @item.common_event_id > 0
          # Common event call reservation
          $game_temp.common_event_id = @item.common_event_id
          # Switch to map screen
          $scene = Scene_Map.new
          return
        end
      end
      # If item wasn't used
      unless used
        # Play buzzer SE
        $game_system.se_play($data_system.buzzer_se)
      end
      return
    end
  end
end
#==============================================================================
# ** Scene_Skill
#------------------------------------------------------------------------------
#  This class performs skill screen processing.
#==============================================================================

class Scene_Skill
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     actor_index : actor index
  #--------------------------------------------------------------------------
  def initialize(actor_index = 0, equip_index = 0)
    @actor_index = actor_index
  end
  #--------------------------------------------------------------------------
  # * Main Processing
  #--------------------------------------------------------------------------
  def main
    # Get actor
    @actor = $game_party.actors[@actor_index]
    # Make help window, status window, and skill window
    @help_window = Window_Help.new
    @status_window = Window_SkillStatus.new(@actor)
    @skill_window = Window_Skill.new(@actor)
    # Associate help window
    @skill_window.help_window = @help_window
    # Make target window (set to invisible / inactive)
    @target_window = Window_Target.new
    @target_window.visible = false
    @target_window.active = false
    # Execute transition
    Graphics.transition
    # Main loop
    loop do
      # Update game screen
      Graphics.update
      # Update input information
      Input.update
      # Frame update
      update
      # Abort loop if screen is changed
      if $scene != self
        break
      end
    end
    # Prepare for transition
    Graphics.freeze
    # Dispose of windows
    @help_window.dispose
    @status_window.dispose
    @skill_window.dispose
    @target_window.dispose
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # Update windows
    @help_window.update
    @status_window.update
    @skill_window.update
    @target_window.update
    # If skill window is active: call update_skill
    if @skill_window.active
      update_skill
      return
    end
    # If skill target is active: call update_target
    if @target_window.active
      update_target
      return
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (if skill window is active)
  #--------------------------------------------------------------------------
  def update_skill
    # If B button was pressed
    if Input.trigger?(Input::B)
      # Play cancel SE
      $game_system.se_play($data_system.cancel_se)
      # Switch to menu screen
      $scene = Scene_Menu.new(1)
      return
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # Get currently selected data on the skill window
      @skill = @skill_window.skill
      # If unable to use
      if @skill == nil or not @actor.skill_can_use?(@skill.id)
        # Play buzzer SE
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      # Play decision SE
      $game_system.se_play($data_system.decision_se)
      # If effect scope is ally
      if @skill.scope >= 3
        # Activate target window
        @skill_window.active = false
        @target_window.x = (@skill_window.index + 1) % 2 * 304
        @target_window.visible = true
        @target_window.active = true
        # Set cursor position to effect scope (single / all)
        if @skill.scope == 4 || @skill.scope == 6
          @target_window.index = -1
        elsif @skill.scope == 7
          @target_window.index = @actor_index - 10
        else
          @target_window.index = 0
        end
      # If effect scope is other than ally
      else
        # If common event ID is valid
        if @skill.common_event_id > 0
          # Common event call reservation
          $game_temp.common_event_id = @skill.common_event_id
          # Play use skill SE
          $game_system.se_play(@skill.menu_se)
          # Use up SP
          @actor.sp -= @skill.sp_cost
          # Remake each window content
          @status_window.refresh
          @skill_window.refresh
          @target_window.refresh
          # Switch to map screen
          $scene = Scene_Map.new
          return
        end
      end
      return
    end
    # If R button was pressed
    if Input.trigger?(Input::R)
      # Play cursor SE
      $game_system.se_play($data_system.cursor_se)
      # To next actor
      @actor_index += 1
      @actor_index %= $game_party.actors.size
      # Switch to different skill screen
      $scene = Scene_Skill.new(@actor_index)
      return
    end
    # If L button was pressed
    if Input.trigger?(Input::L)
      # Play cursor SE
      $game_system.se_play($data_system.cursor_se)
      # To previous actor
      @actor_index += $game_party.actors.size - 1
      @actor_index %= $game_party.actors.size
      # Switch to different skill screen
      $scene = Scene_Skill.new(@actor_index)
      return
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (when target window is active)
  #--------------------------------------------------------------------------
  def update_target
    # If B button was pressed
    if Input.trigger?(Input::B)
      # Play cancel SE
      $game_system.se_play($data_system.cancel_se)
      # Erase target window
      @skill_window.active = true
      @target_window.visible = false
      @target_window.active = false
      return
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # If unable to use because SP ran out
      unless @actor.skill_can_use?(@skill.id)
        # Play buzzer SE
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      # If target is all
      if @target_window.index == -1
        # Apply skill use effects to entire party
        used = false
        for i in $game_party.actors
          used |= i.skill_effect(@actor, @skill)
        end
      end
      # If target is user
      if @target_window.index <= -2
        # Apply skill use effects to target actor
        target = $game_party.actors[@target_window.index + 10]
        used = target.skill_effect(@actor, @skill)
      end
      # If single target
      if @target_window.index >= 0
        # Apply skill use effects to target actor
        target = $game_party.actors[@target_window.index]
        used = target.skill_effect(@actor, @skill)
      end
      # If skill was used
      if used
        # Play skill use SE
        $game_system.se_play(@skill.menu_se)
        # Use up SP
        @actor.sp -= @skill.sp_cost
        # Remake each window content
        @status_window.refresh
        @skill_window.refresh
        @target_window.refresh
        # If entire party is dead
        if $game_party.all_dead?
          # Switch to game over screen
          $scene = Scene_Gameover.new
          return
        end
        # If command event ID is valid
        if @skill.common_event_id > 0
          # Command event call reservation
          $game_temp.common_event_id = @skill.common_event_id
          # Switch to map screen
          $scene = Scene_Map.new
          return
        end
      end
      # If skill wasn't used
      unless used
        # Play buzzer SE
        $game_system.se_play($data_system.buzzer_se)
      end
      return
    end
  end
end
#==============================================================================
# ** Scene_Equip
#------------------------------------------------------------------------------
#  This class performs equipment screen processing.
#==============================================================================

class Scene_Equip
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     actor_index : actor index
  #     equip_index : equipment index
  #--------------------------------------------------------------------------
  def initialize(actor_index = 0, equip_index = 0)
    @actor_index = actor_index
    @equip_index = equip_index
  end
  #--------------------------------------------------------------------------
  # * Main Processing
  #--------------------------------------------------------------------------
  def main
    # Get actor
    @actor = $game_party.actors[@actor_index]
    # Make windows
    @help_window = Window_Help.new
    @left_window = Window_EquipLeft.new(@actor)
    @right_window = Window_EquipRight.new(@actor)
    @item_window1 = Window_EquipItem.new(@actor, 0)
    @item_window2 = Window_EquipItem.new(@actor, 1)
    @item_window3 = Window_EquipItem.new(@actor, 2)
    @item_window4 = Window_EquipItem.new(@actor, 3)
    @item_window5 = Window_EquipItem.new(@actor, 4)
    # Associate help window
    @right_window.help_window = @help_window
    @item_window1.help_window = @help_window
    @item_window2.help_window = @help_window
    @item_window3.help_window = @help_window
    @item_window4.help_window = @help_window
    @item_window5.help_window = @help_window
    # Set cursor position
    @right_window.index = @equip_index
    refresh
    # Execute transition
    Graphics.transition
    # Main loop
    loop do
      # Update game screen
      Graphics.update
      # Update input information
      Input.update
      # Frame update
      update
      # Abort loop if screen is changed
      if $scene != self
        break
      end
    end
    # Prepare for transition
    Graphics.freeze
    # Dispose of windows
    @help_window.dispose
    @left_window.dispose
    @right_window.dispose
    @item_window1.dispose
    @item_window2.dispose
    @item_window3.dispose
    @item_window4.dispose
    @item_window5.dispose
  end
  #--------------------------------------------------------------------------
  # * Refresh
  #--------------------------------------------------------------------------
  def refresh
    # Set item window to visible
    @item_window1.visible = (@right_window.index == 0)
    @item_window2.visible = (@right_window.index == 1)
    @item_window3.visible = (@right_window.index == 2)
    @item_window4.visible = (@right_window.index == 3)
    @item_window5.visible = (@right_window.index == 4)
    # Get currently equipped item
    item1 = @right_window.item
    # Set current item window to @item_window
    case @right_window.index
    when 0
      @item_window = @item_window1
    when 1
      @item_window = @item_window2
    when 2
      @item_window = @item_window3
    when 3
      @item_window = @item_window4
    when 4
      @item_window = @item_window5
    end
    # If right window is active
    if @right_window.active
      # Erase parameters for after equipment change
      @left_window.set_new_parameters(nil, nil, nil)
    end
    # If item window is active
    if @item_window.active
      # Get currently selected item
      item2 = @item_window.item
      # Change equipment
      last_hp = @actor.hp
      last_sp = @actor.sp
      @actor.equip(@right_window.index, item2 == nil ? 0 : item2.id)
      # Get parameters for after equipment change
      new_atk = @actor.atk
      new_pdef = @actor.pdef
      new_mdef = @actor.mdef
      # Return equipment
      @actor.equip(@right_window.index, item1 == nil ? 0 : item1.id)
      @actor.hp = last_hp
      @actor.sp = last_sp
      # Draw in left window
      @left_window.set_new_parameters(new_atk, new_pdef, new_mdef)
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # Update windows
    @left_window.update
    @right_window.update
    @item_window.update
    refresh
    # If right window is active: call update_right
    if @right_window.active
      update_right
      return
    end
    # If item window is active: call update_item
    if @item_window.active
      update_item
      return
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (when right window is active)
  #--------------------------------------------------------------------------
  def update_right
    # If B button was pressed
    if Input.trigger?(Input::B)
      # Play cancel SE
      $game_system.se_play($data_system.cancel_se)
      # Switch to menu screen
      $scene = Scene_Menu.new(2)
      return
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # If equipment is fixed
      if @actor.equip_fix?(@right_window.index)
        # Play buzzer SE
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      # Play decision SE
      $game_system.se_play($data_system.decision_se)
      # Activate item window
      @right_window.active = false
      @item_window.active = true
      @item_window.index = 0
      return
    end
    # If R button was pressed
    if Input.trigger?(Input::R)
      # Play cursor SE
      $game_system.se_play($data_system.cursor_se)
      # To next actor
      @actor_index += 1
      @actor_index %= $game_party.actors.size
      # Switch to different equipment screen
      $scene = Scene_Equip.new(@actor_index, @right_window.index)
      return
    end
    # If L button was pressed
    if Input.trigger?(Input::L)
      # Play cursor SE
      $game_system.se_play($data_system.cursor_se)
      # To previous actor
      @actor_index += $game_party.actors.size - 1
      @actor_index %= $game_party.actors.size
      # Switch to different equipment screen
      $scene = Scene_Equip.new(@actor_index, @right_window.index)
      return
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (when item window is active)
  #--------------------------------------------------------------------------
  def update_item
    # If B button was pressed
    if Input.trigger?(Input::B)
      # Play cancel SE
      $game_system.se_play($data_system.cancel_se)
      # Activate right window
      @right_window.active = true
      @item_window.active = false
      @item_window.index = -1
      return
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # Play equip SE
      $game_system.se_play($data_system.equip_se)
      # Get currently selected data on the item window
      item = @item_window.item
      # Change equipment
      @actor.equip(@right_window.index, item == nil ? 0 : item.id)
      # Activate right window
      @right_window.active = true
      @item_window.active = false
      @item_window.index = -1
      # Remake right window and item window contents
      @right_window.refresh
      @item_window.refresh
      return
    end
  end
end
#==============================================================================
# ** Scene_Status
#------------------------------------------------------------------------------
#  This class performs status screen processing.
#==============================================================================

class Scene_Status
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     actor_index : actor index
  #--------------------------------------------------------------------------
  def initialize(actor_index = 0, equip_index = 0)
    @actor_index = actor_index
  end
  #--------------------------------------------------------------------------
  # * Main Processing
  #--------------------------------------------------------------------------
  def main
    # Get actor
    @actor = $game_party.actors[@actor_index]
    # Make status window
    @status_window = Window_Status.new(@actor)
    # Execute transition
    Graphics.transition
    # Main loop
    loop do
      # Update game screen
      Graphics.update
      # Update input information
      Input.update
      # Frame update
      update
      # Abort loop if screen is changed
      if $scene != self
        break
      end
    end
    # Prepare for transition
    Graphics.freeze
    # Dispose of windows
    @status_window.dispose
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # If B button was pressed
    if Input.trigger?(Input::B)
      # Play cancel SE
      $game_system.se_play($data_system.cancel_se)
      # Switch to menu screen
      $scene = Scene_Menu.new(3)
      return
    end
    # If R button was pressed
    if Input.trigger?(Input::R)
      # Play cursor SE
      $game_system.se_play($data_system.cursor_se)
      # To next actor
      @actor_index += 1
      @actor_index %= $game_party.actors.size
      # Switch to different status screen
      $scene = Scene_Status.new(@actor_index)
      return
    end
    # If L button was pressed
    if Input.trigger?(Input::L)
      # Play cursor SE
      $game_system.se_play($data_system.cursor_se)
      # To previous actor
      @actor_index += $game_party.actors.size - 1
      @actor_index %= $game_party.actors.size
      # Switch to different status screen
      $scene = Scene_Status.new(@actor_index)
      return
    end
  end
end
#==============================================================================
# ** Scene_File
#------------------------------------------------------------------------------
#  This is a superclass for the save screen and load screen.
#==============================================================================

class Scene_File
  #--------------------------------------------------------------------------
  # * Object Initialization
  #     help_text : text string shown in the help window
  #--------------------------------------------------------------------------
  def initialize(help_text)
    @help_text = help_text
  end
  #--------------------------------------------------------------------------
  # * Main Processing
  #--------------------------------------------------------------------------
  def main
    # Make help window
    @help_window = Window_Help.new
    @help_window.set_text(@help_text)
    # Make save file window
    @savefile_windows = []
    for i in 0..3
      @savefile_windows.push(Window_SaveFile.new(i, make_filename(i)))
    end
    # Select last file to be operated
    @file_index = $game_temp.last_file_index
    @savefile_windows[@file_index].selected = true
    # Execute transition
    Graphics.transition
    # Main loop
    loop do
      # Update game screen
      Graphics.update
      # Update input information
      Input.update
      # Frame update
      update
      # Abort loop if screen is changed
      if $scene != self
        break
      end
    end
    # Prepare for transition
    Graphics.freeze
    # Dispose of windows
    @help_window.dispose
    for i in @savefile_windows
      i.dispose
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # Update windows
    @help_window.update
    for i in @savefile_windows
      i.update
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # Call method: on_decision (defined by the subclasses)
      on_decision(make_filename(@file_index))
      $game_temp.last_file_index = @file_index
      return
    end
    # If B button was pressed
    if Input.trigger?(Input::B)
      # Call method: on_cancel (defined by the subclasses)
      on_cancel
      return
    end
    # If the down directional button was pressed
    if Input.repeat?(Input::DOWN)
      # If the down directional button pressed down is not a repeat,
      # or cursor position is more in front than 3
      if Input.trigger?(Input::DOWN) or @file_index < 3
        # Play cursor SE
        $game_system.se_play($data_system.cursor_se)
        # Move cursor down
        @savefile_windows[@file_index].selected = false
        @file_index = (@file_index + 1) % 4
        @savefile_windows[@file_index].selected = true
        return
      end
    end
    # If the up directional button was pressed
    if Input.repeat?(Input::UP)
      # If the up directional button pressed down is not a repeat、
      # or cursor position is more in back than 0
      if Input.trigger?(Input::UP) or @file_index > 0
        # Play cursor SE
        $game_system.se_play($data_system.cursor_se)
        # Move cursor up
        @savefile_windows[@file_index].selected = false
        @file_index = (@file_index + 3) % 4
        @savefile_windows[@file_index].selected = true
        return
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Make File Name
  #     file_index : save file index (0-3)
  #--------------------------------------------------------------------------
  def make_filename(file_index)
    return "Save#{file_index + 1}.rxdata"
  end
end
#==============================================================================
# ** Scene_Save
#------------------------------------------------------------------------------
#  This class performs save screen processing.
#==============================================================================

class Scene_Save < Scene_File
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    super("Which file would you like to save to?")
  end
  #--------------------------------------------------------------------------
  # * Decision Processing
  #--------------------------------------------------------------------------
  def on_decision(filename)
    # Play save SE
    $game_system.se_play($data_system.save_se)
    # Write save data
    file = File.open(filename, "wb")
    write_save_data(file)
    file.close
    # If called from event
    if $game_temp.save_calling
      # Clear save call flag
      $game_temp.save_calling = false
      # Switch to map screen
      $scene = Scene_Map.new
      return
    end
    # Switch to menu screen
    $scene = Scene_Menu.new(4)
  end
  #--------------------------------------------------------------------------
  # * Cancel Processing
  #--------------------------------------------------------------------------
  def on_cancel
    # Play cancel SE
    $game_system.se_play($data_system.cancel_se)
    # If called from event
    if $game_temp.save_calling
      # Clear save call flag
      $game_temp.save_calling = false
      # Switch to map screen
      $scene = Scene_Map.new
      return
    end
    # Switch to menu screen
    $scene = Scene_Menu.new(4)
  end
  #--------------------------------------------------------------------------
  # * Write Save Data
  #     file : write file object (opened)
  #--------------------------------------------------------------------------
  def write_save_data(file)
    # Make character data for drawing save file
    characters = []
    for i in 0...$game_party.actors.size
      actor = $game_party.actors[i]
      characters.push([actor.character_name, actor.character_hue])
    end
    # Write character data for drawing save file
    Marshal.dump(characters, file)
    # Wrire frame count for measuring play time
    Marshal.dump(Graphics.frame_count, file)
    # Increase save count by 1
    $game_system.save_count += 1
    # Save magic number
    # (A random value will be written each time saving with editor)
    $game_system.magic_number = $data_system.magic_number
    # Write each type of game object
    Marshal.dump($game_system, file)
    Marshal.dump($game_switches, file)
    Marshal.dump($game_variables, file)
    Marshal.dump($game_self_switches, file)
    Marshal.dump($game_screen, file)
    Marshal.dump($game_actors, file)
    Marshal.dump($game_party, file)
    Marshal.dump($game_troop, file)
    Marshal.dump($game_map, file)
    Marshal.dump($game_player, file)
  end
end
#==============================================================================
# ** Scene_Load
#------------------------------------------------------------------------------
#  This class performs load screen processing.
#==============================================================================

class Scene_Load < Scene_File
  #--------------------------------------------------------------------------
  # * Object Initialization
  #--------------------------------------------------------------------------
  def initialize
    # Remake temporary object
    $game_temp = Game_Temp.new
    # Timestamp selects new file
    $game_temp.last_file_index = 0
    latest_time = Time.at(0)
    for i in 0..3
      filename = make_filename(i)
      if FileTest.exist?(filename)
        file = File.open(filename, "r")
        if file.mtime > latest_time
          latest_time = file.mtime
          $game_temp.last_file_index = i
        end
        file.close
      end
    end
    super("Which file would you like to load?")
  end
  #--------------------------------------------------------------------------
  # * Decision Processing
  #--------------------------------------------------------------------------
  def on_decision(filename)
    # If file doesn't exist
    unless FileTest.exist?(filename)
      # Play buzzer SE
      $game_system.se_play($data_system.buzzer_se)
      return
    end
    # Play load SE
    $game_system.se_play($data_system.load_se)
    # Read save data
    file = File.open(filename, "rb")
    read_save_data(file)
    file.close
    # Restore BGM and BGS
    $game_system.bgm_play($game_system.playing_bgm)
    $game_system.bgs_play($game_system.playing_bgs)
    # Update map (run parallel process event)
    $game_map.update
    # Switch to map screen
    $scene = Scene_Map.new
  end
  #--------------------------------------------------------------------------
  # * Cancel Processing
  #--------------------------------------------------------------------------
  def on_cancel
    # Play cancel SE
    $game_system.se_play($data_system.cancel_se)
    # Switch to title screen
    $scene = Scene_Title.new
  end
  #--------------------------------------------------------------------------
  # * Read Save Data
  #     file : file object for reading (opened)
  #--------------------------------------------------------------------------
  def read_save_data(file)
    # Read character data for drawing save file
    characters = Marshal.load(file)
    # Read frame count for measuring play time
    Graphics.frame_count = Marshal.load(file)
    # Read each type of game object
    $game_system        = Marshal.load(file)
    $game_switches      = Marshal.load(file)
    $game_variables     = Marshal.load(file)
    $game_self_switches = Marshal.load(file)
    $game_screen        = Marshal.load(file)
    $game_actors        = Marshal.load(file)
    $game_party         = Marshal.load(file)
    $game_troop         = Marshal.load(file)
    $game_map           = Marshal.load(file)
    $game_player        = Marshal.load(file)
    # If magic number is different from when saving
    # (if editing was added with editor)
    if $game_system.magic_number != $data_system.magic_number
      # Load map
      $game_map.setup($game_map.map_id)
      $game_player.center($game_player.x, $game_player.y)
    end
    # Refresh party members
    $game_party.refresh
  end
end
#==============================================================================
# ** Scene_End
#------------------------------------------------------------------------------
#  This class performs game end screen processing.
#==============================================================================

class Scene_End
  #--------------------------------------------------------------------------
  # * Main Processing
  #--------------------------------------------------------------------------
  def main
    # Make command window
    s1 = "To Title"
    s2 = "Shutdown"
    s3 = "Cancel"
    @command_window = Window_Command.new(192, [s1, s2, s3])
    @command_window.x = 320 - @command_window.width / 2
    @command_window.y = 240 - @command_window.height / 2
    # Execute transition
    Graphics.transition
    # Main loop
    loop do
      # Update game screen
      Graphics.update
      # Update input information
      Input.update
      # Frame Update
      update
      # Abort loop if screen is changed
      if $scene != self
        break
      end
    end
    # Prepare for transition
    Graphics.freeze
    # Dispose of window
    @command_window.dispose
    # If switching to title screen
    if $scene.is_a?(Scene_Title)
      # Fade out screen
      Graphics.transition
      Graphics.freeze
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # Update command window
    @command_window.update
    # If B button was pressed
    if Input.trigger?(Input::B)
      # Play cancel SE
      $game_system.se_play($data_system.cancel_se)
      # Switch to menu screen
      $scene = Scene_Menu.new(5)
      return
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # Branch by command window cursor position
      case @command_window.index
      when 0  # to title
        command_to_title
      when 1  # shutdown
        command_shutdown
      when 2  # quit
        command_cancel
      end
      return
    end
  end
  #--------------------------------------------------------------------------
  # * Process When Choosing [To Title] Command
  #--------------------------------------------------------------------------
  def command_to_title
    # Play decision SE
    $game_system.se_play($data_system.decision_se)
    # Fade out BGM, BGS, and ME
    Audio.bgm_fade(800)
    Audio.bgs_fade(800)
    Audio.me_fade(800)
    # Switch to title screen
    $scene = Scene_Title.new
  end
  #--------------------------------------------------------------------------
  # * Process When Choosing [Shutdown] Command
  #--------------------------------------------------------------------------
  def command_shutdown
    # Play decision SE
    $game_system.se_play($data_system.decision_se)
    # Fade out BGM, BGS, and ME
    Audio.bgm_fade(800)
    Audio.bgs_fade(800)
    Audio.me_fade(800)
    # Shutdown
    $scene = nil
  end
  #--------------------------------------------------------------------------
  # *  Process When Choosing [Cancel] Command
  #--------------------------------------------------------------------------
  def command_cancel
    # Play decision SE
    $game_system.se_play($data_system.decision_se)
    # Switch to menu screen
    $scene = Scene_Menu.new(5)
  end
end
#==============================================================================
# ** Scene_Battle 
#------------------------------------------------------------------------------
#  This class performs battle screen processing.
#==============================================================================

class Scene_Battle
  #--------------------------------------------------------------------------
  # * Main Processing
  #--------------------------------------------------------------------------
  def main
    # Initialize each kind of temporary battle data
    $game_temp.in_battle = true
    $game_temp.battle_turn = 0
    $game_temp.battle_event_flags.clear
    $game_temp.battle_abort = false
    $game_temp.battle_main_phase = false
    $game_temp.battleback_name = $game_map.battleback_name
    $game_temp.forcing_battler = nil
    # Initialize battle event interpreter
    $game_system.battle_interpreter.setup(nil, 0)
    # Prepare troop
    @troop_id = $game_temp.battle_troop_id
    $game_troop.setup(@troop_id)
    # Make actor command window
    s1 = $data_system.words.attack
    s2 = $data_system.words.skill
    s3 = $data_system.words.guard
    s4 = $data_system.words.item
    @actor_command_window = Window_Command.new(160, [s1, s2, s3, s4])
    @actor_command_window.y = 160
    @actor_command_window.back_opacity = 160
    @actor_command_window.active = false
    @actor_command_window.visible = false
    # Make other windows
    @party_command_window = Window_PartyCommand.new
    @help_window = Window_Help.new
    @help_window.back_opacity = 160
    @help_window.visible = false
    @status_window = Window_BattleStatus.new
    @message_window = Window_Message.new
    # Make sprite set
    @spriteset = Spriteset_Battle.new
    # Initialize wait count
    @wait_count = 0
    # Execute transition
    if $data_system.battle_transition == ""
      Graphics.transition(20)
    else
      Graphics.transition(40, "Graphics/Transitions/" +
        $data_system.battle_transition)
    end
    # Start pre-battle phase
    start_phase1
    # Main loop
    loop do
      # Update game screen
      Graphics.update
      # Update input information
      Input.update
      # Frame update
      update
      # Abort loop if screen is changed
      if $scene != self
        break
      end
    end
    # Refresh map
    $game_map.refresh
    # Prepare for transition
    Graphics.freeze
    # Dispose of windows
    @actor_command_window.dispose
    @party_command_window.dispose
    @help_window.dispose
    @status_window.dispose
    @message_window.dispose
    if @skill_window != nil
      @skill_window.dispose
    end
    if @item_window != nil
      @item_window.dispose
    end
    if @result_window != nil
      @result_window.dispose
    end
    # Dispose of sprite set
    @spriteset.dispose
    # If switching to title screen
    if $scene.is_a?(Scene_Title)
      # Fade out screen
      Graphics.transition
      Graphics.freeze
    end
    # If switching from battle test to any screen other than game over screen
    if $BTEST and not $scene.is_a?(Scene_Gameover)
      $scene = nil
    end
  end
  #--------------------------------------------------------------------------
  # * Determine Battle Win/Loss Results
  #--------------------------------------------------------------------------
  def judge
    # If all dead determinant is true, or number of members in party is 0
    if $game_party.all_dead? or $game_party.actors.size == 0
      # If possible to lose
      if $game_temp.battle_can_lose
        # Return to BGM before battle starts
        $game_system.bgm_play($game_temp.map_bgm)
        # Battle ends
        battle_end(2)
        # Return true
        return true
      end
      # Set game over flag
      $game_temp.gameover = true
      # Return true
      return true
    end
    # Return false if even 1 enemy exists
    for enemy in $game_troop.enemies
      if enemy.exist?
        return false
      end
    end
    # Start after battle phase (win)
    start_phase5
    # Return true
    return true
  end
  #--------------------------------------------------------------------------
  # * Battle Ends
  #     result : results (0:win 1:lose 2:escape)
  #--------------------------------------------------------------------------
  def battle_end(result)
    # Clear in battle flag
    $game_temp.in_battle = false
    # Clear entire party actions flag
    $game_party.clear_actions
    # Remove battle states
    for actor in $game_party.actors
      actor.remove_states_battle
    end
    # Clear enemies
    $game_troop.enemies.clear
    # Call battle callback
    if $game_temp.battle_proc != nil
      $game_temp.battle_proc.call(result)
      $game_temp.battle_proc = nil
    end
    # Switch to map screen
    $scene = Scene_Map.new
  end
  #--------------------------------------------------------------------------
  # * Battle Event Setup
  #--------------------------------------------------------------------------
  def setup_battle_event
    # If battle event is running
    if $game_system.battle_interpreter.running?
      return
    end
    # Search for all battle event pages
    for index in 0...$data_troops[@troop_id].pages.size
      # Get event pages
      page = $data_troops[@troop_id].pages[index]
      # Make event conditions possible for reference with c
      c = page.condition
      # Go to next page if no conditions are appointed
      unless c.turn_valid or c.enemy_valid or
             c.actor_valid or c.switch_valid
        next
      end
      # Go to next page if action has been completed
      if $game_temp.battle_event_flags[index]
        next
      end
      # Confirm turn conditions
      if c.turn_valid
        n = $game_temp.battle_turn
        a = c.turn_a
        b = c.turn_b
        if (b == 0 and n != a) or
           (b > 0 and (n < 1 or n < a or n % b != a % b))
          next
        end
      end
      # Confirm enemy conditions
      if c.enemy_valid
        enemy = $game_troop.enemies[c.enemy_index]
        if enemy == nil or enemy.hp * 100.0 / enemy.maxhp > c.enemy_hp
          next
        end
      end
      # Confirm actor conditions
      if c.actor_valid
        actor = $game_actors[c.actor_id]
        if actor == nil or actor.hp * 100.0 / actor.maxhp > c.actor_hp
          next
        end
      end
      # Confirm switch conditions
      if c.switch_valid
        if $game_switches[c.switch_id] == false
          next
        end
      end
      # Set up event
      $game_system.battle_interpreter.setup(page.list, 0)
      # If this page span is [battle] or [turn]
      if page.span <= 1
        # Set action completed flag
        $game_temp.battle_event_flags[index] = true
      end
      return
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # If battle event is running
    if $game_system.battle_interpreter.running?
      # Update interpreter
      $game_system.battle_interpreter.update
      # If a battler which is forcing actions doesn't exist
      if $game_temp.forcing_battler == nil
        # If battle event has finished running
        unless $game_system.battle_interpreter.running?
          # Rerun battle event set up if battle continues
          unless judge
            setup_battle_event
          end
        end
        # If not after battle phase
        if @phase != 5
          # Refresh status window
          @status_window.refresh
        end
      end
    end
    # Update system (timer) and screen
    $game_system.update
    $game_screen.update
    # If timer has reached 0
    if $game_system.timer_working and $game_system.timer == 0
      # Abort battle
      $game_temp.battle_abort = true
    end
    # Update windows
    @help_window.update
    @party_command_window.update
    @actor_command_window.update
    @status_window.update
    @message_window.update
    # Update sprite set
    @spriteset.update
    # If transition is processing
    if $game_temp.transition_processing
      # Clear transition processing flag
      $game_temp.transition_processing = false
      # Execute transition
      if $game_temp.transition_name == ""
        Graphics.transition(20)
      else
        Graphics.transition(40, "Graphics/Transitions/" +
          $game_temp.transition_name)
      end
    end
    # If message window is showing
    if $game_temp.message_window_showing
      return
    end
    # If effect is showing
    if @spriteset.effect?
      return
    end
    # If game over
    if $game_temp.gameover
      # Switch to game over screen
      $scene = Scene_Gameover.new
      return
    end
    # If returning to title screen
    if $game_temp.to_title
      # Switch to title screen
      $scene = Scene_Title.new
      return
    end
    # If battle is aborted
    if $game_temp.battle_abort
      # Return to BGM used before battle started
      $game_system.bgm_play($game_temp.map_bgm)
      # Battle ends
      battle_end(1)
      return
    end
    # If waiting
    if @wait_count > 0
      # Decrease wait count
      @wait_count -= 1
      return
    end
    # If battler forcing an action doesn't exist,
    # and battle event is running
    if $game_temp.forcing_battler == nil and
       $game_system.battle_interpreter.running?
      return
    end
    # Branch according to phase
    case @phase
    when 1  # pre-battle phase
      update_phase1
    when 2  # party command phase
      update_phase2
    when 3  # actor command phase
      update_phase3
    when 4  # main phase
      update_phase4
    when 5  # after battle phase
      update_phase5
    end
  end
  #--------------------------------------------------------------------------
  # * Start Pre-Battle Phase
  #--------------------------------------------------------------------------
  def start_phase1
    # Shift to phase 1
    @phase = 1
    # Clear all party member actions
    $game_party.clear_actions
    # Set up battle event
    setup_battle_event
  end
  #--------------------------------------------------------------------------
  # * Frame Update (pre-battle phase)
  #--------------------------------------------------------------------------
  def update_phase1
    # Determine win/loss situation
    if judge
      # If won or lost: end method
      return
    end
    # Start party command phase
    start_phase2
  end
  #--------------------------------------------------------------------------
  # * Start Party Command Phase
  #--------------------------------------------------------------------------
  def start_phase2
    # Shift to phase 2
    @phase = 2
    # Set actor to non-selecting
    @actor_index = -1
    @active_battler = nil
    # Enable party command window
    @party_command_window.active = true
    @party_command_window.visible = true
    # Disable actor command window
    @actor_command_window.active = false
    @actor_command_window.visible = false
    # Clear main phase flag
    $game_temp.battle_main_phase = false
    # Clear all party member actions
    $game_party.clear_actions
    # If impossible to input command
    unless $game_party.inputable?
      # Start main phase
      start_phase4
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (party command phase)
  #--------------------------------------------------------------------------
  def update_phase2
    # If C button was pressed
    if Input.trigger?(Input::C)
      # Branch by party command window cursor position
      case @party_command_window.index
      when 0  # fight
        # Play decision SE
        $game_system.se_play($data_system.decision_se)
        # Start actor command phase
        start_phase3
      when 1  # escape
        # If it's not possible to escape
        if $game_temp.battle_can_escape == false
          # Play buzzer SE
          $game_system.se_play($data_system.buzzer_se)
          return
        end
        # Play decision SE
        $game_system.se_play($data_system.decision_se)
        # Escape processing
        update_phase2_escape
      end
      return
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (party command phase: escape)
  #--------------------------------------------------------------------------
  def update_phase2_escape
    # Calculate enemy agility average
    enemies_agi = 0
    enemies_number = 0
    for enemy in $game_troop.enemies
      if enemy.exist?
        enemies_agi += enemy.agi
        enemies_number += 1
      end
    end
    if enemies_number > 0
      enemies_agi /= enemies_number
    end
    # Calculate actor agility average
    actors_agi = 0
    actors_number = 0
    for actor in $game_party.actors
      if actor.exist?
        actors_agi += actor.agi
        actors_number += 1
      end
    end
    if actors_number > 0
      actors_agi /= actors_number
    end
    # Determine if escape is successful
    success = rand(100) < 50 * actors_agi / enemies_agi
    # If escape is successful
    if success
      # Play escape SE
      $game_system.se_play($data_system.escape_se)
      # Return to BGM before battle started
      $game_system.bgm_play($game_temp.map_bgm)
      # Battle ends
      battle_end(1)
    # If escape is failure
    else
      # Clear all party member actions
      $game_party.clear_actions
      # Start main phase
      start_phase4
    end
  end
  #--------------------------------------------------------------------------
  # * Start After Battle Phase
  #--------------------------------------------------------------------------
  def start_phase5
    # Shift to phase 5
    @phase = 5
    # Play battle end ME
    $game_system.me_play($game_system.battle_end_me)
    # Return to BGM before battle started
    $game_system.bgm_play($game_temp.map_bgm)
    # Initialize EXP, amount of gold, and treasure
    exp = 0
    gold = 0
    treasures = []
    # Loop
    for enemy in $game_troop.enemies
      # If enemy is not hidden
      unless enemy.hidden
        # Add EXP and amount of gold obtained
        exp += enemy.exp
        gold += enemy.gold
        # Determine if treasure appears
        if rand(100) < enemy.treasure_prob
          if enemy.item_id > 0
            treasures.push($data_items[enemy.item_id])
          end
          if enemy.weapon_id > 0
            treasures.push($data_weapons[enemy.weapon_id])
          end
          if enemy.armor_id > 0
            treasures.push($data_armors[enemy.armor_id])
          end
        end
      end
    end
    # Treasure is limited to a maximum of 6 items
    treasures = treasures[0..5]
    # Obtaining EXP
    for i in 0...$game_party.actors.size
      actor = $game_party.actors[i]
      if actor.cant_get_exp? == false
        last_level = actor.level
        actor.exp += exp
        if actor.level > last_level
          @status_window.level_up(i)
        end
      end
    end
    # Obtaining gold
    $game_party.gain_gold(gold)
    # Obtaining treasure
    for item in treasures
      case item
      when RPG::Item
        $game_party.gain_item(item.id, 1)
      when RPG::Weapon
        $game_party.gain_weapon(item.id, 1)
      when RPG::Armor
        $game_party.gain_armor(item.id, 1)
      end
    end
    # Make battle result window
    @result_window = Window_BattleResult.new(exp, gold, treasures)
    # Set wait count
    @phase5_wait_count = 100
  end
  #--------------------------------------------------------------------------
  # * Frame Update (after battle phase)
  #--------------------------------------------------------------------------
  def update_phase5
    # If wait count is larger than 0
    if @phase5_wait_count > 0
      # Decrease wait count
      @phase5_wait_count -= 1
      # If wait count reaches 0
      if @phase5_wait_count == 0
        # Show result window
        @result_window.visible = true
        # Clear main phase flag
        $game_temp.battle_main_phase = false
        # Refresh status window
        @status_window.refresh
      end
      return
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # Battle ends
      battle_end(0)
    end
  end
  #--------------------------------------------------------------------------
  # * Start Actor Command Phase
  #--------------------------------------------------------------------------
  def start_phase3
    # Shift to phase 3
    @phase = 3
    # Set actor as unselectable
    @actor_index = -1
    @active_battler = nil
    # Go to command input for next actor
    phase3_next_actor
  end
  #--------------------------------------------------------------------------
  # * Go to Command Input for Next Actor
  #--------------------------------------------------------------------------
  def phase3_next_actor
    # Loop
    begin
      # Actor blink effect OFF
      if @active_battler != nil
        @active_battler.blink = false
      end
      # If last actor
      if @actor_index == $game_party.actors.size-1
        # Start main phase
        start_phase4
        return
      end
      # Advance actor index
      @actor_index += 1
      @active_battler = $game_party.actors[@actor_index]
      @active_battler.blink = true
    # Once more if actor refuses command input
    end until @active_battler.inputable?
    # Set up actor command window
    phase3_setup_command_window
  end
  #--------------------------------------------------------------------------
  # * Go to Command Input of Previous Actor
  #--------------------------------------------------------------------------
  def phase3_prior_actor
    # Loop
    begin
      # Actor blink effect OFF
      if @active_battler != nil
        @active_battler.blink = false
      end
      # If first actor
      if @actor_index == 0
        # Start party command phase
        start_phase2
        return
      end
      # Return to actor index
      @actor_index -= 1
      @active_battler = $game_party.actors[@actor_index]
      @active_battler.blink = true
    # Once more if actor refuses command input
    end until @active_battler.inputable?
    # Set up actor command window
    phase3_setup_command_window
  end
  #--------------------------------------------------------------------------
  # * Actor Command Window Setup
  #--------------------------------------------------------------------------
  def phase3_setup_command_window
    # Disable party command window
    @party_command_window.active = false
    @party_command_window.visible = false
    # Enable actor command window
    @actor_command_window.active = true
    @actor_command_window.visible = true
    # Set actor command window position
    @actor_command_window.x = @actor_index * 160
    # Set index to 0
    @actor_command_window.index = 0
  end
  #--------------------------------------------------------------------------
  # * Frame Update (actor command phase)
  #--------------------------------------------------------------------------
  def update_phase3
    # If enemy arrow is enabled
    if @enemy_arrow != nil
      update_phase3_enemy_select
    # If actor arrow is enabled
    elsif @actor_arrow != nil
      update_phase3_actor_select
    # If skill window is enabled
    elsif @skill_window != nil
      update_phase3_skill_select
    # If item window is enabled
    elsif @item_window != nil
      update_phase3_item_select
    # If actor command window is enabled
    elsif @actor_command_window.active
      update_phase3_basic_command
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (actor command phase : basic command)
  #--------------------------------------------------------------------------
  def update_phase3_basic_command
    # If B button was pressed
    if Input.trigger?(Input::B)
      # Play cancel SE
      $game_system.se_play($data_system.cancel_se)
      # Go to command input for previous actor
      phase3_prior_actor
      return
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # Branch by actor command window cursor position
      case @actor_command_window.index
      when 0  # attack
        # Play decision SE
        $game_system.se_play($data_system.decision_se)
        # Set action
        @active_battler.current_action.kind = 0
        @active_battler.current_action.basic = 0
        # Start enemy selection
        start_enemy_select
      when 1  # skill
        # Play decision SE
        $game_system.se_play($data_system.decision_se)
        # Set action
        @active_battler.current_action.kind = 1
        # Start skill selection
        start_skill_select
      when 2  # guard
        # Play decision SE
        $game_system.se_play($data_system.decision_se)
        # Set action
        @active_battler.current_action.kind = 0
        @active_battler.current_action.basic = 1
        # Go to command input for next actor
        phase3_next_actor
      when 3  # item
        # Play decision SE
        $game_system.se_play($data_system.decision_se)
        # Set action
        @active_battler.current_action.kind = 2
        # Start item selection
        start_item_select
      end
      return
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (actor command phase : skill selection)
  #--------------------------------------------------------------------------
  def update_phase3_skill_select
    # Make skill window visible
    @skill_window.visible = true
    # Update skill window
    @skill_window.update
    # If B button was pressed
    if Input.trigger?(Input::B)
      # Play cancel SE
      $game_system.se_play($data_system.cancel_se)
      # End skill selection
      end_skill_select
      return
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # Get currently selected data on the skill window
      @skill = @skill_window.skill
      # If it can't be used
      if @skill == nil or not @active_battler.skill_can_use?(@skill.id)
        # Play buzzer SE
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      # Play decision SE
      $game_system.se_play($data_system.decision_se)
      # Set action
      @active_battler.current_action.skill_id = @skill.id
      # Make skill window invisible
      @skill_window.visible = false
      # If effect scope is single enemy
      if @skill.scope == 1
        # Start enemy selection
        start_enemy_select
      # If effect scope is single ally
      elsif @skill.scope == 3 or @skill.scope == 5
        # Start actor selection
        start_actor_select
      # If effect scope is not single
      else
        # End skill selection
        end_skill_select
        # Go to command input for next actor
        phase3_next_actor
      end
      return
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (actor command phase : item selection)
  #--------------------------------------------------------------------------
  def update_phase3_item_select
    # Make item window visible
    @item_window.visible = true
    # Update item window
    @item_window.update
    # If B button was pressed
    if Input.trigger?(Input::B)
      # Play cancel SE
      $game_system.se_play($data_system.cancel_se)
      # End item selection
      end_item_select
      return
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # Get currently selected data on the item window
      @item = @item_window.item
      # If it can't be used
      unless $game_party.item_can_use?(@item.id)
        # Play buzzer SE
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      # Play decision SE
      $game_system.se_play($data_system.decision_se)
      # Set action
      @active_battler.current_action.item_id = @item.id
      # Make item window invisible
      @item_window.visible = false
      # If effect scope is single enemy
      if @item.scope == 1
        # Start enemy selection
        start_enemy_select
      # If effect scope is single ally
      elsif @item.scope == 3 or @item.scope == 5
        # Start actor selection
        start_actor_select
      # If effect scope is not single
      else
        # End item selection
        end_item_select
        # Go to command input for next actor
        phase3_next_actor
      end
      return
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Updat (actor command phase : enemy selection)
  #--------------------------------------------------------------------------
  def update_phase3_enemy_select
    # Update enemy arrow
    @enemy_arrow.update
    # If B button was pressed
    if Input.trigger?(Input::B)
      # Play cancel SE
      $game_system.se_play($data_system.cancel_se)
      # End enemy selection
      end_enemy_select
      return
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # Play decision SE
      $game_system.se_play($data_system.decision_se)
      # Set action
      @active_battler.current_action.target_index = @enemy_arrow.index
      # End enemy selection
      end_enemy_select
      # If skill window is showing
      if @skill_window != nil
        # End skill selection
        end_skill_select
      end
      # If item window is showing
      if @item_window != nil
        # End item selection
        end_item_select
      end
      # Go to command input for next actor
      phase3_next_actor
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (actor command phase : actor selection)
  #--------------------------------------------------------------------------
  def update_phase3_actor_select
    # Update actor arrow
    @actor_arrow.update
    # If B button was pressed
    if Input.trigger?(Input::B)
      # Play cancel SE
      $game_system.se_play($data_system.cancel_se)
      # End actor selection
      end_actor_select
      return
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # Play decision SE
      $game_system.se_play($data_system.decision_se)
      # Set action
      @active_battler.current_action.target_index = @actor_arrow.index
      # End actor selection
      end_actor_select
      # If skill window is showing
      if @skill_window != nil
        # End skill selection
        end_skill_select
      end
      # If item window is showing
      if @item_window != nil
        # End item selection
        end_item_select
      end
      # Go to command input for next actor
      phase3_next_actor
    end
  end
  #--------------------------------------------------------------------------
  # * Start Enemy Selection
  #--------------------------------------------------------------------------
  def start_enemy_select
    # Make enemy arrow
    @enemy_arrow = Arrow_Enemy.new(@spriteset.viewport1)
    # Associate help window
    @enemy_arrow.help_window = @help_window
    # Disable actor command window
    @actor_command_window.active = false
    @actor_command_window.visible = false
  end
  #--------------------------------------------------------------------------
  # * End Enemy Selection
  #--------------------------------------------------------------------------
  def end_enemy_select
    # Dispose of enemy arrow
    @enemy_arrow.dispose
    @enemy_arrow = nil
    # If command is [fight]
    if @actor_command_window.index == 0
      # Enable actor command window
      @actor_command_window.active = true
      @actor_command_window.visible = true
      # Hide help window
      @help_window.visible = false
    end
  end
  #--------------------------------------------------------------------------
  # * Start Actor Selection
  #--------------------------------------------------------------------------
  def start_actor_select
    # Make actor arrow
    @actor_arrow = Arrow_Actor.new(@spriteset.viewport2)
    @actor_arrow.index = @actor_index
    # Associate help window
    @actor_arrow.help_window = @help_window
    # Disable actor command window
    @actor_command_window.active = false
    @actor_command_window.visible = false
  end
  #--------------------------------------------------------------------------
  # * End Actor Selection
  #--------------------------------------------------------------------------
  def end_actor_select
    # Dispose of actor arrow
    @actor_arrow.dispose
    @actor_arrow = nil
  end
  #--------------------------------------------------------------------------
  # * Start Skill Selection
  #--------------------------------------------------------------------------
  def start_skill_select
    # Make skill window
    @skill_window = Window_Skill.new(@active_battler)
    # Associate help window
    @skill_window.help_window = @help_window
    # Disable actor command window
    @actor_command_window.active = false
    @actor_command_window.visible = false
  end
  #--------------------------------------------------------------------------
  # * End Skill Selection
  #--------------------------------------------------------------------------
  def end_skill_select
    # Dispose of skill window
    @skill_window.dispose
    @skill_window = nil
    # Hide help window
    @help_window.visible = false
    # Enable actor command window
    @actor_command_window.active = true
    @actor_command_window.visible = true
  end
  #--------------------------------------------------------------------------
  # * Start Item Selection
  #--------------------------------------------------------------------------
  def start_item_select
    # Make item window
    @item_window = Window_Item.new
    # Associate help window
    @item_window.help_window = @help_window
    # Disable actor command window
    @actor_command_window.active = false
    @actor_command_window.visible = false
  end
  #--------------------------------------------------------------------------
  # * End Item Selection
  #--------------------------------------------------------------------------
  def end_item_select
    # Dispose of item window
    @item_window.dispose
    @item_window = nil
    # Hide help window
    @help_window.visible = false
    # Enable actor command window
    @actor_command_window.active = true
    @actor_command_window.visible = true
  end
  #--------------------------------------------------------------------------
  # * Start Main Phase
  #--------------------------------------------------------------------------
  def start_phase4
    # Shift to phase 4
    @phase = 4
    # Turn count
    $game_temp.battle_turn += 1
    # Search all battle event pages
    for index in 0...$data_troops[@troop_id].pages.size
      # Get event page
      page = $data_troops[@troop_id].pages[index]
      # If this page span is [turn]
      if page.span == 1
        # Clear action completed flags
        $game_temp.battle_event_flags[index] = false
      end
    end
    # Set actor as unselectable
    @actor_index = -1
    @active_battler = nil
    # Enable party command window
    @party_command_window.active = false
    @party_command_window.visible = false
    # Disable actor command window
    @actor_command_window.active = false
    @actor_command_window.visible = false
    # Set main phase flag
    $game_temp.battle_main_phase = true
    # Make enemy action
    for enemy in $game_troop.enemies
      enemy.make_action
    end
    # Make action orders
    make_action_orders
    # Shift to step 1
    @phase4_step = 1
  end
  #--------------------------------------------------------------------------
  # * Make Action Orders
  #--------------------------------------------------------------------------
  def make_action_orders
    # Initialize @action_battlers array
    @action_battlers = []
    # Add enemy to @action_battlers array
    for enemy in $game_troop.enemies
      @action_battlers.push(enemy)
    end
    # Add actor to @action_battlers array
    for actor in $game_party.actors
      @action_battlers.push(actor)
    end
    # Decide action speed for all
    for battler in @action_battlers
      battler.make_action_speed
    end
    # Line up action speed in order from greatest to least
    @action_battlers.sort! {|a,b|
      b.current_action.speed - a.current_action.speed }
  end
  #--------------------------------------------------------------------------
  # * Frame Update (main phase)
  #--------------------------------------------------------------------------
  def update_phase4
    case @phase4_step
    when 1
      update_phase4_step1
    when 2
      update_phase4_step2
    when 3
      update_phase4_step3
    when 4
      update_phase4_step4
    when 5
      update_phase4_step5
    when 6
      update_phase4_step6
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (main phase step 1 : action preparation)
  #--------------------------------------------------------------------------
  def update_phase4_step1
    # Hide help window
    @help_window.visible = false
    # Determine win/loss
    if judge
      # If won, or if lost : end method
      return
    end
    # If an action forcing battler doesn't exist
    if $game_temp.forcing_battler == nil
      # Set up battle event
      setup_battle_event
      # If battle event is running
      if $game_system.battle_interpreter.running?
        return
      end
    end
    # If an action forcing battler exists
    if $game_temp.forcing_battler != nil
      # Add to head, or move
      @action_battlers.delete($game_temp.forcing_battler)
      @action_battlers.unshift($game_temp.forcing_battler)
    end
    # If no actionless battlers exist (all have performed an action)
    if @action_battlers.size == 0
      # Start party command phase
      start_phase2
      return
    end
    # Initialize animation ID and common event ID
    @animation1_id = 0
    @animation2_id = 0
    @common_event_id = 0
    # Shift from head of actionless battlers
    @active_battler = @action_battlers.shift
    # If already removed from battle
    if @active_battler.index == nil
      return
    end
    # Slip damage
    if @active_battler.hp > 0 and @active_battler.slip_damage?
      @active_battler.slip_damage_effect
      @active_battler.damage_pop = true
    end
    # Natural removal of states
    @active_battler.remove_states_auto
    # Refresh status window
    @status_window.refresh
    # Shift to step 2
    @phase4_step = 2
  end
  #--------------------------------------------------------------------------
  # * Frame Update (main phase step 2 : start action)
  #--------------------------------------------------------------------------
  def update_phase4_step2
    # If not a forcing action
    unless @active_battler.current_action.forcing
      # If restriction is [normal attack enemy] or [normal attack ally]
      if @active_battler.restriction == 2 or @active_battler.restriction == 3
        # Set attack as an action
        @active_battler.current_action.kind = 0
        @active_battler.current_action.basic = 0
      end
      # If restriction is [cannot perform action]
      if @active_battler.restriction == 4
        # Clear battler being forced into action
        $game_temp.forcing_battler = nil
        # Shift to step 1
        @phase4_step = 1
        return
      end
    end
    # Clear target battlers
    @target_battlers = []
    # Branch according to each action
    case @active_battler.current_action.kind
    when 0  # basic
      make_basic_action_result
    when 1  # skill
      make_skill_action_result
    when 2  # item
      make_item_action_result
    end
    # Shift to step 3
    if @phase4_step == 2
      @phase4_step = 3
    end
  end
  #--------------------------------------------------------------------------
  # * Make Basic Action Results
  #--------------------------------------------------------------------------
  def make_basic_action_result
    # If attack
    if @active_battler.current_action.basic == 0
      # Set anaimation ID
      @animation1_id = @active_battler.animation1_id
      @animation2_id = @active_battler.animation2_id
      # If action battler is enemy
      if @active_battler.is_a?(Game_Enemy)
        if @active_battler.restriction == 3
          target = $game_troop.random_target_enemy
        elsif @active_battler.restriction == 2
          target = $game_party.random_target_actor
        else
          index = @active_battler.current_action.target_index
          target = $game_party.smooth_target_actor(index)
        end
      end
      # If action battler is actor
      if @active_battler.is_a?(Game_Actor)
        if @active_battler.restriction == 3
          target = $game_party.random_target_actor
        elsif @active_battler.restriction == 2
          target = $game_troop.random_target_enemy
        else
          index = @active_battler.current_action.target_index
          target = $game_troop.smooth_target_enemy(index)
        end
      end
      # Set array of targeted battlers
      @target_battlers = [target]
      # Apply normal attack results
      for target in @target_battlers
        target.attack_effect(@active_battler)
      end
      return
    end
    # If guard
    if @active_battler.current_action.basic == 1
      # Display "Guard" in help window
      @help_window.set_text($data_system.words.guard, 1)
      return
    end
    # If escape
    if @active_battler.is_a?(Game_Enemy) and
       @active_battler.current_action.basic == 2
      # Display "Escape" in help window
      @help_window.set_text("Escape", 1)
      # Escape
      @active_battler.escape
      return
    end
    # If doing nothing
    if @active_battler.current_action.basic == 3
      # Clear battler being forced into action
      $game_temp.forcing_battler = nil
      # Shift to step 1
      @phase4_step = 1
      return
    end
  end
  #--------------------------------------------------------------------------
  # * Set Targeted Battler for Skill or Item
  #     scope : effect scope for skill or item
  #--------------------------------------------------------------------------
  def set_target_battlers(scope)
    # If battler performing action is enemy
    if @active_battler.is_a?(Game_Enemy)
      # Branch by effect scope
      case scope
      when 1  # single enemy
        index = @active_battler.current_action.target_index
        @target_battlers.push($game_party.smooth_target_actor(index))
      when 2  # all enemies
        for actor in $game_party.actors
          if actor.exist?
            @target_battlers.push(actor)
          end
        end
      when 3  # single ally
        index = @active_battler.current_action.target_index
        @target_battlers.push($game_troop.smooth_target_enemy(index))
      when 4  # all allies
        for enemy in $game_troop.enemies
          if enemy.exist?
            @target_battlers.push(enemy)
          end
        end
      when 5  # single ally (HP 0) 
        index = @active_battler.current_action.target_index
        enemy = $game_troop.enemies[index]
        if enemy != nil and enemy.hp0?
          @target_battlers.push(enemy)
        end
      when 6  # all allies (HP 0) 
        for enemy in $game_troop.enemies
          if enemy != nil and enemy.hp0?
            @target_battlers.push(enemy)
          end
        end
      when 7  # user
        @target_battlers.push(@active_battler)
      end
    end
    # If battler performing action is actor
    if @active_battler.is_a?(Game_Actor)
      # Branch by effect scope
      case scope
      when 1  # single enemy
        index = @active_battler.current_action.target_index
        @target_battlers.push($game_troop.smooth_target_enemy(index))
      when 2  # all enemies
        for enemy in $game_troop.enemies
          if enemy.exist?
            @target_battlers.push(enemy)
          end
        end
      when 3  # single ally
        index = @active_battler.current_action.target_index
        @target_battlers.push($game_party.smooth_target_actor(index))
      when 4  # all allies
        for actor in $game_party.actors
          if actor.exist?
            @target_battlers.push(actor)
          end
        end
      when 5  # single ally (HP 0) 
        index = @active_battler.current_action.target_index
        actor = $game_party.actors[index]
        if actor != nil and actor.hp0?
          @target_battlers.push(actor)
        end
      when 6  # all allies (HP 0) 
        for actor in $game_party.actors
          if actor != nil and actor.hp0?
            @target_battlers.push(actor)
          end
        end
      when 7  # user
        @target_battlers.push(@active_battler)
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Make Skill Action Results
  #--------------------------------------------------------------------------
  def make_skill_action_result
    # Get skill
    @skill = $data_skills[@active_battler.current_action.skill_id]
    # If not a forcing action
    unless @active_battler.current_action.forcing
      # If unable to use due to SP running out
      unless @active_battler.skill_can_use?(@skill.id)
        # Clear battler being forced into action
        $game_temp.forcing_battler = nil
        # Shift to step 1
        @phase4_step = 1
        return
      end
    end
    # Use up SP
    @active_battler.sp -= @skill.sp_cost
    # Refresh status window
    @status_window.refresh
    # Show skill name on help window
    @help_window.set_text(@skill.name, 1)
    # Set animation ID
    @animation1_id = @skill.animation1_id
    @animation2_id = @skill.animation2_id
    # Set command event ID
    @common_event_id = @skill.common_event_id
    # Set target battlers
    set_target_battlers(@skill.scope)
    # Apply skill effect
    for target in @target_battlers
      target.skill_effect(@active_battler, @skill)
    end
  end
  #--------------------------------------------------------------------------
  # * Make Item Action Results
  #--------------------------------------------------------------------------
  def make_item_action_result
    # Get item
    @item = $data_items[@active_battler.current_action.item_id]
    # If unable to use due to items running out
    unless $game_party.item_can_use?(@item.id)
      # Shift to step 1
      @phase4_step = 1
      return
    end
    # If consumable
    if @item.consumable
      # Decrease used item by 1
      $game_party.lose_item(@item.id, 1)
    end
    # Display item name on help window
    @help_window.set_text(@item.name, 1)
    # Set animation ID
    @animation1_id = @item.animation1_id
    @animation2_id = @item.animation2_id
    # Set common event ID
    @common_event_id = @item.common_event_id
    # Decide on target
    index = @active_battler.current_action.target_index
    target = $game_party.smooth_target_actor(index)
    # Set targeted battlers
    set_target_battlers(@item.scope)
    # Apply item effect
    for target in @target_battlers
      target.item_effect(@item)
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (main phase step 3 : animation for action performer)
  #--------------------------------------------------------------------------
  def update_phase4_step3
    # Animation for action performer (if ID is 0, then white flash)
    if @animation1_id == 0
      @active_battler.white_flash = true
    else
      @active_battler.animation_id = @animation1_id
      @active_battler.animation_hit = true
    end
    # Shift to step 4
    @phase4_step = 4
  end
  #--------------------------------------------------------------------------
  # * Frame Update (main phase step 4 : animation for target)
  #--------------------------------------------------------------------------
  def update_phase4_step4
    # Animation for target
    for target in @target_battlers
      target.animation_id = @animation2_id
      target.animation_hit = (target.damage != "Miss")
    end
    # Animation has at least 8 frames, regardless of its length
    @wait_count = 8
    # Shift to step 5
    @phase4_step = 5
  end
  #--------------------------------------------------------------------------
  # * Frame Update (main phase step 5 : damage display)
  #--------------------------------------------------------------------------
  def update_phase4_step5
    # Hide help window
    @help_window.visible = false
    # Refresh status window
    @status_window.refresh
    # Display damage
    for target in @target_battlers
      if target.damage != nil
        target.damage_pop = true
      end
    end
    # Shift to step 6
    @phase4_step = 6
  end
  #--------------------------------------------------------------------------
  # * Frame Update (main phase step 6 : refresh)
  #--------------------------------------------------------------------------
  def update_phase4_step6
    # Clear battler being forced into action
    $game_temp.forcing_battler = nil
    # If common event ID is valid
    if @common_event_id > 0
      # Set up event
      common_event = $data_common_events[@common_event_id]
      $game_system.battle_interpreter.setup(common_event.list, 0)
    end
    # Shift to step 1
    @phase4_step = 1
  end
end
#==============================================================================
# ** Scene_Shop
#------------------------------------------------------------------------------
#  This class performs shop screen processing.
#==============================================================================

class Scene_Shop
  #--------------------------------------------------------------------------
  # * Main Processing
  #--------------------------------------------------------------------------
  def main
    # Make help window
    @help_window = Window_Help.new
    # Make command window
    @command_window = Window_ShopCommand.new
    # Make gold window
    @gold_window = Window_Gold.new
    @gold_window.x = 480
    @gold_window.y = 64
    # Make dummy window
    @dummy_window = Window_Base.new(0, 128, 640, 352)
    # Make buy window
    @buy_window = Window_ShopBuy.new($game_temp.shop_goods)
    @buy_window.active = false
    @buy_window.visible = false
    @buy_window.help_window = @help_window
    # Make sell window
    @sell_window = Window_ShopSell.new
    @sell_window.active = false
    @sell_window.visible = false
    @sell_window.help_window = @help_window
    # Make quantity input window
    @number_window = Window_ShopNumber.new
    @number_window.active = false
    @number_window.visible = false
    # Make status window
    @status_window = Window_ShopStatus.new
    @status_window.visible = false
    # Execute transition
    Graphics.transition
    # Main loop
    loop do
      # Update game screen
      Graphics.update
      # Update input information
      Input.update
      # Frame update
      update
      # Abort loop if screen is changed
      if $scene != self
        break
      end
    end
    # Prepare for transition
    Graphics.freeze
    # Dispose of windows
    @help_window.dispose
    @command_window.dispose
    @gold_window.dispose
    @dummy_window.dispose
    @buy_window.dispose
    @sell_window.dispose
    @number_window.dispose
    @status_window.dispose
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # Update windows
    @help_window.update
    @command_window.update
    @gold_window.update
    @dummy_window.update
    @buy_window.update
    @sell_window.update
    @number_window.update
    @status_window.update
    # If command window is active: call update_command
    if @command_window.active
      update_command
      return
    end
    # If buy window is active: call update_buy
    if @buy_window.active
      update_buy
      return
    end
    # If sell window is active: call update_sell
    if @sell_window.active
      update_sell
      return
    end
    # If quantity input window is active: call update_number
    if @number_window.active
      update_number
      return
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (when command window is active)
  #--------------------------------------------------------------------------
  def update_command
    # If B button was pressed
    if Input.trigger?(Input::B)
      # Play cancel SE
      $game_system.se_play($data_system.cancel_se)
      # Switch to map screen
      $scene = Scene_Map.new
      return
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # Branch by command window cursor position
      case @command_window.index
      when 0  # buy
        # Play decision SE
        $game_system.se_play($data_system.decision_se)
        # Change windows to buy mode
        @command_window.active = false
        @dummy_window.visible = false
        @buy_window.active = true
        @buy_window.visible = true
        @buy_window.refresh
        @status_window.visible = true
      when 1  # sell
        # Play decision SE
        $game_system.se_play($data_system.decision_se)
        # Change windows to sell mode
        @command_window.active = false
        @dummy_window.visible = false
        @sell_window.active = true
        @sell_window.visible = true
        @sell_window.refresh
      when 2  # quit
        # Play decision SE
        $game_system.se_play($data_system.decision_se)
        # Switch to map screen
        $scene = Scene_Map.new
      end
      return
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (when buy window is active)
  #--------------------------------------------------------------------------
  def update_buy
    # Set status window item
    @status_window.item = @buy_window.item
    # If B button was pressed
    if Input.trigger?(Input::B)
      # Play cancel SE
      $game_system.se_play($data_system.cancel_se)
      # Change windows to initial mode
      @command_window.active = true
      @dummy_window.visible = true
      @buy_window.active = false
      @buy_window.visible = false
      @status_window.visible = false
      @status_window.item = nil
      # Erase help text
      @help_window.set_text("")
      return
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # Get item
      @item = @buy_window.item
      # If item is invalid, or price is higher than money possessed
      if @item == nil or @item.price > $game_party.gold
        # Play buzzer SE
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      # Get items in possession count
      case @item
      when RPG::Item
        number = $game_party.item_number(@item.id)
      when RPG::Weapon
        number = $game_party.weapon_number(@item.id)
      when RPG::Armor
        number = $game_party.armor_number(@item.id)
      end
      # If 99 items are already in possession
      if number == 99
        # Play buzzer SE
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      # Play decision SE
      $game_system.se_play($data_system.decision_se)
      # Calculate maximum amount possible to buy
      max = @item.price == 0 ? 99 : $game_party.gold / @item.price
      max = [max, 99 - number].min
      # Change windows to quantity input mode
      @buy_window.active = false
      @buy_window.visible = false
      @number_window.set(@item, max, @item.price)
      @number_window.active = true
      @number_window.visible = true
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (when sell window is active)
  #--------------------------------------------------------------------------
  def update_sell
    # If B button was pressed
    if Input.trigger?(Input::B)
      # Play cancel SE
      $game_system.se_play($data_system.cancel_se)
      # Change windows to initial mode
      @command_window.active = true
      @dummy_window.visible = true
      @sell_window.active = false
      @sell_window.visible = false
      @status_window.item = nil
      # Erase help text
      @help_window.set_text("")
      return
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # Get item
      @item = @sell_window.item
      # Set status window item
      @status_window.item = @item
      # If item is invalid, or item price is 0 (unable to sell)
      if @item == nil or @item.price == 0
        # Play buzzer SE
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      # Play decision SE
      $game_system.se_play($data_system.decision_se)
      # Get items in possession count
      case @item
      when RPG::Item
        number = $game_party.item_number(@item.id)
      when RPG::Weapon
        number = $game_party.weapon_number(@item.id)
      when RPG::Armor
        number = $game_party.armor_number(@item.id)
      end
      # Maximum quanitity to sell = number of items in possession
      max = number
      # Change windows to quantity input mode
      @sell_window.active = false
      @sell_window.visible = false
      @number_window.set(@item, max, @item.price / 2)
      @number_window.active = true
      @number_window.visible = true
      @status_window.visible = true
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (when quantity input window is active)
  #--------------------------------------------------------------------------
  def update_number
    # If B button was pressed
    if Input.trigger?(Input::B)
      # Play cancel SE
      $game_system.se_play($data_system.cancel_se)
      # Set quantity input window to inactive / invisible
      @number_window.active = false
      @number_window.visible = false
      # Branch by command window cursor position
      case @command_window.index
      when 0  # buy
        # Change windows to buy mode
        @buy_window.active = true
        @buy_window.visible = true
      when 1  # sell
        # Change windows to sell mode
        @sell_window.active = true
        @sell_window.visible = true
        @status_window.visible = false
      end
      return
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # Play shop SE
      $game_system.se_play($data_system.shop_se)
      # Set quantity input window to inactive / invisible
      @number_window.active = false
      @number_window.visible = false
      # Branch by command window cursor position
      case @command_window.index
      when 0  # buy
        # Buy process
        $game_party.lose_gold(@number_window.number * @item.price)
        case @item
        when RPG::Item
          $game_party.gain_item(@item.id, @number_window.number)
        when RPG::Weapon
          $game_party.gain_weapon(@item.id, @number_window.number)
        when RPG::Armor
          $game_party.gain_armor(@item.id, @number_window.number)
        end
        # Refresh each window
        @gold_window.refresh
        @buy_window.refresh
        @status_window.refresh
        # Change windows to buy mode
        @buy_window.active = true
        @buy_window.visible = true
      when 1  # sell
        # Sell process
        $game_party.gain_gold(@number_window.number * (@item.price / 2))
        case @item
        when RPG::Item
          $game_party.lose_item(@item.id, @number_window.number)
        when RPG::Weapon
          $game_party.lose_weapon(@item.id, @number_window.number)
        when RPG::Armor
          $game_party.lose_armor(@item.id, @number_window.number)
        end
        # Refresh each window
        @gold_window.refresh
        @sell_window.refresh
        @status_window.refresh
        # Change windows to sell mode
        @sell_window.active = true
        @sell_window.visible = true
        @status_window.visible = false
      end
      return
    end
  end
end
#==============================================================================
# ** Scene_Name
#------------------------------------------------------------------------------
#  This class performs name input screen processing.
#==============================================================================

class Scene_Name
  #--------------------------------------------------------------------------
  # * Main Processing
  #--------------------------------------------------------------------------
  def main
    # Get actor
    @actor = $game_actors[$game_temp.name_actor_id]
    # Make windows
    @edit_window = Window_NameEdit.new(@actor, $game_temp.name_max_char)
    @input_window = Window_NameInput.new
    # Execute transition
    Graphics.transition
    # Main loop
    loop do
      # Update game screen
      Graphics.update
      # Update input information
      Input.update
      # Frame update
      update
      # Abort loop if screen is changed
      if $scene != self
        break
      end
    end
    # Prepare for transition
    Graphics.freeze
    # Dispose of windows
    @edit_window.dispose
    @input_window.dispose
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # Update windows
    @edit_window.update
    @input_window.update
    # If B button was pressed
    if Input.repeat?(Input::B)
      # If cursor position is at 0
      if @edit_window.index == 0
        return
      end
      # Play cancel SE
      $game_system.se_play($data_system.cancel_se)
      # Delete text
      @edit_window.back
      return
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # If cursor position is at [OK]
      if @input_window.character == nil
        # If name is empty
        if @edit_window.name == ""
          # Return to default name
          @edit_window.restore_default
          # If name is empty
          if @edit_window.name == ""
            # Play buzzer SE
            $game_system.se_play($data_system.buzzer_se)
            return
          end
          # Play decision SE
          $game_system.se_play($data_system.decision_se)
          return
        end
        # Change actor name
        @actor.name = @edit_window.name
        # Play decision SE
        $game_system.se_play($data_system.decision_se)
        # Switch to map screen
        $scene = Scene_Map.new
        return
      end
      # If cursor position is at maximum
      if @edit_window.index == $game_temp.name_max_char
        # Play buzzer SE
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      # If text character is empty
      if @input_window.character == ""
        # Play buzzer SE
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      # Play decision SE
      $game_system.se_play($data_system.decision_se)
      # Add text character
      @edit_window.add(@input_window.character)
      return
    end
  end
end
#==============================================================================
# ** Scene_Gameover
#------------------------------------------------------------------------------
#  This class performs game over screen processing.
#==============================================================================

class Scene_Gameover
  #--------------------------------------------------------------------------
  # * Main Processing
  #--------------------------------------------------------------------------
  def main
    # Make game over graphic
    @sprite = Sprite.new
    @sprite.bitmap = RPG::Cache.gameover($data_system.gameover_name)
    # Stop BGM and BGS
    $game_system.bgm_play(nil)
    $game_system.bgs_play(nil)
    # Play game over ME
    $game_system.me_play($data_system.gameover_me)
    # Execute transition
    Graphics.transition(120)
    # Main loop
    loop do
      # Update game screen
      Graphics.update
      # Update input information
      Input.update
      # Frame update
      update
      # Abort loop if screen is changed
      if $scene != self
        break
      end
    end
    # Prepare for transition
    Graphics.freeze
    # Dispose of game over graphic
    @sprite.bitmap.dispose
    @sprite.dispose
    # Execute transition
    Graphics.transition(40)
    # Prepare for transition
    Graphics.freeze
    # If battle test
    if $BTEST
      $scene = nil
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # If C button was pressed
    if Input.trigger?(Input::C)
      # Switch to title screen
      $scene = Scene_Title.new
    end
  end
end
#==============================================================================
# ** Scene_Debug
#------------------------------------------------------------------------------
#  This class performs debug screen processing.
#==============================================================================

class Scene_Debug
  #--------------------------------------------------------------------------
  # * Main Processing
  #--------------------------------------------------------------------------
  def main
    # Make windows
    @left_window = Window_DebugLeft.new
    @right_window = Window_DebugRight.new
    @help_window = Window_Base.new(192, 352, 448, 128)
    @help_window.contents = Bitmap.new(406, 96)
    # Restore previously selected item
    @left_window.top_row = $game_temp.debug_top_row
    @left_window.index = $game_temp.debug_index
    @right_window.mode = @left_window.mode
    @right_window.top_id = @left_window.top_id
    # Execute transition
    Graphics.transition
    # Main loop
    loop do
      # Update game screen
      Graphics.update
      # Update input information
      Input.update
      # Frame update
      update
      # Abort loop if screen is changed
      if $scene != self
        break
      end
    end
    # Refresh map
    $game_map.refresh
    # Prepare for transition
    Graphics.freeze
    # Dispose of windows
    @left_window.dispose
    @right_window.dispose
    @help_window.dispose
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # Update windows
    @right_window.mode = @left_window.mode
    @right_window.top_id = @left_window.top_id
    @left_window.update
    @right_window.update
    # Memorize selected item
    $game_temp.debug_top_row = @left_window.top_row
    $game_temp.debug_index = @left_window.index
    # If left window is active: call update_left
    if @left_window.active
      update_left
      return
    end
    # If right window is active: call update_right
    if @right_window.active
      update_right
      return
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (when left window is active)
  #--------------------------------------------------------------------------
  def update_left
    # If B button was pressed
    if Input.trigger?(Input::B)
      # Play cancel SE
      $game_system.se_play($data_system.cancel_se)
      # Switch to map screen
      $scene = Scene_Map.new
      return
    end
    # If C button was pressed
    if Input.trigger?(Input::C)
      # Play decision SE
      $game_system.se_play($data_system.decision_se)
      # Display help
      if @left_window.mode == 0
        text1 = "C (Enter) : ON / OFF"
        @help_window.contents.draw_text(4, 0, 406, 32, text1)
      else
        text1 = "Left : -1   Right : +1"
        text2 = "L (Pageup) : -10"
        text3 = "R (Pagedown) : +10"
        @help_window.contents.draw_text(4, 0, 406, 32, text1)
        @help_window.contents.draw_text(4, 32, 406, 32, text2)
        @help_window.contents.draw_text(4, 64, 406, 32, text3)
      end
      # Activate right window
      @left_window.active = false
      @right_window.active = true
      @right_window.index = 0
      return
    end
  end
  #--------------------------------------------------------------------------
  # * Frame Update (when right window is active)
  #--------------------------------------------------------------------------
  def update_right
    # If B button was pressed
    if Input.trigger?(Input::B)
      # Play cancel SE
      $game_system.se_play($data_system.cancel_se)
      # Activate left window
      @left_window.active = true
      @right_window.active = false
      @right_window.index = -1
      # Erase help
      @help_window.contents.clear
      return
    end
    # Get selected switch / variable ID
    current_id = @right_window.top_id + @right_window.index
    # If switch
    if @right_window.mode == 0
      # If C button was pressed
      if Input.trigger?(Input::C)
        # Play decision SE
        $game_system.se_play($data_system.decision_se)
        # Reverse ON / OFF
        $game_switches[current_id] = (not $game_switches[current_id])
        @right_window.refresh
        return
      end
    end
    # If variable
    if @right_window.mode == 1
      # If right button was pressed
      if Input.repeat?(Input::RIGHT)
        # Play cursor SE
        $game_system.se_play($data_system.cursor_se)
        # Increase variables by 1
        $game_variables[current_id] += 1
        # Maximum limit check
        if $game_variables[current_id] > 99999999
          $game_variables[current_id] = 99999999
        end
        @right_window.refresh
        return
      end
      # If left button was pressed
      if Input.repeat?(Input::LEFT)
        # Play cursor SE
        $game_system.se_play($data_system.cursor_se)
        # Decrease variables by 1
        $game_variables[current_id] -= 1
        # Minimum limit check
        if $game_variables[current_id] < -99999999
          $game_variables[current_id] = -99999999
        end
        @right_window.refresh
        return
      end
      # If R button was pressed
      if Input.repeat?(Input::R)
        # Play cursor SE
        $game_system.se_play($data_system.cursor_se)
        # Increase variables by 10
        $game_variables[current_id] += 10
        # Maximum limit check
        if $game_variables[current_id] > 99999999
          $game_variables[current_id] = 99999999
        end
        @right_window.refresh
        return
      end
      # If L button was pressed
      if Input.repeat?(Input::L)
        # Play cursor SE
        $game_system.se_play($data_system.cursor_se)
        # Decrease variables by 10
        $game_variables[current_id] -= 10
        # Minimum limit check
        if $game_variables[current_id] < -99999999
          $game_variables[current_id] = -99999999
        end
        @right_window.refresh
        return
      end
    end
  end
end
#==============================================================================
# ** Main
#------------------------------------------------------------------------------
#  After defining each class, actual processing begins here.
#==============================================================================

begin
  # Prepare for transition
  Graphics.freeze
  # Make scene object (title screen)
  $scene = Scene_Title.new
  # Call main method as long as $scene is effective
  while $scene != nil
    $scene.main
  end
  # Fade out
  Graphics.transition(20)
rescue Errno::ENOENT
  # Supplement Errno::ENOENT exception
  # If unable to open file, display message and end
  filename = $!.message.sub("No such file or directory - ", "")
  print("Unable to find file #{filename}.")
end



