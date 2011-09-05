'''
Created on Sep 4, 2011

ARC_Dump: dumps data into msgpack structured files
'''
import types

import msgpack

__io = None
__symbols = {}
__strings = {}
__ids = {}
__stack = []
__finaldump = {}
__sym_count = 0
__pending_objects = []
__post_load_objects = []
__class_path_redirects = {}

def dump(obj, io, redirects={}):
    global __io
    global __class_path_redirects
    __class_path_redirects = redirects
    __io = io
    queue_dump_object(obj)
    start_dump()
    write_dump()
    reset()
  
  
def load(io, redirects={}):
    global __io
    global __symbols
    global __class_path_redirects
    __class_path_redirects = redirects
    __io = io
    build_object_table()
    link_objects()
    call_arc_post_load()
    object = __symbols[0]
    if object[0] >= 0 and object[0] <= 4: #False, True, Nil, String, Numeric
        return_obj = object[1]
    elif object[0] >= 5 and object[0] <= 7:#Array, Hash, Class
        return_obj = object[1][0]
    else:
        return_obj = None
    reset()
    return return_obj
  
  
def build_object_table():
    global __io
    global __symbols
    global __pending_objects
    global __class_path_redirects
    load_string = __io.read()
    objects = msgpack.unpackb(load_string)
    for key, item in objects:
        __symbols[key] = item 
        if item[0] >= 0 and item[0] <= 4: #False, True, Nil, String, Numeric
            continue
        elif item[0] >= 5 and item[0] <= 6: #Array, Hash
            if len(item[1]) > 0:
                __pending_objects.append(key) 
        elif item[0] == 7:    #Class
            if __class_path_redirects.has_key(item[1][0]):
                klass_path = __class_path_redirects[item[1][0]]
            else:
                klass_path =item[1][0]
            klasses = klass_path.split("::")
            if globals().has_key(klasses[0]):
                klass = globals()[klasses[0]]
            else:
                raise TypeError, "No class defined: %s} " % klasses[0]
            if len(klasses) > 1:
                for index in range(len(klasses)):
                    if index == 0:
                        continue
                    if klass.__dict__.has_key(klasses[index]):
                        klass = klass.__dict__[klasses[index]]
                    else:
                        raise TypeError, "No class defined: %s} " % klasses[index]
            klass_obj = klass.__new__(klass)
            item[1][0] = klass_obj
            __pending_objects.append(key)
        else:
            raise TypeError, "Unrecognized type declaration: %s" % type
  
  
def link_objects():
    global __symbols
    global __pending_objects
    global __post_load_objects
    for obj_key in __pending_objects:
        obj = __symbols[obj_key]
        if obj[0] == 5: #array
            new_array = obj[1][0]
            for item in obj[1][1]:
                if item[0] == 0: #actualy object
                    new_array.append(item[1])
                elif item[0] == 1: #link to array, hash, or user object
                    new_array.append(__symbols[item[1]][1][0])
                elif item[0] == 2: #string
                    new_array.append(__symbols[item[1]][1])
        elif obj[0] == 6: #hash
            new_hash = obj[1][0]
            for pair in obj[1][1]:
                if pair[0][0] == 0: #actualy object
                    key = pair[0][1]
                elif pair[0][0] == 1: #link to array, hash, or user object
                    key = __symbols[pair[0][1]][1][0]
                elif pair[0][0] == 2: #string
                    key = __symbols[pair[0][1]][1]
                if pair[1][0] == 0: #actualy object
                    value = pair[1][1]
                elif pair[1][0] == 1: #link to array, hash, or user object
                    value = __symbols[pair[1][1]][1][0]
                elif pair[1][0] == 2: #string
                    value = __symbols[pair[1][0]][1]
                new_hash[key] = value    
        elif obj[0] == 7: #nonstandard object
            klass_obj = obj[1][0]
            if hasattr(klass_obj, "_arc_load"):
                klass_obj._arc_load(obj[1][1])
            else:
                for pair in obj[1][1]:
                    variable = pair[0]
                    if pair[1][0] == 0: #actualy object
                        value = pair[1][1]
                    elif pair[1][0] == 1: #link to array, hash, or user object
                        value = __symbols[pair[1][1]][1][0]
                    elif pair[1][0] == 2: #string
                        value = __symbols[pair[1][1]][1]
                    setattr(klass_obj, variable, value)
            if hasattr(klass_obj, "_post_arc_load"):
                __post_load_objects.append(klass_obj)
        
      
  
  
def call_arc_post_load():
    global __post_load_objects
    for obj in __post_load_objects:
        obj._post_arc_load()
  
def reset():
    global __io
    global __symbols
    global __strings
    global __ids
    global __stack
    global __finaldump
    global __sym_count
    global __pending_objects
    global __post_load_objects
    global __class_path_redirects
    __io = None
    __symbols = {}
    __strings = {}
    __ids = {}
    __stack = []
    __finaldump = {}
    __sym_count = 0
    __pending_objects = []
    __post_load_objects = []
    __class_path_redirects = {}
  
  
