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
s2.bitmap = Bitmap.new(64, 64)
c = Color.new(255, 255, 255)
s2.bitmap.set_pixel(0, 0, c)
s2.bitmap.set_pixel(1, 0, c)
s2.bitmap.set_pixel(0, 1, c)
s2.bitmap.set_pixel(1, 1, c)
s2.bitmap.fill_rect(5, 5, 10, 10, Color.new(0, 255, 0))
s2.bitmap.fill_rect(Rect.new(0, 30, 30, 30), Color.new(255, 255, 0))
c = s2.bitmap.get_pixel(5, 31)
p c.class
p c
s2.y = 100
s1.z = 10
GC.start
loop do
	Graphics.update
	Input.update
	Graphics.frame_reset if Input.press?(Input::C)
	s1.y = 100 + Graphics::frame_count % 20
	s2.x = 100 + Graphics::frame_count % 20
	begin
		
	rescue
	end
	break if Input.press?(Input::B)
end

