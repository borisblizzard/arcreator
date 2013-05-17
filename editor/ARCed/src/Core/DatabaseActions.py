import types
from copy import copy, deepcopy
import numpy

import Kernel
from Kernel import Manager as KM

import Actions

class DatabaseAction(Actions.ActionManager):
    ''' an action that edits RGSS Datatypes'''

    def __init__(self, data={}, sub_action=False):
        super(DatabaseAction, self).__init__(sub_action)
        if not isinstance(data, types.DictType):
            raise TypeError("Error: Expected dict type for 'data'")
        self.data = data
        self.keys = []
        self.old_data = {}
        self.obj = None
        self.type = None

    def setType(self, type):
        self.type = type

    def setKeys(self, *args):
        self.keys = []
        val = args
        if len(args) == 1 and isinstance(args[0], (types.ListType, types.TupleType)):
            val = args[0]
        self.keys.extend(val)

    def addKeys(self, *args):
        val = args
        if len(args) == 1 and isinstance(args[0], (types.ListType, types.TupleType)):
            val = args[0]
        self.keys.extend(val)

    def setObj(self, obj):
        self.obj = obj

    def do_apply(self):
        result = self.apply_keys()
        if not result: return result
        result &= self.apply_extra()
        if not result: self.undo_keys()
        return result

    def do_undo(self):
        result = self.undo_keys()
        if not result: return result
        result &= self.undo_extra()
        if not result: self.apply_keys()
        return result

    def apply_keys(self):
        keys_applyed = []
        try:
            for key, value in self.data:
                if key in self.keys:
                    if hasattr(self.obj, key):
                        self.old_data[key] = copy(getattr(self.obj, key))
                        setattr(self.obj, key, copy(value))
                        keys_applyed.append(key)
            return True
        except StandardError:
            Kernel.Log("Exception applying Database Action(%s), will atempt to revert" % self.type, "[DatabaseAction]", True, True)
            try:
                for key in keys_applyed:
                    self.data[key] = getattr(self.obj, key)
                    setattr(self.obj, key, self.old_data[key])
                Kernel.Log("'Apply' Database Action(%s) sucessfuly reverted" % self.type, "[DatabaseAction]", True)
            except StandardError:
                Kernel.Log("Exception reverting failed 'Apply' Database Action(%s), Possible Project coruption" % self.type, "[DatabaseAction]", True, True)
        return False

    def apply_extra(self):
        return True

    def undo_keys(self):
        keys_applyed = []
        try:
            for key, value in self.old_data:
                if key in self.keys:
                    if hasattr(self.obj, key):
                        self.data[key] = copy(getattr(self.obj, key))
                        setattr(self.obj, key, copy(value))
                        keys_applyed.append(key)
            return True
        except StandardError:
            Kernel.Log("Exception undoing Database Action(%s), will atempt to revert" % self.type, "[DatabaseAction]", True, True)
            try:
                for key in keys_applyed:
                    self.old_data[key] = getattr(self.obj, key)
                    setattr(self.obj, key, self.data[key])
                Kernel.Log("'Undo' Database Action(%s) sucessfuly reverted" % self.type, "[DatabaseAction]", True)
            except StandardError:
                Kernel.Log("Exception reverting failed 'Undo' Database Action(%s), Possible Project coruption" % self.type, "[DatabaseAction]", True, True)
        return False

    def undo_extra(self):
        return True
    
