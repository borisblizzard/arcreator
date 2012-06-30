using System;
using System.Collections.Generic;
using System.Windows.Forms;
using ARCed.Helpers;

namespace ARCed.Database.Enemies
{
	public partial class EditActionDialog : Form
	{

		public RPG.Enemy.Action EnemyAction 
		{
			get { return GetAction(); }
			set { SetAction(value); }
		}

		public EditActionDialog()
		{
			InitializeComponent();
			RefreshSkills();
			trackBarRating.DataBindings.Add("Value", numericUpDownRating, "Value", false,
				DataSourceUpdateMode.OnPropertyChanged | DataSourceUpdateMode.OnValidation);
			RefreshSwitches();
		}

		private void SetAction(RPG.Enemy.Action action)
		{
			bool turnC = !(action.condition_turn_a == 0 && action.condition_turn_b == 1);
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

		private RPG.Enemy.Action GetAction()
		{
			var action = new RPG.Enemy.Action();
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

		public void RefreshSkills()
		{
			DatabaseHelper.Populate(comboBoxSkill, Project.Data.Skills, false);
		}

		public void RefreshSwitches()
		{
			DatabaseHelper.Populate(comboBoxSwitch, Project.Switches, false);
		}

		private void checkBoxTurn_CheckedChanged(object sender, EventArgs e)
		{
			bool enable = checkBoxTurn.Checked;
			numericUpDownTurn.Enabled = enable;
			numericUpDownTurnX.Enabled = enable;
		}

		private void checkBoxHP_CheckedChanged(object sender, EventArgs e)
		{
			numericUpDownHP.Enabled = checkBoxHP.Checked;
		}

		private void checkBoxLevel_CheckedChanged(object sender, EventArgs e)
		{
			numericUpDownLevel.Enabled = checkBoxLevel.Checked;
		}

		private void checkBoxSwitch_CheckedChanged(object sender, EventArgs e)
		{
			comboBoxSwitch.Enabled = checkBoxSwitch.Checked;
			comboBoxSwitch.SelectedIndex = Math.Max(0, comboBoxSwitch.SelectedIndex);
		}

		private void radioButton_CheckedChanged(object sender, EventArgs e)
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

		private void buttonOK_Click(object sender, EventArgs e)
		{
			this.DialogResult = DialogResult.OK;
			this.Close();
		}
	}
}
