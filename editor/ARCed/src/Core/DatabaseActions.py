import types
import numpy

import Kernel
from Kernel import Manager as KM

import Actions

class TableEditAction(Actions.ActionTemplate):

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
        #TODO: implement this function
        # data = { "dim": 1-3, "index": a tuple of list of len dim that looks like so (x, y, z), "value": the python list or preferably numpy array /value to set the table too
        # for a slice ((x1,x2), (y1,y2), (z1,z2))) or for a slice with a step ((x1,x2,xstep), (y1,y2,ystep), (z1,z2,zstep)) 
        # the values in a slice may be none just like in real slice notation ie.
        # [::2, 0, 0] (every other value in the array) would look like ((None,None,2), 0, 0) 
        # remember Tables are basically a dimension limited numpy array of of dtype int17 use numpy. they indexing so look at the numpy documentation for more information
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
            raise ArgumentError("new dimension and table old dimension must be the same (%d for %d)" % (len(shape), len(self.table.getShape())))
        self.oldvalue = numpy.copy(self.table._data)
        self.table.resize(*shape)

    def normal_apply(self):
        dim = self.data['dim']
        index = self.data['index']
        value = self.data['value']
        if dim > 3:
            raise ArgumentError("dim can't be less than 0")
        if dim < 0:
            raise ArgumentError("dim can't be greater than 3 or less than 0")
        if isinstance(index, int):
            if dim > 1:
                raise ArgumentError("wrong number of arguments (%d for %d)" % (1, dim))
            else:
                self.oldvalue = numpy.copy(self.table[index])
                self.table[index] = value
        elif len(index) != dim:
            raise ArgumentError("wrong number of arguments (%d for %d)" % (len(index), dim))
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
            raise ArgumentError("wrong number of arguments (%d for %d)" % (len(index), dim))
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
            raise ArgumentError("new dimension and table old dimension must be the same (%d for %d)" % (len(shape), len(self.table.getShape())))
        self.table._data[:] = self.oldvalue[:]

    def normal_undo(self):
        dim = self.data['dim']
        index = self.data['index']
        if dim > 3:
            raise ArgumentError("dim can't be less than 0")
        if dim < 0:
            raise ArgumentError("dim can't be greater than 3 or less than 0")
        if isinstance(index, int):
            if dim > 1:
                raise ArgumentError("wrong number of arguments (%d for %d)" % (1, dim))
            else:
                self.data['value'] = self.table[index]
                self.table[index] = self.oldvalue
        elif len(index) != dim:
            raise ArgumentError("wrong number of arguments (%d for %d)" % (len(index), dim))
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
            raise ArgumentError("wrong number of arguments (%d for %d)" % (len(index), dim))
        return True

class LearningEditAction(Actions.ActionTemplate):
    def __init__(self, id, index, data={}, sub_action=False):
        super(LearningEditAction, self).__init__(sub_action)
        if not isinstance(data, types.DictType):
            raise TypeError("Error: Expected dict type for 'data'")
        elif not isinstance(id, types.IntType):
            raise TypeError("Error: Expected int type for 'id'")
        else:
            self.id = id
            self.index = index
            self.data = data
            self.old_data = {}
            
            
    def do_apply(self):
        if Kernel.GlobalObjects.has_key("PROJECT"):
            project = Kernel.GlobalObjects.get_value("PROJECT")
            if project is not None:
                klass = project.getData("Classes")[self.id]
                if klass is not None:
                    if self.data.has_key("level"):
                        self.old_data["level"] = klass.learnings[self.index].level
                        klass.learnings[self.index].level = self.data["level"]
                    if self.data.has_key("skill_id"):
                        self.old_data["skill_id"] = klass.learnings[self.index].skill_id
                        klass.learnings[self.index].level = self.data["skill_id"]
                    return True
                else:
                    return False
            else:
                return False
                
                
    def do_undo(self):
        if Kernel.GlobalObjects.has_key("PROJECT"):
            project = Kernel.GlobalObjects.get_value("PROJECT")
            if project is not None:
                klass = project.getData("Classes")[self.id]
                if klass is not None:
                    if self.old_data.has_key("level"):
                        self.data["level"] = klass.learnings[self.index].level
                        klass.learnings[self.index].level = self.old_data["level"]
                    if self.old_data.has_key("skill_id"):
                        self.data["skill_id"] = klass.learnings[self.index].skill_id
                        klass.learnings[self.index].level = self.old_data["skill_id"]
                    return True
                else:
                    return False
            else:
                return False
                
