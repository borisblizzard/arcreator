﻿#region Using Directives

using System;
using System.Windows.Forms;

#endregion

namespace ARCed.EventBuilder
{
	public partial class CmdWaitDialog : Form
	{
		/// <summary>
		/// Gets or sets the number of frames defined.
		/// </summary>
		public int Frames
		{
			get { return (int)this.numericUpDownFrames.Value; }
			set { this.numericUpDownFrames.Value = value.Clamp(1, 1000); }
		}

		/// <summary>
		/// Default constructor
		/// </summary>
		public CmdWaitDialog()
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
