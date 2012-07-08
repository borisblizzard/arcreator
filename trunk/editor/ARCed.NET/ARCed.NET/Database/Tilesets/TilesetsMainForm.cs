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
			for (int i = 0; i < Constants.AUTOTILES; i++)
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
			using (ImageSelectionForm dialog = new ImageSelectionForm(@"Autotiles", tile))
			{
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					string name = dialog.ImageName;
					_tileset.autotile_names[index] = name;
					(sender as TextBoxButton).Text = String.IsNullOrWhiteSpace(name) ?
						"<None>" : name;
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
			checkBoxGrid.Checked = Editor.Settings.ImageColorSettings.ShowGrid;
			RefreshObjectList();
			InitializeAutotiles();
			dataObjectList.SelectedIndex = 0;
		}

		private void buttonColors_Click(object sender, EventArgs e)
		{
			using (ImageColorsDialog dialog = new ImageColorsDialog(Editor.Settings.ImageColorSettings))
			{
				dialog.XnaPanel = tilesetXnaPanel;
				if (dialog.ShowDialog() != DialogResult.OK)
				{
					Editor.Settings.ImageColorSettings = dialog.OriginalSettings;
					tilesetXnaPanel.Invalidate();
				}
			}
		}

		private void checkBoxGrid_CheckedChanged(object sender, EventArgs e)
		{
			Editor.Settings.ImageColorSettings.ShowGrid = checkBoxGrid.Checked;
			tilesetXnaPanel.Invalidate();
		}

		private void TilesetsMainForm_KeyDown(object sender, KeyEventArgs e)
		{
			if (e.KeyCode == Keys.ControlKey)
				checkBoxBatch.Checked = !checkBoxBatch.Checked;
		}

		private void radioMode_Clicked(object sender, EventArgs e)
		{
			int mode = Convert.ToInt32((sender as RadioButton).Tag);
			tilesetXnaPanel.TilesetMode = (TilesetMode)mode;
		}

		private void textBoxTileset_OnButtonClick(object sender, EventArgs e)
		{
			using (ImageSelectionForm dialog = 
				new ImageSelectionForm(@"Tilesets", _tileset.tileset_name))
			{
				dialog.Height = 640;
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					_tileset.tileset_name = dialog.ImageName;
					ResizeTileset();
					textBoxTileset.Text = _tileset.tileset_name;
				}
			}
		}

		private void ResizeTileset()
		{
			tilesetXnaPanel.Tileset = _tileset;
			Size size = tilesetXnaPanel.Size;
			int ids = (size.Height / Constants.TILESIZE) * (size.Width / Constants.TILESIZE);
			ids += Constants.AUTO_IDS;
			_tileset.priorities.resize(ids);
			_tileset.passages.resize(ids);
			_tileset.terrain_tags.resize(ids);
			RefreshCurrentObject();
		}	
	
		 void textBoxPanorama_OnButtonClick(object sender, EventArgs e)
		{
			using (ImageSelectionForm dialog =
				new ImageSelectionForm(@"Panoramas", _tileset.panorama_name))
			{
				dialog.Hue = _tileset.panorama_hue;
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					_tileset.panorama_name = dialog.ImageName;
					_tileset.panorama_hue = dialog.Hue;
					textBoxPanorama.Text = _tileset.panorama_name;
				}
			}
		}

		private void textBoxBattleback_OnButtonClick(object sender, EventArgs e)
		{
			using (ImageSelectionForm dialog =
				new ImageSelectionForm(@"Battlebacks", _tileset.battleback_name))
			{
				dialog.Width = 800;
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					_tileset.battleback_name = dialog.ImageName;
					textBoxBattleback.Text = _tileset.battleback_name;
				}
			}	
		}

		private void textBoxFog_OnButtonClick(object sender, EventArgs e)
		{
			using (ImageSelectionForm dialog =
				new ImageSelectionForm(@"Fogs", _tileset.fog_name))
			{
				dialog.Hue = _tileset.fog_hue;
				dialog.ScrollX = _tileset.fog_sx;
				dialog.ScrollY = _tileset.fog_sy;
				dialog.Zoom = _tileset.fog_zoom;
				dialog.ImageOpacity = _tileset.fog_opacity;
				dialog.BlendMode = _tileset.fog_blend_type;
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					_tileset.fog_name = dialog.ImageName;
					_tileset.fog_hue = dialog.Hue;
					_tileset.fog_opacity = dialog.ImageOpacity;
					_tileset.fog_sx = dialog.ScrollX;
					_tileset.fog_sy = dialog.ScrollY;
					_tileset.fog_zoom = dialog.Zoom;
					textBoxFog.Text = _tileset.fog_name;
				}
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

		private void checkBoxBatch_CheckedChanged(object sender, EventArgs e)
		{
			tilesetXnaPanel.SelectionEnabled = checkBoxBatch.Checked;
		}
	}
}
