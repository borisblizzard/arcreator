#==============================================================================
# module KGC
#==============================================================================

module KGC
  $game_special_elements = {}
  $imported = {}
  $data_states = load_data('Data/States.rxdata')
  $data_system = load_data('Data/System.rxdata')
  BC_SPEED_INIT = 24
end

$imported['BattleCamera'] = true
$imported['Base Reinforce'] = true

#==============================================================================
# Game_Enemy
#==============================================================================

class Game_Enemy < Game_Battler
  
  attr_reader :origin_x, :origin_y
  
  alias initialize_KGC_BattleCamera initialize
  def initialize(troop_id, member_index)
    initialize_KGC_BattleCamera(troop_id, member_index)
    @origin_x = $data_troops[@troop_id].members[@member_index].x
    @origin_y = $data_troops[@troop_id].members[@member_index].y
  end
  
  def screen_x
    return @origin_x - $scene.camera.x * self.zoom
  end
  
  def screen_y
    return @origin_y - $scene.camera.y * self.zoom
  end
  
  def zoom
    if $game_variables[25] == 0
      n = (1.00 + $scene.camera.z / 512.00) * ((@origin_y - 304) / 256.00 + 1)
    else
      n = 1
    end
    return n
  end
  
end

#==============================================================================
# Sprite_Battler
#==============================================================================

class Sprite_Battler < RPG::Sprite
  
  alias update_KGC_BattleCamera update
  def update
    update_KGC_BattleCamera
    return if @battler == nil
    if $game_variables[25] == 0 && @battler.is_a?(Game_Enemy) && !@nocam
      self.zoom_x = self.zoom_y = @battler.zoom
    end
  end
  
end

#==============================================================================
# Spriteset_Battle
#==============================================================================

class Spriteset_Battle
  
  alias update_KGC_BattleCamera update
  def update
    update_KGC_BattleCamera
    return if $game_variables[25] > 0
    cx, cy, cz = $scene.camera.x, $scene.camera.y, $scene.camera.z
    bx, by = @battleback_sprite.x + 320, @battleback_sprite.y + 304
    if bx != cx || by != cy || @bz != cz
      zoom = cz / 512.00 + 1
      @battleback_sprite.zoom_x = zoom * 1.5
      @battleback_sprite.zoom_y = zoom * 1.5
      if $imported['Base Reinforce']
        @battleback_sprite.ox = @battleback_sprite.bitmap.width * 0.52
        @battleback_sprite.oy = @battleback_sprite.bitmap.height / 2 
        mag_x = 600.0 / @battleback_sprite.bitmap.width
        mag_y = 300.0 / @battleback_sprite.bitmap.height
        @battleback_sprite.zoom_x *= mag_x
        @battleback_sprite.zoom_y *= mag_y
      end
      @battleback_sprite.x = -cx * zoom / 2 - 320 + @battleback_sprite.ox * 2
      @battleback_sprite.y = -cy * zoom / 2 - 144 + @battleback_sprite.oy * 2
      @bz = cz
    end
  end
  
end

#==============================================================================
# Camera
#==============================================================================

