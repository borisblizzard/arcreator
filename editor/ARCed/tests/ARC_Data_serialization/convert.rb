$frompath = ARGV[0]
$topath = ARGV[1]
changed_files = ARGV[2]
$static_mode = false
$files = []
if changed_files != nil && changed_files != 'all'
	$files = changed_files.split("|")
else
	$static_mode = true
end

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
