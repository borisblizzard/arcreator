puts "Using Ruby '#{RUBY_VERSION}' built for '#{RUBY_PLATFORM}' released on '#{RUBY_RELEASE_DATE}'\n\nHello World."
puts 'Press ESCAPE to exit'

s1 = Sprite.new
def test
	bitmap = Bitmap.new("test_resources/arc-logo")
	return
end

GC.start
test()
s1.bitmap = Bitmap.new("test_resources/arc-logo")
p s1.bitmap
s1.x = 100
GC.start
s1.bitmap.fill_rect(200, 0, 50, 50, Color.new(255, 0, 0))

s2 = Sprite.new
s2.bitmap = Bitmap.new(64, 64)
c = Color.new(255, 255, 255)
s2.bitmap.set_pixel(0, 0, c)
s2.bitmap.set_pixel(1, 0, c)
s2.bitmap.set_pixel(0, 1, c)
s2.bitmap.set_pixel(1, 1, c)
s2.bitmap.fill_rect(5, 5, 10, 10, Color.new(0, 255, 0, 128))
s2.bitmap.fill_rect(Rect.new(0, 30, 30, 30), Color.new(255, 255, 0, 128))

s1.bitmap.blt(240, 290, s2.bitmap, Rect.new(0, 0, 64, 64))

s3 = Sprite.new
s3.bitmap = s2.bitmap.clone
s3.bitmap.fill_rect(0, 0, 50, 50, Color.new(0, 128, 255))

c = s2.bitmap.get_pixel(5, 31)
p c.class
p c
s2.y = 100
s3.y = 300
s1.z = 10
GC.start
s2.bitmap.fill_rect(0, 0, s2.bitmap.width, s2.bitmap.height, Color.new(255, 255, 255))
s2.bitmap.fill_rect(s2.bitmap.width / 2, s2.bitmap.width / 2, s2.bitmap.width / 2, s2.bitmap.height / 2, Color.new(0, 255, 0))
s2.x = 32
s2.ox = 32
s2.oy = 32
s2.src_rect.set(16, 16, 40, 40)
p s2.src_rect
w1 = Window.new
#p1 = Plane.new()

loop do
	Graphics.update
	Input.update
	Graphics.frame_reset if Input.press?(Input::C)
	s1.y = 100 + Graphics::frame_count % 40
	#s2.x = 100 + Graphics::frame_count % 40
	s3.x = Graphics::frame_count % 40
	s3.y = 150 + Graphics::frame_count % 40
	s2.angle += 1
	s2.visible = Graphics::frame_count % 20 > 10
	break if Input.press?(Input::B)
end

