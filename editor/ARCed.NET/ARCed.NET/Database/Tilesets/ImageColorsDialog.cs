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

		public ImageColorSettings Settings { get { return _settings; } }
		public ImageColorSettings OriginalSettings { get { return _original; } }
		public GraphicsDeviceControl XnaPanel { get; set; }

		public ImageColorsDialog(ImageColorSettings settings)
		{
			InitializeComponent();
			_original = Util.CloneObject(settings);
			_settings = settings;
			RefreshColors();
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
			panelBackground.BackColor = _settings.BackgroundColor.ToSystemColor();
			panelSelector.BackColor = _settings.SelectorColor.ToSystemColor();
			panelGrid.BackColor = _settings.GridColor.ToSystemColor();
			if (XnaPanel != null)
				XnaPanel.Invalidate();
		}

		private void panelBackgroundColor_DoubleClick(object sender, EventArgs e)
		{
			_settings.BackgroundColor = GetColor(panelBackground.BackColor).ToXnaColor();
			RefreshColors();
		}

		private void panelSelectorColor_DoubleClick(object sender, EventArgs e)
		{
			_settings.SelectorColor = GetColor(panelSelector.BackColor).ToXnaColor();
			RefreshColors();
		}

		private void panelGridColor_DoubleClick(object sender, EventArgs e)
		{
			_settings.GridColor = GetColor(panelGrid.BackColor).ToXnaColor();
			RefreshColors();
		}

		private void buttonOK_Click(object sender, EventArgs e)
		{
			this.DialogResult = DialogResult.OK;
			this.Close();
		}
	}
}
