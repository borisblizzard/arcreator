#==============================================================================
# Game_Enemy
#==============================================================================

class Game_Enemy
  
  def pdef
    return (super + (@pdef_plus == nil ? 0 : @pdef_plus))
  end
  
  def mdef
    return (super + (@mdef_plus == nil ? 0 : @mdef_plus))
  end
  
end
  
#==============================================================================
# Game_Actor
#==============================================================================

class Game_Actor
  
  alias setup_equap_later setup
  def setup(id)
    setup_equap_later(id)
    CP.gun_database(@armor1_id).each {|e_id| learn_skill(e_id)}
  end
  
  alias equip_equap_later equip
  def equip(equip_type, id)
    CP.gun_database(@armor1_id).each {|e_id| forget_skill(e_id)}
    equip_equap_later(equip_type, id)
    CP.gun_database(@armor1_id).each {|e_id| learn_skill(e_id)}
  end
  
end

#==============================================================================
# Game_Battler
#==============================================================================

MUDLOR_RATE = 50

class Game_Battler
  
  alias attack_effect_mudlor attack_effect
  def attack_effect(attacker)
    result = attack_effect_mudlor(attacker)
    if result && self.is_a?(Game_Enemy) && self.id == 86
      @pdef_plus = 0 if @pdef_plus == nil
      @mdef_plus = 0 if @mdef_plus == nil
      if attacker.element_set.include?(4)
        @pdef_plus -= MUDLOR_RATE
        @mdef_plus -= MUDLOR_RATE
      elsif !attacker.element_set.include?(2)
        @pdef_plus += MUDLOR_RATE
        @mdef_plus += MUDLOR_RATE
      end
    end
    return result
  end
  
  alias skill_effect_mudlor skill_effect
  def skill_effect(user, skill)
    self.remove_state(32) if skill.id == 142
    result = skill_effect_mudlor(user, skill)
    if result && self.is_a?(Game_Enemy) && self.id == 86
      @pdef_plus = 0 if @pdef_plus == nil
      @mdef_plus = 0 if @mdef_plus == nil
      if skill.element_set.include?(4)
        @pdef_plus -= MUDLOR_RATE
        @mdef_plus -= MUDLOR_RATE
      elsif !skill.element_set.include?(2)
        @pdef_plus += MUDLOR_RATE
        @mdef_plus += MUDLOR_RATE
      end
    end
    return result
  end
  
end

#==============================================================================
# RPG::Enemy
#==============================================================================

class RPG::Enemy
  
  def maxhp
    return case @id
    when 3 then 1000000
    when 26 then 1000000
    when 40 then 2000000
    when 44 then 1000000
    when 48 then 100000
    when 49 then 250000
    when 65 then 336189
    when 66 then 102514
    when 69 then 100000
    when 70 then 250000
    when 71 then 169618
    when 73 then 200000
    when 74 then 500000
    when 79 then 1000000
    when 97 then 165873
    when 103 then 250000
    when 111 then 228723
    when 115 then 263475
    when 121 then 100000
    when 122 then 100000
    when 123 then 100000
    when 124 then 100000
    when 125 then 100000
    when 126 then 100000
    when 127 then 292137
    when 133 then 380000
    when 134 then 150000
    when 135 then 300000
    when 159 then 150000
    when 160 then 200000
    when 161 then 200000
    when 162 then 250000
    when 163 then 333333
    else
      @maxhp
    end
  end

end

#==============================================================================
# RPG::Actor
#==============================================================================

