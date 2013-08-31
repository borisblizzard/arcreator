from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')
KM = Kernel.Manager

import wx
Panels = Core.Panels
import wx.lib.agw.foldpanelbar as fpb
import wx.lib.agw.flatnotebook as fnb
import  wx.lib.scrolledpanel as scrolled
PILCache = Core.Cache.PILCache


class EventPanel(wx.Panel, Panels.PanelBase):

    _arc_panel_info_string = "Name Caption Center CloseB CaptionV BestS MinimizeM MinimizeB MaximizeB Floatable Resizable Snappable NotebookD Movable IconARCM DestroyOC"
    _arc_panel_info_data = {"Name": "Event Editor:", "Caption": "Event Editor:", "CaptionV": True, "BestS": (32 * 10, 32 * 18), "MinimizeM": ["POS_SMART", "CAPT_SMART"],
                            "MinimizeB": True, "CloseB": True, "NotebookP": [1], 'IconARCM': 'eventlayericon'}

    def __init__(self, parent, event):
        wx.Panel.__init__(self, parent)

        self._event = event
        #self.common = event._common

        self.mainsizer = wx.BoxSizer(wx.VERTICAL)
        self.pagesizer = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonsPanel = EventButtonsPanel(self, self._event)

        self.pagesizer.Add(self.buttonsPanel, 0, wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)

        style = fnb.FNB_NODRAG | fnb.FNB_NO_X_BUTTON | fnb.FNB_FF2 | fnb.FNB_DROPDOWN_TABS_LIST | fnb.FNB_NO_NAV_BUTTONS
        self.pageNotebook = fnb.FlatNotebook(self, wx.ID_ANY, agwStyle=style)

        self.mainsizer.Add(self.pagesizer, 0, wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)
        self.mainsizer.Add(self.pageNotebook, 1, wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)

        self.SetSizer(self.mainsizer)
        self.mainsizer.Layout()

        for i in reversed(xrange(len(self._event.pages))):
            self.AddPage(i, False)
        self.pageNotebook.SetSelection(0)

        self.Bind(fnb.EVT_FLATNOTEBOOK_PAGE_CHANGED, self.OnPageChanged)

    def AddPage(self, index, select=True):
        self.Freeze()
        self.pageNotebook.AddPage(self.CreatePage(self._event.pages[index]), "Page %s" % (index + 1), select, -1)
        self.Thaw()

    def CreatePage(self, page):
        page = EventPagePanel(self, page)
        return page

    def OnPageChanged(self, event):
        print ("Page Changed To %d" % event.GetSelection())
        event.Skip()


class EventPagePanel(wx.Panel):

    def __init__(self, parent, page):
        wx.Panel.__init__(self, parent)

        self._page = page

        self.mainsizer = wx.BoxSizer(wx.HORIZONTAL)

        self.foldPanel = fpb.FoldPanelBar(self, wx.ID_ANY, wx.DefaultPosition, (150, -1), agwStyle=fpb.FPB_EXCLUSIVE_FOLD)

        #in fold panel left side
        #Conditions
        self.graphicPanelFold = self.foldPanel.AddFoldPanel("Conditions", collapsed=False)  # , foldIcons=Images
        self.conditonsPanel = EventConditionsPanel(self.graphicPanelFold, self._page)
        self.foldPanel.AddFoldPanelWindow(self.graphicPanelFold, self.conditonsPanel, flags=fpb.FPB_ALIGN_WIDTH)
        #Event Graphic
        self.graphicPanelFold = self.foldPanel.AddFoldPanel("Graphic", collapsed=True)  # , foldIcons=Images
        self.graphicPanel = EventGraphicPanel(self.graphicPanelFold, self._page.graphic)
        self.foldPanel.AddFoldPanelWindow(self.graphicPanelFold, self.graphicPanel, flags=fpb.FPB_ALIGN_WIDTH)
        #Event Move Route
        self.moveRoutePanelFold = self.foldPanel.AddFoldPanel("Move Route", collapsed=True)  # , foldIcons=Images
        self.moveRoutePanel = EventMoveRoutePanel(self.moveRoutePanelFold, self._page.graphic)
        self.foldPanel.AddFoldPanelWindow(self.moveRoutePanelFold, self.moveRoutePanel, flags=fpb.FPB_ALIGN_WIDTH)
        #Event Options
        self.optionsPanelFold = self.foldPanel.AddFoldPanel("Options", collapsed=True)  # , foldIcons=Images
        self.optionsPanel = EventOptionsPanel(self.optionsPanelFold, self._page)
        self.foldPanel.AddFoldPanelWindow(self.optionsPanelFold, self.optionsPanel, flags=fpb.FPB_ALIGN_WIDTH)
        #Event Trigger
        self.triggerPanelFold = self.foldPanel.AddFoldPanel("Trigger", collapsed=True)  # , foldIcons=Images
        self.triggerPanel = EventTriggerPanel(self.triggerPanelFold, self._page)
        self.foldPanel.AddFoldPanelWindow(self.triggerPanelFold, self.triggerPanel, flags=fpb.FPB_ALIGN_WIDTH)

        self.mainsizer.Add(self.foldPanel, 1, wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)

        #Event List
        self.listctrl = EventListCtrl(self, self._page.list, style=wx.BORDER_SUNKEN)

        self.mainsizer.Add(self.listctrl, 4, wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)

        #event commands and filter
        self.commandsPanel = EventCommandsPanel(self)

        self.mainsizer.Add(self.commandsPanel, 0, wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)

        self.SetSizer(self.mainsizer)
        self.mainsizer.Layout()


