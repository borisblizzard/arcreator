#==============================================================================
# Undynamic Day and Night System (UDNS) by Blizzard
# Version: 1.7b CP DX
# Date v1.0: 27.6.2006
# Date v1.1b: 29.6.2006
# Date v1.2b: 08.9.2006
# Date v1.3b: 11.9.2006
# Date v1.7b: 7.8.2007
#==============================================================================

#==============================================================================
# The configuration
#==============================================================================

DAY = 26
NIGHT = 27
INSIDE = 29
OUTSIDE = 28
INSIDEDARK = 32
DAY_V = 3
NIGHT_V = 4
DAY_L = 720
NIGHT_L = 720

#==============================================================================
# Game_System
#==============================================================================

class Game_System
  
  attr_accessor :ddns_off
  attr_accessor :day_count
  
  alias init initialize
  def initialize
    init
    @ddns_off, @day_count = true, 0
  end

end

#==============================================================================
# Game_DDNS
#==============================================================================

class Game_DDNS
  
  def go_inside
    unless $game_system.ddns_off
      $game_switches[INSIDE] = true
      $game_switches[INSIDEDARK] = false
      $game_switches[OUTSIDE] = false
    end
    return
  end
  
  def go_outside
    unless $game_system.ddns_off
      $game_switches[INSIDE] = false
      $game_switches[INSIDEDARK] = false
      $game_switches[OUTSIDE] = true
    end
    return
  end
  
  def go_inside_dark_place
    unless $game_system.ddns_off
      $game_switches[INSIDE] = false
      $game_switches[INSIDEDARK] = true
      $game_switches[OUTSIDE] = false
    end
    return
  end
  
  def turn_off
    $game_switches[INSIDE] = false
    $game_switches[INSIDEDARK] = false
    $game_switches[OUTSIDE] = false
    $game_system.ddns_off = true
    return
  end
  
  def turn_on
    $game_system.ddns_off = false
    return
  end
  
  def advance(hours)
    if $game_switches[DAY]
      $game_variables[DAY_V] += DAY_L * hours / 12
    elsif $game_switches[NIGHT]
      $game_variables[NIGHT_V] += NIGHT_L * hours / 12
    end
    return
  end
  
  def make_it_day
    $game_system.day_count += 1
    $game_variables[110] += 1
    $game_switches[198] = $game_switches[208] = false
    if $game_switches[INSIDE] || $game_switches[OUTSIDE] ||
       $game_switches[INSIDEDARK]
      $game_switches[DAY], $game_switches[NIGHT] = true, false
      $game_variables[DAY_V] = $game_variables[NIGHT_V] = 0
      if $game_switches[OUTSIDE]
        speed = ([28, 300].include?($game_map.map_id) ? 16 : 160)
        $game_screen.start_tone_change(Tone.new(0, 0, 0, 0), speed)
      end
    end
    $game_map.need_refresh = true
  end
  
  def make_it_night
    if $game_switches[INSIDE] || $game_switches[OUTSIDE] ||
       $game_switches[INSIDEDARK]
      $game_switches[DAY], $game_switches[NIGHT] = false, true
      $game_variables[DAY_V] = $game_variables[NIGHT_V] = 0
      if $game_switches[OUTSIDE]
        speed = ([28, 300].include?($game_map.map_id) ? 16 : 160)
        $game_screen.start_tone_change(Tone.new(-100, -100, 0, 50), speed)
      end
    end
    $game_map.need_refresh = true
  end
  
end

#==============================================================================
# Scene_Map
#==============================================================================

$game_ddns = Game_DDNS.new

class Scene_Map
  
  alias update_ddns_later update
  def update
    rate = ([28, 300].include?($game_map.map_id) ? 10 : 1)
    if @timer != 2 * rate * Graphics.frame_count / Graphics.frame_rate
      @timer = 2 * rate * Graphics.frame_count / Graphics.frame_rate
      unless $game_system.ddns_off
        if $game_switches[DAY]
          $game_variables[DAY_V] += 1
          $game_ddns.make_it_night if $game_variables[DAY_V] >= DAY_L
        elsif $game_switches[NIGHT]
          $game_variables[NIGHT_V] += 1
          $game_ddns.make_it_day if $game_variables[NIGHT_V] >= NIGHT_L
        end
      end
    end
    update_ddns_later
  end
  
  alias transfer_player_ddns_later transfer_player
  def transfer_player
    if $game_map.map_id != $game_temp.player_new_map_id
      if $game_switches[INSIDE]
        $game_screen.start_tone_change(Tone.new(0, 0, 0, 0), 0)
      elsif $game_switches[OUTSIDE]
        if $game_switches[DAY]
          $game_screen.start_tone_change(Tone.new(0, 0, 0, 0), 0)
        elsif $game_switches[NIGHT]
          $game_screen.start_tone_change(Tone.new(-100, -100, 0, 50), 0)
        end
      elsif $game_switches[INSIDEDARK]
        $game_screen.start_tone_change(Tone.new(-40, -40, -40, 0), 0)
      end
    end
    rate = ([28, 300].include?($game_map.map_id) ? 10 : 1)
    @timer = 2 * rate * Graphics.frame_count / Graphics.frame_rate
    transfer_player_ddns_later
  end
  
end
