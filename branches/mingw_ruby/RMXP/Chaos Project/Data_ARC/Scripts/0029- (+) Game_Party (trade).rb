#==============================================================================
# Game_Party
#==============================================================================

class Game_Party
  
  def test_trade
    return 2 if self.item_number($game_variables[105]) == 100
    if $game_variables[106].is_a?(Array)
      $game_variables[106].each_index {|i|
          all = $game_variables[5] * $game_variables[106][i]
          return 1 if all > self.item_number($game_variables[107][i])}
      tmp = $game_variables[5]
    else
      if $game_variables[106] < 0
        all = $game_variables[5] / (-$game_variables[106])
        tmp = $game_variables[5] / (-$game_variables[106]) * (-$game_variables[106])
      else
        all = $game_variables[5] * $game_variables[106]
        tmp = $game_variables[5]
      end
      return 1 if all > ($game_variables[107] == 0 ? $game_party.gold : self.item_number($game_variables[107]))
    end
    return 3 if $game_variables[5] != 0 && tmp == 0
    return 0
  end
  
  def do_trade
    id = $game_variables[105]
    price = $game_variables[106]
    c_id = $game_variables[107]
    if price.is_a?(Array)
      price.each_index {|i|
          $game_party.lose_item(c_id[i], $game_variables[5] * price[i])}
      $game_party.gain_item(id, $game_variables[5])
    else
      all = (price < 0 ? $game_variables[5] / (-price) : $game_variables[5] * price)
      c_id == 0 ? $game_party.lose_gold(all) : $game_party.lose_item(c_id, all)
      if price < 0
        $game_party.gain_item(id, $game_variables[5] / (-price) * (-price))
      else
        $game_party.gain_item(id, $game_variables[5])
      end
    end
  end
  
  def make_text1
    name = $data_items[$game_variables[105]].name
    name = CP.fixname(name)
    return "I am trading with \\c[1]#{name}\\c[0].\n"
  end
  
  def make_text2
    if $game_variables[106].is_a?(Array)
      text = "I give you 1 \\c[1]#{$data_items[$game_variables[105]].name}\\c[0] for"
      name = $data_items[$game_variables[107][0]].name
      name = CP.fixname(name) if $game_variables[106][0] > 1
      text += " #{$game_variables[106][0]} \\c[1]#{name}\\c[0]"
      text += ($game_variables[106].size > 2 ? ",\n" : "\n")
      (1...$game_variables[106].size).each {|i|
          name = $data_items[$game_variables[107][i]].name
          name = CP.fixname(name) if $game_variables[106][i] > 1
          if i == $game_variables[106].size-1
            text += "and #{$game_variables[106][i]} \\c[1]#{name}\\c[0]."
          else
            text += "#{$game_variables[106][i]} \\c[1]#{name}\\c[0]"
            text += (i == $game_variables[106].size-2 ? ' ' : ', ')
          end}
      return text
    else
      name = $data_items[$game_variables[105]].name
      name = CP.fixname(name) if $game_variables[106] < 0
      if $game_variables[107] > 0
        name2 = $data_items[$game_variables[107]].name
        name2 = CP.fixname(name2) if $game_variables[106] > 1
      else
        name2 = $data_system.words.gold
      end
      if $game_variables[106] < 0
        return "I give you #{-$game_variables[106]} \\c[1]#{name}\\c[0] for 1 \\c[1]#{name2}\\c[0]."
      else
        return "I give you 1 \\c[1]#{name}\\c[0] for #{$game_variables[106]} \\c[1]#{name2}\\c[0]."
      end
    end
  end
  
  def make_text3
    if $game_variables[107].is_a?(Array) || $game_variables[107] > 0
      return "You don't have enough items."
    else
      return "You don't have enough #{$data_system.words.gold}."
    end
  end
  
  def make_text4(flag = true)
    if !$game_variables[106].is_a?(Array) && $game_variables[106] < 0 &&
        $game_variables[5] != $game_variables[5] / $game_variables[106] * $game_variables[106]
      calc = $game_variables[5]/(-$game_variables[106])*(-$game_variables[106])
      if flag
        return "You can't buy #{$game_variables[5]}.", "Do you want #{calc} instead?"
      else
        $game_temp.choice_start = 99
        return "You can't buy #{$game_variables[5]}."
      end
    else
      return "You want #{$game_variables[5]}?", 0
    end
  end
  
end
