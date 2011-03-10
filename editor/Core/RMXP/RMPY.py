import types
import re
from RGSS1_RPG import RPG
from RPGutil import *

__io = None
__symbols = {}
__stack = []
__top_string = "\\^ "
__sym_count = 0
__good_objects = [types.BooleanType, types.NoneType, types.StringType,
                  types.IntType, types.LongType, types.FloatType,
                  types.TupleType, types.ListType,
                  types.DictType, RPG.Actor, RPG.Class, RPG.Class.Learning, #@UndefinedVariable
                  RPG.Skill, RPG.Item, RPG.EventCommand, RPG.Weapon,
                  RPG.Armor, RPG.Enemy, RPG.Enemy.Action, RPG.Troop, #@UndefinedVariable
                  RPG.Troop.Member, RPG.Troop.Page, #@UndefinedVariable
                  RPG.Troop.Page.Condition, RPG.State, #@UndefinedVariable
                  RPG.Animation, RPG.Animation.Frame, #@UndefinedVariable
                  RPG.Animation.Timing, RPG.Tileset, RPG.CommonEvent, #@UndefinedVariable
                  RPG.System, RPG.System.Words, RPG.System.TestBattler, #@UndefinedVariable
                  RPG.AudioFile, RPG.Map, RPG.MapInfo, RPG.Event,
                  RPG.Event.Page, RPG.Event.Page.Condition, #@UndefinedVariable
                  RPG.Event.Page.Graphic, RPG.MoveRoute, #@UndefinedVariable
                  RPG.MoveCommand, Table, Color, Tone]
__pending_objects = []
__post_load_objects = []
__top_object_key = 0


def dump(obj, io):
    global __io
    global __top_string
    __io = io
    __top_string += queue_dump_object(obj)
    start_dump()
    write_dump()
    reset()

def load(io):
    global __io
    global __symbols
    __io = io
    build_object_table()
    link_objects()
    call_rmpy_post_load()
    object = __symbols[__top_object_key][0]
    reset()
    return object

def build_object_table():
    global __io
    global __symbols
    global __pending_objects
    global __top_object_key
    objects = __io.read().split("\n")
    for item in objects:
        flag = False
        match = re.search("\\#([0-9]+)\s-#(.+)", item)
        if match: #Numeric
            key = int(match.group(1))
            if __symbols.has_key(key):
                raise TypeError, "Duplicate object declaration: %s" % key

            number = match.group(2)
            if re.search("\A-?[0-9]+\Z", number): #integer
                number = int(number)
            elif re.search("\A-?[0-9]+\.[0-9]+\Z", number):
                number = float(number)
            else:
                raise TypeError, "Bad Numeric format: #s" % number
            __symbols[key] = [number, item]
            flag = True
        match = re.search("\\#([0-9]+)\s\"(.*)", item)
        if (not flag) and match: #String
            key = int(match.group(1))
            if __symbols.has_key(key):
                raise TypeError, "Duplicate object declaration: %s" % key

            string = match.group(2)
            __symbols[key] = [string, item]
            flag = True
        match = re.search("\\#([0-9]+)\s\[(.*)", item)
        if (not flag) and match: #Array
            key = int(match.group(1))
            if __symbols.has_key(key):
                raise TypeError, "Duplicate object declaration: %s" % key

            array = match.group(2).split(",")
            __symbols[key] = [array, item]
            if not len(array) == 0:
                __pending_objects.append(key)
            flag = True
        match = re.search("\\#([0-9]+)\s\{(.*)", item)
        if (not flag) and match: #Hash
            key = int(match.group(1))
            if __symbols.has_key(key):
                raise TypeError, "Duplicate object declaration: %s" % key

            items = match.group(2).split(",")
            hash = {}
            for pair in items:
                pair_array = pair.split("=>")
                hash[pair_array[0]] = pair_array[1]

            __symbols[key] = [hash, item]
            __pending_objects.append(key)
            flag = True
        match = re.search("\\#([0-9]+)\s\/-(.)(.*)", item)
        if (not flag) and match: #type declaration
            key = int(match.group(1))
            if __symbols.has_key(key):
                raise TypeError, "Duplicate object declaration: %s" % key
            type = match.group(2)
            extra = match.group(3)
            if re.search("T", type): #true
                __symbols[key] = [True, item]
                flag = True
            elif re.search("F", type): #false
                __symbols[key] = [False, item]
                flag = True
            elif re.search("N", type): #none
                __symbols[key] = [None, item]
                flag = True
            elif re.search("C", type):
                match = re.search("([^\s]+?)\s\{(.*)", extra)
                if match:
                    klasses = match.group(1).split("::")
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
                    __symbols[key] = [klass_obj, item]
                    __pending_objects.append(key)
                    flag = True
                else:
                    raise TypeError, "Invalad class declaration: %s" % item
            else:
                raise TypeError, "Unrecognized type declaration: %s" % type
        match = re.search("\\^\s\/#([0-9]+)", item)
        if (not flag) and match: #top object
            __top_object_key = int(match.group(1))
            flag = True
        if (not flag):
            if not (item == ""):
                raise TypeError, "Unrecognized object declaration: %s" % item

