#==============================================================================
# Numeric
#==============================================================================

class Numeric
  
  def sgn
    return (self == 0 ? 0 : self/self.abs)
  end
  
end

#==============================================================================
# Char_Icon
#==============================================================================

class Char_Icon < Icon
  
  def initialize(cycle, range = 80, horizontal = true, view = nil)
    super
    @org_dir = 0
  end
  
  def dir=(val)
    @dir = @org_dir = val
  end
  
  def degrees=(val)
    @degrees = (val) % 360
    setup_zoom
    zo = self.bitmap.width * (1 - self.zoom_x) / 2 / self.zoom_x
    self.ox = - zo.round - @range * (Math.sin(Math::PI*@degrees/180))
    self.opacity = self.zoom_x * 255
  end
  
  def bitmap=(bit)
    super(RPG::Cache.icon('Battle/icon_back').clone)
    self.bitmap.blt(4, 4, bit, Rect.new(0, 0, 24, 24))
  end
  
  def update
    return unless self.visible || moving?
    if moving?
      self.degrees += 2 * @org_dir
      @dir -= @dir.sgn if self.degrees / (360/@cycle) * (360/@cycle) == self.degrees
    end
    dr = @dir
    super
    @dir = dr
  end
  
end

#==============================================================================
# Menu_PartyCommand
#==============================================================================

class Menu_NameCommand < Menu_Command
  
  def initialize(table)
    @table = table
    super()
    36.times {@icons.push(Char_Icon.new(36, 300))}
    refresh
    @icons.each_index {|i| @icons[i].degrees, @icons[i].oy = i*360 / 36, -160}
    @index = 0
    self.x, self.y = 320, 200
    self.visible = false
    self.active = true
  end
  
  def update
    @icons.each_index {|i|
        @index == i ? @icons[i].blink_on : @icons[i].blink_off
        @icons[i].update}
    if !@icons[0].moving? && self.active
      if Input.repeat?($controls.right)
        $game_system.se_play($data_system.cursor_se)
        @index = (@index + 1) % 36
        @icons.each {|s| s.dir = -1}
      elsif Input.repeat?($controls.left)
        $game_system.se_play($data_system.cursor_se)
        @index = (@index + 35) % 36
        @icons.each {|s| s.dir = 1}
      elsif Input.repeat?($controls.nex)
        $game_system.se_play($data_system.cursor_se)
        @index = (@index + 5) % 36
        @icons.each {|s| s.dir = -5}
      elsif Input.repeat?($controls.prev)
        $game_system.se_play($data_system.cursor_se)
        @index = (@index + 31) % 36
        @icons.each {|s| s.dir = 5}
      end
    end
  end
  
  def character
    return @table[@index]
  end
  
  def refresh
    @icons.each_index {|i|
        @icons[i].bitmap.dispose if @icons[i].bitmap != nil
        if @table[i] == 'OK'
          bitmap = RPG::Cache.icon('vvv')
        else
          bitmap = Bitmap.new(24, 24)
          bitmap.font.name = $fontface
          if $fontface == 'Papyrus'
            bitmap.font.size += 6
            bitmap.font.bold = true
            bitmap.draw_text_shaded(0, -2, 24, 26, @table[i], 1)
          else
            bitmap.draw_text_shaded(0, 0, 24, 24, @table[i], 1)
          end
        end
        @icons[i].bitmap = bitmap}
  end
  
  def update_help
  end
  
end

#==============================================================================
# Scene_Name
#==============================================================================

TABLE = [
    'A','B','C','D','E','F','G','H','I','J',' ','K','L','M','N','O','P','Q',
    'R','S','T',' ','U','V','W','X','Y','Z',' ','0','1','2','3','4',' ','OK',
    'a','b','c','d','e','f','g','h','i','j',' ','k','l','m','n','o','p','q',
    'r','s','t',' ','u','v','w','x','y','z',' ','5','6','7','8','9',' ','OK',
    '+','-','*','/','=','!','?',' ','$','%','&',' ','(',')','[',']','{','}',
    ' ','#','~','<','>','|',' ',',','.',';',':','_','\\','^','\'','"',' ','OK']
  
