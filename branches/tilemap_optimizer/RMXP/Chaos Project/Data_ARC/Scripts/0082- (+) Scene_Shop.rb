#==============================================================================
# Shop_Sprite
#==============================================================================

class Shop_Sprite < Sprite
  
  def initialize(viewport = nil)
    super
    self.visible = ($game_system.visible_info == true)
    self.bitmap = Bitmap.new(1, 1)
    self.bitmap.font.name = $fontface
    self.bitmap.font.size += 6 if $fontface == 'Papyrus'
    self.z = 20000
    refresh
  end
  
  def set(window)
    self.visible, @window = ($game_system.visible_info == true), window
    refresh
  end
  
  def unset
    self.visible, @window = false, nil
    self.bitmap.dispose unless self.bitmap == nil || self.bitmap.disposed?
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
    return if @window == nil
    self.bitmap = Bitmap.new(1, 1)
    self.bitmap.font.name = $fontface
    text, w = [], 0
    id = case @window.item
    when RPG::Weapon then CP.sr_weapons(@window.item.id)
    when RPG::Armor then CP.sr_armors(@window.item.id)
    end
    if id != nil && id != 0
      text = self.bitmap.slice_bitmap(
          "#{$data_skills[id].name}: #{$data_skills[id].description}")
      text.each {|i|
          tw = self.bitmap.text_size(i).width+16
          w = tw if w < tw}
      w = (w * 1.4).to_i if $fontface == 'Papyrus'
      self.x, self.y = @window.info_position(w / 2)
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
# Window_ShopBuy
#==============================================================================

class Window_ShopBuy < Window_Selectable

  def initialize(shop_goods)
    super(320, 64, 304, 352)
    @shop_goods = []
    weapons, armors, items = CP.resort_weapons, CP.resort_armors, CP.resort_items
    weapons.shift
    armors.shift
    items.shift
    items.each {|item| shop_goods.each {|good|
        @shop_goods.push([0, item.id]) if good[0] == 0 && good[1] == item.id}}
    weapons.each {|weapon| shop_goods.each {|good|
        @shop_goods.push([1, weapon.id]) if good[0] == 1 && good[1] == weapon.id}}
    armors.each {|armor| shop_goods.each {|good|
        @shop_goods.push([2, armor.id]) if good[0] == 2 && good[1] == armor.id}}
    refresh
    self.index = 0
  end

  def item
    return @data[self.index]
  end

  def info_position(w)
    return [self.x - w, self.y + self.cursor_rect.y - 40]
  end
  
  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    @data = []
    @shop_goods.each {|goods_item|
        item = case goods_item[0]
        when 0 then $data_items[goods_item[1]]
        when 1 then $data_weapons[goods_item[1]]
        when 2 then $data_armors[goods_item[1]]
        end
        @data.push(item) if item != nil}
    @item_max = @data.size
    if @item_max > 0
      self.contents = Bitmap.new(width - 32, row_max * 32)
      self.contents.font.name = $fontface
      self.contents.font.size = $fontsize
      self.contents.font.bold = true if $fontface == 'Papyrus'    
      (0...@item_max).each {|i| draw_item(i)}
    end
  end

  def draw_item(index)
    item = @data[index]
    number = case item
    when RPG::Item then $game_party.item_number(item.id)
    when RPG::Weapon then $game_party.weapon_number(item.id)
    when RPG::Armor then $game_party.armor_number(item.id)
    end
    x, y = 4, index*32
    if item.price <= $game_party.gold && number < 100
      self.contents.font.color = normal_color
    else
      self.contents.font.color = disabled_color
    end
    rect = Rect.new(x, y, self.width - 32, 32)
    self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
    if self.contents.font.color == normal_color
      bitmap = RPG::Cache.icon(item.icon_name)
    else
      bitmap = RPG::Cache.desaturated(item.icon_name)
    end
    self.contents.blt(x, y + 4, bitmap, Rect.new(0, 0, 24, 24))
    if item.price <= $game_party.gold && number < 100
      self.contents.font.color = normal_color
    else
      self.contents.font.color = disabled_color
    end
    self.contents.draw_text(x + 28, y, 212, 32, item.name, 0)
    self.contents.draw_text(x + 174, y, 90, 32, item.price.to_s, 2)
  end
  
  def update_help
    @help_window.set_text(self.item == nil ? '' : self.item.description)
  end
  
