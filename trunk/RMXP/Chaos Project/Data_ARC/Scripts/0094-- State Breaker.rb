STATE_BREAKER_IDS = [161, 219]

#==============================================================================
# Game_Battler
#==============================================================================

class Game_Battler
  
  alias skill_effect_state_breaker_later skill_effect
  def skill_effect(user, skill)
    result = skill_effect_state_breaker_later(user, skill)
    if STATE_BREAKER_IDS.include?(skill.id) && self.damage != 'Immune'
      skill.plus_state_set.each {|id| add_state(id)}
      if self.is_a?(Game_Actor)
        self.damage = 'Defeated!'
      else
        self.damage = 'Dead!'
      end
      return true
    end
    return result
  end
  
end
