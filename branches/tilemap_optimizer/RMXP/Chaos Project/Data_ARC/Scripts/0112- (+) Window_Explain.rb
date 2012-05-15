#==============================================================================
# Game_System
#==============================================================================

class Game_System
  
  attr_accessor :info_pages
  attr_accessor :total_money
  attr_accessor :most_money
  attr_accessor :kill_arshes
  attr_accessor :beasts
  attr_accessor :fights
  attr_accessor :escaped
  attr_accessor :max_damage
  attr_reader   :fish
  attr_writer   :total_damage
  
  alias init_table_later initialize
  def initialize
    init_table_later
    @info_pages = [false, false, false, false, false, false, false]
    @beasts, @fish = [], [0.0, 0]
    @total_money = @most_money = @kill_arshes = @fights = @max_damage =
        @total_damage = 0
  end
  
  def caught=(data)
    @fish[0] = data[0] if data[0] > @fish[0]
    @fish[1] = data[1] if data[1] > @fish[1]
  end
  
  def total_damage
    return (@total_damage != nil ? @total_damage : 0)
  end
  
end
  
#==============================================================================
# Window_Base
#==============================================================================

class Window_Base
  
  def draw_enemy_battler(enemy, w, h)
    if enemy != nil && enemy.battler_name != ''
      bitmap = RPG::Cache.battler(enemy.battler_name, enemy.battler_hue)
      bitmap_w, bitmap_h = bitmap.width / 2, bitmap.height / 2
      src_rect = Rect.new(0, 0, bitmap.width, bitmap.height)
      self.contents.blt(w/2 - bitmap_w, h/2 - bitmap_h, bitmap, src_rect)
    end
  end
    
end

#==============================================================================
# Window_AdCommand
#==============================================================================

class Window_AdCommand < Window_Command
  
  def initialize(width, commands1, commands2, commands3)
    @commands2, @commands3 = commands2, commands3
    super(width, commands1)
  end
  
  def refresh
    super
    (0...@item_max).each {|i|
        draw_item2(i, system_color, @commands2[i], false)
        draw_item2(i, system_color, @commands3[i], true)}
  end

  def draw_item2(index, color, command, flag)
    x = (flag ? 384 : 208)
    rect1 = Rect.new(x, 32 * index, self.contents.width - 8, 32)
    rect2 = Rect.new(x + 64, 32 * index, 64, 32)
    self.contents.font.color = color
    self.contents.draw_text(rect1, command[0])
    self.contents.font.color = normal_color
    self.contents.draw_text(rect2, command[1], 2)
  end
    
end

#==============================================================================
# Window_ListCommand
#==============================================================================

class Window_ListCommand < Window_Command
  
  def initialize(width, commands)
    commands, @bosses = commands
    super(width, commands)
  end
  
  def refresh
    self.contents.clear
    (0...@item_max).each {|i|
        draw_item(i, @bosses[i] ? down_color : normal_color)}
  end
      
end

#==============================================================================
# Window_HybridExplain
#==============================================================================

MAXMODE = 7

