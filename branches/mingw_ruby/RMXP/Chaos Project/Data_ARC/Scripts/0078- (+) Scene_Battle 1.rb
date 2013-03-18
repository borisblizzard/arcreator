#==============================================================================
# Scene_Battle (1)
#==============================================================================

class Scene_Battle
  
  attr_accessor :spriteset
  attr_accessor :sprites
  attr_reader   :status_window
  
  def return_in_time
    return if @time.size < 2
    @time.pop
    $game_party, $game_troop = @time[@time.size - 1]
    @time.pop
    $game_party.apply
    $game_troop.apply
    @spriteset.refresh
  end
  
  def save_time
    party = $game_party.clone
    troop = $game_troop.clone
    party.save
    troop.save
    @time.push([party, troop])
    @time.shift if @time.size > 5
  end
  
  def main
    $game_screen.start_shake(0, 0, 0)
    $game_screen.update
    @time = []
    @uf_overload = 0
    @disrupted_texts = []
    if $game_map.map_id == 106 && @sprites != nil
      $game_screen.start_tone_change(Tone.new(0, 0, 0, 0), 0)
    end
    @last_actions = []
    $game_party.actors.size.times {@last_actions.push(Game_BattleAction.new)}
    $game_party.actors.each {|actor|
        actor.sr = actor.sr
        actor.damage = nil
        actor.damage_pop = false
        actor.update_auto_state}
    @levels = []
    @select_type = true
    $game_party.actors.each {|actor| @levels.push([actor.level, actor.all_exp])}
    $game_temp.in_battle = true
    $game_temp.battle_turn = 0
    $game_temp.battle_event_flags.clear
    $game_temp.battle_abort = $game_temp.battle_main_phase = false
    $game_temp.battleback_name = $game_map.battleback_name
    $game_temp.forcing_battler = nil
    $game_system.battle_interpreter.setup(nil, 0)
    @troop_id = $game_temp.battle_troop_id
    $game_troop.setup(@troop_id)
    case @troop_id
    when 149 then $game_variables[25] = 1
    when 157, 200 then $game_troop.enemies[0].hp = $game_troop.enemies[2].hp = 0
    when 182 then $game_troop.enemies[0].disappear = true
    end
    save_time
    @help_window = Window_Help.new
    @help_window.back_opacity = 160
    @help_window.z = 10000
    @help_window.visible = false
    @actor_arrows, @enemy_arrows = [], []
    @ability_command_windows = []
    $game_party.actors.each_index {|i|
        win = Menu_AbilityCommand.new($game_party.actors[i])
        win.help_window = @help_window
        win.reset
        case $game_party.actors.size
        when 1 then win.x, win.ox = 320, 0
        when 2 then win.x, win.ox = 220 + i*200, 60 - i*120
        when 3 then win.x, win.ox = 220 + i*100, 60 - i*60
        when 4
          if i < 2
            win.x, win.ox = 160 + i*120, 80 - i*40
          else
            win.x, win.ox = 360 + (i-2)*120, (1-i)*40
          end
        end
        @ability_command_windows.push(win)}
    @actor_command_window = Menu_ActorBattle.new
    @actor_command_window.help_window = @help_window
    @party_command_window = Menu_PartyCommand.new
    @party_command_window.help_window = @help_window
    @status_window = Window_BattleStatus.new
    @message_window = Window_Message.new
    @spriteset = Spriteset_Battle.new
    @wait_count = 0
    if @sprites == nil && $battle_sprite == nil
      $data_system.battle_transition = case rand(7)
      when 0 then 'Blurification'
      when 1 then 'Electro'
      when 2 then 'Doted'
      when 3 then 'Twirl'
      when 4 then 'Perl'
      when 5 then 'Tunnel'
      when 6 then 'Darkspace'
      end
      if $game_system.playing_bgm != $game_system.battle_bgm &&
          $game_system.battle_bgm.name != ''
        $game_system.bgm_play($game_system.battle_bgm)
      end
      unless $game_system.battle_bgm.name == 'Astral Projection - Chaos ' +
          '(Bizzare Contact RMX, Blizzard Mix for CP)' ||
          $game_system.battle_bgm.name ==  'Astral Projection - Nilaya ' +
        '(Melicia RMX, Blizzard Mix for CP)'
        $game_system.se_play($data_system.battle_start_se)
      end
      $game_system.bgs_memorize
      Audio.bgs_stop
      if $data_system.battle_transition == ''
        Graphics.transition(45)
      else
        Graphics.transition(45, 'Graphics/Transitions/' +
          $data_system.battle_transition)
      end
    else
      if $battle_sprite == nil
        Graphics.transition(0)
        $game_system.bgs_memorize
        Audio.bgs_stop
        if $game_system.playing_bgm != $game_system.battle_bgm &&
            $game_system.battle_bgm.name != ''
          $game_system.bgm_play($game_system.battle_bgm)
        end
        animate_breaking_screen
      elsif !$no_transit
        sprite = Sprite.new
        sprite.bitmap = Bitmap.new(640, 480)
        sprite.bitmap.fill_rect(0, 0, 640, 480, Color.new(0, 0, 0))
        sprite.z = 900000
        $battle_sprite.bitmap = RPG::Cache.battleback($game_temp.battleback_name)
        $battle_sprite.zoom_y *= 1.5
        zoom = $battle_sprite.zoom_x - 1
        $battle_sprite.visible = true
        $battle_sprite.opacity = 0
        $battle_sprite.oy = 160
        $battle_sprite.blend_type = 0
        $battle_sprite.z = 1000000
        $game_system.bgs_memorize
        Audio.bgs_stop
        if $game_system.playing_bgm != $game_system.battle_bgm &&
            $game_system.battle_bgm.name != ''
          $game_system.bgm_play($game_system.battle_bgm)
        end
        Graphics.transition(0)
        (0...32).each {|i|
            $battle_sprite.zoom_y = 1 + (39 - i) * zoom / 40
            $battle_sprite.zoom_x = 1 + (39 - i) * zoom / 40
            $battle_sprite.y -= 2
            $battle_sprite.opacity += 8
            Graphics.update}
        sprite.dispose
        sprite = nil
        (32...39).each {|i|
            $battle_sprite.zoom_y = 1 + (39 - i) * zoom / 40
            $battle_sprite.zoom_x = 1 + (39 - i) * zoom / 40
            $battle_sprite.y -= 2
            Graphics.update}
        $battle_sprite.dispose
        $battle_sprite = nil
        Graphics.update
      else
        $battle_sprite.dispose
        $battle_sprite = nil
        Graphics.transition(20)
      end
    end
    $no_transit = nil
    if CP::Cache::MainParty.any? {|i|
        $game_party.actors.include?($game_actors[i])}
      $game_system.fights += 1
    end
    start_phase1
    loop do
      Graphics.update
      Input.update
      update
      break if $scene != self
    end
    $game_map.refresh
    Graphics.freeze
    $game_temp.trance = nil
    $game_system.get_cam
    ([@actor_command_window, @party_command_window, @rage_command_window,
        @help_window, @status_window, @message_window, @uf_window,
        @skill_window, @item_window, @result_window, @spriteset] +
        @ability_command_windows).each {|object|
            object.dispose unless object == nil}
    if $scene.is_a?(Scene_Title)
      Graphics.transition
      Graphics.freeze
    end
  end
  
  def animate_breaking_screen
    sqrt2 = Math.sqrt(2)
    $game_system.se_play(RPG::AudioFile.new('glass', 90, 100))
    (-10...35).each {|j| @sprites.each_index {|i|
          next if @sprites[i] == nil
          @sprites[i][0].x += i/15 - 10
          @sprites[i][0].y += i%15 + j
          case @sprites[i][1]
          when 0 then @sprites[i][0].zoom_x -= 0.02
          when 1 then @sprites[i][0].zoom_y -= 0.02
          when 2
            @sprites[i][0].zoom_y -= 0.02
            @sprites[i][0].zoom_x -= 0.02
          when 4 then @sprites[i][0].zoom_x += 0.03
          when 3 then @sprites[i][0].zoom_y += 0.03
          when 5
            @sprites[i][0].zoom_x += 0.03
            @sprites[i][0].zoom_y += 0.03
          end
          case @sprites[i][2]
          when 0 then @sprites[i][0].angle += 5
          when 1 then @sprites[i][0].angle += 10
          when 2 then @sprites[i][0].angle += 12
          when 3 then @sprites[i][0].angle += 30
          end
          if @sprites[i][0].zoom_x > @sprites[i][0].zoom_y
            zoom = @sprites[i][0].zoom_x
          else
            zoom = @sprites[i][0].zoom_y
          end
          if @sprites[i][0].x + sqrt2 * 32 * zoom < 0 ||
              @sprites[i][0].x - sqrt2 * 32 * zoom > 640 ||
              @sprites[i][0].y - sqrt2 * 32 * zoom > 480
            @sprites[i][0].dispose
            @sprites[i] = nil
          end}
        @spriteset.update_panorama
        Graphics.update}
    @sprites.compact.each{|sprite| sprite[0].dispose}
    @sprites = nil
  end
  
  def judge
    $game_party.actors.each_index {|i|
        actor = $game_party.actors[i]
        if $game_party.actors[i].states.include?(32) && $game_party.actors[i].dead?
          $game_party.actors[i].hp += $game_party.actors[i].maxhp / 5
          $game_party.actors[i].remove_state(1)
          $game_party.actors[i].remove_state(32)
          $game_party.actors[i].animation_id = 25
          $game_party.actors[i].restorative = true
          $game_party.actors[i].damage = 'Auto-Revive!'
          $game_party.actors[i].damage_pop = true
          @status_window.refresh
        end}
    if $game_party.all_dead? || $game_party.actors.size == 0
      if $game_temp.battle_can_lose
        $game_system.bgm_play($game_temp.map_bgm)
        battle_end(2)
        return true
      end
      $game_temp.gameover = true
      return true
    end
    $game_troop.enemies.each {|enemy| return false if enemy.exist?}
    start_phase5
    return true
  end
  
  def battle_end(result)
    $game_party.gold_factor = $game_party.item_factor = 1
    $game_temp.in_battle = false
    $game_party.clear_actions
    $game_party.actors.each {|actor|
        actor.remove_states_battle
        actor.blink = false}
    $game_troop.enemies.clear
    if $game_temp.battle_proc != nil
      $game_temp.battle_proc.call(result)
      $game_temp.battle_proc = nil
    end
    $scene = Scene_Map.new
    $game_system.bgs_restore
  end
  
  def setup_battle_event
    return if $game_system.battle_interpreter.running?
    $data_troops[@troop_id].pages.each_index {|index|
        page = $data_troops[@troop_id].pages[index]
        c = page.condition
        next unless c.turn_valid || c.enemy_valid || c.actor_valid || c.switch_valid
        next if $game_temp.battle_event_flags[index]
        if c.turn_valid
          n = $game_temp.battle_turn
          a = c.turn_a
          b = c.turn_b
          next if (b == 0 && n != a) || (b > 0 && (n < 1 || n < a || n % b != a % b))
        end
        if c.enemy_valid
          enemy = $game_troop.enemies[c.enemy_index]
          next if enemy == nil || enemy.hp * 100.0 / enemy.maxhp > c.enemy_hp
        end
        if c.actor_valid
          actor = $game_actors[c.actor_id]
          next if actor == nil || actor.hp * 100.0 / actor.maxhp > c.actor_hp
        end
        next if c.switch_valid && $game_switches[c.switch_id] == false
        $game_system.battle_interpreter.setup(page.list, 0)
        $game_temp.battle_event_flags[index] = true if page.span <= 1
        return}
  end
  
  def update
    if $game_system.battle_interpreter.running?
      $game_system.battle_interpreter.update
      unless $game_temp.forcing_battler != nil ||
          $game_system.battle_interpreter.running? || judge
        setup_battle_event
      end
    end
    $game_system.update
    $game_screen.update
    if $game_system.timer_working && $game_system.timer == 0
      $game_temp.battle_abort = true
    end
    @help_window.update
    @party_command_window.update
    @actor_command_window.update
    @ability_command_windows.each {|win| win.update if win != nil}
    @status_window.update
    @message_window.update
    @spriteset.update if $scene.is_a?(Scene_Battle)
    if $game_temp.transition_processing
      $game_temp.transition_processing = false
      if $game_temp.transition_name == ''
        Graphics.transition(20)
      else
        Graphics.transition(40, 'Graphics/Transitions/' +
            $game_temp.transition_name)
      end
    end
    return if $game_temp.message_window_showing || @spriteset.effect?
    if $game_temp.gameover
      $scene = Scene_Gameover.new
    elsif $game_temp.to_title
      $scene = Scene_Title.new
    elsif $game_temp.battle_abort
      @levels.each_index {|i|
          $game_party.actors[i].level = @levels[i][0]
          $game_party.actors[i].all_exp = @levels[i][1]}
      $game_system.bgm_play($game_temp.map_bgm)
      battle_end(1)
    elsif @wait_count > 0
      @wait_count -= 1
    elsif $game_temp.forcing_battler != nil ||
        !$game_system.battle_interpreter.running?
      case @phase
      when 1 then update_phase1
      when 2 then update_phase2
      when 3 then update_phase3
      when 4 then update_phase4
      when 5 then update_phase5
      when 6 then update_phase6
      when 7 then update_phase7
      end
    end
  end
  
  def get_valid_enemies
    return $game_troop.enemies.find_all {|enemy| enemy.exist?}
  end
  
end
