module RPG::Cache
  
  def self.load_bitmap(folder_name, filename, hue = 0)
    path = folder_name + filename
    if !@cache.has_key?(path) || @cache[path].disposed?
      if filename != ''
        if folder_name != ''
          file = File.open(folder_name + filename + '.cpg', 'rb')
          rawdata = file.read
          file.close
          first = nil
          rawdata.each_byte {|byte|
              first = byte
              break}
          rawdata[0] = ((first + 128) % 256).chr
          data = Zlib::Inflate.inflate(rawdata)
          file = File.open(CP.temp + 'tmp.png', 'wb')
          file.write(data)
          file.close
          @cache[path] = Bitmap.new(CP.temp + 'tmp.png')
          File.delete(CP.temp + 'tmp.png')
        else
          @cache[path] = Bitmap.new(path)
        end
      else
        @cache[path] = Bitmap.new(32, 32)
      end
    end
    return @cache[path] if hue == 0
    key = [path, hue]
    if !@cache.has_key?(key) || @cache[key].disposed?
      @cache[key] = @cache[path].clone
      @cache[key].hue_change(hue)
    end
    return @cache[key]
  end
  
  class << RPG::Cache
    alias icon_later icon
  end
  
  def self.icon(filename)
    icon = icon_later(filename)
    @desaturated = {} if @desaturated == nil
    @desaturated[filename] = icon.desaturate if !@desaturated.has_key?(filename)
    return icon
  end
  
  def self.desaturated(filename)
    self.icon(filename) if @desaturated == nil || !@desaturated.has_key?(filename)
    return @desaturated[filename] 
  end
  
end