end

#==============================================================================
# Window_ShopSell
#==============================================================================

class Window_ShopSell < Window_Selectable

  def initialize
    super(16, 64, 608, 352)
    @column_max = 2
    self.z = 4000
    refresh
    self.index = 0
  end

  def item
    return @data[self.index]
  end

  def info_position(w)
    return [self.x + self.width / 2 - w, self.y + self.cursor_rect.y - 40]
  end
  
  def refresh
    if self.contents != nil
      self.contents.dispose
      self.contents = nil
    end
    @data = []
    if $game_switches[196]
      items = CP.resort_items
      items.shift
      CP::Cache::Trade.each {|id|
          @data.push($data_items[id]) if $game_party.item_number(id) > 0}
    else
      weapons, armors, items = CP.resort_weapons, CP.resort_armors, CP.resort_items
      (1...items.size).each {|i|
          if $game_party.item_number(items[i].id) > 0 && items[i].price > 0 &&
              !(CP::Cache::Trade | CP::Cache::Quest).include?(items[i].id)
            @data.push(items[i])
          end}
      (1...weapons.size).each {|i|
          if $game_party.weapon_number(weapons[i].id) > 0 && weapons[i].price > 0
            @data.push(weapons[i])
          end}
      (1...armors.size).each {|i|
          if $game_party.armor_number(armors[i].id) > 0 && armors[i].price > 0
            @data.push(armors[i])
          end}
    end
    @item_max = @data.size
    if @item_max > 0
      self.contents = Bitmap.new(width - 32, row_max * 32)
      self.contents.font.name = $fontface
      self.contents.font.size = $fontsize
      self.contents.font.bold = true if $fontface == 'Papyrus'    
      (0...@item_max).each {|i| draw_item(i)}
    end
  end

  def draw_item(index)
    item = @data[index]
    number = case item
    when RPG::Item then $game_party.item_number(item.id)
    when RPG::Weapon then $game_party.weapon_number(item.id)
    when RPG::Armor then $game_party.armor_number(item.id)
    end
    x, y = 4 + index%2 * 288, index/2 * 32
    if item.price > 0
      self.contents.font.color = normal_color
    else
      self.contents.font.color = disabled_color
    end
    rect = Rect.new(x, y, (self.width - 32) / @column_max, 32)
    self.contents.fill_rect(rect, Color.new(0, 0, 0, 0))
    if self.contents.font.color == normal_color
      bitmap = RPG::Cache.icon(item.icon_name)
    else
      bitmap = RPG::Cache.desaturated(item.icon_name)
    end
    self.contents.blt(x, y + 4, bitmap, Rect.new(0, 0, 24, 24))
    self.contents.draw_text(x + 28, y, 222, 32, item.name, 0)
    self.contents.draw_text(x + 226, y, 16, 32, ':', 1)
    self.contents.draw_text(x + 234, y, 40, 32, number.to_s, 2)
  end

  def update_help
    @help_window.set_text(self.item == nil ? '' : self.item.description)
  end
  
  def update_cursor_rect
    if @index < 0
      self.cursor_rect.empty
      return
    end
    row = @index / @column_max
    self.top_row = row if row < top_row
    self.top_row = row - (page_row_max - 1) if row > top_row + (page_row_max - 1)
    self.cursor_rect.set(index % 2 * 288, index / 2 * 32 - self.oy, 288, 32)
  end
  
end

#==============================================================================
# Window_ShopNumber
#==============================================================================

