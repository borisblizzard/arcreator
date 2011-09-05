import sys
import os
import time

from RGSS1_RPG import RPG
from RPGutil import *

import ARC_Dump

exe_path = os.path.dirname(os.path.abspath(__file__))

frompath = exe_path + '/python_import'
topath = exe_path + '/python_export' 


def arc_load_data(filename):
    print "- Loading ARC %s..." % filename
    f = open(filename, 'rb')
    data = ARC_Dump.load(f, {}, globals())
    f.close()
    return data

def arc_dump_data(filename, data):
    print "- Dumping ARC %s..." % filename
    f = open(filename, 'wb')
    ARC_Dump.dump(data, f)
    f.close()
    
 
print "================================"
print "Python ARC load and dump test"
print "================================"
#load /Data
t1 = time.time()
actors = arc_load_data(frompath + "/Data/Actors.arc")
classes = arc_load_data(frompath + "/Data/Classes.arc")
skills = arc_load_data(frompath + "/Data/Skills.arc")
items = arc_load_data(frompath + "/Data/Items.arc")
weapons = arc_load_data(frompath + "/Data/Weapons.arc")
armors = arc_load_data(frompath + "/Data/Armors.arc")
enemies = arc_load_data(frompath + "/Data/Enemies.arc")
troops = arc_load_data(frompath + "/Data/Troops.arc")
states = arc_load_data(frompath + "/Data/States.arc")
animations = arc_load_data(frompath + "/Data/Animations.arc")
tilesets = arc_load_data(frompath + "/Data/Tilesets.arc")
common_events = arc_load_data(frompath + "/Data/CommonEvents.arc")
system = arc_load_data(frompath + "/Data/System.arc")
map_infos = arc_load_data(frompath + "/Data/MapInfos.arc")
scripts = arc_load_data(frompath + "/Data/Scripts.arc")
maps = []
for key, map in map_infos.items():
    _map = arc_load_data(frompath + "/Data/Map%03d.arc" % key)
    maps.append(_map)
print ""
print "Loading took %s s" % (time.time()-t1)
print ""

#dump Data
t1 = time.time()
arc_dump_data(topath + "/Data/Actors.arc", actors)
arc_dump_data(topath + "/Data/Classes.arc", classes)
arc_dump_data(topath + "/Data/Skills.arc", skills)
arc_dump_data(topath + "/Data/Items.arc", items)
arc_dump_data(topath + "/Data/Weapons.arc", weapons)
arc_dump_data(topath + "/Data/Armors.arc", armors)
arc_dump_data(topath + "/Data/Enemies.arc", enemies)
arc_dump_data(topath + "/Data/Troops.arc", troops)
arc_dump_data(topath + "/Data/States.arc", states)
arc_dump_data(topath + "/Data/Animations.arc", animations)
arc_dump_data(topath + "/Data/Tilesets.arc", tilesets)
arc_dump_data(topath + "/Data/CommonEvents.arc", common_events)
arc_dump_data(topath + "/Data/System.arc", system)
arc_dump_data(topath + "/Data/MapInfos.arc", map_infos)
arc_dump_data(topath + "/Data/Scripts.arc", scripts)
i = 0
for key, map in map_infos.items():
    arc_dump_data(topath + "/Data/Map%03d.arc" % key, maps[i])
    i += 1
print ""
print "Dumping took %s s" % (time.time()-t1)
print ""

print "Done"