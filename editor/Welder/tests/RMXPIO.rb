mode = ARGV[0]
frompath = ARGV[1]
topath = ARGV[2]
changed_files = ARGV[3]
static_mode = false
files = []
if changed_files != nil && changed_files != 'all'
  files = changed_files.split("|")
else
  static_mode = true
end
#the next few lines are here only for script compialation
mode = 'import' if mode == nil
frompath = '.' if frompath == nil
topath = './import' if topath == nil
#END script compialation nil handleing

require './data'
require './RMPY'

def load_data(filename)
  puts "- loading #{filename}..."
  f = open(filename, 'rb')
  data = Marshal.load(f)
  f.close()
  return data
end

def rmpy_load_data(filename)
  puts "- loading rmpy #{filename}..."
  f = open(filename, 'rb')
  data = RMPY.load(f)
  f.close()
  return data
end

def dump_data(filename, data)
  puts "- dumping rmpy #{filename}..."
  f = open(filename, 'wb')
  Marshal.dump(data, f)
  f.close()
end

def rmpy_dump_data(filename, data)
  puts "- dumping rmpy #{filename}..."
  f = open(filename, 'wb')
  RMPY.dump(data, f)
  f.close()
end

success = false

filename = "RMXPIO.log"
begin
  unless File.directory?(topath)
      Dir.mkdir(topath)
    end
  unless File.directory?(topath + "/Data")
    Dir.mkdir(topath + "/Data")
  end
  case mode
  when "import"
    filename = "import.log"
    puts "================================"
    puts "Importing RMXP data to RMPY"
    puts "================================"
    if !static_mode
      domaps = false
      for file in files
        if file == "Maps"
          domaps = true
        else
          data = load_data(frompath + "/Data/#{file}.rxdata")
          rmpy_dump_data(topath + "Data/acotrs")
        end
      end
      if domaps
        map_infos = load_data(frompath + "/Data/MapInfos.rxdata")
        maps = []
        for key in map_infos.keys()
          _map = load_data(frompath + "/Data/Map%03d.rxdata" % key)
          maps.push(_map)
        end
        rmpy_dump_data(topath + "/Data/MapInfos.rmpy", map_infos)
        i = 0
        for key in map_infos.keys()
          rmpy_dump_data(topath + "/Data/Map%03d.rmpy" % key, maps[i])
          i += 1
        end
      end
    else
      #load /Data
      actors = load_data(frompath + "/Data/Actors.rxdata")
      classes = load_data(frompath + "/Data/Classes.rxdata")
      skills = load_data(frompath + "/Data/Skills.rxdata")
      items = load_data(frompath + "/Data/Items.rxdata")
      weapons = load_data(frompath + "/Data/Weapons.rxdata")
      armors = load_data(frompath + "/Data/Armors.rxdata")
      enemies = load_data(frompath + "/Data/Enemies.rxdata")
      troops = load_data(frompath + "/Data/Troops.rxdata")
      states = load_data(frompath + "/Data/States.rxdata")
      animations = load_data(frompath + "/Data/Animations.rxdata")
      tilesets = load_data(frompath + "/Data/Tilesets.rxdata")
      common_events = load_data(frompath + "/Data/CommonEvents.rxdata")
      system = load_data(frompath + "/Data/System.rxdata")
      map_infos = load_data(frompath + "/Data/MapInfos.rxdata")
      maps = []
      for key in map_infos.keys()
        _map = load_data(frompath + "/Data/Map%03d.rxdata" % key)
        maps.push(_map)
      end
      #dump /Data
      rmpy_dump_data(topath + "/Data/Actors.rmpy", actors)
      rmpy_dump_data(topath + "/Data/Classes.rmpy", classes)
      rmpy_dump_data(topath + "/Data/Skills.rmpy", skills)
      rmpy_dump_data(topath + "/Data/Items.rmpy", items)
      rmpy_dump_data(topath + "/Data/Weapons.rmpy", weapons)
      rmpy_dump_data(topath + "/Data/Armors.rmpy", armors)
      rmpy_dump_data(topath + "/Data/Enemies.rmpy", enemies)
      rmpy_dump_data(topath + "/Data/Troops.rmpy", troops)
      rmpy_dump_data(topath + "/Data/States.rmpy", states)
      rmpy_dump_data(topath + "/Data/Animations.rmpy", animations)
      rmpy_dump_data(topath + "/Data/Tilesets.rmpy", tilesets)
      rmpy_dump_data(topath + "/Data/CommonEvents.rmpy", common_events)
      rmpy_dump_data(topath + "/Data/System.rmpy", system)
      rmpy_dump_data(topath + "/Data/MapInfos.rmpy", map_infos)
      i = 0
      for key in map_infos.keys()
        rmpy_dump_data(topath + "/Data/Map%03d.rmpy" % key, maps[i])
        i += 1
      end
    end
    puts "Done"
    success = true
  when "export"
    filename = "export.log"
    puts "================================"
    puts "Exporting RMPY data to RMXP"
    puts "================================"
    if !static_mode
      domaps = false
      for file in files
        if file == "Maps"
          domaps = true
        else
          data = load_data(frompath + "/Data/#{file}.rxdata")
          rmpy_dump_data(topath + "Data/acotrs")
        end
      end
      if domaps
        map_infos = rmpy_load_data(frompath + "/Data/MapInfos.rmpy")
        maps = []
        for key in map_infos.keys()
          _map = rmpy_load_data(frompath + "/Data/Map%03d.rmpy" % key)
          maps.push(_map)
        end
        dump_data(topath + "/Data/MapInfos.rxdata", map_infos)
        i = 0
        for key in map_infos.keys()
          dump_data(topath + "/Data/Map%03d.rxdata" % key, maps[i])
          i += 1
        end
      end
    else
      #load /Data
      actors = rmpy_load_data(frompath + "/Data/Actors.rmpy")
      classes = rmpy_load_data(frompath + "/Data/Classes.rmpy")
      skills = rmpy_load_data(frompath + "/Data/Skills.rmpy")
      items = rmpy_load_data(frompath + "/Data/Items.rmpy")
      weapons = rmpy_load_data(frompath + "/Data/Weapons.rmpy")
      armors = rmpy_load_data(frompath + "/Data/Armors.rmpy")
      enemies = rmpy_load_data(frompath + "/Data/Enemies.rmpy")
      troops = rmpy_load_data(frompath + "/Data/Troops.rmpy")
      states = rmpy_load_data(frompath + "/Data/States.rmpy")
      animations = rmpy_load_data(frompath + "/Data/Animations.rmpy")
      tilesets = rmpy_load_data(frompath + "/Data/Tilesets.rmpy")
      common_events = rmpy_load_data(frompath + "/Data/CommonEvents.rmpy")
      system = rmpy_load_data(frompath + "/Data/System.rmpy")
      map_infos = rmpy_load_data(frompath + "/Data/MapInfos.rmpy")
      maps = []
      for key in map_infos.keys()
        _map = rmpy_load_data(frompath + "/Data/Map%03d.rmpy" % key)
        maps.push(_map)
      end
      #dump Data
      dump_data(topath + "/Data/Actors.rxdata", actors)
      dump_data(topath + "/Data/Classes.rxdata", classes)
      dump_data(topath + "/Data/Skills.rxdata", skills)
      dump_data(topath + "/Data/Items.rxdata", items)
      dump_data(topath + "/Data/Weapons.rxdata", weapons)
      dump_data(topath + "/Data/Armors.rxdata", armors)
      dump_data(topath + "/Data/Enemies.rxdata", enemies)
      dump_data(topath + "/Data/Troops.rxdata", troops)
      dump_data(topath + "/Data/States.rxdata", states)
      dump_data(topath + "/Data/Animations.rxdata", animations)
      dump_data(topath + "/Data/Tilesets.rxdata", tilesets)
      dump_data(topath + "/Data/CommonEvents.rxdata", common_events)
      dump_data(topath + "/Data/System.rxdata", system)
      dump_data(topath + "/Data/MapInfos.rxdata", map_infos)
      i = 0
      for key in map_infos.keys()
        dump_data(topath + "/Data/Map%03d.rxdata" % key, maps[i])
        i += 1
      end
    end
    puts "Done"
    success = true
  end
rescue
  puts "there was an error"
  puts $!.message
  puts $!.backtrace.join("\n").gsub(Dir.getwd){'.'}
  success = false
  f = open(filename, 'wb')
  f.write($!.message)
  f.write($!.backtrace.join("\n").gsub(Dir.getwd) {'.'})
  f.close
ensure
  f = open(filename, 'wb')
  if success
    puts "writeing log"
    f.write("success")
  end
  f.close()
end
