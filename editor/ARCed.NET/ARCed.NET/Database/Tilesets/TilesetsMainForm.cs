using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using ARCed.Helpers;
using ARCed.Controls;

namespace ARCed.Database.Tilesets
{
	public partial class TilesetsMainForm : DatabaseWindow
	{

		private RPG.Tileset _tileset;

		#region Protected Properties

		/// <summary>
		/// Gets the object list control of this database panel.
		/// </summary>
		protected override DatabaseObjectListBox DataObjectList { get { return dataObjectList; } }

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets the data associated with this panel.
		/// </summary>
		public override List<dynamic> Data { get { return Project.Data.Tilesets; } }

		#endregion

		public TilesetsMainForm()
		{
			InitializeComponent();
			checkBoxGrid.Checked = Editor.Settings.TilesetSettings.ShowGrid;
			RefreshObjectList();
		}

		/// <summary>
		/// Refreshes objects by type flag
		/// </summary>
		/// <param name="type">Flag for type of object to refresh</param>
		public override void NotifyRefresh(RefreshType type)
		{

		}

		public override void RefreshCurrentObject()
		{
			suppressEvents = true;

			tilesetXnaPanel.Tileset = _tileset;


			suppressEvents = false;
		}

		private void dataObjectList_OnListBoxIndexChanged(object sender, EventArgs e)
		{
			int index = dataObjectList.SelectedIndex;
			if (index >= 0)
			{
				_tileset = Data[index + 1];
				RefreshCurrentObject();
			}
		}

		private void TilesetsMainForm_Load(object sender, EventArgs e)
		{
			dataObjectList.SelectedIndex = 0;
		}

		private void buttonColors_Click(object sender, EventArgs e)
		{
			using (TilemapColorDialog dialog = new TilemapColorDialog(Editor.Settings.TilesetSettings))
			{
				dialog.XnaPanel = tilesetXnaPanel;
				if (dialog.ShowDialog() != DialogResult.OK)
				{
					Editor.Settings.TilesetSettings = dialog.OriginalSettings;
					tilesetXnaPanel.Settings = dialog.OriginalSettings;
					tilesetXnaPanel.Invalidate();
				}
			}
		}

		private void checkBoxGrid_CheckedChanged(object sender, EventArgs e)
		{
			Editor.Settings.TilesetSettings.ShowGrid = checkBoxGrid.Checked;
			tilesetXnaPanel.Settings = Editor.Settings.TilesetSettings;
			tilesetXnaPanel.Invalidate();
		}

		private void TilesetsMainForm_KeyDown(object sender, KeyEventArgs e)
		{
			if (e.KeyCode == Keys.ControlKey)
				tilesetXnaPanel.SelectionEnabled = true;
		}

		private void TilesetsMainForm_KeyUp(object sender, KeyEventArgs e)
		{
			if (e.KeyCode == Keys.ControlKey)
				tilesetXnaPanel.SelectionEnabled = false;
		}

		private void radioMode_Clicked(object sender, EventArgs e)
		{
			int mode = Convert.ToInt32((sender as RadioButton).Tag);
			tilesetXnaPanel.TilesetMode = (TilesetMode)mode;
			

		}
	}
}
