#region Using Directives

using System;
using System.Collections.Generic;
using System.Windows.Forms;
using ARCed.Controls;
using ARCed.Dialogs;
using ARCed.Helpers;
using RPG;

#endregion

namespace ARCed.Database.Armors
{
    /// <summary>
    /// Main form for configuring Project <see cref="RPG.Armor"/> data.
    /// </summary>
	public sealed partial class ArmorMainForm : DatabaseWindow
	{
		#region Private Fields

		private Armor _armor;

		#endregion

		#region Protected Properties

		/// <summary>
		/// Gets the object list control of this database panel.
		/// </summary>
		protected override DatabaseObjectListBox DataObjectList { get { return this.dataObjectList; } }

        /// <summary>
        /// Gets the data associated with this panel.
        /// </summary>
        public override List<dynamic> Data { get { return Project.Data.Armors; } }

		#endregion

		#region Constructors

		/// <summary>
		/// Default constructor
		/// </summary>
		public ArmorMainForm()
		{
			this.InitializeComponent();
			this.InitializeElements();
			this.InitializeStates();
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
			if (type.HasFlag(RefreshType.EquipKinds))
			{

			}
		}

        /// <summary>
        /// Refreshes the form to display data for the currently selected <see cref="RPG.Armor"/>.
        /// </summary>
		public override void RefreshCurrentObject()
		{
			SuppressEvents = true;
			this.textBoxName.Text = this._armor.name;
			this.textBoxDescription.Text = this._armor.description;
			this.comboBoxKind.SelectedIndex = this._armor.kind;
			this.comboBoxAutoState.SelectedIndex = this._armor.auto_state_id;
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
            this.checkGroupBoxStates.BeginUpdate();
            this.comboBoxAutoState.BeginUpdate();
            this.checkGroupBoxStates.Items.Clear();
            this.comboBoxAutoState.Items.Clear();
            this.comboBoxAutoState.Items.Add("<None>");
            for (int i = 1; i < Project.Data.States.Count; i++)
            {
                this.checkGroupBoxStates.Items.Add(Project.Data.States[i].name);
                this.comboBoxAutoState.Items.Add(Project.Data.States[i].ToString());
            }
            this.checkGroupBoxStates.EndUpdate();
            this.comboBoxAutoState.EndUpdate();
        }

		private void RefreshElements()
		{
			this.checkGroupBoxElements.CheckAll(false);
			foreach (int id in this._armor.guard_element_set)
				this.checkGroupBoxElements.SetItemChecked(id - 1, true);
		}

		private void RefreshStates()
		{
			this.checkGroupBoxStates.CheckAll(false);
			foreach (int id in this._armor.guard_state_set)
				this.checkGroupBoxStates.SetItemChecked(id - 1, true);
		}

		private void RefreshParameters()
		{
			foreach (Control ctrl in this.flowPanel.Controls)
			{
				if (ctrl is ParamBox)
				{
					var param = ctrl as ParamBox;
					var property = typeof(Armor).GetProperty(param.RpgAttribute);
					if (property != null)
						param.Value = (int)property.GetValue(this._armor, null);
				}
			}
		}

		private void RefreshIcon()
		{
			if (this._armor.icon_name == "")
			{
				this.pictureBoxIcon.BackgroundImage = null;
				this.textBoxIcon.Text = "<None>";
			}
			else
			{
				this.pictureBoxIcon.BackgroundImage = Cache.Icon(this._armor.icon_name);
				this.textBoxIcon.Text = this._armor.icon_name;
			}
		}

		private void ListBoxArmorsOnListBoxIndexChanged(object sender, EventArgs e)
		{
			int index = this.dataObjectList.SelectedIndex;
			if (index >= 0)
			{
				this._armor = this.Data[index + 1];
				this.RefreshCurrentObject();
			}
		}

		private void TextBoxNameTextChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
			{
				this._armor.name = this.textBoxName.Text;
				int index = this.dataObjectList.SelectedIndex;
				this.dataObjectList.Items[index] = this._armor.ToString();
				this.dataObjectList.Invalidate(this.dataObjectList.GetItemRectangle(index));
			}
		}

		private void TextBoxDescriptionTextChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
				this._armor.description = this.textBoxDescription.Text;
		}

		private void ButtonIconClick(object sender, EventArgs e)
		{
			using (var dialog = new ImageSelectionForm(@"Icons", this._armor.icon_name))
			{
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					this._armor.icon_name = dialog.ImageName;
					this.RefreshIcon();
				}
			}
		}

		private void ParamBoxOnValueChanged(object sender, ParameterEventArgs e)
		{
		    if (SuppressEvents) return;
		    var paramBox = sender as ParamBox;
		    var value = (int)paramBox.Value;
		    string propertyName = paramBox.RpgAttribute;
		    typeof(Armor).GetProperty(propertyName).SetValue(this._armor, value, null);
		}

		private void CheckGroupBoxElementsOnCheckChange(object sender, ItemCheckEventArgs e)
		{
		    if (SuppressEvents) return;
		    int id = e.Index + 1;
		    if (e.NewValue == CheckState.Checked && !this._armor.guard_element_set.Contains(id))
		        this._armor.guard_element_set.Add(id);
		    else if (e.NewValue == CheckState.Unchecked && this._armor.guard_element_set.Contains(id))
		        this._armor.guard_element_set.Remove(id);
		}

		private void CheckGroupBoxStatesOnCheckChange(object sender, ItemCheckEventArgs e)
		{
		    if (SuppressEvents) return;
		    int id = e.Index + 1;
		    if (e.NewValue == CheckState.Checked && !this._armor.guard_state_set.Contains(id))
		        this._armor.guard_state_set.Add(id);
		    else if (e.NewValue == CheckState.Unchecked && this._armor.guard_state_set.Contains(id))
		        this._armor.guard_state_set.Remove(id);
		}

		private void NoteTextBoxNoteTextChanged(object sender, EventArgs e)
		{
			//if (!suppressEvents)
			//_armor.note = noteTextBox.NoteText;
		}

		private void ComboBoxKindSelectedIndexChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
				this._armor.kind = this.comboBoxKind.SelectedIndex;
		}

		private void ComboBoxAutoStateSelectedIndexChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
				this._armor.auto_state_id = this.comboBoxAutoState.SelectedIndex;
		}

        #endregion
	}
}
