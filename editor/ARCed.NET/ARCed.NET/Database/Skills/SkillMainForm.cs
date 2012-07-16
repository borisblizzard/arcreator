#region Using Directives

using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;
using ARCed.Controls;
using ARCed.Dialogs;
using ARCed.Helpers;
using RPG;

#endregion

namespace ARCed.Database.Skills
{
    /// <summary>
    /// Main form for configuring Project <see cref="RPG.State"/> data.
    /// </summary>
	public sealed partial class SkillMainForm : DatabaseWindow
	{
		#region Private Fields

		private Skill _skill;

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
		public override List<dynamic> Data { get { return Project.Data.Skills; } }

		#endregion

        #region Constructor

        /// <summary>
		/// Default constructor
		/// </summary>
		public SkillMainForm()
		{
			InitializeComponent();
			InitializeElements();
			InitializeStates();
			InitializeAnimations();
			InitializeCommonEvents();
			RefreshObjectList();
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
            if (type.HasFlag(RefreshType.Animations))
            {

            }
            if (type.HasFlag(RefreshType.Scopes))
            {

            }
            if (type.HasFlag(RefreshType.Parameters))
            {

            }
            if (type.HasFlag(RefreshType.Occasions))
            {

            }
            if (type.HasFlag(RefreshType.CommonEvents))
            {

            }
        }

        /// <summary>
        /// Refreshes the form to display data for the currently selected <see cref="RPG.Skill"/>.
        /// </summary>
        public override void RefreshCurrentObject()
        {
            SuppressEvents = true;
            RefreshIcon();
            textBoxName.Text = _skill.name;
            textBoxDescription.Text = _skill.description;
            RefreshElements();
            RefreshStates();
            comboBoxScope.SelectedIndex = _skill.scope;
            comboBoxOccasion.SelectedIndex = _skill.occasion;
            comboBoxCommonEvent.SelectedIndex = _skill.common_event_id;
            RefreshMenuSE();
            RefreshAnimations();
            RefreshParameters();
            //noteTextBox.NoteText = _item.note;
            SuppressEvents = false;
        }

        #endregion

		#region Private Methods

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
			var states = Project.Data.States;
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
			foreach (Animation animation in Project.Data.Animations.Cast<Animation>().Where(animation => animation != null))
			{
			    name = animation.ToString();
			    this.comboBoxUserAnimation.Items.Add(name);
			    this.comboBoxTargetAnimation.Items.Add(name);
			}
			comboBoxUserAnimation.EndUpdate();
			comboBoxTargetAnimation.EndUpdate();
		}

		private void InitializeCommonEvents()
		{
			ControlHelper.Populate(comboBoxCommonEvent, Project.Data.CommonEvents, true);
		}

        private void RefreshParameters()
		{
			foreach (Control ctrl in flowPanel.Controls)
			{
			    if (!(ctrl is ParamBox)) continue;
			    var param = ctrl as ParamBox;
			    var property = typeof(Skill).GetProperty(param.RpgAttribute);
			    if (property != null)
			        param.Value = (int)property.GetValue(this._skill, null);
			}
		}

		private void RefreshIcon()
		{
			if (_skill.icon_name == "")
			{
				pictureBoxIcon.BackgroundImage = null;
				textBoxIcon.Text = "<None>";
			}
			else
			{
				pictureBoxIcon.BackgroundImage = Cache.Icon(_skill.icon_name);
				textBoxIcon.Text = _skill.icon_name;
			}
		}

		private void RefreshElements()
		{
			checkGroupBoxElements.CheckAll(false);
			foreach (int id in _skill.element_set)
				checkGroupBoxElements.SetItemChecked(id - 1, true);
		}

		private void RefreshStates()
		{
			checkedListBoxStates.SetAll(0);
			foreach (int id in _skill.plus_state_set)
				checkedListBoxStates.SetItemIndex(id - 1, 1);
			foreach (int id in _skill.minus_state_set)
				checkedListBoxStates.SetItemIndex(id - 1, 2);
		}

		private void RefreshAnimations()
		{
#warning Fix this after loading of animations is fixed
			return;
			comboBoxUserAnimation.SelectedIndex = _skill.animation1_id;
			comboBoxTargetAnimation.SelectedIndex = _skill.animation2_id;
		}

