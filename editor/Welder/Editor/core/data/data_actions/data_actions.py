from copy import copy
import numpy

import welder_kernel as kernel

from PyitectConsumes import Table, ActionTemplate


class DataAction(ActionTemplate):

    ''' an action that edits RGSS Datatypes'''

    def __init__(self, data={}, sub_action=False):
        super(DataAction, self).__init__(sub_action)
        if not isinstance(data, dict):
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
        if len(args) == 1 and isinstance(args[0], (list, tuple)):
            val = args[0]
        self.keys.extend(val)

    def addKeys(self, *args):
        val = args
        if len(args) == 1 and isinstance(args[0], (list, tuple)):
            val = args[0]
        self.keys.extend(val)

    def setObj(self, obj):
        self.obj = obj

    def do_apply(self):
        result = self.apply_keys()
        if not result:
            return result
        result &= self.apply_extra()
        if not result:
            self.undo_keys()
        return result

    def do_undo(self):
        result = self.undo_keys()
        if not result:
            return result
        result &= self.undo_extra()
        if not result:
            self.apply_keys()
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
        except Exception:
            kernel.Log(
                "Exception applying Database Action(%s), "
                "will atempt to revert" % self.type,
                "[DataAction]", True, True)
            try:
                for key in keys_applyed:
                    self.data[key] = getattr(self.obj, key)
                    setattr(self.obj, key, self.old_data[key])
                kernel.Log("'Apply' Database Action(%s) sucessfuly reverted" %
                           self.type, "[DataAction]", True)
            except Exception:
                kernel.Log(
                    "Exception reverting failed 'Apply' "
                    "Database Action(%s), Possible Project coruption" %
                    self.type, "[DataAction]", True, True)
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
        except Exception:
            kernel.Log(
                "Exception undoing Database Action(%s), "
                "will atempt to revert" %
                self.type, "[DataAction]", True, True)

            try:
                for key in keys_applyed:
                    self.old_data[key] = getattr(self.obj, key)
                    setattr(self.obj, key, self.data[key])
                kernel.Log("'Undo' Database Action(%s) sucessfuly reverted" %
                           self.type, "[DataAction]", True)
            except Exception:
                kernel.Log(
                    "Exception reverting failed 'Undo' Database "
                    "Action(%s), Possible Project coruption" %
                    self.type, "[DataAction]", True, True)

        return False

    def undo_extra(self):
        return True


