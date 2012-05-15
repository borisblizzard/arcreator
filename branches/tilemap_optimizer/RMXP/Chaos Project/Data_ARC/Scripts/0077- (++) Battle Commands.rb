#==============================================================================
# Icon
#==============================================================================

MAX_COMMAND = 5

class Icon < RPG::Sprite
  
  attr_accessor :dir
  attr_accessor :exception
  attr_accessor :ov
  attr_reader   :degrees
  attr_reader   :range
  attr_reader   :oz
  
  def initialize(cycle, range = 80, horizontal = true, view = nil)
    @oox = @ooy = @ov = 0
    super(view)
    @degrees = @dir = @real_z = @oz = 0
    @cycle = cycle
    @horizontal = horizontal
    @range = range
    @blink = false
    @bitmap_offset = 0
  end
  
  def ox=(val)
    @oox = val
    super(@oox - @bitmap_offset)
  end
  
  def ox
    return @oox
  end
  
  def oy=(val)
    @ooy = val
    super(@ooy - @bitmap_offset)
  end
  
  def oy
    return @ooy
  end
  
  def oz=(val)
    @oz = val
    self.z_is(@real_z + val, true)
  end
  
  alias z2 z=
  def z=(val)
    z_is(val)
  end
  
  def z_is(val, flag = false)
    @real_z = val unless flag
    z2(val)
  end
  
  def update
    return unless self.visible || moving?
    self.color.set(255, 255, 255, (16-@_blink_count).abs*12) if @_blink
    if moving? && !@exception
      case @cycle
      when 1 then self.degrees += 30 * @dir
      when 2 then self.degrees += 20 * @dir
      when 3..4 then self.degrees += 15 * @dir
      when 5 then self.degrees += 12 * @dir
      when 6 then self.degrees += 10 * @dir
      when 8 then self.degrees += 9 * @dir
      end
      @dir = 0 if self.degrees / (360/@cycle) * (360/@cycle) == self.degrees
    end
    super
  end
  
  def moving?
    return (@dir != 0)
  end
  
  def setup_zoom
    self.zoom_x = self.zoom_y = (4 + (Math.cos(Math::PI*@degrees/180)+1)) / 6
    self.oz = 1000 * self.zoom_x
  end
  
end

#==============================================================================
# Battle_Icon
#==============================================================================

class Battle_Icon < Icon
  
  def degrees=(val)
    @degrees = (val) % 360
    setup_zoom unless @exception
    zo = self.bitmap.width * (1 - self.zoom_x) / 2 / self.zoom_x
    @bitmap_offset = zo.round
    if @horizontal
      self.ox = -@range * (Math.sin(Math::PI*@degrees/180))
      self.oy = self.oy
    else
      self.oy = -@range * (Math.sin(Math::PI*@degrees/180))
      self.ox = self.ox
    end
    self.opacity = self.zoom_x * 255
  end
  
  def bitmap=(bit)
    super(RPG::Cache.icon('Battle/icon_back').clone)
    if bit.is_a?(Array)
      tmp = RPG::Cache.icon('Battle/0')
      self.bitmap.blt(4, 4, bit[0], Rect.new(0, 0, 24, 24))
      self.bitmap.blt(4, 4, tmp, Rect.new(0, 0, 24, 24), bit[1])
    else
      self.bitmap.blt(4, 4, bit, Rect.new(0, 0, 24, 24))
    end
  end
  
end

#==============================================================================
# Party_Icon
#==============================================================================

class Party_Icon < Icon
  
  def degrees=(val)
    @degrees = (val) % 360
    setup_zoom
    zo = self.bitmap.width * (1 - self.zoom_x) / 2 / self.zoom_x
    self.ox = - zo.round - @range * (Math.sin(Math::PI*@degrees/180))
    self.opacity = self.zoom_x * 255
  end
  
  def bitmap=(bit)
    super(RPG::Cache.icon('Battle/party_icon_back').clone)
    if bit.is_a?(Array)
      tmp = RPG::Cache.icon('Battle/no_party')
      self.bitmap.blt(8, 8, bit[0], Rect.new(0, 0, 48, 48))
      self.bitmap.blt(8, 8, tmp, Rect.new(0, 0, 48, 48), bit[1])
    else
      self.bitmap.blt(8, 8, bit, Rect.new(0, 0, 48, 48))
    end
  end
  
