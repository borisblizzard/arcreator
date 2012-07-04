using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using ARCed.Helpers;
using ARCed.Dialogs;
using ARCed.Controls;

namespace ARCed.Database.Tilesets
{
	public partial class TilesetsMainForm : DatabaseWindow
	{

		private RPG.Tileset _tileset;
		private const int AUTOTILES = 7;

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
		}

		private void InitializeAutotiles()
		{
			for (int i = 0; i < AUTOTILES; i++)
			{
				TextBoxButton textBox = new TextBoxButton();
				textBox.Tag = i;
				textBox.Location = new Point(6, 6 + (i * 24));
				textBox.Size = new Size(panelAutotiles.ClientSize.Width - 12, 20);
				textBox.Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right;
				panelAutotiles.Controls.Add(textBox);
				textBox.OnButtonClick += new TextBoxButton.ButtonClickHandler(textBoxAutotile_ButtonClick);
			}
		}

		void textBoxAutotile_ButtonClick(object sender, EventArgs e)
		{
			int index = Convert.ToInt32((sender as TextBoxButton).Tag);
			string tile = _tileset.autotile_names[index];
			using (ImageSelectionForm dialog = new ImageSelectionForm(@"Graphics\Autotiles", tile))
			{
				dialog.SelectionEnabled = false;
				dialog.HueEnabled = false;
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					_tileset.autotile_names[index] = dialog.ImageName;
					tilesetXnaPanel.Invalidate();
				}
			}
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
			textBoxName.Text = _tileset.name;
			textBoxTileset.Text = String.IsNullOrWhiteSpace(_tileset.tileset_name) ?
				"<None>" : _tileset.tileset_name; 
			textBoxFog.Text = String.IsNullOrWhiteSpace(_tileset.fog_name) ?
				"<None>" : _tileset.fog_name;
			textBoxPanorama.Text = String.IsNullOrWhiteSpace(_tileset.panorama_name) ?
				"<None>" : _tileset.panorama_name;
			textBoxBattleback.Text = String.IsNullOrWhiteSpace(_tileset.battleback_name) ?
				"<None>" : _tileset.battleback_name;
			string autotile;
			for (int i = 0; i < _tileset.autotile_names.Count; i++)
			{
				autotile = _tileset.autotile_names[i];
				(panelAutotiles.Controls[i] as TextBoxButton).Text = 
					String.IsNullOrWhiteSpace(autotile) ? "<None>" : autotile;
			}
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
			checkBoxGrid.Checked = Editor.Settings.TilesetSettings.ShowGrid;
			RefreshObjectList();
			InitializeAutotiles();
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

		private void textBoxTileset_OnButtonClick(object sender, EventArgs e)
		{
			using (ImageSelectionForm dialog = 
				new ImageSelectionForm(@"Graphics\Tilesets", _tileset.tileset_name))
			{
				dialog.SelectionEnabled = false;
				dialog.HueEnabled = false;
				dialog.Height = 640;
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					_tileset.tileset_name = dialog.ImageName;
					tilesetXnaPanel.Invalidate();
				}
			}
		}

		private void textBoxPanorama_OnButtonClick(object sender, EventArgs e)
		{
			using (ImageSelectionForm dialog =
				new ImageSelectionForm(@"Graphics\Panoramas", _tileset.panorama_name))
			{
				dialog.SelectionEnabled = false;
				dialog.Hue = _tileset.panorama_hue;
				if (dialog.ShowDialog(this) == DialogResult.OK)
					_tileset.panorama_name = dialog.ImageName;
			}
		}

		private void textBoxBattleback_OnButtonClick(object sender, EventArgs e)
		{
			using (ImageSelectionForm dialog =
				new ImageSelectionForm(@"Graphics\Battlebacks", _tileset.battleback_name))
			{
				dialog.SelectionEnabled = false;
				dialog.HueEnabled = false;
				dialog.Width = 800;
				if (dialog.ShowDialog(this) == DialogResult.OK)
					_tileset.panorama_name = dialog.ImageName;
			}
		}

		private void textBoxName_TextChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
			{
				_tileset.name = textBoxName.Text;
				int index = dataObjectList.SelectedIndex;
				dataObjectList.Items[index] = _tileset.ToString();
				dataObjectList.Invalidate(dataObjectList.GetItemRectangle(index));
			}
		}
	}
}