class TableEditAction(ActionTemplate):

    ''' an action that edits a RGSS Table'''

    def __init__(self, table, data={}, sub_action=False):
        super(TableEditAction, self).__init__(sub_action)
        if not isinstance(data, dict):
            raise TypeError("Error: Expected dict type for 'data'")
        if not isinstance(table, Table):
            raise TypeError("Error: Expected %s type for 'table'" % Table)
        self.table = table
        self.data = data
        self.oldvalue = None

    def do_apply(self):
        """
        applies the action described by self.data

        self.data should be a dict or other mapping object
        the keys of the object should look like the following
        {
            # an int in the range of 1 to 3
            # describes the dimensions of the data
            "dim": int(1 - 3),

            # a tuple of list of len dim that looks like so (x, y, z)
            # indicating an index to change
            # if editing a slice, index values are themselves tulples
            # for a slice:
            # ((x1,x2), (y1,y2), (z1,z2)))
            # or for a slice with a step
            # ((x1,x2,xstep), (y1,y2,ystep), (z1,z2,zstep))
            # a slice index may by none just like in real slice notation ie.:
            # [::2, 0, 0] (every other value in the array)
            # would look like:
            # ((None,None,2), 0, 0)
            # remember Tables are basically a wrapper
            # for a numpy n-dimensional arrays of of dtype int16
            # but limited to useing at most 3 dimision.
            # look at the numpy documentation for more information
            # http://docs.scipy.org/doc/numpy/reference/
            # note: unlike full numpy arrays you can't use
            # less indexes than the dim of the table
            # so you must explicitly slice the remaining dimensions
            # aka: len(index) == dim
            # if your doing a slice on a 1d table
            # put the slice tupel or list in a tuple or list like so
            # ((0,2),)
            "index": (x [, y [, z]]),

            # the python list (pref numpy array)
            # or value to set the table too
            "value": []
            #-----------------------------
            # if resizeing the table
            "resize": True,
            # NOTE CAN NOT CHANGE SHAPE DIMENSION JUST SIZE
            # len(shape) == len(table.getShape())
            "shape": (x [, y [, z]])
        }
        """

        if 'resize' in self.data and self.data['resize']:
            return self.resize_apply()
        else:
            return self.normal_apply()

    def resize_apply(self):
        shape = self.data['shape']
        if len(shape) != len(self.table.getShape()):
            raise TypeError(
                "new dimension and table old dimension"
                " must be the same (%d for %d)"
                % (len(shape), len(self.table.getShape())))

        self.oldvalue = numpy.copy(self.table._data)
        self.table.resize(*shape)

    def ensure_shape(self, dim):
        if dim > 3:
            raise TypeError("dim can't be greater than 3")
        if dim < 0:
            raise TypeError("dim can't be less than 0")

    def convert_index(self, index):
        args = []
        for index_part in index:
            if isinstance(index_part, int):
                args.append(index_part)
            elif isinstance(index_part, (tuple, list)):
                args.append(slice(*index_part))
            else:
                raise TypeError(
                    "Error: %s is not an int, tuple or list" % index_part)
        return args

    def normal_apply(self):
        # collect data
        dim = self.data['dim']
        index = self.data['index']
        value = self.data['value']
        # ensure the data is the right shape
        self.ensure_shape(dim)

        if isinstance(index, int):
            # a 1D index
            if dim > 1:
                raise TypeError(
                    "wrong number of arguments (%d for %d)" % (1, dim))
            else:
                # copy out old value
                self.oldvalue = numpy.copy(self.table[index])
                # store new value
                self.table[index] = value
                # we're done here
                return True
        elif len(index) != dim:
            raise TypeError(
                "wrong number of arguments (%d for %d)" % (len(index), dim))
        # an ND index
        # convert index
        args = self.convert_index(index)

        self.oldvalue = numpy.copy(self.table.__getitem__(args))
        self.table.__setitem__(args, value)
        return True

    def do_undo(self):
        if 'resize' in self.data:
            if self.data['resize']:
                return self.resize_undo()
            else:
                return self.normal_undo()
        else:
            return self.normal_undo()

    def resize_undo(self):
        shape = self.data['shape']
        if len(shape) != len(self.table.getShape()):
            raise TypeError(
                "new dimension and table old dimension"
                " must be the same (%d for %d)"
                % (len(shape), len(self.table.getShape())))
        self.table._data[:] = self.oldvalue[:]

    def normal_undo(self):
        # collect data
        dim = self.data['dim']
        index = self.data['index']
        # ensure the data is the right shape
        self.ensure_shape(dim)

        if isinstance(index, int):
            # a 1D index
            if dim > 1:
                raise TypeError(
                    "wrong number of arguments (%d for %d)" % (1, dim))
            else:
                # write back old value
                self.table[index] = self.oldvalue
                # we're done here
                return True
        elif len(index) != dim:
            raise TypeError(
                "wrong number of arguments (%d for %d)" % (len(index), dim))
        # an ND index
        # convert index
        args = self.convert_index(index)
        # write back old value
        self.table.__setitem__(args, self.oldvalue)
        return True


