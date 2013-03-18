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
			get { return this.GetLearning(); }
			set { this.SetLearning(value); }
		}

        #endregion

        #region Constructor

        /// <summary>
		/// Default constructor
		/// </summary>
		public EditSkillDialog()
		{
			this.InitializeComponent();
			ControlHelper.Populate(this.comboBoxSkill, Project.Data.Skills, false);
			this.comboBoxSkill.SelectedIndex = 0;
		}

        #endregion

        #region Private Methods

        private void SetLearning(Class.Learning learning)
		{
			this.comboBoxSkill.SelectedIndex = learning.skill_id - 1;
			this.numericLevel.Value = learning.level;
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
