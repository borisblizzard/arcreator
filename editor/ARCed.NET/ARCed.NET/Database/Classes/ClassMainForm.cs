using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Controls;
using ARCed.Helpers;
using ARCed.UI;
using ARCed.Controls;

namespace ARCed.Database.Classes
{
	public partial class ClassMainForm : DatabaseWindow
	{
		#region Private Fields

		private RPG.Class _class;
		private ListViewColumnSorter _listViewSorter;

		#endregion

		#region Protected Properties

		/// <summary>
		/// Gets the object list control of this database panel.
		/// </summary>
		protected override DatabaseObjectListBox DataObjectList { get { return dataObjectList; } }

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets the data associated with this panel.
		/// </summary>
		public override List<dynamic> Data { get { return Project.Data.Classes; } }

		#endregion

		/// <summary>
		/// 
		/// </summary>
		public ClassMainForm() : base()
		{
			InitializeComponent();
			InitializeElements();
			InitializeStates();
			RefreshObjectList();
			RefreshAvailableEquipment();
			_listViewSorter = new ListViewColumnSorter();
			listViewSkills.ListViewItemSorter = _listViewSorter;
			dataObjectList.SelectedIndex = 0;
		}

		public void InitializeElements()
		{
			checkedListElements.ClearItems();
			List<dynamic> elements = Project.Data.System.elements;
			for (int i = 1; i < elements.Count; i++)
				checkedListElements.AddItem(elements[i % elements.Count]);
		}

		public void InitializeStates()
		{
			checkedListStates.ClearItems();
			List<dynamic> states = Project.Data.States;
			for (int i = 1; i < states.Count; i++)
				checkedListStates.AddItem(states[i % states.Count].name);
		}

		private void RefreshElements()
		{
			for (int i = 1; i < Project.Data.System.elements.Count; i++)
				checkedListElements.SetItemIndex(i - 1, _class.element_ranks[i]);
		}

		private void RefreshStates()
		{
			for (int i = 1; i < Project.Data.States.Count; i++)
				checkedListStates.SetItemIndex(i - 1, _class.state_ranks[i]);
		}

		private void RefreshSkills()
		{
			listViewSkills.BeginUpdate();
			listViewSkills.Items.Clear();
			if (_class != null)
			{
				string name;
				foreach (RPG.Class.Learning learning in _class.learnings)
				{
					name = Project.Data.Skills[learning.skill_id].name;
					ListViewItem item = new ListViewItem(new[] { learning.level.ToString(), 
						learning.skill_id.ToString(), name });
					listViewSkills.Items.Add(item);
				}
			}
			listViewSkills.EndUpdate();
		}

		/// <summary>
		/// Refreshes objects by type flag
		/// </summary>
		/// <param name="type">Flag for type of object to refresh</param>
		public override void NotifyRefresh(RefreshType type)
		{
			if (type.HasFlag(RefreshType.States))
			{

			}
			if (type.HasFlag(RefreshType.Elements))
			{

			}
			if (type.HasFlag(RefreshType.Weapons))
			{

			}
			if (type.HasFlag(RefreshType.Armors))
			{

			}
			if (type.HasFlag(RefreshType.Skills))
			{

			}
		}

		public override void RefreshCurrentObject()
		{
			suppressEvents = true;
			textBoxName.Text = _class.name;
			comboBoxPosition.SelectedIndex = _class.position;
			RefreshEquipment();
			RefreshSkills();
			RefreshElements();
			RefreshStates();
			suppressEvents = false;
		}

		private void listBoxClasses_SelectedIndexChanged(object sender, EventArgs e)
		{
			int index = dataObjectList.SelectedIndex;
			if (index >= 0)
			{	
				_class = Data[index + 1];
				RefreshCurrentObject();
			}
		}

		private void textBoxName_TextChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
			{
				_class.name = textBoxName.Text;
				int index = dataObjectList.SelectedIndex;
				dataObjectList.Items[index] = _class.ToString();
				dataObjectList.Invalidate(dataObjectList.GetItemRectangle(index));
			}
		}

		private void RefreshAvailableEquipment()
		{
			checkGroupWeapons.BeginUpdate();
			checkGroupWeapons.Items.Clear();
			foreach (RPG.Weapon weapon in Project.Data.Weapons)
			{
				if (weapon != null)
					checkGroupWeapons.Items.Add(weapon.name);
			}
			checkGroupWeapons.EndUpdate();
			checkGroupArmor.BeginUpdate();
			checkGroupArmor.Items.Clear();
			foreach (RPG.Armor armor in Project.Data.Armors)
			{
				if (armor != null)
					checkGroupArmor.Items.Add(armor.name);
			}
			checkGroupArmor.EndUpdate();
		}