class RPG::Actor
  
  PARAMETERS = [
    [[1,9999,0],[1,999,0],[1,999,0],[1,999,0],[1,999,0],[1,999,0]], # template
    [[827,8441,1],[72,744,1],[67,749,0],[81,721,0],[54,502,0],[68,613,-5]],
    [[712,8532,0],[92,845,0],[89,619,1],[139,784,0],[69,600,0],[89,741,-2]],
    [[766,7168,0],[89,812,3],[65,655,-1],[71,677,1],[43,591,-3],[142,883,4]],
    [[911,9999,-4],[78,312,2],[79,727,0],[89,819,1],[72,711,0],[67,672,-4]],
    [[798,9113,0],[72,744,1],[67,749,0],[81,721,0],[54,502,0],[103,589,-5]],
    [[600,7200,0],[70,750,0],[72,756,0],[137,883,0],[90,621,2],[120,871,2]],
    [[9999,9999,0],[999,999,0],[999,999,0],[999,999,0],[999,999,0],[999,999,0]],
    [[6653,6653,0],[560,560,0],[548,548,0],[532,532,0],[370,370,0],[395,395,0]],
    [[827,8441,1],[52,428,0],[78,846,0],[81,721,1],[54,502,0],[68,753,-3]],
    [[579,7180,0],[58,896,0],[49,617,0],[61,527,0],[71,592,0],[64,695,0]],
    [[9999,9999,0],[999,999,0],[999,999,0],[999,999,0],[999,999,0],[999,999,0]],
    [[673,7612,1],[63,470,0],[69,764,0],[111,847,0],[66,589,-1],[63,723,-3]],
    [[963,9881,-3],[91,493,0],[93,897,0],[89,847,0],[30,474,0],[49,689,-2]],
    [[9999,9999,0],[999,999,0],[999,999,0],[999,999,0],[999,999,0],[999,999,0]],
    [[1324,9999,-2],[98,774,0],[89,684,0],[102,778,1],[76,724,-1],[68,713,-2]],
    [[911,9999,-4],[78,312,2],[79,727,0],[89,819,1],[72,711,0],[67,672,-4]]
  ]

  def generate_parameters
    @parameters = Table.new(6, 101)
    table = PARAMETERS[@id]
    table = PARAMETERS[0] if table == nil
    (1..100).each {|l| (0...6).each {|i|
        min, max, factor = table[i]
        range = max - min
        linear = (min + range * ((l - 1) / 98.0)).ceil
        if factor < 0
          curve = (min + range * (((l - 1) / 98.0) ** 2)).ceil
        else
          curve = (max - range * (((99 - l) / 98.0) ** 2)).ceil
        end
        @parameters[i, l] = (curve * factor.abs + linear * (10 - factor.abs)) / 10}}
  end

  def final_level
    return 1 if @id == 7 || @id == 8 || @id == 14
    return 32 if @id == 10
    return 100
  end
  
end

#==============================================================================
# RPG::Weapon
#==============================================================================

class RPG::Weapon
  
  def icon_name
    if @id == 51 && $game_switches && (!$game_switches[50] || $game_switches[168])
      return @icon_name + '_dark'
    end
    return @icon_name
  end
  
  def description
    result = @description
    result += ' (2H)' if CP::Cache::TwoHanded.include?(@id)
    id = CP.sr_weapons(@id)
    return (id != 0 ? "#{result} SR: #{$data_skills[id].name}" : result)
  end
  
end

#==============================================================================
# RPG::Armor
#==============================================================================

class RPG::Armor
  
  def atk
    return case @id
    when 29 then 30
    when 61 then 10
    when 62 then 20
    when 88 then 50
    when 103 then 30
    when 138 then 40
    when 155 then 50
    else
      0
    end
  end
  
  def description
    id = CP.sr_armors(@id)
    if @id == 122
      return "#{@description} SR: Energy"
    elsif id != 0
      return "#{@description} SR: #{$data_skills[id].name}"
    end
    return @description
  end
  
end

#==============================================================================
# RPG::Item
#==============================================================================

class RPG::Item
  
  def name
    return (@id == 117 ? @name + $game_variables[109].to_s : @name)
  end
  
end

#==============================================================================
# RPG::Skill
#==============================================================================

class RPG::Skill
  
  def description
    req = CP.ammo_req(@id)
    if req > 0
      if req == 1
        return "#{@description} (1 bullet)"
      else
        return "#{@description} (#{req} bullets)"
      end
    end
    return @description
  end
  
  def animation2_id
    case @id
    when 254 then return [104, 105, 104, 105, 104, 105]
    end
    return @animation2_id
  end
  
  def scope
    return 8 if [210, 381].include?(@id)
    return 9 if [271, 424].include?(@id)
    return 10 if [161, 219].include?(@id)
    return @scope
  end
  
end

#==============================================================================
# RPG::Animation
#==============================================================================

class RPG::Animation
  
  def max_cells
    result = 0
    @frames.each {|frame| result = frame.cell_max if result < frame.cell_max}
    return result
  end

end

#==============================================================================
# Scene_Save
#==============================================================================

class Window_Yes_No < Window_Selectable

  def initialize
    super(0, 0, 160, 128)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.visible = self.active = false
    self.opacity = 192
    self.y = 240 - self.height/2
    self.z = 12500
    self.windowskin = RPG::Cache.windowskin('Black Death')
    @item_max = 2
    refresh
  end
  
  def refresh
    text = ['Overwrite this file?', 'Yes', 'No']
    self.width = self.contents.text_size(text[0]).width + 40
    self.contents.dispose
    self.contents = Bitmap.new(self.width-32, self.height-32)
    self.x = 320 - self.width / 2
    self.contents.font.color = normal_color
    (0...3).each {|i| self.contents.draw_text(0, i*32, width-32, 32, text[i], 1)}
  end
  
  def update_cursor_rect
    if @index < 0
      self.cursor_rect.empty
      return
    end
    row = @index / @column_max
    self.top_row = row if row < top_row
    self.top_row = row - (page_row_max - 1) if row > top_row + (page_row_max - 1)
    cursor_width = 64
    x = (self.contents.width - cursor_width) / 2
    y = @index / @column_max * 32 - self.oy
    self.cursor_rect.set(x, y + 32, cursor_width, 32)
  end
  
