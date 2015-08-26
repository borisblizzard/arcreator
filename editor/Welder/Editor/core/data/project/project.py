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

    def __init__(self):
        pass


class Project(object):

    def __init__(self, path):
        self.path = str(path)
        self.cfg = {}
        self._data = {}
        self._info = {}
        self._del = {}

    def getProjectPath(self):
        return self.path

    def setData(self, key, value, changed=True):
        if not isinstance(key, str):
            raise TypeError("project key must be string")
        self._data[key] = changed
        self.setChanged(key)
        del self._del[key]

    def getData(self, key):
        if not isinstance(key, str):
            raise TypeError("project key must be string")
        if key in self._data:
            if isinstance(self._data[key], DeferredObject):
                self._data[key] = self._data[key].get()
            return self._data[key]
        else:
            raise KeyError("key '%s' does not exist in project data")

    def setChanged(self, key, state=True):
        if not isinstance(key, str):
            raise TypeError("project key must be string")
        if key not in self._info:
            self._info = {}
        self._info[key]['changed'] = state

    def getChanged(self, key):
        if not isinstance(key, str):
            raise TypeError("project key must be string")
        if key in self._data:
            if key in self._info:
                if 'changed' not in self._info[key]:
                    self.setChanged(key, False)
                return self._info[key]['changed']
            else:
                self.setChanged(key)
                return self._info[key]
        else:
            raise KeyError("key '%s' does not exist in project data")

    def removeData(self, key):
        if not isinstance(key, str):
            raise TypeError("project key must be string")
        if key in self._data:
            del self._data[key]
        if key in self._info:
            del self._info[key]
        self._del[key] = True

    def isRemoved(self, key):
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
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()

    def getDataCopy(self, key):
        data = self.getData(key)
        return copy.copy(data)

    def getDataDeepcopy(self, key):
        data = self.getData(key)
        return copy.deepcopy(data)

    def getConfig(self, key):
        return self.cfg[key]

    def setConfig(self, key, value):
        return self.cfg[key] = value
