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
    # Load database
    $data_actors        = ARC::Data::load("Data/Actors.arc")
    $data_classes       = ARC::Data::load("Data/Classes.arc")
    $data_skills        = ARC::Data::load("Data/Skills.arc")
    $data_items         = ARC::Data::load("Data/Items.arc")
    $data_weapons       = ARC::Data::load("Data/Weapons.arc")
    $data_armors        = ARC::Data::load("Data/Armors.arc")
    $data_enemies       = ARC::Data::load("Data/Enemies.arc")
    $data_troops        = ARC::Data::load("Data/Troops.arc")
    $data_states        = ARC::Data::load("Data/States.arc")
    $data_animations    = ARC::Data::load("Data/Animations.arc")
    $data_tilesets      = ARC::Data::load("Data/Tilesets.arc")
    $data_common_events = ARC::Data::load("Data/CommonEvents.arc")
    $data_system        = ARC::Data::load("Data/System.arc")
    # Make system object
    $game_system = Game_System.new
    # Make title graphic
    @sprite = Sprite.new
    @sprite.bitmap = RPG::Cache.title($data_system.title_name)
    # Make command window
    s1 = "New Game"
    s2 = "Continue"
    s3 = "Shutdown"
    @command_window = Window_Command.new(192, [s1, s2, s3])
    @command_window.back_opacity = 160
    @command_window.x = 320 - @command_window.width / 2
    @command_window.y = 288
    # Continue enabled determinant
    # Check if at least one save file exists
    # If enabled, make @continue_enabled true; if disabled, make it false
    @continue_enabled = false
    for i in 0..3
      if FileTest.exist?("Save#{i+1}.arc")
        @continue_enabled = true
      end
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
      if $scene != self
        break
      end
    end
    # Prepare for transition
    Graphics.freeze
    # Dispose of command window
    @command_window.dispose
    # Dispose of title graphic
    @sprite.bitmap.dispose
    @sprite.dispose
  end
  #--------------------------------------------------------------------------
  # * Frame Update
  #--------------------------------------------------------------------------
  def update
    # Update command window
    @command_window.update
    # If C button was pressed
    if Input.trigger?(Input::C)
      # Branch by command window cursor position
      case @command_window.index
      when 0  # New game
        command_new_game
      when 1  # Continue
        command_continue
      when 2  # Shutdown
        command_shutdown
      end
    end
  end
  #--------------------------------------------------------------------------
  # * Command: New Game
  #--------------------------------------------------------------------------
  def command_new_game
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
    # Set up initial party
    $game_party.setup_starting_members
    # Set up initial map position
    $game_map.setup($data_system.start_map_id)
    # Move player to initial position
    $game_player.moveto($data_system.start_x, $data_system.start_y)
    # Refresh player
    $game_player.refresh
    # Run automatic change for BGM and BGS set with map
    $game_map.autoplay
    # Update map (run parallel process event)
    $game_map.update
    # Switch to map screen
    $scene = Scene_Map.new
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
    $data_actors        = ARC::Data::load("Data/BT_Actors.arc")
    $data_classes       = ARC::Data::load("Data/BT_Classes.arc")
    $data_skills        = ARC::Data::load("Data/BT_Skills.arc")
    $data_items         = ARC::Data::load("Data/BT_Items.arc")
    $data_weapons       = ARC::Data::load("Data/BT_Weapons.arc")
    $data_armors        = ARC::Data::load("Data/BT_Armors.arc")
    $data_enemies       = ARC::Data::load("Data/BT_Enemies.arc")
    $data_troops        = ARC::Data::load("Data/BT_Troops.arc")
    $data_states        = ARC::Data::load("Data/BT_States.arc")
    $data_animations    = ARC::Data::load("Data/BT_Animations.arc")
    $data_tilesets      = ARC::Data::load("Data/BT_Tilesets.arc")
    $data_common_events = ARC::Data::load("Data/BT_CommonEvents.arc")
    $data_system        = ARC::Data::load("Data/BT_System.arc")
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
