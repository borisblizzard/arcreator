from struct import pack, unpack
import types

class ARC_Data(object):

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
    def dump(io, obj, redirects={}):
        global _class_path_redirects
        global _io
        _class_path_redirects = redirects
        _io = io
        _io.write(ARC_Data._VERSION)
        try:
            ARC_Data._dump(obj)
        except Exception:
            try:
                print "stream position: %s" % _io.tell()
            except Exception:
                pass
            raise
        ARC_Data._reset()
    
    
    @staticmethod
    def load(io, redirects={}, extended_namespace={}):
        global _class_path_redirects
        global _io
        global _extended_namespace
        _class_path_redirects = redirects
        _extended_namespace = dict(extended_namespace.update(globals()))
        extended_namespace = {}
        _io = io
        version = _io.read(2)
        if ARC_Data._VERSION != version:
            raise "Error: version mismatch! Expected: %s Found: %s" %(repr(ARC_Data._VERSION), repr(version))
        try:
            data = ARC_Data._load()
        except Exception:
            try:
                print "stream position: %s" % _io.tell()
            except Exception:
                pass
            raise
        ARC_Data._reset()
        return data
    
    
    @staticmethod
    def _reset():
        global _io
        global _strings
        global _arrays
        global _hashes
        global _objects
        global _class_path_redirects
        global _extended_namespace
        _io = None
        _strings = [None]
        _arrays = [None]
        _hashes = [None]
        _objects = [None]
        _class_path_redirects = {}
        _extended_namespace = {}
    

    @staticmethod
    def __get_class_path(name):
        if _class_path_redirects.has_key(name):
            return _class_path_redirects[name]
        else: 
            return name
    
    
    @staticmethod
    def __get_class_object(class_path):
        classes = class_path.split("::")
        if not _extended_namespace.has_key(classes[0]):
            raise TypeError("Class not defined: %s" % classes[0])    
        classe = _extended_namespace[classes.pop(0)]
        for c in classes:
            if not classe.__dict__.has_key(c):
                raise TypeError("Class not defined: %s" % c)
            classe = classe.const_get(c.to_sym)
        return classe
    

    @staticmethod
    def __try_map(data, obj):
        index = data.index(obj)
        if index is None:
            ARC_Data.__dump_int32(len(data))
            data.append(obj)
            return True
        ARC_Data.__dump_int32(index)
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
        _io.write(pack("<I", obj))
    

    @staticmethod
    def __load_int32():
        return unpack("<I", _io.read(4))
    
    
    @staticmethod
    def _dump(obj):
        if obj is None:
            return ARC_Data._dump_none(obj)
        if obj is False:
            return ARC_Data._dump_false(obj) 
        if obj is True:
            return ARC_Data._dump_true(obj)
        if isinstance(obj, types.IntType):
            return ARC_Data._dump_fixnum(obj)
        if isinstance(obj, types.LongType):
            return ARC_Data._dump_bignum(obj)
        if isinstance(obj, types.FloatType):
            return ARC_Data._dump_float(obj)
        if isinstance(obj, types.StringTypes):
            return ARC_Data._dump_string(obj)
        if isinstance(obj, (types.ListType, types.TupleType)):
            return ARC_Data._dump_array(obj)
        if isinstance(obj, types.DictType):
            return ARC_Data._dump_hash(obj)
        if isinstance(obj, object):
            return ARC_Data._dump_object(obj)
        raise TypeError("Error: %s cannot be dumped!" % obj.__class__)
    
    @staticmethod
    def _load():
        type_id = _io.read(1)
        if type_id is ARC_Data._TYPES["NoneClass"]:
            return ARC_Data._load_none()
        elif type_id is ARC_Data._TYPES["FalseClass"]:
            return ARC_Data._load_false()
        elif type_id is ARC_Data._TYPES["TrueClass"]:
            return ARC_Data._load_true()
        elif type_id is ARC_Data._TYPES["Fixnum"]:
            return ARC_Data._load_fixnum()
        elif type_id is ARC_Data._TYPES["Bignum"]:
            return ARC_Data._load_bignum()
        elif type_id is ARC_Data._TYPES["Float"]:
            return ARC_Data._load_float()
        elif type_id is ARC_Data._TYPES["String"]:
            return ARC_Data._load_string()
        elif type_id is ARC_Data._TYPES["Array"]:
            return ARC_Data._load_array()
        elif type_id is ARC_Data._TYPES["Hash"]:
            return ARC_Data._load_hash()
        elif type_id is ARC_Data._TYPES["Object"]:
            return ARC_Data._load_object()
        
        raise "Error: Unknown type 0x%02X detected!" % ord(type_id)
    
    
    @staticmethod
    def _dump_none(obj):
        _io.write(ARC_Data._TYPES["NoneClass"])
    

    @staticmethod
    def _dump_false(obj):
        _io.write(ARC_Data._TYPES["FalseClass"])
    

    @staticmethod
    def _dump_true(obj):
        _io.write(ARC_Data._TYPES["TrueClass"])
    
    
    @staticmethod
    def _dump_fixnum(obj):
        _io.write(ARC_Data._TYPES["Fixnum"])
        ARC_Data.__dump_int32(obj)
    
    
    @staticmethod
    def _dump_bignum(obj):
        _io.write(ARC_Data._TYPES["Bignum"])
        ARC_Data.__dump_int32(obj) # our C++ implementation uses a "long" of 32 bit
    
    
    @staticmethod
    def _dump_float(obj):
        _io.write(ARC_Data._TYPES["Float"])
        _io.write(pack("<f", obj))
    
    
    @staticmethod
    def _dump_string(obj):
        _io.write(ARC_Data._TYPES["String"])
        if obj.size > 0:
            if not ARC_Data.__try_map(_strings, obj): # abort if object has already been mapped
                return
            ARC_Data.__dump_int32(len(obj))
            _io.write(obj)
        else:
            ARC_Data.__dump_int32(0)
        
    
    
    @staticmethod
    def _dump_array(obj):
        _io.write(ARC_Data._TYPES["Array"])
        if obj.size > 0:
            if not ARC_Data.__try_map(_arrays, obj): # abort if object has already been mapped
                return 
            ARC_Data.__dump_int32(len(obj))
            for value in obj:
                ARC_Data._dump(value)
        else:
            ARC_Data.__dump_int32(0)
        
    
    
    @staticmethod
    def _dump_hash(obj):
        _io.write(ARC_Data._TYPES["Hash"])
        if obj.size > 0:
            if not ARC_Data.__try_map(_hashes, obj): # abort if object has already been mapped
                return 
            ARC_Data.__dump_int32(len(obj))
            for key, value in obj.items():
                ARC_Data._dump(key)
                ARC_Data._dump(value)
        else:
            ARC_Data.__dump_int32(0)
        
    
    @staticmethod
    def _request_instance_variables(obj):
        if hasattr(obj, "_arc_instance_variables"):
            return obj._arc_instance_variables
        else:
            l = []
            for key, value in obj.__dict__.items():
                if key[0] is not "_":
                    if not isinstance(value, (types.FunctionType, types.ClassType, types.MethodType, 
                                              types.ModuleType, types.SliceType, types.LambdaType, 
                                              types.GeneratorType)):
                        l.append(key)
            return l
    
    @staticmethod
    def _dump_object(obj):
        _io.write(ARC_Data._TYPES["Object"])
        if hasattr(obj, "_arc_class_path"):
            klass_path = obj._arc_class_path
        else:
            klass_path = "%s::%s" % (obj.__class__.__module__, obj.__class__.__name__)
        ARC_Data._dump_string(ARC_Data.__get_class_path(klass_path)) # first the string path because this is required to load the object
        if not ARC_Data.__try_map(_objects, obj): # abort if object has already been mapped
            return
        if hasattr(obj, "_arc_dump"):
            data = obj._arc_dump()
            ARC_Data.__dump_int32(len(data))
            _io.write(data)
        else:
            if hasattr(obj, "_arc_exclude"):
                excludes = obj._arc_exclude
            else:
                excludes = []
            variables = list(set(ARC_Data._request_instance_variables(obj)) - set(excludes))
            ARC_Data.__dump_int32(len(variables))
            for variable in variables:
                ARC_Data._dump_string(variable)
                ARC_Data._dump(getattr(obj, variable))
        
    
    
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
        return ARC_Data.__load_int32()
    
    
    @staticmethod
    def _load_bignum():
        return ARC_Data.__load_int32() # our C++ implementation uses a "long" of 32 bit
    
    
    @staticmethod
    def _load_float():
        return unpack("<f", _io.read(4))
    
    
    @staticmethod
    def _load_string():
        id_num = ARC_Data.__load_int32()
        if id_num == 0:
            return ""
        obj = ARC_Data.__find_mapped(_strings, id_num)
        if obj != None:
            return obj.clone
        size = ARC_Data.__load_int32()
        obj = _io.read(size)
        ARC_Data.__map(_strings, obj)
        return obj
    
    
    @staticmethod
    def _load_array():
        id_num = ARC_Data.__load_int32()
        if id_num == 0:
            return []
        obj = ARC_Data.__find_mapped(_arrays, id_num)
        if obj != None:
            return obj
        size = ARC_Data.__load_int32()
        obj = []
        ARC_Data.__map(_arrays, obj)
        for i in range(size):
            obj.append(ARC_Data._load())
        return obj
    
    
    @staticmethod
    def _load_hash():
        id_num = ARC_Data.__load_int32()
        if id_num == 0:
            return {}
        obj = ARC_Data.__find_mapped(_hashes, id_num)
        if obj != None:
            return obj
        size = ARC_Data.__load_int32()
        obj = {}
        ARC_Data.__map(_hashes, obj)
        for i in range(size):
            key = ARC_Data._load() # making sure key is always loaded first
            obj[key] = ARC_Data._load()
        return obj
    
    
    @staticmethod
    def _load_object():
        class_path = ARC_Data._load()
        obj = ARC_Data.__find_mapped(_objects, ARC_Data.__load_int32())
        if obj != None:
            return obj
        classe = ARC_Data.__get_class_object(class_path)
        size = ARC_Data.__load_int32()
        if hasattr(classe, "_arc_load"):
            obj = classe._arc_load(_io.read(size))
            ARC_Data.__map(_objects, obj)
            return obj
        obj = classe.__new__(classe)
        ARC_Data.__map(_objects, obj)
        for i in range(size):
            setattr(obj, ARC_Data._load(), ARC_Data._load())
        return obj
    
    



