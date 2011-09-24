#==============================================================================
# Scene_Slotmachine
#==============================================================================

class Scene_Slotmachine
  
  def main
    @times = []
    time = 40
    (0...3).each {|i|
        time += 40 + rand(41)
        @times.push(time)}
    setup_background_sprites
    Graphics.transition
    loop do
      Graphics.update
      Input.update
      update
      break if $scene != self
    end
    Graphics.freeze
    @backgrounds.each {|sprite|
        sprite.bitmap.dispose
        sprite.dispose}
    Graphics.transition
    Graphics.freeze
  end
  
  def setup_background_sprites
    @backgrounds = [Sprite.new, Sprite.new, Sprite.new, Sprite.new, Sprite.new]
    @backgrounds[0].bitmap = RPG::Cache.picture('slots blurred')
    @backgrounds[1].bitmap = RPG::Cache.picture('slots blurred')
    @backgrounds[2].bitmap = RPG::Cache.picture('slots blurred')
    @backgrounds[3].bitmap = RPG::Cache.picture('slotmachine')
    @backgrounds[4].bitmap = Bitmap.new(640, 40)
    @backgrounds[0].x = 110
    @backgrounds[0].y = 230
    @backgrounds[0].src_rect.set(0, 50 + rand(9) * 100, 100, 200)
    @backgrounds[1].x = 270
    @backgrounds[1].y = 230
    @backgrounds[1].src_rect.set(0, 50 + rand(9) * 100, 100, 200)
    @backgrounds[2].x = 430
    @backgrounds[2].y = 230
    @backgrounds[2].src_rect.set(0, 50 + rand(9) * 100, 100, 200)
    @backgrounds[3].z = 500
    @backgrounds[4].y = 212
    @backgrounds[4].z = 1000
    @backgrounds[4].bitmap.font.name = 'Brush Script'
    @backgrounds[4].bitmap.font.size = 40
  end
  
  def update
    @times.each_index {|i| @times[i] -= 1}
    if @times[0] == @times[1] && @times[0] == @times[2]
      $scene = Scene_Map.new if Input.trigger?($controls.confirm)
    else
      finished = true
      (0...3).each {|i|
          y = @backgrounds[i].src_rect.y
          if @times[i] > 0 || y % 100 != 50
            if i == 2 && y % 100 == 0
              $game_system.se_play(RPG::AudioFile.new('032-Switch01', 80, 100))
            end
            y = (y - 25) % 900
            if @times[i] <= 1 && y % 100 == 50
              @backgrounds[i].bitmap = RPG::Cache.picture('slots')
            else
              finished = false
            end
            @backgrounds[i].src_rect.set(0, y, 100, 200)
          end}
      setup_result if finished
    end
  end
  
  def setup_result
    @times.each_index {|i| @times[i] = 0}
    result = []
    (0...3).each {|i| result.push(((@backgrounds[i].src_rect.y + 50) % 900) / 100)}
    matches = []
    CP::Cache::Slots.each {|slot|
        if (slot[0] == -1 || slot[0] == result[0]) &&
            (slot[1] == -1 || slot[1] == result[1]) &&
            (slot[2] == -1 || slot[2] == result[2])
          matches.push(slot)
        end}
    matches |= matches
    if matches.size == 0
      @backgrounds[4].bitmap.font.color = Color.new(255, 0, 0)
      @backgrounds[4].bitmap.draw_text_outline(0, 0, 640, 40,
          "You lost #{$game_variables[174]} #{$data_system.words.gold}!", 1)
      $game_system.se_play($data_system.buzzer_se)
    else
      max = matches.shift
      matches.each {|slot| max = slot if max[3] < slot[3]}
      gold = max[3] * $game_variables[174]
      @backgrounds[4].bitmap.font.color = Color.new(0, 255, 0)
      text = "You won #{gold} #{$data_system.words.gold}!"
      text = "Jackpot! #{text}" if max[3] == 250
      @backgrounds[4].bitmap.draw_text_outline(0, 0, 640, 40, text, 1)
      $game_party.gain_gold(max[3] * $game_variables[174])
      $game_system.se_play($data_system.save_se)
    end
  end

end
