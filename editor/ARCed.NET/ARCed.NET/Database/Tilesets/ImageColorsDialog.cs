#region Using Directives

using System;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Controls;
using ARCed.Dialogs;
using ARCed.Helpers;
using ARCed.Settings;

#endregion

namespace ARCed.Database.Tilesets
{
	public partial class ImageColorsDialog : Form
	{
		private readonly ImageColorSettings _original, _settings;

		public ImageColorSettings Settings { get { return this._settings; } }
		public ImageColorSettings OriginalSettings { get { return this._original; } }
		public GraphicsDeviceControl XnaPanel { get; set; }

		public ImageColorsDialog(ImageColorSettings settings)
		{
			this.InitializeComponent();
			this._original = Util.CloneObject(settings);
			this._settings = settings;
			this.RefreshColors();
		}

		private static Color GetColor(Color color)
		{
			using (var dialog = new ColorChooserForm())
			{
				dialog.Color = color;
				if (dialog.ShowDialog() == DialogResult.OK)
					color = dialog.Color;
			}
			return color;
		}

		private void RefreshColors()
		{
			this.panelBackground.BackColor = this._settings.BackgroundColor.ToSystemColor();
			this.panelSelector.BackColor = this._settings.SelectorColor.ToSystemColor();
			this.panelGrid.BackColor = this._settings.GridColor.ToSystemColor();
			if (this.XnaPanel != null)
				this.XnaPanel.Invalidate();
		}

		private void panelBackgroundColor_DoubleClick(object sender, EventArgs e)
		{
			this._settings.BackgroundColor = GetColor(this.panelBackground.BackColor).ToXnaColor();
			this.RefreshColors();
		}

		private void panelSelectorColor_DoubleClick(object sender, EventArgs e)
		{
			this._settings.SelectorColor = GetColor(this.panelSelector.BackColor).ToXnaColor();
			this.RefreshColors();
		}

		private void panelGridColor_DoubleClick(object sender, EventArgs e)
		{
			this._settings.GridColor = GetColor(this.panelGrid.BackColor).ToXnaColor();
			this.RefreshColors();
		}

		private void buttonOK_Click(object sender, EventArgs e)
		{
			DialogResult = DialogResult.OK;
			Close();
		}
	}
}
