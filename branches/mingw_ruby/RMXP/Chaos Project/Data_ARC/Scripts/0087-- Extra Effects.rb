#==============================================================================
# Game_Battler
#==============================================================================

NO_DMG = [210]
MACHINE = 18

class Game_Battler
  
  alias skill_effect_ex_later skill_effect
  def skill_effect(user, skill)
    case skill.id
    when 77
      self.damage = -user.maxhp / 4
      self.hp -= self.damage
    when 78
      self.damage = -user.maxhp / 2
      self.hp -= self.damage
    when 79
      self.damage = -user.maxhp * 3 / 4
      self.hp -= self.damage
    when 80
      self.damage = -user.maxhp
      self.hp -= self.damage
    when 130
      self.damage = user.maxsp / 4
      self.sp += self.damage
      self.damage = "#{self.damage} #{$data_system.words.sp}"
      self.restorative_mp = true
    when 131
      self.damage = user.maxsp / 2
      self.sp += self.damage
      self.damage = "#{self.damage} #{$data_system.words.sp}"
      self.restorative_mp = true
    when 132
      self.damage = user.maxsp * 3 / 4
      self.sp += self.damage
      self.damage = "#{self.damage} #{$data_system.words.sp}"
      self.restorative_mp = true
    when 133
      self.sp += user.maxsp
      self.damage = "#{user.maxsp} #{$data_system.words.sp}"
      self.restorative_mp = true
    when 221, 231, 235, 325, 363
      if self.is_a?(Game_Actor) || !self.boss
        self.damage = self.hp / 4
        self.hp -= self.damage
      else
        self.damage = 'Immune'
      end
    when 444
      if self.is_a?(Game_Actor) || !self.boss
        self.damage = self.hp * 3 / 4
        self.hp -= self.damage
      else
        self.damage = 'Immune'
      end
    else
      return skill_effect_ex_later(user, skill)
    end
    return true
  end
          
end