using System;
using System.Windows.Forms;
using System.Collections.Generic;
using System.Linq;
using ARCed.Controls;
using RPG;

namespace ARCed.Database.States
{
	public sealed partial class StateMainForm : DatabaseWindow
	{

		#region Private Fields

		private RPG.State _state;

		#endregion

		#region Protected Properties

		/// <summary>
		/// Gets the object list control of this database panel.
		/// </summary>
		protected override DatabaseObjectListBox DataObjectList { get { return this.dataObjectList; } }

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets the data associated with this panel.
		/// </summary>
		public override List<dynamic> Data { get { return Project.Data.States; } }

		#endregion

		#region Constructor

		public StateMainForm()
		{
			InitializeComponent();
			RefreshObjectList();
			InitializeElements();
			InitializeStates();
			InitializeAnimations();
			dataObjectList.SelectedIndex = 0;
		}

		#endregion

		#region Public Methods

		/// <summary>
		/// Refreshes objects by type flag
		/// </summary>
		/// <param name="type">Flag for type of object to refresh</param>
		public override void NotifyRefresh(RefreshType type)
		{
			if (type.HasFlag(RefreshType.Elements))
			{

			}
			if (type.HasFlag(RefreshType.Animations))
			{

			}
			if (type.HasFlag(RefreshType.Parameters))
			{

			}
		}

		/// <summary>
		/// Refreshes the form to display data for the currently selected <see cref="RPG.Item"/>.
		/// </summary>
		public override void RefreshCurrentObject()
		{
			SuppressEvents = true;
			textBoxName.Text = _state.name;
			checkBoxNonrestistance.Checked = _state.nonresistance;
			checkBoxRegardHp0.Checked = _state.zero_hp;
			checkBoxNoExp.Checked = _state.cant_get_exp;
			checkBoxNoEvade.Checked = _state.cant_evade;
			//comboBoxAnimation.SelectedIndex = _state.animation_id;
			comboBoxRestriction.SelectedIndex = _state.restriction;
			checkGroupBoxElements.CheckAll(false);
			foreach (int id in _state.guard_element_set)
				checkGroupBoxElements.SetItemChecked(id - 1, true);
			checkedListBoxStates.SetAll(0);
			foreach (int id in _state.plus_state_set)
				checkedListBoxStates.SetItemIndex(id - 1, 1);
			foreach (int id in _state.minus_state_set)
				checkedListBoxStates.SetItemIndex(id - 1, 2);
			checkBoxReleaseEndBattle.Checked = _state.battle_only;
			numericTurns.Value = _state.hold_turn;
			numericTurnChance.Value = _state.auto_release_prob;
			numericDamageChance.Value = _state.shock_release_prob;
			RefreshParameters();


			//noteTextBox.NoteText = _state.note;
			SuppressEvents = false;
		}

		#endregion

		#region Private Methods

		private void DataObjectListIndexChanged(object sender, EventArgs e)
		{
			int index = this.dataObjectList.SelectedIndex;
			if (index < 0) return;
			this._state = this.Data[index + 1];
			this.RefreshCurrentObject();
		}

		private void RefreshParameters()
		{
			foreach (ParamBox ctrl in this.flowPanelParameters.Controls)
			{
				var property = typeof(State).GetProperty(ctrl.RpgAttribute);
				if (property != null)
					ctrl.Value = (int)property.GetValue(this._state, null);
			}
		}

		private void InitializeElements()
		{
			this.checkGroupBoxElements.BeginUpdate();
			this.checkGroupBoxElements.Items.Clear();
			for (int i = 1; i < Project.Data.System.elements.Count; i++)
				this.checkGroupBoxElements.Items.Add(Project.Data.System.elements[i]);
			this.checkGroupBoxElements.EndUpdate();
		}

		private void InitializeStates()
		{
			this.checkedListBoxStates.ClearItems();
			for (int i = 1; i < Data.Count; i++)
				this.checkedListBoxStates.AddItem(Data[i % Data.Count].name);
		}

