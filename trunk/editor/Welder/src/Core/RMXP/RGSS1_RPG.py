'''
Created on Sep 9, 2010

a Python implementation of the RGSS1 RPG module 

Classes in this module
----------------------
Actor
Animation
Armor
AudioFile
Class
CommonEvent
Enemy
Event
EventCommand
Item
Map
MapInfo
MoveCommand
MoveRoute
Skill
State
System
Tileset
Troop
Weapon
'''
import wx
import os
import gc
import types

from Boot import WelderImport
Core = WelderImport('Core')

Table = Core.RPGutil.Table
Color = Core.RPGutil.Color
Tone = Core.RPGutil.Tone

class _Actor(object):
    _arc_class_path = "RPG::Actor"
    _arc_instance_variables = ['id', 'name', 'class_id', 'initial_level',
                              'final_level', 'exp_basis', 'exp_inflation',
                              'exp_list', 'character_name', 'character_hue',
                              'battler_name', 'battler_hue', 'parameters',
                              'weapon_id', 'armor1_id', 'armor2_id',
                              'armor3_id', 'armor4_id', 'armor1_fix',
                              'armor2_fix', 'armor3_fix', 'armor4_fix', 'note']
    def __init__(self):
        self.id = 0
        self.name = ""
        self.class_id = 1
        self.initial_level = 1
        self.final_level = 99
        self.exp_basis = 30
        self.exp_inflation = 30
        self.exp_list = []
        self.character_name = ""
        self.character_hue = 0
        self.battler_name = ""
        self.battler_hue = 0
        self.parameters = Table(6, 100)
        for i in xrange(1, 100):
            self.parameters[0, i] = 500 + i * 50
            self.parameters[1, i] = 500 + i * 50
            self.parameters[2, i] = 50 + i * 5
            self.parameters[3, i] = 50 + i * 5
            self.parameters[4, i] = 50 + i * 5
            self.parameters[5, i] = 50 + i * 5
        self.weapon_id = 0
        self.armor1_id = 0
        self.armor2_id = 0
        self.armor3_id = 0
        self.armor4_id = 0
        self.weapon_fix = False
        self.armor1_fix = False
        self.armor2_fix = False
        self.armor3_fix = False
        self.armor4_fix = False
        self.note = ''

class _Animation(object):
    _arc_class_path = "RPG::Animation"
    _arc_instance_variables = ['id', 'name', 'animation_name',
                              'animation_hue', 'position', 'frame_max',
                              'frames', 'timings']

    def __init__(self):
        self.id = 0
        self.name = ""
        self.animation_name = ""
        self.animation_hue = 0
        self.position = 1
        self.frame_max = 1
        self.frames = [RPG.Animation.Frame()]
        self.timings = []

class _Frame(object):
    _arc_class_path = "RPG::Animation::Frame"
    _arc_instance_variables = ['cell_max', 'cell_data']
    def __init__(self):
        self.cell_max = 0
        self.cell_data = Table(0, 0)

class _Timing(object):
    _arc_class_path = "RPG::Animation::Timing"
    _arc_instance_variables = ['frame', 'se', 'flash_scope',
                             'flash_color', 'flash_duration',
                             'condition']
    def __init__(self):
        self.frame = 0
        self.se = RPG.AudioFile("", 80)
        self.flash_scope = 0
        self.flash_color = Color(255, 255, 255, 255)
        self.flash_duration = 5
        self.condition = 0

class _Armor(object):
    _arc_class_path = "RPG::Armor"
    _arc_instance_variables = ['id', 'name', 'icon_name', 'description',
                              'kind', 'auto_state_id', 'price', 'pdef',
                              'mdef', 'eva', 'str_plus', 'dex_plus',
                              'agi_plus', 'int_plus', 'guard_element_set',
                              'guard_state_set', 'note']
    def __init__(self):
        self.id = 0
        self.name = ""
        self.icon_name = ""
        self.description = ""
        self.kind = 0
        self.auto_state_id = 0
        self.price = 0
        self.pdef = 0
        self.mdef = 0
        self.eva = 0
        self.str_plus = 0
        self.dex_plus = 0
        self.agi_plus = 0
        self.int_plus = 0
        self.guard_element_set = []
        self.guard_state_set = []
        self.note = ''

