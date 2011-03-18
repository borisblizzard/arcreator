puts "Using Ruby '#{RUBY_VERSION}' built for '#{RUBY_PLATFORM}' released on '#{RUBY_RELEASE_DATE}'\n\nHello World."
puts 'Press ENTER to exit'
s1 = Sprite.new
s1.x = 100
s2 = Sprite.new
s2.y = 100
s1.z = 10
loop do
	Graphics.update
	Input.update
	Graphics.frame_reset if Input.press?(Input::C)
	s1.y = 100 + Graphics::frame_count % 20
	s2.x = 100 + Graphics::frame_count % 20
	break if Input.press?(Input::B)
end