class TableEditAction(Actions.ActionTemplate):
    ''' an action that edits a RGSS Table'''
    def __init__(self, table, data={}, sub_action=False):
        super(TableEditAction, self).__init__(sub_action)
        if not isinstance(data, types.DictType):
            raise TypeError("Error: Expected dict type for 'data'")
        table_class = KM.get_component("Table").object
        if not isinstance(table, table_class):
            raise TypeError("Error: Expected %s type for 'table'" % table_class)
        self.table = table
        self.data = data
        self.oldvalue = None

    def do_apply(self):
        # data = { "dim": 1-3, "index": a tuple of list of len dim that looks like so (x, y, z), "value": the python list or preferably numpy array /value to set the table too
        # for a slice ((x1,x2), (y1,y2), (z1,z2))) or for a slice with a step ((x1,x2,xstep), (y1,y2,ystep), (z1,z2,zstep)) 
        # the values in a slice may be none just like in real slice notation ie.
        # [::2, 0, 0] (every other value in the array) would look like ((None,None,2), 0, 0) 
        # remember Tables are basically a dimension limited numpy array of of dtype int16 use numpy. they indexing so look at the numpy documentation for more information
        # note that unlike full numpy arrays you can't use less indexes than the dim of the table so you must explicitly slice the remaining dimensions
        # ie a index of [0:2, 0:3] on a 3d numpy would implicitly slice the missing dim but in the table you must state it explicitly or you'll get dim errors
        # so use this index instead [0:2, 0:3, :] in the tuple syntax for the data hash it would look like so ((0,2), (0,3), (None, None))
        # if your doing a slice on a id table you need to put the slice tupel or list in a tuple or list like so ((0,2),) 
        # note the , after the inside tupel this is to force the creation of the outer tupel. you could also do a list for the outer tuple instead in which case you don;t need the ,
        # [(0,2)] or [[0,2]]
        if self.data.has_key('resize'):
            if self.data['resize']:
                return self.resize_apply()
            else:
                return self.normal_apply()
        else:
            return self.normal_apply()
        
    def resize_apply(self):
        shape = self.data['shape']
        if len(shape) != len(self.table.getShape()):
            raise TypeError("new dimension and table old dimension must be the same (%d for %d)" % (len(shape), len(self.table.getShape())))
        self.oldvalue = numpy.copy(self.table._data)
        self.table.resize(*shape)

    def normal_apply(self):
        dim = self.data['dim']
        index = self.data['index']
        value = self.data['value']
        if dim > 3:
            raise TypeError("dim can't be greater than 3")
        if dim < 0:
            raise TypeError("dim can't be less than 0")  
        if isinstance(index, int):
            if dim > 1:
                raise TypeError("wrong number of arguments (%d for %d)" % (1, dim))
            else:
                self.oldvalue = numpy.copy(self.table[index])
                self.table[index] = value
        elif len(index) != dim:
            raise TypeError("wrong number of arguments (%d for %d)" % (len(index), dim))
        if len(index) == 1:
            # 1D slice
            s = slice(*index[0])
            self.oldvalue = numpy.copy(self.table[index])
            self.table[s] = value
        elif len(index) == 2:
            #2D index
            if isinstance(index[0], int):
                x = index[0]
            elif isinstance(index[0], (tuple, list)):
                x = slice(*index[0])
            else:
                raise TypeError("Error: %s is not an int, tuple or list" % index[0])
            if isinstance(index[1], int):
                y = index[1]
            elif isinstance(index[1], (tuple, list)):
                y = slice(*index[1])
            else:
                raise TypeError("Error: %s is not an int, tuple or list" % index[0])
            self.oldvalue = numpy.copy(self.table[x, y])
            self.table[x, y] = value
        elif len(index) == 3:
            #2D index
            if isinstance(index[0], int):
                x = index[0]
            elif isinstance(index[0], (tuple, list)):
                x = slice(*index[0])
            else:
                raise TypeError("Error: %s is not an int, tuple or list" % index[0])
            if isinstance(index[1], int):
                y = index[1]
            elif isinstance(index[1], (tuple, list)):
                y = slice(*index[1])
            else:
                raise TypeError("Error: %s is not an int, tuple or list" % index[1])
            if isinstance(index[2], int):
                z = index[2]
            elif isinstance(index[2], (tuple, list)):
                z = slice(*index[2])
            else:
                raise TypeError("Error: %s is not an int, tuple or list" % index[2])
            self.oldvalue = numpy.copy(self.table[x, y, z])
            self.table[x, y, z] = value
        else:
            raise TypeError("wrong number of arguments (%d for %d)" % (len(index), dim))
        return True
        
    def do_undo(self):
        if self.data.has_key('resize'):
            if self.data['resize']:
                return self.resize_undo()
            else:
                return self.normal_undo()
        else:
            return self.normal_undo()

    def resize_undo(self):
        shape = self.data['shape']
        if len(shape) != len(self.table.getShape()):
            raise TypeError("new dimension and table old dimension must be the same (%d for %d)" % (len(shape), len(self.table.getShape())))
        self.table._data[:] = self.oldvalue[:]

    def normal_undo(self):
        dim = self.data['dim']
        index = self.data['index']
        if dim > 3:
            raise TypeError("dim can't be less than 0")
        if dim < 0:
            raise TypeError("dim can't be greater than 3 or less than 0")
        if isinstance(index, int):
            if dim > 1:
                raise TypeError("wrong number of arguments (%d for %d)" % (1, dim))
            else:
                self.data['value'] = self.table[index]
                self.table[index] = self.oldvalue
        elif len(index) != dim:
            raise TypeError("wrong number of arguments (%d for %d)" % (len(index), dim))
        if len(index) == 1:
            # 1D slice
            s = slice(*index[0])
            self.data['value'] = self.table[index]
            self.table[index] = self.oldvalue
        elif len(index) == 2:
            #2D index
            if isinstance(index[0], int):
                x = index[0]
            elif isinstance(index[0], (tuple, list)):
                x = slice(*index[0])
            else:
                raise TypeError("Error: %s is not an int, tuple or list" % index[0])
            if isinstance(index[1], int):
                y = index[1]
            elif isinstance(index[1], (tuple, list)):
                y = slice(*index[1])
            else:
                raise TypeError("Error: %s is not an int, tuple or list" % index[0])
            self.data['value'] = self.table[x, y]
            self.table[x, y] = self.oldvalue
        elif len(index) == 3:
            #2D index
            if isinstance(index[0], int):
                x = index[0]
            elif isinstance(index[0], (tuple, list)):
                x = slice(*index[0])
            else:
                raise TypeError("Error: %s is not an int, tuple or list" % index[0])
            if isinstance(index[1], int):
                y = index[1]
            elif isinstance(index[1], (tuple, list)):
                y = slice(*index[1])
            else:
                raise TypeError("Error: %s is not an int, tuple or list" % index[1])
            if isinstance(index[2], int):
                z = index[2]
            elif isinstance(index[2], (tuple, list)):
                z = slice(*index[2])
            else:
                raise TypeError("Error: %s is not an int, tuple or list" % index[2])
            self.data['value'] = self.table[x, y, z]
            self.table[x, y, z] = self.oldvalue
        else:
            raise TypeError("wrong number of arguments (%d for %d)" % (len(index), dim))
        return True     
            