class LearningsEditAction(Actions.ActionTemplate):

    def __init__(self, id, data={}, sub_action=False):
        super(LearningsEditAction, self).__init__(sub_action)
        if not isinstance(data, types.DictType):
            raise TypeError("Error: Expected dict type for 'data'")
        elif not isinstance(id, types.IntType):
            raise TypeError("Error: Expected int type for 'id'")
        else:
            self.id = id
            self.data = data
            self.old_data = {}
            self.learning_actions = []
    
    def do_apply(self):
        if Kernel.GlobalObjects.has_key("PROJECT"):
            project = Kernel.GlobalObjects.get_value("PROJECT")
            if project is not None:
                klass = project.getData("Classes")[self.id]
                if klass is not None:
                    if self.data.has_key("learnings"):
                        self.old_data = klass.learnings
                        for i in range(len(self.data["learnings"])):
                            learning = {"level" : self.data["learnings"][i].level, "skill_id" : self.data["learnings"][i].skill_id}
                            self.learning_actions[i] = LearningEditAction(self.id, i, learning, sub_action=True)
                            self.learning_actions[i].apply();
                    return True
                else:
                    return False
            else:
                return False
                        
                        
    def do_undo(self):
        if Kernel.GlobalObjects.has_key("PROJECT"):
            project = Kernel.GlobalObjects.get_value("PROJECT")
            if project is not None:
                klass = project.getData("Classes")[self.id]
                if klass is not None:
                    if self.old_data.has_key("learnings"):
                        self.data = klass.learnings
                        for i in range(len(self.old_data["learnings"])):
                            if self.learning_actions[i] is not None:
                                self.learning_actions[i].undo()
                    return True
                else:
                    return False
            else:
                return False
            
class ArmorEditAction(Actions.ActionTemplate):

    def __init__(self, id, data={}, sub_action=False):
        super(ArmorEditAction, self).__init__(sub_action)
        if not isinstance(data, types.DictType):
            raise TypeError("Error: Expected dict type for 'data'")
        elif not isinstance(id, types.IntType):
            raise TypeError("Error: Expected int type for 'id'")
        else:
            self.id = id
            self.data = data
            self.old_data = {}
            
    def do_apply(self):
        if Kernel.GlobalObjects.has_key("PROJECT"):
            project = Kernel.GlobalObjects.get_value("PROJECT")
            if project is not None:
                armors = project.getData("Armors")
                if armors is not None:
                    armor = armors[self.id]
                    if armor is not None:
                        if self.data.has_key("id"):
                            self.old_data["id"] = armor.id
                            actor.id = self.data["id"]
                        if self.data.has_key("name"):
                            self.old_data["name"] = armor.name
                            armor.name = self.data["name"]
                        if self.data.has_key("icon_name"):
                            self.old_data["icon_name"] = armor.icon_name
                            armor.icon_name = self.data["icon_name"]
                        if self.data.has_key("description"):
                            self.old_data["description"] = armor.description
                            armor.description = self.data["description"]
                        if self.data.has_key("kind"):
                            self.old_data["kind"] = armor.kind
                            armor.kind = self.data["kind"]
                        if self.data.has_key("auto_state_id"):
                            self.old_data["auto_state_id"] = armor.auto_state_id
                            armor.auto_state_id = self.data["armor_state_id"]
                        if self.data.has_key("price"):
                            self.old_data["price"] = armor.price
                            armor.price = self.data["price"]
                        if self.data.has_key("pdef"):
                            self.old_data["pdef"] = armor.pdef
                            armor.pdef = self.data["pdef"]
                        if self.data.has_key("mdef"):
                            self.old_data["mdef"] = armor.mdef
                            armor.mdef = self.data["mdef"]
                        if self.data.has_key("eva"):
                            self.old_data["eva"] = armor.eva
                            armor.eva = self.data["eva"]
                        if self.data.has_key("str_plus"):
                            self.old_data["str_plus"] = armor.str_plus
                            armor.str_plus = self.data["str_plus"]
                        if self.data.has_key("dex_plus"):
                            self.old_data["dex_plus"] = armor.dex_plus
                            armor.dex_plus = self.data["dex_plus"]
                        if self.data.has_key("agi_plus"):
                            self.old_data["agi_plus"] = armor.agi_plus
                            armor.agi_plus = self.data["agi_plus"]
                        if self.data.has_key("int_plus"):
                            self.old_data["int_plus"] = armor.int_plus
                            armor.int_plus = self.data["int_plus"]
                        if self.data.has_key("guard_element_set"):
                            self.old_data["guard_element_set"] = armor.guard_element_set
                            armor.guard_element_set = self.data["guard_element_set"]
                        if self.data.has_key("guard_state_set"):
                            self.old_data["guard_state_set"] = armor.guard_state_set
                            armor.guard_state_set = self.data["guard_state_set"]
                        return True
                    else:
                        Kernel.log("Warning: ArmorEditAction apply not completed successfully, Armor ID %s is none" % self.id, "[ArmorEditAction]")
                        return False
                else:
                     Kernel.log("Warning: ArmorEditAction apply not completed successfully, Armors array from project is none", "[ArmorEditAction]")
                     return False
            else:
                Kernel.log("Warning: ArmorEditAction apply not completed successfully, Project is None", "[ArmorEditAction]")
                return False
    
    def do_undo(self):
        if Kernel.GlobalObjects.has("PROJECT"):
            project = Kernel.GlobalObjects.get_value("PROJECT")
            if project is not None:
                armors = project.getData("Armors")
                if classes is not None:
                    armor = armors[self.id]
                    if armor is not None:
                        if self.old_data.has_key("id"):
                            self.data["id"] = armor.id
                            actor.id = self.old_data["id"]
                        if self.old_data.has_key("name"):
                            self.data["name"] = armor.name
                            armor.name = self.old_data["name"]
                        if self.old_data.has_key("icon_name"):
                            self.data["icon_name"] = armor.icon_name
                            armor.icon_name = self.old_data["icon_name"]
                        if self.old_data.has_key("description"):
                            self.data["description"] = armor.description
                            armor.description = self.old_data["description"]
                        if self.old_data.has_key("kind"):
                            self.data["kind"] = armor.kind
                            armor.kind = self.old_data["kind"]
                        if self.old_data.has_key("auto_state_id"):
                            self.data["auto_state_id"] = armor.auto_state_id
                            armor.auto_state_id = self.old_data["armor_state_id"]
                        if self.old_data.has_key("price"):
                            self.data["price"] = armor.price
                            armor.price = self.old_data["price"]
                        if self.data.has_key("pdef"):
                            self.data["pdef"] = armor.pdef
                            armor.pdef = self.old_data["pdef"]
                        if self.old_data.has_key("mdef"):
                            self.data["mdef"] = armor.mdef
                            armor.mdef = self.old_data["mdef"]
                        if self.old_data.has_key("eva"):
                            self.data["eva"] = armor.eva
                            armor.eva = self.old_data["eva"]
                        if self.old_data.has_key("str_plus"):
                            self.data["str_plus"] = armor.str_plus
                            armor.str_plus = self.old_data["str_plus"]
                        if self.old_data.has_key("dex_plus"):
                            self.data["dex_plus"] = armor.dex_plus
                            armor.dex_plus = self.old_data["dex_plus"]
                        if self.old_data.has_key("agi_plus"):
                            self.data["agi_plus"] = armor.agi_plus
                            armor.agi_plus = self.old_data["agi_plus"]
                        if self.old_data.has_key("int_plus"):
                            self.data["int_plus"] = armor.int_plus
                            armor.int_plus = self.old_data["int_plus"]
                        if self.old_data.has_key("guard_element_set"):
                            self.data["guard_element_set"] = armor.guard_element_set
                            armor.guard_element_set = self.old_data["guard_element_set"]
                        if self.old_data.has_key("guard_state_set"):
                            self.data["guard_state_set"] = armor.guard_state_set
                            armor.guard_state_set = self.old_data["guard_state_set"]
                        return True
                    else:
                        Kernel.log("Warning: ArmorEditAction apply not completed successfully, Armor ID %s is none" % self.id, "[ArmorEditAction]")
                        return False
                else:
                     Kernel.log("Warning: ArmorEditAction apply not completed successfully, Armors array from project is none", "[ArmorEditAction]")
                     return False
            else:
                Kernel.log("Warning: ArmorEditAction apply not completed successfully, Project is None", "[ArmorEditAction]")
                return False
                     
