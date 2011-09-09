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

from RPGutil import Table, Color

class Actor(object):
    _arc_class_path = "RPG::Actor"
    def __init__(self):
        self.id = 0
        self.name = ""
        self.class_id = 1
        self.initial_level = 1
        self.final_level = 99
        self.exp_basis = 30
        self.exp_inflation = 30
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

class Animation(object):
    _arc_class_path = "RPG::Animation"
    def __init__(self):
        self.id = 0
        self.name = ""
        self.animation_name = ""
        self.animation_hue = 0
        self.position = 1
        self.frame_max = 1
        self.frames = [RPG.Animation.Frame()]
        self.timings = []

class Frame(object):
    _arc_class_path = "RPG::Animation::Frame"
    def __init__(self):
        self.cell_max = 0
        self.cell_data = Table(0, 0)

class Timing(object):
    _arc_class_path = "RPG::Animation::Timing"
    def __init__(self):
        self.frame = 0
        self.se = RPG.AudioFile("", 80)
        self.flash_scope = 0
        self.flash_color = Color(255, 255, 255, 255)
        self.flash_duration = 5
        self.condition = 0

class Armor(object):
    _arc_class_path = "RPG::Armor"
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

class AudioFile(object):
    _arc_class_path = "RPG::AudioFile"
    def __init__(self, name="", volume=100, pitch=100):
        self.name = name
        self.volume = volume
        self.pitch = pitch

class Class(object):
    _arc_class_path = "RPG::Class"
    def __init__(self):
        self.id = 0
        self.name = ""
        self.position = 0
        self.weapon_set = []
        self.armor_set = []
        self.element_ranks = Table(1)
        self.state_ranks = Table(1)
        self.learnings = []

class Learning(object):
    _arc_class_path = "RPG::Class::Learning"
    def __init__(self):
        self.level = 1
        self.skill_id = 1

class CommonEvent(object):
    _arc_class_path = "RPG::CommonEvent"
    def __init__(self):
        self.id = 0
        self.name = ""
        self.trigger = 0
        self.switch_id = 1
        self.list = [RPG.EventCommand()]

class Enemy(object):
    _arc_class_path = "RPG::Enemy"
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

class Action(object):
    _arc_class_path = "RPG::Enemy::Action"
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

class Event(object):
    _arc_class_path = "RPG::Event"
    def __init__(self, x=0, y=0):
        self.id = 0
        self.name = ""
        self.x = x
        self.y = y
        self.pages = [RPG.Event.Page()]

class EventPage(object):
    _arc_class_path = "RPG::Event::Page"
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

class EventCondition(object):
    _arc_class_path = "RPG::Event::Page::Condition"
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

class EventGraphic(object):
    _arc_class_path = "RPG::Event::Page::Graphic"
    def __init__(self):
        self.tile_id = 0
        self.character_name = ""
        self.character_hue = 0
        self.direction = 2
        self.pattern = 0
        self.opacity = 255
        self.blend_type = 0

class EventCommand(object):
    _arc_class_path = "RPG::EventCommand"
    def __init__(self, code=0, indent=0, parameters=[]):
        self.code = code
        self.indent = indent
        self.parameters = parameters

class Item(object):
    _arc_class_path = "RPG::Item"
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

class Map(object):
    _arc_class_path = "RPG::Map"
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

class MapInfo(object):
    _arc_class_path = "RPG::MapInfo"
    def __init__(self):
        self.name = ""
        self.parent_id = 0
        self.order = 0
        self.expanded = False
        self.scroll_x = 0
        self.scroll_y = 0

class MoveCommand(object):
    _arc_class_path = "RPG::MoveCommand"
    def __init__(self, code=0, parameters=[]):
        self.code = code
        self.parameters = parameters

class MoveRoute(object):
    _arc_class_path = "RPG::MoveRoute"
    def __init__(self):
        self.repeat = True
        self.skippable = False
        self.list = [RPG.MoveCommand()]

class Skill(object):
    _arc_class_path = "RPG::Skill"
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

class State(object):
    _arc_class_path = "RPG::State"
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

class System(object):
    _arc_class_path = "RPG::System"
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

class TestBattler(object):
    _arc_class_path = "RPG::System::TestBattler"
    def __init__(self):
        self.actor_id = 1
        self.level = 1
        self.weapon_id = 0
        self.armor1_id = 0
        self.armor2_id = 0
        self.armor3_id = 0
        self.armor4_id = 0

class Words(object):
    _arc_class_path = "RPG::System::Words"
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

class Tileset(object):
    _arc_class_path = "RPG::Tileset"
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

class Troop(object):
    _arc_class_path = "RPG::Troop"
    def __init__(self):
        self.id = 0
        self.name = ""
        self.members = []
        self.pages = [RPG.Troop.Page()]

class TroopPage(object):
    _arc_class_path = "RPG::Troop::Page"
    def __init__(self):
        self.condition = RPG.Troop.Page.Condition()
        self.span = 0
        self.list = [RPG.EventCommand()]

class TroopCondition(object):
    _arc_class_path = "RPG::Troop::Page::Condition"
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

class Member(object):
    _arc_class_path = "RPG::Troop::Member"
    def __init__(self):
        self.enemy_id = 1
        self.x = 0
        self.y = 0
        self.hidden = False
        self.immortal = False

class Weapon(object):
    _arc_class_path = "RPG::Weapon"
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

class RPG(object):
    _arc_class_path = "RPG"
    Actor = Actor
    Animation = Animation
    Animation.Frame = Frame
    Animation.Timing = Timing
    Armor = Armor
    AudioFile = AudioFile
    Weapon = Weapon
    Troop = Troop
    Troop.Member = Member
    Troop.Page = TroopPage
    Troop.Page.Condition = TroopCondition
    Tileset = Tileset
    System = System
    System.TestBattler = TestBattler
    System.Words = Words
    State = State
    Skill = Skill
    MoveRoute = MoveRoute
    MoveCommand = MoveCommand
    MapInfo = MapInfo
    Map = Map
    Item = Item
    EventCommand = EventCommand
    Event = Event
    Event.Page = EventPage
    Event.Page.Graphic = EventGraphic
    Event.Page.Condition = EventCondition
    Enemy = Enemy
    Enemy.Action = Action
    CommonEvent = CommonEvent
    Class = Class
    Class.Learning = Learning



