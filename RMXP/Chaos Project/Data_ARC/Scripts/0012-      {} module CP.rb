$version = 1.220
$release = 'Full Game'

INIT_PASSABLE = false
GENERATE_DAMAGE = false
#GENERATE_DAMAGE = true
#INIT_PASSABLE = false
#INIT_PASSABLE = true

#==============================================================================
# module CP
#==============================================================================

module CP
  
  MAX_BGMS = 11
  
  # used in encryption
  EXTENSIONS = {}
  EXTENSIONS['rxdata'] = 'cpd'
  EXTENSIONS['cpx'] = 'cpf'
  EXTENSIONS['png'] = 'cpg'
  EXTENSIONS['jpg'] = 'cpg'
  
  class Controls
    
    attr_accessor :up
    attr_accessor :left
    attr_accessor :down
    attr_accessor :right
    attr_accessor :confirm
    attr_accessor :cancel
    attr_accessor :menu
    attr_accessor :leximus
    attr_accessor :prev
    attr_accessor :nex
    attr_accessor :snap
    attr_accessor :ctrl
    attr_accessor :pass
    attr_accessor :debug
    
    def initialize
      set_new_controls([
          Input::Let['W'],
          Input::Let['A'],
          Input::Let['S'],
          Input::Let['D'],
          Input::Let['K'],
          Input::Let['J'],
          Input::Let['I'],
          Input::Let['L'],
          Input::Let['Q'],
          Input::Let['E'],
          Input::Let['Z']])
      @ctrl    = Input::Ctrl
      @pass    = Input::Fkeys[5]
      @debug   = Input::Fkeys[9]
    end
    
    def set_new_controls(new_controls)
      @up, @left, @down, @right, @confirm, @cancel, @menu, @leximus, @prev, @nex,
          @snap = new_controls
    end
    
    def key_convert
      if @turn != nil
        @leximus = @turn
        @turn = nil
      end
    end
  
  end
  
  def self.move_pandemonium(direction)
    key = [$game_variables[148], $game_variables[149], direction]
    return false if !CP::Cache::PandemoniumCursor.has_key?(key)
    cursor = ($game_map.events.values.find_all {|e| e.name == 'Cursor'})[0]
    CP::Cache::PandemoniumCursor[key].each {|direction|
        cursor.move_in_direction(direction)}
    if cursor.x == 10
      cursor.instance_variable_set('@character_name', 'giant_cursor')
    else
      cursor.instance_variable_set('@character_name', 'large_cursor')
    end
    return true
  end
  
  def self.switch_pandemonium(reverse = false)
    key = [$game_variables[148], $game_variables[149]]
    spheres = []
    CP::Cache::PandemoniumSpheres[key].each {|c|
        spheres.push(($game_map.pass(c[0], c[1]).find_all {|e|
            e.name.clone.gsub!('SPHERE') {''} != nil})[0])}
    if reverse
      spheres.push(spheres.shift)
    else
      spheres.unshift(spheres.pop)
    end
    CP::Cache::PandemoniumSpheres[key].each_index {|i|
        x, y = CP::Cache::PandemoniumSpheres[key][i]
        old_x, old_y = spheres[i].x, spheres[i].y
        spheres[i].instance_variable_set('@x', x)
        spheres[i].instance_variable_set('@y', y)
        $game_map.update_event(old_x, old_y, spheres[i])}
    return true
  end
  
  def self.check_pandemonium
    map_events = $game_map.events.values
    spheres = (map_events.find_all {|e| e.name.clone.gsub!('SPHERE') {}})
    arrows = (map_events.find_all {|e| e.name.clone.gsub!('Arrow') {}})
    l_arrows = (arrows.find_all {|e| e.name.clone.gsub!('Arrow L') {}})
    u_arrows = (arrows.find_all {|e| e.name.clone.gsub!('Arrow U') {}})
    spheres.each {|sphere|
        l_arrow = l_arrows.find_all {|arrow| arrow.y == sphere.y}[0]
        u_arrow = u_arrows.find_all {|arrow| arrow.x == sphere.x}[0]
        if (l_arrow.character_hue - u_arrow.character_hue).abs == 240
          return false if sphere.character_hue != 300
        elsif sphere.character_hue != (l_arrow.character_hue + u_arrow.character_hue) / 2
          return false
        end}
    return true
  end
  
  def self.setup_pandemonium
    map_events = $game_map.events.values
    arrows = (map_events.find_all {|e| e.name.clone.gsub!('Arrow') {}})
    l_arrows = (arrows.find_all {|e| e.name.clone.gsub!('Arrow L') {}})
    u_arrows = (arrows.find_all {|e| e.name.clone.gsub!('Arrow U') {}})
    l_arrows = DREAM.randomize_ary(l_arrows)
    u_arrows = DREAM.randomize_ary(u_arrows)
    red_arrows, green_arrows, blue_arrows = [], [], []
    [red_arrows, green_arrows, blue_arrows][rand(3)].push(l_arrows[6])
    red_arrows |= [l_arrows[0], l_arrows[1]]
    green_arrows |= [l_arrows[2], l_arrows[3]]
    blue_arrows |= [l_arrows[4], l_arrows[5]]
    red_arrows |= [u_arrows[0], u_arrows[1]]
    green_arrows |= [u_arrows[2], u_arrows[3]]
    blue_arrows |= [u_arrows[4], u_arrows[5]]
    green_arrows.each {|arrow| arrow.character_hue = 120}
    blue_arrows.each {|arrow| arrow.character_hue = 240}
    spheres = (map_events.find_all {|e| e.name.clone.gsub!('SPHERE') {}})
    coos = []
    spheres.each {|sphere|
        l_arrow = l_arrows.find_all {|arrow| arrow.y == sphere.y}[0]
        u_arrow = u_arrows.find_all {|arrow| arrow.x == sphere.x}[0]
        if (l_arrow.character_hue - u_arrow.character_hue).abs == 240
          sphere.character_hue = 300
        else
          sphere.character_hue =
              (l_arrow.character_hue + u_arrow.character_hue) / 2
        end
        coos.push([sphere.x, sphere.y])}
    $game_map.need_refresh = true
    self.scramble_pandemonium(spheres, coos)
    return true
  end
  
  def self.scramble_pandemonium(spheres, coos)
    coos = DREAM.randomize_ary(coos)
    spheres.each_index {|i| spheres[i].moveto(coos[i][0], coos[i][1])}
    return true
  end
  
  def self.check_hyperion_2
    squares, events = [], []
    Cache::Hyperion2VEvents.each {|y| events |= $game_map.pass(5, y)}
    Cache::Hyperion2Colors.each {|color|
        event = (events.find_all {|e| e.name == color + ' Arrow'})[0]
        squares.push([event.y, color])}
    squares.each {|set| Cache::Hyperion2HEvents.each {|x|
        events = $game_map.pass(x, set[0])
        events = events.find_all {|e| e.name == set[1] + ' Square'}
        return false if events.size != 1}}
    return true
  end
  
  def self.switch_hyperion_2(reverse = false)
    map_events = $game_map.events.values
    cursor = (map_events.find_all {|e| e.name == 'Cursor'})[0]
    e, cx, cy = [], cursor.x, cursor.y
    if $game_switches[402]
      Cache::Hyperion2HEvents.each {|x|
          e |= $game_map.pass(x, cy).find_all {|e|
              e.name.clone.gsub!('Square') {''} != nil}}
    else
      Cache::Hyperion2VEvents.each {|y|
          e |= $game_map.pass(cx, y).find_all {|e|
              e.name.clone.gsub!('Square') {''} != nil}}
    end
    e.reverse! if reverse
    x, y = e[0].x, e[0].y
    e.each_index {|i| e[i].moveto(e[(i+1)%e.size].x, e[(i+1)%e.size].y)}
    e[e.size-1].moveto(x, y)
    return true
  end
  
  def self.setup_hyperion_2
    xc, yc = Cache::Hyperion2HEvents, Cache::Hyperion2VEvents
    xs, ys, events = [], [], []
    yc.each {|y| events |= $game_map.pass(5, y)}
    coos = yc.clone
    events.each_index {|i|
        j = coos.size == 1 ? 0 : rand(coos.size)
        y = coos[j]
        coos.delete_at(j)
        events[i].moveto(5, y)}
    4.times {
        xs.push(xc.clone)
        ys.push(yc.clone)}
    4.times {
        xs.each {|xary| xary.delete_at(rand(xary.size)) if rand(3) == 0}
        ys.each {|yary| yary.delete_at(rand(yary.size)) if rand(3) == 0}}
    self.scramble_hyperion_2(xs, ys)
    return true
  end
  
  def self.scramble_hyperion_2(xs, ys)
    map_events = $game_map.events.values
    cursor = (map_events.find_all {|e| e.name == 'Cursor'})[0]
    while xs.size > 0 || ys.size > 0
      if xs[0].size > 0 || ys[0].size > 0
        self.prepare_hyperion(xs[0], ys[0], cursor)
        (rand(4)+1).times {self.switch_hyperion_2((rand(2) == 0))}
      else
        xs.delete_at(0)
        ys.delete_at(0)
      end
    end
    return true
  end
  
  def self.check_hyperion_1
    x1, x2 = Cache::Hyperion1HEvents
    y1, y2 = Cache::Hyperion1VEvents
    reds, greens, blues, yellows = [x1, y1], [x2, y1], [x1, y2], [x2, y2]
    [[reds, 2], [greens, 6], [blues, 8], [yellows, 4]].each {|set|
        coos, direction = set
        coos[0].each {|x| coos[1].each {|y|
            events = $game_map.pass(x, y).find_all {|e| e.name == 'Sphere'}
            return false if events.any? {|e| e.direction != direction}}}}
    return true
  end
  
  def self.switch_hyperion_1
    map_events = $game_map.events.values
    cursor = (map_events.find_all {|e| e.name == 'Cursor'})[0]
    e1, e2, x, y = [], [], cursor.x, cursor.y
    if $game_switches[402]
      a, b = Cache::Hyperion1HEvents
      a.each_index {|i|
          e1 |= $game_map.pass(a[i], y).find_all {|e| e.name == 'Sphere'}
          e2 |= $game_map.pass(b[i], y).find_all {|e| e.name == 'Sphere'}}
    else
      a, b = Cache::Hyperion1VEvents
      a.each_index {|i|
          e1 |= $game_map.pass(x, a[i]).find_all {|e| e.name == 'Sphere'}
          e2 |= $game_map.pass(x, b[i]).find_all {|e| e.name == 'Sphere'}}
    end
    e1.each_index {|i|
        x, y = e1[i].x, e1[i].y
        e1[i].moveto(e2[i].x, e2[i].y)
        e2[i].moveto(x, y)}
    return true
  end
  
  def self.setup_hyperion_1
    x1, x2 = Cache::Hyperion1HEvents
    y1, y2 = Cache::Hyperion1VEvents
    xs, ys = [], []
    4.times {
        xs.push(x1 + x2)
        ys.push(y1 + y2)}
    3.times {
        xs.each {|xary| xary.delete_at(rand(xary.size)) if rand(3) == 0}
        ys.each {|yary| yary.delete_at(rand(yary.size)) if rand(3) == 0}}
    self.scramble_hyperion_1(xs, ys)
    return true
  end
  
  def self.scramble_hyperion_1(xs, ys)
    map_events = $game_map.events.values
    cursor = (map_events.find_all {|e| e.name == 'Cursor'})[0]
    while xs.size > 0 || ys.size > 0
      if xs[0].size > 0 || ys[0].size > 0
        self.prepare_hyperion(xs[0], ys[0], cursor)
        self.switch_hyperion_1
      else
        xs.delete_at(0)
        ys.delete_at(0)
      end
    end
    return true
  end
  
  def self.prepare_hyperion(xs, ys, cursor)
    if xs.size > 0 && ys.size > 0
      if rand(2) == 0
        i = xs.size == 1 ? 0 : rand(xs.size)
        x = xs[i]
        xs.delete_at(i)
        cursor.moveto(x, cursor.y)
        $game_switches[402] = false
      else
        i = ys.size == 1 ? 0 : rand(ys.size)
        y = ys[i]
        ys.delete_at(i)
        cursor.moveto(cursor.x, y)
        $game_switches[402] = true
      end
    elsif xs.size > 0
      i = xs.size == 1 ? 0 : rand(xs.size)
      x = xs[i]
      xs.delete_at(i)
      cursor.moveto(x, cursor.y)
      $game_switches[402] = false
    else
      i = ys.size == 1 ? 0 : rand(ys.size)
      y = ys[i]
      ys.delete_at(i)
      cursor.moveto(cursor.x, y)
      $game_switches[402] = true
    end
    return true
  end
  
  def self.thirsty_dunes_setup
    $game_system.mine_table = Table.new(17, 11)
    c = []
    c[0] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    c[1] = [0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
    c[2] = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0]
    c[3] = [0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0]
    c[4] = [0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0]
    c[5] = [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
    c[6] = [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0]
    c[7] = [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0]
    c[8] = [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1]
    c[9] = [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0]
   c[10] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    (0...c.size).each {|y| (0...c[y].size).each {|x|
        $game_system.mine_table[x, y] = c[y][x]}}
    return true
  end
  
  def self.thirsty_dunes_check_mines(dir)
    x, y, count = $game_player.x - 12, $game_player.y - 6, 0
    case dir
    when 2
      count += 1 if $game_system.mine_table[x, y+1] == 0
      count += 1 if $game_system.mine_table[x, y+2] == 0
      count += 1 if $game_system.mine_table[x, y+3] == 0
    when 4
      count += 1 if $game_system.mine_table[x-1, y] == 0
      count += 1 if $game_system.mine_table[x-2, y] == 0
      count += 1 if $game_system.mine_table[x-3, y] == 0
    when 6
      count += 1 if $game_system.mine_table[x+1, y] == 0
      count += 1 if $game_system.mine_table[x+2, y] == 0
      count += 1 if $game_system.mine_table[x+3, y] == 0
    when 8
      count += 1 if $game_system.mine_table[x, y-1] == 0
      count += 1 if $game_system.mine_table[x, y-2] == 0
      count += 1 if $game_system.mine_table[x, y-3] == 0
    end
    return count
  end
  
  def self.thirsty_dunes_detonate_mines
    x, y = $game_player.x - 12, $game_player.y - 6
    return ($game_system.mine_table[x, y] == 0)
  end
  
  def self.thirsty_dunes_change_map
    (0...$game_system.mine_table.ysize).each {|y|
        (0...$game_system.mine_table.xsize).each {|x|
            if $game_system.mine_table[x, y] == 0
              $game_map.data[x+12, y+6, 1] = 48 * 7
            end}}
    return true
  end
  
  def self.thirsty_dunes_change_map_back
    (0...$game_system.mine_table.ysize).each {|y|
        (0...$game_system.mine_table.xsize).each {|x|
            if $game_system.mine_table[x, y] == 0
              $game_map.data[x+12, y+6, 1] = 384 + 17 * 8 + 3
            end}}
    return true
  end
  
  def self.genesis_text_setup
    r = (($game_variables[126] & 0x4) == 0 ? 'Deactivate' : 'Activate')
    r += ' red component'
    g = (($game_variables[126] & 0x2) == 0 ? 'Deactivate' : 'Activate')
    g += ' green component'
    b = (($game_variables[126] & 0x1) == 0 ? 'Deactivate' : 'Activate')
    b += ' blue component'
    $game_variables[118], $game_variables[119], $game_variables[123] = r, g, b
    return true
  end
  
  def self.genesis_setup
    coos1 = []
    (2..18).each {|x| (4..12).each {|y| coos1.push([x, y])}}
    coos2 = coos1.clone
    coos3 = coos1.clone
    coos4 = coos1.clone
    $game_variables[127], $game_variables[128] = coos1.delete(coos1[rand(coos1.size)])
    $game_variables[129], $game_variables[130] = coos1.delete(coos1[rand(coos1.size)])
    $game_variables[131], $game_variables[132] = coos2.delete(coos2[rand(coos2.size)])
    $game_variables[133], $game_variables[134] = coos2.delete(coos2[rand(coos2.size)])
    $game_variables[135], $game_variables[136] = coos3.delete(coos3[rand(coos3.size)])
    $game_variables[137], $game_variables[138] = coos3.delete(coos3[rand(coos3.size)])
    $game_variables[139], $game_variables[140] = coos4.delete(coos4[rand(coos4.size)])
    $game_variables[141], $game_variables[142] = coos4.delete(coos4[rand(coos4.size)])    
    nums = (1..6).to_a
    $game_variables[143] = nums.delete(nums[rand(nums.size)])
    $game_variables[144] = nums.delete(nums[rand(nums.size)])
    $game_variables[145] = nums.delete(nums[rand(nums.size)])
    $game_variables[146] = nums.delete(nums[rand(nums.size)])
    return true
  end
  
  def self.setup_crios_teleport
    coos = [$game_player.x, $game_player.y]
    if Cache::CriosTeleport[coos] != nil
      if Cache::CriosTeleport[coos][0].is_a?(Numeric)
        coos = Cache::CriosTeleport[coos]
      else
        i = case $game_variables[124]
        when 0, 4, 5 then 0
        when 1, 3 then 1
        when 2 then 2
        end
        i = Cache::CriosTeleport[coos].size - 1 if i >= Cache::CriosTeleport[coos].size
        coos = Cache::CriosTeleport[coos][i]
      end
    else
      Cache::CriosTeleport.each_key {|key|
          if Cache::CriosTeleport[key][0].is_a?(Numeric) &&
              Cache::CriosTeleport[key] == coos ||
              Cache::CriosTeleport[key][0] == coos
            coos = key
            break
          end}
    end
    $game_variables[118], $game_variables[119] = coos
    return true
  end
  
  def self.deactivate_crios_beacon(event)
    if event.y == 35 && Cache::CriosXCoos.include?(event.x)
      self.crios_beacon(event, -1)
    end
    return true
  end
  
  def self.activate_crios_beacon(event)
    if event.y == 35 && Cache::CriosXCoos.include?(event.x)
      self.crios_beacon(event, 1)
    end
    return true
  end
  
  def self.crios_beacon(event, num)
    x, y = event.x, event.y
    event.direction = (num > 0 ? 8 : 6)
    events = $game_map.pass(x, y).find_all {|e| e.is_a?(Game_Event) && e != event}
    if events.size > 0
      events[0].direction = (num > 0 ? 8 : 6)
      $game_variables[124] += num
    end
    return true
  end
  
  def self.init_andras_beacons(reinit = false)
    @beacons, @active = Table.new(6, 6), Table.new(6, 6)
    return true unless reinit
    (0...6).each {|x| (0...6).each {|y|
        $game_map.pass(x*2+15, y+36)[0].direction = 6}}
    return true
  end
  
  def self.init_andras_full
    self.init_andras_beacons
    @andras_positions, all, correct = {}, [], []
    (0...6).each {|x| (0...6).each {|y| all.push([x, y])}}
    4.times {correct.push(all.delete(all[rand(all.size)]))
    all.each {|key|
        @andras_positions[key], n, select = [], 3 + rand(14), all.clone
        while n > 0
          @andras_positions[key].push(select.delete(select[rand(select.size)]))
          n -= 1
        end}}
    (0...3).each {|i|
        key = correct[i]
        @andras_positions[key], n = [], rand(all.size/2+(i-2)*2) + 1
        while n > 0
          @andras_positions[key].push(all.delete(all[rand(all.size)]))
          n -= 1
        end}
    @andras_positions[correct[3]] = all
    return true
  end
  
  def self.deactivate_andras_beacon(event)
    if ((event.x-15)/2).between?(0, 5) && event.x % 2 == 1 && event.y.between?(36, 41)
      self.andras_beacon(event, -1)
      ([$game_map.events[6], $game_map.events[7], $game_map.events[8],
          $game_map.events[9]] - [event]).each {|ev| activate_andras_beacon(ev)}
    end
    return true
  end
  
  def self.activate_andras_beacon(event)
    if ((event.x-15)/2).between?(0, 5) && event.x % 2 == 1 && event.y.between?(36, 41)
      self.andras_beacon(event, 1)
      if (0...6).all? {|x| (0...6).all? {|y| @beacons[x, y] == 1}}
        $game_switches[307] = $game_map.need_refresh = true
      end
    end
    return true
  end
  
  def self.andras_beacon(event, num)
    x, y = (event.x-15)/2, event.y-36
    return if num > 0 && @beacons[x, y] > 0 || num < 0 && @active[x, y] == 0
    if num > 0
      @active[x, y], event.direction = 1, 8
    else
      @active[x, y], event.direction = 0, 6
    end
    positions = [[x, y]] + @andras_positions[[x, y]]
    positions.each {|c|
        sx, sy = c
        x, y = sx*2+15, sy+36
        events = $game_map.pass(x, y).find_all {|e|
            e.is_a?(Game_Event) && !e.id.between?(6, 9)}
        @beacons[sx, sy] += num
        events[0].direction = (@beacons[sx, sy] > 0 ? 8 : 6)}
    return true
  end
  
  def self.sewer_execute
    $game_switches[4] = false
    x, y = $game_map.events[1].x, $game_map.events[1].y - 1
    return if $game_map.pass(x, y).size == 0
    coordinates = [[x, y+3, 2], [x-3, y, 4], [x+3, y, 6], [x, y-3, 8]]
    coordinates = coordinates.find_all {|coos|
        coos[0].between?(9, 20) && coos[1].between?(10, 21) &&
        (coos[0] != 10 || coos[1] != 20)}
    coos = coordinates.find_all {|c| $game_map.pass(c[0], c[1]).size == 0}
    if coos.size > 0
      c = coos[0]
      ids = Cache::SewerDirs[c[2]]
      routes = [$game_map.events[ids[0]].event.pages[0].move_route.clone,
          $game_map.events[ids[1]].event.pages[0].move_route.clone,
          $game_map.events[ids[2]].event.pages[0].move_route.clone]
      move_events = $game_map.pass(x, y) + $game_map.pass(x, y+1) +
          $game_map.pass(x-1, y) + $game_map.pass(x+1, y) +
          $game_map.pass(x, y-1) - [$game_map.events[1]]
      x, y = c[0, 2]
      other_events = $game_map.pass(x, y+1) + $game_map.pass(x-1, y) +
          $game_map.pass(x+1, y) + $game_map.pass(x, y-1)
      move_events.each {|event|
          if !event.through
            event.force_move_route(routes[0])
          else
            event.force_move_route(routes[1])
          end}
      other_events.each {|event| event.force_move_route(routes[2])}
      $game_switches[4] = true
    end
    return true
  end
  
  def self.adel_coordinates
    if $game_variables[9] == 17
      return true if $game_variables[10] == 24
      return true if $game_variables[10] == 25
      return true if $game_variables[10] == 26
    end
    if $game_variables[9] == 7
      return true if $game_variables[10] == 22
      return true if $game_variables[10] == 23
      return true if $game_variables[10] == 24
    end
    if $game_variables[9] == 11
      return true if $game_variables[10] == 16
      return true if $game_variables[10] == 17
      return true if $game_variables[10] == 18
    end
    if $game_variables[9] == 6
      return true if $game_variables[10] == 8
      return true if $game_variables[10] == 9
      return true if $game_variables[10] == 10
      return true if $game_variables[10] == 11
    end
    if $game_variables[9] == 18
      return true if $game_variables[10] == 8
      return true if $game_variables[10] == 9
      return true if $game_variables[10] == 10
    end
    if $game_variables[9] == 27
      return true if $game_variables[10] == 16
      return true if $game_variables[10] == 17
      return true if $game_variables[10] == 18
    end
    if $game_variables[9] == 13
      return true if $game_variables[10] == 20
      return true if $game_variables[10] == 21
    end
    if $game_variables[9] == 14
      return true if $game_variables[10] == 20
      return true if $game_variables[10] == 21
      return true if $game_variables[10] == 13
      return true if $game_variables[10] == 14
    end
    if $game_variables[9] == 15
      return true if $game_variables[10] == 13
      return true if $game_variables[10] == 14
    end
    return false
  end
  
  def self.controls_name(trigger)
    return case trigger
    when 160 then 'L. Shift'
    when 161 then 'R. Shift'
    when 13 then 'Enter'
    when 32 then 'Space'
    when 27 then 'Esc'
    when 40 then 'Down Arrow'
    when 37 then 'Left Arrow'
    when 39 then 'Right Arrow'
    when 38 then 'Up Arrow'
    else
      trigger.chr
    end
  end
  
  def self.info?(index)
    return $game_system.info_pages[index]
  end
  
  def self.any_info?
    return ($game_system.info_pages.include?(true) && !$game_party.no_info?)
  end
  
  def self.unlock_info(index)
    $game_system.info_pages[index] = true
    return true
  end
  
  def self.get_book
    if $game_variables[109] == $game_variables[151]
      coos = [[23, 10], [24, 10]]
    else
      ys, coos = [4, 5, 7, 8, 10, 11, 13, 14, 16, 17], []
      ((2..7).to_a + (21..26).to_a).each {|i| ys.each {|j| coos.push([i, j])}}
      ((9..12).to_a + (16..19).to_a).each {|i| [5, 7, 8].each {|j| coos.push([i, j])}}
      coos -= [[21, 14], [22, 14], [23, 10], [24, 10]]
    end
    $game_variables[12], $game_variables[19] = coos[rand(coos.size)]
    return true
  end
  
  def self.exp_dist_money
    valid = $game_party.actors.find_all {|actor|
        actor.level < $data_actors[actor.id].final_level}
    cash = 0
    valid.each {|i| valid.each {|j| cash += (i.exp - j.exp).abs}}
    $game_variables[5] = cash / 2
    return true
  end
  
  def self.exp_dist_exec
    actors = $game_party.actors.find_all {|actor|
        actor.level < $data_actors[actor.id].final_level}
    exp = 0
    actors.each {|actor| exp += actor.exp}
    full = []
    loopme = true
    while loopme
      loopme = false
      nexp = exp / actors.size
      actors.each_index {|i|
          if nexp > actors[i].maxexp
            full.push(actors[i])
            exp -= actors[i].maxexp
            actors[i] = nil
            loopme = true
            break
          end}
      actors.compact!
    end
    nexp = exp / actors.size
    full.each {|actor| actor.exp = actor.maxexp}
    actors.each {|actor| actor.exp = nexp}
    return true
  end
  
  def self.activate_trace(id)
    @trace_route = [$game_map.events[id]]
    return true
  end
  
  def self.trace
    return @trace_route
  end
  
  def self.trace_back
    event = @trace_route.shift
    last = @trace_route[0].clone
    @trace_route.reverse!
    last.code = 0
    @trace_route.push(last)
    $game_system.map_interpreter.setup_trace
    @trace_route = nil
    return true
  end
  
  def self.char(sym)
    return ((sym != 0 and sym != nil) ? sym.chr : '')
  end
  
  def self.name_2(name)
    return case name
    when 'Falchion'           then 'Falchions'
    when 'Edge'               then 'Edges'
    when 'Adiemus Blade'      then 'Adiemus Blades'
    when 'Sonic Blade'        then 'Sonic Blades'
    when 'Azoth'              then 'Azoths'
    when 'Dragon Sword'       then 'Dragon Swords'
    else
      name
    end
  end
  
  def self.meta_text(meta)
    text = case meta
    when 1 then 'Excellent'
    when 2 then 'Good'
    when 3 then 'O.K.'
    when 4 then 'Bad'
    when 5 then 'Critical'
    when 6 then 'Ready'
    when 7 then 'Confident'
    when 8 then 'Balanced'
    when 9 then 'Beaten'
    when 10 then 'Raging'
    when 11 then 'Super'
    when 12 then 'Strong'
    when 13 then 'Average'
    when 14 then 'Furious'
    when 15 then 'Berserking'
    when 16 then 'Godlike'
    when 17 then 'Disrupting'
    when 18 then 'Avenging'
    when 19 then 'Devastating'
    when 20 then 'Destroying'
    end
    return text
  end
  
  # Trance Database
  def self.trance_database(id)
    skill_ids = []
    case id
    when 45 # Dragmatek
      skill_ids.push(297)
      skill_ids.push(310)
      skill_ids.push(342)
      skill_ids.push(343)
      skill_ids.push(344)
      skill_ids.push(424)
      skill_ids.push(445)
    when 46 # Blaze
      skill_ids.push(9)
      skill_ids.push(102)
      skill_ids.push(193)
      skill_ids.push(205)
      skill_ids.push(319)
      skill_ids.push(320)
    when 47 # Thanatos
      skill_ids.push(161)
      skill_ids.push(178)
      skill_ids.push(389)
      skill_ids.push(434)
      skill_ids.push(443)
      skill_ids.push(449)
    when 48 # Devas
      skill_ids.push(3)
      skill_ids.push(5)
      skill_ids.push(112)
      skill_ids.push(192)
      skill_ids.push(194)
      skill_ids.push(195)
      skill_ids.push(237)
    when 49 # Cluster
      skill_ids.push(54)
      skill_ids.push(55)
      skill_ids.push(314)
    when 52 # Nexus
      skill_ids.push(356)
      skill_ids.push(376)
      skill_ids.push(377)
      skill_ids.push(378)
      skill_ids.push(379)
      skill_ids.push(380)
      skill_ids.push(381)
      skill_ids.push(445)
    end
    return skill_ids
  end
  
  # Gun Database
  def self.gun_database(id)
    skill_ids = []
    case id
    when 45
      skill_ids.push(286)
    when 58
      skill_ids.push(286)
      skill_ids.push(289)
    when 59
      skill_ids.push(286)
      skill_ids.push(289)
      skill_ids.push(315)
    when 142
      skill_ids.push(286)
      skill_ids.push(289)
      skill_ids.push(295)
    when 148
      skill_ids.push(286)
      skill_ids.push(289)
      skill_ids.push(295)
      skill_ids.push(358)
    when 149
      skill_ids.push(286)
      skill_ids.push(289)
      skill_ids.push(295)
      skill_ids.push(359)
      skill_ids.push(360)
    when 176
      skill_ids.push(286)
      skill_ids.push(289)
      skill_ids.push(295)
      skill_ids.push(315)
      skill_ids.push(358)
      skill_ids.push(359)
      skill_ids.push(360)
      skill_ids.push(436)
    end
    return skill_ids
  end
  
  def self.ammo_req(id)
    case id
    when 286 then return 1
    when 289 then return 3
    when 295 then return 3 * ($game_troop.enemies.find_all {|e| e.exist?}).size
    when 315 then return 4
    when 358 then return 1
    when 359 then return 5 * ($game_troop.enemies.find_all {|e| e.exist?}).size
    when 360 then return 10
    when 436 then return 15
    end
    return 0
  end
  
  # SR Database
  def self.sr_weapons(id)
    case id
    when 2 then return 70
    when 3 then return 71
    when 5 then return 147
    when 6 then return 232
    when 7 then return 163
    when 8 then return 148
    when 9 then return 196
    when 10 then return 209
    when 11 then return 210
    when 14 then return 209
    when 15 then return 217
    when 16 then return 218
    when 17 then return 229
    when 18 then return 398
    when 19 then return 253
    when 20 then return 233
    when 21 then return 235
    when 22 then return 239
    when 23 then return 203
    when 24 then return 244
    when 25 then return 235
    when 27 then return 291
    when 28 then return 294
    when 29 then return 211
    when 30 then return 266
    when 31 then return 203
    when 32 then return 401
    when 33 then return 62
    when 34 then return 72
    when 35 then return 146
    when 36 then return 162
    when 38 then return 219
    when 39 then return 148
    when 40 then return 241
    when 41 then return 259
    when 42 then return 242
    when 43 then return 243
    when 44 then return 156
    when 45 then return 204
    when 46 then return 265
    when 47 then return 348
    when 48 then return 323
    when 49 then return 239
    when 50 then return 71
    when 51 then return 206
    when 52 then return 291
    when 53 then return 142
    when 55 then return 73
    when 57 then return 74
    when 58 then return 75
    when 59 then return 62
    when 60 then return 76
    when 61 then return 146
    when 62 then return 62
    when 65 then return 208
    when 67 then return 292
    when 69 then return 280
    when 70 then return 322
    when 71 then return 330
    when 72 then return 294
    when 73 then return 328
    when 74 then return 329
    when 75 then return 349
    when 76 then return 346
    when 77 then return 147
    when 78 then return 347
    when 79 then return 355
    when 80 then return 228
    when 81 then return 362
    when 82 then return 363
    when 83 then return 148
    when 84 then return 364
    when 86 then return 400
    when 87 then return 437
    when 91 then return 450
    end
    return 0
  end
  
  def self.sr_armors(id, user = nil, pos = nil)
    case id
    when 3 then return 122
    when 4 then return 78
    when 6 then return 63
    when 7 then return 64
    when 8 then return 66
    when 10 then return 31
    when 11 then return 31
    when 12 then return 150
    when 14 then return 67
    when 15 then return 74
    when 22 then return 31
    when 23 then return 66
    when 24 then return 31
    when 25 then return 32
    when 27 then return 31
    when 38 then return 79
    when 39 then return 267
    when 40 then return 166
    when 41 then return 351
    when 42 then return 212
    when 43 then return 181
    when 44 then return 78
    when 47 then return 78
    when 48 then return 130
    when 50 then return 430
    when 51 then return 398
    when 53 then return 366
    when 55 then return 365
    when 56 then return 228
    when 57 then return 204
    when 60 then return 122
    when 63 then return 136
    when 64 then return 134
    when 65 then return 135
    when 66 then return 137
    when 70 then return 68
    when 71 then return 77
    when 72 then return 77
    when 73 then return 80
    when 74 then return 152
    when 75 then return 155
    when 76 then return 120
    when 77 then return 127
    when 78 then return 77
    when 79 then return 199
    when 80 then return 128
    when 81 then return 78
    when 82 then return 166
    when 83 then return 168
    when 84 then return 174
    when 85 then return 80
    when 86 then return 174
    when 87 then return 170
    when 88 then return 175
    when 89 then return 431
    when 90 then return 432
    when 91 then return 173
    when 92 then return 179
    when 93 then return 167
    when 95 then return 229
    when 98 then return 207
    when 99 then return 208
    when 100 then return 131
    when 102 then return 211
    when 103 then return 137
    when 104 then return 181
    when 105 then return 214
    when 106 then return 167
    when 110 then return 255
    when 111 then return 267
    when 112 then return 321
    when 113 then return 133
    when 114 then return 228
    when 115 then return 240
    when 116 then return 245
    when 119 then return 246
    when 120 then return 255
    when 122
      return 256 if user == nil
      case ([user.armor4_id, user.armor5_id, user.armor6_id].find_all {|id|
          id == 122}).size
      when 1 then return 256
      when 2
        case pos
        when 4 then return 256
        when 5 then return (user.armor4_id == 122 ? 257 : 256)
        when 6 then return 257
        end
      when 3
        case pos
        when 4 then return 256
        when 5 then return 257
        when 6 then return 258
        end
      end
      return 256
    when 123 then return 268
    when 124 then return 274
    when 125 then return 270
    when 126 then return 79
    when 127 then return 229
    when 128 then return 80
    when 129 then return 293
    when 130 then return 323
    when 132 then return 275
    when 133 then return 312
    when 134 then return 199
    when 135 then return 324
    when 136 then return 130
    when 137 then return 325
    when 138 then return 351
    when 139 then return 170
    when 140 then return 78
    when 141 then return 150
    when 143 then return 128
    when 144 then return 350
    when 145 then return 130
    when 146 then return 79
    when 147 then return 133
    when 151 then return 168
    when 153 then return 368
    when 154 then return 372
    when 155 then return 351
    when 156 then return 129
    when 157 then return 367
    when 158 then return 370
    when 159 then return 349
    when 160 then return 375
    when 162 then return 371
    when 163 then return 413
    when 164 then return 403
    when 165 then return 131
    when 166 then return 405
    when 167 then return 79
    when 168 then return 399
    when 169 then return 402
    when 170 then return 351
    when 171 then return 363
    when 172 then return 81
    when 173 then return 402
    when 177 then return 133
    when 178 then return 220
    when 179 then return 174
    when 180 then return 345
    when 181 then return 149
    end
    return 0
  end
  
  def self.event_comment(event, comment)
    return (event.list.is_a?(Array) &&
        event.list.any? {|c| c.code == 108 && c.parameters[0] == comment})
  end
    
  def self.first_comment(event, comment)
    return (event.list.is_a?(Array) && event.list[0].code == 108 &&
        event.list[0].parameters[0] == comment)
  end
  
  def self.alter_encouter_list(list)
    other = ($game_switches[397] ? CP::Cache::EncList1 : CP::Cache::EncList2)
    return (list - other)
  end
  
  def self.riddle1_generate
    $game_variables[5] = 0
    $game_variables[9] = 4 + 2 * rand(4)
    $game_variables[10] = 3 * $game_variables[9]
    $game_variables[12] = 2 * $game_variables[9]
    $game_variables[19] = rand(5)
    return true
  end
  
  def self.riddle1_solution_check
    case $game_variables[19]
    when 0 then return ($game_variables[5] == $game_variables[9])
    when 1 then return ($game_variables[5] == $game_variables[9]/2)
    when 2 then return ($game_variables[5] == $game_variables[9])
    when 3 then return ($game_variables[5] == $game_variables[10])
    when 4 then return ($game_variables[5] == $game_variables[12])
    end
    return false
  end
  
  def self.riddle2_setup
    $game_variables[9], $game_variables[10] = rand(25), 50 + rand(151)
    $game_variables[12], $game_variables[19] = rand(25), 50 + rand(151)
    $game_variables[5] = 200 + rand(801)
    return true
  end
  
  def self.riddle2_generate
    str = 'Train A leaves Termina at with a speed of kmh Train B leaves ' +
        'Astralis at with a speed of kmh If the two cities are away from ' +
        'each other exactly km'
    str.upcase!
    letters = []
    str.each_byte {|c| letters.push(c.chr)}
    letters = letters | letters
    letters.delete(' ')
    letter, count = letters[rand(letters.size)], 0
    str.each_byte {|c| count += 1 if c == letter}
    $game_variables[5] = 0
    $game_variables[9] = letter
    $game_variables[10] = count
    return true
  end
  
  def self.riddle3_generate
    border = 11 + rand(15)
    $game_variables[5] = 0
    $game_variables[9] = border ** 2
    $game_variables[10] = (border + 2) ** 2
    $game_variables[12] = (border + 4) ** 2
    $game_variables[19] = (border + 6) ** 2
    return true
  end
  
  def self.fixname(name)
    if name == 'Potato'
      name += 'es'
    elsif name != 'Fish' && name != 'Chicken' && name != 'Cheese' &&
        name != 'Bread'
      if name[name.size-1, 1] == 's'
        name += '\''
      elsif name[name.size-1, 1] == 'y'
        name = name1[0, name.size-1] + 'ies'
      elsif name[name.size-1, 1] == 'f'
        name = name[0, name.size-1] + 'ves'
      else
        name += 's'
      end
    end
    return name
  end
  
  def self.data_load
    if File.exist?(CP.saves + 'Settings.bcx')
      file = File.open(CP.saves + 'Settings.bcx', 'rb')
      Marshal.load(file) unless file.eof?
      Marshal.load(file) unless file.eof?
      Marshal.load(file) unless file.eof?
      Marshal.load(file) unless file.eof?
      $unlocks = Marshal.load(file) unless file.eof?
      $controls = Marshal.load(file) unless file.eof?
      file.close
    else
      self.data_save
    end
  end
  
  def self.sver_load
    result = ''
    if File.exist?(CP.saves + 'Settings.bcx')
      file = File.open(CP.saves + 'Settings.bcx', 'rb')
      result = Marshal.load(file)
      file.close
    end
    return result
  end
  
  def self.data_save
    file = File.open(CP.saves + 'Settings.bcx', 'wb')
    ["CP_Settings_#{self.ver($version)}", false, false, false, $unlocks,
        $controls].each {|i| Marshal.dump(i, file)}
    file.close
  end
  
  def self.unlock(mode)
    if mode >= 4
      $unlocks[mode-3] = true
    elsif $unlocks[0] < mode
      $unlocks[0] = mode
    end
    self.data_save
  end
  
  def self.ver(version = $game_system.version)
    v = []
    v.push((version).to_i)
    v.push((version * 10).to_i % 10)
    v.push((version * 100).to_i % 10)
    v.push((version * 1000).round % 10)
    return "#{v[0]}.#{v[1]}.#{v[2]}.#{v[3]}"
  end
  
  def self.map_name(id = $game_map.map_id, switches = $game_switches)
    name = $map_names[id].clone
    if (name == 'Unknown Aircraft' || name == 'Unbekanntes Flugschiff') &&
        switches[182]
      name = 'Cravgon'
    end
    if !switches[277]
      name = 'Unknown House' if name == 'Ariana\'s House'
      name = 'Unbekanntes Haus' if name == 'Arianas Haus'
    end
    return name
  end
  
  def self.make_game_text(type = true)
    text = (type ? 'Loading game...' : 'Saving game...')
    bitmap = Bitmap.new(1, 1)
    bitmap.font.size = 22
    w = bitmap.text_size(text).width + 40
    bitmap.dispose
    $game = Window_Base.new(320 - w/2, 208, w, 80)
    $game.contents = Bitmap.new(w - 32, 48)
    $game.windowskin = RPG::Cache.windowskin('Black Death')
    $game.contents.font.size = 22
    $game.contents.draw_text(0, 0, w - 32, 32, text, 1)
    $game.contents.progress_bar(w-40, 0, true)
    $game.opacity, $game.z = 192, 15000
    Graphics.update
  end
  
  # sorted:    1~448
  # Recovery
  Skills = [1, 2, 3, 377, 357, 342, 86, 87, 356, 4, 5, 6, 376, 237, 378, 424]
  # Attack Magic
  # - Fire
  Skills += [7, 115, 153, 8, 9, 279, 230, 320, 205, 185]
  # - Ice
  Skills += [10, 213, 11, 12, 305]
  # - Electro
  Skills += [13, 14, 15, 308, 374, 191, 373]
  # - Water
  Skills += [16, 17, 18, 189, 382]
  # - Earth
  Skills += [19, 20, 21, 264, 184, 395]
  # - Air
  Skills += [22, 23, 24, 190, 396]
  # - Light
  Skills += [25, 26, 27, 319, 186, 348, 201]
  # - Darkness
  Skills += [28, 29, 30, 178, 389, 434]
  # - Nova
  Skills += [182, 82, 169, 227, 81, 183]
  # - Other Attack
  Skills += [303, 310, 435, 438]
  # - Other
  Skills += [221, 231, 194, 195, 411, 161, 83]
  # Support
  Skills += [109, 110, 54, 262, 55, 263, 53, 281, 177, 56, 379, 85, 138, 409,
             249, 111, 344, 192, 112, 343, 88, 89, 90, 91, 92, 93, 94, 95, 96,
             336, 381]
  # Status Magic
  Skills += [33, 34, 41, 42, 43, 44, 35, 36, 39, 40, 37, 38, 45, 46, 47, 48,
             49, 50, 380, 51, 52, 407, 408, 421, 164, 165]
  # Technique
  # - Basic
  Skills += [61, 57, 100, 288, 222, 427, 420, 119, 216, 277, 391, 392, 425,
             116, 117, 236, 101, 102, 180, 250, 439, 449, 193, 385, 299, 300,
             369, 273, 394, 415, 426, 429, 446, 447, 314, 215, 84, 443, 445,
             98]
  # - Gun
  Skills += [286, 289, 315, 295, 358, 359, 360, 436]
  # - Dragon
  Skills += [307, 311, 313, 309]
  # - UF
  Skills += [225, 361, 448, 223, 224, 226, 254, 252, 433, 306, 442]
  
  # sorted:    1~164
  # basic items
  Items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 23, 155]
  # negative status removal items
  Items += [11, 12, 24, 25, 29, 26, 27, 28]
  # positive status add items
  Items += [13, 14, 15, 16, 30, 78, 42, 79, 45, 46, 47, 48, 49, 50, 51, 52]
  # game manipulating items
  Items += [31, 32]
  # bullets
  Items += [122, 123, 128, 137, 149]
  # special utility items
  Items += [159, 160, 164]
  # dragons
  Items += [129, 153]
  # dragon skills
  Items += [133, 134, 135, 136, 138, 147, 154, 157, 150]
  # UF items
  Items += [81, 110, 152, 156, 158]
  # permanent attribute increaser
  Items += [17, 18, 19, 20, 21, 22]
  # permanent monster attribute increaser
  Items += [73, 74, 75, 76, 77]
  # trading items
  Items += [83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98,
            99, 100, 101, 102, 103, 104, 105, 106]
  # utility items
  Items += [151, 33, 36, 80, 43]
  # main quest items
  Items += [35, 39, 40, 120, 44, 37, 82, 118, 124, 125, 127, 130, 131, 146,
            144, 140, 141, 142, 145, 143, 139]
  # main quest expendable items
  Items += [66, 67, 68, 69, 70, 71, 72, 34, 111, 119, 121, 148]
  # side quest collection items
  Items += [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 107, 108, 109]
  # side quest other items
  Items += [38, 41, 65, 161, 162, 163, 112, 113, 114, 115, 116, 117, 126]
  
  def self.resort_skills(ary)
    # -> Rest
    skills = Skills + ((1...$data_skills.size).to_a - Skills)
    return (skills - (skills - ary))
  end
  
  def self.resort_items
    # rest
    items = Items + ((1...$data_items.size).to_a - Items)
    result = [nil]
    items.each {|i| result.push($data_items[i])}
    return result
  end
  
  def self.resort_weapons
    weapons = []
    (1...$data_weapons.size).each {|i| weapons.push(i)}
    weapons.sort! do |a, b|
      if $data_weapons[a].atk > $data_weapons[b].atk
        +1
      elsif $data_weapons[a].atk < $data_weapons[b].atk
        -1
      elsif $data_weapons[a].price == 0 && $data_weapons[b].price > 0
        +1
      elsif $data_weapons[a].price > 0 && $data_weapons[b].price == 0
        -1
      elsif $data_weapons[a].price > $data_weapons[b].price
        +1
      elsif $data_weapons[a].price < $data_weapons[b].price
        -1
      elsif $data_weapons[a].name > $data_weapons[b].name
        +1
      elsif $data_weapons[a].name < $data_weapons[b].name
        -1
      else
        b <=> a
      end
    end
    result = [nil]
    weapons.each {|i| result.push($data_weapons[i])}
    return result
  end
  
  Armors = [25, 26, 27, 28, 29, 30, 32, 63, 64, 132, 109, 76, 73, 178, 179,
            174, 175, 173, 172, 162, 65, 66, 67, 68, 40, 128, 77, 80, 53, 55,
            57, 78, 106, 122, 92, 95, 180, 181, 177, 107, 108, 94, 96, 97]
  
  def self.resort_armors
    armors = []
    (1...$data_armors.size).each {|i| armors.push(i)}
    armors.sort! do |a, b|
      if $data_armors[a].kind > $data_armors[b].kind
        +1
      elsif $data_armors[a].kind < $data_armors[b].kind
        -1
      elsif $data_armors[a].pdef + $data_armors[a].mdef > $data_armors[b].pdef + $data_armors[b].mdef
        +1
      elsif $data_armors[a].pdef + $data_armors[a].mdef < $data_armors[b].pdef + $data_armors[b].mdef
        -1
      elsif $data_armors[a].price == 0 && $data_armors[b].price > 0
        +1
      elsif $data_armors[a].price > 0 && $data_armors[b].price == 0
        -1
      elsif $data_armors[a].price > $data_armors[b].price
        +1
      elsif $data_armors[a].price < $data_armors[b].price
        -1
      elsif $data_armors[a].name > $data_armors[b].name
        +1
      elsif $data_armors[a].name < $data_armors[b].name
        -1
      else
        b <=> a
      end
    end
    armors = (armors - Armors) + Armors
    result = [nil]
    armors.each {|i| result.push($data_armors[i])}
    return result
  end
  
  SCREEN = Win32API.new('chaosengine.cpx', 'Screenshot', ['l', 'l', 'l', 'l', 'p', 'l', 'l'], '')
  SAVE_FILE = 'LLIVCP %Y-%m-%d %H-%M-%S.png'
  
  def self.get_window
    game_name = "\0" * 256
    read_ini = Win32API.new('kernel32', 'GetPrivateProfileStringA', ['p', 'p', 'p', 'p', 'l', 'p'], 'l')
    read_ini.call('Game', 'Title', '', game_name, 255, './Chaos.ini')
    game_name += "\0"
    find_window = Win32API.new('user32', 'FindWindowA', ['p', 'p'], 'L')
    return find_window.call('RGSS Player', game_name)
  end
  WINDOW = self.get_window
  
  def self.break_screen
    SCREEN.call(0, 0, 640, 480, CP.temp + 'tmp.png', WINDOW, 2)
    bitmap = RPG::Cache.load_bitmap('', CP.temp + 'tmp')
    File.delete(CP.temp + 'tmp.png')
    return bitmap
  end
  
  def self.screen
    SCREEN.call(0, 0, 640, 480, Time.now.strftime(CP.screens + SAVE_FILE),
        WINDOW, 2)
    if $game_system != nil
      $game_system.se_play(RPG::AudioFile.new('snap', 65, 100))
    else
      Audio.se_play('Audio/SE/snap', 65, 100)
    end
  end
  
  def self.init_game
    $data_actors        = load_data('Data/Actors.rxdata')
    $data_classes       = load_data('Data/Classes.rxdata')
    $data_skills        = load_data('Data/Skills.rxdata')
    $data_items         = load_data('Data/Items.rxdata')
    $data_weapons       = load_data('Data/Weapons.rxdata')
    $data_armors        = load_data('Data/Armors.rxdata')
    $data_enemies       = load_data('Data/Enemies.rxdata')
    $data_troops        = load_data('Data/Troops.rxdata')
    $data_states        = load_data('Data/States.rxdata')
    $data_animations    = load_data('Data/Animations.rxdata')
    $data_tilesets      = load_data('Data/Tilesets.rxdata')
    $data_common_events = load_data('Data/CommonEvents.rxdata')
    $data_system        = load_data('Data/System.rxdata')
    ($data_actors - [nil]).each {|actor| actor.generate_parameters}
    $map_names          = load_data('Data/MapInfos.rxdata')
    $map_lex = {}
    $map_names.each_key {|key|
        $map_lex[key] = ($map_names[key].name.gsub!('\\lex') {''} == nil)
        $map_names[key] = $map_names[key].name}
  end
  
  def self.setup_temp_folder
    begin
      @temp = ENV['TEMP'].gsub('\\', '/') + '/'
    rescue
      @temp = ''
    end
  end
  
  def self.temp
    return @temp
  end
  
  def self.setup_system_path
    path = ENV['ALLUSERSPROFILE'].gsub('\\') {'/'}
    path += '/' + ENV['APPDATA'].split('\\').pop if ENV['LOCALAPPDATA'] == nil
    path += '/Stormtronics/Lexima Legends IV - Chaos Project/'
    path += ENV['USERNAME'] + '/'
    return path
  end
  
  def self.setup_saves_folder
    begin
      @saves = self.setup_system_path + 'Saves/'
      self.create_folder(@saves)
    rescue
      @saves = 'Saves/'
      self.create_folder(@saves)
    end
  end
  
  def self.setup_screens_folder
    begin
      @screens = self.setup_system_path + 'Screenshots/'
      self.create_folder(@screens)
    rescue
      @screens = 'Screenshots/'
      self.create_folder(@screens)
    end
  end
  
  def self.create_folder(path)
    folders = path.split('/')
    path = folders.shift
    folders.each {|folder|
        path += '/' + folder
        Dir.mkdir(path) if !FileTest.exist?(path)}
  end
  
  def self.saves
    create_folder(@saves)
    return @saves
  end
  
  def self.screens
    create_folder(@screens)
    return @screens
  end
  
end

if $CP
  if File.exist?('../tools/require/modules.rb')
    require File.expand_path('../tools/require/modules.rb')
  end
end

# Game Initialization

CP.setup_temp_folder
CP.setup_saves_folder
CP.setup_screens_folder
$english = true

$unlocks, $controls = [0], CP::Controls.new
CP.data_load
if $CP
  if GENERATE_DAMAGE && File.exist?('../tools/require/generate_damage.rb')
    require File.expand_path('../tools/require/generate_damage.rb')
    CP::Cache.generate_damage
  end
end
CP::Cache.load
if @unlocks == true || $unlocks == false
  $unlocks, $controls = [0], CP::Controls.new
elsif CP.sver_load == 'CPStaticSettings'
  $controls = CP::Controls.new
end
$controls.key_convert
