#region Using Directives

using System;
using System.Windows.Forms;

#endregion

namespace ARCed.EventBuilder
{
	public partial class CmdChangeTextOptionsDialog : Form
	{
		/// <summary>
		/// Gets or sets the position setting of the window.
		/// </summary>
		public int Position
		{
			get 
			{
				int count = 0;
				foreach (RadioButton radio in this.groupBoxPosition.Controls)
				{
					if (radio.Checked) return count;
					count++;
				}
				return count;
			}
			set
			{
				(this.groupBoxPosition.Controls[value] as RadioButton).Checked = true;
			}
		}

		/// <summary>
		/// Gets or sets the visiblity state of the window.
		/// </summary>
		public int WindowVisibility
		{
			get { return this.radioButtonShow.Checked ? 0 : 1; }
			set 
			{
				if (value == 0) this.radioButtonShow.Checked = true;
				else this.radioButtonHide.Checked = true;
			}
		}
		
		/// <summary>
		/// Default constructor
		/// </summary>
		public CmdChangeTextOptionsDialog()
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
