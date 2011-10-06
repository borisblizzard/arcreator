if $CP
  if File.exist?('../tools/require/absmap.rb')
    require File.expand_path('../tools/require/absmap.rb')
  end
  if File.exist?('../tools/require/beta.rb')
    require File.expand_path('../tools/require/beta.rb')
  end
end