class ArmorEditAction(DatabaseAction):
    ''' edits an Armor object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(ArmorEditAction, self).__init__(data, sub_action)
        self.setObj(obj)
        self.setType("Armor")
        self.addKeys("id", "name", "icon_name", "description", "kind", 
                     "auto_state_id", "price", "pdef", "mdef", "eva", 
                     "str_plus", "dex_plus", "agi_plus", "int_plus", 
                     "guard_element_set", "guard_state_set")
                     
class ActorEditAction(DatabaseAction):
    ''' edits an Actor object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(ActorEditAction, self).__init__(data, sub_action)
        self.setType("Actor")
        self.parameters_action = None
        self.setObj(obj)
        self.addKeys("id", "name", "initial_level", "final_level", "exp_basis", "exp_inflation", "character_name", 
                     "character_hue", "battler_name", "battler_hue", "weapon_id", "armor1_id", "armor2_id",
                     "armor3_id", "armor4_id", "weapon_fix", "armor1_fix", "armor2_fix", "armor3_fix", "armor4_fix")

    def apply_extra(self):
        result = True
        actions_now = []
        try:
            if self.data.has_key("parameters"):
                self.parameters_action = KM.get_component("TableEditAction").object(self.obj.parameters, self.data["parameters"], sub_action=True)
                result &= self.parameters_action.apply()
                actions_now.append(self.parameters_action)
                if not result:
                    raise StandardError("'Apply' Sub action failed: %s" %  self.parameters_action)
        except StandardError:
            Kernel.Log("Exception applying Actor Edit Action, will atempt to revert", "[DatabaseAction]", True, True)
            try:
                for action in actions_now:
                    test = action.undo()
                    if not test:
                        raise StandardError("'Apply' Sub action revert failed: %s" % action)
                Kernel.Log("'Apply' Actor Edit Action sucessfuly reverted", "[DatabaseAction]", True)
            except StandardError:
                Kernel.Log("Exception reverting failed 'Apply' Actor Edit Action, Possible Project coruption", "[DatabaseAction]", True, True)
            result = False
        return result

    def undo_extra(self):
        actions_now = []
        result = True
        try:
            if self.parameters_action is not None:
                result &= self.parameters_action.undo()
                actions_now.append(self.parameters_action)
                if not result:
                    raise StandardError("'Undo' Sub action failed: %s" %  self.parameters_action)
        except StandardError:
            Kernel.Log("Exception undoing Actor Edit Action, will atempt to revert", "[DatabaseAction]", True, True)
            try:
                for action in actions_now:
                    test = action.apply()
                    if not test:
                        raise StandardError("'Undo' Sub action revert failed: %s" % action)
                Kernel.Log("'Undo' Actor Edit Action sucessfuly reverted", "[DatabaseAction]", True)
            except StandardError:
                Kernel.Log("Exception reverting failed 'Undo' Actor Edit Action, Possible Project coruption", "[DatabaseAction]", True, True)
        return result
                                               
