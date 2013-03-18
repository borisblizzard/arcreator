#region Using Directives

using System;
using System.Windows.Forms;
using ARCed.Helpers;

#endregion

namespace ARCed.EventBuilder
{
	public partial class CmdButtonInputDialog : Form
	{
		/// <summary>
		/// Gets or sets the selected variable ID.
		/// </summary>
		public int VariableId
		{
			get { return this.comboBoxVariables.SelectedIndex + 1; }
			set {
			    this.comboBoxVariables.SelectedIndex = 
                    value < this.comboBoxVariables.Items.Count ? value : 0;
			}
		}

		/// <summary>
		/// Default constructor
		/// </summary>
		public CmdButtonInputDialog()
		{
			this.InitializeComponent();
			ControlHelper.Populate(this.comboBoxVariables, Project.Variables, false);
			this.comboBoxVariables.SelectedIndex = 0;
		}

		private void buttonOK_Click(object sender, EventArgs e)
		{
			DialogResult = DialogResult.OK;
			Close();
		}
	}
}
