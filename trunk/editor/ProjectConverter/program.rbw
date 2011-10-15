# Wx frame based RMXP to ARC Project Converter

#get WX
require "wx"

Dir.chdir(File.dirname(__FILE__)) 

require "./ini_file"

#get RMXP data
require './data'
require './arc_data_dump'

class LogEvent < Wx::CommandEvent
  EVT_CONVERTER_LOG = Wx::EvtHandler.register_class(self, nil, "evt_converter_log", 1)
  
  def initialize(ctrl, message)
    # The constant id is the arg to super
    super(EVT_CONVERTER_LOG)
    # client_data should be used to store any information associated
    # with the event.
    self.client_data = { :message => message  }
    self.id = ctrl.get_id
  end
  
  def message
    client_data[:message]
  end

end

class ConverterFrame < Wx::Frame
  
  def initialize
    super(nil,
      :title => 'RMXP to ARC Project Converter',
      :pos => Wx::DEFAULT_POSITION,
      :size => Wx::Size.new(600, 480)
      )
    #set our inital paths
    @rmxp_path = ""
    @arc_path = find_next_project_folder(File.expand_path(File.join(Dir.home, "Documents", "ARC")))
    @project_title = ""
    
    # create the panel
    @panel = Wx::Panel.new(self)
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
    @run_convertion_bt = Wx::Button.new(@panel, -1, "Run Converter")
    
    #output
    @output_tb = Wx::TextCtrl.new(@panel, -1, "", Wx::DEFAULT_POSITION, Wx::DEFAULT_SIZE,
      Wx::TE_READONLY|Wx::TE_MULTILINE|Wx::TE_WORDWRAP)
    
    # add to sizers
    @rmxp_project_sizer.add(@project_location_tb, 2, Wx::GROW|Wx::ALL, 2)
    @rmxp_project_sizer.add(@project_location_bt, 0, Wx::GROW|Wx::ALL, 2)
    @rmxp_box_sizer.add(@rmxp_project_sizer, 0, Wx::GROW|Wx::ALL, 2)
    @arc_project_sizer.add(@arc_project_location_tb, 2, Wx::GROW|Wx::ALL, 2)
    @arc_project_sizer.add(@arc_project_location_bt, 0, Wx::GROW|Wx::ALL, 2)
    @arc_box_sizer.add(@arc_project_sizer, 0, Wx::GROW|Wx::ALL, 2)
    @panel_sizer.add(@rmxp_box_sizer, 0, Wx::GROW|Wx::ALL, 2)
    @panel_sizer.add(@arc_box_sizer, 0, Wx::GROW|Wx::ALL, 2)
    @panel_sizer.add(@run_convertion_bt, 0, Wx::GROW|Wx::ALL, 2)
    @panel_sizer.add(@output_tb, 1, Wx::GROW|Wx::ALL|Wx::EXPAND, 2)
   
    #set the frame sizer
    @panel.set_sizer(@panel_sizer)
     
    #p Wx::StandardPaths.get_config_dir
    #p Wx::StandardPaths.get_data_dir
    #p Wx::StandardPaths.get_local_data_dir
    #p Wx::StandardPaths.get_plugins_dir
    #p Wx::StandardPaths.get_user_config_dir
    #p Wx::StandardPaths.get_user_data_dir
    #p Wx::StandardPaths.get_user_local_data_dir
    
    #set up events
    #button events
    evt_button(@project_location_bt.get_id) {|event| rmxpFileBrowse(event)}
    evt_button(@arc_project_location_bt.get_id) {|event| arcFileBrowse(event)}
    evt_button(@run_convertion_bt.get_id) {|event| runConverter(event)}
      
    #text events
    evt_text(@project_location_tb.get_id) {|event| textEventprojectLocationTB(event)}
    evt_text(@arc_project_location_tb.get_id) {|event| textEventarcprojectLocationTB(event)}
        
    #update ui events
    evt_update_ui(@project_location_tb.get_id) {|event| projectLocationTBUpdate(event)}
    evt_update_ui(@arc_project_location_tb.get_id) {|event| arcprojectLocationTBUpdate(event)}
    
    #log event
    evt_converter_log(self.get_id) {|event| write_to_log(event)}
      
    #show the frame
    show
    
  end
  
  def rmxpFileBrowse(event)
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
  
  def arcFileBrowse(event)
    defaultDir = @arc_project_location_tb.get_value
    dirDialog = Wx::DirDialog.new(self,  "Choose a directory to save the new ARC project in", 
    defaultDir, Wx::DD_DEFAULT_STYLE)
    case dirDialog.show_modal()
    when Wx::ID_OK
      @arc_path = dirDialog.get_path
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
    if @project_location_tb.get_value != @rmxp_path
      @project_location_tb.set_value(@rmxp_path)
    end
  end
  
  def arcprojectLocationTBUpdate(event)
    if @arc_project_location_tb.get_value != @arc_path
      @arc_project_location_tb.set_value(@arc_path)
    end
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
    pathn = path.dup
    folders_to_create = []
    loop do
      if !File.exists?(pathn)
        names = File.split(pathn)
        pathn = names[0]
        folders_to_create.push(names[1])
      else
        break
      end
    end
    while !folders_to_create.empty?
      pathn = File.join(pathn, folders_to_create.pop)
      Dir.mkdir(pathn)
    end
  end
  
  def runConverter(event)
    do_convertion
  end
  
  def log(text)
    evt = LogEvent.new(self, text)
    event_handler.process_event(evt)
  end
  
  def write_to_log(event)
    s = @output_tb.get_value
    s << event.message << "\n"
    @output_tb.set_value(s)
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
    log("- Converting #{rmxp_name} to #{arc_name} ...")
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
      return nil
    end
  end
  
  def writeARCProjectFile(arc_path, title)
    filename = File.join(arc_path, title.gsub(/[\x00\/\\:\*\?\"<>\|]/, '_')) + ".arcproj"
    arc_ini = Ini.new(filename)
    arc_ini["Project"] = {"Title" => title}
    arc_ini["Files"] =  {"list" => "Troops|Skills|Items|System|Weapons|Armors|Classes|Actors|Tilesets|CommonEvents|MapInfos"}
    arc_ini.update
  end
  
  def do_convertion
    rmxp_dir, rmxp_projectfile = File.split(@rmxp_path)
    log("Beginning convertion on RMXP project located at #{rmxp_dir}")
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
    unless map_infos == nil
      log("--Converting Maps--")
      for key in map_infos.keys
        convert_file(rmxp_dir, @arc_path, "Map%03d" % key)
      end
    end
    log("- Writing project file")
    writeARCProjectFile(@arc_path, project_title)
    log("Convertion Finished")
  end
  
end

class ConverterApp < Wx::App
  def on_init
    ConverterFrame.new
  end
end

ConverterApp.new.main_loop

