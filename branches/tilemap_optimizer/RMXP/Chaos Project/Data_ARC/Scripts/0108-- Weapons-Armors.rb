#==============================================================================
# "Weapon/Armor HP/SP Plus" Add-on by Blizzard
# Version: 1.0
# Date: 18.8.2006
#==============================================================================

MAX_HP = 9999 # change if needed, 9999 is standard
MAX_SP = 999 # change if needed, 9999 is standard

#==============================================================================
# Game_Battler
#==============================================================================

class Game_Battler
  
  alias maxsp_hpsp_add_on_later maxsp
  def maxsp
    val = get_changed_maxsp
    val = MAX_SP if val > MAX_SP
    @sp = val if @sp > val
    return val
  end
  
  def get_changed_maxsp
    return maxsp_hpsp_add_on_later
  end
  
end

#==============================================================================
# Game_Actor
#==============================================================================

class Game_Actor < Game_Battler
  
  alias maxhp_hpsp_add_on_later maxhp
  def maxhp
    val = get_changed_maxhp
    val = MAX_HP if val > MAX_HP
    @hp = val if @hp > val
    return val
  end
  
  def get_changed_maxhp
    plus, multi = 0, 1.0
    (get_equips - [nil]).each {|equip|
        equip.hp_plus[0] ? multi *= equip.hp_plus[1] : plus += equip.hp_plus[1]}
    return (multi * (plus + maxhp_hpsp_add_on_later)).to_i
  end
  
  def get_changed_maxsp
    plus, multi = 0, 1.0
    (get_equips - [nil]).each {|equip|
        equip.sp_plus[0] ? multi *= equip.sp_plus[1] : plus += equip.sp_plus[1]}
    return (multi * (plus + maxsp_hpsp_add_on_later)).to_i
  end
  
  def get_equips
    equips = [$data_weapons[@weapon_id]]
    ary = (CP::Cache::Lucius.include?(self.id) ? $data_weapons : $data_armors)
    equips.push(ary[@armor1_id])
    [@armor2_id, @armor3_id, @armor4_id, @armor5_id, @armor6_id].each {|id|
        equips.push($data_armors[id])}
    return equips
  end
  
end

#==============================================================================
# module RPG
# Weapon
#==============================================================================

class RPG::Weapon
  
  def hp_plus
    case @id
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Weapon HP plus Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    when 5 then return [false, 100]
    when 7 then return [true, 0.95]
    when 9 then return [true, 1.05]
    when 14 then return [true, 1.1]
    when 19 then return [false, 50]
    when 33 then return [true, 1.1]
    when 38 then return [true, 0.8]
    when 39 then return [true, 1.05]
    when 50 then return [false, 100]
    when 55 then return [false, 50]
    when 57 then return [false, 50]
    when 72 then return [false, 200]
    when 75 then return [false, 100]
    when 76 then return [false, 100]
    when 77 then return [false, -100]
    when 81 then return [false, 100]
    when 82 then return [true, 1.05]
    when 83 then return [false, 200]
    when 85 then return [false, 100]
    when 86 then return [false, 200]
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Weapon HP plus Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    else
      return [false, 0]
    end
  end
  
  def sp_plus
    case @id
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Weapon SP plus Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    when 4 then return [true, 1.1]
    when 6 then return [true, 1.15]
    when 7 then return [true, 0.95]
    when 12 then return [true, 1.05]
    when 13 then return [true, 1.05]
    when 25 then return [false, 10]
    when 32 then return [false, 20]
    when 38 then return [true, 0.8]
    when 48 then return [true, 1.1]
    when 60 then return [false, 20]
    when 69 then return [false, 5]
    when 79 then return [true, 1.1]
    when 81 then return [false, 10]
    when 85 then return [false, 20]
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Weapon SP plus Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    else
      return [false, 0]
    end
  end
  
end

#==============================================================================
# module RPG
# Armor
#==============================================================================

class RPG::Armor
  
  def hp_plus
    case @id
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Armor HP plus Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    when 3 then return [true, 1.1]
    when 35 then return [false, 150]
    when 39 then return [true, 1.1]
    when 40 then return [true, 1.05]
    when 46 then return [true, 1.1]
    when 42 then return [false, 350]
    when 47 then return [false, 300]
    when 49 then return [true, 1.1]
    when 62 then return [false, 50]
    when 67 then return [false, 200]
    when 76 then return [false, 100]
    when 82 then return [false, 50]
    when 83 then return [false, 50]
    when 85 then return [true, 1.1]
    when 90 then return [true, 1.1]
    when 91 then return [true, 0.9]
    when 93 then return [false, 300]
    when 95 then return [true, 1.1]
    when 101 then return [true, 0.9]
    when 103 then return [false, 100]
    when 114 then return [false, 1000]
    when 118 then return [true, 1.1]
    when 123 then return [true, 1.05]
    when 125 then return [true, 1.05]
    when 128 then return [false, 200]
    when 136 then return [true, 1.05]
    when 138 then return [false, 100]
    when 140 then return [false, 100]
    when 144 then return [false, 100]
    when 155 then return [false, 100]
    when 156 then return [false, -100]
    when 157 then return [false, 100]
    when 159 then return [true, 1.05]
    when 160 then return [false, 200]
    when 161 then return [false, 100]
    when 165 then return [true, 1.05]
    when 171 then return [true, 1.05]
    when 174 then return [true, 1.2]
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Armor HP plus Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    else
      return [false, 0]
    end
  end
  
  def sp_plus
    case @id
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# START Armor SP plus Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    when 23 then return [true, 1.05]
    when 37 then return [true, 1.1]
    when 38 then return [true, 1.1]
    when 39 then return [true, 1.1]
    when 40 then return [true, 1.1]
    when 47 then return [false, 20]
    when 48 then return [true, 1.2]
    when 60 then return [true, 1.05]
    when 70 then return [false, 15]
    when 84 then return [false, 5]
    when 86 then return [false, 25]
    when 87 then return [true, 1.2]
    when 89 then return [true, 1.2]
    when 99 then return [true, 1.1]
    when 104 then return [true, 1.15]
    when 110 then return [false, 10]
    when 112 then return [false, 10]
    when 113 then return [false, 100]
    when 116 then return [false, 5]
    when 117 then return [false, 10]
    when 123 then return [true, 1.1]
    when 133 then return [true, 1.1]
    when 135 then return [false, 10]
    when 136 then return [true, 0.95]
    when 138 then return [false, 10]
    when 139 then return [false, 10]
    when 143 then return [true, 1.1]
    when 145 then return [false, 5]
    when 151 then return [true, 1.1]
    when 152 then return [false, 20]
    when 155 then return [false, 10]
    when 156 then return [false, 10]
    when 158 then return [true, 1.05]
    when 166 then return [true, 1.1]
    when 171 then return [false, 20]
    when 175 then return [true, 1.2]
    when 181 then return [true, 1.05]
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# END Armor SP plus Configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    else
      return [false, 0]
    end
  end
  
end
  