class ArmorEditAction(DataAction):

    ''' edits an Armor object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(ArmorEditAction, self).__init__(data, sub_action)
        self.setObj(obj)
        self.setType("Armor")
        self.addKeys(
            "id", "name", "icon_name", "description", "kind",
            "auto_state_id", "price", "pdef", "mdef", "eva",
            "str_plus", "dex_plus", "agi_plus", "int_plus",
            "guard_element_set", "guard_state_set")


class ActorEditAction(DataAction):

    ''' edits an Actor object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(ActorEditAction, self).__init__(data, sub_action)
        self.setType("Actor")
        self.parameters_action = None
        self.setObj(obj)
        self.addKeys(
            "id", "name", "initial_level", "final_level",
            "exp_basis", "exp_inflation", "character_name",
            "character_hue", "battler_name", "battler_hue",
            "weapon_id", "armor1_id", "armor2_id",
            "armor3_id", "armor4_id", "weapon_fix",
            "armor1_fix", "armor2_fix", "armor3_fix",
            "armor4_fix")

    def apply_extra(self):
        result = True
        actions_now = []
        try:
            if "parameters" in self.data:
                self.parameters_action = TableEditAction(
                    self.obj.parameters,
                    self.data["parameters"],
                    sub_action=True)
                result &= self.parameters_action.apply()
                actions_now.append(self.parameters_action)
                if not result:
                    raise Exception(
                        "'Apply' Sub action failed: %s"
                        % self.parameters_action)
        except Exception:
            kernel.Log(
                "Exception applying Actor Edit Action, will atempt to revert",
                "[DataAction]", True, True)
            try:
                for action in actions_now:
                    test = action.undo()
                    if not test:
                        raise Exception(
                            "'Apply' Sub action revert failed: %s" % action)
                kernel.Log(
                    "'Apply' Actor Edit Action sucessfuly reverted",
                    "[DataAction]", True)
            except Exception:
                kernel.Log(
                    "Exception reverting failed 'Apply' Actor Edit Action, "
                    "Possible Project coruption", "[DataAction]", True, True)
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
                    raise Exception(
                        "'Undo' Sub action failed: %s"
                        % self.parameters_action)
        except Exception:
            kernel.Log(
                "Exception undoing Actor Edit Action, will atempt to revert",
                "[DataAction]", True, True)
            try:
                for action in actions_now:
                    test = action.apply()
                    if not test:
                        raise Exception(
                            "'Undo' Sub action revert failed: %s" % action)
                kernel.Log(
                    "'Undo' Actor Edit Action sucessfuly reverted",
                    "[DataAction]", True)
            except Exception:
                kernel.Log(
                    "Exception reverting failed 'Undo' Actor Edit Action, "
                    "Possible Project coruption", "[DataAction]", True, True)
        return result


class ClassEditAction(DataAction):

    ''' edits a Class object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(ClassEditAction, self).__init__(data, sub_action)
        self.setType("Class")
        self.setObj(obj)
        self.addKeys(
            "id", "name", "position", "weapon_set", "armor_set", "learnings")
        self.element_ranks_action = None
        self.state_ranks_action = None

    def apply_extra(self):
        result = True
        actions_now = []
        try:
            if "element_ranks" in self.data:
                self.element_ranks_action = TableEditAction(
                    self.obj.element_ranks,
                    self.data["element_ranks"],
                    sub_action=True)
                result &= self.element_ranks_action.apply()
                actions_now.append(self.element_ranks_action)
                if not result:
                    raise Exception(
                        "'Apply' Sub action failed: %s"
                        % self.element_ranks_action)
            if "state_ranks" in self.data:
                self.state_ranks_action = TableEditAction(
                    self.obj.state_ranks,
                    self.data["state_ranks"],
                    sub_action=True)
                result &= self.element_ranks_action.apply()
                actions_now.append(self.element_ranks_action)
                if not result:
                    raise Exception(
                        "'Apply' Sub action failed: %s"
                        % self.element_ranks_action)
        except Exception:
            kernel.Log(
                "Exception applying Class Edit Action, will atempt to revert",
                "[DataAction]", True, True)
            try:
                for action in actions_now:
                    test = action.undo()
                    if not test:
                        raise Exception(
                            "'Apply' Sub action revert failed: %s" % action)
                kernel.Log(
                    "'Apply' Class Edit Action sucessfuly reverted",
                    "[DataAction]", True)
            except Exception:
                kernel.Log(
                    "Exception reverting failed 'Apply' Class Edit Action, "
                    "Possible Project coruption", "[DataAction]", True, True)
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
                    raise Exception(
                        "'Undo' Sub action failed: %s"
                        % self.state_ranks_action)
            if self.element_ranks_action is not None:
                result &= self.element_ranks_action.undo()
                actions_now.append(self.element_ranks_action)
                if not result:
                    raise Exception(
                        "'Undo' Sub action failed: %s"
                        % self.element_ranks_action)
        except Exception:
            kernel.Log(
                "Exception undoing Class Edit Action, will atempt to revert",
                "[DataAction]", True, True)
            try:
                for action in actions_now:
                    test = action.apply()
                    if not test:
                        raise Exception(
                            "'Undo' Sub action revert failed: %s" % action)
                kernel.Log(
                    "'Undo' Class Edit Action sucessfuly reverted",
                    "[DataAction]", True)
            except Exception:
                kernel.Log(
                    "Exception reverting failed 'Undo' Class Edit "
                    "Action, Possible Project coruption", "[DataAction]",
                    True, True)
        return result


class LearningEditAction(DataAction):

    ''' Edits a single Learning object'''

    def __init__(self, obj, data={}, sub_action=False):
        super(LearningEditAction, self).__init__(data, sub_action)
        self.setType("Learning")
        self.setObj(obj)
        self.addKeys("level", "skill_id")


class TroopEditAction(DataAction):

    ''' edits a Troop object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(TroopEditAction, self).__init__(data, sub_action)
        self.setType("Troop")
        self.setObj(obj)
        self.addKeys("id", "name", "members", "pages", "note")