end

#==============================================================================
# Rage_Icon
#==============================================================================

class Rage_Icon < Icon
  
  def degrees=(val)
    @degrees = (val) % 360
    setup_zoom unless @exception
    @bitmap_offset_y = (self.bitmap.height * (1 - self.zoom_x) / 2 / self.zoom_x).round
    @bitmap_offset = (self.bitmap.width * (1 - self.zoom_x) / 2 / self.zoom_x).round
    self.oy = -@range * (Math.sin(Math::PI*@degrees/180))
    self.ox = self.ox
    self.opacity = self.zoom_x * 255
  end
  
  def bitmap=(bit)
    if bit == [4]
      super(Bitmap.new(80, 32))
    else
      super(RPG::Cache.icon('Battle/rage_back').clone)
      case bit[0]
      when 0
        self.bitmap.blt(4, 4, bit[1], Rect.new(0, 0, 24, 24))
        self.bitmap.blt(52, 4, bit[2], Rect.new(0, 0, 24, 24))
      when 1
        tmp = RPG::Cache.icon('Battle/0')
        self.bitmap.blt(4, 4, bit[1], Rect.new(0, 0, 24, 24))
        self.bitmap.blt(52, 4, bit[2], Rect.new(0, 0, 24, 24))
        self.bitmap.blt(52, 4, tmp, Rect.new(0, 0, 24, 24))
      when 2
        tmp = RPG::Cache.icon('Battle/0')
        self.bitmap.blt(4, 4, bit[1], Rect.new(0, 0, 24, 24))
        self.bitmap.blt(52, 4, tmp, Rect.new(0, 0, 24, 24))
      when 3
        tmp = RPG::Cache.icon('Battle/0')
        self.bitmap.blt(4, 4, tmp, Rect.new(0, 0, 24, 24))
        self.bitmap.blt(52, 4, tmp, Rect.new(0, 0, 24, 24))
      end
    end
  end
  
  def oy=(val)
    super(val + @bitmap_offset - @bitmap_offset_y)
    @ooy = val
  end
  
end

#==============================================================================
# Menu_Command
#==============================================================================

class Menu_Command
  
  attr_accessor :index
  attr_accessor :help_window
  attr_reader   :active
  attr_reader   :x
  attr_reader   :y
  
  def initialize
    @icons = []
    self.active = false
    self.x, self.y, self.z = 0, 0, 2000
  end
  
  def active=(expr)
    @active = expr
    update_help
  end
  
  def visible=(expr)
    @icons.each {|s| s.visible = expr}
    update_help
  end
  
  def visible
    return @icons[0].visible
  end
  
  def x=(val)
    @icons.each {|s| s.x = val - s.bitmap.width/2}
  end
  
  def y=(val)
    @icons.each {|s| s.y = val - s.bitmap.height/2}
  end
  
  def z=(val)
    @icons.each {|s| s.z = val}
  end
  
  def update(range)
    if !self.active
      range.each {|i|
          if !@icons[i].exception
            @icons[i].degrees = ((i-@index)%range.last) * 360 / range.last
            @icons[i].dir = 0
          end}
    end
  end
  
  def dispose
    @icons.each {|s| s.dispose}
  end
  
  def disable_item(index)
    @icons[index].bitmap = [@icons[index].bitmap, 255]
  end
  
  def reset
    @index = 0
    @icons.each_index {|i|
        @icons[i].degrees = i * 360 / @icons.size
        @icons[i].blink_off
        @icons[i].dir = 0}
    update_help
  end
  
end

#==============================================================================
# Menu_ActorBattle
#==============================================================================

