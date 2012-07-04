using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Controls;
using ARCed.Dialogs;
using ARCed.Helpers;

namespace ARCed.Database.Enemies
{
	/// <summary>
	/// Database window for editing RPG.Enemy data
	/// </summary>
	public partial class EnemyMainForm : DatabaseWindow
	{
		#region Private Fields

		private static string[] _actions = new[] { "Attack", "Defend", "Escape", "Do Nothing" };
		private RPG.Enemy _enemy;
		private ListViewColumnSorter _listViewSorter;

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
		public override List<dynamic> Data { get { return Project.Data.Enemies; } }

		#endregion

		#region Constructor

		public EnemyMainForm() : base()
		{
			InitializeComponent();
			InitializeElements();
			InitializeStates();
			RefreshObjectList();
			_listViewSorter = new ListViewColumnSorter();
			listViewActions.ListViewItemSorter = _listViewSorter;
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
			if (type.HasFlag(RefreshType.Skills))
			{

			}
			if (type.HasFlag(RefreshType.Parameters))
			{

			}
			if (type.HasFlag(RefreshType.Items))
			{

			}
			if (type.HasFlag(RefreshType.Weapons))
			{

			}
			if (type.HasFlag(RefreshType.Armors))
			{

			}
			if (type.HasFlag(RefreshType.Switches))
			{

			}
		}

		public override void RefreshCurrentObject()
		{
			suppressEvents = true;
			textBoxName.Text = _enemy.name;
			RefreshParameters();
			RefreshImages();
			numericUpDownExp.Value = _enemy.exp;
			numericUpDownGold.Value = _enemy.gold;
			RefreshTreasure();
			RefreshElements();
			RefreshStates();
			RefreshActions();
			suppressEvents = false;
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

		private void RefreshActions()
		{
			listViewActions.BeginUpdate();
			listViewActions.Items.Clear();
			foreach (RPG.Enemy.Action action in _enemy.actions)
				listViewActions.Items.Add(MakeActionItem(action));
			listViewActions.EndUpdate();
		}

		private ListViewItem MakeActionItem(RPG.Enemy.Action action)
		{
			List<string> conditions = new List<string>();
			bool turnCondition = !(action.condition_turn_a == 0 && action.condition_turn_b == 1);
			if (turnCondition)
				conditions.Add(String.Format("Turn {0} + {1}X",
					action.condition_turn_a, action.condition_turn_b));
			if (action.condition_hp != 100)
				conditions.Add(String.Format("{0}% HP or below", action.condition_hp));
			if (action.condition_level != 1)
				conditions.Add(String.Format("Level {0} or above", action.condition_level));
			if (action.condition_switch_id != 0)
				conditions.Add(String.Format("Switch [{0:d4}: {1}] is ON",
					action.condition_switch_id, Project.Data.System.switches[action.condition_switch_id]));
			if (conditions.Count == 0)
				conditions.Add("<None>");
			string condition = String.Join(", ", conditions);
			string cmd;
			if (action.kind == 0)
				cmd = _actions[action.basic];
			else
				cmd = Project.Data.Skills[action.skill_id].name;
			return new ListViewItem(new string[] { cmd, condition, action.rating.ToString() });
		}

		private void RefreshElements()
		{
			for (int i = 1; i < Project.Data.System.elements.Count; i++)
				checkedListElements.SetItemIndex(i - 1, _enemy.element_ranks[i]);
		}

		private void RefreshStates()
		{
			for (int i = 1; i < Project.Data.States.Count; i++)
				checkedListStates.SetItemIndex(i - 1, _enemy.state_ranks[i]);
		}

		private void RefreshTreasure()
		{
			RPG.IRpgObject obj;
			if (_enemy.item_id > 0) obj = Project.Data.Items[_enemy.item_id];
			else if (_enemy.weapon_id > 0) obj = Project.Data.Weapons[_enemy.weapon_id];
			else if (_enemy.armor_id > 0) obj = Project.Data.Armors[_enemy.armor_id];
			else
			{
				textBoxTreasure.Text = "<None>";
				return;
			}
			textBoxTreasure.Text = String.Format("{0}% {1}", _enemy.treasure_prob, obj.name);
		}

		private void RefreshParameters()
		{
			foreach (Control ctrl in flowPanel.Controls)
			{
				if (ctrl is ParamBox)
				{
					ParamBox param = ctrl as ParamBox;
					var property = typeof(RPG.Enemy).GetProperty(param.RpgAttribute);
					if (property != null)
						param.Value = (int)property.GetValue(_enemy, null);
				}
			}
		}

		private void RefreshImages()
		{
			pictureBattler.Image = Cache.Battler(_enemy.battler_name, _enemy.battler_hue);
		}

		private void paramBox_OnValueChanged(object sender, ParameterEventArgs e)
		{
			if (!suppressEvents)
			{
				ParamBox paramBox = sender as ParamBox;
				int value = (int)paramBox.Value;
				string propertyName = paramBox.RpgAttribute;
				typeof(RPG.Enemy).GetProperty(propertyName).SetValue(_enemy, value, null);
			}
		}

		private void dataObjectList_OnListBoxIndexChanged(object sender, EventArgs e)
		{
			int index = dataObjectList.SelectedIndex;
			if (index >= 0)
			{
				_enemy = Data[index + 1];
				RefreshCurrentObject();
			}
		}

		private void textBoxName_TextChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
			{
				_enemy.name = textBoxName.Text;
				int index = dataObjectList.SelectedIndex;
				dataObjectList.Items[index] = _enemy.ToString();
				dataObjectList.Invalidate(dataObjectList.GetItemRectangle(index));
			}
		}

