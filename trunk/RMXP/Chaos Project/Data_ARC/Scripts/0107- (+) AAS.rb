#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=
# Advanced Analyze System by Blizzard
# Version: 2.0b CP DX
# Date v1.0: 5.7.2006
# Date v1.1b: 31.8.2006
# Date v1.2b: 23.2.2007
# Date v1.3b: 7.7.2007
# Date v2.0b: 12.7.2007
#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=

#==============================================================================
# Game_System
#==============================================================================

class Game_System
  
  attr_accessor :analyze_mode
  
  alias init_aas_later initialize
  def initialize
    init_aas_later
    @analyze_mode = 0
  end
  
end

#==============================================================================
# Game_Battler
#==============================================================================

class Game_Battler
  
  alias skill_effect_aas_later skill_effect
  def skill_effect(user, skill)
    return true if CP::Cache::AnalyzeIDs.include?(skill.id)
    return skill_effect_aas_later(user, skill)
  end

end

#==============================================================================
# Game_Enemy
#==============================================================================

class Game_Enemy < Game_Battler

  attr_reader :cant_analyze
  attr_reader :immune
  
  alias init_aas_later initialize
  def initialize(troop_id, member_index)
    init_aas_later(troop_id, member_index)
    @cant_analyze = (CP::Cache::CantAnalyze.include?(self.id))
    @immune = (CP::Cache::Immune.include?(self.id))
    @boss = ($data_enemies[self.id].element_ranks[CP::Cache::DBoss] != 3)
    @superboss = ($data_enemies[self.id].element_ranks[CP::Cache::DSBoss] != 3)
  end
  
  def boss
    return (@boss || @superboss || @enemy_id == 40)
  end

  def superboss
    return @superboss
  end

end

#==============================================================================
# Window_Analyze
#==============================================================================

