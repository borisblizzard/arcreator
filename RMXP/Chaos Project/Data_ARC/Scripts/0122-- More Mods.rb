#==============================================================================
# Game_Actor
#==============================================================================

class Game_Actor < Game_Battler
  
  attr_reader :exp_factor
  
  alias setup_exp_later setup
  def setup(actor_id)
    self.exp_factor = 100000
    setup_exp_later(actor_id)
  end
  
  def exp_factor=(factor)
    if factor > 120000
      @exp_factor = 120000
    elsif factor < 100000
      @exp_factor = 100000
    else
      @exp_factor = factor
    end
  end
  
end

#==============================================================================
# Game_Battler
#==============================================================================

REFLECT_ID = 40
REFLECT_ANIMATION = 168
BREAK_REFLECT = [6, 77, 78, 79, 80, 84, 85, 98, 99, 130, 131, 132, 133, 141,
                 142, 150, 152, 158, 160, 161, 168, 187, 188, 192, 197, 199,
                 207, 214, 219, 224, 225, 226, 233, 237, 238, 249, 251, 252,
                 254, 256, 257, 258, 282, 283, 284, 285, 297, 306, 307, 309,
                 310, 311, 313, 322, 326, 333, 334, 335, 339, 349, 351, 361,
                 364, 371, 372, 378, 402, 407, 408, 409, 411, 421, 422, 424,
                 428, 431, 433, 435, 438, 441, 442, 448]

class Game_Battler
  
  # EXP Factor
  
  alias attack_effect_exp_later attack_effect
  def attack_effect(attacker)
    result = attack_effect_exp_later(attacker)
    if attacker.is_a?(Game_Actor)
      if self.damage.is_a?(Numeric) && self.damage > 0
        attacker.exp_factor += 3000 * self.damage / attacker.maxhp
      end
      attacker.exp_factor = 100000 if attacker.dead?
    elsif self.is_a?(Game_Actor)
      self.exp_factor -= 2000 if self.damage.is_a?(Numeric) && self.damage > 0
      self.exp_factor = 100000 if self.dead?
    end
    return result
  end
    
  alias skill_effect_exp_later skill_effect
  def skill_effect(user, skill)
    result = skill_effect_exp_later(user, skill)
    if user.is_a?(Game_Actor)
      if self.damage.is_a?(Numeric) && self.damage > 0
        user.exp_factor += 3000 * self.damage / user.maxhp
      end
      user.exp_factor = 100000 if user.dead?
    elsif self.is_a?(Game_Actor)
      self.exp_factor -= 2000 if self.damage.is_a?(Numeric) && self.damage > 0
      self.exp_factor = 100000 if self.dead?
    end
    return result
  end
  
  # Dragon Trance
  
  alias add_state_dragon_trance add_state
  def add_state(state_id)
    result = add_state_dragon_trance(state_id)
    if result
      if self.is_a?(Game_Actor) && CP::Cache::BadStates.include?(state_id)
        self.sr += 80
        self.sr += 40 if @armor4_id == 92
        self.sr += 40 if @armor5_id == 92
        self.sr += 40 if @armor6_id == 92
        self.sr += 40 if self.current_action.kind == 5
      end
      @disappear = true if state_id == 50 && @battler_name != 'empty'
      if self.dragon_skills(state_id).size > 0
        $game_temp.trance = true
        self.damage = $data_states[state_id].name
        @states_turn[state_id] += 1 if @armor4_id == 180
        @states_turn[state_id] += 1 if @armor5_id == 180
        @states_turn[state_id] += 1 if @armor6_id == 180
      end
    end
    return result
  end
  
  alias remove_state_dragon_trance remove_state
  def remove_state(state_id)
    result = remove_state_dragon_trance(state_id)
    if result
      @disappear = false if state_id == 50
      $game_temp.trance = false if self.dragon_skills(state_id).size > 0
    end
    return result
  end
  
  # Reflection
  
  alias skill_effect_reflect_later skill_effect
  def skill_effect(user, skill, reflect = false)
    if reflect || !test_reflection(skill)
      return skill_effect_reflect_later(user, skill)
    end
    return false
  end
  
  def test_reflection(skill)
    return ((skill.int_f > 0 || skill.mdef_f > 0 ||
        skill.plus_state_set.size > 0 && skill.power == 0 &&
        skill.atk_f == 0 && skill.str_f == 0 && skill.dex_f == 0) &&
        @states.include?(REFLECT_ID) && !BREAK_REFLECT.include?(skill.id) &&
        !skill.minus_state_set.include?(REFLECT_ID))
  end
  
