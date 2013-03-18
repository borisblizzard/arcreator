module Kernel
  
  class << Kernel
    alias load_cp_data load_data
  end
  
  def load_data(filename)
    if filename == 'Data/MapData.cpx' || filename =~ /Map(\d{3}).rxdata/
      CP::EXTENSIONS.each_key {|key|
          filename = filename.gsub(".#{key}") {".#{CP::EXTENSIONS[key]}"}}
      file = File.open(filename, 'rb')
      rawdata = file.read
      file.close
      first = nil
      rawdata.each_byte {|byte|
          first = byte
          break}
      rawdata[0] = ((first + 128) % 256).chr
      data = Zlib::Inflate.inflate(rawdata)
      return Marshal.load(data)
    end
    return Kernel.load_cp_data(filename)
  end
  
end
