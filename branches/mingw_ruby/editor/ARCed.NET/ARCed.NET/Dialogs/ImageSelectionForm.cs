#region Using Directives

using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Windows.Forms;
using ARCed.Core;
using ARCed.Helpers;
using ARCed.Properties;

#endregion

namespace ARCed.Dialogs
{
	/// <summary>
	/// Dialog for getting a user-selected game graphic
	/// </summary>
	internal partial class ImageSelectionForm : Form
	{
		#region Private Fields

		private List<GameResource> _resources;
		private string _folder;
		private string _filename;
		private bool _initialized;

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets the image under the selection rectangle
		/// </summary>
        public Image SelectedImage { get; private set; }

		/// <summary>
		/// Gets or sets the hue rotation applied to the image
		/// </summary>
		public int Hue
		{
			get { return this.trackBarHue.Value; }
			set { this.trackBarHue.Value = value.Clamp(0, 359); }
		}

		public int ImageOpacity
		{
			get { return (int)this.numericOpacity.Value; }
			set 
			{ 
				this.numericOpacity.Value = value.Clamp(0, 255);
				this.pictureBox.ImageOpacity = value.Clamp(0, 255);
			}
		}

		public int Zoom
		{
			get { return (int)this.numericZoom.Value; }
			set { this.numericZoom.Value = value.Clamp(100, 800); }
		}

		public int ScrollX
		{
			get { return (int)this.numericSX.Value; }
			set { this.numericSX.Value = value.Clamp(-480, 480); }
		}

		public int ScrollY
		{
			get { return (int)this.numericSY.Value; }
			set { this.numericSY.Value = value.Clamp(-480, 480); }
		}

		public int BlendMode
		{
			get { return this.comboBoxBlend.SelectedIndex; }
			set { this.comboBoxBlend.SelectedIndex = value.Clamp(0, 2); }
		}

		/// <summary>
		/// Gets or sets the root folder searched for images
		/// </summary>
		public string ImageFolder 
		{
			get { return this._folder; }
			set { this.SetFolder(value); }
		}

		/// <summary>
		/// Gets or sets the filename (without extension) of the image that is found in the current folder
		/// </summary>
		public string ImageName
		{
			get { return Path.GetFileNameWithoutExtension(this._filename); }
			set { this.SetFilename(value); }
		}

		/// <summary>
		/// Gets or sets the ability to select individual tiles of the _srcTexture
		/// </summary>
		public bool SelectionEnabled 
		{
			get { return this.pictureBox.SelectionEnabled; }
			set { this.pictureBox.SelectionEnabled = value; }
		}

		/// <summary>
		/// Gets or sets the visibility of the trackbar for changing image hue.
		/// </summary>
		public bool HueEnabled 
		{
			get { return this.groupBoxHue.Enabled; }
			set { this.groupBoxHue.Enabled = value; }
		}

		/// <summary>
		/// Gets or sets the visibility of the panel for changing options.
		/// </summary>
		public bool OptionsEnabled
		{
			get { return this.groupBoxOptions.Enabled; }
			set { this.groupBoxOptions.Enabled = value; }
		}

		/// <summary>
		/// Gets or sets the enabled status of the scroll options.
		/// </summary>
		public bool AdvancedOptionEnabled
		{
			get { return this.pictureBox.AdvancedEnabled; }
			set { this.pictureBox.AdvancedEnabled = this.panelAdvanced.Enabled = value; }
		}

		#endregion

		#region Construction

		public void SetDefaultOptions(string folder)
		{
			var hue = new List<string> { "Animations", "Battlers", "Characters",
				"Fogs", "Panoramas", "Pictures" };
			var options = new List<string> { "Battlers", "Fogs" };
			this.OptionsEnabled = options.Contains(folder);
			this.HueEnabled = hue.Contains(folder);
			this.AdvancedOptionEnabled = (folder == "Fogs");
		}

		/// <summary>
		/// Constructor that sets the folder and selected _srcTexture
		/// </summary>
		/// <param name="folder">Root folder searched for images</param>
		/// <param name="filename">FullPath (without extension) of the _srcTexture that is found in the current folder</param>
		public ImageSelectionForm(string folder, string filename) : this()
		{
			// Find all valid filenames
			this._folder = folder;
			this._filename = filename;
		}

		/// <summary>
		/// Default constructor
		/// </summary>
		public ImageSelectionForm()
		{
			this.InitializeComponent();
			ResizeBegin += (s, e) => SuspendLayout();
			ResizeEnd += (s, e) => ResumeLayout();
		}

		private void ImageSelectionFormLoad(object sender, EventArgs e)
		{
			if (this._folder != null)
			{
				this.SetDefaultOptions(this._folder);
				if (!this._folder.StartsWith("Graphics"))
					this._folder = Path.Combine("Graphics", this._folder);
				this._resources = ResourceHelper.GetTypes(this._folder);
				this.SetFolder(this._folder);
			}
			else
				this._resources = new List<GameResource>();
			this._initialized = true;
			if (this._filename != null)
				this.SetFilename(this._filename);
		}

