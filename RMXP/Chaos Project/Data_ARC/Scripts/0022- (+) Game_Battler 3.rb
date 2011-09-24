#==============================================================================
# Game_Battler (3)
#==============================================================================

BREAK_SILENCE = [357, 374, 386, 399, 405, 422]

class Game_Battler
  
  def skill_can_use?(skill_id)
    skill = $data_skills[skill_id]
    if @states.include?(31)
      return false if (skill.sp_cost / 2.0).ceil > self.sp
    else
      return false if skill.sp_cost > self.sp
    end
    return false if dead?
    if (skill.int_f > 0 || skill.mdef_f > 0 ||
        skill.plus_state_set.size > 0 && skill.power == 0 &&
        skill.atk_f == 0 && skill.str_f == 0 && skill.dex_f == 0) &&
        !BREAK_SILENCE.include?(skill.id)
      return false if self.restriction == 1
    end
    occasion = skill.occasion
    return true if occasion == 0
    return (occasion == ($game_temp.in_battle ? 1 : 2))
  end
  
  def attack_effect(attacker)
    self.critical = false
    if @states.include?(50)
      hit_result = false
    elsif attacker.is_a?(Game_Actor) && (attacker.weapon_id == 21 ||
        attacker.meta == 7 || attacker.meta == 14 || attacker.meta == 19)
      hit_result = true
    else
      hit_result = (rand(100) < attacker.hit)
    end
    if hit_result
      if attacker.is_a?(Game_Actor) && attacker.meta == 11
        atk = attacker.atk - self.pdef * 2 / 3
      elsif self.is_a?(Game_Actor) && self.meta == 9
        atk = attacker.atk - self.pdef / 3
      else
        atk = attacker.atk - self.pdef / 2
      end
      atk = 0 if atk < 0
      self.damage = atk * (20 + attacker.str) / 20
      self.damage *= elements_correct(attacker.element_set)
      self.damage /= 100
      if self.damage > 0
        if attacker.is_a?(Game_Actor) && attacker.weapon_id == 21
          self.damage *= 2
          self.critical = true
        else
          if attacker.states.include?(18)
            critical = 250
          elsif self.is_a?(Game_Actor) && self.meta == 15
            critical = 80 * attacker.dex / self.agi
          elsif self.is_a?(Game_Actor) && self.meta == 10
            critical = 60 * attacker.dex / self.agi
          else
            critical = 40 * attacker.dex / self.agi
          end
          if rand(1000) < critical
            self.damage *= 2 
            self.critical = true 
          end
        end
        if self.guarding?
          self.damage /= (self.is_a?(Game_Actor) && self.meta == 12 ? 3 : 2)
        end
      end
      if self.damage.abs > 0
        amp = self.damage.abs * 15 / 100
        amp = 1 if amp < 1
        self.damage += rand(amp+1) + rand(amp+1) - amp
      end
      eva = 8 * self.agi / attacker.dex + self.eva
      hit = self.damage < 0 ? 100 : 100 - eva
      hit = self.cant_evade? ? 100 : hit + 10
      hit_result = (rand(100) < hit)
    end
    if hit_result
      remove_states_shock
      self.hp -= self.damage
      @state_changed = false
      states_plus(attacker.plus_state_set)
      states_minus(attacker.minus_state_set)
    else
      self.critical = false
      self.damage = 'Missed'
    end
    return true
  end
  
  def skill_effect(user, skill)
    self.critical = false
    if skill.id == 381
      self.damage = 'Time'
      return true
    end
    if skill.id == 218 && self.is_a?(Game_Enemy) &&
        $data_enemies[self.id].element_ranks[MACHINE] != 3
      add_state(8)
      self.damage = 'Shut down!'
      self.critical = true
      return true
    end
    if skill.id == 237 || skill.id == 378
      return false if !self.dead?
      self.hp = self.maxhp
      self.damage = -self.hp
      return true
    end
    if skill.scope != 9
      if @hp == 0
        return false if skill.scope >= 1 && skill.scope <= 4
      else
        return false if skill.scope == 5 || skill.scope == 6
      end
    end
    effective = (skill.common_event_id > 0)
    if user.is_a?(Game_Actor) && (user.meta == 7 || user.meta == 14 ||
        user.meta == 19) || CP::Cache::FullHit.include?(skill.id)
      hit_result = true 
    else
      hit = skill.hit
      hit *= user.hit / 100 if skill.atk_f > 0
      hit_result = (rand(100) < hit)
      effective |= hit < 100
    end
    if hit_result
      if skill.id == 198
        self.damage = 5000
      elsif skill.id == 406
        self.damage = 9999
      elsif skill.id == 271 || skill.id == 378 || skill.id == 424
        self.damage = -9999
      else
        power = skill.power + user.atk * skill.atk_f / 100
        if power > 0
          power -= self.pdef * skill.pdef_f / 200
          power -= self.mdef * skill.mdef_f / 200
          power = 0 if power < 0
        end
        rate = 20
        rate += (user.str * skill.str_f / 100)
        rate += (user.dex * skill.dex_f / 100)
        rate += (user.agi * skill.agi_f / 100)
        rate += (user.int * skill.int_f / 100)
        if user.is_a?(Game_Actor) && user.meta == 16
          self.damage = power * rate * 3 / 50
        else
          self.damage = power * rate * 2 / 25
        end
        self.damage *= elements_correct(skill.element_set)
        self.damage /= 100
        if self.damage > 0 && self.guarding?
          self.damage /= (self.is_a?(Game_Actor) && self.meta == 12 ? 3 : 2)
        end
        if skill.variance > 0 && self.damage.abs > 0
          amp = self.damage.abs * skill.variance / 100
          amp = 1 if amp < 1
          self.damage += rand(amp+1) + rand(amp+1) - amp
        end
        if skill.pdef_f > 0 && self.damage > 0 && self.guarding?
          factor = (self.is_a?(Game_Actor) && self.meta == 12 ? 2 : 1)
          self.damage /= 1 + (factor * skill.pdef_f / 100)
        end
      end
      if user.is_a?(Game_Actor) && (user.meta == 7 || user.meta == 14 ||
          user.meta == 19) && !@states.include?(50)
        hit_result = true
      else
        eva = 8 * self.agi / user.dex + self.eva
        hit = self.damage < 0 ? 100 : 100 - eva * skill.eva_f / 100
        hit = self.cant_evade? ? 100 : hit + 10
        hit_result = (rand(100) < hit)
        effective |= hit < 100
      end
    end
    if hit_result
      if skill.power != 0 && skill.atk_f > 0
        if user.is_a?(Game_Actor) && skill.id == 266 &&
            @states.include?(SLEEPING_ID)
          self.damage *= 2
          self.critical = true
        elsif !CP::Cache::NoCritical.include?(skill.id)
          if user.states.include?(18)
            critical = 250
          elsif self.is_a?(Game_Actor) && self.meta == 15
            critical = 20 * user.dex / self.agi
          elsif self.is_a?(Game_Actor) && self.meta == 10
            critical = 15 * user.dex / self.agi
          else
            critical = 10 * user.dex / self.agi
          end
          if rand(1000) < critical
            self.damage *= 2 
            self.critical = true 
          end
        end
        remove_states_shock
        effective = true
      end
      last_hp = self.hp
      self.hp -= self.damage
      effective |= self.hp != last_hp
      @state_changed = false
      effective |= states_plus(skill.plus_state_set)
      plus = (!@state_changed && skill.plus_state_set.size > 0)
      effective |= states_minus(skill.minus_state_set)
      if skill.power == 0
        self.damage = '' if !self.damage.is_a?(String)
        if plus && !NO_DMG.include?(skill.id)
          if state_immune?(skill.plus_state_set)
            self.damage = 'Immune'
          else
            self.damage = 'Failed'
          end
        end
      end
      @state_changed = false
    else
      self.damage = 'Missed'
    end
    self.damage = nil unless $game_temp.in_battle
    return effective
  end
  
  def item_effect(item)
    self.critical = false
    if self.is_a?(Game_Actor)
      case item.id
      when 42
        self.level += 2
        self.damage = -2
        return true
      when 79
        self.level -= 2
        self.damage = 2
        states_plus(item.plus_state_set)
        return true
      when 155
        return false if self.sr == self.maxsr
        self.sr = self.maxsr
        if $game_temp.in_battle
          self.damage = "#{self.maxsr/10},#{self.maxsr%10}% SR"
          self.critical = true
        end
        return true
      end
    end
    if @hp == 0
      return false if item.scope >= 1 && item.scope <= 4
    else
      return false if item.scope == 5 || item.scope == 6
    end
    effective = (item.common_event_id > 0)
    hit_result = (rand(100) < item.hit)
    effective |= item.hit < 100
    if hit_result
      recover_hp = maxhp * item.recover_hp_rate / 100 + item.recover_hp
      recover_sp = maxsp * item.recover_sp_rate / 100 + item.recover_sp
      if recover_hp < 0
        recover_hp += self.pdef * item.pdef_f/20 + self.mdef * item.mdef_f/20
        recover_hp = 0 if recover_hp > 0
      end
      elements = elements_correct(item.element_set)
      recover_hp = recover_hp * elements / 100
      recover_sp = recover_sp * elements / 100
      if item.variance > 0 && recover_hp.abs > 0
        amp = recover_hp.abs * item.variance / 100
        amp = 1 if amp < 1
        recover_hp += rand(amp+1) + rand(amp+1) - amp
      end
      if item.variance > 0 && recover_sp.abs > 0
        amp = recover_sp.abs * item.variance / 100
        amp = 1 if amp < 1
        recover_sp += rand(amp+1) + rand(amp+1) - amp
      end
      recover_hp /= 2 if recover_hp < 0 && self.guarding?
      self.damage = -recover_hp
      last_hp = self.hp
      last_sp = self.sp
      self.hp += recover_hp
      self.sp += recover_sp
      effective |= (self.hp != last_hp)
      effective |= (self.sp != last_sp)
      @state_changed = false
      effective |= states_plus(item.plus_state_set)
      plus = (!@state_changed && item.plus_state_set.size > 0)
      effective |= states_minus(item.minus_state_set)
      if item.parameter_type > 0 && item.parameter_points != 0
        case item.parameter_type
        when 1 then @maxhp_plus += item.parameter_points
        when 2 then @maxsp_plus += item.parameter_points
        when 3 then @str_plus += item.parameter_points
        when 4 then @dex_plus += item.parameter_points
        when 5 then @agi_plus += item.parameter_points
        when 6 then @int_plus += item.parameter_points
        end
        effective = true
      end
      if item.recover_hp_rate == 0 && item.recover_hp == 0
        if item.recover_sp_rate == 0 && item.recover_sp == 0
          self.damage = ''
          if item.parameter_type == 0 || item.parameter_points == 0
            if plus
              if state_immune?(item.plus_state_set)
                self.damage = 'Immune'
              else
                self.damage = 'Failed'
              end
            end
          end
        else
          self.damage = "#{recover_sp} #{$data_system.words.sp}"
          self.restorative_mp = true
        end
        @state_changed = false
      end
    else
      self.damage = 'Missed'
    end
    self.damage = nil unless $game_temp.in_battle
    return effective
  end
  
  def elements_correct(elements)
    return 100 if elements.size == 0
    multiplier = 0
    size = 0
    absorber = 0
    flag = true
    elements.each {|i|
        if !CP::Cache::DummyElements.include?(i) && self.element_rate(i) != 100
          if self.element_rate(i) < -200
            absorber += self.element_rate(i)/10
            flag = false
          end
          multiplier += self.element_rate(i)
          size += 1
        end}
    return 100 if size == 0
    return multiplier/size if flag
    return absorber
  end
  
end
