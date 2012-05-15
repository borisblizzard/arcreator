#==============================================================================
# Interpreter (6)
#==============================================================================

class Interpreter
  
  def command_301
    if $data_troops[@parameters[0]] != nil
      $game_temp.battle_abort = true
      $game_temp.battle_calling = [true, true]
      $game_temp.battle_troop_id = @parameters[0]
      $game_temp.battle_can_escape = @parameters[1]
      $game_temp.battle_can_lose = @parameters[2]
      current_indent = @list[@index].indent
      $game_temp.battle_proc = Proc.new { |n| @branch[current_indent] = n }
    end
    @index += 1
    return false
  end
  
  def command_601
    if @branch[@list[@index].indent] == 0
      @branch.delete(@list[@index].indent)
      return true
    end
    return command_skip
  end
  
  def command_602
    if @branch[@list[@index].indent] == 1
      @branch.delete(@list[@index].indent)
      return true
    end
    return command_skip
  end
  
  def command_603
    if @branch[@list[@index].indent] == 2
      @branch.delete(@list[@index].indent)
      return true
    end
    return command_skip
  end
  
  def command_302
    $game_temp.battle_abort = $game_temp.shop_calling = true
    $game_temp.shop_goods = [@parameters]
    loop do
      @index += 1
      if @list[@index].code == 605
        $game_temp.shop_goods.push(@list[@index].parameters)
      else
        return false
      end
    end
  end
  
  def command_303
    if $data_actors[@parameters[0]] != nil
      $game_temp.battle_abort = true
      $game_temp.name_calling = true
      $game_temp.name_actor_id = @parameters[0]
      $game_temp.name_max_char = @parameters[1]
    end
    @index += 1
    return false
  end
  
  def command_311
    value = operate_value(@parameters[1], @parameters[2], @parameters[3])
    iterate_actor(@parameters[0])  {|actor|
        if actor.hp > 0
          if @parameters[4] == false && actor.hp + value <= 0
            actor.hp = 1
          else
            actor.hp += value
          end
        end}
    $game_temp.gameover = $game_party.all_dead?
    return true
  end
  
  def command_312
    value = operate_value(@parameters[1], @parameters[2], @parameters[3])
    iterate_actor(@parameters[0]) {|actor| actor.sp += value}
    return true
  end
  
  def command_313
    iterate_actor(@parameters[0]) {|actor|
        if @parameters[1] == 0
          actor.add_state(@parameters[2])
        else
          actor.remove_state(@parameters[2])
        end}
    return true
  end
  
  def command_314
    iterate_actor(@parameters[0]) {|actor| actor.recover_all}
    return true
  end
  
  def command_315
    value = operate_value(@parameters[1], @parameters[2], @parameters[3])
    iterate_actor(@parameters[0]) {|actor| actor.exp += value}
    return true
  end
  
  def command_316
    value = operate_value(@parameters[1], @parameters[2], @parameters[3])
    iterate_actor(@parameters[0]) {|actor| actor.level += value}
    return true
  end
  
  def command_317
    value = operate_value(@parameters[2], @parameters[3], @parameters[4])
    actor = $game_actors[@parameters[0]]
    if actor != nil
      case @parameters[1]
      when 0 then actor.maxhp += value
      when 1 then actor.maxsp += value
      when 2 then actor.str += value
      when 3 then actor.dex += value
      when 4 then actor.agi += value
      when 5 then actor.int += value
      end
    end
    return true
  end
  
  def command_318
    actor = $game_actors[@parameters[0]]
    if actor != nil
      if @parameters[1] == 0
        actor.learn_skill(@parameters[2])
      else
        actor.forget_skill(@parameters[2])
      end
    end
    return true
  end
  
  def command_319
    actor = $game_actors[@parameters[0]]
    actor.equip(@parameters[1], @parameters[2]) if actor != nil
    return true
  end
  
  def command_320
    actor = $game_actors[@parameters[0]]
    actor.name = @parameters[1] if actor != nil
    return true
  end
  
  def command_321
    actor = $game_actors[@parameters[0]]
    actor.class_id = @parameters[1] if actor != nil
    return true
  end
  
  def command_322
    actor = $game_actors[@parameters[0]]
    if actor != nil
      actor.set_graphic(@parameters[1], @parameters[2],
          @parameters[3], @parameters[4])
    end
    $game_player.refresh
    return true
  end
  
end