class ClassEditAction(DatabaseAction):
    ''' edits a Class object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(ClassEditAction, self).__init__(data, sub_action)
        self.setType("Class")
        self.setObj(obj)
        self.addKeys("id", "name", "position", "weapon_set", "armor_set", "learnings")
        self.element_ranks_action = None
        self.state_ranks_action = None

    def apply_extra(self):
        result = True
        actions_now = []
        try:
            if self.data.has_key("element_ranks"):
                self.element_ranks_action = TableEditAction(self.obj.element_ranks, self.data["element_ranks"], sub_action = True)
                result &= self.element_ranks_action.apply()
                actions_now.append(self.element_ranks_action)
                if not result:
                    raise StandardError("'Apply' Sub action failed: %s" %  self.element_ranks_action)
            if self.data.has_key("state_ranks"):
                self.state_ranks_action = TableEditAction(self.obj.state_ranks, self.data["state_ranks"], sub_action = True)
                result &= self.element_ranks_action.apply()
                actions_now.append(self.element_ranks_action)
                if not result:
                    raise StandardError("'Apply' Sub action failed: %s" %  self.element_ranks_action)
        except StandardError:
            Kernel.Log("Exception applying Class Edit Action, will atempt to revert", "[DatabaseAction]", True, True)
            try:
                for action in actions_now:
                    test = action.undo()
                    if not test:
                        raise StandardError("'Apply' Sub action revert failed: %s" % action)
                Kernel.Log("'Apply' Class Edit Action sucessfuly reverted", "[DatabaseAction]", True)
            except StandardError:
                Kernel.Log("Exception reverting failed 'Apply' Class Edit Action, Possible Project coruption", "[DatabaseAction]", True, True)
            result = False
        return result

    def undo_extra(self):
        actions_now = []
        result = True
        try:
            if self.state_ranks_action is not None:
                result &= self.state_ranks_action.undo()
                actions_now.append(self.state_ranks_action)
                if not result:
                    raise StandardError("'Undo' Sub action failed: %s" %  self.state_ranks_action)
            if self.element_ranks_action is not None:
                result &= self.element_ranks_action.undo()
                actions_now.append(self.element_ranks_action)
                if not result:
                    raise StandardError("'Undo' Sub action failed: %s" %  self.element_ranks_action)
        except StandardError:
            Kernel.Log("Exception undoing Class Edit Action, will atempt to revert", "[DatabaseAction]", True, True)
            try:
                for action in actions_now:
                    test = action.apply()
                    if not test:
                        raise StandardError("'Undo' Sub action revert failed: %s" % action)
                Kernel.Log("'Undo' Class Edit Action sucessfuly reverted", "[DatabaseAction]", True)
            except StandardError:
                Kernel.Log("Exception reverting failed 'Undo' Class Edit Action, Possible Project coruption", "[DatabaseAction]", True, True)
        return result
     
class LearningEditAction(DatabaseAction):
    ''' Edits a single Learning object'''

    def __init__(self, obj, data={}, sub_action=False):
        super(LearningEditAction, self).__init__(data, sub_action)
        self.setType("Learning")
        self.setObj(obj)
        self.addKeys("level", "skill_id")
        self.setType("Learning")      

class TroopEditAction(DatabaseAction):
    ''' edits a Troop object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(TroopEditAction, self).__init__(data, sub_action)
        self.setType("Troop")
        self.setObj(obj)
        self.addKeys("id", "name", "members" ,"pages", "note")
     
