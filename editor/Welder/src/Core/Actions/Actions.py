'''
Created on Oct 10, 2011

'''
import Kernel

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
        i = 0
        success = False
        for action in actions:
            if action != None:
                if direction == 0:
                   success = action.undo()
                elif direction == 1:
                   success = action.apply()
                if not success:
                    break
                i += 1  
        if direction == 0:
            end_action = start - i
        elif direction == 1:
            end_action = start + i
        else:
            end_action = ActionManager._current_action
        ActionManager._current_action = end_action
        if ActionManager._current_action < 0:
            ActionManager._current_action = 0
        if ActionManager._current_action >= len(ActionManager._action_stack):
            ActionManager._current_action = len(ActionManager._action_stack) - 1
        if not success:
            Kernel.log("Warning: Action(s) not completed successfully", "[Action Framwork]")
        
    @staticmethod
    def AddActions(*actions):
        del ActionManager._action_stack[ActionManager._current_action + 1:]
        ActionManager._action_stack.extend(actions)

        
class ActionTemplate(object):
    
    _AM = ActionManager
    
    def __init__(self, sub_action=False):
        self._applyed = False
        self.sub_action = sub_action
        
    def apply(self):
        if not self._applyed:
            updatecurrentactionflag = False
            success = self.do_apply()
            if success:
                if not self.sub_action or not self.in_stack():
                    updatecurrentactionflag = True
                    self._AM.AddActions(self)
            
                self._applyed = True
                if not self.sub_action and updatecurrentactionflag:
                    self._AM._current_action = len(self._AM._action_stack) - 1
            return success
        else:
            return False
    
    def do_apply(self):
        return False
        
    def undo(self):
        if self._applyed:
            success = self.do_undo()
            if success:
                self._applyed = False
            return success
        else:
            return False
                
    def do_undo(self):
        return False
        
    def in_stack(self):
        return self in self._AM._action_stack
        