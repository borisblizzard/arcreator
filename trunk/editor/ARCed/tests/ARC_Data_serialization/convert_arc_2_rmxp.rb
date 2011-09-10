require './convert.rb'

frompath = ARGV[0]
topath = ARGV[1]
changed_files = ARGV[2]
static_mode = false
files = []
if changed_files != nil && changed_files != 'all'
	files = changed_files.split("|")
else
	static_mode = true
end

#python test
frompath = './ARC_original' if frompath == nil
topath = './RMXP_imported' if topath == nil
#END script compialation nil handleing

filename = "convert.log"
begin
	Dir.mkdir(topath) if !File.directory?(topath)
	Dir.mkdir(topath + "/Data") if !File.directory?(topath + "/Data")
	filename = "convert_arc_2_rxmp.log"
	puts "================================"
	puts "Converting ARC to RMXP"
	puts "================================"
	if !static_mode
		domaps = false
		for file in files
			if file == "Maps"
				domaps = true
			else
				data = arc_load_data(frompath + "/Data/#{file}.rxdata")
				arc_dump_data(topath + "Data/#{file}.arc")
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
		system = arc_load_data(frompath + "/Data/System.arc")
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
		scripts = arc_load_data(frompath + "/Data/Scripts.arc")
		maps = []
		for key in map_infos.keys
			_map = arc_load_data(frompath + "/Data/Map%03d.arc" % key)
			maps.push(_map)
		end
		puts ""
		puts "Completed Loading in: #{Time.now - time_now} Seconds"
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
		for key in map_infos.keys
			dump_data(topath + "/Data/Map%03d.rxdata" % key, maps[i])
			i += 1
		end
		puts ""
		puts "Completed Dumping in: #{Time.now - time_now} Seconds"
		puts ""
	end
rescue
	puts "there was an error"
	puts $!.message
	puts $!.backtrace.join("\n").gsub(Dir.getwd){'.'}
end
gets rescue nil
