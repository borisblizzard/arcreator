#==============================================================================
# Game_Actor
#==============================================================================

class Game_Actor
  
  alias str_uf_later str
  def str
    result = str_uf_later
    if $game_temp.uf_override
      $game_temp.uf_override = nil
      new = (($game_party.actors - [self]).sort {|a, b| b.str - a.str})[0].str
      $game_temp.uf_override = true
      result = new if new > result
    end
    return result
  end
  
  alias dex_uf_later dex
  def dex
    result = dex_uf_later
    if $game_temp.uf_override
      $game_temp.uf_override = nil
      new = (($game_party.actors - [self]).sort {|a, b| b.dex - a.dex})[0].dex
      $game_temp.uf_override = true
      result = new if new > result
    end
    return result
  end
  
  alias agi_uf_later agi
  def agi
    result = agi_uf_later
    if $game_temp.uf_override
      $game_temp.uf_override = nil
      new = (($game_party.actors - [self]).sort {|a, b| b.agi - a.agi})[0].agi
      $game_temp.uf_override = true
      result = new if new > result
    end
    return result
  end
  
  alias int_uf_later int
  def int
    result = int_uf_later
    if $game_temp.uf_override
      $game_temp.uf_override = nil
      new = (($game_party.actors - [self]).sort {|a, b| b.int - a.int})[0].int
      $game_temp.uf_override = true
      result = new if new > result
    end
    return result
  end
  
  alias hit_uf_later hit
  def hit
    result = hit_uf_later
    if $game_temp.uf_override
      $game_temp.uf_override = nil
      new = (($game_party.actors - [self]).sort {|a, b| b.hit - a.hit})[0].hit
      $game_temp.uf_override = true
      result = new if new > result
    end
    return result
  end
  
  alias atk_uf_later atk
  def atk
    result = atk_uf_later
    if $game_temp.uf_override
      $game_temp.uf_override = nil
      new = (($game_party.actors - [self]).sort {|a, b| b.atk - a.atk})[0].atk
      $game_temp.uf_override = true
      result = new if new > result
    end
    return result
  end
  
  alias pdef_uf_later pdef
  def pdef
    result = pdef_uf_later
    if $game_temp.uf_override
      $game_temp.uf_override = nil
      new = (($game_party.actors - [self]).sort {|a, b| b.pdef - a.pdef})[0].pdef
      $game_temp.uf_override = true
      result = new if new > result
    end
    return result
  end
  
  alias mdef_uf_later mdef
  def mdef
    result = mdef_uf_later
    if $game_temp.uf_override
      $game_temp.uf_override = nil
      new = (($game_party.actors - [self]).sort {|a, b| b.mdef - a.mdef})[0].mdef
      $game_temp.uf_override = true
      result = new if new > result
    end
    return result
  end
  
  alias eva_uf_later eva
  def eva
    result = eva_uf_later
    if $game_temp.uf_override
      $game_temp.uf_override = nil
      new = (($game_party.actors - [self]).sort {|a, b| b.eva - a.eva})[0].eva
      $game_temp.uf_override = true
      result = new if new > result
    end
    return result
  end
  
end
