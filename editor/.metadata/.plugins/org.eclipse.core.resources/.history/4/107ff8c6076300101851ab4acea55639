'''
Created on Sep 12, 2010

Contains application data for the open RMXP project

Functions is this module
------------------------
get_map - gets map data
'''
class Project(object):
    RTP_Location = ""
    Location = ""
    Data_actors = []
    Data_classes = []
    Data_skills = []
    Data_items = []
    Data_weapons = []
    Data_armors = []
    Data_enemies = []
    Data_troops = []
    Data_states = []
    Data_animations = []
    Data_tilesets = []
    Data_common_events = []
    Data_system = []
    Event_redraw_flags = {}
    Map_infos = {}
    Maps = {}

    @staticmethod
    def getMap(id):
        if Project.Map_infos.has_key(id):
            return Project.Maps[id]
