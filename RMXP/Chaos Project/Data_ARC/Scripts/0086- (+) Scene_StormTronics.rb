#==============================================================================
# Scene_Stormtronics
#==============================================================================

class Scene_Stormtronics
  
  def delay(sec)
    (0...(sec*10)).each {|i|
        if @last && Graphics.frame_count % 2 == 1
          @introX.y -= 1 if @introX != nil
          @introY.y -= 1 if @introY != nil
        end
        Graphics.update
        Input.update
        return true if Input.press?($controls.confirm) || Input.press?($controls.cancel)}
    Input.update
    return true if sec == 0 && (Input.press?($controls.confirm) || Input.press?($controls.cancel))
    return false
  end
  
  def correct(index, mode)
    case index
    when 0 then result = 450
    when 1 then result = 360
    when 2 then result = 270
    when 3 then result = 180
    when 4 then result = 90
    when 5 then result = 0
    when 6 then result = -80
    when 7 then result = -160
    when 8 then result = -240
    when 9 then result = -320
    when 10 then result = -400
    when 11 then result = -480
    end
    result /= 10 if mode
    return result
  end
  
  def main
    @intro_fade = false
    @view = Viewport.new(0, 0, 640, 480)
    @white = Bitmap.new(640, 480)
    @white.fill_rect(0, 0, 640, 480, Color.new(255, 255, 255))
    show_intro
    if @white.is_a?(Bitmap)
      white = @white
      @white = Sprite.new(@view)
      @white.bitmap = white
      @white.z = 10000
      @white.opacity = 0
    end
    loop do
      delay(0.1)
      @white.opacity += (@last ? 5 : 15)
      break if @white.opacity == 255
    end
    delay(@last ? 5 : 1)
    Graphics.freeze
    @intro1.dispose unless @intro1 == nil || @intro1.disposed?
    @intro2.dispose unless @intro2 == nil || @intro2.disposed?
    @intro3.dispose unless @intro3 == nil || @intro3.disposed?
    @intro4.dispose unless @intro4 == nil || @intro4.disposed?
    if @intro != nil
      if @intro.is_a?(Array)
        @intro.each {|i| i.dispose unless i.disposed?}
      else
        @intro.dispose unless @intro.disposed?
      end
    end
    @white.dispose unless @white == nil || @white.disposed?
    @view.dispose unless @view == nil
    $scene = Scene_Title.new
    $scene.intro_fade = @intro_fade
  end
  
  def cache
    (0...12).each {|i| RPG::Cache.picture("Intro/#{i}")}
    RPG::Cache.picture('StormTronics')
    RPG::Cache.picture('Intro/StormGlow')
    RPG::Cache.picture('Intro/StormMask')
    RPG::Cache.picture('Intro/StormFlash')
    RPG::Cache.picture('presents').clone
    RPG::Cache.picture('ChaosProject')
    RPG::Cache.picture('Intro/ChaosMask')
    RPG::Cache.picture('Intro/cp1')
    RPG::Cache.picture('Intro/cp2')
    RPG::Cache.picture('Intro/cp3')
    RPG::Cache.picture('Intro/cp4')
    RPG::Cache.picture('Intro/cp5')
  end
  
  def show_intro
    cache
    Graphics.transition
    Graphics.freeze
    delay(5)
    @intro = Sprite.new(@view)
    @intro.bitmap = Bitmap.new(640, 480)
    @intro.bitmap.draw_text(0, 160, 640, 32, 'This game was created for non-commercial and', 1)
    @intro.bitmap.draw_text(0, 192, 640, 32, 'educational purposes only. It is protected', 1)
    @intro.bitmap.draw_text(0, 224, 640, 32, 'by the Fair use doctrine of the copyright law.', 1)
    @intro.bitmap.draw_text(0, 288, 640, 32, 'Thank you for your understanding and your cooperation.', 1)
    Graphics.transition
    Graphics.freeze
    delay(30)
    @intro.dispose
    @intro = nil
    Graphics.transition
    Graphics.freeze
    delay(1)
    Audio.me_fade(800)
    delay(1.5)
    Graphics.freeze
    @intro1 = Sprite.new(@view)
    @intro2 = Sprite.new(@view)
    @intro3 = Sprite.new(@view)
    @intro4 = Sprite.new(@view)
    delay(2.5)
    $game_system.bgm_play($data_system.title_bgm)
    return if delay(1)
    Graphics.freeze
    @intro = Sprite.new(@view)
    @intro1 = Sprite.new(@view)
    @intro2 = Sprite.new(@view)
    @intro3 = Sprite.new(@view)
    @intro4 = Sprite.new(@view)
    @intro1.bitmap = RPG::Cache.picture('StormTronics')
    @intro2.bitmap = RPG::Cache.picture('Intro/StormGlow')
    @intro3.bitmap = RPG::Cache.picture('Intro/StormMask')
    @intro2.x = -240
    Graphics.transition
    return if delay(3)
    Graphics.freeze
    @intro4.bitmap = RPG::Cache.picture('Intro/StormFlash')
    Graphics.transition(2)
    Graphics.freeze
    @intro4.bitmap = nil
    Graphics.transition(2)
    return if delay(1)
    loop do
      @intro2.x += 70
      Graphics.update
      break if @intro2.x > 700
    end
    return if delay(4)
    Graphics.freeze
    @intro4.bitmap = RPG::Cache.picture('presents')
    Graphics.transition(12)
    return if delay(8)
    Graphics.freeze
    @intro2.dispose
    @intro3.dispose
    @intro4.dispose
    @intro1.bitmap = @intro2 = @intro3 = @intro4 = nil
    Graphics.transition(12)
    Graphics.freeze
    return if delay(8)
    @intro, flags = [], [true]
    (0..11).each {|i|
        sprite = Sprite.new(@view)
        sprite.bitmap = RPG::Cache.picture("Intro/#{i}")
        sprite.x = sprite.ox = 320 + 48 * (i - (i >= 6 ? 6 : 5))
        sprite.x -= 2000
        sprite.y = sprite.oy = 200
        sprite.zoom_x = sprite.zoom_y = 5.0
        @intro.push(sprite)
        flags.push(false)}
    Graphics.transition(10)
    @intro[0].x += 2000
    i = j = 0
    loop do
      Graphics.update
      if flags[i]
        @intro[i].zoom_x -= 0.4
        @intro[i].zoom_y -= 0.4
        if j > 0 && j < @intro.size
          @intro[j].zoom_x -= 0.4
          @intro[j].zoom_y -= 0.4
        end
        if @intro[i].zoom_x.between?(2.7, 3.3)
          j += 1
          @intro[j].x += 2000
        end
        if @intro[i].zoom_x <= 1
          i += 1
          j += 1
          flags[i] = true
          @intro[j].x += 2000 if @intro[j] != nil
        end
      end
      return if delay(0)
      break if flags[@intro.size]
    end
    Graphics.freeze
    @intro.reverse.each {|sprite| sprite.dispose}
    @intro = nil
    return if delay(2)
    @intro1 = Sprite.new(@view)
    @intro2 = Sprite.new(@view)
    @intro3 = Sprite.new(@view)
    @intro4 = Sprite.new(@view)
    @intro1.bitmap = RPG::Cache.picture('ChaosProject')
    @intro1.z = 70
    Graphics.transition(30, 'Graphics/Transitions/ChaosForms')
    @intro2.bitmap = RPG::Cache.picture('Intro/ChaosMask')
    @intro2.x, @intro2.y, @intro2.ox, @intro2.oy = 310, 220, 310, 220
    @intro3.bitmap = @intro4.bitmap = RPG::Cache.picture('Intro/ch_fog')
    @intro3.blend_type = @intro4.blend_type = 1
    @intro3.z = @intro4.z = 50
    @intro3.y = @intro4.y = 384
    @intro3.ox = @intro4.ox = 640
    @intro3.oy = @intro4.oy = 300
    @intro2.z, @intro3.x, @intro4.x = 100, 0, 640
    return if delay(8)
    loop do
      Graphics.update
      @intro1.opacity -= 5
      @intro3.x += 4
      @intro4.x -= 4
      @intro3.y = 384 + rand(49)
      @intro4.y = 384 + rand(49)
      break if @intro3.x > 480
    end
    loop do
      Graphics.update
      @intro2.zoom_x *= 1.1
      @intro2.zoom_y *= 1.1
      @intro3.zoom_x *= 1.1
      @intro3.zoom_y *= 1.1
      @intro4.zoom_x *= 1.1
      @intro4.zoom_y *= 1.1
      @intro3.opacity -= 10
      @intro4.opacity -= 10
      @intro3.x += 4 * @intro3.zoom_x
      @intro4.x -= 4 * @intro4.zoom_x
      break if @intro2.zoom_x > 100
    end
    Graphics.update
    @intro1.dispose
    @intro2.dispose
    @intro3.dispose
    @intro4.dispose
    @intro = Sprite.new(@view)
    @intro1 = Sprite.new(@view)
    @intro2 = Sprite.new(@view)
    @intro3 = Sprite.new(@view)
    @intro4 = Sprite.new(@view)
    @intro1.bitmap = RPG::Cache.picture('Intro/cp1')
    @intro2.bitmap = RPG::Cache.picture('Intro/cp2')
    @intro3.bitmap = RPG::Cache.picture('Intro/cp3')
    @intro4.bitmap = RPG::Cache.picture('Intro/cp4')
    @intro.bitmap = RPG::Cache.picture('Intro/cp5')
    @intro.opacity = 255
    @intro1.opacity = 255
    @intro2.opacity = 255
    @intro3.opacity = 255
    @intro1.z = 1000
    @intro2.z = 1000
    @intro3.z = 1000
    @intro1.x = @intro1.y = @intro2.x = @intro2.y =  @intro3.x = @intro3.y =
        @intro4.x = @intro4.y = @intro.x = @intro.y = 0
    @intro1.x = -480
    @intro2.y = 640
    @intro3.y = -640
    @intro4.opacity = 0
    @intro.x = @intro.ox = 320
    @intro.y = @intro.oy = 240
    @intro.zoom_x = @intro.zoom_y = 1.1 ** 16
    @intro.opacity = 0
    return if delay(2)
    loop do
      Graphics.update
      if @intro1.x == -16
        @intro1.x += 8
      elsif @intro1.x == -8
        @intro1.x += 4
      elsif @intro1.x == -4
        @intro1.x += 2
      elsif @intro1.x == -2 || @intro1.x == -1
        @intro1.x += 1
      else
        @intro1.x += 16
      end
      break if @intro1.x >= 0
    end
    loop do
      Graphics.update
      @intro2.y -= 16
      @intro3.y += 16
      break if @intro3.y >= 0
    end
    Graphics.update
    @intro1.x -= 8
    @intro2.y -= 8
    @intro3.x += 8
    Graphics.update
    @intro1.y -= 8
    @intro2.x -= 8
    @intro3.y += 8
    Graphics.update
    @intro1.y += 8
    @intro2.x += 8
    @intro3.y -= 8
    Graphics.update
    @intro1.x += 8
    @intro2.y += 8
    @intro3.x -= 8
    return if delay(1)
    loop do
      Graphics.update
      @intro4.opacity += 5
      break if @intro4.opacity == 255
    end
    return if delay(1)
    @intro.opacity = 255
    loop do
      Graphics.update
      @intro.zoom_x /= 1.1
      @intro.zoom_y /= 1.1
      break if @intro.zoom_x <= 1.0
    end
    @intro.zoom_x = @intro.zoom_y = 1.0
    return if delay(5)
    Graphics.freeze
    white = @white
    @white = Sprite.new(@view)
    @white.bitmap = white
    @white.z = 10000
    Graphics.transition(10)
    @intro_fade = true
  end
  
end
