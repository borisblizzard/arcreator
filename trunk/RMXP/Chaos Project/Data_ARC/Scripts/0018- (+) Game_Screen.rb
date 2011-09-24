#==============================================================================
# Game_Screen
#==============================================================================

class Game_Screen
  
  attr_reader :tone
  attr_reader :flash_color
  attr_reader :shake
  attr_reader :tremble
  attr_reader :pictures
  attr_reader :weather_type
  attr_reader :weather_max
  
  def initialize
    @tone, @tone_target = Tone.new(0, 0, 0, 0), Tone.new(0, 0, 0, 0)
    @flash_color = Color.new(0, 0, 0, 0)
    @tone_duration = @flash_duration = @shake_power = @shake_speed =
    @weather_type = @weather_type_target = @weather_duration = 0
    init_tremble
    init_shake
    @pictures = [nil]
    CP::Cache::PictureRange.each {|i| @pictures.push(Game_Picture.new(i))}
    @weather_max = @weather_max_target = 0.0
  end
  
  def init_tremble
    @tremble, @tremble_power, @tremble_direction = 0, 0, 1
  end
  
  def init_shake
    @shake_duration, @shake, @shake_direction = 0, 0, 1
  end
  
  def start_tone_change(tone, duration)
    @tone_target = tone.clone
    @tone_duration = duration
    @tone = @tone_target.clone if @tone_duration == 0
  end
  
  def start_flash(color, duration)
    @flash_color = color.clone
    @flash_duration = duration
  end
  
  def start_shake(power, speed, duration)
    if power == 0 || speed == 0 || duration == 0
      @shake_power = 0
      init_shake
      init_tremble
    else
      @shake_power, @shake_speed = power, speed
      @shake_duration, @tremble_power = duration, power * 8 / 7
    end
  end
  
  def weather(type, power, duration)
    @weather_type_target = type
    @weather_type = @weather_type_target if @weather_type_target != 0
    @weather_max_target = (@weather_type_target == 0 ? 0.0 : (power + 1) * 4.0)
    @weather_duration = duration
    if @weather_duration == 0
      @weather_type, @weather_max = @weather_type_target, @weather_max_target
    end
  end
  
  def update
    if @tone_duration >= 1
      d = @tone_duration
      @tone.red = (@tone.red * (d - 1) + @tone_target.red) / d
      @tone.green = (@tone.green * (d - 1) + @tone_target.green) / d
      @tone.blue = (@tone.blue * (d - 1) + @tone_target.blue) / d
      @tone.gray = (@tone.gray * (d - 1) + @tone_target.gray) / d
      @tone_duration -= 1
    end
    if @flash_duration >= 1
      d = @flash_duration
      @flash_color.alpha = @flash_color.alpha * (d - 1) / d
      @flash_duration -= 1
    end
    if @shake_duration >= 1 || @shake != 0
      delta = (@shake_power * @shake_speed * @shake_direction) / 10.0
      if @shake_duration <= 1 && @shake * (@shake + delta) < 0
        @shake = 0
      else
        @shake += delta
      end
      @shake_direction = -1 if @shake > @shake_power * 2
      @shake_direction = 1 if @shake < - @shake_power * 2
      @shake_duration -= 1 if @shake_duration >= 1
    end
    if @shake_duration >= 1 || @tremble != 0
      delta = (@tremble_power * (@shake_speed + 1) * @tremble_direction) / 10.0
      if @shake_duration <= 1 && @tremble * (@tremble + delta) < 0
        @tremble = 0
      else
        @tremble += delta
      end
      @tremble_direction = -1 if @tremble > @tremble_power * 1.5
      @tremble_direction = 1 if @tremble < -@tremble_power * 1.5
      @shake_duration -= 1 if @shake_duration >= 1
    end
    if @weather_duration >= 1
      d = @weather_duration
      @weather_max = (@weather_max * (d - 1) + @weather_max_target) / d
      @weather_duration -= 1
      @weather_type = @weather_type_target if @weather_duration == 0
    end
    ($game_temp.in_battle ? 51..100 : 1..50).each {|i| @pictures[i].update}
  end
  
end
