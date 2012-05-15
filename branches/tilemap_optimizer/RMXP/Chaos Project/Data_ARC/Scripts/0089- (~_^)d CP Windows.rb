#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=
# StormTronics Hybrid by Blizzard
# Version: 6.4b - Hybrid Edition DX
# Type: Enhanced Custom Menu System
# Window class definitions
#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=

BGM, PLANET, CITY, CAM = 22, 23, 24, 25

TELEPORT_Lock, BGM_Lock = 35, 42

#==============================================================================
# Info_Sprite
#==============================================================================

class Info_Sprite < Sprite
  
  attr_reader :mode
  attr_reader :index
  attr_writer :rage_window
  
  def initialize(viewport = nil)
    super
    @mode = @index = 0
    self.visible = ($game_system.visible_info == true)
    self.bitmap = Bitmap.new(1, 1)
    self.bitmap.font.name = $fontface
    self.bitmap.font.size += 6 if $fontface == 'Papyrus'
    self.z = 20000
    refresh
  end
  
  def set(mod, i)
    if @mode != mod || @mode == 12 || @index != i
      @mode, @index = mod, i
      refresh
    end
  end
  
  def index=(i)
    if @index != i || @mode == 12
      @index = i
      refresh
    end
  end
  
  def update
    super
    if Input.trigger?($controls.menu)
      $game_system.se_play($data_system.cursor_se)
      $game_system.visible_info = (!self.visible)
      self.visible = $game_system.visible_info
      refresh
    end
  end
  
  def refresh
    return unless $game_system.visible_info
    self.bitmap.dispose unless self.bitmap == nil || self.bitmap.disposed?
    self.bitmap = Bitmap.new(1, 1)
    self.bitmap.font.name = $fontface
    text, w = [], 0
    case @mode
    when 0
      case @index
      when 0
        text.push('All items and equipment in possession.')
        text.push('You can see and use items here.')
      when 1
        text.push('All equipment in possession.')
        text.push('You can change equipment')
        text.push('and see the effects here.')
      when 2
        text.push('All character abilities.')
        text.push('You can see and use abilities here.')
      when 3
        text.push('All Soul Rage abilities.')
        text.push('You can see Soul Rage abilities here.')
      when 4
        text.push('You can view the character status,')
        text.push('set up the SR Increase Mode and')
        text.push('the Default Repeat Action here.')
      when 5 then text.push('You can change the game options here.')
      when 6
        text.push('You can teleport to locations')
        text.push('you have already visited.')
      when 7
        text.push('You can see and load')
        text.push('previously saved games here.')
      when 8
        text.push('You can exit the game or')
        text.push('return to the title screen here.')
      end
      text.each {|i|
          tw = self.bitmap.text_size(i).width+16
          w = tw if w < tw}
      w = (w * 1.4).to_i if $fontface == 'Papyrus'
      self.x = 488 - w
      self.y = @index * 32 + 32
    when 1
      case @index
      when 0 then text.push('See and use items.')
      when 1 then text.push('Change item order.')
      when 2 then text.push('See equipment.')
      when 3 then text.push('See important items.')
      end
      text.each {|i|
          tw = self.bitmap.text_size(i).width+16
          w = tw if w < tw}
      w = (w * 1.4).to_i if $fontface == 'Papyrus'
      self.x = 170 + @index * 150 - w/2
      self.y = 48
    when 11
      case @index
      when 0 then text.push('Sorts items by ID number.')
      when 1 then text.push('Sorts items by quantity.')
      when 2 then text.push('Sorts items by alphabet.')
      end
      text.each {|i|
          tw = self.bitmap.text_size(i).width+16
          w = tw if w < tw}
      w = (w * 1.4).to_i if $fontface == 'Papyrus'
      self.x = 256
      self.y = 124 + @index * 32
    when 5
      case @index
      when 0
        text.push('SR Increase Mode')
        text.push('Active: SR increases when suffering damage.')
        text.push('Passive: SR increases with time.')
      when 1
        text.push('Default Repeat Action')
        text.push('Fail: Action simply fails.')
        text.push('Attack: Attacks if action would fail.')
        text.push('Defend: Defends if action would fail.')
        text.push('Despair: Uses Despair if action would fail.')
      end
      text.each {|i|
          tw = self.bitmap.text_size(i).width+16
          w = tw if w < tw}
      w = (w * 1.4).to_i if $fontface == 'Papyrus'
      self.x = 608 - w
      self.y = @index * 28 + 226
    when 6
      case @index
      when 0 then text.push('Increase/decrease background music volume.')
      when 1 then text.push('Increase/decrease sound effect volume.')
      when 2 then text.push('Set the menu display mode.')
      when 3 then text.push('Set the battle background music.')
      when 4 then text.push('Set Pseudo 3D Battle Camera.')
      when 5
        text.push('Set the battle encounter mode.')
        text.push('Prompt me: Asks every time you are able to evade fights.')
        text.push('Always evade: Automatically tries to evade fights.')
        text.push('Always engage: Automatically engages into fights.')
      when 6
        text.push('Set the Unity Force Overload mode.')
        text.push('Automatic: Always 100% efficiency.')
        text.push('Manual: Trigger efficiency between 50% and 200%.')
      when 7 then text.push('Set to use one out of 7 bar styles.')
      when 8 then text.push('Set the bar opacity.')
      when 9 then text.push('Set the text font uses to display text.')
      when 10 then text.push('Set the messagebox/classic-menu windowskin.')
      when 11 then text.push('Shows earned game information.')
      end
      text.each {|i|
          tw = self.bitmap.text_size(i).width+16
          w = tw if w < tw}
      w = (w * 1.4).to_i if $fontface == 'Papyrus'
      self.x = 80
      self.y = @index * 28 + 44
    when 9
      case @index
      when 0 then text.push('Returns to the menu.')
      when 1 then text.push('Returns to the title screen.')
      when 2 then text.push('Exits the game.')
      end
      text.each {|i|
          tw = self.bitmap.text_size(i).width+16
          w = tw if w < tw}
      w = (w * 1.4).to_i if $fontface == 'Papyrus'
      self.x = 480 - w
      self.y = @index * 32 + 336
    when 12
      if @rage_window != nil
        item = @rage_window.data
        id = case item
        when RPG::Weapon then CP.sr_weapons(item.id)
        when RPG::Armor
          CP.sr_armors(item.id, @rage_window.actor, @rage_window.index)
        end
        if id != nil && id != 0
          text = self.bitmap.slice_bitmap(
              "#{$data_skills[id].name}: #{$data_skills[id].description}")
          text.each {|i|
              tw = self.bitmap.text_size(i).width+16
              w = tw if w < tw}
          w = (w * 1.4).to_i if $fontface == 'Papyrus'
          self.x, self.y = @rage_window.info_position(w / 2)
        end
      end
    end
    if text.size > 0
      self.bitmap.dispose unless self.bitmap == nil || self.bitmap.disposed?
      self.bitmap = Bitmap.new(w, text.size * 24 + 6)
      self.bitmap.font.name = $fontface
      if $fontface == 'Papyrus'
        self.bitmap.font.size += 6
        self.bitmap.font.bold = true
      end
      self.bitmap.fill_rect(0, 0, w, self.bitmap.height, Color.new(255, 255, 255, 192))
      self.bitmap.fill_rect(1, 1, w-2, self.bitmap.height-2, Color.new(0, 0, 0, 192))
      text.each_index {|i| self.bitmap.draw_text(0, 24*i, w, 26, text[i], 1)}
    end
  end
  
end

#==============================================================================
# Game_System
#==============================================================================

class Game_System
  
  attr_accessor :bgm_volume
  attr_accessor :sfx_volume
  attr_accessor :bar_style
  attr_accessor :cam
  attr_accessor :message_walking
  attr_accessor :encounter_mode
  attr_accessor :uf_mode
  attr_accessor :menu_mode
  attr_accessor :ex_mode
  attr_accessor :black_back
  attr_accessor :visible_info
  attr_reader   :bar_opacity
  
  alias init_cpnw_cms_later initialize
  def initialize
    init_cpnw_cms_later
    @bgm_volume = @sfx_volume = 100
    @bar_style = @cam = @encounter_mode = @menu_mode = @ex_mode = 0
    @bar_opacity = 256
    @message_walking = true
    @uf_mode = @black_back = @visible_info = false
  end
  
  def bar_opacity=(alpha)
    if alpha < 0
      @bar_opacity = 0
    elsif alpha > 256
      @bar_opacity = 256
    else
      @bar_opacity = alpha
    end
  end
  
  def get_cam
    $game_variables[CAM] = @cam
    return true
  end
    
  def test_custom(number, flag = nil)
    if flag
      if FileTest.exist?("custom_back#{number}.jpg") ||
          FileTest.exist?("custom_back#{number}.png")
        bitmap = RPG::Cache.custom_back("back#{number}")
        return (bitmap.width == 640 && bitmap.height == 480)
      else
        return false
      end
    elsif flag == false
      if FileTest.exist?("custom_black#{number}.jpg") ||
          FileTest.exist?("custom_black#{number}.png")
        bitmap = RPG::Cache.custom_back("black#{number}")
        return (bitmap.width == 640 && bitmap.height == 480)
      else
        return false
      end
    end
    if FileTest.exist?("custom_back#{number}.jpg") ||
        FileTest.exist?("custom_back#{number}.png")
      bitmap = RPG::Cache.custom_back("back#{number}")
      return (bitmap.width == 640 && bitmap.height == 480)
    end
    if FileTest.exist?("custom_black#{number}.jpg") ||
        FileTest.exist?("custom_black#{number}.png")
      bitmap = RPG::Cache.custom_back("black#{number}")
      return (bitmap.width == 640 && bitmap.height == 480)
    end
    return false
  end
  
  def bgm_play(bgm)
    @playing_bgm = bgm
    vol = correction(@bgm_volume)
    if bgm != nil && bgm.name != ''
      Audio.bgm_play("Audio/BGM/#{bgm.name}", bgm.volume * vol / 100, bgm.pitch)
    else
      Audio.bgm_stop
    end
    Graphics.frame_reset
  end
  
  def bgs_play(bgs)
    @playing_bgs = bgs
    vol = correction(@sfx_volume)
    if bgs != nil && bgs.name != ''
      Audio.bgs_play("Audio/BGS/#{bgs.name}", bgs.volume * vol / 100, bgs.pitch)
    else
      Audio.bgs_stop
    end
    Graphics.frame_reset
  end
  
  def me_play(me)
    vol = correction(@bgm_volume)
    if me != nil && me.name != ''
      Audio.me_play("Audio/ME/#{me.name}", me.volume * vol / 100, me.pitch)
    else
      Audio.me_stop
    end
    Graphics.frame_reset
  end

  def se_play(se)
    vol = correction(@sfx_volume)
    if se != nil && se.name != ''
      Audio.se_play("Audio/SE/#{se.name}", se.volume * vol / 100, se.pitch)
    end
  end
  
  def correction(volume)
    case volume
    when 100 then return 100
    when 95 then return 97
    when 90 then return 95
    when 85 then return 92
    when 80 then return 90
    when 75 then return 87
    when 70 then return 85
    when 65 then return 82
    when 60 then return 80
    when 55 then return 77
    when 50 then return 75
    when 45 then return 72
    when 40 then return 70
    when 35 then return 65
    when 30 then return 60
    when 25 then return 55
    when 20 then return 50
    when 15 then return 40
    when 10 then return 35
    when 5 then return 25
    when 0 then return 0
    else
      return 0
    end
  end
  
