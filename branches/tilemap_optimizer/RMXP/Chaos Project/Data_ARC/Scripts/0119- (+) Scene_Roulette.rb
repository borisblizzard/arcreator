#==============================================================================
# Scene_Roulette
#==============================================================================

class Scene_Roulette
  
  def initialize(digits = 4)
    @digits = digits
  end
  
  def main
    reset_wheel
    setup_background_sprites
    @cursor = Sprite.new
    @cursor.bitmap = RPG::Cache.picture('chip_1')
    @cursor.z = 1000
    @cursor.visible = false
    commands = ['Place Bet', 'Remove Bet', 'Spin', 'Quit']
    @command_window = Window_Command.new(160, commands)
    @command_window.opacity = 0
    @command_window.y = 64
    @command_window.x = 480
    @command_window.z = 500
    @command_window.active = true
    @bet_window = Window_InputNumber.new(@digits)
    @bet_window.x = 320 - @bet_window.width / 2
    @bet_window.y = 160
    @bet_window.active = false
    @bet_window.visible = false
    setup_command_window
    Graphics.transition
    loop do
      Graphics.update
      Input.update
      update
      break if $scene != self
    end
    Graphics.freeze
    (@backgrounds + @chips).each {|sprite| sprite.dispose}
    @cursor.dispose
    @command_window.dispose
    @bet_window.dispose
    Graphics.transition
    Graphics.freeze
  end
  
  def reset_wheel
    @spin, @time = 6.0, 0
    @chips, @bets = [], []
  end
  
  def setup_background_sprites
    @backgrounds = [Sprite.new, Sprite.new, Sprite.new, Sprite.new, Sprite.new]
    @backgrounds[0].bitmap = CP::Cache.image('roulette')
    @backgrounds[1].bitmap = Bitmap.new(320, 32)
    @backgrounds[2].bitmap = Bitmap.new(640, 40)
    @backgrounds[3].bitmap = RPG::Cache.picture('roulette wheel')
    @backgrounds[4].bitmap = RPG::Cache.picture('roulette ball')
    @backgrounds[1].bitmap.font.name = 'Geometrix'
    @backgrounds[1].y = 16
    @backgrounds[1].x = 300
    refresh_gold
    @backgrounds[2].y = 212
    @backgrounds[2].z = 1000
    @backgrounds[2].bitmap.font.name = 'Brush Script'
    @backgrounds[2].bitmap.font.size = 40
    @backgrounds[3].y = 120
    @backgrounds[3].x = 120
    @backgrounds[3].oy = @backgrounds[3].ox = 100
    @backgrounds[3].z = 1000
    @backgrounds[3].angle = rand(37) * 360 / 37.0
    @backgrounds[4].y = 120
    @backgrounds[4].x = 120
    @backgrounds[4].oy = 105
    @backgrounds[4].ox = 5
    @backgrounds[4].z = 1100
    @backgrounds[4].angle = rand(37) * 360 / 37.0
    
  end
  
  def refresh_gold
    @backgrounds[1].bitmap.clear
    sum = 0
    @bets.each {|bet| sum += bet.value}
    @backgrounds[1].bitmap.draw_text_outline(0, 0, 240, 32,
        "#{sum} / #{$game_party.gold} #{$data_system.words.gold}", 2)
  end
  
  def update
    if @command_window.active
      @backgrounds[3].angle += @spin
      @backgrounds[4].angle -= @spin * 2
      update_command
    elsif @bet_window.active
      @backgrounds[3].angle += @spin
      @backgrounds[4].angle -= @spin * 2
      update_bet
    elsif @cursor.visible
      @backgrounds[3].angle += @spin
      @backgrounds[4].angle -= @spin * 2
      update_cursor
    else
      update_spin
    end
  end

  def update_command
    @command_window.update
    if Input.trigger?($controls.cancel)
      $game_system.se_play($data_system.cancel_se)
      $scene = Scene_Map.new
    elsif Input.trigger?($controls.confirm)
      case @command_window.index
      when 0
        sum = 0
        @bets.each {|bet| sum += bet.value}
        if @bets.size == 151 || $game_party.gold - sum == 0
          $game_system.se_play($data_system.buzzer_se)
          return
        end
        $game_system.se_play($data_system.decision_se)
        setup_cursor
        @command_window.active = false
      when 1
        if @bets.size == 0
          $game_system.se_play($data_system.buzzer_se)
          return
        end
        $game_system.se_play($data_system.decision_se)
        setup_cursor(false)
        @command_window.active = false
      when 2
        if @bets.size == 0
          $game_system.se_play($data_system.buzzer_se)
          return
        end
        $game_system.se_play($data_system.decision_se)
        @command_window.active = false
        sum = 0
        @bets.each {|bet| sum += bet.value}
        $game_party.lose_gold(sum)
        @time = 80 + rand(161)
      when 3
        $game_system.se_play($data_system.decision_se)
        $scene = Scene_Map.new
      end
    end
  end
  
  def update_cursor
    if Input.repeat?($controls.up)
      $game_system.se_play($data_system.cursor_se) if try_move_cursor_up
    elsif Input.repeat?($controls.left)
      $game_system.se_play($data_system.cursor_se) if try_move_cursor_left
    elsif Input.repeat?($controls.right)
      $game_system.se_play($data_system.cursor_se) if try_move_cursor_right
    elsif Input.repeat?($controls.down)
      $game_system.se_play($data_system.cursor_se) if try_move_cursor_down
    elsif Input.trigger?($controls.cancel)
      $game_system.se_play($data_system.cancel_se)
      setup_command_window
      @command_window.active = true
      @cursor.visible = false
    elsif Input.trigger?($controls.confirm)
      case @command_window.index
      when 0
        if @chips.any? {|chip| @cursor.x == chip.x && @cursor.y == chip.y}
          $game_system.se_play($data_system.buzzer_se)
          return
        end
        $game_system.se_play($data_system.decision_se)
        @bet_window.active = true
        @bet_window.visible = true
        @bet_window.reset
      when 1
        found_chip = nil
        @chips.each {|chip|
            if @cursor.x == chip.x && @cursor.y == chip.y
              found_chip = chip
              break
            end}
        if found_chip == nil
          $game_system.se_play($data_system.buzzer_se)
          return
        end
        $game_system.se_play($data_system.decision_se)
        index = @chips.index(found_chip)
        @chips.delete_at(index)
        @bets.delete_at(index)
        found_chip.dispose
        setup_command_window
        refresh_gold
        if @bets.size == 0
          @command_window.active = true
          @cursor.visible = false
        end
      end
    end
  end
  
  def update_bet
    @bet_window.update
    if Input.trigger?($controls.cancel)
      $game_system.se_play($data_system.cancel_se)
      @bet_window.active = false
      @bet_window.visible = false
    elsif Input.trigger?($controls.confirm)
      sum = 0
      @bets.each {|bet| sum += bet.value}
      if @bet_window.number > $game_party.gold - sum || @bet_window.number == 0
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      $game_system.se_play($data_system.decision_se)
      create_new_chip
      create_new_bet
      @bet_window.active = false
      @bet_window.visible = false
      @cursor.visible = false
      @command_window.active = true
      refresh_gold
      setup_command_window
      if @bets.size == 151 || $game_party.gold - sum == 0
        @command_window.active = true
        @cursor.visible = false
      end
    end
  end
  
  def update_spin
    @time -= 1
    if @time > 0
      @backgrounds[3].angle += @spin
      @backgrounds[4].angle -= @spin * 2
      if @time % 2 == 0
        $game_system.se_play(RPG::AudioFile.new('032-Switch01', 80, 100))
      end
    else
      if @time == 0
        offset1 = @backgrounds[3].angle - (@backgrounds[3].angle / 360 * 37).floor * 360.0 / 37
        offset2 = @backgrounds[4].angle - (@backgrounds[4].angle / 360 * 37).floor * 360.0 / 37
        @backgrounds[4].angle = @backgrounds[4].angle + offset1 - offset2
        angle = (@backgrounds[3].angle - @backgrounds[4].angle + 0.001) % 360
        number = CP::Cache::Roulette[(angle * 37.0 / 360).floor]
        sum = payout = 0
        @bets.each {|bet|
            sum += bet.value
            payout += bet.payout if bet.won?(number.value)}
        @backgrounds[2].visible = true
        @backgrounds[2].bitmap.clear
        if payout < sum
          @backgrounds[2].bitmap.font.color = Color.new(255, 0, 0)
          @backgrounds[2].bitmap.draw_text_outline(0, 0, 640, 40,
              "You lost #{sum - payout} #{$data_system.words.gold}!", 1)
          $game_system.se_play($data_system.buzzer_se)
        else
          @backgrounds[2].bitmap.font.color = Color.new(0, 255, 0)
          @backgrounds[2].bitmap.draw_text_outline(0, 0, 640, 40,
              "You won #{payout - sum} #{$data_system.words.gold}!", 1)
          $game_system.se_play($data_system.save_se)
        end
        $game_party.gain_gold(payout)
      end
      if @spin > 0.1
        @backgrounds[3].angle += @spin
        @backgrounds[4].angle += @spin
      end
      @spin *= 0.98
      if @spin < 0.05
        @backgrounds[2].visible = false
        @chips.each {|sprite| sprite.dispose}
        reset_wheel
        @command_window.active = true
        setup_command_window
        refresh_gold
      end
    end
  end
  
  def setup_command_window
    @command_window.refresh
    if @bets.size == 0
      @command_window.disable_item(1)
      @command_window.disable_item(2)
    end
    sum = 0
    @bets.each {|bet| sum += bet.value}
    if @bets.size == 151 || $game_party.gold - sum == 0
      @command_window.disable_item(0)
    end
  end
  
  def setup_cursor(flag = true)
    @cursor.bitmap = RPG::Cache.picture(flag ? 'chip_1' : 'chip_2')
    @cursor.visible = true
    @cursor.x, @cursor.y = 70, 270
  end
  
  def create_new_chip
    sprite = Sprite.new
    sprite.bitmap = RPG::Cache.picture('chip_0')
    sprite.x, sprite.y = @cursor.x, @cursor.y
    sprite.z = 500
    @chips.push(sprite)
  end
  
  def create_new_bet
    numbers = []
    if @cursor.y == 390
      case @cursor.x
      when 130
        CP::Cache::Roulette.each {|n| numbers.push(n.value) if n.is_1_to_12?}
      when 290
        CP::Cache::Roulette.each {|n| numbers.push(n.value) if n.is_13_to_24?}
      when 450
        CP::Cache::Roulette.each {|n| numbers.push(n.value) if n.is_25_to_36?}
      end
    elsif @cursor.y == 430
      case @cursor.x
      when 90
        CP::Cache::Roulette.each {|n| numbers.push(n.value) if n.is_1_to_18?}
      when 170
        CP::Cache::Roulette.each {|n| numbers.push(n.value) if n.even?}
      when 250
        CP::Cache::Roulette.each {|n| numbers.push(n.value) if n.red?}
      when 330
        CP::Cache::Roulette.each {|n| numbers.push(n.value) if n.black?}
      when 410
        CP::Cache::Roulette.each {|n| numbers.push(n.value) if n.odd?}
      when 490
        CP::Cache::Roulette.each {|n| numbers.push(n.value) if n.is_19_to_36?}
      end
    elsif @cursor.x == 30
      CP::Cache::Roulette.each {|n| numbers.push(n.value) if n.is_0?}
    elsif @cursor.x == 570
      case @cursor.y
      when 270
        CP::Cache::Roulette.each {|n| numbers.push(n.value) if n.column3?}
      when 310
        CP::Cache::Roulette.each {|n| numbers.push(n.value) if n.column2?}
      when 350
        CP::Cache::Roulette.each {|n| numbers.push(n.value) if n.column1?}
      end
    else
      if @cursor.y == 370
        x = @cursor.x - 70
        (0...3).each {|i|
            numbers.push(x / 40 * 3 + i + 1)
            numbers.push((x + 20) / 40 * 3 + i + 1)}
      else
        x, y = @cursor.x - 70, @cursor.y - 270
        numbers.push(x / 40 * 3 + (2 - y / 40) + 1)
        numbers.push((x + 20) / 40 * 3 + (2 - y / 40) + 1)
        numbers.push(x / 40 * 3 + (2 - (y + 20) / 40) + 1)
        numbers.push((x + 20) / 40 * 3 + (2 - (y + 20) / 40) + 1)
      end
      numbers |= numbers
    end
    @bets.push(Roulette_Bet.new(@bet_window.number, numbers.sort))
  end
  
  def try_move_cursor_up
    x, y = @cursor.x, @cursor.y
    if @cursor.y >= 270 && @cursor.y <= 370 && @cursor.x >= 70 && @cursor.x <= 570
      if @cursor.y > 270
        @cursor.y -= 20
        @cursor.y -= 20 if @cursor.x == 570
      end
    elsif @cursor.y == 390
      @cursor.y -= 20
    elsif @cursor.y == 430
      @cursor.y -= 40
      @cursor.x = 130 + (@cursor.x - 70) / 160 * 160
    end
    return (@cursor.x != x || @cursor.y != y)
  end
  
  def try_move_cursor_down
    x, y = @cursor.x, @cursor.y
    if @cursor.y >= 270 && @cursor.y <= 370 && @cursor.x >= 70 && @cursor.x <= 570
      @cursor.y += 20
      @cursor.y += 20 if @cursor.x == 570
      if @cursor.y == 390
        @cursor.x = 130 + (@cursor.x - 70) / 160 * 160
        @cursor.x -= 160 if @cursor.x > 450
      end
    elsif @cursor.y == 390
      @cursor.y += 40
      @cursor.x = 90 + (@cursor.x - 70) / 160 * 160
    elsif @cursor.x < 70
      @cursor.y += 80
      @cursor.x += 100
    end
    return (@cursor.x != x || @cursor.y != y)
  end
  
  def try_move_cursor_left
    x, y = @cursor.x, @cursor.y
    if @cursor.y >= 270 && @cursor.y <= 370 && @cursor.x >= 40 && @cursor.x <= 570
      @cursor.x -= 20
      @cursor.x -= 40 if @cursor.x > 510
    elsif @cursor.x >= 530
      @cursor.x = 510
    elsif @cursor.y == 390
      @cursor.x -= 160
    elsif @cursor.y == 430
      @cursor.x -= 80
    end
    if @cursor.x < 70
      @cursor.x = 30
      @cursor.y = 310
    end
    return (@cursor.x != x || @cursor.y != y)
  end
  
  def try_move_cursor_right
    x, y = @cursor.x, @cursor.y
    if @cursor.y >= 270 && @cursor.y <= 370 && @cursor.x >= 40 && @cursor.x <= 510
      @cursor.x += 20
      @cursor.x += 40 if @cursor.x > 510
    elsif @cursor.x == 30
      @cursor.x += 40
    elsif @cursor.y == 390
      @cursor.x += 160
    elsif @cursor.y == 430
      @cursor.x += 80
    end
    if @cursor.x > 510
      @cursor.x = 570
      @cursor.y = 350 if @cursor.y > 350
      @cursor.y = 270 + (@cursor.y - 270) / 40 * 40
    end
    return (@cursor.x != x || @cursor.y != y)
  end
  
end
