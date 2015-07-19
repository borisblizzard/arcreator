#==============================================================================
# Enhanced module Input
#------------------------------------------------------------------------------
#  This module handles Blizz-ABS input.
#==============================================================================

module Input
  #----------------------------------------------------------------------------
  # Setup of Controls (ASCII)
  #----------------------------------------------------------------------------
  LMB, RMB, MMB, Backspace, Tab, Enter, Shift, Ctrl, Alt, Esc, D_Down, D_Left,
  D_Right, D_Up, Space = 1, 2, 4, 8, 9, 13, 16, 17, 18, 27, 40, 37, 39, 38, 32
  NumKeys = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
  NumPad = [45, 35, 40, 34, 37, 12, 39, 36, 38, 33]
  Let = {'A' => 65, 'B' => 66, 'C' => 67, 'D' => 68, 'E' => 69, 'F' => 70, 
         'G' => 71, 'H' => 72, 'I' => 73, 'J' => 74, 'K' => 75, 'L' => 76, 
         'M' => 77, 'N' => 78, 'O' => 79, 'P' => 80, 'Q' => 81, 'R' => 82, 
         'S' => 83, 'T' => 84, 'U' => 85, 'V' => 86, 'W' => 87, 'X' => 88, 
         'Y' => 89, 'Z' => 90}
  Fkeys = [-1, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123]
  Collon, Equal, Comma, Underscore, Dot, Backslash, Lb, Rb, Quote = 186, 187,
  188, 189, 190, 191, 219, 221, 222
  # dll call
  State = Win32API.new('user32', 'GetKeyState', ['i'], 'i')
  Key = Win32API.new('user32', 'GetAsyncKeyState', ['i'], 'i')
  # All ASCII keys
  All_keys = 0..255
  @repeating = []
  256.times{@repeating.push(-1)}
  # Blizz-ABS control setup
  if BlizzABS::Control::CUSTOM_CONTROLS
    eval("Up       = #{BlizzABS::Control::UP}")
    eval("Left     = #{BlizzABS::Control::LEFT}")
    eval("Down     = #{BlizzABS::Control::DOWN}")
    eval("Right    = #{BlizzABS::Control::RIGHT}")
    eval("Prevpage = #{BlizzABS::Control::PREVPAGE}")
    eval("Nextpage = #{BlizzABS::Control::NEXTPAGE}")
    eval("Confirm  = #{BlizzABS::Control::CONFIRM}")
    eval("Cancel   = #{BlizzABS::Control::CANCEL}")
    eval("Attack   = #{BlizzABS::Control::ATTACK}")
    eval("Defend   = #{BlizzABS::Control::DEFEND}")
    eval("Skill    = #{BlizzABS::Control::SKILL}")
    eval("Item     = #{BlizzABS::Control::ITEM}")
    eval("Select   = #{BlizzABS::Control::SELECT}")
    eval("Hud      = #{BlizzABS::Control::HUD}")
    eval("Hotkey   = #{BlizzABS::Control::HOTKEY}")
    eval("Minimap  = #{BlizzABS::Control::MINIMAP}")
    eval("Run      = #{BlizzABS::Control::RUN}")
    eval("Sneak    = #{BlizzABS::Control::SNEAK}")
    eval("Jump     = #{BlizzABS::Control::JUMP}")
    eval("Turn     = #{BlizzABS::Control::TURN}")
  # default controls
  else
    Up       = [Let['W']]
    Left     = [Let['A']]
    Down     = [Let['S']]
    Right    = [Let['D']]
    Prevpage = [Let['Q']]
    Nextpage = [Let['E']]
    Confirm  = [Let['H']]
    Cancel   = [Let['F']]
    Attack   = [Let['K']]
    Defend   = [Let['L']]
    Skill    = [Let['J']]
    Item     = [Let['I']]
    Select   = [Let['O']]
    Hud      = [Let['Z']]
    Hotkey   = [Let['X']]
    Minimap  = [Let['C']]
    Run      = [Let['M']]
    Sneak    = [Dot]
    Jump     = [Comma]
    Turn     = [Let['U']]
  end
  #--------------------------------------------------------------------------
  # get_current_state
  #  key - the ASCII number of the key
  #  This method checks if the key is being pressed.
  #-------------------------------------------------------------------------- 
  def Input.get_current_state(key)
    return State.call(key).between?(0, 1)
  end
  #--------------------------------------------------------------------------
  # test_key
  #  key - the ASCII number of the key
  #  This method checks if the key was pressed.
  #-------------------------------------------------------------------------- 
  def Input.test_key(key)
    Key.call(key) & 0x01 == 1
  end
  #--------------------------------------------------------------------------
  # get_symbol
  #  sym - the given symbol
  #  Transforms given number into ASCII character.
  #-------------------------------------------------------------------------- 
  def Input.get_symbol(sym)
    return ((sym != 0 && sym != nil) ? sym.chr : '')
  end
  #--------------------------------------------------------------------------
  # update
  #  Updates input.
  #-------------------------------------------------------------------------- 
  def Input.update
    # storing old keys
    @_keys = (@_keys == nil ? [] : @_keys) | (@keys == nil ? [] : @keys.clone)
    # empty current keys
    @keys, @pressed = [], []
    # checking through all possible keys
    All_keys.each {|key|
        # key is triggered if not triggered before
        @keys.push(key) if Input.test_key(key) && !@_keys.include?(key)
        # if key is not being hold
        if Input.get_current_state(key)
          # remove from helping array
          @_keys.delete(key)
          # remove repeat? flag
          @repeating[key] = 0
        else
          # push into pressed array
          @pressed.push(key)
          # needed for repeat? and repeated?
          if @repeating[key] > 0
            @repeating[key] < 17 ? @repeating[key] += 1 : @repeating[key] = 14
          else
            @repeating[key] = 1
          end
        end}
  end
  #--------------------------------------------------------------------------
  # triggered?
  #  Internal method to check the trigger state.
  #-------------------------------------------------------------------------- 
  def Input.triggered?(key)
    return (@keys.include?(key) && !@_keys.include?(key))
  end
  #--------------------------------------------------------------------------
  # pressed?
  #  Internal method to check the pressed state.
  #-------------------------------------------------------------------------- 
  def Input.pressed?(key)
    return (@pressed.include?(key))
  end
  #--------------------------------------------------------------------------
  # repeated?
  #  Internal method to check the pressed state for repeat?.
  #-------------------------------------------------------------------------- 
  def Input.repeated?(key)
    return ([1, 16].include?(@repeating[key]))
  end
  #--------------------------------------------------------------------------
  # dir4
  #  4 direction check.
  #-------------------------------------------------------------------------- 
  def Input.dir4
    return 2 if Input.press?(Down)
    return 4 if Input.press?(Left)
    return 6 if Input.press?(Right)
    return 8 if Input.press?(Up)
    return 0
  end
  #--------------------------------------------------------------------------
  # dir8
  #  8 direction check.
  #-------------------------------------------------------------------------- 
  def Input.dir8
    return 1 if Input.press?(Down) && Input.press?(Left)
    return 3 if Input.press?(Down) && Input.press?(Right)
    return 7 if Input.press?(Up) && Input.press?(Left)
    return 9 if Input.press?(Up) && Input.press?(Right)
    return 2 if Input.press?(Down)
    return 4 if Input.press?(Left)
    return 6 if Input.press?(Right)
    return 8 if Input.press?(Up)
    return 0
  end
  #--------------------------------------------------------------------------
  # trigger?
  #  Test if key was triggered once.
  #-------------------------------------------------------------------------- 
  def Input.trigger?(keys)
    if keys.is_a?(Array)
      keys.each {|key| Input.check_old_keys(key).each {|k|
          return true if Input.triggered?(k)}}
    else
      Input.check_old_keys(keys).each {|k| return true if Input.triggered?(k)}
    end
    return false
  end
  #--------------------------------------------------------------------------
  # press?
  #  Test if key is being pressed.
  #-------------------------------------------------------------------------- 
  def Input.press?(keys)
    if keys.is_a?(Array)
      keys.each {|key| Input.check_old_keys(key).each {|k|
          return true if Input.pressed?(k)}}
    else
      Input.check_old_keys(keys).each {|k| return true if Input.pressed?(k)}
    end
    return false
  end     
  #--------------------------------------------------------------------------
  # repeat?
  #  Test if key is being pressed for repeating.
  #-------------------------------------------------------------------------- 
  def Input.repeat?(keys)
    if keys.is_a?(Array)
      keys.each {|key| Input.check_old_keys(key).each {|k|
          return true if Input.repeated?(k)}}
    else
      Input.check_old_keys(keys).each {|k| return true if Input.repeated?(k)}
    end
    return false
  end
  #--------------------------------------------------------------------------
  # check_old_keys
  #  Converts all the old keys into the new format if not overriding RMXP's
  #  controls.
  #-------------------------------------------------------------------------- 
  def Input.check_old_keys(key)
    if BlizzABS::Control::DISABLE_DEFAULT
      case key
      when UP then return Up
      when LEFT then return Left
      when DOWN then return Down
      when RIGHT then return Right
      when B then return Cancel
      when C then return Confirm
      when L then return Prevpage
      when R then return Nextpage
      when F9 then return [Fkeys[9]]
      when CTRL then return [Ctrl]
      end
    else
      case key
      when UP then return Up
      when LEFT then return Left
      when DOWN then return Down
      when RIGHT then return Right
      when A then return [Shift]
      when B then return ([Esc, NumPad[0]] | Cancel)
      when C then return ([Space, Enter] | Confirm)
      when X then return [Let['A']]
      when Y then return [Let['S']]
      when Z then return [Let['D']]
      when L then return ([Let['Q']] | Prevpage)
      when R then return ([Let['W']] | Nextpage)
      when F5 then return [Fkeys[5]]
      when F6 then return [Fkeys[6]]
      when F7 then return [Fkeys[7]]
      when F8 then return [Fkeys[8]]
      when F9 then return [Fkeys[9]]
      when SHIFT then return [Shift]
      when CTRL then return [Ctrl]
      when ALT then return [Alt]
      end
    end
    return (key.is_a?(Array) ? key : [key])
  end
  #--------------------------------------------------------------------------
  # Anykey
  #  Checks if ANY key was pressed.
  #-------------------------------------------------------------------------- 
  def Input.Anykey
    return (@keys != [])
  end
  
end

#==============================================================================
# Numeric
#------------------------------------------------------------------------------
#  This class serves as superclass for all numbers.
#==============================================================================

class Numeric
  
  #--------------------------------------------------------------------------
  # sgn
  #  Returns the sign of the number or 0 if the number is 0.
  #-------------------------------------------------------------------------- 
  def sgn
    return (self == 0 ? 0 : self / self.abs)
  end
  
end

#==============================================================================
# Array
#------------------------------------------------------------------------------
#  This class handles array data structures.
#==============================================================================

class Array
  
  #----------------------------------------------------------------------------
  # sum
  #  Sums up all the numeric values of the array.
  #----------------------------------------------------------------------------
  def sum
    # first sum is 0
    sum = 0
    # add each element that's a number to sum
    self.each {|i| sum += i if i.is_a?(Numeric)}
    # return sum as float
    return sum.to_f
  end
  
end

#==============================================================================
# Sprite
#------------------------------------------------------------------------------
#  This class was enhanced with quick color access, a critical animation flag
#  and special viewport coordinate calculation that is used by all HUD
#  elements.
#==============================================================================

class Sprite
  
  # setting all accessable variables
  attr_accessor :critical
  #----------------------------------------------------------------------------
  # system_color
  #  Returns the system color.
  #----------------------------------------------------------------------------
  def system_color
    return Color.new(192, 224, 255)
  end
  #----------------------------------------------------------------------------
  # normal_color
  #  Returns the normal color.
  #----------------------------------------------------------------------------
  def normal_color
    return Color.new(255, 255, 255)
  end
  #----------------------------------------------------------------------------
  # disabled_color
  #  Returns the disabled color.
  #----------------------------------------------------------------------------
  def disabled_color
    return Color.new(255, 255, 255, 128)
  end
  #----------------------------------------------------------------------------
  # crisis_color
  #  Returns the crisis color.
  #----------------------------------------------------------------------------
  def crisis_color
    return Color.new(255, 255, 64)
  end
  #----------------------------------------------------------------------------
  # knockout_color
  #  Returns the knockout color.
  #----------------------------------------------------------------------------
  def knockout_color
    return Color.new(255, 64, 0)
  end
  #----------------------------------------------------------------------------
  # vx
  #  Returns the x position on the screen.
  #----------------------------------------------------------------------------
  def vx
    return (self.x + (viewport == nil ? 0 : viewport.rect.x))
  end
  #----------------------------------------------------------------------------
  # vy
  #  Returns the y position on the screen.
  #----------------------------------------------------------------------------
  def vy
    return (self.y + (viewport == nil ? 0 : viewport.rect.y))
  end
  #----------------------------------------------------------------------------
  # vw
  #  Returns the width visible on the screen.
  #----------------------------------------------------------------------------
  def vw
    return (viewport == nil ? self.bitmap.width : viewport.rect.width)
  end
  #----------------------------------------------------------------------------
  # vh
  #  Returns the height visible on the screen.
  #----------------------------------------------------------------------------
  def vh
    return (viewport == nil ? self.bitmap.height : viewport.rect.height)
  end
  #----------------------------------------------------------------------------
  # in_screen?
  #  Checks if the sprite is visible on the screen.
  #----------------------------------------------------------------------------
  def in_screen?
    return (self.x.between?(0, 639) && (self.y-16).between?(0, 479))
  end
  
end

#==============================================================================
# RPG::Weapon
#------------------------------------------------------------------------------
#  This class was enhanced with optional data drawing either in name or in
#  description.
#==============================================================================

class RPG::Weapon
  
  #----------------------------------------------------------------------------
  # name
  #  Encapsulation of the name variable to provide the possibility of
  #  additional display.
  #----------------------------------------------------------------------------
  def name
    # if range is 0 or the option isn't used for names
    if BlizzABS::Weapons.range(@id) == 0 ||
        BlizzABS::Config::WEAPON_DATA_MODE.all? {|v| v != 1}
      # return normal name
      return @name
    end
    # set up result
    text = @name
    # iterate through configuration
    BlizzABS::Config::WEAPON_DATA_MODE.each_index {|i|
        # if current option was set up for names
        if BlizzABS::Config::WEAPON_DATA_MODE[i] == 1
          # add extra information to result text
          case i
          when 0
            text += case BlizzABS::Weapons.type(@id)
            when 0 then ' (Melee)'
            when 1 then ' (Thrusting)'
            when 2 then ' (Flail)'
            when 3 then ' (Returning Projectile)'
            when 4 then ' (Projectile)'
            when 5 then ' (Shooter)'
            when 6 then ' (Throwing)'
            end
          when 1 then text += " R: #{[BlizzABS::Weapons.range(@id), 1].max}"
          end
        end}
    # return result text
    return text
  end
  #----------------------------------------------------------------------------
  # description
  #  Encapsulation of the description variable to provide the possibility of
  #  additional display.
  #----------------------------------------------------------------------------
  def description
    # if range is 0 or the option isn't used for descriptions
    if BlizzABS::Weapons.range(@id) == 0 ||
        BlizzABS::Config::WEAPON_DATA_MODE.all? {|v| v != 2}
      # return normal description
      return @description
    end
    # set up result
    text = @description
    # iterate through configuration
    BlizzABS::Config::WEAPON_DATA_MODE.each_index {|i|
        # if current option was set up for descriptions
        if BlizzABS::Config::WEAPON_DATA_MODE[i] == 2
          # add extra information to result text
          case i
          when 0
            text += case BlizzABS::Weapons.type(@id)
            when 0 then ' (Melee)'
            when 1 then ' (Thrusting)'
            when 2 then ' (Flail)'
            when 3 then ' (Returning Projectile)'
            when 4 then ' (Projectile)'
            when 5 then ' (Shooter)'
            when 6 then ' (Throwing)'
            end
          when 1 then text += " R: #{[BlizzABS::Weapons.range(@id), 1].max}"
          end
        end}
    # return result text
    return text
  end
  
end

#==============================================================================
# RPG::Skill
#------------------------------------------------------------------------------
#  This class was enhanced with optional data drawing either in name or in
#  description.
#==============================================================================

class RPG::Skill
  
  #----------------------------------------------------------------------------
  # name
  #  Encapsulation of the name variable to provide the possibility of
  #  additional display.
  #----------------------------------------------------------------------------
  def name
    # if range is 0 or the option isn't used for names
    if BlizzABS::Skills.range(@id) == 0 ||
        BlizzABS::Config::SKILL_DATA_MODE.all? {|v| v != 1}
      # return normal name
      return @name
    end
    # set up result
    text = @name
    # iterate through configuration
    BlizzABS::Config::SKILL_DATA_MODE.each_index {|i|
        # if current option was set up for names
        if BlizzABS::Config::SKILL_DATA_MODE[i] == 1
          # add extra information to result text
          case i
          when 0
            next if [0, 7].include?(@scope)
            text += case BlizzABS::Skills.type(@id)[0]
            when 0 then [1, 3, 5].include?(@scope) ? ' (Shooter)' : ' (Thruster)'
            when 1 then [1, 3, 5].include?(@scope) ? ' (Homing)' : ' (S. Homing)'
            when 2 then [1, 3, 5].include?(@scope) ? ' (Selecter)' : ' (Shockwave)'
            when 3 then [1, 3, 5].include?(@scope) ? ' (Beam)' : ' (Fullscreen)'
            when 4 then ' (Summoner)'
            end
          when 1 then text += ' (explodes)' if BlizzABS::Skills.type(@id)[1] > 0
          when 2 then text += " R: #{[BlizzABS::Skills.range(@id), 1].max}"
          end
        end}
    # return result text
    return text
  end
  #----------------------------------------------------------------------------
  # description
  #  Encapsulation of the description variable to provide the possibility of
  #  additional display.
  #----------------------------------------------------------------------------
  def description
    # if range is 0 or the option isn't used for descriptions
    if BlizzABS::Skills.range(@id) == 0 ||
        BlizzABS::Config::SKILL_DATA_MODE.all? {|v| v != 2}
      # return normal description
      return @description
    end
    # set up result
    text = @description
    # iterate through configuration
    BlizzABS::Config::SKILL_DATA_MODE.each_index {|i|
        # if current option was set up for descriptions
        if BlizzABS::Config::SKILL_DATA_MODE[i] == 2
          # add extra information to result text
          case i
          when 0
            next if [0, 7].include?(@scope)
            text += case BlizzABS::Skills.type(@id)[0]
            when 0 then [1, 3, 5].include?(@scope) ? ' (Shooter)' : ' (Thruster)'
            when 1 then [1, 3, 5].include?(@scope) ? ' (Homing)' : ' (S. Homing)'
            when 2 then [1, 3, 5].include?(@scope) ? ' (Selecter)' : ' (Shockwave)'
            when 3 then [1, 3, 5].include?(@scope) ? ' (Beam)' : ' (Fullscreen)'
            when 4 then ' (Summoner)'
            end
          when 1 then text += ' (explodes)' if BlizzABS::Skills.type(@id)[1] > 0
          when 2 then text += " R: #{[BlizzABS::Skills.range(@id), 1].max}"
          end
        end}
    # return result text
    return text
  end
  
end

#==============================================================================
# RPG::Item
#------------------------------------------------------------------------------
#  This class was enhanced with optional data drawing either in name or in
#  description.
#==============================================================================

class RPG::Item
  
  #----------------------------------------------------------------------------
  # name
  #  Encapsulation of the name variable to provide the possibility of
  #  additional display.
  #----------------------------------------------------------------------------
  def name
    # if range is 0 or the option isn't used for names
    if BlizzABS::Items.range(@id) == 0 ||
        BlizzABS::Config::ITEM_DATA_MODE.all? {|v| v != 1}
      # return normal name
      return @name
    end
    # set up result
    text = @name
    # iterate through configuration
    BlizzABS::Config::ITEM_DATA_MODE.each_index {|i|
        # if current option was set up for names
        if BlizzABS::Config::ITEM_DATA_MODE[i] == 1
          # add extra information to result text
          case i
          when 0
            next if [0, 7].include?(@scope)
            text += case BlizzABS::Items.type(@id)[0]
            when 0 then [1, 3, 5].include?(@scope) ? ' (Shooter)' : ' (Thruster)'
            when 1 then [1, 3, 5].include?(@scope) ? ' (Homing)' : ' (S. Homing)'
            when 2 then [1, 3, 5].include?(@scope) ? ' (Selecter)' : ' (Shockwave)'
            when 3 then [1, 3, 5].include?(@scope) ? ' (Beam)' : ' (Fullscreen)'
            when 4 then ' (Summoner)'
            end
          when 1 then text += ' (explodes)' if BlizzABS::Items.type(@id)[1] > 0
          when 2 then text += " R: #{[BlizzABS::Items.range(@id), 1].max}"
          end
        end}
    # return result text
    return text
  end
  #----------------------------------------------------------------------------
  # description
  #  Encapsulation of the description variable to provide the possibility of
  #  additional display.
  #----------------------------------------------------------------------------
  def description
    # if range is 0 or the option isn't used for descriptions
    if BlizzABS::Items.range(@id) == 0 ||
        BlizzABS::Config::ITEM_DATA_MODE.all? {|v| v != 2}
      # return normal description
      return @description
    end
    # set up result
    text = @description
    # iterate through configuration
    BlizzABS::Config::ITEM_DATA_MODE.each_index {|i|
        # if current option was set up for descriptions
        if BlizzABS::Config::ITEM_DATA_MODE[i] == 2
          # add extra information to result text
          case i
          when 0
            next if [0, 7].include?(@scope)
            text += case BlizzABS::Items.type(@id)[0]
            when 0 then [1, 3, 5].include?(@scope) ? ' (Shooter)' : ' (Thruster)'
            when 1 then [1, 3, 5].include?(@scope) ? ' (Homing)' : ' (S. Homing)'
            when 2 then [1, 3, 5].include?(@scope) ? ' (Selecter)' : ' (Shockwave)'
            when 3 then [1, 3, 5].include?(@scope) ? ' (Beam)' : ' (Fullscreen)'
            when 4 then ' (Summoner)'
            end
          when 1 then text += ' (explodes)' if BlizzABS::Items.type(@id)[1] > 0
          when 2 then text += " R: #{[BlizzABS::Items.range(@id), 1].max}"
          end
        end}
    # return result text
    return text
  end
  
end

#==============================================================================
# AI_Data
#------------------------------------------------------------------------------
#  This class serves as superclass for AI_Data classes.
#==============================================================================

class AI_Data
  
  # setting all accessable variables
  attr_accessor :state
  attr_accessor :in_action
  attr_accessor :attacked
  attr_accessor :aggressive
  attr_accessor :find_x
  attr_accessor :find_y
  attr_accessor :last_x
  attr_accessor :last_y
  attr_accessor :dmg
  attr_accessor :fear
  attr_accessor :boss
  attr_accessor :damage
  attr_accessor :memory
  attr_accessor :stay_count
  attr_reader   :origin_aggressive
  #----------------------------------------------------------------------------
  # AI initialization
  #----------------------------------------------------------------------------
  def initialize
    # last x and y of the player when lost out of sight
    @find_x = @find_y = -1
  end
  #----------------------------------------------------------------------------
  # judge
  #  Defines if the enemy has lost enough energy in an enough short period of
  #  time to flee.
  #----------------------------------------------------------------------------
  def judge
    # calculating the result
    result = (@dmg.sum * 100 / @maxhp > 100.0 - @coward)
    # set new fear factor if result is true
    @fear = ((@coward.to_f ** (1/4) + 1) * 20).to_i if result
    # return result
    return result
  end
  #----------------------------------------------------------------------------
  # refresh
  #  Removes the least recent damage accumulation, used by judge.
  #----------------------------------------------------------------------------
  def refresh
    # remove damage accumulation if damage was accumulated and escaping
    @dmg.shift unless @dmg.size == 0 && @fear > 0
  end
  
end

#==============================================================================
# AI_Data_Map_Enemy
#------------------------------------------------------------------------------
#  This class holds all data important for the enemy AI.
#==============================================================================

class AI_Data_Map_Enemy < AI_Data
  
  #----------------------------------------------------------------------------
  # AI initialization
  #----------------------------------------------------------------------------
  def initialize(id, maxhp, eva, aggressive, boss)
    # call superclass method
    super()
    # the ID of the enemy in the database, can be used for enhancement and
    # unique enemy AIs for every enemy in the future
    @id = id
    # possible AI states:
    # 0 - idle movement
    # 1 - move
    # 2 - attack
    # 3 - skill
    # 4 - defend
    # 5 - run away
    # 6 - exception
    # 7 - memorized position
    # 8 - dying
    # 9 - in action
    # 10 - idle, map interpreter is running
    @state = 0
    # enemy's max HP
    @maxhp = maxhp
    # how likely is the enemy to flee
    @coward = eva.to_f
    # collection of last damages to test if the player is stronger
    @dmg = []
    # memory flag
    @memory = false
    # fear shock count
    @fear = 0
    # boss flag
    @boss = boss
    # determines if enemy has an aggressive nature or a passive nature
    @origin_aggressive = @aggressive = aggressive
    # counter if enemy lost out of sight
    @stay_count = 0
  end
  
end

#==============================================================================
# AI_Data_Ally
#------------------------------------------------------------------------------
#  This class holds all data important for the actor AI.
#==============================================================================

class AI_Data_Ally < AI_Data
  
  #----------------------------------------------------------------------------
  # AI initialization
  #----------------------------------------------------------------------------
  def initialize(id)
    # call superclass method
    super()
    # own ID
    @id = id
    # possible AI states:
    # 0 - follow player
    # 1 - engage enemy
    ## 2 - attack
    ## 3 - skill
    ## 4 - defend
    # 5 - return to player
    ## 6 - exception
    ## 7 - memorized position
    ## 8 - dying
    ## 9 - in action
    ## 10 - idle, map interpreter is running
    @state = 0
  end
  
end

#==============================================================================
# AI
#------------------------------------------------------------------------------
#  This module processes Map_Enemy AI based upon AI Data, character position
#  and battler status.
#==============================================================================

module AI
  
  #============================================================================
  # AI::Boss_AI
  #----------------------------------------------------------------------------
  #  This class serves the processing of Boss behaviour.
  #============================================================================
  
  class Boss_AI
    
    #--------------------------------------------------------------------------
    # Initialization
    #  id    - unique Boss AI ID
    #  owner - the Map_Enemy instance using this AI
    #--------------------------------------------------------------------------
    def initialize(id, owner)
      @id, @owner = id, owner
    end
    #--------------------------------------------------------------------------
    # behaviour
    #  This method is empty, so plugins can alias it.
    #--------------------------------------------------------------------------
    def behaviour
    end
    
  end
  
  # create empty Boss AI data hash
  BOSS_AI = {}
  #----------------------------------------------------------------------------
  # log_AI
  #  name - x-coordinate
  #  id   - unique Boss AI ID
  #  This method allows Boss AI plug-ins to be tested on ID conflicts.
  #----------------------------------------------------------------------------
  def self.log_AI(name, id)
    # if AI with this ID already exists
    if BOSS_AI[id] != nil && BOSS_AI[id] != name
      # print text
      p 'Blizz-ABS detected an ID conflict with unique Boss AI IDs. ' +
        "RMXP will now close.   AI 1: #{name}   AI 2: #{BOSS_AI[id]}" +
        "   ID number: #{id}"
      # close RMXP
      exit
    end
    # log new AI under new ID
    BOSS_AI[id] = name
  end
  #----------------------------------------------------------------------------
  # behaviour(x, y, dir, enemy)
  #  x     - x-coordinate
  #  y     - y-coordinate
  #  dir   - facing direction
  #  enemy - the actual battler
  #  Sets the enemy's behaviour depending on the fact if the player is inside
  #  a specific range.
  #----------------------------------------------------------------------------
  def self.behaviour(enemy)
    # temporary variables
    x, y = enemy.x, enemy.y
    # if event code is running
    if $game_system.map_interpreter.running?
      # set state
      enemy.AI_data.state = 10
      # return speed
      return 3
    end
    # if enemy was attacked
    if enemy.attacked > 0
      # decrease shock count
      enemy.attacked -= 1
      # cancel the attack
      enemy.in_action = 0
      # set state
      enemy.AI_data.state = 6
      # return speed
      return 5
    end
    # if enemy attacked the player
    if enemy.in_action > 0
      # decrease shock count if not freeze action
      enemy.in_action -= 1 unless enemy.freeze_action || enemy.current_sprite != ''
      # set state
      enemy.AI_data.state = (enemy.AI_data.state == 4 ? 4 : 9)
      # return speed
      return 4
    end
    # if enemy should flee or already fleeing
    if enemy.AI_data.fear > 0 || enemy.AI_data.judge
      # decrease the fear count
      enemy.AI_data.fear -= 1
      # set state
      enemy.AI_data.state = 5
      # return speed
      return 4
    end
    # calculates the distance
    d = Math.hypot($game_player.x-x, $game_player.y-y)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # get direction
    dir = enemy.direction
    # if player is within range and either seen/heard or already 
    # memorized by the enemy or making noise and aggressive
    if d <= BlizzABS::Config::PERCEPTION_RANGE.to_f * pix &&
        enemy.AI_data.aggressive && (enemy.AI_data.memory ||
        $game_player.in_action > 0 ||
        (AI.can_perceive_enemy?(x, y, dir) && !AI.wall(x, y)))
      # player sighted, remembers that
      enemy.AI_data.memory = true
      # set the last coordinates of the player
      enemy.AI_data.find_x, enemy.AI_data.find_y = $game_player.x, $game_player.y
      # calculate own attack range
      max = BlizzABS::Enemies.range(enemy.battler.id)
      min = (BlizzABS::Enemies.type(enemy.battler.id) == 2 ? max/2 : 0)
      # player within attack range and positioning correct
      if ($game_player.x-x).abs.between?(min*pix, max*pix) &&
          ($game_player.y-y).abs < pix/2 || ($game_player.x-x).abs < pix/2 &&
          ($game_player.y-y).abs.between?(min*pix, max*pix)
        # create action
        enemy.battler.make_action
        # if basic action type
        if enemy.battler.current_action.kind == 0
          # set state depending on which type
          enemy.AI_data.state = case enemy.battler.current_action.basic
          when 0 then 2
          when 1 then 4
          when 2..3 then 1
          end
        else
          # set state
          enemy.AI_data.state = 3
        end
      # too close if flail attack type, so back off a bit
      elsif ($game_player.x-x).abs < min*pix &&
          ($game_player.y-y).abs < pix/2 || ($game_player.x-x).abs < pix/2 &&
          ($game_player.y-y).abs < min*pix
        # set state
        enemy.AI_data.state = 5
        # return speed
        return 4
      else
        # set state
        enemy.AI_data.state = 1
      end
      # return speed
      return 4
    # has lost player out of sight, but remembers last position
    elsif enemy.AI_data.memory
      # set last x and last y
      enemy.AI_data.last_x, enemy.AI_data.last_y = x, y
      # if not moving
      if enemy.AI_data.last_x == x && enemy.AI_data.last_y == y
        # increase counter
        enemy.AI_data.stay_count += 1
      else
        # reset counter
        enemy.AI_data.stay_count = 0
      end
      # difference between coordinates
      dx = x - enemy.AI_data.find_x
      dy = y - enemy.AI_data.find_y
      # if the enemy has reached x and y OR not moving for 2.5 seconds or more
      if dx.abs <= pix * 3.0 / 2 && dy.abs <= pix * 3.0 / 2 ||
          enemy.AI_data.stay_count >= 100
        # reset counter
        enemy.AI_data.stay_count = 0
        # player lost out of sight
        enemy.AI_data.memory = false
        # set idle state
        enemy.AI_data.state = 0
        # return speed
        return 3
      end
      # set state
      enemy.AI_data.state = 7
      # return speed
      return 4
    # otherwise player is not in sight, be "idle"
    else
      # is passive again if passive enemy
      enemy.AI_data.aggressive = false unless enemy.AI_data.origin_aggressive
      # set idle state
      enemy.AI_data.state = 0
      # return speed
      return 3
    end
  end
  #----------------------------------------------------------------------------
  # wall
  #  x - x-coordinate
  #  y - y-coordinate
  #  Checks if between the enemy and the player is a "wall".
  #----------------------------------------------------------------------------
  def self.wall(x, y)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # difference between coordinates
    dx, dy = $game_player.x - x, $game_player.y - y
    # if x difference is not 0
    if dx != 0
      # line coefficient
      k = dy/dx
      # virtual graph drawing
      (1...dx.abs).each {|i|
          # if wall lies on the graph line
          if $game_map.terrain_tag((x+i)/pix, (y+k*i)/pix) ==
              BlizzABS::Config::WALL_TAG
            # wall is between
            return true
          end}
    # if y difference is not 0
    elsif dy != 0
      # line coefficient
      k = dx/dy
      # virtual graph drawing
      (1...dy.abs).each {|i|
          # if wall lies on the graph line
          if $game_map.terrain_tag((x+k*i)/pix, (y+i)/pix) ==
              BlizzABS::Config::WALL_TAG
            # wall is between
            return true
          end}
    end
    # no wall between
    return false
  end
  #----------------------------------------------------------------------------
  # can_perceive_enemy?(x, y, dir)
  #  x   - x-coordinate
  #  y   - y-coordinate
  #  dir - facing direction
  #  Checks if the player can be heard or seen.
  #----------------------------------------------------------------------------
  def self.can_perceive_enemy?(x, y, dir)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # calculate differences of x and y
    dx = $game_player.x - x
    dy = $game_player.y - y
    # check facing direction and return true if the player is inside the
    # seeing/hearing area of the enemy
    return case dir
    when 2
      (dy < 0 && (dx.abs < dy.abs || dx.abs <= pix*2 && dy.abs <= pix*2))
    when 4
      (dx < 0 && (dx.abs > dy.abs || dx.abs <= pix*2 && dy.abs <= pix*2))
    when 6
      (dx > 0 && (dx.abs > dy.abs || dx.abs <= pix*2 && dy.abs <= pix*2))
    when 8
      (dy > 0 && (dx.abs < dy.abs || dx.abs <= pix*2 && dy.abs <= pix*2))
    else
      false
    end
  end
  
