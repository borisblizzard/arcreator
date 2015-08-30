from .rpg_rgss1 import extend_namespace
from .rpg_rgss1 import RPG as RPG_RGSS1


def bind_on_enable():
    import welder_kernel as kernel

    kernel.System.bind_event("ARCExtendNamespaceOnLoad", extend_namespace)
    kernel.Log(
        "RMXP: bound RPG_RGSS1.extend_namespace to 'ARCExtendNamespaceOnLoad'",
        "[PLUGIN]"
    )
