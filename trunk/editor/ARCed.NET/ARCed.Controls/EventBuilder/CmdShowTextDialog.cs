#region Using Directives

using System;
using System.Windows.Forms;

#endregion

namespace ARCed.EventBuilder
{
	public partial class CmdShowTextDialog : Form
	{
		/// <summary>
		/// Gets or sets the lines of text in the form's text control.
		/// </summary>
		public string[] Lines 
		{
			get { return this.textBoxText.Lines; }
			set { this.textBoxText.Lines = value; }
		}

		/// <summary>
		/// Default constructor
		/// </summary>
		public CmdShowTextDialog()
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
