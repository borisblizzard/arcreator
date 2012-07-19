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
		protected override DatabaseObjectListBox DataObjectList { get { return this.dataObjectList; } }

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
			this.InitializeComponent();
			this.InitializeElements();
			this.InitializeStates();
			RefreshObjectList();
			this._listViewSorter = new ListViewColumnSorter();
			this.listViewActions.ListViewItemSorter = this._listViewSorter;
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
			this.textBoxName.Text = this._enemy.name;
			this.RefreshParameters();
			this.RefreshImages();
			this.numericUpDownExp.Value = this._enemy.exp;
			this.numericUpDownGold.Value = this._enemy.gold;
			this.RefreshTreasure();
			this.RefreshElements();
			this.RefreshStates();
			this.RefreshActions();
			SuppressEvents = false;
		}

		#endregion

		#region Private Methods

		private void InitializeElements()
		{
			this.checkedListElements.ClearItems();
			List<dynamic> elements = Project.Data.System.elements;
			for (int i = 1; i < elements.Count; i++)
				this.checkedListElements.AddItem(elements[i % elements.Count]);
		}

		private void InitializeStates()
		{
			this.checkedListStates.ClearItems();
			List<dynamic> states = Project.Data.States;
			for (int i = 1; i < states.Count; i++)
				this.checkedListStates.AddItem(states[i % states.Count].name);
		}

		private void RefreshActions()
		{
			this.listViewActions.BeginUpdate();
			this.listViewActions.Items.Clear();
			foreach (Enemy.Action action in this._enemy.actions)
				this.listViewActions.Items.Add(MakeActionItem(action));
			this.listViewActions.EndUpdate();
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
				this.checkedListElements.SetItemIndex(i - 1, this._enemy.element_ranks[i]);
		}

		private void RefreshStates()
		{
			for (int i = 1; i < Project.Data.States.Count; i++)
				this.checkedListStates.SetItemIndex(i - 1, this._enemy.state_ranks[i]);
		}

		private void RefreshTreasure()
		{
			IRpgObject obj;
			if (this._enemy.item_id > 0) obj = Project.Data.Items[this._enemy.item_id];
			else if (this._enemy.weapon_id > 0) obj = Project.Data.Weapons[this._enemy.weapon_id];
			else if (this._enemy.armor_id > 0) obj = Project.Data.Armors[this._enemy.armor_id];
			else
			{
				this.textBoxTreasure.Text = "<None>";
				return;
			}
			this.textBoxTreasure.Text = String.Format("{0}% {1}", this._enemy.treasure_prob, obj.name);
		}

		private void RefreshParameters()
		{
			foreach (Control ctrl in this.flowPanel.Controls)
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
			this.pictureBattler.Image = Cache.Battler(this._enemy.battler_name, this._enemy.battler_hue);
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
			int index = this.dataObjectList.SelectedIndex;
			if (index >= 0)
			{
				this._enemy = this.Data[index + 1];
				this.RefreshCurrentObject();
			}
		}

		private void TextBoxNameTextChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
			{
				this._enemy.name = this.textBoxName.Text;
				int index = this.dataObjectList.SelectedIndex;
				this.dataObjectList.Items[index] = this._enemy.ToString();
				this.dataObjectList.Invalidate(this.dataObjectList.GetItemRectangle(index));
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
			if (e.Column == this._listViewSorter.SortColumn)
			{
				this._listViewSorter.Order = (this._listViewSorter.Order == SortOrder.Ascending) ?
					SortOrder.Descending : SortOrder.Ascending;
			}
			else
			{
				this._listViewSorter.SortColumn = e.Column;
				this._listViewSorter.Order = SortOrder.Ascending;
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
					this._enemy.actions.Add(dialog.EnemyAction);
					this.RefreshActions();
				}
			}
		}

		private void ButtonRemoveActionClick(object sender, EventArgs e)
		{
			int index = this.GetActionIndex();
			if (this._enemy != null && index >= 0)
			{
				this._enemy.actions.RemoveAt(index);
				this.RefreshActions();
				this.listViewActions.Focus();
				this.ListViewActionsSelectedIndexChanged(sender, e);
			}
			if (this.listViewActions.Items.Count > 0)
				this.listViewActions.Items[index.Clamp(0, this.listViewActions.Items.Count - 1)].Selected = true;
		}

		private int GetActionIndex()
		{
			if (this.listViewActions.SelectedIndices.Count > 0)
				return this.listViewActions.SelectedIndices[0];
			return -1;
		}

		private void ButtonEditActionClick(object sender, EventArgs e)
		{
			int index = this.GetActionIndex();
			using (var dialog = new EditActionDialog())
			{
				dialog.EnemyAction = this._enemy.actions[index];
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					this._enemy.actions[index] = dialog.EnemyAction;
					this.RefreshActions();
				}
			}
		}

		private void ListViewActionsDoubleClick(object sender, EventArgs e)
		{
			Point pnt = this.listViewActions.PointToClient(MousePosition);
			ListViewHitTestInfo info = this.listViewActions.HitTest(pnt);
			if (info.Item != null)
				this.ButtonEditActionClick(sender, e);
		}

		private void ListViewActionsSelectedIndexChanged(object sender, EventArgs e)
		{
			bool enable = this.listViewActions.SelectedItems.Count > 0;
			this.buttonEditAction.Enabled = enable;
			this.buttonRemoveAction.Enabled = enable;
			this.contextButtonActionEdit.Enabled = enable;
			this.contextButtonActionRemove.Enabled = enable;
		}

		private void ButtonTreasureClick(object sender, EventArgs e)
		{
			using (var dialog = new TreasureSelectDialog())
			{
				dialog.SetTreasure(this._enemy.treasure_prob, this._enemy.item_id,
					this._enemy.weapon_id, this._enemy.armor_id);
				if (dialog.ShowDialog() == DialogResult.OK)
				{
					this._enemy.treasure_prob = dialog.TreasureProbablity;
					this._enemy.item_id = this._enemy.weapon_id = this._enemy.armor_id = 0;
					if (dialog.ItemId > 0)
						this._enemy.item_id = dialog.ItemId;
					else if (dialog.WeaponId > 0)
						this._enemy.weapon_id = dialog.WeaponId;
					else if (dialog.ArmorId > 0)
						this._enemy.armor_id = dialog.ArmorId;
					this.RefreshTreasure();
				}
			}
		}

		private void PictureBattlerDoubleClick(object sender, EventArgs e)
		{
			using (var dialog =
				new ImageSelectionForm(@"Battlers", this._enemy.battler_name))
			{
				dialog.Hue = this._enemy.battler_hue;
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					this._enemy.battler_name = dialog.ImageName;
					this._enemy.battler_hue = dialog.Hue;
					this.pictureBattler.Image =
						Cache.Battler(this._enemy.battler_name, this._enemy.battler_hue);
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
