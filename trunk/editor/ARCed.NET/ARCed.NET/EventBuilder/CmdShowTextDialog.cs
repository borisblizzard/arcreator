﻿using System;
using System.Windows.Forms;

namespace ARCed.EventBuilder
{
	public partial class CmdShowTextDialog : Form
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
		public CmdShowTextDialog()
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