		private void checkedListElements_OnItemChanged(object sender, MultiStateCheckEventArgs e)
		{
			if (!suppressEvents)
				_enemy.element_ranks[e.Index + 1] = (sender as MultiStateCheckbox).SelectedState;
		}

		private void checkedListStates_OnItemChanged(object sender, MultiStateCheckEventArgs e)
		{
			if (!suppressEvents)
				_enemy.state_ranks[e.Index + 1] = (sender as MultiStateCheckbox).SelectedState;
		}

		private void listViewSkills_ColumnClick(object sender, ColumnClickEventArgs e)
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

		private void noteTextBox_NoteTextChanged(object sender, EventArgs e)
		{
			//if (suppressEvents)
				//_enemy.note = noteTextBox.NoteText;
		}

		private void buttonAddAction_Click(object sender, EventArgs e)
		{
			using (EditActionDialog dialog = new EditActionDialog())
			{
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					_enemy.actions.Add(dialog.EnemyAction);
					RefreshActions();
				}
			}
		}

		private void buttonRemoveAction_Click(object sender, EventArgs e)
		{
			int index = GetActionIndex();
			if (_enemy != null && index >= 0)
			{
				_enemy.actions.RemoveAt(index);
				RefreshActions();
				listViewActions.Focus();
				listViewActions_SelectedIndexChanged(sender, e);
			}
			if (listViewActions.Items.Count > 0)
				listViewActions.Items[index.Clamp(0, listViewActions.Items.Count - 1)].Selected = true;
		}

		private int GetActionIndex()
		{
			if (listViewActions.SelectedIndices.Count > 0)
				return listViewActions.SelectedIndices[0];
			return -1;
		}

		private void buttonEditAction_Click(object sender, EventArgs e)
		{
			int index = GetActionIndex();
			using (EditActionDialog dialog = new EditActionDialog())
			{
				dialog.EnemyAction = _enemy.actions[index];
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					_enemy.actions[index] = dialog.EnemyAction;
					RefreshActions();
				}
			}
		}

		private void listViewActions_DoubleClick(object sender, EventArgs e)
		{
			Point pnt = listViewActions.PointToClient(MousePosition);
			ListViewHitTestInfo info = listViewActions.HitTest(pnt);
			if (info.Item != null)
				buttonEditAction_Click(sender, e);
		}

		private void listViewActions_SelectedIndexChanged(object sender, EventArgs e)
		{
			bool enable = listViewActions.SelectedItems.Count > 0;
			buttonEditAction.Enabled = enable;
			buttonRemoveAction.Enabled = enable;
			contextButtonActionEdit.Enabled = enable;
			contextButtonActionRemove.Enabled = enable;
		}

		private void buttonTreasure_Click(object sender, EventArgs e)
		{
			using (TreasureSelectDialog dialog = new TreasureSelectDialog())
			{
				dialog.SetTreasure(_enemy.treasure_prob, _enemy.item_id,
					_enemy.weapon_id, _enemy.armor_id);
				if (dialog.ShowDialog() == DialogResult.OK)
				{
					_enemy.treasure_prob = dialog.TreasureProbablity;
					_enemy.item_id = _enemy.weapon_id = _enemy.armor_id = 0;
					if (dialog.ItemId > 0)
						_enemy.item_id = dialog.ItemId;
					else if (dialog.WeaponId > 0)
						_enemy.weapon_id = dialog.WeaponId;
					else if (dialog.ArmorId > 0)
						_enemy.armor_id = dialog.ArmorId; ;
					RefreshTreasure();
				}
			}
		}

		private void pictureBattler_DoubleClick(object sender, EventArgs e)
		{
			using (ImageSelectionForm dialog =
				new ImageSelectionForm(@"Graphics\Battlers", _enemy.battler_name, _enemy.battler_hue))
			{
				dialog.SelectionEnabled = false;
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					_enemy.battler_name = dialog.ImageName;
					_enemy.battler_hue = dialog.Hue;
					pictureBattler.Image =
						Cache.Battler(_enemy.battler_name, _enemy.battler_hue);
				}
			}
		}

		private void contextMenuImages_Opening(object sender, CancelEventArgs e)
		{
			PictureBoxSizeMode mode =
				(contextMenuImages.SourceControl as PictureBox).SizeMode;
			contextImageNormal.Checked = mode == PictureBoxSizeMode.Normal;
			contextImageCenter.Checked = mode == PictureBoxSizeMode.CenterImage;
			contextImageStretch.Checked = mode == PictureBoxSizeMode.StretchImage;
			contextImageZoom.Checked = mode == PictureBoxSizeMode.Zoom;
		}

		private void contextImagesSizeMode_Clicked(object sender, EventArgs e)
		{
			int num = Convert.ToInt32((sender as ToolStripMenuItem).Tag);
			PictureBoxSizeMode mode = (PictureBoxSizeMode)num;
			(contextMenuImages.SourceControl as PictureBox).SizeMode = mode;
		}

		#endregion
	}
}