		private void RefreshEquipment()
		{
			suppressEvents = true;
			checkGroupWeapons.CheckAll(false);
			foreach (int id in _class.weapon_set)
				checkGroupWeapons.SetItemChecked(id - 1, true);
			checkGroupArmor.CheckAll(false);
			foreach (int id in _class.armor_set)
				checkGroupArmor.SetItemChecked(id - 1, true);
			suppressEvents = false;
		}

		private void comboBoxPosition_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
				_class.position = comboBoxPosition.SelectedIndex;
		}

		private void checkGroupWeapons_OnCheckChange(object sender, ItemCheckEventArgs e)
		{
			int id = e.Index + 1;
			if (e.NewValue == CheckState.Checked && !_class.weapon_set.Contains(id))
				_class.weapon_set.Add(id);
			else if (e.NewValue == CheckState.Unchecked && _class.weapon_set.Contains(id))
				_class.weapon_set.Remove(id);
		}

		private void checkGroupArmor_OnCheckChange(object sender, ItemCheckEventArgs e)
		{
			int id = e.Index + 1;
			if (e.NewValue == CheckState.Checked && !_class.armor_set.Contains(id))
				_class.armor_set.Add(id);
			else if (e.NewValue == CheckState.Unchecked && _class.armor_set.Contains(id))
				_class.armor_set.Remove(id);
		}

		private void checkGroup_FocusLeave(object sender, EventArgs e)
		{
			(sender as CheckGroupBox).SelectedIndex = -1;
		}

		private void buttonAddSkill_Click(object sender, EventArgs e)
		{
			using (EditSkillDialog dialog = new EditSkillDialog())
			{
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					_class.learnings.Add(dialog.Learning);
					RefreshSkills();
				}
			}
		}

		private void buttonRemoveSkill_Click(object sender, EventArgs e)
		{
			int index = GetSkillIndex();
			if (_class != null && index >= 0)
			{
				_class.learnings.RemoveAt(index);
				RefreshSkills();
				listViewSkills.Focus();
				listViewSkills_SelectedIndexChanged(sender, e);
			}
			if (listViewSkills.Items.Count > 0)
				listViewSkills.Items[index.Clamp(0, listViewSkills.Items.Count - 1)].Selected = true;
		}

		private void buttonEditSkill_Click(object sender, EventArgs e)
		{
			int index = GetSkillIndex();
			using (EditSkillDialog dialog = new EditSkillDialog())
			{
				RPG.Class.Learning learning = _class.learnings[index];
				dialog.Learning = learning;
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					_class.learnings[index] = dialog.Learning;
					RefreshSkills();
				}
			}
		}

		private int GetSkillIndex()
		{
			if (listViewSkills.SelectedIndices.Count > 0)
				return listViewSkills.SelectedIndices[0];
			return -1;
		}

		private void listViewSkills_SelectedIndexChanged(object sender, EventArgs e)
		{
			bool enable = listViewSkills.SelectedItems.Count > 0;
			buttonEditSkill.Enabled = enable;
			buttonRemoveSkill.Enabled = enable;
			contextButtonSkillEdit.Enabled = enable;
			contextButtonSkillRemove.Enabled = enable;
		}

		private void listViewSkills_DoubleClick(object sender, EventArgs e)
		{
			Point pnt = listViewSkills.PointToClient(MousePosition);
			ListViewHitTestInfo info = listViewSkills.HitTest(pnt);
			if (info.Item != null)
				buttonEditSkill_Click(sender, e);
		}

		private void listViewSkills_ColumnClick(object sender, ColumnClickEventArgs e)
		{
			if (e.Column == _listViewSorter.SortColumn)
			{
				_listViewSorter.Order = (_listViewSorter.Order == SortOrder.Ascending) ? 
					SortOrder.Descending : SortOrder.Ascending;
			}
			else
			{
				_listViewSorter.SortColumn = e.Column;
				_listViewSorter.Order = SortOrder.Ascending;
			}
			((ListView)sender).Sort();
		}

		private void efficiencyElements_OnItemChanged(object sender, MultiStateCheckEventArgs e)
		{
			if (!suppressEvents)
				_class.element_ranks[e.Index + 1] = (sender as MultiStateCheckbox).SelectedState;
		}

		private void efficiencyStates_OnItemChanged(object sender, MultiStateCheckEventArgs e)
		{
			if (!suppressEvents)
				_class.state_ranks[e.Index + 1] = (sender as MultiStateCheckbox).SelectedState;
		}

		private void noteTextBox_NoteTextChanged(object sender, EventArgs e)
		{
			//if (!suppressEvents)
				//_class.note = noteTextBox.NoteText;
		}
	}
}
