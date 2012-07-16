#region Using Directives

using System;
using System.Collections.Generic;
using System.Windows.Forms;
using ARCed.Controls;
using ARCed.Dialogs;
using ARCed.Helpers;
using RPG;

#endregion

namespace ARCed.Database.Weapons
{
	public partial class WeaponMainForm : DatabaseWindow
	{

		#region Private Fields

		private Weapon _weapon;

		#endregion

		protected override DatabaseObjectListBox DataObjectList { get { return dataObjectList; } }
		public override List<dynamic> Data { get { return Project.Data.Weapons; } }

		#region Constructors

		/// <summary>
		/// Default constructor
		/// </summary>
		public WeaponMainForm()
		{
			InitializeComponent();
			InitializeElements();
			InitializeStates();
			InitializeAnimations();
			RefreshObjectList();
			dataObjectList.SelectedIndex = 0;
		}

		#endregion

		#region Control Initialization

		private void InitializeElements()
		{
			checkGroupBoxElements.BeginUpdate();
			checkGroupBoxElements.Items.Clear();
			for (int i = 1; i < Project.Data.System.elements.Count; i++)
				checkGroupBoxElements.Items.Add(Project.Data.System.elements[i]);
			checkGroupBoxElements.EndUpdate();
		}

		private void InitializeStates()
		{
			checkedListBoxStates.ClearItems();
			List<dynamic> states = Project.Data.States;
			for (int i = 1; i < states.Count; i++)
				checkedListBoxStates.AddItem(states[i % states.Count].name);
		}

		private void InitializeAnimations()
		{
#warning Fix this after loading of animations is fixed
			return;
			comboBoxUserAnimation.BeginUpdate();
			comboBoxTargetAnimation.BeginUpdate();
			comboBoxUserAnimation.Items.Clear();
			comboBoxTargetAnimation.Items.Clear();
			comboBoxUserAnimation.Items.Add("<None>");
			comboBoxTargetAnimation.Items.Add("<None>");
			string name;
			foreach (Animation animation in Project.Data.Animations)
			{
				if (animation != null)
				{
					name = animation.ToString();
					comboBoxUserAnimation.Items.Add(name);
					comboBoxTargetAnimation.Items.Add(name);
				}
			}
			comboBoxUserAnimation.EndUpdate();
			comboBoxTargetAnimation.EndUpdate();
		}

		#endregion

		#region Refreshing

		/// <summary>
		/// Refreshes objects by type flag
		/// </summary>
		/// <param name="type">Flag for type of object to refresh</param>
		public override void NotifyRefresh(RefreshType type)
		{
			if (type.HasFlag(RefreshType.Enemies))
			{

			}
			if (type.HasFlag(RefreshType.Switches))
			{

			}
		}

		public override void RefreshCurrentObject()
		{
			SuppressEvents = true;
			textBoxName.Text = _weapon.name;
			textBoxDescription.Text = _weapon.description;
			//comboBoxUserAnimation.SelectedIndex = _armor.animation1_id;
			//comboBoxTargetAnimation.SelectedIndex = _armor.animation2_id;
			RefreshIcon();
			RefreshParameters();
			RefreshElements();
			RefreshStates();
			SuppressEvents = false;
		}

		private void RefreshElements()
		{
			checkGroupBoxElements.CheckAll(false);
			foreach (int id in _weapon.element_set)
				checkGroupBoxElements.SetItemChecked(id - 1, true);
		}

		private void RefreshStates()
		{
			checkedListBoxStates.SetAll(0);
			foreach (int id in _weapon.plus_state_set)
				checkedListBoxStates.SetItemIndex(id - 1, 1);
			foreach (int id in _weapon.minus_state_set)
				checkedListBoxStates.SetItemIndex(id - 1, 2);
		}

		private void RefreshParameters()
		{
			foreach (Control ctrl in flowPanel.Controls)
			{
				if (ctrl is ParamBox)
				{
					var param = ctrl as ParamBox;
					var property = typeof(Weapon).GetProperty(param.RpgAttribute);
					if (property != null)
						param.Value = (int)property.GetValue(_weapon, null);
				}
			}
		}

		private void RefreshIcon()
		{
			if (_weapon.icon_name == "")
			{
				pictureBoxIcon.BackgroundImage = null;
				textBoxIcon.Text = "<None>";
			}
			else
			{
				pictureBoxIcon.BackgroundImage = Cache.Icon(_weapon.icon_name);
				textBoxIcon.Text = _weapon.icon_name;
			}
		}

		#endregion

		private void listBoxWeapons_OnListBoxIndexChanged(object sender, EventArgs e)
		{
			int index = dataObjectList.SelectedIndex;
			if (index >= 0)
			{
				_weapon = Data[index + 1];
				RefreshCurrentObject();
			}
		}

		private void textBoxName_TextChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
			{
				_weapon.name = textBoxName.Text;
				int index = dataObjectList.SelectedIndex;
				dataObjectList.Items[index] = _weapon.ToString();
				dataObjectList.Invalidate(dataObjectList.GetItemRectangle(index));
			}
		}

		private void textBoxDescription_TextChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
				_weapon.description = textBoxDescription.Text;
		}

		private void buttonIcon_Click(object sender, EventArgs e)
		{
			using (var dialog = new ImageSelectionForm(@"Icons", _weapon.icon_name))
			{
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					_weapon.icon_name = dialog.ImageName;
					RefreshIcon();
				}
			}
		}

		private void comboBoxUserAnimation_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
				_weapon.animation1_id = comboBoxUserAnimation.SelectedIndex;
		}

		private void comboBoxTargetAnimation_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
				_weapon.animation2_id = comboBoxTargetAnimation.SelectedIndex;
		}

		private void paramBox_OnValueChanged(object sender, ParameterEventArgs e)
		{
			if (!SuppressEvents)
			{
				var paramBox = sender as ParamBox;
				var value = (int)paramBox.Value;
				string propertyName = paramBox.RpgAttribute;
				typeof(Weapon).GetProperty(propertyName).SetValue(_weapon, value, null);
			}
		}

		private void checkGroupBoxElements_OnCheckChange(object sender, ItemCheckEventArgs e)
		{
			if (!SuppressEvents)
			{
				int id = e.Index + 1;
				if (e.NewValue == CheckState.Checked && !_weapon.element_set.Contains(id))
					_weapon.element_set.Add(id);
				else if (e.NewValue == CheckState.Unchecked && _weapon.element_set.Contains(id))
					_weapon.element_set.Remove(id);
			}
		}

		private void checkedListBoxStates_OnItemChanged(object sender, MultiStateCheckEventArgs e)
		{
			if (!SuppressEvents)
			{
				int id = e.Index + 1;
				_weapon.plus_state_set.Remove(id);
				_weapon.minus_state_set.Remove(id);
				if (e.ValueIndex == 1)
					_weapon.plus_state_set.Add(id);
				if (e.ValueIndex == 2)
					_weapon.minus_state_set.Add(id);
			}
		}

		private void noteTextBox_NoteTextChanged(object sender, EventArgs e)
		{
			//if (!suppressEvents)
				//_armor.note = noteTextBox.NoteText;
		}
	}
}