class EventConditionsPanel(wx.Panel):

    def __init__(self, parent, page):
        wx.Panel.__init__(self, parent, size=(-1, 300))
        self._page = page

        box = wx.StaticBox(self, wx.ID_ANY, "Conditions")
        self.mainsizer = wx.StaticBoxSizer(box, wx.VERTICAL)

        self.conditionsList = EventCondidtionsList(self.mainsizer.GetStaticBox(), self._page)
        self.conditionsList.SetSelection(0)       
        self.mainsizer.Add(self.conditionsList, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)

        self.conditionsProperties = EventCondidtionsPropertiesPanel(self.mainsizer.GetStaticBox(), self._page)
        self.conditionsProperties.setType(0)       
        self.mainsizer.Add(self.conditionsProperties, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)

        self.SetSizer(self.mainsizer)
        self.mainsizer.Layout()


class EventCondidtionsList(wx.HtmlListBox):

    def __init__(self, parent, page, style=wx.DEFAULT):
        wx.HtmlListBox.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, (-1, 150), style)
        self._page = page
        self.SetItemCount(4)

    def OnGetItem(self, n):
        template = " %(enabeled)s : <b>%(name)s</b>"
        data = {}
        enabeled = '<font color="green">&#x2713;</font>'
        disabled = '<font color="red">&#8211;</font>'
        if n == 0:
            data["name"] = "Switch 1"
            data["enabeled"] = enabeled if self._page.condition.switch1_valid else disabled
        elif n == 1:
            data["name"] = "Switch 2"
            data["enabeled"] = enabeled if self._page.condition.switch2_valid else disabled
        elif n == 2:
            data["name"] = "Variable"
            data["enabeled"] = enabeled if self._page.condition.variable_valid else disabled
        elif n == 3:
            data["name"] = "Self Switch"
            data["enabeled"] = enabeled if self._page.condition.self_switch_valid else disabled
        html = template % data
        return html