end

#==============================================================================
# Game_Temp
#------------------------------------------------------------------------------
#  This class was enhanced with a data pack that holds everything needed for
#  the character selection exception handling.
#==============================================================================

class Game_Temp
  
  attr_accessor :select_data
  
end

#==============================================================================
# Game_System
#------------------------------------------------------------------------------
#  This class was enhanced with Blizz-ABS system settings, enemy creation and
#  destruction process handling.
#==============================================================================

class Game_System
  
  # setting all accessable variables
  attr_accessor :controls
  attr_accessor :killed
  attr_accessor :hud
  attr_accessor :minimap
  attr_accessor :assignment
  attr_accessor :move_fix
  attr_accessor :_8_way
  attr_accessor :bar_style
  attr_accessor :blizzabs
  attr_reader   :pixel_rate
  attr_reader   :bar_opacity
  attr_reader   :enemy_number
  #----------------------------------------------------------------------------
  # override initiliaze
  #----------------------------------------------------------------------------
  alias init_blizzabs_later initialize
  def initialize
    # call original method
    init_blizzabs_later
    # set input controller
    @controls = Game_Controls.new
    # set array of killed enemies
    @killed = []
    # turn HUD on
    @hud = true
    # turn Minimap off
    @minimap = 0
    # turn Hotkey display off
    @assignment = false
    # set movement fix
    @move_fix = BlizzABS::Config::REPAIR_MOVEMENT
    # set 8-way movement
    @_8_way = BlizzABS::Config::EIGHT_WAY_MOVEMENT
    # set pixel movement rate
    self.pixel_rate = BlizzABS::Config::PIXEL_MOVEMENT_RATE
  end
  #----------------------------------------------------------------------------
  # override update
  #----------------------------------------------------------------------------
  alias upd_blizzabs_later update
  def update
    # call original method
    upd_blizzabs_later
    # iterate through all party members
    $game_party.actors.each {|actor|
        # remove set skill for use if actor didn't learn skill
        actor.skill = 0 unless actor.skill_learn?(actor.skill)}
    # return except if scene is Scene_Map
    return unless $scene.is_a?(Scene_Map)
    # iterate through all killed
    @killed.clone.each {|killed|
        # decrease respawn counter
        killed[1] -= 1
        # if dead enemy has event code to be executed
        if killed[0].execute
          # update interpreter
          killed[0].update
        # if respawn counter reached 0
        elsif killed[1] <= 0
          # remove from map
          $game_map.events.delete(killed[0].event_id)
          # if respawning available
          if BlizzABS::Config::RESPAWN_TIME > 0
            # create a new enemy on the old one's template
            new_enemy = respawn_enemy(killed[0])
            # add new enemy on old enemy's place
            $game_map.events[new_enemy.event_id] = new_enemy
          end
          # this enemy is not "killed" anymore
          @killed.delete(killed)
        end}
    # remove all nil values from killed
    @killed.compact!
    # iterate through all events on the map
    $game_map.events.each_value {|event|
        # if event is Map_Enemy
        if event.is_a?(Map_Enemy)
          # start removing the enemy if he's dead
          remove_enemy(event) if event.dead?
          # if enemy spriteset missing and not meeting preconditions
          if event.character_name == '' && event.precondition
            # remove completely
            $game_map.events.delete(event.event_id)
          end
        # if event is dropped item and either item taken or stay time expired
        elsif event.is_a?(Drop_Event) && event.terminate
          # remove completely
          $game_map.events.delete(event.id)
        end}
  end
  #----------------------------------------------------------------------------
  # enemies_refresh
  #  Replaces correctly named events with Blizz-ABS Enemies.
  #----------------------------------------------------------------------------
  def enemies_refresh
    # set original enemy count to 0
    @enemy_number = 0
    # reset the killed array
    @killed = []
    # temporary variable for map
    map = $game_map.map
    # iterate through all events
    map.events.each_key {|i|
        # if the current event exists
        if map.events[i] != nil
          # initialize
          enemy = 0
          attributes = 0x0000
          id_check = []
          # set intern variable to ID
          map.events[i].name.clone.gsub!(/\\[Ee]\[([0-9]+)\]/) {"#[$1]"}
          # temporary variable for ID
          id = $1.to_i
          # if passive flag exists
          if map.events[i].name.clone.gsub!(/\\[Pp]\[([0-9]+)\]/) {"\001[#{$1}]"}
            # set random passive attribute
            id_check.push($1.to_i)
          else
            # don't set random passive attribute
            id_check.push(nil)
          end
          # if boss flag exists
          if map.events[i].name.clone.gsub!(/\\[Bb]/) {''}
            # set boss attribute
            id_check.push(true)
          else
            # don't set boss attribute
            id_check.push(nil)
          end
          # iterate through all attributes
          id_check.each_index {|j|
              # if current attibute is valid
              if id_check[j]
                # which one
                case j
                when 0 # passive
                  # set passive with X% chance
                  attributes |= 0x0001 if (rand(100) < id_check[j])
                when 1 # boss
                  # set boss
                  attributes |= 0x0002
                end
              end}
          # if id is valid and enemy exists in database
          if id != nil && $data_enemies[id] != nil
            # create the enemy event
            enemy = Map_Enemy.new($game_map.map_id, map.events[i], id, i, attributes)
            # replace the real event with the enemy
            $game_map.events[i] = enemy
            # increase original enemy count
            @enemy_number += 1
          end
          # reset ID for next enemy
          id = nil
        end}
  end
  #----------------------------------------------------------------------------
  # remove_enemy
  #  enemy - the killed enemy event
  #  Processes the after-death period of enemies.
  #----------------------------------------------------------------------------
  def remove_enemy(enemy)
    # except if enemy event code is to be executed or enemy is erased
    unless enemy.execute || enemy.erased
      # if getting and item
      if rand(100) < enemy.battler.treasure_prob
        # if enemy drops item
        if enemy.battler.item_id > 0
          # set ID 
          item = $data_items[enemy.battler.item_id]
        # if enemy drops weapon
        elsif enemy.battler.weapon_id > 0
          # set ID
          item = $data_weapons[enemy.battler.weapon_id]
        # if enemy drops armor
        elsif enemy.battler.armor_id > 0
          # set ID
          item = $data_armors[enemy.battler.armor_id]
        end
      end
      # start event code if there is some
      enemy.start if enemy.list != nil
      # remove except if code needs to be executed
      $game_map.events.delete(enemy.event_id) unless enemy.execute
      # create a dropped item on the map if item exists
      Drop_Event.new(item, enemy.x, enemy.y) if item != nil
      # iterate through all party members
      $game_party.actors.each {|actor|
          # increase EXP except if actor can't get EXP
          actor.exp += enemy.exp unless actor.cant_get_exp?}
      # if enemy drops gold
      if enemy.gold != 0
        # if using drop gold mode
        if BlizzABS::Config::DROP_GOLD != ''
          # create dropped gold on the map
          Drop_Event.new(enemy.gold, enemy.x, enemy.y)
        else
          # just increase gold
          $game_party.gain_gold(enemy.gold)
        end
      end
    end
  end
  #----------------------------------------------------------------------------
  # enemies_in_range
  #  Checks how many alive enemies are within ABSEAL range.
  #----------------------------------------------------------------------------
  def enemies_in_range
    # initialize
    result = 0
    # increase counter if not dead and within ABSEAL range for all enemies
    $game_map.enemies.each {|enemy| result += 1 if !enemy.dead? && enemy.update?}
    # return number
    return result
  end
  #----------------------------------------------------------------------------
  # respawn_enemy
  #  enemy - the killed enemy event
  #  Processes the respawn of a dead enemy.
  #----------------------------------------------------------------------------
  def respawn_enemy(enemy)
    # create new enemy on old enemy's template
    new_enemy = Map_Enemy.new($game_map.map_id, enemy)
    # get virtual map passability
    v_map = $game_map.virtual_passability
    # passable
    passables = []
    # find all passable tiles
    (0...v_map.xsize).each {|x| (0...v_map.ysize).each {|y|
        # if passable and enemy may respawn and no event on position
        if v_map[x, y] != 0x00 &&
            $game_map.terrain_tag(x, y) != BlizzABS::Config::NO_ENEMY_TAG &&
            $game_map.event_passable?(x, y)
          passables.push([x, y])
        end}}
    # get coordinates on the map
    x, y = passables[rand(passables.size)]
    # move enemy to x, y coordinate
    new_enemy.moveto(x, y)
    # create sprite for respawned enemy
    sprite = Sprite_Character.new($scene.spriteset.viewport1, new_enemy)
    # set fade_in flag
    sprite.fade_in = true
    # add new sprite into spriteset
    $scene.spriteset.character_sprites.push(sprite)
    # enemy is invisible at first
    new_enemy.opacity = 0
    # return new enemy
    return new_enemy
  end
  #----------------------------------------------------------------------------
  # pixel_rate=
  #  val - new pixel movement rate
  #  Changes the pixel movement rate is necessary.
  #----------------------------------------------------------------------------
  def pixel_rate=(val)
    @pixel_rate = [[val, 0].max, 5].min
  end
  
end

#==============================================================================
# Game_Battler
#------------------------------------------------------------------------------
#  This class was enhanced with helping variables and methods.
#==============================================================================

class Game_Battler
  
  # setting all accessable variables
  attr_reader :hpdamage
  attr_reader :spdamage
  #----------------------------------------------------------------------------
  # override hp=
  #----------------------------------------------------------------------------
  alias hp_is_blizzabs_later hp=
  def hp=(val)
    # store difference
    @hpdamage = @hp-val
    # call original method
    hp_is_blizzabs_later(val)
  end
  #----------------------------------------------------------------------------
  # override sp=
  #----------------------------------------------------------------------------
  alias sp_is_blizzabs_later sp=
  def sp=(val)
    # store difference
    @spdamage = @sp-val
    # call original method
    sp_is_blizzabs_later(val)
  end
  #----------------------------------------------------------------------------
  # eva
  #  Overrides the real Evasion value.
  #----------------------------------------------------------------------------
  def eva
    return 0
  end
  
end

#==============================================================================
# Game_BattleAction
#------------------------------------------------------------------------------
#  This class was modified to prevent a bug where deciding a random target
#  for an enemy would cause the action to be cleared.
#==============================================================================

class Game_BattleAction
  
  #--------------------------------------------------------------------------
  # decide_random_target_for_enemy
  #  Dummy method.
  #--------------------------------------------------------------------------
  def decide_random_target_for_enemy
  end
  
end

#============================================================================== 
# Game_Actor
#------------------------------------------------------------------------------
#  This class was enhanced with helping variables and methods.
#============================================================================== 

class Game_Actor < Game_Battler
  
  # setting all accessable variables
  attr_accessor :item
  attr_accessor :skill
  #----------------------------------------------------------------------------
  # override setup
  #----------------------------------------------------------------------------
  alias setup_blizzabs_later setup
  def setup(id)
    setup_blizzabs_later(id)
    # skill and item IDs on hotkeys
    @skill, @item = 0, 0
    # last known level
    @old_level = @level
  end
  #----------------------------------------------------------------------------
  # now_exp
  #  Returns the current EXP as number.
  #----------------------------------------------------------------------------
  def now_exp
    return (@exp - @exp_list[@level])
  end 
  #----------------------------------------------------------------------------
  # next_exp
  #  Returns the EXP needed to level up or 0 is there are no more levels.
  #----------------------------------------------------------------------------
  def next_exp
    return (@exp_list[@level+1] > 0 ? @exp_list[@level+1]-@exp_list[@level] : 0)
  end
  #----------------------------------------------------------------------------
  # full_next_exp
  #  Returns the EXP needed to reach the next level.
  #----------------------------------------------------------------------------
  def full_next_exp
    return (@exp_list[@level+1] > 0 ? @exp_list[@level+1] : 0)
  end
  #----------------------------------------------------------------------------
  # level_up?
  #  Compares current level to lastly known level and returns a level up.
  #----------------------------------------------------------------------------
  def level_up?
    # result of level up
    result = (@old_level < @level)
    # current level is now last known level
    @old_level = @level
    # return result
    return result
  end
  
end

#==============================================================================
# Game_Enemy
#------------------------------------------------------------------------------
#  This class was enhanced with helping variables.
#==============================================================================

class Game_Enemy < Game_Battler
  
  #----------------------------------------------------------------------------
  # Changed Initialization
  #  enemy - enemy in the database
  #----------------------------------------------------------------------------
  def initialize(enemy)
    # call superclass method
    super()
    # the enemy ID
    @enemy_id = enemy.id
    # battler spriteset name
    @battler_name = enemy.battler_name
    # battler spriteset hue
    @battler_hue = enemy.battler_hue
    # current HP and SP
    @hp, @sp = maxhp, maxsp
    # no troop and not member in troop
    @troop_id, @member_index = 0, 0
    # not hidden
    @hidden = false
    # not immortal
    @immortal = false
  end
  
end

#==============================================================================
# Game_Map
#------------------------------------------------------------------------------
#  This class was redefined by large parts for pixel movement handling and
#  quick minimap passability access.
#==============================================================================

class Game_Map
  
  # setting all accessable variables
  attr_reader :virtual_passability
  attr_reader :map
  #----------------------------------------------------------------------------
  # override setup
  #----------------------------------------------------------------------------
  alias setup_blizzabs_later setup
  def setup(map_id)
    # call original method
    setup_blizzabs_later(map_id)
    # setup enemies on the map
    $game_system.enemies_refresh
    # if using the intelligent minimap system
    if BlizzABS::Config::INTELLIGENT_PASSABILTY
      # load virtual passability map from file
      @virtual_passability = load_data('Data/Map_Data.abs')[0][map_id]
    else
      # create virtual passability map
      @virtual_passability = BlizzABS.setup_passability(@map)
    end
    # reset projectiles and damage sprites
    BlizzABS::Cache.clean
  end
  #----------------------------------------------------------------------------
  # enemies
  #  flag - flag to determine whether to return all enemies or everything else
  #  Returns an array of all enemy events or an array of all events that are
  #  not enemies.
  #----------------------------------------------------------------------------
  def enemies(flag = false)
    # initialize
    result = []
    # add all enemies or everything else to result
    @events.each_value {|e| result.push(e) if flag ^ e.is_a?(Map_Enemy)}
    # return result
    return result
  end
  #----------------------------------------------------------------------------
  # self_valid?
  #  x - x-coordinate
  #  y - y-coordinate
  #  Checks if coordinates are valid. (pixel movement)
  #----------------------------------------------------------------------------
  def self_valid?(x, y)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # checks if coordinates are valid
    return (x >= 0 && x < width*pix-pix+1 && y >= 0 && y < height*pix-pix+1)
  end
  #----------------------------------------------------------------------------
  # direction_valid?
  #  x - x-coordinate
  #  y - y-coordinate
  #  Checks if coordinates are valid. (pixel movement)
  #----------------------------------------------------------------------------
  def direction_valid?(x, y)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # checks if coordinates are valid
    return (x >= 0 && x < width * pix && y >= 0 && y < height * pix)
  end
  #----------------------------------------------------------------------------
  # self_passable?
  #  x          - x-coordinate
  #  y          - y-coordinate
  #  d          - direction
  #  self_event - self event
  #  Checks if passable. (pixel movement)
  #----------------------------------------------------------------------------
  def self_passable?(x, y, d, self_event)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # set bit
    bit = (1 << (d / 2 - 1)) & 0x0F
    # if not in horizontal center of 32x32 pixel tile
    if x != x/pix*pix
      # if current two tiles are impassable from one to another
      unless direction_passable?(x/pix*pix, y, 6) &&
          direction_passable?((x+pix)/pix*pix, y, 4)
        # impassable
        return false
      end
    end
    # if not in vertical center of 32x32 pixel tile
    if y != y/pix*pix
      # if current two tiles are impassable from one to another
      unless direction_passable?(x, y/pix*pix, 2) &&
          direction_passable?(x, (y+pix)/pix*pix, 8)
        # impassable
        return false
      end
    end
    # if jumping
    if d == 0
      # return passability in any direction
      return (direction_passable?(x, y+pix-1, 2) ||
          direction_passable?(x, y, 4) ||
          direction_passable?(x+pix-1, y, 6) ||
          direction_passable?(x, y, 8))
    end
    # if exception works
    if exception(x, y, d)
      # iterate through all corners
      (0...4).each {|i|
          # gets coordinates to check
          xr, yr = x + (pix-1)*(i%2), y + (pix-1)*(i/2)
          # unless checking event and checking tile
          unless event_check(xr, yr, bit, self_event) && tile_check(xr, yr, d)
            # impassable
            return false
          end}
      # passable
      return true
    end
    # impassable
    return false
  end
  #----------------------------------------------------------------------------
  # direction_passable?
  #  x          - x-coordinate
  #  y          - y-coordinate
  #  d          - direction
  #  self_event - self event
  #  Checks if passable. (pixel movement)
  #----------------------------------------------------------------------------
  def direction_passable?(x, y, d)
    # impassable if coordinates not valid
    return false unless direction_valid?(x, y)
    # set bit
    bit = (1 << (d / 2 - 1)) & 0x0F
    # return event check and tile check result
    return (event_check(x, y, bit) && tile_check(x, y, d))
  end
  #----------------------------------------------------------------------------
  # event_check
  #  x          - x-coordinate
  #  y          - y-coordinate
  #  bit        - passability attributes
  #  self_event - self event
  #  Checks if passable events. (pixel movement)
  #----------------------------------------------------------------------------
  def event_check(x, y, bit, self_event = nil)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # iterate trough all events
    self.enemies(true).each {|event|
        # if there's an event that's not through
        if event != self_event && event.x == x/pix && event.y == y/pix &&
            !event.through
          # if obstacle bit is set
          if @passages[event.tile_id] & bit != 0
            # impassable in the given direction
            return false
          # if obstacle bit is set in all directions
          elsif @passages[event.tile_id] & 0x0F == 0x0F
            # impassable tile in the given direction
            return false
          # if priority is 0
          elsif @priorities[event.tile_id] == 0
            # passable in the given direction
            return true
          end
        end}
    # passable
    return true
  end
  #----------------------------------------------------------------------------
  # tile_check
  #  x - x-coordinate
  #  y - y-coordinate
  #  d - direction
  #  Checks if passable tile. (pixel movement)
  #----------------------------------------------------------------------------
  def tile_check(x, y, d)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # set bit
    bit = (1 << (d / 2 - 1)) & 0x0F
    # get virtual passability
    v_map = $game_map.virtual_passability
    # get x and y of next tile
    case d
    when 2 then nx, ny = x/pix, (y+1)/pix
    when 4 then nx, ny = (x-1)/pix, y/pix
    when 6 then nx, ny = (x+1)/pix, y/pix
    when 8 then nx, ny = x/pix, (y-1)/pix
    else
      nx = ny = nil
    end
    # return true whether still on the same tile or next tile is passable
    return (x/pix == nx && y/pix == ny || v_map[x/pix, y/pix] & bit != 0x00)
  end
  #----------------------------------------------------------------------------
  # exception
  #  x - x-coordinate
  #  y - y-coordinate
  #  d - direction
  #  Checks if passable when changing tiles. (pixel movement)
  #----------------------------------------------------------------------------
  def exception(x, y, d)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # if not changing the tile (up/down)
    if (y/pix != (y+pix-1)/pix || x/pix == (x+pix-1)/pix) && [2, 8].include?(d)
      # passable
      return true
    end
    # if not changing the tile (left/right)
    if (x/pix != (x+pix-1)/pix || y/pix == (y+pix-1)/pix) && [4, 6].include?(d)
      # passable 
      return true
    end
    # check direction and return passability depending on direction
    return case d
    when 2
      ($game_map.virtual_passability[x/pix, (y+pix)/pix] & 0x04 == 0x04) &&
      ($game_map.virtual_passability[(x+pix)/pix, (y+pix)/pix] & 0x02 == 0x02)
    when 4
      ($game_map.virtual_passability[(x-pix)/pix, y/pix] & 0x01 == 0x01) &&
      ($game_map.virtual_passability[(x-pix)/pix, (y+pix)/pix] & 0x08 == 0x08)
    when 6
      ($game_map.virtual_passability[(x+pix)/pix, y/pix] & 0x01 == 0x01) &&
      ($game_map.virtual_passability[(x+pix)/pix, (y+pix)/pix] & 0x08 == 0x08)
    when 8
      ($game_map.virtual_passability[x/pix, (y-pix)/pix] & 0x04 == 0x04) &&
      ($game_map.virtual_passability[(x+pix)/pix, (y-pix)/pix] & 0x02 == 0x02)
    end
  end
  #----------------------------------------------------------------------------
  # pixel_counter?
  #  x - x-coordinate
  #  y - y-coordinate
  #  Checks if counter. (pixel movement)
  #----------------------------------------------------------------------------
  def pixel_counter?(x, y)
    # if map ID is value
    if @map_id != 0
      # get pixel movement rate
      pix = BlizzABS.pixel
      # initialize result
      result = false
      # iterate through all layers and check each modified tile (pixel movement)
      [2, 1, 0].each {|i| (0...pix).each {|j| (0...pix).each {|k|
                # if tile is not valid ID
                if data[(x+j)/pix, (y+k)/pix, i] == nil
                  # no counter
                  return false
                # if counter bit is set
                elsif @passages[data[(x+j)/pix, (y+k)/pix, i]] & 0x80 == 0x80
                  # counter
                  result = true
                else
                  # no counter
                  return false
                end}}
            # return the result
            return result}
    end
    # no counter
    return false
  end
  #----------------------------------------------------------------------------
  # pixel_bush?
  #  x - x-coordinate
  #  y - y-coordinate
  #  Checks if bush. (pixel movement)
  #----------------------------------------------------------------------------
  def pixel_bush?(x, y)
    # if map ID valid
    if @map_id != 0
      # get pixel movement rate
      pix = BlizzABS.pixel
      # iterate through all layers
      [2, 1, 0].each {|i|
          # if tile ID not valid
          if data[(x+pix/2)/pix, (y+pix/2)/pix, i] == nil
            # no bush
            return false
          # if bush bit is set
          elsif @passages[data[(x+pix/2)/pix, (y+pix/2)/pix, i]] & 0x40 == 0x40
            # bush
            return true
          end}
    end
    # no bush
    return false
  end
  #----------------------------------------------------------------------------
  # jump_passable?
  #  x  - x-coordinate
  #  y  - y-coordinate
  #  nx - new x-coordinate
  #  ny - new y-coordinate
  #  Checks if there is a tile with JUMP_TAG or WALL_TAG tag, so jumping isn't
  #  possible.
  #----------------------------------------------------------------------------
  def jump_passable?(x, y, nx, ny)
    # if tags are not being used at all (to save process time)
    unless (0..6).include?(BlizzABS::Config::JUMP_TAG) ||
        (0..6).include?(BlizzABS::Config::WALL_TAG)
      # passable
      return true
    end
    # get pixel movement rate
    pix = BlizzABS.pixel
    # get jump direction
    xdir, ydir = (nx-x).sgn, (ny-y).sgn
    # temporary variable
    tags = [BlizzABS::Config::JUMP_TAG, BlizzABS::Config::WALL_TAG]
    # iterate
    loop do
      # passable if all tiles are passable
      return true if x == nx && y == ny
      # impassable if tile has one of the terrain tags
      return false if tags.include?(terrain_tag(x/pix, y/pix))
      # next tile
      x += xdir*pix
      y += ydir*pix
    end
  end
  #----------------------------------------------------------------------------
  # event_passable?
  #  x - x-coordinate
  #  y - y-coordinate
  #  Checks if the given tile is passable in any direction right now.
  #----------------------------------------------------------------------------
  def event_passable?(x, y)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # iterate trough all events
    self.enemies(true).each {|event|
        # if there's an event that's no enemy/actor/dropped item and not through
        if event.tile_id >= 0 && event.x == x/pix && event.y == y/pix &&
            !event.through
          # if obstacle bit is set
          if @passages[event.tile_id] & 0x0F == 0x0F
            # impassable tile in the given direction
            return false
          # if priority is 0
          elsif @priorities[event.tile_id] == 0
            # passable in the given direction
            return true
          end
        end}
    # passable
    return true
  end
  
end
  
#==============================================================================
# Game_Party
#------------------------------------------------------------------------------
#  This class was redefined to create characters used by the caterpillar and to
#  delete all projectiles when a saved game was loaded.
#==============================================================================

class Game_Party
  
  #----------------------------------------------------------------------------
  # override setup_starting_members
  #----------------------------------------------------------------------------
  alias setup_starting_members_blizzabs_later setup_starting_members
  def setup_starting_members
    # call original method
    setup_starting_members_blizzabs_later
    # initialize caterpillar
    BlizzABS.init_caterpillar
  end
  #----------------------------------------------------------------------------
  # override refresh
  #----------------------------------------------------------------------------
  alias refresh_blizzabs_later refresh
  def refresh
    # call original method
    refresh_blizzabs_later
    # reset projectiles and damage sprites
    BlizzABS::Cache.clean
    # reinitialize caterpillar
    BlizzABS.init_caterpillar
  end
  
end

#==============================================================================
# Game_Character
#------------------------------------------------------------------------------
#  This class was redefined to support name event command input, looping
#  animations and ABSEAL update limitation.
#==============================================================================

class Game_Character
  
  # setting all accessable variables
  attr_accessor :erased
  attr_accessor :loop_animation_id
  attr_accessor :terminate
  attr_accessor :teleport
  #----------------------------------------------------------------------------
  # override initialize
  #----------------------------------------------------------------------------
  alias init_blizzabs_later initialize
  def initialize
    # call original method
    init_blizzabs_later
    # set loop animation
    @loop_animation_id = 0
  end
  #----------------------------------------------------------------------------
  # update?
  #  Checks if the event is within update range of ABSEAL.
  #----------------------------------------------------------------------------
  def update?
    # if this map has ABSEAL disabled or it's the player or an actor
    if self.is_a?(Map_Actor) ||
        BlizzABS::Config::DISABLE_ANTI_LAG_IDS.include?($game_map.map_id)
      # update
      return true
    end
    # if auto-start or parallel process or excluded from ABSEAL
    if [3, 4].include?(self.trigger) || self.name.clone.gsub!('\eal') {''}
      # update
      return true
    end
    # if autokiller is on and no character sprite and no tile sprite
    if BlizzABS::Config::ABSEAL_AUTOKILL && @character_name == '' &&
        @tile_id < 384 && !@teleport
      # don't update
      return false
    end
    # correct value out of range for ABSEAL factor
    factor = BlizzABS::Config::FACTOR < 1 ? 1 : BlizzABS::Config::FACTOR.to_i
    # don't update if outside of screen (left)
    return false if @real_x < $game_map.display_x - factor * 128
    # don't update if outside of screen (up)
    return false if @real_y < $game_map.display_y - factor * 128
    # don't update if outside of screen (right)
    return false if @real_x >= $game_map.display_x + 2560 + factor * 128
    # don't update if outside of screen (down)
    return false if @real_y >= $game_map.display_y + 1920 + factor * 128
    # update
    return true
  end
  #----------------------------------------------------------------------------
  # name
  #  Returns the event's name if the is one.
  #----------------------------------------------------------------------------
  def name
    return (@event != nil ? @event.name : '')
  end
  
