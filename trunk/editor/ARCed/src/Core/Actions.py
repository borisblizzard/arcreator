'''
Created on Oct 10, 2011

'''

class ActionManager(object):
    
    _action_stack = [None]
    _current_action = 0
    
    @staticmethod
    def Undo():
        if ActionManager._current_action > 0:
            ActionManager.BatchAction(ActionManager._current_action, ActionManager._current_action - 1, 0)
    
    @staticmethod
    def Redo():
        if len(ActionManager._action_stack) > 1:
            ActionManager.BatchAction(ActionManager._current_action, ActionManager._current_action + 1, 1)
    
    @staticmethod
    def BatchAction(start, end, direction):
        args = [start, end]
        reverse_flag= False
        if args[0] > args[1]:
            args.sort()
            reverse_flag = True
        actions = ActionManager._action_stack[args[0]:args[1]]
        if reverse_flag:
            actions.reverse()
        for action in actions:
            if action != None:
                if direction == 0:
                    action.undo()
                elif direction == 1:
                    action.apply()
        ActionManager._current_action = end
        if ActionManager._current_action < 0:
            ActionManager._current_action = 0
        if ActionManager._current_action >= len(ActionManager._action_stack):
            ActionManager._current_action = len(ActionManager._action_stack) - 1
        
    @staticmethod
    def AddActions(*actions):
        del ActionManager._action_stack[ActionManager._current_action + 1:]
        ActionManager._action_stack.extend(actions)

        
class ActionTemplate(object):
    
    _AM = ActionManager
    
    def __init__(self):
        self._applyed = False
        
    def apply(self):
        if not self._applyed:
            updatecurrentactionflag = False
            if not self.in_stack():
                updatecurrentactionflag = True
                self._AM.AddActions(self)
            self.do_apply()
            self._applyed = True
            if updatecurrentactionflag:
                self._AM._current_action = len(self._AM._action_stack) - 1
    
    def do_apply(self):
        pass
        
    def undo(self):
        if self._applyed:
            self.do_undo()
            self._applyed = False
        
    def do_undo(self):
        pass
        
    def in_stack(self):
        return self in self._AM._action_stack
        