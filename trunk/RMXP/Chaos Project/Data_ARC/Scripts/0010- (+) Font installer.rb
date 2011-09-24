#==============================================================================
# Scene_Stormtronics
#==============================================================================

Fontfiles = [
    'Impressed.ttf',
    'Future.ttf',
    'Papyrus.ttf',
    'CopperPlate-Normal.ttf',
    'Brush.ttf',
    'Geometrix.ttf',
    'LED_REAL.ttf',
    'EurostileExtended-Roman-DTC.ttf'
    ]
Fontnames = [
    'Impressed',
    'Future',
    'Papyrus',
    'CopperPlate-Normal',
    'Brush Script',
    'Geometrix',
    'LED Real',
    'EurostileExtended-Roman-DTC'
    ]
          
module CP
  
  def self.font_install
    str = ENV['SystemRoot'].sub('WINNT', '')
    win = ENV['SystemRoot'].dup.sub(str, '')
    if win == 'WINNT'
      p 'Lexima 4 found a possible problem while initializing the ' +
         'font installer. Please install these fonts manually if problems occur.'
    end
    install = Win32API.new('gdi32', 'AddFontResource', ['P'], 'L')
    nofity_WINDOZE = Win32API.new('kernel32', 'WriteProfileString', ['P', 'P', 'P'], 'L')
    nofity_user = Win32API.new('user32', 'SendMessage', ['L', 'L', 'L', 'L'], 'L')
    _SourceF = 'Fontfiles/'
    _WINFonts = ENV['SystemRoot'].sub('\\') {'/'} + '/Fonts/'
    succeeded, failed, missing = [], [], []
    Fontfiles.each_index {|i|
        font = Fontfiles[i]
        if FileTest.exists?(_SourceF + font)
          if FileTest.exists?(_WINFonts + font) &&
              FileTest.size(_WINFonts + font) == FileTest.size(_SourceF + font)
            next
          end
          begin
            FileUtils.copy(_SourceF + font, _WINFonts + font)
            install.call(_SourceF + font)
            nofity_WINDOZE.call('Fonts', Fontnames[i], font)
            nofity_user.call(0xFFFF, 0x001D,0,0)
            if FileTest.exists?(_WINFonts + font)
              succeeded.push(Fontnames[i])
            else
              failed.push(font)
            end
          rescue
            failed.push(font)
          end
        else
          missing.push(font)
        end}
    succeeded_fonts = succeeded.join(', ')
    if succeeded_fonts != nil && succeeded_fonts != ''
      p "Installed following fonts: #{succeeded_fonts}"
    end
    failed_fonts = failed.join(', ')
    if failed_fonts != nil && failed_fonts != ''
      p "Could not install following fontfiles: #{failed_fonts}" +
        '. Please install these fonts manually.'
    end
    missing_fonts = missing.join(', ')
    if missing_fonts != nil && missing_fonts != ''
      p "Could not find following fontfiles: #{missing_fonts}"
    end
    if succeeded_fonts != nil && succeeded_fonts != ''
      p 'New fonts were installed. Restarting Lexima 4 now. If you ' +
        'experience any problems, please manually install the fonts by ' +
        "copying the font files located in .\\#{_SourceF} folder" +
        " into your #{_WINFonts} folder and/or restaring your PC."
      Thread.new {system(FileTest.exist?('Chaos.exe') ? 'Chaos' : 'Game')}  
      exit
    end
  end
  
end

CP.font_install
