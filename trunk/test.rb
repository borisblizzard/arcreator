puts "Using Ruby '#{RUBY_VERSION}' built for '#{RUBY_PLATFORM}' released on '#{RUBY_RELEASE_DATE}'\n\nHello World."
puts 'Press ENTER to exit'
s1 = Sprite.new

def test
	bitmap = Bitmap.new("docs/arc-logo")
	return
end

GC.start
test()
s1.bitmap = Bitmap.new("docs/arc-logo")
p s1.bitmap
s1.x = 100
GC.start
s2 = Sprite.new
s2.bitmap = s1.bitmap
#s2.bitmap = Bitmap.new(32, 32)
#s2.set_pixel(0, 0, Color.new(255, 255, 255))
s2.y = 100
s1.z = 10
GC.start
loop do
	Graphics.update
	Input.update
	Graphics.frame_reset if Input.press?(Input::C)
	s1.y = 100 + Graphics::frame_count % 20
	s2.x = 100 + Graphics::frame_count % 20
	break if Input.press?(Input::B)
end

