import types

import Kernel
from Kernel import Manager as KM

import Actions

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