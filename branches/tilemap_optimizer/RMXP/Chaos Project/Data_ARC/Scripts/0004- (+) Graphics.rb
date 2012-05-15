if !defined?(Reset)
  class Reset < Exception
  end
end

module Graphics
  
  class << Graphics
    alias transition_enc_later transition
    alias update_f12fix_later update
  end
  
  def self.transition(time = nil, filepath = nil)
    while true
      begin
        frame_count = Graphics.frame_count
        if time == nil
          transition_enc_later
        elsif filepath == nil
          transition_enc_later(time)
        else
          begin
            file = File.open(filepath + '.cpg', 'rb')
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
            transition_enc_later(time, CP.temp + 'tmp')
            File.delete(CP.temp + 'tmp.png')
          rescue
            transition_enc_later(time, filepath)
          end
        end
        break
      rescue Reset
        time = 0
        Graphics.frame_count = frame_count
      end
    end
  end
  
  def self.update
    while true
      begin
        frame_count = Graphics.frame_count
        update_f12fix_later
        break
      rescue Reset
        Graphics.frame_count = frame_count
      end
    end
  end
  
end
