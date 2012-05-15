if $game_exists
  Thread.new {system(FileTest.exist?('Chaos.exe') ? 'Chaos' : 'Game')}
  exit
end
$game_exists = true