end

#============================================================================== 
# Game_Actor 
#============================================================================== 

class Game_Actor < Game_Battler 
  
  def now_exp 
    return @exp - @exp_list[@level] 
  end 
  
  def next_exp
    return @exp_list[@level+1] > 0 ? @exp_list[@level+1] - @exp_list[@level] : 0 
  end 
  
  def test_equip(equip_type, id)
    weapon = @weapon_id
    armor1 = @armor1_id
    armor2 = @armor2_id
    armor3 = @armor3_id
    armor4 = @armor4_id
    armor5 = @armor5_id
    armor6 = @armor6_id
    case equip_type
    when 0
      @weapon_id = id
      if CP::Cache::Lucius.include?(self.id)
        @armor1_id = 0 if CP::Cache::TwoHanded.include?(id) || CP::Cache::TwoHanded.include?(@weapon_id)
      end
    when 1
      if CP::Cache::Lucius.include?(self.id)
        if CP::Cache::TwoHanded.include?(id)
          @weapon_id, @armor1_id = id, 0
        else
          @weapon_id = 0 if CP::Cache::TwoHanded.include?(@weapon_id)
          @armor1_id = id
        end
      else
        @armor1_id = id
      end
    when 2
      @armor2_id = id
    when 3
      @armor3_id = id
    when 4
      @armor4_id = id
    when 5
      @armor5_id = id
    when 6
      @armor6_id = id
    end
    tested = [self.maxhp, self.maxsp, self.atk, self.pdef, self.mdef,
        self.str, self.dex, self.agi, self.int, self.eva]
    @weapon_id = weapon
    @armor1_id = armor1
    @armor2_id = armor2
    @armor3_id = armor3
    @armor4_id = armor4
    @armor5_id = armor5
    @armor6_id = armor6
    return tested
  end
  
end 

#============================================================================== 
# Game_Map 
#============================================================================== 

class Game_Map
        
  def leximus
    return $map_lex[@map_id]
  end
   
  def name
    return CP.map_name
  end
   
end

#==============================================================================
# Bitmap
#==============================================================================

class Bitmap
  
  alias draw_text_shaded draw_text
  def draw_text(x2, y2, w2 = 0, h2 = 0, text2 = '', a2 = 0)
    if x2.is_a?(Rect)
      x, y, w, h, text, a = x2.x, x2.y, x2.width, x2.height, y2, w2
    else
      x, y, w, h, text, a = x2, y2, w2, h2, text2, a2
    end
    if $scene.is_a?(Scene_Menu) && self.font.color == normal_color &&
        ($game_system.black_back || LIGHT_MODES.include?($game_system.menu_mode))
      save_color = self.font.color.clone
      self.font.color = Color.new(255, 255, 255, 160)
    else
      save_color, self.font.color = self.font.color.clone, Color.new(0, 0, 0)
    end
    draw_text_shaded(x+1, y+1, w, h, text, a)
    self.font.color = save_color
    draw_text_shaded(x, y, w, h, text, a)
  end
  
  def draw_text_outline(x2, y2, w2 = 0, h2 = 0, text2 = '', a2 = 0)
    if x2.is_a?(Rect)
      x, y, w, h, text, a = x2.x, x2.y, x2.width, x2.height, y2, w2
    else
      x, y, w, h, text, a = x2, y2, w2, h2, text2, a2
    end
    if $scene.is_a?(Scene_Menu) && self.font.color == normal_color &&
        ($game_system.black_back || LIGHT_MODES.include?($game_system.menu_mode))
      save_color = self.font.color.clone
      self.font.color = Color.new(255, 255, 255, 160)
    else
      save_color, self.font.color = self.font.color.clone, Color.new(0, 0, 0)
    end
    draw_text_shaded(x-1, y-1, w, h, text, a)
    draw_text_shaded(x-1, y+1, w, h, text, a)
    draw_text_shaded(x+1, y-1, w, h, text, a)
    draw_text_shaded(x+1, y+1, w, h, text, a)
    self.font.color = save_color
    draw_text_shaded(x, y, w, h, text, a)
  end
  
  def normal_color
    if $scene.is_a?(Scene_Menu) && ($game_system.black_back ||
        LIGHT_MODES.include?($game_system.menu_mode))
      return Color.new(0, 0, 0)
    else
      return Color.new(255, 255, 255)
    end
  end
  
  def draw_element_graph(x_plus, y_plus, rad, color, limit = -1)
    (-rad-1...0).each {|r| (r...0).each {|x|
        color.alpha = 255 * (rad+1.0-r.abs)/(rad+1)
        y = (r.abs * Math.sin(Math.acos(x/r.to_f))).to_i
        h = y * 2
        case limit
        when 1, 8 then h = (y < x.abs ? 0 : y - x.abs)
        when 2, 7 then y > x.abs ? h = y = x.abs : h = y
        when 3, 6
          y > x.abs ? h = y = x.abs : h = y
          y = 0 if y > 0
        when 4, 5
          h = (y < x.abs ? 0 : y - x.abs)
          y = -x.abs
        end
        if limit < 5
          fill_rect(rad*2-x + x_plus, rad-y + y_plus, 1, h, color)
        else
          fill_rect(rad*2+x+1 + x_plus, rad-y + y_plus, 1, h, color)
        end}}
  end
  
  def slice_bitmap(input)
    (0...input.length).each {|i|
        return [input[0, i], input[i+1, input.length-i-1]] if input[i, 1] == '/'}
    return [input, ''] if text_size(input).width < 140
    pos1 = input.length/2 - 1
    pos2 = input.length/2
    str1 = str2 = ''
    loop do
      if input[pos2, 1] == ' '
        str1 = input[0, pos2]
        str2 = input[pos2+1, input.length-pos1-1]
        break
      end
      if input[pos1, 1] == ' '
        str1 = input[0, pos1]
        str2 = input[pos1+1, input.length-pos1-1]
        break
      end
      pos1 -= 1
      pos2 += 1
      if pos1 == 0 || pos2 == input.length-1
        str1 = input
        str2 = ''
        break
      end
    end
    return [str1, str2]
  end
  
end

#============================================================================== 
# Window_Base 
#============================================================================== 

