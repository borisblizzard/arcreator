from RMXPProject import Project
import RGSS1_RPG as RPG	

for i in xrange(10):
	Project.Data_actors.append(RPG.Actor())
	Project.Data_classes.append(RPG.Class())
	Project.Data_skills.append(RPG.Item())
	Project.Data_items.append(RPG.Item())
	Project.Data_weapons.append(RPG.Weapon())
	Project.Data_armors.append(RPG.Armor())
	
	
