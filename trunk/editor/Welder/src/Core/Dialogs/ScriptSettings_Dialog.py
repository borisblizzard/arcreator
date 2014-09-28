from copy import deepcopy

import wx


import Kernel


#-------------------------------------------------------------------------
# ScriptSettings_Dialog
#-------------------------------------------------------------------------

from PyitectConsumes import ScriptSettings_Dialog_Template


class ScriptSettings_Dialog(ScriptSettings_Dialog_Template):

    def __init__(self, parent, scriptcontrol):
        """Basic constructor for the ScriptSettings_Dialog"""
        ScriptSettings_Dialog_Template.__init__(self, parent)
        global Config
        Config = deepcopy(Kernel.GlobalObjects.get_value(
            'Welder_config').get_section('ScriptEditor'))
        self.ScriptControl = scriptcontrol
        self.InstalledFonts = sorted(wx.FontEnumerator.GetFacenames())
        self.comboBoxFont.AppendItems(self.InstalledFonts)
        self.listBoxDisplayItems.SetSelection(0)
        self.panelForeColor.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.panelBackColor.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.RefreshFontPage()

    def GetStyle(self, index):
        """Returns the associated style at the passed index"""
        SM = Kernel.System.load("ScriptEditorManager")
        return SM.GetStyles()[index]

    def ParseFormatString(self, index):
        """Parses the user defined format string for the style, and returns it"""
        SM = Kernel.System.load("ScriptEditorManager")
        key = self.GetStyle(index)[1]
        fstring = Config.get(key)
        style = ScintillaStyle()
        for format in fstring.split(','):
            if format.startswith('fore:'):
                style.fore = SM.ParseColor(format.split(':')[1])
            elif format.startswith('back:'):
                style.back = SM.ParseColor(format.split(':')[1])
            elif format.startswith('face:'):
                style.face = format.split(':')[1]
            elif format.startswith('size:'):
                style.size = int(format.split(':')[1])
            elif format.lower() == 'bold':
                style.bold = True
            elif format.lower() == 'italic':
                style.italic = True
        if style.face is None:
            if index == 0:
                style.face = self.GetSystemFont()
            else:
                style.face = self.ParseFormatString(0).face
        if style.size is None:
            if index == 0:
                style.size = 10
            else:
                style.size = self.ParseFormatString(0).size
        return style

    def GetSystemFont(self):
        """Returns a default mono-spaced font for the system"""
        return wx.Font(10, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL,
                       wx.FONTWEIGHT_NORMAL).GetFaceName()

    def listBoxDisplayItems_SelectionChanged(self, event):
        """Refreshes the page to show the selected item's style"""
        self.RefreshFontPage()

    def RefreshFontPage(self):
        """Refreshes the controls to reflect the selected style"""
        itemIndex = self.listBoxDisplayItems.GetSelection()
        if itemIndex < 0:
            return
        style = self.ParseFormatString(itemIndex)
        try:
            index = self.InstalledFonts.index(style.face)
        except:
            index = self.InstalledFonts.index(style.GetSystemFont())
            Kernel.Log(str.format('Font \"{}\" not found on system.', style.face),
                       '[Script Editor]', True, False)
        self.comboBoxFont.SetSelection(index)
        self.textCtrlForeColor.ChangeValue(style.GetForeColorAsString())
        self.textCtrlBackColor.ChangeValue(style.GetBackColorAsString())
        self.checkBoxBold.SetValue(style.bold)
        self.checkBoxItalic.SetValue(style.italic)
        style.size = max(6, min(style.size, 24))
        self.comboBoxSize.SetSelection(style.size - 6)
        self.panelForeColor.SetBackgroundColour(style.fore)
        self.panelBackColor.SetBackgroundColour(style.back)
        self.panelForeColor.Refresh()
        self.panelBackColor.Refresh()

    def RefreshEditorPage(self):
        """Refreshes the controls to reflect the selected style"""
        SM = Kernel.System.load("ScriptEditorManager")
        self.spinCtrlTabWidth.SetValue(int(Config.get('tab_width')))
        self.spinCtrlEdgeColumn.SetValue(int(Config.get('edge_column')))
        self.checkBoxCaret.SetValue(Config.get('show_caret').lower() == 'true')
        self.checkBoxIndentGuides.SetValue(
            Config.get('indent_guides').lower() == 'true')
        self.checkBoxBraceMatch.SetValue(
            Config.get('brace_match').lower() == 'true')
        self.spinCtrlCaretAlpha.SetValue(int(Config.get('caret_alpha')))
        fore = SM.ParseColor(Config.get('caret_fore'))
        back = SM.ParseColor(Config.get('caret_back'))
        self.panelCaretFore.SetBackgroundColour(fore)
        self.panelCaretBack.SetBackgroundColour(back)
        self.textCtrlCaretFore.ChangeValue(
            fore.GetAsString(wx.C2S_HTML_SYNTAX))
        self.textCtrlCaretBack.ChangeValue(
            back.GetAsString(wx.C2S_HTML_SYNTAX))
        self.panelCaretFore.Refresh()
        self.panelCaretBack.Refresh()

    def updateConfig(self, style, index):
        """updates the copy of the Configuration section with the new style"""
        SM = Kernel.System.load("ScriptEditorManager")
        keys = SM.GetStyles()
        Config.set(keys[index][1], style.GetFormatString())

    def noteBookSettings_PageChanged(self, event):
        """Refreshes the page then displays and switches control to it"""
        index = event.GetSelection()
        if index == 0:
            self.RefreshFontPage()
        else:
            self.RefreshEditorPage()
        self.noteBookSettings.ChangeSelection(index)

    def comboBoxFont_SelectionChanged(self, event):
        """updates the style for this item with the new font face"""
        index = self.listBoxDisplayItems.GetSelection()
        if index < 0:
            return
        style = self.ParseFormatString(index)
        style.face = event.GetString()
        self.updateConfig(style, index)

    def comboBoxSize_SelectionChanged(self, event):
        """updates the style for this item with the new size"""
        index = self.listBoxDisplayItems.GetSelection()
        if index < 0:
            return
        style = self.ParseFormatString(index)
        style.size = int(event.GetString())
        self.updateConfig(style, index)

    def textCtrlForeColor_TextChanged(self, event):
        # TODO: Implement
        index = self.listBoxDisplayItems.GetSelection()
        if index < 0:
            return

    def buttonForeColor_Clicked(self, event):
        # TODO: Implement
        index = self.listBoxDisplayItems.GetSelection()
        if index < 0:
            return

    def textCtrlBackColor_TextChanged(self, event):
        # TODO: Implement
        index = self.listBoxDisplayItems.GetSelection()
        if index < 0:
            return

    def buttonBackColor_Clicked(self, event):
        # TODO: Implement buttonBackColor_Clicked
        pass

    def checkBoxBold_CheckChanged(self, event):
        """Changes the bold setting for the selected style and updates the config"""
        index = self.listBoxDisplayItems.GetSelection()
        if index < 0:
            return
        style = self.ParseFormatString(index)
        style.bold = event.Checked()
        self.updateConfig(style, index)

    def checkBoxItalic_CheckChanged(self, event):
        """Changes the italic setting for the selected style and updates the config"""
        index = self.listBoxDisplayItems.GetSelection()
        if index < 0:
            return
        style = self.ParseFormatString(index)
        style.italic = event.Checked()
        self.updateConfig(style, index)

    def spinCtrlTabWidth_ValueChanged(self, event):
        """updates the tab width setting in the config"""
        Config.set('tab_width', event.GetInt())

    def spinCtrlEdgeColumn_ValueChanged(self, event):
        """updates the edge column setting in the config"""
        Config.set('edge_column', str(event.GetInt()))

    def checkBoxIndentGuide_CheckChanged(self, event):
        """updates the indent guide setting in the config"""
        Config.set('indent_guides', str(event.Checked()))

    def checkBoxCaret_CheckChanged(self, event):
        """updates the caret setting in the config"""
        Config.set('show_caret', str(event.Checked()))

    def checkBoxBraceMatch_CheckChanged(self, event):
        """updates the brace matching setting in the config"""
        Config.set('brace_match', str(event.Checked()))

    def textCtrlCaretFore_TextChanged(self, event):
        # TODO: Implement textCtrlCaretColor_TextChanged
        print('text fore')
        pass

    def textCtrlCaretBack_TextChanged(self, event):
        # TODO: Implement textCtrlCaretColor_TextChanged
        print('text back')
        pass

    def buttonCaretFore_Clicked(self, event):
        # TODO: Implement buttonCaretColor_Clicked
        print('button fore')
        pass

    def buttonCaretBack_Clicked(self, event):
        # TODO: Implement buttonCaretColor_Clicked
        print('button back')
        pass

    def spinCtrlCaretAlpha_ValueChanged(self, event):
        """updates the caret alpha setting in the config"""
        Config.set('caret_alpha', str(event.GetInt()))

    def buttonOK_Clicked(self, event):
        """Ends the dialog and returns wx.ID_OK"""
        self.EndModal(wx.ID_OK)

    def buttonCancel_Clicked(self, event):
        """Ends the dialog and returns wx.ID_CANCEL"""
        self.EndModal(wx.ID_CANCEL)

    def buttonDefault_Clicked(self, event):
        """Sets all the styles to the internal default settings"""
        SM = Kernel.System.load("ScriptEditorManager")
        msg = 'This action is irreversible.\nAre you sure you want to reapply all default styles?'
        if wx.MessageBox(msg, 'Confirm', wx.YES | wx.NO | wx.CENTRE, self) == wx.YES:

            # TODO: HAVE APPLY TO ALL OPEN SCRIPT CONTROLS
            SM.ApplyDefaultSettings(self.ScriptControl)
            self.EndModal(wx.ID_OK)

    def GetConfiguration(self):
        """Returns the new configuration"""
        return Config

#-------------------------------------------------------------------------
# ScintillaStyle
#-------------------------------------------------------------------------


class ScintillaStyle(object):

    def __init__(self, fore=wx.BLACK, back=wx.WHITE, face=None, size=None,
                 bold=False, italic=False):
        """Basic constructor for the ScintillaStyle"""
        self.fore = fore
        self.back = back
        self.face = face
        self.size = size
        self.bold = bold
        self.italic = italic

    def GetForeColorAsString(self):
        """Returns the fore color setting in string hexadecimal notation"""
        return self.fore.GetAsString(wx.C2S_HTML_SYNTAX)

    def GetBackColorAsString(self):
        """Returns the back color setting in string hexadecimal notation"""
        return self.back.GetAsString(wx.C2S_HTML_SYNTAX)

    def GetFormatString(self):
        """Returns a formatted string to be used with the configuration"""
        fstring = str.format('fore:{0},back:{1},face:{2},size:{3}',
                             self.GetForeColorAsString(
                             ), self.GetBackColorAsString(),
                             self.face, self.size)
        if self.bold:
            fstring += ',bold'
        if self.italic:
            fstring += ',italic'
        return fstring
