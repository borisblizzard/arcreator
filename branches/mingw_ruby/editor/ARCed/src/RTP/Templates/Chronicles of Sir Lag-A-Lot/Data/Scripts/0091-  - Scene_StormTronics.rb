#==============================================================================
# Scene_StormTronics
#------------------------------------------------------------------------------
#  Intro scene for games from StormTronics. You are not allowed to use any code
#  of this, but you are allowed to take a look at it and maybe understant the
#  idea and animation process.
#==============================================================================

class Scene_StormTronics
  
  # initialize which game
  def initialize(game)
    @game = game
  end
  
  # make display delay in seconds
  def delay(frame)
    (frame*40).to_i.times {Graphics.update}
  end
  
  # main process
  def main
    # pre-initialization
    $game_party.setup_starting_members
    $game_map.setup($data_system.start_map_id)
    # intro handling
    unless false #$DEBUG
      show_intro
      Graphics.freeze
    end
    $game_map.autoplay
    # post-initialization
    $game_player.moveto($data_system.start_x, $data_system.start_y)
    $game_player.refresh
    $game_map.update
    # change scene
    $scene = Scene_Map.new
  end
    
  # StormTronics intro
  def show_intro
    # create common viewport
    view = Viewport.new(0, 0, 640, 480)
    Graphics.transition
    Graphics.freeze
    # create a few sprites
    @intro1 = Sprite.new
    @intro2 = Sprite.new
    @intro3 = Sprite.new
    @presents = Sprite.new
    @intro4 = Sprite.new
    @intro4.z = 100
    # stop all audio playing
    Audio.se_stop
    Audio.me_stop
    Audio.bgm_stop
    Audio.bgs_stop
    # delay
    delay(0.5)
    # cache StromTronics imgaes
    @intro1.bitmap = RPG::Cache.title('StormTronics')
    @intro2.bitmap = RPG::Cache.title('glow')
    @intro3.bitmap = RPG::Cache.title('StormMask')
    @presents.bitmap = RPG::Cache.title('presents')
    @presents.x = @presents.y = 160
    @intro2.x = -240
    # transition
    Graphics.transition
    # delay
    delay(0.5)
    Graphics.freeze
    # set up flash effect
    @intro4.visible = true
    @intro4.bitmap = RPG::Cache.title('StormFlash')
    # show flash effect within 4 frames
    Graphics.transition(2)
    Graphics.freeze
    @intro4.dispose
    Graphics.transition(2)
    # delay
    delay(0.5)
    # make the reflection seem to move
    loop do
      @intro2.x += 50
      Graphics.update
      break if @intro2.x > 700
    end
    # delay
    delay(2)
    Graphics.freeze
    # free memory from image
    @intro1.dispose
    @intro2.dispose
    @intro3.dispose
    @presents.dispose
    @intro1 = @intro2 = @intro3 = @intro4 = @presents = nil
    Graphics.transition(10)
    # delay
    delay(1)
    # pre-cache images to avoid lag later
    RPG::Cache.title('back')
    RPG::Cache.title('lagalot')
    RPG::Cache.title('letters1')
    RPG::Cache.title('letters2')
    RPG::Cache.title('letters3')
    RPG::Cache.title('final')
    RPG::Cache.title('abs_game')
    RPG::Cache.title('inverted')
    Graphics.freeze
    (1..8).each {|i| RPG::Cache.title(i.to_s)}
    # music play depending on which example game
    music = case @game
    when 1
      'E Nomine - Die Schwarzen Reiter (Blizzard Edit for Blizz-ABS Demo)'
    end
    Audio.me_play("Audio/BGM/#{music}", 95, 100)
    # create a few sprites
    @stripes = Sprite.new(view)
    @back = Sprite.new(view)
    @lag = Sprite.new(view)
    @letters1 = Sprite.new(view)
    @letters2 = Sprite.new(view)
    @letters3 = Sprite.new(view)
    # use the cached images
    @back.bitmap = RPG::Cache.title('back')
    @lag.bitmap = RPG::Cache.title('lagalot')
    @letters1.bitmap = RPG::Cache.title('letters1')
    @letters2.bitmap = RPG::Cache.title('letters2')
    @letters3.bitmap = RPG::Cache.title('letters3')
    @stripes.bitmap = Bitmap.new(640, 480)
    # make movie stripes
    @stripes.bitmap.fill_rect(0, 0, 640, 80, Color.new(0, 0, 0))
    @stripes.bitmap.fill_rect(0, 400, 640, 80, Color.new(0, 0, 0))
    # set up position of all sprites
    @stripes.z = 100
    @back.zoom_x = @back.zoom_y = 2.0
    @letters1.y = -4400
    @letters2.x = 4840
    @letters3.y = 4770
    @back.x = @lag.x = @back.ox = @lag.ox = 640
    @back.y = 80
    @lag.oy = -80
    @lag.zoom_x = @lag.zoom_y = 1.7
    @letters1.x = 270
    @letters2.y = 190
    @letters3.x = 140
    @letters1.z = @letters2.z = @letters3.z = 200
    Graphics.transition(2)
    # make the animation
    loop do
      Graphics.update
      @back.zoom_x = @back.zoom_y = [@back.zoom_x - 0.004, 1.0].max
      @letters1.y += 16
      @letters2.x -= 16
      @letters3.y -= 16
      @lag.zoom_x = @lag.zoom_y = [@back.zoom_x - 0.0028, 1.0].max
      break if @letters1.y == 80
    end
    # delete all sprites
    view.dispose
    # make a new viewport
    view = Viewport.new(0, 0, 640, 480)
    # make a white flashing animation that transits to the final title image
    @white = Sprite.new(view)
    @white.z = 300
    @white.bitmap = RPG::Cache.title('inverted')
    #@white.bitmap = Bitmap.new(640, 480)
    #@white.bitmap.fill_rect(0, 0, 640, 480, Color.new(255, 255, 255))
    @final = Sprite.new(view)
    @final.z = 200
    @final.bitmap = RPG::Cache.title('final')
    17.times {Graphics.update; @white.opacity -= 15}
    Graphics.update
    Graphics.freeze
    Graphics.transition(80)
    # delay
    delay(0.9)
    Graphics.freeze
    # show the ABS example image
    @abs = Sprite.new(view)
    @abs.bitmap = RPG::Cache.title('abs_game')
    @abs.y, @abs.z = 400, 500
    Graphics.transition(80)
    Graphics.freeze
    delay(1.7)
    # delete all sprites
    view.dispose
    Graphics.transition(60)
    Graphics.freeze
    # delay
    delay(1)
    # Credits
    Graphics.transition
    Graphics.freeze
    @snap = Sprite.new
    @credits = Sprite.new
    @snap.bitmap = RPG::Cache.title('1')
    @snap.x = 320
    @snap.y = 256
    @credits.bitmap = Bitmap.new(640, 480)
    @credits.bitmap.font.name = 'Arial'
    @credits.bitmap.font.size = 26
    @credits.bitmap.draw_text(64, 96, 480, 32, 'Producer')
    @credits.bitmap.draw_text(64, 160, 480, 32, 'Boris Mikić alias Blizzard')
    Graphics.transition
    delay(3.5)
    Graphics.freeze
    @snap.bitmap.dispose
    @credits.bitmap.clear
    Graphics.transition
    delay(1)
    Graphics.freeze
    @snap.bitmap = RPG::Cache.title('2')
    @snap.x = 96
    @snap.y = 64
    @credits.bitmap.draw_text(354, 256, 640, 32, 'Graphics')
    @credits.bitmap.draw_text(354, 320, 640, 32, 'Enterbrain')
    @credits.bitmap.draw_text(354, 352, 640, 32, 'landofshadows')
    @credits.bitmap.draw_text(354, 384, 640, 32, 'Various artists')
    Graphics.transition
    delay(3.5)
    Graphics.freeze
    @snap.bitmap.dispose
    @credits.bitmap.clear
    Graphics.transition
    delay(1)
    Graphics.freeze
    @snap.bitmap = RPG::Cache.title('3')
    @snap.x = 400
    @snap.y = 80
    @credits.bitmap.draw_text(64, 256, 640, 32, 'Music')
    @credits.bitmap.draw_text(64, 320, 640, 32, 'Enterbrain')
    @credits.bitmap.draw_text(64, 352, 640, 32, 'Various artists')
    Graphics.transition
    delay(3.5)
    Graphics.freeze
    @snap.bitmap.dispose
    @credits.bitmap.clear
    Graphics.transition
    delay(1)
    Graphics.freeze
    @snap.bitmap = RPG::Cache.title('4')
    @snap.x = 96
    @snap.y = 288
    @credits.bitmap.draw_text(320, 96, 640, 32, 'Main Engine')
    @credits.bitmap.draw_text(320, 160, 640, 32, 'Enterbrain')
    Graphics.transition
    delay(3.5)
    Graphics.freeze
    @snap.bitmap.dispose
    @credits.bitmap.clear
    Graphics.transition
    delay(1)
    Graphics.freeze
    @snap.bitmap = RPG::Cache.title('5')
    @snap.x = 352
    @snap.y = 288
    @credits.bitmap.draw_text(96, 96, 640, 32, 'Custom Scripts and Blizz-ABS')
    @credits.bitmap.draw_text(96, 160, 640, 32, 'Blizzard')
    Graphics.transition
    delay(3.5)
    Graphics.freeze
    @snap.bitmap.dispose
    @credits.bitmap.clear
    Graphics.transition
    delay(1)
    Graphics.freeze
    @snap.bitmap = RPG::Cache.title('6')
    @snap.x = 64
    @snap.y = 64
    @credits.bitmap.draw_text(224, 288, 640, 32, 'Additional Blizz-ABS Graphics')
    @credits.bitmap.draw_text(224, 352, 640, 32, 'Blizzard')
    Graphics.transition
    delay(3.5)
    Graphics.freeze
    @snap.bitmap.dispose
    @credits.bitmap.clear
    Graphics.transition
    delay(1)
    Graphics.freeze
    @snap.bitmap = RPG::Cache.title('7')
    @snap.x = 416
    @snap.y = 96
    @credits.bitmap.draw_text(32, 224, 640, 32, 'Mapping')
    @credits.bitmap.draw_text(32, 288, 640, 32, 'Original maps by Blizzard')
    @credits.bitmap.draw_text(32, 320, 640, 32, 'Maps from "The Legend of Lexima™ IV - Chaos Project"')
    Graphics.transition
    delay(3.5)
    Graphics.freeze
    @snap.bitmap.dispose
    @credits.bitmap.clear
    Graphics.transition
    delay(1)
    Graphics.freeze
    @snap.bitmap = RPG::Cache.title('8')
    @snap.x = 64
    @snap.y = 288
    @credits.bitmap.draw_text(192, 96, 640, 32, 'Title Music:')
    @credits.bitmap.draw_text(192, 160, 640, 32, 'E Nomine - Die schwarzen Reiter')
    @credits.bitmap.draw_text(192, 192, 640, 32, '(Blizzard Edit for Blizz-ABS Demo)')
    Graphics.transition
    delay(3.5)
    Graphics.freeze
    @snap.dispose
    @credits.dispose
    # last transition
    Graphics.transition
    delay(2)
  end

end
