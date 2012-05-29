load 'data.rb'

module ARC

	module Data
	
		HEADER = "ARCD"
		VERSION = "\x01\x00" # 1.0
		
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
		
		UNBOUND_IDENTITY = Object.instance_method(:object_id)		
		
		@@io = nil
		@@strings = [nil]
		@@arrays = [nil]
		@@hashes = [nil]
		@@objects = [nil]
		@@class_path_redirects = {}
		
		def self.dump(io, obj, redirects = {})
			@@class_path_redirects = redirects
			@@io = io
			@@io.write(HEADER)
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
			header = @@io.read(4)
			raise "Error: #{self} header mismatch! Expected: #{HEADER.inspect} Found: \"#{header.inspect}" if HEADER != header
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
			@@strings = [nil]
			@@arrays = [nil]
			@@hashes = [nil]
			@@objects = [nil]
			@@class_path_redirects = {}
		end
  
		def self.__get_class_path(name)
			return (@@class_path_redirects.has_key?(name) ? @@class_path_redirects[name] : name)
		end
		
		def self.__get_class_object(class_path)
			classes = class_path.split('::')
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
			return classe
		end

		def self.__try_map_equality(data, obj)
			index = data.index(obj)
			if index == nil
				self.__dump_int32(data.size)
				data.push(obj)
				return true
			end
			self.__dump_int32(index)
			return false
		end

		def self.__try_map_identity(data, obj)
			index = nil
			data.each_index {|i|
				if UNBOUND_IDENTITY.bind(data[i]).call == UNBOUND_IDENTITY.bind(obj).call
					index = i
					break
				end
			}
			if index == nil
				self.__dump_int32(data.size)
				data.push(obj)
				return true
			end
			self.__dump_int32(index)
			return false
		end

		def self.__map(data, obj)
			data.push(obj)
		end

		def self.__find_mapped(data, id)
			return (id < data.size ? data[id] : nil)
		end
		
		def self.__dump_int32(obj)
			@@io.write([obj].pack('V'))
		end

		def self.__load_int32
			return @@io.read(4).unpack('V')[0]
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
			@@io.write([obj].pack('e'))
		end
		
		def self._dump_string(obj)
			@@io.write(TYPES[String])
			return if !self.__try_map_equality(@@strings, obj) # abort if object has already been mapped
			self.__dump_int32(obj.size)
			@@io.write(obj) if obj.size > 0
		end
		
		def self._dump_array(obj)
			@@io.write(TYPES[Array])
			return if !self.__try_map_identity(@@arrays, obj) # abort if object has already been mapped
			self.__dump_int32(obj.size)
			obj.each {|value| self._dump(value)}
		end
		
		def self._dump_hash(obj)
			@@io.write(TYPES[Hash])
			return if !self.__try_map_identity(@@hashes, obj) # abort if object has already been mapped
			self.__dump_int32(obj.size)
			obj.each_pair {|key, value| self._dump(key); self._dump(value)}
		end
		
		def self._dump_object(obj)
			@@io.write(TYPES[Object])
			self._dump_string(self.__get_class_path(obj.class.name)) # first the string path because this is required to load the object
			return if !self.__try_map_identity(@@objects, obj) # abort if object has already been mapped
			if obj.respond_to?(:_arc_dump)
				data = obj._arc_dump
				self.__dump_int32(data.size)
				@@io.write(data)
			else
				variables = obj.instance_variables
				self.__dump_int32(variables.size)
				variables.each {|variable|
					self._dump_string(variable.to_s.gsub('@', ''))
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
			return @@io.read(4).unpack('e')[0]
		end
		
		def self._load_string
			id = self.__load_int32
			obj = self.__find_mapped(@@strings, id)
			return obj.clone if obj != nil
			size = self.__load_int32
			obj = @@io.read(size)
			self.__map(@@strings, obj)
			return obj
		end
		
		def self._load_array
			id = self.__load_int32
			obj = self.__find_mapped(@@arrays, id)
			return obj if obj != nil
			size = self.__load_int32
			obj = []
			self.__map(@@arrays, obj)
			size.times {obj.push(self._load)}
			return obj
		end
		
		def self._load_hash
			id = self.__load_int32
			obj = self.__find_mapped(@@hashes, id)
			return obj if obj != nil
			size = self.__load_int32
			obj = {}
			self.__map(@@hashes, obj)
			# obj[key] can be evaluated after the second self._load, this makes sure the key is loaded first
			size.times {key = self._load; obj[key] = self._load}
			return obj
		end
		
		def self._load_object
			class_path = self._load
			obj = self.__find_mapped(@@objects, self.__load_int32)
			return obj if obj != nil
			classe = self.__get_class_object(class_path)
			size = self.__load_int32
			if classe.respond_to?(:_arc_load)
				obj = classe._arc_load(@@io.read(size))
				self.__map(@@objects, obj)
				return obj
			end
			obj = classe.allocate
			self.__map(@@objects, obj)
			size.times {obj.instance_variable_set(('@' + self._load), self._load)}
			return obj
		end
		
	end
	
end
