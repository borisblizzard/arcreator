greeting = "\
Using Ruby '#{RUBY_VERSION}' built for '#{RUBY_PLATFORM}' released on '#{RUBY_RELEASE_DATE}'

Hello World. 
"
puts greeting
puts 'Press ENTER to exit'
input = '1'
c = Color.new(128, 128, 128)
p c.alpha
c = Color.new(128, 128, 128, 128)
p c.alpha
c.set(564, 64, 64, 64)
p c.red
c.red = 500
p c.red
p Graphics.frame_count
10.times {
Graphics.update
Input.update
}
p Graphics.frame_count
Graphics.frame_count = 50
p Graphics.frame_count
=begin
while input != '' && input != "\n"
	input = gets
end
=end