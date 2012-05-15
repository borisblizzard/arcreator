#==============================================================================
# Game_Picture
#==============================================================================

class Game_Picture
  
  attr_reader   :number
  attr_reader   :name
  attr_reader   :origin
  attr_reader   :x
  attr_reader   :y
  attr_reader   :zoom_x
  attr_reader   :zoom_y
  attr_reader   :opacity
  attr_reader   :blend_type
  attr_reader   :tone
  attr_reader   :angle
  
  def initialize(number)
    @number = number
    @name = ''
    @origin = 0
    @x = @y = 0.0
    @zoom_x = @zoom_y = 100.0
    @opacity, @blend_type, @duration = 255.0, 1, 0
    @target_x, @target_y, @target_zoom_x, @target_zoom_y = @x, @y, @zoom_x, @zoom_y
    @target_opacity = @opacity
    @tone, @tone_target = Tone.new(0, 0, 0, 0), Tone.new(0, 0, 0, 0)
    @tone_duration = @angle = @rotate_speed = 0
  end
  
  def show(name, origin, x, y, zoom_x, zoom_y, opacity, blend_type)
    @name = name
    @origin = origin
    @x, @y = x.to_f,  y.to_f
    @zoom_x, @zoom_y = zoom_x.to_f, zoom_y.to_f
    @opacity, @blend_type, @duration = opacity.to_f, blend_type, 0
    @target_x, @target_y, @target_zoom_x, @target_zoom_y = @x, @y, @zoom_x, @zoom_y
    @target_opacity = @opacity
    @tone, @tone_target = Tone.new(0, 0, 0, 0), Tone.new(0, 0, 0, 0)
    @tone_duration = @angle = @rotate_speed = 0
  end
  
  def move(duration, origin, x, y, zoom_x, zoom_y, opacity, blend_type)
    @duration, @origin = duration, origin
    @target_x, @target_y = x.to_f, y.to_f
    @target_zoom_x, @target_zoom_y = zoom_x.to_f, zoom_y.to_f
    @target_opacity, @blend_type = opacity.to_f, blend_type
  end
  
  def rotate(speed)
    @rotate_speed = speed
  end
  
  def start_tone_change(tone, duration)
    @tone_target, @tone_duration = tone.clone, duration
    @tone = @tone_target.clone if @tone_duration == 0
  end
  
  def erase
    @name = ''
  end
  
  def update
    if @duration >= 1
      d = @duration
      @x, @y = (@x * (d - 1) + @target_x) / d, (@y * (d - 1) + @target_y) / d
      @zoom_x = (@zoom_x * (d - 1) + @target_zoom_x) / d
      @zoom_y = (@zoom_y * (d - 1) + @target_zoom_y) / d
      @opacity = (@opacity * (d - 1) + @target_opacity) / d
      @duration -= 1
    end
    if @tone_duration >= 1
      d = @tone_duration
      @tone.red = (@tone.red * (d - 1) + @tone_target.red) / d
      @tone.green = (@tone.green * (d - 1) + @tone_target.green) / d
      @tone.blue = (@tone.blue * (d - 1) + @tone_target.blue) / d
      @tone.gray = (@tone.gray * (d - 1) + @tone_target.gray) / d
      @tone_duration -= 1
    end
    if @rotate_speed != 0
      @angle += @rotate_speed / 2.0
      @angle += 360 while @angle < 0
      @angle %= 360
    end
  end
  
end