class SkillEditAction(DataAction):

    ''' edits a Skill object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(SkillEditAction, self).__init__(data, sub_action)
        self.setType("Skill")
        self.setObj(obj)
        self.addKeys(
            "id", "name", "icon_name", "description", "scope",
            "occasion", "animation1_id", "animation2_id",
            "menu_se", "common_event_id", "sp_cost", "power",
            "atk_f", "eva_f", "str_f", "dex_f", "agi_f",
            "int_f", "hit", "pdef_f", "mdef_f", "variance",
            "element_set", "plus_state_set", "minus_state_set",
            "note")


class WeaponEditAction(DataAction):

    ''' edits a Weapon object'''

    def __init__(self, obj, data={}, sub_action=False):
        super(ClassEditAction, self).__init__(data, sub_action)
        self.setType("Weapon")
        self.setObj(obj)
        self.addKeys(
            "id", "name", "icon_name", "description", "animation1_id",
            "animation2_id", "price", "atk", "pdef",
            "mdef", "str_plus", "int_plus", "dex_plus", "agi_plus",
            "element_set", "plus_state_set", "minus_state_set")


class ItemEditActon(DataAction):

    ''' edits a Item object'''

    def __init__(self, obj, data={}, sub_action=False):
        super(ItemEditActon, self).__init__(data, sub_action)
        self.setType("Item")
        self.setObj(obj)
        self.addKeys(
            'id', 'name', 'icon_name', 'description',
            'scope', 'occasion', 'animation1_id',
            'animation2_id', 'menu_se', 'common_event_id',
            'price', 'consumable', 'parameter_type',
            'parameter_points', 'recover_hp_rate',
            'recover_hp', 'recover_sp_rate', 'recover_sp',
            'hit', 'pdef_f', 'mdef_f', 'variance', 'element_set',
            'plus_state_set', 'minus_state_set', 'note')


class AnimationFrameEditAction(DataAction):

    ''' edits a Animation::Frame object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(AnimationFrameEditAction, self).__init__(data, sub_action)
        self.setType("AnimationFrame")
        self.setObj(obj)
        self.addKeys('cell_max')
        self.cell_data_action = None

    def apply_extra(self):
        result = True
        actions_now = []
        try:
            if "cell_data" in self.data:
                self.cell_data_action = TableEditAction(
                    self.obj.cell_data, self.data["cell_data"],
                    sub_action=True)
                result &= self.cell_data_action.apply()
                actions_now.append(self.cell_data_action)
                if not result:
                    raise Exception(
                        "'Apply' Sub action failed: %s"
                        % self.cell_data_action)
        except Exception:
            kernel.Log(
                "Exception applying Animation Frame Edit Action, "
                "will atempt to revert",
                "[DataAction]", True, True)
            try:
                for action in actions_now:
                    test = action.undo()
                    if not test:
                        raise Exception(
                            "'Apply' Sub action revert failed: %s" % action)
                kernel.Log(
                    "'Apply' Animation Frame Edit Action sucessfuly reverted",
                    "[DataAction]", True)
            except Exception:
                kernel.Log(
                    "Exception reverting failed 'Apply' Animation Frame Edit "
                    "Action, Possible Project coruption", "[DataAction]",
                    True, True)
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
                    raise Exception(
                        "'Undo' Sub action failed: %s" % self.cell_data_action)
        except Exception:
            kernel.Log(
                "Exception undoing Animation Frame Edit Action, will atempt "
                "to revert", "[DataAction]", True, True)
            try:
                for action in actions_now:
                    test = action.apply()
                    if not test:
                        raise Exception(
                            "'Undo' Sub action revert failed: %s" % action)
                kernel.Log(
                    "'Undo' Animation Frame Edit Action sucessfuly reverted",
                    "[DataAction]", True)
            except Exception:
                kernel.Log(
                    "Exception reverting failed 'Undo' Animation Frame Edit "
                    "Action, Possible Project coruption", "[DataAction]",
                    True, True)
        return result


