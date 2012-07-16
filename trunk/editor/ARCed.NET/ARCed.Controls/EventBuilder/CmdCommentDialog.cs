#region Using Directives

using System;
using System.Windows.Forms;

#endregion

namespace ARCed.EventBuilder
{
	public partial class CmdCommentDialog : Form
	{
		/// <summary>
		/// Gets or sets the lines of text in the form's text control.
		/// </summary>
		public string[] Lines 
		{
			get { return textBoxText.Lines; }
			set { textBoxText.Lines = value; }
		}

		/// <summary>
		/// Default constructor
		/// </summary>
		public CmdCommentDialog()
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
