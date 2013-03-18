#region Using Directives

using System;
using System.Windows.Forms;

#endregion

namespace ARCed.EventBuilder
{
	public partial class CmdConditionDialog : Form
	{
		/// <summary>
		/// Default constructor
		/// </summary>
		public CmdConditionDialog()
		{
			this.InitializeComponent();
		}

		private void buttonOK_Click(object sender, EventArgs e)
		{
			DialogResult = DialogResult.OK;
			Close();
		}
	}
}
