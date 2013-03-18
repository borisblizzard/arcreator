#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=
# DREAM by Blizzard
# Version: 4.0
# Date: 19.8.2007
#:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=

module DREAM
  
  def self.initialize
    @version = 4.0
  end  
    
  def self.decode_old_dream(data_ary)
    ary = []
    data_ary.each {|i|
        index = case i
        when Array then 0
        when Numeric then 1
        when Game_System then 2
        when Game_Switches then 3
        when Game_Variables then 4
        when Game_SelfSwitches then 5
        when Game_Screen then 6
        when Game_Actors then 7
        when Game_Party then 8
        when Game_Troop, nil then 9
        when Game_Map then 10
        when Game_Player then 11
        when String then 12
        end
        if index == 0 && i[0].is_a?(String)
          if i[1].is_a?(Numeric)
            ary[1] = i[1]
          elsif i[2].is_a?(Numeric)
            ary[1] = i[2]
          end
        end
        ary[index] = i if ary[index] == nil}
    return ary
  end
  
  def self.randomize_ary(data_ary)
    ary = data_ary.clone
    result = []
    data_ary.each_index {|i| result.push(ary.delete_at(rand(ary.size)))}
    return result
  end
  
  def self.create_encryption_pattern(ary, sys)
    data = []
    (0...ary.size**2).each {|i| data.push(rand(500) + 1001)}
    dat = self.make_primes(2, 1000, 16000)
    result = [ary.shift, self.randomize_ary(data + (0...ary.size).to_a)]
    result[1].each_index {|i|
        if result[1][i] < 1000
          result.push(ary[result[1][i]])
          result[1][i] *= dat[1]
        else
          result[1][i] = (result[1][i] - 1000) * dat[0]
        end}
    result[1].unshift(dat[0] * dat[1])
    variation = rand(result[1].size - 1) + 1
    result[1].push(rand(0xFFFF) / variation * variation + 1)
    (0...(result[1].size-1)).each {|i|
        if i != variation
          result[1][i] -= result[1][result[1].size-1] * result[1][variation]
        end}
    result[1][variation] = -result[1][variation]
    result[1][result[1].size-1] = (result[1][result[1].size-1]-1) / variation
    result[1].push(variation.to_s)
    return result + sys
  end
  
  def self.read_encryption_pattern(ary)
    ary.shift
    ary[0][ary[0].size-2] = ary[0][ary[0].size-2] * ary[0][ary[0].size-1].to_i+1
    ary[0][(ary[0][ary[0].size-1]).to_i] = -ary[0][(ary[0][ary[0].size-1]).to_i]
    (0...(ary[0].size-2)).each {|i|
        if i != (ary[0][ary[0].size-1]).to_i
          ary[0][i] += ary[0][ary[0].size-2] * ary[0][(ary[0][ary[0].size-1]).to_i]
        end}
    ary[0] = ary[0][0, ary[0].size-2]
    pattern = ary.shift
    dat = self.get_primes(pattern.shift)
    if dat == false
      raise "Critical error occured while returning the saved data. RMXP will now close."
    end
    result = []
    pattern.each_index {|i|
        if pattern[i] == pattern[i] / dat[1] * dat[1]
          result[pattern[i]/dat[1]] = ary.shift
        end}
    return result, ary
  end
  
  def self.make_primes(num, min, max)
    primes, dat, x = [], [], []
    (0...max/32).each {|i| x[i] = -1}
    (0...max).each {|i|
        if (x[i/32] >> (i%32) & 1) != 0
          step = 2*i+3;
          primes.push(step) if i > min
          ((step**2-3)/2).step(max, step){|j| x[j/32] &= ~(1<<j%32)}
        end}
    num.times {dat.push(primes.delete_at(rand(primes.size)))}
    return dat.sort
  end
  
  def self.get_primes(prime)
    (2...(prime-1)).each {|i| return [i, prime / i] if prime == prime / i * i}
    return false
  end
  
  def self.dream4_encryption(ary)
    key = 'Encrypted with Blizzard\'s DREAM v4.x. Try hacking THIS, n00b. =P'
    result1, result2 = [], []
    ary.each_index {|i|
        result1.push((ary[i].is_a?(Numeric) ? ary[i] : ary[i].clone).encdream4a)
        result2.push((ary[i].is_a?(Numeric) ? ary[i] : ary[i].clone).encdream4b)
        $game.contents.progress_bar($game.width-40, (i+1).to_f/(ary.size+1), 1)
        Graphics.update}
    return [key] + result1 + result2
  end
  
  def self.dream4_decryption(ary, data)
    data.each_index {|i|
        data[i] = data[i].decdream4(ary[0, ary.size/2][i], ary[ary.size/2, ary.size/2][i])
        if $game != nil
          $game.contents.progress_bar($game.width-40, (i+1).to_f/(data.size+1), 2)
          Graphics.update
        elsif i % 3 == 0
          Graphics.update
        end}
    return data
  end

  def self.dat(file1, ary)
    return Marshal.load(file1) if ary == true
    Marshal.dump(ary, file1)
  end

end

#==============================================================================
# Object
#==============================================================================

class Object

  def encdream4a
    ary = []
    if self.is_a?(Array)
      self.each {|i| ary.push(i.encdream4a)}
    elsif self.is_a?(Hash)
      ary = {}
      self.each_key {|i| ary[i] = self[i].encdream4a}
    else
      tmp = nil
      self.instance_variables.each {|item|
          eval("tmp = #{item}")
          ary.push(tmp.encdream4a)}
    end
    return ((ary.is_a?(Array) && ary.size == 0) ? self : ary)
  end
  
  def encdream4b
    ary = []
    if self.is_a?(Array)
      self.each {|i| ary.push(i.encdream4b)}
    elsif self.is_a?(Hash)
      ary = {}
      self.each_key {|i| ary[i] = self[i].encdream4b}
    else
      tmp = nil
      self.instance_variables.each {|item|
          eval("tmp = #{item}")
          ary.push(item, tmp.encdream4b)}
    end
    return ary
  end
  
  def decdream4(data1, data2)
    if self.is_a?(Array)
      self.each_index {|i| self[i] = self[i].decdream4(data1[i], data2[i])}
    elsif self.is_a?(Hash)
      self.each_key {|i| self[i] = self[i].decdream4(data1[i], data2[i])}
    elsif !data2.is_a?(String)
      tmp, i, j = nil, 0, 0
      while i < data2.size do
        eval("tmp = #{data2[i]}")
        tmp = tmp.decdream4(data1[j], data2[i+1])
        eval("#{data2[i]} = tmp")
        i, j = i+2, j+1
      end
    end
    return self
  end
  
end
