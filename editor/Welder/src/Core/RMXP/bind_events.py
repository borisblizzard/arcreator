import Kernel
from version import VERSION

def extend_namespace(namespace):
    Kernel.System.load_plugin("RMXP", VERSION) # dont worry it doesn't get reloaded if it already it
    Kernel.System.get_plugin_module("RMXP", VERSION).extend_namespace(namespace)

Kernel.System.bind_event("ARCExtendNamespaceOnLoad", extend_namespace)
Kernel.Log("RMXP: bound RGSS1_RPG.extend_namespace to 'ARCExtendNamespaceOnLoad'", "[PLUGIN]" )