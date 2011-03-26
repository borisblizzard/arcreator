#==============================================================================
# WindowX
#==============================================================================

class WindowX
  
  BLANK_COLOR = Color.new(0, 0, 0, 0)
  ICON_RECT = Rect.new(0, 0, 24, 24)
  SCROLLBAR_AREA = Rect.new(0, 0, 8, 8)
  
  attr_accessor :active
  attr_accessor :width
  attr_accessor :height
  attr_reader   :x
  attr_reader   :y
  attr_reader   :ox
  attr_reader   :oy
  attr_reader   :opacity
  attr_reader   :back_opacity
  attr_reader   :contents_opacity
  attr_reader   :pad_right
  attr_reader   :pad_bottom
  attr_reader   :pad_left
  attr_reader   :pad_top
  attr_reader   :cursor_rect
  
  def initialize(x, y, width, height)
    super()
    @active = true
    @x = x
    @y = y
    @z = 100
    @ox = 0
    @oy = 0
    @width = width
    @height = height
    @opacity = 255
    @back_opacity = 255
    @contents_opacity = 255
    @pad_top = 0
    @pad_bottom = 0
    @pad_left = 0
    @pad_right = 0
    @background = nil
    @contents = Sprite.new
    @cursor_rect = CursorX.new(self)
    self.update_contents
    self.update_cursor
    @scrollbar_area = SCROLLBAR_AREA.clone
    @scrollbar = nil
  end
  
  def pad_left=(value)
    @pad_left = value
    self.update_window
  end
  
  def pad_top=(value)
    @pad_top = value
    self.update_window
  end
  
  def pad_right=(value)
    @pad_right = value
    self.update_window
  end
  
  def pad_bottom=(value)
    @pad_bottom = value
    self.update_window
  end
  
  def pad_horizontal
    return (@pad_left + @pad_right)
  end
  
  def pad_vertical
    return (@pad_top + @pad_bottom)
  end
  
  def background=(value)
    @background.dispose if @background != nil
    @background = Sprite.new
    @background.bitmap = value
    @background.src_rect.set(0, 0, @width, @height)
    self.update_window
  end
  
  def background
    return (@background != nil ? @background.bitmap : nil)
  end
  
  def update
    @cursor_rect.update if self.active
  end
  
  def update_window
    self.update_contents
    self.update_background
    self.update_cursor
    self.update_scrollbar
  end
  
  def update_contents
    @contents.x = @x
    @contents.y = @y
    @contents.ox = -@pad_left
    @contents.oy = -@pad_top
    @contents.z = @z + 5
    @contents.opacity = @contents_opacity
    @contents.src_rect.x = @ox
    @contents.src_rect.y = @oy
    @contents.src_rect.width = @width - self.pad_horizontal
    @contents.src_rect.height = @height - self.pad_vertical
  end
  
  def update_background
    if @background != nil
      @background.x = @x
      @background.y = @y
      @background.z = @z
      @background.visible = @contents.visible
      @background.opacity = @opacity * @back_opacity / 255
    end
  end
  
  def update_cursor
    @cursor_rect.ox = -@x - @pad_left
    @cursor_rect.oy = -@y - @pad_top
    @cursor_rect.z = @z + 10
  end
  
  def update_scrollbar
    if @scrollbar != nil
      @scrollbar.x = @x + @scrollbar_area.x
      @scrollbar.y = @y + @scrollbar_area.y +
        (@scrollbar_area.height - @scrollbar.bitmap.height) *
        @oy / (@contents.bitmap.height - @contents.src_rect.height)
      @scrollbar.z = @z + 6
      @scrollbar.visible = @contents.visible
    end
  end
  
  def windowskin=(value)
    @cursor_rect.windowskin = value
    self.update_window
  end
  
  def contents
    return @contents.bitmap
  end
  
  def contents=(value)
    @contents.bitmap = value
    self.update_window
  end
  
  def x=(value)
    @x = value
    self.update_window
  end
  
  def y=(value)
    @y = value
    self.update_window
  end
  
  def z=(value)
    @z = value
    self.update_window
  end
  
  def ox=(value)
    @ox = value
    self.update_window
  end
  
  def oy=(value)
    @oy = value
    self.update_window
  end
  
  def width=(value)
    @width = value
    self.update_window
  end
  
  def height=(value)
    @height = value
    self.update_window
  end
  
  def visible
    return @contents.visible
  end
  
  def visible=(value)
    @background.visible = value if @background != nil
    @contents.visible = value
    @cursor_rect.visible = value
    @scrollbar.visible = value if @scrollbar != nil
  end
  
  def opacity=(value)
    @opacity = value
    self.update_window
  end
  
  def contents_opacity=(value)
    @contents_opacity = value
    self.update_window
  end
  
  def back_opacity=(value)
    @back_opacity = value
    self.update_window
  end
  
  def scrollbar
    return (@scrollbar != nil ? @scrollbar.bitmap : nil)
  end
  
  def scrollbar=(value)
    if value != nil
      if @scrollbar == nil
        @scrollbar = Sprite.new
        @scrollbar.bitmap = value
      end
    elsif @scrollbar != nil
      @scrollbar.dispose
      @scrollbar = nil
    end
    self.update_window
  end
  
  def dispose
    @contents.dispose
    @background.dispose if @background != nil
    @cursor_rect.dispose
    @scrollbar.dispose if @scrollbar != nil
  end
  
end
