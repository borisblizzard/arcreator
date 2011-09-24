#==============================================================================
# Main
#==============================================================================

begin
  Font.default_name = 'Geometrix'
  Font.default_size = 24
  $fontface = 'Geometrix'
  $fontsize = 24
  Graphics.update
  Graphics.freeze
  GC.enable
  GC.start
  $scene = Scene_Stormtronics.new
  $scene.main while $scene
  Graphics.transition(20)
  Graphics.freeze
rescue Errno::ENOENT
  filename = $!.message.sub('No such file or directory - ', '')
  p "File #{filename} was not found."
end
