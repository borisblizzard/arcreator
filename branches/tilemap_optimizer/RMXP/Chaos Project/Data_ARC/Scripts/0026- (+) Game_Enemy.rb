#==============================================================================
# Game_Enemy
#==============================================================================

class Game_Enemy < Game_Battler
  
  attr_accessor :battler_hue
  attr_writer   :battler_name
  
  def initialize(troop_id, member_index)
    super()
    @troop_id, @member_index = troop_id, member_index
    troop = $data_troops[@troop_id]
    @enemy_id = troop.members[@member_index].enemy_id
    enemy = $data_enemies[@enemy_id]
    @battler_name, @battler_hue = enemy.battler_name, enemy.battler_hue
    @hp, @sp = maxhp, maxsp
    @hidden = troop.members[@member_index].hidden
    @immortal = troop.members[@member_index].immortal
  end
  
  def can_use_any_skill?
    return (get_available_actions.any? {|action| action.kind == 1})
  end
  
  def id
    return @enemy_id
  end
  
  def index
    return @member_index
  end
  
  def name
    return $data_enemies[@enemy_id].name
  end
  
  def base_maxhp
    return $data_enemies[@enemy_id].maxhp
  end
  
  def base_maxsp
    return $data_enemies[@enemy_id].maxsp
  end
  
  def base_str
    return $data_enemies[@enemy_id].str
  end
  
  def base_dex
    return $data_enemies[@enemy_id].dex
  end
  
  def base_agi
    return $data_enemies[@enemy_id].agi
  end
  
  def base_int
    return $data_enemies[@enemy_id].int
  end
  
  def base_atk
    return $data_enemies[@enemy_id].atk
  end
  
  def base_pdef
    return $data_enemies[@enemy_id].pdef
  end
  
  def base_mdef
    return $data_enemies[@enemy_id].mdef
  end
  
  def base_eva
    return $data_enemies[@enemy_id].eva
  end
  
  def animation1_id
    return $data_enemies[@enemy_id].animation1_id
  end
  
  def animation2_id
    return $data_enemies[@enemy_id].animation2_id
  end
  
  def element_rate(element_id)
    result = CP::Cache::ElementRates[$data_enemies[@enemy_id].element_ranks[element_id]]
    @states.each {|i|
        result /= 2 if $data_states[i].guard_element_set.include?(element_id)}
    return result
  end
  
  def state_ranks
    return $data_enemies[@enemy_id].state_ranks
  end
  
  def state_guard?(state_id)
    return false
  end
  
  def element_set
    return []
  end
  
  def plus_state_set
    return []
  end
  
  def minus_state_set
    return []
  end
  
  def actions
    return $data_enemies[@enemy_id].actions
  end
  
  def exp
    return ($data_enemies[@enemy_id].exp * $game_system.exp_rate).to_i
  end
  
  def gold
    return ($data_enemies[@enemy_id].gold * $game_system.gold_rate).to_i
  end
  
  def item_id
    return $data_enemies[@enemy_id].item_id
  end
  
  def weapon_id
    return $data_enemies[@enemy_id].weapon_id
  end
  
  def armor_id
    return $data_enemies[@enemy_id].armor_id
  end
  
  def treasure_prob
    return $data_enemies[@enemy_id].treasure_prob
  end
  
  def screen_x
    return $data_troops[@troop_id].members[@member_index].x
  end
  
  def screen_y
    return $data_troops[@troop_id].members[@member_index].y
  end
  
  def screen_z
    return screen_y
  end
  
  def escape
    @hidden = true
    self.current_action.clear
  end
  
  def transform(enemy_id)
    @enemy_id = enemy_id
    @battler_name = $data_enemies[@enemy_id].battler_name
    @battler_hue = $data_enemies[@enemy_id].battler_hue
    make_action
  end
  
  def make_action
    self.current_action.clear
    if !self.movable?
      remove_state(2) if @states.include?(2)
      return
    end
    available_actions = get_available_actions
    rating_max = ratings_total = 0
    available_actions.each {|action|
        rating_max = action.rating if rating_max < action.rating}
    available_actions.each {|action|
        if action.rating > rating_max - 3
          ratings_total += action.rating - (rating_max - 3)
        end}
    if ratings_total > 0
      value = rand(ratings_total)
      available_actions.each {|action|
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
          end}
    end
  end
  
  def get_available_actions
    available_actions = []
    self.actions.each {|action|
        n = $game_temp.battle_turn
        a = action.condition_turn_a
        b = action.condition_turn_b
        next if (b == 0 && n != a)
        next if (b > 0 && (n < 1 || n < a || n % b != a % b))
        next if self.hp * 100.0 / self.maxhp > action.condition_hp
        next if $game_party.max_level < action.condition_level
        switch_id = action.condition_switch_id
        next if switch_id > 0 && !$game_switches[switch_id]
        available_actions.push(action)}
    available_actions.each_index {|i|
        if available_actions[i].kind == 1 &&
            !self.skill_can_use?(available_actions[i].skill_id)
          available_actions[i] = nil
        end}
    available_actions.compact!
    return available_actions
  end
  
  def hp=(hp)
    super(hp)
    if self.dead?
      @states.each {|id| remove_state(id) if !$data_states[id].zero_hp}
    end
  end
  
end
