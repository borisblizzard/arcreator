#region Using Directives

using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;

#endregion

namespace ARCed.Controls
{
	/// <summary>
	/// Control for advanced searching script files for strings.
	/// </summary>
	[Description("Control for advanced searching script files for strings.")]
	[ToolboxBitmap(typeof(Panel))]
	public partial class SearchControl : UserControl
	{
		#region Contsructors

		/// <summary>
		/// Default constructor
		/// </summary>
		public SearchControl()
		{
			this.InitializeComponent();
			Dock = DockStyle.Fill;
			this.toolStripComboBox_Scope.SelectedIndex = 0;
		}

		#endregion

		#region Private Methods

		private void toolStripMenuItem_OptionsItem_Click(object sender, EventArgs e)
		{
			this.toolStripDropDownButton_Options.ShowDropDown();
			((ToolStripMenuItem)sender).Select();
		}

		private void toolStripTextBox_SearchString_KeyDown(object sender, KeyEventArgs e)
		{
			if (e.KeyCode == Keys.Enter)
			{
				this.buttonSearch.PerformClick();
				e.Handled = true;
				e.SuppressKeyPress = true;
			}
		}

		#endregion
	}
}
