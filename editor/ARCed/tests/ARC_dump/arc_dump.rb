load 'data.rb'
require 'msgpack'

module ARC_Dump

  @@io = nil
  @@symbols = {}
  @@strings = {}
  @@ids = {}
  @@stack = []
  @@finaldump = {}
  @@sym_count = 0
  @@pending_objects = []
  @@post_load_objects = []
  @@class_path_redirects = {}

  def self.dump(obj, io, redirects = {})
    @@class_path_redirects = redirects
    @@io = io
    self.queue_dump_object(obj)
    self.start_dump
    self.write_dump
    self.reset
  end
  
  def self.load(io, redirects = {})
    @@class_path_redirects = redirects
    @@io = io
    self.build_object_table
    self.link_objects
    self.call_arc_post_load
    object = @@symbols[0]
    case object[0]
    when 0..4 #False, True, Nil, String, Numeric
      return_obj = object[1]
    when 5..7 #Array, Hash, Class
      return_obj = object[1][0]
    else
      return_obj = nil
    end
    self.reset
    return return_obj
  end
  
  def self.build_object_table
    load_string = @@io.read()
    objects = MessagePack.unpack(load_string)
    objects.each {|key, item|
      @@symbols[key] = item 
      case item[0]
      when 0..4 #False, True, Nil, String, Numeric
        next
      when 5..6 #Array, Hash
        @@pending_objects.push(key) if !item[1].empty?
      when 7    #Class
        if @@class_path_redirects.has_key?(item[1][0])
          klass_path = @@class_path_redirects[item[1][0]]
        else
          klass_path = item[1][0]
        end
        klasses = klass_path.split("::")
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
        item[1][0] = klass_obj
        @@pending_objects.push(key)
      else
        raise TypeError, "Unrecognized object declaration: #{item}"
      end
    } 
  end
  
  def self.link_objects
    @@pending_objects.each {|obj_key|
      obj = @@symbols[obj_key]
      case obj[0]
      when 5
        new_array = obj[1][0]
        obj[1][1].each {|item|
          case item[0]
          when 0 #actualy object
            new_array.push(item[1])
          when 1 #link to array, hash, or user object
            new_array.push(@@symbols[item[1]][1][0])
          when 2 #string
            new_array.push(@@symbols[item[1]][1])
          end
        }
      when 6
        new_hash = obj[1][0]
        obj[1][1].each {|pair|
          case pair[0][0]
          when 0 #actualy object
            key = pair[0][1]
          when 1 #link to array, hash, or user object
            key = @@symbols[pair[0][1]][1][0]
          when 2 #string
            key = @@symbols[pair[0][1]][1]
          end
          case pair[1][0]
          when 0 #actualy object
            value = pair[1][1]
          when 1 #link to array, hash, or user object
            value = @@symbols[pair[1][1]][1][0]
          when 2 #string
            value = @@symbols[pair[1][1]][1]
          end
          new_hash[key] = value
        }
      when 7
        klass_obj = obj[1][0]
        if klass_obj.class.method_defined?("_arc_load")
          klass_obj._arc_load(obj[1][1])
        else
          obj[1][1].each {|pair|
            variable = pair[0]
            case pair[1][0]
            when 0 #actualy object
              value = pair[1][1]
            when 1 #link to array, hash, or user object
              value = @@symbols[pair[1][1]][1][0]
            when 2 #string
              value = @@symbols[pair[1][1]][1]
            end
            klass_obj.instance_variable_set(("@" + variable.strip).to_sym, value)
          }
        end
        if klass_obj.class.method_defined?("_post_arc_load")
          @@post_load_objects.push(klass_obj)
        end
      end
    }
  end
  
  def self.call_arc_post_load
    @@post_load_objects.each {|obj|
      obj._post_arc_load
    }
  end
  
  def self.reset
    @@io = nil
    @@symbols = {}
    @@strings = {}
    @@ids = {}
    @@stack = []
    @@finaldump = {}
    @@sym_count = 0
    @@pending_objects = []
    @@class_path_redirects = {}
  end
  
  def self.start_dump
    while !@@stack.empty?
      self.dump_object(@@stack.shift)
    end
  end
  
  def self.write_dump
    dump_string = @@finaldump.to_msgpack
    @@io.write(dump_string)
  end
  
  def self.queue_dump_object(obj)
    if obj.is_a?(FalseClass)
      result = self.dump_false_object(obj)
    elsif obj.is_a?(TrueClass)
      result = self.dump_true_object(obj)
    elsif obj.is_a?(NilClass)
      result = self.dump_nil_object(obj)
    elsif obj.is_a?(Numeric)
      result = self.dump_numeric_object(obj)
    elsif obj.is_a?(String)
      result = self.dump_string_object(obj)
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
    return [0, true]
  end
  
  def self.dump_false_object(obj)
    return [0, false]
  end
  
  def self.dump_nil_object(obj)
    return [0, nil]
  end
  
  def self.dump_numeric_object(obj)
    return [0, obj]
  end
  
  def self.dump_string_object(obj)
    if !@@strings.has_key?(obj)
      @@strings[obj] = obj.object_id
      dump_array = self.enter_obj(obj)
      dump_array[0], dump_array[1] = 4, obj
    end
    return [2, @@ids[@@strings[obj]]]
  end
  
  def self.queue_dump_array_object(obj)
    if !@@symbols.has_key?(obj.object_id)
      @@stack.push(obj)
      dump_array = self.enter_obj(obj)
      dump_array[0], dump_array[1] = 5, [[],[]]
    end
    return [1, @@ids[obj.object_id]]
  end
  
  def self.dump_array_object(obj)
    dump_array = @@symbols[obj.object_id][1]
    obj.each {|value| 
      dump_array[1][1].push(self.queue_dump_object(value))
    }
  end
  
  def self.queue_dump_hash_object(obj)
    if !@@symbols.has_key?(obj.object_id)
      @@stack.push(obj)
      dump_array = self.enter_obj(obj)
      dump_array[0], dump_array[1] = 6, [{}, []]
    end
    return [1, @@ids[obj.object_id]]
  end
 
  def self.dump_hash_object(obj)
    dump_array = @@symbols[obj.object_id][1]
    obj.each_pair {|key, value|
      pair = [self.queue_dump_object(key), self.queue_dump_object(value)]
      dump_array[1][1].push(pair)
    }
  end
 
  def self.queue_dump_nonstandard_object(obj)
    if !@@symbols.has_key?(obj.object_id)
      @@stack.push(obj)
      dump_array = self.enter_obj(obj)
      if @@class_path_redirects.has_key?(obj.class.to_s)
        klass_path = @@class_path_redirects[obj.class.to_s]
      else
        klass_path = obj.class.to_s
      end
      dump_array[0], dump_array[1] = 7, [klass_path,[]]
    end
    return [1, @@ids[obj.object_id]]
  end
  
  def self.dump_nonstandard_object(obj)
    dump_array = @@symbols[obj.object_id][1]
    if obj.class.method_defined?("_prep_arc_dump")
      obj._prep_arc_dump
    end
    if obj.class.method_defined?("_arc_dump")
      dump_array[1][1] = obj._arc_dump
    else
      if obj.class.method_defined?("_arc_exclude")
        excludes = obj._arc_exclude
      else
        excludes = []
      end
      instance_variables = obj.instance_variables
      instance_variables.each {|value|
        name = value.to_s.gsub("@", "")
        next if excludes.include?(name)
        pair = [name, self.queue_dump_object(obj.instance_variable_get(value))]
        dump_array[1][1].push(pair)
      }
    end
  end
 
  def self.enter_obj(obj)
    key = obj.object_id
    dump_array = [nil,nil]
    @@symbols[key] = [obj, dump_array]
    @@ids[key] = @@sym_count
    @@finaldump[@@sym_count] = dump_array
    @@sym_count += 1
    return dump_array
  end

end
