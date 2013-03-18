#==============================================================================
# Chaos Event Anti-Lag (CEAL) by Blizzard
# Version: 3.0
# Type: Performance Improving System
#==============================================================================

#==============================================================================
# Control_Sprite_Character
#==============================================================================

class Control_Sprite_Character
  
  attr_reader :character
  attr_reader :sprite
  
  def initialize(viewport, character = nil)
    @viewport = viewport
    self.character = character
  end
  
  def character=(char)
    @character = char
    @sprite.character = char unless @sprite == nil
    @shadow.character = char unless @shadow == nil
    @sight.character = char unless @sight == nil
    @reflection.character = char unless @reflection == nil
    update
  end
  
  def sprite_update
    if @character.update?
      if @sprite == nil || @sprite.disposed?
        @sprite = Sprite_Character_CPEAL.new(@viewport, @character)
      else
        @sprite.update
      end
      if @sprite.bitmap != nil
        @character.sprite_size = [64-@sprite.src_rect.width*2,
            63+@sprite.src_rect.width*2, 128-@sprite.src_rect.height*4, 127]
        if !@character.update?
          @sprite.dispose unless @sprite.disposed?
          @sprite = nil
        end
      else
        @character.sprite_size = [0, 127, 0, 127]
      end
    elsif @sprite != nil
      @sprite.dispose unless @sprite.disposed?
      @sprite = nil
    end
  end
  
  def shadow_update
    if @character.shadow?
      if @shadow == nil || @shadow.disposed?
        @shadow = Sprite_Shadow.new(@viewport, @character)
      else
        @shadow.update
      end
      if @shadow.bitmap != nil
        @character.shadow_size = [64-@shadow.src_rect.width*2,
            63+@shadow.src_rect.width*2, 128-@shadow.src_rect.height*4, 127]
        if !@character.shadow?
          @shadow.dispose unless @shadow.disposed?
          @shadow = nil
        end
      else
        @character.shadow_size = [0, 127, 0, 127]
      end
    elsif @shadow != nil
      @shadow.dispose unless @shadow.disposed?
      @shadow = nil
    end
  end
  
  def sight_update
    if @character.sight?
      if @sight == nil || @sight.disposed?
        @sight = Sprite_Sight.new(@viewport, @character)
      else
        @sight.update
      end
      if @sight.bitmap != nil
        @character.sight_size = [64-288*2, 63+288*2, 64-288*2, 63+288*2]
        if !@character.sight?
          @sight.dispose unless @sight.disposed?
          @sight = nil
        end
      else
        @character.sight_size = [0, 127, 0, 127]
      end
    elsif @sight != nil
      @sight.dispose unless @sight.disposed?
      @sight = nil
    end
  end
  
  def reflection_update
    if @character.reflection?
      if @reflection == nil || @reflection.disposed?
        @reflection = Sprite_Reflection.new(@viewport, @character)
      else
        @reflection.update
      end
      if @reflection.bitmap != nil
        @character.reflection_size = [64-@reflection.src_rect.width*2,
            63+@reflection.src_rect.width*2, 111,
            111+@reflection.src_rect.height*4]
        if !@character.reflection?
          @reflection.dispose unless @reflection.disposed?
          @reflection = nil
        end
      else
        @character.reflection_size = [0, 127, 0, 127]
      end
    elsif @reflection != nil
      @reflection.dispose unless @reflection.disposed?
      @reflection = nil
    end
  end
  
  def update
    if @character != nil
      @character.init_ceal if @character.sight_size == nil
      sprite_update
      shadow_update
      sight_update
      reflection_update
    else
      @sprite.dispose if @sprite != nil && !@sprite.disposed?
      @shadow.dispose if @shadow != nil && !@shadow.disposed?
      @sight.dispose if @sight != nil && !@sight.disposed?
      @reflection.dispose if @reflection != nil && !@reflection.disposed?
      @sprite = @shadow = @sight = @reflection = nil
    end
  end
  
  def blink_on
    @sprite.blink_on if @sprite != nil
  end
  
  def blink_off
    @sprite.blink_off if @sprite != nil
  end
  
  def dispose
    @sprite.dispose unless @sprite == nil || @sprite.disposed?
    @shadow.dispose unless @shadow == nil || @shadow.disposed?
    @sight.dispose unless @sight == nil || @sight.disposed?
    @reflection.dispose unless @reflection == nil || @reflection.disposed?
    @sprite = @shadow = @sight = @reflection = nil
  end
  
  def center
    return [0, 0] if @sprite == nil
    x = @sprite.x - @sprite.ox + @sprite.bitmap.width/8
    y = @sprite.y - @sprite.oy + @sprite.bitmap.height/8
    return x, y
  end
  