class Menu_ActorBattle < Menu_Command
  
  attr_reader :actor
  
  def initialize
    super
    6.times {@icons.push(Battle_Icon.new(5))}
    @icons[5].exception = true
    @icons[5].visible = false
    (0...@icons.size-1).each {|i| @icons[i].bitmap = RPG::Cache.icon("Battle/#{i}")}
    @icons[5].bitmap = Bitmap.new(24, 24)
    @icons.each_index {|i| @icons[i].degrees = i * 360 / MAX_COMMAND}
    @icons[5].zoom_x = @icons[5].zoom_y = 0.85
    @icons[5].degrees = 0
    @icons[5].oy = -24
    @icons[5].z = 500
    @commands = [$data_system.words.attack, setup_command_name,
        $data_system.words.guard, $data_system.words.item, 'Soul Rage',
        get_player_command]
    @index, @old_index, @meta_select, self.x, self.y = 0, 0, 0, 0, 176
    self.visible = false
  end
  
  def update
    super(0...5)
    @icons.each_index {|i|
        @index == i ? @icons[i].blink_on : @icons[i].blink_off
        @icons[i].update}
    @icons[5].visible = (@actor != nil && @actor.meta == 20 && self.visible)
    if !@icons[0].moving? && self.active
      if @meta_select == 0
        if Input.repeat?($controls.right)
          $game_system.se_play($data_system.cursor_se)
          @index = (@index + 1) % MAX_COMMAND
          @icons.each {|s| s.dir = -1 unless s.exception}
        elsif Input.repeat?($controls.left)
          $game_system.se_play($data_system.cursor_se)
          @index = (@index + MAX_COMMAND - 1) % MAX_COMMAND
          @icons.each {|s| s.dir = 1 unless s.exception}
        elsif @actor != nil && @actor.meta == 20
          if Input.repeat?($controls.up)
            $game_system.se_play($data_system.cursor_se)
            @real_index = @index
            @index = 5
            @icons.each {|s| s.exception = true}
            @meta_select = 2
          end
        end
      elsif @meta_select == 1
        if Input.repeat?($controls.down)
          $game_system.se_play($data_system.cursor_se)
          @index = @real_index
          @meta_select = -1
        end
      elsif @meta_select >= 2
        @icons[@real_index].oy -= 14
        @icons[@real_index].zoom_x -= 0.05
        @icons[@real_index].zoom_y -= 0.05
        @icons[@real_index].degrees = 0
        @icons[(@real_index - 1) % MAX_COMMAND].oy -= 6
        @icons[(@real_index - 1) % MAX_COMMAND].zoom_x -= 0.03
        @icons[(@real_index - 1) % MAX_COMMAND].zoom_y -= 0.03
        @icons[(@real_index - 1) % MAX_COMMAND].degrees += 5
        @icons[(@real_index + 1) % MAX_COMMAND].oy -= 6
        @icons[(@real_index + 1) % MAX_COMMAND].zoom_x -= 0.03
        @icons[(@real_index + 1) % MAX_COMMAND].zoom_y -= 0.03
        @icons[(@real_index + 1) % MAX_COMMAND].degrees -= 5
        @icons[(@real_index - 2) % MAX_COMMAND].oy += 7
        @icons[(@real_index - 2) % MAX_COMMAND].zoom_x += 0.01
        @icons[(@real_index - 2) % MAX_COMMAND].zoom_y += 0.01
        @icons[(@real_index - 2) % MAX_COMMAND].degrees -= 2
        @icons[(@real_index + 2) % MAX_COMMAND].oy += 7
        @icons[(@real_index + 2) % MAX_COMMAND].zoom_x += 0.01
        @icons[(@real_index + 2) % MAX_COMMAND].zoom_y += 0.01
        @icons[(@real_index + 2) % MAX_COMMAND].degrees += 2
        @icons[5].oy -= 7
        @icons[5].zoom_x += 0.03
        @icons[5].zoom_y += 0.03
        @icons[5].degrees = 0
        @meta_select += 1
        @meta_select = 1 if @meta_select == 7
      elsif @meta_select < 0
        @icons[@real_index].oy += 14
        @icons[@real_index].zoom_x += 0.05
        @icons[@real_index].zoom_y += 0.05
        @icons[@real_index].degrees = 0
        @icons[(@real_index - 1) % MAX_COMMAND].oy += 6
        @icons[(@real_index - 1) % MAX_COMMAND].zoom_x += 0.03
        @icons[(@real_index - 1) % MAX_COMMAND].zoom_y += 0.03
        @icons[(@real_index - 1) % MAX_COMMAND].degrees -= 5
        @icons[(@real_index + 1) % MAX_COMMAND].oy += 6
        @icons[(@real_index + 1) % MAX_COMMAND].zoom_x += 0.03
        @icons[(@real_index + 1) % MAX_COMMAND].zoom_y += 0.03
        @icons[(@real_index + 1) % MAX_COMMAND].degrees += 5
        @icons[(@real_index - 2) % MAX_COMMAND].oy -= 7
        @icons[(@real_index - 2) % MAX_COMMAND].zoom_x -= 0.01
        @icons[(@real_index - 2) % MAX_COMMAND].zoom_y -= 0.01
        @icons[(@real_index - 2) % MAX_COMMAND].degrees += 2
        @icons[(@real_index + 2) % MAX_COMMAND].oy -= 7
        @icons[(@real_index + 2) % MAX_COMMAND].zoom_x -= 0.01
        @icons[(@real_index + 2) % MAX_COMMAND].zoom_y -= 0.01
        @icons[(@real_index + 2) % MAX_COMMAND].degrees -= 2
        @icons[5].oy += 7
        @icons[5].zoom_x -= 0.03
        @icons[5].zoom_y -= 0.03
        @icons[5].degrees = 0
        @meta_select -= 1
        if @meta_select == -6
          @meta_select = 0
          (0...@icons.size-1).each {|i| @icons[i].exception = false}
        end
      end
    end
    update_help
  end
  
  def rotation_reset
    if @meta_select != 0
      @icons[@real_index].zoom_x += 0.25
      @icons[@real_index].zoom_y += 0.25
      @icons[@real_index].degrees = 0
      @icons[(@real_index - 1) % MAX_COMMAND].zoom_x += 0.20
      @icons[(@real_index - 1) % MAX_COMMAND].zoom_y += 0.20
      @icons[(@real_index - 1) % MAX_COMMAND].degrees -= 25
      @icons[(@real_index + 1) % MAX_COMMAND].zoom_x += 0.20
      @icons[(@real_index + 1) % MAX_COMMAND].zoom_y += 0.20
      @icons[(@real_index + 1) % MAX_COMMAND].degrees += 25
      @icons[(@real_index - 2) % MAX_COMMAND].zoom_x -= 0.1
      @icons[(@real_index - 2) % MAX_COMMAND].zoom_y -= 0.1
      @icons[(@real_index - 2) % MAX_COMMAND].degrees += 10
      @icons[(@real_index + 2) % MAX_COMMAND].zoom_x -= 0.1
      @icons[(@real_index + 2) % MAX_COMMAND].zoom_y -= 0.1
      @icons[(@real_index + 2) % MAX_COMMAND].degrees -= 10
      @meta_select = 0
      (0...@icons.size-1).each {|i| @icons[i].exception = false}
    end
  end
  
  def actor=(actor)
    @actor = actor
    rotation_reset
    @icons.each_index {|i|
        unless @icons[i].exception
          @icons[i].degrees = i * 360 / MAX_COMMAND
          @icons[i].blink_off
          @icons[i].oy = -64
        end
        @icons[i].color.set(0, 0, 0, 0)
        @icons[i].dir = 0}
    w_text = 'with '
    if CP::Cache::Lucius.include?(@actor.id) && @actor.weapon_id == 0 &&
        @actor.armor1_id == 0 || @actor.weapon_id == 0
      @icons[0].bitmap.clear
      @icons[0].bitmap = RPG::Cache.icon('Battle/0')
      w_text = 'without weapon'
      name = ''
    elsif CP::Cache::Lucius.include?(@actor.id)
      if @actor.weapon_id > 0 && @actor.armor1_id == 0
        @icons[0].bitmap = RPG::Cache.icon($data_weapons[@actor.weapon_id].icon_name)
        name = $data_weapons[@actor.weapon_id].name
      elsif @actor.weapon_id == 0 && @actor.armor1_id > 0
        @icons[0].bitmap = RPG::Cache.icon($data_weapons[@actor.armor1_id].icon_name)
        name = $data_weapons[@actor.armor1_id].name
      else
        b2 = RPG::Cache.icon($data_weapons[@actor.weapon_id].icon_name)
        if @actor.weapon_id == @actor.armor1_id
          b1 = b2.clone
          name = "2 #{CP.name_2($data_weapons[@actor.weapon_id].name)}"
        else  
          b1 = RPG::Cache.icon($data_weapons[@actor.armor1_id].icon_name).clone
          name = "#{$data_weapons[@actor.weapon_id].name} & " + 
              $data_weapons[@actor.armor1_id].name
        end
        b1.mirror
        b1.blt(0, 0, b2, Rect.new(0, 0, b2.width, b2.height))
        @icons[0].bitmap = b1
      end
    else
      @icons[0].bitmap = RPG::Cache.icon($data_weapons[@actor.weapon_id].icon_name)
      name = $data_weapons[@actor.weapon_id].name
    end
    @commands[0] = "#{$data_system.words.attack} #{w_text}#{name}"
    @icons[1].bitmap.clear
    begin
      id = (@actor.states.include?(45) ? 'dragmatech' : @actor.class_id)
      @icons[1].bitmap = RPG::Cache.icon("Battle/Tech/#{id}")
    rescue
      @icons[1].bitmap = RPG::Cache.icon('Battle/0')
    end
    if @actor != nil && @actor.meta == 20
      @icons[5].bitmap = RPG::Cache.icon($data_skills[get_skill_id].icon_name)
    else
      @icons[5].bitmap.clear
    end
    @icons[5].zoom_x = @icons[5].zoom_y = 0.85
    @icons[5].degrees = 0
    @icons[5].oy = -24
    @commands[5] = get_player_command
    update_help
  end
  
  def update_help
    if @help_window != nil && self.active
      if @index == 5
        @help_window.set_text(@commands[@index], 1, Color.new(255, 0, 0), $data_skills[get_skill_id].description)
      else
        @help_window.set_text(@commands[@index], 1)
      end
    end
  end
  
  def get_player_command
    return '' if @actor == nil
    case @actor.id
    when 1 then return 'Lexima Burst'
    when 2 then return 'Blood Plague'
    when 3 then return 'Psychokinesis'
    when 4 then return 'Burnout'
    when 5 then return 'Exodus'
    when 6 then return 'Neo Genesis'
    when 7 then return ''
    when 8 then return ''
    when 9 then return 'Ultimatex'
    when 10 then return 'Dark Doom'
    when 11 then return ''
    when 12 then return 'Fighter\'s Wrath'
    when 13 then return 'Dragmatek'
    when 15 then return 'When Hell freezes over'
    when 16 then return 'Gigamedra'
    end
    return 'N/A'
  end
  
  def get_skill_id
    case @actor.id
    when 1 then return 187
    when 2 then return 157
    when 3 then return 188
    when 4 then return 198
    when 5 then return 202
    when 6 then return 271
    when 7 then return 160
    when 8 then return 198
    when 9 then return 160
    when 10 then return 158
    when 11 then return 160
    when 12 then return 159
    when 13 then return 251
    when 14 then return 160
    when 15 then return 428
    when 16 then return 444
    end
    return 160
  end
    
  def setup_command_name
    return if @actor == nil
    if @actor.states.include?(45)
      @commands[1] = 'Dragmatech'
      return
    end
    case @actor.class_id
    when 1 then @commands[1] = 'Burnatech'
    when 2 then @commands[1] = 'Armatech'
    when 3 then @commands[1] = 'Magitech'
    when 4 then @commands[1] = 'Devitech'
    when 5 then @commands[1] = 'Executech'
    when 6 then @commands[1] = 'Lexitech'
    when 7 then @commands[1] = 'Swortech'
    when 8 then @commands[1] = 'Lucitech'
    when 9 then @commands[1] = 'Alphatech'
    when 10 then @commands[1] = 'Wolvetech'
    when 11 then @commands[1] = 'Devastech'
    when 12 then @commands[1] = 'Killtech'
    when 13 then @commands[1] = 'Exotech'
    when 14 then @commands[1] = 'Chaotech'
    end
  end
  
