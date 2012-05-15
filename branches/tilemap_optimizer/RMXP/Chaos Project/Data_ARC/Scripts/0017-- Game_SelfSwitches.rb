#==============================================================================
# Game_SelfSwitches
#==============================================================================

class Game_SelfSwitches
  
  def initialize
    @data = {}
  end
  
  def [](key)
    return (@data[key] == true)
  end
  
  def []=(key, value)
    @data[key] = value
  end
  
end