class ActorEditAction(Actions.ActionTemplate):

    def __init__(self, id, data={}, sub_action=False):
        super(ActorEditAction, self).__init__(sub_action)
        if not isinstance(data, types.DictType):
            raise TypeError("Error: Expected dict type for 'data'")
        elif not isinstance(id, types.IntType):
            raise TypeError("Error: Expected int type for 'id'")
        else:
            self.id = id
            self.data = data
            self.old_data = {}
            self.parameters_action = None

    def do_apply(self):
        if Kernel.GlobalObjects.has_key("PROJECT"):
            project = Kernel.GlobalObjects.get_value("PROJECT")
            if project is not None:
                actors = project.getData("Actors")
                if actors is not None:
                    actor = actors[self.id]
                    if actor is not None:
                        if self.data.has_key("id"):
                            self.old_data["id"] = actor.id
                            actor.id = self.data["id"]
                        if self.data.has_key("name"):
                            self.old_data["name"] = actor.name
                            actor.name = self.data["name"]
                        if self.data.has_key("initial_level"):
                            self.old_data["initial_level"] = actor.initial_level
                            actor.initial_level = self.data["initial_level"]
                        if self.data.has_key("final_level"):
                            self.old_data["final_level"] = actor.final_level
                            actor.final_level = self.data["final_level"]
                        if self.data.has_key("exp_basis"):
                            self.old_data["exp_basis"] = actor.exp_basis
                            actor.exp_basis = self.data["exp_basis"]
                        if self.data.has_key("exp_inflation"):
                            self.old_data["exp_inflation"] = actor.exp_inflation
                            actor.exp_inflation = self.data["exp_inflation"]
                        if self.data.has_key("character_name"):
                            self.old_data["character_name"] = actor.character_name
                            actor.character_name = self.data["character_name"]
                        if self.data.has_key("character_hue"):
                            self.old_data["character_hue"] = actor.character_hue
                            actor.character_hue = self.data["character_hue"]
                        if self.data.has_key("battler_name"):
                            self.old_data["battler_name"] = actor.battler_name
                            actor.battler_name = self.data["battler_name"]
                        if self.data.has_key("battler_hue"):
                            self.old_data["battler_hue"] = actor.battler_hue
                            actor.battler_hue = self.data["battler_hue"]
                        if self.data.has_key("parameters"):
                            self.parameters_action = KM.get_component("TableEditAction").object(actor.parameters, self.data["parameters"], sub_action=True)
                            self.parameters_action.apply()
                        if self.data.has_key("weapon_id"):
                            self.old_data["weapon_id"] = actor.weapon_id
                            actor.weapon_id = self.data["weapon_id"]
                        if self.data.has_key("armor1_id"):
                            self.old_data["armor1_id"] = actor.armor1_id
                            actor.armor1_id = self.data["armor1_id"]
                        if self.data.has_key("armor2_id"):
                            self.old_data["armor2_id"] = actor.armor2_id
                            actor.armor2_id = self.data["armor2_id"]
                        if self.data.has_key("armor3_id"):
                            self.old_data["armor3_id"] = actor.armor3_id
                            actor.armor3_id = self.data["armor3_id"]
                        if self.data.has_key("armor4_id"):
                            self.old_data["armor4_id"] = actor.armor4_id
                            actor.armor4_id = self.data["armor4_id"]
                        if self.data.has_key("weapon_fix"):
                            self.old_data["weapon_fix"] = actor.weapon_fix
                            actor.weapon_fix = self.data["weapon_fix"]
                        if self.data.has_key("armor1_fix"):
                            self.old_data["armor1_fix"] = actor.armor1_fix
                            actor.armor1_fix = self.data["armor1_fix"]
                        if self.data.has_key("armor2_fix"):
                            self.old_data["armor2_fix"] = actor.armor2_fix
                            actor.armor2_fix = self.data["armor2_fix"]
                        if self.data.has_key("armor3_fix"):
                            self.old_data["armor3_fix"] = actor.armor3_fix
                            actor.armor3_fix = self.data["armor3_fix"]
                        if self.data.has_key("armor4_fix"):
                            self.old_data["armor4_fix"] = actor.armor4_fix
                            actor.armor4_fix = self.data["armor4_fix"]
                        return True
                    else:
                        Kernel.log("Warning: ActorEditAction apply not completed successfully, Actor ID %s is none" % self.id, "[ActorEditAction]")
                        return False
                else:
                     Kernel.log("Warning: ActorEditAction apply not completed successfully, Actors array from project is none", "[ActorEditAction]")
                     return False
            else:
                Kernel.log("Warning: ActorEditAction apply not completed successfully, Project is None", "[ActorEditAction]")
                return False

    def do_undo(self):
        if Kernel.GlobalObjects.has_key("PROJECT"):
            project = Kernel.GlobalObjects.get_value("PROJECT")
            if project is not None:
                actors = project.getData("Actors")
                if actors is not None:
                    actor = actors[self.id]
                    if actor is not None:
                        if self.old_data.has_key("id"):
                            self.data["id"] = actor.id
                            actor.id = self.old_data["id"]
                        if self.old_data.has_key("name"):
                            self.data["name"] = actor.name
                            actor.name = self.old_data["name"]
                        if self.old_data.has_key("initial_level"):
                            self.data["initial_level"] = actor.initial_level
                            actor.initial_level = self.old_data["initial_level"]
                        if self.old_data.has_key("final_level"):
                            self.data["final_level"] = actor.final_level
                            actor.final_level = self.old_data["final_level"]
                        if self.old_data.has_key("exp_basis"):
                            self.data["exp_basis"] = actor.exp_basis
                            actor.exp_basis = self.old_data["exp_basis"]
                        if self.old_data.has_key("exp_inflation"):
                            self.data["exp_inflation"] = actor.exp_inflation
                            actor.exp_inflation = self.old_data["exp_inflation"]
                        if self.old_data.has_key("character_name"):
                            self.data["character_name"] = actor.character_name
                            actor.character_name = self.old_data["character_name"]
                        if self.old_data.has_key("character_hue"):
                            self.data["character_hue"] = actor.character_hue
                            actor.character_hue = self.old_data["character_hue"]
                        if self.old_data.has_key("battler_name"):
                            self.data["battler_name"] = actor.battler_name
                            actor.battler_name = self.old_data["battler_name"]
                        if self.old_data.has_key("battler_hue"):
                            self.data["battler_hue"] = actor.battler_hue
                            actor.battler_hue = self.old_data["battler_hue"]
                        if self.parameters_action is not None:
                            self.parameters_action.undo()
                        if self.old_data.has_key("weapon_id"):
                            self.data["weapon_id"] = actor.weapon_id
                            actor.weapon_id = self.old_data["weapon_id"]
                        if self.old_data.has_key("armor1_id"):
                            self.data["armor1_id"] = actor.armor1_id
                            actor.armor1_id = self.old_data["armor1_id"]
                        if self.old_data.has_key("armor2_id"):
                            self.data["armor2_id"] = actor.armor2_id
                            actor.armor2_id = self.old_data["armor2_id"]
                        if self.old_data.has_key("armor3_id"):
                            self.data["armor3_id"] = actor.armor3_id
                            actor.armor3_id = self.old_data["armor3_id"]
                        if self.old_data.has_key("armor4_id"):
                            self.data["armor4_id"] = actor.armor4_id
                            actor.armor4_id = self.old_data["armor4_id"]
                        if self.old_data.has_key("weapon_fix"):
                            self.data["weapon_fix"] = actor.weapon_fix
                            actor.weapon_fix = self.old_data["weapon_fix"]
                        if self.old_data.has_key("armor1_fix"):
                            self.data["armor1_fix"] = actor.armor1_fix
                            actor.armor1_fix = self.old_data["armor1_fix"]
                        if self.old_data.has_key("armor2_fix"):
                            self.data["armor2_fix"] = actor.armor2_fix
                            actor.armor2_fix = self.old_data["armor2_fix"]
                        if self.old_data.has_key("armor3_fix"):
                            self.data["armor3_fix"] = actor.armor3_fix
                            actor.armor3_fix = self.old_data["armor3_fix"]
                        if self.old_data.has_key("armor4_fix"):
                            self.data["armor4_fix"] = actor.armor4_fix
                            actor.armor4_fix = self.old_data["armor4_fix"]
                        return True
                    else:
                        Kernel.log("Warning: ActorEditAction undo not completed successfully, Actor ID %s is none" % self.id, "[ActorEditAction]")
                        return False
                else:
                     Kernel.log("Warning: ActorEditAction undo not completed successfully, Actors array from project is none", "[ActorEditAction]")
                     return False
            else:
                Kernel.log("Warning: ActorEditAction undo not completed successfully, Project is None", "[ActorEditAction]")
                return False
                                               
