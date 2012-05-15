QUANTIZER = 32
ITREMBLE = 10
XTREMBLE = 16
DISASSEMBLE = 10
PIXEL_SIZE = 4

#==============================================================================
# RPG::Sprite
#==============================================================================

class RPG::Sprite
  
  attr_accessor :nocam
  
  def appear
    self.blend_type = self.opacity = 0
    @_appear_duration = 16
    @_whiten_duration = @_escape_duration = @_collapse_duration = 0
  end
  
  def escape
    self.blend_type, self.opacity = 0, 255
    @_escape_duration = 32
    @_whiten_duration = @_appear_duration = @_collapse_duration = 0
  end
  
  def collapse
    return if $data_enemies[@battler.id].element_ranks[CP::Cache::DNone] != 3
    self.bitmap = self.bitmap.clone
    if @battler.is_a?(Game_Enemy) && @battler.boss && !@battler.superboss
      self.opacity = 255
      begin
        invert while @pos[0] < @w_ && @pos[1] < @h_
        @destructor = @inversion
      rescue
        p 'CPError: Inverted graphic file could not be created.'
        @destructor = Bitmap.new(1, 1)
      end
      @factor, @lines = (self.bitmap.height > 240 ? 2 : 1), []
      @_collapse_duration = self.bitmap.height / @factor + 48
    elsif @battler.is_a?(Game_Enemy) && @battler.superboss
      detect_pixels while @pos[0] < @w_ && @pos[1] < @h_
      @particles = []
      self.opacity, @_collapse_duration = 255, 0xFFFF
    else
      self.opacity, @_collapse_duration = 255, 48
      if @battler.is_a?(Game_Actor) ||
          $data_enemies[@battler.id].element_ranks[CP::Cache::DMachine] == 3 &&
          $data_enemies[@battler.id].element_ranks[CP::Cache::DExplode] == 3
        self.blend_type = 1
      end
    end
    @_whiten_duration = @_appear_duration = @_escape_duration = 0
  end
  
  def collapse_boss
    if @destructor != nil
      tmp = [(0...self.bitmap.height).to_a - @lines, []]
      number = tmp[0].size
      number = @factor if number > @factor
      number.times {
          t = tmp[0][rand(tmp[0].size)]
          tmp[1].push(t)
          tmp[0].delete(t)}
      c = Color.new(0, 0, 0, 0)
      tmp[1].each {|y|
          rect = Rect.new(0, y, self.bitmap.width, 1)
          self.bitmap.fill_rect(rect, c)
          self.bitmap.blt(0, y, @destructor, rect)}
      @lines += tmp[1]
    end
    if self.ox == self.bitmap.width/2
      if @_collapse_duration % 4 == 0
        ex = self.bitmap.width/QUANTIZER
        exl = ITREMBLE/2
        exu = XTREMBLE/2
        if ex < exl
          self.ox += exl
        elsif ex > exu
          self.ox += exu
        else
          self.ox += ex
        end
      elsif @_collapse_duration % 4 == 2
        ex = self.bitmap.width/QUANTIZER
        exl = ITREMBLE/2
        exu = XTREMBLE/2
        if ex < exl
          self.ox -= exl
        elsif ex > exu
          self.ox -= exu
        else
          self.ox -= ex
        end
      end
    elsif @_collapse_duration % 4 == 0
      if @_collapse_duration == 0
        ex = self.bitmap.width/QUANTIZER
        exl = ITREMBLE/2
        exu = XTREMBLE/2
      else
        ex = self.bitmap.width*2/QUANTIZER
        exl = ITREMBLE
        exu = XTREMBLE
      end
      if ex < exl
        self.ox += exl
      elsif ex > exu
        self.ox += exu
      else
        self.ox += ex
      end
    elsif @_collapse_duration % 4 == 2
      ex = self.bitmap.width*2/QUANTIZER
      exl = ITREMBLE
      exu = XTREMBLE
      if ex < exl
        self.ox -= exl
      elsif ex > exu
        self.ox -= exu
      else
        self.ox -= ex
      end
    end
  end
  
  def collapse_superboss
    coos = []
    (DISASSEMBLE / 2 + rand(DISASSEMBLE + 1)).times {
        break if @pixels.size == 0
        i = rand(@pixels.size)
        coos.push(@pixels[i])
        @pixels.delete_at(i)}
    c = Color.new(0, 0, 0, 0)
    coos.each {|coo|
        particle = Sprite.new
        particle.bitmap = Bitmap.new(PIXEL_SIZE, PIXEL_SIZE)
        particle.bitmap.blt(0, 0, self.bitmap,
            Rect.new(coo[0], coo[1], PIXEL_SIZE, PIXEL_SIZE))
        particle.ox = particle.oy = PIXEL_SIZE / 2
        particle.x = self.x - self.ox + coo[0] + PIXEL_SIZE / 2
        particle.y = self.y - self.oy + coo[1] + PIXEL_SIZE / 2
        @particles.push(particle)
        self.bitmap.fill_rect(coo[0], coo[1], PIXEL_SIZE, PIXEL_SIZE, c)}
    @particles.each_index {|i|
        @particles[i].opacity -= 4
        @particles[i].y -= 2
        @particles[i].angle += 15
        if @particles[i].opacity == 0 ||
            @particles[i].y - @particles[i].oy + PIXEL_SIZE < 0
          @particles[i].dispose
          @particles[i] = nil
        end}
    @particles.compact!
    @_collapse_duration = 0 if @particles.size == 0
  end
  
  def slicer
    return if self.bitmap == nil
    if @slicer == nil
      @slicer = [self.bitmap.clone, self.bitmap.clone]
      @w_ = self.bitmap.width
      @h_ = self.bitmap.height
      if @w_ > @h_
        @s_ = @h_*3/5 - @w_/4
        @e_ = @h_*3/5 + @w_/4
      else
        @s_ = @h_*3/5 - @w_/2
        @e_ = @h_*3/5 + @w_/2
      end
      @slicer[0].fill_rect(0, 0, @w_, @s_, Color.new(0, 0, 0, 0))
      @slicer[1].fill_rect(0, @e_, @w_, @h_-@e_, Color.new(0, 0, 0, 0))
      @pos = [0, @s_]
    elsif @pos[0] < @w_ && @pos[1] < @e_
      @slicer[0].fill_rect(@pos[0], @pos[1], @w_-@pos[0], 1, Color.new(0, 0, 0, 0))
      @slicer[1].fill_rect(0, @pos[1], @pos[0], 1, Color.new(0, 0, 0, 0))
      @pos[0] += (@w_ > @h_ ? 2 : 1)
      @pos[1] += 1
    end
  end
  
  def invert
    return if self.bitmap == nil
    if @inversion == nil
      if @battler.is_a?(Game_Enemy) && @battler.id == 111
        @inversion = RPG::Cache.battler('evaniel', 0).clone
      else
        @inversion = self.bitmap.clone
      end
      @pos = [0, 0]
      @w_ = self.bitmap.width
      @h_ = self.bitmap.height
    else
      c = 0
      while @pos[0] < @w_ && @pos[1] < @h_ && c < 100
        @inversion.invert_pixel(@pos[0], @pos[1])
        @pos[0] = (@pos[0]+1) % @w_
        @pos[1] += 1 if @pos[0] == 0
        c += 1
      end
    end
  end
  
  def detect_pixels
    return if self.bitmap == nil
    if @pixels == nil
      @pos = [0, 0]
      @pixels = []
      @w_ = self.bitmap.width
      @h_ = self.bitmap.height
    else
      c = 0
      f = PIXEL_SIZE ** 2
      while @pos[0] < @w_ && @pos[1] < @h_ && c < 200 / f
        alpha = false
        (0...PIXEL_SIZE).each {|j| (0...PIXEL_SIZE).each {|i|
            x, y = @pos[0] + i, @pos[1] + j
            next if x >= @w_ || y >= @h_
            color = self.bitmap.get_pixel(x, y)
            if color.alpha > 0
              alpha = true
              break
            end}}
        @pixels.push([@pos[0], @pos[1]]) if alpha
        @pos[0] = (@pos[0] + PIXEL_SIZE) % @w_
        @pos[1] += PIXEL_SIZE if @pos[0] == 0
        c += 1
      end
    end
  end
  
  def update
    super
    if @battler.is_a?(Game_Enemy) &&
        $data_enemies[@battler.id].element_ranks[CP::Cache::DNone] == 3
      if @battler.boss && !@battler.superboss
        invert
      elsif @battler.superboss
        detect_pixels
      elsif $data_enemies[@battler.id].element_ranks[CP::Cache::DSlicer] != 3
        slicer
      end
    end
    if @_whiten_duration > 0
      @_whiten_duration -= 1
      self.color.alpha = 128 - (16 - @_whiten_duration) * 10
    end
    if @_appear_duration > 0
      @_appear_duration -= 1
      self.opacity = (16 - @_appear_duration) * 16
    end
    if @_escape_duration > 0
      @_escape_duration -= 1
      self.opacity = 255 - (32 - @_escape_duration) * 10
    end
    if @_collapse_duration > 0
      @_collapse_duration -= 1
      if @battler.is_a?(Game_Enemy)
        if @battler.boss && !@battler.superboss
          collapse_boss
        elsif @battler.superboss
          collapse_superboss
        elsif CP::Cache::DeathAnimations.any? {|id|
            $data_enemies[@battler.id].element_ranks[id] != 3}
          if $data_enemies[@battler.id].element_ranks[CP::Cache::DGhost] != 3
            @nocam = [self.zoom_x, self.zoom_y] unless @nocam
            self.zoom_x = (@_collapse_duration / 48.0) * @nocam[0]
            self.zoom_y = (1.5 - @_collapse_duration / 96.0) * @nocam[1]
          elsif $data_enemies[@battler.id].element_ranks[CP::Cache::DFallROTL] != 3
            @nocam = [self.x, self.y] unless @nocam
            self.angle += 1
            self.x += 2
            self.y += 1
          elsif $data_enemies[@battler.id].element_ranks[CP::Cache::DSplat] != 3
            @nocam = [self.zoom_x, self.zoom_y] unless @nocam
            if zoom_y / @nocam[0] > 0.4
              self.zoom_y = (@_collapse_duration / 10.0 - 3.8) * @nocam[0]
              self.y -= 4
            end
          elsif $data_enemies[@battler.id].element_ranks[CP::Cache::DSlicer] != 3
            if @destructor == nil
              @destructor = RPG::Sprite.new
              slicer while @pos[0] < @w_ && @pos[1] < @e_
              self.bitmap, @destructor.bitmap = @slicer
              @destructor.x = self.x
              @destructor.y = self.y
              @destructor.z = self.z
              @destructor.ox = self.ox
              @destructor.oy = self.oy
              @destructor.zoom_x = self.zoom_x
              @destructor.zoom_y = self.zoom_y
              @destructor.nocam = @nocam = true
              @destructor.collapse
            else
              @destructor.x += (@w_ > @h_ ? 2 : 1)
              @destructor.y += 1
              @destructor.update
            end
          elsif $data_enemies[@battler.id].element_ranks[CP::Cache::DMachine] != 3
            if @_collapse_duration == 47
              animation($data_animations[97], true)
            elsif @_collapse_duration == 30
              self.blend_type = 1
              animation($data_animations[98], true)
            end
          elsif $data_enemies[@battler.id].element_ranks[CP::Cache::DExplode] != 3 &&
              @_collapse_duration == 47
            animation($data_animations[209], true)
          end
        end
      end
      if $data_enemies[@battler.id].element_ranks[CP::Cache::DMachine] == 3
        self.opacity = 255 - (48 - @_collapse_duration) * 6
      elsif @_collapse_duration <= 24
        self.opacity = 255 - (24 - @_collapse_duration) * 12
      end
    elsif @destructor != nil
      @destructor.dispose
      @destructor == nil
    end
    if @_damage_duration > 0
      @_damage_sprite.update
      @_damage_duration == 1 ? dispose_damage : (@_damage_duration -= 1)
    end
    if @_animation != nil && (Graphics.frame_count % 2 == 0)
      @_animation_duration -= 1
      update_animation
      @@_animations.clear if @_animation_duration == 0
    end
    if @_loop_animation != nil && (Graphics.frame_count % 2 == 0)
      update_loop_animation
      @_loop_animation_index += 1
      @_loop_animation_index %= @_loop_animation.frame_max
    end
    if @_blink
      @_blink_count = (@_blink_count + 1) % 32
      alpha = (@_blink_count < 16 ? (16-@_blink_count) : (@_blink_count-16)) * 6
      self.color.set(255, 255, 255, alpha)
    end
  end
  
  alias dispose_destructor_later dispose
  def dispose
    if @particles != nil
      @particles.each_index {|i|
          @particles[i].dispose
          @particles[i] = nil}
      @particles.compact!
    end
    if @destructor != nil && !@destructor.disposed?
      @destructor.dispose
      @destructor == nil
    end
    if @inversion != nil && !@inversion.disposed?
      @inversion.dispose
      @inversion == nil
    end
    dispose_destructor_later
  end
    