end

#==============================================================================
# Game_Event
#------------------------------------------------------------------------------
#  This class was redefined as non-pixel movement character to support pixel
#  movement from other character types and ABSEAL update limitation in case
#  Tons of Add-ons is not available.
#==============================================================================

class Game_Event < Game_Character
  
  #----------------------------------------------------------------------------
  # override update
  #----------------------------------------------------------------------------
  # if Tons is not there or version too low
  if $tons_version == nil || $tons_version < 4.7
    alias upd_player_blizzabs_later update
    def update
      # call original method if within ABSEAL range
      upd_player_blizzabs_later if update?
    end
  end
  #----------------------------------------------------------------------------
  # refresh
  #  A flag addition was added to this method.
  #----------------------------------------------------------------------------
  alias refresh_blizzabs_later refresh
  def refresh
    # call original method
    refresh_blizzabs_later
    # test command list on teleport command if command list exists
    @teleport = (@list != nil && @list.any? {|i| i.code == 201})
  end
  #----------------------------------------------------------------------------
  # passable?
  #  x - x-coordinate
  #  y - y-coordinate
  #  d - facing direction
  #  Checks if the tile is passable.
  #----------------------------------------------------------------------------
  def passable?(x, y, d)
    # get new coordinates
    nx, ny = x+(d == 6 ? 1 : d == 4 ? -1 : 0), y+(d == 2 ? 1 : d == 8 ? -1 : 0)
    # not passable if coordinates are outside of map
    return false unless $game_map.valid?(nx, ny)
    # passable if through is ON
    return true if @through
    # not passable if unable to leave current tile in designated direction
    return false unless $game_map.passable?(x, y, d, self)
    # not passable if unable to enter move tile in designated direction
    return false unless $game_map.passable?(nx, ny, 10 - d)
    # impassable if any event on new position and not through
    return false if $game_map.enemies(true).any? {|event|
        !event.through && event.x == nx && event.y == ny}
    # get pixel movement rate
    pix = BlizzABS.pixel
    # return actor coordinate consistency with move destination
    return (@character_name != '' && !BlizzABS.player.actors.any?{|actor|
        actor.x/pix <= nx && (actor.x+pix-1)/pix >= nx && actor.y/pix <= ny &&
        (actor.y+pix-1)/pix >= ny && !actor.through && actor.character_name != ''})
  end
  #----------------------------------------------------------------------------
  # move_toward_player
  #  Moves towards the player. (pixel movement)
  #----------------------------------------------------------------------------
  def move_toward_player
    # get pixel movement rate
    pix = BlizzABS.pixel
    # calculates differences in x and y
    dx, dy = @x - ($game_player.x+pix/2)/pix, @y - ($game_player.y+pix*3/4)/pix
    # determines where to move according to the x and y differences
    if dx > 0 && dy > 0 # player is up left
      move_left if !move_upper_left && !move_up
    elsif dx > 0 && dy < 0 # player is down left
      move_left if !move_lower_left && !move_down
    elsif dx < 0 && dy > 0 # player is up right
      move_right if !move_upper_right && !move_up
    elsif dx < 0 && dy < 0 # player is down right
      move_right if !move_lower_right && !move_down
    elsif dx < 0 && dy == 0 # player is right
      move_right
    elsif dx > 0 && dy == 0 # player is left
      move_left
    elsif dx == 0 && dy < 0 # player is down
      move_down
    elsif dx == 0 && dy > 0 # player is up
      move_up
    end
  end
  #----------------------------------------------------------------------------
  # move_away_from_player
  #  Moves away from the player. (pixel movement)
  #----------------------------------------------------------------------------
  def move_away_from_player
    # get pixel movement rate
    pix = BlizzABS.pixel
    # calculates differences in x and y
    dx, dy = @x - ($game_player.x+pix/2)/pix, @y - ($game_player.y+pix*3/4)/pix
    # determines where to move according to the x and y differences
    if dx > 0 && dy > 0 # player is up left
      move_right if !move_lower_right && !move_down
    elsif dx > 0 && dy < 0 # player is down left
      move_right if !move_upper_right && !move_up
    elsif dx < 0 && dy > 0 # player is up right
      move_left if !move_lower_left && !move_down
    elsif dx < 0 && dy < 0 # player is down right
      move_left if !move_upper_left && !move_up
    elsif dx < 0 && dy == 0 # player is right
      move_left
    elsif dx > 0 && dy == 0 # player is left
      move_right
    elsif dx == 0 && dy < 0 # player is down
      move_up
    elsif dx == 0 && dy > 0 # player is up
      move_down
    end
  end
  #----------------------------------------------------------------------------
  # turn_toward_player
  #  Turn towards the player. (pixel movement)
  #----------------------------------------------------------------------------
  def turn_toward_player
    # get pixel movement rate
    pix = BlizzABS.pixel
    # calculates differences in x and y
    dx, dy = @x - ($game_player.x+pix/2)/pix, @y - ($game_player.y+pix*3/4)/pix
    # determines where to turn according to the x and y differences
    if dx < 0 && dx.abs >= dy.abs # player is right
      turn_right
    elsif dx > 0 && dx.abs >= dy.abs # player is left
      turn_left
    elsif dy < 0 # player is down
      turn_down
    elsif dy > 0 # player is up
      turn_up
    end
  end
  #----------------------------------------------------------------------------
  # turn_away_from_player
  #  Turn away from the player. (pixel movement)
  #----------------------------------------------------------------------------
  def turn_away_from_player
    # get pixel movement rate
    pix = BlizzABS.pixel
    # calculates differences in x and y
    dx, dy = @x - ($game_player.x+pix/2)/pix, @y - ($game_player.y+pix*3/4)/pix
    # determines where to turn according to the x and y differences
    if dx < 0 && dx.abs >= dy.abs # player is right
      turn_left
    elsif dx > 0 && dx.abs >= dy.abs # player is left
      turn_right
    elsif dy < 0 # player is down
      turn_up
    elsif dy > 0 # player is up
      turn_down
    end
  end
  #----------------------------------------------------------------------------
  # check_event_trigger_touch
  #  x - x-coordinate
  #  y - y-coordinate
  #  Check event if was triggered by touch. (pixel movement)
  #----------------------------------------------------------------------------
  def check_event_trigger_touch(x, y)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # stop check if map interpreter is already running
    return if $game_system.map_interpreter.running?
    # if player touched this event
    if @trigger == 2 && x >= $game_player.x/pix &&
        x <= ($game_player.x+pix-1)/pix && y >= $game_player.y/pix &&
        y <= ($game_player.y+pix-1)/pix
      # start except if jumping or over_trigger
      start unless jumping? || over_trigger?
    end
  end
  #----------------------------------------------------------------------------
  # check_event_trigger_auto
  #  x - x-coordinate
  #  y - y-coordinate
  #  Check event if was triggered automaticactor. (pixel movement)
  #----------------------------------------------------------------------------
  def check_event_trigger_auto
    # get pixel movement rate
    pix = BlizzABS.pixel
    # if player touched this event
    if @trigger == 2 && x >= $game_player.x/pix &&
        x <= ($game_player.x+pix-1)/pix && y >= $game_player.y/pix &&
        y <= ($game_player.y+pix-1)/pix
      # start except if jumping or over_trigger
      start unless jumping? || over_trigger?
    end
    # start if auto-start
    start if @trigger == 3
  end
  
end

#==============================================================================
# Map_Battler
#------------------------------------------------------------------------------
#  This class serves as superclass for characters that fight on the map and
#  can use pixel movement.
#==============================================================================
    
class Map_Battler < Game_Character
  
  # setting all accessable variables
  attr_accessor :in_action
  attr_accessor :defending
  attr_accessor :s_count
  attr_accessor :current_sprite
  attr_accessor :weapon_sprite
  attr_accessor :freeze_action
  attr_accessor :fade_out
  attr_accessor :blend_type
  attr_accessor :opacity
  attr_accessor :battler
  attr_reader   :attacked
  #----------------------------------------------------------------------------
  # Initialization
  #----------------------------------------------------------------------------
  def initialize
    # call superclass method
    super
    # sprite animation name add-on and weapon sprite animation name add-on
    @current_sprite = @weapon_sprite = ''
    # sprite animation counter, penalty counter and action penalty counter
    @s_count = @attacked = @in_action = 0
    # action freezing flag
    @freeze_action = false
    # pixel rate setting
    @pixel_rate = $game_system.pixel_rate
    # set original character name
    @character_name_org = @character_name
  end
  #----------------------------------------------------------------------------
  # update
  #  Checks if everything is ok with the pixel rate.
  #----------------------------------------------------------------------------
  def update
    # if pixel movement rate different than the stored one
    if @pixel_rate != $game_system.pixel_rate
      # refresh coordinates
      @x *= 2 ** ($game_system.pixel_rate - @pixel_rate)
      @y *= 2 ** ($game_system.pixel_rate - @pixel_rate)
      # store new pixel movement rate
      @pixel_rate = $game_system.pixel_rate
    end
    # call superclass method
    super
  end
  #----------------------------------------------------------------------------
  # set_action
  #  rate - penalty rate in seconds
  #  Set frame penalty counter.
  #----------------------------------------------------------------------------
  def set_action(rate)
    @in_action = (rate*20).to_i
  end
  #----------------------------------------------------------------------------
  # use_attack
  #  Processes using an attack.
  #----------------------------------------------------------------------------
  def use_attack
    # sets everything up for attack sprites
    setup_sprites('_atk')
    # set frame penalty
    set_action(self.is_a?(Map_Actor) ? 0.8 : 1.6)
    # set animation ID if ANIMATIONS is turned on
    @animation_id = battler.animation1_id if BlizzABS::Config::ANIMATIONS
    # execute attack process and return result
    return (BlizzABS.attack_process(self))
  end
  #----------------------------------------------------------------------------
  # use_skill
  #  skill - the skill to be used
  #  Processes using a skill.
  #----------------------------------------------------------------------------
  def use_skill(skill)
    # set animation ID if ANIMATIONS is turned on
    @animation_id = skill.animation1_id if BlizzABS::Config::ANIMATIONS
    # if battler can use the skill and skill data was processes with success
    if @battler.skill_can_use?(skill.id) &&
        BlizzABS.skillitem_process(self, skill)
      # setup sprite extension
      setup_sprites('_skl')
      # set extended frame penalty depending on whether actor or enemy
      set_action(self.is_a?(Map_Actor) ? 1.6 : 3.2)
      # SP consumption
      @battler.sp -= skill.sp_cost 
      # if skill calls common event
      if skill.common_event_id > 0
        # temporary variable
        common_event = $data_common_events[skill.common_event_id]
        # setup common event execution
        $game_system.map_interpreter.setup(common_event.list, 0)
      end
      # used
      return true
    end
    # reset animation ID, since not used
    @animation_id = 0
    # not used
    return false
  end
  #----------------------------------------------------------------------------
  # use_item
  #  item - the skill to be used
  #  Processes using an item.
  #----------------------------------------------------------------------------
  def use_item(item)
    # set animation ID if ANIMATIONS is turned on
    @animation_id = item.animation1_id if BlizzABS::Config::ANIMATIONS
    # if party can use the item and item data was processes with success
    if $game_party.item_can_use?(item.id) &&
        BlizzABS.skillitem_process(self, item)
      # setup sprite extension
      setup_sprites('_itm')
      # set extended frame penalty depending on whether actor or enemy
      set_action(self.is_a?(Map_Actor) ? 1.6 : 3.2)
      # item consumption if item can be consumed
      $game_party.lose_item(item.id, 1) if item.consumable
      # if item calls common event
      if item.common_event_id > 0
        # temporary variable
        common_event = $data_common_events[item.common_event_id]
        # setup common event execution
        $game_system.map_interpreter.setup(common_event.list, 0)
      end
      # used
      return true
    end
    # reset animation ID, since not used
    @animation_id = 0
    # not used
    return false
  end
  #----------------------------------------------------------------------------
  # attack_effect
  #  character - the character that holds attack data (can be projectile)
  #  _battler  - the attacking battler
  #  This method executes attack upon a map character.
  #----------------------------------------------------------------------------
  def attack_effect(character, _battler)
    # stop attack if no battler assigned or still invincible
    return false if @battler == nil || @blinking != nil && @blinking > 0
    # stop attack if pressing CTRL in debug mode
    return false if $DEBUG && self.is_a?(Map_Actor) && Input.press?(Input::CTRL)
    # if defending
    if self.defending
      # set attacked counter
      self.attacked = BlizzABS.pixel
      # set damage to 0
      @battler.damage = 0
      # turn towards attacker
      turn_toward(character)
      # not executed
      return false
    end
    # remove last hpdamage and spdamage values
    @battler.hp, @battler.sp = @battler.hp, @battler.sp
    # if effect processing was executed
    if @battler.attack_effect(_battler) || @battler.hpdamage != 0 ||
        @battler.spdamage != 0
      # if damage dealt
      if @battler.hpdamage > 0 || @battler.spdamage > 0
        # set attacked counter
        self.attacked = BlizzABS.pixel
      end
      # turn towards attacker
      turn_toward(character)
      # set attacking enemy animation ID if ANIMATIONS is turned on
      @animation_id = _battler.animation2_id if BlizzABS::Config::ANIMATIONS
      # attack was executed
      result = true
    end
    # if no numeric damage and SP were changed
    unless @battler.damage.is_a?(Numeric) || @battler.spdamage == 0
      # manipulate damage text with spdamage
      @battler.damage = "#{@battler.spdamage.abs} #{$data_system.words.sp}"
    end
    # determine execution
    return (result == true)
  end
  #----------------------------------------------------------------------------
  # skill_effect
  #  character - the character that holds skill use (can be projectile)
  #  _battler  - the skill using battler
  #  skill     - the skill
  #  This method executes skill use upon a map character.
  #----------------------------------------------------------------------------
  def skill_effect(character, _battler, skill)
    # stop skill if no battler assigned
    return false if @battler == nil
    # stop skill if pressing CTRL in debug mode
    return false if $DEBUG && self.is_a?(Map_Actor) && Input.press?(Input::CTRL)
    # remove last hpdamage and spdamage values
    @battler.hp, @battler.sp = @battler.hp, @battler.sp
    # if effect processing was executed
    if @battler.skill_effect(_battler, skill)  || @battler.hpdamage != 0 ||
        @battler.spdamage != 0
      # if damage dealt
      if @battler.hpdamage > 0 || @battler.spdamage > 0
        # set attacked counter
        self.attacked = BlizzABS.pixel
      end
      # turn towards attacker
      turn_toward(character)
      # set attacked enemy animation ID if ANIMATIONS is turned on
      @animation_id = skill.animation2_id if BlizzABS::Config::ANIMATIONS
      # attack was executed
      result = true
    end
    # if no numeric damage and SP were changed
    unless @battler.damage.is_a?(Numeric) || @battler.spdamage == 0
      # manipulate damage text with spdamage
      @battler.damage = "#{@battler.spdamage.abs} #{$data_system.words.sp}"
    end
    # determine execution
    return (result == true)
  end
  #----------------------------------------------------------------------------
  # item_effect
  #  character - the character that holds item use (can be projectile)
  #  item      - the item
  #  This method executes item use upon a map character.
  #----------------------------------------------------------------------------
  def item_effect(character, item)
    # stop item if no battler assigned
    return false if @battler == nil 
    # stop item if pressing CTRL in debug mode
    return false if $DEBUG && self.is_a?(Map_Actor) && Input.press?(Input::CTRL)
    # remove last hpdamage and spdamage values
    @battler.hp, @battler.sp = @battler.hp, @battler.sp
    # if effect processing was executed
    if @battler.item_effect(item) || @battler.hpdamage != 0 ||
        @battler.spdamage != 0
      # if damage dealt
      if @battler.hpdamage > 0 || @battler.spdamage > 0
        # set attacked counter
        self.attacked = BlizzABS.pixel
      end
      # turn towards attacker
      turn_toward(character)
      # set attacked enemy animation ID if ANIMATIONS is turned on
      @animation_id = item.animation2_id if BlizzABS::Config::ANIMATIONS
      # attack was executed
      result = true
    end
    # if no numeric damage and SP were changed
    unless @battler.damage.is_a?(Numeric) || @battler.spdamage == 0
      # manipulate damage text with spdamage
      @battler.damage = "#{@battler.spdamage.abs} #{$data_system.words.sp}"
    end
    # determine execution
    return (result == true)
  end
  #----------------------------------------------------------------------------
  # pattern
  #  Overriding method for accessing the pattern number of the spriteset.
  #----------------------------------------------------------------------------
  def pattern
    # return animated forced pattern or last forced pattern if in action
    return (in_action <= 0 ? @pattern : (@s_count > 0 ? (12-@s_count)/3 : 0))
  end
  #----------------------------------------------------------------------------
  # turn_toward
  #  character - a character
  #  Same as turn_towards_player, but working with any pixel movement
  #  character.
  #----------------------------------------------------------------------------
  def turn_toward(character)
    # calculate the differences
    dx, dy = @x - character.x, @y - character.y
    # check the differences
    if dx < 0 && dx.abs >= dy.abs # target is right
      turn_right
    elsif dx > 0 && dx.abs >= dy.abs # target is left
      turn_left
    elsif dy < 0 # target is down
      turn_down
    elsif dy > 0 # target is up
      turn_up
    end
  end
  #----------------------------------------------------------------------------
  # sprite_update
  #  Processes the sprite-animation timing.
  #----------------------------------------------------------------------------
  def sprite_update
    # return if scene not Scene_Map or spriteset doesn't exist
    return if !$scene.is_a?(Scene_Map) || $scene.spriteset == nil
    # set spriteset name
    @character_name = @character_name_org + @current_sprite
    # if defending
    if self.defending
      # spriteset name add-on _def
      @current_sprite = '_def'
    # spriteset name add-on not '' and not _def
    elsif @current_sprite != '' && @current_sprite != '_def'
      # decrease animation counter
      @s_count -= 1
      # if counter reached 0
      if @s_count <= 0
        # reset spriteset name
        @character_name = @character_name_org
        # reset animation counter
        @s_count = 0
        # reset spriteset name add-ons
        @current_sprite = @weapon_sprite = ''
      end
    else
      # reset spriteset name
      @character_name = @character_name_org
      # reset spriteset name add-on
      @current_sprite = ''
    end
  end
  #----------------------------------------------------------------------------
  # setup_sprites
  #  type - the spriteset extension
  #  Sets up everything used for skill sprite combination.
  #----------------------------------------------------------------------------
  def setup_sprites(type)
    # straighten
    straighten
    # set sprite count
    @s_count = 12
    # if this character holds an actor
    if self.battler.is_a?(Game_Actor)
      # if active
      if BlizzABS::Config::ACTOR_ACTION_SPRITES
        # set current sprite extension
        @current_sprite = type 
        # if attack sprites
        if type == '_atk'
          # add weapon type number
          @current_sprite += BlizzABS::Weapons.type(self.battler.weapon_id).to_s
          # if weapon sprite active
          if BlizzABS::Config::WEAPON_SPRITES && self.battler.weapon_id > 0
            # set up the weapon sprite name
            @weapon_sprite = "_#{$data_weapons[self.battler.weapon_id].icon_name}"
          end
        end
      end
    else
      # set current sprite extension if active
      @current_sprite = type if BlizzABS::Config::ENEMY_ACTION_SPRITES
    end
  end
  #----------------------------------------------------------------------------
  # attacked=
  #  val - number
  #  Sets the attacked counter and resets all sprites.
  #----------------------------------------------------------------------------
  def attacked=(val)
    # reset sprites
    @current_sprite = @weapon_sprite = ''
    # set attacked counter and reset sprite counter
    @attacked, @s_count = val, 0
  end
  #----------------------------------------------------------------------------
  # moving?
  #  Determines if the character is moving.
  #----------------------------------------------------------------------------
  def moving?
    # get pixel movement rate
    pix = BlizzABS.pixel
    # return if player is moving
    return (@real_x != @x * 128 / pix || @real_y != @y * 128 / pix)
  end
  #----------------------------------------------------------------------------
  # moveto
  #  x - x-coordinate
  #  y - y-coordinate
  #  Instant moving.
  #----------------------------------------------------------------------------
  def moveto(x, y)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # calculate new coordinates
    @x = (x * pix) % ($game_map.width * pix)
    @y = (y * pix) % ($game_map.height * pix)
    @real_x = @x * 128 / pix
    @real_y = @y * 128 / pix
    # reset pre-lock direction
    @prelock_direction = 0
  end
  #--------------------------------------------------------------------------
  # move_down
  #  turn_enabled - flag that determines whether to turn in moving direction
  #  Moves. (pixel movement)
  #--------------------------------------------------------------------------
  def move_down(turn_enabled = true)
    # turn if turn enabled
    turn_down if turn_enabled
    # if passable (if pixel movement is on, allow corner skip)
    if passable?(@x, @y, 2)
      # set new coordinates
      @y += 1
      # increase steps
      increase_steps
      # moved
      return true
    end
    # check touched events
    check_event_trigger_touch(@x, @y+1)
    # not moved
    return false
  end
  #--------------------------------------------------------------------------
  # move_left
  #  turn_enabled - flag that determines whether to turn in moving direction
  #  Moves. (pixel movement)
  #--------------------------------------------------------------------------
  def move_left(turn_enabled = true)
    # turn if turn enabled
    turn_left if turn_enabled
    # if passable (if pixel movement is on, allow corner skip)
    if passable?(@x, @y, 4)
      # set new coordinates
      @x -= 1
      # increase steps
      increase_steps
      # moved
      return true
    end
    # check touched events
    check_event_trigger_touch(@x-1, @y)
    # not moved
    return false
  end
  #--------------------------------------------------------------------------
  # move_right
  #  turn_enabled - flag that determines whether to turn in moving direction
  #  Moves. (pixel movement)
  #--------------------------------------------------------------------------
  def move_right(turn_enabled = true)
    # turn if turn enabled
    turn_right if turn_enabled
    # if passable (if pixel movement is on, allow corner skip)
    if passable?(@x, @y, 6)
      # set new coordinates
      @x += 1
      # increase steps
      increase_steps
      # moved
      return true
    end
    # check touched events
    check_event_trigger_touch(@x+1, @y)
    # not moved
    return false
  end
  #--------------------------------------------------------------------------
  # move_up
  #  turn_enabled - flag that determines whether to turn in moving direction
  #  Moves. (pixel movement)
  #--------------------------------------------------------------------------
  def move_up(turn_enabled = true)
    # turn if turn enabled
    turn_up if turn_enabled
    # if passable (if pixel movement is on, allow corner skip)
    if passable?(@x, @y, 8)
      # set new coordinates
      @y -= 1
      # increase steps
      increase_steps
      # moved
      return true
    end
    # check touched events
    check_event_trigger_touch(@x, @y-1)
    # not moved
    return false
  end
  #----------------------------------------------------------------------------
  # move_lower_left
  #  Moves. (pixel movement)
  #----------------------------------------------------------------------------
  def move_lower_left
    # if not direction fixed
    unless @direction_fix
      # set direction
      @direction = (@direction == 6 ? 4 : @direction == 8 ? 2 : @direction)
    end
    # if passable (if pixel movement is on, allow corner skip)
    if BlizzABS.pixel > 1 &&
       (passable?(@x, @y, 2) && passable?(@x, @y + 1, 4) ||
        passable?(@x, @y, 4) && passable?(@x - 1, @y, 2)) ||
        passable?(@x, @y, 2) && passable?(@x, @y + 1, 4) &&
        passable?(@x, @y, 4) && passable?(@x - 1, @y, 2)
      # set new coordinates
      @x -= 1
      @y += 1
      # increase steps
      increase_steps
      # moved
      return true
    end
    # check touched events
    check_event_trigger_touch(@x-1, @y+1)
    # not moved
    return false
  end
  #----------------------------------------------------------------------------
  # move_lower_right
  #  Moves. (pixel movement)
  #----------------------------------------------------------------------------
  def move_lower_right
    # if not direction fixed
    unless @direction_fix
      # set direction
      @direction = (@direction == 4 ? 6 : @direction == 8 ? 2 : @direction)
    end
    # if passable (if pixel movement is on, allow corner skip)
    if BlizzABS.pixel > 1 &&
       (passable?(@x, @y, 2) && passable?(@x, @y + 1, 6) ||
        passable?(@x, @y, 6) && passable?(@x + 1, @y, 2)) ||
        passable?(@x, @y, 2) && passable?(@x, @y + 1, 6) &&
        passable?(@x, @y, 6) && passable?(@x + 1, @y, 2)
      # set new coordinates
      @x += 1
      @y += 1
      # increase steps
      increase_steps
      # moved
      return true
    end
    # check touched events
    check_event_trigger_touch(@x+1, @y+1)
    # not moved
    return false
  end
  #----------------------------------------------------------------------------
  # move_upper_left
  #  Moves. (pixel movement)
  #----------------------------------------------------------------------------
  def move_upper_left
    # if not direction fixed
    unless @direction_fix
      # set direction
      @direction = (@direction == 6 ? 4 : @direction == 2 ? 8 : @direction)
    end
    # if passable (if pixel movement is on, allow corner skip)
    if BlizzABS.pixel > 1 &&
       (passable?(@x, @y, 8) && passable?(@x, @y - 1, 4) ||
        passable?(@x, @y, 4) && passable?(@x - 1, @y, 8)) ||
        passable?(@x, @y, 8) && passable?(@x, @y - 1, 4) &&
        passable?(@x, @y, 4) && passable?(@x - 1, @y, 8)
      # set new coordinates
      @x -= 1
      @y -= 1
      # increase steps
      increase_steps
      # moved
      return true
    end
    # check touched events
    check_event_trigger_touch(@x-1, @y-1)
    # not moved
    return false
  end
  #----------------------------------------------------------------------------
  # move_upper_right
  #  Moves. (pixel movement)
  #----------------------------------------------------------------------------
  def move_upper_right
    # if not direction fixed
    unless @direction_fix
      # set direction
      @direction = (@direction == 4 ? 6 : @direction == 2 ? 8 : @direction)
    end
    # if passable (if pixel movement is on, allow corner skip)
    if BlizzABS.pixel > 1 &&
       (passable?(@x, @y, 8) && passable?(@x, @y - 1, 6) ||
        passable?(@x, @y, 6) && passable?(@x + 1, @y, 8)) ||
        passable?(@x, @y, 8) && passable?(@x, @y - 1, 6) &&
        passable?(@x, @y, 6) && passable?(@x + 1, @y, 8)
      # set new coordinates
      @x += 1
      @y -= 1
      # increase steps
      increase_steps
      # moved
      return true
    end
    # check touched events
    check_event_trigger_touch(@x+1, @y-1)
    # not moved
    return false
  end
  #----------------------------------------------------------------------------
  # update_move
  #  Processes moving progress. (pixel movement)
  #----------------------------------------------------------------------------
  def update_move
    # get pixel movement rate
    pix = BlizzABS.pixel
    # moving distance
    distance = 2 ** @move_speed
    # set new coordinates
    @real_y = [@real_y + distance, @y * 128/pix].min if @y * 128/pix > @real_y
    @real_x = [@real_x - distance, @x * 128/pix].max if @x * 128/pix < @real_x
    @real_x = [@real_x + distance, @x * 128/pix].min if @x * 128/pix > @real_x
    @real_y = [@real_y - distance, @y * 128/pix].max if @y * 128/pix < @real_y
    # if walking
    if @walk_anime
      # increase anime_count
      @anime_count += 1.5
    # if standing
    elsif @step_anime
      # increase anime_count
      @anime_count += 1
    end
  end
  #----------------------------------------------------------------------------
  # update_jump
  #  Processes jumping progress. (pixel movement)
  #----------------------------------------------------------------------------
  def update_jump
    # get pixel movement rate
    pix = BlizzABS.pixel
    # decrease jump count
    @jump_count -= 1
    # set new coordinates
    @real_x = (@real_x * @jump_count + @x * 128 / pix) / (@jump_count + 1)
    @real_y = (@real_y * @jump_count + @y * 128 / pix) / (@jump_count + 1)
  end
  #----------------------------------------------------------------------------
  # jump
  #  x - x-coordinate
  #  y - y-coordinate
  #  Jumps. (pixel movement)
  #----------------------------------------------------------------------------
  def jump(x_plus, y_plus, d = nil)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # if jumping onto another tile
    if x_plus != 0 or y_plus != 0
      # if horizontal distance is longer
      if x_plus.abs > y_plus.abs
        # turn left or right
        x_plus < 0 ? turn_left : turn_right
      else
        # turn up or down
        y_plus < 0 ? turn_up : turn_down
      end
    end
    # if direction unknown
    if d == nil
      # determine direction depending plus values
      if x_plus > 0 and y_plus > 0 # jumping down right
        d = 3
      elsif x_plus > 0 and y_plus < 0 # jumping up left
        d = 9
      elsif x_plus < 0 and y_plus > 0 # jumping down right
        d = 1
      elsif x_plus < 0 and y_plus < 0 # jumping up left
        d = 7
      elsif x_plus < 0 and y_plus == 0 # jumping left
        d = 4
      elsif x_plus > 0 and y_plus == 0 # jumping right
        d = 6
      elsif x_plus == 0 and y_plus < 0 # jumping up
        d = 8
      elsif x_plus == 0 and y_plus > 0 # jumping down
        d = 2
      end
    end
    # straighten
    straighten
    # find new coordinates
    nx, ny = @x + x_plus*pix, @y + y_plus*pix
    # if can't jump to new location
    if jump_passable?(nx, ny, d) && $game_map.jump_passable?(@x, @y, nx, ny)
      # set new coordinates
      @x, @y = nx, ny
    else
      # reset coordinates
      x_plus = y_plus = 0
    end
    # set jump peak
    @jump_peak = 10 + Math.hypot(x_plus, y_plus).round - @move_speed
    # set jump count
    @jump_count = @jump_peak * 2
    # set stop count
    @stop_count = 0
    # jumped if x and y plus are 0
    return (x_plus != 0 || y_plus != 0)
  end
  #----------------------------------------------------------------------------
  # bush_depth
  #  Checks the bush depth. (pixel movement)
  #----------------------------------------------------------------------------
  def bush_depth
    # return 0 tile exists and not on bottom and not bush, else 12
    return ((@jump_count == 0 && $game_map.pixel_bush?(@x, @y) &&
        @tile_id == 0 && !@always_on_top) ? 12 : 0)
  end
  #----------------------------------------------------------------------------
  # terrain_tag
  #  Checks the terrain tag. (pixel movement)
  #----------------------------------------------------------------------------
  def terrain_tag
    # get pixel movement rate
    pix = BlizzABS.pixel
    # return terrain tag at the character's center
    return $game_map.terrain_tag((@x+pix/2)/pix, (@y+pix/2)/pix)
  end
  #----------------------------------------------------------------------------
  # running?
  #  Dummy method.
  #----------------------------------------------------------------------------
  def running?
    return false
  end
  #----------------------------------------------------------------------------
  # sneaking?
  #  Dummy method.
  #----------------------------------------------------------------------------
  def sneaking?
    return false
  end
  