class _AudioFile(object):
    _arc_class_path = "RPG::AudioFile"
    _arc_instance_variables = ['name', 'volume', 'pitch']
    def __init__(self, name="", volume=100, pitch=100):
        self.name = name
        self.volume = volume
        self.pitch = pitch

class _Class(object):
    _arc_class_path = "RPG::Class"
    _arc_instance_variables = ['id', 'name', 'position', 'weapon_set',
                             'armor_set', 'element_ranks', 'state_ranks',
                             'learnings', 'note']
    def __init__(self):
        self.id = 0
        self.name = ""
        self.position = 0
        self.weapon_set = []
        self.armor_set = []
        self.element_ranks = Table(1)
        self.state_ranks = Table(1)
        self.learnings = []
        self.note = ''

class _Learning(object):
    _arc_class_path = "RPG::Class::Learning"
    _arc_instance_variables = ['level', 'skill_id']
    def __init__(self):
        self.level = 1
        self.skill_id = 1

class _CommonEvent(object):
    _arc_class_path = "RPG::CommonEvent"
    _arc_instance_variables = ['id', 'name', 'trigger', 'switch_id', 'list']
    def __init__(self):
        self.id = 0
        self.name = ""
        self.trigger = 0
        self.switch_id = 1
        self.list = [RPG.EventCommand()]

class _Enemy(object):
    _arc_class_path = "RPG::Enemy"
    _arc_instance_variables = ['id', 'name', 'battler_name', 'battler_hue',
                             'maxhp', 'maxsp', 'str', 'dex', 'agi', 'int',
                             'atk', 'pdef', 'mdef', 'eva', 'animation1_id',
                             'animation2_id', 'element_ranks',
                             'state_ranks', 'actions', 'exp', 'gold',
                             'item_id', 'weapon_id', 'armor_id',
                             'treasure_prob', 'note']
    def __init__(self):
        self.id = 0
        self.name = ""
        self.battler_name = ""
        self.battler_hue = 0
        self.maxhp = 500
        self.maxsp = 500
        self.str = 50
        self.dex = 50
        self.agi = 50
        self.int = 50
        self.atk = 100
        self.pdef = 100
        self.mdef = 100
        self.eva = 0
        self.animation1_id = 0
        self.animation2_id = 0
        self.element_ranks = Table(1)
        self.state_ranks = Table(1)
        self.actions = [RPG.Enemy.Action()]
        self.exp = 0
        self.gold = 0
        self.item_id = 0
        self.weapon_id = 0
        self.armor_id = 0
        self.treasure_prob = 100
        self.note = ''

class _Action(object):
    _arc_class_path = "RPG::Enemy::Action"
    _arc_instance_variables = ['kind', 'basic', 'skill_id',
                             'condition_turn_a', 'condition_turn_b',
                             'condition_hp', 'condition_level',
                             'condition_switch_id', 'rating']
    def __init__(self):
        self.kind = 0
        self.basic = 0
        self.skill_id = 1
        self.condition_turn_a = 0
        self.condition_turn_b = 1
        self.condition_hp = 100
        self.condition_level = 1
        self.condition_switch_id = 0
        self.rating = 5

class _Event(object):
    _arc_class_path = "RPG::Event"
    _arc_instance_variables = ['id', 'name', 'x', 'y', 'pages']
    def __init__(self, x=0, y=0):
        self.id = 0
        self.name = ""
        self.x = x
        self.y = y
        self.pages = [RPG.Event.Page()]

class _EventPage(object):
    _arc_class_path = "RPG::Event::Page"
    _arc_instance_variables = ['condition', 'graphic', 'move_type',
                             'move_speed', 'move_frequency',
                             'move_route', 'walk_anime', 'step_anime',
                             'direction_fix', 'through',
                             'always_on_top', 'trigger', 'list']
    def __init__(self):
        self.condition = RPG.Event.Page.Condition()
        self.graphic = RPG.Event.Page.Graphic()
        self.move_type = 0
        self.move_speed = 3
        self.move_frequency = 3
        self.move_route = RPG.MoveRoute()
        self.walk_anime = True
        self.step_anime = False
        self.direction_fix = False
        self.through = False
        self.always_on_top = False
        self.trigger = 0
        self.list = [RPG.EventCommand()]

