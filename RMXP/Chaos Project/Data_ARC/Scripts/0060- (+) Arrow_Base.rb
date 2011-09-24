#==============================================================================
# Arrow_Base
#==============================================================================

class Arrow_Base < Sprite
  
  attr_reader :index
  attr_reader :help_window
  
  def initialize(viewport)
    super(viewport)
    @arrow = Sprite.new(viewport)
    @arrow.bitmap = self.bitmap = RPG::Cache.windowskin($game_system.windowskin_name)
    self.ox = @arrow.ox = 16
    self.z = @arrow.z = 50000
    @arrow.src_rect.set(160, 96, 32, 32)
    self.src_rect.set(128, 96, 32, 32)
    @blink_change = false
    @index = 0
    @help_window = nil
  end
  
  def index=(index)
    @index = index
    update
  end
  
  def help_window=(help_window)
    @help_window = help_window
    update_help if @help_window != nil
  end
  
  def update
    if @blink_change
      @arrow.oy += 2
      self.oy += 2
      @arrow.opacity -= 17
      @blink_change = (@arrow.opacity > 0)
    else
      @arrow.oy -= 2
      self.oy -= 2
      @arrow.opacity += 17
      @blink_change = (@arrow.opacity == 255)
    end
    update_help if @help_window != nil
  end
  
  def dispose
    @arrow.dispose unless @arrow == nil || @arrow.disposed?
    super
  end
  
end
