#==============================================================================
# Sprite_Character
#==============================================================================

class Sprite_Sight < RPG::Sprite
  
  attr_accessor :character
  
  def initialize(viewport, character)
    super(viewport)
    self.bitmap = RPG::Cache.picture('sight_area')
    self.ox = self.bitmap.width/2
    @character = character
    update
  end
  
  def update
    super
    sy = (8 - (Graphics.frame_count % 16)).abs * 145
    new_mirror = (((Graphics.frame_count + 8) / 16) % 2 == 0)
    self.mirror = new_mirror if self.mirror != new_mirror
    new_angle = case @character.direction
    when 2 then 0
    when 4 then 270
    when 6 then 90
    when 8 then 180
    end
    self.angle = new_angle if self.angle != new_angle
    self.src_rect.set(0, sy, self.bitmap.width, self.bitmap.height / 9)
    self.x = @character.screen_x
    self.y = @character.screen_y - 16
    self.z = 2000
    self.opacity = @character.opacity
    self.blend_type = @character.blend_type
    self.bush_depth = @character.bush_depth
  end
  
end