class _EventCondition(object):
    _arc_class_path = "RPG::Event::Page::Condition"
    _arc_instance_variables = ['switch1_valid', 'switch2_valid',
                             'variable_valid', 'self_switch_valid',
                             'switch1_id', 'switch2_id',
                             'variable_id', 'variable_value',
                             'self_switch_ch']
    def __init__(self):
        self.switch1_valid = False
        self.switch2_valid = False
        self.variable_valid = False
        self.self_switch_valid = False
        self.switch1_id = 1
        self.switch2_id = 1
        self.variable_id = 1
        self.variable_value = 0
        self.self_switch_ch = "A"

class _EventGraphic(object):
    _arc_class_path = "RPG::Event::Page::Graphic"
    _arc_instance_variables = ['tile_id', 'character_name',
                             'character_hue', 'direction',
                             'pattern', 'opacity', 'blend_type']
    def __init__(self):
        self.tile_id = 0
        self.character_name = ""
        self.character_hue = 0
        self.direction = 2
        self.pattern = 0
        self.opacity = 255
        self.blend_type = 0

class _EventCommand(object):
    _arc_class_path = "RPG::EventCommand"
    _arc_instance_variables = ['code', 'indent', 'parameters']
    def __init__(self, code=0, indent=0, parameters=[]):
        self.code = code
        self.indent = indent
        self.parameters = parameters

class _Item(object):
    _arc_class_path = "RPG::Item"
    _arc_instance_variables = ['id', 'name', 'icon_name', 'description',
                             'scope', 'occasion', 'animation1_id',
                             'animation2_id', 'menu_se', 'common_event_id',
                             'price', 'consumable', 'parameter_type',
                             'parameter_points', 'recover_hp_rate',
                             'recover_hp', 'recover_sp_rate', 'recover_sp',
                             'hit', 'pdef_f', 'mdef_f', 'variance',
                             'element_set', 'plus_state_set',
                             'minus_state_set', 'note']
    def __init__(self):
        self.id = 0
        self.name = ""
        self.icon_name = ""
        self.description = ""
        self.scope = 0
        self.occasion = 0
        self.animation1_id = 0
        self.animation2_id = 0
        self.menu_se = RPG.AudioFile("", 80)
        self.common_event_id = 0
        self.price = 0
        self.consumable = True
        self.parameter_type = 0
        self.parameter_points = 0
        self.recover_hp_rate = 0
        self.recover_hp = 0
        self.recover_sp_rate = 0
        self.recover_sp = 0
        self.hit = 100
        self.pdef_f = 0
        self.mdef_f = 0
        self.variance = 0
        self.element_set = []
        self.plus_state_set = []
        self.minus_state_set = []
        self.note = ''

class _Map(object):
    _arc_class_path = "RPG::Map"
    _arc_instance_variables = ['tileset_id', 'width', 'height',
                             'autoplay_bgm', 'bgs', 'encounter_list',
                             'encounter_step', 'data', 'events']
    def __init__(self, width=20, height=15):
        self.tileset_id = 1
        self.width = width
        self.height = height
        self.autoplay_bgm = False
        self.bgm = RPG.AudioFile()
        self.autoplay_bgs = False
        self.bgs = RPG.AudioFile("", 80)
        self.encounter_list = []
        self.encounter_step = 30
        self.data = Table(width, height, 3)
        self.events = {}

class _MapInfo(object):
    _arc_class_path = "RPG::MapInfo"
    _arc_instance_variables = ['name', 'parent_id', 'order', 'expanded',
                             'scroll_x', 'scroll_y']
    def __init__(self):
        self.name = ""
        self.parent_id = 0
        self.order = 0
        self.expanded = False
        self.scroll_x = 0
        self.scroll_y = 0

class _MoveCommand(object):
    _arc_class_path = "RPG::MoveCommand"
    _arc_instance_variables = ['code', 'parameters']
    def __init__(self, code=0, parameters=[]):
        self.code = code
        self.parameters = parameters

class _MoveRoute(object):
    _arc_class_path = "RPG::MoveRoute"
    _arc_instance_variables = ['repeat', 'skippable', 'list']
    def __init__(self):
        self.repeat = True
        self.skippable = False
        self.list = [RPG.MoveCommand()]

