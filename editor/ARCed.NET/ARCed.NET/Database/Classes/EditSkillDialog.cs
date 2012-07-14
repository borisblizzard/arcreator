using System;
using System.Windows.Forms;
using ARCed.Helpers;

namespace ARCed.Database.Classes
{
	public partial class EditSkillDialog : Form
	{
		/// <summary>
		/// Gets or sets the current RPG.Learning defined on the form
		/// </summary>
		public RPG.Class.Learning Learning 
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

		private void SetLearning(RPG.Class.Learning learning)
		{
			comboBoxSkill.SelectedIndex = learning.skill_id - 1;
			numericLevel.Value = learning.level;
		}

		private RPG.Class.Learning GetLearning()
		{
			RPG.Class.Learning learning = new RPG.Class.Learning();
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
