using System;
using System.Windows.Forms;

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
			get { return (int)numericUpDownDigits.Value; }
			set { numericUpDownDigits.Value = value.Clamp(0, 12); }
		}

		/// <summary>
		/// Gets or sets the currently selected variable ID.
		/// </summary>
		public int VariableId
		{
			get { return comboBoxVariable.SelectedIndex + 1; }
			set 
			{
				if (comboBoxVariable.Items.Count < (value - 1))
					comboBoxVariable.SelectedIndex = value - 1;
				else
					comboBoxVariable.SelectedIndex = 0;
			}
		}

		/// <summary>
		/// Default constructor.
		/// </summary>
		public CmdInputNumberDialog()
		{
			InitializeComponent();
			ARCed.Helpers.DatabaseHelper.Populate(comboBoxVariable, Project.Variables, false);
		}

		private void OK_Click(object sender, EventArgs e)
		{
			this.DialogResult = DialogResult.OK;
			this.Close();
		}
	}
}
