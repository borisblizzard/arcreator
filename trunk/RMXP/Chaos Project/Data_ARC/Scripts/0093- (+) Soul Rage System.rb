#==============================================================================
# Soul Rage System by Blizzard
# Version 2.9b DX
# Date: 15.06.2006
# Date v2.7b DX: 8.9.2006
# Date v2.9b DX: 2.8.2007
#==============================================================================

SRS_rate = 500
RAGE_COLOR = Color.new(255, 255, 255)

#==============================================================================
# Game_Actor
#==============================================================================

class Game_Actor < Game_Battler

  attr_reader   :sr
  attr_accessor :sr_mode
  attr_accessor :def_mode
  
  alias setup_srs_later setup   
  def setup(actor_id)
    self.sr = @sr_mode = @def_mode = 0
    setup_srs_later(actor_id)
  end

  def sr=(sr)
    min_sr = self.minsr
    if sr < min_sr
      @sr = min_sr
    else
      max_sr = self.maxsr
      @sr = (sr > max_sr ? max_sr : sr)
    end
  end
  
  def minsr
    plus = 0
    plus += 300 if @armor4_id == 122
    plus += 300 if @armor5_id == 122
    plus += 300 if @armor6_id == 122
    return plus.to_i
  end
  
  def maxsr
    plus = 1000
    plus += 500 if @armor4_id == 106
    plus += 500 if @armor5_id == 106
    plus += 500 if @armor6_id == 106
    plus += 100 if @states.any? {|id| self.dragon_skills(id).size > 0}
    plus *= 1.25 if @states.include?(41)
    return plus.to_i
  end
  
  def hp=(val)
    super
    self.sr = 0 unless self.hp != 0 || self.states.include?(32)
  end
  
end
 
#==============================================================================
# Game_Battler
#==============================================================================

class Game_Battler
  
  def sr_can_use?(skill_id)
    return false if skill_id == 0
    return false if self.is_a?(Game_Actor) && $data_skills[skill_id].sp_cost > self.sr/10
    return true
  end
  
  alias attack_effect_srs_later attack_effect
  def attack_effect(attacker)
    last_hp = self.hp
    result = attack_effect_srs_later(attacker)
    if self.damage.is_a?(Numeric) && self.damage > 0 &&
        self.is_a?(Game_Actor) && self.hp != 0 && self.sr_mode == 0
      self.sr += self.damage * SRS_rate / last_hp
      self.sr += self.damage * SRS_rate / last_hp / 2 if @armor4_id == 92
      self.sr += self.damage * SRS_rate / last_hp / 2 if @armor5_id == 92
      self.sr += self.damage * SRS_rate / last_hp / 2 if @armor6_id == 92
      self.sr += self.damage * SRS_rate / last_hp / 2 if self.current_action.kind == 5
    end
    return result
  end  
    
  alias skill_effect_srs_later skill_effect
  def skill_effect(user, skill)
    last_hp = self.hp
    result = skill_effect_srs_later(user, skill)
    if self.damage.is_a?(Numeric) && self.damage > 0 &&
        self.is_a?(Game_Actor) && self.hp != 0 && self.sr_mode == 0
      self.sr += self.damage * SRS_rate / last_hp
      self.sr += self.damage * SRS_rate / last_hp / 2 if @armor4_id == 92
      self.sr += self.damage * SRS_rate / last_hp / 2 if @armor5_id == 92
      self.sr += self.damage * SRS_rate / last_hp / 2 if @armor6_id == 92
      self.sr += self.damage * SRS_rate / last_hp / 2 if self.current_action.kind == 5
    end
    return result
  end
  
end

#==============================================================================
# Window_Base
#==============================================================================

class Window_Base < Window
  
  def draw_item_name2(item, x, y, color)
    return if item == nil
    if self.contents.font.color == normal_color
      bitmap = RPG::Cache.icon(item.icon_name)
    else
      bitmap = RPG::Cache.desaturated(item.icon_name)
    end
    self.contents.blt(x, y + 4, bitmap, Rect.new(0, 0, 24, 24))
    self.contents.font.color = color
    self.contents.draw_text(x + 28, y, 288, 32, item.name)
  end
  
end

#==============================================================================
# Menu_RageCommand
#==============================================================================

