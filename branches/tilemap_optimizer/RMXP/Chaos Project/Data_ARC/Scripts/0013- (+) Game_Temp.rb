#==============================================================================
# Game_Temp
#==============================================================================

class Game_Temp
  
  attr_accessor :map_bgm
  attr_accessor :message_text
  attr_accessor :message_proc
  attr_accessor :choice_start
  attr_accessor :choice_max
  attr_accessor :choice_cancel_type
  attr_accessor :choice_proc
  attr_accessor :num_input_start
  attr_accessor :num_input_variable_id
  attr_accessor :num_input_digits_max
  attr_accessor :message_window_showing
  attr_accessor :common_event_id
  attr_accessor :in_battle
  attr_accessor :battle_calling
  attr_accessor :battle_troop_id
  attr_accessor :battle_can_escape
  attr_accessor :battle_can_lose
  attr_accessor :battle_proc
  attr_accessor :battle_turn
  attr_accessor :battle_event_flags
  attr_accessor :battle_abort
  attr_accessor :battle_main_phase
  attr_accessor :battleback_name
  attr_accessor :forcing_battler
  attr_accessor :shop_calling
  attr_accessor :shop_goods
  attr_accessor :name_calling
  attr_accessor :name_actor_id
  attr_accessor :name_max_char
  attr_accessor :menu_calling
  attr_accessor :menu_beep
  attr_accessor :event_menu
  attr_accessor :save_calling
  attr_accessor :debug_calling
  attr_accessor :player_transferring
  attr_accessor :player_new_map_id
  attr_accessor :player_new_x
  attr_accessor :player_new_y
  attr_accessor :player_new_direction
  attr_accessor :transition_processing
  attr_accessor :transition_name
  attr_accessor :gameover
  attr_accessor :to_title
  attr_accessor :last_file_index
  attr_accessor :debug_top_row
  attr_accessor :debug_index
  attr_accessor :animator
  attr_accessor :trance
  attr_accessor :uf_override
  attr_accessor :event_id
  
  def initialize
    @battle_calling = [false, false]
    @map_bgm = @message_text = @message_proc = @choice_proc = @battle_proc =
    @forcing_battler = nil
    @choice_start = @num_input_start = 99
    @choice_max = @choice_cancel_type = @num_input_variable_id =
    @num_input_digits_max = @common_event_id = @battle_troop_id =
    @battle_turn = @shop_id = @name_actor_id = @name_max_char =
    @last_file_index = @debug_top_row = @debug_index = 0
    @battle_event_flags = {}
    @battle_can_escape = @battle_can_lose = @in_battle = @battle_abort =
    @battle_main_phase = @message_window_showing = @shop_calling =
    @menu_calling = @menu_beep = @save_calling = @debug_calling =
    @name_calling = @player_transferring = @transition_processing = @gameover =
    @to_title = false
    @player_new_map_id = @player_new_x = @player_new_y = @player_new_direction = 0
    @battleback_name = @transition_name = ''
  end
  
end
