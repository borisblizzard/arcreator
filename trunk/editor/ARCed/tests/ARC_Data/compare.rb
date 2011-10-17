require './convert.rb'

$frompath = './RMXP_original' if $frompath == nil
$topath = './RMXP_imported' if $topath == nil

def check_data(filename)
	file = File.open($frompath + filename, 'rb')
	data1 = file.read
	file.close
	file = File.open($topath + filename, 'rb')
	data2 = file.read
	file.close
	return (data1 == data2)
end

begin
	puts "================================"
	puts "Comparing RMXP old to RMXP new"
	puts "================================"
	# check data
	time_now = Time.now
	puts "not matching: Actors.rxdata" if !check_data("/Data/Actors.rxdata")
	puts "not matching: Ckasses.rxdata" if !check_data("/Data/Classes.rxdata")
	puts "not matching: Skills.rxdata" if !check_data("/Data/Skills.rxdata")
	puts "not matching: Items.rxdata" if !check_data("/Data/Items.rxdata")
	puts "not matching: Weapons.rxdata" if !check_data("/Data/Weapons.rxdata")
	puts "not matching: Armors.rxdata" if !check_data("/Data/Armors.rxdata")
	puts "not matching: Enemies.rxdata" if !check_data("/Data/Enemies.rxdata")
	puts "not matching: Troops.rxdata" if !check_data("/Data/Troops.rxdata")
	puts "not matching: States.rxdata" if !check_data("/Data/States.rxdata")
	puts "not matching: Animations.rxdata" if !check_data("/Data/Animations.rxdata")
	puts "not matching: Tilesets.rxdata" if !check_data("/Data/Tilesets.rxdata")
	puts "not matching: CommonEvents.rxdata" if !check_data("/Data/CommonEvents.rxdata")
	puts "not matching: System.rxdata" if !check_data("/Data/System.rxdata")
	puts "not matching: MapInfos.rxdata" if !check_data("/Data/MapInfos.rxdata")
	map_infos = load_data($frompath + "/Data/MapInfos.rxdata")
	for key in map_infos.keys
		puts "not matching: Map%03d.rxdata" % key if !check_data("/Data/Map%03d.rxdata" % key)
	end
	puts ""
	puts "Completed Loading in: #{Time.now - time_now} Seconds"
	puts ""
rescue
	puts "there was an error"
	puts $!.message
	puts $!.backtrace.join("\n").gsub(Dir.getwd){'.'}
end
gets rescue nil
