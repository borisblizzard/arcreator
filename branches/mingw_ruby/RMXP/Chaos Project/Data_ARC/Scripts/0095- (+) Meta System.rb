#==============================================================================
# Meta System and Meta Limit System by Blizzard
# Version 1.0b
# Date: 10.10.2006
#==============================================================================

#==============================================================================
# Game_Actor
#==============================================================================

class Game_Actor < Game_Battler
  
  attr_accessor :meta
  
  alias setup_meta_later setup
  def setup(actor_id)
    setup_meta_later(actor_id)
    meta_state
  end
  
  def meta_state
    if self.sr >= 900
      self.meta = 20 - (self.hp-1)*5 / self.maxhp
    elsif self.sr < 900 && self.sr >= 600
      self.meta = 15 - (self.hp-1)*5 / self.maxhp
    elsif self.sr < 600 && self.sr >= 300
      self.meta = 10 - (self.hp-1)*5 / self.maxhp
    elsif self.sr < 300
      self.meta = 5 - (self.hp-1)*5 / self.maxhp
    end
    if self.meta != 20
      self.meta = 15 if @armor2_id == 123
    end
  end
  
end

#==============================================================================
# Game_Battler
#==============================================================================

class Game_Battler
  
  def make_meta
    w = Window_Base.new(0, 0, 1, 1)
    w.make_battler_state_text(self, 0, false, 0, 0)
    w.dispose
  end
  
end

#==============================================================================
# Window_Base
#==============================================================================

class Window_Base < Window
  
  def make_battler_state_text(battler, width, need_draw, x = 0, y = 0)
    text = ''
    if battler.is_a?(Game_Actor)
      battler.meta_state
      text = CP.meta_text(battler.meta)
    elsif battler.is_a?(Game_Enemy)
      text = CP.meta_text(5 - (battler.hp-1)*5 / battler.maxhp)
    end
    states = battler.states.find_all {|i| battler.dragon_skills(i).size == 0}
    if states.size == 0 && need_draw
      return "»#{text}«" if $scene.is_a?(Scene_Menu) || $scene.is_a?(Scene_File)
      return text
    end
    return '' unless need_draw
    rect = Rect.new(0, 0, 24, 24)
    states.each {|i|
        if CP::Cache::SuperStates.include?($data_states[i].name)
          return $data_states[i].name
        elsif $data_states[i].name == 'Normal'
          return text
        elsif i == 33 || i == 35
          self.contents.blt(x, y + 4, RPG::Cache.icon('stat_proto-shield'), rect)
          return ''
        end}
    w = 0
    states.each {|i|
        if $data_states[i].rating >= 1
          icon = RPG::Cache.icon("stat_#{$data_states[i].name.downcase}")
          self.contents.blt(x + 28 * w, y + 4, icon, rect)
          w += 1
        end
        break if width < 28 * (w+1)}
    return ''
  end
  
  def draw_actor_state(actor, x, y, width = 112, align = 1)
    text = make_battler_state_text(actor, width, true, x, y)
    self.contents.font.color = actor.hp == 0 ? knockout_color : normal_color
    self.contents.draw_text(x, y, width, 32, text, align)
  end

end

#==============================================================================
# Scene_Battle
#==============================================================================

class Scene_Battle
  
  def start_meta_select
    @active_battler.current_action.skill_id = @actor_command_window.get_skill_id
    @skill = $data_skills[@active_battler.current_action.skill_id]
    case @skill.scope
    when 1 then start_enemy_select
    when 2 then start_enemy_select_all
    when 3, 5 then start_actor_select
    when 4, 6, 9 then start_actor_select_all
    when 7 then start_self_select
    when 8, 10 then start_select_all
    else
      phase3_next_actor
    end
  end
  
  def make_meta_action_result
    @skill = $data_skills[@active_battler.current_action.skill_id]
    @active_battler.sr -= 900
    @status_window.refresh
    @help_window.set_text(@skill.name, 1)
    @animation1_id, @animation2_id = @skill.animation1_id, @skill.animation2_id
    @common_event_id = @skill.common_event_id
    set_target_battlers(@skill.scope)
    @target_battlers.each {|target| target.skill_effect(@active_battler, @skill)}
  end
  
end
