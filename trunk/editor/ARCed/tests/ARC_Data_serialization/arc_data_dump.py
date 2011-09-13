from struct import pack, unpack
import types

class Data(object):

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
        _io.write(VERSION)
        try:
            _dump(obj)
        except Exception:
            try:
                print "stream position: %s" % _io.tell()
            except Exception:
                pass
            raise
        _reset()
    
    
    @staticmethod
    def load(io, redirects = {}, extended_namespace={}):
        global _class_path_redirects
        global _io
        global _extended_namespace
        _class_path_redirects = redirects
        _extended_namespace = dict(extended_namespace.update(globals()))
        extended_namespace = {}
        _io = io
        version = _io.read(2)
        if _VERSION != version:
            raise "Error: version mismatch! Expected: %s Found: %s" %(repr(VERSION), repr(version))
        try:
            data = _load()
        except Execption:
            try:
                print "stream position: %s" % _io.tell()
            except Exception:
                pass
            raise
        _reset()
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
            __dump_int32(len(data))
            data.append(obj)
            return True
        __dump_int32(index)
        return False
    

    @staticmethod
    def __map(data, obj):
        data.append(obj)
    

    @staticmethod
    def __find_mapped(data, id):
        if id < len(data):
            return data[id]
        else:
            return None
    
    
    @staticmethod
    def __dump_int32(obj):
        _io.write(pack("<I", obj))
    

    @staticmethod
    def __load_int32():
        return _io.read(4).unpack("V")[0]
    
    
    @staticmethod
    def _dump(obj):
        if obj is None:
            return _dump_none(obj)
        if obj is False:
            return _dump_false(obj) 
        if obj is True:
            return _dump_true(obj)
        if isinstance(obj, types.IntType):
            return _dump_fixnum(obj)
        if isinstance(obj, types.LongType):
            return _dump_bignum(obj)
        if isinstance(obj, types.FloatType):
            return _dump_float(obj)
        if isinstance(ojb, types.StringTypes):
            return _dump_string(obj)
        if isinstance(obj, (types.ListType, types.TupleType)):
            return _dump_array(obj)
        if isinstance(obj, types.DictType):
            return _dump_hash(obj)
        if isinstance(obj, object):
            return _dump_object(obj)
        raise TypeError("Error: %s cannot be dumped!" % obj.__class__)
    
    @staticmethod
    def _load():
        type = _io.read(1)
        if type is _TYPES["NoneClass"]:
            return _load_none()
        elif type is _TYPES["FalseClass"]:
            return _load_false()
        elif type is _TYPES["TrueClass"]:
            return _load_true()
        elif type is _TYPES["Fixnum"]:
            return _load_fixnum()
        elif type is _TYPES["Bignum"]:
            return _load_bignum()
        elif type is _TYPES["Float"]:
            return _load_float()
        elif type is _TYPES["String"]:
            return _load_string()
        elif type is _TYPES["Array"]:
            return _load_array()
        elif type is _TYPES["Hash"]:
            return _load_hash()
        elif type is _TYPES["Object"]:
            return _load_object()
        
        raise "Error: Unknown type 0x%02X detected!" % type.ord
    
    
    @staticmethod
    def _dump_none(obj):
        _io.write(_TYPES["NoneClass"])
    

    @staticmethod
    def _dump_false(obj):
        _io.write(_TYPES["FalseClass"])
    

    @staticmethod
    def _dump_true(obj):
        _io.write(_TYPES["TrueClass"])
    
    
    @staticmethod
    def _dump_fixnum(obj):
        _io.write(_TYPES["Fixnum"])
        __dump_int32(obj)
    
    
    @staticmethod
    def _dump_bignum(obj):
        _io.write(_TYPES["Bignum"])
        __dump_int32(obj) # our C++ implementation uses a "long" of 32 bit
    
    
    @staticmethod
    def _dump_float(obj):
        _io.write(_TYPES["Float"])
        _io.write(pack("<f", obj))
    
    
    @staticmethod
    def _dump_string(obj):
        _io.write(_TYPES["String"])
        if obj.size > 0:
            if not __try_map(_strings, obj): # abort if object has already been mapped
                return
            __dump_int32(len(obj))
            _io.write(obj)
        else:
            __dump_int32(0)
        
    
    
    @staticmethod
    def _dump_array(obj):
        _io.write(_TYPES["Array"])
        if obj.size > 0:
            if not __try_map(_arrays, obj): # abort if object has already been mapped
                return 
            __dump_int32(len(obj))
            for value in obj:
                _dump(value)
        else:
            __dump_int32(0)
        
    
    
    @staticmethod
    def _dump_hash(obj):
        _io.write(_TYPES["Hash"])
        if obj.size > 0:
            if not __try_map(_hashes, obj): # abort if object has already been mapped
                return 
            __dump_int32(len(obj))
            for key, value in obj.items():
                _dump(key)
                _dump(value)
        else:
            __dump_int32(0)
        
    
    @staticmethod
    def _request_instance_variables(obj):
        if hasattr(obj, "_arc_instance_variables"):
            return obj._arc_instance_variables
        else:
            list = []
            for key, value in obj.__dict__.items():
                if key[0] is not "_":
                    if not isinstance(value, (types.FunctionType, types.ClassType, types.MethodType, 
                                              types.ModuleType, types.SliceType, types.LambdaType, 
                                              types.GeneratorType)):
                        list.append(key)
            return list
    
    @staticmethod
    def _dump_object(obj):
        _io.write(_TYPES["Object"])
        if hasattr(obj, "_arc_class_path"):
            klass_path = obj._arc_class_path
        else:
            klass_path = "%s::%s" % (obj.__class__.__module__, obj.__class__.__name__)
        _dump_string(__get_class_path(klass_path)) # first the string path because this is required to load the object
        if not __try_map(_objects, obj): # abort if object has already been mapped
            return
        if hasattr(obj, "_arc_dump"):
            data = obj._arc_dump()
            __dump_int32(len(data))
            _io.write(data)
        else:
            if hasattr(obj, "_arc_exclude"):
                excludes = obj._arc_exclude
            else:
                excludes = []
            variables = list(set(_request_instance_variables(obj)) - set(excludes))
            __dump_int32(len(variables))
            for variable in variables:
                _dump_string(variable)
                _dump(getattr(obj, variable))
        
    
    
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
        return __load_int32()
    
    
    @staticmethod
    def _load_bignum():
        return __load_int32() # our C++ implementation uses a "long" of 32 bit
    
    
    @staticmethod
    def _load_float():
        return unpack("<f", _io.read(4))
    
    
    @staticmethod
    def _load_string():
        id = __load_int32()
        if id == 0:
            return ""
        obj = __find_mapped(_strings, id)
        if obj != None:
            return obj.clone
        size = __load_int32()
        obj = _io.read(size)
        __map(_strings, obj)
        return obj
    
    
    @staticmethod
    def _load_array():
        id = __load_int32()
        if id == 0:
            return []
        obj = __find_mapped(_arrays, id)
        if obj != None:
            return obj
        size = __load_int32()
        obj = []
        __map(_arrays, obj)
        for i in range(size):
            obj.append(_load())
        return obj
    
    
    @staticmethod
    def _load_hash():
        id = __load_int32()
        if id == 0:
            return {}
        obj = __find_mapped(_hashes, id)
        if obj != None:
            return obj
        size = __load_int32()
        obj = {}
        __map(_hashes, obj)
        for i in range(size):
            key = _load() # making sure key is always loaded first
            obj[key] = _load()
        return obj
    
    
    @staticmethod
    def _load_object():
        class_path = _load()
        obj = __find_mapped(_objects, __load_int32())
        if obj != None:
            return obj
        classe = __get_class_object(class_path)
        size = __load_int32()
        if hasattr(classe, "_arc_load"):
            obj = classe._arc_load(_io.read(size))
            __map(_objects, obj)
            return obj
        obj = classe.__new__(classe)
        __map(_objects, obj)
        for i in range(size):
            setattr(obj, _load(), _load())
        return obj
    
    