class ClassEditAction(Actions.ActionTemplate):
    def __init__(self, id, data={}, sub_action=False):
        super(ClassEditAction, self).__init__(sub_action)
        if not isinstance(data, types.DictType):
            raise TypeError("Error: Expected dict type for 'data'")
        elif not isinstance(id, types.IntType):
            raise TypeError("Error: Expected int type for 'id'")
        else:
            self.id = id
            self.data = data
            self.old_data = {}
            self.element_ranks_action = None
            self.state_ranks_action = None
            self.learnings_action = None
            
    def do_apply(self):
        if Kernel.GlobalObjects.has_key("PROJECT"):
            project = Kernel.GlobalObjects.get_value("PROJECT")
            if project is not None:
                classes = project.getData("Classes")
                if classes is not None:
                    klass = classes[self.id]
                    if klass is not None:
                        if self.data.has_key("id"):
                            self.old_data["id"] = klass.id
                            klass.id = self.data["id"]
                        if self.data.has_key("name"):
                            self.old_data["name"] = klass.name
                            klass.name = self.data["name"]
                        if self.data.has_key("position"):
                            self.old_data["position"] = klass.position
                            klass.position = self.data["position"]
                        if self.data.has_key("weapon_set"):
                            self.old_data["weapon_set"] = klass.weapon_set
                            klass.weapon_set = self.data["weapon_set"]
                        if self.data.has_key("armor_set"):
                            self.old_data["armor_set"] = klass.armor_set
                            klass.armor_set = self.data["armor_set"]
                        if self.data.has_key("learnings"):
                            self.learnings_action = LearningsEditAction(self.id, data={"learnings" : self.data["learnings"]}, sub_action=True)
                            self.learnings_action.apply()
                        if self.data.has_key("element_ranks"):
                            self.element_ranks_action = TableEditAction(actor.element_ranks, self.data["element_ranks"], sub_action = True)
                            self.element_ranks_action.apply()
                        if self.data.has_key("state_ranks"):
                            self.state_ranks_action = TableEditAction(actor.state_ranks, self.data["state_ranks"], sub_action = True)
                            self.state_ranks_action.apply()
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
    
    def do_undo(self):
        if Kernel.GlobalObjects.has_key("PROJECT"):
            project = Kernel.GlobalObjects.get_value("PROJECT")
            if project is not None:
                classes = project.getData("Classes")
                if classes is not None:
                    klass = classes[self.id]
                    if klass is not None:
                        if self.old_data.has_key("id"):
                            self.data["id"] = klass.id
                            klass.id = self.old_data["id"]
                        if self.old_data.has_key("name"):
                            self.data["name"] = klass.name
                            klass.name = self.old_data["name"]
                        if self.old_data.has_key("position"):
                            self.data["position"] = klass.position
                            klass.position = self.old_data["position"]
                        if self.learnings_action is not None:
                            self.learnings_action.undo()
                        if self.old_data.has_key("weapon_set"):
                            self.data["weapon_set"] = klass.weapon_set
                            klass.weapon_set = self.old_data["weapon_set"]
                        if self.old_data.has_key("armor_set"):
                            self.data["armor_set"] = klass.armor_set
                            klass.armor_set = self.old_data["armor_set"]
                        if self.state_ranks_action is not None:
                            self.state_ranks_action.undo()
                        if self.element_ranks_action is not None:
                            self.element_ranks_action.undo()
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
     


