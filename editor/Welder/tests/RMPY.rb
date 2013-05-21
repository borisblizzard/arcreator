load 'data.rb'

module RMPY

  @@io = nil
  @@symbols = {}
  @@strings = {}
  @@stack = []
  @@top_string = "\\^ "
  @@sym_count = 0
  @@good_objects = [FalseClass, TrueClass, NilClass, String, Numeric, Array] + 
                   [Hash, RPG::Actor, RPG::Class, RPG::Class::Learning] +
                   [RPG::Skill, RPG::Item, RPG::EventCommand, RPG::Weapon] +
                   [RPG::Armor, RPG::Enemy, RPG::Enemy::Action, RPG::Troop] +
                   [RPG::Troop::Member, RPG::Troop::Page] + 
                   [RPG::Troop::Page::Condition, RPG::State] +
                   [RPG::Animation, RPG::Animation::Frame] +
                   [RPG::Animation::Timing, RPG::Tileset, RPG::CommonEvent] +
                   [RPG::System, RPG::System::Words, RPG::System::TestBattler] +
                   [RPG::AudioFile,RPG::Map, RPG::MapInfo, RPG::Event] +
                   [RPG::Event::Page, RPG::Event::Page::Condition] +
                   [RPG::Event::Page::Graphic, RPG::MoveRoute] +
                   [RPG::MoveCommand, Table, Color, Tone]
  @@pending_objects = []
  @@top_object_key = 0

  def self.dump(obj, io)
    @@io = io
    @@top_string += self.queue_dump_object(obj)
    self.start_dump
    self.write_dump
    self.reset
  end
  
  def self.load(io)
    @@io = io
    self.build_object_table
    self.link_objects
    object = @@symbols[@@top_object_key][0]
    self.reset
    return object
  end
  
  def self.build_object_table
    objects = @@io.read().split("\n")
    objects.each {|item|
      case item
      when /\\#([0-9]+)\s-#(.+)/ #Numeric
        key = Integer($1)
        if @@symbols.has_key?(key)
          raise TypeError, "Duplicate object declaration: #{key}"
        end
        number = $2
        case number
        when /\A-?[0-9]+\Z/ #integer
          number = Integer(number)
        when /\A-?[0-9]+\.[0-9]+\Z/ #float
          number = Float(number)
        else
          raise TypeError, "Bad Numeric format: #{number}"
        end
        @@symbols[key] = [number, item]
      when /\\#([0-9]+)\s"(.*)/ #String
        key = Integer($1)
        if @@symbols.has_key?(key)
          raise TypeError, "Duplicate object declaration: #{key}"
        end
        string = $2
        @@symbols[key] = [string, item]
      when /\\#([0-9]+)\s\[(.*)/ #Array
        key = Integer($1)
        if @@symbols.has_key?(key)
          raise TypeError, "Duplicate object declaration: #{key}, #{item}"
        end
        array = $2.split(",")
        @@symbols[key] = [array, item]
        @@pending_objects.push(key) if !array.empty?
      when /\\#([0-9]+)\s\{(.*)/ #Hash
        key = Integer($1)
        if @@symbols.has_key?(key)
          raise TypeError, "Duplicate object declaration: #{key}"
        end
        items = $2.split(",")
        hash = {}
        items.each {|pair|
          pair_array = pair.split("=>")
          hash[pair_array[0]] = pair_array[1]
        }
        @@symbols[key] = [hash, item]
        @@pending_objects.push(key)
      when /\\#([0-9]+)\s\/-(.)(.*)/
        key = Integer($1)
        if @@symbols.has_key?(key)
          raise TypeError, "Duplicate object declaration: #{key}"
        end
        type = $2
        extra = $3
        case type
        when /T/
          @@symbols[key] = [true, item]
        when /F/
          @@symbols[key] = [false, item]
        when /N/
          @@symbols[key] = [nil, item]
        when /C/
          case extra
          when /([^\s]+?)\s\{(.*)/
            klasses = $1.split("::")
            if Kernel.const_defined?(klasses[0].to_sym)
              klass = Kernel.const_get(klasses[0].to_sym)

            else
              raise TypeError, "No class defined: #{klasses[0]} "
            end
            if klasses.size > 1
              klasses.each_index {|index|
                next if index == 0
                klass = klass.const_get(klasses[index].to_sym)
              }
            end
            klass_obj = klass.allocate()
            @@symbols[key] = [klass_obj, item]
            @@pending_objects.push(key)
          else
            raise TypeError, "Invalad class declaration"
          end
        else
          raise TypeError, "Unrecognized type declaration: #{type}"
        end
      when /\\\^\s\/#([0-9]+)/
        @@top_object_key = Integer($1)
      else
        unless item == ""
          raise TypeError, "Unrecognized object declaration: #{item}"
        end
      end
    } 
  end
  
  def self.link_objects
    @@pending_objects.each {|obj_key|
      obj = @@symbols[obj_key][0]
      declaration = @@symbols[obj_key][1]
      if obj.is_a?(Array)
        new_array = []
        obj.each {|item|
          case item
          when /\/#([0-9]+)/
            key = Integer($1)
            new_array.push(@@symbols[key][0])
          else
            raise TypeError, "Unrecognized item link: #{item}"
          end
        }
        obj.replace(new_array)
      elsif obj.is_a?(Hash)
        new_hash = {}
        obj.each_pair {|key, value|
          case key
          when /\/#([0-9]+)/
            new_key = @@symbols[Integer($1)][0]
          else
            raise TypeError, "Unrecognized item link: #{key}"
          end
          case value
          when /\/#([0-9]+)/
            new_value = @@symbols[Integer($1)][0]
          else
            raise TypeError, "Unrecognized item link: #{value}"
          end
          new_hash[new_key] = new_value
        }
        obj.replace(new_hash)
      else
        case declaration
        when /[^\s]+?\s\{(.*)/
          items = $1.split(",")
          items.each {|item|
            pair = item.split("=>")
            variable = "@" + pair[0].strip
            case pair[1]
            when /\/#([0-9]+)/
              key = Integer($1)
            else
              raise TypeError, "Unrecognized item link: #{pair[1]}"
            end
            obj.instance_variable_set(variable.to_sym, @@symbols[key][0])
          }
        else
        end
      end
    }
  end
  
  def self.reset
    @@io = nil
    @@symbols = {}
    @@strings = {}
    @@stack = []
    @@top_string = "\\^ "
    @@sym_count = 0
    @@pending_objects = []
    @@top_object_key = 0
  end
  
  def self.start_dump
    while !@@stack.empty?
      self.dump_object(@@stack.shift)
    end
  end
  
  def self.write_dump
    objects = @@symbols.sort {|a, b| a[1][1]<=>b[1][1]}
    object_strings = []
    objects.each {|value| object_strings.push(value[1][2])}
    object_strings.each {|string|
      @@io.write(string + "\n")
    }
    @@io.write(@@top_string + "\n")
  end
  
  def self.queue_dump_object(obj)
    flag = false
    for klass in @@good_objects
      if obj.is_a?(klass)
        flag = true
        break
      end
    end
    if !flag
      raise TypeError, "Can't dump #{obj.class.to_s}"
    end
    if obj.is_a?(FalseClass)
      result = self.dump_false_object(obj)
    elsif obj.is_a?(TrueClass)
      result = self.dump_true_object(obj)
    elsif obj.is_a?(NilClass)
      result = self.dump_nil_object(obj)
    elsif obj.is_a?(String)
      result = self.dump_string_object(obj)
    elsif obj.is_a?(Numeric)
      result = self.dump_numeric_object(obj)
    elsif obj.is_a?(Array)
      result = self.queue_dump_array_object(obj)
    elsif obj.is_a?(Hash)
      result = self.queue_dump_hash_object(obj)
    else
      result = self.queue_dump_nonstandard_object(obj)
    end
    return result
  end
  
  def self.dump_object(obj)
    if obj.is_a?(Array)
      self.dump_array_object(obj)
    elsif obj.is_a?(Hash)
      self.dump_hash_object(obj)
    else
      self.dump_nonstandard_object(obj)
    end
  end
  
  def self.dump_true_object(obj)
    if !@@symbols.has_key?(obj.object_id)
      return self.enter_obj(obj, "/-T")
    end
    return "/##{@@symbols[obj.object_id][1]}"
  end
  
  def self.dump_false_object(obj)
    if !@@symbols.has_key?(obj.object_id)
      return self.enter_obj(obj, "/-F")
    end
    return "/##{@@symbols[obj.object_id][1]}"
  end
  
  def self.dump_nil_object(obj)
    if !@@symbols.has_key?(obj.object_id)
      return self.enter_obj(obj, "/-N")
    end
    return "/##{@@symbols[obj.object_id][1]}"
  end
  
  def self.dump_string_object(obj)
    if !@@strings.has_key?(obj)
      @@strings[obj] = obj.object_id
      return self.enter_obj(obj, "\"" + obj)
    end
    return "/##{@@symbols[@@strings[obj]][1]}"
  end
  
  def self.dump_numeric_object(obj)
    if !@@symbols.has_key?(obj.object_id)
      return self.enter_obj(obj, "-##{obj.to_s}")
    end
    return "/##{@@symbols[obj.object_id][1]}"
  end
  
  def self.queue_dump_array_object(obj)
    if !@@symbols.has_key?(obj.object_id)
      str = "["
      @@stack.push(obj)
      return self.enter_obj(obj, str)
    end
    return "/##{@@symbols[obj.object_id][1]}"
  end
  
  def self.dump_array_object(obj)
    str = @@symbols[obj.object_id][2]
    i = 0
    obj.each {|value|
        str += self.queue_dump_object(value)
        str += "," if !(i + 1 >= obj.size)
        i += 1
    }
    @@symbols[obj.object_id][2] = str
  end
  
  def self.queue_dump_hash_object(obj)
    if !@@symbols.has_key?(obj.object_id)
      str = "{"
      @@stack.push(obj)
      return self.enter_obj(obj, str)
    end
    return "/##{@@symbols[obj.object_id][1]}"
  end
 
  def self.dump_hash_object(obj)
    str = @@symbols[obj.object_id][2]
    i = 0
    obj.each_pair {|key, value|
        str += (self.queue_dump_object(key) + "=>" + 
                self.queue_dump_object(value))
        str += "," if !(i + 1 >= obj.size)
        i += 1
    }
    @@symbols[obj.object_id][2] = str
  end
 
  def self.queue_dump_nonstandard_object(obj)
    if !@@symbols.has_key?(obj.object_id)
      str = "/-C #{obj.class.to_s} {"
      @@stack.push(obj)
      return self.enter_obj(obj, str)
    end
    return "/##{@@symbols[obj.object_id][1]}"
  end
  
  def self.dump_nonstandard_object(obj)
    str = @@symbols[obj.object_id][2]
    if obj.class.method_defined?("_rmpy_dump")
      str += "/-U " + obj._rmpy_dump
    else
      i = 0
      instance_variables = obj.instance_variables
      instance_variables.each {|value|
        str += (value.to_s.gsub("@", "") + "=>" + 
          self.queue_dump_object(obj.instance_variable_get(value)))
        str += "," if !(i + 1 >= instance_variables.size)
        i += 1
      }
    end
    @@symbols[obj.object_id][2] = str
  end
 
  def self.enter_obj(obj, str)
    key = obj.object_id
    str = "\\##{@@sym_count} " + str
    @@symbols[key] = [obj, @@sym_count, str]
    @@sym_count += 1
    return "/##{@@sym_count - 1}"
  end

end
