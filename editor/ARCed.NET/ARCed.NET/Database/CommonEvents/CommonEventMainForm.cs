using System;
using System.Collections.Generic;
using ARCed.Controls;

namespace ARCed.Database.CommonEvents
{
	public sealed partial class CommonEventMainForm : DatabaseWindow
	{
		#region Private Fields

		private RPG.CommonEvent _event;

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
		public override List<dynamic> Data { get { return Project.Data.CommonEvents; } }

		#endregion

		#region Constructor

		public CommonEventMainForm()
		{
			InitializeComponent();
			RefreshSwitches();
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

		}

		/// <summary>
		/// Refreshes the form to display data for the currently selected <see cref="RPG.Item"/>.
		/// </summary>
		public override void RefreshCurrentObject()
		{
			SuppressEvents = true;
			textBoxName.Text = _event.name;
			comboBoxTrigger.SelectedIndex = _event.trigger;
			comboBoxCondition.SelectedIndex = _event.switch_id;
			eventTextBox.Parse(_event.list);
			//noteTextBox.NoteText = _event.note;
			SuppressEvents = false;
		}

		#endregion

		private void RefreshSwitches()
		{
			int index = comboBoxCondition.SelectedIndex;
			comboBoxCondition.BeginUpdate();
			comboBoxCondition.Items.Clear();
			comboBoxCondition.Items.Add("<None>");
			foreach (var obj in Project.Switches)
				if (obj != null)
					comboBoxCondition.Items.Add(obj.ToString());
			comboBoxCondition.EndUpdate();
			if (index >= comboBoxCondition.Items.Count)
				comboBoxCondition.SelectedIndex = index.Clamp(0, comboBoxCondition.Items.Count - 1);
		}

		private void DataObjectListIndexChanged(object sender, EventArgs e)
		{
			int index = this.dataObjectList.SelectedIndex;
			if (index < 0) return;
			this._event = this.Data[index + 1];
			this.RefreshCurrentObject();
		}

		private void ComboBoxTriggerSelectedIndexChanged(object sender, EventArgs e)
		{
			comboBoxCondition.Enabled = comboBoxTrigger.SelectedIndex > 0;
			if (SuppressEvents) return;
			_event.trigger = comboBoxTrigger.SelectedIndex;
		}

		private void ComboBoxConditionSelectedIndexChanged(object sender, EventArgs e)
		{
			if (SuppressEvents) return;
			_event.switch_id = comboBoxCondition.SelectedIndex;
		}
	}
}
