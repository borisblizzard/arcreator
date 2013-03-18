#==============================================================================
# Location Names merged with Arrow over Player by Blizzard
# Version: 3.0b CP DX
# 
# NOTE: This script WILL corrupt old savegames!
# 
# Instructions:
# Connect map IDs with picture names. All pictures MUST be in the the Names
# folder in your picture folder.
#==============================================================================

#==============================================================================
# Game_System
#==============================================================================

class Game_System
  
  attr_accessor :map_name_id
  attr_accessor :name_timer
  
  alias init_names_later initialize
  def initialize
    init_names_later
    @map_name_id = @names_timer = 0
  end
  
end

#==============================================================================
# Name_Sprite
#==============================================================================

class Name_Sprite < Sprite
  
  attr_reader :timer
  
  def initialize(move = 0)
    super()
    if $game_system.map_name_id == $game_map.map_id
      @timer = $game_system.name_timer
    else
      @timer = -1
    end
    $game_system.map_name_id = $game_map.map_id if move < 0
    self.bitmap = get_image($game_map.map_id)
    if self.bitmap != nil
      @timer = -1 if @timer == nil
      @move = move
      @org_y = self.y
      self.z = 2000
      if @move > 0
        c = Color.new(0, 0, 0, 0)
        (0..self.bitmap.width/16).each {|i|
            self.bitmap.fill_rect(i*16, 0, 8, self.bitmap.height, c)}
      else
        c = Color.new(0, 0, 0, 0)
        (0..self.bitmap.width/16).each {|i|
            self.bitmap.fill_rect(8 + i*16, 0, 8, self.bitmap.height, c)}
      end
      update
    else
      self.dispose
    end
  end
  
  def update
    super
    if @timer < 16
      self.opacity = @timer * 15
      rate = case @timer
      when 15 then 1
      when 14 then 2
      when 13 then 4
      when 12 then 8
      else
        (13 - @timer) * 6
      end
      self.y = @org_y - rate * @move
    elsif @timer > 78
      self.opacity = 255 - ((@timer - 78) * 15)
      rate = case @timer
      when 79 then 1
      when 80 then 2
      when 81 then 4
      when 82 then 6
      when 83 then 8
      else
        (@timer - 82) * 6
      end
      self.y = @org_y - rate * @move
    else
      self.opacity = 255
      self.y = @org_y
    end
    @timer += 1
  end
  
  def get_image(id)
    case id
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START of Database
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    when 23 then name = 'Reeva'
    when 32, 321 then name = 'Reeva West Cave'
    when 36 then name = 'Reeva East Cave'
    when 46, 797 then name = 'South Lisk'
    when 49 then name = 'Lisk Forest'
    when 50 then name = 'Forest of Illusions'
    when 54 then name = 'Lisk'
    when 75 then name = 'Esteria'
    when 81, 82 then name = 'Echo Cave'
    when 87 then name = 'Giada Castle'
    when 109, 724 then name = 'Great Marsh'
    when 110 then name = 'Lorence Castle'
    when 115 then name = 'Lorence'
    when 140 then name = 'South Esteria Canyon'
    when 146 then name = 'Vendetta'
    when 147 then name = 'Krato'
    when 179 then name = 'Genesis Dome'
    when 191 then name = 'Dalia'
    when 195 then name = 'Adel Tower'
    when 213, 215, 218 then name = 'Katana Desert'
    when 217 then name = 'Desert Port'
    when 220 then name = 'Lucius Home'
    when 221 then name = 'White Peak City'
    when 231, 235, 237 then name = 'Silent Forest'
    when 249 then name = 'Great Lake'
    when 245 then name = 'Ice Cavern'
    when 247 then name = 'Tower of Memories'
    when 254 then name = 'Ice Temple'
    when 292 then name = 'Luvia'
    when 299 then name = 'Castle Luvia'
    when 361 then name = 'Kaeri'
    when 378, 389 then name = 'Marla Pass'
    when 405 then name = 'Termina Sewers'
    when 413 then name = 'Termina'
    when 441 then name = 'Black Jack City'
    when 442 then name = 'Astralis'
    when 480, 504 then name = 'Ember Volcano'
    when 507 then name = 'Lakeside'
    when 520 then name = 'Andras Temple'
    when 542, 548 then name = 'Forgotten Plains'
    when 543, 549 then name = 'Mountains of Slumber'
    when 561 then name = 'Mandora Kingdom'
    when 615 then name = 'Crios Island'
    when 616 then name = 'Medirok'
    when 617 then name = 'Ferry Port'
    when 668 then name = 'Unitopia'
    when 712 then name = 'Hyperion'
    when 713 then name = 'Thirsty Dunes'
    when 774 then name = 'Diovlleh Island'
    when 798 then name = 'Pandemonium'
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END of Database
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    else
      return nil
    end
    return RPG::Cache.picture("Names/#{name}").clone
  end
  
  def dispose
    $game_system.name_timer = @timer if @move != nil && @move > 0
    super
  end
  
end

#==============================================================================
# Spriteset_Map
#==============================================================================

class Spriteset_Map
  
  attr_accessor :name
  
  alias init_name_later initialize
  def initialize
    @names = [Name_Sprite.new(1), Name_Sprite.new(-1)]
    init_name_later
    if $scene.is_a?(Scene_Map)
      @arrow = Sprite.new(@viewport1)
      @arrow.bitmap = CP::Cache.image('arrow')
      @arrow.z, @arrow.ox, @arrow_mode = 5000, 8, true
      arrow_update
    end
  end
  
  alias upd_name_later update
  def update
    if @names != nil
      unless @names[0].disposed?
        @names.each {|s| s.update}
        if @names[0].opacity == 0 && @names[0].timer > 16
          @names.each {|s| s.dispose}
          @names = nil
        end
      else
        @names = nil
      end
    end
    upd_name_later
    arrow_update
  end
  
  def arrow_update
    if $scene.is_a?(Scene_Map) && @arrow != nil
      @arrow.x, @arrow.y = $game_player.screen_x, $game_player.screen_y - 56
      @arrow.visible = false
      if $game_player.character_name != '' && !$game_player.always_on_top &&
          $game_player.opacity > 0
        (0..2).each {|n|
            tile_id = $game_map.data[$game_player.x, $game_player.y-1, n]
            if tile_id != nil && tile_id != 0 && $game_map.priorities[tile_id] > 1
              tile = RPG::Cache.tile($game_map.tileset_name, tile_id, 0)
              if tile_id < 384
                @arrow.visible = true
              else
                counter = 0
                (0...32).each {|i| (8...32).each {|j|
                    counter += 1 if tile.get_pixel(i, j).alpha > 192
                    if counter > 128
                      @arrow.visible = true
                      break
                    end}}
              end
            end}
      end
      if @arrow_mode
        @arrow.oy += 1
        @arrow_mode = (@arrow.oy < 4)
      else
        @arrow.oy -= 1
        @arrow_mode = (@arrow.oy <= -4)
      end
    end
  end
  
  def extra_dispose
    unless @names == nil
      $game_system.name_timer = @names[0].timer
      @names.each {|s| s.dispose}
      @names = nil
    end
    unless @arrow == nil
      @arrow.dispose
      @arrow = nil
    end
  end
  
end
