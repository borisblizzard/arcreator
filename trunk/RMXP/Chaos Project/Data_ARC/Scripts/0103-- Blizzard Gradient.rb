#==============================================================================
# Blizz-Art Gradient styler by Blizzard
# Version: 4.5b
# Date: 13.11.2006
#==============================================================================

class Bitmap

  def gradient_bar(x, y, w, color1, color2, color3, rate)
    styles = [1, 3, 4, 5, 6]
    ex_styles = [5, 6]
    offs = 5
    x += offs
    y += 26
    if styles.include?($game_system.bar_style)
      offs += 2
      w = w / 8 * 8
      y -= 1
      ex_styles.include?($game_system.bar_style) ? y -= 2 :  x += 1
    end
    a = $game_system.bar_opacity
    return if a == 0
    if $game_system.bar_style < 5
      (0...(offs+3)).each {|i| fill_rect(x-i, y+i-2, w+3, 1, Color.new(0, 0, 0, a))}
      (0...(offs+1)).each {|i| fill_rect(x-i, y+i-1, w+1, 1, Color.new(255, 255, 255, a))}
      if $game_system.bar_style < 2
        (0...w+offs).each {|i|
            r = color3.red * i / (w+offs)
            g = color3.green * i / (w+offs)
            b = color3.blue * i / (w+offs)
            oy = i < offs ? offs-i : 0
            off = i < offs ? i : i > w ? w+offs-i : offs
            fill_rect(x+i-offs+1, y+oy-1, 1, off, Color.new(r, g, b, a))}
        if (w*rate).to_i >= offs
          (0...((w*rate).to_i+offs)).each {|i|
              r = color1.red + (color2.red-color1.red)*i / ((w+offs)*rate)
              g = color1.green + (color2.green-color1.green)*i / ((w+offs)*rate)
              b = color1.blue + (color2.blue-color1.blue)*i / ((w+offs)*rate)
              oy = i < offs ? offs-i : 0
              off = i < offs ? i : i > w*rate ? (w*rate).to_i+offs-i : offs
              fill_rect(x+i-offs+1, y+oy-1, 1, off, Color.new(r, g, b, a))}
        else
          (0...(w * rate).to_i).each {|i| (0...offs).each {|j|
              r = color1.red + (color2.red-color1.red)*i / (w*rate)
              g = color1.green + (color2.green-color1.green)*i / (w*rate)
              b = color1.blue + (color2.blue-color1.blue)*i / (w*rate)
              set_pixel(x+i-j+1, y+j-1, Color.new(r, g, b, a))}}
        end
      else
        (0...offs).each {|i|
            r = color3.red * i / offs
            g = color3.green * i / offs
            b = color3.blue * i / offs
            fill_rect(x-i+1, y+i-1, w, 1, Color.new(r, g, b, a))}
        if $game_system.bar_style == 4
          (0...offs/2+1).each {|i|
              r = color2.red * (i+1) / (offs/2)
              g = color2.green * (i+1) / (offs/2)
              b = color2.blue * (i+1) / (offs/2)
              fill_rect(x-i+1, y+i-1, w*rate, 1, Color.new(r, g, b, a))
              fill_rect(x-offs+i+2, y+offs-i-2, w*rate, 1, Color.new(r, g, b, a))}
        else
          (0...offs).each {|i|
              r = color1.red + (color2.red-color1.red)*i / offs
              g = color1.green + (color2.green-color1.green)*i / offs
              b = color1.blue + (color2.blue-color1.blue)*i / offs
              fill_rect(x-i+1, y+i-1, w*rate, 1, Color.new(r, g, b, a))}
        end
      end
      if styles.include?($game_system.bar_style)
        (0...w).each {|i| (0...offs).each {|j|
            if styles.include?($game_system.bar_style) && i % 8 < 2
              set_pixel(x+i-j+1, y+j-1, Color.new(0, 0, 0, a))
            end}}
      end
    else
      fill_rect(x+1, y-3, w+2, 12, Color.new(255, 255, 255, a))
      (0..4).each {|i|
          r1, r2 = color3.red * (i+1) / 5, color2.red * (i+1) / 5
          g1, g2 = color3.green * (i+1) / 5, color2.green * (i+1) / 5
          b1, b2 = color3.blue * (i+1) / 5, color2.blue * (i+1) / 5
          if i == 4
            fill_rect(x+2, y+2, w, 2, Color.new(r1, g1, b1, a))
            fill_rect(x+2, y+2, w*rate, 2, Color.new(r2, g2, b2, a))
          else
            fill_rect(x+2, y+i-2, w, 1, Color.new(r1, g1, b1, a))
            fill_rect(x+2, y-i+7, w, 1, Color.new(r1, g1, b1, a))
            fill_rect(x+2, y+i-2, w*rate, 1, Color.new(r2, g2, b2, a))
            fill_rect(x+2, y-i+7, w*rate, 1, Color.new(r2, g2, b2, a))
          end}
      if $game_system.bar_style == 5
        (0...w/8).each {|i|
            fill_rect(x+2+i*8, y-2, 1, 10, Color.new(0, 0, 0, a))
            fill_rect(x+2+(i+1)*8-1, y-2, 1, 10, Color.new(0, 0, 0, a))}
      end
    end
  end
  
