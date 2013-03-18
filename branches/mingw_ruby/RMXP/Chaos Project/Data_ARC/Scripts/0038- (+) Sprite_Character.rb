#==============================================================================
# Sprite_Character
#==============================================================================

class Sprite_Character < RPG::Sprite
  
  attr_accessor :character
  
  def initialize(viewport, character = nil)
    @character = character
    super(viewport)
    update
  end
  
  def update
    super
    if @tile_id != @character.tile_id ||
       @character_name != @character.character_name ||
       @character_hue != @character.character_hue
      @tile_id = @character.tile_id
      @character_name = @character.character_name
      @character_hue = @character.character_hue
      if @tile_id >= 384
        self.bitmap = RPG::Cache.tile($game_map.tileset_name,
          @tile_id, @character.character_hue)
        self.src_rect.set(0, 0, 32, 32)
        self.ox, self.oy = 16, 32
      else
        self.bitmap = RPG::Cache.character(@character.character_name,
          @character.character_hue)
        @cw, @ch = bitmap.width / 4, bitmap.height / 4
        self.ox, self.oy = @cw / 2, @ch
      end
    end
    self.visible = (!@character.transparent)
    if @tile_id == 0
      sx = @character.pattern * @cw
      sy = (@character.direction - 2) / 2 * @ch
      self.src_rect.set(sx, sy, @cw, @ch)
    end
    self.x = @character.screen_x
    self.y = @character.screen_y
    self.z = @character.screen_z(@ch)
    self.opacity = @character.opacity
    self.blend_type = @character.blend_type
    self.bush_depth = @character.bush_depth
    if @character.loop_id != 0 && @character.loop_id != nil
      loop_animation($data_animations[@character.loop_id])
    else
      loop_animation(nil)
    end
    if @character.animation_id != 0
      animation = $data_animations[@character.animation_id]
      animation(animation, true)
      @character.animation_id = 0
    end
  end
  
end
