#==============================================================================
# Spriteset_Map
#==============================================================================

class Spriteset_Map
  
  attr_reader :viewport1
  attr_reader :viewport4
  attr_reader :tilemap
  attr_reader :character_sprites
  
  def initialize
    @dx = @dy = 0
    @viewport1 = Viewport.new(0, 0, 640, 480)
    @viewport2 = Viewport.new(0, 0, 640, 480)
    @viewport3 = Viewport.new(0, 0, 640, 480)
    @viewport4 = Viewport.new(0, 0, 640, 480)
    @viewport2.z = 200
    @viewport3.z = 5000
    @viewport4.z = 900
    @tilemap = Tilemap.new(@viewport1)
    load_tilemap
    @tilemap.map_data = $game_map.data
    @tilemap.priorities = $game_map.priorities
    @panorama = Plane.new(@viewport1)
    @panorama.z = -1000
    @fog = Plane.new(@viewport1)
    @fog.z = 3000
    @character_sprites = []
    $game_map.events.keys.sort.each {|i|
        @character_sprites.push(Sprite_Character.new(@viewport1,
            $game_map.events[i]))}
    @character_sprites.push(Sprite_Character.new(@viewport1, $game_player))
    @weather = RPG::Weather.new(@viewport1)
    @picture_sprites = []
    (1..50).each {|i|
        @picture_sprites.push(Sprite_Picture.new(@viewport2,
            $game_screen.pictures[i]))}
    @timer_sprite = Sprite_Timer.new
    update
  end
  
  def clear_tilemap
    @tilemap.tileset = RPG::Cache.tileset('')
    (0..6).each {|i| @tilemap.autotiles[i] = RPG::Cache.autotile('')}
  end
  
  def load_tilemap
    @tilemap.tileset = RPG::Cache.tileset($game_map.tileset_name)
    (0..6).each {|i|
        @tilemap.autotiles[i] = RPG::Cache.autotile($game_map.autotile_names[i])}
    clear_tilemap if $game_switches[395]
  end
  
  def dispose
    pre_dispose
    su_dispose
    final_dispose
  end
  
  def pre_dispose
    @tilemap.tileset.dispose if @tilemap.tileset != nil
    (0..6).each {|i| @tilemap.autotiles[i].dispose if @tilemap.autotiles[i] != nil}
    ([@tilemap, @panorama, @fog, @weather] + @character_sprites +
        @picture_sprites).each {|sprite| sprite.dispose}
    extra_dispose
  end
  
  def final_dispose
    @timer_sprite.dispose
  end
  
  def su_dispose
    [@viewport1, @viewport2, @viewport3, @viewport4].each {|view|
        view.dispose unless view == nil}
  end
  
  def update
    if @panorama_name != $game_map.panorama_name ||
        @panorama_hue != $game_map.panorama_hue
      @panorama_name = $game_map.panorama_name
      @panorama_hue = $game_map.panorama_hue
      if @panorama.bitmap != nil
        @panorama.bitmap.dispose
        @panorama.bitmap = nil
      end
      if @panorama_name != ''
        @panorama.bitmap = RPG::Cache.panorama(@panorama_name, @panorama_hue)
      end
      Graphics.frame_reset
    end
    if @fog_name != $game_map.fog_name || @fog_hue != $game_map.fog_hue
      @fog_name = $game_map.fog_name
      @fog_hue = $game_map.fog_hue
      if @fog.bitmap != nil
        @fog.bitmap.dispose
        @fog.bitmap = nil
      end
      @fog.bitmap = RPG::Cache.fog(@fog_name, @fog_hue) if @fog_name != ''
      Graphics.frame_reset
    end
    @tilemap.ox = $game_map.display_x / 4
    @tilemap.oy = $game_map.display_y / 4
    @tilemap.update
    if $game_switches[395]
      @panorama.ox = @panorama.oy = 0
    else
      ox = @panorama.ox - @dx
      oy = @panorama.oy - @dy
      @panorama.ox = $game_map.display_x / 8
      @panorama.oy = $game_map.display_y / 8
      @panorama.ox += $game_variables[121] + ox
      @panorama.oy += $game_variables[122] + oy
      @dx = $game_map.display_x / 8
      @dy = $game_map.display_y / 8
    end
    @fog.zoom_x = $game_map.fog_zoom / 100.0
    @fog.zoom_y = $game_map.fog_zoom / 100.0
    @fog.opacity = $game_map.fog_opacity
    @fog.blend_type = $game_map.fog_blend_type
    @fog.ox = $game_map.display_x / 4 + $game_map.fog_ox
    @fog.oy = $game_map.display_y / 4 + $game_map.fog_oy
    @fog.tone = $game_map.fog_tone
    @character_sprites.each {|sprite| sprite.update}
    @weather.type = $game_screen.weather_type
    @weather.max = $game_screen.weather_max
    @weather.ox = $game_map.display_x / 4
    @weather.oy = $game_map.display_y / 4
    @weather.update
    @picture_sprites.each {|sprite| sprite.update}
    @timer_sprite.update
    @viewport1.tone = $game_screen.tone
    @viewport1.oy = $game_screen.tremble unless $game_screen.tremble == nil
    @viewport1.ox = $game_screen.shake
    @viewport3.color = $game_screen.flash_color
    @viewport1.update
    @viewport3.update
  end
  
end
