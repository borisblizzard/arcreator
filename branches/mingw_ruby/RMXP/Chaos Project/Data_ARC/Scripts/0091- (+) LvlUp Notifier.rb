#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=
# Easy LvlUp Notifier by Blizzard
# Version: 2.0 DX
# Type: Battle Report Display
#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=

#============================================================================== 
# Game_Actor 
#============================================================================== 

class Game_Actor < Game_Battler 
  
  def all_exp
    return @exp
  end 
  
  def all_exp=(exp)
    @exp = exp
  end 

end

#==============================================================================
# Window_LevelUp
#==============================================================================

class Window_LevelUp < Window_Base
  
  attr_reader :limit
  
  def initialize(a, d)
    x = case $game_party.actors.size
    when 1 then 240
    when 2 then a.index * 320 + 80
    when 3 then a.index * 160 + 80
    when 4 then a.index * 160
    end
    text = []
    text.push(['Level:', d[0], a.level]) if d[0] != a.level
    text.push([$data_system.words.hp[0, 3], d[1], a.maxhp]) if d[1] != a.maxhp
    text.push([$data_system.words.sp[0, 3], d[2], a.maxsp]) if d[2] != a.maxsp
    text.push([$data_system.words.str[0, 3], d[3], a.str]) if d[3] != a.str
    text.push([$data_system.words.dex[0, 3], d[4], a.dex]) if d[4] != a.dex
    text.push([$data_system.words.agi[0, 3], d[5], a.agi]) if d[5] != a.agi
    text.push([$data_system.words.int[0, 3], d[6], a.int]) if d[6] != a.int
    h = text.size * 24 + 56
    @limit, y = 320 - h, 480 - h + (h/64+1)*64
    super(x, y, 160, h)
    self.z = 100
    self.contents = Bitmap.new(self.width - 32, self.height - 32)
    if $fontface != nil
      self.contents.font.name = $fontface
    elsif $defaultfonttype != nil
      self.contents.font.name = $defaultfonttype
    end
    if $fontface == 'Papyrus'
      self.contents.font.size = 26
    elsif $fontface == 'Future'
      self.contents.font.size = 18
    else
      self.contents.font.size = 20
    end
    self.contents.font.bold = true
    self.contents.font.color = normal_color
    self.contents.draw_text(0, 0, 128, 24, "#{a.exp - d[7]} EXP", 1)
    text.each_index {|i|
        index = i + 1
        self.contents.font.color = system_color
        self.contents.draw_text(0, index*24, 128, 24, text[i][0])
        self.contents.draw_text(78, index*24, 32, 24, '»')
        self.contents.font.color = normal_color
        self.contents.draw_text(0, index*24, 76, 24, text[i][1].to_s, 2)
        if text[i][1] > text[i][2]
          self.contents.font.color = Color.new(255, 64, 0)
        else
          self.contents.font.color = Color.new(0, 255, 64)
        end
        self.contents.draw_text(0, index*24, 128, 24, text[i][2].to_s, 2)}
  end
  
end

#============================================================================== 
# Scene_Battle
#============================================================================== 

class Scene_Battle
  
  alias main_lvlup_later main
  def main
    @lvlup_data = {}
    @moving_windows, @pending_windows = [], []
    (1...$data_actors.size).each {|i|
        actor = $game_actors[i]
        @lvlup_data[actor] = [actor.level, actor.maxhp, actor.maxsp, actor.str,
            actor.dex, actor.agi, actor.int, actor.exp, actor.skills.clone]}
    main_lvlup_later
    (@moving_windows + @pending_windows).each {|win| win.dispose if win != nil}
  end
  
  alias return_in_time_lvlup_later return_in_time
  def return_in_time
    return if @time.size < 2
    actors = $game_party.actors.clone
    return_in_time_lvlup_later
    actors.each_index {|i|
        @lvlup_data[$game_party.actors[i]] = @lvlup_data[actors[i]]
        @lvlup_data.delete(actors[i])}
  end
  
  alias start_phase5_lvlup_later start_phase5
  def start_phase5
    $game_party.actors.each {|actor| actor.remove_states_battle}
    @start_win = 0
    start_phase5_lvlup_later
    $game_temp.battle_main_phase = false
    @phase5_wait_count = (@escaped ? 0 : 30)
    @skill_texts = []
    $game_party.actors.each {|actor|
        if @lvlup_data[actor][0] != actor.level ||
            @lvlup_data[actor][8] != actor.skills
          @pending_windows.push(Window_LevelUp.new(actor, @lvlup_data[actor]))
          @skill_texts.push('')
          (actor.skills - @lvlup_data[actor][8]).each {|id|
              @skill_texts.push("#{actor.name} learned #{$data_skills[id].name}!")}
        elsif !actor.cant_get_exp? && (@escaped ||
            @lvlup_data[actor][7] != actor.exp)
          @moving_windows.push(Window_LevelUp.new(actor, @lvlup_data[actor]))
        end}
    @status_window.refresh
    @help_window.set_text('Absconded', 1) if @escaped
  end
  
  def update_phase5
    if @phase5_wait_count > 0
      @phase5_wait_count -= 1
      if @phase5_wait_count == 0
        @result_window.visible, $game_temp.battle_main_phase = true, false
        @status_window.refresh
      end
      return
    end
    moving = false
    @moving_windows.each {|win|
        if win.y > win.limit
          cc = ((win.y - win.limit) / 2.0).ceil
          win.y -= (cc > 64 ? 64 : cc)
          moving = true
        end}
    if !moving && Input.trigger?($controls.confirm)
      @result_window.visible = false
      if @skill_texts.size > 0
        text = @skill_texts.shift
        if text == ''
          $game_system.se_play(RPG::AudioFile.new('087-Action02', 80, 100))
          @moving_windows.push(@pending_windows.shift)
          @help_window.visible = false
        else
          $game_system.se_play(RPG::AudioFile.new('106-Heal02', 80, 100))
          @help_window.set_text(text, 1)
        end
      else
        battle_end(@escaped ? 1 : 0)
      end
    end
  end
  
end