end

#==============================================================================
# Map_Actor
#------------------------------------------------------------------------------
#  This class serves as character class for any actor on the map.
#  Player_Controller controls that instance of this class which has the first
#  party member as battler.
#==============================================================================

class Map_Actor < Map_Battler

  # setting all accessable variables
  attr_accessor :cindex
  attr_accessor :buffer
  attr_accessor :move_speed
  attr_accessor :character_name
  attr_accessor :character_name_org
  attr_accessor :encounter_count
  #----------------------------------------------------------------------------
  # Initialization
  #----------------------------------------------------------------------------
  def initialize(index)
    # call superclass method
    super()
    # store battler
    @battler = $game_party.actors[index]
    # set blinking counter
    @blinking = 0
    # save index in caterpillar
    @cindex = index
    # enforce the next force_movement from the buffer
    @force_movement = 0
    # set movement buffer
    @buffer = []
    # create actor AI data pack
    @AI_data = AI_Data_Ally.new(@id)
    # dummy
    @encounter_count = 1
  end
  #----------------------------------------------------------------------------
  # update
  #  Processes all the data.
  #----------------------------------------------------------------------------
  def update
    # if this character is being controlled by the player
    if BlizzABS.player.player == self
      # update player control over this character
      result = BlizzABS.player.update_control
      # call superclass method
      super
      # call post update process
      BlizzABS.player.update_move(result)
      # exit method
      return
    end
    # if pixel movement rate different than the stored one
    if @pixel_rate != $game_system.pixel_rate
      # stores old buffer
      tmp = @buffer
      # clears buffer
      @buffer = []
      # while there is still data in the old buffer
      while tmp.size > 0
        # if instant jump command
        if tmp[0].is_a?(Array)
          # directly add into new buffer
          @buffer.push(tmp.shift)
        else
          # get current command
          move = tmp.shift
          # remove the rest of the commands depending on old pixel movement
          (2**@pixel_rate-1).times {tmp.shift}
          # add into new buffer depending on new pixel movement
          (2**$game_system.pixel_rate).times {@buffer.push(move)}
        end
      end
    end
    # reset spriteset name
    @character_name = @character_name_org
    # if battler exists
    if battler != nil
      # update spriteset animation 
      sprite_update 
      # if battler is dead
      if battler != nil && battler.dead?
        # make a ghost animation using opacity
        @opacity = 64 + 192 * (Graphics.frame_count%4/2).abs
      # if defending and not attacking and not in action
      elsif @defending && @attacked == 0 && self.in_action == 0
        # straighten
        straighten
        # exit method
        return
      end
      # updates any attack action
      update_attacked
    end
    # if in action
    if self.in_action > 0
      # decrease counter
      @in_action -= 1 if @in_action > 0
      # call superclass method
      super
      # set stopped animation flag if actor's character is animated
      @step_anime = true if BlizzABS::Config::ANIMATED_IDS.include?(battler.id)
      # exit method
    end
    # transparent flag inheritance from player
    @transparent = $game_player.transparent
    # through flag inheritance from player
    @through = $game_player.through
    # set blendtype to "ghost" if dead, otherwise to normal
    @blend_type = dead? ? 1 : 0
    # get pixel movement rate
    pix = BlizzABS.pixel
    # test the AI state
    case @AI_data.state
    when 0
      # if far enough from the player
      if Math.hypot(@real_x-$game_player.real_x,
          @real_y-$game_player.real_y) > (@cindex+2)*128
        # remove from caterpillar
        update_ci(nil)
        # empty movement buffer
        @buffer = []
        # set to return state
        @AI_data.state = 5
      else
        # set speed to the player's move speed
        @move_speed = $game_player.move_speed
        # if not moving and buffer not empty and either forced or buffer full
        if !moving? && @buffer.size > 0 && (@buffer.size > @cindex * pix ||
            @force_movement > 0)
          # get next command
          move = @buffer.shift
          # if command is complex
          if move.is_a?(Array)
            # check command and decide jump direction
            case move[0]
            when 1 then x, y = -1, 1
            when 2 then x, y = 0, 1
            when 3 then x, y = 1, 1
            when 4 then x, y = -1, 0
            when 6 then x, y = 1, 0
            when 7 then x, y = -1, -1
            when 8 then x, y = 0, -1
            when 9 then x, y = 1, -1
            else
              x, y = 0, 0
            end
            # get jumping range
            range = BlizzABS::Config::JUMPING
            # jump into direction with considering running/sneaking
            jump(x*range + x*move[1], y*range + y*move[1], move[0])
          else
            # check command and move
            case move
            when 1 then move_lower_left
            when 2 then move_down(true)
            when 3 then move_lower_right
            when 4 then move_left(true)
            when 6 then move_right(true)
            when 7 then move_upper_left
            when 8 then move_up(true)
            when 9 then move_upper_right
            when false
              # remove from caterpillar
              update_ci(nil)
              # empty movement buffer
              @buffer = []
              # set to return state
              @AI_data.state = 5
              # remove force counter
              @force_movement = 0
            end
          end
          # decrease counter if counter is active
          @force_movement -= 1 if @force_movement > 0
        end
      end
    when 5
      # if not moving already
      unless moving?
        # get current index
        ind = self.index
        # iterate through all actors in front of self
        (0...ind).each {|i|
            # decrease @cindex each time an actor is missing in the caterpillar
            ind -= 1 if BlizzABS.player.actors[i].cindex == nil}
        # if not at correct position depending on player
        if (@x-$game_player.x).abs > ind*pix ||
            (@y-$game_player.y).abs > ind*pix
          # move towards player
          move_toward($game_player)
          # turn towards the player
          turn_toward_player
        else
          # integrate back into caterpillar
          update_ci(self.index)
          # calculate movement buffer commands depending on player's position
          calc_movement
          # set to follow mode
          @AI_data.state = 0
        end
      end
    end
    # call superclass method
    super
    # set stopped animation flag if actor's character is animated
    @step_anime = true if BlizzABS::Config::ANIMATED_IDS.include?(battler.id)
  end
  #----------------------------------------------------------------------------
  # calc_movement
  #  This method calculates a movement pattern to the player's current position
  #  when integrating back into the caterpillar, so this characeter doesn't
  #  need to go to the player's position, but can stay as far as possible.
  #----------------------------------------------------------------------------
  def calc_movement
    # get differences
    dx, dy = @x - $game_player.x, @y - $game_player.y
    # while differences exist
    while dx.abs > 0 || dy.abs > 0
      # add move command into direction to player
      if dx > 0 and dy > 0 # up left
        @buffer.push(7)
      elsif dx > 0 and dy < 0 # down right
        @buffer.push(1)
      elsif dx < 0 and dy > 0 # up left
        @buffer.push(9)
      elsif dx < 0 and dy < 0 # down right
        @buffer.push(3)
      elsif dx < 0 and dy == 0 # right
        @buffer.push(6)
      elsif dx > 0 and dy == 0 # left
        @buffer.push(4)
      elsif dx == 0 and dy < 0 # down
        @buffer.push(2)
      elsif dx == 0 and dy > 0 # up
        @buffer.push(8)
      end
      # decrease difference
      dx -= dx.sgn unless dx == 0
      dy -= dy.sgn unless dy == 0
    end
  end
  #----------------------------------------------------------------------------
  # update_attacked
  #  Processes being attacked and blinking animation.
  #----------------------------------------------------------------------------
  def update_attacked
    # if blinking
    if @blinking > 0
      # set blink opacity
      @opacity = 128 + 128 * ((@blinking+2)%4/2).abs
      # decrease blinking counter
      @blinking -= 1
    end
    # if attacked
    if @attacked > 0
      # decrease attacked counter
      @attacked -= 1
      # get thrown back
      move_backward
    end
  end
  #----------------------------------------------------------------------------
  # sprite_update
  #  Enhanced with movement system sprite handling.
  #----------------------------------------------------------------------------
  def sprite_update
    # update action spriteset animation if enabled
    super if BlizzABS::Config::ACTOR_ACTION_SPRITES
    # if no sprite extension
    if @current_sprite == ''
      # if jumping and turned on JUMPING_SPRTES
      if self.jumping? && BlizzABS::Config::JUMPING_SPRITES
        # set spriteset name
        @character_name = @character_name_org + '_jmp'
      # if running and turned on RUNNING_SPRTES
      elsif self.running? && BlizzABS::Config::RUNNING_SPRITES
        # set spriteset name
        @character_name = @character_name_org + '_run'
      # if sneaking and turned on SNEAKING_SPRTES
      elsif self.sneaking? && BlizzABS::Config::SNEAKING_SPRITES
        # set spriteset name
        @character_name = @character_name_org + '_snk'
      end
    end
  end
  #----------------------------------------------------------------------------
  # refresh
  #  Refreshes the character.
  #----------------------------------------------------------------------------
  def refresh(flag = false)
    # refresh all actors if self is controlled by player and not calling again
    BlizzABS.player.refresh if !flag && BlizzABS.player.player == self
    # if battler exists
    if battler == nil
      # set spriteset name
      @character_name_org = @character_name = ''
      # set spriteset hue
      @character_hue = 0
      # exit method
      return
    end
    # set spriteset name
    @character_name_org = @character_name = battler.character_name
    # set spriteset hue
    @character_hue = battler.character_hue
    # set opacity to full
    @opacity = 255
    # set blend type to normal
    @blend_type = 0
  end
  #----------------------------------------------------------------------------
  # update_ci
  #  index - new caterpillar index
  #  Integrates back into the caterpillar by setting up @cindex.
  #----------------------------------------------------------------------------
  def update_ci(ind = (@cindex == nil ? nil : self.index))
    # set new @cindex
    @cindex = ind
    # if index isn't removing from caterpillar
    if ind != nil
      # iterate through all actors in front of self
      (0...index).each {|i|
          # decrease @cindex each time an actor is missing in the caterpillar
          @cindex -= 1 if BlizzABS.player.actors[i].cindex == nil}
    end
    # update the @cindex of the actor behind if he exists
    BlizzABS.player.actors[index+1].update_ci if BlizzABS.player.actors[index+1] != nil
  end
  #----------------------------------------------------------------------------
  # update_buffer
  #  move - new command added into the buffer
  #  Handles the movement command delay system for caterpillar movement.
  #----------------------------------------------------------------------------
  def update_buffer(move)
    # exit if removed from caterpillar
    return if @cindex == nil || move == nil
    # if enforce emptying buffer command
    if move == nil
      # set enforcement to the current buffer size
      @force_movement = @buffer.size
    else
      # add new command into buffer
      @buffer.push(move)
      # set enforcement to the current buffer size if command is jumping
      @force_movement = @buffer.size if move.is_a?(Array) || move == false
    end
  end
  #----------------------------------------------------------------------------
  # passable?
  #  x - x-coordinate
  #  y - y-coordinate
  #  d - direction
  #  Checks the passability. (pixel movement)
  #----------------------------------------------------------------------------
  def passable?(x, y, d)
    # calculate new coordinates
    nx = x + (d == 6 ? 1 : d == 4 ? -1 : 0)
    ny = y + (d == 2 ? 1 : d == 8 ? -1 : 0)
    # impassable if new coordinates not valid
    return false unless $game_map.self_valid?(nx, ny)
    # passable through or pressing CTRL in DEBUG mode
    return true if $DEBUG && Input.press?(Input::CTRL) || @through
    # impassable if standing on impassable tile
    return false unless $game_map.self_passable?(x, y, d, self)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # if impassable in all directions
    unless $game_map.direction_passable?(nx, ny, 10 - d) &&
        $game_map.direction_passable?(nx, ny+pix-1, 10 - d) &&
        $game_map.direction_passable?(nx+pix-1, ny, 10 - d) &&
        $game_map.direction_passable?(nx+pix-1, ny+pix-1, 10 - d)
      # impassable
      return false
    end
    # impassable if any event is in the way
    return (self != $game_player || !$game_map.enemies(true).any? {|event|
        event.x >= nx/pix && event.x <= (nx+pix-1)/pix && event.y >= ny/pix &&
        event.y <= (ny+pix-1)/pix && !event.through && event.character_name != ''})
  end
  #----------------------------------------------------------------------------
  # jump_passable?
  #  x  - x-coordinate
  #  y  - y-coordinate
  #  nx - new x-coordinate
  #  ny - new y-coordinate
  #  Checks if there is a tile with JUMP_TAG tag so jumping isn't possible.
  #----------------------------------------------------------------------------
  def jump_passable?(x, y, d)
    # impassable if new coordinates not valid
    return false unless $game_map.self_valid?(x, y)
    # passable through or pressing CTRL in DEBUG mode
    return true if $DEBUG && Input.press?(Input::CTRL) || @through
    # passable if landing tile passable
    return ($game_map.self_passable?(x, y, 0, self))
  end
  #----------------------------------------------------------------------------
  # move_down
  #  turn_enabled - turning flag
  #  Moves. (pixel movement)
  #----------------------------------------------------------------------------
  def move_down(turn_enabled = true)
    # call superclass method and store result
    result = super
    # update buffer if self is controlled by player
    BlizzABS.player.update_buffer(2) if BlizzABS.player.player == self && result
    # return result
    return result
  end
  #----------------------------------------------------------------------------
  # move_left
  #  turn_enabled - turning flag
  #  Moves. (pixel movement)
  #----------------------------------------------------------------------------
  def move_left(turn_enabled = true)
    # call superclass method and store result
    result = super
    # update buffer if self is controlled by player
    BlizzABS.player.update_buffer(4) if BlizzABS.player.player == self && result
    # return result
    return result
  end
  #----------------------------------------------------------------------------
  # move_right
  #  turn_enabled - turning flag
  #  Moves. (pixel movement)
  #----------------------------------------------------------------------------
  def move_right(turn_enabled = true)
    # call superclass method and store result
    result = super
    # update buffer if self is controlled by player
    BlizzABS.player.update_buffer(6) if BlizzABS.player.player == self && result
    # return result
    return result
  end
  #----------------------------------------------------------------------------
  # move_up
  #  turn_enabled - turning flag
  #  Moves. (pixel movement)
  #----------------------------------------------------------------------------
  def move_up(turn_enabled = true)
    # call superclass method and store result
    result = super
    # update buffer if self is controlled by player
    BlizzABS.player.update_buffer(8) if BlizzABS.player.player == self && result
    # return result
    return result
  end
  #----------------------------------------------------------------------------
  # move_lower_left
  #  Moves. (pixel movement)
  #----------------------------------------------------------------------------
  def move_lower_left
    # call superclass method and store result
    result = super
    # update buffer if self is controlled by player
    BlizzABS.player.update_buffer(1) if BlizzABS.player.player == self && result
    # return result
    return result
  end
  #----------------------------------------------------------------------------
  # move_lower_right
  #  Moves. (pixel movement)
  #----------------------------------------------------------------------------
  def move_lower_right
    # call superclass method and store result
    result = super
    # update buffer if self is controlled by player
    BlizzABS.player.update_buffer(3) if BlizzABS.player.player == self && result
    # return result
    return result
  end
  #----------------------------------------------------------------------------
  # move_upper_left
  #  Moves. (pixel movement)
  #----------------------------------------------------------------------------
  def move_upper_left
    # call superclass method and store result
    result = super
    # update buffer if self is controlled by player
    BlizzABS.player.update_buffer(7) if BlizzABS.player.player == self && result
    # return result
    return result
  end
  #----------------------------------------------------------------------------
  # move_upper_right
  #  Moves. (pixel movement)
  #----------------------------------------------------------------------------
  def move_upper_right
    # call superclass method and store result
    result = super
    # update buffer if self is controlled by player
    BlizzABS.player.update_buffer(9) if BlizzABS.player.player == self && result
    # return result
    return result
  end
  #----------------------------------------------------------------------------
  # jump
  #  x - x-coordinate
  #  y - y-coordinate
  #  Jumps. (pixel movement)
  #----------------------------------------------------------------------------
  def jump(x_plus, y_plus, d = nil)
    # if direction is unknown
    if d == nil
      # determines direction
      if x_plus > 0 and y_plus > 0 # jumping down right
        d = 3
      elsif x_plus > 0 and y_plus < 0 # jumping up left
        d = 9
      elsif x_plus < 0 and y_plus > 0 # jumping down right
        d = 1
      elsif x_plus < 0 and y_plus < 0 # jumping up left
        d = 7
      elsif x_plus < 0 and y_plus == 0 # jumping left
        d = 4
      elsif x_plus > 0 and y_plus == 0 # jumping right
        d = 6
      elsif x_plus == 0 and y_plus < 0 # jumping up
        d = 8
      elsif x_plus == 0 and y_plus > 0 # jumping down
        d = 2
      end
    end
    # if jumped
    if super
      # if self is controlled by player
      if BlizzABS.player.player == self
        # update buffer
        BlizzABS.player.update_buffer([d, @move_speed - BlizzABS.player.normal_speed])
      end
      # jumped
      return true
    end
    # not jumped
    return false
  end
  #----------------------------------------------------------------------------
  # moveto
  #  x - x-coordinate
  #  y - y-coordinate
  #  Moves the player instantly to a postion, moves all actors and centers the
  #  screen upon the player.
  #----------------------------------------------------------------------------
  def moveto(x, y)
    # call superclass method 
    super
    # call controller method if self is controlled by player
    BlizzABS.player.moveto(x, y) if BlizzABS.player.player == self
  end
  #----------------------------------------------------------------------------
  # center
  #  x - x-coordinate
  #  y - y-coordinate
  #  Centers the screen upon the player's character if the character is
  #  controlled by the player.
  #----------------------------------------------------------------------------
  def center(x, y)
    BlizzABS.player.center(x, y, flag) if BlizzABS.player.player == self
  end
  #----------------------------------------------------------------------------
  # overriding move_type_custom
  #----------------------------------------------------------------------------
  alias move_type_custom_blizzabs_later move_type_custom
  def move_type_custom
    # call original method
    move_type_custom_blizzabs_later
    # if self is controlled by player and current command is "Set move speed"
    if BlizzABS.player.player == self && @move_route != nil &&
        @move_route_index < @move_route.list.size &&
        @move_route.list[@move_route_index].code == 29
      # set new normal speed
      BlizzABS.player.normal_speed = @move_speed
    end
  end
  #----------------------------------------------------------------------------
  # move_toward
  #  character - next actor in the line
  #  Moves towards a character.
  #----------------------------------------------------------------------------
  def move_toward(character)
    # get pixelmovement rate
    pix = BlizzABS.pixel
    # get x and y differences
    dx = @real_x - character.real_x
    dy = @real_y - character.real_y
    # exit if already same position
    return if dx == 0 && dy == 0
    # determines where to move according to the x and y differences
    if dx > 0 && dy > 0 # character is up left
      move_left if !move_upper_left && !move_up
    elsif dx > 0 && dy < 0 # character is down left
      move_left if !move_lower_left && !move_down
    elsif dx < 0 && dy > 0 # character is up right
      move_right if !move_upper_right && !move_up
    elsif dx < 0 && dy < 0 # character is down right
      move_right if !move_lower_right && !move_down
    elsif dx < 0 && dy == 0 # character is right
      move_right
    elsif dx > 0 && dy == 0 # character is left
      move_left
    elsif dx == 0 && dy < 0 # character is down
      move_down
    elsif dx == 0 && dy > 0 # character is up
      move_up
    end
  end
  #----------------------------------------------------------------------------
  # dead?
  #  Checks if the assigned battler is dead if existent.
  #----------------------------------------------------------------------------
  def dead?
    return (battler == nil || battler.dead?)
  end
  #----------------------------------------------------------------------------
  # attacked=
  #  val - number
  #  Sets the attacked counter and blinking value.
  #----------------------------------------------------------------------------
  def attacked=(val)
    # call superclass method
    super
    # set blinking counter if not defending
    @blinking = val * 8 unless @defending
  end
  #----------------------------------------------------------------------------
  # pattern
  #  Overriding method for accessing the pattern number of the spriteset.
  #----------------------------------------------------------------------------
  def pattern
    # if not in action and jumping and turned on JUMPING_SPRITES
    if self.in_action == 0 && jumping? && BlizzABS::Config::JUMPING_SPRITES
      # pattern 1 if jumping up, 3 if falling down again else 2
      return (@jump_count > @jump_peak + 1 ? 1 :
          (@jump_count < @jump_peak - 1 ? 3 : 2))
    end
    # call superclass method
    return super
  end
  #----------------------------------------------------------------------------
  # check_event_trigger_touch
  #  Checks event touching if self is controlled by player.
  #----------------------------------------------------------------------------
  def check_event_trigger_touch(x, y)
    BlizzABS.player.check_event_trigger_touch(x, y) if BlizzABS.player.player == self
  end
  #----------------------------------------------------------------------------
  # index
  #  Returns own position in actor array.
  #----------------------------------------------------------------------------
  def index
    return BlizzABS.player.actors.index(self)
  end
  #----------------------------------------------------------------------------
  # running?
  #  Checks if the player is running.
  #----------------------------------------------------------------------------
  def running?
    return (BlizzABS::Config::RUN_SPEED == @move_speed)
  end
  #----------------------------------------------------------------------------
  # sneaking?
  #  Checks if the player is sneaking.
  #----------------------------------------------------------------------------
  def sneaking?
    return (BlizzABS::Config::SNEAK_SPEED == @move_speed)
  end
  #----------------------------------------------------------------------------
  # atk_offset
  #  Gets an offset if necessary.
  #----------------------------------------------------------------------------
  def atk_offset
    return ((@current_sprite[0, 4] == '_atk' && @direction == 2 &&
        @s_count < 12) ? BlizzABS::Config::ACTOR_SPRITE_Y_OFFSET : 0)
  end
  #----------------------------------------------------------------------------
  # screen_z
  #  height - height on the screen
  #  Gets character's z-coordinate.
  #----------------------------------------------------------------------------
  def screen_z(height = 0)
    return (super - (index == nil ? BlizzABS::Config::MAX_PARTY : index))
  end

end

#==============================================================================
# Game_Player
#------------------------------------------------------------------------------
#  This class serves as override, so a Map_Actor class is loaded as current
#  player.
#==============================================================================

class Game_Player < Map_Actor
  
  #----------------------------------------------------------------------------
  # Initialization
  #----------------------------------------------------------------------------
  def initialize
    # call superclass method for first actor
    super(0)
  end
  
end

#==============================================================================
# Map_Enemy
#------------------------------------------------------------------------------
#  This class handles a map enemy character. It supports pixel movement,
#  complete AI handling, advanced sprite handling and battle handling.
#==============================================================================

