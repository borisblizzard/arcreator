#==============================================================================
# Game_CommonEvent
#==============================================================================

class Game_CommonEvent
  
  def initialize(common_event_id)
    @common_event_id, @interpreter = common_event_id, nil
    refresh
  end
  
  def name
    return $data_common_events[@common_event_id].name
  end
  
  def trigger
    return $data_common_events[@common_event_id].trigger
  end
  
  def switch_id
    return $data_common_events[@common_event_id].switch_id
  end
  
  def list
    return $data_common_events[@common_event_id].list
  end
  
  def refresh
    if self.trigger == 2 && $game_switches[self.switch_id]
      @interpreter = Interpreter.new if @interpreter == nil
    else
      @interpreter = nil
    end
  end
  
  def update
    if @interpreter != nil
      @interpreter.setup(self.list, 0) unless @interpreter.running?
      @interpreter.update
    end
  end
  
end
