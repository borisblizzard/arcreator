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
		protected override DatabaseObjectListBox DataObjectList { get { return this.dataObjectList; } }

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
			this.InitializeComponent();
			this.InitializeElements();
			this.InitializeStates();
			this.InitializeAnimations();
			this.InitializeCommonEvents();
			RefreshObjectList();
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
            this.RefreshIcon();
            this.textBoxName.Text = this._skill.name;
            this.textBoxDescription.Text = this._skill.description;
            this.RefreshElements();
            this.RefreshStates();
            this.comboBoxScope.SelectedIndex = this._skill.scope;
            this.comboBoxOccasion.SelectedIndex = this._skill.occasion;
            this.comboBoxCommonEvent.SelectedIndex = this._skill.common_event_id;
            this.RefreshMenuSE();
            this.RefreshAnimations();
            this.RefreshParameters();
            //noteTextBox.NoteText = _item.note;
            SuppressEvents = false;
        }

        #endregion

		#region Private Methods

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
			var states = Project.Data.States;
			for (int i = 1; i < states.Count; i++)
				this.checkedListBoxStates.AddItem(states[i % states.Count].name);
		}

		private void InitializeAnimations()
		{
#warning Fix this after loading of animations is fixed
			return;
			this.comboBoxUserAnimation.BeginUpdate();
			this.comboBoxTargetAnimation.BeginUpdate();
			this.comboBoxUserAnimation.Items.Clear();
			this.comboBoxTargetAnimation.Items.Clear();
			this.comboBoxUserAnimation.Items.Add("<None>");
			this.comboBoxTargetAnimation.Items.Add("<None>");
			string name;
			foreach (Animation animation in Project.Data.Animations.Cast<Animation>().Where(animation => animation != null))
			{
			    name = animation.ToString();
			    this.comboBoxUserAnimation.Items.Add(name);
			    this.comboBoxTargetAnimation.Items.Add(name);
			}
			this.comboBoxUserAnimation.EndUpdate();
			this.comboBoxTargetAnimation.EndUpdate();
		}

		private void InitializeCommonEvents()
		{
			ControlHelper.Populate(this.comboBoxCommonEvent, Project.Data.CommonEvents, true);
		}

        private void RefreshParameters()
		{
			foreach (Control ctrl in this.flowPanel.Controls)
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
			if (this._skill.icon_name == "")
			{
				this.pictureBoxIcon.BackgroundImage = null;
				this.textBoxIcon.Text = "<None>";
			}
			else
			{
				this.pictureBoxIcon.BackgroundImage = Cache.Icon(this._skill.icon_name);
				this.textBoxIcon.Text = this._skill.icon_name;
			}
		}

		private void RefreshElements()
		{
			this.checkGroupBoxElements.CheckAll(false);
			foreach (int id in this._skill.element_set)
				this.checkGroupBoxElements.SetItemChecked(id - 1, true);
		}

		private void RefreshStates()
		{
			this.checkedListBoxStates.SetAll(0);
			foreach (int id in this._skill.plus_state_set)
				this.checkedListBoxStates.SetItemIndex(id - 1, 1);
			foreach (int id in this._skill.minus_state_set)
				this.checkedListBoxStates.SetItemIndex(id - 1, 2);
		}

		private void RefreshAnimations()
		{
#warning Fix this after loading of animations is fixed
			return;
			this.comboBoxUserAnimation.SelectedIndex = this._skill.animation1_id;
			this.comboBoxTargetAnimation.SelectedIndex = this._skill.animation2_id;
		}

		private void RefreshMenuSE() 
        {
		    this.textBoxMenuSe.Text = this._skill.menu_se.name != "" ? 
                this._skill.menu_se.ToString() : "";
		}

        private void ListBoxSkillsOnListBoxIndexChanged(object sender, EventArgs e)
		{
			var index = this.dataObjectList.SelectedIndex;
			if (index >= 0)
			{
				this._skill = this.Data[index + 1];
				this.RefreshCurrentObject();
			}
		}

		private void ButtonIconClick(object sender, EventArgs e)
		{
			using (var dialog = new ImageSelectionForm(@"Icons", this._skill.icon_name))
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
				this._skill.description = this.textBoxDescription.Text;
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
				this._skill.scope = this.comboBoxScope.SelectedIndex;
		}

		private void ComboBoxOccasionSelectedIndexChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
				this._skill.occasion = this.comboBoxOccasion.SelectedIndex;
		}

		private void ComboBoxUserAnimationSelectedIndexChanged(object sender, EventArgs e)
		{
			if (SuppressEvents)
				this._skill.animation1_id = this.comboBoxUserAnimation.SelectedIndex;
		}

		private void ComboBoxTargetAnimationSelectedIndexChanged(object sender, EventArgs e)
		{
			if (SuppressEvents)
				this._skill.animation2_id = this.comboBoxTargetAnimation.SelectedIndex;
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
			this._skill.plus_state_set.Remove(id);
			this._skill.minus_state_set.Remove(id);
			if (e.ValueIndex == 1)
				this._skill.plus_state_set.Add(id);
			if (e.ValueIndex == 2)
				this._skill.minus_state_set.Add(id);
		}

		private void ComboBoxCommonEventSelectedIndexChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
				this._skill.common_event_id = this.comboBoxCommonEvent.SelectedIndex;
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
