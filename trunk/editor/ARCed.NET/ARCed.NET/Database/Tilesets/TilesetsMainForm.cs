#region Using Directives

using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Controls;
using ARCed.Dialogs;
using RPG;

#endregion

namespace ARCed.Database.Tilesets
{
    /// <summary>
    /// Main form for configuring Project <see cref="RPG.Tileset"/> data.
    /// </summary>
	public partial class TilesetsMainForm : DatabaseWindow
	{
		#region Private Fields

		private Tileset _tileset;

		#endregion

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

		#region Construction

		/// <summary>
		/// Default constructor
		/// </summary>
		public TilesetsMainForm()
		{
			InitializeComponent();
		}

		#endregion

		#region Public Methods

		/// <summary>
		/// Refreshes objects by type flag
		/// </summary>
		/// <param name="type">Flag for type of object to refresh</param>
		public override void NotifyRefresh(RefreshType type)
		{

		}

        /// <summary>
        /// Refreshes the form to display data for the currently selected <see cref="RPG.Tileset"/>.
        /// </summary>
		public override void RefreshCurrentObject()
		{
			SuppressEvents = true;
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
			//noteTextBox.NoteText = _tileset.note;
			string autotile;
			for (int i = 0; i < _tileset.autotile_names.Count; i++)
			{
			    autotile = _tileset.autotile_names[i];
			    var textBoxButton = this.panelAutotiles.Controls[i] as TextBoxButton;
			    if (textBoxButton != null)
			        textBoxButton.Text = String.IsNullOrWhiteSpace(autotile) ? "<None>" : autotile;
			}
            SuppressEvents = false;
		}

		#endregion

		#region Private Methods

        private void TilesetsMainFormLoad(object sender, EventArgs e)
        {
            checkBoxGrid.Checked = Editor.Settings.ImageColorSettings.ShowGrid;
            RefreshObjectList();
            InitializeAutotiles();
            dataObjectList.SelectedIndex = 0;
        }

		private void InitializeAutotiles()
		{
			for (int i = 0; i < Constants.AUTOTILES; i++)
			{
				var textBox = new TextBoxButton
				{
				    Tag = i,
				    Location = new Point(6, 6 + (i * 24)),
				    Size = new Size(this.panelAutotiles.ClientSize.Width - 12, 20),
				    Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right
				};
			    panelAutotiles.Controls.Add(textBox);
				textBox.OnButtonClick += this.TextBoxAutotileButtonClick;
			}
		}

		private void TextBoxAutotileButtonClick(object sender, EventArgs e)
		{
		    var textBoxButton = sender as TextBoxButton;
		    if (textBoxButton == null) return;
		    var index = Convert.ToInt32(textBoxButton.Tag);
		    string tile = this._tileset.autotile_names[index];
		    using (var dialog = new ImageSelectionForm(@"Autotiles", tile))
		    {
		        if (dialog.ShowDialog(this) != DialogResult.OK) return;
		        var name = dialog.ImageName;
		        this._tileset.autotile_names[index] = name;
		        textBoxButton.Text = String.IsNullOrWhiteSpace(name) ? "<None>" : name;
		        this.tilesetXnaPanel.Invalidate();
		    }
		}

        private void DataObjectListOnListBoxIndexChanged(object sender, EventArgs e)
		{
			var index = dataObjectList.SelectedIndex;
            if (index < 0) return;
            this._tileset = this.Data[index + 1];
            this.RefreshCurrentObject();
		}

		private void ButtonColorsClick(object sender, EventArgs e)
		{
			using (var dialog = new ImageColorsDialog(Editor.Settings.ImageColorSettings))
			{
				dialog.XnaPanel = tilesetXnaPanel;
			    if (dialog.ShowDialog() == DialogResult.OK) return;
			    Editor.Settings.ImageColorSettings = dialog.OriginalSettings;
			    this.tilesetXnaPanel.Invalidate();
			}
		}

		private void CheckBoxGridCheckedChanged(object sender, EventArgs e)
		{
			Editor.Settings.ImageColorSettings.ShowGrid = checkBoxGrid.Checked;
			tilesetXnaPanel.Invalidate();
		}

