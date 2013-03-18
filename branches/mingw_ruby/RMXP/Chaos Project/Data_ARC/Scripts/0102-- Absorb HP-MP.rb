#==============================================================================
# Absorbing HP and SP by Blizzard
# Version: 2.0b CP DX
#==============================================================================

#==============================================================================
# Game_Battler
#==============================================================================

class Game_Battler

  alias skill_effect_mp_absorb_later skill_effect
  def skill_effect(user, skill)
    @restorative = @restorative_mp = false
    @flag = nil
    @mp_flag = 0
    last_hp = self.hp
    last_sr = self.sr if self.is_a?(Game_Actor)
    result = skill_effect_mp_absorb_later(user, skill)
    if result && self.damage.is_a?(Numeric)
      if CP::Cache::AbsorbSP.include?(skill.id)
        self.hp = last_hp
        self.sr = last_sr if self.is_a?(Game_Actor)
        if self != user
          factor = ((self.is_a?(Game_Enemy) && self.boss) ? 100 : 10)
          if CP::Cache::StealSP.include?(skill.id) && factor == 100
            self.damage = 'Immune'
          else
            if self.sp >= self.damage / factor && ![81, 410].include?(skill.id)
              self.damage /= factor
            else
              self.damage = self.sp
            end
            self.sp -= self.damage
            @mp_flag = self.damage
            self.damage = "#{self.damage} #{$data_system.words.sp}"
          end
        else
          self.damage = 0
        end
      elsif CP::Cache::AbsorbHP.include?(skill.id)
        self.hp = last_hp
        self.sr = last_sr if self.is_a?(Game_Actor)
        if self != user
          if self.is_a?(Game_Enemy) && CP::Cache::UndeadIDs.include?(@id) && skill.id != 157
            self.damage = -self.damage
            self.hp -= self.damage
          elsif self.hp > self.damage
            self.hp -= self.damage
            if self.is_a?(Game_Actor) && self.sr_mode == 0
              self.sr += self.damage * SRS_rate / last_hp
              self.sr += self.damage * SRS_rate / last_hp / 2 if @armor4_id == 92
              self.sr += self.damage * SRS_rate / last_hp / 2 if @armor5_id == 92
              self.sr += self.damage * SRS_rate / last_hp / 2 if @armor6_id == 92
              self.sr += self.damage * SRS_rate / last_hp / 2 if self.current_action.kind == 5
            end
          else
            self.damage = self.hp
            self.hp = 0
          end
        else
          self.damage = 0
        end
      end
    end
    if last_hp > self.hp && self.is_a?(Game_Actor) && self.hp > 0 &&
        user.is_a?(Game_Enemy) && self.meta == 18 && rand(100) < 50
      @flag = last_hp - self.hp
    end
    return result
  end
  
  alias attack_effect_counter_later attack_effect
  def attack_effect(attacker)
    @flag = nil
    last_hp = self.hp
    result = attack_effect_counter_later(attacker)
    if last_hp > self.hp && self.is_a?(Game_Actor) &&
        attacker.is_a?(Game_Enemy) && self.can_counter? && rand(100) < 50
      @flag = last_hp - self.hp
    end
    @mp_flag = 0
    return result
  end  
    
  def absorb_post_process(user)
    if user.current_action.kind == 1 || user.current_action.kind == 3 ||
        user.current_action.kind == 9
      skill = $data_skills[user.current_action.skill_id]
    end
    effective = false
    unless self == user || BREAK_REFLECT.include?(skill.id)
      user.critical = user.restorative = user.restorative_mp = false
    end
    if skill != nil && (self.damage.is_a?(Numeric) || @mp_flag != 0)
      if CP::Cache::AbsorbHP.include?(skill.id)
        user.hp += self.damage
        user.damage = -self.damage
        user.restorative = user.damage_pop = effective = true
        user.make_meta
      elsif CP::Cache::AbsorbSP.include?(skill.id)
        user.sp += @mp_flag
        user.damage = "#{@mp_flag} #{$data_system.words.sp}"
        user.restorative_mp = user.damage_pop = effective = true
        user.make_meta
      elsif skill.id == 157
        user.hp = user.maxhp
        user.sp = user.maxsp
        user.damage = 'Full!'
        user.damage_pop = effective = true
        user.make_meta
      end
    end
    if @flag != nil
      dam = @flag*8/5 + rand(@flag*4/5+1)
      user.damage = (user.damage.is_a?(Numeric) ? user.damage + dam : dam)
      user.hp -= user.damage
      user.damage = "Counter #{user.damage}"
      user.critical = user.damage_pop = effective = true
      user.restorative = user.restorative_mp = false
      user.make_meta
      @flag = nil
    end
    @mp_flag = 0
    return effective
  end
    
end