class _Skill(object):
    _arc_class_path = "RPG::Skill"
    _arc_instance_variables = ['id', 'name', 'icon_name', 'description',
                             'scope', 'occasion', 'animation1_id',
                             'animation2_id', 'menu_se', 'common_event_id',
                             'sp_cost', 'power', 'atk_f', 'eva_f', 'str_f',
                             'dex_f', 'agi_f', 'int_f', 'hit', 'pdef_f',
                             'mdef_f', 'variance', 'element_set',
                             'plus_state_set', 'minus_state_set', 'note']
    def __init__(self):
        self.id = 0
        self.name = ""
        self.icon_name = ""
        self.description = ""
        self.scope = 0
        self.occasion = 1
        self.animation1_id = 0
        self.animation2_id = 0
        self.menu_se = RPG.AudioFile("", 80)
        self.common_event_id = 0
        self.sp_cost = 0
        self.power = 0
        self.atk_f = 0
        self.eva_f = 0
        self.str_f = 0
        self.dex_f = 0
        self.agi_f = 0
        self.int_f = 100
        self.hit = 100
        self.pdef_f = 0
        self.mdef_f = 100
        self.variance = 15
        self.element_set = []
        self.plus_state_set = []
        self.minus_state_set = []
        self.note = ''

class _State(object):
    _arc_class_path = "RPG::State"
    _arc_instance_variables = ['id', 'name', 'animation_id', 'restriction',
                             'nonresistance', 'zero_hp', 'cant_get_exp',
                             'cant_evade', 'slip_damage', 'rating',
                             'hit_rate', 'maxhp_rate', 'maxsp_rate',
                             'str_rate', 'dex_rate', 'int_rate',
                             'atk_rate', 'pdef_rate', 'mdef_rate', 'eva',
                             'battle_only', 'hold_turn',
                             'auto_release_prob', 'shock_release_prob',
                             'guard_element_set', 'plus_state_set',
                             'minus_state_set', 'note']
    def __init__(self):
        self.id = 0
        self.name = ""
        self.animation_id = 0
        self.restriction = 0
        self.nonresistance = False
        self.zero_hp = False
        self.cant_get_exp = False
        self.cant_evade = False
        self.slip_damage = False
        self.rating = 5
        self.hit_rate = 100
        self.maxhp_rate = 100
        self.maxsp_rate = 100
        self.str_rate = 100
        self.dex_rate = 100
        self.agi_rate = 100
        self.int_rate = 100
        self.atk_rate = 100
        self.pdef_rate = 100
        self.mdef_rate = 100
        self.eva = 0
        self.battle_only = True
        self.hold_turn = 0
        self.auto_release_prob = 0
        self.shock_release_prob = 0
        self.guard_element_set = []
        self.plus_state_set = []
        self.minus_state_set = []
        self.note = ''

class _System(object):
    _arc_class_path = "RPG::System"
    _arc_instance_variables = ['magic_number', 'party_members', 'elements',
                             'switches', 'variables', 'windowskin_name',
                             'title_name', 'gameover_name',
                             'battle_transition', 'title_bgm',
                             'battle_bgm', 'battle_end_me', 'gameover_me',
                             'cursor_se', 'decision_se', 'cancel_se',
                             'buzzer_se', 'equip_se', 'shop_se', 'save_se',
                             'load_se', 'battle_start_se', 'escape_se',
                             'actor_collapse_se', 'words', 'test_battlers',
                             'test_troop_id', 'start_map_id', 'start_x',
                             'start_y', 'battleback_name', 'battler_name',
                             'battler_hue', 'edit_map_id']
    def __init__(self):
        self.magic_number = 0
        self.party_members = [1]
        self.elements = [None, ""]
        self.switches = [None, ""]
        self.variables = [None, ""]
        self.windowskin_name = ""
        self.title_name = ""
        self.gameover_name = ""
        self.battle_transition = ""
        self.title_bgm = RPG.AudioFile()
        self.battle_bgm = RPG.AudioFile()
        self.battle_end_me = RPG.AudioFile()
        self.gameover_me = RPG.AudioFile()
        self.cursor_se = RPG.AudioFile("", 80)
        self.decision_se = RPG.AudioFile("", 80)
        self.cancel_se = RPG.AudioFile("", 80)
        self.buzzer_se = RPG.AudioFile("", 80)
        self.equip_se = RPG.AudioFile("", 80)
        self.shop_se = RPG.AudioFile("", 80)
        self.save_se = RPG.AudioFile("", 80)
        self.load_se = RPG.AudioFile("", 80)
        self.battle_start_se = RPG.AudioFile("", 80)
        self.escape_se = RPG.AudioFile("", 80)
        self.actor_collapse_se = RPG.AudioFile("", 80)
        self.enemy_collapse_se = RPG.AudioFile("", 80)
        self.words = RPG.System.Words()
        self.test_battlers = []
        self.test_troop_id = 1
        self.start_map_id = 1
        self.start_x = 0
        self.start_y = 0
        self.battleback_name = ""
        self.battler_name = ""
        self.battler_hue = 0
        self.edit_map_id = 1

