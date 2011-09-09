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
#import test
# mode = 'import' if mode == nil
# frompath = '.' if frompath == nil
# topath = './import' if topath == nil

#export test
# mode = 'export' if mode == nil
# frompath = './import' if frompath == nil
# topath = './export' if topath == nil

#python test
mode = 'export' if mode == nil
frompath = './python_export' if frompath == nil
topath = './ruby_python_export' if topath == nil
#END script compialation nil handleing

require './data'
require './arc_dump'

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
  data = ARC_Dump.load(f)
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
  ARC_Dump.dump(data, f)
  f.close()
end

success = false

filename = "ARC_DUMP_IO.log"
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
    puts "Importing RMXP data to ARC"
    puts "================================"
    if !static_mode
      domaps = false
      for file in files
        if file == "Maps"
          domaps = true
        else
          data = load_data(frompath + "/Data/#{file}.rxdata")
          arc_dump_data(topath + "Data/acotrs")
        end
      end
      if domaps
        map_infos = load_data(frompath + "/Data/MapInfos.rxdata")
        maps = []
        for key in map_infos.keys()
          _map = load_data(frompath + "/Data/Map%03d.rxdata" % key)
          maps.push(_map)
        end
        arc_dump_data(topath + "/Data/MapInfos.arc", map_infos)
        i = 0
        for key in map_infos.keys()
          arc_dump_data(topath + "/Data/Map%03d.arc" % key, maps[i])
          i += 1
        end
      end
    else
      #load /Data
      time_now = Time.now
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
      scripts = load_data(frompath + "/Data/Scripts.rxdata")
      maps = []
      for key in map_infos.keys()
        _map = load_data(frompath + "/Data/Map%03d.rxdata" % key)
        maps.push(_map)
      end
      puts ""
      puts "Compleated Loading in: #{Time.now - time_now} Seconds"
      puts ""
      time_now = Time.now
      #dump /Data
      arc_dump_data(topath + "/Data/Actors.arc", actors)
      arc_dump_data(topath + "/Data/Classes.arc", classes)
      arc_dump_data(topath + "/Data/Skills.arc", skills)
      arc_dump_data(topath + "/Data/Items.arc", items)
      arc_dump_data(topath + "/Data/Weapons.arc", weapons)
      arc_dump_data(topath + "/Data/Armors.arc", armors)
      arc_dump_data(topath + "/Data/Enemies.arc", enemies)
      arc_dump_data(topath + "/Data/Troops.arc", troops)
      arc_dump_data(topath + "/Data/States.arc", states)
      arc_dump_data(topath + "/Data/Animations.arc", animations)
      arc_dump_data(topath + "/Data/Tilesets.arc", tilesets)
      arc_dump_data(topath + "/Data/CommonEvents.arc", common_events)
      arc_dump_data(topath + "/Data/System.arc", system)
      arc_dump_data(topath + "/Data/MapInfos.arc", map_infos)
      arc_dump_data(topath + "/Data/Scripts.arc", scripts)
      i = 0
      for key in map_infos.keys()
        arc_dump_data(topath + "/Data/Map%03d.arc" % key, maps[i])
        i += 1
      end
      puts ""
      puts "Compleated Dumping in: #{Time.now - time_now} Seconds"
      puts ""
    end
    puts "Done"
    success = true
  when "export"
    filename = "export.log"
    puts "================================"
    puts "Exporting ARC data to RMXP"
    puts "================================"
    if !static_mode
      domaps = false
      for file in files
        if file == "Maps"
          domaps = true
        else
          data = arc_load_data(frompath + "/Data/#{file}.arc")
          arc_dump_data(topath + "Data/acotrs")
        end
      end
      if domaps
        map_infos = arc_load_data(frompath + "/Data/MapInfos.arc")
        maps = []
        for key in map_infos.keys()
          _map = arc_load_data(frompath + "/Data/Map%03d.arc" % key)
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
      time_now = Time.now
      actors = arc_load_data(frompath + "/Data/Actors.arc")
      classes = arc_load_data(frompath + "/Data/Classes.arc")
      skills = arc_load_data(frompath + "/Data/Skills.arc")
      items = arc_load_data(frompath + "/Data/Items.arc")
      weapons = arc_load_data(frompath + "/Data/Weapons.arc")
      armors = arc_load_data(frompath + "/Data/Armors.arc")
      enemies = arc_load_data(frompath + "/Data/Enemies.arc")
      troops = arc_load_data(frompath + "/Data/Troops.arc")
      states = arc_load_data(frompath + "/Data/States.arc")
      animations = arc_load_data(frompath + "/Data/Animations.arc")
      tilesets = arc_load_data(frompath + "/Data/Tilesets.arc")
      common_events = arc_load_data(frompath + "/Data/CommonEvents.arc")
      system = arc_load_data(frompath + "/Data/System.arc")
      map_infos = arc_load_data(frompath + "/Data/MapInfos.arc")
      scripts = arc_load_data(frompath + "/Data/Scripts.arc")
      maps = []
      for key in map_infos.keys()
        _map = arc_load_data(frompath + "/Data/Map%03d.arc" % key)
        maps.push(_map)
      end
      puts ""
      puts "Compleated Loading in: #{Time.now - time_now} Seconds"
      puts ""
      time_now = Time.now
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
      dump_data(topath + "/Data/Scripts.rxdata", scripts)
      i = 0
      for key in map_infos.keys()
        dump_data(topath + "/Data/Map%03d.rxdata" % key, maps[i])
        i += 1
      end
      puts ""
      puts "Compleated Dumping in: #{Time.now - time_now} Seconds"
      puts ""
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