class Window_Analyze < Window_Base

  attr_accessor :mode
  
  def initialize
    super(0, 0, 576, 224)
    @index_enemy = 0
    @index_page = 0
    @pages = 12
    @mode = $game_system.analyze_mode
    self.contents = Bitmap.new(width - 30, height - 30)
    self.ox = self.oy = 1
    self.contents.font.name = $fontface
    self.contents.font.size = $fontsize
    self.contents.font.bold = true if $fontface == 'Papyrus'
    self.x = 320 - self.width / 2
    self.y = 160 - self.height / 2
    self.visible = false
    self.active = false
    refresh
  end
  
  def update
    if Input.trigger?($controls.right)
      $game_system.se_play($data_system.cursor_se)
      @index_enemy = (@index_enemy + 1) % @enemies.size
      refresh
    elsif Input.trigger?($controls.left)
      $game_system.se_play($data_system.cursor_se)
      @index_enemy = (@index_enemy + @enemies.size - 1) % @enemies.size
      refresh
    elsif Input.trigger?($controls.down)
      $game_system.se_play($data_system.cursor_se)
      @index_page = (@index_page + 1) % @pages
      refresh
    elsif Input.trigger?($controls.up)
      $game_system.se_play($data_system.cursor_se)
      @index_page = (@index_page + @pages - 1) % @pages
      refresh
    end
  end
  
  def refresh
    case @mode
    when 0
      self.opacity = 255
      self.back_opacity = 255
    when 1 then self.back_opacity = 128
    when 2 then self.opacity = 0
    end
    self.contents.clear
    x = 5
    ox = x + 160
    y = 1
    @enemies = []
    $game_troop.enemies.each {|enemy| @enemies.push(enemy) if enemy.exist?}
    enemy = @enemies[@index_enemy]
    w = self.width - self.contents.text_size(enemy.name).width
    if enemy.day_active
      activity = '  (Day Active)'
    elsif enemy.night_active
      activity = '  (Night Active)'
    else
      activity = ''
    end
    name = "#{enemy.name}#{activity}"
    name = "#{@index_enemy+1}.  #{name}" if @enemies.size > 1
    self.contents.draw_text(1, y, 544, 32, name, 1)
    unless enemy.cant_analyze
      ext_el = 'Extremely efficient elements:'
      eff_el = 'Efficient elements:'
      res_el = 'Elemental resistances:'
      nul_el = 'Elemental nullifications:'
      abs_el = 'Elemental absorptions:'
      ext_sta = 'Extremely efficient status effects:'
      eff_sta = 'Efficient status effects:'
      res_sta = 'Status effect resistances:'
      str_sta = 'Strong status effect resistances:'
      imu_sta = 'Status effect immunities:'
      every = 'Every negative status effect'
      case @index_page
      when 0
        if enemy.item_id > 0
          drop = $data_items[enemy.item_id]
        elsif enemy.weapon_id > 0
          drop = $data_weapons[enemy.weapon_id]
        elsif enemy.armor_id > 0
          drop = $data_armors[enemy.armor_id]
        else
          drop = nil
        end
        t = "#{drop.name} (#{enemy.treasure_prob}% chance)" if drop != nil
        self.contents.draw_text(x+64, y+32, 128, 32, $data_system.words.hp, 2)
        self.contents.draw_text(x+64, y+64, 128, 32, $data_system.words.sp, 2)
        self.contents.draw_text(x+64, y+96, 128, 32, 'EXP', 2)
        self.contents.draw_text(x+64, y+128, 128, 32, $data_system.words.gold, 2)
        self.contents.draw_text(x+64, y+160, 128, 32, 'Drops', 2)
        self.contents.draw_text(ox+64, y+32, 256, 32, "#{enemy.hp} / #{enemy.maxhp}")
        self.contents.draw_text(ox+64, y+64, 256, 32, "#{enemy.sp} / #{enemy.maxsp}")
        self.contents.draw_text(ox+64, y+96, 256, 32, enemy.exp.to_s)
        gold_text = "#{(enemy.gold*0.9).to_i} - #{(enemy.gold*1.1).to_i}"
        self.contents.draw_text(ox+64, y+128, 256, 32, gold_text)
        self.contents.draw_text(ox+64, y+160, 320, 32, (drop != nil ? t : 'nothing'))
      when 1
        self.contents.draw_text(x, y+32, 536, 32, 'Attributes:', 1)
        self.contents.draw_text(x+32, y+64, 128, 32, $data_system.words.str, 2)
        self.contents.draw_text(x+32, y+96, 128, 32, $data_system.words.dex, 2)
        self.contents.draw_text(x+32, y+128, 128, 32, $data_system.words.agi, 2)
        self.contents.draw_text(x+32, y+160, 128, 32, $data_system.words.int, 2)
        self.contents.draw_text(ox+32, y+64, 256, 32, enemy.str.to_s)
        self.contents.draw_text(ox+32, y+96, 256, 32, enemy.dex.to_s)
        self.contents.draw_text(ox+32, y+128, 256, 32, enemy.agi.to_s)
        self.contents.draw_text(ox+32, y+160, 256, 32, enemy.int.to_s)
        self.contents.draw_text(x+256, y+64, 160, 32, $data_system.words.atk, 2)
        self.contents.draw_text(x+256, y+96, 160, 32, $data_system.words.pdef, 2)
        self.contents.draw_text(x+256, y+128, 160, 32, $data_system.words.mdef, 2)
        self.contents.draw_text(x+256, y+160, 160, 32, 'Evasion', 2)
        self.contents.draw_text(ox+288, y+64, 256, 32, enemy.atk.to_s)
        self.contents.draw_text(ox+288, y+96, 256, 32, enemy.pdef.to_s)
        self.contents.draw_text(ox+288, y+128, 256, 32, enemy.mdef.to_s)
        self.contents.draw_text(ox+288, y+160, 256, 32, enemy.eva.to_s)
      when 2
        self.contents.draw_text(x, y+32, 536, 32, ext_el, 1)
        draw_elements(enemy, x, y, 1)
      when 3
        self.contents.draw_text(x, y+32, 536, 32, eff_el, 1)
        draw_elements(enemy, x, y, 2)
      when 4
        self.contents.draw_text(x, y+32, 536, 32, res_el, 1)
        draw_elements(enemy, x, y, 4)
      when 5
        self.contents.draw_text(x, y+32, 536, 32, nul_el, 1)
        draw_elements(enemy, x, y, 5)
      when 6
        self.contents.draw_text(x, y+32, 536, 32, abs_el, 1)
        draw_elements(enemy, x, y, 6)
      when 7
        self.contents.draw_text(x, y+32, 536, 32, ext_sta, 1)
        draw_states(enemy, x, y, 1)
      when 8
        self.contents.draw_text(x, y+32, 536, 32, eff_sta, 1)
        draw_states(enemy, x, y, 2)
      when 9
        self.contents.draw_text(x, y+32, 536, 32, res_sta, 1)
        draw_states(enemy, x, y, 4)
      when 10
        self.contents.draw_text(x, y+32, 536, 32, str_sta, 1)
        draw_states(enemy, x, y, 5)
      when 11
        self.contents.draw_text(x, y+32, 536, 32, imu_sta, 1)
        if enemy.immune
          self.contents.draw_text(x, y+64, 536, 32, every, 1)
        else
          draw_states(enemy, x, y, 6)
        end
      end
    else
      self.contents.draw_text(1, y+96, 544, 32, 'Cannot analyze this enemy', 1)
    end
  end
  
  def draw_elements(enemy, x, y, index)
    elements = []
    (1...$data_system.elements.size).each {|id|
        if !CP::Cache::DummyElements.include?(id) &&
            index == $data_enemies[@enemies[@index_enemy].id].element_ranks[id]
          elements.push($data_system.elements[id])
        end}
    if elements.size == 0
      self.contents.draw_text(x, y+64, 544, 32, 'Nothing')
    else
      rect = Rect.new(0, 0, 24, 24)
      elements.each_index {|i|
          icon = RPG::Cache.icon("elm_#{elements[i].downcase}")
          self.contents.blt(x + i%3*160, y+68 + i/3*32, icon, rect)
          self.contents.draw_text(x + i%3*160 + 32, y+64 + i/3*32, 164, 32, elements[i])}
    end
  end
    
  def draw_states(enemy, x, y, index)
    states = []
    (1...$data_states.size).each {|id|
        if !CP::Cache::DummyStates.include?(id) &&
            index == $data_enemies[@enemies[@index_enemy].id].state_ranks[id]
          states.push($data_states[id].name)
        end}
    if states.size == 0
      self.contents.draw_text(x, y+64, 544, 32, 'Nothing')
    else
      rect = Rect.new(0, 0, 24, 24)
      states.each_index {|i|
          icon = RPG::Cache.icon("stat_#{states[i].downcase}")
          self.contents.blt(x + i%3*160, y+68 + i/3*32, icon, rect)
          self.contents.draw_text(x + i%3*160 + 32, y+64 + i/3*32, 164, 32, states[i])}
    end
  end
    