class Window_ShopNumber < Window_Base

  def initialize
    super(320, 64, 304, 352)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.contents.font.name = $fontface
    self.contents.font.size = $fontsize
    self.contents.font.bold = true if $fontface == 'Papyrus'    
    @item = nil
    @max = 1
    @price = 0
    @number = 1
    @sell = false
    self.z = 5000
  end

  def set(item, max, price, sell = false)
    @item = item
    @max = max
    @price = price
    @number = 1
    @sell = sell
    refresh
  end

  def number
    return @number
  end

  def refresh
    self.contents.clear
    self.contents.font.color = system_color
    self.contents.draw_text(4, 0, 276, 32, 'How many?')
    draw_item_name(@item, 4, 96)
    self.contents.font.color = normal_color
    save_font = self.contents.font.name
    self.contents.font.name = 'Arial'
    self.contents.font.bold = false
    self.contents.draw_text(32, 128 + 2, 32, 32, '×')
    self.contents.font.name = save_font
    self.contents.font.bold = true if save_font == 'Papyrus'
    self.contents.draw_text(48, 128, 48, 32, @number.to_s, 2)
    self.contents.draw_text(116, 128, 32, 32, '=')
    self.cursor_rect.set(56, 128, 48, 32)
    domination = $data_system.words.gold
    width = self.contents.text_size(domination).width + 4
    total_price = @price * @number
    total_price = total_price * 2 / 3 if @sell && !$game_switches[196]
    self.contents.font.color = normal_color
    self.contents.draw_text(140 - width, 128, 128, 32, total_price.to_s, 2)
    self.contents.font.color = system_color
    self.contents.draw_text(140, 128, 128, 32, domination, 2)
  end

  def update
    super
    if self.active
      if Input.repeat?($controls.right) && @number < @max
        $game_system.se_play($data_system.cursor_se)
        @number += 1
        refresh
      elsif Input.repeat?($controls.left) && @number > 1
        $game_system.se_play($data_system.cursor_se)
        @number -= 1
        refresh
      elsif Input.repeat?($controls.up) && @number < @max
        $game_system.se_play($data_system.cursor_se)
        @number += 10
        @number = @max if @number > @max
        refresh
      elsif Input.repeat?($controls.down) && @number > 1
        $game_system.se_play($data_system.cursor_se)
        @number -= 10
        @number = 1 if @number < 1
        refresh
      end
    end
  end
  
end

#==============================================================================
# Window_ShopStatus
#==============================================================================

