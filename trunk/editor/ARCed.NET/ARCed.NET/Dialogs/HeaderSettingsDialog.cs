using System;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Helpers;

namespace ARCed.Dialogs
{
	public partial class HeaderSettingsDialog : Form
	{
		#region Private Fields

		private ARCed.Settings.HeaderSettings _settings;

		#endregion

		#region Constructors

		/// <summary>
		/// Default constructor
		/// </summary>
		public HeaderSettingsDialog()
		{
			InitializeComponent();
			_settings = Util.CloneObject(Project.Settings.HeaderImage);
			panelStartGradient.BackColor = _settings.GradientLeft;
			panelEndGradient.BackColor = _settings.GradientRight;
			panelTextColor.BackColor = _settings.TextColor;
			fontSelector.UserFont = _settings.Font.FontValue;
		}

		#endregion

		#region Private Methods

		private void panelStartGradient_DoubleClick(object sender, EventArgs e)
		{
			_settings.GradientLeft = GetColor(_settings.GradientLeft);
			panelStartGradient.BackColor = _settings.GradientLeft;
		}

		private void panelEndGradient_DoubleClick(object sender, EventArgs e)
		{
			_settings.GradientRight = GetColor(_settings.GradientRight);
			panelEndGradient.BackColor = _settings.GradientRight;
		}

		private void panelTextColor_DoubleClick(object sender, EventArgs e)
		{
			_settings.TextColor = GetColor(_settings.TextColor);
			panelTextColor.BackColor = _settings.TextColor;
		}

		private Color GetColor(Color color)
		{
			using (ColorChooserForm dialog = new ColorChooserForm())
			{
				dialog.Color = color;
				dialog.AlphaEnabled = false;
				if (dialog.ShowDialog() == DialogResult.OK)
					color = dialog.Color;
			}
			return color;
		}

		private void buttonOK_Click(object sender, EventArgs e)
		{
			Project.Settings.HeaderImage = _settings;
			foreach (ARCed.Database.DatabaseWindow window in Windows.DatabaseForms)
				window.RefreshHeader();
			Windows.ScriptMenu.RefreshHeader();
			this.DialogResult = DialogResult.OK;
			this.Close();
		}

		private void fontSelector_OnUserFontChanged(object sender, EventArgs e)
		{
			_settings.Font = fontSelector.UserFont;
		}

		#endregion
	}
}
