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
10.times {Graphics.update}
=begin
while input != '' && input != "\n"
	input = gets
end
=end