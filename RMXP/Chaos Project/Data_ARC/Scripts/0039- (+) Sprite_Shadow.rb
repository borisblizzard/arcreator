#==============================================================================
# Sprite_Shadow
#==============================================================================

class Sprite_Shadow < RPG::Sprite
  
  attr_accessor :character
  
  def initialize(viewport, character = nil)
    super(viewport)
    @character = character
    if !@character.is_a?(Game_Event) ||
        CP.first_comment(@character, 'shadow')
      self.bitmap = RPG::Cache.character('bottom_shadow', 0)
    elsif CP.first_comment(@character, 'bigshadow')
      self.bitmap = RPG::Cache.character('big_shadow', 0)
    elsif CP.first_comment(@character, 'hugeshadow')
      self.bitmap = RPG::Cache.character('huge_shadow', 0)
    end
    self.ox, self.oy = 16, 10
    update
  end
  
  def update
    super
    self.visible = !@character.transparent
    sx = @character.pattern % 2 * 32
    sy = (@character.direction - 2) * 5
    self.src_rect.set(sx, sy, 32, 10)
    self.x = @character.screen_x
    self.y = @character.screen_y
    self.z = @character.screen_z(self.bitmap.height / 4) - 1
    self.z = 0 if self.z < 1
    self.opacity = @character.opacity
    self.blend_type = @character.blend_type
    self.bush_depth = @character.bush_depth
  end
  
end