class Map_Enemy < Map_Battler
  
  # setting all accessable variables
  attr_accessor :event_id
  attr_reader   :AI_data
  attr_reader   :event
  attr_reader   :trigger
  attr_reader   :list
  attr_reader   :page
  attr_reader   :starting
  attr_reader   :execute
  attr_reader   :force_move
  attr_reader   :precondition
  #----------------------------------------------------------------------------
  # Initialization
  #----------------------------------------------------------------------------
  def initialize(map_id, event, id = 0, event_id = 0, attributes = 0x0000)
    # if respawning system active
    if event.is_a?(Map_Enemy)
      # get aggression of earlier enemy
      aggr = event.AI_data.origin_aggressive
      # get boss flag of earlier enemy
      boss = event.boss
      # get event ID of earlier enemy
      event_id = event.event_id
      # get own ID of earlier enemy
      id = event.id
      # get event of earlier enemy
      event = event.event
    else
      # get aggression from attribute
      aggr = (attributes & 0x0001 != 0x0001)
      # get boss flag from attribute
      boss = (attributes & 0x0002 == 0x0002)
    end
    # give the enemy all attributes of a DX character
    super()
    # set map ID
    @map_id = map_id
    # @event is needed for respawn
    @event = event
    # move to starting position
    moveto(@event.x, @event.y)
    # set erased flag
    @erased = false
    # set starting flag
    @starting = false
    # set execute flag
    @execute = false
    # set through flag
    @through = true
    # set precondition flag
    @precondition = false
    # set character spriteset name
    @character_name_org = @character_name = ''
    # refresh
    refresh
    # the database enemy
    @enemy = $data_enemies[id]
    # the battler
    @battler = Game_Enemy.new(@enemy)
    # create AI Data
    @AI_data = AI_Data_Map_Enemy.new(id, @enemy.maxhp, @enemy.eva, aggr, boss)
    # own ID
    @id = id
    # own event ID
    @event_id = event_id
    # create array of moving commands
    @force_move = []
    # set turning flag
    @turn_flag = false
  end
  #----------------------------------------------------------------------------
  # boss
  #  Quick access to the boss flag.
  #----------------------------------------------------------------------------
  def boss
    return @AI_data.boss
  end
  #----------------------------------------------------------------------------
  # agressive
  #  Quick access to the aggressive flag.
  #----------------------------------------------------------------------------
  def aggressive
    return @AI_data.aggressive
  end
  #----------------------------------------------------------------------------
  # in_action
  #  Overriding method needed for sprite animation.
  #----------------------------------------------------------------------------
  def in_action
    # in action if sprite add-on is there
    return (@current_sprite != '' ? 1 : @in_action)
  end
  #----------------------------------------------------------------------------
  # clear_starting
  #  Clears the starting flag
  #----------------------------------------------------------------------------
  def clear_starting
    @starting = false
  end
  #----------------------------------------------------------------------------
  # start
  #  Setups the starting event code.
  #----------------------------------------------------------------------------
  def start
    # event code exists
    if @list.size > 1
      # store interpreter
      @interpreter = $game_system.map_interpreter
      # setup code
      @interpreter.setup(@list, @event_id)
      # start
      @interpreter.setup_starting_event
      # set execute flag
      @execute = true
    end
  end
  #----------------------------------------------------------------------------
  # erase
  #  Dummy method.
  #----------------------------------------------------------------------------
  def erase
  end
  #----------------------------------------------------------------------------
  # over_trigger?
  #  Dummy method.
  #----------------------------------------------------------------------------
  def over_trigger?
    return false
  end
  #--------------------------------------------------------------------------
  # refresh
  #  Refreshes the character.
  #--------------------------------------------------------------------------
  def refresh
    # initialize
    new_page = nil
    # if not erased
    unless @erased
      # iterate through all pages in reverse order
      @event.pages.reverse.each {|page|
          # temporary variable
          c = page.condition
          # switch 1 condition test
          next if c.switch1_valid && !$game_switches[c.switch1_id]
          # switch 2 condition test
          next if c.switch2_valid && !$game_switches[c.switch2_id]
          # variable condition test
          if c.variable_valid
            # next page if condition not fulfilled
            next if $game_variables[c.variable_id] < c.variable_value
          end
          # self switch condition test
          if c.self_switch_valid
            # temporary variable
            key = [@map_id, @event.id, c.self_switch_ch]
            # next page if condition not fulfilled
            next unless $game_self_switches[key]
          end
          # set local variable
          new_page = page
          # stop looping
          break}
    end
    # end method if event page is the same as last time
    return if new_page == @page
    # set as current event page
    @page = new_page
    # if no page fulfills conditions
    if @page == nil
      # set up variables
      @tile_id = 0
      @character_name_org = @character_name = ''
      @character_hue = 0
      @move_type = 0
      @through = true
      @trigger = nil
      @list = nil
      @interpreter = nil
      @precondition = false
      # exit method
      return
    end
    # set up variables
    @tile_id = @page.graphic.tile_id
    @character_name_org = @character_name = @page.graphic.character_name
    @character_hue = @page.graphic.character_hue
    # if direction is different
    if @original_direction != @page.graphic.direction
      @direction = @page.graphic.direction
      @original_direction = @direction
      @prelock_direction = 0
    end
    # if pattern is different
    if @original_pattern != @page.graphic.pattern
      @pattern = @page.graphic.pattern
      @original_pattern = @pattern
    end
    @opacity = @page.graphic.opacity
    @blend_type = @page.graphic.blend_type
    @move_type = @page.move_type
    @move_speed = @page.move_speed
    @move_frequency = @page.move_frequency
    @move_route = @page.move_route
    @move_route_index = 0
    @move_route_forcing = false
    @walk_anime = @page.walk_anime
    @step_anime = @page.step_anime
    @direction_fix = @page.direction_fix
    @through = @page.through
    @always_on_top = @page.always_on_top
    @trigger = @page.trigger
    @list = @page.list
    # set precondtion flag
    @precondition = true
  end
  #----------------------------------------------------------------------------
  # update
  #  Executes the enemy behaviour according to the AI.
  #----------------------------------------------------------------------------
  def update
    # don't update if outside of ABSEAL range
    return unless self.update?
    # reset loop animation
    @loop_animation_id = 0
    # reset spriteset name
    @character_name = @character_name_org
    # update spriteset animation if enabled
    sprite_update if BlizzABS::Config::ENEMY_ACTION_SPRITES
    # if interpreter exists
    if @interpreter != nil
      # if running
      if @interpreter.running?
        # update
        @interpreter.update
        # exit method
        return
      # if opacity is 0
      elsif @opacity == 0
        # set execute flag
        @execute = false
        # set erased flag
        @erased = true
        # refresh
        refresh
      end
    end
    # return if page doesn't exist
    return if @page == nil
    # calcuation of the update pattern number
    factor = ((Graphics.frame_rate*2+@id)%(rand(11)+45)+1) * (rand(2)+1)
    # refreshes the AI after a certain ammount of time
    @AI_data.refresh if Graphics.frame_count % (factor*3.7).to_i == 0
    # defines the current move speed and sets new AI behaviour
    @move_speed = AI.behaviour(self)
    # if no move route commands
    if @force_move == []
      # set turning flag
      @turn_flag = false
    else
      # get next moving command and execute special movement override
      case @force_move.shift
      when 1 then move_lower_left(11)
      when 2 then move_down(11, @turn_flag)
      when 3 then move_lower_right(11)
      when 4 then move_left(11, @turn_flag)
      when 6 then move_right(11, @turn_flag)
      when 7 then move_upper_left(11)
      when 8 then move_up(11, @turn_flag)
      when 9 then move_upper_right(11)
      end
    end
    # if already moving or special state
    if moving? && ![5, 6].include?(@AI_data.state)
      # update the event with the superclass method
      super
      # exit method
      return
    end
    # reset defending
    self.defending = false
    # test the AI state
    case @AI_data.state
    # idle
    when 0
      # after a certain ammount of time
      if Graphics.frame_count % factor == 0
        # either turn random (33% chance) or move random (67% chance)
        rand(3) == 0 ? turn_random : move_random
      end
    # seen/heard the player
    when 1
      # turn toward the player no matter what (follows the player's movement)
      turn_toward_player
      # moves toward the player
      move_toward_player
      # set frame penalty
      set_action(0.8)
    # in_action the player
    when 2
      # turn toward the player no matter what (follows the player's movement)
      turn_toward_player
      # attacks the player
      use_attack
    # in_action with a skill
    when 3
      # turn toward the player no matter what (follows the player's movement)
      turn_toward_player
      # attacks the player with a skill
      use_skill($data_skills[@battler.current_action.skill_id])
    # defend
    when 4
      # turn toward the player no matter what (follows the player's movement)
      turn_toward_player
      # defending is true
      self.defending = true
      # set defend time unless already defending
      set_action(rand(3)*1.0+1) unless self.in_action > 0
    # run away
    when 5
      # turn away from player no matter what (follows the player's movement)
      turn_away_from_player
      # move away from player
      move_away_from_player
      # if really running away out of fear
      if @AI_data.fear > 0
        # set loop animation
        @loop_animation_id = BlizzABS::Config::FLEE_LOOP_ANIMATION_ID
      end
    # attack shock state
    when 6
      # turns toward the player
      turn_toward_player
      # freezes the direction
      @turn_flag = true
      # simulation of getting thrown back
      move_away_from_player
    # memory
    when 7
      # turns toward the player's last coordinate
      turn_toward_player(false)
      # moves toward the player's last coordinate
      move_toward_player(false)
      # set penalty flag
      set_action(0.8)
    end
    # update the event with the superclass method
    super
  end
  #----------------------------------------------------------------------------
  # attack_effect
  #  character - the character that holds attack data (can be projectile)
  #  _battler  - the attacking battler
  #  This method executes additional attack processing upon the enemy.
  #----------------------------------------------------------------------------
  def attack_effect(character, _battler)
    # store last HP
    last_hp = @battler.hp
    # call superclass method and store result
    result = super
    # call additional process if damage done to HP
    damage_test(last_hp-@battler.hp) if result && last_hp > @battler.hp
    # return original result
    return result
  end
  #----------------------------------------------------------------------------
  # skill_effect
  #  character - the character that holds skill use (can be projectile)
  #  _battler  - the skill using battler
  #  skill     - the skill
  #  This method executes additional skill processing upon the enemy.
  #----------------------------------------------------------------------------
  def skill_effect(character, _battler, skill)
    # store last HP
    last_hp = @battler.hp
    # call superclass method and store result
    result = super
    # call additional process if damage done to HP
    damage_test(last_hp-@battler.hp) if result && last_hp > @battler.hp
    # return original result
    return result
  end
  #----------------------------------------------------------------------------
  # item_effect
  #  character - the character that holds item use (can be projectile)
  #  item      - the item
  #  This method executes additional item processing upon the enemy.
  #----------------------------------------------------------------------------
  def item_effect(character, item)
    # store last HP
    last_hp = @battler.hp
    # call superclass method and store result
    result = super
    # call additional process if damage done to HP
    damage_test(last_hp-@battler.hp) if result && last_hp > @battler.hp
    # return original result
    return result
  end
  #----------------------------------------------------------------------------
  # damage_test
  #  This method executes the actual additional damage effect used by the AI.
  #----------------------------------------------------------------------------
  def damage_test(damage)
    # accumulate damage 
    @AI_data.dmg.push(damage)
    # set to aggressive
    @AI_data.aggressive = true
  end
  #----------------------------------------------------------------------------
  # dead?
  #  Checks if the enemy is dead.
  #----------------------------------------------------------------------------
  def dead?
    return (@battler == nil || @battler.dead?)
  end
  #----------------------------------------------------------------------------
  # exp
  #  Returns the experience.
  #----------------------------------------------------------------------------
  def exp
    return @battler.exp
  end
  #----------------------------------------------------------------------------
  # gold
  #  Returns the gold.
  #----------------------------------------------------------------------------
  def gold
    return @battler.gold
  end
  #----------------------------------------------------------------------------
  # move_random
  #  Moves into a random direction. (8-way)
  #----------------------------------------------------------------------------
  def move_random
    case rand(8)
    when 0 then move_down(0)
    when 1 then move_left(0)
    when 2 then move_right(0)
    when 3 then move_up(0)
    when 4 then move_lower_left
    when 5 then move_upper_left
    when 6 then move_lower_right
    when 7 then move_upper_right
    end
  end
  #----------------------------------------------------------------------------
  # move_down
  #  mode  - flag for overriding
  #  check - turning flag
  #  Moves. (pixel movement)
  #----------------------------------------------------------------------------
  def move_down(mode = true, check = true)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # which type of moving
    case mode
    # override and set moving route
    when 0 then rand(pix*2).times{@force_move.push(2)}
    # move
    when 11 then super(check)
    # re-routing the method
    else
      # set moving route
      pix.times{@force_move.push(2)}
      # set turning flag
      @turn_flag = mode
    end
  end
  #----------------------------------------------------------------------------
  # move_left
  #  mode  - flag for overriding
  #  check - turning flag
  #  Moves. (pixel movement)
  #----------------------------------------------------------------------------
  def move_left(mode = true, check = false)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # which type of moving
    case mode
    # override and set moving route
    when 0 then rand(pix*2).times{@force_move.push(4)}
    # move
    when 11 then super((!check))
    # re-routing the method
    else
      # set moving route
      pix.times{@force_move.push(4)}
      # set turning flag
      @turn_flag = mode
    end
  end
  #----------------------------------------------------------------------------
  # move_right
  #  mode  - flag for overriding
  #  check - turning flag
  #  Moves. (pixel movement)
  #----------------------------------------------------------------------------
  def move_right(mode = true, check = false)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # which type of moving
    case mode
    # override and set moving route
    when 0 then rand(pix*2).times{@force_move.push(6)}
    # move
    when 11 then super((!check))
    # re-routing the method
    else
      # set moving route
      pix.times{@force_move.push(6)}
      # set turning flag
      @turn_flag = mode
    end
  end
  #----------------------------------------------------------------------------
  # move_up
  #  mode  - flag for overriding
  #  check - turning flag
  #  Moves. (pixel movement)
  #----------------------------------------------------------------------------
  def move_up(mode = true, check = false)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # which type of moving
    case mode
    # override and set moving route
    when 0 then rand(pix*2).times{@force_move.push(4)}
    # move
    when 11 then super((!check))
    # re-routing the method
    else
      # set moving route
      pix.times{@force_move.push(4)}
      # set turning flag
      @turn_flag = mode
    end
  end
  #----------------------------------------------------------------------------
  # move_lower_left
  #  mode - overriding flag
  #  Moves diagonal. (pixel movement)
  #----------------------------------------------------------------------------
  def move_lower_left(mode = 0)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # which type of moving
    case mode
    # override and set moving route
    when 0 then rand(pix*2).times{@force_move.push(1)}
    # move
    when 11 then super()
    end
  end
  #----------------------------------------------------------------------------
  # move_lower_right
  #  mode - overriding flag
  #  Moves diagonal. (pixel movement)
  #----------------------------------------------------------------------------
  def move_lower_right(mode = 0)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # which type of moving
    case mode
    # override and set moving route
    when 0 then rand(pix*2).times{@force_move.push(3)}
    # move
    when 11 then super()
    end
  end
  #----------------------------------------------------------------------------
  # move_upper_left
  #  mode - overriding flag
  #  Moves diagonal. (pixel movement)
  #----------------------------------------------------------------------------
  def move_upper_left(mode = 0)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # which type of moving
    case mode
    # override and set moving route
    when 0 then rand(pix*2).times{@force_move.push(7)}
    # move
    when 11 then super()
    end
  end
  #----------------------------------------------------------------------------
  # move_upper_right
  #  mode - overriding flag
  #  Moves diagonal. (pixel movement)
  #----------------------------------------------------------------------------
  def move_upper_right(mode = 0)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # which type of moving
    case mode
    # override and set moving route
    when 0 then rand(pix*2).times{@force_move.push(9)}
    # move
    when 11 then super()
    end
  end
  #----------------------------------------------------------------------------
  # overriding move_type_custom
  #----------------------------------------------------------------------------
  alias move_type_custom_blizzabs_later move_type_custom
  def move_type_custom
    # call original method
    move_type_custom_blizzabs_later
    # exit method if jumping or moving
    return if jumping? || moving?
    # if move route exists and basic movement command
    if @move_route_index < @move_route.list.size &&
        @move_route.list[@move_route_index].code <= 14
      # increase move_route_index
      @move_route_index += 1
    end
  end
  #----------------------------------------------------------------------------
  # passable?
  #  x - x-coordinate
  #  y - y-coordinate
  #  d - facing direction
  #  Checks the passability.
  #----------------------------------------------------------------------------
  def passable?(x, y, d)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # get new coordinates
    nx = x + (d == 6 ? 1 : d == 4 ? -1 : 0)
    ny = y + (d == 2 ? 1 : d == 8 ? -1 : 0)
    # impassable if new coordinates not valid
    return false unless $game_map.self_valid?(nx, ny)
    # impassable if current tile is impassable
    return false unless $game_map.self_passable?(x, y, d, self)
    # if all directions impassable
    unless $game_map.direction_passable?(nx, ny, 10 - d) &&
        $game_map.direction_passable?(nx, ny+pix-1, 10 - d) &&
        $game_map.direction_passable?(nx+pix-1, ny, 10 - d) &&
        $game_map.direction_passable?(nx+pix-1, ny+pix-1, 10 - d)
      # impassable
      return false
    end
    # impassable if any event is in the way
    return (!$game_map.enemies(true).any? {|event|
        event.x >= nx/pix && event.x <= (nx+pix-1)/pix &&
        event.y >= ny/pix && event.y <= (ny+pix-1)/pix &&
        !event.through && event.character_name != ''})
  end
  #----------------------------------------------------------------------------
  # move_toward_player
  #  is_player - moving toward the player or his remembered last position
  #  Processes moving toward the player or his last remembered postion.
  #----------------------------------------------------------------------------
  def move_toward_player(is_player = true)
    # get pixel movement rate
    pix = BlizzABS.pixel
    # is it the player
    if is_player
      # calculate differences in x and y
      dx, dy = @x - $game_player.x, @y - $game_player.y
    else # or only his remembered position
      # calculate differences in x and y
      dx = @AI_data.find_x > 0 ? @x - @AI_data.find_x : 0
      dy = @AI_data.find_y > 0 ? @y - @AI_data.find_y : 0
    end
    # determines where to move according to the x and y differences
    if dx < 0 && dy.abs <= pix*3.0/2 # player is right
      rand(pix*2).times {@force_move.push(6)}
    elsif dx > 0 && dy.abs <= pix*3.0/2 # player is left
      rand(pix*2).times {@force_move.push(4)}
    elsif dx.abs <= pix*3.0/2 && dy < 0 # player is down
      rand(pix*2).times {@force_move.push(2)}
    elsif dx.abs <= pix*3.0/2 && dy > 0 # player is up
      rand(pix*2).times {@force_move.push(8)}
    elsif dx > 0 && dy > 0 # player is up left
      rand(pix*2).times {@force_move.push(7)}
    elsif dx > 0 && dy < 0 # player is down left
      rand(pix*2).times {@force_move.push(1)}
    elsif dx < 0 && dy > 0 # player is up right
      rand(pix*2).times {@force_move.push(9)}
    elsif dx < 0 && dy < 0 # player is down right
      rand(pix*2).times {@force_move.push(3)}
    end
  end
  #----------------------------------------------------------------------------
  # move_away_from_player
  #  Moves away from the player. (pixel movement)
  #----------------------------------------------------------------------------
  def move_away_from_player
    # get pixel movement rate
    pix = BlizzABS.pixel
    # calculates differences in x and y
    dx, dy = @x - $game_player.x, @y - $game_player.y
    # sets movement route depending on the x and y differences
    if dx < 0 && dy.abs <= pix/2 # player is right
      @force_move.push(4)
    elsif dx > 0 && dy.abs <= pix/2 # player is left
      @force_move.push(6)
    elsif dx.abs <= pix/2 && dy < 0 # player is down
      @force_move.push(8)
    elsif dx.abs <= pix/2 && dy > 0 # player is up
      @force_move.push(2)
    elsif dx > 0 && dy > 0 # player is up left
      @force_move.push(3)
    elsif dx > 0 && dy < 0 # player is down left
      @force_move.push(9)
    elsif dx < 0 && dy > 0 # player is up right
      @force_move.push(1)
    elsif dx < 0 && dy < 0 # player is down right
      @force_move.push(7)
    end
  end
  #----------------------------------------------------------------------------
  # turn_toward_player
  #  is_player - turning toward the player or his remembered last position
  #  Processes turning toward the player or his last remembered postion.
  #----------------------------------------------------------------------------
  def turn_toward_player(is_player = true)
    # is it the player
    if is_player
      # calculates differences in x and y
      dx, dy = @x - $game_player.x, @y - $game_player.y
    # or only his remembered position
    else
      # calculates differences in x and y
      dx = @AI_data.find_x > 0 ? @x - @AI_data.find_x : 0
      dy = @AI_data.find_y > 0 ? @y - @AI_data.find_y : 0
    end
    # determines where to turn according to the x and y differences
    if dx < 0 && dx.abs >= dy.abs # player is right
      turn_right
    elsif dx > 0 && dx.abs >= dy.abs # player is left
      turn_left
    elsif dy < 0 # player is down
      turn_down
    elsif dy > 0 # player is up
      turn_up
    end
  end
  #----------------------------------------------------------------------------
  # turn_away_from_player
  #  Moves away from the player. (pixel movement)
  #----------------------------------------------------------------------------
  def turn_away_from_player
    # calculates differences in x and y
    dx, dy = @x - $game_player.x, @y - $game_player.y
    # determines where to turn according to the x and y differences
    if dx < 0 && dx.abs >= dy.abs # player is right
      turn_left
    elsif dx > 0 && dx.abs >= dy.abs # player is left
      turn_right
    elsif dy < 0 # player is down
      turn_up
    elsif dy > 0 # player is up
      turn_down
    end
  end
  #----------------------------------------------------------------------------
  # check_event_trigger_touch
  #  Dummy method.
  #----------------------------------------------------------------------------
  def check_event_trigger_touch(x, y)
  end
  #----------------------------------------------------------------------------
  # atk_offset
  #  Gets an offset if necessary.
  #----------------------------------------------------------------------------
  def atk_offset
    return ((@current_sprite[0, 4] == '_atk' && @direction == 2 &&
        @s_count < 12) ? BlizzABS::Config::ENEMY_SPRITE_Y_OFFSET : 0)
  end
  
end

#==============================================================================
# Projectile
#------------------------------------------------------------------------------
#  This class handles projectiles used in battle. It supports pixel movement
#  and deals attack/skill/item according to the battler's state when the
#  projectile was created.
#==============================================================================

class Projectile < Map_Battler
  
  #----------------------------------------------------------------------------
  # Initialization
  #  character_name - spriteset file name
  #  creator        - character that created the projectile or item
  #  id             - skill id
  #  direction      - initial facing direction
  #  target         - data pack to determine movement and target
  #----------------------------------------------------------------------------
  def initialize(character_name, creator, id, distance, type, target_class,
                 dead_type, explode = nil)
    # call superclass method without arguments
    super()
    # id of weapon/skill/item
    @id = id
    # defines whether exploding or not
    @explode = explode
    # set type
    @type = type
    # target class
    @classe = target_class
    # targetting dead or alive targets
    @dead_type = dead_type
    # a number of projectile appear instantly while other need a moment
    @request_time = ([0, 5, 6, 7, 9, 10, 11].include?(type) ? 4 : 10)
    # set character_name
    @character_name = character_name
    # set coordinates to the same a the creator
    @real_x, @real_y = creator.real_x, creator.real_y
    # move in creator's facing direction slightly
    case creator.direction
    when 2 then @real_y += 64
    when 4 then @real_x -= 64
    when 6 then @real_x += 64
    when 8 then @real_y -= 64
    end
    # if distance is a fixed target
    if distance.is_a?(Game_Character)
      # set target, speed and projectile range
      @target, @move_speed, d = distance, 3, 2
    else
      # set target, speed and projectile range
      @target, @move_speed, d = nil, 5, (distance-1) * BlizzABS.pixel
    end
    # set map coordinates to real coordinates, taking pixel movement into account
    @x, @y = @real_x * BlizzABS.pixel / 128, @real_y * BlizzABS.pixel / 128
    # set up final position depending on creator's facing direction
    case creator.direction
    when 2 then @y += d
    when 4 then @x -= d
    when 6 then @x += d
    when 8 then @y -= d
    end
    # set opacity
    @opacity = 255
    # create a copy of the battler
    @battler_copy = creator.battler.clone
    # store the creator
    @creator = creator
    # create array of already hit targets
    @hit = []
    # set direction to the same as the creator's
    @direction = creator.direction
    # set termination flag
    @terminate = false
    # animate and goes through anything
    @walk_anime = @step_anime = @through = true
    # freeze player's action in case of returning projectile
    @creator.freeze_action = (@type == 0)
    # helping variable
    @accelerate = 0
  end
  #----------------------------------------------------------------------------
  # create
  #  After creation time delay expires, the sprite is being created.
  #----------------------------------------------------------------------------
  def create
    # create own sprite
    sprite = Sprite_Character.new($scene.spriteset.viewport1, self)
    # update sprite once
    sprite.update
    # add to spriteset
    $scene.spriteset.character_sprites.push(sprite)
  end
  #----------------------------------------------------------------------------
  # update?
  #  Overrides ABSEAL as it gets terminated as soon as it goes out of the
  #  screen anyway, so some process time is being saved.
  #----------------------------------------------------------------------------
  def update?
    return true
  end
  #----------------------------------------------------------------------------
  # execute
  #  Executes the projectile's effect.
  #----------------------------------------------------------------------------
  def execute(target = @target)
    # if item
    if @type >= 9
      # execute item
      target.item_effect(self, $data_items[@id])
    # if skill
    elsif @type >= 5
      # execute skill
      target.skill_effect(self, @battler_copy, $data_skills[@id])
    else
      # execute attack
      target.attack_effect(self, @battler_copy)
      # if shot item
      if @type == 3
        # store damage
        dmg = target.battler.damage
        # execute item
        target.item_effect(self, $data_items[@id])
        # if damage is a number and any damage done
        if target.battler.damage.is_a?(Numeric) &&
          (target.battler.hpdamage > 0 || target.battler.spdamage > 0)
          # add attack damage if attack damage was a number
          target.battler.damage += dmg if dmg.is_a?(Numeric)
        # if no damage done with item
        elsif target.battler.hpdamage == 0 && target.battler.spdamage == 0
          # set back to attack damage
          target.battler.damage = dmg
        end
      end
    end
    # add to already hit targets
    @hit.push(target)
    # sets flag for self-termination if necessary
    @terminate = true unless [0, 1, 6, 10].include?(@type)
  end
  #--------------------------------------------------------------------------
  # update
  #  Processes projectile movement.
  #--------------------------------------------------------------------------
  def update
    # if projectile creation request hasn't expired yet
    if @request_time > 0
      # decrease counter
      @request_time -= 1
      # abort method or create whether projectile creation request has expired
      @request_time == 0 ? create : return
    end
    # if accelerating counter
    if @accelerate > 0
      # decrease accelerating counter
      @accelerate -= 1
      # accelerate if accelerating counter expired
      @move_speed = 5 if @accelerate == 0
    end
    # additional stop animation updates depending on speed
    ([@move_speed - 2, 3].min).times {update_stop}
    # find target or return to creator depending on the type
    case @type
    when 1 then @x, @y = @creator.x, @creator.y
    when 8, 12 then @x, @y = @target.x, @target.y
    end
    # turn toward the target position
    turn_toward_target
    # get pixel movement rate
    pix = BlizzABS.pixel
    # if not moving or out of screen hitting a wall
    if !moving? || out_of_screen(128) ||
        $game_map.terrain_tag(@real_x*pix/128, @real_y*pix/128) ==
        BlizzABS::Config::WALL_TAG
      # which internal type of projectile
      case @type
      when 0
        # returning projectil returns now
        @type = 1
        # set coordinates to creator's
        @x, @y = @creator.x, @creator.y
        # slow down
        @move_speed = 4
        # set acceleration count
        @accelerate = 5
      # homing projectile ready for pursuit
      when 7, 11 then @type, @move_speed, @accelerate = @type + 1, 4, 9
      # homing projectile hit the target
      when 8, 12 then execute
      else
        # set termination flag
        @terminate = true
        # unfreeze creator action
        @creator.freeze_action = false
        # depending on type, drop a weapon/item
        case @type
        when 3, 9, 10 then Drop_Event.new($data_items[@id], @x.to_i, @y.to_i)
        when 4 then Drop_Event.new($data_weapons[@id], @x.to_i, @y.to_i)
        end
      end
    end
    # if homing projetile that is pursuing a target
    if [7, 8, 11, 12].include?(@type)
      # create rectangle
      rect = Rect.new(@target.real_x, @target.real_y, 128, 128)
      # execute action if target's and projectile's rectangles intersect
      execute if BlizzABS.intersection(rect, Rect.new(@real_x+32, @real_y+32, 64, 64))
    # if not out of screen at all
    elsif !out_of_screen(0)
      # if moving and not returning projectile and close to final position
      if moving? && ![1, 7, 8, 11, 12].include?(@type) &&
         (@real_x-@x*128/pix).abs < 128 && (@real_y-@y*128/pix).abs < 128
        # slow down
        @move_speed = 4
        # start fade out animation if skill
        @fade_out = true if [5, 6].include?(@type)
      end
      # iterate through all battlers
      ($game_map.enemies + BlizzABS.player.actors).each {|battler|
          rect = Rect.new(battler.real_x, battler.real_y, 128, 128)
          # if battler can be hit and battler and projectile intersect
          if battler.battler != nil && battler.is_a?(@classe) &&
              @dead_type ^ battler.battler.dead? &&
              BlizzABS.intersection(rect, Rect.new(@real_x+32, @real_y+32, 64, 64))
            # execute action unless already hit
            execute(battler) unless @hit.include?(battler)
            # if exploding skill/item
            if @explode
              # iterate through all map battlers
              ($game_map.enemies + BlizzABS.player.actors).each {|ch|
                  # get differences in coordinates
                  dx, dy = ch.real_x-battler.real_x, ch.real_y-battler.real_y
                  # create affection area shape
                  r = [battler.real_x+64, battler.real_y+64, @explode[0]*128, 0]
                  # create target position rectangle
                  rect = Rect.new(ch.real_x, ch.real_y, 128, 128)
                  # if target can be hit adn not already hit
                  if ch.battler != nil && @dead_type ^ ch.battler.dead? &&
                      self.intersection(r, rect) && !@hit.include?(ch)
                    # execute action
                    execute(ch)
                    # override with explosion animation if using animations
                    ch.animation_id = @explode[1] if BlizzABS::Config::ANIMATIONS
                  end}
            end
            # stop iteration
            break
          end}
    end
    # call superclass method
    super
  end
  #----------------------------------------------------------------------------
  # turn_toward_target
  #  Same as turn_towards_player, but turning toward the destination.
  #----------------------------------------------------------------------------
  def turn_toward_target
    # get pixel movement rate
    pix = BlizzABS.pixel
    # calculate the differences
    dx, dy = @real_x*pix/128-@x, @real_y*pix/128-@y
    # check the differences
    if dx < 0 && dx.abs >= dy.abs # target is right
      turn_right
    elsif dx > 0 && dx.abs >= dy.abs # target is left
      turn_left
    elsif dy < 0 # target is down
      turn_down
    elsif dy > 0 # target is up
      turn_up
    end
  end
  #----------------------------------------------------------------------------
  # out_of_screen
  #  add - how much extra out of the screen is allowed.
  #  Quick test if the projectile is out of the visible screen.
  #----------------------------------------------------------------------------
  def out_of_screen(add)
    return (self.real_x - $game_map.display_x + add < 0 ||
            self.real_x - $game_map.display_x + add > 2560 ||
            self.real_y - $game_map.display_y + add < 0 ||
            self.real_y - $game_map.display_y + add > 1920)
  end
  
end

#==============================================================================
# Drop_Event
#------------------------------------------------------------------------------
#  This class creates an event that is specificactor designed to add weapons,
#  armors, items and gold to the party. It integrates itself into a Game_Map
#  instance as normal event.
#==============================================================================

class Drop_Event < Game_Event
  
  # setting all accessable variables
  attr_accessor :name
  #----------------------------------------------------------------------------
  # Initialization
  #----------------------------------------------------------------------------
  def initialize(item, x, y)
    # call superclass method
    super($game_map.map_id, RPG::Event.new(0, 0))
    # 0th page
    @page = 0
    # loop
    loop do
      # create item ID number
      id = rand(9999000) + 1000
      # if no object with this ID exists
      if $game_map.events[id] == nil
        # set new ID
        @id = id
        # add into map events
        $game_map.events[id] = self
        # stop looping
        break
      end
    end
    # set own event name DROP + ID
    self.name = "DROP#{@id}"
    # create 3 event commands
    3.times {@list.push(RPG::EventCommand.new)}
    # first event command
    case item
    # what is the dropped item
    when Numeric
      # which event command
      @list[0].code = 125
      # increase quantity by number command
      @list[0].parameters = [0, 0, item]
      # set icon name to display dropped gold
      @character_name = BlizzABS::Config::DROP_GOLD
    when RPG::Item, RPG::Weapon, RPG::Armor
      # which event command
      case item
      when RPG::Item then @list[0].code = 126
      when RPG::Weapon then @list[0].code = 127
      when RPG::Armor then @list[0].code = 128
      end
      # increase quantity by 1 command
      @list[0].parameters = [item.id, 0, 0, 1]
      # set icon name to display dropped item
      @character_name = item.icon_name
    end
    # play sound effect
    @list[1].code = 250
    # if ITEM_PICKUP_SOUND_FILE exists
    if BlizzABS::Config::ITEM_PICKUP_SOUND_FILE.name != ''
      # set file to be played
      @list[1].parameters = [BlizzABS::Config::ITEM_PICKUP_SOUND_FILE]
    end
    # erase event command
    @list[2].code = 116
    # get pixel movement rate
    pix = BlizzABS.pixel
    # move to correct position
    moveto((x+pix/2)/pix, (y+pix/2)/pix)
    # set through
    @through = true
    # dummy settings that are not used anyway, but they are necessary
    @prelock_direction = @tile_id = @character_hue = @blend_type =
    @animation_id = @move_type = @move_speed = @move_frequency = 
    @move_route_index = @original_move_route_index = @anime_count =
    @stop_count = @jump_count = @jump_peak = @wait_count = @prelock_direction =
    @pattern = @original_pattern = 0
    @original_direction = @direction = 2
    @opacity = 255
    @walk_anime = true
    @move_route_forcing = @transparent = @step_anime = @direction_fix =
    @always_on_top = @locked = false
    @move_route = @original_move_route = nil
    # create own sprite
    sprite = Sprite_Character.new($scene.spriteset.viewport1, self)
    # set sprite to blinking
    sprite.select = 2
    # add to spriteset handler
    $scene.spriteset.character_sprites.push(sprite)
    # set dieance counter
    @count = BlizzABS::Config::ITEM_TIME * 20
  end
  #----------------------------------------------------------------------------
  # update
  #  Processes basic update and decreased expire counter.
  #----------------------------------------------------------------------------
  def update
    # call superclass method
    super
    # decrease stay time if stay time is greater than 0
    @count -= 1 if @count > 0
    # set deletion flag if item taken or stay time expired
    @terminate = true if @count <= 0
  end
  #----------------------------------------------------------------------------
  # erase
  #  Usually used to temporary erase the event, here used to completely
  #  terminate the event.
  #----------------------------------------------------------------------------
  def erase
    @terminate = true
  end
  
end

#==============================================================================
# Game_Controls
#------------------------------------------------------------------------------
#  This class handling player input for battle.
#==============================================================================

class Game_Controls
  
  # setting all accessable variables
  attr_accessor :hotkeys
  attr_accessor :skills
  attr_accessor :items
  attr_accessor :skill
  attr_accessor :defend
  attr_writer   :projectiles
  #----------------------------------------------------------------------------
  # Initialization
  #----------------------------------------------------------------------------
  def initialize
    # skills -> skill ID on key index
    @skills = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # items -> item ID on key index
    @items = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  end
  #----------------------------------------------------------------------------
  # update
  #  Processes the player's input.
  #----------------------------------------------------------------------------
  def update
    # update each projectile
    BlizzABS::Cache.projectiles.each {|projectile| projectile.update}
    # if not allowed to act
    if !$game_temp.in_battle || $game_player.jumping? ||
        $game_player.freeze_action || $game_player.move_route_forcing ||
        $game_player.in_action > 0 || $game_player.battler == nil
      # freeze battle controls
      return
    end
    # if defend button pressed
    if Input.press?(Input::Defend)
      # player defends
      $game_player.defending = true
      # exit method
      return
    end
    # doesn't defend
    $game_player.defending = false
    # if attack button is pressed and equipped weapon
    if Input.trigger?(Input::Attack) && $game_player.battler.weapon_id > 0
      # attack
      $game_player.use_attack
    # if pressed main skill hotkey
    elsif Input.trigger?(Input::Skill)
      # if skill not assigned or skill use process not executed and no selection
      if $game_player.battler.skill == 0 ||
          !$game_player.use_skill($data_skills[$game_player.battler.skill]) &&
          $game_temp.select_data == nil
        # play buzzer, can't use
        $game_system.se_play($data_system.buzzer_se)
      end
    # if pressed main item hotkey
    elsif Input.trigger?(Input::Item)
      # if item not assigned or item use process not executed and no selection
      if $game_player.battler.item == 0 ||
          !$game_player.use_item($data_items[$game_player.battler.item]) &&
          $game_temp.select_data == nil
        # play buzzer, can't use
        $game_system.se_play($data_system.buzzer_se)
      end
    end
  end
  
end

#==============================================================================
# Bitmap
#------------------------------------------------------------------------------
#  This class was enhanced with methods to support the drawing of gradient bars
#  and outlined text.
#==============================================================================

