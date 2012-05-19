#==============================================================================
# ** Main
#------------------------------------------------------------------------------
#  After defining each class, actual processing begins here.
#==============================================================================
=begin
#p (GC.methods - Object.new.methods - Module.methods).sort()
    $data_actors        = ARC::Data.load("Data/Actors.arc")
    $data_classes       = ARC::Data.load("Data/Classes.arc")
    $data_skills        = ARC::Data.load("Data/Skills.arc")
    $data_items         = ARC::Data.load("Data/Items.arc")
    $data_weapons       = ARC::Data.load("Data/Weapons.arc")
    $data_armors        = ARC::Data.load("Data/Armors.arc")
    $data_enemies       = ARC::Data.load("Data/Enemies.arc")
    $data_troops        = ARC::Data.load("Data/Troops.arc")
    $data_states        = ARC::Data.load("Data/States.arc")
    $data_animations    = ARC::Data.load("Data/Animations.arc")
    $data_tilesets      = ARC::Data.load("Data/Tilesets.arc")
    $data_common_events = ARC::Data.load("Data/CommonEvents.arc")
    $data_system        = ARC::Data.load("Data/System.arc")
    # Make system object
    $game_system = Game_System.new
	#$game_map = Game_Map.new
	#$game_map.setup(13)
	
    map = ARC::Data.load("Data/Map013.arc")
    # set tile set information in opening instance variables
    tileset = $data_tilesets[map.tileset_id]
    #tileset.tileset_name
    #tileset.autotile_names
    #@passages = tileset.passages
    #tileset.priorities
    #@terrain_tags = tileset.terrain_tags
	
RPG::Cache.tileset(tileset.tileset_name)
for i in 0..6
  RPG::Cache.autotile(tileset.autotile_names[i])
end
v = Viewport.new(0, 0, 640, 480)
win = Window_Base.new(0, 0, 160, 160)
win.dispose
{
	#Game_M
	#Spriteset_Map.new
}
#RPG::Cache.windowskin($game_system.windowskin)
print "    - WAITING FOR INPUT"
loop do
	Input.update
	Graphics.update
	break if Input.trigger?(Input::C)
end

print "    - STARTING"
#o = []
GC.stress = true

40.times { |i|
	#Font.new("Arial", 24)
	#Color.new(255, 255, 255)
	#Tone.new(255, 255, 255)
	#Rect.new(0, 0, 0, 0)
	#RGSSError.new
	#Table.new(100000, 1, 1)
	#b = Bitmap.new(64, 64)
	#w = Window_Base.new(0, 0, 160, 160)
	#w.contents = b
	#s = Sprite.new
	#s.bitmap = b
	#b.fill_rect(0, 0, 64, 64, Color.new(255, 255, 0))
	t = Tilemap.new(v)
	t.tileset = RPG::Cache.tileset(tileset.tileset_name)
	for i in 0..6
	  t.autotiles[i] = RPG::Cache.autotile(tileset.autotile_names[i])
	end
	t.map_data = map.data
	t.priorities = tileset.priorities
	Graphics.update
	#w = Window_Base.new(0, 0, 160, 160)
	#w = Sprite.new
	#w.width = 160
	#w.height = 160
	#w.dispose
}
#o = nil
GC.start
GC.stress = false
print "    - DONE"

loop do
GC.start
	Input.update
	Graphics.update
	break if Input.trigger?(Input::C)
end

exit
=end

begin
  # Prepare for transition
  Graphics.freeze
  # Make scene object (title screen)
  $scene = Scene_Title.new
  # Call main method as long as $scene is effective
  $scene.main while $scene != nil
  # Fade out
  Graphics.transition(20)
  Graphics.update
rescue Errno::ENOENT
  # Supplement Errno::ENOENT exception
  # If unable to open file, display message and end
  filename = $!.message.sub("No such file or directory - ", "")
  print("Unable to find file #{filename}.")
end