end

#==============================================================================
# Window_Base
#==============================================================================

class Window_Base < Window

  alias draw_actor_hp_new draw_actor_hp
  def draw_actor_hp(actor, x, y, w = 148)
    w -= 12
    rate = actor.hp.to_f / actor.maxhp
    if rate < 0
      rate = 0
    elsif rate > 1
      rate = 1
    end
    if rate > 0.6
      color1 = Color.new(80 - 150 * (rate-0.6), 80, 50 * (rate-0.6), 192) 
      color2 = Color.new(240 - 450 * (rate-0.6), 240, 150 * (rate-0.6), 192) 
    elsif rate > 0.2 && rate <= 0.6
      color1 = Color.new(80, 200 * (rate-0.2), 0, 192) 
      color2 = Color.new(240, 600 * (rate-0.2), 0, 192) 
    elsif rate <= 0.2
      color1 = Color.new(400 * rate, 0, 0, 192) 
      color2 = Color.new(240, 0, 0, 192) 
    end
    color3 = Color.new(0, 80, 0, 192)
    self.contents.gradient_bar(x, y, w, color1, color2, color3, rate)
    if $scene.is_a?(Scene_Battle)
      draw_actor_hp_new(actor, x, y, w)
    else
      draw_actor_hp_new(actor, x, y)
    end
  end

  alias draw_actor_sp_new draw_actor_sp
  def draw_actor_sp(actor, x, y, w = 148)
    w -= 12
    rate = actor.sp.to_f / actor.maxsp
    if rate < 0
      rate = 0
    elsif rate > 1
      rate = 1
    end
    if rate > 0.4
      color1 = Color.new(60 - 66 * (rate-0.4), 20, 80, 192) 
      color2 = Color.new(180 - 200 * (rate-0.4), 60, 240, 192) 
    elsif rate <= 0.4
      color1 = Color.new(20 + 100 * rate, 50 * rate, 26 + 166 * rate, 192) 
      color2 = Color.new(60 + 300 * rate, 150 * rate, 80 + 400 * rate, 192) 
    end
    color3 = Color.new(0, 0, 80, 192) 
    self.contents.gradient_bar(x, y, w, color1, color2, color3, rate)
    if $scene.is_a?(Scene_Battle)
      draw_actor_sp_new(actor, x, y, w)
    else
      draw_actor_sp_new(actor, x, y)
    end
  end

  alias draw_actor_exp_new draw_actor_exp
  def draw_actor_exp(actor, x, y, w = 148)
    w -= 12
    if actor.next_exp == 0
      rate = 1
    else
      rate = actor.now_exp.to_f / actor.next_exp
      if rate < 0
        rate = 0
      elsif rate > 1
        rate = 1
      end
    end
    if rate < 0.5
      color1 = Color.new(20 * rate, 60, 80, 192) 
      color2 = Color.new(60 * rate, 180, 240, 192) 
    elsif rate >= 0.5
      color1 = Color.new(20 + 120 * (rate-0.5), 60 + 40 * (rate-0.5), 80, 192) 
      color2 = Color.new(60 + 360 * (rate-0.5), 180 + 120 * (rate-0.5), 240, 192) 
    end
    color3 = Color.new(80, 80, 80, 192) 
    self.contents.gradient_bar(x, y, w, color1, color2, color3, rate)
    draw_actor_exp_new(actor, x, y)
  end

  alias draw_actor_sr_new draw_actor_sr
  def draw_actor_sr(actor, x, y, w = 148)
    w -= 12
    rate = actor.sr.to_f / actor.maxsr
    if rate < 0
      rate = 0
    elsif rate > 1
      rate = 1
    end
    if $game_party.can_use_any_uf?
      color1, color2 = Color.new(80, 0, 0), Color.new(240, 0, 0)
    else
      color1, color2 = Color.new(80, 80, 0), Color.new(240, 240, 0)
    end
    color3 = Color.new(80, 0, 0, 192)
    self.contents.gradient_bar(x, y, w, color1, color2, color3, rate)
    if $scene.is_a?(Scene_Battle)
      draw_actor_sr_new(actor, x, y, w)
    else
      draw_actor_sr_new(actor, x, y)
    end
  end

end