class Window_Base < Window 
  
  attr_accessor :sprites
  attr_accessor :sx
  attr_accessor :sy
  
  alias cms_hybrid_hack_init initialize
  def initialize(xx, yy, w, h)
    cms_hybrid_hack_init(xx, yy, w, h)
    if @background != nil
      @backsprite = Sprite.new
      @backsprite.x, @backsprite.y = self.x, self.y
      cache_sprite
    end
  end
  
  def draw_actor_face(actor, x, y)
    if actor != nil && actor.battler_name != ''
      if actor.dead?
        bitmap = RPG::Cache.character('Faces/invs/' + actor.battler_name, actor.battler_hue)
      else
        bitmap = RPG::Cache.character('Faces/' + actor.battler_name, actor.battler_hue)
      end
      cw, ch = bitmap.width, bitmap.height
      self.contents.blt(x+16, y+16, bitmap, Rect.new(0, 0, cw, ch))
    end
  end

  def draw_actor_battler(actor, x, y)
    if actor != nil && actor.battler_name != ''
      if actor.dead?
        bitmap = RPG::Cache.battler('invs/'+actor.battler_name, actor.battler_hue)
      else
        bitmap = RPG::Cache.battler(actor.battler_name, actor.battler_hue)
      end
      cw, ch = bitmap.width, bitmap.height
      self.contents.blt(x - cw / 2, y - ch, bitmap, Rect.new(0, 0, cw, ch))
    end
  end
  
  def draw_actor_name2(actor, x, y, w, a = 1)
    save_font = self.contents.font.name
    self.contents.font.name = 'EurostileExtended-Roman-DTC'
    self.contents.font.size = 18
    self.contents.font.bold = true
    self.contents.font.italic = true
    self.contents.font.color = (actor.dead? ? down_color : normal_color)
    self.contents.draw_text(x, y, w, 36, actor.name, a)
    self.contents.font.italic = false
    self.contents.font.bold = false unless save_font == 'Papyrus'
    self.contents.font.name = save_font 
    self.contents.font.size = (save_font == 'Papyrus' ? 28 : 22)
    self.contents.font.color = normal_color
  end
  
  def draw_actor_sr(actor, x, y, width = 144)
    self.contents.font.color = normal_color
    self.contents.draw_text(x, y, width, 32, "#{actor.sr/10},#{actor.sr%10}%", 2)
    self.contents.font.color = system_color
    self.contents.draw_text(x, y-16, width - 4, 64, 'SR', 0)
  end

  def up_color
    return Color.new(0, 240, 0)
  end
 
  def down_color
    return Color.new(240, 0, 0)
  end
  
  def draw_actor_element_vulnerability(actor, x, y, rad = 60)
    colors = []
    (1..8).each {|i|
        rate = actor.element_rate(i)
        if rate < 0
          colors.push(Color.new(0, 255 * (100-rate.abs) / 200, 255))
        elsif rate == 0
          colors.push(Color.new(0, 128, 255))
        elsif rate <= 50
          colors.push(Color.new(0, 255 * (rate+50) / 100, 255 * (50-rate) / 50))
        elsif rate <= 100
          colors.push(Color.new(255 * (rate-50) / 50 , 255, 0))
        elsif rate <= 200
          colors.push(Color.new(255, 255 * (200-rate) / 100, 0))
        else
          colors.push(normal_color)
        end}
    (1..8).each {|i|
        self.contents.draw_element_graph(x + 16, y + 32, rad, colors[i-1], i)}
    save_color = self.contents.font.color.clone
    (1..8).each {|i|
        str1 = $data_system.elements[i]
        rate = actor.element_rate(i)
        rate /= 10 if rate < -200
        str2 = "#{rate}%"
        w1 = self.contents.text_size(str1).width
        w2 = self.contents.text_size(str2).width
        case i
        when 1 then x2, y2, x3, y3 = x+152,    y+20,  x+168,    y+4
        when 2 then x2, y2, x3, y3 = x+176,    y+56,  x+192,    y+40
        when 3 then x2, y2, x3, y3 = x+176,    y+92,  x+192,    y+108
        when 4 then x2, y2, x3, y3 = x+152,    y+128, x+168,    y+144
        when 5 then x2, y2, x3, y3 = x+120-w1, y+128, x+104-w2, y+144
        when 6 then x2, y2, x3, y3 = x+96-w1,  y+92,  x+80-w2,  y+108
        when 7 then x2, y2, x3, y3 = x+96-w1,  y+56,  x+80-w2,  y+40
        when 8 then x2, y2, x3, y3 = x+120-w1, y+20,  x+104-w2, y+4
        end
        self.contents.font.color = save_color
        self.contents.draw_text(x2, y2, w1, 32, str1)
        self.contents.font.color = colors[i-1]
        self.contents.draw_text(x3, y3, w2, 32, str2)}
    self.contents.font.color = save_color
  end
  
  def normal_color
    if $scene.is_a?(Scene_Menu) && ($game_system.black_back ||
        LIGHT_MODES.include?($game_system.menu_mode))
      return Color.new(0, 0, 0)
    else
      return Color.new(255, 255, 255)
    end
  end

  def system_color
    if $scene.is_a?(Scene_Menu) && ($game_system.black_back ||
        LIGHT_MODES.include?($game_system.menu_mode))
      return Color.new(64, 128, 255)
    else
      return Color.new(128, 192, 255)
    end
  end

  def disabled_color
    if $scene.is_a?(Scene_Menu) && ($game_system.black_back ||
        LIGHT_MODES.include?($game_system.menu_mode))
      return Color.new(128, 128, 128)
    else
      return Color.new(255, 255, 255, 128)
    end
  end
  
  def crisis_color
    if $scene.is_a?(Scene_Menu) && ($game_system.black_back ||
        LIGHT_MODES.include?($game_system.menu_mode))
      return Color.new(192, 192, 0)
    else
      return Color.new(255, 255, 0)
    end
  end
  
  alias cms_hybrid_hack_x_ x=
  def x=(xx)
    cms_hybrid_hack_x_(xx)
    @backsprite.x = xx unless @backsprite == nil || @backsprite.disposed?
  end
  
  alias cms_hybrid_hack_y_ y=
  def y=(yy)
    cms_hybrid_hack_y_(yy)
    @backsprite.y = yy unless @backsprite == nil || @backsprite.disposed?
  end
  
  alias cms_hybrid_hack_z z=
  def z=(z)
    cms_hybrid_hack_z(z)
    @backsprite.z = z-10 unless @backsprite == nil || @backsprite.disposed?
  end
  
  alias cms_hybrid_hack_visible visible=
  def visible=(expr)
    cms_hybrid_hack_visible(expr)
    @backsprite.visible = expr unless @backsprite == nil || @backsprite.disposed?
  end
  
  alias disp_sprite_later dispose
  def dispose
    @backsprite.dispose unless @backsprite == nil || @backsprite.disposed?
    disp_sprite_later
  end
  
  def cache_sprite
    return if @backsprite == nil
    if $game_system.menu_mode == MODES.size - 1
      if @backsprite.bitmap != nil && !@backsprite.bitmap.disposed?
        @backsprite.bitmap.dispose
        @backsprite.bitmap = nil
      end
    elsif $game_system.menu_mode >= MODES.size
      if @backsprite.bitmap != nil && !@backsprite.bitmap.disposed?
        @backsprite.bitmap.dispose
        @backsprite.bitmap = nil
      end
      tmp = ($game_system.menu_mode - MODES.size + 1).to_s
      if $game_system.test_custom(tmp, true)
        tmp = "back#{$game_system.menu_mode - MODES.size + 1}"
      elsif $game_system.test_custom(tmp, false)
        tmp = "black#{$game_system.menu_mode - MODES.size + 1}"
        $game_system.black_back = true
      end
      if tmp != ($game_system.menu_mode - MODES.size + 1).to_s
        @backsprite.bitmap = RPG::Cache.custom_back(tmp)
        @backsprite.src_rect.set(@sx, @sy, self.width, self.height)
      end
    elsif ONE_PIC_MODES.include?($game_system.menu_mode)
      name = MODES[$game_system.menu_mode]
      @backsprite.bitmap = RPG::Cache.picture("Menu/#{name}")
      @backsprite.src_rect.set(@sx, @sy, self.width, self.height)
    else
      name = "Menu/#{@background}#{$game_system.menu_mode}"
      @backsprite.bitmap = RPG::Cache.picture(name)
    end
  end
  
end

#==============================================================================
# Window_HybridCommand
#==============================================================================

class Window_HybridCommand < Window_Command
  
  attr_reader :continue
  
  def initialize(index, continue)
    @background, @continue, @sx, @sy = 'Menu', continue, 460, 0
    commands = [$data_system.words.item, $data_system.words.equip,
          $data_system.words.skill, 'Soul Rage', 'Status']
    commands.push('Options', 'Teleport', 'Load', 'Exit')
    super(180, commands)
    self.index, self.x, self.y, self.z = index, 972, 0, 999
  end
  
  def refresh
    self.contents.font.name = $fontface
    if $fontface == 'Papyrus'
      self.contents.font.size = 28
      self.contents.font.bold = true
    else
      self.contents.font.size = 22
    end
    self.contents.clear
    (0...@item_max).each {|i| draw_item(i, normal_color)}
  end

  def draw_item(i, color)
    self.contents.fill_rect(0, i*32, 148, 32, Color.new(0, 0, 0, 0))
    if color == normal_color
      bitmap = RPG::Cache.icon("Menu/#{i}")
    else
      bitmap = RPG::Cache.desaturated("Menu/#{i}")
    end
    self.contents.blt(4, 4 + i*32, bitmap, Rect.new(0, 0, 24, 24))
    self.contents.font.color = color
    self.contents.draw_text(32, i*32, 148, 32, @commands[i])
  end
  
end

#==============================================================================
# Window_HybridChooseItem
#==============================================================================

class Window_HybridChooseItem < Window_HCommand
  
  def initialize
    @background, @sx, @sy = 'Help', 0, 0
    super(152, ['Items', 'Sort', 'Equipment', 'Quest Items'])
    self.x, self.y = 0, -576
    @item_max = @column_max = @commands.size
    self.contents = Bitmap.new(width - 32, 32)
    self.contents.font.name = $fontface
    if $fontface == 'Papyrus'
      self.contents.font.size = 28
      self.contents.font.bold = true
    else
      self.contents.font.size = 22
    end
    refresh
    self.active, self.z, self.index = true, 2900, 0
  end
  
  def draw_item(i, color = normal_color)
    w = self.contents.width / @column_max
    self.contents.font.color = color
    self.contents.fill_rect(4 + i*w, 0, w, 32, Color.new(0, 0, 0, 0))
    self.contents.draw_text(4 + i*w, 0, w, 32, @commands[i], 1)
  end
  
  def update_cursor_rect
    w = self.contents.width / @column_max
    if @index < 0
      self.cursor_rect.empty
    else
      self.cursor_rect.set(4 + w*@index, 0, w, 32)
    end
  end
  
end

#==============================================================================
# Window_HybridOptions
#==============================================================================

