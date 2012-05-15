#==============================================================================
# Monster
#==============================================================================

class Monster
  
  attr_accessor :character_name
  attr_accessor :name
  attr_accessor :health
  attr_accessor :obey
  attr_accessor :fights
  attr_accessor :won
  attr_accessor :critical
  attr_accessor :restorative
  attr_reader   :id
  attr_reader   :hp
  attr_reader   :exp
  attr_reader   :rate
  attr_reader   :own
  attr_reader   :character_hue
  attr_reader   :hp_stim
  attr_reader   :power_stim
  attr_reader   :aggressive_stim
  attr_reader   :speed_stim
  attr_reader   :obey_stim
  attr_accessor :damage
  
  def initialize(id = 1)
    @won = @hp_stim = @power_stim = @aggressive_stim = @speed_stim = @obey_stim =
        @character_hue = @power_plus = @aggressive_plus = @speed_plus = 0
    @rate = 1.0
    @damage = nil
    @critical = false
    @restorative = false
    @obey = 0
    id == 0 ? init_own_monster : database(id)
    @hp = @health
  end
  
  def generate_stats(average)
    @health = average + 80 + rand(41)
    @power = average - 2 + rand(5)
    @aggressive = average - 2 + rand(5)
    @speed = average - 2 + rand(5)
    @obey = average / 2 - 1 + rand(3)
  end
  
  def init_own_monster
    @id = 0
    @name = ''
    @health = 200
    @power = 10
    @aggressive = 10
    @speed = 10
    @obey = 10
    @exp = @fights = 0
    @character_name = ''
    @own = true
  end
  
  def hp=(hp)
    @hp = (hp < 0 ? 0 : (hp > @health ? @health : hp))
  end
    
  def training(kind)
    case kind
    when 0 then self.hp_stim += $game_variables[14] * 4 / ((@health / 15) ** 2)
    when 1 then self.power_stim += $game_variables[14] * 4 / (@power ** 2)
    when 2 then self.aggressive_stim += $game_variables[14] * 4 / (@aggressive ** 2)
    when 3 then self.speed_stim += $game_variables[14] * 4 / (@speed ** 2)
    when 4 then self.obey_stim += $game_variables[14] * 4 / (@obey ** 2)
    end  
    return stat_increase(kind)
  end
  
  def can_attack?(enemy)
    if self.aggressive > enemy.speed
      chance = 90 + ((self.aggressive.to_f / enemy.speed - 1) * 10).to_i
      chance = 100 if chance > 100
    else
      chance = self.aggressive * 90 / enemy.speed
      chance = 80 if chance < 80
    end
    return (rand(100) < chance)
  end
  
  def attack(enemy)
    @critical = false
    if enemy.aggressive > self.speed
      chance = 90 + ((enemy.aggressive.to_f / self.speed - 1) * 10).to_i
    else
      chance = enemy.aggressive * 90 / self.speed
      chance = 70 if chance < 70
    end
    hit = (rand(100) < chance)
    if hit
      base = 5 + ((enemy.power * 0.7 + enemy.aggressive * 0.4) ** 1.5 / (self.speed ** 1.2)).round
      damage = base + enemy.power / 2 + rand((enemy.power * 1.5).to_i)
      damage = 1 if damage < 1
      if rand(100) < enemy.aggressive * 10 / self.aggressive
        damage *= 2
        enemy.aggressive_stim += 1
        @critical = true
      end
      self.damage = damage
      self.hp -= self.damage
      self.hp_stim += self.damage * 20 / self.health
      power_plus = self.health / (self.damage * 20)
      power_plus = 1 if power_plus < 1
      enemy.power_stim += power_plus
      enemy.aggressive_stim += 1
      reset_stats
    else
      self.damage = 'Missed'
    end
    self.speed_stim += 1
    @restorative = false
  end
  
  def command(kinds)
    return false if self.damage != nil
    success = false
    kinds.each {|kind|
        chance = Math.sqrt(self.obey.to_f / self.aggressive) * (rand(6) + 5)
        if (rand(100) < chance.to_i)
          self.damage = '' if self.damage == nil
          success = true
          plus = rand(2) + 1
          case kind
          when 0
            if @power_plus == 0
              @power_plus = plus
            else
              plus = 1
              @power_plus += plus
            end
            self.power_stim += 1 if rand(10) == 0
            self.damage += 'P'
          when 1
            if @aggressive_plus == 0
              @aggressive_plus = plus
            else
              plus = 1
              @aggressive_plus += plus
            end
            self.aggressive_stim += 1 if rand(10) == 0
            self.damage += 'A'
          when 2
            if @speed_plus == 0
              @speed_plus = plus
            else
              plus = 1
              @speed_plus += plus
            end
            self.speed_stim += 1 if rand(10) == 0
            self.damage += 'S'
          end
          self.obey_stim += 1
        end}
    @restorative = true
    if success
      self.damage += '+'
      return true
    end
    return false
  end
  
  def power
    return (@power + @power_plus)
  end
  
  def aggressive
    return (@aggressive + @aggressive_plus)
  end
  
  def speed
    return (@speed + @speed_plus)
  end
  
  def power=(pow)
    @power = pow - @power_plus
  end
  
  def aggressive=(ag)
    @aggressive = ag - @aggressive_plus
  end
  
  def speed=(agi)
    @speed = agi - @speed_plus
  end
  
  def reset_stats
    @power_plus = 0 if rand(100) < 75
    @aggressive_plus = 0 if rand(100) < 75
    @speed_plus = 0 if rand(100) < 75
  end
    
  def dead?
    return (self.hp == 0)
  end
  
  def fight_end
    result = false
    if @own
      reset_stats
      (0...5).each {|i| result |= stat_increase(i)}
      add_exp(5 + rand(6))
      if @hp > 0
        add_exp(@health / 20)
        add_exp(rand(@health / 40)) if @health >= 40
      else
        add_exp(@health / 100)
        add_exp(rand(@health / 200)) if @health >= 200
      end
    end
    @hp = @health
    return result
  end
  
  def stat_increase(kind)
    case kind
    when 0
      if self.hp_stim >= 15 && rand(@hp_stim) >= 10
        @health += self.hp_stim * 10 / 15 + rand(41)
        @hp_stim = 0
        return true
      end
    when 1
      if self.power_stim >= 15 && rand(@power_stim) >= 10
        @power += self.power_stim / 15 + rand(2)
        @power_stim = 0
        return true
      end
    when 2
      if self.aggressive_stim >= 15 && rand(@aggressive_stim) >= 10
        @aggressive += self.aggressive_stim / 15 + rand(2)
        @aggressive_stim = 0
        return true
      end
    when 3
      if self.speed_stim >= 15 && rand(@speed_stim) >= 10
        @speed += self.speed_stim / 15 + rand(2)
        @speed_stim = 0
        return true
      end
    when 4
      if self.obey_stim >= 20 && rand(@obey_stim) >= 10
        @obey += 1 + rand(2)
        @obey_stim = 0
        return true
      end
    end
    return false
  end
  
  def add_exp(add_value)
    exp = add_value
    @exp += exp if exp > 0 && rand(4) > 1
  end
  
  def hp_stim=(val)
    add_exp(val - @hp_stim)
    @hp_stim = val
  end
  
  def power_stim=(val)
    add_exp(val - @power_stim)
    @power_stim = val
  end
  
  def aggressive_stim=(val)
    add_exp(val - @aggressive_stim)
    @aggressive_stim = val
  end
  
  def speed_stim=(val)
    add_exp(val - @speed_stim)
    @speed_stim = val
  end
  
  def obey_stim=(val)
    add_exp(val - @obey_stim)
    @obey_stim = val
  end
  
