#==============================================================================
# Game_Switches
#==============================================================================

class Game_Switches
  
  def initialize
    @data = []
  end
  
  def [](switch_id)
    return @data[switch_id] if switch_id <= 5000 && @data[switch_id] != nil
    return false
  end
  
  def []=(switch_id, value)
    @data[switch_id] = value if switch_id <= 5000
  end
  
end