		private void TilesetsMainFormKeyDown(object sender, KeyEventArgs e)
		{
			if (e.KeyCode == Keys.ControlKey)
				checkBoxBatch.Checked = !checkBoxBatch.Checked;
		}

		private void RadioModeClicked(object sender, EventArgs e)
		{
		    var radioButton = sender as RadioButton;
		    if (radioButton == null) return;
		    var mode = Convert.ToInt32(radioButton.Tag);
		    this.tilesetXnaPanel.TilesetMode = (TilesetMode)mode;
		}

        private void TextBoxTilesetOnButtonClick(object sender, EventArgs e)
		{
			using (var dialog = new ImageSelectionForm(@"Tilesets", _tileset.tileset_name))
			{
				dialog.Height = 640;
			    if (dialog.ShowDialog(this) != DialogResult.OK) return;
			    this._tileset.tileset_name = dialog.ImageName;
			    this.ResizeTileset();
			    this.textBoxTileset.Text = this._tileset.tileset_name;
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
	
		private void TextBoxPanoramaOnButtonClick(object sender, EventArgs e)
		{
			using (var dialog = new ImageSelectionForm(@"Panoramas", _tileset.panorama_name))
			{
				dialog.Hue = _tileset.panorama_hue;
			    if (dialog.ShowDialog(this) != DialogResult.OK) return;
			    this._tileset.panorama_name = dialog.ImageName;
			    this._tileset.panorama_hue = dialog.Hue;
			    this.textBoxPanorama.Text = this._tileset.panorama_name;
			}
		}

		private void TextBoxBattlebackOnButtonClick(object sender, EventArgs e)
		{
			using (var dialog = new ImageSelectionForm(@"Battlebacks", _tileset.battleback_name))
			{
				dialog.Width = 800;
			    if (dialog.ShowDialog(this) != DialogResult.OK) return;
			    this._tileset.battleback_name = dialog.ImageName;
			    this.textBoxBattleback.Text = this._tileset.battleback_name;
			}	
		}

		private void TextBoxFogOnTextBoxFogOnButtonClick(object sender, EventArgs e)
		{
			using (var dialog = new ImageSelectionForm(@"Fogs", _tileset.fog_name))
			{
				dialog.Hue = _tileset.fog_hue;
				dialog.ScrollX = _tileset.fog_sx;
				dialog.ScrollY = _tileset.fog_sy;
				dialog.Zoom = _tileset.fog_zoom;
				dialog.ImageOpacity = _tileset.fog_opacity;
				dialog.BlendMode = _tileset.fog_blend_type;
			    if (dialog.ShowDialog(this) != DialogResult.OK) return;
			    this._tileset.fog_name = dialog.ImageName;
			    this._tileset.fog_hue = dialog.Hue;
			    this._tileset.fog_opacity = dialog.ImageOpacity;
			    this._tileset.fog_sx = dialog.ScrollX;
			    this._tileset.fog_sy = dialog.ScrollY;
			    this._tileset.fog_zoom = dialog.Zoom;
			    this.textBoxFog.Text = this._tileset.fog_name;
			}
		}

		private void TextBoxNameTextChanged(object sender, EventArgs e)
		{
		    if (SuppressEvents) return;
		    this._tileset.name = this.textBoxName.Text;
		    int index = this.dataObjectList.SelectedIndex;
		    this.dataObjectList.Items[index] = this._tileset.ToString();
		    this.dataObjectList.Invalidate(this.dataObjectList.GetItemRectangle(index));
		}

		private void CheckBoxBatchCheckedChanged(object sender, EventArgs e)
		{
			tilesetXnaPanel.SelectionEnabled = checkBoxBatch.Checked;
		}

		private void CheckBoxIconsCheckedChanged(object sender, EventArgs e)
		{
			tilesetXnaPanel.DisplayIcons = checkBoxIcons.Checked;
		}

		private void NoteTextBoxNoteTextChanged(object sender, EventArgs e)
		{
			//if (!suppressEvents)
			//_tileset.note = noteTextBox.NoteText;
		}

		#endregion

	}
}
