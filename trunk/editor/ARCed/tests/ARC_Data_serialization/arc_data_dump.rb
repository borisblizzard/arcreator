load 'data.rb'

module ARC

	module Data
	
		VERSION = "\x01\x00"
		
		DEBUG_DISABLE_STRING_MAPPING = false
		DEBUG_DISABLE_OBJECT_MAPPING = false
		
		TYPES = {
			NilClass => 0x10.chr,
			FalseClass => 0x11.chr,
			TrueClass => 0x12.chr,
			Fixnum => 0x21.chr,
			Bignum => 0x22.chr,
			Float => 0x23.chr,
			String => 0x30.chr,
			Array => 0x40.chr,
			Hash => 0x41.chr,
			Object => 0x00.chr
		}
		
		@@io = nil
		@@objects = [nil]
		@@class_path_redirects = {}
		
		def self.dump(io, obj, redirects = {})
			@@class_path_redirects = redirects
			@@io = io
			@@io.write(VERSION)
			begin
				self._dump(obj)
			rescue
				puts "stream position: #{@@io.tell}" rescue nil
				raise
			end
			self._reset
		end
		
		def self.load(io, redirects = {})
			@@class_path_redirects = redirects
			@@io = io
			version = @@io.read(2)
			raise "Error: #{self} version mismatch! Expected: #{VERSION.inspect} Found: #{version.inspect}" if VERSION != version
			begin
				data = self._load
			rescue
				puts "stream position: #{@@io.tell}" rescue nil
				raise
			end
			self._reset
			return data
		end
		
		def self._reset
			@@io = nil
			@@objects = [nil]
			@@class_path_redirects = {}
		end
  
		def self.__get_class_path(name)
			return (@@class_path_redirects.has_key?(name) ? @@class_path_redirects[name] : name)
		end
		
		def self.__try_map_object(obj)
			index = @@objects.index(obj)
			if index == nil
				self.__dump_int32(@@objects.size)
				@@objects.push(obj)
				return true
			end
			self.__dump_int32(index)
			return false
		end

		def self.__map_object(obj)
			@@objects.push(obj)
		end

		def self.__find_mapped_object(id)
			return (id < @@objects.size ? @@objects[id] : nil)
		end
		
		def self.__dump_int32(obj)
			@@io.write([obj].pack("V"))
		end

		def self.__load_int32
			return @@io.read(4).unpack("V")[0]
		end

		def self._dump(obj)
			return self._dump_nil(obj) if obj.is_a?(NilClass)
			return self._dump_false(obj) if obj.is_a?(FalseClass)
			return self._dump_true(obj) if obj.is_a?(TrueClass)
			return self._dump_fixnum(obj) if obj.is_a?(Fixnum)
			return self._dump_bignum(obj) if obj.is_a?(Bignum)
			return self._dump_float(obj) if obj.is_a?(Float)
			return self._dump_string(obj) if obj.is_a?(String)
			return self._dump_array(obj) if obj.is_a?(Array)
			return self._dump_hash(obj) if obj.is_a?(Hash)
			return self._dump_object(obj) if obj.is_a?(Object)
			raise "Error: #{obj.class} cannot be dumped!"
		end
		
		def self._load
			type = @@io.read(1)
			case type
			when TYPES[NilClass] then return self._load_nil
			when TYPES[FalseClass] then return self._load_false
			when TYPES[TrueClass] then return self._load_true
			when TYPES[Fixnum] then return self._load_fixnum
			when TYPES[Bignum] then return self._load_bignum
			when TYPES[Float] then return self._load_float
			when TYPES[String] then return self._load_string
			when TYPES[Array] then return self._load_array
			when TYPES[Hash] then return self._load_hash
			when TYPES[Object] then return self._load_object
			end
			raise "Error: Unknown type 0x%02X detected!" % type.ord
		end
		
		def self._dump_nil(obj)
			@@io.write(TYPES[NilClass])
		end

		def self._dump_false(obj)
			@@io.write(TYPES[FalseClass])
		end

		def self._dump_true(obj)
			@@io.write(TYPES[TrueClass])
		end
		
		def self._dump_fixnum(obj)
			@@io.write(TYPES[Fixnum])
			self.__dump_int32(obj)
		end
		
		def self._dump_bignum(obj)
			@@io.write(TYPES[Bignum])
			self.__dump_int32(obj) # our C++ implementation uses a "long" of 32 bit
		end
		
		def self._dump_float(obj)
			@@io.write(TYPES[Float])
			@@io.write([obj].pack("e"))
		end
		
		def self._dump_string(obj)
			@@io.write(TYPES[String])
			if obj.size > 0
				if !DEBUG_DISABLE_STRING_MAPPING && !DEBUG_DISABLE_OBJECT_MAPPING
					return if !self.__try_map_object(obj) # abort if object has already been mapped
				end
				self.__dump_int32(obj.size)
				@@io.write(obj)
			else
				self.__dump_int32(0)
			end
		end
		
		def self._dump_array(obj)
			@@io.write(TYPES[Array])
			if obj.size > 0
				if !DEBUG_DISABLE_OBJECT_MAPPING
					return if !self.__try_map_object(obj) # abort if object has already been mapped
				end
				self.__dump_int32(obj.size)
				obj.each {|value| self._dump(value)}
			else
				self.__dump_int32(0)
			end
		end
		
		def self._dump_hash(obj)
			@@io.write(TYPES[Hash])
			if obj.size > 0
				if !DEBUG_DISABLE_OBJECT_MAPPING
					return if !self.__try_map_object(obj) # abort if object has already been mapped
				end
				self.__dump_int32(obj.size)
				obj.each_pair {|key, value| self._dump(key); self._dump(value)}
			else
				self.__dump_int32(0)
			end
		end
		
		def self._dump_object(obj)
			@@io.write(TYPES[Object])
			self._dump_string(self.__get_class_path(obj.class.name)) # first the string path because this is required to load the object
			if !DEBUG_DISABLE_OBJECT_MAPPING
				return if !self.__try_map_object(obj) # abort if object has already been mapped
			end
			if obj.respond_to?("_arc_dump")
				data = obj._arc_dump
				self.__dump_int32(data.size)
				@@io.write(data)
			else
				variables = obj.instance_variables
				self.__dump_int32(variables.size)
				variables.each {|variable|
					self._dump_string(variable.to_s.gsub("@", ""))
					self._dump(obj.instance_variable_get(variable))
				}
			end
		end
		
		def self._load_nil
			return nil
		end

		def self._load_false
			return false
		end

		def self._load_true
			return true
		end
		
		def self._load_fixnum
			return self.__load_int32
		end
		
		def self._load_bignum
			return self.__load_int32 # our C++ implementation uses a "long" of 32 bit
		end
		
		def self._load_float
			return @@io.read(4).unpack("e")[0]
		end
		
		def self._load_string
			if !DEBUG_DISABLE_STRING_MAPPING && !DEBUG_DISABLE_OBJECT_MAPPING
				id = self.__load_int32
				return "" if id == 0
				obj = self.__find_mapped_object(id)
				return obj.clone if obj != nil
			end
			size = self.__load_int32
			obj = @@io.read(size)
			if !DEBUG_DISABLE_STRING_MAPPING && !DEBUG_DISABLE_OBJECT_MAPPING
				self.__map_object(obj)
			end
			return obj
		end
		
		def self._load_array
			if !DEBUG_DISABLE_OBJECT_MAPPING
				id = self.__load_int32
				return [] if id == 0
				obj = self.__find_mapped_object(id)
				return obj if obj != nil
			end
			size = self.__load_int32
			obj = []
			if !DEBUG_DISABLE_OBJECT_MAPPING
				self.__map_object(obj)
			end
			size.times {obj.push(self._load)}
			return obj
		end
		
		def self._load_hash
			if !DEBUG_DISABLE_OBJECT_MAPPING
				id = self.__load_int32
				return {} if id == 0
				obj = self.__find_mapped_object(id)
				return obj if obj != nil
			end
			size = self.__load_int32
			obj = {}
			if !DEBUG_DISABLE_OBJECT_MAPPING
				self.__map_object(obj)
			end
			size.times {key = self._load; obj[key] = self._load} # making sure key is always loaded first
			return obj
		end
		
		def self._load_object
			class_path = self._load
			if !DEBUG_DISABLE_OBJECT_MAPPING
				obj = self.__find_mapped_object(self.__load_int32)
				return obj if obj != nil
			end
			classes = class_path.split("::")
			if !Kernel.const_defined?(classes[0].to_sym)
				raise TypeError, "Class not defined: #{classes[0]}"
			end
			classe = Kernel.const_get(classes.shift.to_sym)
			classes.each {|c|
				if !classe.const_defined?(c.to_sym)
					raise TypeError, "Class not defined: #{c}"
				end
				classe = classe.const_get(c.to_sym)
			}
			size = self.__load_int32
			if classe.respond_to?("_arc_load")
				obj = classe._arc_load(@@io.read(size))
				if !DEBUG_DISABLE_OBJECT_MAPPING
					self.__map_object(obj)
				end
				return obj
			end
			obj = classe.allocate
			if !DEBUG_DISABLE_OBJECT_MAPPING
				self.__map_object(obj)
			end
			size.times {obj.instance_variable_set(("@" + self._load).to_sym, self._load)}
			return obj
		end
		
	end
	
end
