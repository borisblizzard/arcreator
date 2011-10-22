import Kernel
from Kernel import Manager as KM

if Kernel.GlobalObjects.has_key("CurrentProjectDir"):
    Kernel.GlobalObjects.set_value("CurrentProjectDir", 'C:/Users/Eric/Documents/ARC/Project1/New Project.arcproj')
#get a project loader
projectloader = KM.get_component("ARCProjectLoader").object()
projectloader.load('C:/Users/Eric/Documents/ARC/Project1/New Project.arcproj')
#place the project in the global namespace
if Kernel.GlobalObjects.has_key("PROJECT"):
    Kernel.GlobalObjects.set_value("PROJECT", projectloader.getProject())
else:
    Kernel.GlobalObjects.request_new_key("PROJECT", "CORE", projectloader.getProject())
#set the Project Title
if Kernel.GlobalObjects.has_key("Title"):
    Kernel.GlobalObjects.set_value("Title", projectloader.getProject().getInfo("Title"))
else:
    Kernel.GlobalObjects.request_new_key("Title", "CORE", projectloader.getProject().getInfo("Title"))
#set the current project directory
if Kernel.GlobalObjects.has_key("CurrentProjectDir"):
    Kernel.GlobalObjects.set_value("CurrentProjectDir", os.path.dirname(path))
else:
    Kernel.GlobalObjects.request_new_key("CurrentProjectDir", "CORE", os.path.dirname(path))
#set that there is an open project
if Kernel.GlobalObjects.has_key("ProjectOpen"):
    Kernel.GlobalObjects.set_value("ProjectOpen", True)
else:
    Kernel.GlobalObjects.request_new_key("ProjectOpen", "CORE", True)