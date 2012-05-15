#==============================================================================
# Window_Controls
#==============================================================================

class Window_Controls < Window_Selectable
  
  attr_reader :controls
  
  def initialize
    super(0, 0, 640, 480)
    self.contents = Bitmap.new(width - 32, height - 32)
    self.contents.font.name = $fontface
    self.contents.font.size = 24
    @controls = [$controls.up, $controls.left, $controls.down, $controls.right,
        $controls.confirm, $controls.cancel, $controls.menu, $controls.leximus,
        $controls.prev, $controls.nex, $controls.snap]
    refresh
    self.index = 0
  end
  
  def refresh
    self.contents.clear
    @commands = ['Move Up', 'Move Left', 'Move Down', 'Move Right',
        'Confirm', 'Cancel', 'Call Menu / Trigger Menu Info',
        'Special', 'Previous Page', 'Next Page', 'Take Screenshot',
        'Save and exit', 'Discard changes']
    @item_max = @commands.size
    (0...@item_max).each {|i| draw_item(i)}
  end
  
  def draw_item(i)
    self.contents.fill_rect(0, i*32, 608, 32, Color.new(0, 0, 0, 0))
    self.contents.font.color = text_color(i == 11 ? 3 : (i == 12 ? 2 : 0))
    self.contents.draw_text(44, i*32, 320, 32, @commands[i])
    if i < 11
      if !correct?(i)
        self.contents.font.color = self.active ? down_color : up_color 
        chr = 'None'
      else
        self.contents.font.color = up_color unless self.active
        chr = CP.controls_name(@controls[i])
      end
      self.contents.draw_text(444, i*32, 320, 32, chr)
      self.contents.font.color = normal_color
    end
  end
  
  def update
    super
    if @index < 11
      if !self.active && Input.Anykey
        $game_system.se_play($data_system.decision_se)
        self.active = true
        i = @controls.index(Input.get(0))
        unless i == nil
          @controls[i] = @controls[@index]
          draw_item(i)
        end
        @controls[@index] = Input.get(0)
        @controls[@index] = Input.get(1) if @controls[@index] == 16
        draw_item(@index)
      elsif Input.repeat?($controls.confirm)
        $game_system.se_play($data_system.decision_se)
        self.active = false
        draw_item(@index)
      end
    end
  end
  
  def update_cursor_rect
    self.cursor_rect.set(0, @index * 32, 400, 32)
  end
  
  def correct?(i = nil)
    if i != nil
      return (@controls[i].between?(65, 90) || @controls[i].between?(48, 57) ||
          [160, 161, 13, 27, 40, 37, 39, 38, 32].include?(@controls[i]))
    end
    @controls.each {|c|
        unless c.between?(65, 90) || c.between?(48, 57) ||
            [160, 161, 13, 27, 40, 37, 39, 38, 32].include?(c)
          return false
        end}
    return true
  end
  
end

#==============================================================================
# Scene_Controls
#==============================================================================

class Scene_Controls
  
  def main
    $fontface = 'Geometrix'
    $fontsize = 24
    @window = Window_Controls.new
    @version = Sprite.new
    @version.bitmap = Bitmap.new(320, 32)
    @version.x = 316
    @version.y = 456
    @version.z = 12000
    @version.bitmap.font.name = 'EurostileExtended-Roman-DTC'
    @version.bitmap.font.bold = true
    @version.bitmap.font.size = 14
    @version.bitmap.draw_text(0, 0, 320, 32, "#{$release}: #{CP.ver($version)}", 2)
    Graphics.transition
    loop do
      Graphics.update
      Input.update
      update
      break if $scene != self
    end
    Graphics.freeze
    @window.dispose
    @version.dispose
  end
  
  def update
    active = @window.active
    @window.update
    if active
      if Input.trigger?($controls.cancel) ||
          @window.index == 12 && Input.trigger?($controls.confirm)
        $game_system.se_play($data_system.cancel_se)
        $scene = Scene_Title.new
      elsif @window.index == 11 && Input.trigger?($controls.confirm)
        if @window.correct?
          $game_system.se_play($data_system.decision_se)
          $controls.set_new_controls(@window.controls)
          CP.data_save
          $scene = Scene_Title.new
        else
          $game_system.se_play($data_system.buzzer_se)
        end
      end
    end
  end
  
end