end

#==============================================================================
# Game_Party
#==============================================================================

class Game_Party
  
  attr_accessor :monster
  
end

#==============================================================================
# Game_System
#==============================================================================

class Game_System
  
  attr_accessor :monster
  
  alias init_monster_later initialize
  def initialize
    init_monster_later
    @monster = [false, Monster.new(-1), Monster.new(-1)]
  end
  
  def make_monster_order(range)
    ran = randomize_monsters(range.to_a)
    monsters = []
    (0...4).each {|i| monsters.push(Monster.new(ran[i]))}
    $game_variables[19] = monsters
  end
  
  def randomize_monsters(range)
    ran1 = rand(range.size) + range.min
    ran2 = (range - [ran1])[rand(range.size - 1)]
    ran3 = (range - [ran1, ran2])[rand(range.size - 2)]
    ran4 = (range - [ran1, ran2, ran3])[rand(range.size - 3)]
    return [ran1, ran2, ran3, ran4]
  end
  
  def make_fights
    monsters = $game_variables[19]
    $game_variables[5] = "#{monsters[0].name} VS. #{monsters[1].name}"
    $game_variables[9] = "(#{monsters[0].rate}:1  OR  #{monsters[1].rate}:1)"
    $game_variables[10] = "#{monsters[2].name} VS. #{monsters[3].name}"
    $game_variables[12] = "(#{monsters[2].rate}:1  OR  #{monsters[3].rate}:1)"
  end
  
  def make_names
    monsters = $game_variables[19]
    (0...4).each {|i|
        j = (i == 0 ? 5 : (i == 1 ? 9 : (i == 2 ? 10 : 12)))
        $game_variables[j] = "#{monsters[i].name}  (#{monsters[i].rate.to_s}:1)"}
  end
  
