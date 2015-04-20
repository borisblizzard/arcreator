import wx

import Kernel
from PyitectConsumes import PanelBase, Tilesets_Panel_Template
from PyitectConsumes import DatabaseManager as DM

from PyitectConsumes import ChangeMaximum_Dialog
from PyitectConsumes import ChooseGraphic_Dialog
from PyitectConsumes import ChooseFogGraphic_Dialog

# --------------------------------------------------------------------------------------
# Tilesets_Panel
# --------------------------------------------------------------------------------------

# Implementing Tilesets_Panel


class Tilesets_Panel(Tilesets_Panel_Template, PanelBase):

    _arc_panel_info_string = "Name Caption Center CloseB CaptionV DestroyOC Floatable Float IconARCM MaximizeB MinimizeM MinimizeB Movable NotebookD Resizable Snappable"
    _arc_panel_info_data = {"Name": "Tilesets Panel", "Caption": "Tilesets Panel", "CaptionV": True,  "MinimizeM": ["POS_SMART", "CAPT_SMART", ],
                            "MinimizeB": True, "CloseB": True, 'IconARCM': 'tilesetsicon'}

    def __init__(self, parent):
        Tilesets_Panel_Template.__init__(self, parent)

        DM.DrawHeaderBitmap(self.bitmapTilesets, 'Tilesets')

        # Bind the panel tot he Panel Manager
        self.bindPanelManager()

    # Handlers for Tilesets_Panel events.
    def listBoxTilesets_SelectionChanged(self, event):
        # TODO: Implement listBoxTilesets_SelectionChanged
        pass

    def buttonMaximum_Clicked(self, event):
        # TODO: Implement buttonMaximum_Clicked
        pass

    def textCtrlName_ValueChanged(self, event):
        # TODO: Implement textCtrlName_ValueChanged
        pass

    def comboBoxTileset_Clicked(self, event):
        # TODO: Implement comboBoxTileset_Clicked
        pass

    def comboBoxAutotiles1_Clicked(self, event):
        # TODO: Implement comboBoxAutotiles1_Clicked
        pass

    def comboBoxAutotiles2_Clicked(self, event):
        # TODO: Implement comboBoxAutotiles2_Clicked
        pass

    def comboBoxAutotiles3_Clicked(self, event):
        # TODO: Implement comboBoxAutotiles3_Clicked
        pass

    def comboBoxAutotiles4_Clicked(self, event):
        # TODO: Implement comboBoxAutotiles4_Clicked
        pass

    def comboBoxAutotiles5_Clicked(self, event):
        # TODO: Implement comboBoxAutotiles5_Clicked
        pass

    def comboBoxAutotiles6_Clicked(self, event):
        # TODO: Implement comboBoxAutotiles6_Clicked
        pass

    def comboBoxAutotiles7_Clicked(self, event):
        # TODO: Implement comboBoxAutotiles7_Clicked
        pass

    def comboBoxPanorama_Clicked(self, event):
        # TODO: Implement comboBoxPanorama_Clicked
        pass

    def comboBoxFog_Clicked(self, event):
        # TODO: Implement comboBoxFog_Clicked
        pass

    def comboBoxBattleback_Clicked(self, event):
        # TODO: Implement comboBoxBattleback_Clicked
        pass

    def bitmapTileset_LeftClick(self, event):
        # TODO: Implement bitmapTileset_LeftClick
        pass

    def bitmapTileset_LMouseDown(self, event):
        # TODO: Implement bitmapTileset_LMouseDown
        pass

    def bitmapTileset_LeftMouseUp(self, event):
        # TODO: Implement bitmapTileset_LeftMouseUp
        pass

    def bitmapTileset_RightClick(self, event):
        # TODO: Implement bitmapTileset_RightClick
        pass

    def bitmapTileset_RightMouseDown(self, event):
        # TODO: Implement bitmapTileset_RightMouseDown
        pass

    def bitmapTileset_RightMouseUP(self, event):
        # TODO: Implement bitmapTileset_RightMouseUP
        pass

    def buttonPassage_Clicked(self, event):
        # TODO: Implement buttonPassage_Clicked
        pass

    def buttonPassage4Dir_Clicked(self, event):
        # TODO: Implement buttonPassage4Dir_Clicked
        pass

    def buttonPriority_Clicked(self, event):
        # TODO: Implement buttonPriority_Clicked
        pass

    def buttonBushFlag_Clicked(self, event):
        # TODO: Implement buttonBushFlag_Clicked
        pass

    def buttonCounter_Clicked(self, event):
        # TODO: Implement buttonCounter_Clicked
        pass

    def buttonTerrainTag_Clicked(self, event):
        # TODO: Implement buttonTerrainTag_Clicked
        pass
