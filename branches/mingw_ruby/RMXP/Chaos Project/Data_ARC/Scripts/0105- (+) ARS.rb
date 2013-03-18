#==============================================================================
# Advanced Recognize System by Blizzard
# Version: 2.0b DX
#==============================================================================

#==============================================================================
# Game_System
#==============================================================================

class Game_System
  
  attr_accessor :recognize_mode
  
  alias init_ars_later initialize
  def initialize
    init_ars_later
    @recognize_mode = 0
  end

end

#==============================================================================
# Game_Battler
#==============================================================================

class Game_Battler
  
  alias skill_effect_ars_later skill_effect
  def skill_effect(user, skill)
    return true if CP::Cache::RecognizeIDs.include?(skill.id)
    return skill_effect_ars_later(user, skill)
  end

end

#==============================================================================
# Game_Enemy
#==============================================================================

class Game_Enemy < Game_Battler

  attr_accessor :day_active
  attr_accessor :night_active
  
  alias init_ars_later initialize
  def initialize(troop_id, member_index)
    init_ars_later(troop_id, member_index)
    @day_active = (DAY_ACTIVE.include?(self.id))
    @night_active = (NIGHT_ACTIVE.include?(self.id))
  end

end

#==============================================================================
# Window_Recognize
#==============================================================================

class Window_Recognize < Window_Base

  attr_accessor :mode
  
  def initialize
    super(0, 0, 576, 224)
    @index_enemy, @mode = 0, $game_system.recognize_mode
    self.contents = Bitmap.new(width - 30, height - 32)
    self.ox = 1
    self.x, self.y = 320 - self.width/2, 160 - self.height/2
    self.visible = self.active = false
    case @mode
    when 0 then self.opacity = self.back_opacity = 255
    when 1 then self.back_opacity = 128
    when 2 then self.opacity = 0
    end
    @e = []
    $game_troop.enemies.each {|enemy| @e.push(enemy) if enemy.exist?}
    refresh
  end
  
  def update
    if Input.trigger?($controls.right)
      $game_system.se_play($data_system.cursor_se)
      if @e.size > 1
        @index_enemy = (@index_enemy + 1) % @e.size
        refresh
      end
    elsif Input.trigger?($controls.left)
      $game_system.se_play($data_system.cursor_se)
      if @e.size > 1
        @index_enemy = (@index_enemy + @e.size - 1) % @e.size
        refresh
      end
    end
  end
  
  def refresh
    self.contents.clear
    _HP = "#{$data_system.words.hp}: #{get_hp(@e[@index_enemy])}"
    _SP = "#{$data_system.words.sp}: #{get_sp(@e[@index_enemy])}"
    name = "#{@e[@index_enemy].name}  -  #{_HP}  -  #{_SP}"
    name = "#{@index_enemy+1}.  #{name}" if @e.size > 1
    self.contents.draw_text(1, 0, 544, 32, name, 1)
    draw_special_text(@e[@index_enemy].id)
  end

  def get_hp(enemy)
    over = 'over '
    infinite = 'infinite'
    case enemy.id
    when 38 then return "#{over} 9000"
    when 35 then return '????'
    when 41 then return "#{over} 15000"
    when 42 then return '19???'
    when 31, 47 then return '2????'
    when 32, 61 then return '3????'
    when 92, 93 then return "#{over} 50000"
    when 88 then return '5????'
    when 95 then return '6????'
    when 87 then return '8????'
    when 83 then return "#{over} 80000"
    when 96 then return "#{over} 90000"
    when 34, 43, 77, 78, 94 then return '?????'
    when 97 then return "#{over} 150000"
    when 70, 71, 111, 115 then return "#{over} 200000"
    when 127 then return '29????'
    when 103 then return '25????'
    when 65, 135 then return '3?????'
    when 133 then return "#{over} 350000"
    when 48, 66, 74, 134, 159, 160, 161, 162, 163 then return '??????'
    when 3, 40, 79 then return '???????'
    end
    return enemy.maxhp.to_s
  end
  
  def get_sp(enemy)
    over = 'over '
    infinite = 'infinite'
    case enemy.id
    when 39, 95 then return '3??'
    when 93 then return '4??'
    when 92 then return '5??'
    when 61, 71, 96 then return "#{over} 600"
    when 94 then return "#{over} 700"
    when 77, 78 then return '7??'
    when 31, 32, 69, 70, 74, 83, 87, 88, 111, 115, 127 then return '9??'
    when 34, 41, 43, 50, 65, 66, 97, 103, 133, 134, 135, 159, 160, 161, 162 then return '???'
    when 3, 40, 45, 60, 79, 163 then return infinite
    end
    return enemy.maxsp.to_s
  end
  
  def draw_special_text(id)
    texts, w = CP::ARS.get_recognition(id), self.contents.width
    texts.each_index {|i| self.contents.draw_text(0, (i+1)*32, w, 32, texts[i], 1)}
  end
  
  def switch_mode
    @mode = (@mode + 1) % 3
    $game_system.recognize_mode = @mode
  end
  
end

#==============================================================================
# Scene_Battle
#==============================================================================

class Scene_Battle
  
  alias make_skill_action_result_ars_later make_skill_action_result
  def make_skill_action_result
    test = make_skill_action_result_ars_later
    @recog_window = Window_Recognize.new if test && CP::Cache::RecognizeIDs.include?(@skill.id)
    return test
  end
  
  alias update_phase4_step5_ars_later update_phase4_step5
  def update_phase4_step5
    update_phase4_step5_ars_later
    if @recog_window != nil
      Graphics.freeze
      @recog_window.visible = true
      Graphics.transition(10)
      loop do
        Graphics.update
        Input.update
        @recog_window.update
        @spriteset.update
        $game_screen.update
        if Input.trigger?($controls.confirm)
          $game_system.se_play($data_system.cursor_se)
          Graphics.freeze
          case @recog_window.mode
          when 0 then @recog_window.back_opacity = 128
          when 1 then @recog_window.opacity = 0
          when 2 then @recog_window.opacity = @recog_window.back_opacity = 255
          end
          @recog_window.switch_mode
          Graphics.transition(5)
        elsif Input.trigger?($controls.cancel)
          $game_system.se_play($data_system.cancel_se)
          break
        end
      end
      Graphics.freeze
      @recog_window.dispose
      @recog_window = nil
      Graphics.transition(10)
    end
  end
  
end
