#==============================================================================
# Game_Variables
#==============================================================================

class Game_Variables
  
  def initialize
    @data = []
  end
  
  def [](variable_id)
    return @data[variable_id] if variable_id <= 5000 && @data[variable_id] != nil
    return 0
  end
  
  def []=(variable_id, value)
    @data[variable_id] = value if variable_id <= 5000
  end
  
end