class EventCondidtionsPropertiesPanel(wx.Panel):

    def __init__(self, parent, page):
        wx.Panel.__init__(self, parent, size=(-1, 150))
        self._page = page
        self.type = 0
        self.index = -1
        self.mainsizer = wx.BoxSizer(wx.VERTICAL)
        
        self.setupProperties()
        self.SetSizer(self.mainsizer) 

    def setupProperties(self):
        #clear children
        self.mainsizer.Clear()
        self.DestroyChildren()
        #setup based on condition type
        if self.type == -1:  # blank
            self.dummypanel = wx.Panel(self)
            self.mainsizer.Add(self.dummypanel, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)

        elif self.type == 0:  # switch
            sizerSwitch = wx.BoxSizer(wx.VERTICAL)

            self.checkBoxSwitch = wx.CheckBox(self, wx.ID_ANY, u"Switch", wx.DefaultPosition, wx.DefaultSize, 0)
            sizerSwitch.Add(self.checkBoxSwitch, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

            comboBoxSwitchChoices = []
            self.comboBoxSwitch = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxSwitchChoices, 0)
            sizerSwitch.Add(self.comboBoxSwitch, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

            self.labelSwitchOn = wx.StaticText(self, wx.ID_ANY, u"is ON", wx.DefaultPosition, wx.DefaultSize, 0)
            self.labelSwitchOn.Wrap(-1)
            sizerSwitch.Add(self.labelSwitchOn, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

            self.mainsizer.Add(sizerSwitch, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)

        elif self.type == 1:  # variable

            sizerVariable1 = wx.BoxSizer(wx.VERTICAL)

            self.checkBoxVariable = wx.CheckBox(self, wx.ID_ANY, u"Variable", wx.DefaultPosition, wx.DefaultSize, 0)
            sizerVariable1.Add(self.checkBoxVariable, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

            comboBoxVariableChoices = []
            self.comboBoxVariable = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxVariableChoices, 0)
            sizerVariable1.Add(self.comboBoxVariable, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

            self.labeVariable1 = wx.StaticText(self, wx.ID_ANY, u"is", wx.DefaultPosition, wx.DefaultSize, 0)
            self.labeVariable1.Wrap(-1)
            sizerVariable1.Add(self.labeVariable1, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

            self.mainsizer.Add(sizerVariable1, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)

            sizerVariable2 = wx.BoxSizer(wx.VERTICAL)

            self.labelDummy = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(76, -1), 0)
            self.labelDummy.Wrap(-1)
            sizerVariable2.Add(self.labelDummy, 0, wx.ALL, 5)

            self.spinCtrlVariable = wx.SpinCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
            sizerVariable2.Add(self.spinCtrlVariable, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

            self.labelVariable2 = wx.StaticText(self, wx.ID_ANY, u"or Higher", wx.DefaultPosition, wx.DefaultSize, 0)
            self.labelVariable2.Wrap(-1)
            sizerVariable2.Add(self.labelVariable2, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)

            self.mainsizer.Add(sizerVariable2, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)

        elif self.type == 2:  # self switch

            sizerSelfSwitch = wx.BoxSizer(wx.VERTICAL)

            self.checkBoxSelfSwitch = wx.CheckBox(self, wx.ID_ANY, u"Self Switch", wx.DefaultPosition, wx.DefaultSize, 0)
            sizerSelfSwitch.Add(self.checkBoxSelfSwitch, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)

            comboBoxSelfSwitchChoices = [u"A", u"B", u"C", u"D", u"E", u"F", u"G", u"H", u"I", u"J", u"K", u"L", u"M",
                                         u"N", u"O", u"P", u"Q", u"R", u"S", u"T", u"U", u"V", u"W", u"X", u"Y", u"Z"]
            self.comboBoxSelfSwitch = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboBoxSelfSwitchChoices, 0)
            self.comboBoxSelfSwitch.SetSelection(0)
            sizerSelfSwitch.Add(self.comboBoxSelfSwitch, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

            self.labelSelfSwitch = wx.StaticText(self, wx.ID_ANY, u"is ON", wx.DefaultPosition, wx.DefaultSize, 0)
            self.labelSelfSwitch.Wrap(-1)
            sizerSelfSwitch.Add(self.labelSelfSwitch, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)

            self.mainsizer.Add(sizerSelfSwitch, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)

        elif self.type == 3:  # self variable

            sizerSelfVariable = wx.BoxSizer(wx.VERTICAL)

            self.checkBoxSelfVariable = wx.CheckBox(self, wx.ID_ANY, u"Self Variable", wx.DefaultPosition, wx.DefaultSize, 0)
            sizerSelfVariable.Add(self.checkBoxSelfVariable, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)

            self.spinCtrlSelfVariable = wx.SpinCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0)
            sizerSelfVariable.Add(self.spinCtrlSelfVariable, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

            self.labelSelfVariable = wx.StaticText(self, wx.ID_ANY, u"or Higher", wx.DefaultPosition, wx.DefaultSize, 0)
            self.labelSelfVariable.Wrap(-1)
            sizerSelfVariable.Add(self.labelSelfVariable, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)

            self.mainsizer.Add(sizerSelfVariable, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)

        elif self.type == 4:  # script

            sizerScript = wx.BoxSizer(wx.VERTICAL)

            self.labelScript = wx.CheckBox(self, wx.ID_ANY, u"Script", wx.DefaultPosition, wx.DefaultSize, 0)
            sizerScript.Add(self.labelScript, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)

            comboBoxScriptChoices = []
            self.comboBoxScript = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBoxScriptChoices, 0)
            sizerScript.Add(self.comboBoxScript, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

            self.labelScript = wx.StaticText(self, wx.ID_ANY, u"is TRUE", wx.DefaultPosition, wx.DefaultSize, 0)
            self.labelScript.Wrap(-1)
            sizerScript.Add(self.labelScript, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

            self.mainsizer.Add(sizerScript, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)

        self.mainsizer.Layout()

    def bindProperties(self):
        if self.type == -1:  # blank
            pass
        elif self.type == 0:  # switch
            pass
        elif self.type == 1:  # variable
            pass
        elif self.type == 2:  # self switch
            pass
        elif self.type == 3:  # self variable
            pass
        elif self.type == 4:  # script
            pass
           
    def setType(self, value):
        self.type = value
        self.setupProperties()


class EventOptionsPanel(wx.Panel):

    def __init__(self, parent, page):
        wx.Panel.__init__(self, parent, size=(-1, 125))
        self._page = page

        sizerOptions = wx.BoxSizer(wx.VERTICAL)

        self.checkBoxMoveAnimation = wx.CheckBox(self, wx.ID_ANY, u"Move Animation", wx.DefaultPosition, (-1, -1), 0)
        self.checkBoxMoveAnimation.SetValue(True)
        sizerOptions.Add(self.checkBoxMoveAnimation, 0, wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)

        self.checkBoxStopAnimation = wx.CheckBox(self, wx.ID_ANY, u"Stop Animation", wx.DefaultPosition, (-1, -1), 0)
        sizerOptions.Add(self.checkBoxStopAnimation, 0, wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)

        self.checkBoxDirectionFix = wx.CheckBox(self, wx.ID_ANY, u"Direction Fix", wx.DefaultPosition, (-1, -1), 0)
        sizerOptions.Add(self.checkBoxDirectionFix, 0, wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)

        self.checkBoxThrough = wx.CheckBox(self, wx.ID_ANY, u"Through", wx.DefaultPosition, (-1, -1), 0)
        sizerOptions.Add(self.checkBoxThrough, 0, wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)

        self.checkBoxAlwaysTop = wx.CheckBox(self, wx.ID_ANY, u"Always on Top", wx.DefaultPosition, (-1, -1), 0)
        sizerOptions.Add(self.checkBoxAlwaysTop, 0, wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)

        self.SetSizer(sizerOptions)
        sizerOptions.Layout()


class EventTriggerPanel(wx.Panel):
    def __init__(self, parent, page):
        wx.Panel.__init__(self, parent, size=(-1, 150))
        self._page = page

        radioBoxTriggerChoices = [ u"Action Button", u"Player Touch", u"Event Touch", u"Autorun", u"Parallel Process" ]
        self.radioBoxTrigger = wx.RadioBox(self, wx.ID_ANY, u"Trigger", wx.DefaultPosition, wx.DefaultSize, radioBoxTriggerChoices, 1, wx.RA_SPECIFY_COLS)
        self.radioBoxTrigger.SetSelection(0)


class EventButtonsPanel(wx.Panel):

    def __init__(self, parent, event):
        wx.Panel.__init__(self, parent)
        self._event = event

        self.mainsizer = wx.BoxSizer(wx.HORIZONTAL)

        sizerControls = wx.BoxSizer(wx.HORIZONTAL)

        sizerName = wx.BoxSizer(wx.VERTICAL)

        self.labelName = wx.StaticText(self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelName.Wrap(-1)
        sizerName.Add(self.labelName, 0, wx.ALL | wx.EXPAND, 5)

        self.textCtrlName = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        sizerName.Add(self.textCtrlName, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND, 5)

        self.buttonNewPage = wx.Button(self, wx.ID_ANY, u"New\nEvent Page", wx.DefaultPosition, wx.DefaultSize, 0)
        sizerControls.Add(self.buttonNewPage, 0, wx.ALL | wx.CENTER, 5)

        self.buttonCopyPage = wx.Button(self, wx.ID_ANY, u"Export\nEvent Page", wx.DefaultPosition, wx.DefaultSize, 0)
        sizerControls.Add(self.buttonCopyPage, 0, wx.ALL | wx.CENTER, 5)

        self.buttonPastePage = wx.Button(self, wx.ID_ANY, u"Import\nEvent Page", wx.DefaultPosition, wx.DefaultSize, 0)
        sizerControls.Add(self.buttonPastePage, 0, wx.ALL | wx.CENTER, 5)

        self.buttonDeletePage = wx.Button(self, wx.ID_ANY, u"Delete\nEvent Page", wx.DefaultPosition, wx.DefaultSize, 0)
        sizerControls.Add(self.buttonDeletePage, 0, wx.ALL | wx.CENTER, 5)

        self.buttonClearPage = wx.Button(self, wx.ID_ANY, u"Clear\nEvent Page", wx.DefaultPosition, wx.DefaultSize, 0)
        sizerControls.Add(self.buttonClearPage, 0, wx.ALL | wx.CENTER, 5)

        self.mainsizer.Add(sizerName, 0, wx.ALL | wx.EXPAND, 5)
        self.mainsizer.Add(sizerControls, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(self.mainsizer)
        self.mainsizer.Layout()


class EventGraphicPanel(wx.Panel):
    def __init__(self, parent, graphic):
        wx.Panel.__init__(self, parent, size=wx.Size(32*2,32*3), style=wx.BORDER_SUNKEN)
        self._graphic = graphic

        sizerGraphic = wx.BoxSizer(wx.VERTICAL)
        if self._graphic.tile_id > 0:
            rows = 1
            columns = 1
            self.tile = True
        else:
            rows = 4
            columns = 4
            self.tile = False
        self.graphic = Core.EditorGLPanel.EditorGLPanel(self, id=wx.ID_ANY, rows=rows, columns=columns, drawmode=1)
        sizerGraphic.Add(self.graphic, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)
        if self.tile:
            img = PILCache.Tile(self._graphic.character_name, self._graphic.tile_id, self._graphic.character_hue)
        else:
            img = PILCache.Character(self._graphic.character_name, self._graphic.character_hue)
        self.graphic.ChangeImage(img)

        self.sizerGraphic = sizerGraphic
        self.SetSizer(self.sizerGraphic)
        self.sizerGraphic.Layout()


class EventMoveRoutePanel(wx.Panel):
    def __init__(self, parent, move_route):
        wx.Panel.__init__(self, parent, size=(-1, 150))
        self._move_route = move_route

        self.mainsizer = wx.BoxSizer(wx.VERTICAL)

        sizerMovement = wx.StaticBoxSizer(wx.StaticBox( self, wx.ID_ANY, u"Autonomous Movement"), wx.VERTICAL)
        
        sizerMoveType = wx.BoxSizer(wx.HORIZONTAL)
        
        self.labelMoveType = wx.StaticText(self, wx.ID_ANY, u"Type:", wx.DefaultPosition, wx.Size( 36,-1 ), 0)
        self.labelMoveType.Wrap( -1 )
        sizerMoveType.Add( self.labelMoveType, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        comboBoxMoveTypeChoices = [ u"Fixed", u"Random", u"Approach", u"Custom" ]
        self.comboBoxMoveType = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 64,-1 ), comboBoxMoveTypeChoices, 0 )
        self.comboBoxMoveType.SetSelection( 0 )
        sizerMoveType.Add( self.comboBoxMoveType, 1, wx.EXPAND|wx.ALIGN_BOTTOM|wx.ALL, 5 )
        
        sizerMovement.Add( sizerMoveType, 0, wx.EXPAND, 5 )
        
        sizerMoveRoute = wx.BoxSizer( wx.HORIZONTAL )
        
        self.labelMoveDummy = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 36,-1 ), 0 )
        self.labelMoveDummy.Wrap( -1 )
        sizerMoveRoute.Add( self.labelMoveDummy, 0, wx.ALL, 5 )
        
        self.buttonMoveRoute = wx.Button( self, wx.ID_ANY, u"Move Route...", wx.DefaultPosition, wx.DefaultSize, 0 )
        sizerMoveRoute.Add( self.buttonMoveRoute, 1, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.ALIGN_RIGHT, 5 )
        
        sizerMovement.Add( sizerMoveRoute, 0, wx.EXPAND, 5 )
        
        sizerMoveSpeed = wx.BoxSizer( wx.HORIZONTAL )
        
        self.labelMoveSpeed = wx.StaticText( self, wx.ID_ANY, u"Speed:", wx.DefaultPosition, wx.Size( 36,-1 ), 0 )
        self.labelMoveSpeed.Wrap( -1 )
        sizerMoveSpeed.Add( self.labelMoveSpeed, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        comboBoxMoveSpeedChoices = [ u"1: Slowest", u"2: Slower", u"3: Slow", u"4: Fast", u"5: Faster", u"6: Fastest" ]
        self.comboBoxMoveSpeed = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 64,-1 ), comboBoxMoveSpeedChoices, 0 )
        self.comboBoxMoveSpeed.SetSelection( 3 )
        sizerMoveSpeed.Add( self.comboBoxMoveSpeed, 1, wx.EXPAND|wx.ALIGN_BOTTOM|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        sizerMovement.Add( sizerMoveSpeed, 0, wx.EXPAND, 5 )
        
        sizerMoveFreq = wx.BoxSizer( wx.HORIZONTAL )
        
        self.labelMoveFreq = wx.StaticText( self, wx.ID_ANY, u"Freq:", wx.DefaultPosition, wx.Size( 36,-1 ), 0 )
        self.labelMoveFreq.Wrap( -1 )
        sizerMoveFreq.Add( self.labelMoveFreq, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        comboBoxMoveFreqChoices = [ u"1: Lowest", u"2: Lower", u"3: Low", u"4: High", u"5: Higher", u"6: Highest" ]
        self.comboBoxMoveFreq = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 64,-1 ), comboBoxMoveFreqChoices, 0 )
        self.comboBoxMoveFreq.SetSelection( 3 )
        sizerMoveFreq.Add( self.comboBoxMoveFreq, 1, wx.EXPAND|wx.ALIGN_BOTTOM|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        sizerMovement.Add( sizerMoveFreq, 0, wx.EXPAND, 5 )

        self.mainsizer.Add(sizerMovement, 1, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 0)

        self.SetSizer(self.mainsizer)
        self.mainsizer.Layout()


class EventCommandsPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.mainsizer = wx.BoxSizer(wx.VERTICAL)

        self.foldPanel = fpb.FoldPanelBar(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, agwStyle=0)
        self.mainsizer.Add(self.foldPanel, 4, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)

        self.search = wx.SearchCtrl(self, size=(150, -1), style=wx.TE_PROCESS_ENTER)
        self.mainsizer.Add(self.search, 0, wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.EXPAND | wx.ALL, 5)

        self.SetSizer(self.mainsizer)
        self.mainsizer.Layout()


class EventListCtrl(wx.HtmlListBox):

    __KNOWN_FILLER = []

    def __init__(self, parent, list, style=wx.DEFAULT):
        wx.HtmlListBox.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, style | wx.LB_MULTIPLE)
        self.list = list
        self.strip_filler()
        self.SetItemCount(len(self.list))

    def strip_filler(self):
        for command in list(self.list):
            if command.code in self.__KNOWN_FILLER:
                self.list.remove(command)

    def OnGetItem(self, n):
        EventCommandFormater = KM.get_component("EventCommandFormater").object
        html = EventCommandFormater.format(self.list[n])
        return html

    def OnGetItemMarkup(self, n):
        html = self.OnGetItem(n)
        body = '<font face="Courier New" size="3">%s</font>' % html
        return body