FINAL = !true

if !FINAL
$CP = true

require File.expand_path('debug.rb') if File.exist?('debug.rb')
require File.expand_path('test.rb') if File.exist?('test.rb')
require File.expand_path('rtester.rb') if File.exist?('rtester.rb')
end

if !$CP && ($DEBUG || $BTEST)
  raise 'Critical Error! Chaos.exe is corrupted. Please reinstall the game.'
end
