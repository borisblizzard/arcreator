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
			this.InitializeComponent();
		}

		private void buttonOK_Click(object sender, EventArgs e)
		{
			DialogResult = DialogResult.OK;
			Close();
		}
	}
}
