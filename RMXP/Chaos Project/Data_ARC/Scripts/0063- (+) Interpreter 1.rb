#==============================================================================
# Interpreter (1)
#==============================================================================

class Interpreter
  
  attr_reader :event_id
  
  def initialize(depth = 0, main = false)
    @depth, @main = depth, main
    if depth > 500
      p 'The common event call exceeded the upper boundary.'
      p 'It is recommended that you save your game state and restart the game.'
    end
    clear
  end
  
  def clear
    @map_id = @event_id = @button_input_variable_id = @wait_count = 0
    @message_waiting = @move_route_waiting = false
    @child_interpreter, @branch = nil, {}
  end
  
  def setup(list, event_id)
    clear
    @map_id, @event_id, @list, @index = $game_map.map_id, event_id, list, 0
    @branch.clear
  end
  
  def setup_trace
    command = RPG::EventCommand.new
    command.code, command.parameters = 209, [0, RPG::MoveRoute.new]
    command.parameters[1].list, command.parameters[1].repeat = CP.trace, false
    @list[@index + 1] = command
  end
  
  def set_name(id, name)
    $game_temp.event_id, $game_map.events[id].name = id, name
  end
  
  def reset_name
    $game_map.events[$game_temp.event_id].name = nil
    $game_temp.event_id = nil
  end
  
  def running?
    return (@list != nil)
  end
  
  def setup_starting_event
    $game_map.refresh if $game_map.need_refresh
    if $game_temp.common_event_id > 0
      setup($data_common_events[$game_temp.common_event_id].list, 0)
      $game_temp.common_event_id = 0
      return
    end
    $game_map.events.each_value {|event|
        if event.starting
          if event.trigger < 3
            event.clear_starting
            event.lock
          end
          setup(event.list, event.id)
          return
        end}
    $data_common_events.compact.each {|common_event|
        if common_event.trigger == 1 &&
            $game_switches[common_event.switch_id] == true
          setup(common_event.list, 0)
          return
        end}
  end
  
  def update
    @loop_count = 0
    loop do
      @loop_count += 1
      if @loop_count > 100
        Graphics.update
        @loop_count = 0
      end
      @event_id = 0 if $game_map.map_id != @map_id
      if @child_interpreter != nil
        @child_interpreter.update
        @child_interpreter = nil unless @child_interpreter.running?
        return if @child_interpreter != nil
      end
      return if @message_waiting
      if @move_route_waiting
        return if $game_player.move_route_forcing
        $game_map.events.each_value {|event| return if event.move_route_forcing}
        @move_route_waiting = false
      end
      if @button_input_variable_id > 0
        input_button
        return
      end
      if @wait_count > 0
        @wait_count -= 1
        return
      end
      return if $game_temp.forcing_battler != nil
      if $game_temp.battle_calling[0] || $game_temp.shop_calling ||
          $game_temp.name_calling || $game_temp.menu_calling ||
          $game_temp.save_calling || $game_temp.gameover
        return
      end
      if @list == nil
        setup_starting_event if @main
        return if @list == nil
      end
      return unless execute_command
      @index += 1
    end
  end
  
  def input_button
    n = 0
    (1...18).each {|i| n = i if Input.trigger?(i)}
    if n > 0
      $game_variables[@button_input_variable_id] = n
      $game_map.need_refresh = true
      @button_input_variable_id = 0
    end
  end
  
  def setup_choices(parameters)
    $game_temp.choice_max = parameters[0].size
    parameters[0].each {|text| $game_temp.message_text += text + "\n"}
    $game_temp.choice_cancel_type = parameters[1]
    current_indent = @list[@index].indent
    $game_temp.choice_proc = Proc.new {|n| @branch[current_indent] = n}
  end
  
  def iterate_actor(parameter)
    if parameter == 0
      $game_party.actors.each {|actor| yield actor}
    else
      actor = $game_actors[parameter]
      yield actor if actor != nil
    end
  end
  
  def iterate_enemy(parameter)
    if parameter == -1
      $game_troop.enemies.each {|enemy| yield enemy}
    else
      enemy = $game_troop.enemies[parameter]
      yield enemy if enemy != nil
    end
  end
  
  def iterate_battler(parameter1, parameter2)
    if parameter1 == 0
      iterate_enemy(parameter2) do |enemy|
        yield enemy
      end
    elsif parameter2 == -1
      $game_party.actors.each {|actor| yield actor}
    else
      actor = $game_party.actors[parameter2]
      yield actor if actor != nil
    end
  end
  
end
