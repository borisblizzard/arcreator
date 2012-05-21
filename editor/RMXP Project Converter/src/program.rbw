# Wx frame based RMXP to ARC Project Converter

#get WX
require "wx"
require "fileutils"
require "zlib"

Dir.chdir(File.dirname(__FILE__)) 

require "./ini_file"

ARCIcon = ("" +
"iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAABKVJ" +
"REFUWIXtlXtQVFUcx7/n7r0r+wAWVmV9IVqpDEqo+KAME2PUFJ3saRpjICbOiO6gyJgWYuhk" +
"xsQ0iuBEpqKJ6UghpuM4vMwkH5SLigSBjCDy2rsP93HvPbc/lOQ1/Wl/tJ+Z88c5v9f39ztz" +
"5gAePHj4v0MGOjwZNWrU8E15QyMWRF8byH4xa2d48ZY5hu69AiJU0TH2zGVVVy3vBln7+vvr" +
"Ug3GoDUv8rUt3NMY4MaIZR39BBQF1Y8sOTi2ShIFv0zT3KVkQ1lhT/v7wh79iEvGejtPfGT5" +
"SRcEUCplUI6xbjwhbgjM4fIAINlYzcw8lL+7LD9tPSSWFYWneVi1DMPivCSmr4COti9THTZR" +
"77QSZmukKcNmfLuXz8LBbSmOR7KPJFBQ8fGSBAqHXYbLLHnveZMemE2tMwDg1TPln5QdSU92" +
"2xjW7XjqL1MK3iXdaz4Rnsv2TD41q8JQPnZKvNBJAQBCU0sIPyQqBkAhADjcF0mi6TDPdyRm" +
"wLtHIAtwXK2OaS6KU/NK1RJhXWx6Qtzdw4tjU8QuCrMkdCmfW3pYsAdaQQFWC0yIu1S6o+aW" +
"q5eAJcvzk6uLpno53QJESZI0LlaRNrNuc7cAlTJKBrCz79S6+eh6jMpsKo4z/VIWFKn0nW0z" +
"E5VddMrD1q1akGs7d2WgmH8EzGkco796avcayeZCO3SXVfrQKsKXJzpqaiL+SDs6OzQtsbTh" +
"ZjY5nfHViM6zfbKogJWX4vUpVz6NcJrdsGjVlorC3NG2YAEOVnUn11YwYPFeAiY530mqbrdr" +
"XRRwzm/NCFp7oLpxoXWVhlFw28fvSAVQ+nmBVlM/+UITG9L/8Vw+xoBKKyCwDli8Pz5ba2r3" +
"dewPBOujEfo594ABgPDomz6mY2vWUd6MjjZ6vXLK3eLjlVsbnAg9Qh1WdNwunde6Qwpru/UQ" +
"TpsDjyyWfkvkzXDZrWhsHnQ+UzH/aN39WXWSzQrXg/qQYb9mj/vXCbz22YHEK9+/5+cSAQWX" +
"sPe0dX5ykW0LCg7tdTXWdoKhbpI0LnwzSoITMPplUImiqYUrJyKxQMFArbFPG+wtDVWwXti0" +
"jd8XZZguFrx1rmyXv5bXeYm+E05FXkio2pA9MSjACkqftM7ht86oeyRMPK7Wr/evp86HAQ94" +
"nSkicuUPf5my0yDaeymVOT9pbboxfO+2zBuEyHj9pGVySntsFQCEbr8xg635s8RX5fQiSr3Z" +
"64Oc6cUvFdYGx2k3+uPgF0rY0Rc3NGj1+W4FMX7jl1R5PjVLlCis4orVetWpXVQw6wG5z2UN" +
"gq//pHy+6/ZyQggWZ2VNTgloquo2j3+j60Nfsj+PU0hQeQ+vPvf81Ahxi80WPLdzt3bQNaNW" +
"zSgInnRPGLRbtKaJ8T+FkbAYObqt5ccAympp7Lz4iiM/50RC6q8YAHRDXhDMfCsHSUJOQeuZ" +
"RaNju3raA2c1LJKc13VQarBq5cjK7atD7gLAKzG3x9R1WqYR130lAEDhBUNg0e/XTuy7SSpm" +
"5KdLHXafbnHPDAaQ9RoLWfh1swy74hlXf4yklsDeKWn4lnE/8MZ/MAKRM/T7OT148ODhmfM3" +
"b4ogByEpKFQAAAAASUVORK5CYII=")

