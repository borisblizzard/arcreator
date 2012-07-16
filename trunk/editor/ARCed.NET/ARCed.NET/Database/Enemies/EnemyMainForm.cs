#region Using Directives

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Globalization;
using System.Windows.Forms;
using ARCed.Controls;
using ARCed.Dialogs;
using ARCed.Helpers;
using RPG;

#endregion

namespace ARCed.Database.Enemies
{
    /// <summary>
    /// Main form for configuring Project <see cref="RPG.Enemy"/> data.
    /// </summary>
	public sealed partial class EnemyMainForm : DatabaseWindow
	{
		#region Private Fields

		private static readonly string[] _actions = new[] { "Attack", "Defend", "Escape", "Do Nothing" };
		private Enemy _enemy;
		private readonly ListViewColumnSorter _listViewSorter;

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

        /// <summary>
        /// Default constructor
        /// </summary>
		public EnemyMainForm()
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

        /// <summary>
        /// Refreshes the form to display data for the currently selected <see cref="RPG.Enemy"/>.
        /// </summary>
		public override void RefreshCurrentObject()
		{
			SuppressEvents = true;
			textBoxName.Text = _enemy.name;
			RefreshParameters();
			RefreshImages();
			numericUpDownExp.Value = _enemy.exp;
			numericUpDownGold.Value = _enemy.gold;
			RefreshTreasure();
			RefreshElements();
			RefreshStates();
			RefreshActions();
			SuppressEvents = false;
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
			foreach (Enemy.Action action in _enemy.actions)
				listViewActions.Items.Add(MakeActionItem(action));
			listViewActions.EndUpdate();
		}

		private static ListViewItem MakeActionItem(Enemy.Action action)
		{
			var conditions = new List<string>();
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
			string cmd = action.kind == 0 ? _actions[action.basic] : 
                Project.Data.Skills[action.skill_id].name;
			return new ListViewItem(new[] { cmd, condition, 
                action.rating.ToString(CultureInfo.InvariantCulture) });
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
			IRpgObject obj;
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
			    if (!(ctrl is ParamBox)) continue;
			    var param = ctrl as ParamBox;
			    var property = typeof(Enemy).GetProperty(param.RpgAttribute);
			    if (property != null)
			        param.Value = (int)property.GetValue(this._enemy, null);
			}
		}

		private void RefreshImages()
		{
			pictureBattler.Image = Cache.Battler(_enemy.battler_name, _enemy.battler_hue);
		}

		private void ParamBoxOnValueChanged(object sender, ParameterEventArgs e)
		{
		    if (SuppressEvents) return;
		    var paramBox = sender as ParamBox;
		    if (paramBox != null)
		    {
		        var value = (int)paramBox.Value;
		        var propertyName = paramBox.RpgAttribute;
		        typeof(Enemy).GetProperty(propertyName).SetValue(this._enemy, value, null);
		    }
		}

		private void DataObjectListOnListBoxIndexChanged(object sender, EventArgs e)
		{
			int index = dataObjectList.SelectedIndex;
			if (index >= 0)
			{
				_enemy = Data[index + 1];
				RefreshCurrentObject();
			}
		}