class TroopEditAction(Actions.ActionTemplate):
    def __init(self, id, data={}, sub_action=False):
        super(TroopEditAction, self).__init__(sub_action)
        if not isinstance(data, types.DictType):
            raise TypeError("Error: Expected dict type for 'data'")
        elif not isinstance(id, types.IntType):
            raise TypeError("Error: Expected int type for 'id'")
        else:
            self.id = id
            self.data = data
            self.old_data = {}
            
            
            
    def do_apply():
        if Kernel.GlobalObjects.has_key("PROJECT"):
            project = Kernel.GlobalObjects.get_value("PROJECT")
            if project is not None:
                troops = project.getData("Troops")
                if troops is not None:
                    troop = troops[self.id]
                    if troop is not None:
                        if self.data.has_key("id"):
                            self.old_data["id"] = troop.id
                            troop.id = self.data["id"]
                        if self.data.has_key("name"):
                            self.old_data["name"] = troop.name
                            troop.name = self.data["name"]
                        if self.data.has_key("members"):
                            self.old_data["members"] = troop.members
                            troop.members = self.data["members"]
                        if self.data.has_key("pages"):
                            self.old_data["pages"] = troop.pages
                            troop.pages = self.data["pages"]
                        if self.data.has_key("note"):
                            self.old_data["note"] = troop.note
                            troop.note = self.data["note"]
    def do_apply():
        if Kernel.GlobalObjects.has_key("PROJECT"):
            project = Kernel.GlobalObjects.get_value("PROJECT")
            if project is not None:
                troops = project.getData("Troops")
                if troops is not None:
                    troop = troops[self.id]
                    if troop is not None:
                        if self.old_data.has_key("id"):
                            self.data["id"] = troop.id
                            troop.id = self.old_data["id"]
                        if self.old_data.has_key("name"):
                            self.data["name"] = troop.name
                            troop.name = self.old_data["name"]
                        if self.old_data.has_key("members"):
                            self.data["members"] = troop.members
                            troop.members = self.old_data["members"]
                        if self.old_data.has_key("pages"):
                            self.data["pages"] = troop.pages
                            troop.pages = self.old_data["pages"]
                        if self.old_data.has_key("note"):
                            self.data["note"] = troop.note
                            troop.note = self.old_data["note"]
     
