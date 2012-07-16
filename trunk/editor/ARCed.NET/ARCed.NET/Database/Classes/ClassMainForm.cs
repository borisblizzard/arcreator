#region Using Directives

using System;
using System.Collections.Generic;
using System.Globalization;
using System.Windows.Forms;
using ARCed.Controls;
using RPG;

#endregion

namespace ARCed.Database.Classes
{    
    /// <summary>
    /// Main form for configuring Project <see cref="RPG.Class"/> data.
    /// </summary>
	public sealed partial class ClassMainForm : DatabaseWindow
	{
		#region Private Fields

		private Class _class;
		private readonly ListViewColumnSorter _listViewSorter;

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

        #region Constructor

        /// <summary>
		/// Default constructor
		/// </summary>
		public ClassMainForm()
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

        #endregion

        #region Public Methods

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

        /// <summary>
        /// Refreshes the form to display data for the currently selected <see cref="RPG.Class"/>.
        /// </summary>
        public override void RefreshCurrentObject()
        {
            SuppressEvents = true;
            textBoxName.Text = _class.name;
            comboBoxPosition.SelectedIndex = _class.position;
            RefreshEquipment();
            RefreshSkills();
            RefreshElements();
            RefreshStates();
            SuppressEvents = false;
        }

        #endregion

        #region Private Methods

        private void InitializeElements()
		{
			checkedListElements.ClearItems();
			List<dynamic> elements = Project.Data.System.elements;
			for (int i = 1; i < elements.Count; i++)
				checkedListElements.AddItem(elements[i % elements.Count]);
		}

		private void InitializeStates()
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
				foreach (Class.Learning learning in _class.learnings)
				{
					name = Project.Data.Skills[learning.skill_id].name;
					var item = new ListViewItem(new[] { learning.level.ToString(CultureInfo.InvariantCulture), 
						learning.skill_id.ToString(CultureInfo.InvariantCulture), name });
					listViewSkills.Items.Add(item);
				}
			}
			listViewSkills.EndUpdate();
		}

        private void ListBoxClassesSelectedIndexChanged(object sender, EventArgs e)
        {
            int index = dataObjectList.SelectedIndex;
            if (index >= 0)
            {
                _class = Data[index + 1];
                RefreshCurrentObject();
            }
        }

		private void TextBoxNameTextChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
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
			foreach (Weapon weapon in Project.Data.Weapons)
			{
				if (weapon != null)
					checkGroupWeapons.Items.Add(weapon.name);
			}
			checkGroupWeapons.EndUpdate();
			checkGroupArmor.BeginUpdate();
			checkGroupArmor.Items.Clear();
			foreach (Armor armor in Project.Data.Armors)
			{
				if (armor != null)
					checkGroupArmor.Items.Add(armor.name);
			}
			checkGroupArmor.EndUpdate();
		}

		private void RefreshEquipment()
		{
			SuppressEvents = true;
			checkGroupWeapons.CheckAll(false);
			foreach (int id in _class.weapon_set)
				checkGroupWeapons.SetItemChecked(id - 1, true);
			checkGroupArmor.CheckAll(false);
			foreach (int id in _class.armor_set)
				checkGroupArmor.SetItemChecked(id - 1, true);
			SuppressEvents = false;
		}

		private void ComboBoxPositionSelectedIndexChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
				_class.position = comboBoxPosition.SelectedIndex;
		}

		private void CheckGroupWeaponsOnCheckChange(object sender, ItemCheckEventArgs e)
		{
			int id = e.Index + 1;
			if (e.NewValue == CheckState.Checked && !_class.weapon_set.Contains(id))
				_class.weapon_set.Add(id);
			else if (e.NewValue == CheckState.Unchecked && _class.weapon_set.Contains(id))
				_class.weapon_set.Remove(id);
		}

		private void CheckGroupArmorOnCheckChange(object sender, ItemCheckEventArgs e)
		{
			int id = e.Index + 1;
			if (e.NewValue == CheckState.Checked && !_class.armor_set.Contains(id))
				_class.armor_set.Add(id);
			else if (e.NewValue == CheckState.Unchecked && _class.armor_set.Contains(id))
				_class.armor_set.Remove(id);
		}

		private void CheckGroupFocusLeave(object sender, EventArgs e)
		{
		    var checkGroupBox = sender as CheckGroupBox;
		    if (checkGroupBox != null) checkGroupBox.SelectedIndex = -1;
		}

    private void ButtonAddSkillClick(object sender, EventArgs e)
		{
			using (var dialog = new EditSkillDialog())
			{
			    if (dialog.ShowDialog(this) != DialogResult.OK) return;
			    this._class.learnings.Add(dialog.Learning);
			    this.RefreshSkills();
			}
		}

		private void ButtonRemoveSkillClick(object sender, EventArgs e)
		{
			var index = GetSkillIndex();
			if (_class != null && index >= 0)
			{
				_class.learnings.RemoveAt(index);
				RefreshSkills();
				listViewSkills.Focus();
				this.ListViewSkillsSelectedIndexChanged(sender, e);
			}
			if (listViewSkills.Items.Count > 0)
				listViewSkills.Items[index.Clamp(0, listViewSkills.Items.Count - 1)].Selected = true;
		}

		private void ButtonEditSkillClick(object sender, EventArgs e)
		{
			var index = GetSkillIndex();
			using (var dialog = new EditSkillDialog())
			{
				Class.Learning learning = _class.learnings[index];
				dialog.Learning = learning;
			    if (dialog.ShowDialog(this) != DialogResult.OK) return;
			    this._class.learnings[index] = dialog.Learning;
			    this.RefreshSkills();
			}
		}

		private int GetSkillIndex()
		{
			if (listViewSkills.SelectedIndices.Count > 0)
				return listViewSkills.SelectedIndices[0];
			return -1;
		}

		private void ListViewSkillsSelectedIndexChanged(object sender, EventArgs e)
		{
			var enable = listViewSkills.SelectedItems.Count > 0;
			buttonEditSkill.Enabled = enable;
			buttonRemoveSkill.Enabled = enable;
			contextButtonSkillEdit.Enabled = enable;
			contextButtonSkillRemove.Enabled = enable;
		}

		private void ListViewSkillsDoubleClick(object sender, EventArgs e)
		{
			var pnt = listViewSkills.PointToClient(MousePosition);
			var info = listViewSkills.HitTest(pnt);
			if (info.Item != null)
				this.ButtonEditSkillClick(sender, e);
		}

		private void ListViewSkillsColumnClick(object sender, ColumnClickEventArgs e)
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

		private void EfficiencyElementsOnItemChanged(object sender, MultiStateCheckEventArgs e)
		{
			if (!SuppressEvents)
			{
			    var multiStateCheckbox = sender as MultiStateCheckbox;
			    if (multiStateCheckbox != null)
			        this._class.element_ranks[e.Index + 1] = multiStateCheckbox.SelectedState;
			}
		}

		private void EfficiencyStatesOnItemChanged(object sender, MultiStateCheckEventArgs e)
		{
			if (!SuppressEvents)
			{
			    var multiStateCheckbox = sender as MultiStateCheckbox;
			    if (multiStateCheckbox != null)
			        this._class.state_ranks[e.Index + 1] = multiStateCheckbox.SelectedState;
			}
		}

		private void NoteTextBoxNoteTextChanged(object sender, EventArgs e)
		{
			//if (!suppressEvents)
				//_class.note = noteTextBox.NoteText;
        }

        #endregion
    }
}
