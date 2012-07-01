using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

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