class Window_HybridOptions < Window_Selectable

  attr_accessor :current_font
  attr_accessor :current_skin
  attr_reader   :skin_name
  attr_reader   :font_name
  
  def initialize
    @background, @index, @sx, @sy = 'Menu_back', 0, 0, 0
    @commands = ['BGM Volume', 'SFX Volume', 'Menu Mode', 'Battle BGM',
        'Battle Camera', 'Battle Encounter', 'Unity Force Mode', 'Bar Style',
        'Bar Opacity', 'Font', 'Windowskin']
    @commands.push('Information') if CP.any_info?
    super(0, 512, 640, 480)
    get_skin_and_font
    self.contents = Bitmap.new(width - 32, height - 32)
    self.z = 2999
    @item_max = @commands.size
    refresh
  end
  
  def refresh(index = nil)
    self.contents.font.name = $fontface
    if $fontface == 'Papyrus'
      self.contents.font.size = 28
      self.contents.font.bold = true
    else
      self.contents.font.size = 22
    end
    x = 288
    if index == nil
      self.contents.clear
      @cw = 0
      @commands.each {|com|
          w = self.contents.text_size(com).width
          @cw = w if @cw < w}
      draw_volume(x, 4)
      draw_volume(x, 32, true)
      draw_menu(x, 60)
      draw_battle_bgm(x, 88)
      draw_battle_cam(x, 116)
      draw_battle_enc(x, 144)
      draw_battle_uf(x, 172)
      draw_style(x, 200)
      draw_opacity(x, 228)
      draw_font(x, 256)
      draw_skin(x, 284)
      self.contents.font.color = normal_color
      (0...@item_max).each {|i| self.contents.draw_text(24, i*28, 192, 32, @commands[i])}
      self.contents.draw_text(0, self.height - 56, 320, 32, CP.ver)
    else
      self.contents.fill_rect(Rect.new(x-32, 4+index*28, 320, 30), Color.new(0, 0, 0, 0))
      case index
      when 0 then draw_volume(x, 4+index*28)
      when 1 then draw_volume(x, 4+index*28, true)
      when 2 then draw_menu(x, 4+index*28)
      when 3 then draw_battle_bgm(x, 4+index*28)
      when 4 then draw_battle_cam(x, 4+index*28)
      when 5 then draw_battle_enc(x, 4+index*28)
      when 6 then draw_battle_uf(x, 4+index*28)
      when 7 then draw_style(x, 4+index*28)
      when 8 then draw_opacity(x, 4+index*28)
      when 9 then draw_font(x, 4+index*28)
      when 10 then draw_skin(x, 4+index*28)
      end
    end
  end
  
  def draw_arrows(x, y, width)
    self.contents.font.size += 12
    off = CP::Cache::FontOffsets[self.contents.font.name]
    off = 8 if off == nil
    self.contents.draw_text(x - 20, y-off, 32, 32, '«')
    self.contents.draw_text(x + width + 13, y-off, 32, 32, '»')
    self.contents.font.size -= 12
  end
  
  def draw_volume(x, y, mode = false, width = 224)
    self.contents.font.color = normal_color
    draw_arrows(x, y, width)
    vol = (mode ? $game_system.sfx_volume : $game_system.bgm_volume).to_f / 100
    color1 = Color.new(20, 40, 80)
    color2 = Color.new(60, 120, 240)
    color3 = Color.new(0, 0, 80)
    old = $game_system.bar_opacity
    $game_system.bar_opacity = 255
    self.contents.gradient_bar(x, y-16, width, color1, color2, color3, vol)
    $game_system.bar_opacity = old
  end
  
  def draw_menu(x, y, width = 224)
    self.contents.font.color = normal_color
    draw_arrows(x, y, width)
    if $game_system.menu_mode >= MODES.size
      diff = $game_system.menu_mode - MODES.size + 1
      self.contents.draw_text(x, y-3, 224, 32, "Custom #{diff}", 1)
    else
      self.contents.draw_text(x, y-3, 224, 32, MODES[$game_system.menu_mode], 1)
    end
  end
  
  def draw_style(x, y, width = 224)
    self.contents.font.color = normal_color
    draw_arrows(x, y, width)
    color1 = Color.new(80, 80, 0)
    color2 = Color.new(240, 240, 0)
    color3 = Color.new(80, 80, 0)
    self.contents.gradient_bar(x + 32, y - 16, width - 64, color1, color2, color3, 0.6)
  end
  
  def draw_battle_bgm(x, y, width = 224)
    self.contents.font.color = normal_color
    draw_arrows(x, y, width)
    if $game_switches[BGM_Lock]
      case $game_system.battle_bgm.name
      when 'On the run' then bgm = 'On the run'
      when 'Limited Time' then bgm = 'Limited Time'
      when 'No time to lose' then bgm = 'No time to lose'
      when 'underground church' then bgm = 'Devil\'s Church'
      when 'hyperion showdown' then bgm = 'Hyperion Showdown'
      when 'kn_12_new' then bgm = 'KNight Blade'
      when 'PWAA - Cornered (RMX)' then bgm = 'Last Hope'
      when 'under_siege' then bgm = 'Under Siege'
      when 'Dark Tranquillity - Format C for Cortex (Blizzard Short Cut)'
        bgm = 'Final Decision'
      when 'cyberhellfire' then bgm = 'Cyber Hellfire'
      when 'Technosoft - Thunder Force IV (Blizzard Remake)'
        bgm = 'Thunder Force IV'
      else
        bgm = 'NO NAME'
      end
      self.contents.font.color = disabled_color
    else
      case $game_variables[BGM]
      when 0 then bgm = 'Standard'
      when 1 then bgm = 'The Map'
      when 2 then bgm = 'Lufia Boss'
      when 3 then bgm = 'Astral Chaos'
      when 4 then bgm = 'Mana Beast'
      when 5 then bgm = 'Tranced Pandemonium'
      when 6 then bgm = 'KNight Blade'
      when 7 then bgm = 'Under Siege'
      when 8 then bgm = 'Devil\'s Church'
      when 9 then bgm = 'Underworld Battle'
      when 10 then bgm = 'God of Hell'
      when 11 then bgm = 'VS. Hellvoid'
      else
        bgm = 'NO NAME'
      end
      if !$game_temp.event_menu
        self.contents.font.color = normal_color
      else
        self.contents.font.color = disabled_color
      end
    end
    self.contents.draw_text(x, y-3, 224, 32, bgm, 1)
  end
  
  def draw_battle_cam(x, y, width = 224)
    self.contents.font.color = normal_color
    draw_arrows(x, y, width)
    cam = ($game_variables[CAM] == 0 ? 'ON' : 'OFF')
    self.contents.draw_text(x, y-3, 224, 32, cam, 1)
  end
  
  def draw_battle_enc(x, y, width = 224)
    self.contents.font.color = normal_color
    draw_arrows(x, y, width)
    case $game_system.encounter_mode
    when 0 then mode = 'Prompt me'
    when 1 then mode = 'Always evade'
    when 2 then mode = 'Always engage'
    end
    self.contents.draw_text(x, y-3, 224, 32, mode, 1)
  end
  
  def draw_battle_uf(x, y, width = 224)
    self.contents.font.color = normal_color
    draw_arrows(x, y, width)
    if $game_system.uf_mode
      mode = 'Manual'
    else
      mode = 'Automatic'
    end
    self.contents.draw_text(x, y-3, 224, 32, mode, 1)
  end
  
  def draw_opacity(x, y, width = 224)
    self.contents.font.color = normal_color
    draw_arrows(x, y, width)
    case $game_system.bar_opacity
    when 0 then alpha = 'No bar'
    when 64 then alpha = 'Light'
    when 128 then alpha = 'Medium'
    when 192 then alpha = 'Hard'
    when 256 then alpha = 'Full'
    end
    self.contents.draw_text(x, y-3, 224, 32, alpha, 1)
  end
  
  def draw_font(x, y, width = 224)
    self.contents.font.color = normal_color
    draw_arrows(x, y, width)
    @font_name = CP::Cache::Fonts[@current_font]
    self.contents.font.name = @font_name
    old_bold = self.contents.font.bold
    if self.contents.font.name == 'Papyrus'
      self.contents.font.size = 28
      self.contents.font.bold = true
    else
      self.contents.font.size = 22
      self.contents.font.bold = false
    end
    self.contents.draw_text(x, y-3, 224, 32, @font_name, 1)
    self.contents.font.bold = old_bold
    self.contents.font.name = $fontface
    self.contents.font.size = ($fontface == 'Papyrus' ? 28 : 22)
  end
  
  def draw_skin(x, y, width = 224)
    self.contents.font.color = normal_color
    draw_arrows(x, y, width)
    @skin_name = CP::Cache::Skins[@current_skin]
    self.contents.draw_text(x, y-3, 224, 32, @skin_name, 1)
    if $fontface == 'Papyrus'
      self.contents.font.size = 28
      self.contents.font.bold = true
    else
      self.contents.font.size = 22
    end
    self.contents.fill_rect(x + 48, y + 28, 128, 128, Color.new(0, 0, 0, 0))
    bitmap = RPG::Cache.windowskin(@skin_name)
    self.contents.blt(x+50, y+30, bitmap, Rect.new(2, 2, 124, 124))
    self.contents.blt(x+48, y+28, bitmap, Rect.new(128, 0, 16, 16))
    self.contents.blt(x+160, y+28, bitmap, Rect.new(176, 0, 16, 16))
    self.contents.blt(x+48, y+140, bitmap, Rect.new(128, 48, 16, 16))
    self.contents.blt(x+160, y+140, bitmap, Rect.new(176, 48, 16, 16))
    (2..4).each {|i|
        self.contents.blt(x+i*32, y+28, bitmap, Rect.new(144, 0, 32, 16))}
    (2..4).each {|i|
        self.contents.blt(x+i*32, y+140, bitmap, Rect.new(144, 48, 32, 16))}
    (2..4).each {|i|
        self.contents.blt(x+48, y+i*32-20, bitmap, Rect.new(128, 16, 16, 32))}
    (2..4).each {|i|
        self.contents.blt(x+160, y+i*32-20, bitmap, Rect.new(176, 16, 16, 32))}
  end
  
  def get_skin_and_font
    @font_name = $fontface
    @current_font = CP::Cache::Fonts.index(@font_name)
    @current_font = 0 if @current_font == nil
    @skin_name = $scene.windowskin
    @current_skin = CP::Cache::Skins.index(@skin_name)
    @current_skin = 0 if @current_skin == nil
  end
  
  def update_cursor_rect
    if !self.active
      self.cursor_rect.empty 
    elsif self.index >= 0
      self.cursor_rect.set(18, @index * 28, @cw + 16, 32)
    elsif self.index >= -1
      self.cursor_rect.set(18, 28, @cw + 16, 32)
    end
  end
  
end

#==============================================================================
# Window_HybridTarget
#==============================================================================

class Window_HybridTarget < Window_Selectable

  def initialize(actor)
    @background, @actor, @sx, @sy = 'Target', actor, 0, 64
    super(-304, 64, 256, 416)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.contents.font.name = $fontface
    if $fontface == 'Papyrus'
      self.contents.font.size = 28
      self.contents.font.bold = true
    else
      self.contents.font.size = 22
    end
    self.z = 3999
    @item_max = $game_party.actors.size
    refresh
  end

  def refresh
    self.contents.clear
    if @index == -2
      draw_actor_name(@actor, 4, @actor.index*96)
      draw_actor_state(@actor, 100, @actor.index*96, 112)
      draw_actor_hp(@actor, 44, 28 + @actor.index*96)
      draw_actor_sp(@actor, 44, 56 + @actor.index*96)
    else
      (0...$game_party.actors.size).each {|i|
          draw_actor_name($game_party.actors[i], 4, i*96)
          draw_actor_state($game_party.actors[i], 100, i*96, 112)
          draw_actor_hp($game_party.actors[i], 44, 28 + i*96)
          draw_actor_sp($game_party.actors[i], 44, 56 + i*96)}
    end
  end

  def update_actor(actor)
    @actor = actor
    refresh
  end
  
  def update_cursor_rect
    if !self.active
      self.cursor_rect.empty
    elsif self.index >= 0
      self.cursor_rect.set(0, @index * 96, self.width - 32, 96)
    elsif self.index >= -1
      self.cursor_rect.set(0, 0, self.width - 32, self.height - 32)
    end
  end
  