class Window_ShopStatus < Window_Base

  def initialize
    super(16, 64, 288, 352)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.contents.font.name = $fontface
    self.contents.font.size = $fontsize
    self.contents.font.bold = true if $fontface == 'Papyrus'    
    @item = nil
    self.z = 4000
    refresh
  end

  def refresh
    self.contents.clear
    return if @item == nil
    number = case @item
    when RPG::Item then $game_party.item_number(@item.id)
    when RPG::Weapon then $game_party.weapon_number(@item.id)
    when RPG::Armor then $game_party.armor_number(@item.id)
    end
    self.contents.font.color = system_color
    self.contents.draw_text(44, 0, 200, 32, 'possessed')
    self.contents.font.color = normal_color
    self.contents.draw_text(0, 0, 36, 32, number.to_s, 2)
    return if @item.is_a?(RPG::Item)
    y = -64
    type = -1
    $game_party.actors.each_index {|i|
        change1 = change2 = nil
        type = -1
        y += 64
        twohanded1 = twohanded2 = false
        actor = $game_party.actors[i]
        if actor.equippable?(@item)
          self.contents.font.color = normal_color
          if @item.is_a?(RPG::Weapon)
            type = (CP::Cache::Lucius.include?(actor.id) ? 1 : 0)
          else
            type = 2
          end
        else
          self.contents.font.color = disabled_color
          type = (@item.is_a?(RPG::Weapon) ? 0 : 2) if type == -1
        end
        self.contents.draw_text(4, 32 + y, 120, 32, actor.name)
        if @item.is_a?(RPG::Weapon)
          item1 = $data_weapons[actor.weapon_id]
          if CP::Cache::Lucius.include?(actor.id)
            itemX = $data_weapons[actor.armor1_id]
            twohanded1 = true if CP::Cache::TwoHanded.include?(actor.weapon_id)
            twohanded2 = true if CP::Cache::TwoHanded.include?(@item.id)
          end
        elsif @item.kind == 0
          item1 = $data_armors[actor.armor1_id]
        elsif @item.kind == 1
          item1 = $data_armors[actor.armor2_id]
        elsif @item.kind == 2
          item1 = $data_armors[actor.armor3_id]
        else
          item1 = nil
        end
        if actor.equippable?(@item)
          if @item.is_a?(RPG::Weapon) || @item.is_a?(RPG::Armor) && @item.atk > 0
            atk1 = item1 != nil ? item1.atk : 0
            atkX = itemX != nil ? itemX.atk : 0 if CP::Cache::Lucius.include?(actor.id)
            atk2 = @item != nil ? @item.atk : 0
            if twohanded1 && twohanded2
              change1 = atk2 - atk1
              change2 = 0 if CP::Cache::Lucius.include?(actor.id)
            elsif !twohanded1 && twohanded2
              change1 = atk2 - atk1
              change2 = -atkX if CP::Cache::Lucius.include?(actor.id)
            elsif twohanded1 && !twohanded2
              change1 = atk2 - atk1
              change2 = atk2 if CP::Cache::Lucius.include?(actor.id)
            else
              change1 = atk2 - atk1
              change2 = atk2 - atkX if CP::Cache::Lucius.include?(actor.id)
            end
          end
          if @item.is_a?(RPG::Armor) && @item.atk == 0
            pdef1 = item1 != nil ? item1.pdef : 0
            mdef1 = item1 != nil ? item1.mdef : 0
            pdef2 = @item != nil ? @item.pdef : 0
            mdef2 = @item != nil ? @item.mdef : 0
            change1 = pdef2 - pdef1
            change2 = mdef2 - mdef1
          end
          if change2 != nil
            if @item.is_a?(RPG::Weapon) || @item.kind < 3
              if change1 == 0
                text1 = sprintf('±%d', change1)
                color1 = normal_color
              else
                text1 = sprintf('%+d', change1)
                color1 = (change1 > 0 ? up_color : down_color)
              end
              if change2 == 0
                text2 = sprintf('±%d', change2)
                color2 = normal_color
              else
                text2 = sprintf('%+d', change2)
                color2 = (change2 > 0 ? up_color : down_color)
              end
            else
              text1 = '???' 
              text2 = '???'
              color1 = color2 = normal_color
            end
            if actor.equippable?(@item)
              self.contents.font.color = color1
              self.contents.draw_text(140, 32 + y, 56, 32, text1, 2)
              self.contents.font.color = color2
            else
              self.contents.font.color = disabled_color
              self.contents.draw_text(140, 32 + y, 56, 32, text1, 2)
            end
            self.contents.draw_text(196, 32 + y, 56, 32, text2, 2)
          elsif change1 != nil
            if change1 == 0
              text = sprintf('±%d', change1)
              color1 = normal_color
            else
              text = sprintf('%+d', change1)
              color1 = (change1 > 0 ? up_color : down_color)
            end
            if actor.equippable?(@item)
              self.contents.font.color = color1
            else
              self.contents.font.color = disabled_color
            end
            self.contents.draw_text(140, 32 + y, 112, 32, text, 2)
          end
        end
        if !CP::Cache::Lucius.include?(actor.id)
          if item1 != nil
            if actor.equippable?(@item)
              bitmap = RPG::Cache.icon(item1.icon_name)
              self.contents.font.color = normal_color
            else
              bitmap = RPG::Cache.desaturated(item1.icon_name)
              self.contents.font.color = disabled_color
            end
            self.contents.blt(4, 68 + y, bitmap, Rect.new(0, 0, 24, 24))
            self.contents.draw_text(32, 64 + y, 212, 32, item1.name)
          end
        elsif !@item.is_a?(RPG::Armor) || @item.kind != 0
          if actor.equippable?(@item)
            self.contents.font.color = normal_color
            disabled = false
          else
            self.contents.font.color = disabled_color
            disabled = true
          end
          if item1 != nil
            if !disabled
              bitmap = RPG::Cache.icon(item1.icon_name)
            else
              bitmap = RPG::Cache.desaturated(item1.icon_name)
            end
            self.contents.blt(4, 68 + y, bitmap, Rect.new(0, 0, 24, 24))
            self.contents.draw_text(32, 64 + y, 212, 32, item1.name)
          end
          y += 32
          if itemX != nil
            if !disabled
              bitmap = RPG::Cache.icon(itemX.icon_name)
            else
              bitmap = RPG::Cache.desaturated(itemX.icon_name)
            end
            self.contents.blt(4, 68 + y, bitmap, Rect.new(0, 0, 24, 24))
            self.contents.draw_text(32, 64 + y, 212, 32, itemX.name)
          end
        else
          y += 32
        end}
    self.contents.font.color = normal_color
    self.contents.font.size -= 4 if $fontface == 'Papyrus'
    case type
    when 0
      self.contents.draw_text(196, 0, 56, 32, 'Atk', 2)
    when 1
      self.contents.draw_text(140, 0, 56, 32, 'Atk 1', 2)
      self.contents.draw_text(196, 0, 56, 32, 'Atk 2', 2)
    when 2
      self.contents.draw_text(140, 0, 56, 32, 'PDef', 2)
      self.contents.draw_text(196, 0, 56, 32, 'MDef', 2)
    end
    self.contents.font.size += 4 if $fontface == 'Papyrus'
  end

  def item=(item)
    if @item != item
      @item = item
      refresh
    end
  end
  
