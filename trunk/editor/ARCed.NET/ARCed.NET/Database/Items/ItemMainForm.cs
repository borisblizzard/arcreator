using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using ARCed.Dialogs;
using ARCed.Controls;
using ARCed.UI;
using ARCed.Helpers;

namespace ARCed.Database.Items
{
	public partial class ItemMainForm : DatabaseWindow
	{
		#region Private Fields

		private RPG.Item _item;

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
		public override List<dynamic> Data { get { return Project.Data.Items; } }

		#endregion

		/// <summary>
		/// Default constructor
		/// </summary>
		public ItemMainForm() : base()
		{
			InitializeComponent();
			InitializeElements();
			InitializeStates();
			InitializeAnimations();
			InitializeCommonEvents();
			RefreshObjectList();
			dataObjectList.SelectedIndex = 0;
		}

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
			foreach (RPG.Animation animation in Project.Data.Animations)
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

		private void InitializeCommonEvents()
		{
			comboBoxCommonEvent.BeginUpdate();
			comboBoxCommonEvent.Items.Clear();
			comboBoxCommonEvent.Items.Add("<None>");
			foreach (RPG.CommonEvent commonEvent in Project.Data.CommonEvents)
			{
				if (commonEvent != null)
					comboBoxCommonEvent.Items.Add(commonEvent.ToString());
			}
			comboBoxCommonEvent.EndUpdate();
		}

		#endregion

		#region Refresh Methods

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

		public override void RefreshCurrentObject()
		{
			suppressEvents = true;
			RefreshIcon();
			textBoxName.Text = _item.name;
			textBoxDescription.Text = _item.description;
			RefreshElements();
			RefreshStates();
			comboBoxScope.SelectedIndex = _item.scope;
			comboBoxOccasion.SelectedIndex = _item.occasion;
			comboBoxCommonEvent.SelectedIndex = _item.common_event_id;
			RefreshMenuSE();
			RefreshAnimations();
			RefreshParameters();
			//noteTextBox.NoteText = _item.note;
			suppressEvents = false;
		}

		private void RefreshParameters()
		{
			foreach (Control ctrl in flowPanel.Controls)
			{
				if (ctrl is ParamBox)
				{
					ParamBox param = ctrl as ParamBox;
					var property = typeof(RPG.Item).GetProperty(param.RpgAttribute);
					if (property != null)
						param.Value = (int)property.GetValue(_item, null);	
				}
			}
			comboBoxConsumable.SelectedIndex = _item.consumable ? 0 : 1;
			comboBoxParameter.SelectedIndex = _item.parameter_type;
		}

		private void RefreshIcon()
		{
			if (_item.icon_name == "")
			{
				pictureBoxIcon.BackgroundImage = null;
				textBoxIcon.Text = "<None>";
			}
			else
			{
				pictureBoxIcon.BackgroundImage = Cache.Icon(_item.icon_name);
				textBoxIcon.Text = _item.icon_name;
			}
		}

		private void RefreshElements()
		{
			checkGroupBoxElements.CheckAll(false);
			foreach (int id in _item.element_set)
				checkGroupBoxElements.SetItemChecked(id - 1, true);
		}

		private void RefreshStates()
		{
			checkedListBoxStates.SetAll(0);
			foreach (int id in _item.plus_state_set)
				checkedListBoxStates.SetItemIndex(id - 1, 1);
			foreach (int id in _item.minus_state_set)
				checkedListBoxStates.SetItemIndex(id - 1, 2);
		}

		private void RefreshAnimations()
		{
#warning Fix this after loading of animations is fixed
			return;
			comboBoxUserAnimation.SelectedIndex = _item.animation1_id;
			comboBoxTargetAnimation.SelectedIndex = _item.animation2_id;
		}

		private void RefreshMenuSE()
		{
			if (_item.menu_se.name != "")
				textBoxMenuSe.Text = _item.menu_se.ToString();
			else
				textBoxMenuSe.Text = "";
		}

		#endregion

		private void listBoxItems_OnListBoxIndexChanged(object sender, EventArgs e)
		{
			int index = dataObjectList.SelectedIndex;
			if (index >= 0)
			{
				_item = Data[index + 1];
				RefreshCurrentObject();
			}
		}

		private void buttonIcon_Click(object sender, EventArgs e)
		{
			using (ImageSelectionForm dialog = new ImageSelectionForm(@"Graphics\Icons", _item.icon_name))
			{
				dialog.SelectionEnabled = false;
				dialog.HueEnabled = false;
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					_item.icon_name = dialog.ImageName;
					RefreshIcon();
				}
			}
		}

		private void textBoxName_TextChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
			{
				_item.name = textBoxName.Text;
				int index = dataObjectList.SelectedIndex;
				dataObjectList.Items[index] = _item.ToString();
				dataObjectList.Invalidate(dataObjectList.GetItemRectangle(index));
			}
		}

		private void textBoxDescription_TextChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
				_item.description = textBoxDescription.Text;
		}

		private void checkGroupBoxElements_OnCheckChange(object sender, ItemCheckEventArgs e)
		{
			if (!suppressEvents)
			{
				int id = e.Index + 1;
				if (e.NewValue == CheckState.Checked && !_item.element_set.Contains(id))
					_item.element_set.Add(id);
				else if (e.NewValue == CheckState.Unchecked && _item.element_set.Contains(id))
					_item.element_set.Remove(id);
			}
		}

		private void checkGroup_FocusLeave(object sender, EventArgs e)
		{
			(sender as ARCed.Controls.CheckGroupBox).SelectedIndex = -1;
		}

		private void comboBoxScope_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
				_item.scope = comboBoxScope.SelectedIndex;
		}

		private void comboBoxOccasion_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
				_item.occasion = comboBoxOccasion.SelectedIndex;
		}

		private void comboBoxUserAnimation_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
				_item.animation1_id = comboBoxUserAnimation.SelectedIndex;
		}

		private void comboBoxTargetAnimation_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
				_item.animation2_id = comboBoxTargetAnimation.SelectedIndex;
		}

		private void paramBox_OnValueChanged(object sender, ParameterEventArgs e)
		{
			if (!suppressEvents)
			{
				ParamBox paramBox = sender as ParamBox;
				int value = (int)paramBox.Value;
				string propertyName = paramBox.RpgAttribute;
				typeof(RPG.Item).GetProperty(propertyName).SetValue(_item, value, null);
			}
		}

		private void checkedListBoxStates_OnItemChanged(object sender, MultiStateCheckEventArgs e)
		{
			if (!suppressEvents)
			{
				int id = e.Index + 1;
				_item.plus_state_set.Remove(id);
				_item.minus_state_set.Remove(id);
				if (e.ValueIndex == 1)
					_item.plus_state_set.Add(id);
				if (e.ValueIndex == 2)
					_item.minus_state_set.Add(id);
			}
		}

		private void comboBoxCommonEvent_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
				_item.common_event_id = comboBoxCommonEvent.SelectedIndex;
		}

		private void noteTextBox_NoteTextChanged(object sender, EventArgs e)
		{
			//if (!suppressEvents)
			//_item.note = noteTextBox.NoteText;
		}

		private void comboBoxConsumable_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
				_item.consumable = (comboBoxConsumable.SelectedIndex == 0);
		}

		private void comboBoxParameter_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
				_item.parameter_type = comboBoxParameter.SelectedIndex;
			paramBoxParamInc.Enabled = _item.parameter_type > 0;
		}

		private void textBoxMenuSe_OnButtonClick(object sender, EventArgs e)
		{

		}
	}
}