		private void RefreshMenuSE() 
        {
		    this.textBoxMenuSe.Text = this._skill.menu_se.name != "" ? 
                this._skill.menu_se.ToString() : "";
		}

        private void ListBoxSkillsOnListBoxIndexChanged(object sender, EventArgs e)
		{
			var index = dataObjectList.SelectedIndex;
			if (index >= 0)
			{
				_skill = Data[index + 1];
				RefreshCurrentObject();
			}
		}

		private void ButtonIconClick(object sender, EventArgs e)
		{
			using (var dialog = new ImageSelectionForm(@"Icons", _skill.icon_name))
			{
			    if (dialog.ShowDialog(this) != DialogResult.OK) return;
			    this._skill.icon_name = dialog.ImageName;
			    this.RefreshIcon();
			}
		}

		private void TextBoxNameTextChanged(object sender, EventArgs e)
		{
		    if (SuppressEvents) return;
		    this._skill.name = this.textBoxName.Text;
		    var index = this.dataObjectList.SelectedIndex;
		    this.dataObjectList.Items[index] = this._skill.ToString();
		    this.dataObjectList.Invalidate(this.dataObjectList.GetItemRectangle(index));
		}

		private void TextBoxDescriptionTextChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
				_skill.description = textBoxDescription.Text;
		}

		private void CheckGroupBoxElementsOnCheckChange(object sender, ItemCheckEventArgs e)
		{
		    if (SuppressEvents) return;
		    int id = e.Index + 1;
		    if (e.NewValue == CheckState.Checked && !this._skill.element_set.Contains(id))
		        this._skill.element_set.Add(id);
		    else if (e.NewValue == CheckState.Unchecked && this._skill.element_set.Contains(id))
		        this._skill.element_set.Remove(id);
		}

		private void CheckGroupFocusLeave(object sender, EventArgs e)
		{
		    var checkGroupBox = sender as CheckGroupBox;
		    if (checkGroupBox != null) checkGroupBox.SelectedIndex = -1;
		}

        private void ComboBoxScopeSelectedIndexChanged(object sender, EventArgs e)
		{
			if (SuppressEvents)
				_skill.scope = comboBoxScope.SelectedIndex;
		}

		private void ComboBoxOccasionSelectedIndexChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
				_skill.occasion = comboBoxOccasion.SelectedIndex;
		}

		private void ComboBoxUserAnimationSelectedIndexChanged(object sender, EventArgs e)
		{
			if (SuppressEvents)
				_skill.animation1_id = comboBoxUserAnimation.SelectedIndex;
		}

		private void ComboBoxTargetAnimationSelectedIndexChanged(object sender, EventArgs e)
		{
			if (SuppressEvents)
				_skill.animation2_id = comboBoxTargetAnimation.SelectedIndex;
		}

		private void paramBox_OnValueChanged(object sender, ParameterEventArgs e)
		{
			var paramBox = sender as ParamBox;
		    if (paramBox == null) return;
		    var value = (int)paramBox.Value;
		    string propertyName = paramBox.RpgAttribute;
		    typeof(Skill).GetProperty(propertyName).SetValue(this._skill, value, null);
		}

		private void CheckedListBoxStatesOnItemChanged(object sender, MultiStateCheckEventArgs e)
		{
			int id = e.Index + 1;
			_skill.plus_state_set.Remove(id);
			_skill.minus_state_set.Remove(id);
			if (e.ValueIndex == 1)
				_skill.plus_state_set.Add(id);
			if (e.ValueIndex == 2)
				_skill.minus_state_set.Add(id);
		}

		private void ComboBoxCommonEventSelectedIndexChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
				_skill.common_event_id = comboBoxCommonEvent.SelectedIndex;
		}

		private void NoteTextBoxNoteTextChanged(object sender, EventArgs e)
		{
			//if (!suppressEvents)
				//_item.note = noteTextBox.NoteText;
		}

		private void TextBoxMenuSeOnButtonClick(object sender, EventArgs e)
		{

        }

        #endregion
    }
}
