#==============================================================================
# Game_Actor
#==============================================================================

class Game_Actor < Game_Battler
  
  attr_reader   :character_name
  attr_reader   :character_hue
  attr_reader   :class_id
  attr_reader   :weapon_id
  attr_reader   :armor1_id
  attr_reader   :armor2_id
  attr_reader   :armor3_id
  attr_reader   :armor4_id
  attr_reader   :armor5_id
  attr_reader   :armor6_id
  attr_reader   :level
  attr_reader   :exp
  attr_accessor :name
  attr_accessor :guarded_by
  attr_accessor :disrupting
  
  def initialize(actor_id)
    super()
    @guarded_by = []
    setup(actor_id)
  end
  
  def save
    super
    @guarded_by = @guarded_by.clone
    @skills = @skills.clone
    @dragon_skills = @dragon_skills.clone if @dragon_skills != nil
  end
  
  def setup(actor_id)
    actor = $data_actors[actor_id]
    @actor_id = actor_id
    @name = actor.name
    @character_name = actor.character_name
    @character_hue = actor.character_hue
    @battler_name = actor.battler_name
    @battler_hue = actor.battler_hue
    @class_id = actor.class_id
    @weapon_id = actor.weapon_id
    @armor1_id = (actor.id == 4 ? 12 : actor.armor1_id)
    @armor2_id = actor.armor2_id
    @armor3_id = actor.armor3_id
    @armor4_id = actor.armor4_id
    @armor5_id = 0
    @armor6_id = 0
    @level = actor.initial_level
    @exp_list = Array.new(102)
    make_exp_list
    @exp = @exp_list[@level]
    @skills = []
    @hp = self.maxhp
    @sp = self.maxsp
    @states = []
    @states_turn = {}
    @maxhp_plus = @maxsp_plus = @str_plus = @dex_plus = @agi_plus = @int_plus = 0
    if @class_id == 12
      @skills = (1...$data_skills.size).to_a
    else
      (1..@level).each {|i| $data_classes[@class_id].learnings.each {|j|
          learn_skill(j.skill_id) if j.level == i}}
    end
    @dragon_skills = {} if self.id == CP::Cache::Sydon
  end
  
  def dream
    @bkup = [@weapon_id, @armor1_id, @armor2_id, @armor3_id, @armor4_id,
        @armor5_id, @armor6_id, @states]
    @armor1_id = @armor2_id = @armor3_id = @armor4_id = @armor5_id = @armor6_id = 0
    @weapon_id, @states = 22, []
  end
  
  def wake_up
    @weapon_id, @armor1_id, @armor2_id, @armor3_id, @armor4_id, @armor5_id,
        @armor6_id, @states = @bkup
    @bkup = nil
  end
  
  def no_info?
    return (@bkup != nil)
  end
  
  def equipment_gone
    CP.gun_database(@armor1_id).each {|e_id| forget_skill(e_id)}
    @bkup = [@weapon_id, @armor1_id, @armor2_id, @armor3_id, @armor4_id,
        @armor5_id, @armor6_id, @states]
    @weapon_id = @armor1_id = @armor2_id = @armor3_id = @armor4_id =
        @armor5_id = @armor6_id = 0
    @states = []
  end
  
  def equipment_back
    @weapon_id, @armor1_id, @armor2_id, @armor3_id, @armor4_id, @armor5_id,
        @armor6_id, @states = @bkup
    @bkup = nil
    CP.gun_database(@armor1_id).each {|e_id| learn_skill(e_id)}
  end
  
  def skills
    ids = @skills.clone
    @states.each {|id|
        skills = self.dragon_skills(id)
        if skills.size > 0
          ids |= skills
          ids -= ids.find_all {|i| $data_skills[i].plus_state_set.include?(id)}
        end}
    if @states.include?(45)
      (1...$data_states.size).each {|id|
          skills = self.dragon_skills(id)
          if skills.size > 0
            ids -= ids.find_all {|i| $data_skills[i].plus_state_set.include?(id)}
          end}
    end
    return CP.resort_skills(ids)
  end
  
  def id
    return @actor_id
  end
  
  def index
    return $game_party.actors.index(self)
  end
  
  def make_exp_list
    actor = $data_actors[@actor_id]
    @exp_list[1] = 0
    pow_i = 2.4 + actor.exp_inflation / 100.0
    CP::Cache::Levels.each {|i|
        if i > actor.final_level
          @exp_list[i] = 0
        else
          n = actor.exp_basis * ((i + 3) ** pow_i) / (5 ** pow_i)
          @exp_list[i] = @exp_list[i-1] + Integer(n)
        end}
  end
  
  def element_rate(element_id)
    result = CP::Cache::ElementRates[$data_classes[@class_id].element_ranks[element_id]]
    result2 = 0
    flag = true
    [(CP::Cache::Lucius.include?(self.id) ? 0 : @armor1_id), @armor2_id, @armor3_id,
    @armor4_id, @armor5_id, @armor6_id].each {|i|
        if i != 0
          result /= 2 if $data_armors[i].guard_element_set.include?(element_id)
          if $data_armors[i].guard_element_set.include?(element_id+9)
            result2 -= 500
            result2 -= 500 if $data_armors[i].guard_element_set.include?(element_id)
          end
          flag = false if $data_armors[i].guard_element_set.include?(element_id+9)
        end}
    @states.each {|i|
        result /= 2 if $data_states[i].guard_element_set.include?(element_id)}
    return (flag ? result : result2)
  end
  
  def state_ranks
    return $data_classes[@class_id].state_ranks
  end
  
  def state_guard?(state_id)
    ids = [@armor2_id, @armor3_id, @armor4_id, @armor5_id, @armor6_id]
    ids.unshift(@armor1_id) unless CP::Cache::Lucius.include?(self.id)
    ids.each {|i|
        armor = $data_armors[i]
        return true if armor != nil && armor.guard_state_set.include?(state_id)}
    return false
  end
  
  def element_set
    weapon1 = $data_weapons[@weapon_id]
    weapon2 = $data_weapons[@armor1_id]
    weapon1 = (weapon1 != nil ? weapon1.element_set : [])
    weapon2 = ((weapon2 != nil && (CP::Cache::Lucius.include?(self.id))) ? weapon2.element_set : [])
    return (weapon1 | weapon2)
  end
  
  def plus_state_set
    weapon1 = $data_weapons[@weapon_id]
    weapon2 = $data_weapons[@armor1_id]
    weapon1 = (weapon1 != nil ? weapon1.plus_state_set : [])
    weapon2 = ((weapon2 != nil && (CP::Cache::Lucius.include?(self.id))) ? weapon2.plus_state_set : [])
    return (weapon1 | weapon2)
  end
  
  def minus_state_set
    weapon1 = $data_weapons[@weapon_id]
    weapon2 = $data_weapons[@armor1_id]
    weapon1 = (weapon1 != nil ? weapon1.minus_state_set : [])
    weapon2 = ((weapon2 != nil && (CP::Cache::Lucius.include?(self.id))) ? weapon2.minus_state_set : [])
    return (weapon1 | weapon2)
  end
  
  def maxhp
    n = base_maxhp + @maxhp_plus
    if n < 1
      n = 1
    elsif n > 9999
      n = 9999
    end
    @states.each {|i| n *= $data_states[i].maxhp_rate / 100.0}
    n = n.to_i
    return 1 if n < 1
    return 9999 if n > 9999
    return n
  end
  
  def base_maxhp
    return $data_actors[@actor_id].parameters[0, @level]
  end
  
  def base_maxsp
    return $data_actors[@actor_id].parameters[1, @level]
  end
  
  def base_str
    n = $data_actors[@actor_id].parameters[2, @level]
    n += @weapon_id != 0 ? $data_weapons[@weapon_id].str_plus : 0
    if CP::Cache::Lucius.include?(self.id)
      n += @armor1_id != 0 ? $data_weapons[@armor1_id].str_plus : 0
    else
      n += @armor1_id != 0 ? $data_armors[@armor1_id].str_plus : 0
    end
    n += @armor2_id != 0 ? $data_armors[@armor2_id].str_plus : 0
    n += @armor3_id != 0 ? $data_armors[@armor3_id].str_plus : 0
    n += @armor4_id != 0 ? $data_armors[@armor4_id].str_plus : 0
    n += @armor5_id != 0 ? $data_armors[@armor5_id].str_plus : 0
    n += @armor6_id != 0 ? $data_armors[@armor6_id].str_plus : 0
    return 1 if n < 1
    return 999 if n > 999
    return n
  end
  
  def base_dex
    n = $data_actors[@actor_id].parameters[3, @level]
    n += @weapon_id != 0 ? $data_weapons[@weapon_id].dex_plus : 0
    if CP::Cache::Lucius.include?(self.id)
      n += @armor1_id != 0 ? $data_weapons[@armor1_id].dex_plus : 0
    else
      n += @armor1_id != 0 ? $data_armors[@armor1_id].dex_plus : 0
    end
    n += @armor2_id != 0 ? $data_armors[@armor2_id].dex_plus : 0
    n += @armor3_id != 0 ? $data_armors[@armor3_id].dex_plus : 0
    n += @armor4_id != 0 ? $data_armors[@armor4_id].dex_plus : 0
    n += @armor5_id != 0 ? $data_armors[@armor5_id].dex_plus : 0
    n += @armor6_id != 0 ? $data_armors[@armor6_id].dex_plus : 0
    return 1 if n < 1
    return 999 if n > 999
    return n
  end
  
  def base_agi
    n = $data_actors[@actor_id].parameters[4, @level]
    n += @weapon_id != 0 ? $data_weapons[@weapon_id].agi_plus : 0
    if CP::Cache::Lucius.include?(self.id)
      n += @armor1_id != 0 ? $data_weapons[@armor1_id].agi_plus : 0
    else
      n += @armor1_id != 0 ? $data_armors[@armor1_id].agi_plus : 0
    end
    n += @armor2_id != 0 ? $data_armors[@armor2_id].agi_plus : 0
    n += @armor3_id != 0 ? $data_armors[@armor3_id].agi_plus : 0
    n += @armor4_id != 0 ? $data_armors[@armor4_id].agi_plus : 0
    n += @armor5_id != 0 ? $data_armors[@armor5_id].agi_plus : 0
    n += @armor6_id != 0 ? $data_armors[@armor6_id].agi_plus : 0
    return 1 if n < 1
    return 999 if n > 999
    return n
  end
  
  def base_int
    n = $data_actors[@actor_id].parameters[5, @level]
    n += @weapon_id != 0 ? $data_weapons[@weapon_id].int_plus : 0
    if CP::Cache::Lucius.include?(self.id)
      n += @armor1_id != 0 ? $data_weapons[@armor1_id].int_plus : 0
    else
      n += @armor1_id != 0 ? $data_armors[@armor1_id].int_plus : 0
    end
    n += @armor2_id != 0 ? $data_armors[@armor2_id].int_plus : 0
    n += @armor3_id != 0 ? $data_armors[@armor3_id].int_plus : 0
    n += @armor4_id != 0 ? $data_armors[@armor4_id].int_plus : 0
    n += @armor5_id != 0 ? $data_armors[@armor5_id].int_plus : 0
    n += @armor6_id != 0 ? $data_armors[@armor6_id].int_plus : 0
    return 1 if n < 1
    return 999 if n > 999
    return n
  end
  
  def base_atk
    n = (@weapon_id != 0 ? $data_weapons[@weapon_id].atk : 0)
    if CP::Cache::Lucius.include?(self.id)
      n += (@armor1_id != 0 ? $data_weapons[@armor1_id].atk : 0)
    else
      n += (@armor1_id != 0 ? $data_armors[@armor1_id].atk : 0)
    end
    n += @armor2_id != 0 ? $data_armors[@armor2_id].atk : 0
    n += @armor3_id != 0 ? $data_armors[@armor3_id].atk : 0
    n += @armor4_id != 0 ? $data_armors[@armor4_id].atk : 0
    n += @armor5_id != 0 ? $data_armors[@armor5_id].atk : 0
    n += @armor6_id != 0 ? $data_armors[@armor6_id].atk : 0
    return n
  end
  
  def base_pdef
    n = @weapon_id != 0 ? $data_weapons[@weapon_id].pdef : 0
    if CP::Cache::Lucius.include?(self.id)
      n += @armor1_id != 0 ? $data_weapons[@armor1_id].pdef : 0
    else
      n += @armor1_id != 0 ? $data_armors[@armor1_id].pdef : 0
    end
    n += @armor2_id != 0 ? $data_armors[@armor2_id].pdef : 0
    n += @armor3_id != 0 ? $data_armors[@armor3_id].pdef : 0
    n += @armor4_id != 0 ? $data_armors[@armor4_id].pdef : 0
    n += @armor5_id != 0 ? $data_armors[@armor5_id].pdef : 0
    n += @armor6_id != 0 ? $data_armors[@armor6_id].pdef : 0
    return n
  end
  
  def base_mdef
    n = @weapon_id != 0 ? $data_weapons[@weapon_id].mdef : 0
    if CP::Cache::Lucius.include?(self.id)
      n += @armor1_id != 0 ? $data_weapons[@armor1_id].mdef : 0
    else
      n += @armor1_id != 0 ? $data_armors[@armor1_id].mdef : 0
    end
    n += @armor2_id != 0 ? $data_armors[@armor2_id].mdef : 0
    n += @armor3_id != 0 ? $data_armors[@armor3_id].mdef : 0
    n += @armor4_id != 0 ? $data_armors[@armor4_id].mdef : 0
    n += @armor5_id != 0 ? $data_armors[@armor5_id].mdef : 0
    n += @armor6_id != 0 ? $data_armors[@armor6_id].mdef : 0
    return n
  end
  
  def base_eva
    n = ((@armor1_id != 0 && !CP::Cache::Lucius.include?(self.id))) ? $data_armors[@armor1_id].eva : 0
    n += @armor2_id != 0 ? $data_armors[@armor2_id].eva : 0
    n += @armor3_id != 0 ? $data_armors[@armor3_id].eva : 0
    n += @armor4_id != 0 ? $data_armors[@armor4_id].eva : 0
    n += @armor5_id != 0 ? $data_armors[@armor5_id].eva : 0
    n += @armor6_id != 0 ? $data_armors[@armor6_id].eva : 0
    return 100 if n > 100
    return n
  end
  
  def animation1_id
    if CP::Cache::Lucius.include?(self.id)
      result = []
      result.push($data_weapons[@weapon_id].animation1_id) if @weapon_id != 0
      result.push($data_weapons[@armor1_id].animation1_id) if @armor1_id != 0
      result.delete(0)
      return (result.size == 0 ? 0 : result[0])
    end
    return (@weapon_id != 0 ? $data_weapons[@weapon_id].animation1_id : 0)
  end
  
  def animation2_id
    if CP::Cache::Lucius.include?(self.id)
      result = []
      result.push($data_weapons[@weapon_id].animation2_id) if @weapon_id != 0
      result.push($data_weapons[@armor1_id].animation2_id) if @armor1_id != 0
      return (result.size == 0 ? 0 : (result.size == 1 ? result[0] : result))
    end
    return (@weapon_id != 0 ? $data_weapons[@weapon_id].animation2_id : 0)
  end
  
  def class_name
    return $data_classes[@class_id].name
  end
  
  def exp_s
    return @exp_list[@level+1] > 0 ? @exp.to_s : '-------'
  end
  
  def next_exp_s
    return @exp_list[@level+1] > 0 ? @exp_list[@level+1].to_s : '-------'
  end
  
  def next_rest_exp_s
    return @exp_list[@level+1] > 0 ? (@exp_list[@level+1] - @exp).to_s : '-------'
  end
  
  def update_auto_state
    armors = []
    if !CP::Cache::Lucius.include?(self.id)
      armors.push($data_armors[@armor1_id])
    end
    armors.push($data_armors[@armor2_id])
    armors.push($data_armors[@armor3_id])
    armors.push($data_armors[@armor4_id])
    armors.push($data_armors[@armor5_id])
    armors.push($data_armors[@armor6_id])
    armors.compact!
    armors.each {|armor| remove_state(armor.auto_state_id)}
    armors.each {|armor| add_state(armor.auto_state_id)}
  end
  
  def equip_fix?(equip_type)
    case equip_type
    when 0 then return $data_actors[@actor_id].weapon_fix
    when 1 then return $data_actors[@actor_id].armor1_fix
    when 2 then return $data_actors[@actor_id].armor2_fix
    when 3 then return $data_actors[@actor_id].armor3_fix
    when 4 then return $data_actors[@actor_id].armor4_fix
    when 5, 6 then return (@actor_id == 16)
    end
    return false
  end
  
  def equip(equip_type, id)
    if equip_type <= 1
      if CP::Cache::Lucius.include?(self.id)
        if id == 0 || $game_party.weapon_number(id) > 0
          if CP::Cache::TwoHanded.include?(id)
            $game_party.gain_weapon(@weapon_id, 1)
            $game_party.gain_weapon(@armor1_id, 1)
            @weapon_id, @armor1_id = id, 0
            $game_party.lose_weapon(id, 1)
          elsif CP::Cache::TwoHanded.include?(@weapon_id)
            $game_party.gain_weapon(@weapon_id, 1)
            $game_party.gain_weapon(@armor1_id, 1)
            if equip_type == 0
              @weapon_id, @armor1_id = id, 0
            else
              @armor1_id, @weapon_id = 0, id
            end
            $game_party.lose_weapon(id, 1)
          else
            if equip_type == 0
              $game_party.gain_weapon(@weapon_id, 1)
              @weapon_id = id
            elsif equip_type == 1
              $game_party.gain_weapon(@armor1_id, 1)
              @armor1_id = id
            end
            $game_party.lose_weapon(id, 1)
          end
        end
      elsif equip_type == 0
        if id == 0 || $game_party.weapon_number(id) > 0
          $game_party.gain_weapon(@weapon_id, 1)
          @weapon_id = id
          $game_party.lose_weapon(id, 1)
        end
      elsif equip_type == 1
        if id == 0 || $game_party.armor_number(id) > 0
          $game_party.gain_armor(@armor1_id, 1)
          @armor1_id = id
          $game_party.lose_armor(id, 1)
        end
      end
    end
    case equip_type
    when 2
      if id == 0 || $game_party.armor_number(id) > 0
        $game_party.gain_armor(@armor2_id, 1)
        @armor2_id = id
        $game_party.lose_armor(id, 1)
      end
    when 3
      if id == 0 || $game_party.armor_number(id) > 0
        $game_party.gain_armor(@armor3_id, 1)
        @armor3_id = id
        $game_party.lose_armor(id, 1)
      end
    when 4
      if id == 0 || $game_party.armor_number(id) > 0
        $game_party.gain_armor(@armor4_id, 1)
        @armor4_id = id
        $game_party.lose_armor(id, 1)
      end
    when 5
      if id == 0 || $game_party.armor_number(id) > 0
        $game_party.gain_armor(@armor5_id, 1)
        @armor5_id = id
        $game_party.lose_armor(id, 1)
      end
    when 6
      if id == 0 || $game_party.armor_number(id) > 0
        $game_party.gain_armor(@armor6_id, 1)
        @armor6_id = id
        $game_party.lose_armor(id, 1)
      end
    end
    max_hp = self.maxhp
    @hp = max_hp if @hp > max_hp
    max_sp = self.maxsp
    @sp = max_sp if @sp > max_sp
    min_sr = self.minsr
    @sr = min_sr if @sr < min_sr
    max_sr = self.maxsr
    @sr = max_sr if @sr > max_sr
  end
  
  def equippable?(item)
    return ((item.is_a?(RPG::Weapon) &&
        $data_classes[@class_id].weapon_set.include?(item.id)) ||
        (item.is_a?(RPG::Armor) &&
        $data_classes[@class_id].armor_set.include?(item.id)))
  end
  
  def maxexp
    return @exp_list[$data_actors[@actor_id].final_level]
  end
  
  def exp=(exp)
    if exp > 9999999
      @exp = 9999999
    elsif exp < 0
      @exp = 0
    else
      @exp = exp
    end
    if @exp < @exp_list[@level]
      level = @level
      xp = @exp
      while xp < @exp_list[@level]
        @level -= 1
        xp = @exp
        xp = @exp_list[@level] if xp > @exp_list[@level]
      end
      $data_classes[@class_id].learnings.each {|j| (@level+1..level).each {|i|
          forget_skill(j.skill_id) if j.level == i}}
    else
      @level += 1 while @exp >= @exp_list[@level+1] && @exp_list[@level+1] > 0
    end
    $data_classes[@class_id].learnings.each {|j| (1..@level).each {|i|
        learn_skill(j.skill_id) if j.level == i}}
    if @level >= $data_actors[@actor_id].final_level
      @level = $data_actors[@actor_id].final_level
      @exp = @exp_list[@level]
    end
    max_hp = self.maxhp
    @hp = max_hp if @hp > max_hp
    max_sp = self.maxsp
    @sp = max_sp if @sp > max_sp
  end
  
  def fix_class
    if $data_classes[@class_id] == nil
      @class_id = $data_actors[@actor_id].class_id
    end
  end
  
  def level=(lev)
    if lev > $data_actors[@actor_id].final_level
      lev = $data_actors[@actor_id].final_level
    elsif lev < 1
      lev = 1
    end
    self.exp = @exp_list[lev]
  end
  
  def learn_skill(id)
    @skills = CP.resort_skills(@skills + [id]) if id > 0 && !@skills.include?(id)
  end
  
  def forget_skill(skill_id)
    @skills.delete(skill_id)
  end
  
  def dragon_skills(dragon_id)
    result = setup_dragon_skills(dragon_id)
    return result if result.size == 0
    (result | @dragon_skills[dragon_id])
  end
  
  def dragon_learned?(dragon_id)
    return false if self.id != CP::Cache::Sydon
    return @skills.any? {|id| $data_skills[id].plus_state_set.include?(dragon_id)}
  end
  
  def learn_dragon_skill(dragon_id, skill_id)
    result = setup_dragon_skills(dragon_id)
    return if result.size == 0
    if skill_id > 0 && !@dragon_skills[dragon_id].include?(skill_id)
      @dragon_skills[dragon_id].push(skill_id)
      @dragon_skills[dragon_id] = CP.resort_skills(@dragon_skills[dragon_id])
    end
  end
  
  def forget_dragon_skill(dragon_id, skill_id)
    result = setup_dragon_skills(dragon_id)
    return if result.size == 0
    if skill_id > 0 && @dragon_skills[dragon_id].include?(skill_id)
      @dragon_skills[dragon_id].delete(skill_id)
    end
  end
  
  def setup_dragon_skills(dragon_id)
    return [] if self.id != CP::Cache::Sydon
    @dragon_skills = {} if @dragon_skills == nil
    result = CP.trance_database(dragon_id)
    return result if result.size == 0
    @dragon_skills[dragon_id] = [] if @dragon_skills[dragon_id] == nil
    return result
  end
  
  def skill_can_use?(skill_id)
    return (self.skills.include?(skill_id) && super)
  end
  
  def can_use_any_skill?
    return ((self.skills - NO_CONFUSION_IDS).any? {|id| skill_can_use?(id)})
  end
  
  def class_id=(class_id)
    if $data_classes[class_id] != nil
      if self.id == 9
        @class_id = class_id
        equip(0, 0) unless equippable?($data_weapons[@weapon_id])
        equip(1, 0) unless equippable?($data_armors[@armor1_id])
        equip(2, 0) unless equippable?($data_armors[@armor2_id])
        equip(3, 0) unless equippable?($data_armors[@armor3_id])
        equip(4, 0) unless equippable?($data_armors[@armor4_id])
        equip(5, 0) unless equippable?($data_armors[@armor5_id])
        equip(6, 0) unless equippable?($data_armors[@armor6_id])
      elsif self.id == 15
        @class_id = class_id
      end
    end
  end
  
  def set_graphic(character_name, character_hue, battler_name, battler_hue)
    @character_name = character_name
    @character_hue = character_hue
    @battler_name = battler_name
    @battler_hue = battler_hue
  end
  
  def screen_x
    return (self.index != nil ? self.index * 160 + 80 : 0)
  end
  
  def screen_y
    return 464
  end
  
  def screen_z
    return (self.index != nil ? 4 - self.index : 0)
  end
  
end
