def load_data(filename)
	file = File.open(filename)
	data = Marshal.load(file)
	file.close()
	return data
end
