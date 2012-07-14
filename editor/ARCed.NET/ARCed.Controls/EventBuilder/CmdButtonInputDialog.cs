using System;
using System.Windows.Forms;

namespace ARCed.EventBuilder
{
	public partial class CmdButtonInputDialog : Form
	{
		/// <summary>
		/// Gets or sets the selected variable ID.
		/// </summary>
		public int VariableId
		{
			get { return comboBoxVariables.SelectedIndex + 1; }
			set
			{
				if (value < comboBoxVariables.Items.Count)
					comboBoxVariables.SelectedIndex = value;
				else
					comboBoxVariables.SelectedIndex = 0;
			}
		}

		/// <summary>
		/// Default constructor
		/// </summary>
		public CmdButtonInputDialog()
		{
			InitializeComponent();
			ARCed.Helpers.ControlHelper.Populate(comboBoxVariables, Project.Variables, false);
			comboBoxVariables.SelectedIndex = 0;
		}

		private void buttonOK_Click(object sender, EventArgs e)
		{
			this.DialogResult = DialogResult.OK;
			this.Close();
		}
	}
}
