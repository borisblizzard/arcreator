#==============================================================================
# Arrow_Actor
#==============================================================================

class Arrow_Actor < Arrow_Base
  
  def initialize(viewport)
    super(viewport)
    self.oy = @arrow.oy = 240
    self.z = 2000
    update(true)
  end
  
  def actor
    return $game_party.actors[@index]
  end
  
  def update(allow_change = false)
    super()
    if allow_change
      if Input.repeat?($controls.right)
        $game_system.se_play($data_system.cursor_se)
        @index += 1
        @index %= $game_party.actors.size
      elsif Input.repeat?($controls.left)
        $game_system.se_play($data_system.cursor_se)
        @index += $game_party.actors.size - 1
        @index %= $game_party.actors.size
      end
    end
    if self.actor != nil
      self.x = @arrow.x = case $game_party.actors.size
      when 1 then 240 + self.actor.screen_x
      when 2 then 2 * self.actor.screen_x
      when 3 then 80 + self.actor.screen_x
      when 4 then self.actor.screen_x
      end
      self.y = @arrow.y = self.actor.screen_y
    end
  end
  
  def update_help
    @help_window.set_actor(self.actor)
  end
  
end