end

#==============================================================================
# Menu_PartyCommand
#==============================================================================

class Menu_PartyCommand < Menu_Command
  
  def initialize
    super
    4.times {@icons.push(Party_Icon.new(4, 144))}
    refresh
    @icons.each_index {|i| @icons[i].degrees, @icons[i].oy = i * 360 / 4, -80}
    @commands = ['Fight', 'Unity Force', 'Abscond', 'Repeat']
    @index, self.x, self.y, self.visible = 0, 320, 64, false
  end
  
  def update
    super(0...@icons.size)
    @icons.each_index {|i|
        @index == i ? @icons[i].blink_on : @icons[i].blink_off
        @icons[i].update}
    if !@icons[0].moving? && self.active
      if Input.repeat?($controls.right)
        $game_system.se_play($data_system.cursor_se)
        @index = (@index + 1) % 4
        @icons.each {|s| s.dir = -1}
      elsif Input.repeat?($controls.left)
        $game_system.se_play($data_system.cursor_se)
        @index = (@index + 3) % 4
        @icons.each {|s| s.dir = 1}
      end
    end
    update_help
  end
  
  def refresh
    @icons.each {|s| s.bitmap.clear if s.bitmap.is_a?(Bitmap)}
    @icons[0].bitmap = RPG::Cache.icon('Battle/fight')
    if $game_party.uf_can_use?(-1)
      @icons[1].bitmap = RPG::Cache.icon('Battle/uf')
    else
      @icons[1].bitmap = [RPG::Cache.icon('Battle/uf'), 255]
    end
    if $game_temp.battle_can_escape
      @icons[2].bitmap = RPG::Cache.icon('Battle/abscond')
    else
      @icons[2].bitmap = [RPG::Cache.icon('Battle/abscond'), 255]
    end
    @icons[3].bitmap = RPG::Cache.icon('Battle/repeat')
  end
  
  def update_help
    if @help_window != nil && self.active
      @help_window.set_text(@commands[@index], 1)
    end
  end
  