class Scene_Name
  
  def main
    @actor = $game_actors[$game_temp.name_actor_id]
    @sprite = Sprite.new
    @sprite.bitmap = RPG::Cache.character(@actor.character_name, @actor.character_hue)
    cw, ch = @sprite.bitmap.width / 4, @sprite.bitmap.height / 4
    @sprite.src_rect.set(0, 0, cw, ch)
    @sprite.ox, @sprite.oy = cw/2, ch/2
    @sprite.x, @sprite.y, @sprite.z = 320, 320, 1999
    @name = Sprite.new
    @name.bitmap = Bitmap.new(320, 32)
    @name.x, @name.y = 160, 192
    @name.bitmap.font.name = $fontface
    if $fontface == 'Papyrus'
      @name.bitmap.font.size += 6
      @name.bitmap.font.bold = true
    end
    @name.bitmap.draw_text_shaded(0, 0, 320, 32, @actor.name, 1)
    @info = Sprite.new
    @info.bitmap = Bitmap.new(560, 96)
    @info.x, @info.y = 80, 32
    @info.bitmap.font.name = $fontface
    if $fontface == 'Papyrus'
      @info.bitmap.font.size += 6
      @info.bitmap.font.bold = true
    end
    text = "#{CP.controls_name($controls.left)} / #{CP.controls_name($controls.right)}"
    @info.bitmap.draw_text_shaded(-16, 0, 240, 32, text, 2)
    text = "#{CP.controls_name($controls.prev)} / #{CP.controls_name($controls.nex)}"
    @info.bitmap.draw_text_shaded(-16, 32, 240, 32, text, 2)
    text = "#{CP.controls_name($controls.up)} / #{CP.controls_name($controls.down)}"
    @info.bitmap.draw_text_shaded(-16, 64, 240, 32, text, 2)
    @info.bitmap.draw_text_shaded(240, 0, 320, 32, 'change letter')
    @info.bitmap.draw_text_shaded(240, 32, 320, 32, 'skip 5 letters')
    @info.bitmap.draw_text_shaded(240, 64, 320, 32, 'change character table')
    @edit = @actor.name
    @input = []
    @index = 0
    (0..2).each {|i| @input.push(Menu_NameCommand.new(TABLE[i*36, 36]))}
    @inp = @input[@index]
    @inp.visible = true
    Graphics.transition
    loop do
      Graphics.update
      Input.update
      update
      break if $scene != self
    end
    Graphics.freeze
    @name.dispose
    @info.dispose
    @sprite.dispose
    @input.each {|menu| menu.dispose}
    Graphics.transition
    Graphics.freeze
  end
  
  def update
    @input.each {|menu| menu.update}
    if Input.trigger?($controls.down) || Input.trigger?($controls.up)
      $game_system.se_play($data_system.cursor_se)
      @inp.visible = false
      if Input.trigger?($controls.down)
        @index = (@index+1) % 3
      elsif Input.trigger?($controls.up)
        @index = (@index+2) % 3
      end
      @inp = @input[@index]
      @inp.visible = true
    elsif Input.repeat?($controls.cancel) && @edit != ''
      $game_system.se_play($data_system.cancel_se)
      @edit = @edit[0, @edit.size-1]
      @name.bitmap.clear
      @name.bitmap.draw_text_shaded(0, 0, 320, 32, @edit, 1)
    elsif Input.trigger?($controls.confirm)
      if @inp.character == 'OK'
        if @edit == ''
          $game_system.se_play($data_system.buzzer_se)
        else
          @actor.name = @edit
          $game_system.se_play($data_system.decision_se)
          $scene = Scene_Map.new
        end
      elsif @edit.size == $game_temp.name_max_char || @inp.character == ''
        $game_system.se_play($data_system.buzzer_se)
      else
        $game_system.se_play($data_system.decision_se)
        @edit += @inp.character
        @name.bitmap.clear
        @name.bitmap.draw_text_shaded(0, 0, 320, 32, @edit, 1)
      end
    end
  end
  
end