end

#==============================================================================
# Scene_Save
#==============================================================================

class Scene_Save < Scene_File
  
  def main
    @yes_no_flag = [false, $game_temp.last_file_index]
    @yes_no = Window_Yes_No.new
    super
    @yes_no.dispose
  end
  
  alias upd_overwrite_later update
  def update
    if @yes_no_flag[0]
      update_yes_no
      return
    end
    @yes_no.visible = false
    @yes_no.active = false
    upd_overwrite_later
  end
  
  def update_yes_no
    @yes_no.active = true
    @yes_no.visible = true
    @yes_no.update
    $game_temp.last_file_index = @yes_no_flag[1]
    if Input.trigger?($controls.confirm)
      if @yes_no.index == 0
        on_decision(@file_index, true)
        @yes_no_flag[1] = @file_index
      else
        $game_system.se_play($data_system.cancel_se)
        @yes_no_flag[0] = false
        $game_system = Game_System.new if $game_system == nil
      end
    elsif Input.trigger?($controls.cancel)
      $game_system.se_play($data_system.cancel_se)
      @yes_no_flag[0] = false
      $game_system = Game_System.new if $game_system == nil
    end
  end
  
  alias on_decision_overwrite_later on_decision
  def on_decision(file_index, override = false)
    filename = make_filename(file_index)
    if override || !FileTest.exist?(filename)
      @yes_no.active = @yes_no.visible = false
      on_decision_overwrite_later(file_index)
    else
      $game_system.se_play($data_system.decision_se)
      @yes_no_flag[0] = true
      @yes_no.index = 0
    end
  end
  
end

#==============================================================================
# Scene_Map
#==============================================================================

class Game_Map
  
  alias setup_transform_later setup
  def setup(map_id)
    $game_variables[112] = rand(4)
    setup_transform_later(map_id)
    $game_switches[169] = $game_map.leximus
  end
  
end

#==============================================================================
# Scene_Battle
#==============================================================================

DAY_ACTIVE = [2, 11, 12, 15, 16, 20, 21, 54, 64, 86, 112, 113, 119, 145, 146,
              147]
NIGHT_ACTIVE = [5, 8, 10, 13, 22, 25, 36, 37, 53, 56, 57, 85, 106, 108, 110,
                114, 118]

SLEEPING = [5, 13, 15, 53, 64, 85, 86, 106, 110]
BAD_STATE = [8, 22, 53, 112, 145]
STAT_LOSER = [11, 20, 53, 56, 64, 85, 108, 110, 113, 114]
SLEEPING_ID = 7
BAD_ID = [9, 10, 11, 12, 39]
DAY = 26
NIGHT = 27

class Scene_Battle
  
  attr_accessor :spriteset
  
  alias update_ddns_enemies_later update
  def update
    setup_ddns_enemies unless @ddns_enemies
    update_ddns_enemies_later
  end
  
  def setup_ddns_enemies
    @ddns_enemies = true
    unless $game_variables[79] == 3
      $game_troop.enemies.each {|enemy|
          if (enemy.day_active && $game_switches[NIGHT]) ||
              (enemy.night_active && $game_switches[DAY])
            if SLEEPING.include?(enemy.id) && rand(2) == 0
              enemy.add_state(SLEEPING_ID)
            elsif BAD_STATE.include?(enemy.id) && rand(2) == 0
              enemy.add_state(BAD_ID[rand(BAD_ID.size)])
            elsif STAT_LOSER.include?(enemy.id) && rand(2) == 0
              case rand(4)
              when 0 then enemy.str -= enemy.str * rand(6) / 100
              when 1 then enemy.dex -= enemy.dex * rand(6) / 100
              when 2 then enemy.int -= enemy.int * rand(6) / 100
              when 3 then enemy.agi -= enemy.agi * rand(6) / 100
              end
            else
              enemy.hp -= enemy.maxhp * (rand(11) + 5) / 100
            end
          end}
    end
  end

end

# fix for old caterpillar

module Train_Actor
class Game_Party_Actor
end
module Game_Party_Module
class Move_List_Element
end
end
end
