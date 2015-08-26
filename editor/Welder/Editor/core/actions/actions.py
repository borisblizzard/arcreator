'''
Created on Oct 10, 2011

'''
import welder_kernel as kernel


class ActionStack(object):
    def __init__(self, name):
        self._stack = [None]
        self._current_action = 0
        self.name = name


class ActionManager(object):
    _action_stacks = {None: ActionStack("default")}
    _last_stack = None

    @staticmethod
    def add_stack(name):
        if name not in ActionManager._action_stacks:
            ActionManager._action_stacks[name] = ActionStack(name)
        return ActionManager._action_stacks[name]

    @staticmethod
    def remove_stack(name):
        if name in ActionManager._action_stacks:
            del ActionManager._action_stacks[name]

    @staticmethod
    def undo(stack=None):
        if stack not in ActionManager._action_stacks:
            raise RuntimeError("Action stack '%s' does not exist" % (stack,))
        ActionManager._last_stack = stack
        action_stack = ActionManager._action_stacks[stack]
        if action_stack._current_action > 0:
            ActionManager.BatchAction(
                action_stack._current_action,
                action_stack._current_action - 1,
                True,
                stack=stack)

    @staticmethod
    def redo(stack=None):
        if stack not in ActionManager._action_stacks:
            raise RuntimeError("Action stack '%s' does not exist" % (stack,))
        ActionManager._last_stack = stack
        action_stack = ActionManager._action_stacks[stack]
        if len(action_stack._stack) > 1:
            ActionManager.BatchAction(
                action_stack._current_action,
                action_stack._current_action + 1,
                False,
                stack=stack)

    @staticmethod
    def _do_actions(actions, undo):
        i = 0
        success = False
        for action in actions:
            if action is not None:
                if undo:
                    success = action.undo()
                else:
                    success = action.apply()
                if not success:
                    break
                i += 1
        return success, i

    @staticmethod
    def batch_action(start, end, undo, stack=None):
        if stack not in ActionManager._action_stacks:
            raise RuntimeError("Action stack '%s' does not exist" % (stack,))
        ActionManager._last_stack = stack
        action_stack = ActionManager._action_stacks[stack]
        args = [start, end]
        reverse_flag = False
        if args[0] > args[1]:
            args.sort()
            reverse_flag = True
        actions = action_stack[args[0]:args[1]]
        if reverse_flag:
            actions.reverse()

        success, i = ActionManager._doActions(actions, undo)

        if undo:
            end_action = start - i
        else:
            end_action = start + i

        action_stack._current_action = end_action

        if action_stack._current_action < 0:
            action_stack._current_action = 0
        if action_stack._current_action >= len(action_stack._stack):
            action_stack._current_action = len(action_stack._stack) - 1
        if not success:
            kernel.Log(
                "Warning: Action(s) not completed successfully",
                "[Action Framwork]")

    @staticmethod
    def add_actions(*actions, stack=None):
        if stack not in ActionManager._action_stacks:
            raise RuntimeError("Action stack '%s' does not exist" % (stack,))
        action_stack = ActionManager._action_stacks[stack]
        del action_stack._stack[action_stack._current_action + 1:]
        action_stack._stack.extend(actions)

    @staticmethod
    def remove_actions(*actions, stack=None):
        if stack not in ActionManager._action_stacks:
            raise RuntimeError("Action stack '%s' does not exist" % (stack,))
        action_stack = ActionManager._action_stacks[stack]
        for action in actions:
            if action in action_stack._stack:
                index = action_stack._stack.index(action)
                if index >= action_stack._current_action:
                    action_stack._current_action -= 1
                action_stack._stack.remove(action)


class ActionTemplate(object):

    _AM = ActionManager

    def __init__(self, sub_action=False, stack=None):
        self._applyed = False
        self.sub_action = sub_action
        self.stack = _AM.add_stack(stack)

    def apply(self):
        """apply the action"""
        if not self._applyed:
            updatecurrentactionflag = False
            self.before_apply()
            success = self.do_apply()
            self.after_apply(success)
            if success:
                if not self.sub_action or not self.in_stack():
                    updatecurrentactionflag = True
                    self._AM.add_actions(self, stack=self.stack.name)

                self._applyed = True
                if not self.sub_action and updatecurrentactionflag:
                    self.stack._current_action = len(self.stack._stack) - 1
            return success
        else:
            return False

    def before_apply(self):
        """called before do_apply"""
        pass

    def do_apply(self):
        """actualy modify data in a reversable way, return success"""
        return False

    def after_apply(self, success):
        """called after do_apply with sucess of do_apply"""
        pass

    def undo(self):
        """undo an applyed action"""
        if self._applyed:
            self.before_undo()
            success = self.do_undo()
            self.after_undo(success)
            if success:
                self._applyed = False
            return success
        else:
            return False

    def before_undo(self):
        """called before do_undo"""
        pass

    def do_undo(self):
        """reverse edits to data"""
        return False

    def after_undo(self, success):
        """called after do_undo with success of do_undo"""
        pass

    def in_stack(self):
        """is this action in a stack?"""
        return self in self.stack._stack

    def remove_from_stack(self):
        """"remove the action from it's stack"""
        if self.in_stack():
            self._AM.remove_actions(self, stack=self.stack.name)