end

#==============================================================================
# Window_Help
#==============================================================================

class Window_Help < Window_Base
  
  def initialize(flag = true, sy = 0)
    @background = 'Help' if $scene.is_a?(Scene_Menu) if flag
    @sx, @sy = 0, sy
    super(0, 0, 640, ($scene.is_a?(Scene_Battle) ? 88 : 64))
    @color = normal_color
    self.contents = Bitmap.new(width - 32, height - 32)
    self.opacity = 0 if $scene.is_a?(Scene_Battle) || $scene.is_a?(Scene_Shop)
    refresh
  end
  
  def set_text(text, align = 0, color = normal_color, text2 = nil)
    if text != @text || align != @align || @color != color
      self.contents.clear
      self.contents.font.color = color
      if $scene.is_a?(Scene_Battle) || $scene.is_a?(Scene_Shop)
        self.contents.fill_rect(0, 0, width, 32, Color.new(0, 0, 0, 160))
      end
      self.contents.draw_text(4, 0, self.width - 40, 32, text, align)
      @text, @align, @color, @actor, @enemy = text, align, color, nil, nil
      if @text2 != text2 && text2 != nil && text2 != ''
        self.contents.font.color = normal_color
        if $scene.is_a?(Scene_Battle) || $scene.is_a?(Scene_Shop)
          self.contents.fill_rect(0, 32, width, 24, Color.new(0, 0, 0, 160))
        end
        self.contents.font.size -= 2
        self.contents.draw_text(4, 24, self.width - 40, 32, text2, @align)
        self.contents.font.size += 2
      end
      @text2 = @text2
    end
    self.visible = true
  end
  
  def set_actor(actor)
    if actor != @actor
      self.contents.clear
      if $scene.is_a?(Scene_Battle) || $scene.is_a?(Scene_Shop)
        self.contents.fill_rect(0, 0, width, 32, Color.new(0, 0, 0, 160))
      end
      draw_actor_name(actor, 4, 0)
      draw_actor_state(actor, 140, 0)
      draw_actor_hp(actor, 284, 0)
      draw_actor_sp(actor, 460, 0)
      @actor = actor
      @enemy = @text = nil
      self.visible = true
    end
  end

  def set_enemy(enemy)
    if enemy != @enemy || self.visible == false
      self.contents.clear
      if $scene.is_a?(Scene_Battle) || $scene.is_a?(Scene_Shop)
        self.contents.fill_rect(0, 0, width, 32, Color.new(0, 0, 0, 160))
      end
      text = enemy.name
      hp = (enemy.id != 48 ? enemy.hp : (enemy.hp - 400000))
      maxhp = (enemy.id != 48 ? enemy.maxhp : 100000)
      s = self.contents.text_size(text).width + 16
      w = self.width-40-s
      x = (self.width-40+s)/2 - enemy.states.size * 14
      x = s if x < s
      state_text = make_battler_state_text(enemy, w, true, x, y)
      text += "   »#{state_text}«" if state_text != ''
      self.contents.font.color = normal_color
      s = self.contents.text_size(text).width
      states = enemy.states.clone
      states.each {|id|
          if CP::Cache::SuperStates.include?($data_states[id].name)
            states.clear
            break
          end}
      x = (self.width-40-s)/2
      x -= states.size * 14 + 16 if states.size > 0
      x = 4 if x < 4
      self.contents.draw_text(x, 0, s + 8, 32, text, 1)
      @enemy = enemy
      @actor = nil
      @text = nil
      self.visible = true
    end
  end
  
  def refresh
    self.contents.font.name = $fontface
    if $fontface == 'Papyrus'
      self.contents.font.size = ($scene.is_a?(Scene_Menu) ? 28 : 30)
      self.contents.font.bold = true
    else
      self.contents.font.size = ($scene.is_a?(Scene_Menu) ? 22 : 24)
    end
  end
  
end

#==============================================================================
# Window_HybridItem
#==============================================================================

class Window_HybridItem < Window_Selectable
  
  def initialize
    @background, @sx, @sy = 'Grand', 256, 64
    super(256, -512, 384, 416)
    self.active, self.visible, self.z, self.index = false, false, 2999, -1
    refresh
  end

  def data
    return @data[self.index]
  end
  
  def draw_item(i)
    number = case @data[i]
    when RPG::Item then $game_party.item_number(@data[i].id)
    when RPG::Weapon then $game_party.weapon_number(@data[i].id)
    when RPG::Armor then $game_party.armor_number(@data[i].id)
    end
    if !@data[i].is_a?(RPG::Item) || $game_party.item_can_use?(@data[i].id) ||
        @mode == nil
      self.contents.font.color = normal_color
    else
      self.contents.font.color = disabled_color
    end
    self.contents.fill_rect(4, i*32, 352, 32, Color.new(0, 0, 0, 0))
    if self.contents.font.color == normal_color
      bitmap = RPG::Cache.icon(@data[i].icon_name)
    else
      bitmap = RPG::Cache.desaturated(@data[i].icon_name)
    end
    self.contents.blt(4, i*32 + 4, bitmap, Rect.new(0, 0, 24, 24))
    self.contents.draw_text(32, i*32, 212, 32, @data[i].name, 0)
    self.contents.draw_text(300, i*32, 16, 32, ':', 1)
    self.contents.draw_text(308, i*32, 40, 32, number.to_s, 2)
  end

  def update_help
    @help_window.set_text(data == nil ? '' : data.description)
  end
  
end

#==============================================================================
# Window_NormalItem
#==============================================================================

class Window_NormalItem < Window_HybridItem

  attr_accessor :mode
  
  def initialize
    @mode = 0
    super
    self.visible = true
  end

  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    items = CP.resort_items
    @data = []
    (1...items.size).each {|i|
        if $game_party.item_number(items[i].id) > 0 &&
            !(CP::Cache::Trade | CP::Cache::Quest).include?(items[i].id)
          @data.push(items[i])
        end}
    case @mode
    when 1
      @data.sort! {|a, b|
          $game_party.item_number(a.id) <=> $game_party.item_number(b.id)}
    when 2
      @data.sort! {|a, b|
          $game_party.item_number(b.id) <=> $game_party.item_number(a.id)}
    when 3 then @data.sort! {|a, b| a.name <=> b.name}
    when 4 then @data.sort! {|a, b| b.name <=> a.name}
    end
    @item_max = @data.size
    if @item_max > 0
      self.contents = Bitmap.new(width - 32, @item_max * 32)
      self.contents.font.name = $fontface
      if $fontface == 'Papyrus'
        self.contents.font.size = 28
        self.contents.font.bold = true
      else
        self.contents.font.size = 22
      end
      (0...@item_max).each {|i| draw_item(i)}
    end
  end
  
end

#==============================================================================
# Window_EquipmentItem
#==============================================================================

class Window_EquipmentItem < Window_HybridItem

  attr_accessor :mode
  attr_reader   :actor
  
  def initialize
    @mode = 0
    super
    self.visible = true
  end

  def info_position(w)
    return [self.x - w, self.y + self.cursor_rect.y - 40]
  end
  
  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    weapons, armors = CP.resort_weapons, CP.resort_armors
    sweapons, sarmors = [], []
    (1...weapons.size).each {|i|
        sweapons.push(weapons[i]) if $game_party.weapon_number(weapons[i].id) > 0}
    (1...armors.size).each {|i|
        sarmors.push(armors[i]) if $game_party.armor_number(armors[i].id) > 0}
    case @mode
    when 1
      sweapons.sort! {|a, b|
          $game_party.weapon_number(a.id) <=> $game_party.weapon_number(b.id)}
      sarmors.sort! {|a, b|
          $game_party.armor_number(a.id) <=> $game_party.armor_number(b.id)}
    when 2
      sweapons.sort! {|a, b|
          $game_party.weapon_number(b.id) <=> $game_party.weapon_number(a.id)}
      sarmors.sort! {|a, b|
          $game_party.armor_number(b.id) <=> $game_party.armor_number(a.id)}
    when 3
      sweapons.sort! {|a, b| a.name <=> b.name}
      sarmors.sort! {|a, b| a.name <=> b.name}
    when 4
      sweapons.sort! {|a, b| b.name <=> a.name}
      sarmors.sort! {|a, b| b.name <=> a.name}
    end
    @data = sweapons + sarmors
    @item_max = @data.size
    if @item_max > 0
      self.contents = Bitmap.new(width - 32, @item_max * 32)
      self.contents.font.name = $fontface
      if $fontface == 'Papyrus'
        self.contents.font.size = 28
        self.contents.font.bold = true
      else
        self.contents.font.size = 22
      end
      (0...@item_max).each {|i| draw_item(i)}
    end
  end
  
end

#==============================================================================
# Window_QuestItem
#==============================================================================

class Window_QuestItem < Window_HybridItem

  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    @data = []
    ary = CP.resort_items
    (1...ary.size).each {|i|
        if $game_party.item_number(ary[i].id) > 0 && CP::Cache::Quest.include?(ary[i].id)
          @data.push(ary[i])
        end}
    @item_max = @data.size
    if @item_max > 0
      self.contents = Bitmap.new(width - 32, @item_max * 32)
      self.contents.font.name = $fontface
      if $fontface == 'Papyrus'
        self.contents.font.size = 28
        self.contents.font.bold = true
      else
        self.contents.font.size = 22
      end
      (0...@item_max).each {|i| draw_item(i)}
    end
  end

end

#==============================================================================
# Window_HybridSkill
#==============================================================================

