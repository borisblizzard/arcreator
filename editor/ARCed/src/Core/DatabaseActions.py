import types

import Kernel
from Kernel import Manager as KM

import Actions

class ArmorEditAction(Actions.ActionTemplate):

    def __init__(self, id, data={}):
        super(ArmorEditAction, self).__init__()
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
                        Kernel.log("Warning: ArmorEditAction apply not compleated secessful, Armor ID %s is none" % self.id, "[ArmorEditAction]")
                        return False
                else:
                     Kernel.log("Warning: ArmorEditAction apply not compleated secessful, Armors array from project is none", "[ArmorEditAction]")
                     return False
            else:
                Kernel.log("Warning: ArmorEditAction apply not compleated secessful, Project is None", "[ArmorEditAction]")
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
                        Kernel.log("Warning: ArmorEditAction apply not compleated secessful, Armor ID %s is none" % self.id, "[ArmorEditAction]")
                        return False
                else:
                     Kernel.log("Warning: ArmorEditAction apply not compleated secessful, Armors array from project is none", "[ArmorEditAction]")
                     return False
            else:
                Kernel.log("Warning: ArmorEditAction apply not compleated secessful, Project is None", "[ArmorEditAction]")
                return False
                     
class ActorEditAction(Actions.ActionTemplate):

    def __init__(self, id, data={}):
        super(ActorEditAction, self).__init__()
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
                        #==================================================================
                        #TODO: This needs to be expanded to work off slices not replace the entire Table
                        if self.data.has_key("parameters"):
                            self.old_data["parameters"] = actor.parameters
                            actor.parameters = self.data["parameters"]
                        #==================================================================
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
                        Kernel.log("Warning: ActorEditAction apply not compleated secessful, Actor ID %s is none" % self.id, "[ActorEditAction]")
                        return False
                else:
                     Kernel.log("Warning: ActorEditAction apply not compleated secessful, Actors array from project is none", "[ActorEditAction]")
                     return False
            else:
                Kernel.log("Warning: ActorEditAction apply not compleated secessful, Project is None", "[ActorEditAction]")
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
                        #==================================================================
                        #TODO: This needs to be expanded to work off slices not replace the entire Table
                        if self.old_data.has_key("parameters"):
                            self.data["parameters"] = actor.parameters
                            actor.parameters = self.old_data["parameters"]
                        #==================================================================
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
                        Kernel.log("Warning: ActorEditAction undo not compleated secessful, Actor ID %s is none" % self.id, "[ActorEditAction]")
                        return False
                else:
                     Kernel.log("Warning: ActorEditAction undo not compleated secessful, Actors array from project is none", "[ActorEditAction]")
                     return False
            else:
                Kernel.log("Warning: ActorEditAction undo not compleated secessful, Project is None", "[ActorEditAction]")
                return False
                
                
                
class ClassEditAction(Actions.ActionTemplate):
    def __init__(self, id, data={}):
        super(ClassEditAction, self).__init__()
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
                            self.old_data["learnings"] = klass.learnings
                            klass.learnings = self.data["learnings"]
                        if self.data.has_key("element_ranks"):
                            self.old_data["element_ranks"] = klass.element_ranks
                            klass.element_ranks = self.data["element_ranks"]
                        if self.data.has_key("state_ranks"):
                            self.old_data["state_ranks"] = klass.state_ranks
                            klass.state_ranks = self.data["state_ranks"]
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
                        if self.old_data.has_key("learnings"):
                            self.data["learnings"] = klass.learnings
                            klass.learnings = self.old_data["learnings"]
                        if self.old_data.has_key("weapon_set"):
                            self.data["weapon_set"] = klass.weapon_set
                            klass.weapon_set = self.old_data["weapon_set"]
                        if self.old_data.has_key("armor_set"):
                            self.data["armor_set"] = klass.armor_set
                            klass.armor_set = self.old_data["armor_set"]
                        if self.old_data.has_key("element_ranks"):
                            self.data["element_ranks"] = klass.element_ranks
                            klass.element_ranks = self.old_data["element_ranks"]
                        if self.old_data.has_key("state_ranks"):
                            self.data["state_ranks"] = klass.state_ranks
                            klass.state_ranks = self.old_data["state_ranks"]
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
                
                
class WeaponEditAction(Actions.ActionTemplate):
    def __init(self, id, data={}):
        super(ClassEditAction, self).__init__()
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