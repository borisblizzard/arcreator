#==============================================================================
# UF_Trigger
#==============================================================================

class UF_Trigger < Sprite
  
  def initialize(mode, viewport = nil)
    super(viewport)
    @mode = mode
    case @mode
    when 0
      self.bitmap = RPG::Cache.picture('uf_ring')
      self.x, self.y, self.ox, self.oy, self.z = 320, 160, 32, 32, 500
      @sub_sprites = [Sprite.new(viewport), Sprite.new(viewport), Sprite.new(viewport)]
      (0...3).each {|i|
          @sub_sprites[i].bitmap = Bitmap.new(4, 20)
          @sub_sprites[i].bitmap.fill_rect(0, 0, 4, 20, Color.new(255, 255, 255, 80))
          @sub_sprites[i].bitmap.fill_rect(1, 0, 2, 20, Color.new(255, 255, 255, 160))
          @sub_sprites[i].bitmap.fill_rect(0, 1, 4, 18, Color.new(255, 255, 255, 160))
          @sub_sprites[i].bitmap.fill_rect(1, 1, 2, 18, Color.new(255, 255, 255))
          @sub_sprites[i].x, @sub_sprites[i].y = 320, 160
          @sub_sprites[i].ox, @sub_sprites[i].oy = 2, 40
          @sub_sprites[i].z, @sub_sprites[i].angle = 600, i*120}
    when 1
      self.bitmap = RPG::Cache.picture('uf_hitring')
      self.x, self.y, self.ox, self.oy, self.z = 320, 160, 32, 32, 500
      @sub_sprites = [Sprite.new(viewport), Sprite.new(viewport), Sprite.new(viewport)]
      (0...2).each {|i|
          @sub_sprites[i].bitmap = Bitmap.new(4, 20)
          @sub_sprites[i].bitmap.fill_rect(0, 0, 4, 20, Color.new(255, 255, 255, 80))
          @sub_sprites[i].bitmap.fill_rect(1, 0, 2, 20, Color.new(255, 255, 255, 160))
          @sub_sprites[i].bitmap.fill_rect(0, 1, 4, 18, Color.new(255, 255, 255, 160))
          @sub_sprites[i].bitmap.fill_rect(1, 1, 2, 18, Color.new(255, 255, 255))
          @sub_sprites[i].x, @sub_sprites[i].y = 320, 160
          @sub_sprites[i].ox, @sub_sprites[i].oy = 2, 40
          @sub_sprites[i].z, @sub_sprites[i].angle = 600, i*180}
    when 2
      self.bitmap = Bitmap.new(48, 128)
      self.bitmap.fill_rect(0, 0, 48, 128, Color.new(255, 255, 255))
      self.bitmap.fill_rect(1, 1, 46, 126, Color.new(0, 0, 0, 160))
      self.x, self.y, self.ox, self.oy, self.z = 320, 160, 24, 64, 500
      @sub_sprites = [Sprite.new(viewport), Sprite.new(viewport), Sprite.new(viewport)]
      (0...2).each {|i|
          @sub_sprites[i].bitmap = RPG::Cache.picture('uf_indicator')
          @sub_sprites[i].mirror = (i == 1)
          @sub_sprites[i].x, @sub_sprites[i].y = 303 + i*18, 152
          @sub_sprites[i].z, @sub_sprites[i].oy = 600, 48-i*96}
      @degrees, @calc_oy = [90, -90], [48, -48]
    end
  end
  
  def update
    super
    case @mode
    when 0
      (0...3).each {|i|
          @sub_sprites[i].angle = (@sub_sprites[i].angle+6+i*6+rand(13)) % 360}
    when 1
      (0...2).each {|i|
          @sub_sprites[i].angle = (@sub_sprites[i].angle+6+i*6+rand(7)) % 360}
      self.angle = (self.angle - 3 - rand(7)) % 360
    when 2
      (0...2).each {|i|
          @degrees[i] = (@degrees[i] + 6 + rand(13)) % 360
          @sub_sprites[i].oy = 48 * (Math.sin(Math::PI*@degrees[i]/180))
          @calc_oy[i] = 48 * (Math.sin(Math::PI*@degrees[i]/180))}
    end
  end
  
  def hit
    result = 1000
    case @mode
    when 0
      result = 0
      results= [0, 0, 0]
      (0...3).each {|i|
          results[i] = (@sub_sprites[i].angle - @sub_sprites[(i+1)%3].angle).abs
          results[i] = 360 - results[i] if results[i] > 180
          result += results[i]}
      flag = true
      (0...3).each {|i|
          if results[i] <= 15
            flag = false
            break
          end}
      result = (500 + (flag ? 1500 : 1000) * (result - 45) / 135).to_i
    when 1
      result = 500
      results= [0, 0]
      (0...2).each {|i|
          results[i] = (@sub_sprites[i].angle - self.angle).abs
          results[i] = 360 - results[i] if results[i] > 180
          if results[i] <= 22.5
            results[i] = 0
          else
            results[i] = 750 * (results[i] - 22.5)/45
            results[i] = 750 if results[i] > 750
          end}
      result += (results[0] + results[1]).to_i
    when 2
      result = (@calc_oy[0] - @calc_oy[1]).abs
      if result <= 8
        result = 500
      elsif result <= 24
        result = (1000 + 500 * (result-24) / 16).to_i
      else
        result = (1000 + 1000 * (result-24) / 16).to_i
      end
    end
    return 500 if result < 500
    return 2000 if result > 2000
    return result
  end
  
  def dispose
    (0...3).each {|i| @sub_sprites[i].dispose}
    super
  end
  
