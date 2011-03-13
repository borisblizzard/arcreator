class A
	def p
		puts 'HAI'
	end
end
greeting = "\
Useing Ruby '#{RUBY_VERSION}' built for '#{RUBY_PLATFORM}' releaced on '#{RUBY_RELEASE_DATE}'

Hello World. 

"
puts greeting
puts 'Press ENTER to exit'
input = '1'
p Graphics.frame_count
10.times {Graphics.update}
p Graphics.frame_count
Graphics.frame_count = 50
p Graphics.frame_count
=begin
while input != '' && input != "\n"
	input = gets
end
=end