end

#===============================================================================
# Game_Battler
#===============================================================================

class Game_Battler 
  
  attr_accessor :restorative
  attr_accessor :restorative_mp
  attr_accessor :mp_flag
  
  alias game_battler_initialize initialize 
  def initialize 
    game_battler_initialize 
    @restorative, @restorative_mp, @mp_flag = false, false, 0
  end

end 

#==============================================================================
# Scene_Battle
#==============================================================================

class Scene_Battle
  
  def phase3_setup_command_window
    @party_command_window.active = @party_command_window.visible = false
    @actor_command_window.index = 0
    @actor_command_window.active = @actor_command_window.visible = true
    @actor_command_window.actor = @active_battler
    @actor_command_window.x = case $game_party.actors.size
    when 1 then 320
    when 2 then 160 + @actor_index * 320
    when 3 then 160 + @actor_index * 160
    when 4 then 80 + @actor_index * 160
    end
    if @rage_command_window != nil
      @rage_command_window.update_actor(@active_battler)
      @rage_command_window.x = case $game_party.actors.size
      when 1 then 320
      when 2 then 160 + @actor_index * 320
      when 3 then 160 + @actor_index * 160
      when 4 then 80 + @actor_index * 160
      end
    end
    @ability_command_windows.each {|win| win.reset}
    @actor_command_window.setup_command_name
  end

  def update_phase4_step1
    @help_window.visible = false
    return if judge
    if $game_temp.forcing_battler == nil
      setup_battle_event
      return if $game_system.battle_interpreter.running?
    end
    if $game_temp.forcing_battler != nil
      @action_battlers.delete($game_temp.forcing_battler)
      @action_battlers.unshift($game_temp.forcing_battler)
    end
    if @action_battlers.size == 0
      start_phase2
      return
    end
    @animation1_id = @animation2_id = @common_event_id = 0
    @active_battler = @action_battlers.shift
    return if @active_battler.index == nil
    @phase4_step = 2
    if @active_battler.hp > 0 && @active_battler.can_slip_damage
      if @active_battler.regen? && !@active_battler.slip_damage?
        @active_battler.regen_effect
        @active_battler.damage_pop = true
        @status_window.refresh
      elsif !@active_battler.regen? && @active_battler.slip_damage?
        @active_battler.slip_damage_effect
        @active_battler.damage_pop = true
        @status_window.refresh
      elsif @active_battler.regen? && @active_battler.slip_damage?
        @active_battler.regen_slip_damage_effect
        @active_battler.damage_pop = true
        @status_window.refresh
      end
      if @active_battler.dead?
        @phase4_step = 6
        if @active_battler.states.include?(32)
          @action_battlers.unshift(@active_battler)
          #@phase4_step = 1
        end
      end
    end
    @status_window.refresh
  end

end
