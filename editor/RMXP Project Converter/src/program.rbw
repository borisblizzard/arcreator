# Wx frame based RMXP to ARC Project Converter

#get WX
require "wx"
require "fileutils"
require "zlib"

Dir.chdir(File.dirname(__FILE__)) 

require "./ini_file"

#get RMXP data
require './data'
require './arc_data_dump'


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
        @convertionrunning = false
        @convertionfinushed = false
        @copyresourcefiles = true
        @log = ""
        @graphicscopyed = false
        @audiocopyed = false
        @errors = false



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
            arc_ini["Files"] =  {"list" => "Troops|Skills|Items|System|Weapons|Armors|Classes|Actors|Tilesets|CommonEvents|MapInfos"}
            arc_ini.update
        rescue
            log("Error writing project file: #{$!.message}")
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
                log("- Copying Audio folder to #{File.join(arc_path, "Audio")}")
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
        f.write(Zlib::Inflate.inflate(script))
        f.close
    end
  
    def convert_scripts(rmxp_path, arc_path)
        rmxp_name = File.join(rmxp_path, "Data",  "Scripts") + ".rxdata"
        scripts_folder = File.join(arc_path, "Data", "Scripts")
        log("------------ Converting RMXP Scripts ------------")
        begin
            scripts = load_data(rmxp_name)
            make_path(scripts_folder)
            i = 0
            for script in scripts
                script_name = "%04d" % i
                script_name += "-#{script[1]}"
                script_file_path = File.join(scripts_folder, script_name) + ".rb"
                log("        - Writing #{script_file_path} ...")
                write_script(script_file_path, script[2])   
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
        log("- Writing project file")
        writeARCProjectFile(@arc_path, project_title)
        if @copyresourcefiles
            log("--------- Copying resource files -----------------")
            copyresourcefiles(rmxp_dir, @arc_path)
        end
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

ConverterApp.new.main_loop

