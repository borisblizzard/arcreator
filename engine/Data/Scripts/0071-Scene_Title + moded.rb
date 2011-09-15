#==============================================================================
# ** Scene_Title
#------------------------------------------------------------------------------
#  This class performs title screen processing.
#==============================================================================

class Scene_Title
  
  #--------------------------------------------------------------------------
  # * Main Processing
  #--------------------------------------------------------------------------
  def main
    # If battle test
    if $BTEST
      battle_test
      return
    end
    # add some extras
    @mask = Sprite.new
    @mask.bitmap = RPG::Cache.title("logo_mask")
    @mask.z = 100
    @glow = Sprite.new
    @glow.bitmap = RPG::Cache.title("glow")
    @glow.z = 50
    @glow.x = -160
    @ver = Sprite.new
    @ver.bitmap = Bitmap.new(160, 32)
    @ver.bitmap.font.name = "Arial"
    @ver.bitmap.font.size = 18
    @ver.bitmap.font.color.set(0, 96, 255)
    @ver.bitmap.font.bold = true
    ver = (BlizzABS::VERSION * 1000 + 0.1).to_i
    ver = "Version #{ver/1000%10}.#{ver/100%10}.#{ver/10%10}.#{ver%10}"
    @ver.bitmap.draw_text(0, 0, 160, 32, ver, 1)
    @ver.x = 240
    @ver.y = 200
    @ver.z = 150
    @count = false
    # Load database
    $data_actors        = load_data("Data/Actors.rxdata")
    $data_classes       = load_data("Data/Classes.rxdata")
    $data_skills        = load_data("Data/Skills.rxdata")
    $data_items         = load_data("Data/Items.rxdata")
    $data_weapons       = load_data("Data/Weapons.rxdata")
    $data_armors        = load_data("Data/Armors.rxdata")
    $data_enemies       = load_data("Data/Enemies.rxdata")
    $data_troops        = load_data("Data/Troops.rxdata")
    $data_states        = load_data("Data/States.rxdata")
    $data_animations    = load_data("Data/Animations.rxdata")
    $data_tilesets      = load_data("Data/Tilesets.rxdata")
    $data_common_events = load_data("Data/CommonEvents.rxdata")
    $data_system        = load_data("Data/System.rxdata")
    # Make system object
    $game_system = Game_System.new
    # Make title graphic
    @sprite = Sprite.new
    @sprite.bitmap = RPG::Cache.title($data_system.title_name)
    # Make command window
    commands1 = ["Run Blizz-ABS #{ver}", 'Resume', 'Quit']
    commands2 = ['Chronicles of Sir Lag-A-Lot', 'Back to Main Menu']
    @command_window = Window_Command.new(352, commands1)
    @command_window.back_opacity = 160
    @command_window.x = 320 - @command_window.width / 2
    @command_window.y = 320 - @command_window.height / 2
    @command_window2 = Window_Command.new(320, commands2)
    @command_window2.back_opacity = 160
    @command_window2.x = 320 - @command_window2.width / 2
    @command_window2.y = 320 - @command_window2.height / 2
    @command_window2.active = @command_window2.visible = false
    # Continue enabled determinant
    # Check if at least one save file exists
    # If enabled, make @continue_enabled true; if disabled, make it false
    @continue_enabled = false
    for i in 0..3
      @continue_enabled = true if FileTest.exist?("Save#{i+1}.rxdata")
    end
    # If continue is enabled, move cursor to "Continue"
    # If disabled, display "Continue" text in gray
    if @continue_enabled
      @command_window.index = 1
    else
      @command_window.disable_item(1)
    end
    # Play title BGM
    $game_system.bgm_play($data_system.title_bgm)
    # Stop playing ME and BGS
    Audio.me_stop
    Audio.bgs_stop
    # Execute transition
    Graphics.transition
    # Main loop
    loop do
      # Update game screen
      Graphics.update
      # Update input information
      Input.update
      # Frame update
      update
      # Abort loop if screen is changed
      break if $scene != self
    end
    # Prepare for transition
    Graphics.freeze
    # Dispose of command window
    @command_window.dispose
    @command_window2.dispose
    # Dispose of title graphic
    @sprite.bitmap.dispose
    @sprite.dispose
    # dispose the extras
    @mask.dispose
    @glow.dispose
    @ver.dispose
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # is it time to update the glow
    if (Graphics.frame_count + 100) % 150 == 0 or @count
      # move glowing frame
      @glow.x += 50
      # still glowing
      @count = (@glow.x < 640)
    else
      # reset glow position
      @glow.x = -160
    end
    # Update command window
    @command_window.update if @command_window.active
    @command_window2.update if @command_window2.active
    # If C button was pressed
    if Input.trigger?(Input::B)
      if @command_window.active
        $game_system.se_play($data_system.buzzer_se)
      elsif @command_window2.active
        $game_system.se_play($data_system.cancel_se)
        @command_window.active = @command_window.visible = true
        @command_window2.active = @command_window2.visible = false
      end
    end
    if Input.trigger?(Input::C)
      if @command_window.active
        case @command_window.index
        when 0  # Next window
          $game_system.se_play($data_system.decision_se)
          @command_window.active = @command_window.visible = false
          @command_window2.active = @command_window2.visible = true
        when 1  # Continue
          command_continue
        when 2  # Shutdown
          command_shutdown
        end
      elsif @command_window2.active
      # Branch by command window cursor position
        case @command_window2.index
        when 0  # Start game 1
          command_start_lag_a_lot
        when 1  # Back to Main Menu
          $game_system.se_play($data_system.decision_se)
          @command_window2.index = 0
          @command_window.active = @command_window.visible = true
          @command_window2.active = @command_window2.visible = false
        end
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Command: Start Game "Chronicles of Sir Lag-A-Lot"
  #--------------------------------------------------------------------------
  def command_start_lag_a_lot
    # basic game initialization
    command_init_game
    # Switch to intro screen
    $scene = Scene_StormTronics.new(1)
  end
  #--------------------------------------------------------------------------
  # * Command: Initialize Game
  #--------------------------------------------------------------------------
  def command_init_game
    # Play decision SE
    $game_system.se_play($data_system.decision_se)
    # Stop BGM
    Audio.bgm_stop
    # Reset frame count for measuring play time
    Graphics.frame_count = 0
    # Make each type of game object
    $game_temp          = Game_Temp.new
    $game_system        = Game_System.new
    $game_switches      = Game_Switches.new
    $game_variables     = Game_Variables.new
    $game_self_switches = Game_SelfSwitches.new
    $game_screen        = Game_Screen.new
    $game_actors        = Game_Actors.new
    $game_party         = Game_Party.new
    $game_troop         = Game_Troop.new
    $game_map           = Game_Map.new
    $game_player        = Game_Player.new
  end
  #--------------------------------------------------------------------------
  # * Command: Continue
  #--------------------------------------------------------------------------
  def command_continue
    # If continue is disabled
    unless @continue_enabled
      # Play buzzer SE
      $game_system.se_play($data_system.buzzer_se)
      return
    end
    # Play decision SE
    $game_system.se_play($data_system.decision_se)
    # Switch to load screen
    $scene = Scene_Load.new
  end
  #--------------------------------------------------------------------------
  # * Command: Shutdown
  #--------------------------------------------------------------------------
  def command_shutdown
    # Play decision SE
    $game_system.se_play($data_system.decision_se)
    # Fade out BGM, BGS, and ME
    Audio.bgm_fade(800)
    Audio.bgs_fade(800)
    Audio.me_fade(800)
    # Shutdown
    $scene = nil
  end
  #--------------------------------------------------------------------------
  # * Battle Test
  #--------------------------------------------------------------------------
  def battle_test
    # Load database (for battle test)
    $data_actors        = load_data("Data/BT_Actors.rxdata")
    $data_classes       = load_data("Data/BT_Classes.rxdata")
    $data_skills        = load_data("Data/BT_Skills.rxdata")
    $data_items         = load_data("Data/BT_Items.rxdata")
    $data_weapons       = load_data("Data/BT_Weapons.rxdata")
    $data_armors        = load_data("Data/BT_Armors.rxdata")
    $data_enemies       = load_data("Data/BT_Enemies.rxdata")
    $data_troops        = load_data("Data/BT_Troops.rxdata")
    $data_states        = load_data("Data/BT_States.rxdata")
    $data_animations    = load_data("Data/BT_Animations.rxdata")
    $data_tilesets      = load_data("Data/BT_Tilesets.rxdata")
    $data_common_events = load_data("Data/BT_CommonEvents.rxdata")
    $data_system        = load_data("Data/BT_System.rxdata")
    # Reset frame count for measuring play time
    Graphics.frame_count = 0
    # Make each game object
    $game_temp          = Game_Temp.new
    $game_system        = Game_System.new
    $game_switches      = Game_Switches.new
    $game_variables     = Game_Variables.new
    $game_self_switches = Game_SelfSwitches.new
    $game_screen        = Game_Screen.new
    $game_actors        = Game_Actors.new
    $game_party         = Game_Party.new
    $game_troop         = Game_Troop.new
    $game_map           = Game_Map.new
    $game_player        = Game_Player.new
    # Set up party for battle test
    $game_party.setup_battle_test_members
    # Set troop ID, can escape flag, and battleback
    $game_temp.battle_troop_id = $data_system.test_troop_id
    $game_temp.battle_can_escape = true
    $game_map.battleback_name = $data_system.battleback_name
    # Play battle start SE
    $game_system.se_play($data_system.battle_start_se)
    # Play battle BGM
    $game_system.bgm_play($game_system.battle_bgm)
    # Switch to battle screen
    $scene = Scene_Battle.new
  end
  
end