def link_objects():
    global __pending_objects
    global __symbols
    global __post_load_objects
    for obj_key in __pending_objects:
        obj = __symbols[obj_key][0]
        declaration = __symbols[obj_key][1]
        if isinstance(obj, types.ListType):
            new_array = []
            for item in obj:
                if item == "":
                    continue
                match = re.search("\/#([0-9]+)", item)
                if match:
                    key = int(match.group(1))
                    new_array.append(__symbols[key][0])
                else:
                    raise TypeError, "Unrecognized item link: %s" % item
            obj[0:len(obj)] = new_array
        elif isinstance(obj, types.DictType):
            new_hash = {}
            for key, value in obj.iteritems():
                match = re.search("\/#([0-9]+)", key)
                if match:
                    new_key = __symbols[int(match.group(1))][0]
                else:
                    raise TypeError, "Unrecognized item link: %s" % key
                match = re.search("\/#([0-9]+)", value)
                if match:
                    new_value = __symbols[int(match.group(1))][0]
                else:
                    raise TypeError, "Unrecognized item link: %s" % value
                if isinstance(new_key, types.ListType):
                    new_hash[tuple(new_key)] = new_value
                else:
                    new_hash[new_key] = new_value
            obj.clear()
            obj.update(new_hash)
        else:
            match = re.search("[^\s]+?\s\{(.*)", declaration)
            if match:
                items = match.group(1).split(",")
                for item in items:
                    pair = item.split("=>")
                    variable = pair[0].strip()
                    match = re.search("\/#([0-9]+)", pair[1])
                    if match:
                        key = int(match.group(1))
                    else:
                        raise TypeError, "Unrecognized item link: %s" % pair[1]
                    setattr(obj, variable, __symbols[key][0])
                if hasattr(obj, "_post_rmpy_load"):
                    #add it to the list of objects to load
                    __post_load_objects.append(obj)
            else:
                pass

def call_rmpy_post_load():
    for obj in __post_load_objects:
        obj._post_rmpy_load()

def reset():
    global __io
    global __symbols
    global __stack
    global __top_object_key
    global __sym_count
    global __pending_objects
    global __top_string
    __io = None
    __symbols = {}
    __stack = []
    __top_string = "\\^ "
    __sym_count = 0
    __pending_objects = []
    __top_object_key = 0

def start_dump():
    while len(__stack) > 0:
        dump_object(__stack.pop(0))

def write_dump():
    global __symbols
    global __io
    global __top_string
    sort_func = lambda a, b: cmp(int(a[1][1]), int(b[1][1]))
    objects = sorted(__symbols.iteritems(), sort_func)
    object_strings = []
    for value in objects:
        object_strings.append(value[1][2])
    for string in object_strings:
        __io.write(string + "\n")
    __io.write(__top_string + "\n")