end

#==============================================================================
# Sprite_Health
#==============================================================================

class Sprite_Health < Sprite
  
  def initialize(monster, viewport = nil)
    super(viewport)
    @monster = monster
    self.bitmap = Bitmap.new(80, 16)
    self.ox, self.oy = 40, 136
    redraw
  end
  
  def redraw
    self.bitmap.clear
    rate = @monster.hp.to_f / @monster.health
    width1 = (76 * rate + 2).to_i
    width2 = 80 - width1
    if rate > 0.6
      full_bitmap = RPG::Cache.picture('health1')
    elsif rate > 0.2
      full_bitmap = RPG::Cache.picture('health2')
    else
      full_bitmap = RPG::Cache.picture('health3')
    end
    self.bitmap.blt(0, 0, full_bitmap, Rect.new(0, 0, width1, 16))
    empty_bitmap = RPG::Cache.picture('health0')
    self.bitmap.blt(width1, 0, empty_bitmap, Rect.new(width1, 0, width2, 16))
  end
  
end

#==============================================================================
# Scene_Map
#==============================================================================

class Scene_Map
  
  alias upd_monster_later update
  def update
    if $game_system.monster[0]
      if @monster1_sprite == nil
        @spriteset.character_sprites.each {|sprite|
            if sprite.character.name == 'Monster 1'
              @monster1_sprite = sprite.sprite
              @monster1_character = sprite.character
            elsif sprite.character.name == 'Monster 2'
              @monster2_sprite = sprite.sprite
              @monster2_character = sprite.character
            end}
        @health1_sprite = Sprite_Health.new($game_system.monster[1])
        @health2_sprite = Sprite_Health.new($game_system.monster[2])
        @health1_sprite.x = @monster1_sprite.x
        @health1_sprite.y = @monster1_sprite.y
        @health2_sprite.x = @monster2_sprite.x
        @health2_sprite.y = @monster2_sprite.y
      end
      if !$game_system.monster[1].dead? && !$game_system.monster[2].dead? &&
          $game_system.monster[1].damage == nil &&
          $game_system.monster[2].damage == nil &&
          ($game_system.monster[1] == $game_party.monster &&
          !@monster1_character.moving? ||
          $game_system.monster[2] == $game_party.monster &&
          !@monster2_character.moving?)
        kinds = []
        kinds.push(1) if Input.trigger?($controls.left)
        kinds.push(0) if Input.trigger?($controls.confirm)
        kinds.push(2) if Input.trigger?($controls.right)
        $game_party.monster.command(kinds) if kinds.size > 0
      end
      damage = false
      if $game_system.monster[1].damage != nil
        @health1_sprite.redraw if $game_system.monster[1].damage.is_a?(Numeric)
        create_damage_display($game_system.monster[1], @monster1_sprite)
      end
      if $game_system.monster[2].damage != nil
        @health2_sprite.redraw if $game_system.monster[2].damage.is_a?(Numeric)
        create_damage_display($game_system.monster[2], @monster2_sprite)
      end
    elsif $game_system.monster[1].id == -1 && $game_system.monster[2].id == -1
      if @monster1_sprite != nil
        @monster1_sprite = @monster2_sprite = nil
        @monster1_character = @monster2_character = nil
        @health1_sprite.dispose
        @health2_sprite.dispose
        @health1_sprite = @health2_sprite = nil
      end
    end
    upd_monster_later
  end
  
  def create_damage_display(monster, sprite)
    sprite.damage(monster.damage, monster.critical, monster.restorative, false)
    monster.damage = nil
    monster.critical = false
    monster.restorative = false
  end
      
end