class Menu_RageCommand < Menu_Command
  
  def initialize(actor)
    super()
    (0...8).each {|i|
        icon = Rage_Icon.new(8, 80, false)
        icon.bitmap = [3]
        @icons.push(icon)}
    @icons[7].bitmap = self.get_dispair_bitmaps
    @index = 0
    @equips = [nil, nil, nil, nil, nil, nil, nil]
    @skill_ids = [0, 0, 0, 0, 0, 0, 0]
    @reqs = [false, false, false, false, false, false, false]
    @need_refresh = []
    update_actor(actor)
    refresh if test_changes
    self.x, self.y, self.visible = 0, 176, true
    @icons.each_index {|i| @icons[i].degrees = i * 360 / 8}
  end
  
  def get_dispair_bitmaps
    begin
      id = (@actor.states.include?(45) ? 'dragmatech' : @actor.class_id)
      icon = RPG::Cache.icon("Battle/Tech/#{id}")
    rescue
      icon = RPG::Cache.icon('Battle/0')
    end
    return [0, icon, RPG::Cache.icon('despair')]
  end
  
  def update
    @icons.each_index {|i|
        @index == i ? @icons[i].blink_on : @icons[i].blink_off
        @icons[i].update}
    if !@icons[0].moving? && self.active
      if Input.repeat?($controls.down)
        $game_system.se_play($data_system.cursor_se)
        @index = (@index + 1) % 8
        @icons.each {|s| s.dir = -1}
      elsif Input.repeat?($controls.up)
        $game_system.se_play($data_system.cursor_se)
        @index = (@index + 7) % 8
        @icons.each {|s| s.dir = 1}
      end
    end
    update_help
  end
  
  def refresh
    @need_refresh.each {|i|
        @icons[i].bitmap.clear if @icons[i].bitmap.is_a?(Bitmap)
        if @equips[i] != nil
          if @skill_ids[i] != 0
            if @reqs[i]
              @icons[i].bitmap = [0, RPG::Cache.icon(@equips[i].icon_name), RPG::Cache.icon($data_skills[@skill_ids[i]].icon_name)]
            else
              @icons[i].bitmap = [1, RPG::Cache.icon(@equips[i].icon_name), RPG::Cache.icon($data_skills[@skill_ids[i]].icon_name)]
            end
          else
            @icons[i].bitmap = [2, RPG::Cache.icon(@equips[i].icon_name)]
          end
        elsif i == 7
          @icons[i].bitmap = self.get_dispair_bitmaps
        else
          @icons[i].bitmap = [3]
        end}
    @need_refresh = []
  end
  
  def setup_rages
    equips = []
    skill_ids = [0, 0, 0, 0, 0, 0, 0]
    reqs = [false, false, false, false, false, false, false]
    (0...7).each {|i|
        weapon = (i == 0)
        equip = nil
        case i
        when 0 then equip = $data_weapons[@actor.weapon_id]
        when 1
          if CP::Cache::Lucius.include?(@actor.id)
            equip = $data_weapons[@actor.armor1_id]
            weapon = true
          else
            equip = $data_armors[@actor.armor1_id]
          end
        when 2 then equip = $data_armors[@actor.armor2_id]
        when 3 then equip = $data_armors[@actor.armor3_id]
        when 4 then equip = $data_armors[@actor.armor4_id]
        when 5 then equip = $data_armors[@actor.armor5_id]
        when 6 then equip = $data_armors[@actor.armor6_id]
        end
        id = (equip == nil ? 0 : equip.id)
        skill_ids[i] = (weapon ? CP.sr_weapons(id) : CP.sr_armors(id, @actor, i))
        reqs[i] = (skill_ids[i] != 0 && @actor.sr_can_use?(skill_ids[i]))
        equips.push(equip)}
    return [equips, skill_ids, reqs]
  end
  
  def test_changes
    new_equips, new_rages, new_reqs = setup_rages
    if new_equips != @equips || new_rages != @skill_ids || new_reqs != @reqs
      (0...7).each {|i|
          if new_equips[i] != @equips[i] || new_rages[i] != @skill_ids[i] || new_reqs[i] != @reqs[i]
            @need_refresh.push(i)
          end}
      @equips, @skill_ids, @reqs = new_equips, new_rages, new_reqs
    end
    @need_refresh |= @need_refresh
    return (@need_refresh.size > 0)
  end
  
  def update_actor(actor)
    @actor = actor
    @need_refresh |= [7]
    reset
  end
  
  def update_help
    if @help_window != nil && self.active
      if @index == 7
        color = Color.new(255, 0, 0)
        text = 'Despair'
        text2 = 'Gains 50% more SR for one turn.'
      elsif @equips[@index] != nil
        if @skill_ids[@index] != 0
          if @actor.sr_can_use?(@skill_ids[@index])
            color = Color.new(0, 255, 0)
          else
            color = Color.new(255, 255, 255, 128)
          end
          text = @equips[@index].name
          text += " » #{$data_skills[@skill_ids[@index]].name}"
          if $data_skills[@skill_ids[@index]].sp_cost != 0
            text += " (#{$data_skills[@skill_ids[@index]].sp_cost}%)"
          end
          text2 = "#{$data_skills[@skill_ids[@index]].description}"
        else
          color = Color.new(255, 255, 255, 128)
          text = @equips[@index].name
          text2 = ''
        end
      else
        color = Color.new(255, 255, 255, 128)
        text = 'Nothing equipped'
        text2 = ''
      end
      @help_window.set_text(text, 1, color, text2)
    end
  end
  
  def visible=(expr)
    refresh if test_changes
    super
  end
  
  def skill
    return $data_skills[@skill_ids[@index]]
  end
  
