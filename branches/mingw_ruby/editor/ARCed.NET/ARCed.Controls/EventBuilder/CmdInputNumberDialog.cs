#region Using Directives

using System;
using System.Windows.Forms;
using ARCed.Helpers;

#endregion

namespace ARCed.EventBuilder
{
	/// <summary>
	/// Dialog for creating a user-defined Input Number event.
	/// </summary>
	public partial class CmdInputNumberDialog : Form
	{
		/// <summary>
		/// Gets or sets the number of possible digits.
		/// </summary>
		public int Digits 
		{
			get { return (int)this.numericUpDownDigits.Value; }
			set { this.numericUpDownDigits.Value = value.Clamp(0, 12); }
		}

		/// <summary>
		/// Gets or sets the currently selected variable ID.
		/// </summary>
		public int VariableId
		{
			get { return this.comboBoxVariable.SelectedIndex + 1; }
			set 
			{
				if (this.comboBoxVariable.Items.Count < (value - 1))
					this.comboBoxVariable.SelectedIndex = value - 1;
				else
					this.comboBoxVariable.SelectedIndex = 0;
			}
		}

		/// <summary>
		/// Default constructor.
		/// </summary>
		public CmdInputNumberDialog()
		{
			this.InitializeComponent();
			ControlHelper.Populate(this.comboBoxVariable, Project.Variables, false);
		}

		private void OK_Click(object sender, EventArgs e)
		{
			DialogResult = DialogResult.OK;
			Close();
		}
	}
}
