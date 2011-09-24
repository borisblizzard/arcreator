#==============================================================================
# Sprite_Battler
#==============================================================================

class Sprite_Battler < RPG::Sprite
  
  attr_accessor :battler
  
  def initialize(viewport, battler = nil)
    super(viewport)
    @battler = battler
    @battler_visible = false
    if @battler != nil && @battler.disappear == true
      self.opacity = 0
      @battler.hide_battler
      @battler.disappear = nil
    end
  end
  
  def update
    super
    if @battler == nil
      self.bitmap = nil
      loop_animation(nil)
      return
    end
    update_trance if @battler == $game_actors[CP::Cache::Sydon]
    update_appearance
    if @battler.battler_name != @battler_name ||
        @battler.battler_hue != @battler_hue
      @battler_name = @battler.battler_name
      @battler_hue = @battler.battler_hue
      self.bitmap = RPG::Cache.battler(@battler_name, @battler_hue)
      @width = bitmap.width
      @height = bitmap.height
      self.ox = @width / 2
      self.oy = @height
      self.opacity = 0 if @battler.id != 111 && (@battler.dead? || @battler.hidden)
    end
    if @battler.damage == nil &&
        @battler.state_animation_id != @state_animation_id
      @state_animation_id = @battler.state_animation_id
      loop_animation($data_animations[@state_animation_id])
    end
    @battler.blink ? blink_on : blink_off
    if !@battler_visible && !@battler.hidden && !@battler.dead? &&
        (@battler.damage == nil || @battler.damage_pop)
      appear
      @battler_visible = true
    end
    if @battler_visible
      if @battler.hidden
        $game_system.se_play($data_system.escape_se)
        escape
        @battler_visible = false
      end
      if @battler.white_flash
        whiten
        @battler.white_flash = false
      end
      if @battler.animation_id != 0
        animation = $data_animations[@battler.animation_id]
        animation(animation, @battler.animation_hit)
      end
      if @battler.damage_pop
        damage(@battler.damage, @battler.critical, @battler.restorative,
            @battler.restorative_mp)
        @battler.damage = nil
        @battler.critical = @battler.damage_pop = @battler.restorative =
            @battler.restorative_mp = false
      end
      if @battler.damage == nil && @battler.dead?
        collapse
        if @battler.is_a?(Game_Enemy)
          se = $data_system.enemy_collapse_se.clone
          if @battler.boss &&
              $data_enemies[@battler.id].element_ranks[CP::Cache::DNone] == 3
            se = RPG::AudioFile.new('BossDead', 100, 100)
            if $data_enemies[@battler.id].element_ranks[CP::Cache::DFinal] != 3
              se = $data_system.actor_collapse_se
            end
          elsif $data_enemies[@battler.id].element_ranks[CP::Cache::DMachine] != 3 ||
              $data_enemies[@battler.id].element_ranks[CP::Cache::DNone] != 3 ||
              $data_enemies[@battler.id].element_ranks[CP::Cache::DExplode] != 3
            se.name = ''
          end
          $game_system.se_play(se)
        else
          $game_system.se_play($data_system.actor_collapse_se)
        end
        @battler_visible = false
      end
    end
    @battler.animation_id = 0
    if battler.is_a?(Game_Actor)
      self.x = case $game_party.actors.size
      when 1 then @battler.screen_x + 240
      when 2 then @battler.screen_x + 80 + @battler.index * 160
      when 3 then @battler.screen_x + 80
      when 4 then @battler.screen_x
      end
    elsif battler.is_a?(Game_Enemy)
      self.x = @battler.screen_x unless @nocam
    end
    self.y = @battler.screen_y unless @nocam
    self.z = @battler.screen_z
  end
  
  def update_trance
    if $game_temp.trance != nil && !@battler.dead?
      self.opacity -= 16 if self.effect? || $game_temp.trance == false
      $game_temp.trance, @battler_visible = nil, false if self.opacity == 0
    end
  end
  
  def update_appearance
    if @battler.disappear == true
      self.opacity -= 16
      if self.opacity == 0
        @battler.hide_battler
        self.opacity, @battler.disappear = 255, nil
      end
    elsif @battler.disappear == false
      if self.opacity == 255
        self.opacity = 0
        @battler.return_battler
      end
      self.opacity += 16
      @battler.disappear = nil if self.opacity == 255
    end
  end
  
end