class Window_HybridExplain < Window_Base
  
  attr_accessor :index
  attr_accessor :help_window
  attr_accessor :mode
  
  def initialize(page_index = 0)
    @background, @sx, @sy = 'Menu_back', 0, 0
    super(0, 512, 640, 480)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.contents.font.name = $fontface
    if $fontface == 'Papyrus'
      self.contents.font.size = 30
      self.contents.font.bold = true
    else
      self.contents.font.size = 24
    end
    self.contents.font.color = normal_color
    @item_max = 0
    @mode = page_index
    @index = -1
    @sec = Graphics.frame_count / Graphics.frame_rate
    @enemies, names, bosses = [], [], []
    $game_system.beasts.each_index {|i|
        enemy = $data_enemies[$game_system.beasts[i]]
        next if enemy.name == '???' || enemy.name == ''
        @enemies.push(enemy)
        names.push(sprintf(" %03d.  #{enemy.name}", i+1))
        bosses.push(enemy.element_ranks[CP::Cache::DBoss] != 3 ||
            enemy.element_ranks[CP::Cache::DSBoss] != 3)}
    metas1, metas2, metas3 = [], [], []
    (0...20).each {|i|
        metas1.push(CP.meta_text(i+1))
        metas2.push(["#{$data_system.words.hp} over", "#{100*(4-(i%5))/5}%"])
        metas3.push(["SR over", "#{i/5*30}%"])}
    @meta_page = Window_AdCommand.new(560, metas1, metas2, metas3)
    @meta_page.x, @meta_page.y, @meta_page.z = 40, 72, 27999
    @meta_page.height, @meta_page.index, @meta_page.opacity = 384, 0, 0
    @monster_page = Window_ListCommand.new(320, [names, bosses])
    @monster_page.x, @monster_page.y, @monster_page.z = 40, 56, 27999
    @monster_page.height, @monster_page.index, @monster_page.opacity = 416, 0, 0
    @meta_page.visible, @monster_page.visible, self.z = false, false, 24999
  end
  
  def refresh
    self.contents.clear
    rect = Rect.new(0, 0, 24, 24)
    case @mode
    when 0
      title = 'Elements'
      sym = 'Symbols'
      table = 'Table of efficiency'
      w = self.contents.text_size(sym).width
      self.contents.draw_text(40, 64, w, 32, sym)
      w = self.contents.text_size(table).width + 8
      self.contents.draw_text(240, 64, w, 32, table)
      (2...10).each {|i|
          factor = [64 * ((i-2) % 4 + 2), (i-2)/4 * 120]
          icon = RPG::Cache.icon("elm_#{$data_system.elements[i-1].downcase}")
          self.contents.blt(40, 32 * (i+1) + 4, icon, rect)
          w = self.contents.text_size("- #{$data_system.elements[i-1]}").width
          self.contents.draw_text(72, 32*(i+1), w, 32, "- #{$data_system.elements[i-1]}")
          self.contents.blt(240+factor[1], factor[0]-28, icon, rect)
          self.contents.blt(240+factor[1], factor[0]+4, icon, rect)
          w = self.contents.text_size('»').width
          h = self.contents.text_size('»').height
          self.contents.draw_text(272+factor[1], factor[0]-28, w, h, '»')
          self.contents.draw_text(272+factor[1], factor[0]+4, w, h, '»')
          elm2 = case (i - 1)
          when 1 then [2, 8]
          when 2 then [4, 7]
          when 3 then [4, 6]
          when 4 then [1, 5]
          when 5 then [3, 6]
          when 6 then [1, 5]
          when 7 then [3, 8]
          when 8 then [2, 7]
          end
          icons = [RPG::Cache.icon("elm_#{$data_system.elements[elm2[0]].downcase}"),
                   RPG::Cache.icon("elm_#{$data_system.elements[elm2[1]].downcase}")]
          self.contents.blt(280+w+factor[1], factor[0]-28, icons[0], rect)
          self.contents.blt(280+w+factor[1], factor[0]+4, icons[1], rect)}
    when 1
      self.index = -1
      @help_window.visible = false
      title = 'Monster Status'
      unless $game_party.monster == nil
        health = 'Health:'
        power = 'Power:'
        aggressive = 'Aggressive:'
        speed = 'Speed:'
        obey = 'Obey:'
        exp = 'EXP:'
        fought = 'Fights fought:'
        won = 'Fights won:'
        offset = 0
        draw_actor_name($game_party.monster, 40, 64)
        draw_actor_graphic($game_party.monster, 56, 160)
        (0...8).each {|i|
            case i
            when 0 then text1, text2 = health, $game_party.monster.health.to_s
            when 1 then text1, text2 = power, $game_party.monster.power.to_s
            when 2 then text1, text2 = aggressive, $game_party.monster.aggressive.to_s
            when 3 then text1, text2 = speed, $game_party.monster.speed.to_s
            when 4 then text1, text2 = obey, $game_party.monster.obey.to_s
            when 5 then text1, text2 = exp, $game_party.monster.exp.to_s
            when 6 then text1, text2 = fought, $game_party.monster.fights.to_s
            when 7 then text1, text2 = won, $game_party.monster.won.to_s
            else
              text1 = text2 = ''
            end
            self.contents.draw_text(96, 96 + i*32, 128, 32, text1)
            self.contents.draw_text(96, 96 + i*32, 208 + offset, 32, text2, 2)}
      end
    when 2
      @help_window.visible = true
      title = 'Status Effects'
      states = $data_states[1, 8] |
              [$data_states[17]] |
               $data_states[30, 3] |
               $data_states[13, 4] |
              [$data_states[34], $data_states[38], $data_states[18]] |
               $data_states[9, 4] |
              [$data_states[39]] |
               $data_states[19, 9] |
              [$data_states[37], $data_states[40]]
      states.each_index {|i|
          icon = RPG::Cache.icon("stat_#{states[i].name.downcase}")
          self.contents.blt(36+i/12*180, 32 * (i%12+2) + 4, icon, rect)
          self.contents.draw_text(66+i/12*180, 32 * (i%12+2), 144, 32, states[i].name)}
      if $game_system.info_pages[@mode]
        self.index = 0
        @item_max = states.size
      else
        self.index = -1
        @item_max = 0
      end
    when 3
      @meta_page.visible, @help_window.visible, @bag = false, true, []
      ary = CP.resort_items
      (1...ary.size).each {|i|
          if CP::Cache::Trade.include?(ary[i].id)
            @bag.push(ary[i]) if $game_party.item_number(ary[i].id) > 0
          end}
      if $game_system.info_pages[@mode] && @bag.size > 0
        self.index, @item_max = 0, @bag.size
      else
        self.index, @item_max = -1, 0
      end
      @bag.each_index {|i|
          icon = RPG::Cache.icon(@bag[i].icon_name)
          self.contents.blt(36+i/12*270, 32 * (i%12+2) + 4, icon, rect)
          self.contents.draw_text(66+i/12*270, 32 * (i%12+2), 234, 32, @bag[i].name)
          self.contents.draw_text(242+i/12*270, 32 * (i%12+2), 8, 32, ':')
          self.contents.draw_text(250+i/12*270, 32 * (i%12+2), 40, 32, $game_party.item_number(@bag[i].id).to_s, 2)}
      title = 'Trading Bag'
    when 4
      self.index = -1
      @help_window.visible, @monster_page.visible = true, false
      title = 'Meta Explanations'
    when 5
      self.index = -1
      @help_window.visible = @meta_page.visible = false
      draw_enemy_battler(@enemies[@monster_page.index], self.contents.width, self.contents.height)
      title = 'Monster Gallery'
    when 6
      @monster_page.visible = false
      title = 'Game Statistics'
      (0...15).each {|i|
          case i
          when 0
            text = "Times game saved:  #{$game_system.save_count}"
          when 1
            text = 'Time played:  '
            @sec = Graphics.frame_count / Graphics.frame_rate
            @sec = 359999 if @sec > 359999
            text += sprintf('%02d:%02d:%02d', @sec/60/60, @sec/60%60, @sec%60)
          when 2
            text = "Days past in game:  #{$game_system.day_count}"
          when 3
            text = "Steps:  #{$game_party.steps}"
          when 4
            count = 0
            $game_system.info_pages.each {|page| count += 1 if page}
            text = "Information pages unlocked:  #{count} / 7"
          when 5
            text = "Highscore in \"Kill Arshes\":  #{$game_system.kill_arshes}"
          when 6
            text = 'Biggest fish caught:  '
            text += "#{$game_system.fish[0]}cm, #{$game_system.fish[1]}g"
          when 7
            text = 'Most money ever had:  '
            text += "#{$game_system.most_money} #{$data_system.words.gold}"
          when 8
            text = 'Total money acquired:  '
            text += "#{$game_system.total_money} #{$data_system.words.gold}"
          when 9
            text = "Battles fought:  #{$game_system.fights}"
          when 10
            text = "Enemies met:  #{$game_system.beasts.size} / 137"
          when 11
            text = "Highest damage ever done:  #{$game_system.max_damage}"
          when 12
            text = "Total damage done:  #{$game_system.total_damage}"
          else
            text = ''
          end
          w = self.contents.text_size(text).width + 8
          self.contents.draw_text(72, 30 * (i+2), w, 32, text)}
    end
    save_color = self.contents.font.color.clone
    self.contents.font.color = system_color
    self.contents.draw_text(4, 0, self.width-40, 32, title, 1)
    self.contents.font.color = save_color
    if !$game_system.info_pages[@mode]
      self.contents.clear
      text = 'Page not available'
      self.contents.draw_text(4, (height-64)/2, self.width-40, 32, text, 1)
    else
      case @mode
      when 2 then @help_window.set_text(get_description, 1)
      when 3
        if @item_max == 0
          @help_window.set_text('The Trading Bag is empty.', 1)
        else
          @help_window.set_text(@bag[self.index].description, 1)
        end
      when 4
        @meta_page.visible = true
        @help_window.set_text(get_meta, 1)
      when 5 then @monster_page.visible = true
      end
    end
    save_size = self.contents.font.size
    self.contents.font.size = 90
    y = (self.height - 32)/2 - (self.contents.text_size('»').height*1.5/2).to_i
    x = self.width - (self.contents.text_size('»').width/1.5).to_i - 32
    w = self.contents.text_size('»').width
    h = self.contents.text_size('»').height
    self.contents.draw_text(0, y, (w/1.5).to_i, (h*1.5).to_i, '«')
    self.contents.draw_text(x, y, (w/1.5).to_i, (h*1.5).to_i, '»')
    self.contents.font.size = save_size
    self.contents.draw_text(4, 0, 160, 32, "Page #{@mode+1} / 7")
    update_cursor_rect
  end
  
  def get_description
    text = case @index
    when 0 then 'Can\'t act, can\'t gain EXP, can\'t be attacked.'
    when 1 then 'Can\'t act.'
    when 2 then 'Gets progressive damage.'
    when 3 then 'The accuracy of the character\'s attacks decreases to 20%.'
    when 4 then 'Unable to cast magic-based spells.'
    when 5 then 'Out of control and attacks anybody.'
    when 6 then 'Can\'t act, but can easily be woken up by an attack.'
    when 7 then 'Can\'t act for a longer period of time.'
    when 8 then 'Can\'t use magic-based spells and gets progressive damage.'
    when 9 then 'Gets progressive healing.'
    when 10 then 'Casts spells and uses abilities at half MP cost.'
    when 11 then 'Automatic removing of the "Defeated" status (once).'
    when 12 then 'Increased attack power.'
    when 13 then 'Increased physical defense.'
    when 14 then 'Increased magical resistance.'
    when 15 then 'Increased evasion probability.'
    when 16 then 'Increased agility and speed.'
    when 17 then 'Increased magical attack power (Intelligence).'
    when 18 then 'Increased attack power and increased "Critical Hit Rate".'
    when 19 then 'Decreased attack power.'
    when 20 then 'Decreased physical defense.'
    when 21 then 'Decreased agility and speed.'
    when 22 then 'Decreased magical attack power (Intelligence).'
    when 23 then 'Decreased magical defense.'
    when 24 then 'Shield against fire-elemental based attacks and spells.'
    when 25 then 'Shield against ice-elemental based attacks and spells.'
    when 26 then 'Shield against electro-elemental based attacks and spells.'
    when 27 then 'Shield against water-elemental based attacks and spells.'
    when 28 then 'Shield against earth-elemental based attacks and spells.'
    when 29 then 'Shield against air-elemental based attacks and spells.'
    when 30 then 'Shield against light-elemental based attacks and spells.'
    when 31 then 'Shield against dark-elemental based attacks and spells.'
    when 32 then 'Shield against any elemental based attacks and spells.'
    when 33 then 'Doubled physical and magical defense.'
    when 34 then 'Reflects magic-based abilities back at the user/enemies.'
    else
      ''
    end
    return text
  end
    
  def get_meta
    return '' if @mode != 4
    text = case (@meta_page.index + 1)
    when 1 then 'No special effect.'
    when 2 then 'No special effect.'
    when 3 then 'No special effect.'
    when 4 then 'No special effect.'
    when 5 then 'No special effect.'
    when 6 then 'No special effect.'
    when 7 then '100% Hit rate and 100% Ability success.'
    when 8 then 'No special effect.'
    when 9 then 'Slightly lower physical defense.'
    when 10 then '50% higher Critical Hit Rate.'
    when 11 then 'Slightly higher physical defense.'
    when 12 then 'Only 33% damage instead of 50% when "defending".'
    when 13 then 'No special effect.'
    when 14 then '100% Hit rate and 100% Ability success.'
    when 15 then '100% higher Critical Hit Rate.'
    when 16 then '33% higher ability damage.'
    when 17 then '25% chance to cancel an enemy attack.'
    when 18 then '50% chance of counterattacking the enemy.'
    when 19 then '100% Hit rate and 100% Ability success.'
    when 20 then 'Meta Limit available (consumes 90% SR).'
    else
      ''
    end
    return text
  end
  
  def update_cursor_rect
    if @index < 0
      self.cursor_rect.empty
    else
      ex = (@mode.between?(2, 3) ? @mode * 90 : nil)
      self.cursor_rect.set(@index/12*ex+32, @index%12*32+64-self.oy, ex, 32) if ex != nil
    end
  end
  
  def update
    super
    refresh if Graphics.frame_count / Graphics.frame_rate != @sec && @mode == 6
    if @mode == 2 && $game_system.info_pages[@mode]
      if @index >= 0
        if Input.repeat?($controls.up)
          if Input.trigger?($controls.up) || @index != 0
            @index = (@index + @item_max - 1) % @item_max
            $game_system.se_play($data_system.cursor_se)
            @help_window.set_text(get_description, 1)
          end
        elsif Input.repeat?($controls.down)
          if Input.trigger?($controls.down) || @index < @item_max - 1
            @index = (@index + 1) % @item_max
            $game_system.se_play($data_system.cursor_se)
            @help_window.set_text(get_description, 1)
          end
        elsif Input.repeat?($controls.right)
          if Input.trigger?($controls.right) || @index / 12 < 2
            $game_system.se_play($data_system.cursor_se)
            if @index / 12 < 2
              @index += 12 if @index < @item_max - 10
              @index = 34 if @index == 35
              @help_window.set_text(get_description, 1)
            else
              @mode = (@mode + 1) % MAXMODE
              @help_window.set_text('')
              refresh
            end
          end
        elsif Input.repeat?($controls.left)
          if Input.trigger?($controls.left) || @index / 12 > 0
            $game_system.se_play($data_system.cursor_se)
            if @index / 12 > 0
              @index -= 12 if @index >= 12
              $game_system.se_play($data_system.cursor_se)
              @help_window.set_text(get_description, 1)
            else
              @mode = (@mode + MAXMODE - 1) % MAXMODE
              @help_window.set_text('')
              refresh
            end
          end
        end
      end
    elsif @mode == 3 && $game_system.info_pages[@mode] && @item_max > 0
      if @index >= 0
        if Input.repeat?($controls.up)
          if Input.trigger?($controls.up) || @index != 0
            @index = (@index + @item_max - 1) % @item_max
            $game_system.se_play($data_system.cursor_se)
            @help_window.set_text(@bag[self.index].description, 1)
          end
        elsif Input.repeat?($controls.down)
          if Input.trigger?($controls.down) || @index < @item_max - 1
            @index = (@index + 1) % @item_max
            $game_system.se_play($data_system.cursor_se)
            @help_window.set_text(@bag[self.index].description, 1)
          end
        elsif Input.repeat?($controls.right)
          if Input.trigger?($controls.right) || @index / 12 < (@bag.size-1) / 12
            $game_system.se_play($data_system.cursor_se)
            if @index / 12 < (@bag.size-1) / 12
              @index += 12 if @index < @item_max - 10
              @index = @bag.size-1 if @index >= @bag.size
              @help_window.set_text(@bag[self.index].description, 1)
            else
              @mode = (@mode + 1) % MAXMODE
              @help_window.set_text('')
              refresh
            end
          end
        elsif Input.repeat?($controls.left)
          if Input.trigger?($controls.left) || @index / 12 > 0
            $game_system.se_play($data_system.cursor_se)
            if @index / 12 > 0
              @index -= 12 if @index >= 12
              @help_window.set_text(@bag[self.index].description, 1)
            else
              @mode = (@mode + MAXMODE - 1) % MAXMODE
              @help_window.set_text('')
              refresh
            end
          end
        end
      end
    else
      if @mode == 4
        old_index, old_mode = @meta_page.index, @mode
      elsif @mode == 5
        old_index, old_mode = @monster_page.index, @mode
      end
      if Input.repeat?($controls.right)
        if Input.trigger?($controls.right)
          $game_system.se_play($data_system.cursor_se)
          @mode = (@mode + 1) % MAXMODE
          @help_window.set_text('')
          refresh
        end
      elsif Input.repeat?($controls.left)
        if Input.trigger?($controls.left)
          $game_system.se_play($data_system.cursor_se)
          @mode = (@mode + MAXMODE - 1) % MAXMODE
          @help_window.set_text('')
          refresh
        end
      end
      if old_mode == @mode
        if @mode == 4
          @meta_page.update
          refresh if old_index != @meta_page.index
        elsif @mode == 5
          @monster_page.update
          refresh if old_index != @monster_page.index
        end
      end
    end
    update_cursor_rect
  end

  alias dispose_later dispose
  def dispose
    [@monster_page, @meta_page].each {|page| page.dispose}
    dispose_later
  end
  
end

#==============================================================================
# Scene_Battle
#==============================================================================

class Scene_Battle
  
  alias main_beast_later main
  def main
    @log = true
    main_beast_later
  end
    
  alias update_beast_later update
  def update
    if @log
      @log = false
      $game_troop.enemies.each {|enemy|
          if !$game_system.beasts.include?(enemy.id) &&
              CP::Cache::MainParty.any? {|i|
                  $game_party.actors.include?($game_actors[i])} &&
              !CP::Cache::NoLog.include?(enemy.id)
            $game_system.beasts.push(enemy.id)
          end}
    end
    update_beast_later
  end
  
end