class _TestBattler(object):
    _arc_class_path = "RPG::System::TestBattler"
    _arc_instance_variables = ['actor_id', 'level', 'weapon_id',
                         'armor1_id', 'armor2_id', 'armor3_id',
                         'armor4_id']
    def __init__(self):
        self.actor_id = 1
        self.level = 1
        self.weapon_id = 0
        self.armor1_id = 0
        self.armor2_id = 0
        self.armor3_id = 0
        self.armor4_id = 0

class _Words(object):
    _arc_class_path = "RPG::Words"
    _arc_instance_variables = ['gold', 'hp', 'sp', 'str', 'dex', 'agi',
                            'int', 'atk', 'pdef', 'mdef', 'weapon',
                            'armor1', 'armor2', 'armor3', 'armor4',
                            'attack', 'skill', 'guard', 'item', 'equip']
    def __init__(self):
        self.gold = ""
        self.hp = ""
        self.sp = ""
        self.str = ""
        self.dex = ""
        self.agi = ""
        self.int = ""
        self.atk = ""
        self.pdef = ""
        self.mdef = ""
        self.weapon = ""
        self.armor1 = ""
        self.armor2 = ""
        self.armor3 = ""
        self.armor4 = ""
        self.attack = ""
        self.skill = ""
        self.guard = ""
        self.item = ""
        self.equip = ""

class _Tileset(object):
    _arc_class_path = "RPG::Tileset"
    _arc_instance_variables = ['id', 'name', 'tileset_name',
                             'autotile_names', 'panorama_name',
                             'panorama_hue', 'fog_name', 'fog_hue',
                             'fog_opacity', 'fog_blend_type', 'fog_zoom',
                             'fog_sx', 'fog_sy', 'battleback_name',
                             'passages', 'priorities', 'terrain_tags']
    def __init__(self):
        self.id = 0
        self.name = ""
        self.tileset_name = ""
        self.autotile_names = [""] * 7
        self.panorama_name = ""
        self.panorama_hue = 0
        self.fog_name = ""
        self.fog_hue = 0
        self.fog_opacity = 64
        self.fog_blend_type = 0
        self.fog_zoom = 200
        self.fog_sx = 0
        self.fog_sy = 0
        self.battleback_name = ""
        self.passages = Table(384)
        self.priorities = Table(384)
        self.priorities[0] = 5
        self.terrain_tags = Table(384)

class _Troop(object):
    _arc_class_path = "RPG::Troop"
    _arc_instance_variables = ['id', 'name', 'members', 'pages', 'note']
    def __init__(self):
        self.id = 0
        self.name = ""
        self.members = []
        self.pages = [RPG.Troop.Page()]
        self.note = ''

class _TroopPage(object):
    _arc_class_path = "RPG::Troop::Page"
    _arc_instance_variables = ['span', 'list']
    def __init__(self):
        self.condition = RPG.Troop.Page.Condition()
        self.span = 0
        self.list = [RPG.EventCommand()]

class _TroopCondition(object):
    _arc_class_path = "RPG::Troop::Page::Condition"
    _arc_instance_variables = ['turn_valid', 'enemy_valid',
                             'actor_valid', 'switch_valid',
                             'turn_a', 'turn_b', 'enemy_index',
                             'enemy_hp', 'actor_id', 'actor_hp',
                             'switch_id']
    def __init__(self):
        self.turn_valid = False
        self.enemy_valid = False
        self.actor_valid = False
        self.switch_valid = False
        self.turn_a = 0
        self.turn_b = 0
        self.enemy_index = 0
        self.enemy_hp = 50
        self.actor_id = 1
        self.actor_hp = 50
        self.switch_id = 1

class _Member(object):
    _arc_class_path = "RPG::Troop::Member"
    _arc_instance_variables = ['enemy_id', 'x', 'y', 'hidden', 'immortal']
    def __init__(self):
        self.enemy_id = 1
        self.x = 0
        self.y = 0
        self.hidden = False
        self.immortal = False

