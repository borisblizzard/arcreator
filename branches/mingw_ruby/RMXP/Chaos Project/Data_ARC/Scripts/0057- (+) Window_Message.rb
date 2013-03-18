#==============================================================================
# Animator
#  Message Arbiter System
#==============================================================================

# blue
HEROES = ['Jason', 'Endout', 'Lilith', 'Ariana', 'Lucius', 'Vamp', 'Nosferatu',
          'Setzer', 'Duke', 'Siegfried', 'Sydon']
# red
NEMESIS = ['Nemesis', 'Archnemsis']
# pentagram
EVILS = ['Earayl', 'Boss', 'Faberell', 'Anoxis', 'Seraphine', 'Coga',
         'Raz\'nar', 'Vampire', '???', 'Monster', 'Grid Stalker',
         'Lord Terence', 'Nocturno', 'Celestia', 'Chaos Behemoth', 'Blood Bat',
         'Phantom Bat', 'Grave Guard', 'Spirit Sword',
         'Bounty Hunter', 'Gangster Boss', 'Breath of Ice']
# green
LEXIMAS = ['Leximus', 'Vex', 'Vortex', 'Lexima Warrior']
# bunny
BUNNY = ['Bunny']
# purple
CHAOSES = ['Rivy', 'Hellvoid']
# none
OUTS = ['Hint', 'Hinweis', 'Voice', 'voice', 'Stimme', 'Everybody', 'Alle',
        '&', 'HP and MP restored', 'KP und MP wiederhergestellt',
        'HP restored', 'KP wiederhergestellt', 'Chaos', 'Computer']
OUTS_IGNORE = ['Chaos Behemoth', 'First Orb of Chaos']
# ??? replacements
NOT_KNOWN = ['Faberell', 'Nemesis', 'Rivy', 'Seraphine', 'Boss', '???',
             'Anoxis'] + EVILS
NOT_KNOWN2 = ['Baron', 'Endout', 'Lilith', 'Bunny']

class Animator < RPG::Sprite
  
  attr_reader :host
  
  def initialize(viewport = nil)
    super
    @name = ''
    self.bitmap = Bitmap.new(2, 2)
    self.x, self.y, self.z, self.opacity, @count = 320, 240, 900, 0, 0
  end
  
  def update
    tone = $game_screen.tone
    quota = (tone.red + tone.green + tone.blue) / (-3)
    self.opacity = 255 - quota if quota > 0
    if self.opacity == 0 || @sprite == nil
      loop_animation(nil)
      instant_move
    else
      super
      evils = EVILS.clone
      evils.push('Professor Simonair') if $game_switches[375]
      if evils.include?(@host.name)
        id = 84
      elsif HEROES.include?(@host.name)
        id = 83
      elsif CHAOSES.include?(@host.name)
        id = 82
      elsif LEXIMAS.include?(@host.name)
        id = 81
      elsif BUNNY.include?(@host.name)
        id = 254
      elsif NEMESIS.include?(@host.name)
        id = 2
      else
        id = 80
      end
      loop_animation($data_animations[id])
      @count > 0 ? update_move : instant_move
    end
  end
  
  def update_move
    dx, dy = @sprite.center
    self.x += (dx-self.x)/@count
    self.y += (dy-self.y)/@count
    @count -= 1
    self.x, self.y = @sprite.center if @count == 0
  end
  
  def instant_move
    self.x, self.y = @sprite.center if @sprite != nil
  end
  
  def host=(new)
    if @sprite != new
      @sprite.blink_off if @sprite != nil
      @sprite = new
      if @sprite != nil
        @sprite.blink_on if new.character.name != 'Hellvoid'
        @host = new.character
        @count = 8
      else
        @host = nil
      end
    end
  end
  
  def dispose
    self.host = nil if @host == nil
    super
  end
  
end

#==============================================================================
# Window_Message
#==============================================================================