end

#==============================================================================
# Window_UnityForce
#==============================================================================

class Window_UnityForce < Window_Skill

  def initialize
    super(nil, 0)
    @column_max = 1
    refresh
  end
  
  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    @data = []
    $game_party.ufs.each_index {|i|
        skill = $data_skills[$game_party.ufs[i]]
        @data.push(skill) if skill != nil && $game_party.uf_req(skill.id).size > 0}
    @item_max = @data.size
    if @item_max > 0
      self.contents = Bitmap.new(width - 32, row_max * 32)
      self.contents.font.name = $fontface
      self.contents.font.size = $fontsize
      self.contents.font.bold = true if $fontface == 'Papyrus'
      (0...@item_max).each {|i| draw_item(i)}
    end
  end
  
  def draw_item(index)
    skill = @data[index]
    x, y = 32, index*32
    if $game_party.uf_can_use?(skill.id)
      self.contents.font.color = normal_color
    else
      self.contents.font.color = disabled_color
    end
    sp_cost = skill.sp_cost 
    rect = Rect.new(x, y, (self.width - 32) / @column_max, 32)
    self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
    if self.contents.font.color == normal_color
      bitmap = RPG::Cache.icon(skill.icon_name)
    else
      bitmap = RPG::Cache.desaturated(skill.icon_name)
    end
    self.contents.blt(x, y + 4, bitmap, Rect.new(0, 0, 24, 24))
    self.contents.draw_text(x + 28, y, 492, 32, skill.name, 0)
    mem = $game_party.uf_req(skill.id)
    if mem.size > 1
      mem = "#{mem.min}-#{mem.max}"
    else
      mem = mem.shift.to_s
    end
    self.contents.draw_text(x + 280, y, 240, 32, "#{sp_cost}% (#{mem} members)", 2)
  end
  
  def update_help
    @help_window.set_text(self.skill.description, 1) if self.skill != nil
  end
  
  def update_cursor_rect
    if @index < 0
      self.cursor_rect.empty
      return
    end
    row = @index
    self.top_row = row if row < top_row
    self.top_row = row - (page_row_max - 1) if row > top_row + (page_row_max - 1)
    y = @index * 32 - self.oy
    self.cursor_rect.set(0, y, self.width - 32, 32)
  end
  
end

#==============================================================================
# Scene_Battle
#==============================================================================

