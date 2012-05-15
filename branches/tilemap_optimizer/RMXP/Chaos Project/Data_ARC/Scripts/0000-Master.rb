if File.exist?('../tools/require/devmode.rb')
  require File.expand_path('../tools/require/devmode.rb')
end

$CP = true
if !$CP && ($DEBUG || $BTEST)
  raise 'Critical Error! Chaos.exe is corrupted. Please reinstall the game.'
end
