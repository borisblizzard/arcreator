using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using ARCed.Dialogs;
using ARCed.Helpers;
using ARCed.Settings;

namespace ARCed.Database.Tilesets
{
	public partial class ImageColorsDialog : Form
	{
		private ImageColorSettings _original, _settings;

		public ImageColorSettings Settings { get { return _settings; } }
		public ImageColorSettings OriginalSettings { get { return _original; } }
		public ARCed.Controls.GraphicsDeviceControl XnaPanel { get; set; }

		public ImageColorsDialog(ImageColorSettings settings)
		{
			InitializeComponent();
			_original = Util.CloneObject(settings);
			_settings = settings;
			RefreshColors();
		}

		private Color GetColor(Color color)
		{
			using (ColorChooserForm dialog = new ColorChooserForm())
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
