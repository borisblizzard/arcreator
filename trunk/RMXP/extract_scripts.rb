require 'zlib'

file = File.open('./Data/Scripts.rxdata', 'r')
scripts = Marshal.load(file)
file.close

decrypted = []
keys = []
scripts.each {|script|
	puts "Processing #{script[1]}..."
	s = Zlib::Inflate.inflate(script[2])
	s.gsub!("\r") {''}
	decrypted.push(s)
	keys.push(script[1])
}

file = File.open('./Scripts.rb', 'w')
file.write(decrypted.join("\n"))
file.close

puts 'Done.'