#get RMXP data
require './data'
require './arc_data_dump'
require './extras'


class RMXPProjectFileDropTarget < Wx::FileDropTarget
  def initialize(droplist)
    super()
    @list = droplist
  end
  
  # This method is overridden to specify what happens when a file is
  # dropped 
  def on_drop_files(x, y, files)
    path = File.basename(files[0])
    ext = File.extname(path)
    if ext == ".rxproj"
        @list.push(files[0])
    end
    true # currently need to return boolean from this method
  end
end

class ConverterFrame < Wx::Frame
  
  def initialize
    super(nil,
      :title => 'RMXP to ARC Project Converter',
      :pos => Wx::DEFAULT_POSITION,
      :size => Wx::Size.new(600, 480)
      )
    #set the fraem icon
    icon = Wx::Icon.new("icon.ico")
    set_icon(icon)
    # set our inital paths
    @rmxp_path = ""
    if (ARGV[0] != nil)
      path = File.basename(ARGV[0])
      ext = File.extname(path)
      if ext == ".rxproj"
        @rmxp_path = ARGV[0]
      end
    end
    @arc_path = find_next_project_folder(File.expand_path(File.join(Dir.home, "Documents", "ARC")))
    @project_title = ""
    @convertionrunning = false
    @copyresourcefiles = true
    @log = ""
    @graphicscopyed = false
    @audiocopyed = false
    @errors = false
    @droplist = []

    # create the panel
    @panel = Wx::Panel.new(self)
    
    #setup the file drop target
    
    file_drop_target = RMXPProjectFileDropTarget.new(@droplist)
    @panel.set_drop_target(file_drop_target)
    
    # create the layout

    #create sizers
    @panel_sizer = Wx::BoxSizer.new(Wx::VERTICAL)
    @rmxp_project_sizer = Wx::BoxSizer.new(Wx::HORIZONTAL)
    @arc_project_sizer = Wx::BoxSizer.new(Wx::HORIZONTAL)

    #get project location
    @rmxp_box_sizer = Wx::StaticBoxSizer.new(Wx::VERTICAL, @panel, "RMXP Project to Convert")
    @project_location_tb = Wx::TextCtrl.new(@panel, -1, "")
    @project_location_bt = Wx::Button.new(@panel, -1, "Browse")

    #get project create location
    @arc_box_sizer = Wx::StaticBoxSizer.new(Wx::VERTICAL, @panel, "Location to Save ARC Project")
    @arc_project_location_tb = Wx::TextCtrl.new(@panel, -1, "")
    @arc_project_location_bt = Wx::Button.new(@panel, -1, "Browse")

    #run button
    @converter_box_sizer = Wx::StaticBoxSizer.new(Wx::HORIZONTAL, @panel, "Convert Project")
    @copy_resources_cb = Wx::CheckBox.new(@panel, -1,  "Copy Grapics and Audio to Arc project folder")
    @copy_resources_cb.set_value(true)
    @run_convertion_bt = Wx::Button.new(@panel, -1, "Run Converter")


    #output
    @output_tb = Wx::TextCtrl.new(@panel, -1, "", Wx::DEFAULT_POSITION, Wx::DEFAULT_SIZE,
      Wx::TE_READONLY|Wx::TE_MULTILINE|Wx::TE_WORDWRAP)
        
    #reset button
    @reset_bt = Wx::Button.new(@panel, -1, "Reset")
    
    # add to sizers
    @rmxp_project_sizer.add(@project_location_tb, 2, Wx::GROW|Wx::ALL, 2)
    @rmxp_project_sizer.add(@project_location_bt, 0, Wx::GROW|Wx::ALL, 2)
    @rmxp_box_sizer.add(@rmxp_project_sizer, 0, Wx::GROW|Wx::ALL, 2)
    @arc_project_sizer.add(@arc_project_location_tb, 2, Wx::GROW|Wx::ALL, 2)
    @arc_project_sizer.add(@arc_project_location_bt, 0, Wx::GROW|Wx::ALL, 2)
    @arc_box_sizer.add(@arc_project_sizer, 0, Wx::GROW|Wx::ALL, 2)
    @converter_box_sizer.add(@copy_resources_cb, 0, Wx::GROW|Wx::ALL, 2)
    @converter_box_sizer.add(@run_convertion_bt, 1, Wx::GROW|Wx::ALL, 2)
    @converter_box_sizer.add(@reset_bt, 0, Wx::ALL|Wx::GROW, 2)
    @panel_sizer.add(@rmxp_box_sizer, 0, Wx::GROW|Wx::ALL, 2)
    @panel_sizer.add(@arc_box_sizer, 0, Wx::GROW|Wx::ALL, 2)
    @panel_sizer.add(@converter_box_sizer, 0, Wx::GROW|Wx::ALL, 2)
    @panel_sizer.add(@output_tb, 1, Wx::GROW|Wx::ALL|Wx::EXPAND, 2)

    #set the frame sizer
    @panel.set_sizer(@panel_sizer)

    #set up events
    #button events
    evt_button(@project_location_bt.get_id) {|event| rmxpFileBrowse(event)}
    evt_button(@arc_project_location_bt.get_id) {|event| arcFileBrowse(event)}
    evt_button(@run_convertion_bt.get_id) {|event| runConverter(event)}
    evt_button(@reset_bt.get_id) {|event| restButtonClick(event)}
      
    #text events
    evt_text(@project_location_tb.get_id) {|event| textEventprojectLocationTB(event)}
    evt_text(@arc_project_location_tb.get_id) {|event| textEventarcprojectLocationTB(event)}
        
    #update ui events
    evt_update_ui(@project_location_tb.get_id) {|event| projectLocationTBUpdate(event)}
    evt_update_ui(@arc_project_location_tb.get_id) {|event| arcprojectLocationTBUpdate(event)}
    evt_update_ui(@copy_resources_cb.get_id) {|event| copyResoucesCBUpdate(event)} 
      
    #cb events
    evt_checkbox(@copy_resources_cb.get_id) {|event| copyResourcesCBChecked(event)}
        
    #show the frame
    show
  end
  
  def reset
    @rmxp_path = ""
    @arc_path = find_next_project_folder(File.expand_path(File.join(Dir.home, "Documents", "ARC")))
    @project_title = ""
    @convertionrunning = false
    @convertionfinushed = false
    @copyresourcefiles = true
    @log = ""
    @output_tb.set_value(@log)
    @graphicscopyed = false
    @audiocopyed = false
    @errors = false
  end
  
  def restButtonClick(event)
    if @convertionrunning && @convertionfinushed
      reset
    end
  end
  
  def log(text)
    @log << text << "\n"
    @output_tb.set_value(@log)
    @output_tb.set_insertion_point_end
    Wx::get_app.yield(true)
  end
  
  def rmxpFileBrowse(event)
    if !@convertionrunning
      filetypes = "RMXP Project files (*.rxproj)|*.rxproj"
      if @project_location_tb.get_value == ""
        defaultDir = File.expand_path(File.join(Dir.home, "Documents", "RPGXP"))
        defaultFile = ""
      else
        names = File.split(@project_location_tb.get_value)
        defaultDir = names[0]
        defaultfile = names[1]
      end
        fileDialog = Wx::FileDialog.new(self, "Select a RMXP project file", defaultDir,
        defaultFile, filetypes,  Wx::OPEN|Wx::FILE_MUST_EXIST)
      case fileDialog.show_modal()
      when Wx::ID_OK
        @rmxp_path = File.join(fileDialog.get_directory, fileDialog.get_filename)
      end
    end
  end
  
  def arcFileBrowse(event)
    if !@convertionrunning
      defaultDir = @arc_project_location_tb.get_value
      dirDialog = Wx::DirDialog.new(self,  "Choose a directory to save the new ARC project in", 
      defaultDir, Wx::DD_DEFAULT_STYLE)
      case dirDialog.show_modal()
      when Wx::ID_OK
        @arc_path = dirDialog.get_path
      end
    end
  end
  
  def textEventprojectLocationTB(event)
    if @rmxp_path != @project_location_tb.get_value
      @rmxp_path = @project_location_tb.get_value
    end
  end
  
  def textEventarcprojectLocationTB(event)  
    if @arc_path != @arc_project_location_tb.get_value
      @arc_path = @arc_project_location_tb.get_value
    end
  end
  
  def projectLocationTBUpdate(event)
    if !@droplist.empty?
      if File.exists?(@droplist[0])
        @rmxp_path = @droplist[0]
      end
      @droplist.clear 
    end
    if @project_location_tb.get_value != @rmxp_path
      @project_location_tb.set_value(@rmxp_path)
    end
  end
  
  def arcprojectLocationTBUpdate(event)
    if @arc_project_location_tb.get_value != @arc_path
      @arc_project_location_tb.set_value(@arc_path)
    end
  end
  
  def copyResoucesCBUpdate(event)
    if @copy_resources_cb.get_value != @copyresourcefiles
      @copy_resources_cb.set_value(@copyresourcefiles)
    end
  end
  
  def copyResourcesCBChecked(event)
    @copyresourcefiles = @copy_resources_cb.get_value
  end
  
  def find_next_project_folder(path)
    foundDir = false
    dirname = "Project"
    startnum = 0
    while !foundDir
      startnum += 1
      dername = "Project" + startnum.to_s
      pathtocheck = File.join(path, dername)
      if !File.exists?(pathtocheck)
        foundDir = true
        dirname = dername
      end
    end
    return File.join(path, dirname)
  end
  
  def make_path(path)
    FileUtils.mkdir_p(path)
  end
  
  def runConverter(event)
    if File.exists?(@rmxp_path) && !@convertionrunning
      do_convertion
    end
  end
  
  def load_data(filename)
    f = open(filename, 'rb')
    data = Marshal.load(f)
    f.close()
    return data
  end
  
  def arc_load_data(filename)
    f = open(filename, 'rb')
    data = ARC::Data.load(f)
    f.close()
    return data
  end
  
  def dump_data(filename, data)
    f = open(filename, 'wb')
    Marshal.dump(data, f)
    f.close()
  end
  
  def arc_dump_data(filename, data)
    f = open(filename, 'wb')
    ARC::Data.dump(f, data)
    f.close()
  end
  
  def convert_file(rmxp_path, arc_path, name)
    rmxp_name = File.join(rmxp_path, "Data",  name) + ".rxdata"
    arc_name = File.join(arc_path, "Data", name) + ".arc"
    log("        - Converting #{rmxp_name} to #{arc_name} ...")
    begin
      make_path(File.dirname(rmxp_name))
      data = load_data(rmxp_name)
      make_path(File.dirname(arc_name))
      arc_dump_data(arc_name, data)
      return data
    rescue
      log("Error converting #{name} data: #{$!.message}")
      backtrace = $!.backtrace.join("\n").gsub(Dir.getwd){'.'}
      log("Backtrace: #{backtrace}")
      @errors = true
      return nil
    end
  end
  
  def writeARCProjectFile(arc_path, title)
    begin
      filename = File.join(arc_path, title.gsub(/[\x00\/\\:\*\?\"<>\|]/, '_')) + ".arcproj"
      arc_ini = Ini.new(filename)
      arc_ini["Project"] = {"Title" => title}
      arc_ini["Files"] =  {"list" => "Actors|Classes|Skills|Items|Weapons|Armors|Enemies|Troops|States|Animations|Tilesets|CommonEvents|System|MapInfos"}
      arc_ini.update
      cfgfile = File.new(File.join(arc_path, "arc.cfg"), "wb")
      cfgfile.write("Title:#{title}\n")
      cfgfile.write("Resolution:640x480\n")
      cfgfile.write("Fullscreen:false\n")
      cfgfile.write("FrameRate:40\n")
      cfgfile.write("InactiveAudio:false\n")
      cfgfile.write("FontBaseSize:48\n")
      cfgfile.write("GameVersion:1.0.0\n")
      cfgfile.close
    rescue
      log("Error writing project file: #{$!.message}")
      backtrace = $!.backtrace.join("\n").gsub(Dir.getwd){'.'}
      log("Backtrace: #{backtrace}")
      @errors = true
    end
  end
  
  def writeARCExtras(arc_path)
    begin
      ARC_EXTRA_INCLUDES::EXTRAS.each {|extra|
        filename = File.join(arc_path, extra[0])
        f = File.new(filename, "wb")
        f.write(extra[1])
        f.close
      }
    rescue
      log("Error writing extra project files: #{$!.message}")
      backtrace = $!.backtrace.join("\n").gsub(Dir.getwd){'.'}
      log("Backtrace: #{backtrace}")
      @errors = true
    end
  end
  
  def copyresourcefiles(rmxp_path, arc_path)
    begin
      if File.directory?(File.join(rmxp_path, "Graphics"))
        log("        - Copying Graphics folder to #{File.join(arc_path, "Graphics")}")
        FileUtils.cp_r(File.join(rmxp_path, "Graphics"), File.join(arc_path, "Graphics"))
        @graphicscopyed  = true
      else
        log("        - No Graphics folder found in the RMXP project folder")
      end
    rescue
      log("Error copying Graphics folder: #{$!.message}")
      backtrace = $!.backtrace.join("\n").gsub(Dir.getwd){'.'}
      log("Backtrace: #{backtrace}")
      @errors = true
    end
    begin
      if File.directory?(File.join(rmxp_path, "Audio"))
        log("        - Copying Audio folder to #{File.join(arc_path, "Audio")}")
        FileUtils.cp_r(File.join(rmxp_path, "Audio"), File.join(arc_path, "Audio"))
        @audiocopyed = true
      else
        log("        - No Audio folder found in the RMXP project folder")
      end
    rescue
      log("Error copying Audio folder: #{$!.message}")
      backtrace = $!.backtrace.join("\n").gsub(Dir.getwd){'.'}
      log("Backtrace: #{backtrace}")
      @errors = true
    end
  end
  
  def write_script(path, script)
    f = open(path, 'wb')
    f.write("\xef\xbb\xbf") 
    f.write(script.force_encoding("UTF-8")) 
    f.close
  end
  
  def convert_scripts(rmxp_path, arc_path)
    rmxp_name = File.join(rmxp_path, "Data",  "Scripts") + ".rxdata"
    scripts_folder = File.join(arc_path, "Data", "Scripts")
    log("------------ Converting RMXP Scripts ------------")
    replacements = [['"Save#{@file_index + 1}.rxdata"', '"Save#{@file_index + 1}.dat"'],
                    ['"Save#{i+1}.rxdata"', '"Save#{i+1}.dat"'],
                    ['"Save#{file_index + 1}.rxdata"', '"Save#{file_index + 1}.dat"'],
                    ['load_data(sprintf("Data/Map%03d.rxdata"', 'ARC::Data::load(sprintf("Data/Map%03d.arc"'],
                    ['load_data("Data/Actors.rxdata")', 'ARC::Data::load("Data/Actors.arc")'],
                    ['load_data("Data/Classes.rxdata")', 'ARC::Data::load("Data/Classes.arc")'],
                    ['load_data("Data/Skills.rxdata")', 'ARC::Data::load("Data/Skills.arc")'],
                    ['load_data("Data/Items.rxdata")', 'ARC::Data::load("Data/Items.arc")'],
                    ['load_data("Data/Weapons.rxdata")', 'ARC::Data::load("Data/Weapons.arc")'],
                    ['load_data("Data/Armors.rxdata")', 'ARC::Data::load("Data/Armors.arc")'],
                    ['load_data("Data/Enemies.rxdata")', 'ARC::Data::load("Data/Enemies.arc")'],
                    ['load_data("Data/Troops.rxdata")', 'ARC::Data::load("Data/Troops.arc")'],
                    ['load_data("Data/States.rxdata")', 'ARC::Data::load("Data/States.arc")'],
                    ['load_data("Data/Animations.rxdata")', 'ARC::Data::load("Data/Animations.arc")'],
                    ['load_data("Data/Tilesets.rxdata")', 'ARC::Data::load("Data/Tilesets.arc")'],
                    ['load_data("Data/CommonEvents.rxdata")', 'ARC::Data::load("Data/CommonEvents.arc")'],
                    ['load_data("Data/System.rxdata")', 'ARC::Data::load("Data/System.arc")'],
                    ['load_data("Data/BT_Actors.rxdata")', 'ARC::Data::load("Data/BT_Actors.arc")'],
                    ['load_data("Data/BT_Classes.rxdata")', 'ARC::Data::load("Data/BT_Classes.arc")'],
                    ['load_data("Data/BT_Skills.rxdata")', 'ARC::Data::load("Data/BT_Skills.arc")'],
                    ['load_data("Data/BT_Items.rxdata")', 'ARC::Data::load("Data/BT_Items.arc")'],
                    ['load_data("Data/BT_Weapons.rxdata")', 'ARC::Data::load("Data/BT_Weapons.arc")'],
                    ['load_data("Data/BT_Armors.rxdata")', 'ARC::Data::load("Data/BT_Armors.arc")'],
                    ['load_data("Data/BT_Enemies.rxdata")', 'ARC::Data::load("Data/BT_Enemies.arc")'],
                    ['load_data("Data/BT_Troops.rxdata")', 'ARC::Data::load("Data/BT_Troops.arc")'],
                    ['load_data("Data/BT_States.rxdata")', 'ARC::Data::load("Data/BT_States.arc")'],
                    ['load_data("Data/BT_Animations.rxdata")', 'ARC::Data::load("Data/BT_Animations.arc")'],
                    ['load_data("Data/BT_Tilesets.rxdata")', 'ARC::Data::load("Data/BT_Tilesets.arc")'],
                    ['load_data("Data/BT_CommonEvents.rxdata")', 'ARC::Data::load("Data/BT_CommonEvents.arc")'],
                    ['load_data("Data/BT_System.rxdata")', 'ARC::Data::load("Data/BT_System.arc")'],
                    ['load_data("Data/MapInfos.rxdata")', 'ARC::Data.load("Data/MapInfos.arc")']]    
    begin
      scripts = load_data(rmxp_name)
      make_path(scripts_folder)
      i = 0
      for script in scripts
        script_name = "%04d" % i
        name = script[1]
        name.force_encoding("US-ASCII")
        script_name += "-#{name.gsub(/[\x00\/\\:\*\?\"<>\|]/, '_').gsub(/[\n\r]/, '')}"
        script_file_path = File.join(scripts_folder, script_name) + ".rb"
        log("        - Writing #{script_file_path} ...")
        #fix some rmxp lines
        text = Zlib::Inflate.inflate(script[2]) 
        replacements.each {|replacement|
          text.gsub!(replacement[0], replacement[1])
        }
        write_script(script_file_path, text)   
        i += 1
      end
    rescue
      log("Error converting scripts: #{$!.message}")
      backtrace = $!.backtrace.join("\n").gsub(Dir.getwd){'.'}
      log("Backtrace: #{backtrace}")
      @errors = true
    end
  end
  
  def do_convertion
    @convertionrunning = true
    @log = ""
    rmxp_dir, rmxp_projectfile = File.split(@rmxp_path)
    log("===============================================")
    log("Beginning convertion on RMXP project located at #{rmxp_dir}")
    log("===============================================")
    log("------------Converting Data files -------------")
    rmxp_ini = Ini.new(File.join(rmxp_dir, "Game.ini"))
    project_title = rmxp_ini["Game"]["Title"]
    convert_file(rmxp_dir, @arc_path, "Actors")
    convert_file(rmxp_dir, @arc_path, "Classes")
    convert_file(rmxp_dir, @arc_path, "Skills")
    convert_file(rmxp_dir, @arc_path, "Items")
    convert_file(rmxp_dir, @arc_path, "Weapons")
    convert_file(rmxp_dir, @arc_path, "Armors")
    convert_file(rmxp_dir, @arc_path, "Enemies")
    convert_file(rmxp_dir, @arc_path, "Troops")
    convert_file(rmxp_dir, @arc_path, "States")
    convert_file(rmxp_dir, @arc_path, "Animations")
    convert_file(rmxp_dir, @arc_path, "Tilesets")
    convert_file(rmxp_dir, @arc_path, "CommonEvents")
    convert_file(rmxp_dir, @arc_path, "System")
    map_infos = convert_file(rmxp_dir, @arc_path, "MapInfos")
    log("------------Converting Maps -------------")
    for key in map_infos.keys
      convert_file(rmxp_dir, @arc_path, "Map%03d" % key)
    end
    convert_scripts(rmxp_dir, @arc_path)
    if @copyresourcefiles
      log("--------- Copying resource files -----------------")
      copyresourcefiles(rmxp_dir, @arc_path)
    end
    log("--------- Writing extra files files -----------------")
    log("        - Writing system files")
    writeARCExtras(@arc_path)
    log("        - Writing project file")
    writeARCProjectFile(@arc_path, project_title)
    log("============== Convertion Finished =================")
    display_end_message
  end
  
  def display_end_message
    if @errors
      message = "There were errors converting the project. \n Please see the log for messages and backtraces"
      dialog = Wx::MessageDialog.new(self, message, 
        "Errors Converting Project", 
        Wx::ICON_ERROR|Wx::OK|Wx::STAY_ON_TOP)
      dialog.show_modal
    else
      message = "The project was converted successfully. \n"
      if @copyresourcefiles
        if @graphicscopyed && @audiocopyed
          message += "The Graphics and Audio folders in the project folder were copied \n to the ARC project folder"
        elsif @graphicscopyed
          message += "The Graphics folder in the project folder was copied \n to the ARC project folder. The Audio folder was not found."
        elsif @audiocopyed
          message += "The Audio folder in the project folder was copied \n to the ARC project folder. The Graphics folder was not found."
        else
          message += "The Graphics and Audio folders were not found in the \n RMXP project folder and were not copied"
        end
      end
      message += "\n\nIf you would like to convert another project press the reset button"
      dialog = Wx::MessageDialog.new(self, message, 
        "Project Successfully Converted", 
        Wx::ICON_INFORMATION|Wx::OK|Wx::STAY_ON_TOP)
      dialog.show_modal
    end
    @convertionfinushed = true
  end
  
end

class ConverterApp < Wx::App
    def on_init
        ConverterFrame.new
    end
end

app = ConverterApp.new
if not defined?(Ocra)
  app.main_loop
end

