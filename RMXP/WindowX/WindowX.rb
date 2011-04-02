#==============================================================================
# WindowX
#==============================================================================

class WindowX 
  
  BLANK_COLOR = Color.new(0, 0, 0, 0)
  ICON_RECT = Rect.new(0, 0, 24, 24)
  SCROLLBAR_AREA = Rect.new(0, 0, 8, 8)
  WIDTH = 192  # Template Width
  HEIGHT = 128 # Template Height
  BW = 128     # Background Width
  BH = 128     # Background Height
  PW = 16      # Pause Width
  PH = 16      # Pause Height
  CW = 16      # Corner Width
  CH = 16      # Corner Height
  BHW = 32     # Border Horizontal Width
  BHH = 16     # Border Horizontal Height
  BVW = 16     # Border Vertical Width
  BVH = 32     # Border Vertical Height
  AHW = 8      # Arrow Horizontal Width
  AHH = 16     # Arrow Horizontal Height
  AVW = 16     # Arrow Vertical Width
  AVH = 8      # Arrow Vertical Height
  RECTS = [
    Rect.new(0,                    0,                 BW,  BH),    # Background
    Rect.new(WIDTH - PW * 2,       BVH + CH * 2,      PW,  PH),    # Pause 1
    Rect.new(WIDTH - PW,           BVH + CH * 2,      PW,  PH),    # Pause 2
    Rect.new(WIDTH - PW * 2,       PH + BVH + CH * 2, PW,  PH),    # Pause 3
    Rect.new(WIDTH - PW,           PH + BVH + CH * 2, PW,  PH),    # Pause 4
    Rect.new(BW + BVW + AHW,       CH,                AVW, AVH),   # Arrow Up
    Rect.new(BW + BVW + AHW,       CH + AVH + AHH,    AVW, AVH),   # Arrow Down
    Rect.new(BW + BVW,             BHH + AVH,         AHW, AHH),   # Arrow Left
    Rect.new(BW + BVW + AHW + AVW, BHH + AVH,         AHW, AHH),   # Arrow Right
    Rect.new(BW,                   0,                 CW,  CH),    # Upper-Left Corner
    Rect.new(WIDTH - CW,           0,                 CW,  CH),    # Upper-Right Corner
    Rect.new(BW,                   CH + BVH,          CW,  CH),    # Bottom-Left Corner
    Rect.new(WIDTH - CW,           CH + BVH,          CW,  CH),    # Bottom-Right Corner
    Rect.new(BW + CW,              0,                 BHW, BHH),   # Border Top
    Rect.new(BW + CW,              CH + BVH,          BHW, BHH),   # Border Bottom 
    Rect.new(BW,                   CH,                BVW, BVH),   # Border Left
    Rect.new(WIDTH - BVW,          CH,                BVW, BVH)    # Border Right
  ]
  CORNER_RECTS = [RECTS[9], RECTS[10], RECTS[11], RECTS[12]]
  BORDER_RECTS = [RECTS[13], RECTS[14], RECTS[15], RECTS[16]]
  PAUSE_RECTS = [RECTS[1], RECTS[2], RECTS[3], RECTS[4]]
  ARROW_RECTS = [RECTS[5], RECTS[6], RECTS[7], RECTS[8]]
  BACKGROUND_RECT = RECTS[0]
  
  def create_bitmap
    self.contents.dispose if self.contents != nil && !self.contents.disposed?
    return if @width <= 0 || @height <= 0 || @windowskin == nil
    
    self.contents = Bitmap.new(@width, @height)
    # corners
    self.contents.blt(0, 0, @windowskin, CORNER_RECTS[0])
    self.contents.blt(@width - CW, 0, @windowskin, CORNER_RECTS[1])
    self.contents.blt(0, @height - CH, @windowskin, CORNER_RECTS[2])
    self.contents.blt(@width - CW, @height - CH, @windowskin, CORNER_RECTS[3])
    # borders
    self.contents.stretch_blt(Rect.new(CW, 0, @width - CW * 2, BHH),
      @windowskin, BORDER_RECTS[0])
    self.contents.stretch_blt(Rect.new(CW, @height - BHH, @width - CW * 2, BHH),
      @windowskin, BORDER_RECTS[1])
    self.contents.stretch_blt(Rect.new(0, CH, BVW, @height - CH * 2),
      @windowskin, BORDER_RECTS[2])
    self.contents.stretch_blt(Rect.new(@width - BVW, CH, BVW, @height - CH * 2),
      @windowskin, BORDER_RECTS[3])
    # center
    self.background = Bitmap.new(@width, @height)
    rect = Rect.new(@pad_left, @pad_top, @width - @pad_left - @pad_right,
      @height - @pad_top - @pad_bottom)
    self.background.stretch_blt(rect, @windowskin, BACKGROUND_RECT)
  end
  
  
  
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
    @windowskin = nil
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
    @windowskin = value
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
