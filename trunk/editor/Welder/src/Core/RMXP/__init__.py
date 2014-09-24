import RGSS1_RPG

import Kernel

# bind the namespace extender function
Kernel.System.bind_event("ARCExtendNamespaceOnLoad", RGSS1_RPG.extend_namespace)

del Kernel