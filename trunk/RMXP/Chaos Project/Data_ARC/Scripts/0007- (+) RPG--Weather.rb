#==============================================================================
# RPG::Weather
#==============================================================================

class RPG::Weather
  
  attr_reader :type
  attr_reader :max
  attr_reader :ox
  attr_reader :oy

  def initialize(viewport = nil)
    @viewport = viewport
    @type = @max = @ox = @oy = 0
    color1, color2 = Color.new(255, 255, 255), Color.new(255, 255, 255, 128)
    color3, color4 = Color.new(16, 16, 16), Color.new(16, 16, 16, 128)
    @rain_bitmap = Bitmap.new(7, 56)
    (0..6).each {|i| @rain_bitmap.fill_rect(6-i, i*8, 1, 8, color1)}
    @storm_bitmap = Bitmap.new(34, 64)
    (0..31).each {|i|
        @storm_bitmap.fill_rect(33-i, i*2, 1, 2, color2)
        @storm_bitmap.fill_rect(32-i, i*2, 1, 2, color1)
        @storm_bitmap.fill_rect(31-i, i*2, 1, 2, color2)}
    @snow_bitmap = Bitmap.new(6, 6)
    @snow_bitmap.fill_rect(0, 1, 6, 4, color2)
    @snow_bitmap.fill_rect(1, 0, 4, 6, color2)
    @snow_bitmap.fill_rect(1, 2, 4, 2, color1)
    @snow_bitmap.fill_rect(2, 1, 2, 4, color1)
    @ash_bitmap = Bitmap.new(6, 6)
    @ash_bitmap.fill_rect(0, 1, 6, 4, color4)
    @ash_bitmap.fill_rect(1, 0, 4, 6, color4)
    @ash_bitmap.fill_rect(1, 2, 4, 2, color3)
    @ash_bitmap.fill_rect(2, 1, 2, 4, color3)
    @sprites = []
    (1..80).each {|i|
        sprite = Sprite.new(viewport)
        sprite.z = 1000
        sprite.visible = false
        sprite.opacity = 0
        @sprites.push(sprite)}
  end
  
  def reinit(flag)
    @sprites.each {|sprite| sprite.dispose}
    @sprites = []
    (1..(flag ? 160 : 80)).each {|i|
        sprite = Sprite.new(@viewport)
        sprite.z = 1000
        sprite.visible = false
        sprite.opacity = 0
        @sprites.push(sprite)}
    xx, yy, self.ox, self.oy = @ox, @oy, 0, 0
    self.ox, self.oy = xx, yy
  end
  
  def dispose
    @rain_bitmap.dispose
    @storm_bitmap.dispose
    @snow_bitmap.dispose
    @ash_bitmap.dispose
  end
  
  def type=(type)
    return if @type == type
    reinit((type >= 4)) if (@type >= 4) != (type >= 4)
    @type = type
    bitmap = case @type
    when 1 then @rain_bitmap
    when 2 then @storm_bitmap
    when 3, 4 then @snow_bitmap
    when 5 then @ash_bitmap
    else
      nil
    end
    (1..(@type >= 4 ? 120 : 40)).each {|i|
        if @sprites[i] != nil
          @sprites[i].visible, @sprites[i].bitmap = (i <= @max), bitmap
        end}
  end
  
  def ox=(ox)
    return if @ox == ox
    @ox = ox
    @sprites.each {|sprite| sprite.ox = @ox}
  end
  
  def oy=(oy)
    return if @oy == oy;
    @oy = oy
    @sprites.each {|sprite| sprite.oy = @oy}
  end
  
  def max=(max)
    if @type >= 4
      return if @max == max * 3
      @max = (max < 0 ? 0 : (max > 40 ? 120 : max * 3))
      mm = 120
    else
      return if @max == max
      @max = (max < 0 ? 0 : (max > 40 ? 40 : max))
      mm = 40
    end
    (1..mm).each {|i| @sprites[i].visible = (i <= @max) if @sprites[i] != nil}
  end
  
  def update
    return if @type == 0
    (1..@max).each {|i|
        break if @sprites[i] == nil
        case @type
        when 1
          @sprites[i].x -= 2
          @sprites[i].y += 16
          @sprites[i].opacity -= 8
        when 2
          @sprites[i].x -= 8
          @sprites[i].y += 16
          @sprites[i].opacity -= 12
        when 3
          @sprites[i].x -= 2
          @sprites[i].y += 8
          @sprites[i].opacity -= 8
        when 4, 5
          @sprites[i].x -= 16
          @sprites[i].y += 4
          @sprites[i].opacity -= 8
        end
        x, y = @sprites[i].x - @ox, @sprites[i].y - @oy
        if @type == 4 || @type == 5
          if @sprites[i].opacity < 64 || x < -20 || x > 660 || y < -20 || y > 500
            @sprites[i].x = rand(800) - 50 + @ox
            @sprites[i].y = rand(800) - 200 + @oy
            @sprites[i].opacity = 255
          end
        elsif @sprites[i].opacity < 64 || x < -50 || x > 750 || y < -300 || y > 500
          @sprites[i].x = rand(800) - 50 + @ox
          @sprites[i].y = rand(800) - 200 + @oy
          @sprites[i].opacity = 255
        end}
  end
  
end
