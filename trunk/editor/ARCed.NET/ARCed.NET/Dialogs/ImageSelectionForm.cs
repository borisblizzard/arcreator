﻿#region Using Directives

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
			set { trackBarHue.Value = value.Clamp(0, 359); }
		}

		public int ImageOpacity
		{
			get { return (int)numericOpacity.Value; }
			set 
			{ 
				numericOpacity.Value = value.Clamp(0, 255);
				pictureBox.ImageOpacity = value.Clamp(0, 255);
			}
		}

		public int Zoom
		{
			get { return (int)numericZoom.Value; }
			set { numericZoom.Value = value.Clamp(100, 800); }
		}

		public int ScrollX
		{
			get { return (int)numericSX.Value; }
			set { numericSX.Value = value.Clamp(-480, 480); }
		}

		public int ScrollY
		{
			get { return (int)numericSY.Value; }
			set { numericSY.Value = value.Clamp(-480, 480); }
		}

		public int BlendMode
		{
			get { return comboBoxBlend.SelectedIndex; }
			set { comboBoxBlend.SelectedIndex = value.Clamp(0, 2); }
		}

		/// <summary>
		/// Gets or sets the root folder searched for images
		/// </summary>
		public string ImageFolder 
		{
			get { return _folder; }
			set { SetFolder(value); }
		}

		/// <summary>
		/// Gets or sets the filename (without extension) of the image that is found in the current folder
		/// </summary>
		public string ImageName
		{
			get { return Path.GetFileNameWithoutExtension(_filename); }
			set { SetFilename(value); }
		}

		/// <summary>
		/// Gets or sets the ability to select individual tiles of the _srcTexture
		/// </summary>
		public bool SelectionEnabled 
		{
			get { return pictureBox.SelectionEnabled; }
			set { pictureBox.SelectionEnabled = value; }
		}

		/// <summary>
		/// Gets or sets the visibility of the trackbar for changing image hue.
		/// </summary>
		public bool HueEnabled 
		{
			get { return groupBoxHue.Enabled; }
			set { groupBoxHue.Enabled = value; }
		}

		/// <summary>
		/// Gets or sets the visibility of the panel for changing options.
		/// </summary>
		public bool OptionsEnabled
		{
			get { return groupBoxOptions.Enabled; }
			set { groupBoxOptions.Enabled = value; }
		}

		/// <summary>
		/// Gets or sets the enabled status of the scroll options.
		/// </summary>
		public bool AdvancedOptionEnabled
		{
			get { return pictureBox.AdvancedEnabled; }
			set { pictureBox.AdvancedEnabled = panelAdvanced.Enabled = value; }
		}

		#endregion

		#region Construction

		public void SetDefaultOptions(string folder)
		{
			var hue = new List<string> { "Animations", "Battlers", "Characters",
				"Fogs", "Panoramas", "Pictures" };
			var options = new List<string> { "Battlers", "Fogs" };
			OptionsEnabled = options.Contains(folder);
			HueEnabled = hue.Contains(folder);
			AdvancedOptionEnabled = (folder == "Fogs");
		}

		/// <summary>
		/// Constructor that sets the folder and selected _srcTexture
		/// </summary>
		/// <param name="folder">Root folder searched for images</param>
		/// <param name="filename">FullPath (without extension) of the _srcTexture that is found in the current folder</param>
		public ImageSelectionForm(string folder, string filename) : this()
		{
			// Find all valid filenames
			_folder = folder;
			_filename = filename;
		}

		/// <summary>
		/// Default constructor
		/// </summary>
		public ImageSelectionForm()
		{
			InitializeComponent();
			ResizeBegin += (s, e) => SuspendLayout();
			ResizeEnd += (s, e) => ResumeLayout();
		}

		private void ImageSelectionFormLoad(object sender, EventArgs e)
		{
			if (_folder != null)
			{
				SetDefaultOptions(_folder);
				if (!_folder.StartsWith("Graphics"))
					_folder = Path.Combine("Graphics", _folder);
				_resources = ResourceHelper.GetTypes(_folder);
				SetFolder(_folder);
			}
			else
				_resources = new List<GameResource>();
			_initialized = true;
			if (_filename != null)
				SetFilename(_filename);
		}

		#endregion

		#region Private Methods

		private void SetFolder(string folder)
		{
			listBoxGraphics.BeginUpdate();
			listBoxGraphics.Items.Clear();
		    _folder = folder;
			foreach (GameResource rsx in _resources)
				listBoxGraphics.Items.Add(rsx.Name);
			_resources.Insert(0, null);
			listBoxGraphics.Items.Insert(0, "<None>");
			listBoxGraphics.EndUpdate();
		}

		private void SetFilename(string filename)
		{
			var index = listBoxGraphics.FindStringExact(filename, 1);
			listBoxGraphics.SelectedIndex = Math.Max(0, index);
		}

		// TODO: Improve this to me more dyanamic
		private void RefreshPicture()
		{
			if (!_initialized)
				return;
			if (OptionsEnabled)
			{
				pictureBox.BlendMode = comboBoxBlend.SelectedIndex;
				if (AdvancedOptionEnabled)
				{
					pictureBox.Zoom = (int)numericZoom.Value;
					pictureBox.ScrollX = (int)numericSX.Value;
					pictureBox.ScrollY = (int)numericSY.Value;
				}
			}
			switch (_folder)
			{
				case @"Graphics\Animations":
					pictureBox.Image = new Bitmap(Cache.Animation(_filename, this.trackBarHue.Value));
					break;
				case @"Graphics\Characters": 
					pictureBox.Image = new Bitmap(Cache.Character(_filename, this.trackBarHue.Value));
					break;
				case @"Graphics\Battlers":
					pictureBox.Image = new Bitmap(Cache.Battler(_filename, this.trackBarHue.Value));
					break;
				case @"Graphics\Icons":
					pictureBox.Image = new Bitmap(Cache.Icon(_filename));
					break;
				case @"Graphics\Battlebacks":
					pictureBox.Image = new Bitmap(Cache.Battleback(_filename));
					break;
				case @"Graphics\Tilesets":
					pictureBox.Image = new Bitmap(Cache.Tileset(_filename));
					break;
				case @"Graphics\Autotiles":
					pictureBox.Image = new Bitmap(Cache.Autotile(_filename));
					break;
				case @"Graphics\Fogs":
					pictureBox.Image = 
						new Bitmap(Cache.Fog(_filename, this.trackBarHue.Value));
					break;
				case @"Graphics\Panoramas":
					pictureBox.Image = new Bitmap(Cache.Panorama(_filename, this.trackBarHue.Value));
					break;
			}
		}

		private void ListBoxGraphicsSelectedIndexChanged(object sender, EventArgs e)
		{
			var index = listBoxGraphics.SelectedIndex;
			if (index > 0)
			{
				_filename = _resources[listBoxGraphics.SelectedIndex].Name;
				RefreshPicture();
			}
			else
			{
				pictureBox.Image = null;
				_filename = "";
			}
		}

		private void ImageOptionChanged(object sender, EventArgs e)
		{
			if (_initialized)
				RefreshPicture();
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
			var str = (index == 0) ? "<None>" : _resources[e.Index].Name;
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
			pictureBox.AlphaPreview = checkAlphaPreview.Checked;
			pictureBox.Invalidate();
		}

		private void NumericOpacityValueChanged(object sender, EventArgs e)
		{
			pictureBox.ImageOpacity = (int)numericOpacity.Value;
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
