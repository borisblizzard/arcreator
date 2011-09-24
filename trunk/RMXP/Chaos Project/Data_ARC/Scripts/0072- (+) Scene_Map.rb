#==============================================================================
# Scene_Map
#==============================================================================

class Scene_Map
  
  attr_accessor :spriteset
  attr_writer   :special_fix
  
  def main
    $game_party.actors.each {|actor| actor.exp_factor = 100000}
    if $game_temp.player_transferring
      transfer_player
      $game_screen.start_shake(0, 0, 0)
      $game_screen.update
      @spriteset.update
    else
      @spriteset = Spriteset_Map.new
    end
    @message_window = Window_Message.new
    Graphics.transition
    loop do
      Graphics.update
      Input.update
      update
      break if $scene != self && !$game_temp.message_window_showing
    end
    if $scene.is_a?(Scene_Battle)
      if $game_switches[394]
        transpose
      else
        $game_switches[190] ? call_fade_boss : call_fade
      end
    else
      Graphics.freeze
      @spriteset.dispose
      @message_window.dispose
      unless $scene.is_a?(Scene_Gameover)
        Graphics.transition
        Graphics.freeze
      end
    end
    if @special_fix == 0
      (8..9).each {|i| $game_map.events[i].erase}
    elsif @special_fix == 1
      (10..13).each {|i| $game_map.events[i].erase}
    elsif @special_fix == 2
      (2..3).each {|i| $game_map.events[i].erase}
    end
  end
  
  def transpose(frames=120, max_zoom=100, times=8)
    $game_switches[394] = false
    @spriteset.dispose
    max_zoom -= 1 # difference b/w zooms
    max_zoom = max_zoom.to_f / frames / times # unit zoom
    unit_opacity = (255.0 / frames).ceil
    spr_opacity = (255.0 * times / 2 / frames).ceil
    @sprite = Sprite.new
    @sprite.bitmap = CP.break_screen
    @sprites = []
    @sprites2 = []
    (0...(times * 3 / 2)).each {|i|
        s = Sprite.new
        s.x, s.y, s.ox, s.oy = 320, 240, 320, 240
        s.bitmap = @sprite.bitmap
        s.blend_type = 1
        s.opacity = 128
        s.visible = false
        s.zoom_x = s.zoom_y = 1 + i * 0.05
        @sprites.push(s)
        s = Sprite.new
        s.x, s.y, s.ox, s.oy = 320, 240, 320, 240
        s.bitmap = @sprite.bitmap
        s.blend_type = 1
        s.opacity = 128
        s.visible = false
        s.zoom_x = s.zoom_y = 1 - i * 0.05
        @sprites2.push(s)}
    count = 0
    loop {
        @sprites[count].visible = true
        @sprites2[count].visible = true
        if count < times * 3 / 2 - 1
          $game_system.se_play(RPG::AudioFile.new('138-Darkness01', 90, 150))
          count += 1
        end
        (frames / times / 2).times {
            @sprites.each {|s|
                break if !s.visible
                s.zoom_x += max_zoom
                s.zoom_y += max_zoom
                s.opacity -= spr_opacity}
            @sprites2.each {|s|
                break if !s.visible
                s.zoom_x -= max_zoom
                s.zoom_y -= max_zoom
                s.opacity -= spr_opacity}
            @sprite.opacity -= unit_opacity
        Graphics.update}
        break if @sprite.opacity == 0}
    $battle_sprite = @sprites[0]
    @sprites.delete_at(0)
    @sprites.each {|s| s.dispose}
    @sprite.bitmap.dispose
    @sprite.dispose
  end
  
  def update
    if $game_temp.battle_calling[0] && !$game_temp.battle_calling[1]
      @battle_window.update
      if @battle_window.mode == 4
        call_battle_data
      elsif @battle_window.mode == 3
        call_not_battle unless @battle_window.fade_out
        @battle_window.fade_out = true
      end
      return
    end
    @battle_window.mode = -1 if @battle_window.mode == 3
    loop do
      $game_system.map_interpreter.update
      $game_map.update
      $game_player.update
      $game_system.update
      $game_screen.update
      break unless $game_temp.player_transferring
      transfer_player
      break if $game_temp.transition_processing
    end
    @spriteset.update
    @message_window.update
    if $game_temp.gameover
      $scene = Scene_Gameover.new
      return
    end
    if $game_temp.to_title
      $scene = Scene_Title.new
      return
    end
    if $game_temp.transition_processing
      $game_temp.transition_processing = false
      if $game_temp.transition_name == ''
        if $game_variables[104] > 0
          Graphics.transition($game_variables[104])
          $game_variables[104] = 0
        else
          Graphics.transition(20)
        end
      else
        if $game_variables[104] > 0
          Graphics.transition($game_variables[104], 'Graphics/Transitions/' + 
              $game_temp.transition_name)
          $game_variables[104] = 0
        else
          Graphics.transition(40, 'Graphics/Transitions/' + 
              $game_temp.transition_name)
        end
      end
    end
    return if $game_temp.message_window_showing
    $game_system.message_walking = true
    if $game_player.encounter_count == 0 && $game_map.encounter_list.size > 0
      unless $game_system.map_interpreter.running? ||
             $game_system.encounter_disabled
        $game_temp.battle_calling = [true, false]
      end
    end
    if Input.trigger?($controls.menu)
      unless $game_system.map_interpreter.running? ||
             $game_system.menu_disabled || $game_switches[167]
        $game_temp.menu_calling = true
        $game_temp.menu_beep = true
      end
    end
    update_calling
  end
  
  def update_calling
    unless $game_player.moving?
      if $game_temp.battle_calling[1]
        call_battle
      elsif !$game_temp.battle_calling[0]
        if $game_temp.shop_calling
          call_shop
        elsif $game_temp.name_calling
          call_name
        elsif $game_temp.menu_calling
          call_menu
        elsif $game_temp.save_calling
          call_save
        end
      end
    end
  end
  
  def call_not_battle
    $game_player.make_encounter_count
    $game_player.straighten
  end
    
  def call_battle_data
    list = CP.alter_encouter_list($game_map.encounter_list)
    n = rand(list.size)
    troop_id = list[n]
    if $data_troops[troop_id] != nil
      $game_temp.battle_troop_id = troop_id
      $game_temp.battle_can_escape = true
      $game_temp.battle_can_lose = false
      $game_temp.battle_proc = nil
    end
    $game_player.straighten
    call_battle
  end
  
  def call_battle
    $game_temp.battle_calling = [false, false]
    $game_temp.menu_calling = false
    $game_temp.menu_beep = false
    $game_player.make_encounter_count
    if $game_system.playing_bgm != $game_system.battle_bgm
      $game_temp.map_bgm = $game_system.playing_bgm
    end
    $game_player.straighten
    $scene = Scene_Battle.new
  end
  
  def call_shop
    $game_temp.shop_calling = false
    $game_player.straighten
    $scene = Scene_Shop.new
  end
  
  def call_name
    $game_temp.name_calling = false
    $game_player.straighten
    $scene = Scene_Name.new
  end
  
  def call_menu
    $game_temp.menu_calling = false
    if $game_temp.menu_beep
      $game_system.se_play($data_system.decision_se)
      $game_temp.menu_beep = false
    end
    $game_player.straighten
    $scene = Scene_Menu.new
  end
  
  def call_save
    $game_player.straighten
    $scene = Scene_Save.new
  end
  
  def transfer_player
    if $ice_temple_flag
      $game_switches[163] = true
      $ice_temple_flag = nil
    end
    $game_temp.player_transferring = false
    @spriteset.dispose unless @spriteset == nil
    if $game_temp.transition_processing
      load_sprite = Sprite.new
      load_sprite.bitmap = Bitmap.new(640, 480)
      load_sprite.z = 10000
      text = 'Loading...'
      Graphics.transition
      load_sprite.bitmap.draw_text_shaded(484, 452, 152, 24, text, 2)
      Graphics.freeze
    end
    old_id = $game_map.map_id
    if $game_map.map_id != $game_temp.player_new_map_id ||
        CP::Cache::ResetMaps.include?($game_temp.player_new_map_id) ||
        $game_switches[329]
      $game_map.setup($game_temp.player_new_map_id)
      $game_system.name_timer = 100
    end
    @id = $game_map.map_id
    if CP::Cache::DirectFadeMaps.include?(old_id) &&
        CP::Cache::DirectFadeMaps.include?(@id)
      $game_player.move_caterpillar($game_temp.player_new_x, $game_temp.player_new_y)
    else
      $game_player.moveto($game_temp.player_new_x, $game_temp.player_new_y)
      case $game_temp.player_new_direction
      when 2
        $game_player.turn_down
        $game_player.members.each {|member| member.turn_down}
      when 4
        $game_player.turn_left
        $game_player.members.each {|member| member.turn_left}
      when 6
        $game_player.turn_right
        $game_player.members.each {|member| member.turn_right}
      when 8
        $game_player.turn_up
        $game_player.members.each {|member| member.turn_up}
      else
        case $game_player.direction
        when 2 then $game_player.members.each {|member| member.turn_down}
        when 4 then $game_player.members.each {|member| member.turn_left}
        when 6 then $game_player.members.each {|member| member.turn_right}
        when 8 then $game_player.members.each {|member| member.turn_up}
        end
      end
    end
    $game_player.straighten
    $game_map.update
    remove_points
    @spriteset = Spriteset_Map.new
    if $game_temp.transition_processing
      Graphics.transition(0)
      load_sprite.bitmap.fill_rect(0, 0, 640, 480, Color.new(0, 0, 0))
      Graphics.freeze
      load_sprite.dispose
      Graphics.transition
    end
    $game_screen.start_shake(0, 0, 0)
    $game_screen.update
    @spriteset.update
    $game_temp.transition_processing = false
    $game_map.autoplay
    Graphics.frame_reset
    Input.update
  end
  
  def call_fade
    type = rand(8)
    if type < 4
      data = []
      sprites = []
      (0...15).each {|j| (0...20).each {|i|
          data.push(i + j*20)
          sprite = Sprite.new(@spriteset.viewport4)
          sprite.bitmap = Bitmap.new(32, 32)
          sprite.bitmap.fill_rect(0, 0, 32, 32, Color.new(0, 0, 0))
          sprite.x, sprite.y, sprite.z, sprite.opacity = i * 32, j * 32, 900, 0
          sprite.tone = $game_screen.tone
          sprites.push(sprite)}}
    else
      trans = case type
      when 4 then 'Graphics/Transitions/Teleport'
      when 5 then 'Graphics/Transitions/Vertical'
      when 6 then 'Graphics/Transitions/Downfall'
      when 7 then 'Graphics/Transitions/Worldmap'
      end
    end
    case type
    when 0
      (0...50).each {|i| (0...6).each {|j|
            index = data[rand(data.size)]
            tile = sprites[index].opacity = 255
            data.delete(index)}
        Graphics.update}
      2.times {Graphics.update}
      Graphics.freeze
      (sprites + [@spriteset, @message_window]).each {|sprite| sprite.dispose}
    when 1
      dir = 6
      xs = ys = x = y = count = 0
      loop do
        (0...6).each {|j|
            sprites[x + y * 20].opacity = 255
            case dir
            when 2
              if y >= 14 - ys
                dir = 4
                x -= 1
                ys += 1
              else
                y += 1
              end
            when 4
              if x <= 0 + xs
                dir = 8
                y -= 1
                xs += 1
              else
                x -= 1
              end
            when 6
              if x >= 19 - xs
                dir = 2
                y += 1
              else
                x += 1
              end
            when 8
              if y <= 0 + ys
                dir = 6
                x += 1
              else
                y -= 1
              end
            end}
        count += 1
        break if count >= 50
        Graphics.update
      end
      2.times {Graphics.update}
      Graphics.freeze
      (sprites + [@spriteset, @message_window]).each {|sprite| sprite.dispose}
    when 2
      dir = 6
      ax = ay = count = 0
      bx, by = 19, 14
      loop do
        (0...3).each {|j|
            sprites[ax + ay * 20].opacity = sprites[bx + by * 20].opacity = 255
            case dir
            when 4
              if ax <= 0
                dir = 6
                ay += 1
                by -= 1
              else
                ax -= 1
                bx += 1
              end
            when 6
              if ax >= 19
                dir = 4
                ay += 1
                by -= 1
              else
                ax += 1
                bx -= 1
              end
            end}
        count += 1
        break if count >= 50
        Graphics.update
      end
      2.times {Graphics.update}
      Graphics.freeze
      (sprites + [@spriteset, @message_window]).each {|sprite| sprite.dispose}
    when 3
      dir = 2
      ax = ay = count = 0
      bx, by = 19, 14
      loop do
        (0...3).each {|j|
            sprites[ax + ay * 20].opacity = sprites[bx + by * 20].opacity = 255
            case dir
            when 2
              if ay >= 14
                dir = 8
                ax += 1
                bx -= 1
              else
                ay += 1
                by -= 1
              end
            when 8
              if ay <= 0
                dir = 2
                ax += 1
                bx -= 1
              else
                ay -= 1
                by += 1
              end
            end}
        count += 1
        break if count >= 50
        Graphics.update
      end
      2.times {Graphics.update}
      Graphics.freeze
      (sprites + [@spriteset, @message_window]).each {|sprite| sprite.dispose}
    when 4..7
      Graphics.freeze
      @spriteset.pre_dispose
      @message_window.dispose
      Graphics.transition(30, trans)
      Graphics.freeze
      @spriteset.su_dispose
      @spriteset.final_dispose
    end
  end
  
  def call_fade_boss
    Graphics.freeze
    $game_switches[190] = false
    bitmap = CP.break_screen
    $scene.sprites = []
    @spriteset.pre_dispose
    @spriteset.su_dispose
    @message_window.dispose
    (0...20).each {|i| (0...15).each {|j|
        sprite = Sprite.new
        sprite.bitmap = Bitmap.new(32, 32)
        sprite.bitmap.blt(0, 0, bitmap, Rect.new(i*32, j*32, 32, 32))
        sprite.x, sprite.y, sprite.z = i*32+16, j*32+16, 100000
        sprite.ox = sprite.oy = 16
        $scene.sprites.push([sprite, rand(8), rand(6)])}}
    bitmap.dispose
    @spriteset.final_dispose
  end

end