class Scene_Battle
  
  def start_phase_uf
    @phase = 6
    @party_command_window.active = @party_command_window.visible = false
    @uf_window = Window_UnityForce.new
    @uf_window.help_window = @help_window
    @help_window.visible = true
  end

  def update_phase6
    @uf_window.update
    @uf_window.help_window = @help_window
    if Input.trigger?($controls.cancel)
      $game_system.se_play($data_system.cancel_se)
      @phase = 2
      @uf_window.dispose
      @uf_window = nil
      @help_window.visible = false
      @party_command_window.refresh
      @party_command_window.active = @party_command_window.visible = true
      @skill = nil
    elsif Input.trigger?($controls.confirm)
      @skill = @uf_window.skill
      if @skill == nil || !$game_party.uf_can_use?(@skill.id)
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      $game_system.se_play($data_system.decision_se)
      if $game_system.uf_mode
        @uf_window.visible = false
        @uf_window.active = false
        @help_window.set_text('Unity Force Overload', 1, Color.new(0, 255, 0))
        @phase = 7
        @trigger = UF_Trigger.new(@uf_overload)
      else
        $game_party.actors.each {|actor|
            actor.current_action.skill_id = @skill.id
            actor.current_action.kind = 4}
        @phase = 4
        $game_temp.battle_turn += 1
        $data_troops[@troop_id].pages.each_index {|index|
            page = $data_troops[@troop_id].pages[index]
            $game_temp.battle_event_flags[index] = false if page.span == 1}
        @actor_index = -1
        @uf_window.dispose
        @uf_window = nil
        $game_temp.battle_main_phase = true
        $game_troop.enemies.each {|enemy| enemy.make_action}
        make_action_orders
        @phase4_step = 1
      end
    end
  end
  
  def update_phase7
    if Input.trigger?($controls.cancel)
      $game_system.se_play($data_system.cancel_se)
      @phase = 6
      @uf_window.visible = @uf_window.active = true
      @trigger.dispose
      @trigger = nil
    elsif Input.trigger?($controls.confirm)
      $game_system.se_play($data_system.decision_se)
      $game_party.actors.each {|actor|
          actor.current_action.skill_id = @skill.id
          actor.current_action.kind = 4}
      @phase = 4
      $game_temp.battle_turn += 1
      $data_troops[@troop_id].pages.each_index {|index|
          page = $data_troops[@troop_id].pages[index]
          $game_temp.battle_event_flags[index] = false if page.span == 1}
      @actor_index = -1
      @uf_window.dispose
      @uf_window = nil
      @uf_cost_rate = @trigger.hit
      @wait_count = 40
      cost = 1000000/@uf_cost_rate
      text = "#{cost/10},#{cost%10}%"
      color = case cost
      when 1100..2000 then Color.new(0, 255, 0)
      when 950...1100 then Color.new(255, 255, 255)
      else
        Color.new(255, 0, 0)
      end
      @help_window.set_text(text, 1, color)
      $game_temp.battle_main_phase = true
      $game_troop.enemies.each {|enemy| enemy.make_action}
      make_action_orders
      @phase4_step = 1
      return
    end
    @trigger.update unless @trigger == nil
  end
  
  def make_uf_action_result
    if @active_battler.dead?
      @phase4_step = 1
      return
    end
    @skill = $data_skills[@active_battler.current_action.skill_id]
    unless @active_battler.current_action.forcing ||
        $game_party.uf_can_use?(@skill.id)
      @active_battler.current_action.fail = 5
      make_fail_action_result
      $game_temp.forcing_battler = nil
      @phase4_step = 1
      return
    end
    @uf_cost_rate = 1000 unless $game_system.uf_mode
    $game_party.actors.each {|actor|
        actor.sr -= (@skill.sp_cost * @uf_cost_rate / 100) unless actor.dead?}
    $game_party.clear_actions
    @status_window.refresh
    @help_window.set_text(@skill.name, 1)
    @animation1_id, @animation2_id = @skill.animation1_id, @skill.animation2_id
    @common_event_id = @skill.common_event_id
    set_target_battlers(@skill.scope)
    $game_temp.uf_override = true
    @target_battlers.each {|target| target.skill_effect(@active_battler, @skill)}
    $game_temp.uf_override = nil
  end
  
end