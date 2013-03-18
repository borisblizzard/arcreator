#==============================================================================
# Game_Party
#==============================================================================

class Game_Party
  
  attr_accessor :ufs
  attr_accessor :actors
  attr_reader   :gold
  attr_reader   :steps
  attr_reader   :items
  attr_reader   :weapons
  attr_writer   :characters
  attr_writer   :item_factor
  attr_writer   :gold_factor
  
  def initialize
    @actors = []
    @gold = 0
    @steps = 0
    @items = {}
    @weapons = {}
    @armors = {}
    @ufs = []
    @item_factor = 1
    @gold_factor = 1
  end
  
  def item_factor
    return (@item_factor != nil ? @item_factor : 1)
  end
  
  def gold_factor
    return (@gold_factor != nil ? @gold_factor : 1)
  end
  
  def setup_starting_members
    @actors = []
    $data_system.party_members.each {|i| @actors.push($game_actors[i])}
  end
  
  def setup_battle_test_members
    @actors = []
    $data_system.test_battlers.each {|battler|
        actor = $game_actors[battler.actor_id]
        actor.level = battler.level
        gain_weapon(battler.weapon_id, 1)
        gain_armor(battler.armor1_id, 1)
        gain_armor(battler.armor2_id, 1)
        gain_armor(battler.armor3_id, 1)
        gain_armor(battler.armor4_id, 1)
        actor.equip(0, battler.weapon_id)
        actor.equip(1, battler.armor1_id)
        actor.equip(2, battler.armor2_id)
        actor.equip(3, battler.armor3_id)
        actor.equip(4, battler.armor4_id)
        actor.recover_all
        actor.sr = actor.maxsr
        @actors.push(actor)}
    @items = {}
    (1...$data_items.size).each {|i|
        if $data_items[i].name != '' && [0, 1].include?($data_items[i].occasion)
          @items[i] = 100
        end}
  end
  
  def save
    @copies = []
    @actors.each_index {|i|
        @copies[i] = @actors[i].clone
        @copies[i].save}
    @items = @items.clone
    @weapons = @weapons.clone
    @armors = @armors.clone
    @ufs = @ufs.clone
  end
  
  def apply
    @actors = @copies
    @actors.each {|actor|
        actor.current_action.clear
        actor.damage = 'Timeshift!'
        actor.damage_pop = true
        $game_actors[actor.id] = actor}
    @copies = nil
  end
  
  def refresh
    new_actors = []
    @actors.each_index {|i|
        new_actors.push($game_actors[@actors[i].id]) if $data_actors[@actors[i].id] != nil}
    @actors = new_actors
  end
  
  def max_level
    return 0 if @actors.size == 0
    level = 0
    @actors.each {|actor| level = actor.level if level < actor.level}
    return level
  end
  
  def add_actor(actor_id)
    actor = $game_actors[actor_id]
    if @actors.size < 4 && !@actors.include?(actor)
      @actors.push(actor)
      $game_player.refresh
    end
  end
  
  def remove_actor(actor_id)
    @actors.delete($game_actors[actor_id])
    @actors.compact!
    $game_player.refresh
  end
  
  def gain_gold(n, override = false)
    if CP::Cache::MainParty.any? {|i| @actors.include?($game_actors[i])}
      $game_system.total_money += n if n > 0 && !override
    end
    @gold = @gold + n
    if @gold > 9999999
      @gold = 9999999
    elsif @gold < 0
      @gold = 0
    end
    if CP::Cache::MainParty.any? {|i| @actors.include?($game_actors[i])} &&
        !override && $game_system.most_money < @gold
      $game_system.most_money = @gold
    end
  end
  
  def lose_gold(n)
    gain_gold(-n)
  end
  
  def increase_steps
    @steps += 1
  end
  
  def item_number(item_id)
    return @items.include?(item_id) ? @items[item_id] : 0
  end
  
  def weapon_number(weapon_id)
    return @weapons.include?(weapon_id) ? @weapons[weapon_id] : 0
  end
  
  def armor_number(armor_id)
    return @armors.include?(armor_id) ? @armors[armor_id] : 0
  end
  
  def gain_item(id, n)
    if id > 0
      @items[id] = item_number(id) + n
      if @items[id] > 100
        @items[id] = 100
      elsif @items[id] < 0
        @items[id] = 0
      end
    end
  end
  
  def gain_weapon(id, n)
    if id > 0
      @weapons[id] = weapon_number(id) + n
      if @weapons[id] > 100
        @weapons[id] = 100
      elsif @weapons[id] < 0
        @weapons[id] = 0
      end
    end
  end
  
  def gain_armor(id, n)
    if id > 0
      @armors[id] = armor_number(id) + n
      if @armors[id] > 100
        @armors[id] = 100
      elsif @armors[id] < 0
        @armors[id] = 0
      end
    end
  end
  
  def lose_item(item_id, n)
    gain_item(item_id, -n)
  end
  
  def lose_weapon(weapon_id, n)
    gain_weapon(weapon_id, -n)
  end
  
  def lose_armor(armor_id, n)
    gain_armor(armor_id, -n)
  end
  
  def item_can_use?(item_id)
    return false if item_number(item_id) == 0
    occasion = $data_items[item_id].occasion
    if $game_temp.event_menu
      return false if $data_items[item_id].common_event_id != 0
    end
    return ([0, 1].include?(occasion)) if $game_temp.in_battle
    return ([0, 2].include?(occasion))
  end
  
  def ammo_can_use?(skill_id, ammo_id)
    return (item_number(ammo_id) >= CP.ammo_req(skill_id))
  end
  
  def clear_actions
    @actors.each {|actor|
        actor.current_action.clear
        actor.guarded_by = []}
  end
  
  def reset_slip_damage
    @actors.each {|actor| actor.can_slip_damage = true}
  end
  
  def inputable?
    return (@actors.any? {|actor| actor.inputable?})
  end
  
  def all_dead?
    return false if $game_party.actors.size == 0
    return !(@actors.any? {|actor| actor.hp > 0 || actor.states.include?(32)})
  end
  
  def check_map_slip_damage
    @actors.each {|actor|
        if actor.hp > 0 && actor.slip_damage? && !actor.regen?
          damage = actor.maxhp / 100
          damage = 1 if damage < 1
          if damage >= actor.hp
            actor.hp = 1
          else
            actor.hp -= damage
          end
          $game_screen.start_flash(Color.new(255, 0, 0, 128), 4)
          $game_temp.gameover = $game_party.all_dead?
        end}
  end
  
  def do_damage(val)
    $game_temp.gameover = true
    @actors.each {|actor|
        if actor.hp > 0
          actor.hp -= val
          $game_system.se_play($data_system.actor_collapse_se) if actor.hp == 0
          $game_temp.gameover = false if actor.hp > 0
        end}
  end
  
  def random_target_actor(hp0 = false, override = false)
    roulette = []
    @actors.each {|actor|
        if (hp0 ? actor.hp0? : actor.exist?)
          position = $data_classes[actor.class_id].position
          (0...(4 - position)).each {|i|
              if actor.guarded_by.size > 0 && !override
                roulette.push(actor.guarded_by[rand(actor.guarded_by.size)])
              else
                roulette.push(actor)
              end}
        end}
    return (roulette.size == 0 ? nil : roulette[rand(roulette.size)])
  end
  
  def decide_cover_target
    roulette = @actors.find_all {|actor| actor.coverable?}
    return (roulette.size == 0 ? nil : roulette[rand(roulette.size)])
  end
  
  def random_target_actor_hp0
    return random_target_actor(true)
  end
  
  def random_target_actor_con
    return random_target_actor(false, true)
  end
  
  def smooth_target_actor(actor_index)
    actor = @actors[actor_index]
    return actor if actor != nil && actor.exist?
    @actors.each {|actor| return actor if actor.exist?}
  end
  
  def can_use_any_item?
    return (@items.keys.any? {|id|
        @items[id] > 0 && [0, 1].include?($data_items[id].occasion)})
  end
  
  def can_use_any_uf?
    return (@ufs != nil && @ufs.any? {|id| uf_can_use?(id)})
  end
  
  def uf_can_use?(id)
    alive = 0
    @actors.each {|actor| alive += 1 unless actor.dead?}
    return true if id == -1 && alive > 1
    return false if !uf_req(id).include?(alive)
    return !(@actors.any? {|actor|
        !actor.dead? && actor.sr < $data_skills[id].sp_cost * 10})
  end
  
  def uf_req(id)
    case id
    when 223 then return [2, 3]
    when 224 then return [3]
    when 225 then return [2, 3, 4]
    when 226 then return [3, 4]
    when 252 then return [4]
    when 254 then return [3, 4]
    when 306 then return [4]
    when 361 then return [2, 3, 4]
    when 433 then return [4]
    when 442 then return [4]
    when 448 then return [2, 3, 4]
    end
    return []
  end
  
  def add_uf(id)
    @ufs = CP.resort_skills(@ufs + [id]) if id > 0 && !@ufs.include?(id)
  end
  
  def any_dead?
    return (@actors.any? {|actor| actor.dead?})
  end
  
  def no_info?
    return (@actors.any? {|actor| actor.no_info?} ||
        @actors.include?($game_actors[1]))
  end
  
end