end

#==============================================================================
# Scene_Battle
#==============================================================================

class Scene_Battle
  
  alias main_reflect_later main
  def main
    @old_targets = []
    main_reflect_later
  end
  
  alias set_target_battlers_reflect_later set_target_battlers
  def set_target_battlers(scope, override = false)
    if !BREAK_REFLECT.include?(@skill.id) && !override &&
        @active_battler.current_action.kind == 1
      return []
    end
    return set_target_battlers_reflect_later(scope)
  end
  
  alias make_skill_action_result_reflect_later make_skill_action_result
  def make_skill_action_result
    result = make_skill_action_result_reflect_later
    if result && !BREAK_REFLECT.include?(@skill.id)
      set_target_battlers(@skill.scope, true)
      @target_battlers.each_index {|i|
          if @skill != nil && @active_battler.current_action.kind == 1 &&
              @target_battlers[i].test_reflection(@skill)
            new_target = swap_targets(@target_battlers[i], @active_battler)
            if @target_battlers[i] != new_target
              @old_targets.push(@target_battlers[i])
              @target_battlers[i] = new_target
            end
          end}
      @target_battlers.each {|target|
          dam = (target.damage.is_a?(Numeric) ? target.damage : 0)
          target.skill_effect(@active_battler, @skill, true)
          target.damage += dam if target.damage.is_a?(Numeric)
          target.animation_hit = (target.damage != 'Missed')}
    end
    return result
  end
  
  alias update_phase4_step4_reflect_later update_phase4_step4
  def update_phase4_step4
    @old_targets.each {|target| target.animation_id = REFLECT_ANIMATION}
    @old_targets = []
    update_phase4_step4_reflect_later
  end
  
  def swap_targets(battler1, battler2)
    if battler1.is_a?(Game_Enemy) && battler2.is_a?(Game_Enemy)
      actors = []
      $game_party.actors.each {|actor| actors.push(actor) if actor.exist?}
      battler3 = actors[rand(actors.size)]
    elsif battler1.is_a?(Game_Actor) && battler2.is_a?(Game_Actor)
      enemies = []
      $game_troop.enemies.each {|enemy| enemies.push(enemy) if enemy.exist?}
      battler3 = enemies[rand(enemies.size)]
    elsif battler1.is_a?(Game_Enemy) && battler2.is_a?(Game_Actor)
      actors = []
      $game_party.actors.each {|actor| actors.push(actor) if actor.exist?}
      battler3 = actors[rand(actors.size)]
    elsif battler1.is_a?(Game_Actor) && battler2.is_a?(Game_Enemy)
      enemies = []
      $game_troop.enemies.each {|enemy| enemies.push(enemy) if enemy.exist?}
      battler3 = enemies[rand(enemies.size)]
    else
      battler3 = battler2
    end
    if CP::Cache::AbsorbHP.include?(@skill) || CP::Cache::AbsorbSP.include?(@skill)
      loop do
        break if battler2 != battler3
        if battler2.is_a?(Game_Actor)
          actors = []
          $game_party.actors.each {|actor| actors.push(actor) if actor.exist?}
          battler3 = actors[rand(actors.size)]
        elsif battler2.is_a?(Game_Enemy)
          enemies = []
          $game_troop.enemies.each {|enemy| enemies.push(enemy) if enemy.exist?}
          battler3 = enemies[rand(enemies.size)]
        end
      end
    end
    return battler3
  end
  
