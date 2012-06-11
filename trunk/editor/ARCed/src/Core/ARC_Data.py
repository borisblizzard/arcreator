from struct import pack, unpack
import types

class ARC_Dump(object):
    
    _HEADER = "ARCD"
    _VERSION = "\x01\x00" # 1.0
    
    _TYPES = {
        "NoneClass" : chr(0x10),
        "FalseClass" : chr(0x11),
        "TrueClass" : chr(0x12),
        "Fixnum" : chr(0x21),
        "Bignum" : chr(0x22),
        "Float" : chr(0x23),
        "String" : chr(0x30),
        "Array" : chr(0x40),
        "Hash" : chr(0x41),
        "Object" : chr(0x00)
        }
    
    _io = None
    _strings = [None]
    _arrays = [None]
    _hashes = [None]
    _objects = [None]
    _class_path_redirects = {}
    _extended_namespace = {}
    
    @staticmethod
    def dump(io, obj, redirects = {}):
        global _class_path_redirects
        global _io
        _class_path_redirects = redirects
        _io = io
        _io.write(ARC_Dump._HEADER)
        _io.write(ARC_Dump._VERSION)
        try:
            ARC_Dump._dump(obj)
        except Exception:
            try:
                print "stream position: %s" % _io.tell()
            except Exception:
                pass
            raise
        ARC_Dump._reset()
    
    
    @staticmethod
    def load(io, redirects = {}, extended_namespace={}):
        ARC_Dump._class_path_redirects = redirects
        extended_namespace.update(globals())
        ARC_Dump._extended_namespace = dict(extended_namespace)
        extended_namespace = {}
        ARC_Dump._io = io
        header = ARC_Dump._io.read(4)
        if ARC_Dump._HEADER != header:
            raise TypeError("Error: header mismatch! Expected: %s Found: %s" %(repr(ARC_Dump._HEADER), repr(header)))
        version = ARC_Dump._io.read(2)
        if ARC_Dump._VERSION != version:
            raise TypeError("Error: version mismatch! Expected: %s Found: %s" %(repr(ARC_Dump._VERSION), repr(version)))
        try:
            data = ARC_Dump._load()
        except Exception:
            try:
                print "stream position: %s" % ARC_Dump._io.tell()
            except Exception:
                pass
            raise
        ARC_Dump._reset()
        return data
    
    
    @staticmethod
    def _reset():
        ARC_Dump._io = None
        ARC_Dump._strings = [None]
        ARC_Dump._arrays = [None]
        ARC_Dump._hashes = [None]
        ARC_Dump._objects = [None]
        ARC_Dump._class_path_redirects = {}
        ARC_Dump._extended_namespace = {}
    

    @staticmethod
    def __get_class_path(name):
        if ARC_Dump._class_path_redirects.has_key(name):
            return ARC_Dump._class_path_redirects[name]
        else: 
            return name
    
    
    @staticmethod
    def __get_class_object(class_path):
        classes = class_path.split("::")
        if not ARC_Dump._extended_namespace.has_key(classes[0]):
            raise TypeError("Class not defined: %s" % classes[0])	
        classe = ARC_Dump._extended_namespace[classes.pop(0)]
        for c in classes:
            if not classe.__dict__.has_key(c):
                raise TypeError("Class not defined: %s" % c)
            classe = classe.__dict__[c]
        return classe
    

    @staticmethod
    def __try_map_equality(data, obj):
        index = data.index(obj)
        if index == None:
            ARC_Dump.__dump_int32(len(data))
            data.append(obj)
            return True
        ARC_Dump.__dump_int32(index)
        return False
    

    @staticmethod
    def __try_map_identity(data, obj):
        index = None
        for i in xrange(len(data)):
            if data[i] is obj:
                index = i
                break
        if index == None:
            ARC_Dump.__dump_int32(len(data))
            data.append(obj)
            return True
        ARC_Dump.__dump_int32(index)
        return False
    

    @staticmethod
    def __map(data, obj):
        data.append(obj)
    

    @staticmethod
    def __find_mapped(data, id_num):
        if id_num < len(data):
            return data[id_num]
        else:
            return None
    
    
    @staticmethod
    def __dump_int32(obj):
        ARC_Dump._io.write(pack("<I", obj))
    

    @staticmethod
    def __load_int32():
        return unpack("<I", ARC_Dump._io.read(4))[0]
    
    
    @staticmethod
    def _dump(obj):
        if obj == None:
            return ARC_Dump._dump_none(obj)
        if obj == False:
            return ARC_Dump._dump_false(obj) 
        if obj == True:
            return ARC_Dump._dump_true(obj)
        if isinstance(obj, types.IntType):
            return ARC_Dump._dump_fixnum(obj)
        if isinstance(obj, types.LongType):
            return ARC_Dump._dump_bignum(obj)
        if isinstance(obj, types.FloatType):
            return ARC_Dump._dump_float(obj)
        if isinstance(obj, types.StringTypes):
            return ARC_Dump._dump_string(obj)
        if isinstance(obj, (types.ListType, types.TupleType)):
            return ARC_Dump._dump_array(obj)
        if isinstance(obj, types.DictType):
            return ARC_Dump._dump_hash(obj)
        if isinstance(obj, object):
            return ARC_Dump._dump_object(obj)
        raise TypeError("Error: %s cannot be dumped!" % obj.__class__)
    
    @staticmethod
    def _load():
        type_id = ARC_Dump._io.read(1)
        if type_id == ARC_Dump._TYPES["NoneClass"]:
            return ARC_Dump._load_none()
        elif type_id == ARC_Dump._TYPES["FalseClass"]:
            return ARC_Dump._load_false()
        elif type_id == ARC_Dump._TYPES["TrueClass"]:
            return ARC_Dump._load_true()
        elif type_id == ARC_Dump._TYPES["Fixnum"]:
            return ARC_Dump._load_fixnum()
        elif type_id == ARC_Dump._TYPES["Bignum"]:
            return ARC_Dump._load_bignum()
        elif type_id == ARC_Dump._TYPES["Float"]:
            return ARC_Dump._load_float()
        elif type_id == ARC_Dump._TYPES["String"]:
            return ARC_Dump._load_string()
        elif type_id == ARC_Dump._TYPES["Array"]:
            return ARC_Dump._load_array()
        elif type_id == ARC_Dump._TYPES["Hash"]:
            return ARC_Dump._load_hash()
        elif type_id == ARC_Dump._TYPES["Object"]:
            return ARC_Dump._load_object()
        
        raise TypeError("Error: Unknown type 0x%02X detected!" % ord(type_id))
    
    
    @staticmethod
    def _dump_none(obj):
        ARC_Dump._io.write(ARC_Dump._TYPES["NoneClass"])
    

    @staticmethod
    def _dump_false(obj):
        ARC_Dump._io.write(ARC_Dump._TYPES["FalseClass"])
    

    @staticmethod
    def _dump_true(obj):
        ARC_Dump._io.write(ARC_Dump._TYPES["TrueClass"])
    
    
    @staticmethod
    def _dump_fixnum(obj):
        ARC_Dump._io.write(ARC_Dump._TYPES["Fixnum"])
        ARC_Dump.__dump_int32(obj)
    
    
    @staticmethod
    def _dump_bignum(obj):
        ARC_Dump._io.write(ARC_Dump._TYPES["Bignum"])
        ARC_Dump.__dump_int32(obj) # our C++ implementation uses a "long" of 32 bit
    
    
    @staticmethod
    def _dump_float(obj):
        ARC_Dump._io.write(ARC_Dump._TYPES["Float"])
        ARC_Dump._io.write(pack("<f", obj))
    
    
    @staticmethod
    def _dump_string(obj):
        ARC_Dump._io.write(ARC_Dump._TYPES["String"])
        if not ARC_Dump.__try_map_equality(ARC_Dump._strings, obj): # abort if object has already been mapped
            return
        ARC_Dump.__dump_int32(len(obj))
        ARC_Dump._io.write(obj)
    
    
    @staticmethod
    def _dump_array(obj):
        ARC_Dump._io.write(ARC_Dump._TYPES["Array"])
        if not ARC_Dump.__try_map_identity(ARC_Dump._arrays, obj): # abort if object has already been mapped
            return 
        ARC_Dump.__dump_int32(len(obj))
        for value in obj:
            ARC_Dump._dump(value)
    
    
    @staticmethod
    def _dump_hash(obj):
        ARC_Dump._io.write(ARC_Dump._TYPES["Hash"])
        if not ARC_Dump.__try_map_identity(ARC_Dump._hashes, obj): # abort if object has already been mapped
            return 
        ARC_Dump.__dump_int32(len(obj))
        for key, value in obj.items():
            ARC_Dump._dump(key)
            ARC_Dump._dump(value)
        
    
    @staticmethod
    def _request_instance_variables(obj):
        if hasattr(obj, "_arc_instance_variables"):
            return obj._arc_instance_variables
        result = []
        for key, value in obj.__dict__.items():
            if key[0] != "_":
                if not isinstance(value, (types.FunctionType, types.ClassType, types.MethodType, 
                                          types.ModuleType, types.SliceType, types.LambdaType, 
                                          types.GeneratorType)):
                    result.append(key)
        return result
    
    @staticmethod
    def _dump_object(obj):
        ARC_Dump._io.write(ARC_Dump._TYPES["Object"])
        if hasattr(obj, "_arc_class_path"):
            klass_path = obj._arc_class_path
        else:
            klass_path = "%s::%s" % (obj.__class__.__module__, obj.__class__.__name__)
        ARC_Dump._dump_string(ARC_Dump.__get_class_path(klass_path)) # first the string path because this is required to load the object
        if not ARC_Dump.__try_map_identity(_objects, obj): # abort if object has already been mapped
            return
        if hasattr(obj, "_arc_dump"):
            data = obj._arc_dump()
            ARC_Dump.__dump_int32(len(data))
            _io.write(data)
        else:
            if hasattr(obj, "_arc_exclude"):
                excludes = obj._arc_exclude
            else:
                excludes = []
            variables = list(set(ARC_Dump._request_instance_variables(obj)) - set(excludes))
            ARC_Dump.__dump_int32(len(variables))
            variables.sort()
            for variable in variables:
                ARC_Dump._dump_string(variable)
                ARC_Dump._dump(getattr(obj, variable))
        
    
    
    @staticmethod
    def _load_none():
        return None
    

    @staticmethod
    def _load_false():
        return False
    

    @staticmethod
    def _load_true():
        return True
    
    
    @staticmethod
    def _load_fixnum():
        return ARC_Dump.__load_int32()
    
    
    @staticmethod
    def _load_bignum():
        return ARC_Dump.__load_int32() # our C++ implementation uses a "long" of 32 bit
    
    
    @staticmethod
    def _load_float():
        return unpack("<f", _io.read(4))[0]
    
    
    @staticmethod
    def _load_string():
        id_num = ARC_Dump.__load_int32()
        obj = ARC_Dump.__find_mapped(ARC_Dump._strings, id_num)
        if obj != None:
            return obj
        size = ARC_Dump.__load_int32()
        obj = ARC_Dump._io.read(size)
        ARC_Dump.__map(ARC_Dump._strings, obj)
        return obj
    
    
    @staticmethod
    def _load_array():
        id_num = ARC_Dump.__load_int32()
        obj = ARC_Dump.__find_mapped(ARC_Dump._arrays, id_num)
        if obj != None:
            return obj
        size = ARC_Dump.__load_int32()
        obj = []
        ARC_Dump.__map(ARC_Dump._arrays, obj)
        for i in xrange(size):
            obj.append(ARC_Dump._load())
        return obj
    
    
    @staticmethod
    def _load_hash():
        id_num = ARC_Dump.__load_int32()
        obj = ARC_Dump.__find_mapped(ARC_Dump._hashes, id_num)
        if obj != None:
            return obj
        size = ARC_Dump.__load_int32()
        obj = {}
        ARC_Dump.__map(ARC_Dump._hashes, obj)
        for i in xrange(size):
            # obj[key] can be evaluated after the second ARC_Dump._load, this makes sure the key is loaded first
            key = ARC_Dump._load()
            obj[key] = ARC_Dump._load()
        return obj
    
    
    @staticmethod
    def _load_object():
        class_path = ARC_Dump._load()
        obj = ARC_Dump.__find_mapped(ARC_Dump._objects, ARC_Dump.__load_int32())
        if obj != None:
            return obj
        classe = ARC_Dump.__get_class_object(class_path)
        size = ARC_Dump.__load_int32()
        if hasattr(classe, "_arc_load"):
            obj = classe._arc_load(ARC_Dump._io.read(size))
            ARC_Dump.__map(ARC_Dump._objects, obj)
            return obj
        obj = classe.__new__(classe)
        ARC_Dump.__map(ARC_Dump._objects, obj)
        for i in xrange(size):
            setattr(obj, ARC_Dump._load(), ARC_Dump._load())
        return obj
    
