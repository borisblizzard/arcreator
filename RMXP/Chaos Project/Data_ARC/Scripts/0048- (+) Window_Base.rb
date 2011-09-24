#==============================================================================
# Window_Base
#==============================================================================

class Window_Base < Window
  
  def initialize(x, y, w, h)
    super()
    @windowskin_name = $game_system.windowskin_name
    self.windowskin = RPG::Cache.windowskin(@windowskin_name)
    self.x, self.y, self.width, self.height, self.z = x, y, w, h, 100
  end
  
  def setup_skin
    if @windowskin_name != $game_system.windowskin_name
      @windowskin_name = $game_system.windowskin_name
      self.windowskin = RPG::Cache.windowskin(@windowskin_name)
    end
  end
  
  def dispose
    if !self.disposed? && self.contents != nil && !self.contents.disposed?
      self.contents.dispose
    end
    super
  end
  
  def text_color(n)
    return case n
    when 0 then Color.new(255, 255, 255)
    when 1 then Color.new(96, 128, 255)
    when 2 then Color.new(255, 0, 0)
    when 3 then Color.new(0, 255, 0)
    when 4 then Color.new(0, 255, 255)
    when 5 then Color.new(255, 0, 255)
    when 6 then Color.new(255, 255, 0)
    when 7 then Color.new(160, 160, 160)
    when 8 then Color.new(255, 128, 0)
    when 9 then Color.new(160, 64, 255)
    when 99 then Color.new(0, 0, 0)
    else
      normal_color
    end
  end
  
  def normal_color
    return Color.new(255, 255, 255, 255)
  end
  
  def disabled_color
    return Color.new(255, 255, 255, 128)
  end
  
  def system_color
    return Color.new(128, 192, 255, 255)
  end
  
  def crisis_color
    return Color.new(255, 255, 0, 255)
  end
  
  def knockout_color
    return Color.new(255, 0, 0)
  end
  
  def update
    super
    setup_skin
  end
  
  def draw_actor_graphic(actor, x, y)
    bitmap = RPG::Cache.character(actor.character_name, actor.character_hue)
    cw = bitmap.width / 4
    ch = bitmap.height / 4
    src_rect = Rect.new(0, 0, cw, ch)
    self.contents.blt(x - cw / 2, y - ch, bitmap, src_rect)
  end
  
  def draw_actor_name(actor, x, y)
    self.contents.font.color = normal_color
    self.contents.draw_text(x, y, 120, 32, actor.name)
  end
  
  def draw_actor_class(actor, x, y)
    self.contents.font.color = normal_color
    self.contents.draw_text(x, y, 236, 32, actor.class_name)
  end
  
  def draw_actor_level(actor, x, y)
    self.contents.font.color = system_color
    self.contents.draw_text(x, y, 32, 32, 'Lv')
    self.contents.font.color = normal_color
    self.contents.draw_text(x + 16, y, 40, 32, actor.level.to_s, 2)
  end
  
  def draw_actor_state(actor, x, y, width = 120)
    text = make_battler_state_text(actor, width, true)
    self.contents.font.color = actor.hp == 0 ? knockout_color : normal_color
    self.contents.draw_text(x, y, width, 32, text)
  end
  
  def draw_actor_exp(actor, x, y)
    self.contents.font.color = system_color
    self.contents.draw_text(x, y, 48, 32, 'EXP')
    if actor.exp_s.to_i > 9999999
      w = self.contents.text_size('9999999').width
    else
      w = self.contents.text_size(actor.exp_s).width
    end
    if actor.next_exp_s.to_i > 9999999
      w2 = self.contents.text_size('9999999').width
    else
      w2 = self.contents.text_size(actor.next_exp_s).width
    end
    self.contents.font.color = normal_color
    self.contents.draw_text(x + 108 - w2, y, w2, 32, actor.exp_s, 2)
    self.contents.draw_text(x + 108, y, 12, 32, '/', 1)
    self.contents.draw_text(x + 120, y, w2, 32, actor.next_exp_s)
  end
  
  def draw_actor_hp(actor, x, y, width = 144)
    self.contents.font.color = system_color
    self.contents.draw_text(x, y, 32, 32, $data_system.words.hp)
    if width - 32 >= 108
      hp_x = x + width - 108
      flag = true
    elsif width - 32 >= 48
      hp_x = x + width - 48
      flag = false
    end
    self.contents.font.color = actor.hp == 0 ? knockout_color :
      actor.hp <= actor.maxhp / 4 ? crisis_color : normal_color
    self.contents.draw_text(hp_x - 12, y, 60, 32, actor.hp.to_s, 2)
    if flag
      self.contents.font.color = normal_color
      self.contents.draw_text(hp_x + 48, y, 12, 32, '/', 1)
      self.contents.draw_text(hp_x + 60, y, 48, 32, actor.maxhp.to_s)
    end
  end
  
  def draw_actor_sp(actor, x, y, width = 144)
    self.contents.font.color = system_color
    self.contents.draw_text(x, y, 32, 32, $data_system.words.sp)
    if width - 32 >= 108
      sp_x = x + width - 108
      flag = true
    elsif width - 32 >= 48
      sp_x = x + width - 48
      flag = false
    end
    self.contents.font.color = actor.sp == 0 ? knockout_color :
      actor.sp <= actor.maxsp / 4 ? crisis_color : normal_color
    self.contents.draw_text(sp_x, y, 48, 32, actor.sp.to_s, 2)
    if flag
      self.contents.font.color = normal_color
      self.contents.draw_text(sp_x + 48, y, 12, 32, '/', 1)
      self.contents.draw_text(sp_x + 60, y, 48, 32, actor.maxsp.to_s)
    end
  end
  
  def draw_actor_parameter(actor, x, y, type)
    case type
    when 0 then name, value = $data_system.words.atk, actor.atk
    when 1 then name, value = $data_system.words.pdef, actor.pdef
    when 2 then name, value = $data_system.words.mdef, actor.mdef
    when 3 then name, value = $data_system.words.str, actor.str
    when 4 then name, value = $data_system.words.dex, actor.dex
    when 5 then name, value = $data_system.words.agi, actor.agi
    when 6 then name, value = $data_system.words.int, actor.int
    when 7 then name, value = 'Evasion', actor.eva
    end
    self.contents.font.color = system_color
    self.contents.draw_text(x, y, 120, 32, name)
    self.contents.font.color = normal_color
    self.contents.draw_text(x + 128, y, 44, 32, value.to_s, 2)
  end
  
  def draw_item_name(item, x, y)
    return if item == nil
    bitmap = RPG::Cache.icon(item.icon_name)
    self.contents.blt(x, y + 4, bitmap, Rect.new(0, 0, 24, 24))
    self.contents.font.color = normal_color
    self.contents.draw_text(x + 28, y, 212, 32, item.name)
  end
  
end
