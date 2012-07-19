#region Using Directives

using System;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Database;
using ARCed.Helpers;
using ARCed.Settings;

#endregion

namespace ARCed.Dialogs
{
	public partial class HeaderSettingsDialog : Form
	{
		#region Private Fields

		private readonly HeaderSettings _settings;

		#endregion

		#region Constructors

		/// <summary>
		/// Default constructor
		/// </summary>
		public HeaderSettingsDialog()
		{
			this.InitializeComponent();
			this._settings = Util.CloneObject(Project.Settings.HeaderImage);
			this.panelStartGradient.BackColor = this._settings.GradientLeft;
			this.panelEndGradient.BackColor = this._settings.GradientRight;
			this.panelTextColor.BackColor = this._settings.TextColor;
			this.fontSelector.UserFont = this._settings.Font.FontValue;
		}

		#endregion

		#region Private Methods

		private void panelStartGradient_DoubleClick(object sender, EventArgs e)
		{
			this._settings.GradientLeft = GetColor(this._settings.GradientLeft);
			this.panelStartGradient.BackColor = this._settings.GradientLeft;
		}

		private void panelEndGradient_DoubleClick(object sender, EventArgs e)
		{
			this._settings.GradientRight = GetColor(this._settings.GradientRight);
			this.panelEndGradient.BackColor = this._settings.GradientRight;
		}

		private void panelTextColor_DoubleClick(object sender, EventArgs e)
		{
			this._settings.TextColor = GetColor(this._settings.TextColor);
			this.panelTextColor.BackColor = this._settings.TextColor;
		}

		private static Color GetColor(Color color)
		{
			using (var dialog = new ColorChooserForm())
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
			Project.Settings.HeaderImage = this._settings;
			foreach (DatabaseWindow window in Windows.DatabaseForms)
				window.RefreshHeader();
			Windows.ScriptMenu.RefreshHeader();
			DialogResult = DialogResult.OK;
			Close();
		}

		private void fontSelector_OnUserFontChanged(object sender, EventArgs e)
		{
			this._settings.Font = this.fontSelector.UserFont;
		}

		#endregion
	}
}
