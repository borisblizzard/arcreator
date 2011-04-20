'''
Created on Sep 12, 2010

Contains application data for the open RMXP project

Functions is this module
------------------------
get_map - gets map data
'''
class Project(object):
    
    def __init__(self):
        self.RTP_Location = ""
        self.Location = ""
        self.Data_actors = []
        self.Data_classes = []
        self.Data_skills = []
        self.Data_items = []
        self.Data_weapons = []
        self.Data_armors = []
        self.Data_enemies = []
        self.Data_troops = []
        self.Data_states = []
        self.Data_animations = []
        self.Data_tilesets = []
        self.Data_common_events = []
        self.Data_system = []
        self.Event_redraw_flags = {}
        self.Map_infos = {}
        self.Maps = {}

    def getMap(self, id):
        if Project.Map_infos.has_key(id):
            return Project.Maps[id]
        
    def getActors(self):
        return self.Data_actors
   
    def getClasses(self):
        return self.Data_classes
    
    def getSkills(self):
        return self.Data_skills
    
    def getItems(self):
        return self.Data_items

    def getWeapons(self):
        return self.Data_weapons
    
    def getArmors(self):
        return self.Data_armors
    
    def getEnemies(self):
        return self.Data_enemies
    
    def getTroops(self):
        return self.Data_troops
    
    def getStates(self):
        return self.Data_states
    
    def getAnimations(self):
        return self.Data_animations
    
    def getTilesets(self):
        return self.Data_tilesets
    
    def getCommonEvents(self):
        return self.Data_common_events
    
    def getSystem(self):
        return self.Data_system
    
    def getMapInfos(self):
        return self.Map_infos