		#endregion

		#region Private Methods

		private void SetFolder(string folder)
		{
			this.listBoxGraphics.BeginUpdate();
			this.listBoxGraphics.Items.Clear();
		    this._folder = folder;
			foreach (GameResource rsx in this._resources)
				this.listBoxGraphics.Items.Add(rsx.Name);
			this._resources.Insert(0, null);
			this.listBoxGraphics.Items.Insert(0, "<None>");
			this.listBoxGraphics.EndUpdate();
		}

		private void SetFilename(string filename)
		{
			var index = this.listBoxGraphics.FindStringExact(filename, 1);
			this.listBoxGraphics.SelectedIndex = Math.Max(0, index);
		}

		// TODO: Improve this to me more dyanamic
		private void RefreshPicture()
		{
			if (!this._initialized)
				return;
			if (this.OptionsEnabled)
			{
				this.pictureBox.BlendMode = this.comboBoxBlend.SelectedIndex;
				if (this.AdvancedOptionEnabled)
				{
					this.pictureBox.Zoom = (int)this.numericZoom.Value;
					this.pictureBox.ScrollX = (int)this.numericSX.Value;
					this.pictureBox.ScrollY = (int)this.numericSY.Value;
				}
			}
			switch (this._folder)
			{
				case @"Graphics\Animations":
					this.pictureBox.Image = new Bitmap(Cache.Animation(this._filename, this.trackBarHue.Value));
					break;
				case @"Graphics\Characters": 
					this.pictureBox.Image = new Bitmap(Cache.Character(this._filename, this.trackBarHue.Value));
					break;
				case @"Graphics\Battlers":
					this.pictureBox.Image = new Bitmap(Cache.Battler(this._filename, this.trackBarHue.Value));
					break;
				case @"Graphics\Icons":
					this.pictureBox.Image = new Bitmap(Cache.Icon(this._filename));
					break;
				case @"Graphics\Battlebacks":
					this.pictureBox.Image = new Bitmap(Cache.Battleback(this._filename));
					break;
				case @"Graphics\Tilesets":
					this.pictureBox.Image = new Bitmap(Cache.Tileset(this._filename));
					break;
				case @"Graphics\Autotiles":
					this.pictureBox.Image = new Bitmap(Cache.Autotile(this._filename));
					break;
				case @"Graphics\Fogs":
					this.pictureBox.Image = 
						new Bitmap(Cache.Fog(this._filename, this.trackBarHue.Value));
					break;
				case @"Graphics\Panoramas":
					this.pictureBox.Image = new Bitmap(Cache.Panorama(this._filename, this.trackBarHue.Value));
					break;
			}
		}

		private void ListBoxGraphicsSelectedIndexChanged(object sender, EventArgs e)
		{
			var index = this.listBoxGraphics.SelectedIndex;
			if (index > 0)
			{
				this._filename = this._resources[this.listBoxGraphics.SelectedIndex].Name;
				this.RefreshPicture();
			}
			else
			{
				this.pictureBox.Image = null;
				this._filename = "";
			}
		}

		private void ImageOptionChanged(object sender, EventArgs e)
		{
			if (this._initialized)
				this.RefreshPicture();
		}

		private void ButtonOkClick(object sender, EventArgs e)
		{
			DialogResult = DialogResult.OK;
			Close();
		}

		#endregion

		private void ListBoxGraphicsDrawItem(object sender, DrawItemEventArgs e)
		{
			var index = e.Index;
			var str = (index == 0) ? "<None>" : this._resources[e.Index].Name;
			using (e.Graphics)
			{
				e.DrawBackground();
				if (index > 0)
				{
				    e.Graphics.DrawImageUnscaled(
				        this._resources[index].Location == Core.Location.Local ? 
                        Resources.ResourceLocal : Resources.ResourceRTP,
				        e.Bounds);
				}
				e.Graphics.DrawString("     " + str, e.Font, Brushes.Black, e.Bounds);
				e.DrawFocusRectangle();
			}
		}

		private void CheckAlphaPreviewCheckedChanged(object sender, EventArgs e)
		{
			this.pictureBox.AlphaPreview = this.checkAlphaPreview.Checked;
			this.pictureBox.Invalidate();
		}

		private void NumericOpacityValueChanged(object sender, EventArgs e)
		{
			this.pictureBox.ImageOpacity = (int)this.numericOpacity.Value;
		}

		private void ButtonColorClick(object sender, EventArgs e)
		{
			using (var dialog = new ColorChooserForm())
			{
				dialog.AlphaEnabled = false;
                dialog.Color = Editor.Settings.ImageColorSettings.BackgroundColor.ToSystemColor();
			    if (dialog.ShowDialog() != DialogResult.OK) return;
			    Editor.Settings.ImageColorSettings.BackgroundColor = dialog.Color.ToXnaColor();
			    this.pictureBox.ImageBackColor = Editor.Settings.ImageColorSettings.BackgroundColor;
			}
		}
	}
}
