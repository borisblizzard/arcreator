#==============================================================================
# CP module Input
#==============================================================================

module Input
  
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
  LShift, RShift, Collon, Equal, Comma, Underscore, Dot, Backslash, Lb, Rb,
  Quote = 160, 161, 186, 187, 188, 189, 190, 191, 219, 221, 222
  
  State = Win32API.new('user32', 'GetKeyState', ['i'], 'i')
  Key = Win32API.new('user32', 'GetAsyncKeyState', ['i'], 'i')
  
  All_keys = 0..255
  @repeating, @pressed = [], []
  256.times{@repeating.push(-1)}
  
  def Input.get_current_state(key)
    return State.call(key).between?(0, 1)
  end
  
  def Input.test_key(key)
    Key.call(key) & 0x01 == 1
  end
  
  def Input.update
    @_keys = (@_keys == nil ? [] : @_keys) | (@keys == nil ? [] : @keys.clone)
    @keys = []
    All_keys.each {|key|
        @keys.push(key) if Input.test_key(key) && !@_keys.include?(key)
        if Input.get_current_state(key)
          @_keys.delete(key)
          @repeating[key] = 0
          @pressed.delete(key)
        else
          @pressed.push(key) unless @pressed.include?(key)
          if @repeating[key] > 0
            @repeating[key] < 17 ? @repeating[key] += 1 : @repeating[key] = 15
          else
            @repeating[key] = 1
          end
        end}
    if !$scene.is_a?(Scene_Controls)
      CP.screen if Input.trigger?($controls.snap)
    end
  end
  
  def Input.dir4
    @pressed.reverse.each {|i|
        case i
        when $controls.up then return 8
        when $controls.left then return 4
        when $controls.down then return 2
        when $controls.right then return 6
        end}
    return 0
  end
  
  def Input.trigger?(key)
    return (@keys.include?(key) && !@_keys.include?(key))
  end
  
  def Input.press?(key)
    return @pressed.include?(key)
  end     
  
  def Input.repeat?(key)
    return (@repeating[key] == 1 || @repeating[key] == 16)
  end
  
  def Input.get(i)
    return @keys[i]
  end
  
  def Input.Anykey
    return (@keys.size > 0)
  end
  
end