class SkillEditAction(Actions.ActionTemplate):
    def __init(self, id, data={}, sub_action=False):
        super(SkillEditAction, self).__init__(sub_action)
        if not isinstance(data, types.DictType):
            raise TypeError("Error: Expected dict type for 'data'")
        elif not isinstance(id, types.IntType):
            raise TypeError("Error: Expected int type for 'id'")
        else:
            self.id = id
            self.data = data
            self.old_data = {}
            
    def do_apply(self):
        if Kernel.GlobalObjects.has_key("PROJECT"):
            project = Kernel.GlobalObjects.get_value("PROJECT")
            if project is not None:
                skills = project.getData("Skills")
                if skills is not None:
                    skill = skills[self.id]
                    if skill is not None:
                        if self.data.has_key("id"):
                            self.old_data["id"] = skill.id
                            skill.id = self.data["id"]
                        if self.data.has_key("name"):
                            self.old_data["name"] = skill.name
                            skill.name = self.data["name"]
                        if self.data.has_key("icon_name"):
                            self.old_data["icon_name"] = skill.icon_name
                            skill.icon_name = self.data["icon_name"]
                        if self.data.has_key("description"):
                            self.old_data["description"] = skill.description
                            skill.description = self.data["description"]
                        if self.data.has_key("scope"):
                            self.old_data["scope"] = skill.scope
                            skill.scope = self.data["scope"]
                        if self.data.has_key("occasion"):
                            self.old_data["occasion"] = skill.occasion
                            skill.occasion = self.data["occasion"]
                        if self.data.has_key("animation1_id"):
                            self.old_data["animation1_id"] = skill.animation1_id
                            skill.animation1_id = self.data["animation1_id"]
                        if self.data.has_key("animation2_id"):
                            self.old_data["animation2_"] = skill.animation2_
                            skill.animation2_ = self.data["animation2_"]
                        if self.data.has_key("menu_se"):
                            self.old_data["menu_se"] = skill.menu_se
                            skill.menu_se = self.data["menu_se"]
                        if self.data.has_key("common_event_id"):
                            self.old_data["common_event_id"] = skill.common_event_id
                            skill.common_event_id = self.data["common_event_id"]
                        if self.data.has_key("sp_cost"):
                            self.old_data["sp_cost"] = skill.sp_cost
                            skill.sp_cost = self.data["sp_cost"]
                        if self.data.has_key("power"):
                            self.old_data["power"] = skill.power
                            skill.power = self.data["power"]
                        if self.data.has_key("atk_f"):
                            self.old_data["atk_f"] = skill.atk_f
                            skill.atk_f = self.data["atk_f"]
                        if self.data.has_key("eva_f"):
                            self.old_data["eva_f"] = skill.eva_f
                            skill.eva_f = self.data["eva_f"]
                        if self.data.has_key("str_f"):
                            self.old_data["str_f"] = skill.str_f
                            skill.str_f = self.data["str_f"]
                        if self.data.has_key("dex_f"):
                            self.old_data["dex_f"] = skill.dex_f
                            skill.dex_f = self.data["dex_f"]
                        if self.data.has_key("agi_f"):
                            self.old_data["agi_f"] = skill.agi_f
                            skill.agi_f = self.data["agi_f"]
                        if self.data.has_key("int_f"):
                            self.old_data["int_f"] = skill.int_f
                            skill.int_f = self.data["int_f"]
                        if self.data.has_key("hit"):
                            self.old_data["hit"] = skill.hit
                            skill.hit = self.data["hit"]
                        if self.data.has_key("pdef_f"):
                            self.old_data["pdef_f"] = skill.pdef_f
                            skill.pdef_f = self.data["pdef_f"]
                        if self.data.has_key("mdef_f"):
                            self.old_data["mdef_f"] = skill.mdef_f
                            skill.mdef_f = self.data["mdef_f"]
                        if self.data.has_key("variance"):
                            self.old_data["variance"] = skill.variance
                            skill.variance = self.data["variance"]
                        if self.data.has_key("element_set"):
                            self.old_data["element_set"] = skill.element_set
                            skill.element_set = self.data["element_set"]
                        if self.data.has_key("plus_state_set"):
                            self.old_data["plus_state_set"] = skill.plus_state_set
                            skill.plus_state_set = self.data["plus_state_set"]
                        if self.data.has_key("minus_state_set"):
                            self.old_data["minus_state_set"] = skill.minus_state_set
                            skill.minus_state_set = self.data["minus_state_set"]
                        if self.data.has_key("note"):
                            self.old_data["note"] = skill.note
                            skill.note = self.data["note"]
                            
                            
    def do_undo(self):
        if Kernel.GlobalObjects.has_key("PROJECT"):
            project = Kernel.GlobalObjects.get_value("PROJECT")
            if project is not None:
                skills = project.getData("Skills")
                if skills is not None:
                    skill = skills[self.id]
                    if skill is not None:
                        if self.old_data.has_key("id"):
                            self.data["id"] = skill.id
                            skill.id = self.old_data["id"]
                        if self.old_data.has_key("name"):
                            self.data["name"] = skill.name
                            skill.name = self.old_data["name"]
                        if self.old_data.has_key("icon_name"):
                            self.data["icon_name"] = skill.icon_name
                            skill.icon_name = self.old_data["icon_name"]
                        if self.old_data.has_key("description"):
                            self.data["description"] = skill.description
                            skill.description = self.old_data["description"]
                        if self.old_data.has_key("scope"):
                            self.data["scope"] = skill.scope
                            skill.scope = self.old_data["scope"]
                        if self.old_data.has_key("occasion"):
                            self.data["occasion"] = skill.occasion
                            skill.occasion = self.old_data["occasion"]
                        if self.data.has_key("animation1_id"):
                            self.data["animation1_id"] = skill.animation1_id
                            skill.animation1_id = self.data["animation1_id"]
                        if self.old_data.has_key("animation2_id"):
                            self.data["animation2_"] = skill.animation2_
                            skill.animation2_ = self.old_data["animation2_"]
                        if self.old_data.has_key("menu_se"):
                            self.data["menu_se"] = skill.menu_se
                            skill.menu_se = self.old_data["menu_se"]
                        if self.old_data.has_key("common_event_id"):
                            self.data["common_event_id"] = skill.common_event_id
                            skill.common_event_id = self.old_data["common_event_id"]
                        if self.old_data.has_key("sp_cost"):
                            self.data["sp_cost"] = skill.sp_cost
                            skill.sp_cost = self.old_data["sp_cost"]
                        if self.old_data.has_key("power"):
                            self.data["power"] = skill.power
                            skill.power = self.old_data["power"]
                        if self.old_data.has_key("atk_f"):
                            self.data["atk_f"] = skill.atk_f
                            skill.atk_f = self.old_data["atk_f"]
                        if self.old_data.has_key("eva_f"):
                            self.data["eva_f"] = skill.eva_f
                            skill.eva_f = self.old_data["eva_f"]
                        if self.old_data.has_key("str_f"):
                            self.data["str_f"] = skill.str_f
                            skill.str_f = self.old_data["str_f"]
                        if self.old_data.has_key("dex_f"):
                            self.data["dex_f"] = skill.dex_f
                            skill.dex_f = self.old_data["dex_f"]
                        if self.old_data.has_key("agi_f"):
                            self.data["agi_f"] = skill.agi_f
                            skill.agi_f = self.old_data["agi_f"]
                        if self.old_data.has_key("int_f"):
                            self.data["int_f"] = skill.int_f
                            skill.int_f = self.old_data["int_f"]
                        if self.old_data.has_key("hit"):
                            self.data["hit"] = skill.hit
                            skill.hit = self.old_data["hit"]
                        if self.old_data.has_key("pdef_f"):
                            self.data["pdef_f"] = skill.pdef_f
                            skill.pdef_f = self.old_data["pdef_f"]
                        if self.old_data.has_key("mdef_f"):
                            self.data["mdef_f"] = skill.mdef_f
                            skill.mdef_f = self.old_data["mdef_f"]
                        if self.old_data.has_key("variance"):
                            self.data["variance"] = skill.variance
                            skill.variance = self.old_data["variance"]
                        if self.old_data.has_key("element_set"):
                            self.data["element_set"] = skill.element_set
                            skill.element_set = self.old_data["element_set"]
                        if self.old_data.has_key("plus_state_set"):
                            self.data["plus_state_set"] = skill.plus_state_set
                            skill.plus_state_set = self.old_data["plus_state_set"]
                        if self.old_data.has_key("minus_state_set"):
                            self.data["minus_state_set"] = skill.minus_state_set
                            skill.minus_state_set = self.old_data["minus_state_set"]
                        if self.old_data.has_key("note"):
                            self.data["note"] = skill.note
                            skill.note = self.old_data["note"]
          