class Window_Message < Window_Selectable
  
  attr_accessor :timer
  attr_accessor :timer_active
  attr_accessor :frames
  
  def initialize
    super(40, 374, 560, 20)
    @rotator = Animator.new
    @rotator.z = 1000
    $game_system.message_walking, self.z, @cursor_width = true, 9998, 0
    @frame = $game_system.message_frame
    self.visible = self.active = @timer_active = @contents_showing =
        @fade_in = @fade_out = false
    self.index = @timer = -1
    @frames = 2 * Graphics.frame_count / Graphics.frame_rate
  end
  
  alias visible_later visible=
  def visible=(val)
    @rotator.visible = ($game_temp.message_text != nil)
    visible_later(val)
  end
  
  alias opacity_later opacity=
  def opacity=(val)
    @rotator.opacity = ($game_temp.message_text == nil ? 0 : 192)
    opacity_later(val)
  end
  
  def dispose
    terminate_message
    $game_temp.message_window_showing = false
    @input_number_window.dispose if @input_number_window != nil
    super
  end
  
  def replace_text(tt, txt)
    case tt
    when 'White-haired man' then txt.gsub!(tt) {'Leximus'}
    when 'Caped man' then txt.gsub!(tt) {'Setzer'}
    when 'Armored man' then txt.gsub!(tt) {'Siegfried'}
    when 'Masked man' then txt.gsub!(tt) {'Duke'}
    when 'Man in black', 'Man in the center', 'Archnemesis' then txt.gsub!(tt) {'Nemesis'}
    when 'Monster' then txt.gsub!(tt) {'Faberell'}
    when 'King-like dressed man', 'Loderro'  then txt.gsub!(tt) {'Lord Terence'}
    when 'Female vampire' then txt.gsub!(tt) {'Celestia'}
    when 'Pale man' then txt.gsub!(tt) {'Lucius'}
    when 'Red-haired man' then txt.gsub!(tt) {'Robert'}
    when 'Weird man' then txt.gsub!(tt) {'Dr. Chunk'}
    when 'Unusual man' then txt.gsub!(tt) {'Rose Skye'}
    when 'Mysterious man' then txt.gsub!(tt) {'Sydon'}
    when 'Man in red' then txt.gsub!(tt) {'Bounty Hunter'}
    when 'Blonde woman', 'Beautiful woman' then txt.gsub!(tt) {'Ariana'}
    when 'Käpt\'n Rack\'em' then txt.gsub!(tt) {'Captain Rack\'em'}
    when 'Prisoner' then txt.gsub!(tt) {'Dio'}
    when 'Head scientist' then txt.gsub!(tt) {'Professor Simonair'}
    when '???'
      $scene.spriteset.character_sprites.each {|sprite|
          if sprite.character != nil && sprite.character.opacity > 0 &&
              sprite.character.character_name != '' &&
              NOT_KNOWN.include?(sprite.character.name)
            txt.gsub!(tt) {sprite.character.name}
            return
          end}
      $scene.spriteset.character_sprites.each {|sprite|
          if sprite.character != nil && sprite.character.opacity > 0 &&
              sprite.character.character_name != '' &&
              NOT_KNOWN2.include?(sprite.character.name)
            txt.gsub!(tt) {sprite.character.name}
            return
          end}
    end
  end
  
  def update_rotator(flag = false)
    return unless $scene.is_a?(Scene_Map)
    flag = true if @rotator.host == nil
    if $game_temp.message_text == nil
      @rotator.instant_move if flag
      return
    end
    if $game_temp.animator != nil
      if $game_temp.animator == true
        $game_temp.animator = nil
        @rotator.host = nil
        return
      end
      txt = "\001[3]#{$game_temp.animator}\001[0]:\n"
      $game_temp.animator = nil
    else
      text = $game_temp.message_text.clone
      begin
        last_text = text.clone
        text.gsub!(/\\[Vv]\[([0-9]+)\]/) { $game_variables[$1.to_i] }
      end until text == last_text
      text.gsub!(/\\\\/) { "\000" }
      text.gsub!(/\\[Cc]\[([0-9]+)\]/) { "\001[#{$1}]" }
      txt = ''
      text.clone.each_line {|s| txt = s; break}
      if txt == "\n"
        @rotator.host = nil
        return
      end
      if ($game_temp.choice_max > 0 || $game_temp.num_input_variable_id > 0)
        if $game_player.opacity > 0 && $game_player.character_name != ''
          @rotator.host = get_sprite($game_player)
        else
          @rotator.host = nil
        end
        @rotator.instant_move if flag
        return
      end
      need = false
    end
    tt = txt.clone
    tt.gsub!("\001[3]") {''}
    tt.gsub!("\001[0]") {''}
    tt.gsub!("\n") {''}
    tt.gsub!(':') {''}
    replace_text(tt, txt)
    host = @rotator.host
    if (!(txt.clone.gsub!("\001[3]") {''}) || !(txt.clone.gsub!(':') {''})) &&
        !(txt.clone.gsub!("\001[4]") {''} && txt.clone.gsub!("\001[0]") {''}) &&
        @rotator.host == nil
      event = $game_map.events[$game_system.map_interpreter.event_id]
      if event != nil && event.opacity > 0 && event.character_name != ''
        @rotator.host = get_sprite(event)
        @rotator.instant_move if flag
      end
      return
    end
    return if @rotator.host != nil && txt.clone.gsub!(@rotator.host.name) {''}
    if OUTS.any? {|x| txt.clone.gsub!(x) {''}} &&
        !OUTS_IGNORE.any? {|x| txt.clone.gsub!(x) {''}} &&
        txt.clone.gsub!("\001[3]") {''} && txt.clone.gsub!("\001[0]:") {''} ||
        txt.clone.gsub!("\001[4]") {''} && txt.clone.gsub!("\001[0]") {''}
      @rotator.host = nil
    elsif txt.clone.gsub!("\001[3]") {''}
      $scene.spriteset.character_sprites.each {|sprite|
          if sprite.character != nil && sprite.character.opacity > 0 &&
              sprite.character.character_name != '' &&
              txt.clone.gsub!(sprite.character.name) {''}
            @rotator.host = sprite
            break
          end}
      if host == @rotator.host
        members = [$game_player] + $game_player.members[0, $game_party.actors.size-1]
        members.each_index {|i|
            if (txt.clone.gsub!("\001[3]") {''}) &&
                (txt.clone.gsub!($game_party.actors[i].name) {''}) &&
                members[i].opacity > 0 && members[i].character_name != ''
              @rotator.host = get_sprite(members[i])
              break
            end}
        if $game_switches[366]
          other = $game_player.members[$game_party.actors.size]
          if (txt.clone.gsub!("\001[3]") {''}) &&
              (txt.clone.gsub!('Luvian King') {''}) &&
              other.opacity > 0 && other.character_name != ''
            @rotator.host = get_sprite(other)
          end
        end
      end
      if @rotator.host == nil && host == nil
        event = $game_map.events[$game_system.map_interpreter.event_id]
        if event != nil && event.opacity > 0 && event.character_name != ''
          @rotator.host = get_sprite(event)
        end
      end
    elsif @rotator.host == nil && host == nil
      event = $game_map.events[$game_system.map_interpreter.event_id]
      if event != nil && event.opacity > 0 && event.character_name != ''
        @rotator.host = get_sprite(event)
      end
    end
    @rotator.instant_move if flag
  end
  
  def get_sprite(character)
    $scene.spriteset.character_sprites.each {|sprite|
        return sprite if character == sprite.character}
    return nil
  end
  
  def terminate_message
    self.active = self.pause = @contents_showing = false
    self.index = -1
    $game_temp.message_proc.call if $game_temp.message_proc != nil
    $game_temp.message_text = $game_temp.message_proc =
    $game_temp.choice_proc = nil
    $game_temp.choice_start = $game_temp.num_input_start = 99
    $game_temp.choice_max = $game_temp.choice_cancel_type =
    $game_temp.num_input_variable_id = $game_temp.num_input_digits_max = 0
    if @gold_window != nil
      @gold_window.dispose
      @gold_window = nil
    end
    @fade_out = true
    update_rotator
    @timer_active = false
  end
  
  def get_icons(text)
    test = text.clone
    return [] if test.size == 0
    icons = []
    if test[0].chr == "\n"
      test = test[1, test.size-1]
      test.each_line {|line|
          if line.clone.gsub!($data_system.words.gold) {''} != nil &&
              line.clone.gsub!($data_system.words.gold + 'en') {''} == nil ||
              line.clone.gsub!('EXP') {''} != nil &&
              line.clone.gsub!('Orb') {''} == nil
            next
          end
          line.gsub!("\n") {''}
          if line.gsub!('1 × ') {''} == nil &&
              line.gsub!('12 × ') {''} == nil &&
              line.gsub!('16 × ') {''} == nil &&
              line.gsub!('2 × ') {''} == nil &&
              line.gsub!('3 × ') {''} == nil &&
              line.gsub!('5 × ') {''} == nil &&
              line.gsub!('8 × ') {''} == nil &&
              line.gsub!('10 × ') {''} == nil &&
              line.gsub!('20 × ') {''} == nil &&
              line.gsub!('30 × ') {''} == nil &&
              line.gsub!('50 × ') {''} == nil &&
              line.gsub!('100 × ') {''} == nil
            (1...$data_actors.size).each {|i|
                line.gsub!($game_actors[i].name + ' ') {''}}
            $data_skills[1, $data_skills.size-1].each {|skill|
                line.gsub!('- ' + skill.name + ' ') {''}}
            line.gsub!('- ') {''}
            line.gsub!('learned ') {''}
            line.gsub!('Unity Force ') {''}
            line.gsub!(/\\[Cc]\[([0-9]+)\]/) { '' }
          end
          objects = $data_items[1, $data_items.size-1]
          objects += $data_weapons[1, $data_weapons.size-1]
          objects += $data_armors[1, $data_armors.size-1]
          objects += $data_skills[1, $data_skills.size-1]
          objects.each {|object|
              if object.name != 'Raging' &&
                  line[0, object.name.size] == object.name &&
                  (!(line.clone.gsub!('Ruby Star') {''}) &&
                  !(line.clone.gsub!('Ruby Pendant') {''}) ||
                  object.name != 'Ruby') && object.name != ''
                text.gsub!(object.name) {
                    "\006[#{icons.size}]\\c[1]#{object.name}\\c[0]" }
                icons.push(object.icon_name)
                break
              end}}
    end
    return icons
  end
  
  def get_faces(text)
    test = text.clone
    faces = []
    test.each_line {|line|
        if line.gsub!('\\c[3]') {''} != nil &&
            (line.gsub!('\\c[0]:') {''} != nil ||
            line.gsub!('\\c[0] (furious):') {''} != nil) &&
            @rotator.host != nil
          text.sub!("\\c[3]") {"\007[#{faces.size}]\\c[3]"}
          tt = line.clone
          tt.gsub!("\001[3]") {''}
          tt.gsub!("\001[0]") {''}
          tt.gsub!("\n") {''}
          tt.gsub!(':') {''}
          tt.gsub!(' (furious)') {''}
          begin
            last_text = line.clone
            line.gsub!(/\\[Vv]\[([0-9]+)\]/) { $game_variables[$1.to_i] }
          end until line == last_text
          line.gsub!(/\\[Nn]\[([0-9]+)\]/) do
            $game_actors[$1.to_i] != nil ? $game_actors[$1.to_i].name : ''
          end
          replace_text(tt, line)
          $scene.spriteset.character_sprites.each {|sprite|
              if sprite.character != nil && sprite.character.opacity > 0 &&
                  sprite.character.character_name != '' &&
                  line.clone.gsub!(sprite.character.name) {''}
                character_name = replace_face(sprite.character.character_name)
                if character_name == 'faberell X faces' ||
                    character_name == 'grave_guard faces' ||
                    character_name == 'spirit_sword faces'
                  faces.push([character_name, sprite.character.character_hue,
                      [sprite.character.pattern,
                          sprite.character.direction / 2 - 1]])
                else
                  faces.push([character_name, sprite.character.character_hue])
                end
                break
              end}
          if faces.size == 0
            event = $game_map.events[$game_system.map_interpreter.event_id]
            if event != nil && event.opacity > 0 && event.character_name != ''
              character_name = replace_face(event.character_name)
              if character_name == 'faberell X faces' ||
                  character_name == 'grave_guard faces' ||
                  character_name == 'spirit_sword faces'
                faces.push([character_name, event.character_hue,
                    [event.pattern, event.direction / 2 - 1]])
              else
                faces.push([character_name, event.character_hue])
              end
            end
          end
        end
        break}
    return faces
  end
  
  def replace_face(character_name)
    return case character_name
    when 'faberell X' then 'faberell X faces'
    when 'grave_guard' then 'grave_guard faces'
    when 'spirit_sword' then 'spirit_sword faces'
    when 'jason down', 'jason float' then 'jason'
    when 'jason lex float' then 'jason lex'
    when 'endout down' then 'endout'
    when 'ariana down' then 'ariana'
    when 'sydon down' then 'sydon'
    when 'Leximus extra' then 'Leximus'
    when '189-Down01' then '001-Fighter01'
    when '192-Down04' then '130-Noble05'
    when 'sitting_no_chair' then '150-Sailor01'
    when 'sitting_no_chair2' then '149-Captain01'
    when 'duke_load' then 'duke'
    when 'vex_shaded_with_sword' then 'vex_shaded'
    else
      character_name
    end
  end
  
  def refresh
    @timer_active = false
    self.contents = Bitmap.new(self.width - 32, self.height - 32)
    self.contents.font.color = normal_color
    self.contents.font.name = $fontface
    self.contents.font.size = $fontsize
    self.contents.font.bold = true if $fontface == 'Papyrus'
    y = 0
    x = ($game_temp.choice_start == 0 ? 8 : 0)
    @cursor_width = 0
    if $game_temp.message_text != nil
      text = $game_temp.message_text
      begin
        last_text = text.clone
        text.gsub!(/\\[Vv]\[([0-9]+)\]/) { $game_variables[$1.to_i] }
      end until text == last_text
      icons = get_icons(text)
      faces = get_faces(text)
      text.gsub!(/\\[Nn]\[([0-9]+)\]/) {
          $game_actors[$1.to_i] != nil ? $game_actors[$1.to_i].name : ''}
      text.gsub!(/\\[Ii]\[([\w]+)\]/) {
          case $1
          when 'w' then CP.controls_name($controls.up)
          when 'a' then CP.controls_name($controls.left)
          when 's' then CP.controls_name($controls.down)
          when 'd' then CP.controls_name($controls.right)
          when 'k' then CP.controls_name($controls.confirm)
          when 'j' then CP.controls_name($controls.cancel)
          when 'i' then CP.controls_name($controls.menu)
          when 'l' then CP.controls_name($controls.leximus)
          when 'q' then CP.controls_name($controls.prev)
          when 'e' then CP.controls_name($controls.nex)
          when 'z' then CP.controls_name($controls.snap)
          end}
      text.gsub!(/\\\\/) { "\000" }
      text.gsub!(/\\[Cc]\[([0-9]+)\]/) { "\001[#{$1}]" }
      text.gsub!(/\\[Gg]/) { "\002" }
      text.gsub!(/\\[Hh]/) { "\003" }
      text.gsub!(/\\[Ss]\[([0-9]+)\]/) { "\004[#{$1}]" }
      text.gsub!(/\\[Tt]\[([0-9]+)\]/) { "\005[#{$1}]" }
      while ((c = text.slice!(/./m)) != nil)
        c = "\\" if c == "\000"
        case c
        when "\001"
          text.sub!(/\[([0-9]+)\]/, '')
          color = $1.to_i
          self.contents.font.color = text_color(color) if color.between?(0, 9)
        when "\002"
          if @gold_window == nil
            @gold_window = Window_Trade.new(true)
            @gold_window.x = 600 - @gold_window.width
            if $game_temp.in_battle
              @gold_window.y = 192
            else
              @gold_window.y = self.y >= 128 ? 32 : 448 - @gold_window.height
            end
            @gold_window.opacity = self.opacity
            @gold_window.back_opacity = self.back_opacity
          end
        when "\003"
          if @gold_window == nil
            @gold_window = Window_Trade.new
            @gold_window.x = 600 - @gold_window.width
            @gold_window.y = ($game_temp.in_battle ? 192 : (self.y >= 128 ? 32 : 448 - @gold_window.height))
            @gold_window.opacity = self.opacity
            @gold_window.back_opacity = self.back_opacity
          end
        when "\004"
          text.sub!(/\[([0-9]+)\]/, '')
          $game_system.message_walking = false
          unless @timer_active
            @timer = $1.to_i
            @timer_active = true
          end
        when "\005"
          text.sub!(/\[([0-9]+)\]/, '')
          unless @timer_active
            @timer = $1.to_i
            @timer_active = true
          end
        when "\006"
          text.sub!(/\[([0-9]+)\]/, '')
          icon = RPG::Cache.icon(icons[$1.to_i])
          self.contents.blt(x+4, 32 * y + 4, icon, Rect.new(0, 0, 24, 24))
          x += self.contents.text_size(' ').width + 24
        when "\007"
          begin
            text.sub!(/\[([0-9]+)\]/, '')
            i = $1.to_i
            face = RPG::Cache.character(faces[i][0], faces[i][1])
            xx = face.width / 8 - 16
            xx = 0 if xx < 0
            xs = ys = 0
            if faces[i][0] == 'faberell X faces' ||
                faces[i][0] == 'grave_guard faces' ||
                faces[i][0] == 'spirit_sword faces'
              xs, ys = faces[i][2]
              xs *= face.width / 4
              ys *= face.height / 4
            end
            self.contents.blt(x+2, 32 * y + 2, face, Rect.new(xx+xs, ys, 32, 24))
            x += 32
          rescue
          end
        when "\n"
          @cursor_width = x if @cursor_width < x && y >= $game_temp.choice_start
          y += 1
          x = (y >= $game_temp.choice_start ? 8 : 0)
        else
          self.contents.font.color = text_color(color)
          font = self.contents.font.name
          if c == '×'
            self.contents.font.name = 'Arial'
            self.contents.font.bold = false
            if self.opacity == 0
              self.contents.draw_text_outline(x+4, 32 * y + 2, 40, 32, c)
            else
              self.contents.draw_text(x+4, 32 * y + 2, 40, 32, c)
            end
          elsif self.opacity == 0
            self.contents.draw_text_outline(x+4, 32 * y, 40, 32, c)
          else
            self.contents.draw_text(x+4, 32 * y, 40, 32, c)
          end
          self.contents.font.name = font
          self.contents.font.bold = true if font == 'Papyrus'
          x += self.contents.text_size(c).width
        end
        first = 0 if first != 1
      end
    end
    if $game_temp.choice_max > 0
      @item_max = $game_temp.choice_max
      self.active = true
      self.index = 0
    end
    if $game_temp.num_input_variable_id > 0
      digits_max = $game_temp.num_input_digits_max
      number = $game_variables[$game_temp.num_input_variable_id]
      @input_number_window = Window_InputNumber.new(digits_max, (self.opacity == 0))
      @input_number_window.number = number
      @input_number_window.x = self.x + 16
      @input_number_window.y = self.y + y * 32
    end
  end
  
  def reset_window(flag = false)
    if $game_temp.in_battle
      self.y = 16
    elsif !$game_switches[230] && $game_system.message_position != 1 &&
        @rotator.host != nil
      self.y = (@rotator.host.screen_y > 288 ? 16 : 304)
    else
      self.y = CP::Cache::MessageWindow[$game_system.message_position]
    end
    self.y += 70 unless flag
    skinsetup
  end
  
  def skinsetup
    if @frame != $game_system.message_frame
      if $game_system.message_frame == 0
        self.windowskin = RPG::Cache.windowskin(@windowskin_name)
      else
        bitmap = RPG::Cache.windowskin('Black Death').clone
        bitmap.fill_rect(128, 64, 64, 64, Color.new(0, 0, 0, 0))
        bitmap.blt(128, 64, self.windowskin, Rect.new(128, 64, 64, 64))
        self.windowskin, self.opacity = bitmap, 0
      end
      @frame = $game_system.message_frame
    end
  end
  
  def update
    super
    if @fade_in
      skinsetup
      if $game_system.message_frame == 0
        self.opacity, self.back_opacity = 255, 160
        if self.height >= 160
          @input_number_window.contents_opacity = 255 if @input_number_window != nil
          self.height, self.contents_opacity, @fade_in = 160, 255, false
          refresh
        else
          self.height += 20
          self.y -= 10
        end
      else
        self.height, self.back_opacity = 160, 255
        reset_window(true)
        refresh if self.contents_opacity == 0
        self.opacity += 12
        self.contents_opacity += 24
        @input_number_window.contents_opacity += 24 if @input_number_window != nil
        @fade_in = false if self.contents_opacity == 255
      end
    elsif @input_number_window != nil
      @input_number_window.update
      if Input.trigger?($controls.confirm)
        $game_system.se_play($data_system.decision_se)
        $game_variables[$game_temp.num_input_variable_id] =
            @input_number_window.number
        @input_number_window.dispose
        $game_map.need_refresh, @input_number_window = true, nil
        terminate_message
      end
    elsif @contents_showing
      self.pause = true if $game_temp.choice_max == 0
      if Input.trigger?($controls.cancel) &&
          $game_temp.choice_max > 0 && $game_temp.choice_cancel_type > 0
        $game_system.se_play($data_system.cancel_se)
        $game_temp.choice_proc.call($game_temp.choice_cancel_type - 1)
        terminate_message
      end
      if Input.press?($controls.confirm)
        if $game_temp.choice_max > 0
          if Input.trigger?($controls.confirm)
            $game_system.se_play($data_system.decision_se)
            $game_temp.choice_proc.call(self.index)
            terminate_message
          end
        else
          terminate_message
        end
      end
    elsif @fade_out == false && $game_temp.message_text != nil
      update_rotator(true) unless $game_temp.message_window_showing
      @contents_showing = $game_temp.message_window_showing = true
      reset_window
      Graphics.frame_reset
      self.visible, self.contents_opacity = true, 0
      @input_number_window.contents_opacity = 0 if @input_number_window != nil
      @fade_in = true
    elsif self.visible
      @fade_out = true
      @rotator.host = nil if $game_temp.message_text == nil
      if $game_system.message_frame == 0
        unless self.contents == nil || self.contents.disposed?
          self.contents.dispose
        end
        update_rotator
        self.contents = nil
        if self.opacity == 0
          self.height, @fade_out = 20, false
          if $game_temp.message_text == nil
            $game_temp.message_window_showing = self.visible = false
            reset_window
          end
        elsif self.height <= 20
          self.opacity = 0
        else
          self.height -= 20
          self.y += 10
        end
      elsif self.contents_opacity == 0
        unless self.contents == nil || self.contents.disposed?
          self.contents.dispose
          update_rotator
        end
        self.contents, @fade_out = nil, false
        if $game_temp.message_text == nil
          $game_temp.message_window_showing = self.visible = false
          self.height = 20
          reset_window
        end
      else
        self.contents_opacity -= 24
        self.opacity -= 12
      end
    end
    @rotator.update
  end
  
  def update_cursor_rect
    if @index >= 0
      n = $game_temp.choice_start + @index
      self.cursor_rect.set(8, n * 32, @cursor_width, 32)
    else
      self.cursor_rect.empty
    end
  end
  
  def dispose
    @rotator.dispose
    @rotator = nil
    super
  end
  
end
