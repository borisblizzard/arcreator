#==============================================================================
# Game_Battler (1)
#==============================================================================


class Game_Battler
  
  attr_reader   :battler_hue
  attr_reader   :states
  attr_accessor :hidden
  attr_accessor :immortal
  attr_accessor :damage_pop
  attr_accessor :damage
  attr_accessor :critical
  attr_accessor :animation_id
  attr_accessor :animation_hit
  attr_accessor :white_flash
  attr_accessor :blink
  attr_accessor :anima_index
  attr_accessor :anima_count
  attr_accessor :current_action
  attr_accessor :disappear
  attr_accessor :can_slip_damage
  
  def initialize
    @battler_name, @states, @states_turn = '', [], {}
    @battler_hue = @hp = @sp = @maxhp_plus = @maxsp_plus = @str_plus =
    @dex_plus = @agi_plus = @int_plus = @animation_id = @anima_count =
    @anima_index = 0
    @hidden = @immortal = @damage_pop = @critical = @animation_hit =
    @white_flash = @blink = false
    @can_slip_damage = true
    @damage = nil
    @current_action = Game_BattleAction.new
  end
  
  def save
    @states = @states.clone
    @states_turn = @states_turn.clone
  end
  
  def battler_name2
    return @battler_name
  end
    
  def battler_name
    if $game_actors == nil ||
        self != $game_actors[CP::Cache::Sydon]
      return @battler_name
    end
    return @battler_name + @add_on if $game_temp.trance != nil
    @add_on = ''
    @states.each {|id|
        if self.dragon_skills(id).size > 0
          @add_on = id.to_s
          break
        end}
    return @battler_name + @add_on
  end
  
  def dragon_skills(id)
    return []
  end
  
  def hp
    return 0 if @hp < 0
    max_hp = self.maxhp
    return max_hp if @hp > max_hp
    return @hp
  end
  
  def sp
    return 0 if @sp < 0
    max_sp = self.maxsp
    return max_sp if @sp > max_sp
    return @sp
  end
  
  def maxhp
    n = base_maxhp + @maxhp_plus
    if n < 1
      n = 1
    elsif n > 9999999
      n = 9999999
    end
    @states.each {|i| n *= $data_states[i].maxhp_rate / 100.0}
    n = n.to_i
    return 1 if n < 1
    return 9999999 if n > 9999999
    return n
  end
  
  def maxsp
    n = base_maxsp + @maxsp_plus
    if n < 0
      n = 0
    elsif n > 999
      n = 999
    end
    @states.each {|i| n *= $data_states[i].maxsp_rate / 100.0}
    n = n.to_i
    return 0 if n < 0
    return 999 if n > 999
    return n
  end
  
  def str
    n = base_str + @str_plus
    if n < 1
      n = 1
    elsif n > 999
      n = 999
    end
    @states.each {|i| n *= $data_states[i].str_rate / 100.0}
    n = n.to_i
    return 1 if n < 1
    return 999 if n > 999
    return n
  end
  
  def dex
    n = base_dex + @dex_plus
    if n < 1
      n = 1
    elsif n > 999
      n = 999
    end
    @states.each {|i| n *= $data_states[i].dex_rate / 100.0}
    n = n.to_i
    return 1 if n < 1
    return 999 if n > 999
    return n
  end
  
  def agi
    n = base_agi + @agi_plus
    if n < 1
      n = 1
    elsif n > 999
      n = 999
    end
    @states.each {|i| n *= $data_states[i].agi_rate / 100.0}
    n = n.to_i
    return 1 if n < 1
    return 999 if n > 999
    return n
  end
  
  def int
    n = base_int + @int_plus
    if n < 1
      n = 1
    elsif n > 999
      n = 999
    end
    @states.each {|i| n *= $data_states[i].int_rate / 100.0}
    n = n.to_i
    return 1 if n < 1
    return 999 if n > 999
    return n
  end
  
  def maxhp=(maxhp)
    max_hp = self.maxhp
    @maxhp_plus = @maxhp_plus + maxhp - max_hp
    if @maxhp_plus < -9999
      @maxhp_plus = -9999
    elsif @maxhp_plus > 9999
      @maxhp_plus = 9999
    end
    @hp = max_hp if @hp > max_hp
  end
  
  def maxsp=(maxsp)
    max_sp = self.maxsp
    @maxsp_plus = @maxsp_plus + maxsp - max_sp
    if @maxsp_plus < -999
      @maxsp_plus = -999
    elsif @maxsp_plus > 999
      @maxsp_plus = 999
    end
    @sp = max_sp if @sp > max_sp
  end
  
  def str=(str)
    @str_plus = @str_plus + str - self.str
    if @str_plus < -999
      @str_plus = -999
    elsif @str_plus > 999
      @str_plus = 999
    end
  end
  
  def dex=(dex)
    @dex_plus = @dex_plus + dex - self.dex
    if @dex_plus < -999
      @dex_plus = -999
    elsif @dex_plus > 999
      @dex_plus = 999
    end
  end
  
  def agi=(agi)
    @agi_plus = @agi_plus + agi - self.agi
    if @agi_plus < -999
      @agi_plus = -999
    elsif @agi_plus > 999
      @agi_plus = 999
    end
  end
  
  def int=(int)
    @int_plus = @int_plus + int - self.int
    if @int_plus < -999
      @int_plus = -999
    elsif @int_plus > 999
      @int_plus = 999
    end
  end
  
  def hit
    n = 100
    @states.each {|i| n *= $data_states[i].hit_rate / 100.0}
    return n.to_i
  end
  
  def atk
    n = base_atk
    @states.each {|i| n *= $data_states[i].atk_rate / 100.0}
    return n.to_i
  end
  
  def pdef
    n = base_pdef
    @states.each {|i| n *= $data_states[i].pdef_rate / 100.0}
    return n.to_i
  end
  
  def mdef
    n = base_mdef
    @states.each {|i| n *= $data_states[i].mdef_rate / 100.0}
    return n.to_i
  end
  
  def eva
    n = base_eva
    @states.each {|i| n += $data_states[i].eva}
    return n
  end
  
  def hp=(hp)
    if hp < 0
      @hp = 0
    else
      max_hp = self.maxhp
      @hp = (hp > max_hp ? max_hp : hp)
    end
    if dead? 
      (1...$data_states.size).each {|i| add_state(i) if $data_states[i].zero_hp}
    else
      (1...$data_states.size).each {|i| remove_state(i) if $data_states[i].zero_hp}
    end
  end
  
  def sp=(sp)
    if sp < 0
      @sp = 0
    else
      max_sp = self.maxsp
      @sp = (sp > max_sp ? max_sp : sp)
    end
  end
  
  def recover_all
    @hp, @sp = self.maxhp, self.maxsp
    (@states - CP::Cache::PositiveStates).each {|i| remove_state(i)}
  end
  
  def dead?
    return (@hp == 0 && !@immortal)
  end
  
  def exist?
    return (!@hidden && (@hp > 0 || @immortal))
  end
  
  def hp0?
    return (!@hidden && @hp == 0)
  end
  
  def inputable?
    return (!@hidden && restriction <= 1)
  end
  
  def movable?
    return (!@hidden && restriction < 4)
  end
  
  def confused?
    return (restriction == 3)
  end
  
  def can_counter?
    return (!self.dead? && self.meta == 18 && restriction < 4)
  end
  
  def coverable?
    return (!self.dead?)
  end
  
  def guarding?
    return (@current_action.kind == 0 && @current_action.basic == 1 && @current_action.target_index == self.index)
  end
  
  def resting?
    return (@current_action.kind == 0 && @current_action.basic == 3 && @current_action.target_index == self.index)
  end
  
  def hide_battler
    @old_battler, @battler_name = @battler_name, 'empty'
  end
  
  def return_battler
    if @old_battler != nil
      @battler_name, @old_battler = @old_battler, nil
    end
  end
  
end
