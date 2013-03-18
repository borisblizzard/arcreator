#==============================================================================
# Sprite_Picture
#==============================================================================

class Sprite_Picture < Sprite
  
  def initialize(viewport, picture)
    super(viewport)
    @picture = picture
    update
  end
  
  def dispose
    self.bitmap.dispose if self.bitmap != nil
    super
  end
  
  def update
    super
    if @picture_name != @picture.name
      @picture_name = @picture.name
      self.bitmap = RPG::Cache.picture(@picture_name) if @picture_name != ''
    end
    if @picture_name == ''
      self.visible = false
      return
    end
    self.visible = true
    if @picture.origin == 0
      self.ox = self.oy = 0
    else
      self.ox = self.bitmap.width / 2
      self.oy = self.bitmap.height / 2
    end
    self.x, self.y, self.z = @picture.x, @picture.y, @picture.number
    self.zoom_x, self.zoom_y = @picture.zoom_x / 100.0, @picture.zoom_y / 100.0
    self.opacity, self.blend_type = @picture.opacity, @picture.blend_type
    self.angle, self.tone = @picture.angle, @picture.tone
  end
  
end