class SkillEditAction(DatabaseAction):
    ''' edits a Skill object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(SkillEditAction, self).__init__(data,sub_action)
        self.setType("Skill")
        self.setObj(obj)
        self.addKeys("id", "name", "icon_name", "description", "scope", "occasion", "animation1_id", "animation2_id", 
                     "menu_se", "common_event_id", "sp_cost", "power", "atk_f", "eva_f", "str_f", "dex_f", "agi_f",
                     "int_f", "hit", "pdef_f", "mdef_f", "variance", "element_set", "plus_state_set", "minus_state_set", 
                     "note")
          
class WeaponEditAction(DatabaseAction):
    ''' edits a Weapon object'''

    def __init__(self, obj, data={}, sub_action=False):
        super(ClassEditAction, self).__init__(data, sub_action)
        self.setType("Weapon")
        self.setObj(obj)
        self.addKeys("id", "name", "icon_name", "description", "animation1_id", "animation2_id", "price", "atk", "pdef",
                     "mdef", "str_plus", "int_plus", "dex_plus", "agi_plus", "element_set", "plus_state_set", "minus_state_set")
 
class ItemEditActon(DatabaseAction):
    ''' edits a Item object'''

    def __init__(self, obj, data = {}, sub_action=False):
        super(ItemEditActon, self).__init__(data, sub_action)
        self.setType("Item")
        self.setObj(obj)
        self.addKeys('id', 'name', 'icon_name', 'description', 'scope', 'occasion', 'animation1_id',
                     'animation2_id', 'menu_se', 'common_event_id', 'price', 'consumable', 'parameter_type',
                     'parameter_points', 'recover_hp_rate', 'recover_hp', 'recover_sp_rate', 'recover_sp',
                     'hit', 'pdef_f', 'mdef_f', 'variance', 'element_set', 'plus_state_set', 'minus_state_set', 'note')

class AnimationFrameEditAction(DatabaseAction):
    ''' edits a Animation::Frame object '''

    def __init__(self, obj, data = {}, sub_action = False):
        super(AnimationFrameEditAction, self).__init__(data, sub_action)
        self.setType("AnimationFrame")
        self.setObj(obj)
        self.addKeys('cell_max')
        self.cell_data_action = None

    def apply_extra(self):
        result = True
        actions_now = []
        try:
            if self.data.has_key("cell_data"):
                self.cell_data_action = KM.get_component("TableEditAction").object(self.obj.cell_data, self.data["cell_data"], sub_action=True)
                result &= self.cell_data_action.apply()
                actions_now.append(self.cell_data_action)
                if not result:
                    raise StandardError("'Apply' Sub action failed: %s" %  self.cell_data_action)
        except StandardError:
            Kernel.Log("Exception applying Animation Frame Edit Action, will atempt to revert", "[DatabaseAction]", True, True)
            try:
                for action in actions_now:
                    test = action.undo()
                    if not test:
                        raise StandardError("'Apply' Sub action revert failed: %s" % action)
                Kernel.Log("'Apply' Animation Frame Edit Action sucessfuly reverted", "[DatabaseAction]", True)
            except StandardError:
                Kernel.Log("Exception reverting failed 'Apply' Animation Frame Edit Action, Possible Project coruption", "[DatabaseAction]", True, True)
            result = False
        return result

    def undo_extra(self):
        actions_now = []
        result = True
        try:
            if self.cell_data_action is not None:
                result &= self.cell_data_action.undo()
                actions_now.append(self.cell_data_action)
                if not result:
                    raise StandardError("'Undo' Sub action failed: %s" %  self.cell_data_action)
        except StandardError:
            Kernel.Log("Exception undoing Animation Frame Edit Action, will atempt to revert", "[DatabaseAction]", True, True)
            try:
                for action in actions_now:
                    test = action.apply()
                    if not test:
                        raise StandardError("'Undo' Sub action revert failed: %s" % action)
                Kernel.Log("'Undo' Animation Frame Edit Action sucessfuly reverted", "[DatabaseAction]", True)
            except StandardError:
                Kernel.Log("Exception reverting failed 'Undo' Animation Frame Edit Action, Possible Project coruption", "[DatabaseAction]", True, True)
        return result

class AnimationEditAction(DatabaseAction):
    ''' edits an Animation object '''

    def __init__(self, obj, data = {}, sub_action = False):
        super(AnimationEditAction, self).__init__(data, sub_action)
        self.setType("Animation")
        self.setObj(obj)
        self.addKeys('id', 'name', 'animation_name', 'animation_hue', 'position', 'frame_max', 'frames', 'timings')

class AnimationTimingEditAction(DatabaseAction):
    ''' edits an Animation Timing object '''

    def __init__(self, obj, data = {}, sub_action = False):
        super(AnimationTimingEditAction, self).__init__(data, sub_action)
        self.setType("AnimationTiming")
        self.setObj(obj)
        self.addKeys('frame', 'se', 'flash_scope', 'flash_color', 'flash_duration', 'condition')

class AudioFileEditAction(DatabaseAction):
    ''' edits a RPg Audiofile object '''

    def __init__(self, obj, data = {}, sub_action = False):
        super(AudioFileEditAction, self).__init__(data, sub_action)
        self.setType("AudioFile")
        self.setObj(obj)
        self.addKeys('name', 'volume', 'pitch')
        self.element_ranks_action = None
        self.state_ranks_action = None

class EnemyEditAction(DatabaseAction):
    ''' edits an Enemy object'''

    def __init__(self, obj, data = {}, sub_action = False):
        super(EnemyEditAction, self).__init__(data, sub_action)
        self.setType("Enemy")
        self.setObj(obj)
        self.addKeys('id', 'name', 'battler_name', 'battler_hue', 'maxhp', 'maxsp', 'str', 'dex', 'agi', 'int',
                     'atk', 'pdef', 'mdef', 'eva', 'animation1_id', 'animation2_id', 'actions', 'exp', 'gold', 
                     'item_id', 'weapon_id', 'armor_id', 'treasure_prob', 'note')
        self.element_ranks_action = None
        self.state_ranks_action = None

    def apply_extra(self):
        result = True
        actions_now = []
        try:
            if self.data.has_key("element_ranks"):
                self.element_ranks_action = TableEditAction(self.obj.element_ranks, self.data["element_ranks"], sub_action = True)
                result &= self.element_ranks_action.apply()
                actions_now.append(self.element_ranks_action)
                if not result:
                    raise StandardError("'Apply' Sub action failed: %s" %  self.element_ranks_action)
            if self.data.has_key("state_ranks"):
                self.state_ranks_action = TableEditAction(self.obj.state_ranks, self.data["state_ranks"], sub_action = True)
                result &= self.element_ranks_action.apply()
                actions_now.append(self.element_ranks_action)
                if not result:
                    raise StandardError("'Apply' Sub action failed: %s" %  self.element_ranks_action)
        except StandardError:
            Kernel.Log("Exception applying Enemy Edit Action, will atempt to revert", "[DatabaseAction]", True, True)
            try:
                for action in actions_now:
                    test = action.undo()
                    if not test:
                        raise StandardError("'Apply' Sub action revert failed: %s" % action)
                Kernel.Log("'Apply' Enemy Edit Action sucessfuly reverted", "[DatabaseAction]", True)
            except StandardError:
                Kernel.Log("Exception reverting failed 'Apply' Enemy Edit Action, Possible Project coruption", "[DatabaseAction]", True, True)
            result = False
        return result

    def undo_extra(self):
        actions_now = []
        result = True
        try:
            if self.state_ranks_action is not None:
                result &= self.state_ranks_action.undo()
                actions_now.append(self.state_ranks_action)
                if not result:
                    raise StandardError("'Undo' Sub action failed: %s" %  self.state_ranks_action)
            if self.element_ranks_action is not None:
                result &= self.element_ranks_action.undo()
                actions_now.append(self.element_ranks_action)
                if not result:
                    raise StandardError("'Undo' Sub action failed: %s" %  self.element_ranks_action)
        except StandardError:
            Kernel.Log("Exception undoing Enemy Edit Action, will atempt to revert", "[DatabaseAction]", True, True)
            try:
                for action in actions_now:
                    test = action.apply()
                    if not test:
                        raise StandardError("'Undo' Sub action revert failed: %s" % action)
                Kernel.Log("'Undo' Enemy Edit Action sucessfuly reverted", "[DatabaseAction]", True)
            except StandardError:
                Kernel.Log("Exception reverting failed 'Undo' Enemy Edit Action, Possible Project coruption", "[DatabaseAction]", True, True)
        return result

class EnemyActionEditAction(DatabaseAction):
    ''' edits a Enemy::Action object'''

    def __init__(self, obj, data = {}, sub_action = False):
        super(EnemyActionEditAction, self).__init__(data, sub_action)
        self.setType("EnemyAction")
        self.setObj(obj)
        self.addKeys('kind', 'basic', 'skill_id', 'condition_turn_a', 'condition_turn_b', 
                     'condition_hp', 'condition_level', 'condition_switch_id', 'rating')

class EventEditAction(DatabaseAction):
    ''' edits an Event Object '''
    def __init__(self, obj, data = {}, sub_action = False):
        super(EventEditAction, self).__init__(data, sub_action)
        self.setType("Event")
        self.setObj(obj)
        self.addKeys('id', 'name', 'x', 'y', 'pages')

class EventPageEditAction(DatabaseAction):
    ''' edits a Event::Page object '''

    def __init__(self, obj, data = {}, sub_action = False):
        super(EventPageEditAction, self).__init__(data, sub_action)
        self.setType("EventPage")
        self.setObj(obj)
        self.addKeys('condition', 'graphic', 'move_type', 'move_speed', 'move_frequency', 
                     'move_route', 'walk_anime', 'step_anime',  'direction_fix', 'through', 
                     'always_on_top', 'trigger', 'list')

class EventConditionEditAction(DatabaseAction):
    ''' edits a Event::Page::Condition object'''

    def __init__(self, obj, data = {}, sub_action = False):
        super(EventConditionEditAction, self).__init__(data, sub_action)
        self.setType("EventCondition")
        self.setObj(obj)
        self.addKeys('switch1_valid', 'switch2_valid', 'variable_valid', 'self_switch_valid', 'switch1_id', 
                     'switch2_id', 'variable_id', 'variable_value', 'self_switch_ch')

class EventGraphicEditAction(DatabaseAction):
    ''' edits a Event::Page::Graphic '''

    def __init__(self, obj, data = {}, sub_action = False):
        super(EventGraphicEditAction, self).__init__(data, sub_action)
        self.setType("EventGraphic")
        self.setObj(obj)
        self.addKeys('tile_id', 'character_name', 'character_hue', 'direction', 'pattern', 'opacity', 'blend_type')

class EventCommandEditAction(DatabaseAction):
    ''' edits a EventCommand object '''

    def __init__(self, obj, data = {}, sub_action = False):
        super(EventCommandEditAction, self).__init__(data, sub_action)
        self.setType("EventCommand")
        self.setObj(obj)
        self.addKeys('code', 'indent', 'parameters')

class CommonEventEditAction(DatabaseAction):
    ''' edits a CommonEvent object '''

    def __init__(self, obj, data = {}, sub_action = False):
        super(CommonEventEditAction, self).__init__(data, sub_action)
        self.setType("CommonEvent")
        self.setObj(obj)
        self.addKeys('id', 'name', 'trigger', 'switch_id', 'list')

class MapEditAction(DatabaseAction):
    ''' edits a Map object '''

    def __init__(self, obj, data = {}, sub_action = False):
        super(MapEditAction, self).__init__(data, sub_action)
        self.setType("Map")
        self.setObj(obj)
        self.addKeys('tileset_id', 'width', 'height', 'autoplay_bgm', 'bgs', 
                     'encounter_list', 'encounter_step', 'data', 'events')
        self.data_action = None

    def apply_extra(self):
        result = True
        actions_now = []
        try:
            if self.data.has_key("data"):
                self.data_action = TableEditAction(self.obj.data, self.data["data"], sub_action = True)
                result &= self.data_action.apply()
                actions_now.append(self.data_action)
                if not result:
                    raise StandardError("'Apply' Sub action failed: %s" %  self.element_ranks_action)
        except StandardError:
            Kernel.Log("Exception applying Map Edit Action, will atempt to revert", "[DatabaseAction]", True, True)
            try:
                for action in actions_now:
                    test = action.undo()
                    if not test:
                        raise StandardError("'Apply' Sub action revert failed: %s" % action)
                Kernel.Log("'Apply' Map Edit Action sucessfuly reverted", "[DatabaseAction]", True)
            except StandardError:
                Kernel.Log("Exception reverting failed 'Apply' Map Edit Action, Possible Project coruption", "[DatabaseAction]", True, True)
            result = False
        return result

    def undo_extra(self):
        actions_now = []
        result = True
        try:
            if self.data_action is not None:
                result &= self.data_action.undo()
                actions_now.append(self.data_action)
                if not result:
                    raise StandardError("'Undo' Sub action failed: %s" %  self.state_ranks_action)
        except StandardError:
            Kernel.Log("Exception undoing Map Edit Action, will atempt to revert", "[DatabaseAction]", True, True)
            try:
                for action in actions_now:
                    test = action.apply()
                    if not test:
                        raise StandardError("'Undo' Sub action revert failed: %s" % action)
                Kernel.Log("'Undo' Map Edit Action sucessfuly reverted", "[DatabaseAction]", True)
            except StandardError:
                Kernel.Log("Exception reverting failed 'Undo' Map Edit Action, Possible Project coruption", "[DatabaseAction]", True, True)
        return result

class MapInfoEditAction(DatabaseAction):
    ''' edits a Mapinfo object'''
    def __init__(self, obj, data = {}, sub_action = False):
        super(MapInfoEditAction, self).__init__(data, sub_action)
        self.setType("MapInfo")
        self.setObj(obj)
        self.addKeys('name', 'parent_id', 'order', 'expanded', 'scroll_x', 'scroll_y')

class MoveCommandEditAction(DatabaseAction):
    ''' edits a MoveCommand object '''

    def __init__(self, obj, data = {}, sub_action = False):
        super(MoveCommandEditAction, self).__init__(data, sub_action)
        self.setType("MoveCommand")
        self.setObj(obj)
        self.addKeys('code', 'parameters')

class MoveRouteEditAction(DatabaseAction):
    ''' edits a MoveRoute object '''
    def __init__(self, obj, data = {}, sub_action = False):
        super(MoveRouteEditAction, self).__init__(data, sub_action)
        self.setType("MoveRoute")
        self.setObj(obj)
        self.addKeys('repeat', 'skippable', 'list')

class StateEditAction(DatabaseAction):
    ''' edits a State object '''

    def __init__(self, obj, data = {}, sub_action = False):
        super(StateEditAction, self).__init__(data, sub_action)
        self.setType("State")
        self.setObj(obj)
        self.addKeys('id', 'name', 'animation_id', 'restriction', 'nonresistance', 'zero_hp', 'cant_get_exp', 'cant_evade', 
                     'slip_damage', 'rating', 'hit_rate', 'maxhp_rate', 'maxsp_rate', 'str_rate', 'dex_rate', 'int_rate', 
                     'atk_rate', 'pdef_rate', 'mdef_rate', 'eva', 'battle_only', 'hold_turn', 'auto_release_prob', 
                     'shock_release_prob', 'guard_element_set', 'plus_state_set', 'minus_state_set', 'note')

class SystemEditAction(DatabaseAction):
    ''' edits a System object '''
    def __init__(self, obj, data = {}, sub_action = False):
        super(SystemEditAction, self).__init__(data, sub_action)
        self.setType("System")
        self.setObj(obj)
        self.addKeys('magic_number', 'party_members', 'elements', 'switches', 'variables', 'windowskin_name', 'title_name', 
                     'gameover_name',  'battle_transition', 'title_bgm', 'battle_bgm', 'battle_end_me', 'gameover_me', 
                     'cursor_se', 'decision_se', 'cancel_se', 'buzzer_se', 'equip_se', 'shop_se', 'save_se', 'load_se', 
                     'battle_start_se', 'escape_se', 'actor_collapse_se', 'words', 'test_battlers', 'test_troop_id', 
                     'start_map_id', 'start_x', 'start_y', 'battleback_name', 'battler_name', 'battler_hue', 'edit_map_id')

class TestBattlerEditAction(DatabaseAction):
    ''' edits a TestBattler object '''

    def __init__(self, obj, data = {}, sub_action = False):
        super(TestBattlerEditAction, self).__init__(data, sub_action)
        self.setType("TestBattler")
        self.setObj(obj)
        self.addKeys('actor_id', 'level', 'weapon_id', 'armor1_id', 'armor2_id', 'armor3_id', 'armor4_id')

class WordsEditAction(DatabaseAction):
    ''' edits a System::Words object '''

    def __init__(self, obj, data = {}, sub_action = False):
        super(WordsEditAction, self).__init__(data, sub_action)
        self.setType("Words")
        self.setObj(obj)
        self.addKeys('gold', 'hp', 'sp', 'str', 'dex', 'agi', 'int', 'atk', 'pdef', 'mdef', 'weapon', 
                     'armor1', 'armor2', 'armor3', 'armor4', 'attack', 'skill', 'guard', 'item', 'equip')

class TilesetEditAction(DatabaseAction):
    ''' edits a Tileset object '''

    def __init__(self, obj, data = {}, sub_action = False):
        super(TilesetEditAction, self).__init__(data, sub_action)
        self.setType("Tileset")
        self.setObj(obj)
        self.addKeys('id', 'name', 'tileset_name', 'autotile_names', 'panorama_name', 'panorama_hue', 
                     'fog_name', 'fog_hue', 'fog_opacity', 'fog_blend_type', 'fog_zoom', 'fog_sx', 
                     'fog_sy', 'battleback_name')
        self.passages_action = None
        self.priorities_action = None
        self.terrain_tags_action = None

    def apply_extra(self):
        result = True
        actions_now = []
        try:
            if self.data.has_key("passages"):
                self.passages_action = TableEditAction(self.obj.passages, self.data["passages"], sub_action = True)
                result &= self.passages_action.apply()
                actions_now.append(self.passages_action)
                if not result:
                    raise StandardError("'Apply' Sub action failed: %s" %  self.element_ranks_action)
            if self.data.has_key("priorities"):
                self.priorities_action = TableEditAction(self.obj.priorities, self.data["priorities"], sub_action = True)
                result &= self.priorities_action.apply()
                actions_now.append(self.priorities_action)
                if not result:
                    raise StandardError("'Apply' Sub action failed: %s" %  self.element_ranks_action)
            if self.data.has_key("terrain_tags"):
                self.terrain_tags_action = TableEditAction(self.obj.terrain_tags, self.data["terrain_tags"], sub_action = True)
                result &= self.terrain_tags_action.apply()
                actions_now.append(self.terrain_tags_action)
                if not result:
                    raise StandardError("'Apply' Sub action failed: %s" %  self.element_ranks_action)
        except StandardError:
            Kernel.Log("Exception applying Tileset Edit Action, will atempt to revert", "[DatabaseAction]", True, True)
            try:
                for action in actions_now:
                    test = action.undo()
                    if not test:
                        raise StandardError("'Apply' Sub action revert failed: %s" % action)
                Kernel.Log("'Apply' Tileset Edit Action sucessfuly reverted", "[DatabaseAction]", True)
            except StandardError:
                Kernel.Log("Exception reverting failed 'Apply' Tileset Edit Action, Possible Project coruption", "[DatabaseAction]", True, True)
            result = False
        return result

    def undo_extra(self):
        actions_now = []
        result = True
        try:
            if self.passages_action is not None:
                result &= self.passages_action.undo()
                actions_now.append(self.passages_action)
                if not result:
                    raise StandardError("'Undo' Sub action failed: %s" %  self.state_ranks_action)
            if self.priorities_action is not None:
                result &= self.priorities_action.undo()
                actions_now.append(self.priorities_action)
                if not result:
                    raise StandardError("'Undo' Sub action failed: %s" %  self.element_ranks_action)
            if self.terrain_tags_action is not None:
                result &= self.terrain_tags_action.undo()
                actions_now.append(self.terrain_tags_action)
                if not result:
                    raise StandardError("'Undo' Sub action failed: %s" %  self.element_ranks_action)
        except StandardError:
            Kernel.Log("Exception undoing Tileset Edit Action, will atempt to revert", "[DatabaseAction]", True, True)
            try:
                for action in actions_now:
                    test = action.apply()
                    if not test:
                        raise StandardError("'Undo' Sub action revert failed: %s" % action)
                Kernel.Log("'Undo' Tileset Edit Action sucessfuly reverted", "[DatabaseAction]", True)
            except StandardError:
                Kernel.Log("Exception reverting failed 'Undo' Tileset Edit Action, Possible Project coruption", "[DatabaseAction]", True, True)
        return result

class TroopPageEditAction(DatabaseAction):
    ''' edits a Troop::Page object '''

    def __init__(self, obj, data = {}, sub_action = False):
        super(TroopPageEditAction, self).__init__(data, sub_action)
        self.setType("TroopPage")
        self.setObj(obj)
        self.addKeys('span', 'list')

class TroopConditionEditAction(DatabaseAction):
    ''' edits a Troop::Condition'''

    def __init__(self, obj, data = {}, sub_action = False):
        super(TroopConditionEditAction, self).__init__(data, sub_action)
        self.setType("TroopCondition")
        self.setObj(obj)
        self.addKeys('turn_valid', 'enemy_valid', 'actor_valid', 'switch_valid', 'turn_a', 
                     'turn_b', 'enemy_index', 'enemy_hp', 'actor_id', 'actor_hp', 'switch_id')

class MemberEditAction(DatabaseAction):
    ''' edits a Troop::Member object '''

    def __init__(self, obj, data = {}, sub_action = False):
        super(MemberEditAction, self).__init__(data, sub_action)
        self.setType("Member")
        self.setObj(obj)
        self.addKeys('enemy_id', 'x', 'y', 'hidden', 'immortal')
