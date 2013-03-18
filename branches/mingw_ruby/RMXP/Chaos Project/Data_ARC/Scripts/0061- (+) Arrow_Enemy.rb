#==============================================================================
# Arrow_Enemy
#==============================================================================

class Arrow_Enemy < Arrow_Base
  
  def initialize(viewport)
    super(viewport)
    self.oy = @arrow.oy = 192
    update(true)
  end
  
  def enemy
    return $game_troop.enemies[@index]
  end
  
  def update(allow_change = false)
    super()
    if allow_change
      $game_troop.enemies.size.times do
        break if self.enemy.exist?
        @index += 1
        @index %= $game_troop.enemies.size
      end
      if Input.repeat?($controls.right)
        $game_system.se_play($data_system.cursor_se)
        $game_troop.enemies.size.times do
          @index += 1
          @index %= $game_troop.enemies.size
          break if self.enemy.exist?
        end
      elsif Input.repeat?($controls.left)
        $game_system.se_play($data_system.cursor_se)
        $game_troop.enemies.size.times do
          @index += $game_troop.enemies.size - 1
          @index %= $game_troop.enemies.size
          break if self.enemy.exist?
        end
      end
    end
    if self.enemy != nil
      self.x = @arrow.x = self.enemy.screen_x
      self.y = @arrow.y = self.enemy.screen_y
    end
  end
  
  def update_help
    @help_window.set_enemy(self.enemy)
  end
  
end