class AnimationEditAction(DataAction):

    ''' edits an Animation object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(AnimationEditAction, self).__init__(data, sub_action)
        self.setType("Animation")
        self.setObj(obj)
        self.addKeys('id', 'name', 'animation_name', 'animation_hue',
                     'position', 'frame_max', 'frames', 'timings')


class AnimationTimingEditAction(DataAction):

    ''' edits an Animation Timing object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(AnimationTimingEditAction, self).__init__(data, sub_action)
        self.setType("AnimationTiming")
        self.setObj(obj)
        self.addKeys(
            'frame', 'se', 'flash_scope', 'flash_color',
            'flash_duration', 'condition')


class AudioFileEditAction(DataAction):

    ''' edits a RPg Audiofile object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(AudioFileEditAction, self).__init__(data, sub_action)
        self.setType("AudioFile")
        self.setObj(obj)
        self.addKeys('name', 'volume', 'pitch')
        self.element_ranks_action = None
        self.state_ranks_action = None


class EnemyEditAction(DataAction):

    ''' edits an Enemy object'''

    def __init__(self, obj, data={}, sub_action=False):
        super(EnemyEditAction, self).__init__(data, sub_action)
        self.setType("Enemy")
        self.setObj(obj)
        self.addKeys(
            'id', 'name', 'battler_name', 'battler_hue',
            'maxhp', 'maxsp', 'str', 'dex', 'agi', 'int',
            'atk', 'pdef', 'mdef', 'eva', 'animation1_id',
            'animation2_id', 'actions', 'exp', 'gold',
            'item_id', 'weapon_id', 'armor_id', 'treasure_prob', 'note')
        self.element_ranks_action = None
        self.state_ranks_action = None

    def apply_extra(self):
        result = True
        actions_now = []
        try:
            if "element_ranks" in self.data:
                self.element_ranks_action = TableEditAction(
                    self.obj.element_ranks, self.data["element_ranks"],
                    sub_action=True)
                result &= self.element_ranks_action.apply()
                actions_now.append(self.element_ranks_action)
                if not result:
                    raise Exception(
                        "'Apply' Sub action failed: %s"
                        % self.element_ranks_action)
            if "state_ranks" in self.data:
                self.state_ranks_action = TableEditAction(
                    self.obj.state_ranks, self.data["state_ranks"],
                    sub_action=True)
                result &= self.element_ranks_action.apply()
                actions_now.append(self.element_ranks_action)
                if not result:
                    raise Exception(
                        "'Apply' Sub action failed: %s"
                        % self.element_ranks_action)
        except Exception:
            kernel.Log(
                "Exception applying Enemy Edit Action, will atempt to revert",
                "[DataAction]", True, True)
            try:
                for action in actions_now:
                    test = action.undo()
                    if not test:
                        raise Exception(
                            "'Apply' Sub action revert failed: %s" % action)
                kernel.Log(
                    "'Apply' Enemy Edit Action sucessfuly reverted",
                    "[DataAction]", True)
            except Exception:
                kernel.Log(
                    "Exception reverting failed 'Apply' Enemy Edit Action, "
                    "Possible Project coruption", "[DataAction]", True, True)
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
                    raise Exception(
                        "'Undo' Sub action failed: %s"
                        % self.state_ranks_action)
            if self.element_ranks_action is not None:
                result &= self.element_ranks_action.undo()
                actions_now.append(self.element_ranks_action)
                if not result:
                    raise Exception(
                        "'Undo' Sub action failed: %s"
                        % self.element_ranks_action)
        except Exception:
            kernel.Log(
                "Exception undoing Enemy Edit Action, will atempt to revert",
                "[DataAction]", True, True)
            try:
                for action in actions_now:
                    test = action.apply()
                    if not test:
                        raise Exception(
                            "'Undo' Sub action revert failed: %s" % action)
                kernel.Log(
                    "'Undo' Enemy Edit Action sucessfuly reverted",
                    "[DataAction]", True)
            except Exception:
                kernel.Log(
                    "Exception reverting failed 'Undo' Enemy Edit Action, "
                    "Possible Project coruption", "[DataAction]", True, True)
        return result


class EnemyActionEditAction(DataAction):

    ''' edits a Enemy::Action object'''

    def __init__(self, obj, data={}, sub_action=False):
        super(EnemyActionEditAction, self).__init__(data, sub_action)
        self.setType("EnemyAction")
        self.setObj(obj)
        self.addKeys(
            'kind', 'basic', 'skill_id',
            'condition_turn_a', 'condition_turn_b',
            'condition_hp', 'condition_level',
            'condition_switch_id', 'rating')


class EventEditAction(DataAction):

    ''' edits an Event Object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(EventEditAction, self).__init__(data, sub_action)
        self.setType("Event")
        self.setObj(obj)
        self.addKeys('id', 'name', 'x', 'y', 'pages')


