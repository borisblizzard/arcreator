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
		protected override DatabaseObjectListBox DataObjectList { get { return dataObjectList; } }

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
			InitializeComponent();
			InitializeElements();
			InitializeStates();
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
			textBoxName.Text = _armor.name;
			textBoxDescription.Text = _armor.description;
			comboBoxKind.SelectedIndex = _armor.kind;
			comboBoxAutoState.SelectedIndex = _armor.auto_state_id;
			RefreshIcon();
			RefreshParameters();
			RefreshElements();
			RefreshStates();
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
            checkGroupBoxStates.BeginUpdate();
            comboBoxAutoState.BeginUpdate();
            checkGroupBoxStates.Items.Clear();
            comboBoxAutoState.Items.Clear();
            comboBoxAutoState.Items.Add("<None>");
            for (int i = 1; i < Project.Data.States.Count; i++)
            {
                checkGroupBoxStates.Items.Add(Project.Data.States[i].name);
                comboBoxAutoState.Items.Add(Project.Data.States[i].ToString());
            }
            checkGroupBoxStates.EndUpdate();
            comboBoxAutoState.EndUpdate();
        }

		private void RefreshElements()
		{
			checkGroupBoxElements.CheckAll(false);
			foreach (int id in _armor.guard_element_set)
				checkGroupBoxElements.SetItemChecked(id - 1, true);
		}

		private void RefreshStates()
		{
			checkGroupBoxStates.CheckAll(false);
			foreach (int id in _armor.guard_state_set)
				checkGroupBoxStates.SetItemChecked(id - 1, true);
		}

		private void RefreshParameters()
		{
			foreach (Control ctrl in flowPanel.Controls)
			{
				if (ctrl is ParamBox)
				{
					var param = ctrl as ParamBox;
					var property = typeof(Armor).GetProperty(param.RpgAttribute);
					if (property != null)
						param.Value = (int)property.GetValue(_armor, null);
				}
			}
		}

		private void RefreshIcon()
		{
			if (_armor.icon_name == "")
			{
				pictureBoxIcon.BackgroundImage = null;
				textBoxIcon.Text = "<None>";
			}
			else
			{
				pictureBoxIcon.BackgroundImage = Cache.Icon(_armor.icon_name);
				textBoxIcon.Text = _armor.icon_name;
			}
		}

		private void ListBoxArmorsOnListBoxIndexChanged(object sender, EventArgs e)
		{
			int index = dataObjectList.SelectedIndex;
			if (index >= 0)
			{
				_armor = Data[index + 1];
				RefreshCurrentObject();
			}
		}

		private void TextBoxNameTextChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
			{
				_armor.name = textBoxName.Text;
				int index = dataObjectList.SelectedIndex;
				dataObjectList.Items[index] = _armor.ToString();
				dataObjectList.Invalidate(dataObjectList.GetItemRectangle(index));
			}
		}

		private void TextBoxDescriptionTextChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
				_armor.description = textBoxDescription.Text;
		}

		private void ButtonIconClick(object sender, EventArgs e)
		{
			using (var dialog = new ImageSelectionForm(@"Icons", _armor.icon_name))
			{
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					_armor.icon_name = dialog.ImageName;
					RefreshIcon();
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
				_armor.kind = comboBoxKind.SelectedIndex;
		}

		private void ComboBoxAutoStateSelectedIndexChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
				_armor.auto_state_id = comboBoxAutoState.SelectedIndex;
		}

        #endregion
	}
}
