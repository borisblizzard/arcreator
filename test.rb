puts "Using Ruby '#{RUBY_VERSION}' built for '#{RUBY_PLATFORM}' released on '#{RUBY_RELEASE_DATE}'\n\nHello World."
puts 'Press ENTER to exit'
loop do
	Graphics.update
	Input.update
	Graphics.frame_reset if Input.press?(Input::C)
	break if Input.press?(Input::B)
end