def start_dump():
    global __stack
    while len(__stack) > 0:
        dump_object(__stack.pop(0))
    
  
  
def write_dump():
    global __io
    global __finaldump
    dump_string = msgpack.packb(__finaldump)
    __io.write(dump_string)
  
  
def queue_dump_object(obj):
    if obj is False:
        result = dump_false_object(obj)
    elif obj is True:
        result = dump_true_object(obj)
    elif obj is None:
        result = dump_nil_object(obj)
    elif isinstance(obj, (types.IntType, types.LongType, types.FloatType)):
        result = dump_numeric_object(obj)
    elif isinstance(obj, types.StringType):
        result = dump_string_object(obj)
    elif isinstance(obj, (types.ListType, types.TupleType)):
        result = queue_dump_array_object(obj)
    elif isinstance(obj, types.DictType):
        result = queue_dump_hash_object(obj)
    else:
        result = queue_dump_nonstandard_object(obj)
    return result
  
  
def dump_object(obj):
    if isinstance(obj, (types.ListType, types.TupleType)):
        dump_array_object(obj)
    elif isinstance(obj, types.DictType):
        dump_hash_object(obj)
    else:
        dump_nonstandard_object(obj)
    
  
  
def dump_true_object(obj):
    return [0, True]
  
  
def dump_false_object(obj):
    return [0, False]
  
  
def dump_nil_object(obj):
    return [0, None]
  
  
def dump_numeric_object(obj):
    return [0, obj]
  
  
def dump_string_object(obj):
    global __strings
    global __ids
    if not __strings.has_key(obj):
        __strings[obj] = id(obj)
        dump_array = enter_obj(obj)
        dump_array[0], dump_array[1] = 4, obj
    return [2, __ids[__strings[obj]]]
  
  
def queue_dump_array_object(obj):
    global __symbols
    global __ids
    if not __symbols.has_key(id(obj)):
        __stack.append(obj)
        dump_array = enter_obj(obj)
        dump_array[0], dump_array[1] = 5, [[],[]]
    return [1, __ids[obj.object_id]]
  
  
def dump_array_object(obj):
    global __symbols
    dump_array = __symbols[id(obj)][1]
    for value in obj:
        dump_array[1][1].append(queue_dump_object(value))
  
  
def queue_dump_hash_object(obj):
    global __symbols
    global __ids
    if not __symbols.has_key(id(obj)):
        __stack.append(obj)
        dump_array = enter_obj(obj)
        dump_array[0], dump_array[1] = 6, [{}, []]
    return [1, __ids[id(obj)]]
  
 
def dump_hash_object(obj):
    global __symbols
    dump_array = __symbols[obj.object_id][1]
    for key, value in obj:
        pair = [queue_dump_object(key), queue_dump_object(value)]
        dump_array[1][1].append(pair)
        
        
def request_class_path(obj):
    global __class_path_redirects
    if hasattr(obj, "_arc_class_path"):
        klass_path = obj._arc_class_path
    else:
        klass_path = "%s::%s" % (obj.__class__.__module__, obj.__class__.__name__)
    if __class_path_redirects.has_key(klass_path):
        klass_path = __class_path_redirects[klass_path]
    return klass_path
    
    
def queue_dump_nonstandard_object(obj):
    global __symbols
    global __ids
    if not __symbols.has_key(id(obj)):
        __stack.append(obj)
        dump_array = enter_obj(obj)
        klass = request_class_path(obj)
        dump_array[0], dump_array[1] = 7, [klass,[]]
    return [1, __ids[id(obj)]]

def request_instance_variables(obj):
    if hasattr(obj, "_arc_instance_variables"):
        return obj._arc_instance_variables
    else:
        list = []
        for key, value in obj.__dict__:
            if key[0] is not "_":
                if not isinstance(value, (types.FunctionType, types.ClassType, types.MethodType, 
                                          types.ModuleType, types.SliceType, types.LambdaType, 
                                          types.GeneratorType)):
                    list.append(key)
        return list
  
def dump_nonstandard_object(obj):
    global __symbols
    dump_array = __symbols[obj.object_id][1]
    if hasattr(obj, "_prep_arc_dump"):
        obj._prep_arc_dump()
    if hasattr(obj, "_arc_dump"):
        dump_array[1][1] = obj._arc_dump()
    else:
        if hasattr(obj, "_arc_exclude"):
            excludes = obj._arc_exclude
        else:
            excludes = []
        instance_variables = request_instance_variables(obj)
        for value in instance_variables:
            if value in excludes:
                continue
            pair = [value, queue_dump_object(getattr(obj, value))]
            dump_array[1][1].append(pair)
    
  
 
def enter_obj(obj):
    global __symbols
    global __ids
    global __finaldump
    global __sym_count
    key = obj.object_id
    dump_array = [None, None]
    __symbols[key] = [obj, dump_array]
    __ids[key] = __sym_count
    __finaldump[__sym_count] = dump_array
    __sym_count += 1
    return dump_array
  


