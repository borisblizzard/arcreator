#==============================================================================
# Game_Actors
#==============================================================================

class Game_Actors
  
  def initialize
    @data = []
  end
  
  def [](actor_id)
    return nil if actor_id > 999 || $data_actors[actor_id] == nil
    @data[actor_id] = Game_Actor.new(actor_id) if @data[actor_id] == nil
    return @data[actor_id]
  end
  
  def []=(actor_id, actor)
    @data[actor_id] = actor
  end
  
end