class Window_HybridSkill < Window_HybridItem
  
  def initialize(actor)
    @actor = actor
    super()
    self.x, self.y, self.z, self.index = -512, 64, 2999, 0
    self.active = self.visible = true
  end

  def update_actor(actor)
    @actor = actor
    refresh
  end

  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    @data = []
    @actor.skills.each {|id| @data.push($data_skills[id])}
    @item_max = @data.size
    if @item_max > 0
      self.contents = Bitmap.new(width - 32, row_max * 32)
      self.contents.font.name = $fontface
      if $fontface == 'Papyrus'
        self.contents.font.size = 28
        self.contents.font.bold = true
      else
        self.contents.font.size = 22
      end
      (0...@item_max).each {|i| draw_item(i)}
    end
  end

  def draw_item(i)
    self.contents.fill_rect(4, i*32, 352, 32, Color.new(0, 0, 0, 0))
    self.contents.font.color = @actor.skill_can_use?(@data[i].id) ?
        normal_color : disabled_color
    if self.contents.font.color == normal_color
      bitmap = RPG::Cache.icon(@data[i].icon_name)
    else
      bitmap = RPG::Cache.desaturated(@data[i].icon_name)
    end
    self.contents.blt(4, 4 + i*32, bitmap, Rect.new(0, 0, 24, 24))
    self.contents.draw_text(32, i*32, 204, 32, @data[i].name, 0)
    if @data[i].sp_cost > 0
      sp_cost = (@data[i].sp_cost/(@actor.states.include?(31) ? 2.0 : 1)).ceil
      self.contents.draw_text(292, i*32, 48, 32, sp_cost.to_s, 2)
    end
  end

end

#==============================================================================
# Window_HybridEquipLeft
#==============================================================================

class Window_HybridEquipLeft < Window_Base
  
  attr_accessor :mode
  attr_accessor :current
  attr_accessor :changed
  
  def initialize(actor)
    @background, @sx, @sy = 'eq_left', 0, 64
    super(640, 64, 288, 416)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.contents.font.name = $fontface
    if $fontface == 'Papyrus'
      self.contents.font.size = 28
      self.contents.font.bold = true
    else
      self.contents.font.size = 22
    end
    @elements, @states, @actor, @mode, self.z = [], [], actor, 0, 2999
    @current = @changed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    refresh
  end
  
  def update_actor(actor)
    @actor = actor
    refresh
  end
  
  def draw_actor_hp(actor, x, y, width = 144)
    self.contents.font.color = system_color
    self.contents.draw_text(x, y, 96, 32, "max #{$data_system.words.hp}")
    self.contents.font.color = normal_color
    self.contents.draw_text(x + 128, y, 44, 32, actor.maxhp.to_s, 2)
  end
  
  def draw_actor_sp(actor, x, y, width = 144)
    self.contents.font.color = system_color
    self.contents.draw_text(x, y, 96, 32, "max #{$data_system.words.sp}")
    self.contents.font.color = normal_color
    self.contents.draw_text(x + 128, y, 44, 32, actor.maxsp.to_s, 2)
  end
  
  def element_states_refresh
    self.contents.fill_rect(4, 276, 256, 108, Color.new(0, 0, 0, 0))
    if @mode == 0
      self.contents.font.color = up_color
      self.contents.draw_text(4, 276, 200, 32, 'Elemental Attack:')
      self.contents.draw_text(4, 324, 200, 32, 'Status Attack:')
    elsif @mode == 1
      self.contents.font.color = up_color
      self.contents.draw_text(4, 276, 200, 32, 'Elemental Resistance:')
      self.contents.draw_text(4, 324, 200, 32, 'Status Resistance:')
    end
    self.contents.font.color = normal_color
    draw_elements(4, 300)
    draw_states(4, 348)
  end
  
  def refresh
    self.contents.clear
    draw_actor_name(@actor, 4, 0)
    draw_actor_level(@actor, 180, 0)
    draw_actor_hp(@actor, 4, 28)
    draw_actor_sp(@actor, 4, 52)
    (0...8).each {|i| draw_actor_parameter(@actor, 4, 76 + i*24, i)}
    element_states_refresh
    (0...@current.size).each {|i|
        val = @current[i] - @changed[i]
        if val != 0
          self.contents.font.color = system_color
          self.contents.draw_text(164, 28+i*24, 38, 32, '»»', 2)
          self.contents.font.color = (val > 0 ? down_color : up_color)
          self.contents.draw_text(200, 28+i*24, 52, 32, @changed[i].abs.to_s, 2)
        end}
  end
  
  def set_new_parameters(elements, states)
    @elements, @states = elements, states
  end
  
  def draw_elements(x, y)
    if @elements.all? {|i| i < 10}
      (0...@elements.size).each {|i|
          icon = RPG::Cache.icon("elm_#{$data_system.elements[@elements[i]].downcase}")
          rect = Rect.new(0, 0, 24, 24)
          self.contents.blt(x + i*28, y + 4, icon, rect)}
    else
      i = 0
      @elements.each {|elm|
          if elm > 9
            if @elements.include?(elm-9)
              icon = RPG::Cache.icon("elm_#{$data_system.elements[elm].downcase}2")
            else
              icon = RPG::Cache.icon("elm_#{$data_system.elements[elm].downcase}")
            end
            self.contents.blt(x + i*28, y + 4, icon, Rect.new(0, 0, 24, 24))
            i += 1
          end}
    end
  end
  
  def draw_states(x, y)
    (0...@states.size).each {|i|
        icon = RPG::Cache.icon("stat_#{$data_states[@states[i]].name.downcase}")
        self.contents.blt(x + i*28, y + 4, icon, Rect.new(0, 0, 24, 24))}
  end
  
end
  
#==============================================================================
# Window_HybridEquipRight
#==============================================================================

class Window_HybridEquipRight < Window_Selectable
  
  attr_reader :actor
  
  def initialize(actor)
    @background, @sx, @sy = 'eq_right', 288, 64
    super(928, 64, 352, 256)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.contents.font.name = $fontface
    if $fontface == 'Papyrus'
      self.contents.font.size = 28
      self.contents.font.bold = true
    else
      self.contents.font.size = 22
    end
    @actor, self.active, self.z, self.index = actor, true, 2999, 0
    refresh
  end

  def data
    return @data[self.index]
  end
  
  def info_position(w)
    return [(self.x == 928 ? 288 : self.x) - w, self.y + self.cursor_rect.y + 48]
  end
  
  def update_actor(actor)
    @actor = actor
    refresh
  end

  def refresh
    self.contents.clear
    @data = [$data_weapons[@actor.weapon_id]]
    if CP::Cache::Lucius.include?(@actor.id)
      @data.push($data_weapons[@actor.armor1_id])
    else
      @data.push($data_armors[@actor.armor1_id])
    end
    @data.push($data_armors[@actor.armor2_id], $data_armors[@actor.armor3_id],
               $data_armors[@actor.armor4_id], $data_armors[@actor.armor5_id],
               $data_armors[@actor.armor6_id])
    @item_max = @data.size
    self.contents.font.color = system_color
    self.contents.draw_text(4, 0, 88, 32, $data_system.words.weapon)
    if CP::Cache::Endout.include?(@actor.id)
      self.contents.draw_text(4, 32, 88, 32, 'Add-on')
    elsif @actor.id == 6
      self.contents.draw_text(4, 32, 88, 32, 'Gun')
    elsif CP::Cache::Lucius.include?(@actor.id)
      self.contents.draw_text(4, 32, 88, 32, $data_system.words.weapon)
    else
      self.contents.draw_text(4, 32, 88, 32, $data_system.words.armor1)
    end
    self.contents.draw_text(4, 64, 88, 32, $data_system.words.armor2)
    self.contents.draw_text(4, 96, 88, 32, $data_system.words.armor3)
    (4...7).each {|i|
        self.contents.draw_text(4, i*32, 88, 32, "#{$data_system.words.armor4[0, 6]}.")}
    (0...7).each {|i| draw_item_name(@data[i], 88, i*32)}
    if CP::Cache::Lucius.include?(@actor.id) && CP::Cache::TwoHanded.include?(@actor.weapon_id)
      bitmap = RPG::Cache.desaturated($data_weapons[@actor.weapon_id].icon_name)
      self.contents.blt(88, 36, bitmap, Rect.new(0, 0, 24, 24))
      self.contents.font.color = disabled_color
      self.contents.draw_text(116, 32, 200, 32, $data_weapons[@actor.weapon_id].name)
    end
  end

  def draw_item_name(item, x, y, color = normal_color)
    if item != nil
      bitmap = RPG::Cache.icon(item.icon_name)
      self.contents.blt(x, y + 4, bitmap, Rect.new(0, 0, 24, 24))
      self.contents.font.color = normal_color
      self.contents.draw_text(x + 28, y, 200, 32, item.name)
    end
  end
  
  def update_help
    @help_window.set_text(data == nil ? '' : data.description)
  end
  
end

#==============================================================================
# Window_HybridEquipItem
#==============================================================================

class Window_HybridEquipItem < Window_Selectable
  
  def initialize(actor, equip_type)
    @background, @sx, @sy = 'eq_item', 288, 320
    super(928, 320, 352, 160)
    self.active = self.visible = false
    @actor, @equip_type, self.z, self.index = actor, equip_type, 3000, -1
    refresh
  end
  
  def data
    return @data[self.index]
  end
  
  def actor
    return nil
  end
  
  def info_position(w)
    return [self.x - w, self.y + self.cursor_rect.y - 40]
  end
  
  def update_actor(actor)
    @actor = actor
    self.index = 0
    self.update_cursor_rect
    self.index = -1
    self.update_cursor_rect
    refresh
  end
  
  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    @data = []
    if @equip_type == 0
      ary = CP.resort_weapons
      (1...ary.size).each {|i|
          if $game_party.weapon_number(ary[i].id) > 0 &&
              $data_classes[@actor.class_id].weapon_set.include?(ary[i].id)
            @data.push(ary[i])
          end}
    else
      ary = CP.resort_armors
      (1...ary.size).each {|i|
          if $game_party.armor_number(ary[i].id) > 0 &&
              $data_classes[@actor.class_id].armor_set.include?(ary[i].id)
            @data.push(ary[i]) if ary[i].kind == @equip_type-1
          end}
    end
    @data.push(nil)
    @item_max = @data.size
    self.contents = Bitmap.new(width - 32, @item_max * 32)
    self.contents.font.name = $fontface
    if $fontface == 'Papyrus'
      self.contents.font.size = 28
      self.contents.font.bold = true
    else
      self.contents.font.size = 22
    end
    (0...@item_max-1).each {|i| draw_item(i)}
    self.contents.font.color = system_color
    self.contents.draw_text(4, (@item_max-1)*32, 128, 32, '<Unequip>')
  end

  def draw_item(i)
    number = case @data[i]
    when RPG::Weapon then $game_party.weapon_number(@data[i].id)
    when RPG::Armor then $game_party.armor_number(@data[i].id)
    end
    self.contents.font.color = normal_color
    bitmap = RPG::Cache.icon(@data[i].icon_name)
    self.contents.blt(4, 4 + i*32, bitmap, Rect.new(0, 0, 24, 24))
    self.contents.draw_text(32, i*32, 272, 32, @data[i].name, 0)
    self.contents.draw_text(264, i*32, 16, 32, ':', 1)
    self.contents.draw_text(272, i*32, 40, 32, number.to_s, 2)
  end

  def update_help
    @help_window.set_text(data == nil ? '' : data.description)
  end
  
