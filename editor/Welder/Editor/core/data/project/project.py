import os
import time
import configparser
import zipfile
import re
import copy

import collections

import welder_kernel as kernel


class DeferredObject(object):

    def get(self):
        raise NotImplementedError("DeferredObject subclass must impliment get")


class ProjectManager(object):

    _project = None

    @classmethod
    def get_project(cls):
        """get the curent project object
        returns None if there is no Project yet"""
        return cls._project

    @classmethod
    def create_project(cls, path):
        """create a new Project

        does nothing if a project already exists
        Returns:
            bool: if a new project was created
        """
        if not cls._project:
            cls._project = Project(path)
            return True
        return False

    @classmethod
    def clear_project(cls, force=False):
        """clear the current project
        if the project needs to be saved will not clear unless force is used
        Returns:
            bool: if the project was cleared
        """
        if cls._project:
            if cls._project.needs_save() and not force:
                return False
            else:
                del cls._project
                cls._project = None
                return True
        return False

    @classmethod
    def apply_action(cls, key, action, delay=False, **kwargs):
        """apply an action to key in project data

        if delay is true delays the action for a time under a key
        if another action under the same delay key is applied inside the
        delay time, the first action is discarded and the second action
        is delayed. This allows the ability to keep the history managable
        insted of an action for every edit of a charater in some text.

        Args:
            key (str): the key in the project to apply the action to
            action (DataAction): the action to apply
            delay (bool): should the apply be delayed?
            delay_key (str): (key word only) key to store the delay under
            delay_time (int): (key word only) number of miliseconds to delay
        """
        delay_key = ""
        delay_time = 300
        for key in kwargs:
            if key == "delay_key":
                delay_key = kwargs[key]
            elif key == "delay_time":
                delay_time = kwargs[key]
            else:
                raise TypeError(
                    "apply_action() got an unexpected keyword argument %s"
                    % (key,))
        # TODO drop in a delay function


class Project(object):

    def __init__(self, path):
        self.path = str(path)
        self.cfg = {}
        self._keys = []
        self._data = {}
        self._info = {}
        self._del = {}

    def get_project_path(self):
        return self.path

    def add_key(self, key):
        if not isinstance(key, str):
            raise TypeError("project key must be string")
        if key not in self._keys:
            self._keys.append(key)
        if key not in self._data:
            self._data[key] = None
            self.set_changed(key)

    def set_data(self, key, value, changed=True):
        if not isinstance(key, str):
            raise TypeError("project key must be string")
        self.add_key(key)
        self._data[key] = changed
        self.set_changed(key)
        del self._del[key]

    def get_data(self, key):
        if not isinstance(key, str):
            raise TypeError("project key must be string")
        if key in self._data:
            if isinstance(self._data[key], DeferredObject):
                self._data[key] = self._data[key].get()
            return self._data[key]
        else:
            raise KeyError("key '%s' does not exist in project data")

    def set_changed(self, key, state=True):
        if not isinstance(key, str):
            raise TypeError("project key must be string")
        self.add_key(key)
        if key not in self._info:
            self._info = {}
        self._info[key]['changed'] = state

    def get_changed(self, key):
        if not isinstance(key, str):
            raise TypeError("project key must be string")
        if key in self._keys:
            if key in self._info:
                if 'changed' not in self._info[key]:
                    self.set_changed(key, False)
                return self._info[key]['changed']
            elif key in self._del:
                self.set_changed(key)
                return self._info[key]
            else:
                return False
        else:
            raise KeyError("key '%s' does not exist in project")

    def needs_save(self):
        return any([self.get_changed(key) for key in self._keys])

    def remove_data(self, key):
        if not isinstance(key, str):
            raise TypeError("project key must be string")
        self.add_key(key)
        if key in self._data:
            del self._data[key]
        if key in self._info:
            del self._info[key]
        self._del[key] = True

    def is_removed(self, key):
        if not isinstance(key, str):
            raise TypeError("project key must be string")
        return key in self._del

    def __getitem__(self, key):
        return self.getData(key)

    def __setitem__(self, key, value):
        return self.setData(key, value)

    def __contains__(self, item):
        return item in self._data

    def __delitem__(self, key):
        return self.removeData(key)

    def __iter__(self):
        return self._data.__iter__()

    def keys(self):
        return list(self._keys)

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()

    def get_data_copy(self, key):
        data = self.getData(key)
        return copy.copy(data)

    def get_data_deepcopy(self, key):
        data = self.getData(key)
        return copy.deepcopy(data)

    def get_config(self, key):
        return self.cfg[key]

    def set_config(self, key, value):
        self.cfg[key] = value
