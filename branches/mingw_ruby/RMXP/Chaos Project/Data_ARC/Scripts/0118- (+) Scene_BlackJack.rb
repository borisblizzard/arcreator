#==============================================================================
# Sprite_Card
#==============================================================================

class Sprite_Card < Sprite
  
  SPEED = 20.0
  
  attr_reader :dx
  attr_reader :dy
  
  def initialize(viewport = nil)
    super
    @dx, @dy = self.x, self.y
  end
  
  def dx=(val)
    @dx = val.to_f
  end
  
  def dy=(val)
    @dy = val.to_f
  end
  
  def update
    if moving?
      cx, cy = @dx - self.x, @dy - self.y
      angle = Math.atan2(cy, cx)
      sx, sy = SPEED * Math.cos(angle), SPEED * Math.sin(angle)
      if sx.to_i.abs > cx.to_i.abs || sy.to_i.abs > cy.to_i.abs
        self.x, self.y = @dx, @dy
      else
        self.x += sx
        self.y += sy
      end
    end
  end
  
  def moving?
    return (self.x != @dx || self.y != @dy)
  end
  
end

#==============================================================================
# Scene_BlackJack
#==============================================================================

class Scene_BlackJack
  
  def main
    $game_variables[175] = 0
    @player_sprites, @dealer_sprites = [[]], []
    @sprites = []
    setup_background_sprites
    commands = ['Hit', 'Stand', 'Double', 'Split']
    @command_window = Window_H2Command.new(112, commands)
    @command_window.visible = false
    @command_window.opacity = 0
    @command_window.y = 418
    @command_window.x = 80
    @command_window.z = 500
    @player = [Hand.new]
    @index = 0
    @dealer = Hand.new
    @finished = false
    refresh_hands
    refresh_bet
    shuffle_deck
    deal_to_player
    deal_to_dealer
    deal_to_player
    deal_to_dealer
    Graphics.transition
    loop do
      Graphics.update
      Input.update
      update
      break if $scene != self
    end
    Graphics.freeze
    (@backgrounds + @sprites).each {|sprite| sprite.dispose}
    @command_window.dispose
    Graphics.transition
    Graphics.freeze
  end
  
  def setup_background_sprites
    @backgrounds = [Sprite.new, Sprite.new, Sprite.new, Sprite.new, Sprite.new]
    @backgrounds[0].bitmap = RPG::Cache.picture('blackjack').clone
    @backgrounds[1].bitmap = RPG::Cache.picture('blackjack').clone
    @backgrounds[2].bitmap = Bitmap.new(640, 80)
    @backgrounds[3].bitmap = Bitmap.new(192, 32)
    @backgrounds[4].bitmap = Bitmap.new(160, 32)
    @backgrounds[0, 3].each {|sprite|
        sprite.bitmap.font.name = 'Brush Script'
        sprite.bitmap.font.size = 40
        sprite.bitmap.font.color = Color.new(255, 224, 0)}
    @backgrounds[3, 2].each {|sprite|
        sprite.bitmap.font.name = 'Geometrix'
        sprite.bitmap.font.size = 24
        sprite.bitmap.font.color = Color.new(255, 224, 0)}
    @backgrounds[0].z = 200
    @backgrounds[0].bitmap.draw_text_outline(24, 10, 480, 40, 'Dealer')
    @backgrounds[1].y = 240
    @backgrounds[1].bitmap.draw_text_outline(24, 10, 480, 40, 'Player')
    @backgrounds[2].y = 200
    @backgrounds[2].z = 1000
    @backgrounds[3].x = 224
    @backgrounds[3].y = 248
    @backgrounds[3].z = 500
    @backgrounds[3].bitmap.font.color = Color.new(255, 255, 255)
    @backgrounds[4].x = 464
    @backgrounds[4].y = 248
    @backgrounds[4].z = 500
    @backgrounds[4].bitmap.font.color = Color.new(255, 255, 255)
  end
  
  def refresh_bet
    @backgrounds[3].bitmap.clear
    @backgrounds[3].bitmap.draw_text_outline(0, 0, 64, 32, 'Bet:')
    @backgrounds[3].bitmap.draw_text_outline(0, 0, 192, 32,
        "#{$game_variables[174] * @player.size} #{$data_system.words.gold}", 2)
  end
  
  def refresh_hands
    @backgrounds[4].bitmap.clear
    @backgrounds[4].bitmap.draw_text_outline(0, 0, 160, 32,
        "Hand: #{@index + 1} / #{@player.size}", 2)
  end
  
  def update
    @sprites.each {|sprite|
        if sprite.moving?
          sprite.update
          return
        end}
    if @finished
      if Input.trigger?($controls.confirm)
        $scene = Scene_Map.new
      end
    else
      if @player.size == 1 && @player[0].blackjack? || @dealer.blackjack?
        finish_game
        return
      end
      if @player.any? {|hand| !hand.stand && !hand.busted? &&
          !hand.blackjack? && !hand.full?}
        update_player
      elsif !@dealer.full? && @dealer.score < 17 &&
          @player.all? {|hand| (hand <=> @dealer) > 0} &&
          @player.any? {|hand| !hand.blackjack?}
        deal_to_dealer
      else
        finish_game
      end
    end
  end
  
  def update_player
    setup_command_window if !@command_window.visible
    @command_window.update
    if Input.trigger?($controls.confirm)
      if @player[@index].busted? || @player[@index].has_21? ||
          @player[@index].full?
        if @command_window.index != 1
          $game_system.se_play($data_system.buzzer_se)
          return
        end
      end
      case @command_window.index
      when 0
        $game_system.se_play($data_system.decision_se)
        deal_to_player
        @player[@index].stand = true if @player[@index].cards.size == 5
        @command_window.visible = false
      when 1
        $game_system.se_play($data_system.decision_se)
        @player[@index].stand = true
        switch_to_next_hand
        @command_window.visible = false
      when 2
        if @player.size > 1 || @player[@index].cards.size > 2 ||
            $game_variables[174] * 2 > $game_party.gold
          $game_system.se_play($data_system.buzzer_se)
          return
        end
        $game_variables[174] *= 2
        $game_system.se_play($data_system.decision_se)
        deal_to_player
        @player[@index].stand = true
        @command_window.visible = false
        refresh_bet
      when 3
        if @player.size >= 4 || @player[@index].cards.size > 2 ||
            @player[@index].cards[0].values != @player[@index].cards[1].values ||
            $game_party.gold < (@player.size + 1) * $game_variables[174]
          $game_system.se_play($data_system.buzzer_se)
          return
        end
        $game_system.se_play($data_system.decision_se)
        @player.insert(@index + 1, Hand.new)
        sprite = @player_sprites[@index].pop
        sprite.x = @player_sprites[@index][0].x
        sprite.dx = @player_sprites[@index][0].dx
        sprite.visible = false
        @player_sprites.insert(@index + 1, [sprite])
        @player[@index + 1].cards.push(@player[@index].cards.pop)
        deal_to_player
        refresh_bet
        refresh_hands
        setup_command_window
      end
    end
  end
  
  def setup_command_window
    @command_window.visible = true
    @command_window.refresh
    @command_window.index = 0
    if @player[@index].busted? || @player[@index].has_21? ||
        @player[@index].full?
      @command_window.disable_item(0)
      @command_window.index = 1
      @command_window.disable_item(2)
      @command_window.disable_item(3)
    else
      if @player.size > 1 || @player[@index].cards.size > 2 ||
          $game_variables[174] * 2 > $game_party.gold
        @command_window.disable_item(2)
      end
      if @player.size >= 4 || @player[@index].cards.size > 2 ||
          @player[@index].cards[0].values != @player[@index].cards[1].values ||
          $game_party.gold < (@player.size + 1) * $game_variables[174]
        @command_window.disable_item(3)
      end
    end
  end
    
  def switch_to_next_hand
    return if @index >= @player.size - 1
    @sprites -= @player_sprites[@index]
    @player_sprites[@index].each {|sprite| sprite.dispose}
    @index += 1
    @player_sprites[@index].each {|sprite| sprite.visible = true}
    deal_to_player
    refresh_hands
  end
  
  def shuffle_deck
    deck = CP::Cache::Cards.clone
    @deck = []
    while deck.size > 0
      i = rand(deck.size)
      @deck.push(deck[i])
      deck.delete_at(i)
    end
  end
  
  def finish_game
    @finished = true
    result = 0
    @player.each {|hand| result += (hand <=> @dealer)}
    if result == 0 || (result.abs * $game_variables[174]).to_i == 0
      $game_variables[175] = 0
      @backgrounds[2].bitmap.draw_text_outline(0, 20, 640, 40, 'Push!', 1)
    else
      $game_variables[174] = ($game_variables[174] * result.abs).to_i
      if result < 0
        $game_variables[175] = 1
        @backgrounds[2].bitmap.font.color = Color.new(255, 0, 0)
        @backgrounds[2].bitmap.draw_text_outline(0, 0, 640, 40, 'House wins!', 1)
        @backgrounds[2].bitmap.draw_text_outline(0, 40, 640, 40,
            "You lost #{$game_variables[174]} #{$data_system.words.gold}!", 1)
        $game_party.lose_gold($game_variables[174])
        $game_system.se_play($data_system.buzzer_se)
      else
        $game_variables[175] = 2
        @backgrounds[2].bitmap.font.color = Color.new(0, 255, 0)
        @backgrounds[2].bitmap.draw_text_outline(0, 0, 640, 40, 'House loses!', 1)
        @backgrounds[2].bitmap.draw_text_outline(0, 40, 640, 40,
            "You won #{$game_variables[174]} #{$data_system.words.gold}!", 1)
        $game_party.gain_gold($game_variables[174])
        $game_system.se_play($data_system.save_se)
      end
    end
  end
  
  def deal_to_dealer
    sprite = get_sprite(@dealer.cards)
    sprite.z = 300
    @dealer_sprites.push(sprite)
  end
  
  def deal_to_player
    sprite = get_sprite(@player[@index].cards)
    sprite.z = 100
    sprite.y += 240
    sprite.dy += 240
    @player_sprites[@index].push(sprite)
  end
  
  def get_sprite(cards)
    card = @deck.shift
    cards.push(card)
    sprite = Sprite_Card.new
    sprite.bitmap = CP::Cache.image(card)
    sprite.ox = sprite.bitmap.width / 2
    sprite.oy = sprite.bitmap.height / 2
    sprite.x, sprite.y = 320, -80
    sprite.dx = sprite.ox + (cards.size - 1) * 110 + 60
    sprite.dy = sprite.oy + 60
    @sprites.push(sprite)
    return sprite
  end
  
end
