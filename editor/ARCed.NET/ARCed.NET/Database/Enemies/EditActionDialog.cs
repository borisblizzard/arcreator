#region Using Directives

using System;
using System.Windows.Forms;
using ARCed.Helpers;
using RPG;

#endregion

namespace ARCed.Database.Enemies
{
    /// <summary>
    /// Dialog for getting user-defined <see cref="RPG.Enemy.Action"/>.
    /// </summary>
	public partial class EditActionDialog : Form
    {
        #region Public Properties

        /// <summary>
        /// Gets or sets the <see cref="RPG.Enemy.Action"/> defined on the form.
        /// </summary>
        public Enemy.Action EnemyAction 
		{
			get { return GetAction(); }
			set { SetAction(value); }
		}

        #endregion

        #region Constructor

        /// <summary>
        /// Default constructor
        /// </summary>
        public EditActionDialog()
		{
			InitializeComponent();
			RefreshSkills();
			trackBarRating.DataBindings.Add("Value", numericUpDownRating, "Value", false,
				DataSourceUpdateMode.OnPropertyChanged);
			RefreshSwitches();
		}

        #endregion

        #region Private Methods

        private void SetAction(Enemy.Action action)
		{
			var turnC = !(action.condition_turn_a == 0 && action.condition_turn_b == 1);
			if (turnC)
			{
				checkBoxTurn.Checked = true;
				numericUpDownTurn.Value = action.condition_turn_a;
				numericUpDownTurnX.Value = action.condition_turn_b;
			}
			if (action.condition_hp != 100)
			{
				checkBoxHP.Checked = true;
				numericUpDownHP.Value = action.condition_hp;
			}
			if (action.condition_level != 1)
			{
				checkBoxLevel.Checked = true;
				numericUpDownLevel.Value = action.condition_level;
			}
			if (action.condition_switch_id != 0)
			{
				checkBoxSwitch.Checked = true;
				comboBoxSwitch.SelectedIndex = action.condition_switch_id - 1;
			}
			comboBoxBasic.SelectedIndex = action.basic;
			comboBoxSkill.SelectedIndex = action.skill_id - 1;
			if (action.kind == 0)
				radioButtonBasic.Checked = true;
			else
				radioButtonSkill.Checked = true;
			numericUpDownRating.Value = action.rating;
		}

		private Enemy.Action GetAction()
		{
			var action = new Enemy.Action();
			if (checkBoxTurn.Checked)
			{
				action.condition_turn_a = (int)numericUpDownTurn.Value;
				action.condition_turn_b = (int)numericUpDownTurnX.Value;
			}
			else
			{
				action.condition_turn_a = 0;
				action.condition_turn_b = 1;
			}
			action.condition_hp = checkBoxHP.Checked ? (int)numericUpDownHP.Value : 100;
			action.condition_level = checkBoxLevel.Checked ? (int)numericUpDownLevel.Value : 1;
			action.condition_switch_id = checkBoxSwitch.Checked ?
				comboBoxSwitch.SelectedIndex + 1 : 0;
			action.kind = radioButtonBasic.Checked ? 0 : 1;
			action.basic = comboBoxBasic.SelectedIndex;
			action.skill_id = comboBoxSkill.SelectedIndex + 1;
			action.rating = trackBarRating.Value;
			return action;
		}

		private void RefreshSkills()
		{
			ControlHelper.Populate(comboBoxSkill, Project.Data.Skills, false);
		}

		private void RefreshSwitches()
		{
			ControlHelper.Populate(comboBoxSwitch, Project.Switches, false);
		}

		private void CheckBoxTurnCheckedChanged(object sender, EventArgs e)
		{
			var enable = checkBoxTurn.Checked;
			numericUpDownTurn.Enabled = enable;
			numericUpDownTurnX.Enabled = enable;
		}

		private void CheckBoxHpCheckedChanged(object sender, EventArgs e)
		{
			numericUpDownHP.Enabled = checkBoxHP.Checked;
		}

		private void CheckBoxLevelCheckedChanged(object sender, EventArgs e)
		{
			numericUpDownLevel.Enabled = checkBoxLevel.Checked;
		}

		private void CheckBoxSwitchCheckedChanged(object sender, EventArgs e)
		{
			comboBoxSwitch.Enabled = checkBoxSwitch.Checked;
			comboBoxSwitch.SelectedIndex = Math.Max(0, comboBoxSwitch.SelectedIndex);
		}

		private void RadioButtonCheckedChanged(object sender, EventArgs e)
		{
			if (radioButtonBasic.Checked)
			{
				comboBoxBasic.Enabled = true;
				comboBoxSkill.Enabled = false;
				comboBoxBasic.SelectedIndex = Math.Max(0, comboBoxBasic.SelectedIndex);
			}
			else
			{
				comboBoxBasic.Enabled = false;
				comboBoxSkill.Enabled = true;
				comboBoxSkill.SelectedIndex = Math.Max(0, comboBoxSkill.SelectedIndex);
			}
		}

		private void ButtonOkClick(object sender, EventArgs e)
		{
			DialogResult = DialogResult.OK;
			Close();
        }

        #endregion
    }
}
