from .RGSS1_RPG import extend_namespace
from .RGSS1_RPG import RPG as RGSS1_RPG


def bind_on_enable():
    import Kernel

    Kernel.System.bind_event("ARCExtendNamespaceOnLoad", extend_namespace)
    Kernel.Log(
        "RMXP: bound RGSS1_RPG.extend_namespace to 'ARCExtendNamespaceOnLoad'",
        "[PLUGIN]"
    )