class Camera
  
  attr_reader :x, :y, :z
  attr_accessor :move_speed
  
  def initialize
    @x, @y, @z = 0, 0, 0
    @move_x = @move_y = @move_z = 0
    @move_speed = KGC::BC_SPEED_INIT
  end
  
  def move(x, y, z)
    @move_x, @move_y, @move_z = x - @x - 320, y - @y - 160, z - @z
  end
  
  def move_target(target)
    return if !target.is_a?(Game_Enemy) || $game_variables[25] > 0
    tx, ty = target.origin_x, target.origin_y - 144
    tz = (304 - target.origin_y) * 5
    move(tx, ty, tz)
  end
  
  def centering
    @move_x, @move_y, @move_z = -@x, -@y, -@z
  end
  
  def update
    return if $game_variables[25] > 0
    mv = @move_x.abs * @move_speed / 160
    if mv > @move_speed
      mv = @move_speed
    elsif mv < 1
      mv = 1
    end
    if @move_x > 0
      @x += mv
      @move_x -= mv
      @move_x = 0 if @move_x < 0
    elsif @move_x < 0
      @x -= mv
      @move_x += mv
      @move_x = 0 if @move_x > 0
    end
    mv = @move_y.abs * @move_speed / 160
    if mv > @move_speed
      mv = @move_speed
    elsif mv < 1
      mv = 1
    end
    if @move_y > 0
      @y += mv
      @move_y -= mv
      @move_y = 0 if @move_y < 0
    elsif @move_y < 0
      @y -= mv
      @move_y += mv
      @move_y = 0 if @move_y > 0
    end
    mv = @move_z.abs * @move_speed / 96
    if mv < 1
      mv = 1
    else
      speed = @move_speed * 2
      mv = speed if mv > speed
    end
    if @move_z > 0
      @z += mv
      @move_z = [@move_z - mv, 0].max
    elsif @move_z < 0
      @z -= mv
      @move_z = [@move_z + mv, 0].min
    end
  end
  
end

#==============================================================================
# Scene_Battle
#==============================================================================

class Scene_Battle
  
  attr_reader :camera
  
  alias main_KGC_BattleCamera main
  def main
    @camera = Camera.new
    main_KGC_BattleCamera
  end
  
  alias update_KGC_BattleCamera update
  def update
    @camera.update
    update_KGC_BattleCamera
  end
  
  alias update_phase4_step3_KGC_BattleCamera update_phase4_step3
  def update_phase4_step3
    if $game_variables[25] == 0
      if @active_battler.is_a?(Game_Actor) && @target_battlers.size > 0
        if @target_battlers.size > 1 || @skill != nil && (@skill.scope == 2 ||
            @skill.scope == 4 || @skill.scope == 6 || @skill.scope == 8 ||
            @skill.scope == 9 || @skill.scope == 10) || @item != nil &&
            (@item.scope == 2 || @item.scope == 4 || @item.scope == 6 ||
            @item.scope == 8 || @item.scope == 9 || @item.scope == 10)
          @camera.move(320, 160, -96)
        else
          @camera.move_target(@target_battlers[0])
        end
      elsif @active_battler.is_a?(Game_Enemy)
        if (@skill == nil || @skill.id != 284) &&
            (@active_battler.current_action.kind != 0 ||
            @active_battler.current_action.kind == 0 &&
            @active_battler.current_action.basic <= 1)
          @camera.move_target(@active_battler)
        end
      end
    end
    update_phase4_step3_KGC_BattleCamera
  end 
  
  alias update_phase4_step6_KGC_BattleCamera update_phase4_step6
  def update_phase4_step6
    @camera.centering
    update_phase4_step6_KGC_BattleCamera
  end
  
  alias update_phase3_enemy_select_KGC_BattleCamera update_phase3_enemy_select
  def update_phase3_enemy_select
    if @active_battler.current_action.kind != 0 && (@skill != nil &&
        (@skill.scope == 2 || @skill.scope == 4 || @skill.scope == 6 ||
        @skill.scope == 8 || @skill.scope == 9 || @skill.scope == 10) ||
        @item != nil && (@item.scope == 2 || @item.scope == 4 ||
        @item.scope == 6 || @item.scope == 8 || @item.scope == 9 ||
        @item.scope == 10))
      @camera.move(320, 160, -96)
    else
      @camera.move_target($game_troop.enemies[@enemy_arrows[0].index])
    end
    update_phase3_enemy_select_KGC_BattleCamera
  end
  
  alias end_enemy_select_KGC_BattleCamera end_enemy_select
  def end_enemy_select
    @camera.centering
    end_enemy_select_KGC_BattleCamera
  end

end