class _Weapon(object):
    _arc_class_path = "RPG::Weapon"
    _arc_instance_variables = ['id', 'name', 'icon_name', 'description',
                             'animation1_id', 'animation2_id', 'price',
                             'atk', 'pdef', 'mdef', 'str_plus', 'dex_plus',
                             'agi_plus', 'int_plus', 'element_set',
                             'plus_state_set', 'minus_state_set', 'note']
    def __init__(self):
        self.id = 0
        self.name = ""
        self.icon_name = ""
        self.description = ""
        self.animation1_id = 0
        self.animation2_id = 0
        self.price = 0
        self.atk = 0
        self.pdef = 0
        self.mdef = 0
        self.str_plus = 0
        self.dex_plus = 0
        self.agi_plus = 0
        self.int_plus = 0
        self.element_set = []
        self.plus_state_set = []
        self.minus_state_set = []
        self.note = ''

def instance_repr(self):
    results = []
    for key, value in self.__dict__.items():
        if key[0] != "_":
            if not isinstance(value, (types.FunctionType, types.ClassType, types.MethodType, 
                                      types.ModuleType, types.SliceType, types.LambdaType, 
                                      types.GeneratorType)):
                results.append(key)
    parts = []
    for key in results:
        parts.append("%s:%s" % (key, repr(getattr(self, key))))
    template =  ("%s, " * (len(results) - 1)) + "%s"
    data =  tuple(parts)
    instane_vars = template % data
    return "<%s instance at %s: %s>" % (self.__class__.__name__, id(self), instane_vars)

class RPG(object):
    __repr__ = instance_repr
    _arc_class_path = "RPG"
    Actor = _Actor
    Animation = _Animation
    Animation.Frame = _Frame
    Animation.Timing = _Timing
    Armor = _Armor
    AudioFile = _AudioFile
    Weapon = _Weapon
    Troop = _Troop
    Troop.Member = _Member
    Troop.Page = _TroopPage
    Troop.Page.Condition = _TroopCondition
    Tileset = _Tileset
    System = _System
    System.TestBattler = _TestBattler
    System.Words = _Words
    State = _State
    Skill = _Skill
    MoveRoute = _MoveRoute
    MoveCommand = _MoveCommand
    MapInfo = _MapInfo
    Map = _Map
    Item = _Item
    EventCommand = _EventCommand
    Event = _Event
    Event.Page = _EventPage
    Event.Page.Graphic = _EventGraphic
    Event.Page.Condition = _EventCondition
    Enemy = _Enemy
    Enemy.Action = _Action
    CommonEvent = _CommonEvent
    Class = _Class
    Class.Learning = _Learning

    Actor.__repr__ = instance_repr
    Animation.__repr__ = instance_repr
    Animation.Frame.__repr__ = instance_repr
    Animation.Timing.__repr__ = instance_repr
    Armor.__repr__ = instance_repr
    AudioFile.__repr__ = instance_repr
    Weapon.__repr__ = instance_repr
    Troop.__repr__ = instance_repr
    Troop.Member.__repr__ = instance_repr
    Troop.Page.__repr__ = instance_repr
    Troop.Page.Condition.__repr__ = instance_repr
    Tileset.__repr__ = instance_repr
    System.__repr__ = instance_repr
    System.TestBattler.__repr__ = instance_repr
    System.Words.__repr__ = instance_repr
    State.__repr__ = instance_repr
    Skill.__repr__ = instance_repr
    MoveRoute.__repr__ = instance_repr
    MoveCommand.__repr__ = instance_repr
    MapInfo.__repr__ = instance_repr
    Map.__repr__ = instance_repr
    Item.__repr__ = instance_repr
    EventCommand.__repr__ = instance_repr
    Event.__repr__ = instance_repr
    Event.Page.__repr__ = instance_repr
    Event.Page.Graphic.__repr__ = instance_repr
    Event.Page.Condition.__repr__ = instance_repr
    Enemy.__repr__ = instance_repr
    Enemy.Action.__repr__ = instance_repr
    CommonEvent.__repr__ = instance_repr
    Class.__repr__ = instance_repr
    Class.Learning.__repr__ = instance_repr
    

def extend_namespace(self, namespace):
    namespace.update(self.__dict__)
