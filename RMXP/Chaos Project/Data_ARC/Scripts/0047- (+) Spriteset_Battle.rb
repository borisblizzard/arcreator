#==============================================================================
# Spriteset_Battle
#==============================================================================

class Spriteset_Battle
  
  attr_reader   :viewport1
  attr_reader   :viewport2
  
  def initialize
    @viewport1 = Viewport.new(0, 0, 640, 320)
    @viewport2 = Viewport.new(0, 0, 640, 480)
    @viewport3 = Viewport.new(0, 0, 640, 480)
    @viewport4 = Viewport.new(0, 0, 640, 480)
    @viewport2.z = 101
    @viewport3.z = 200
    @viewport4.z = 5000
    @battleback_sprite = Sprite.new(@viewport1)
    @enemy_sprites = []
    $game_troop.enemies.reverse.each {|enemy|
        @enemy_sprites.push(Sprite_Battler.new(@viewport1, enemy))}
    @actor_sprites = []
    4.times{@actor_sprites.push(Sprite_Battler.new(@viewport2))}
    @weather = RPG::Weather.new(@viewport1)
    @picture_sprites = []
    (51..100).each {|i|
        @picture_sprites.push(Sprite_Picture.new(@viewport3,
            $game_screen.pictures[i]))}
    @timer_sprite = Sprite_Timer.new
    if CP::Cache::PanoramaBattleMaps.include?($game_map.map_id)
      @panorama = Plane.new(@viewport1)
      @panorama.z = -1000
      @panorama.bitmap = RPG::Cache.panorama($game_map.panorama_name, $game_map.panorama_hue)
    end
    update
  end
  
  def dispose
    @enemy_sprites.each {|sprite| sprite.bitmap.dispose if sprite.bitmap != nil}
    ([@battleback_sprite, @weather, @timer_sprite] + @picture_sprites +
        @enemy_sprites + @actor_sprites).each {|sprite| sprite.dispose}
    [@viewport1, @viewport2, @viewport3, @viewport4].each {|view| view.dispose}
    @panorama.dispose if @panorama != nil
  end
  
  def effect?
    return ((@enemy_sprites + @actor_sprites).any? {|sprite| sprite.effect?})
  end
  
  def update
    (0...4).each {|i| @actor_sprites[i].battler = $game_party.actors[i]}
    if @battleback_name != $game_temp.battleback_name
      @battleback_name = $game_temp.battleback_name
      @battleback_sprite.bitmap.dispose if @battleback_sprite.bitmap != nil
      @battleback_sprite.bitmap = RPG::Cache.battleback(@battleback_name)
      @battleback_sprite.src_rect.set(0, 0, 640, 320)
    end
    @enemy_sprites.clone.each {|sprite|
        if !sprite.battler.exist? && sprite.opacity == 0 && !sprite.damage?
          sprite.dispose
          @enemy_sprites.delete(sprite)
        end}
    $game_troop.enemies.each {|enemy|
        if enemy.exist? && @enemy_sprites.all? {|s| s.battler != enemy}
          @enemy_sprites.push(Sprite_Battler.new(@viewport1, enemy))
        end}
    (@enemy_sprites + @actor_sprites).each {|sprite| sprite.update}
    @weather.type = $game_screen.weather_type
    @weather.max = $game_screen.weather_max
    @weather.update
    @picture_sprites.each{|sprite| sprite.update}
    @timer_sprite.update
    @viewport1.tone = $game_screen.tone
    @viewport1.ox = $game_screen.shake
    @viewport1.oy = $game_screen.tremble
    @viewport4.color = $game_screen.flash_color
    [@viewport1, @viewport2, @viewport4].each {|view| view.update}
    update_panorama
  end
  
  def refresh
    (0...4).each {|i| @actor_sprites[i].battler = $game_party.actors[i]}
    already_there = []
    @enemy_sprites.each {|sprite|
        sprite.battler = $game_troop.enemies[sprite.battler.index]
        already_there.push($game_troop.enemies[sprite.battler.index])}
    ($game_troop.enemies - already_there).each {|enemy|
        if enemy.exist?
          @enemy_sprites.push(Sprite_Battler.new(@viewport1, enemy))
        end}
  end
  
  def update_panorama
    if @panorama != nil
      @panorama.ox += $game_variables[121]
      @panorama.oy += $game_variables[122]
    end
  end
  
end