		private void TextBoxNameTextChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
			{
				_enemy.name = textBoxName.Text;
				int index = dataObjectList.SelectedIndex;
				dataObjectList.Items[index] = _enemy.ToString();
				dataObjectList.Invalidate(dataObjectList.GetItemRectangle(index));
			}
		}

		private void CheckedListElementsOnItemChanged(object sender, MultiStateCheckEventArgs e)
		{
		    if (SuppressEvents) return;
		    var multiStateCheckbox = sender as MultiStateCheckbox;
		    if (multiStateCheckbox != null)
		        this._enemy.element_ranks[e.Index + 1] = multiStateCheckbox.SelectedState;
		}

		private void CheckedListStatesOnItemChanged(object sender, MultiStateCheckEventArgs e)
		{
		    if (SuppressEvents) return;
		    var multiStateCheckbox = sender as MultiStateCheckbox;
		    if (multiStateCheckbox != null)
		        this._enemy.state_ranks[e.Index + 1] = multiStateCheckbox.SelectedState;
		}

		private void ListViewSkillsColumnClick(object sender, ColumnClickEventArgs e)
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

		private void NoteTextBoxNoteTextChanged(object sender, EventArgs e)
		{
			//if (suppressEvents)
				//_enemy.note = noteTextBox.NoteText;
		}

		private void ButtonAddActionClick(object sender, EventArgs e)
		{
			using (var dialog = new EditActionDialog())
			{
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					_enemy.actions.Add(dialog.EnemyAction);
					RefreshActions();
				}
			}
		}

		private void ButtonRemoveActionClick(object sender, EventArgs e)
		{
			int index = GetActionIndex();
			if (_enemy != null && index >= 0)
			{
				_enemy.actions.RemoveAt(index);
				RefreshActions();
				listViewActions.Focus();
				this.ListViewActionsSelectedIndexChanged(sender, e);
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

		private void ButtonEditActionClick(object sender, EventArgs e)
		{
			int index = GetActionIndex();
			using (var dialog = new EditActionDialog())
			{
				dialog.EnemyAction = _enemy.actions[index];
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					_enemy.actions[index] = dialog.EnemyAction;
					RefreshActions();
				}
			}
		}

		private void ListViewActionsDoubleClick(object sender, EventArgs e)
		{
			Point pnt = listViewActions.PointToClient(MousePosition);
			ListViewHitTestInfo info = listViewActions.HitTest(pnt);
			if (info.Item != null)
				this.ButtonEditActionClick(sender, e);
		}

		private void ListViewActionsSelectedIndexChanged(object sender, EventArgs e)
		{
			bool enable = listViewActions.SelectedItems.Count > 0;
			buttonEditAction.Enabled = enable;
			buttonRemoveAction.Enabled = enable;
			contextButtonActionEdit.Enabled = enable;
			contextButtonActionRemove.Enabled = enable;
		}

		private void ButtonTreasureClick(object sender, EventArgs e)
		{
			using (var dialog = new TreasureSelectDialog())
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
						_enemy.armor_id = dialog.ArmorId;
					RefreshTreasure();
				}
			}
		}

		private void PictureBattlerDoubleClick(object sender, EventArgs e)
		{
			using (var dialog =
				new ImageSelectionForm(@"Battlers", _enemy.battler_name))
			{
				dialog.Hue = _enemy.battler_hue;
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					_enemy.battler_name = dialog.ImageName;
					_enemy.battler_hue = dialog.Hue;
					pictureBattler.Image =
						Cache.Battler(_enemy.battler_name, _enemy.battler_hue);
				}
			}
		}

		private void ContextMenuImagesOpening(object sender, CancelEventArgs e)
		{
		    var pictureBox = this.contextMenuImages.SourceControl as PictureBox;
		    if (pictureBox != null)
		    {
		        var mode = pictureBox.SizeMode;
		        this.contextImageNormal.Checked = mode == PictureBoxSizeMode.Normal;
		        this.contextImageCenter.Checked = mode == PictureBoxSizeMode.CenterImage;
		        this.contextImageStretch.Checked = mode == PictureBoxSizeMode.StretchImage;
		        this.contextImageZoom.Checked = mode == PictureBoxSizeMode.Zoom;
		    }
		}

        private void ContextImagesSizeModeClicked(object sender, EventArgs e)
		{
		    var toolStripMenuItem = sender as ToolStripMenuItem;
		    if (toolStripMenuItem == null) return;
		    int num = Convert.ToInt32(toolStripMenuItem.Tag);
		    var mode = (PictureBoxSizeMode)num;
		    var pictureBox = this.contextMenuImages.SourceControl as PictureBox;
		    if (pictureBox != null)
		        pictureBox.SizeMode = mode;
		}

        #endregion
	}
}
