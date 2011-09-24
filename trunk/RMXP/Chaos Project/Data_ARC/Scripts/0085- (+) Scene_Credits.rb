#==============================================================================
# Credits v3.0 Scroller Edition - by Blizzard
#==============================================================================

#==============================================================================
# Scene_Credits
#==============================================================================

class Scene_Credits
  
  def get_text
    text = []
    text.push('Director and executive director')
    text.push('')
    text.push('- Boris Mikić')
    text.push('', '', '', '', '', '', '', '')
    text.push('Storyline, character plot and scenario')
    text.push('')
    text.push('- Boris Mikić')
    text.push('', '', '', '', '', '', '', '')
    text.push('Dialogue director')
    text.push('')
    text.push('- Boris Mikić')
    text.push('', '', '', '', '', '', '', '')
    text.push('Final Demo beta testers')
    text.push('')
    text.push('- Chaos of Destruction')
    text.push('- Winged')
    text.push('', '', '', '', '', '', '', '')
    text.push('Full Game beta testers')
    text.push('')
    text.push('- Boris Matešin')
    text.push('- Fantasist')
    text.push('- game_guy')
    text.push('- GuardianAngelX72')
    text.push('- Juan')
    text.push('- King Munkey')
    text.push('- Longfellow')
    text.push('- Memor-X')
    text.push('- mumerus')
    text.push('- NAMKCOR')
    text.push('- Pokol Da\'Erran')
    text.push('- Reno-s--Joker')
    text.push('- Ryexander')
    text.push('- shdwlink1993')
    text.push('- Shining Riku')
    text.push('- winkio')
    text.push('', '', '', '', '', '', '', '')
    text.push('General art')
    text.push('')
    text.push('- Boris Mikić')
    text.push('', '', '', '', '', '', '', '')
    text.push('Map design')
    text.push('')
    text.push('- Boris Mikić')
    text.push('- Peter-Pascal Benn (Kadro cities, Luvia Sewers)')
    text.push('', '', '', '', '', '', '', '')
    text.push('Direct scripter')
    text.push('')
    text.push('- Boris Mikić')
    text.push('', '', '', '', '', '', '', '')
    text.push('Events and in-depth game restructure')
    text.push('')
    text.push('- Boris Mikić')
    text.push('', '', '', '', '', '', '', '')
    text.push('Soundtrack')
    text.push('')
    text.push('For reference about the soundtrack please')
    text.push('see the Audio folder in the game\'s folder')
    text.push('', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    text.push('Special thanks to...')
    text.push('', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    text.push('Enterbrain')
    text.push('')
    text.push('- game engine')
    text.push('- main tilesets')
    text.push('- common system')
    text.push('', '', '', '', '', '', '', '')
    text.push('rod211')
    text.push('')
    text.push('- Grave Guard graphic (originally Wraith)')
    text.push('', '', '', '', '', '', '', '')
    text.push('TheInquisitor, R. Janes, Arramon, HungryMouse')
    text.push('')
    text.push('- world map tileset')
    text.push('', '', '', '', '', '', '', '')
    text.push('poyzinblud')
    text.push('')
    text.push('- satanic church tileset')
    text.push('', '', '', '', '', '', '', '')
    text.push('orochi weapon')
    text.push('')
    text.push('- Death Magic animation set')
    text.push('', '', '', '', '', '', '', '')
    text.push('K-2')
    text.push('')
    text.push('- Sword Slash animation set')
    text.push('', '', '', '', '', '', '', '')
    text.push('The makers of "Ragnarok Online" and')
    text.push('the makers of "Magic - The Gathering"')
    text.push('')
    text.push('- several graphics')
    text.push('', '', '', '', '', '', '', '')
    text.push('landofshadows')
    text.push('')
    text.push('- several graphics')
    text.push('', '', '', '', '', '', '', '')
    text.push('sithjester')
    text.push('')
    text.push('- several graphics')
    text.push('', '', '', '', '', '', '', '')
    text.push('Sam Wise')
    text.push('')
    text.push('- Archnemesis\' graphic')
    text.push('', '', '', '', '', '', '', '')
    text.push('Alex Burness alias Phasedscar')
    text.push('')
    text.push('- several sprites and graphics')
    text.push('', '', '', '', '', '', '', '')
    text.push('Hot Toke')
    text.push('')
    text.push('- several battlers')
    text.push('', '', '', '', '', '', '', '')
    text.push('Dave Allsop')
    text.push('')
    text.push('- several battlers')
    text.push('', '', '', '', '', '', '', '')
    text.push('MightyLink')
    text.push('')
    text.push('- Mountains of Slumber battle background')
    text.push('', '', '', '', '', '', '', '')
    text.push('DeathLock')
    text.push('')
    text.push('- Breath of Ice character graphic')
    text.push('', '', '', '', '', '', '', '')
    text.push('Tori')
    text.push('')
    text.push('- gangster graphics')
    text.push('', '', '', '', '', '', '', '')
    text.push('Spencer Lee Conrad alias legacyblade')
    text.push('')
    text.push('- gangster down graphics')
    text.push('', '', '', '', '', '', '', '')
    text.push('thephantom')
    text.push('')
    text.push('- several tilesets')
    text.push('', '', '', '', '', '', '', '')
    text.push('pamansazz (at deviantart)')
    text.push('')
    text.push('- several dragon images')
    text.push('', '', '', '', '', '', '', '')
    text.push('Cronus')
    text.push('')
    text.push('- Lilith\'s battler')
    text.push('', '', '', '', '', '', '', '')
    text.push('Calintz')
    text.push('')
    text.push('- Lilith\'s sprite')
    text.push('', '', '', '', '', '', '', '')
    text.push('Capcom & Namco')
    text.push('')
    text.push('- several graphics')
    text.push('', '', '', '', '', '', '', '')
    text.push('Andreas21')
    text.push('')
    text.push('- the Screenshot.dll')
    text.push('', '', '', '', '', '', '', '')
    text.push('KGC')
    text.push('')
    text.push('- 3D Pseudo Battle Camera')
    text.push('', '', '', '', '', '', '', '')
    text.push('Matthew Welch')
    text.push('')
    text.push('- LED Real Font')
    text.push('', '', '', '', '', '', '', '')
    text.push('shdwlink1993')
    text.push('')
    text.push('- fixing my English grammar')
    text.push('', '', '', '', '', '', '', '')
    text.push('Zeriab')
    text.push('')
    text.push('- basic F12 Override Code')
    text.push('- general testing')
    text.push('', '', '', '', '', '', '', '')
    text.push('Ericmor, arrowone, thingy, AlbelNox')
    text.push('')
    text.push('- testing a very early version')
    text.push('', '', '', '', '', '', '', '')
    text.push('Boris Matešin')
    text.push('')
    text.push('- fixing my English grammar')
    text.push('- beta testing')
    text.push('- motivating me')
    text.push('', '', '', '', '', '', '', '')
    text.push('Ivan Bosnić and Ivan Kravarščan')
    text.push('')
    text.push('- supporting and motivating me')
    text.push('', '', '', '', '', '', '', '')
    text.push('several members on rmrk.net')
    text.push('and chaos-project.com')
    text.push('')
    text.push('- testing my scripts and such')
    text.push('', '', '', '', '', '', '', '')
    text.push('You')
    text.push('')
    text.push('- for playing')
    text.push('', '', '', '', '', '', '', '')
    text.push('And thanks to everybody')
    text.push('I probably forgot to mention!')
    return text
  end
  
  def get_new_bitmap
    bitmap = Bitmap.new(640, 256)
    bitmap.font.name = 'Geometrix'
    bitmap.font.size = 30
    return bitmap
  end
  
  def draw_next(sprite)
    sprite.bitmap.clear
    i = 0
    while @text.size > 0 && i < 8
      sprite.bitmap.draw_text(32, i*32, 576, 32, @text.shift)
      i += 1
    end
  end
  
  def main
    Audio.bgm_stop
    Audio.bgs_stop
    Graphics.transition
    Graphics.freeze
    Audio.me_play('Audio/BGM/E Nomine - Schwarze Sonne (Talla 2XLC RMX, Blizzard Mix)', 90, 100)
    @Credits = Sprite.new
    @text = self.get_text
    @sprites = [Sprite.new, Sprite.new, Sprite.new]
    @sprites[1].bitmap = RPG::Cache.picture('CreditsFirst')
    @sprites[0].y, @sprites[2].y = -256, 256
    Graphics.transition
    self.delay(3)
    Graphics.freeze
    @stopped = false
    @sprites[0].bitmap = get_new_bitmap
    @sprites[1].bitmap = get_new_bitmap
    @sprites[2].bitmap = get_new_bitmap
    Graphics.transition
    loop do
      Graphics.update
      Input.update
      update
      break if @stopped
    end
    Graphics.freeze
    Graphics.transition
    Graphics.freeze
    @sprites[1].bitmap = @sprites[2].bitmap = nil
    @sprites[1].dispose
    @sprites[2].dispose
    @sprites = [@sprites[0]]
    @sprites[0].y = 0
    @sprites[0].bitmap = RPG::Cache.picture('CreditsLast')
    Graphics.transition
    self.delay(4)
    Graphics.freeze
    @sprites[0].bitmap = nil
    Graphics.transition
    self.delay(1)
    Graphics.freeze
    @sprites[0].bitmap = RPG::Cache.picture('CreditsTheEnd')
    Graphics.transition
    self.delay(8)
    Graphics.freeze
    @sprites[0].dispose
    Graphics.transition
    self.delay(1)
    Audio.me_fade(800)
    Graphics.freeze
    $scene = Scene_Stormtronics.new
  end
  
  def update
    move = ((Input.press?($controls.confirm) ||
          Input.press?($controls.cancel))) ? 32 : 2
    if @text.size > 0
      @sprites.each {|sprite| sprite.y -= move}
      if @sprites[0].y <= -256
        @sprites[0].y += 768
        self.draw_next(@sprites[0])
        @sprites.push(@sprites.shift)
      end
    elsif @sprites.any? {|sprite| sprite.y > -256} && !@stopped
      @sprites.each {|sprite| sprite.y -= move}
    else
      @stopped = true
    end
  end
    
  def delay(sec)
    time = 0
    while time < sec * 40
      Graphics.update
      Input.update
      move = ((Input.press?($controls.confirm) ||
            Input.press?($controls.cancel))) ? 16 : 1
      time += move
    end
  end
  
end