class EventPageEditAction(DataAction):

    ''' edits a Event::Page object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(EventPageEditAction, self).__init__(data, sub_action)
        self.setType("EventPage")
        self.setObj(obj)
        self.addKeys(
            'condition', 'graphic', 'move_type', 'move_speed',
            'move_frequency', 'move_route', 'walk_anime',
            'step_anime',  'direction_fix', 'through',
            'always_on_top', 'trigger', 'list')


class EventConditionEditAction(DataAction):

    ''' edits a Event::Page::Condition object'''

    def __init__(self, obj, data={}, sub_action=False):
        super(EventConditionEditAction, self).__init__(data, sub_action)
        self.setType("EventCondition")
        self.setObj(obj)
        self.addKeys(
            'switch1_valid', 'switch2_valid', 'variable_valid',
            'self_switch_valid', 'switch1_id', 'switch2_id',
            'variable_id', 'variable_value', 'self_switch_ch')


class EventGraphicEditAction(DataAction):

    ''' edits a Event::Page::Graphic '''

    def __init__(self, obj, data={}, sub_action=False):
        super(EventGraphicEditAction, self).__init__(data, sub_action)
        self.setType("EventGraphic")
        self.setObj(obj)
        self.addKeys(
            'tile_id', 'character_name', 'character_hue',
            'direction', 'pattern', 'opacity', 'blend_type')


class EventCommandEditAction(DataAction):

    ''' edits a EventCommand object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(EventCommandEditAction, self).__init__(data, sub_action)
        self.setType("EventCommand")
        self.setObj(obj)
        self.addKeys('code', 'indent', 'parameters')


class CommonEventEditAction(DataAction):

    ''' edits a CommonEvent object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(CommonEventEditAction, self).__init__(data, sub_action)
        self.setType("CommonEvent")
        self.setObj(obj)
        self.addKeys('id', 'name', 'trigger', 'switch_id', 'list')


class MapEditAction(DataAction):

    ''' edits a Map object '''

    def __init__(self, obj, data={}, sub_action=False):
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
            if "data" in self.data:
                self.data_action = TableEditAction(
                    self.obj.data, self.data["data"], sub_action=True)
                result &= self.data_action.apply()
                actions_now.append(self.data_action)
                if not result:
                    raise Exception(
                        "'Apply' Sub action failed: %s"
                        % self.element_ranks_action)
        except Exception:
            kernel.Log(
                "Exception applying Map Edit Action, will atempt to revert",
                "[DataAction]", True, True)
            try:
                for action in actions_now:
                    test = action.undo()
                    if not test:
                        raise Exception(
                            "'Apply' Sub action revert failed: %s" % action)
                kernel.Log(
                    "'Apply' Map Edit Action sucessfuly reverted",
                    "[DataAction]", True)
            except Exception:
                kernel.Log(
                    "Exception reverting failed 'Apply' Map Edit Action, "
                    "Possible Project coruption", "[DataAction]", True, True)
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
                    raise Exception(
                        "'Undo' Sub action failed: %s"
                        % self.state_ranks_action)
        except Exception:
            kernel.Log(
                "Exception undoing Map Edit Action, will atempt to revert",
                "[DataAction]", True, True)
            try:
                for action in actions_now:
                    test = action.apply()
                    if not test:
                        raise Exception(
                            "'Undo' Sub action revert failed: %s" % action)
                kernel.Log(
                    "'Undo' Map Edit Action sucessfuly reverted",
                    "[DataAction]", True)
            except Exception:
                kernel.Log(
                    "Exception reverting failed 'Undo' Map Edit Action, "
                    "Possible Project coruption", "[DataAction]", True, True)
        return result


class MapInfoEditAction(DataAction):

    ''' edits a Mapinfo object'''

    def __init__(self, obj, data={}, sub_action=False):
        super(MapInfoEditAction, self).__init__(data, sub_action)
        self.setType("MapInfo")
        self.setObj(obj)
        self.addKeys(
            'name', 'parent_id', 'order', 'expanded', 'scroll_x', 'scroll_y')


class MoveCommandEditAction(DataAction):

    ''' edits a MoveCommand object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(MoveCommandEditAction, self).__init__(data, sub_action)
        self.setType("MoveCommand")
        self.setObj(obj)
        self.addKeys('code', 'parameters')