def queue_dump_object(obj):
    flag = False
    for klass in __good_objects:
        if isinstance(obj, klass):
            flag = True
            break
    if not flag:
        raise TypeError, "Can't dump #{obj.class.to_s}"
    if obj is False:
        result = dump_false_object(obj)
    elif obj is True:
        result = dump_true_object(obj)
    elif obj is None:
        result = dump_None_object(obj)
    elif isinstance(obj, types.StringType):
        result = dump_string_object(obj)
    elif isinstance(obj, (types.IntType, types.LongType, types.FloatType)):
        result = dump_numeric_object(obj)
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
    if not __symbols.has_key(id(obj)):
        return enter_obj(obj, "/-T")
    return "/#%s" % __symbols[id(obj)][1]


def dump_false_object(obj):
    if  not __symbols.has_key(id(obj)):
        return enter_obj(obj, "/-F")
    return "/#%s" % __symbols[id(obj)][1]


def dump_None_object(obj):
    if not __symbols.has_key(id(obj)):
        return enter_obj(obj, "/-N")
    return "/#%s" % __symbols[id(obj)][1]


def dump_string_object(obj):
    if not __symbols.has_key(id(obj)):
        return enter_obj(obj, "\"" + obj)
    return "/#%s" % __symbols[id(obj)][1]


def dump_numeric_object(obj):
    if not __symbols.has_key(id(obj)):
        return enter_obj(obj, "-#%s" % str(obj))
    return "/#%s" % __symbols[id(obj)][1]


def queue_dump_array_object(obj):
    if not __symbols.has_key(id(obj)):
        string = "["
        __stack.append(obj)
        return enter_obj(obj, string)
    return "/#%s" % __symbols[id(obj)][1]


def dump_array_object(obj):
    string = __symbols[id(obj)][2]
    i = 0
    for value in obj:
        string += queue_dump_object(value)
        if not (i + 1 >= len(obj)):
            string += ","
        i += 1
    __symbols[id(obj)][2] = string


def queue_dump_hash_object(obj):
    if not __symbols.has_key(id(obj)):
        string = "{"
        __stack.append(obj)
        return enter_obj(obj, string)
    return "/#%s" % __symbols[id(obj)][1]


def dump_hash_object(obj):
    string = __symbols[id(obj)][2]
    i = 0
    for key, value in obj.iteritems():
        string += (queue_dump_object(key) + "=>" + queue_dump_object(value))
        if not (i + 1 >= len(obj)):
            string += ","
        i += 1
    __symbols[id(obj)][2] = string


def queue_dump_nonstandard_object(obj):
    if not __symbols.has_key(id(obj)):
        string = "/-C %s {" % request_class_path(obj)
        __stack.append(obj)
        return enter_obj(obj, string)
    return "/#%s" % __symbols[id(obj)][1]


def dump_nonstandard_object(obj):
    string = __symbols[id(obj)][2]
    if hasattr(obj, "_prep_rmpy_dump"):
        obj._prep_rmpy_dump()
    if hasattr(obj, "_rmpy_dump"):
        string += "/-U " + obj._rmpy_dump()
    else:
        i = 0
        instance_variables = request_instance_variables(obj)
        for value in instance_variables:
            string += (str(value) + "=>" +
                    queue_dump_object(getattr(obj, str(value))))
            if not (i + 1 >= len(instance_variables)):
                string += ","
            i += 1
    __symbols[id(obj)][2] = string


def enter_obj(obj, string):
    global __sym_count
    global __symbols
    key = id(obj)
    string = ("\\#%s " % __sym_count) + string
    __symbols[key] = [obj, __sym_count, string]
    __sym_count += 1
    return "/#%s" % (__sym_count - 1)

def request_class_path(obj):
    if hasattr(obj, "__class_path__"):
        return obj.__class_path__
    else:
        raise TypeError, "no __class_path__ atter asigened"

def request_instance_variables(obj):
    if hasattr(obj, "__instance_variables__"):
        return obj.__instance_variables__
    else:
        raise TypeError, "no __instance_variables__ atter asigened"
