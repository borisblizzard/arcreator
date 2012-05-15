#==============================================================================
# DamageSprite
#==============================================================================

class DamageSprite
  
  attr_reader :bitmap
  attr_reader :duration
  
  MOVES = [-12, -12, -6, -3, -2, -1, 1, 2, 3, 6, 12, 12]
  
  def initialize(x, y)
    @x, @y = x - 2, y
    @max_duration = @duration = 1
    @sprites = []
    @width = 0
    @bitmap = Bitmap.new(1, 1)
  end
  
  def create_sprites(damage, color = Color.new(255, 255, 255))
    damage.scan(/./).each {|c|
        if c == ' '
          @width += 8
          @sprites.push(nil)
        else
          sprite = Sprite.new
          sprite.bitmap = CP::Cache.damages[color]
          sprite.src_rect = CP::Cache::DAMAGES[c]
          sprite.x, sprite.y, sprite.z = @x, @y, 3000
          sprite.ox, sprite.oy = sprite.src_rect.width / 2, 20
          sprite.visible = false
          @sprites.push(sprite)
          @width += sprite.src_rect.width - 2
        end}
  end
  
  def finalize
    x = @x - @width / 2
    @sprites.each {|s|
        if s != nil
          s.x = x + s.ox - 1
          x += s.src_rect.width - 2
        else
          x += 8
        end}
    @sprites.compact!
    @max_duration = 50 + @sprites.size * 2
    @duration = @max_duration
  end
  
  def update
    if @duration + @sprites.size * 2 >= 36
      @sprites.each_index {|i|
          move = @max_duration - @duration - i * 2
          if move >= 0 && move < MOVES.size
            @sprites[i].visible = true if move == 0
            @sprites[i].y += MOVES[move]
          end}
    end
    if @duration - @sprites.size < 12
      @sprites.each_index {|i|
          move = @duration - @sprites.size + i
          if move < 12
            @sprites[i].opacity -= 21
            @sprites[i].y -= MOVES[move] * 2 / 3
            @sprites[i].angle += 12
          end}
    end
    @duration -= 1
  end
  
  def dispose
    @sprites.each {|s| s.dispose}
  end
  
end
  
#==============================================================================
# RPG::Sprite
#==============================================================================

class RPG::Sprite
  
  attr_accessor :nocam
  
  def damage(damage, critical, restorative, restorative_mp)
    dispose_damage
    damage_string = (damage.is_a?(Numeric) ? damage.abs : damage).to_s
    if damage.is_a?(Numeric) && damage < 0 || damage == 'Full!' || restorative
      color = CP::Cache::ColorHP
    elsif restorative_mp
      color = CP::Cache::ColorMP
    elsif critical
      color = CP::Cache::ColorCritical
    elsif [0, 'Missed', 'Immune', 'Failed'].include?(damage)
      color = CP::Cache::ColorMissed
    else
      color = CP::Cache::ColorDamage
    end
    @_damage_sprite = DamageSprite.new(self.x, self.y - self.oy / 3)
    @_damage_sprite.create_sprites(damage_string, color)
    @_damage_sprite.finalize
    @_damage_duration = @_damage_sprite.duration
  end
  
  def damage?
    return (@_damage_sprite != nil)
  end
  
end