end

#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=
# Death Image by Blizzard
# Version: 1.0
# Type: Graphic Alteration
# Date: 17.12.2007
#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=

#==============================================================================
# Sprite_BattlerDummy
#==============================================================================

class Sprite_BattlerDummy < RPG::Sprite
  
  attr_accessor :battler
  
  def initialize(viewport, battler = nil)
    super(viewport)
    @battler = battler
    @battler_visible = false
  end
  
  def update
    return if @battler == nil
    super
    if @battler_name != @battler.battler_name2 ||
        @battler_hue != @battler.battler_hue
      @battler_name = @battler.battler_name2
      @battler_hue = @battler.battler_hue
      self.bitmap = RPG::Cache.battler('invs/' + @battler_name, @battler_hue)
      @width, @height = bitmap.width, bitmap.height
      self.ox, self.oy = @width / 2, @height
      self.opacity = 0 if @battler.dead? || @battler.hidden
    end
    if @battler.is_a?(Game_Actor) && @battler_visible
      if $game_temp.battle_main_phase
        self.opacity += 3 if self.opacity < 255
      else
        self.opacity -= 3 if self.opacity > 207
      end
      self.x = case $game_party.actors.size
      when 1 then @battler.screen_x + 240
      when 2 then @battler.screen_x + 80 + @battler.index * 160
      when 3 then @battler.screen_x + 80
      when 4 then @battler.screen_x
      end
    elsif @battler.is_a?(Game_Enemy)
      self.x = @battler.screen_x
    end
    if @battler_visible
      if @battler.animation_id != 0
        animation = $data_animations[@battler.animation_id]
        animation(animation, @battler.animation_hit)
        @battler.animation_id = 0
      end
      if !@battler.hidden && !@battler.dead? &&
          (@battler.damage == nil || @battler.damage_pop)
        escape
        @battler_visible = false
      end
    elsif @battler.dead? && @battler.damage == nil
      appear
      @battler_visible = true
    end
    if battler.is_a?(Game_Actor)
      self.x = case $game_party.actors.size
      when 1 then @battler.screen_x + 240
      when 2 then @battler.screen_x + 80 + @battler.index * 160
      when 3 then @battler.screen_x + 80
      when 4 then @battler.screen_x
      end
    elsif battler.is_a?(Game_Enemy)
      self.x = @battler.screen_x
    end
    self.y, self.z = @battler.screen_y, @battler.screen_z
  end
  
end

#==============================================================================
# Spriteset_Battle
#==============================================================================

class Spriteset_Battle
  
  alias init_death_image_later initialize
  def initialize
    @death_sprites = [nil, nil, nil, nil]
    init_death_image_later
  end
  
  alias disp_death_image_later dispose
  def dispose
    disp_death_image_later
    @death_sprites.each {|sprite| sprite.dispose if sprite != nil}
  end
  
  alias upd_death_image_later update
  def update
    @death_sprites.each_index {|i| 
        if $game_party.actors[i] != nil
          if $game_party.actors[i].dead?
            if @death_sprites[i] == nil
              @death_sprites[i] = Sprite_BattlerDummy.new(@viewport2)
              @death_sprites[i].opacity = 0
              @death_sprites[i].battler = $game_party.actors[i]
              @death_sprites[i].update
            end
          elsif @death_sprites[i] != nil && @death_sprites[i].opacity == 0
            @death_sprites[i].dispose
            @death_sprites[i] = nil
          end
        end}
    @death_sprites.each {|sprite| sprite.update if sprite != nil}
    upd_death_image_later
  end
  
  alias refresh_death_image_later refresh
  def refresh
    refresh_death_image_later
    @death_sprites.each_index {|i|
        if @death_sprites[i] != nil
          @death_sprites[i].battler = $game_party.actors[i]
        end}
  end
  
end
