using System;
using System.Windows.Forms;

namespace ARCed.EventBuilder
{
	public partial class CmdWaitDialog : Form
	{
		/// <summary>
		/// Gets or sets the number of frames defined.
		/// </summary>
		public int Frames
		{
			get { return (int)numericUpDownFrames.Value; }
			set { numericUpDownFrames.Value = value.Clamp(1, 1000); }
		}

		/// <summary>
		/// Default constructor
		/// </summary>
		public CmdWaitDialog()
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
