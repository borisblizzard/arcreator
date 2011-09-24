#============================================================================== 
# Game_System 
#============================================================================== 

class Game_System
  
  attr_reader   :map_interpreter
  attr_reader   :battle_interpreter
  attr_accessor :timer
  attr_accessor :timer_working
  attr_accessor :save_disabled
  attr_accessor :menu_disabled
  attr_accessor :encounter_disabled
  attr_accessor :message_position
  attr_accessor :message_frame
  attr_accessor :save_count
  attr_accessor :magic_number
  attr_accessor :battle_bgm
  attr_accessor :battle_end_me
  attr_accessor :exp_rate
  attr_accessor :gold_rate
  attr_accessor :exerion
  attr_reader   :playing_bgm
  attr_reader   :bgm_list
  
  def initialize 
    @map_interpreter = Interpreter.new(0, true) 
    @battle_interpreter = Interpreter.new(0, false)
    @timer = 0 
    @timer_working = @save_disabled = @menu_disabled = @encounter_disabled = false
    @message_position = 2 
    @message_frame = @save_count = @magic_number = 0
    @exp_rate = 1
    @gold_rate = 1
    @exerion = false
    unlock_bgm((0..5).to_a)
  end
  
  def unlock_bgm(bgm)
    @bgm_list = [] if @bgm_list == nil
    @bgm_list |= (bgm.is_a?(Array) ? bgm : [bgm])
    @bgm_list.sort!
  end
  
  def unlock_all_bgms
    @bgm_list = (0..CP::MAX_BGMS).to_a
  end
  
  def set_exp_rate(rate)
    @exp_rate = rate
  end
  
  def set_gold_rate(rate)
    @gold_rate = rate
  end
  
  def bgm_fade(time) 
    @playing_bgm = nil 
    Audio.bgm_fade(time * 1000) 
  end 
  
  def bgm_memorize 
    @memorized_bgm = @playing_bgm 
  end 
  
  def bgm_restore 
    @playing_bgm = @memorized_bgm
  end 
  
  def bgs_fade(time) 
    @playing_bgs = nil 
    Audio.bgs_fade(time * 1000) 
  end 
  
  def bgs_memorize 
    @memorized_bgs = @playing_bgs 
  end 
  
  def bgs_restore 
    bgs_play(@memorized_bgs) 
  end 
  
  def playing_bgm 
    return @playing_bgm 
  end 
  
  def playing_bgs 
    return @playing_bgs 
  end 
  
  def windowskin_name 
    return $data_system.windowskin_name if @windowskin_name == nil
    return @windowskin_name 
  end 
  
  def windowskin_name=(windowskin_name) 
    @windowskin_name = windowskin_name 
  end 
  
  def battle_bgm 
    return $data_system.battle_bgm if @battle_bgm == nil
    return @battle_bgm 
  end 
  
  def battle_bgm=(battle_bgm) 
    @battle_bgm = battle_bgm 
  end 
  
  def battle_end_me
    return $data_system.battle_end_me if @battle_end_me == nil 
    return @battle_end_me 
  end 
  
  def battle_end_me=(battle_end_me) 
    @battle_end_me = battle_end_me 
  end 
  
  def update
    if @timer_working && !$game_switches[369]
      $game_switches[367] ? @timer += 1 : @timer -= 1
    end
  end
  
end 
