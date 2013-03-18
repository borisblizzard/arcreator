#==============================================================================
# Game_Battler (2)
#==============================================================================

class Game_Battler
  
  def state_full?(state_id)
    return false unless @states.include?(state_id)
    return (@states_turn[state_id] == $data_states[state_id].hold_turn)
  end
  
  def add_state(state_id)
    return false if $data_states[state_id] == nil
    @states.each {|i|
        if $data_states[i].minus_state_set.include?(state_id) &&
            !$data_states[state_id].minus_state_set.include?(i)
          return false
        end}
    return false if @states.include?(state_id)
    last_restriction = self.restriction
    @states.push(state_id)
    if $data_states[state_id].zero_hp
      @hp = 0
      if !@states.include?(32)
        self.sr = 0 if self.is_a?(Game_Actor)
        @current_action.clear
      end
    elsif self.restriction == 4 ||
        last_restriction == 3 && self.restriction != 3 ||
        last_restriction != 3 && self.restriction == 3
      @current_action.clear
    end
    (1...$data_states.size).each {|i|
        add_state(i) if $data_states[state_id].plus_state_set.include?(i)
        if state_id != 1 || !@states.include?(32)
          remove_state(i) if $data_states[state_id].minus_state_set.include?(i)
        end}
    @states.sort! {|a, b|
        if $data_states[a].rating > $data_states[b].rating
          -1
        elsif $data_states[a].rating < $data_states[b].rating
          +1
        elsif $data_states[a].restriction > $data_states[b].restriction
          -1
        elsif $data_states[a].restriction < $data_states[b].restriction
          +1
        else
          a <=> b
        end}
    @states_turn[state_id] = $data_states[state_id].hold_turn
    @current_action.clear unless movable?
    correct_stats
    return true
  end
    
  def remove_state(state_id)
    return false unless @states.include?(state_id)
    if @hp == 0 && $data_states[state_id].zero_hp
      zero_hp = false
      @states.each {|i|
          if i != state_id && $data_states[i].zero_hp
            zero_hp = true
            break
          end}
      @hp = 1 unless zero_hp
    end
    @states.delete(state_id)
    @states_turn.delete(state_id)
    correct_stats
    return true
  end
  
  def correct_stats
    max_hp = self.maxhp
    @hp = max_hp if @hp > max_hp
    max_sp = self.maxsp
    @sp = max_sp if @sp > max_sp
    if self.is_a?(Game_Actor)
      max_sr = self.maxsr
      @sr = max_sr if @sr > max_sr
    end
  end
  
  def state_animation_id
    if @states.size == 0
      @anima_count = @anima_index = 0
      return 0
    end
    size, state = 0, nil
    loop do
      @anima_index %= @states.size
      state = $data_states[@states[@anima_index]]
      break unless $data_animations[state.animation_id] == nil
      @anima_index += 1
      size += 1
      return 0 if size == @states.size
    end
    loops = 6
    loops = 2 if $data_animations[state.animation_id].frame_max > 30
    if @anima_count > loops * $data_animations[state.animation_id].frame_max
      @anima_count = 0
      @anima_index += 1
    else
      @anima_count += 1
    end
    return state.animation_id
  end
  
  def restriction
    restriction_max = 0
    states = @states.clone
    states.delete(1) if states.include?(32)
    states.each {|i|
        if $data_states[i].restriction >= restriction_max
          restriction_max = $data_states[i].restriction
        end}
    return restriction_max
  end
  
  def cant_get_exp?
    return (@states.any? {|i| $data_states[i].cant_get_exp})
  end
  
  def cant_evade?
    return (@states.any? {|i| $data_states[i].cant_evade})
  end
  
  def slip_damage?
    return (@states.any? {|i| $data_states[i].slip_damage && i != 30})
  end
  
  def remove_states_battle
    @states.clone.each {|i| remove_state(i) if $data_states[i].battle_only}
  end
  
  def remove_states_auto
    @states_turn.keys.clone.each {|i|
        if @states_turn[i] > 0
          if self.is_a?(Game_Enemy) && self.boss &&
              !CP::Cache::PositiveStates.include?(i)
            @states_turn[i] -= 2
            @states_turn[i] = 0 if @states_turn[i] < 0
          else
            @states_turn[i] -= 1
          end
        else
          prob = $data_states[i].auto_release_prob
          if self.is_a?(Game_Enemy) && self.boss &&
              !CP::Cache::PositiveStates.include?(i)
            prob *= 2
          end
          remove_state(i) if rand(100) < prob
        end}
  end
  
  def remove_states_trance
    @states_turn.keys.clone.each {|i|
        if @states_turn[i] <= 0
          remove_state(i) if rand(100) < $data_states[i].auto_release_prob
        end}
  end
  
  def remove_states_shock
    @states.clone.each {|i|
        prob = $data_states[i].shock_release_prob
        if self.is_a?(Game_Enemy) && self.boss &&
            !CP::Cache::PositiveStates.include?(i)
          prob *= 2
        end
        remove_state(i) if rand(100) < prob}
  end
  
  def states_plus(plus_state_set)
    effective = false
    plus_state_set.each {|i|
        unless state_guard?(i)
          effective |= !self.state_full?(i)
          if self.is_a?(Game_Enemy) && self.boss
            probabilities = CP::Cache::StateProbabilitiesBoss
          else
            probabilities = CP::Cache::StateProbabilities
          end
          if $data_states[i].nonresistance || !self.state_full?(i) &&
              rand(100) < probabilities[self.state_ranks[i]]
            @state_changed |= add_state(i)
          end
        end}
    return effective
  end
  
  def state_immune?(plus_state_set)
    return (plus_state_set.all? {|i| self.state_ranks[i] == 6 || state_guard?(i)})
  end
  
  def states_minus(minus_state_set)
    effective = false
    minus_state_set.each {|i|
        effective |= @states.include?(i)
        @state_changed |= remove_state(i)}
    return effective
  end
  
  def regen?
    return (@states.any? {|i| i == 30 && $data_states[i].slip_damage})
  end 
  
  def regen_effect
    self.damage = -self.maxhp / 10
    amp = self.damage.abs * 15 / 100
    amp = 1 if amp < 1
    self.damage += rand(amp + 1) + rand(amp + 1) - amp
    self.damage = -9999 if self.damage < -9999
    self.hp -= self.damage
    self.restorative = true
    @can_slip_damage = false
    return true
  end
  
  def slip_damage_effect
    self.damage = self.maxhp / 20
    amp = self.damage.abs * 15 / 100
    amp = 1 if amp < 1
    self.damage += rand(amp + 1) + rand(amp + 1) - amp
    self.hp -= self.damage
    @can_slip_damage = false
    return true
  end
  
  def regen_slip_damage_effect
    self.damage = -self.maxhp / 20
    amp = self.damage.abs * 15 / 100
    amp = 1 if amp < 1
    self.damage += rand(amp + 1) + rand(amp + 1) - amp
    self.damage = -9999 if self.damage < -9999
    self.hp -= self.damage
    self.restorative = true
    @can_slip_damage = false
    return true
  end
  
end