class Bitmap
  
  #----------------------------------------------------------------------------
  # gradient_bar_hud
  #  x      - x-coordinate
  #  y      - y-coordinate
  #  w      - width
  #  color1 - the inner, brighter color
  #  color2 - the outer, darker color
  #  rate   - fill rate
  #  Draws the HUD gradient bar.
  #----------------------------------------------------------------------------
  def gradient_bar_hud(x, y, w, color1, color2, rate)
    # draw extra stuff depending on HUD style
    case BlizzABS::Config::HUD_TYPE
    when 0 then fill_rect(x + 1, y, w + 2, 14, Color.new(255, 255, 255, 192))
    when 1 then fill_rect(x + 1, y, w + 2, 14, Color.new(255, 255, 255, 0))
    end
    # iterate through 6 lines
    (1..6).each {|i|
        # 1st color
        color = Color.new(color2.red*i/6, color2.green*i/6, color2.blue*i/6, 255)
        # fill smaller (only height) becoming rectangle with 1st color (background)
        fill_rect(x + 2, y + i, w, 14 - i * 2, color)
        # 2nd color
        color = Color.new(color1.red*i/6, color1.green*i/6, color1.blue*i/6, 255)
        # fill smaller (only height) becoming rectangle with 1st color (bars)
        fill_rect(x + 2, y + i, w * rate, 14 - i * 2, color)}
  end
  #----------------------------------------------------------------------------
  # draw_circle
  #  x     - x-coordinate
  #  y     - y-coordinate
  #  rad   - radius of the circle
  #  color - fill color
  #  Draws a circle.
  #----------------------------------------------------------------------------
  def draw_circle(x, y, rad, color)
    # iterate from center to right border
    (0...rad).each {|r|
        # calculate y coordinate from x coordinate via trigonometric functions
        h = (rad * Math.sin(Math.acos(r/rad.to_f))).to_i
        # draw vertical bar
        fill_rect(x+rad-r-1, y+rad-h, 1, h*2+1, color)
        # draw identical vertical bar on the left side
        fill_rect(x+rad+r, y+rad-h, 1, h*2+1, color)}
  end
  #----------------------------------------------------------------------------
  # draw_text_full
  # x2    - x-coordinate
  # y2    - y-coordinate
  # w2    - width
  # h2    - height
  # text2 - text
  # a2    - align
  #  Uses an aliased version of draw_text to draw outlined text.
  #----------------------------------------------------------------------------
  # if method not aliased already
  if $tons_version == nil || $tons_version < 1.6
    # alias original method
    alias draw_text_shaded_text_later draw_text
  end
  def draw_text_full(x2, y2, w2 = 0, h2 = 0, text2 = '', a2 = 0)
    # if x2 is a rectangle
    if x2.is_a?(Rect)
      # set temporary variables
      x, y, w, h, text, a = x2.x, x2.y, x2.width, x2.height, y2, w2
    else
      # set temporary variables
      x, y, w, h, text, a = x2, y2, w2, h2, text2, a2
    end
    # save old font color
    save_color = self.font.color.clone
    # set new font color (black)
    self.font.color = Color.new(0, 0, 0)
    # draw text with offsets in all directions
    [x-1, x+1].each {|xx| [y-1, y+1].each {|yy|
            draw_text_shaded_text_later(xx, yy, w, h, text, a)}}
    # restore original color
    self.font.color = save_color
    # drw text at normal postion
    draw_text_shaded_text_later(x, y, w, h, text, a)
  end
  
end

#==============================================================================
# Sprite_Character
#------------------------------------------------------------------------------
#  This class was modified to support animation sprites and dropped item icon
#  display.
#==============================================================================

class Sprite_Character
  
  #----------------------------------------------------------------------------
  # override initialize
  #----------------------------------------------------------------------------
  alias init_blizzabs_later initialize
  def initialize(viewport, character = nil)
    # set spriteset add-on names
    @weapon_sprite = @current_sprite = ''
    # call original method
    init_blizzabs_later(viewport, character)
  end
  #----------------------------------------------------------------------------
  # override update
  #----------------------------------------------------------------------------
  alias upd_player_blizzabs_later update
  def update
    # if not dropped event
    if !@character.is_a?(Drop_Event)
      # if animation ID is different than current one
      if @character.loop_animation_id != @loop_animation_id
        # store new ID
        @loop_animation_id = @character.loop_animation_id
        # show animation loop
        loop_animation($data_animations[@loop_animation_id])
      end
      # save old bitmap
      b = self.bitmap
      # call original method
      upd_player_blizzabs_later
      # if Map_Battler, another bitmap and weapon_sprite
      if @character.is_a?(Map_Battler) && b != self.bitmap &&
          @weapon_sprite != @character.weapon_sprite
        # store current weapon_sprite
        @weapon_sprite = @character.weapon_sprite
        # get display rectangle
        rect = self.src_rect.clone
        # cache bitmap again, but this time use a copy
        self.bitmap = RPG::Cache.character(@character_name, @character_hue).clone
        # cache weapon bitmap
        b = RPG::Cache.character(@character_name + @weapon_sprite, 0)
        # draw weapon onto character copied bitmap
        self.bitmap.blt(0, 0, b, Rect.new(0, 0, b.width, b.height))
        # reset source rectangle
        self.src_rect = rect
      end
      # if Map_Actor or Map_Enemy
      if (@character.is_a?(Map_Actor) || @character.is_a?(Map_Enemy))
        # add to offset for special attack condition
        self.oy = self.bitmap.height/4 - @character.atk_offset
      end
    else
      # call superclass method
      super
      # if bitmap is empty
      if self.bitmap == nil
        # cache new icon bitmap
        self.bitmap = RPG::Cache.icon(@character.character_name)
        # set x and y position offset
        self.ox, self.oy = self.bitmap.width / 2, self.bitmap.height
      end
      # set x and y position
      self.x, self.y = @character.screen_x, @character.screen_y
      # set z position
      self.z = @character.screen_z(self.bitmap.height / 4) + 31
    end
  end
  
end
  
#==============================================================================
# Control_Sprite_Character
#------------------------------------------------------------------------------
#  This class is an interception class for Sprite_Character. It substitutes its
#  instances everywhere and handles them. It provides ABSEAL limitation
#  control, damage sprite control and enemy fade_in/dying animations.
#  It disposes sprites out of the ABSEAL range immediately.
#==============================================================================

class Control_Sprite_Character
  
  # setting all accessable variables
  attr_accessor :fade_in
  attr_accessor :dying
  attr_accessor :fade_out
  attr_accessor :select
  attr_reader   :character
  attr_reader   :damage
  #----------------------------------------------------------------------------
  # Initialization
  #  viewport  - a viewport
  #  character - the character to observe and display
  #----------------------------------------------------------------------------
  def initialize(viewport, character = nil)
    # set all flags
    @fade_in = @dying = @fade_out = false
    # set select animation mode
    @select = 0
    # store character
    self.character = character
    # store viewport
    @viewport = viewport
  end
  #----------------------------------------------------------------------------
  # character=
  #  char - the new character to observe and display
  #  This method gives the character to the sprite as well if it exists.
  #----------------------------------------------------------------------------
  def character=(char)
    # store character
    @character = char
    # give character to sprite if sprite exists
    @sprite.character = char unless @sprite == nil
  end
  #----------------------------------------------------------------------------
  # update
  #  Processes sprite update if the sprite exists. If not, it tests if the
  #  character is within ABSEAL range and creates a sprite. Every sprite
  #  which's character is outside of ABSEAL gets disposed.
  #----------------------------------------------------------------------------
  def update
    # if character within ABSEAL range or special character
    if (@character.is_a?(Game_Event) || @character.is_a?(Map_Enemy)) &&
        @character.update? || !@character.is_a?(Map_Enemy) &&
        @character.is_a?(Map_Battler)|| @character.is_a?(Drop_Event)
      # if sprite doesn't exists yet
      if @sprite == nil || @sprite.disposed?
        # create a sprite
        @sprite = Sprite_Character_ABSEAL_ed.new(@viewport, @character)
      else
        # update the sprite itself
        @sprite.update
        # update selection animation
        update_select
        # update damage animation if the observed character is a map battler
        damage_update if @character.is_a?(Map_Battler)
      end
    # if sprite exists
    elsif @sprite != nil
      # delete sprite
      @sprite.dispose unless @sprite.disposed?
      @sprite = nil
    end
  end
  #----------------------------------------------------------------------------
  # update_select
  #  Updates the animation when selecting a map battler.
  #----------------------------------------------------------------------------
  def update_select
    # if normal blink should be processed
    if @select == 2
      # set blink
      @sprite.blink_on
    # if selected right now
    elsif @select == 1
      # set color with new alpha
      @sprite.color.set(0, 255, 0, (8-Graphics.frame_count%16).abs*24)
    else
      # set to no color
      @sprite.color.set(0, 0, 0, 0)
    end
  end
  #----------------------------------------------------------------------------
  # damage_update
  #  Creates a damage sprite if the map battler has damage to be shown.
  #----------------------------------------------------------------------------
  def damage_update
    # if player/actor/enemy and battler exists and damage exists
    if @character.is_a?(Map_Battler) && @character.battler != nil &&
        @character.battler.damage != nil
      # create sprite
      dmg = Sprite.new
      # create damage text bitmap
      damage(dmg, @character.battler)
      # set coordinates
      dmg.x, dmg.y, dmg.z, dmg.ox, dmg.oy = @sprite.x, @sprite.y, 1, 80, 64
      # add to buffer array
      BlizzABS::Cache.damages.push([dmg, $game_map.display_x,
          $game_map.display_y])
    end
  end
  #----------------------------------------------------------------------------
  # in_screen
  #  Tests the sprite if inside the screen if it exists.
  #----------------------------------------------------------------------------
  def in_screen?
    return (@sprite != nil && @sprite.in_screen?)
  end
  #----------------------------------------------------------------------------
  # x
  #  Returns the sprite's x coordinate.
  #----------------------------------------------------------------------------
  def x
    return (@sprite != nil ? @sprite.x : 0)
  end
  #----------------------------------------------------------------------------
  # y
  #  Returns the sprite's y coordinate.
  #----------------------------------------------------------------------------
  def y
    return (@sprite != nil ? @sprite.y : 0)
  end
  #----------------------------------------------------------------------------
  # z
  #  Returns the sprite's z coordinate.
  #----------------------------------------------------------------------------
  def z
    return (@sprite != nil ? @sprite.z : 0)
  end
  #----------------------------------------------------------------------------
  # z
  #  Returns the sprite's z coordinate.
  #----------------------------------------------------------------------------
  def z=(val)
    @sprite.z = val if @sprite != nil
  end
  #----------------------------------------------------------------------------
  # update_die
  #  Processes a special 18-frame fading out animation that is used to display
  #  dying enemies.
  #----------------------------------------------------------------------------
  def update_die
    # if normal blending
    if @character.blend_type == 0
      # set blending to positive
      @character.blend_type = 1
      # play collapse sound effect
      $game_system.se_play($data_system.enemy_collapse_se)
    end
    # if still fading out
    if @character.opacity > 0
      # decrease opacity
      @character.opacity -= 15
    else
      # set blend type to normal
      @character.blend_type = 0
      # set terminate flag
      @character.terminate = true
    end
  end
  #----------------------------------------------------------------------------
  # update_fade_in
  #  Processes an 18-frame fading in animation.
  #----------------------------------------------------------------------------
  def update_fade_in
    # if still fading in
    if @character.opacity < 255
      # increase opacity
      @character.opacity += 15
    # if opacity is 255
    elsif @character.opacity == 255
      # set fade_in flag
      @fade_in = false
    end
  end
  #----------------------------------------------------------------------------
  # update_fade_out
  #  Processes a 5-frame fading out animation.
  #----------------------------------------------------------------------------
  def update_fade_out
    # if still fading out
    if @character.opacity > 0
      # decrease opacity
      @character.opacity -= 64
    else
      # reset fade_out flag
      @character.fade_out = false
    end
  end
  #----------------------------------------------------------------------------
  # damage
  #  battler - the battler with the damage
  #  last_hp - the battler's last hp
  #  last_sp - the battler's last sp
  #  Creates damage text.
  #----------------------------------------------------------------------------
  def damage(dmg, battler)
    # is damage is a number
    if battler.damage.is_a?(Numeric)
      # create a text
      damage_string = battler.damage.abs.to_s
    else
      # convert to text if possible somehow
      damage_string = battler.damage.to_s
    end
    # create bitmap
    dmg.bitmap = Bitmap.new(160, 48)
    # set font
    dmg.bitmap.font.name = 'Arial Black'
    # set font size
    dmg.bitmap.font.size = 24
    # set font color
    dmg.bitmap.font.color.set(0, 0, 0)
    # draw text with offsets in all directions
    dmg.bitmap.draw_text_shaded_text_later(-1, 11, 160, 36, damage_string, 1)
    dmg.bitmap.draw_text_shaded_text_later(2, 14, 160, 36, damage_string, 1)
    dmg.bitmap.draw_text_shaded_text_later(2, 11, 160, 36, damage_string, 1)
    dmg.bitmap.draw_text_shaded_text_later(-1, 14, 160, 36, damage_string, 1)
    # if damage is number and less than 0
    if battler.damage.is_a?(Numeric) && battler.damage < 0
      # set color to cyan blueish
      dmg.bitmap.font.color.set(0, 192, 255)
    # if damage is "LvUp"
    elsif battler.damage == 'LvUp'
      # set color to violet
      dmg.bitmap.font.color.set(160, 0, 255)
    # if damage is Miss or damage is 0
    elsif battler.damage == 'Miss' || battler.damage == 0
      # set color to bright grey
      dmg.bitmap.font.color.set(192, 192, 192)
    # if damage is critical
    elsif battler.critical
      # set color to red
      dmg.bitmap.font.color.set(255, 0, 0)
      # set critical flag
      dmg.critical = true
    # if HP increased
    elsif battler.hpdamage > 0
      # set color to cyan blueish
      dmg.bitmap.font.color.set(255, 0, 0)
    # if HP increased
    elsif battler.hpdamage < 0
      # set color to cyan blueish
      dmg.bitmap.font.color.set(0, 192, 255)
    # if SP increased
    elsif battler.spdamage < 0
      # set color to green
      dmg.bitmap.font.color.set(0, 255, 64)
    # if SP decreased
    elsif battler.spdamage > 0
      # set color to yellow
      dmg.bitmap.font.color.set(255, 255, 0)
    else
      # set font color to white
      dmg.bitmap.font.color.set(255, 255, 255)
    end
    # draw damage string
    dmg.bitmap.draw_text_shaded_text_later(0, 12, 160, 36, damage_string, 1)
    # reset damage
    battler.damage = nil
  end 
  #----------------------------------------------------------------------------
  # dispose
  #  Deletes and removes sprite from memory.
  #----------------------------------------------------------------------------
  def dispose
    # if sprite exists and not freed yet
    unless @sprite == nil || @sprite.disposed?
      # delete sprite
      @sprite.dispose
      @sprite = nil
    end
  end
  
end

#==============================================================================
# Sprite_Character_ABSEAL_ed
#------------------------------------------------------------------------------
#  This class serves as alias for the original Sprite_Character.
#==============================================================================

class Sprite_Character_ABSEAL_ed < Sprite_Character
end

#==============================================================================
# Sprite_Character
#------------------------------------------------------------------------------
#  Here is where the class substitution occurs.
#==============================================================================

class Sprite_Character < Control_Sprite_Character
end

#==============================================================================
# Hud
#------------------------------------------------------------------------------
#  This class creates and processes the HUD system and is more efficient than
#  the Window class. It also handles the hotkey assignment display and minimap.
#==============================================================================

class Hud < Sprite
  
  # setting all accessable variables
  attr_reader :assignment
  #----------------------------------------------------------------------------
  # Initialization
  #  viewport - the viewport for the sprite
  #----------------------------------------------------------------------------
  def initialize(viewport = nil)
    # call superclass method
    super
    # create bitmap
    self.bitmap = Bitmap.new(156, 112)
    # set font
    self.bitmap.font.name = 'Arial'
    # set font size
    self.bitmap.font.size = 16
    # set font to bold
    self.bitmap.font.bold = true
    # set x and y coordinate depending on which HUD mode
    case BlizzABS::Config::HUD_POSITION
    when 0 then self.x, self.y = 4, 4
    when 1 then self.x, self.y = 480, 4
    when 2 then self.x, self.y = 4, 364
    end
    # set z coordinate
    self.z = 1000
    # create Minimap if available
    @mini_map = Mini_Map.new if $game_system.minimap > 0
    # if assignment display available
    if $game_system.assignment
      # create hotkey assignment display
      @assignment = Hotkey_Assignment.new
      # set z coordinate of hotkey assignment display
      @assignment.z = self.z + 100
    end
    # draw basic HUD
    draw_basic
    # refresh actor display
    test_changes
    # update
    update
  end
  #----------------------------------------------------------------------------
  # draw_basic
  #  Draws the HUD template.
  #----------------------------------------------------------------------------
  def draw_basic
    # fill with grey rectangle
    self.bitmap.fill_rect(0, 0, 156, 112, Color.new(0, 0, 0, 128))
    # set font color
    self.bitmap.font.color = system_color
    # draw "LV"
    self.bitmap.draw_text_full(108, 1, 20, 20, 'LV')
    # draw "Skill:"
    self.bitmap.draw_text_full(4, 80, 48, 20, 'Skill:')
    # draw "Item:"
    self.bitmap.draw_text_full(80, 80, 48, 20, 'Item:')
    # draw "HP"
    self.bitmap.draw_text_full(4, 17, 32, 20, $data_system.words.hp)
    # draw "SP"
    self.bitmap.draw_text_full(4, 33, 32, 20, $data_system.words.sp)
    # draw "next"
    self.bitmap.draw_text_full(4, 49, 80, 20, 'next')
    # set font color
    self.bitmap.font.color = Color.new(255, 255, 0)
    # draw the first letter of the word used for the game currency
    self.bitmap.draw_text_full(96, 64, 56, 20, $data_system.words.gold[0, 1], 2)
  end
  #----------------------------------------------------------------------------
  # draw_empty
  #  Draws the HP, SP and EXP display when actor doesn't exist.
  #----------------------------------------------------------------------------
  def draw_empty
    # set colors
    c = [Color.new(0, 80, 0, 192), Color.new(0, 0, 80, 192), Color.new(80, 80, 80, 192)]
    # draw emtpy bars
    (0..2).each {|i| self.bitmap.gradient_bar_hud(36, 20+i*16, 112, c[i], c[i], 0)}
    # set font color
    self.bitmap.font.color = disabled_color
    # draw first "0"s
    (0..2).each {|i| self.bitmap.draw_text_full(42+i/2*54, 17+i*16, 48, 20, '0', 2)}
    # draw "/"s
    (0..1).each {|i| self.bitmap.draw_text_full(90, 17+i*16, 12, 20, '/', 1)}
    # draw last "0"s
    (0..1).each {|i| self.bitmap.draw_text_full(102, 17+i*16, 48, 20, '0')}
    # reset all flag variables
    @name = @level = @hp = @sp = @exp = @states = @skill =
        @skills_left = @item = @items_left = @gold = nil
  end
  #----------------------------------------------------------------------------
  # draw_name
  #  Draws the name display.
  #----------------------------------------------------------------------------
  def draw_name
    # set current variable
    @name = actor.name
    # remove old display
    self.bitmap.fill_rect(4, 1, 104, 20, Color.new(0, 0, 0, 128))
    # set font color
    self.bitmap.font.color = Color.new(0, 255, 0)
    # draw actor's name
    self.bitmap.draw_text_full(4, 1, 104, 20, @name)
  end
  #----------------------------------------------------------------------------
  # draw_level
  #  Draws the level display.
  #----------------------------------------------------------------------------
  def draw_level
    # set current variable
    @level = actor.level
    # remove old display
    self.bitmap.fill_rect(128, 1, 24, 20, Color.new(0, 0, 0, 128))
    # set font color
    self.bitmap.font.color = normal_color
    # draw actor's level
    self.bitmap.draw_text_full(128, 1, 24, 20, @level.to_s, 2)
  end
  #----------------------------------------------------------------------------
  # draw_hp
  #  Draws the HP display.
  #----------------------------------------------------------------------------
  def draw_hp
    # set current variable
    @hp = actor.hp
    # set fill rate
    rate = (actor.maxhp > 0 ? actor.hp.to_f / actor.maxhp : 0)
    # if filled more than 60%
    if rate > 0.6
      # get color1
      color1 = Color.new(240 - 450 * (rate-0.6), 240, 150 * (rate-0.6), 192) 
    # if filled between 20% and 60%
    elsif rate > 0.2 && rate <= 0.6
      # get color1
      color1 = Color.new(240, 600 * (rate-0.2), 0, 192) 
    # if filled equal or less than 20%
    elsif rate <= 0.2
      # get color1
      color1 = Color.new(240, 0, 0, 192)
    end
    # get color2
    color2 = Color.new(0, 80, 0, 192)
    # draw gradient bar
    self.bitmap.gradient_bar_hud(36, 20, 112, color1, color2, rate)
    # set font color depending on how many HP left
    self.bitmap.font.color = actor.hp == 0 ? knockout_color :
        actor.hp <= actor.maxhp / 4 ? crisis_color : normal_color
    # draw HP
    self.bitmap.draw_text_full(42, 17, 48, 20, actor.hp.to_s, 2)
    # set color
    self.bitmap.font.color = normal_color
    # draw "/"
    self.bitmap.draw_text_full(90, 17, 12, 20, '/', 1)
    # draw max HP
    self.bitmap.draw_text_full(102, 17, 48, 20, actor.maxhp.to_s)
  end
  #----------------------------------------------------------------------------
  # draw_sp
  #  Draws the SP display.
  #----------------------------------------------------------------------------
  def draw_sp
    # set current variable
    @sp = actor.sp
    # set fill rate
    rate = (actor.maxsp > 0 ? actor.sp.to_f / actor.maxsp : 0)
    # if filled more than 40%
    if rate > 0.4
      # get color1
      color1 = Color.new(180 - 200 * (rate-0.4), 60, 240, 192) 
    # if filled less than 40%
    elsif rate <= 0.4
      # get color1
      color1 = Color.new(60 + 300 * rate, 150 * rate, 80 + 400 * rate, 192) 
    end
    # get color2
    color2 = Color.new(0, 0, 80, 192)
    # draw gradient bar
    self.bitmap.gradient_bar_hud(36, 36, 112, color1, color2, rate)
    # set font color depending on how many SP left
    self.bitmap.font.color = actor.sp == 0 ? knockout_color :
        actor.sp <= actor.maxsp / 4 ? crisis_color : normal_color
    # draw SP
    self.bitmap.draw_text_full(42, 33, 48, 20, actor.sp.to_s, 2)
    # set font color
    self.bitmap.font.color = normal_color
    # draw "/"
    self.bitmap.draw_text_full(90, 33, 12, 20, '/', 1)
    # draw max SP
    self.bitmap.draw_text_full(102, 33, 48, 20, actor.maxsp.to_s)
  end
  #----------------------------------------------------------------------------
  # draw_exp
  #  Draws the EXP display.
  #----------------------------------------------------------------------------
  def draw_exp
    # set current variable
    @exp = actor.exp
    # set fill rate
    rate = (actor.next_exp != 0 ? actor.now_exp.to_f / actor.next_exp  : 1)
    # if filled less than 50%
    if rate < 0.5
      # set color1
      color1 = Color.new(60 * rate, 180, 240, 192) 
    # if filled more than 50%
    elsif rate >= 0.5
      # set color1
      color1 = Color.new(60 + 360 * (rate-0.5), 180 + 120 * (rate-0.5), 240, 192) 
    end
    # set color2
    color2 = Color.new(80, 80, 80, 192)
    # draw gradient bar
    self.bitmap.gradient_bar_hud(36, 52, 112, color1, color2, rate)
    # set font color
    self.bitmap.font.color = normal_color
    # draw EXP required for next level
    self.bitmap.draw_text_full(60, 49, 84, 20, actor.next_rest_exp_s, 2)
  end
  #----------------------------------------------------------------------------
  # draw_state
  #  Draws the state display.
  #----------------------------------------------------------------------------
  def draw_state
    # set current variable
    @states = actor.states.clone
    # remove old display
    self.bitmap.fill_rect(4, 68, 80, 16, Color.new(0, 0, 0, 128))
    # create dummy wondow
    win = Window_Base.new(0, 0, 33, 33)
    # create bitmap
    win.contents = Bitmap.new(1, 1)
    # create state text
    state = win.make_battler_state_text(actor, 80, true)
    # remove window
    win.dispose
    # draw state text
    self.bitmap.draw_text_full(4, 64, 80, 20, state)
  end
  #----------------------------------------------------------------------------
  # draw_gold
  #  Draws the gold display.
  #----------------------------------------------------------------------------
  def draw_gold
    # set current variable
    @gold = $game_party.gold
    # remove old display
    self.bitmap.fill_rect(84, 68, 56, 16, Color.new(0, 0, 0, 128))
    # set font color
    self.bitmap.font.color = normal_color
    # draw ammount of gold
    self.bitmap.draw_text_full(84, 64, 56, 20, @gold.to_s, 2)
  end
  #----------------------------------------------------------------------------
  # draw_hskill
  #  Draws the hot skill display.
  #----------------------------------------------------------------------------
  def draw_hskill
    # set current variable
    @skill = actor.skill
    # remove old display
    self.bitmap.fill_rect(52, 84, 24, 24, Color.new(0, 0, 0, 128))
    # if skill hot skill exists
    if actor.skill != 0
      # load bitmap
      bitmap = RPG::Cache.icon($data_skills[@skill].icon_name)
      # draw bitmap
      self.bitmap.blt(52, 84, bitmap, Rect.new(0, 0, 24, 24), 255)
    else
      # removes skills left to use display
      draw_lskill
    end
  end
  #----------------------------------------------------------------------------
  # draw_lskill
  #  Draws the skills left to use display.
  #----------------------------------------------------------------------------
  def draw_lskill
    # remove old display
    self.bitmap.fill_rect(4, 98, 20, 16, Color.new(0, 0, 0, 128))
    # if skill hot skill exists
    if @skill != nil && @skill > 0
      # if SP cost is zero
      if $data_skills[@skill].sp_cost == 0
        # set flag
        @skills_left = -1
      else
        # calculate skills left to use
        @skills_left = @sp / $data_skills[@skill].sp_cost
      end
      # if SP cost is zero
      if @skills_left == -1
        # set font color
        self.bitmap.font.color = Color.new(0, 255, 0)
        # increase font size
        self.bitmap.font.size += 4
        # draw "∞" skill uses left
        self.bitmap.draw_text_full(4, 94, 20, 20, '∞', 2)
        # decrease font size
        self.bitmap.font.size -= 4
      else
        # if not enough sp to use
        if @skills_left == 0
          # set font color
          self.bitmap.font.color = Color.new(255, 0, 0)
        # if enough SP for 5 or less skill uses
        elsif @skills_left <= 5
          # set font color
          self.bitmap.font.color = Color.new(255, 255, 0)
        else
          # set font color
          self.bitmap.font.color = normal_color
        end
        # decrease font color
        self.bitmap.font.size -= 2
        # draw number how many skills left to use
        self.bitmap.draw_text_full(4, 94, 20, 20, @skills_left.to_s, 2)
        # increase font size
        self.bitmap.font.size += 2
      end
    end
  end
  #----------------------------------------------------------------------------
  # draw_hitem
  #  Draws the hot item display.
  #----------------------------------------------------------------------------
  def draw_hitem
    # set current variable
    @item = actor.item
    # remove old display
    self.bitmap.fill_rect(128, 84, 24, 24, Color.new(0, 0, 0, 128))
    # if hot item exists
    if actor.item != 0
      # load bitmap
      bitmap = RPG::Cache.icon($data_items[@item].icon_name)
      # draw bitmap
      self.bitmap.blt(128, 84, bitmap, Rect.new(0, 0, 24, 24), 255)
    else
      # removes items left to use display
      draw_litem
    end
  end
  #----------------------------------------------------------------------------
  # draw_litem
  #  Draws the items left to use display.
  #----------------------------------------------------------------------------
  def draw_litem
    # set current variable
    @items_left = $game_party.item_number(@item)
    # remove old display
    self.bitmap.fill_rect(80, 98, 20, 16, Color.new(0, 0, 0, 128))
    # if hot item exists
    if @item != nil && @item > 0
      # if item exists and cannot be consumed
      if $data_items[@item] != nil && !$data_items[@item].consumable
        # set font color
        self.bitmap.font.color = Color.new(0, 255, 0)
        # increase font size
        self.bitmap.font.size += 4
        # draw "∞" items left
        self.bitmap.draw_text_full(80, 94, 20, 20, '∞', 2)
        # decrease font size
        self.bitmap.font.size -= 4
      else
        # if no items left
        if @items_left == 0
          # set font color
          self.bitmap.font.color = Color.new(255, 0, 0)
        # if equal or less items left
        elsif @items_left <= 10
          # set font color
          self.bitmap.font.color = Color.new(255, 255, 0)
        else
          # set font color
          self.bitmap.font.color = normal_color
        end
        # decrease font color
        self.bitmap.font.size -= 2
        # draw number how many items left to use
        self.bitmap.draw_text_full(80, 94, 20, 20, @items_left.to_s, 2)
        # increase font size
        self.bitmap.font.size += 2
      end
    end
  end
  #----------------------------------------------------------------------------
  # test_changes
  #  Checks if HUD needs refreshing.
  #----------------------------------------------------------------------------
  def test_changes
    # if actor doesn't exist
    if actor == nil
      # unless already drawn empty HUD
      unless @drawn
        # draw HUD template
        draw_basic
        # draw empty HP, SP and EXP bars
        draw_empty
        # empty HUD was drawn
        @drawn = true
      end
    else
      # draw new name if name has changed
      draw_name if actor.name != @name
      # draw new level if level has changed
      draw_level if actor.level != @level
      # draw new HP if HP have changed
      draw_hp if actor.hp != @hp
      # draw new SP if SP have changed
      draw_sp if actor.sp != @sp
      # draw new EXP if EXP have changed
      draw_exp if actor.exp != @exp
      # draw new state if state has changed
      draw_state if actor.states != @states
      # draw new skill icon if assigned skill has changed
      draw_hskill if actor.skill != @skill
      # if skill exists
      if @skill != 0
        # if SP cost greater than zero
        if $data_skills[@skill].sp_cost > 0
          # draw how many skills left to use if this number has changed
          draw_lskill if @sp / $data_skills[@skill].sp_cost != @skills_left
        else
          # draw how many skills left if it wasn't drawn yet
          draw_lskill if @skills_left != -1
        end
      end
      # draw new item icon if assigned item has changed
      draw_hitem if actor.item != @item
      # draw how many items left to use if this number has changed
      draw_litem if $game_party.item_number(@item) != @items_left
      # draw new gold if gold has changed
      draw_gold if $game_party.gold != @gold
      # empty HUD wasn't drawn
      @drawn = false
    end
  end
  #----------------------------------------------------------------------------
  # actor
  #  Returns the party leader's battler.
  #----------------------------------------------------------------------------
  def actor
    return $game_player.battler
  end
  #----------------------------------------------------------------------------
  # update
  #  Processing all HUD information.
  #----------------------------------------------------------------------------
  def update
    # redraw if there are any changes
    test_changes
    # iterate through all the HUD sprites
    [self, @mini_map, @assignment].each {|sprite|
        # if sprite exists
        if sprite != nil
          # if player is on the same position as one of the sprites on the screen
          if $game_player.screen_x < sprite.vx + sprite.vw + 16 &&
              $game_player.screen_y < sprite.vy + sprite.vh + 48 &&
              $game_player.screen_x > sprite.vx &&
              $game_player.screen_y > sprite.vy &&
              ((sprite == @mini_map) ? ($game_system.minimap < 2) : true)
            # decrease opacity quickly if critical opacity not reached
            sprite.opacity -= 25 if sprite.opacity > 80
          # if not full opacity
          elsif sprite.opacity <= 255
            # increase opacity quickly if critical opacity not reached
            sprite.opacity += 25
          end
        end}
    # if minimap display off and minimap still exists
    if $game_system.minimap == 0 && @mini_map != nil
      # delete minimap
      @mini_map.dispose
      @mini_map = nil
    # if minimap display on and minimap doesn't exist yet
    elsif $game_system.minimap == 1 && @mini_map == nil
      # create minimap
      @mini_map = Mini_Map.new
    # if minimap display is in fullscreen mode
    elsif $game_system.minimap == 2
      # unless fullscreen already initialized and no new map
      unless @mini_map.viewport.rect.width == 640 &&
          @mini_map.map_id == $game_map.map_id
        # set display rectangle
        @mini_map.viewport.rect.set(0, 0, 640, 480)
        # update the offset
        @mini_map.update(true)
      end
      # if pressed turning button
      if Input.press?(Input::Turn) && !$game_system.map_interpreter.running? &&
          !@move_route_forcing && !$game_temp.message_window_showing
        # if map width out of screen width
        if @mini_map.bitmap.width > 640
          # if holding right
          if Input.repeat?(Input::RIGHT)
            # if map not out of screen yet
            if @mini_map.ox + 640 < @mini_map.bitmap.width
              # play cursor sound
              $game_system.se_play($data_system.cursor_se)
              # move minimap
              @mini_map.ox += 32
              # move minimap
            else
              # play buzzer sound
              $game_system.se_play($data_system.buzzer_se)
            end
          elsif Input.repeat?(Input::LEFT)
            if @mini_map.ox > 0
              # play cursor sound
              $game_system.se_play($data_system.cursor_se)
              # move minimap
              @mini_map.ox -= 32
            else
              # play buzzer sound
              $game_system.se_play($data_system.buzzer_se)
            end
          end
        end
        if @mini_map.bitmap.height > 480
          if Input.repeat?(Input::DOWN)
            if @mini_map.oy + 480 < @mini_map.bitmap.height
              # play cursor sound
              $game_system.se_play($data_system.cursor_se)
              # move minimap
              @mini_map.oy += 32
            else
              # play buzzer sound
              $game_system.se_play($data_system.buzzer_se)
            end
          elsif Input.repeat?(Input::UP)
            if @mini_map.oy > 0
              # play cursor sound
              $game_system.se_play($data_system.cursor_se)
              # move minimap
              @mini_map.oy -= 32
            else
              # play buzzer sound
              $game_system.se_play($data_system.buzzer_se)
            end
          end
        end
      end
    end
    # if hotkey display off and hotkey display exists
    if !$game_system.assignment && @assignment != nil
      # delete hotkey display
      @assignment.dispose
      @assignment = nil
    # if hotkey display on and hotkey display doesn't exist
    elsif $game_system.assignment && @assignment == nil
      # create hotkey display
      @assignment = Hotkey_Assignment.new
      # set z position
      @assignment.z = self.z + 100
    end
    # update minimap if minimap is turned on
    @mini_map.update if $game_system.minimap > 0
    # iterate through all number keys
    (0..9).each {|i|
        # if number key i was triggered
        if Input.trigger?(Input::NumKeys[i])
          # if hotkey is valid for this skill
          if $game_system.controls.skills[i] != 0
            # if actor learned this skill
            if actor.skill_learn?($game_system.controls.skills[i])
              # set this skill as the hot skill
              actor.skill = $game_system.controls.skills[i]
            else
              # play buzzer sound
              $game_system.se_play($data_system.buzzer_se)
            end
          # if hotkey is valid for this item
          elsif $game_system.controls.items[i] != 0
            # set this item as hot item
            actor.item = $game_system.controls.items[i]
          else
            # reset hot skill and hot item
            actor.skill = actor.item = 0
          end
        end}
  end
  #----------------------------------------------------------------------------
  # dispose
  #  Removes HUD from screen and memory.
  #----------------------------------------------------------------------------
  def dispose
    # delete hotkey display if it exists
    @assignment.dispose unless @assignment == nil
    # if minimap exists
    unless @mini_map == nil
      # delete minimap
      @mini_map.dispose
      @mini_map = nil
    end
    # call superclass method
    super
  end
  