end

#==============================================================================
# Scene_Shop
#==============================================================================

class Scene_Shop

  def main
    Graphics.transition
    Graphics.freeze
    @info = Shop_Sprite.new
    @help_window = Window_Help.new
    @command_window = Window_Command.new(160, ['Buy', 'Sell', 'Exit'])
    @command_window.x, @command_window.y = 16, 64
    @command_window.disable_item(0) if $game_switches[196]
    @gold_window = Window_Trade.new(true)
    @gold_window.x, @gold_window.y = 0, 416
    @buy_window = Window_ShopBuy.new($game_temp.shop_goods)
    @buy_window.help_window = @help_window
    @sell_window = Window_ShopSell.new
    @sell_window.help_window = @help_window
    @number_window = Window_ShopNumber.new
    @status_window = Window_ShopStatus.new
    @buy_window.active = @buy_window.visible = @sell_window.active =
        @sell_window.visible = @number_window.active = @number_window.visible =
        @status_window.visible = false
    @help_window.set_text('')
    [@help_window, @command_window, @buy_window, @sell_window, @number_window,
        @status_window].each {|win|
            win.windowskin = RPG::Cache.windowskin('Black Death')
            win.opacity = 160}
    [@gold_window, @help_window].each {|win| win.opacity = 0}
    @background = Plane.new
    @background.bitmap = RPG::Cache.picture('background')
    Graphics.transition
    loop do
      Graphics.update
      Input.update
      update
      break if $scene != self
    end
    Graphics.freeze
    @background.dispose
    [@help_window, @command_window, @gold_window, @buy_window, @sell_window,
        @number_window, @status_window, @info].each {|obj| obj.dispose}
    Graphics.transition
    Graphics.freeze
  end

  def update
    @background.ox += 1
    @background.oy -= 1
    [@help_window, @command_window, @gold_window, @buy_window, @sell_window,
        @number_window, @status_window, @info].each {|obj| obj.update}
    if @command_window.active
      update_command
    elsif @buy_window.active
      update_buy
    elsif @sell_window.active
      update_sell
    elsif @number_window.active
      update_number
    end
  end

  def update_command
    if Input.trigger?($controls.cancel)
      $game_system.se_play($data_system.cancel_se)
      $scene = Scene_Map.new
    elsif Input.trigger?($controls.confirm)
      case @command_window.index
      when 0
        if $game_switches[196]
          $game_system.se_play($data_system.buzzer_se)
        else
          $game_system.se_play($data_system.decision_se)
          @command_window.active = @command_window.visible = false
          @buy_window.refresh
          @buy_window.active = @buy_window.visible = @status_window.visible = true
          @status_window.item = @buy_window.item
          @info.set(@buy_window)
        end
      when 1
        $game_system.se_play($data_system.decision_se)
        @command_window.active = @command_window.visible = false
        @sell_window.active = @sell_window.visible = true
        @sell_window.refresh
        @info.set(@sell_window)
      when 2
        $game_system.se_play($data_system.decision_se)
        $scene = Scene_Map.new
      end
    end
  end

  def update_buy
    @status_window.item = @buy_window.item
    if Input.trigger?($controls.cancel)
      @info.unset
      $game_system.se_play($data_system.cancel_se)
      @command_window.active = @command_window.visible = true
      @buy_window.active = @buy_window.visible = @status_window.visible = false
      @status_window.item = nil
      @help_window.set_text('')
    elsif Input.trigger?($controls.confirm)
      @info.unset
      @item = @buy_window.item
      if @item == nil || @item.price > $game_party.gold
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      number = case @item
      when RPG::Item then $game_party.item_number(@item.id)
      when RPG::Weapon then $game_party.weapon_number(@item.id)
      when RPG::Armor then $game_party.armor_number(@item.id)
      end
      if number == 100
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      $game_system.se_play($data_system.decision_se)
      max = (@item.price == 0 ? 100 : $game_party.gold / @item.price)
      mx = 100 - number
      max = mx if max > mx
      @buy_window.active = @buy_window.visible = false
      @number_window.set(@item, max, @item.price)
      @number_window.active = @number_window.visible = true
    elsif Input.repeat?($controls.up) || Input.repeat?($controls.down) ||
        Input.repeat?($controls.left) || Input.repeat?($controls.right)
      @info.refresh
    end
  end

  def update_sell
    if Input.trigger?($controls.cancel)
      @info.unset
      $game_system.se_play($data_system.cancel_se)
      @command_window.active = @command_window.visible = true
      @sell_window.active = @sell_window.visible = false
      @status_window.item = nil
      @help_window.set_text('')
    elsif Input.trigger?($controls.confirm)
      @info.unset
      @item = @sell_window.item
      @status_window.item = @item
      if @item == nil || @item.price == 0
        $game_system.se_play($data_system.buzzer_se)
        return
      end
      $game_system.se_play($data_system.decision_se)
      number = case @item
      when RPG::Item then $game_party.item_number(@item.id)
      when RPG::Weapon then $game_party.weapon_number(@item.id)
      when RPG::Armor then $game_party.armor_number(@item.id)
      end
      max = number
      @sell_window.active = @sell_window.visible = false
      @number_window.set(@item, max, @item.price, true)
      @number_window.active = @number_window.visible = @status_window.visible = true
    elsif Input.repeat?($controls.up) || Input.repeat?($controls.down) ||
        Input.repeat?($controls.left) || Input.repeat?($controls.right)
      @info.refresh
    end
  end

  def update_number
    if Input.trigger?($controls.cancel)
      $game_system.se_play($data_system.cancel_se)
      @number_window.active = @number_window.visible = false
      case @command_window.index
      when 0
        @buy_window.active = @buy_window.visible = true
        @info.set(@buy_window)
      when 1
        @sell_window.active = @sell_window.visible = true
        @status_window.visible = false
        @info.set(@sell_window)
      end
    elsif Input.trigger?($controls.confirm)
      $game_system.se_play($data_system.shop_se)
      @number_window.active = @number_window.visible = false
      case @command_window.index
      when 0
        $game_party.lose_gold(@number_window.number * @item.price)
        case @item
        when RPG::Item then $game_party.gain_item(@item.id, @number_window.number)
        when RPG::Weapon then $game_party.gain_weapon(@item.id, @number_window.number)
        when RPG::Armor then $game_party.gain_armor(@item.id, @number_window.number)
        end
        @gold_window.refresh
        @buy_window.refresh
        @status_window.refresh
        @buy_window.active = @buy_window.visible = true
        @info.set(@buy_window)
      when 1
        price = @number_window.number*@item.price*2/($game_switches[196] ? 2 : 3)
        $game_party.gain_gold(price)
        case @item
        when RPG::Item then $game_party.lose_item(@item.id, @number_window.number)
        when RPG::Weapon then $game_party.lose_weapon(@item.id, @number_window.number)
        when RPG::Armor then $game_party.lose_armor(@item.id, @number_window.number)
        end
        @gold_window.refresh
        @sell_window.refresh
        @status_window.refresh
        @sell_window.active = @sell_window.visible = true
        @status_window.visible = false
        @info.set(@sell_window)
      end
    end
  end
  
end
