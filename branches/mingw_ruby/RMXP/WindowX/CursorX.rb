#==============================================================================
# CursorX
#==============================================================================

class CursorX < Sprite
  
  OX = 128
  OY = 64
  CW = 32
  CH = 32
  BW = 2
  BH = 2
  RECTS = [
      Rect.new(OX +       0, OY +       0,          BW,          BH),
      Rect.new(OX +      BW, OY +       0, CW - BW * 2,          BH),
      Rect.new(OX + CW - BW, OY +       0,          BW,          BH),
      Rect.new(OX +       0, OY +      BH,          BW, CH - BH * 2),
      Rect.new(OX +      BW, OY +      BH, CW - BW * 2, CH - BH * 2),
      Rect.new(OX + CW - BW, OY +      BH,          BW, CH - BH * 2),
      Rect.new(OX +       0, OY + CH - BH,          BW,          BH),
      Rect.new(OX +      BW, OY + CH - BH, CW - BW * 2,          BH),
      Rect.new(OX + CW - BW, OY + CH - BH,          BW,          BH)
  ]
  CORNER_RECTS = [RECTS[0], RECTS[2], RECTS[6], RECTS[8]]
  BORDER_RECTS = [RECTS[1], RECTS[3], RECTS[5], RECTS[7]]
  
  attr_reader :width
  attr_reader :height
  
  def initialize(parent)
    super()
    @parent = parent
    @windowskin = nil
    @frames = Graphics.frame_count
    @width = 32
    @height = 32
    self.visible = false
    @visible = true
  end
  
  def create_bitmap(w, h)
    @width = w
    @height = h
    self.bitmap.dispose if self.bitmap != nil && !self.bitmap.disposed?
    return if @width <= 0 || @height <= 0 || @windowskin == nil
    self.bitmap = Bitmap.new(w, h)
    xs = [0, BW, w - BW]
    ys = [0, BW, h - BW]
    # corners
    self.bitmap.blt(xs[0], ys[0], @windowskin, CORNER_RECTS[0])
    self.bitmap.blt(xs[2], ys[0], @windowskin, CORNER_RECTS[1])
    self.bitmap.blt(xs[0], ys[2], @windowskin, CORNER_RECTS[2])
    self.bitmap.blt(xs[2], ys[2], @windowskin, CORNER_RECTS[3])
    # borders
    self.bitmap.stretch_blt(Rect.new(xs[1], ys[0], w - BW * 2, BH),
      @windowskin, BORDER_RECTS[0])
    self.bitmap.stretch_blt(Rect.new(xs[0], ys[1], BW, h - BH * 2),
      @windowskin, BORDER_RECTS[1])
    self.bitmap.stretch_blt(Rect.new(xs[2], ys[1], BW, h - BH * 2),
      @windowskin, BORDER_RECTS[2])
    self.bitmap.stretch_blt(Rect.new(xs[1], ys[2], w - BW * 2, BH),
      @windowskin, BORDER_RECTS[3])
    # center
    self.bitmap.stretch_blt(Rect.new(xs[1], ys[1], w - BW * 2, h - BH * 2),
      @windowskin, RECTS[4])
  end
  
  def windowskin=(value)
    if @windowskin != value
      @windowskin = value
      self.create_bitmap(@width, @height)
    end
  end
  
  def set(x, y, width, height)
    @frames = Graphics.frame_count + 10 if !self.visible
    self.visible = true if @visible
    self.x = x
    self.y = y
    self.create_bitmap(width, height) if @width != width || @height != height
  end
    
  def empty
    visible_old = @visible
    self.visible = false
    @visible = visible_old
  end
  
  def self.visible=(value)
    super
    @visible = value
  end
  
  def update
    self.opacity = 191 + 32 *
      Math.sin((@frames - Graphics.frame_count) * Math::PI / 20)
  end
  
  def dispose
    self.bitmap.dispose if self.bitmap != nil && !self.bitmap.disposed?
    super
  end
  
end