end

#==============================================================================
# Window_HybridStatus
#==============================================================================

class Window_HybridStatus < Window_Base
  
  attr_reader :index
  
  def initialize(actor)
    @background, @sx, @sy = 'Menu_back', 0, 0
    super(0, 512, 640, 480)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.contents.font.name = $fontface
    if $fontface == 'Papyrus'
      self.contents.font.size = 28
      self.contents.font.bold = true
    else
      self.contents.font.size = 22
    end
    @item_max, @actor, self.active, self.z, self.index = 2, actor, true, 2999, 0
    refresh
  end

  def index=(index)
    @index = index
    update_cursor_rect
  end
  
  def refresh
    self.contents.clear
    draw_actor_name2(@actor, 224, 2, 120)
    draw_actor_battler(@actor, 284, 248)
    draw_actor_level(@actor, 400, 0)
    self.contents.font.color = normal_color
    self.contents.draw_text(204, 28, 160, 32, $data_classes[@actor.class_id].name, 1)
    draw_actor_state(@actor, 400, 28, 168)
    draw_actor_hp(@actor, 400, 56, 172)
    draw_actor_sp(@actor, 400, 86, 172)
    draw_actor_sr(@actor, 400, 116, 172)
    draw_actor_exp(@actor, 400, 146, 172)
    draw_actor_sr_mode(@actor, 440, 182, 160)
    draw_actor_def_mode(@actor, 440, 210, 160)
    (0...8).each {|i| draw_actor_parameter(@actor, 4, i*28, i)}
    self.contents.font.color = system_color
    w = self.contents.text_size('Elemental vulnerability').width + 4
    self.contents.draw_text(365, 244, w, 32, 'Elemental vulnerability')
    self.contents.font.size -= 4
    draw_actor_element_vulnerability(@actor, 320, 268)
    self.contents.font.size += 4
    self.contents.font.color = system_color
    self.contents.draw_text(4, 244, 112, 32, $data_system.words.weapon)
    if CP::Cache::Endout.include?(@actor.id)
      self.contents.draw_text(4, 272, 112, 32, 'Add-on')
    elsif @actor.id == 6
      self.contents.draw_text(4, 272, 112, 32, 'Gun')
    elsif CP::Cache::Lucius.include?(@actor.id)
      self.contents.draw_text(4, 272, 112, 32, $data_system.words.weapon)
    else
      self.contents.draw_text(4, 272, 112, 32, $data_system.words.armor1)
    end
    self.contents.draw_text(4, 300, 112, 32, $data_system.words.armor2)
    self.contents.draw_text(4, 328, 112, 32, $data_system.words.armor3)
    self.contents.draw_text(4, 356, 112, 32, $data_system.words.armor4)
    self.contents.draw_text(4, 384, 112, 32, $data_system.words.armor4)
    self.contents.draw_text(4, 412, 112, 32, $data_system.words.armor4)
    noequip = 'Nothing equipped'
    if CP::Cache::Lucius.include?(@actor.id)
      equip = $data_weapons[@actor.weapon_id]
      if @actor.equippable?(equip)
        draw_item_name(equip, 116, 244)
      else 
        self.contents.font.color = @actor.equippable?($data_weapons[
            @actor.armor1_id]) ? crisis_color : knockout_color
        self.contents.draw_text(116, 244, 192, 32, noequip)
      end
      equip = $data_weapons[@actor.armor1_id]
      if @actor.equippable?(equip)
        draw_item_name(equip, 116, 272)
      elsif CP::Cache::TwoHanded.include?(@actor.weapon_id)
        weapon = $data_weapons[@actor.weapon_id]
        bitmap = RPG::Cache.desaturated(weapon.icon_name)
        self.contents.blt(116, 276, bitmap, Rect.new(0, 0, 24, 24))
        self.contents.font.color = disabled_color
        self.contents.draw_text(144, 272, 212, 32, weapon.name)
      else
        unless self.contents.font.color == knockout_color
          self.contents.font.color = crisis_color
        end
        self.contents.draw_text(116, 272, 192, 32, noequip)
      end
    else
      equips = [$data_weapons[@actor.weapon_id], $data_armors[@actor.armor1_id]]
      (0...equips.size).each {|i|
          if @actor.equippable?(equips[i])
            draw_item_name(equips[i], 116, 244 + i*28)
          else
            self.contents.font.color = (i == 0 ? knockout_color : crisis_color)
            self.contents.draw_text(116, 244 + i*28, 192, 32, noequip)
          end}
    end
    equips = [$data_armors[@actor.armor2_id], $data_armors[@actor.armor3_id],
              $data_armors[@actor.armor4_id], $data_armors[@actor.armor5_id],
              $data_armors[@actor.armor6_id]]
    (0...equips.size).each {|i|
        if @actor.equippable?(equips[i])
          draw_item_name(equips[i], 116, 300 + i*28)
        else
          self.contents.font.color = crisis_color
          self.contents.draw_text(116, 300 + i*28, 192, 32, noequip)
        end}
  end
  
  def update_actor(actor)
    @actor = actor
    refresh
  end
  
  def update_cursor_rect
    self.cursor_rect.set(440, 182 + self.index * 28, 160, 32)
  end
  
  def update
    super
    if Input.repeat?($controls.down) || Input.repeat?($controls.up)
      $game_system.se_play($data_system.cursor_se)
      self.index = (self.index + 1) % 2
    elsif Input.repeat?($controls.confirm)
      $game_system.se_play($data_system.decision_se)
      if self.index == 0
        @actor.sr_mode = (@actor.sr_mode + 1) % 2
        self.contents.fill_rect(360, 182, 240, 28, Color.new(0, 0, 0, 0))
        draw_actor_sr_mode(@actor, 440, 182, 160)
      else
        @actor.def_mode = (@actor.def_mode + 1) % 4
        self.contents.fill_rect(360, 210, 240, 28, Color.new(0, 0, 0, 0))
        draw_actor_def_mode(@actor, 440, 210, 160)
      end
    end
  end
  
  def draw_actor_sr_mode(actor, x, y, w)
    text = (actor.sr_mode == 0 ? 'Active' : 'Passive')
    self.contents.font.color = system_color
    self.contents.draw_text(x - 80, y, 80, 32, 'SR:', 2)
    self.contents.font.color = normal_color
    self.contents.draw_text(x, y, w, 32, text, 1)
  end
  
  def draw_actor_def_mode(actor, x, y, w)
    test = ''
    default = 'Action:'
    text = case actor.def_mode
    when 0 then 'Fail'
    when 1 then 'Attack'
    when 2 then 'Defend'
    when 3 then 'Despair'
    end
    self.contents.font.color = system_color
    self.contents.draw_text(x - 80, y, 80, 32, default, 2)
    self.contents.font.color = normal_color
    self.contents.draw_text(x, y, w, 32, text, 1)
  end
  
end

#==============================================================================
# Window_HybridSortCommand
#==============================================================================

class Window_HybridSortCommand < Window_Selectable

  def initialize
    @background, @sx, @sy = 'sort', 230, 64
    commands = ['Standard', 'by quantity', 'by alphabet']
    super(230, -128, 180, 128)
    self.z, self.index = 9999, 0
    self.contents = Bitmap.new(width - 32, height - 32)
    self.contents.font.name = $fontface
    if $fontface == 'Papyrus'
      self.contents.font.size = 28
      self.contents.font.bold = true
    else
      self.contents.font.size = 22
    end
    self.contents.font.color = normal_color
    @item_max = 3
    (0...commands.size).each {|i|
        self.contents.draw_text(12, i*32, 136, 32, commands[i])}
  end
  
end

#==============================================================================
# Window_HybridEndCommand
#==============================================================================

class Window_HybridEndCommand < Window_Selectable

  def initialize
    @background, @sx, @sy = 'End', 460, 320
    commands = ['Back to game', 'Back to title', 'Exit game']
    super(460, 480, 180, 160)
    self.z, self.index = 3999, 0
    self.contents = Bitmap.new(width - 32, height - 32)
    self.contents.font.name = $fontface
    if $fontface == 'Papyrus'
      self.contents.font.size = 28
      self.contents.font.bold = true
    else
      self.contents.font.size = 22
    end
    self.contents.font.color = normal_color
    @item_max = 3
    (0...commands.size).each {|i|
        self.contents.draw_text(4, 16 + i*32, 144, 32, commands[i])}
  end
  
  def update_cursor_rect
    if @index < 0
      self.cursor_rect.empty
    else
      self.cursor_rect.set(0, 16 + self.index*32, width - 32, 32)
    end
  end
  
end

#==============================================================================
# Window_HybridInfo
#==============================================================================

