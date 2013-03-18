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
		protected override DatabaseObjectListBox DataObjectList { get { return this.dataObjectList; } }

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
			this.InitializeComponent();
			this.InitializeElements();
			this.InitializeStates();
			RefreshObjectList();
			this.RefreshAvailableEquipment();
			this._listViewSorter = new ListViewColumnSorter();
			this.listViewSkills.ListViewItemSorter = this._listViewSorter;
			this.dataObjectList.SelectedIndex = 0;
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
            this.textBoxName.Text = this._class.name;
            this.comboBoxPosition.SelectedIndex = this._class.position;
            this.RefreshEquipment();
            this.RefreshSkills();
            this.RefreshElements();
            this.RefreshStates();
            SuppressEvents = false;
        }

        #endregion

        #region Private Methods

        private void InitializeElements()
		{
			this.checkedListElements.ClearItems();
			List<dynamic> elements = Project.Data.System.elements;
			for (int i = 1; i < elements.Count; i++)
				this.checkedListElements.AddItem(elements[i % elements.Count]);
		}

		private void InitializeStates()
		{
			this.checkedListStates.ClearItems();
			List<dynamic> states = Project.Data.States;
			for (int i = 1; i < states.Count; i++)
				this.checkedListStates.AddItem(states[i % states.Count].name);
		}

		private void RefreshElements()
		{
			for (int i = 1; i < Project.Data.System.elements.Count; i++)
				this.checkedListElements.SetItemIndex(i - 1, this._class.element_ranks[i]);
		}

		private void RefreshStates()
		{
			for (int i = 1; i < Project.Data.States.Count; i++)
				this.checkedListStates.SetItemIndex(i - 1, this._class.state_ranks[i]);
		}

		private void RefreshSkills()
		{
			this.listViewSkills.BeginUpdate();
			this.listViewSkills.Items.Clear();
			if (this._class != null)
			{
				string name;
				foreach (Class.Learning learning in this._class.learnings)
				{
					name = Project.Data.Skills[learning.skill_id].name;
					var item = new ListViewItem(new[] { learning.level.ToString(CultureInfo.InvariantCulture), 
						learning.skill_id.ToString(CultureInfo.InvariantCulture), name });
					this.listViewSkills.Items.Add(item);
				}
			}
			this.listViewSkills.EndUpdate();
		}

        private void ListBoxClassesSelectedIndexChanged(object sender, EventArgs e)
        {
            int index = this.dataObjectList.SelectedIndex;
            if (index >= 0)
            {
                this._class = this.Data[index + 1];
                this.RefreshCurrentObject();
            }
        }

		private void TextBoxNameTextChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
			{
				this._class.name = this.textBoxName.Text;
				int index = this.dataObjectList.SelectedIndex;
				this.dataObjectList.Items[index] = this._class.ToString();
				this.dataObjectList.Invalidate(this.dataObjectList.GetItemRectangle(index));
			}
		}

		private void RefreshAvailableEquipment()
		{
			this.checkGroupWeapons.BeginUpdate();
			this.checkGroupWeapons.Items.Clear();
			foreach (Weapon weapon in Project.Data.Weapons)
			{
				if (weapon != null)
					this.checkGroupWeapons.Items.Add(weapon.name);
			}
			this.checkGroupWeapons.EndUpdate();
			this.checkGroupArmor.BeginUpdate();
			this.checkGroupArmor.Items.Clear();
			foreach (Armor armor in Project.Data.Armors)
			{
				if (armor != null)
					this.checkGroupArmor.Items.Add(armor.name);
			}
			this.checkGroupArmor.EndUpdate();
		}

		private void RefreshEquipment()
		{
			SuppressEvents = true;
			this.checkGroupWeapons.CheckAll(false);
			foreach (int id in this._class.weapon_set)
				this.checkGroupWeapons.SetItemChecked(id - 1, true);
			this.checkGroupArmor.CheckAll(false);
			foreach (int id in this._class.armor_set)
				this.checkGroupArmor.SetItemChecked(id - 1, true);
			SuppressEvents = false;
		}

		private void ComboBoxPositionSelectedIndexChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
				this._class.position = this.comboBoxPosition.SelectedIndex;
		}

		private void CheckGroupWeaponsOnCheckChange(object sender, ItemCheckEventArgs e)
		{
			int id = e.Index + 1;
			if (e.NewValue == CheckState.Checked && !this._class.weapon_set.Contains(id))
				this._class.weapon_set.Add(id);
			else if (e.NewValue == CheckState.Unchecked && this._class.weapon_set.Contains(id))
				this._class.weapon_set.Remove(id);
		}

		private void CheckGroupArmorOnCheckChange(object sender, ItemCheckEventArgs e)
		{
			int id = e.Index + 1;
			if (e.NewValue == CheckState.Checked && !this._class.armor_set.Contains(id))
				this._class.armor_set.Add(id);
			else if (e.NewValue == CheckState.Unchecked && this._class.armor_set.Contains(id))
				this._class.armor_set.Remove(id);
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
			var index = this.GetSkillIndex();
			if (this._class != null && index >= 0)
			{
				this._class.learnings.RemoveAt(index);
				this.RefreshSkills();
				this.listViewSkills.Focus();
				this.ListViewSkillsSelectedIndexChanged(sender, e);
			}
			if (this.listViewSkills.Items.Count > 0)
				this.listViewSkills.Items[index.Clamp(0, this.listViewSkills.Items.Count - 1)].Selected = true;
		}

		private void ButtonEditSkillClick(object sender, EventArgs e)
		{
			var index = this.GetSkillIndex();
			using (var dialog = new EditSkillDialog())
			{
				Class.Learning learning = this._class.learnings[index];
				dialog.Learning = learning;
			    if (dialog.ShowDialog(this) != DialogResult.OK) return;
			    this._class.learnings[index] = dialog.Learning;
			    this.RefreshSkills();
			}
		}

		private int GetSkillIndex()
		{
			if (this.listViewSkills.SelectedIndices.Count > 0)
				return this.listViewSkills.SelectedIndices[0];
			return -1;
		}

		private void ListViewSkillsSelectedIndexChanged(object sender, EventArgs e)
		{
			var enable = this.listViewSkills.SelectedItems.Count > 0;
			this.buttonEditSkill.Enabled = enable;
			this.buttonRemoveSkill.Enabled = enable;
			this.contextButtonSkillEdit.Enabled = enable;
			this.contextButtonSkillRemove.Enabled = enable;
		}

		private void ListViewSkillsDoubleClick(object sender, EventArgs e)
		{
			var pnt = this.listViewSkills.PointToClient(MousePosition);
			var info = this.listViewSkills.HitTest(pnt);
			if (info.Item != null)
				this.ButtonEditSkillClick(sender, e);
		}

		private void ListViewSkillsColumnClick(object sender, ColumnClickEventArgs e)
		{
			if (e.Column == this._listViewSorter.SortColumn)
			{
				this._listViewSorter.Order = (this._listViewSorter.Order == SortOrder.Ascending) ? 
					SortOrder.Descending : SortOrder.Ascending;
			}
			else
			{
				this._listViewSorter.SortColumn = e.Column;
				this._listViewSorter.Order = SortOrder.Ascending;
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