end

#==============================================================================
# Menu_AbilityCommand
#==============================================================================

class Menu_AbilityCommand < Menu_Command
  
  def initialize(actor)
    super()
    @actor = actor
    init
    @index, self.x, self.y, self.visible = 0, 0, 192, false
  end
  
  def init
    @skills = @actor.skills.clone
    @types, @commands = [], []
    @actor.skills.each {|id| @types += $data_skills[id].element_set}
    @types = ((@types | @types) - (0..18).to_a).sort
    @types.size.times {@icons.push(Battle_Icon.new(@types.size, 60, false))}
    refresh
    @icons.each_index {|i| @icons[i].degrees = i * 360 / @types.size}
    @types.each {|type| @commands.push($data_system.elements[type])}
  end
  
  def type
    return (@types[@index] - 19)
  end

  def reset
    if @skills != @actor.skills
      x, ox = @icons[0].x + @icons[0].bitmap.width / 2, @icons[0].ox
      y, visible = @icons[0].y + @icons[0].bitmap.height / 2, @icons[0].visible
      @icons.each {|icon| icon.dispose}
      @icons = []
      init
      self.x, self.y, self.ox, self.visible = x, y, ox, visible
    end
    super
  end
  
  def update
    super(0...@icons.size)
    @icons.each_index {|i|
        @index == i ? @icons[i].blink_on : @icons[i].blink_off
        @icons[i].update}
    if !@icons[0].moving? && self.active
      if Input.repeat?($controls.down)
        $game_system.se_play($data_system.cursor_se)
        @index = (@index + 1) % @types.size
        @icons.each {|s| s.dir = -1}
      elsif Input.repeat?($controls.up)
        $game_system.se_play($data_system.cursor_se)
        @index = (@index + @types.size - 1) % @types.size
        @icons.each {|s| s.dir = 1}
      end
    end
    update_help
  end
  
  def refresh
    @icons.each_index {|i|
        @icons[i].bitmap = RPG::Cache.icon("Battle/ab_#{@types[i]-19}")}
  end
  
  def ox=(val)
    @icons.each {|s| s.ox = val}
  end
  
  def update_help
    @help_window.set_text(@commands[@index], 1) if @help_window != nil && self.active
  end
  
end
