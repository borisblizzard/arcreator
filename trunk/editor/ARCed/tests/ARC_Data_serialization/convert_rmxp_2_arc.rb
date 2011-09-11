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

frompath = './RMXP_original' if frompath == nil
topath = './ARC_imported' if topath == nil

filename = "convert.log"
begin
	Dir.mkdir(topath) if !File.directory?(topath)
	Dir.mkdir(topath + "/Data") if !File.directory?(topath + "/Data")
	filename = "convert_rmxp_2_arc.log"
	puts "================================"
	puts "Converting RMXP to ARC"
	puts "================================"
	if !static_mode
		domaps = false
		for file in files
			if file == "Maps"
				domaps = true
			else
				data = load_data(frompath + "/Data/#{file}.rxdata")
				arc_dump_data(topath + "Data/actors")
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
		# load ./Data
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
		maps = []
		for key in map_infos.keys
			_map = load_data(frompath + "/Data/Map%03d.rxdata" % key)
			maps.push(_map)
		end
		puts ""
		puts "Completed Loading in: #{Time.now - time_now} Seconds"
		puts ""
		time_now = Time.now
		# dump ./Data
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
		i = 0
		for key in map_infos.keys
			arc_dump_data(topath + "/Data/Map%03d.arc" % key, maps[i])
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