class MoveRouteEditAction(DataAction):

    ''' edits a MoveRoute object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(MoveRouteEditAction, self).__init__(data, sub_action)
        self.setType("MoveRoute")
        self.setObj(obj)
        self.addKeys('repeat', 'skippable', 'list')


class StateEditAction(DataAction):

    ''' edits a State object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(StateEditAction, self).__init__(data, sub_action)
        self.setType("State")
        self.setObj(obj)
        self.addKeys(
            'id', 'name', 'animation_id', 'restriction',
            'nonresistance', 'zero_hp', 'cant_get_exp', 'cant_evade',
            'slip_damage', 'rating', 'hit_rate', 'maxhp_rate',
            'maxsp_rate', 'str_rate', 'dex_rate', 'int_rate',
            'atk_rate', 'pdef_rate', 'mdef_rate', 'eva',
            'battle_only', 'hold_turn', 'auto_release_prob',
            'shock_release_prob', 'guard_element_set',
            'plus_state_set', 'minus_state_set', 'note')


class SystemEditAction(DataAction):

    ''' edits a System object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(SystemEditAction, self).__init__(data, sub_action)
        self.setType("System")
        self.setObj(obj)
        self.addKeys(
            'magic_number', 'party_members', 'elements',
            'switches', 'variables', 'windowskin_name', 'title_name',
            'gameover_name',  'battle_transition', 'title_bgm',
            'battle_bgm', 'battle_end_me', 'gameover_me',
            'cursor_se', 'decision_se', 'cancel_se', 'buzzer_se',
            'equip_se', 'shop_se', 'save_se', 'load_se',
            'battle_start_se', 'escape_se', 'actor_collapse_se',
            'words', 'test_battlers', 'test_troop_id',
            'start_map_id', 'start_x', 'start_y', 'battleback_name',
            'battler_name', 'battler_hue', 'edit_map_id')


class TestBattlerEditAction(DataAction):

    ''' edits a TestBattler object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(TestBattlerEditAction, self).__init__(data, sub_action)
        self.setType("TestBattler")
        self.setObj(obj)
        self.addKeys(
            'actor_id', 'level', 'weapon_id',
            'armor1_id', 'armor2_id', 'armor3_id', 'armor4_id')


