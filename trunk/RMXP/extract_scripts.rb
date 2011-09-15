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

Dir.mkdir('Scripts') rescue nil

keys.each_index {|i|
	file = File.open("./Scripts/#{"%04d" % i}-#{keys[i].gsub(">", "").gsub("<", "").gsub("*", "+")}.rb", 'w')
	file.write("\xEF\xBB\xBF") # UTF-8 identifier
	file.write(decrypted[i])
	file.close
}
file = File.open('./Scripts/Scripts.rb', 'w')
file.write("\xEF\xBB\xBF") # UTF-8 identifier
file.write(decrypted.join("\n"))
file.close

puts 'Done.'
