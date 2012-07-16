#region Using Directives

using System;
using System.Windows.Forms;
using ARCed.Helpers;
using RPG;

#endregion

namespace ARCed.Database.Classes
{
    /// <summary>
    /// Dialog for getting a user-defined <see cref="RPG.Skill"/> configuration.
    /// </summary>
	public partial class EditSkillDialog : Form
    {
        #region Public Properties

        /// <summary>
		/// Gets or sets the current RPG.Learning defined on the form
		/// </summary>
		public Class.Learning Learning 
		{
			get { return GetLearning(); }
			set { SetLearning(value); }
		}

        #endregion

        #region Constructor

        /// <summary>
		/// Default constructor
		/// </summary>
		public EditSkillDialog()
		{
			InitializeComponent();
			ControlHelper.Populate(comboBoxSkill, Project.Data.Skills, false);
			comboBoxSkill.SelectedIndex = 0;
		}

        #endregion

        #region Private Methods

        private void SetLearning(Class.Learning learning)
		{
			comboBoxSkill.SelectedIndex = learning.skill_id - 1;
			numericLevel.Value = learning.level;
		}

		private Class.Learning GetLearning()
		{
			var learning = new Class.Learning
			{
			    level = (int)this.numericLevel.Value,
			    skill_id = this.comboBoxSkill.SelectedIndex + 1
			};
		    return learning;
		}

		private void ButtonOkClick(object sender, EventArgs e)
		{
			DialogResult = DialogResult.OK;
			Close();
        }

        #endregion
    }
}
