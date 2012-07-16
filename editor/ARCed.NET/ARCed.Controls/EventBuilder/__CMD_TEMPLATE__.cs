#region Using Directives

using System;
using System.Windows.Forms;

#endregion

namespace ARCed.TEMP
{
	public partial class CmdChangeTextOptions : Form
	{
		/// <summary>
		/// Default constructor
		/// </summary>
		public CmdChangeTextOptions()
		{
			InitializeComponent();
		}

		private void buttonOK_Click(object sender, EventArgs e)
		{
			this.DialogResult = DialogResult.OK;
			this.Close();
		}
	}
}
