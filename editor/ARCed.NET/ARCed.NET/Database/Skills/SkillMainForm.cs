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

namespace ARCed.Database.Skills
{
	public partial class SkillMainForm : DatabaseWindow
	{
		#region Private Fields

		private RPG.Skill _skill;

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

		/// <summary>
		/// Default constructor
		/// </summary>
		public SkillMainForm() : base()
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
			DatabaseHelper.Populate(comboBoxCommonEvent, Project.Data.CommonEvents, true);
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
			suppressEvents = false;
		}

		private void RefreshParameters()
		{
			foreach (Control ctrl in flowPanel.Controls)
			{
				if (ctrl is ParamBox)
				{
					ParamBox param = ctrl as ParamBox;
					var property = typeof(RPG.Skill).GetProperty(param.RpgAttribute);
					if (property != null)
						param.Value = (int)property.GetValue(_skill, null);
				}
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
			if (_skill.menu_se.name != "")
				textBoxMenuSe.Text = _skill.menu_se.ToString();
			else
				textBoxMenuSe.Text = "";
		}

		#endregion

		private void listBoxSkills_OnListBoxIndexChanged(object sender, EventArgs e)
		{
			int index = dataObjectList.SelectedIndex;
			if (index >= 0)
			{
				_skill = Data[index + 1];
				RefreshCurrentObject();
			}
		}

		private void buttonIcon_Click(object sender, EventArgs e)
		{
			using (ImageSelectionForm dialog = new ImageSelectionForm(@"Graphics\Icons", _skill.icon_name))
			{
				dialog.TileSelection = false;
				dialog.EnableHueChange = false;
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					_skill.icon_name = dialog.ImageName;
					RefreshIcon();
				}
			}
		}

		private void textBoxName_TextChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
			{
				_skill.name = textBoxName.Text;
				int index = dataObjectList.SelectedIndex;
				dataObjectList.Items[index] = _skill.ToString();
				dataObjectList.Invalidate(dataObjectList.GetItemRectangle(index));
			}
		}

		private void textBoxDescription_TextChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
				_skill.description = textBoxDescription.Text;
		}

		private void checkGroupBoxElements_OnCheckChange(object sender, ItemCheckEventArgs e)
		{
			if (!suppressEvents)
			{
				int id = e.Index + 1;
				if (e.NewValue == CheckState.Checked && !_skill.element_set.Contains(id))
					_skill.element_set.Add(id);
				else if (e.NewValue == CheckState.Unchecked && _skill.element_set.Contains(id))
					_skill.element_set.Remove(id);
			}
		}

		private void checkGroup_FocusLeave(object sender, EventArgs e)
		{
			(sender as ARCed.Controls.CheckGroupBox).SelectedIndex = -1;
		}

		private void comboBoxScope_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (suppressEvents)
				_skill.scope = comboBoxScope.SelectedIndex;
		}

		private void comboBoxOccasion_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
				_skill.occasion = comboBoxOccasion.SelectedIndex;
		}

		private void comboBoxUserAnimation_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (suppressEvents)
				_skill.animation1_id = comboBoxUserAnimation.SelectedIndex;
		}

		private void comboBoxTargetAnimation_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (suppressEvents)
				_skill.animation2_id = comboBoxTargetAnimation.SelectedIndex;
		}

		private void paramBox_OnValueChanged(object sender, ParameterEventArgs e)
		{
			ParamBox paramBox = sender as ParamBox;
			int value = (int)paramBox.Value;
			string propertyName = paramBox.RpgAttribute;
			typeof(RPG.Skill).GetProperty(propertyName).SetValue(_skill, value, null); 
		}

		private void checkedListBoxStates_OnItemChanged(object sender, MultiStateCheckEventArgs e)
		{
			int id = e.Index + 1;
			_skill.plus_state_set.Remove(id);
			_skill.minus_state_set.Remove(id);
			if (e.ValueIndex == 1)
				_skill.plus_state_set.Add(id);
			if (e.ValueIndex == 2)
				_skill.minus_state_set.Add(id);
		}

		private void comboBoxCommonEvent_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
				_skill.common_event_id = comboBoxCommonEvent.SelectedIndex;
		}

		private void noteTextBox_NoteTextChanged(object sender, EventArgs e)
		{
			//if (!suppressEvents)
				//_item.note = noteTextBox.NoteText;
		}
	}
}