end

#==============================================================================
# Scene_Battle
#==============================================================================

class Scene_Battle
  
  
  alias make_skill_action_result_aas_later make_skill_action_result
  def make_skill_action_result
    result = make_skill_action_result_aas_later
    @anlyz_window = Window_Analyze.new if result && CP::Cache::AnalyzeIDs.include?(@skill.id)
    return result
  end
  
  alias make_rage_action_result_aas_later make_rage_action_result
  def make_rage_action_result
    result = make_rage_action_result_aas_later
    @anlyz_window = Window_Analyze.new if result && CP::Cache::AnalyzeIDs.include?(@skill.id)
    return result
  end
  
  alias update_phase4_step5_aas_later update_phase4_step5
  def update_phase4_step5
    update_phase4_step5_aas_later
    if @anlyz_window != nil
      Graphics.freeze
      @anlyz_window.visible = true
      Graphics.transition(10)
      loop do
        Graphics.update
        Input.update
        @anlyz_window.update
        @spriteset.update
        $game_screen.update
        if Input.trigger?($controls.confirm)
          $game_system.se_play($data_system.cursor_se)
          Graphics.freeze
          case @anlyz_window.mode
          when 0 then @anlyz_window.back_opacity = 128
          when 1 then @anlyz_window.opacity = 0
          when 2 then @anlyz_window.opacity = @anlyz_window.back_opacity = 255
          end
          $game_system.analyze_mode = ($game_system.analyze_mode+1) % 3
          @anlyz_window.mode = $game_system.analyze_mode
          Graphics.transition(5)
        elsif Input.trigger?($controls.cancel)
          $game_system.se_play($data_system.cancel_se)
          break
        end
      end
      Graphics.freeze
      @anlyz_window.dispose
      @anlyz_window = nil
      Graphics.transition(10)
    end
  end
  
end
