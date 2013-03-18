#==============================================================================
# Game_Troop
#==============================================================================

class Game_Troop
  
  attr_reader :enemies
  attr_reader :id
  
  def initialize
    clear
  end
  
  def clear
    @enemies = []
  end
  
  def reset_slip_damage
    @enemies.each {|enemy| enemy.can_slip_damage = true}
  end
  
  def setup(troop_id)
    @id = troop_id
    @enemies = []
    troop = $data_troops[troop_id]
    troop.members.each_index {|i|
        enemy = $data_enemies[troop.members[i].enemy_id]
        @enemies.push(Game_Enemy.new(troop_id, i)) if enemy != nil}
  end
  
  def save
    @copies = []
    (0...8).each {|i|
        if @enemies[i] != nil
          @copies[i] = @enemies[i].clone
          @copies[i].save
        end}
  end
  
  def apply
    @enemies = @copies
    @enemies.each {|enemy|
        enemy.current_action.clear
        enemy.damage = 'Timeshift!'
        enemy.damage_pop = true}
    @copies = nil
  end
  
  def random_target_enemy(hp0 = false)
    roulette = []
    @enemies.each {|enemy| roulette.push(enemy) if (hp0 ? enemy.hp0? : enemy.exist?)}
    return (roulette.size == 0 ? nil : roulette[rand(roulette.size)])
  end
  
  def random_target_enemy_hp0
    return random_target_enemy(true)
  end
  
  def smooth_target_enemy(enemy_index)
    enemy = @enemies[enemy_index]
    return enemy if enemy != nil && enemy.exist?
    @enemies.each {|enemy| return enemy if enemy.exist?}
  end
  
end