end

#==============================================================================
# Sprite_Character_CPEAL
#==============================================================================

class Sprite_Character_CPEAL < Sprite_Character
  
end

#==============================================================================
# Sprite_Character
#==============================================================================

class Sprite_Character < Control_Sprite_Character
  
end

#==============================================================================
# Game_Character
#==============================================================================

class Game_Character
  
  attr_accessor :sprite_size
  attr_accessor :shadow_size
  attr_accessor :sight_size
  attr_accessor :reflection_size
  
  alias init_ceal_later initialize
  def initialize
    @no_ceal = false
    init_ceal
    init_ceal_later
  end
  
  def init_ceal
    @sprite_size = [-1600, 1600, -1600, 1600]
    @shadow_size = [-1600, 1600, -1600, 1600]
    @sight_size = [-1600, 1600, -1600, 1600]
    @reflection_size = [-1600, 1600, -1600, 1600]
  end
  
  def update?
    return true if !self.is_a?(Game_Event)
    return false if @erased
    return true if @trigger == 3 || @trigger == 4
    return true if @no_ceal
    return false if @character_name == '' && @tile_id < 384
    return false if @real_x >= $game_map.display_x + 20 * 128 - @sprite_size[0]
    return false if @real_x < $game_map.display_x - @sprite_size[1]
    return false if @real_y >= $game_map.display_y + 15 * 128 - @sprite_size[2]
    return false if @real_y < $game_map.display_y - @sprite_size[3]
    return true
  end
  
  def shadow?
    return false if CP::Cache::NoShade.include?(@character_name)
    return false if @character_name == '' || @tile_id >= 384
    return false if @real_x >= $game_map.display_x + 20 * 128 - @shadow_size[0]
    return false if @real_x < $game_map.display_x - @shadow_size[1]
    return false if @real_y >= $game_map.display_y + 15 * 128 - @shadow_size[2]
    return false if @real_y < $game_map.display_y - @shadow_size[3]
    return true if !self.is_a?(Game_Event)
    return true if CP.first_comment(self, 'shadow')
    return true if CP.first_comment(self, 'bigshadow')
    return true if CP.first_comment(self, 'hugeshadow')
    return false
  end
  
  def sight?
    return false if !@tracer
    return false if @character_name == ''
    return false if @real_x >= $game_map.display_x + 20 * 128 - @sight_size[0]
    return false if @real_x < $game_map.display_x - @sight_size[1]
    return false if @real_y >= $game_map.display_y + 15 * 128 - @sight_size[2]
    return false if @real_y < $game_map.display_y - @sight_size[3]
    return true
  end
  
  def reflection?
    return false if @lowest || !CP::Cache::MirrorMaps.include?($game_map.map_id)
    return false if @character_name == ''
    return false if @real_x >= $game_map.display_x + 20 * 128 - @reflection_size[0]
    return false if @real_x < $game_map.display_x - @reflection_size[1]
    return false if @real_y >= $game_map.display_y + 15 * 128 - @reflection_size[2]
    return false if @real_y < $game_map.display_y - @reflection_size[3]
    return true
  end
  
end
  
#==============================================================================
# Game_Event
#==============================================================================

class Game_Event
  
  alias upd_ceal_later update
  def update
    if !self.moving? && @trigger != 3 && @trigger != 4 && !@tracer &&
        self.name != 'Sphere' && !@no_ceal
      return if @character_name == '' && @tile_id < 384
      return if @real_x >= $game_map.display_x + 20 * 128 - @sprite_size[0]
      return if @real_x < $game_map.display_x - @sprite_size[1]
      return if @real_y >= $game_map.display_y + 15 * 128 - @sprite_size[2]
      return if @real_y < $game_map.display_y - @sprite_size[3]
    end
    upd_ceal_later
  end
  
end