end

#==============================================================================
# Hotkey_Assignment
#------------------------------------------------------------------------------
#  This class creates and display currently assigned hotkeys and is more
#  effiecient than the Window class.
#==============================================================================

class Hotkey_Assignment < Sprite
  
  #----------------------------------------------------------------------------
  # Initialization
  #  viewport - the viewport for the sprite
  #----------------------------------------------------------------------------
  def initialize(viewport = nil)
    # call superclass
    super
    # create bitmap
    self.bitmap = Bitmap.new(320, 32)
    # set font to bold
    self.bitmap.font.bold = true
    # decrease font size
    self.bitmap.font.size -= 8
    # set font color
    self.bitmap.font.color = system_color
    # set x and y position
    self.x, self.y = 160, 0
    # item IDs on hotkeys
    @items = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    # skill IDs on hotkeys
    @skills = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    # draw the display
    draw
  end
  #----------------------------------------------------------------------------
  # draw
  #  Draws the hotkey display.
  #----------------------------------------------------------------------------
  def draw
    # iterate through all hotkeys
    (1..10).each {|i|
        # if any change applied (10 is used for 0)
        if @items[i%10] != $game_system.controls.items[i%10] ||
            @skills[i%10] != $game_system.controls.skills[i%10]
          # remove this icon
          self.bitmap.fill_rect(32*(i-1), 0, 32, 32, Color.new(0, 0, 0, 0))
          # fill icon bachground
          self.bitmap.fill_rect(32*(i-1)+4, 4, 24, 24, Color.new(0, 0, 0, 128))
          # if hotkey is skill hotkey
          if $game_system.controls.skills[i%10] != 0
            # temporary object
            object = $data_skills[$game_system.controls.skills[i%10]]
          # if hotkey is item hotkey
          elsif $game_system.controls.items[i%10] != 0
            # temporary object
            object = $data_items[$game_system.controls.items[i%10]]
          end
          # if object exists
          if object != nil
            # load bitmap
            bitmap = RPG::Cache.icon(object.icon_name)
            # draw bitmap
            self.bitmap.blt(32*(i-1)+4, 4, bitmap, Rect.new(0, 0, 24, 24), 255)
          end
          # draw hotkey number
          self.bitmap.draw_text_full(32*(i-1), 10, 30, 32, (i%10).to_s, 2)
        end}
    # set new items
    @items = $game_system.controls.items.clone
    # set new skills
    @skills = $game_system.controls.skills.clone
  end
  
end

#==============================================================================
# Mini_Map
#------------------------------------------------------------------------------
#  This class creates and handels the minimap/fullscreen map display and is
#  more efficient than the Window class.
#==============================================================================

class Mini_Map < Sprite
  
  # setting all accessable variables
  attr_reader :map_id
  #----------------------------------------------------------------------------
  # Initialization
  #----------------------------------------------------------------------------
  def initialize
    # call superclass method
    super(Viewport.new(476, 356, 160, 120))
    # get autotile image from Blizz-ABS Cache
    @autotile = BlizzABS::Cache.image(3)
    # creates the passable floor map
    create_passable_floor
    # set x and y position
    self.x = self.y = 0
    # set z position
    viewport.z = 5000
    # store events
    @events, @names = check_events
    # create sprites for events
    create_sevents
    # set all sprites visible
    self.visible = true
  end
  #----------------------------------------------------------------------------
  # create_passable_floor
  #  Creates the passable floor map on the bitmap.
  #----------------------------------------------------------------------------
  def create_passable_floor
    # delete bitmap if bitmap exists
    self.bitmap.dispose if self.bitmap != nil
    # store new map ID
    @map_id = $game_map.map_id
    # temporary width and height
    w, h = $game_map.width, $game_map.height
    # create bitmap
    self.bitmap = Bitmap.new(8*w, 8*h)
    # fill rectangle
    self.bitmap.fill_rect(0, 0, 8*w, 8*h, Color.new(0, 0, 0, 128))
    # get passability data
    v_map = $game_map.virtual_passability
    # iterate through all tiles
    (0...v_map.xsize).each {|x| (0...v_map.ysize).each {|y|
        # depending on passable direction, draw the path using the autotile
        case v_map[x, y]
        when 0x01 #    D
          self.bitmap.blt(x*8, y*8+4, @autotile, Rect.new(0, 0, 8, 4), 128)
        when 0x02 #   L
          self.bitmap.blt(x*8, y*8, @autotile, Rect.new(4, 0, 4, 8), 128)
        when 0x03 #   LD
          self.bitmap.blt(x*8, y*8, @autotile, Rect.new(16, 8, 8, 8), 128)
        when 0x04 #  R
          self.bitmap.blt(x*8+4, y*8, @autotile, Rect.new(0, 0, 4, 8), 128)
        when 0x05 #  R D
          self.bitmap.blt(x*8, y*8, @autotile, Rect.new(0, 8, 8, 8), 128)
        when 0x06 #  RL
          self.bitmap.blt(x*8, y*8, @autotile, Rect.new(8, 8, 8, 4), 128)
          self.bitmap.blt(x*8, y*8+4, @autotile, Rect.new(8, 28, 8, 4), 128)
        when 0x07 #  RLD
          self.bitmap.blt(x*8, y*8, @autotile, Rect.new(8, 8, 8, 8), 128)
        when 0x08 # U
          self.bitmap.blt(x*8, y*8, @autotile, Rect.new(0, 4, 8, 4), 128)
        when 0x09 # U  D
          self.bitmap.blt(x*8, y*8, @autotile, Rect.new(0, 16, 4, 8), 128)
          self.bitmap.blt(x*8+4, y*8, @autotile, Rect.new(20, 16, 4, 8), 128)
        when 0x0A # U L
          self.bitmap.blt(x*8, y*8, @autotile, Rect.new(16, 24, 8, 8), 128)
        when 0x0B # U LD
          self.bitmap.blt(x*8, y*8, @autotile, Rect.new(16, 16, 8, 8), 128)
        when 0x0C # UR
          self.bitmap.blt(x*8, y*8, @autotile, Rect.new(0, 24, 8, 8), 128)
        when 0x0D # UR D
          self.bitmap.blt(x*8, y*8, @autotile, Rect.new(0, 16, 8, 8), 128)
        when 0x0E # URL
          self.bitmap.blt(x*8, y*8, @autotile, Rect.new(8, 24, 8, 8), 128)
        when 0x0F # URLD
          self.bitmap.blt(x*8, y*8, @autotile, Rect.new(8, 16, 8, 8), 128)
        end}}
  end
  #----------------------------------------------------------------------------
  # update
  #  Updates the minimap and sprite movement on the minimap.
  #----------------------------------------------------------------------------
  def update(override = false)
    # creates the passable floor map if new map entered
    create_passable_floor if @map_id != $game_map.map_id
    # get events
    ev = check_events
    # if events or names changed
    if [@events, @names] != ev
      # store new events and names
      @events, @names = ev
      # delete sprites of events
      destroy_sevents
      # create sprites of events
      create_sevents
    end
    # if minimap not in fullscreen mode
    if $game_system.minimap < 2
      # set offset display
      self.ox, self.oy = $game_map.display_x / 16, $game_map.display_y / 16
    # if not pressed the turn button to scroll map around
    elsif !Input.press?(Input::Turn) || override
      # if map can be scrolled horizontally
      if self.bitmap.width > 640
        # get left border
        border = [0, -320 + $game_player.real_x/16].max
        # get right border and set offset
        self.ox = [border, -640 + self.bitmap.width].min
      else
        # center map display horizontally
        self.ox = -320 + self.bitmap.width/2
      end
      # if map can be scrolled vertically
      if self.bitmap.height > 480
        # get upper border
        border = [0, -240 + $game_player.real_y/16].max
        # get lower border and set offset
        self.oy = [border, -480 + self.bitmap.height].min
      else
        # center map display vertically
        self.oy = -240 + self.bitmap.height/2
      end
    end
    # iterate through all sprites
    @sevents.each_index {|i|
        # if minimap is not in fullscreen mode and within the range of ABSEAL
        if $game_system.minimap == 2 || @events[i].update?
          # set new coordinates
          @sevents[i].x = self.x + @events[i].real_x / 16
          @sevents[i].y = self.y + @events[i].real_y / 16
          # set offsets
          @sevents[i].ox, @sevents[i].oy = self.ox, self.oy
          # if event has a spriteset
          if @names[i] != '' &&
              (@events[i].is_a?(Map_Actor) ||
              (!@events[i].name.clone.gsub!('\box') {''}))
            # depending on the facing direction of the event
            @sevents[i].src_rect.set((@events[i].direction-2)*7, 0, 14, 14)
            # change offsets
            @sevents[i].ox += 3
            @sevents[i].oy += 3
          end
        end}
  end
  #----------------------------------------------------------------------------
  # check_events
  #  Checks all events.
  #----------------------------------------------------------------------------
  def check_events
    # events and names arrays
    events, names = [], []
    # iterate through all actors
    BlizzABS.player.actors.each {|actor|
        # if not dead
        unless actor.dead?
          # add event and spriteset name
          events.push(actor)
          names.push(actor.character_name)
        end}
    # iterate through all events
    $game_map.events.each_value {|event|
        # skip if defined to skip
        next if event.name.clone.gsub!('\map') {''}
        # if should be displayed
        if defined?(event.dead?) && !event.dead? ||
            event.is_a?(Game_Event) && !event.erased && (event.teleport ||
            event.is_a?(Drop_Event) || event.name.clone.gsub!('\spc') {''})
          # add enemy and spriteset name
          events.push(event)
          names.push(event.character_name)
        end}
    # return result
    return events, names
  end
  #----------------------------------------------------------------------------
  # create_sevents
  #  Creates for each event on the map a sprite on the minimap.
  #----------------------------------------------------------------------------
  def create_sevents
    # set empty array
    @sevents = []
    # ierate through all events on the minimap
    @events.each_index {|i|
        # create sprite
        sprite = Sprite.new(viewport)
        # temporary variable
        rect = Rect.new(0, 0, 56, 14)
        # if event is player
        if @events[i].class == Game_Player 
          # if player has spriteset
          if @names[i] != ''
            # create bitmap
            sprite.bitmap = Bitmap.new(56, 14)
            # get green arrow
            sprite.bitmap.blt(0, 0, BlizzABS::Cache.image(0), rect, 128)
          end
          # highest sprite
          sprite.z = 100
        # if event is actor
        elsif @events[i].class == Map_Actor
          # if actor has spriteset
          if @names[i] != ''
            # create bitmap
            sprite.bitmap = Bitmap.new(56, 14)
            # get green arrow
            sprite.bitmap.blt(0, 0, BlizzABS::Cache.image(0), rect, 128)
            # change arrow to blue
            sprite.bitmap.hue_change(120)
          end
          # 2nd highest sprite
          sprite.z = 80
        # if event is enemy
        elsif @events[i].class == Map_Enemy
          # if event without spriteset or "boxdraw" enforcing
          if @names[i] == '' || @events[i].name.clone.gsub!('\box') {''}
            # create bitmap
            sprite.bitmap = Bitmap.new(8, 8)
            # fill rectangle with black color
            sprite.bitmap.fill_rect(0, 0, 8, 8, Color.new(0, 0, 0, 128))
            # fill rectangle with red color
            sprite.bitmap.fill_rect(1, 1, 6, 6, Color.new(255, 0, 0, 128))
          else
            # create bitmap
            sprite.bitmap = Bitmap.new(56, 14)
            # get green arrow
            sprite.bitmap.blt(0, 0, BlizzABS::Cache.image(0), rect, 128)
            # change arrow to red
            sprite.bitmap.hue_change(-120)
          end
          # 5th highest sprite
          sprite.z = 50
        # if event is dropped item
        elsif @events[i].class == Drop_Event
          # create bitmap
          sprite.bitmap = Bitmap.new(8, 8)
          # fill rectangle with black color
          sprite.bitmap.fill_rect(0, 0, 8, 8, Color.new(0, 0, 0, 128))
          # fill rectangle with cyan color
          sprite.bitmap.fill_rect(1, 1, 6, 6, Color.new(0, 255, 255, 128))
          # 3rd highest sprite
          sprite.z = 70
        # if event is normal event
        elsif @events[i].class == Game_Event
          # if event has spc command
          if @events[i].name.clone.gsub!('\spc') {''}
            # temporary variables
            color, hue = Color.new(255, 255, 0, 128), -60
            # 4th highest sprite
            sprite.z = 60
          # if event code exists and te
          elsif @events[i].teleport
            # temporary variables
            color, hue = Color.new(128, 0, 255, 128), 150
            # 6th highest sprite
            sprite.z = 40
          end
          # if event without spriteset or "boxdraw" enforcing
          if @names[i] == '' || @events[i].name.clone.gsub!('\box') {''}
            # create bitmap
            sprite.bitmap = Bitmap.new(8, 8)
            # fill rectangle with black color
            sprite.bitmap.fill_rect(0, 0, 8, 8, Color.new(0, 0, 0, 128))
            # fill rectangle with yellow color
            sprite.bitmap.fill_rect(1, 1, 6, 6, color)
          else
            # create bitmap
            sprite.bitmap = Bitmap.new(56, 14)
            # get green arrow
            sprite.bitmap.blt(0, 0, BlizzABS::Cache.image(0), rect, 128)
            # change arrow to yellow
            sprite.bitmap.hue_change(hue)
          end
        # if event without spriteset or "boxdraw" enforcing
        elsif @names[i] == '' || @events[i].name.clone.gsub!('\box') {''}
          # create bitmap
          sprite.bitmap = Bitmap.new(8, 8)
          # fill rectangle with black color
          sprite.bitmap.fill_rect(0, 0, 8, 8, Color.new(0, 0, 0, 128))
          # fill rectangle with default white color
          sprite.bitmap.fill_rect(1, 1, 6, 6, Color.new(255, 255, 255, 128))
        else
          # create bitmap
          sprite.bitmap = Bitmap.new(56, 14)
          # get white arrow
          sprite.bitmap.blt(0, 0, BlizzABS::Cache.image(1), Rect.new(0, 0, 56, 14), 128)
        end
        # get sprite out of map screen so ABSEAL can work correctly
        sprite.ox = sprite.oy = 64
        # if event has a spriteset
        if sprite.bitmap.width != 8
          # depending on the facing direction of the event
          sprite.src_rect.set((@events[i].direction-2)*7, 0, 14, 14)
        end
        # add sprite
        @sevents.push(sprite)}
  end
  #----------------------------------------------------------------------------
  # destroy_sevents
  #  Deletes all sprites.
  #----------------------------------------------------------------------------
  def destroy_sevents
    @sevents.each {|i| i.dispose}
    @sevents = nil
  end
  #----------------------------------------------------------------------------
  # visible=
  #  expr - true of false
  #  Overriding the original method so the events sprites also get affected.
  #----------------------------------------------------------------------------
  def visible=(expr)
    # call superclass method
    super
    # set each sprite's visiblity
    @sevents.each {|sprite| sprite.visible = expr}
  end
  #----------------------------------------------------------------------------
  # dispose
  #  Removes Minimap from screen and memory.
  #----------------------------------------------------------------------------
  def dispose
    # delete sprites
    destroy_sevents
    # call superclass method
    super
  end
  
end

#==============================================================================
# Spriteset_Map
#------------------------------------------------------------------------------
#  This class was enhanced to create and handle caterpillar characters and to
#  take over and handle damage sprites upon their host's termination.
#==============================================================================

class Spriteset_Map
  
  # setting all accessable variables
  attr_accessor :viewport1
  attr_accessor :character_sprites
  #----------------------------------------------------------------------------
  # override Initialization
  #----------------------------------------------------------------------------
  alias init_blizzabs_later initialize
  def initialize
    # call original method
    init_blizzabs_later
    # iterate through all active projectiles and all actors except player
    (BlizzABS::Cache.projectiles + BlizzABS.player.actors -
        [BlizzABS.player.player]).each {|character|
        # create sprite
        sprite = Sprite_Character.new(@viewport1, character)
        # update sprite
        sprite.update
        # add sprite to character_sprites
        @character_sprites.push(sprite)}
    # set damage update flag
    @dmg_update = ($scene.is_a?(Scene_Map))
  end
  #----------------------------------------------------------------------------
  # override update
  #----------------------------------------------------------------------------
  alias upd_blizzabs_later update
  def update
    # iterate through all damage sprites
    BlizzABS::Cache.damages.each_index {|i|
        # temporary variable
        dmg = BlizzABS::Cache.damages[i]
        # if damage sprite opacity is 0
        if dmg[0].opacity == 0
          # delete damage sprite
          dmg[0].dispose
          # remove deleted damage sprite
          BlizzABS::Cache.damages[i] = nil
        # if damage sprites allowed to be updated
        elsif @dmg_update
          # calculate offset if map display position has changed
          dmg[0].x += (dmg[1] - $game_map.display_x) / 4
          dmg[0].y += (dmg[2] - $game_map.display_y) / 4
          # store new map display position
          BlizzABS::Cache.damages[i][1] = $game_map.display_x
          BlizzABS::Cache.damages[i][2] = $game_map.display_y
          # increased y position offset
          dmg[0].oy += 2
          # decrease opacity if over critical height
          dmg[0].opacity -= 15 if dmg[0].oy > 88
          # change hue if critical and each second frame
          if dmg[0].critical && Graphics.frame_count % 2 == 0
            # make hue change animation
            dmg[0].bitmap.hue_change(60)
          end
        end}
    # iterate through all character sprites
    @character_sprites.clone.each {|sprite|
        # if character which the sprite observes is a dead enemy
        if sprite.character.is_a?(Map_Enemy) && sprite.character.dead?
          # set dying flag
          sprite.dying = true
        # if character which the sprite observes is a skill projectile
        elsif sprite.character.is_a?(Projectile) && sprite.character.fade_out
          # set fade out flag
          sprite.fade_out = true
        end
        # if dying
        if sprite.dying
          # update die
          sprite.update_die
        # if fading in
        elsif sprite.fade_in
          # update fade in
          sprite.update_fade_in
        # if fading out
        elsif sprite.fade_out
          # update fadeinance
          sprite.update_fade_out
        end
        # if sprite died and ready for deletion or expired character
        if sprite.character.terminate
          # if character is projectile and projectile expired
          if sprite.character.is_a?(Projectile)
            # remove projectile from active projectiles
            BlizzABS::Cache.projectiles.delete(sprite.character)
          # if character which the sprite observes is enemy and not a boss
          elsif sprite.character.is_a?(Map_Enemy) && !sprite.character.boss
            # push into killed array and set respawn time
            $game_system.killed.push([sprite.character, BlizzABS::Config::RESPAWN_TIME*20])
          end
          # dispose sprite
          sprite.dispose
          # remove sprite from spriteset
          @character_sprites.delete(sprite)
        end}
    # remove all nil values from damages
    BlizzABS::Cache.damages.compact!
    # call original method
    upd_blizzabs_later
  end
  
end

#==============================================================================
# Interpreter
#------------------------------------------------------------------------------
#  This class was enhanced to support pixel movement for the force move command
#  in case the player is affected. It was also enhanced to support Blizz-ABS
#  battle handling and ABSEAL limitation.
#==============================================================================

class Interpreter
  
  #----------------------------------------------------------------------------
  # override command_end
  #----------------------------------------------------------------------------
  alias cmd_end_blizzabs_later command_end
  def command_end
    # delete event code
    @list = nil
    # call original method if event exists and return result or return true
    return ($game_map.events[@event_id] != nil ? cmd_end_blizzabs_later : true)
  end
  #----------------------------------------------------------------------------
  # override command_201
  #----------------------------------------------------------------------------
  alias cmd_201_blizzabs_later command_201
  def command_201
    # set in_battle flag if on the map
    $game_temp.in_battle = false
    # call original method
    return cmd_201_blizzabs_later
  end
  #----------------------------------------------------------------------------
  # override command_209
  #----------------------------------------------------------------------------
  alias cmd_209_blizzabs_later command_209
  def command_209
    # call original method
    result = cmd_209_blizzabs_later
    # if REPAIR_MOVEMENT is turned on and character is player
    if $game_system.move_fix && get_character(@parameters[0]) == $game_player
      # create command list duplicate
      old_list = @parameters[1].list.clone
      # remove original command list
      @parameters[1].list = []
      # iterate through all commands
      old_list.each {|command|
          # add command to command list
          @parameters[1].list.push(command)
          # if one of the movement commands
          if command.code >= 1 && command.code <= 13
            # add pixel movement rate - 1 times to correct movement
            (BlizzABS.pixel-1).times{@parameters[1].list.push(command)}
          end}
    end
    # return result
    return result
  end
  
end

#==============================================================================
# Scene_Title
#------------------------------------------------------------------------------
#  This class was enhanced to size down the animations upon loading.
#==============================================================================

class Scene_Title
  
  #----------------------------------------------------------------------------
  # override main
  #----------------------------------------------------------------------------
  alias main_blizzabs_later main
  def main
    # call original method
    main_blizzabs_later
    # if SMAlL_ANIMATIONS is turned on and scene exists
    if BlizzABS::Config::SMALL_ANIMATIONS && $scene != nil
      # size down animations
      BlizzABS.animations_size_down
    end
  end
  
end

#==============================================================================
# Scene_Map
#------------------------------------------------------------------------------
#  This class was enhanced to support HUD control and creation system and
#  Blizz-ABS battle handling and level up text display.
#==============================================================================

