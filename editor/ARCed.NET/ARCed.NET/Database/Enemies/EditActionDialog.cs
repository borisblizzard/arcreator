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
			get { return this.GetAction(); }
			set { this.SetAction(value); }
		}

        #endregion

        #region Constructor

        /// <summary>
        /// Default constructor
        /// </summary>
        public EditActionDialog()
		{
			this.InitializeComponent();
			this.RefreshSkills();
			this.trackBarRating.DataBindings.Add("Value", this.numericUpDownRating, "Value", false,
				DataSourceUpdateMode.OnPropertyChanged);
			this.RefreshSwitches();
		}

        #endregion

        #region Private Methods

        private void SetAction(Enemy.Action action)
		{
			var turnC = !(action.condition_turn_a == 0 && action.condition_turn_b == 1);
			if (turnC)
			{
				this.checkBoxTurn.Checked = true;
				this.numericUpDownTurn.Value = action.condition_turn_a;
				this.numericUpDownTurnX.Value = action.condition_turn_b;
			}
			if (action.condition_hp != 100)
			{
				this.checkBoxHP.Checked = true;
				this.numericUpDownHP.Value = action.condition_hp;
			}
			if (action.condition_level != 1)
			{
				this.checkBoxLevel.Checked = true;
				this.numericUpDownLevel.Value = action.condition_level;
			}
			if (action.condition_switch_id != 0)
			{
				this.checkBoxSwitch.Checked = true;
				this.comboBoxSwitch.SelectedIndex = action.condition_switch_id - 1;
			}
			this.comboBoxBasic.SelectedIndex = action.basic;
			this.comboBoxSkill.SelectedIndex = action.skill_id - 1;
			if (action.kind == 0)
				this.radioButtonBasic.Checked = true;
			else
				this.radioButtonSkill.Checked = true;
			this.numericUpDownRating.Value = action.rating;
		}

		private Enemy.Action GetAction()
		{
			var action = new Enemy.Action();
			if (this.checkBoxTurn.Checked)
			{
				action.condition_turn_a = (int)this.numericUpDownTurn.Value;
				action.condition_turn_b = (int)this.numericUpDownTurnX.Value;
			}
			else
			{
				action.condition_turn_a = 0;
				action.condition_turn_b = 1;
			}
			action.condition_hp = this.checkBoxHP.Checked ? (int)this.numericUpDownHP.Value : 100;
			action.condition_level = this.checkBoxLevel.Checked ? (int)this.numericUpDownLevel.Value : 1;
			action.condition_switch_id = this.checkBoxSwitch.Checked ?
				this.comboBoxSwitch.SelectedIndex + 1 : 0;
			action.kind = this.radioButtonBasic.Checked ? 0 : 1;
			action.basic = this.comboBoxBasic.SelectedIndex;
			action.skill_id = this.comboBoxSkill.SelectedIndex + 1;
			action.rating = this.trackBarRating.Value;
			return action;
		}

		private void RefreshSkills()
		{
			ControlHelper.Populate(this.comboBoxSkill, Project.Data.Skills, false);
		}

		private void RefreshSwitches()
		{
			ControlHelper.Populate(this.comboBoxSwitch, Project.Switches, false);
		}

		private void CheckBoxTurnCheckedChanged(object sender, EventArgs e)
		{
			var enable = this.checkBoxTurn.Checked;
			this.numericUpDownTurn.Enabled = enable;
			this.numericUpDownTurnX.Enabled = enable;
		}

		private void CheckBoxHpCheckedChanged(object sender, EventArgs e)
		{
			this.numericUpDownHP.Enabled = this.checkBoxHP.Checked;
		}

		private void CheckBoxLevelCheckedChanged(object sender, EventArgs e)
		{
			this.numericUpDownLevel.Enabled = this.checkBoxLevel.Checked;
		}

		private void CheckBoxSwitchCheckedChanged(object sender, EventArgs e)
		{
			this.comboBoxSwitch.Enabled = this.checkBoxSwitch.Checked;
			this.comboBoxSwitch.SelectedIndex = Math.Max(0, this.comboBoxSwitch.SelectedIndex);
		}

		private void RadioButtonCheckedChanged(object sender, EventArgs e)
		{
			if (this.radioButtonBasic.Checked)
			{
				this.comboBoxBasic.Enabled = true;
				this.comboBoxSkill.Enabled = false;
				this.comboBoxBasic.SelectedIndex = Math.Max(0, this.comboBoxBasic.SelectedIndex);
			}
			else
			{
				this.comboBoxBasic.Enabled = false;
				this.comboBoxSkill.Enabled = true;
				this.comboBoxSkill.SelectedIndex = Math.Max(0, this.comboBoxSkill.SelectedIndex);
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
