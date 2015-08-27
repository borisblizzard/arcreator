import wx
import Kernel


class MapTreeCtrl(wx.TreeCtrl):

    def __init__(self, parent, id, pos, size, edit=False):
        style = wx.TR_DEFAULT_STYLE | wx.NO_BORDER | wx.TR_HAS_BUTTONS
        self.edit = edit
        if self.edit:
            style |= wx.TR_EDIT_LABELS | wx.WANTS_CHARS
        wx.TreeCtrl.__init__(self, parent, id, pos, size, style)
        self.parent = parent
        Kernel.System.bind_event('RefreshProject', self.Refresh_Map_List)
        IconManager = Kernel.System.load("IconManager")
        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(IconManager.getBitmap("projectopen"))
        imglist.Add(IconManager.getBitmap("map"))
        imglist.Add(IconManager.getBitmap("mappile"))
        self.AssignImageList(imglist)

        root = self.AddRoot("Advanced RPG Creator Project", 0)
        items = []
        self.maps = {}
        self.struct = {0: []}

        self.Expand(root)

        self.Bind(wx.EVT_WINDOW_DESTROY, self.onClose, self)

        self.Refresh_Map_List()

    def buildStruct(self):
        project = Kernel.GlobalObjects["PROJECT"]
        mapinfos = project.getData("MapInfos")
        self.struct = {0: []}
        stack = []
        for key, value in mapinfos.items():
            self.struct[key] = []
            if value.parent_id in self.struct:
                self.struct[value.parent_id].append(key)
            else:
                stack.append([key, value])
        while len(stack) > 0:
            key, value = stack.pop()
            if value.parent_id in self.struct:
                self.struct[value.parent_id].append(key)
            else:
                stack.append([key, value])
        self.sortStruct()

    def sortStruct(self):
        project = Kernel.GlobalObjects["PROJECT"]
        mapinfos = project.getData("MapInfos")

        def chmp(key):
            return mapinfos[key].order
        for key in self.struct:
            self.struct[key].sort(key=chmp, reverse=True)

    def Refresh_Map_List(self):
        # get the roject
        project = Kernel.GlobalObjects["PROJECT"]
        # get the map infos
        mapinfos = project.getData("MapInfos")
        # clear the list
        self.DeleteAllItems()
        # set up the mapping
        self.maps = {}
        # add project root
        root = self.AddRoot(str(project.getInfo("Title")), 0)
        # creat a stack
        stack = []
        # build a sorted scruct to build the list off of
        self.buildStruct()
        # add the top level maps
        for key in self.struct[0]:
            self.maps[key] = self.AppendItem(
                root,
                mapinfos[key].name,
                1,
                data=[key, mapinfos[key].name]
            )
        # now loop through the struct and add the maps
        for key in self.struct:
            if key == 0 or mapinfos[key].parent_id == 0:
                # skip the top level maps as they have already been added
                continue
            if key not in self.maps:
                self.maps[key] = self.AppendItem(
                    self.maps[mapinfos[key].parent_id],
                    mapinfos[key].name,
                    1,
                    data=[key, mapinfos[key].name]
                )
                self.SetItemImage(self.maps[mapinfos[key].parent_id], 2)
            for id_num in self.struct[key]:
                if mapinfos[id_num].parent_id in self.maps:
                    self.maps[id_num] = self.AppendItem(
                        self.maps[mapinfos[id_num].parent_id],
                        mapinfos[id_num].name,
                        1,
                        data=[id_num, mapinfos[id_num].name]
                    )
                    self.SetItemImage(self.maps[mapinfos[id_num].parent_id], 2)
                else:
                    stack.append([id_num, mapinfos[id_num]])
        while len(stack) > 0:
            key, value = stack.pop()
            if value.parent_id in self.maps:
                self.maps[key] = self.AppendItem(
                    self.maps[value.parent_id],
                    value.name,
                    1,
                    data=[key, value.name]
                )
                self.SetItemImage(self.maps[mapinfos[key].parent_id], 2)
            else:
                stack.append([key, value])
        self.Expand(root)

    def onClose(self, event):
        Kernel.System.unbind_event('RefreshProject', self.Refresh_Map_List)
        event.Skip()