		private void InitializeAnimations()
		{
			this.comboBoxAnimation.BeginUpdate();
			this.comboBoxAnimation.Items.Clear();
			this.comboBoxAnimation.Items.Add("<None>");
			//////////////////
#warning Fix this after loading of animations is fixed
			this.comboBoxAnimation.EndUpdate();
			return;
			//////////////////
			string name;
			foreach (Animation animation in Project.Data.Animations.Cast<Animation>().Where(animation => animation != null))
			{
				name = animation.ToString();
				this.comboBoxAnimation.Items.Add(name);
			}
			this.comboBoxAnimation.EndUpdate();
		}

		private void ParamBoxOnValueChanged(object sender, ParameterEventArgs e)
		{
			if (SuppressEvents) return;
			var paramBox = sender as ParamBox;
			if (paramBox != null)
			{
				var value = (int)paramBox.Value;
				var propertyName = paramBox.RpgAttribute;
				typeof(State).GetProperty(propertyName).SetValue(this._state, value, null);
			}
		}

		private void NumericTurnsValueChanged(object sender, EventArgs e)
		{
			if (SuppressEvents) return;
			_state.hold_turn = (int)numericTurns.Value;
		}

		private void NumericTurnChanceValueChanged(object sender, EventArgs e)
		{
			if (SuppressEvents) return;
			_state.auto_release_prob = (int)numericTurnChance.Value;
		}

		private void NumericDamageChanceValueChanged(object sender, EventArgs e)
		{
			if (SuppressEvents) return;
			_state.shock_release_prob = (int)numericDamageChance.Value;
		}

		private void TextBoxNameTextChanged(object sender, EventArgs e)
		{
			if (SuppressEvents) return;
			this._state.name = this.textBoxName.Text;
			int index = this.dataObjectList.SelectedIndex;
			this.dataObjectList.Items[index] = this._state.ToString();
			this.dataObjectList.Invalidate(this.dataObjectList.GetItemRectangle(index));
		}

		private void ComboBoxAnimationSelectedValueChanged(object sender, EventArgs e)
		{
			if (SuppressEvents) return;
			_state.animation_id = comboBoxAnimation.SelectedIndex;
		}

		private void ComboBoxRestrictionSelectedIndexChanged(object sender, EventArgs e)
		{
			if (SuppressEvents) return;
			_state.restriction = comboBoxRestriction.SelectedIndex;
		}

		private void CheckGroupBoxElementsCheckChanged(object sender, ItemCheckEventArgs e)
		{
			if (SuppressEvents) return;
			var id = e.Index + 1;
			if (e.NewValue == CheckState.Checked && !this._state.guard_element_set.Contains(id))
				this._state.guard_element_set.Add(id);
			else if (e.NewValue == CheckState.Unchecked && this._state.guard_element_set.Contains(id))
				this._state.guard_element_set.Remove(id);
		}

		private void CheckedListBoxStatesItemChanged(object sender, MultiStateCheckEventArgs e)
		{
			if (SuppressEvents) return;
			var id = e.Index + 1;
			this._state.plus_state_set.Remove(id);
			this._state.minus_state_set.Remove(id);
			if (e.ValueIndex == 1)
				this._state.plus_state_set.Add(id);
			if (e.ValueIndex == 2)
				this._state.minus_state_set.Add(id);
		}

		private void CheckBoxFlagsCheckChanged(object sender, EventArgs e)
		{
			if (SuppressEvents) return;
			var checkBox = sender as CheckBox;
			if (checkBox != null)
			{
				string propertyName = checkBox.Tag.ToString();
				typeof(State).GetProperty(propertyName).SetValue(this._state, checkBox.Checked, null);
			}
		}

		private void NoteTextBoxNoteTextChanged(object sender, EventArgs e)
		{
			if (SuppressEvents) return;
			//_state.note = this.noteTextBox.NoteText;
		}

		#endregion
	}
}