class Scene_Map
  
  # setting all accessable variables
  attr_accessor :spriteset
  #----------------------------------------------------------------------------
  # override main
  #----------------------------------------------------------------------------
  alias main_blizzabs_later main
  def main
    # create HUD if HUD_ENABLED is turned on and HUD active
    @hud = Hud.new if BlizzABS::Config::HUD_ENABLED && $game_system.hud
    # tests and sets the in_battle flag
    test_in_battle
    # call original method
    main_blizzabs_later
    # set in_battle flag
    $game_temp.in_battle = false
    # delete HUD if HUD exists
    @hud.dispose if @hud != nil
  end
  #----------------------------------------------------------------------------
  # test_in_battle
  #  Sets the in_battle flag to control game flow.
  #----------------------------------------------------------------------------
  def test_in_battle
    # if master override is being used
    if $game_system.blizzabs != nil
      # enforce user's setting
      $game_temp.in_battle = $game_system.blizzabs
    else
      # if event code is being executed or message window is being displayed
      if $game_system.map_interpreter.running? || $game_temp.message_window_showing
        # disable Blizz-ABS controls
        $game_temp.in_battle = false
      else
        # depending on chosen DISABLE_ABS_MODE in battle or not in battle
        $game_temp.in_battle = case BlizzABS::Config::DISABLE_ABS_MODE
        when 0 then true
        when 1 then ($game_system.enemy_number > 0)
        when 2 then ($game_map.enemies.size > 0)
        when 3 then ($game_system.enemies_in_range > 0)
        end
      end
    end
  end
  #----------------------------------------------------------------------------
  # override update
  #----------------------------------------------------------------------------
  alias upd_blizzabs_later update
  def update
    # if temporary character selection
    if $game_temp.select_data != nil
      # call selection update
      update_selection
      # abort scene
      return
    end
    # tests and sets the in_battle flag
    test_in_battle
    # needed to prevent a glitch
    $game_temp.battle_turn = 1
    # if minimap button is pressed
    if Input.trigger?(Input::Minimap)
      # trigger minimap active
      $game_system.minimap = ($game_system.minimap + 1) % 3
    end
    # force minimap off if MINIMAP is turned off
    $game_system.minimap = 0 unless BlizzABS::Config::MINIMAP
    # if hotkey display button is pressed
    if Input.trigger?(Input::Hotkey)
      # trigger hotkey display active
      $game_system.assignment = (!$game_system.assignment)
    end
    # trigger HUD active if HUD button is pressed
    $game_system.hud = (!$game_system.hud) if Input.trigger?(Input::Hud)
    # if HUD not active and HUD exists
    if !$game_system.hud && @hud != nil
      # delete HUD
      @hud.dispose
      @hud = nil
    # if HUD_ENABLED is turned on and HUD active and HUD doesn't exist
    elsif BlizzABS::Config::HUD_ENABLED && $game_system.hud && @hud == nil
      # create HUD
      @hud = Hud.new
    end
    # update HUD if HUD exists
    @hud.update if @hud != nil
    # game over if all actors are dead
    $game_temp.gameover = $game_party.actors.all? {|actor| actor.dead?}
    # if game over
    if $game_temp.gameover
      # play collapse sound effect
      $game_system.se_play($data_system.actor_collapse_se)
      # call original method
      upd_blizzabs_later
      # reset projectiles and damage sprites
      BlizzABS::Cache.clean
      # exit method
      return
    end
    # iterate through all actors
    $game_party.actors.each {|actor|
        # if leveled up
        if actor.level_up?
          # recover if HEAL_ON_LVLUP is turned on
          actor.recover_all if BlizzABS::Config::HEAL_ON_LVLUP
          # set damage text to "LvUp" if DISPLAY_LVLUP is turned on
          actor.damage = 'LvUp' if BlizzABS::Config::DISPLAY_LVLUP
          # if ANIMATIONS is turned on
          if BlizzABS::Config::ANIMATIONS
            # if first actor
            if actor.index == 0
              # set animation ID if LVLUP_ANIMATION_ID is turned on
              $game_player.animation_id = BlizzABS::Config::LVLUP_ANIMATION_ID
            # if CATERPILLAR is turned on
            elsif BlizzABS::Config::CATERPILLAR
              # set animation ID
              BlizzABS.player.actors[actor.index].animation_id =
                  BlizzABS::Config::LVLUP_ANIMATION_ID
            end
          end
        end}
    # call original method
    upd_blizzabs_later
  end
  #----------------------------------------------------------------------------
  # update_selection
  #  This method overrides everything else in the map scene to allow the player
  #  to select an opponent to be attacked.
  #----------------------------------------------------------------------------
  def update_selection
    # if not initialized select interruption
    if @index == nil
      # increase z coordinate of all targets
      $game_temp.select_data[2].each {|sprite| sprite.z += 1000000}
      # initialized select interruption
      @index = 0
      # freeze screen display
      Graphics.freeze
      # temporary variable
      tone = $game_screen.tone
      # make screen slightly darker
      $scene.spriteset.viewport1.tone = Tone.new(tone.red-32, tone.green-32,
          tone.blue-32, tone.gray)
      # temporary variable
      user = $game_temp.select_data[0]
      # play decision sound
      $game_system.se_play($data_system.decision_se)
      # create help window
      @win = Window_Help.new
      # make partially transparent and set z coordinate
      @win.z, @win.opacity = 10000, 192
      # gets range display radius
      r = [BlizzABS::Skills.range($game_temp.select_data[1].id)*32, 32].max
      # create 2 sprite
      @range1 = Sprite.new(@spriteset.viewport1)
      @range2 = Sprite.new(@spriteset.viewport1)
      # set z coordinate
      @range1.z = @range2.z = 950000
      # if targeting all targets and fullscreen skill
      if BlizzABS::Skills.type($game_temp.select_data[1].id)[0] == 3 &&
          [2, 4, 6].include?($game_temp.select_data[1].scope)
        # create 2 bitmaps for the sprites
        @range1.bitmap = Bitmap.new(640, 480)
        @range2.bitmap = Bitmap.new(638, 478)
        # draw big yellow rectangle
        @range1.bitmap.fill_rect(0, 0, 640, 480, Color.new(255, 255, 0, 160))
        # remove inner rectangle area
        @range1.bitmap.fill_rect(1, 1, 638, 478, Color.new(0, 0, 0, 0))
        # set x and y coordinate
        @range2.x = @range2.y = 1
        # if selecting an enemy
        if $game_temp.select_data[1].scope < 3
          # draw slightly smaller red circle
          @range2.bitmap.fill_rect(0, 0, 638, 478, Color.new(255, 0, 0, 96))
        else
          # draw slightly smaller blue circle
          @range2.bitmap.fill_rect(0, 0, 638, 478, Color.new(0, 128, 255, 96))
        end
      else
        # create 2 bitmaps for the sprites
        @range1.bitmap = Bitmap.new(r*2+32, r*2+32)
        @range2.bitmap = Bitmap.new(r*2+32, r*2+32)
        # set sprite position
        @range1.x, @range1.y = user.screen_x, user.screen_y
        @range2.x, @range2.y = user.screen_x, user.screen_y
        # set sprite position offset
        @range1.ox, @range1.oy = r+16, r+32
        @range2.ox, @range2.oy = r+16, r+32
        # draw big yellow circle
        @range1.bitmap.draw_circle(0, 0, r.to_i+16, Color.new(255, 255, 0, 160))
        # remove area that is smaller by radius of 1
        @range1.bitmap.draw_circle(1, 1, r.to_i+15, Color.new(0, 0, 0, 0))
        # if selecting an enemy
        if $game_temp.select_data[1].scope < 3
          # draw slightly smaller red circle
          @range2.bitmap.draw_circle(1, 1, r.to_i+15, Color.new(255, 0, 0, 96))
        else
          # draw slightly smaller blue circle
          @range2.bitmap.draw_circle(1, 1, r.to_i+15, Color.new(0, 128, 255, 96))
        end
      end
      # if targeting all targets
      if [2, 4, 6].include?($game_temp.select_data[1].scope)
        # all targets are selected
        $game_temp.select_data[2].each {|sprite| sprite.select = 1}
        # display "All" in help window
        @win.set_text('All', 1)
      else
        # first target is selected
        $game_temp.select_data[2][0].select = 1
        # display target's name in help window
        @win.set_text($game_temp.select_data[2][0].character.battler.name, 1)
      end
      # set current yellow blinking of sprite
      @range2.color.set(255, 255, 0, (16-Graphics.frame_count%32).abs * 8)
      # make screen transition
      Graphics.transition
    end
    # animate yellow blinking of sprite
    @range2.color.set(255, 255, 0, (16-Graphics.frame_count%32).abs * 8)
    # update select animation for all selectable sprites
    $game_temp.select_data[2].each {|sprite| sprite.update_select}
    # if not targeting all target
    unless [2, 4, 6].include?($game_temp.select_data[1].scope)
      # display target's name in help window
      @win.set_text($game_temp.select_data[2][@index].character.battler.name, 1)
    end
    # if not targeting all enemies
    if [1, 3, 5].include?($game_temp.select_data[1].scope)
      # if pressed left or up
      if Input.repeat?(Input::LEFT) || Input.repeat?(Input::UP)
        # play cursor sound
        $game_system.se_play($data_system.cursor_se)
        # deselect currently selected sprite
        $game_temp.select_data[2][@index].select = 0
        # change selection index
        @index = (@index+1) % $game_temp.select_data[2].size
        # select currently selected sprite
        $game_temp.select_data[2][@index].select = 1
      # if pressed right or down
      elsif Input.repeat?(Input::RIGHT) || Input.repeat?(Input::DOWN)
        # play cursor sound
        $game_system.se_play($data_system.cursor_se)
        # deselect currently selected sprite
        $game_temp.select_data[2][@index].select = 0
        # change selection index
        @index = (@index+$game_temp.select_data[2].size-1) %
            $game_temp.select_data[2].size
        # select currently selected sprite
        $game_temp.select_data[2][@index].select = 1
      end
    end
    if Input.repeat?(Input::B)
      # play cancel sound
      $game_system.se_play($data_system.cancel_se)
      # cancelled
      targets = false
    elsif Input.repeat?(Input::C)
      # play decision sound
      $game_system.se_play($data_system.decision_se)
      # if targeting all enemies
      if [2, 4, 6].include?($game_temp.select_data[1].scope)
        # initialize array
        targets = []
        # add all targets
        $game_temp.select_data[2].each {|sprite| targets.push(sprite.character)}
      else
        # decided target
        targets = [$game_temp.select_data[2][@index].character]
      end
    end
    # if target exists or cancelled
    if targets != nil
      # freeze screen display
      Graphics.freeze
      # iterate through all target sprites
      $game_temp.select_data[2].each {|sprite|
          # deselect sprite
          sprite.select = 0
          # remove selection animation completely
          sprite.update_select
          # reset z coordinate
          sprite.z -= 1000000}
      # reset screen tint
      $scene.spriteset.viewport1.tone = $game_screen.tone
      # temporary variables
      ch = $game_temp.select_data[0]
      object = $game_temp.select_data[1]
      # if not cancelled
      if targets
        # determine reference variable skill and skill/item type
        case object
        when RPG::Skill then skill, type = true, BlizzABS::Skills.type(object.id)
        when RPG::Item then skill, type = false, BlizzABS::Items.type(object.id)
        end
        # set animation ID if ANIMATIONS is turned on
        ch.animation_id = object.animation1_id if BlizzABS::Config::ANIMATIONS
        # if skill/item is projectile
        if type[0] == 1
          # if skill
          if skill
            # set projectile type to either homing skill or homing item
            projectype = 7
            # SP consumption
            ch.battler.sp -= object.sp_cost
          else
            # set projectile type to either homing skill or homing item
            projectype = 11
            # item consumption
            $game_party.lose_item(object.id, 1)
          end
          # iterate through all targets
          targets.each {|target|
              # if exploding skill/item
              if type[1] > 0
                # create exploding projectile
                proj = Projectile.new(object.icon_name, ch, object.id, target,
                    projectype, Map_Enemy, ![5, 6].include?(object.scope),
                    type[1, 2])
              else
                # create projectile
                proj = Projectile.new(object.icon_name, ch, object.id, target,
                    projectype, Map_Enemy, ![5, 6].include?(object.scope))
              end
              # add projectile to buffer
              BlizzABS::Cache.projectiles.push(proj)}
        # if skill
        elsif skill
          # use skill instantly
          targets.each {|t| t.skill_effect(ch, ch.battler, object)}
          # SP consumption
          ch.battler.sp -= object.sp_cost
        else
          # use item instantly
          targets.each {|target| target.item_effect(ch, object)}
          # item consumption
          $game_party.lose_item(object.id, 1)
        end
        # setup sprite extension whether skill or item
        ch.setup_sprites(skill ? '_skl' : '_itm')
        # set extended frame penalty
        ch.set_action(1.6)
        # if skill calls common event
        if object.common_event_id > 0
          # temporary variable
          common_event = $data_common_events[object.common_event_id]
          # setup common event execution
          $game_system.map_interpreter.setup(common_event.list, 0)
        end
      end
      # delete range sprites and help window
      @range1.dispose
      @range2.dispose
      @win.dispose
      # remove all temporary select interuption data from memory
      @range1 = @range2 = @index = @tone = @win = $game_temp.select_data = nil
      # make screen transition
      Graphics.transition
    end
  end
  #----------------------------------------------------------------------------
  # override call_menu
  #----------------------------------------------------------------------------
  alias call_menu_blizzabs_later call_menu
  def call_menu
    # call original method if player not in action
    call_menu_blizzabs_later unless $game_player.in_action > 0
  end
  
end

#==============================================================================
# Window_Skill_Hotkey
#------------------------------------------------------------------------------
#  This class serves as display for skills that can be hotkeyed.
#==============================================================================

class Window_Skill_Hotkey < Window_Skill
  
  # setting all accessable variables
  attr_reader :item_max
  #----------------------------------------------------------------------------
  # Initialization
  #  actor - actor
  #----------------------------------------------------------------------------
  def initialize(actor)
    # call superclass method
    super
    # set max column number
    @column_max = 1
    # set width and height
    self.width, self.height = 320, 416
    # create bitmap
    self.contents = Bitmap.new(width - 32, height - 32)
    # set y position
    self.y = 64
    # remove cursor display
    self.cursor_rect.empty
    # set to not active
    self.active = false
    # set z position
    self.z = 21000
    # refresh display
    refresh
  end
  #----------------------------------------------------------------------------
  # update
  #  Updates only if window is active.
  #----------------------------------------------------------------------------
  def update
    super if self.active
  end
  #----------------------------------------------------------------------------
  # switch_actor
  #  Switch to next actor.
  #----------------------------------------------------------------------------
  def switch_actor
    # get next actor in line
    @actor = $game_party.actors[(@actor.index+1)%$game_party.actors.size]
    # refresh display
    refresh
    # if previous actor had more skills than the current one
    if @index >= @item_max
      # set cursor to last skill
      @index = @item_max - 1
      # update cursor
      update_cursor_rect
    end
  end
  #----------------------------------------------------------------------------
  # refresh
  #  Draws the data on the window.
  #----------------------------------------------------------------------------
  def refresh
    # if bitmap exists
    if self.contents != nil
      # delete bitmap
      self.contents.dispose
      self.contents = nil
    end
    # create array
    @data = []
    # add all learned skills
    @actor.skills.each {|id| @data.push($data_skills[id])}
    # add nil
    @data.push(nil)
    # set size
    @item_max = @data.size
    # create bitmap
    self.contents = Bitmap.new(width - 32, @item_max * 32)
    # draw each skill
    (0...@item_max).each {|i| draw_item(i)}
  end
  #----------------------------------------------------------------------------
  # draw_item
  #  index - skill index
  #  Draws one complete skill.
  #----------------------------------------------------------------------------
  def draw_item(i)
    # if skill is nil
    if @data[i] == nil
      # draw "<Remove>"
      self.contents.draw_text(32, i*32, 204, 32, '<Remove>', 0)
    else
      # if skill can be used
      if @actor.skill_can_use?(@data[i].id)
        # set font color
        self.contents.font.color = normal_color
      else
        # set font color
        self.contents.font.color = disabled_color
      end
      # clean this display
      self.contents.fill_rect(Rect.new(4, i*32, 288, 32), Color.new(0, 0, 0, 0))
      # get icon bitmap
      bitmap = RPG::Cache.icon(@data[i].icon_name)
      # get opacity
      opacity = self.contents.font.color == normal_color ? 255 : 128
      # draw icon bitmap
      self.contents.blt(4, 4+i*32, bitmap, Rect.new(0, 0, 24, 24), opacity)
      # draw skill name
      self.contents.draw_text(32, i*32, 204, 32, @data[i].name, 0)
      # draw skill SP cost
      self.contents.draw_text(236, i*32, 48, 32, @data[i].sp_cost.to_s, 2)
    end
  end
  
end

#==============================================================================
# Window_Item_Hotkey
#------------------------------------------------------------------------------
#  This class serves as display for items that can be hotkeyed.
#==============================================================================

class Window_Item_Hotkey < Window_Item
  
  # setting all accessable variables
  attr_reader :item_max
  #----------------------------------------------------------------------------
  # Initialization
  #  actor - actor
  #----------------------------------------------------------------------------
  def initialize
    # call superclass method
    super
    # set max column number
    @column_max = 1
    # set width and
    self.width, self.height = 320, 416
    # create bitmap
    self.contents = Bitmap.new(width - 32, height - 32)
    # set x and y position
    self.x, self.y = 320, 64
    # remove cursor display
    self.cursor_rect.empty
    # set to not active
    self.active = false
    # set z position
    self.z = 21000
    # refresh display
    refresh
  end
  #----------------------------------------------------------------------------
  # update
  #  Updates only if window is active
  #----------------------------------------------------------------------------
  def update
    # update only if actove
    super if self.active
  end
  #----------------------------------------------------------------------------
  # refresh
  #  Draws the data on the window.
  #----------------------------------------------------------------------------
  def refresh
    # if bitmap exists
    if self.contents != nil
      # delete bitmap
      self.contents.dispose
      self.contents = nil
    end
    # create array
    @data = []
    # iterate through all items
    (1...$data_items.size).each {|i|
        # add item if number of items in possesion greater than 0
        @data.push($data_items[i]) if $game_party.item_number(i) > 0}
    # add nil
    @data.push(nil)
    # set size
    @item_max = @data.size
    # create bitmap
    self.contents = Bitmap.new(width - 32, @item_max * 32)
    # draw each item
    (0...@item_max).each {|i| draw_item(i)}
  end
  #----------------------------------------------------------------------------
  # draw_item
  #  index - item index
  #  Draws one complete item.
  #----------------------------------------------------------------------------
  def draw_item(i)
    # if item is nil
    if @data[i] == nil
      # draw "<Remove>"
      self.contents.draw_text(32, i*32, 212, 32, '<Remove>', 0)
    else
      # get number of items
      number = $game_party.item_number(@data[i].id)
      # if item can be used
      if $game_party.item_can_use?(@data[i].id)
        # set font color
        self.contents.font.color = normal_color
      else
        # set font color
        self.contents.font.color = disabled_color
      end
      # clean this display
      self.contents.fill_rect(Rect.new(4, i*32, 288, 32), Color.new(0, 0, 0, 0))
      # get icon bitmap
      bitmap = RPG::Cache.icon(@data[i].icon_name)
      # get opacity
      opacity = self.contents.font.color == normal_color ? 255 : 128
      # draw icon bitmap
      self.contents.blt(4, 4+i*32, bitmap, Rect.new(0, 0, 24, 24), opacity)
      # draw item name
      self.contents.draw_text(32, i*32, 212, 32, @data[i].name, 0)
      # draw ":"
      self.contents.draw_text(244, i*32, 16, 32, ':', 1)
      # draw number of items left
      self.contents.draw_text(260, i*32, 24, 32, number.to_s, 2)
    end
  end
  
end

#==============================================================================
# Window_Message
#------------------------------------------------------------------------------
#  This class was modified to override Blizz-ABS battle handling for correct
#  window position display.
#==============================================================================

class Window_Message < Window_Selectable
  
  #----------------------------------------------------------------------------
  # override reset_window
  #----------------------------------------------------------------------------
  alias reset_window_blizzabs_later reset_window
  def reset_window
    # store in_battle flag
    tmp = $game_temp.in_battle
    # set in_battle flag
    $game_temp.in_battle = false
    # call original method
    reset_window_blizzabs_later
    # restore in_battle flag
    $game_temp.in_battle = tmp
  end
  
end

#==============================================================================
# Scene_Menu
#------------------------------------------------------------------------------
#  This class was modified to infilitrate the real menu with the Blizz-ABS
#  Pre-Menu.
#==============================================================================

class Scene_Menu
  
  #----------------------------------------------------------------------------
  # override Initialization
  #  index - the cursor index
  #----------------------------------------------------------------------------
  alias init_blizzabs_later initialize
  def initialize(index = nil)
    # set index flag
    @index_flag = index
    # call original method with either 0 or the current index
    init_blizzabs_later(index == nil ? 0 : index)
  end
  #----------------------------------------------------------------------------
  # override main
  #----------------------------------------------------------------------------
  alias main_blizzabs_later main
  def main
    # if index flag does not exist
    if @index_flag == nil
      # set in_battle flag
      $game_temp.in_battle = true
      # create HUD if HUD_ENABLED is turned on and HUD active
      @hud = Hud.new if BlizzABS::Config::HUD_ENABLED && $game_system.hud
      # create options window
      @window = Window_Command.new(192, ['Menu', 'AI Setup', 'Controls', 'Cancel'])
      # disable second option (not available yet)
      @window.disable_item(1)
      # set x and y position
      @window.x, @window.y = 320 - @window.width/2, 240 - @window.height/2
      # set z position
      @window.z = 21000
      # set back opacity
      @window.back_opacity = 160
      # create spriteset
      @spriteset = Spriteset_Map.new
      # create viewport
      @view = Viewport.new(0, 0, 640, 480)
      # tint viewport
      @view.tone = case BlizzABS::Config::MENU_COLOR_TINT
      when 0
        # a random tint
        case rand(8)
        # darker tint
        when 0 then Tone.new(-60, -60, -60, 0)
        # blue tint
        when 1 then Tone.new(-255, -255, 0, 255)
        # green tint
        when 2 then Tone.new(-255, 0, -255, 255)
        # red tint
        when 3 then Tone.new(0, -255, -255, 255)
        # yellow tint
        when 4 then Tone.new(0, 0, -255, 255)
        # mangenta tint
        when 5 then Tone.new(0, -255, 0, 255)
        # cyan tint
        when 6 then Tone.new(-255, 0, 0, 255)
        # black-white tint
        when 7 then Tone.new(-40, -40, -40, 255)
        end
      # blue tint
      when 1 then Tone.new(-255, -255, 0, 255)
      # green tint
      when 2 then Tone.new(-255, 0, -255, 255)
      # red tint
      when 3 then Tone.new(0, -255, -255, 255)
      # yellow tint
      when 4 then Tone.new(0, 0, -255, 255)
      # mangenta tint
      when 5 then Tone.new(0, -255, 0, 255)
      # cyan tint
      when 6 then Tone.new(-255, 0, 0, 255)
      # black-white tint
      when 7 then Tone.new(-40, -40, -40, 255)
      # darker tint
      when 8 then Tone.new(-60, -60, -60, 0)
      end
      # transition
      Graphics.transition(10)
      # loop
      loop do
        # update game screen
        Graphics.update
        # update input
        Input.update
        # stop if frame update
        break if update_before_main
      end
      # freeze screen
      Graphics.freeze
      # delete HUD if HUD exists
      @hud.dispose if @hud != nil
      # delete window
      @window.dispose
      # delete spriteset
      @spriteset.dispose
      # delete viewport (screen tint) if new scene is still the menu or map
      @view.dispose if $scene.is_a?(Scene_Menu) || $scene.is_a?(Scene_Map)
    end
    # call original method if scene is still the menu
    main_blizzabs_later if $scene.is_a?(Scene_Menu)
  end
  #----------------------------------------------------------------------------
  # update_before_main
  #  Processes the pre-menu.
  #----------------------------------------------------------------------------
  def update_before_main
    # update window
    @window.update
    # if window is active
    if @window.active
      # if B is pressed
      if Input.trigger?(Input::B)
        # play cancel sound
        $game_system.se_play($data_system.cancel_se)
        # create map scene
        $scene = Scene_Map.new
        # exit this scene
        return true
      # if C is pressed
      elsif Input.trigger?(Input::C)
        # which option
        case @window.index
        when 0
          # play sound
          $game_system.se_play($data_system.decision_se)
          # set in_battle flag
          $game_temp.in_battle = false
        when 1
          # play buzzer sound effect
          $game_system.se_play($data_system.buzzer_se)
          # don't exit this scene
          return false
        when 2
          # play sound
          $game_system.se_play($data_system.decision_se)
          # create hotkey assignment scene with the current screen tint
          $scene = Scene_Controls.new(@view.tone)
        when 3
          # play sound
          $game_system.se_play($data_system.decision_se)
          # create map scene
          $scene = Scene_Map.new
        end
        # exit this scene
        return true
      end
    end
    # don't exit this scene
    return false
  end
  
end

#==============================================================================
# Scene_Controls
#------------------------------------------------------------------------------
#  This class handles the skill/item hotkey processing.
#==============================================================================

class Scene_Controls
  
  #----------------------------------------------------------------------------
  # Initialization
  #  tone - screen background tone
  #----------------------------------------------------------------------------
  def initialize(tone)
    # store current screen tint
    @tone = tone
  end
  #----------------------------------------------------------------------------
  # main
  #  The main processing method.
  #----------------------------------------------------------------------------
  def main
    # create spriteset
    @spriteset = Spriteset_Map.new
    # create viewport
    @view = Viewport.new(0, 0, 640, 480)
    # set tone to current screen tone
    @view.tone = @tone.clone
    # creat HUD if HUD_ENABLED is turned on and HUD active
    @hud = Hud.new if BlizzABS::Config::HUD_ENABLED && $game_system.hud
    # if hotkey display is turned off
    unless $game_system.assignment
      # create hotkey display
      @hotkeys = Hotkey_Assignment.new
      # set z position
      @hotkeys.z = 5000
    end
    # create sprite
    @choice = Sprite.new
    # create bitmap
    @choice.bitmap = Bitmap.new(16, 9)
    # draw arrow image from BlizzABS Cache
    @choice.bitmap.blt(0, 0, BlizzABS::Cache.image(2), Rect.new(0, 0, 16, 9), 128)
    # set x, y and z positions
    @choice.x, @choice.y, @choice.z = 160, 40, 500
    # set x position offset
    @choice.ox = -8
    # set active flag
    @active = true
    # set index
    @index = 0
    # set up mode flag
    @up_mode = true
    # create modified skill window
    @skill_window = Window_Skill_Hotkey.new($game_player.battler)
    # create modified item window
    @item_window = Window_Item_Hotkey.new
    # set last active
    @last_active = true
    # transtition
    Graphics.transition
    # loop
    loop do
      # update game screen
      Graphics.update
      # update input
      Input.update
      # frame update
      update
      # stop if chosen an option
      break if $scene != self
    end
    # freeze screen
    Graphics.freeze
    # delet spriteset
    @spriteset.dispose
    # delete HUD if HUD exists
    @hud.dispose if @hud != nil
    # delete hotkey display if not hotkey display active
    @hotkeys.dispose unless $game_system.assignment
    # delete choice sprite
    @choice.dispose
    # delete skill window
    @skill_window.dispose
    # delete item window
    @item_window.dispose
    # delete viewport
    @view.dispose
  end
  #----------------------------------------------------------------------------
  # update
  #  The update processing method.
  #----------------------------------------------------------------------------
  def update
    # update choice sprite
    @choice.update
    # update skill window
    @skill_window.update
    # update item window
    @item_window.update
    # move by 2 or 1 whether active in direction depending on @up_mode
    @choice.oy += (@up_mode ? (@active ? 2 : 1) : (@active ? -2 : -1))
    # set new @up_mode if necesseray depending on @up_mode
    @up_mode = (@up_mode ? (@choice.oy < 8) : (@choice.oy <= -8))
    # if select button pressed
    if Input.trigger?(Input::Select)
      # switch to next actor
      @skill_window.switch_actor
    # if active
    elsif @active
      # set choice offset always to a number dividable with 2
      @choice.oy = @choice.oy / 2 * 2
      # update hotkey selection
      update_choice
    # if skill window is active
    elsif @skill_window.active
      # update skill selection
      update_skill
    # if item window is active
    elsif @item_window.active
      # update item selection
      update_item
    end
  end
  #----------------------------------------------------------------------------
  # update_choice
  #  Updates input during the hotkey selection.
  #----------------------------------------------------------------------------
  def update_choice
    # set x position
    @choice.x = 160 + @index * 32
    # if pressed B
    if Input.trigger?(Input::B)
      # play cancel sound
      $game_system.se_play($data_system.cancel_se)
      # create map scene
      $scene = Scene_Map.new
    # if C is pressed
    elsif Input.trigger?(Input::C)
      # play sound
      $game_system.se_play($data_system.decision_se)
      # not active
      @active = false
      # the one that was active the last time is now active
      @skill_window.active = @last_active
      @item_window.active = (!@last_active)
    # if RIGHT is being pressed
    elsif Input.repeat?(Input::RIGHT)
      # if RIGHT is pressed or index is less than 9
      if Input.trigger?(Input::RIGHT) || @index < 9
        # play sound
        $game_system.se_play($data_system.cursor_se)
        # set new index
        @index = (@index + 1) % 10
      end
    # if LEFT is being pressed
    elsif Input.repeat?(Input::LEFT)
      # if LEFT is pressed or index is equal or greater than 1
      if Input.trigger?(Input::LEFT) || @index >= 1
        # play sound
        $game_system.se_play($data_system.cursor_se)
        # set new index
        @index = (@index + 9) % 10
      end
    end
  end
  #----------------------------------------------------------------------------
  # update_skill
  #  Updates input during the skill selection.
  #----------------------------------------------------------------------------
  def update_skill
    # set last active
    @last_active = true
    # if B is pressed
    if Input.trigger?(Input::B)
      # play cancel sound
      $game_system.se_play($data_system.cancel_se)
      # set active
      @active = true
      # skill window is not active
      @skill_window.active = false
      # delete cursor
      @skill_window.cursor_rect.empty
    # if C is pressd
    elsif Input.trigger?(Input::C)
      # play sound
      $game_system.se_play($data_system.decision_se)
      # if last position
      if @skill_window.index == @skill_window.item_max - 1
        # remove hotkey assigmnent from skill
        $game_system.controls.skills[(@index+1)%10] = 0
        # remove hotkey assigmnent from item
        $game_system.controls.items[(@index+1)%10] = 0
      else
        # set skill to hotkey
        $game_system.controls.skills[(@index+1)%10] = @skill_window.skill.id
        # remove hotkey assigmnent from item
        $game_system.controls.items[(@index+1)%10] = 0
      end
      # if hotkey display exists
      if @hotkeys != nil
        # draw hotkey display
        @hotkeys.draw
      # if HUD_ENABLED is turned on and HUD is active
      elsif BlizzABS::Config::HUD_ENABLED && $game_system.hud
        # draw hotkey display within the HUD
        @hud.assignment.draw
      end
      # set active
      @active = true
      # skill window is not active
      @skill_window.active = false
      # delete cursor
      @skill_window.cursor_rect.empty
    # if RIGHT or LEFT is pressed
    elsif Input.trigger?(Input::RIGHT) || Input.trigger?(Input::LEFT)
      # play sound
      $game_system.se_play($data_system.cursor_se)
      # item window is active
      @item_window.active = true
      # skill window is not active
      @skill_window.active = false
      # delete cursor
      @skill_window.cursor_rect.empty
    end
  end
  #----------------------------------------------------------------------------
  # update_item
  #  Updates input during the item selection.
  #----------------------------------------------------------------------------
  def update_item
    # set last active
    @last_active = false
    # if B is pressed
    if Input.trigger?(Input::B)
      # play cancel cound
      $game_system.se_play($data_system.cancel_se)
      # set active
      @active = true
      # item window is not active
      @item_window.active = false
      # delete cursor
      @item_window.cursor_rect.empty
    # if C is pressed
    elsif Input.trigger?(Input::C)
      # play sound
      $game_system.se_play($data_system.decision_se)
      # if last position
      if @item_window.index == @item_window.item_max - 1
        # remove hotkey assigmnent from item
        $game_system.controls.items[(@index+1)%10] = 0
        # remove hotkey assigmnent from skill
        $game_system.controls.skills[(@index+1)%10] = 0
      else
        # set item to hotkey
        $game_system.controls.items[(@index+1)%10] = @item_window.item.id
        # remove hotkey assigmnent from skill
        $game_system.controls.skills[(@index+1)%10] = 0
      end
      # if hotkey display exists
      if @hotkeys != nil
        # draw hotkey display
        @hotkeys.draw
      # if HUD_ENABLED is turned on and HUD is active
      elsif BlizzABS::Config::HUD_ENABLED && $game_system.hud
        # draw hotkey display within the HUD
        @hud.assignment.draw
      end
      # set active
      @active = true
      # item window is not active
      @item_window.active = false
      # delete cursor
      @item_window.cursor_rect.empty
    # if RIGHT or LEFT is pressed
    elsif Input.trigger?(Input::RIGHT) || Input.trigger?(Input::LEFT)
      # play sound
      $game_system.se_play($data_system.cursor_se)
      # skill window is active
      @skill_window.active = true
      # item window is not active
      @item_window.active = false
      # delete cursor
      @item_window.cursor_rect.empty
    end
  end
  
end

#==============================================================================
# Scene_AI_Setup
#------------------------------------------------------------------------------
#  This class doesn't do anything yet. It is planned that it will serve for
#  actor AI setup.
#==============================================================================

class Scene_AI_Setup
  
  #----------------------------------------------------------------------------
  # Initialization
  #  tone - screen background tone
  #----------------------------------------------------------------------------
  def initialize(tone)
    # store current screen tint
    @tone = tone
  end
  #----------------------------------------------------------------------------
  # main
  #  The main processing method.
  #----------------------------------------------------------------------------
  def main
    # create viewport
    @view = Viewport.new(0, 0, 640, 480)
    # set screen tint
    @view.tone = @tone
    # create map scene
    $scene = Scene_Map.new
    # delete viewport
    @view.dispose
  end
  #----------------------------------------------------------------------------
  # update
  #  The update processing method.
  #----------------------------------------------------------------------------
  def update
  end
  
end