class WeaponEditAction(Actions.ActionTemplate):
    def __init(self, id, data={}, sub_action=False):
        super(ClassEditAction, self).__init__(sub_action)
        if not isinstance(data, types.DictType):
            raise TypeError("Error: Expected dict type for 'data'")
        elif not isinstance(id, types.IntType):
            raise TypeError("Error: Expected int type for 'id'")
        else:
            self.id = id
            self.data = data
            self.old_data = {}
    
    def do_apply(self):
        if Kernel.GlobalObjects.has_key("PROJECT"):
            project = Kernel.GlobalObjects.get_value("PROJECT")
            if project is not None:
                weapons = project.getData("Weapons")
                if weapons is not None:
                    weapon = weapons[self.id]
                    if weapon is not None:
                        if self.data.has_key("id"):
                            self.old_data["id"] = weapon.id
                            weapon.id = self.data["id"]
                        if self.data.has_key("name"):
                            self.old_data["name"] = weapon.name
                            weapon.name = self.data["name"]
                        if self.data.has_key("icon_name"):
                            self.old_data["icon_name"] = weapon.icon_name
                            weapon.icon_name = self.data["icon_name"]
                        if self.data.has_key("description"):
                            self.old_data["description"] = weapon.description
                            weapon.description = self.data["description"]
                        if self.data.has_key("animation1_id"):
                            self.old_data["animation1_id"] = weapon.animation1_id
                            weapon.animation1_id = self.data["animation1_id"]
                        if self.data.has_key("animation2_id"):
                            self.old_Data["animation2_id"] = weapon.animation2_id
                            weapon.animation2_id = self.data["animation2_id"]
                        if self.data.has_key("price"):
                            self.old_data["price"] = weapon.price
                            weapon.price = self.data["price"]
                        if self.data.has_key("atk"):
                            self.old_data["atk"] = weapon.atk
                            weapon.atk = self.data["atk"]
                        if self.data.has_key("pdef"):
                            self.old_data["pdef"] = weapon.pdef
                            weapon.pdef = self.data["pdef"]
                        if self.data.has_key("mdef"):
                            self.old_data["mdef"] = weapon.mdef
                            weapon.mdef = self.data["mdef"]
                        if self.data.has_key("str_plus"):
                            self.old_data["str_plus"] = weapon.str_plus
                            weapon.str_plus = self.data["str_plus"]
                        if self.data.has_key("int_plus"):
                            self.old_data["int_plus"] = weapon.int_plus
                            weapon.int_plus = self.data["int_plus"]
                        if self.data.has_key("dex_plus"):
                            self.old_data["dex_plus"] = weapon.dex_plus
                            weapon.dex_plus = self.data["dex_plus"]
                        if self.data.has_key("agi_plus"):
                            self.old_data["agi_plus"] = weapon.agi_plus
                            weapon.agi_plus = self.data["agi_plus"]
                        if self.data.has_key("element_set"):
                            self.old_data["element_set"] = weapon.element_set
                            weapon.element_set = self.data["element_set"]
                        if self.data.has_key("plus_state_set"):
                            self.old_data["plus_state_set"] = weapon.plus_state_set
                            weapon.plus_state_set = self.data["plus_state_set"]
                        if self.data.has_key("minus_state_set"):
                            self.old_data["minus_state_set"] = weapon.minus_state_set
                            weapon.minus_state_set = self.data["minus_state_set"]
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
    
    def do_undo(self):
        if Kernel.GlobalObjects.has_key("PROJECT"):
            project = Kernel.GlobalObjects.get_value("PROJECT")
            if project is not None:
                weapons = project.getData("Weapons")
                if weapons is not None:
                    weapon = weapons[self.id]
                    if weapon is not None:
                        if self.old_data.has_key("id"):
                            self.data["id"] = weapon.id
                            weapon.id = self.old_data["id"]
                        if self.old_data.has_key("name"):
                            self.data["name"] = weapon.name
                            weapon.name = self.old_data["name"]
                        if self.old_data.has_key("icon_name"):
                            self.data["icon_name"] = weapon.icon_name
                            weapon.icon_name = self.old_data["icon_name"]
                        if self.old_data.has_key("description"):
                            self.data["description"] = weapon.description
                            weapon.description = self.old_data["description"]
                        if self.old_data.has_key("animation1_id"):
                            self.data["animation1_id"] = weapon.animation1_id
                            weapon.animation1_id = self.old_data["animation1_id"]
                        if self.old_data.has_key("animation2_id"):
                            self.Data["animation2_id"] = weapon.animation2_id
                            weapon.animation2_id = self.old_data["animation2_id"]
                        if self.old_data.has_key("price"):
                            self.data["price"] = weapon.price
                            weapon.price = self.old_data["price"]
                        if self.old_data.has_key("atk"):
                            self.data["atk"] = weapon.atk
                            weapon.atk = self.old_data["atk"]
                        if self.old_data.has_key("pdef"):
                            self.data["pdef"] = weapon.pdef
                            weapon.pdef = self.old_data["pdef"]
                        if self.old_data.has_key("mdef"):
                            self.data["mdef"] = weapon.mdef
                            weapon.mdef = self.old_data["mdef"]
                        if self.old_data.has_key("str_plus"):
                            self.data["str_plus"] = weapon.str_plus
                            weapon.str_plus = self.old_data["str_plus"]
                        if self.old_data.has_key("int_plus"):
                            self.data["int_plus"] = weapon.int_plus
                            weapon.int_plus = self.old_data["int_plus"]
                        if self.old_data.has_key("dex_plus"):
                            self.data["dex_plus"] = weapon.dex_plus
                            weapon.dex_plus = self.old_data["dex_plus"]
                        if self.old_data.has_key("agi_plus"):
                            self.data["agi_plus"] = weapon.agi_plus
                            weapon.agi_plus = self.old_data["agi_plus"]
                        if self.old_data.has_key("element_set"):
                            self.data["element_set"] = weapon.element_set
                            weapon.element_set = self.old_data["element_set"]
                        if self.old_data.has_key("plus_state_set"):
                            self.data["plus_state_set"] = weapon.plus_state_set
                            weapon.plus_state_set = self.old_data["plus_state_set"]
                        if self.old_data.has_key("minus_state_set"):
                            self.data["minus_state_set"] = weapon.minus_state_set
                            weapon.minus_state_set = self.old_data["minus_state_set"]
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False