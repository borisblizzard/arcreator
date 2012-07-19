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

namespace ARCed.Database.Weapons
{
    /// <summary>
    /// Main form for configuring Project <see cref="RPG.Weapon"/> data.
    /// </summary>
	public sealed partial class WeaponMainForm : DatabaseWindow
	{

		#region Private Fields

		private Weapon _weapon;

		#endregion

        #region Protected Properties

        protected override DatabaseObjectListBox DataObjectList { get { return this.dataObjectList; } }

        #endregion

        #region Public Properties

        public override List<dynamic> Data { get { return Project.Data.Weapons; } }

        #endregion

        #region Constructors

        /// <summary>
		/// Default constructor
		/// </summary>
		public WeaponMainForm()
		{
			this.InitializeComponent();
			this.InitializeElements();
			this.InitializeStates();
			this.InitializeAnimations();
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
			if (type.HasFlag(RefreshType.Enemies))
			{

			}
			if (type.HasFlag(RefreshType.Switches))
			{

			}
		}

        /// <summary>
        /// Refreshes the form to display data for the currently selected <see cref="RPG.Weapon"/>.
        /// </summary>
		public override void RefreshCurrentObject()
		{
			SuppressEvents = true;
			this.textBoxName.Text = this._weapon.name;
			this.textBoxDescription.Text = this._weapon.description;
			//comboBoxUserAnimation.SelectedIndex = _armor.animation1_id;
			//comboBoxTargetAnimation.SelectedIndex = _armor.animation2_id;
			this.RefreshIcon();
			this.RefreshParameters();
			this.RefreshElements();
			this.RefreshStates();
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

        private void RefreshElements()
		{
			this.checkGroupBoxElements.CheckAll(false);
			foreach (int id in this._weapon.element_set)
				this.checkGroupBoxElements.SetItemChecked(id - 1, true);
		}

		private void RefreshStates()
		{
			this.checkedListBoxStates.SetAll(0);
			foreach (int id in this._weapon.plus_state_set)
				this.checkedListBoxStates.SetItemIndex(id - 1, 1);
			foreach (int id in this._weapon.minus_state_set)
				this.checkedListBoxStates.SetItemIndex(id - 1, 2);
		}

		private void RefreshParameters()
		{
			foreach (Control ctrl in this.flowPanel.Controls)
			{
			    if (!(ctrl is ParamBox)) continue;
			    var param = ctrl as ParamBox;
			    var property = typeof(Weapon).GetProperty(param.RpgAttribute);
			    if (property != null)
			        param.Value = (int)property.GetValue(this._weapon, null);
			}
		}

		private void RefreshIcon()
		{
			if (this._weapon.icon_name == "")
			{
				this.pictureBoxIcon.BackgroundImage = null;
				this.textBoxIcon.Text = "<None>";
			}
			else
			{
				this.pictureBoxIcon.BackgroundImage = Cache.Icon(this._weapon.icon_name);
				this.textBoxIcon.Text = this._weapon.icon_name;
			}
		}

		private void ListBoxWeaponsOnListBoxIndexChanged(object sender, EventArgs e)
		{
			var index = this.dataObjectList.SelectedIndex;
		    if (index < 0) return;
		    this._weapon = this.Data[index + 1];
		    this.RefreshCurrentObject();
		}

		private void TextBoxNameTextChanged(object sender, EventArgs e)
		{
		    if (SuppressEvents) return;
		    this._weapon.name = this.textBoxName.Text;
		    var index = this.dataObjectList.SelectedIndex;
		    this.dataObjectList.Items[index] = this._weapon.ToString();
		    this.dataObjectList.Invalidate(this.dataObjectList.GetItemRectangle(index));
		}

		private void TextBoxDescriptionTextChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
				this._weapon.description = this.textBoxDescription.Text;
		}

		private void ButtonIconClick(object sender, EventArgs e)
		{
			using (var dialog = new ImageSelectionForm(@"Icons", this._weapon.icon_name))
			{
			    if (dialog.ShowDialog(this) != DialogResult.OK) return;
			    this._weapon.icon_name = dialog.ImageName;
			    this.RefreshIcon();
			}
		}

		private void ComboBoxUserAnimationSelectedIndexChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
				this._weapon.animation1_id = this.comboBoxUserAnimation.SelectedIndex;
		}

		private void ComboBoxTargetAnimationSelectedIndexChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
				this._weapon.animation2_id = this.comboBoxTargetAnimation.SelectedIndex;
		}

		private void ParamBoxOnValueChanged(object sender, ParameterEventArgs e)
		{
		    if (SuppressEvents) return;
		    var paramBox = sender as ParamBox;
		    if (paramBox != null)
		    {
		        var value = (int)paramBox.Value;
		        var propertyName = paramBox.RpgAttribute;
		        typeof(Weapon).GetProperty(propertyName).SetValue(this._weapon, value, null);
		    }
		}

		private void CheckGroupBoxElementsOnCheckChange(object sender, ItemCheckEventArgs e)
		{
		    if (SuppressEvents) return;
		    var id = e.Index + 1;
		    if (e.NewValue == CheckState.Checked && !this._weapon.element_set.Contains(id))
		        this._weapon.element_set.Add(id);
		    else if (e.NewValue == CheckState.Unchecked && this._weapon.element_set.Contains(id))
		        this._weapon.element_set.Remove(id);
		}

		private void CheckedListBoxStatesOnItemChanged(object sender, MultiStateCheckEventArgs e)
		{
		    if (SuppressEvents) return;
		    var id = e.Index + 1;
		    this._weapon.plus_state_set.Remove(id);
		    this._weapon.minus_state_set.Remove(id);
		    if (e.ValueIndex == 1)
		        this._weapon.plus_state_set.Add(id);
		    if (e.ValueIndex == 2)
		        this._weapon.minus_state_set.Add(id);
		}

		private void NoteTextBoxNoteTextChanged(object sender, EventArgs e)
		{
			//if (!suppressEvents)
				//_armor.note = noteTextBox.NoteText;
        }

        #endregion
    }
}
