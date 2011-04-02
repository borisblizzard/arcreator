#==============================================================================
# WindowX_Base
#==============================================================================

class WindowX_Base < WindowX
  
  NORMAL_COLOR = Color.new(0, 0, 0, 255)
  DISABLED_COLOR = Color.new(0, 0, 0, 128)
  
  def initialize(x, y, width, height)
    super
    @windowskin_name = $game_system.windowskin_name
    self.windowskin = RPG::Cache.windowskin(@windowskin_name)
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.z = 100
  end
  
  def update
    if $game_system.windowskin_name != @windowskin_name
      @windowskin_name = $game_system.windowskin_name
      self.windowskin = RPG::Cache.windowskin(@windowskin_name)
    end
    super
  end
  
  def refresh
  end
  
  def normal_color
    return NORMAL_COLOR
  end
  
  def disabled_color
    return DISABLED_COLOR
  end
  
  def dispose
    self.contents.dispose if self.contents != nil && !self.contents.disposed?
    super
  end
  
end
