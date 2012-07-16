#region Using Directives

using System;
using System.Windows.Forms;
using ARCed.Helpers;
using RPG;

#endregion

namespace ARCed.Database.Classes
{
	public partial class EditSkillDialog : Form
	{
		/// <summary>
		/// Gets or sets the current RPG.Learning defined on the form
		/// </summary>
		public Class.Learning Learning 
		{
			get { return GetLearning(); }
			set { SetLearning(value); }
		}

		/// <summary>
		/// Default constructor
		/// </summary>
		public EditSkillDialog()
		{
			InitializeComponent();
			ControlHelper.Populate(comboBoxSkill, Project.Data.Skills, false);
			comboBoxSkill.SelectedIndex = 0;
		}

		private void SetLearning(Class.Learning learning)
		{
			comboBoxSkill.SelectedIndex = learning.skill_id - 1;
			numericLevel.Value = learning.level;
		}

		private Class.Learning GetLearning()
		{
			var learning = new Class.Learning();
			learning.level = (int)numericLevel.Value;
			learning.skill_id = comboBoxSkill.SelectedIndex + 1;
			return learning;
		}

		private void buttonOK_Click(object sender, EventArgs e)
		{
			this.DialogResult = DialogResult.OK;
			this.Close();
		}
	}
}
