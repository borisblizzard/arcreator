#==============================================================================
# Sprite_Reflection
#==============================================================================

class Sprite_Reflection < Sprite_Character
  
  attr_accessor :character
  
  def initialize(viewport, character = nil)
    super(viewport, character)
    self.angle = 180
    self.mirror = true
    self.color = Color.new(255, 255, 255, 51)
    update
  end
  
  def update
    super
    self.x -= 1
    self.y -= 5 if !@character.mirror_offset
    self.z = @character.screen_z(@ch) - self.src_rect.height
    self.z = 0 if self.z < 0
  end
  
end