class WordsEditAction(DataAction):

    ''' edits a System::Words object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(WordsEditAction, self).__init__(data, sub_action)
        self.setType("Words")
        self.setObj(obj)
        self.addKeys(
            'gold', 'hp', 'sp', 'str', 'dex', 'agi',
            'int', 'atk', 'pdef', 'mdef', 'weapon',
            'armor1', 'armor2', 'armor3', 'armor4',
            'attack', 'skill', 'guard', 'item', 'equip')


class TilesetEditAction(DataAction):

    ''' edits a Tileset object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(TilesetEditAction, self).__init__(data, sub_action)
        self.setType("Tileset")
        self.setObj(obj)
        self.addKeys(
            'id', 'name', 'tileset_name', 'autotile_names',
            'panorama_name', 'panorama_hue', 'fog_name',
            'fog_hue', 'fog_opacity', 'fog_blend_type',
            'fog_zoom', 'fog_sx', 'fog_sy', 'battleback_name')
        self.passages_action = None
        self.priorities_action = None
        self.terrain_tags_action = None

    def apply_extra(self):
        result = True
        actions_now = []
        try:
            if "passages" in self.data:
                self.passages_action = TableEditAction(
                    self.obj.passages, self.data["passages"],
                    sub_action=True)
                result &= self.passages_action.apply()
                actions_now.append(self.passages_action)
                if not result:
                    raise Exception(
                        "'Apply' Sub action failed: %s"
                        % self.element_ranks_action)
            if "priorities" in self.data:
                self.priorities_action = TableEditAction(
                    self.obj.priorities, self.data["priorities"],
                    sub_action=True)
                result &= self.priorities_action.apply()
                actions_now.append(self.priorities_action)
                if not result:
                    raise Exception(
                        "'Apply' Sub action failed: %s"
                        % self.element_ranks_action)
            if "terrain_tags" in self.data:
                self.terrain_tags_action = TableEditAction(
                    self.obj.terrain_tags, self.data["terrain_tags"],
                    sub_action=True)
                result &= self.terrain_tags_action.apply()
                actions_now.append(self.terrain_tags_action)
                if not result:
                    raise Exception(
                        "'Apply' Sub action failed: %s"
                        % self.element_ranks_action)
        except Exception:
            kernel.Log(
                "Exception applying Tileset Edit Action, "
                "will atempt to revert", "[DataAction]", True, True)
            try:
                for action in actions_now:
                    test = action.undo()
                    if not test:
                        raise Exception(
                            "'Apply' Sub action revert failed: %s" % action)
                kernel.Log(
                    "'Apply' Tileset Edit Action sucessfuly reverted",
                    "[DataAction]", True)
            except Exception:
                kernel.Log(
                    "Exception reverting failed 'Apply' Tileset Edit Action, "
                    "Possible Project coruption", "[DataAction]", True, True)
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
                    raise Exception(
                        "'Undo' Sub action failed: %s"
                        % self.state_ranks_action)
            if self.priorities_action is not None:
                result &= self.priorities_action.undo()
                actions_now.append(self.priorities_action)
                if not result:
                    raise Exception(
                        "'Undo' Sub action failed: %s"
                        % self.element_ranks_action)
            if self.terrain_tags_action is not None:
                result &= self.terrain_tags_action.undo()
                actions_now.append(self.terrain_tags_action)
                if not result:
                    raise Exception(
                        "'Undo' Sub action failed: %s"
                        % self.element_ranks_action)
        except Exception:
            kernel.Log(
                "Exception undoing Tileset Edit Action, "
                "will atempt to revert", "[DataAction]", True, True)
            try:
                for action in actions_now:
                    test = action.apply()
                    if not test:
                        raise Exception(
                            "'Undo' Sub action revert failed: %s" % action)
                kernel.Log(
                    "'Undo' Tileset Edit Action sucessfuly reverted",
                    "[DataAction]", True)
            except Exception:
                kernel.Log(
                    "Exception reverting failed 'Undo' Tileset Edit Action, "
                    "Possible Project coruption", "[DataAction]", True, True)
        return result


class TroopPageEditAction(DataAction):

    ''' edits a Troop::Page object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(TroopPageEditAction, self).__init__(data, sub_action)
        self.setType("TroopPage")
        self.setObj(obj)
        self.addKeys('span', 'list')


class TroopConditionEditAction(DataAction):

    ''' edits a Troop::Condition'''

    def __init__(self, obj, data={}, sub_action=False):
        super(TroopConditionEditAction, self).__init__(data, sub_action)
        self.setType("TroopCondition")
        self.setObj(obj)
        self.addKeys(
            'turn_valid', 'enemy_valid', 'actor_valid',
            'switch_valid', 'turn_a', 'turn_b', 'enemy_index',
            'enemy_hp', 'actor_id', 'actor_hp', 'switch_id')


class MemberEditAction(DataAction):

    ''' edits a Troop::Member object '''

    def __init__(self, obj, data={}, sub_action=False):
        super(MemberEditAction, self).__init__(data, sub_action)
        self.setType("Member")
        self.setObj(obj)
        self.addKeys('enemy_id', 'x', 'y', 'hidden', 'immortal')
