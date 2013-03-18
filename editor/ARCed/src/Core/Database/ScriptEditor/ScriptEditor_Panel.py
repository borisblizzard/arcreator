import wx
from wx import stc
import os
from Core.Panels import PanelBase	
import Core.Database
from Core.Database import ARCed_Templates as Templates
from Core.Database import Manager as DM
from Core.Database.ScriptEditor import Manager as SM
from Core.Database.Controls import ScriptTextCtrl
import re
import Kernel
#--------------------------------------------------------------------------------------
# ScriptEditor_Panel
#--------------------------------------------------------------------------------------

class ScriptEditor_Panel( Templates.ScriptEditor_Panel, PanelBase ):

    _arc_panel_info_string = "Name Caption Center CloseB CaptionV DestroyOC Floatable Float IconARCM MaximizeB MinimizeM MinimizeB Movable NotebookD Resizable Snappable"
    _arc_panel_info_data = {"Name": "Script Editor Panel", "Caption": "Script Editor Panel", "CaptionV": True,  "MinimizeM": ["POS_SMART", "CAPT_SMART",], 
                            "MinimizeB": True, "CloseB": True, 'IconARCM': 'script_icon'}

    def __init__( self, parent, index=-1 ):
        """Basic constructor for the ScriptEditor_Panel"""
        Templates.ScriptEditor_Panel.__init__( self, parent )
        self.CreateToolBar()
        #self.statusBar = parent.CreateStatusBar()
        # TODO: give teh script editor it's own status bar
        #self.statusBar = Kernel.GlobalObjects.get_value("MainStatusBar")
        self.statusBar.SetFieldsCount(3)
        self.statusBar.SetStatusWidths([-4, -4, -2])
        # TODO: Get path by using project path + Data/Scripts/
        #path = r"C:\Users\Eric\Desktop\ARC\editor\ARCed\src\RTP\Templates\Chonicles of Sir Lag-A-Lot\Data\Scripts"
        path = os.path.join(Kernel.GlobalObjects.get_value("CurrentProjectDir"), 'Data', 'Scripts')
        try:
            SM.LoadScripts()
        except:
            Kernel.Log('Failed to successfully load all scripts.', '[ScriptEditor]', True, True)
        global Scripts
        Scripts = Kernel.GlobalObjects.get_value('Scripts')
        self.ScriptIndex = -1
        if index >= 0:
            self.OpenScript(index=index)
        self.scriptCtrl.Bind(wx.EVT_KEY_DOWN, Kernel.Protect(self.RefreshStatus))
        self.scriptCtrl.Bind(stc.EVT_STC_UPDATEUI, self.RefreshStatus)
        self.comboBoxScripts.AppendItems([script.GetName() for script in Scripts])
        self.comboBoxScripts.SetSelection(index)
        self.scriptCtrl.CalculateLineNumberMargin()
        # Bind the panel to the Panel Manager
        self.BindPanelManager()
        
    def OpenScript( self, event=None, index=None ):
        if self.ScriptIndex >= 0:
            Scripts[self.ScriptIndex].SetText(self.scriptCtrl.GetText())
        if event is not None: i = event.GetInt()
        elif index is not None: i = index
        else: return
        self.ScriptIndex = i
        self.scriptCtrl.SetText(Scripts[i].GetText())
        self.RefreshScript()

    def CreateToolBar( self ):
        """Creates the toolbar and binds events to it"""
        art = wx.ArtProvider().GetBitmap
        self.toolBar.AddSimpleTool(0, art(wx.ART_COPY), 'Copy', 'Copies the selected text')
        self.toolBar.AddSimpleTool(1, art(wx.ART_CUT), 'Cut', 'Cuts the selected text')
        self.toolBar.AddSimpleTool(2, art(wx.ART_PASTE), 'Paste', 'Pastes previously copied/cut text')
        self.toolBar.AddSeparator()
        self.toolBar.AddSimpleTool(3, art(wx.ART_UNDO), 'Undo', 'Undoes the previous action')
        self.toolBar.AddSimpleTool(4, art(wx.ART_REDO), 'Redo', 'Redoes the previous Undo')
        self.toolBar.AddSeparator()
        self.toolBar.AddSimpleTool(5, art(wx.ART_FIND), 'Find', 'Opens Find window for searching text')
        self.toolBar.AddSimpleTool(6, art(wx.ART_FIND_AND_REPLACE), 'Find and Replace', 'Open Find & Replace window for replacing text')
        self.toolBar.AddSeparator()
        self.toolBar.AddSimpleTool(7, art(wx.ART_HELP_SETTINGS), 'Settings', 'Opens the settings window')
        self.toolBar.AddSimpleTool(8, art(wx.ART_LIST_VIEW), 'Normalize Indents', 'Applies conventional Ruby indenting to the script')
        self.toolBar.AddSimpleTool(9, art(wx.ART_HELP_BOOK), 'Help', 'Opens the compiled HTML help doc')
        self.toolBar.AddSeparator()
        self.textCtrlSearch = wx.TextCtrl(self.toolBar, -1, 'Search...', style=wx.TE_RIGHT)
        self.toolBar.AddControl(self.textCtrlSearch)
        self.toolBar.AddSimpleTool(10, art(wx.ART_GO_BACK), 'Previous', '')
        self.toolBar.AddSimpleTool(11, art(wx.ART_GO_FORWARD), 'Next', '')
        self.toolBar.AddSeparator()
        self.comboBoxScripts = wx.ComboBox(self.toolBar, size=(184,-1), style=wx.GROW)
        self.comboBoxScripts.Bind(wx.EVT_COMBOBOX, self.OpenScript)
        self.comboBoxScripts.Bind(wx.EVT_TEXT, self.comboBoxScripts_TextChanged)
        self.toolBar.AddControl(self.comboBoxScripts)
        self.toolBar.AddSeparator()
        self.toolBar.AddSimpleTool(12, art(wx.ART_FILE_SAVE), 'Save', 'Saves the current script')
        self.toolBar.Realize()
        self.Bind(wx.EVT_TOOL, self.OnCopy, id=0)
        self.Bind(wx.EVT_TOOL, self.OnCut, id=1)
        self.Bind(wx.EVT_TOOL, self.OnPaste, id=2)
        self.Bind(wx.EVT_TOOL, self.OnUndo, id=3)
        self.Bind(wx.EVT_TOOL, self.OnRedo, id=4)
        self.Bind(wx.EVT_TOOL, self.OnFind, id=5)
        self.Bind(wx.EVT_TOOL, self.OnReplace, id=6)
        self.Bind(wx.EVT_TOOL, Kernel.Protect(self.OnSettings), id=7)
        self.Bind(wx.EVT_TOOL, Kernel.Protect(self.OnNormalize), id=8)
        self.Bind(wx.EVT_TOOL, Kernel.Protect(self.OnHelp), id=9)
        self.Bind(wx.EVT_TOOL, Kernel.Protect(self.FindPrevious), id=10)
        self.Bind(wx.EVT_TOOL, Kernel.Protect(self.FindNext), id=11)
        self.Bind(wx.EVT_TOOL, Kernel.Protect(self.OnSave), id=12)

    def RefreshScript( self ):
        """Refreshes the displayed text"""
        self.scriptCtrl.CalculateLineNumberMargin()
        self.RefreshStatus()
        
    def RefreshStatus( self, event=None ):
        """Refreshes the status bar text"""
        chars = len(re.sub(r'\s', '', self.scriptCtrl.Text))
        length = str.format('Lines: {0}   Characters: {1}   Position: {2}', 
            self.scriptCtrl.LineCount, chars, self.scriptCtrl.GetCurrentPos())
        self.statusBar.SetStatusText(length, 1)
        sel = len(self.scriptCtrl.SelectedText)
        if sel > 0: self.statusBar.SetStatusText(str.format('Selection: {}', sel), 2)
        else: self.statusBar.SetStatusText('', 2)
        if event is not None:
            event.Skip()
        # Update text
        if self.ScriptIndex > -1:
            Scripts[self.ScriptIndex].SetText(self.scriptCtrl.GetTextUTF8())
        
    def OnCopy( self, event ):
        """Sets the scripts selected text to the clipboard"""
        self.statusBar.SetStatusText('Copied selected text', 0)
        self.scriptCtrl.Copy()

    def OnCut( self, event ):
        """Sets the scripts selected text to the clipboard"""
        self.statusBar.SetStatusText('Cut selected text', 0)
        self.scriptCtrl.Cut()

    def OnPaste( self, event ):
        """Pastes the clipboard text to the script"""
        self.statusBar.SetStatusText('Text pasted', 0)
        self.scriptCtrl.Paste()

    def OnUndo( self, event ):
        """Performs script Undo action"""
        self.statusBar.SetStatusText('Undo applied', 0)
        self.scriptCtrl.Undo()

    def OnRedo( self, event ):
        """Performs script Redo action"""
        self.statusBar.SetStatusText('Redo applied', 0)
        self.scriptCtrl.Redo()

    def OnFind( self, event ):
        """Opens FindReplace window with Find tab focused"""
        self.scriptCtrl.StartFindReplace(0)

    def OnReplace( self, event ):
        """Opens FindReplace window with Replace tab focused"""
        self.scriptCtrl.StartFindReplace(1)

    def OnSettings( self, event ):
        from Core.Database.Dialogs import ScriptSettings_Dialog
        dlg = ScriptSettings_Dialog(self, self.scriptCtrl)
        if dlg.ShowModal() == wx.ID_OK:
            config = Kernel.GlobalObjects.get_value('ARCed_config').get_section('ScriptEditor')
            new_config = dlg.GetConfiguration()
            for key, value in new_config.iteritems():
                config.set(key, value)
            SM.ApplyUserSettings(self.scriptCtrl)

    def OnNormalize( self, event ):
        """Applies script indent normalization"""
        result = wx.MessageBox('Automatically apply conventional Ruby indents to document?', 
            'Confirm Action', wx.OK|wx.CANCEL|wx.CENTRE, self)
        if result == wx.OK:
            import time
            start = time.time()
            self.scriptCtrl.NormalizeIndenting()
            msg = str.format('Indentation applied in {} seconds', time.time() - start)
            self.statusBar.SetStatusText(msg, 0)

    def OnHelp( self, event ):
        self.statusBar.SetStatusText('Opening Help...', 0)
        print Scripts[self.ScriptIndex].IsModified()

    def OnSave( self, event ):
        """Saves the open script to disk"""
        if self.ScriptIndex >= 0:
            Scripts[self.ScriptIndex].SetText(self.scriptCtrl.GetText())
            Scripts[self.ScriptIndex].SaveScript(self.ScriptIndex)
            msg = str.format('{}.rb Saved!', Scripts[self.ScriptIndex].GetName())
            self.statusBar.SetStatusText(msg, 0)

    def comboBoxScripts_TextChanged( self, event ):
        text = event.GetString()
        Scripts[self.ScriptIndex].ChangeName(text)
        self.comboBoxScripts.SetString(self.ScriptIndex, text)
        self.comboBoxScripts.SetStringSelection(text)	

    #--------------------------------------------------------------
    # Find/Replace Functions
    #--------------------------------------------------------------
    def GetSearchLocations(self, searchString, matchcase, wholeword, scope, regex=None):
        results = {}
        """
        if scope == 0:
            scripts = [Scripts[self.listBoxScripts.GetSelection()]]
        else:
            scripts = Scripts
        if not matchcase:
            searchString = searchString.lower()
        for i, script in enumerate(scripts):
            if not matchcase: text = script.GetText().lower()
            else: text = script.GetText()
            if searchString in text:
                lines, found = text.splitlines(), []
                for j in xrange(len(lines)):
                    if searchString in lines[j] and j not in found:
                        found.append(j)
                results[i] = found
        """



        return results

    def FindPrevious( self, event ):
        result = self.scriptCtrl.Find('Tro.p', True, False, True, False, True)

    def FindNext( self, event ):
        result = self.scriptCtrl.Find('Tro.p', True, False, True, False, False)