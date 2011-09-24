#==============================================================================
# Game_BattleAction
#==============================================================================

class Game_BattleAction
  
  attr_accessor :speed
  attr_accessor :kind
  attr_accessor :basic
  attr_accessor :skill_id
  attr_accessor :item_id
  attr_accessor :target_index
  attr_accessor :forcing
  attr_accessor :fail
  attr_accessor :repeating
  
  def initialize
    clear
  end
  
  def clear
    @speed = @kind = @skill_id = @item_id = 0
    @target_index, @basic, @forcing = -1, 3, false
    @fail = nil
    @repeating = false
  end
  
  def clear?
    return (@speed == 0 && @kind == 0 && @basic == 3 && @skill_id == 0 &&
        @item_id == 0 && @target_index == -1 && !@forcing)
  end
  
  def valid?
    return (@kind != 0 || @basic != 3)
  end
  
  def for_one_friend?
    return (@kind == 0 && @basic == 1 || ((@kind == 1 || @kind == 2) &&
        ($data_skills[@skill_id].scope == 3 ||
        $data_skills[@skill_id].scope == 5 ||
        $data_skills[@skill_id].scope == 9)))
  end
  
  def for_one_friend_hp0?
    return ((@kind == 1 || @kind == 2) && ($data_skills[@skill_id].scope == 5 ||
        $data_skills[@skill_id].scope == 9))
  end
  
  def skill?
    return (@kind == 1)
  end
  
  def item?
    return (@kind == 2)
  end
  
  def sr?
    return (@kind == 3)
  end
  
  def meta?
    return (@kind == 9)
  end
  
  def decide_cover_target
    battler = $game_party.decide_cover_target
    battler != nil ? @target_index = battler.index : clear
  end
  
  def decide_random_target_for_actor
    if for_one_friend_hp0?
      battler = $game_party.random_target_actor_hp0
    elsif for_one_friend?
      battler = $game_party.random_target_actor
    else
      battler = $game_troop.random_target_enemy
    end
    battler != nil ? @target_index = battler.index : clear
  end
  
  def decide_random_target_for_enemy
    if for_one_friend_hp0?
      battler = $game_troop.random_target_enemy_hp0
    elsif for_one_friend?
      battler = $game_troop.random_target_enemy
    else
      battler = $game_party.random_target_actor
    end
    battler != nil ? @target_index = battler.index : clear
  end
  
  def decide_last_target_for_actor
    if @target_index == -1
      battler = nil
    elsif for_one_friend?
      battler = $game_party.actors[@target_index]
    else
      battler = $game_troop.enemies[@target_index]
    end
    clear if battler == nil || !battler.exist?
  end
  
  def decide_last_target_for_enemy
    if @target_index == -1
      battler = nil
    elsif for_one_friend?
      battler = $game_troop.enemies[@target_index]
    else
      battler = $game_party.actors[@target_index]
    end
    clear if battler == nil || !battler.exist?
  end
  
end