end

#==============================================================================
# Scene_Battle
#==============================================================================

class Scene_Battle
  
  alias update_phase3_enemy_select_srs_later update_phase3_enemy_select
  def update_phase3_enemy_select
    if Input.trigger?($controls.cancel) &&
        (@active_battler.current_action.kind == 3 ||
        @active_battler.current_action.kind == 4)
      @rage_command_window.active = @rage_command_window.visible = true
    end
    update_phase3_enemy_select_srs_later
  end

  alias update_phase3_actor_select_srs_later update_phase3_actor_select
  def update_phase3_actor_select
    if Input.trigger?($controls.cancel) &&
        (@active_battler.current_action.kind == 3 ||
        @active_battler.current_action.kind == 4)
      @rage_command_window.active = @rage_command_window.visible = true
    end
    update_phase3_actor_select_srs_later
  end

  def update_phase3_rage_select
    @rage_command_window.update
    if Input.trigger?($controls.cancel)
      $game_system.se_play($data_system.cancel_se)
      @actor_command_window.active = @actor_command_window.visible = true
      end_rage_select
    elsif Input.trigger?($controls.confirm)
      if @rage_command_window.index == 7
        $game_system.se_play($data_system.decision_se)
        @active_battler.current_action.kind = 5
        end_rage_select
        phase3_next_actor
      else
        @skill = @rage_command_window.skill
        if @skill == nil || !@active_battler.sr_can_use?(@skill.id)
          $game_system.se_play($data_system.buzzer_se)
          return
        end
        $game_system.se_play($data_system.decision_se)
        @active_battler.current_action.skill_id = @skill.id
        end_rage_select
        case @skill.scope
        when 1 then start_enemy_select
        when 2 then start_enemy_select_all
        when 3, 5 then start_actor_select
        when 4, 6, 9 then start_actor_select_all
        when 7 then start_self_select
        when 8 then start_select_all
        else
          phase3_next_actor
        end
      end
    end
  end
  
  def start_rage_select
    if @rage_command_window == nil
      @rage_command_window = Menu_RageCommand.new(@active_battler)
      @rage_command_window.help_window = @help_window
      @rage_command_window.x = case $game_party.actors.size
      when 1 then 320
      when 2 then 160 + @actor_index * 320
      when 3 then 160 + @actor_index * 160
      when 4 then 80 + @actor_index * 160
      end
    end
    @rage_command_window.active = @rage_command_window.visible = true
    @actor_command_window.active = @actor_command_window.visible = false
  end
  
  def end_rage_select
    @rage_command_window.active = @rage_command_window.visible = false
  end
  
  alias start_phase4_srs_later start_phase4
  def start_phase4(tried_to_escape = false)
    start_phase4_srs_later(tried_to_escape)
    $game_party.actors.each {|actor|
        if !actor.dead? && actor.sr_mode == 1
          actor.sr += 80
          actor.sr += 40 if actor.armor4_id == 92
          actor.sr += 40 if actor.armor5_id == 92
          actor.sr += 40 if actor.armor6_id == 92
          actor.sr += 40 if actor.current_action.kind == 5
        end}
  end
  
  def make_rage_action_result
    @skill = $data_skills[@active_battler.current_action.skill_id]
    unless @active_battler.current_action.forcing ||
        @active_battler.sr_can_use?(@skill.id)
      $game_temp.forcing_battler = nil
      @phase4_step = 1
      return false
    end
    @active_battler.sr -= @skill.sp_cost * 10
    @status_window.refresh
    @help_window.set_text(@skill.name, 1)
    if @skill.id == 371
      @animation1_id = @skill.animation1_id
      @animation2_id = @skill.animation2_id
    else
      @animation1_id, @animation2_id = 108, @skill.animation2_id
    end
    @common_event_id = @skill.common_event_id
    set_target_battlers(@skill.scope)
    @target_battlers.each {|target| target.skill_effect(@active_battler, @skill)}
    return true
  end
  
end
