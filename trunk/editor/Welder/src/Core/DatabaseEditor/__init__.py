def late_bind():

    global Controls

    import Controls
    Controls.late_bind()

    from Manager import Manager

    global Welder_Templates, Dialogs, ScriptEditor, Manager

    import Welder_Templates
    import Dialogs
    import ScriptEditor

    #late_binding
    Dialogs.late_bind()
    ScriptEditor.late_bind()

    global Actors_Panel, Animations_Panel, Armors_Panel, AudioPlayer_Panel, BattleTestActor_Panel
    global Classes_Panel, CommonEvents_Panel, Configuration_Panel, Enemies_Panel
    global EventCommands1_Panel, EventCommands2_Panel, EventCommands3_Panel, EventEditor_Panel, EventPage_Panel
    global Items_Panel, ParameterGraph_Panel, Skills_Panel, States_Panel, System_Panel, Tilesets_Panel, Troops_Panel, Weapons_Panel

    
    from Actors_Panel import Actors_Panel
    from Animations_Panel import Animations_Panel
    from Armors_Panel import Armors_Panel
    from AudioPlayer_Panel import AudioPlayer_Panel
    from BattleTestActor_Panel import BattleTestActor_Panel
    from Classes_Panel import Classes_Panel
    from CommonEvents_Panel import CommonEvents_Panel
    from Configuration_Panel import Configuration_Panel
    from Enemies_Panel import Enemies_Panel
    from Items_Panel import Items_Panel
    from ParameterGraph_Panel import ParameterGraph_Panel
    from Skills_Panel import Skills_Panel
    from States_Panel import States_Panel
    from System_Panel import System_Panel
    from Tilesets_Panel import Tilesets_Panel
    from Troops_Panel import Troops_Panel
    from Weapons_Panel import Weapons_Panel

    Welder_Templates.late_bind()
    