class Window_HybridInfo < Window_Base

  def initialize
    @background, @sx, @sy = 'Info', 460, 320
    super(460, 832, 180, 160)
    self.contents = Bitmap.new(width - 32, height - 32)
    refresh
    self.active, self.z = false, 1999
  end

  def refresh
    self.contents.font.name = $fontface
    if $fontface == 'Papyrus'
      self.contents.font.size = 28
      self.contents.font.bold = true
    else
      self.contents.font.size = 22
    end
    self.contents.clear
    refresh_time
    self.contents.font.color = system_color
    cx = contents.text_size($data_system.words.gold).width
    self.contents.draw_text(144-cx, 26, cx, 26, $data_system.words.gold, 2)
    self.contents.draw_text(4, 102, 140, 26, 'Planet:', 0)
    self.contents.font.color = normal_color
    self.contents.draw_text(4, 26, 140-cx-4, 26, $game_party.gold.to_s, 2)
    name = self.contents.slice_bitmap($game_map.name)
    (0..1).each {|i| self.contents.draw_text(4, 52+i*24, 140, 26, name[i])}
    if name.any? {|n| n.clone.gsub!('Hyperion') {''} != nil}
      world_name = '------'
    else
      world_name = case $game_variables[PLANET]
      when 1 then 'Arthia'
      when 2 then 'Kadro'
      else
        '------'
      end
    end
    self.contents.draw_text(4, 102, 140, 26, world_name, 2)
  end
  
  def refresh_time
    @double_sec = Graphics.frame_count * 2 / Graphics.frame_rate
    total_sec = @double_sec / 2
    total_sec = 359999 if total_sec > 359999
    hour, min, sec = total_sec / 60 / 60, total_sec / 60 % 60, total_sec % 60
    if @double_sec % 2 == 1
      text = sprintf('%02d %02d %02d', hour, min, sec)
    else
      text = sprintf('%02d:%02d:%02d', hour, min, sec)
    end
    self.contents.font.color = normal_color
    self.contents.fill_rect(4, 0, 140, 26, Color.new(0, 0, 0, 0))
    self.contents.draw_text(4, 0, 140, 26, text, 1)
  end
  
  def update
    super
    refresh_time if Graphics.frame_count * 2 / Graphics.frame_rate != @double_sec
  end
  
end

#==============================================================================
# Window_HybridMenuStatus
#==============================================================================

class Window_HybridMenuStatus < Window_Selectable
  
  attr_reader :actor
  attr_reader :index
  
  def initialize(actor, index)
    @background, @sx, @sy = 'Status', 0, index * 120
    super(-512-index*128, index*120, 460, 120)
    self.contents = Bitmap.new(width - 32, height - 32)
    @actor = actor
    refresh
    self.active, self.index, self.z = false, -1, 300
  end
  
  def index=(i)
    @index = i
    update_cursor_rect
  end
  
  def refresh
    self.contents.font.name = $fontface
    if $fontface == 'Papyrus'
      self.contents.font.size = 28
      self.contents.font.bold = true
    else
      self.contents.font.size = 22
    end
    self.contents.clear
    draw_actor_face(@actor, 18, 18)
    draw_actor_name2(@actor, 4, 0, 108)
    draw_actor_level(@actor, 120, 0)
    draw_actor_state(@actor, 184, 0, 236, 0)
    draw_actor_hp(@actor, 120, 24)
    draw_actor_sp(@actor, 280, 24)
    draw_actor_sr(@actor, 120, 52)
    draw_actor_exp_alt(@actor, 280, 52)
  end
  
  def update_cursor_rect
    if @index < 0
      self.cursor_rect.empty
    else
      self.cursor_rect.set(0, 0, width - 32, height - 32)
    end
  end
  
end

#==============================================================================
# Window_HybridTeleport
#==============================================================================

class Window_HybridTeleport < Window_Selectable

  def initialize
    item_max = $game_variables[CITY]-$game_variables[PLANET]/2*9
    if item_max > 9
      item_max = 9
    elsif item_max < 0
      item_max = 0
    end
    @background, @sx, @sy = 'Teleport', 460, 0
    super(652, 0, 180, 320)
    self.contents = Bitmap.new(width - 32, item_max * 32)
    @item_max = get_commands($game_variables[PLANET] / 2, $game_variables[CITY])
    self.contents.font.name = $fontface
    if $fontface == 'Papyrus'
      self.contents.font.size = 28
      self.contents.font.bold = true
    else
      self.contents.font.size = 22
    end
    refresh
    self.index, self.z = 0, 9999
  end

  def get_commands(world, cities)
    teleports = []
    teleports.push('Reeva')
    teleports.push('Lisk')
    teleports.push('Esteria')
    teleports.push('Lorence')
    teleports.push('Vendetta')
    teleports.push('Dalia')
    teleports.push('White Peak')
    teleports.push('Luvia')
    teleports.push('Vyn Island')
    teleports.push('Kaeri')
    teleports.push('Termina')
    teleports.push('Astralis')
    teleports.push('Mandora')
    teleports.push('Black Jack City')
    teleports.push('Medirok')
    teleports.push('Unitopia')
    teleports.push('Hyperion')
    teleports.push('Last Encounter')
    cities = world * 9 + 9 if cities > world * 9 + 9
    @commands = []
    (world * 9...cities).each {|i| @commands.push(teleports[i])}
    return @commands.size
  end
  
  def refresh
    self.contents.clear
    (0...@item_max).each {|i| draw_item(i, normal_color)}
  end

  def draw_item(index, color)
    rect = Rect.new(8, 32 * index, self.contents.width - 8, 32)
    self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
    self.contents.font.color = color
    self.contents.draw_text(rect, @commands[index])
  end

  def disable_item(index)
    draw_item(index, disabled_color)
  end
  
end

#==============================================================================
# Window_HybridSoulRage
#==============================================================================

class Window_HybridSoulRage < Window_Selectable

  attr_accessor :index
  
  def initialize(actor, help_window2)
    @background, @sx, @sy = 'Rage', 0, 224
    @help_window2 = help_window2
    super(0, -288, 640, 256)
    self.z, @column_max, @actor, @index = 2999, 1, actor, 0
    refresh
    update_cursor_rect
  end
  
  def update_actor(actor)
    @actor = actor
    refresh
  end
  
  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    @equipment, @skill_ids = setup_rages
    @item_max = @equipment.size
    if @item_max > 0
      self.contents = Bitmap.new(width - 32, @item_max * 32)
      if $fontface != nil
        self.contents.font.name = $fontface
        self.contents.font.size = $fontsize
      elsif $defaultfonttype != nil
        self.contents.font.name = $defaultfonttype
        self.contents.font.size = $defaultfontsize
      end
      (0...@item_max).each {|i| draw_item(i)} if @actor != nil
    end
  end
  
  def setup_rages
    equips = []
    skill_ids = [0, 0, 0, 0, 0, 0, 0]
    (0...7).each {|i|
        weapon = (i == 0)
        equip = nil
        has_id = true
        case i
        when 0 then equip = $data_weapons[@actor.weapon_id]
        when 1
          if CP::Cache::Lucius.include?(@actor.id)
            equip = $data_weapons[@actor.armor1_id]
            weapon = true
            if equip == nil && CP::Cache::TwoHanded.include?(@actor.weapon_id)
              equip = $data_weapons[@actor.weapon_id]
              has_id = false
            end
          else
            equip = $data_armors[@actor.armor1_id]
          end
        when 2 then equip = $data_armors[@actor.armor2_id]
        when 3 then equip = $data_armors[@actor.armor3_id]
        when 4 then equip = $data_armors[@actor.armor4_id]
        when 5 then equip = $data_armors[@actor.armor5_id]
        when 6 then equip = $data_armors[@actor.armor6_id]
        end
        id = ((equip == nil || !has_id) ? 0 : equip.id)
        skill_ids[i] = (weapon ? CP.sr_weapons(id) : CP.sr_armors(id, @actor, i))
        equips.push(equip)}
    return [equips, skill_ids]
  end
  
  def draw_item(i)
    id = @skill_ids[i]
    if id != 0
      skill = $data_skills[id]
      self.contents.font.color = normal_color
      rect = Rect.new(0, i*32, self.width / @column_max - 32, 32)
      self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
      bitmap = RPG::Cache.icon(skill.icon_name)
      self.contents.blt(300, 4+i*32, bitmap, Rect.new(0, 0, 24, 24))
      self.contents.draw_text(328, i*32, 204, 32, skill.name, 0)
      unless skill.sp_cost == 0
        self.contents.draw_text(516, i*32, 64, 32, "#{skill.sp_cost}%", 2)
      end
    else
      self.contents.font.color = disabled_color
      self.contents.draw_text(328, i*32, 204, 32, 'not available', 0)
    end
    if @equipment[i] != nil
      if i == 1 && CP::Cache::Lucius.include?(@actor.id) &&
          @equipment[i].is_a?(RPG::Weapon) &&
          CP::Cache::TwoHanded.include?(@equipment[i].id)
        bitmap = RPG::Cache.desaturated(@equipment[i].icon_name)
        self.contents.blt(4, i*32 + 4, bitmap, Rect.new(0, 0, 24, 24))
        self.contents.font.color = disabled_color
      else
        bitmap = RPG::Cache.icon(@equipment[i].icon_name)
        self.contents.blt(4, i*32 + 4, bitmap, Rect.new(0, 0, 24, 24))
        self.contents.font.color = normal_color
      end
      self.contents.draw_text(32, i*32, 288, 32, @equipment[i].name)
    else
      self.contents.font.color = disabled_color
      self.contents.draw_text(32, i*32, 288, 32, 'Nothing equipped')
    end
  end
  
  def update_help
    @help_window.set_text(@equipment[index] == nil ? '' : @equipment[index].description)
    @help_window2.set_text(self.skill == nil ? '' : self.skill.description)
  end
  
  def skill
    return $data_skills[@skill_ids[@index]]
  end
  
end

#==============================================================================
# Window_HybridRageStatus
#==============================================================================

class Window_HybridRageStatus < Window_Base

  def initialize(actor)
    @background, @sx, @sy = 'RStatus', 0, 128
    super(0, -384, 640, 96)
    self.z, @actor = 2999, actor
    self.contents = Bitmap.new(width - 32, height - 32)
    refresh
  end
  
  def update_actor(actor)
    @actor = actor
    refresh  
  end
  
  def refresh
    self.contents.clear
    draw_actor_name(@actor, 4, 0)
    draw_actor_level(@actor, 120, 0)
    draw_actor_state(@actor, 212, 0, 192, 0)
    draw_actor_sr_mode(@actor, 404, 0)
    draw_actor_hp(@actor, 4, 28, 172)
    draw_actor_sp(@actor, 204, 28, 172)
    draw_actor_sr(@actor, 404, 28, 172)
  end
  
  def draw_actor_sr_mode(actor, x, y, w = 200)
    text = (actor.sr_mode == 0 ? 'Active' : 'Passive')
    self.contents.font.color = system_color
    width = self.contents.text_size('SR Mode: ').width + 4
    self.contents.draw_text(x, y, 128, 32, 'SR Mode: ')
    self.contents.font.color = normal_color
    self.contents.draw_text(x + width, y, w, 32, text)
  end
  
end
