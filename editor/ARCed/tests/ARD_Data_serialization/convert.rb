require './data'
require './arc_data_dump'

def load_data(filename)
  puts "- Loading #{filename}..."
  f = open(filename, 'rb')
  data = Marshal.load(f)
  f.close()
  return data
end

def arc_load_data(filename)
  puts "- Loading ARC #{filename}..."
  f = open(filename, 'rb')
  data = ARC::Data.load(f)
  f.close()
  return data
end

def dump_data(filename, data)
  puts "- Dumping RMXP #{filename}..."
  f = open(filename, 'wb')
  Marshal.dump(data, f)
  f.close()
end

def arc_dump_data(filename, data)
  puts "- Dumping ARC #{filename}..."
  f = open(filename, 'wb')
  ARC::Data.dump(f, data)
  f.close()
end
