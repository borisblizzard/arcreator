#region Using Directives

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Globalization;
using System.Linq;
using System.Windows.Forms;
using ARCed.Controls;
using ARCed.Dialogs;
using ARCed.Helpers;
using RPG;

#endregion

namespace ARCed.Database.Troops
{
    /// <summary>
    /// Main form for configuring Project <see cref="RPG.Troop"/> data.
    /// </summary>
	public sealed partial class TroopMainForm : DatabaseWindow
	{
		#region Private Fields

		private string _battleBackName;
		private Troop _troop;

		#endregion

		#region Protected Properties

		/// <summary>
		/// Gets the object list control of this database panel.
		/// </summary>
		protected override DatabaseObjectListBox DataObjectList { get { return this.dataObjectList; } }

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets the data associated with this panel
		/// </summary>
		public override List<dynamic> Data { get { return Project.Data.Troops; } }

		#endregion

		#region Constructor

		/// <summary>
		/// Default constructor
		/// </summary>
		public TroopMainForm()
		{
			this.InitializeComponent();
			this.RefreshEnemies();
			RefreshObjectList();
		}

		#endregion

        #region Public Methods

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
        /// Refreshes the form to display data for the currently selected <see cref="RPG.Troop"/>.
        /// </summary>
		public override void RefreshCurrentObject()
		{
			SuppressEvents = true;
			this.xnaPanel.RemoveAll();
            foreach (Troop.Member member in this._troop.members)
            {
                this.xnaPanel.AddSprite(new EnemySprite(Project.Data.Enemies[member.enemy_id]));
            }
			this.textBoxName.Text = this._troop.name;
			this.RefreshEvents();
			SuppressEvents = false;
		}

        #endregion

        #region Private Methods

        private void RefreshEnemies()
		{
			ControlHelper.Populate(this.listBoxEnemies, Project.Data.Enemies, false);
		}

		private void RefreshEvents()
		{
			this.tabControlEvents.SuspendPainting();
			this.tabControlEvents.TabPages.Clear();
			int count = 1;
			foreach (var page in this._troop.pages)
			{
				var tab = new TabPage(count.ToString(CultureInfo.InvariantCulture));
				var editor = new BattleEventPage();
				tab.Controls.Add(editor);
				editor.Dock = DockStyle.Fill;
				editor.EventPage = page;
				this.tabControlEvents.TabPages.Add(tab);
				count++;
			}
			this.tabControlEvents.ResumePainting(true);
		}

		private void TroopMainFormLoad(object sender, EventArgs e)
		{
			var resources = ResourceHelper.GetTypes(@"Graphics\Battlebacks");
			if (resources.Count > 0)
			{
				this._battleBackName = resources[0].Name;
				this.xnaPanel.SetBackground(Cache.Battleback(this._battleBackName));
			}
			else
			{
				Image image = new Bitmap(640, 320);
				using (Graphics g = Graphics.FromImage(image))
				{
					g.FillRectangle(Brushes.CornflowerBlue, 0, 0, 640, 320);
					g.DrawString("No background image found!", Font, Brushes.White, new PointF(12, 12));
				}
				this.xnaPanel.SetBackground(image);
			}
			this.dataObjectList.SelectedIndex = 0;
		}

		private void ButtonAddEnemyClick(object sender, EventArgs e)
		{
			var index = this.listBoxEnemies.SelectedIndex;
			if (index >= 0)
			{
				var sprite = new EnemySprite(Project.Data.Enemies[index + 1]);
				this.xnaPanel.AddSprite(sprite);
			}
			if (this.xnaPanel.Sprites.Count >= 12)
				this.buttonAddEnemy.Enabled = false;
		}

		private void ButtonRemoveEnemyClick(object sender, EventArgs e)
		{
			this.xnaPanel.RemoveSelected();
		}

		private void ButtonAlignEnemiesClick(object sender, EventArgs e)
		{
			this.xnaPanel.AutoAlign();
		}

		private void ButtonFullClick(object sender, EventArgs e)
		{

		}

		private void XnaPanelOnSelectionChanged(object sender, EventArgs e)
		{
			var enable = this.xnaPanel.Sprites.Any(sprite => sprite.Selected);
		    this.buttonRemoveEnemy.Enabled = enable;
		}

		private void XnaPanelOnTroopChanged(object sender, EventArgs e)
		{
		    if (SuppressEvents) return;
		    this._troop.members.Clear();
		    foreach (EnemySprite sprite in this.xnaPanel.Sprites)
		        this._troop.members.Add(sprite.TroopMember);
		}

		private void FormKeyDown(object sender, KeyEventArgs e)
		{
		    if (e.KeyCode != Keys.Delete) return;
		    this.ButtonRemoveEnemyClick(null, null);
		    e.Handled = true;
		}

		private void ListBoxEnemiesSelectedIndexChanged(object sender, EventArgs e)
		{
			this.buttonAddEnemy.Enabled = this.listBoxEnemies.SelectedIndex >= 0;
		}

		private void ButtonBattlebackClick(object sender, EventArgs e)
		{
			using (var dialog = new ImageSelectionForm(@"Battlebacks", this._battleBackName))
			{
				dialog.Width = 800;
				dialog.SelectionEnabled = false;
				dialog.HueEnabled = false;
			    if (dialog.ShowDialog(this) != DialogResult.OK) return;
			    this._battleBackName = dialog.ImageName;
			    this.xnaPanel.SetBackground(Cache.Battleback(this._battleBackName));
			}
		}

		private void DataObjectListOnListBoxIndexChanged(object sender, EventArgs e)
		{
			var index = this.dataObjectList.SelectedIndex;
		    if (index < 0) return;
		    this._troop = this.Data[index + 1];
		    this.RefreshCurrentObject();
		}

		private void ButtonClearClick(object sender, EventArgs e)
		{
			this.xnaPanel.RemoveAll();
		}

		private void ContextMenuStripMemberOpening(object sender, CancelEventArgs e)
		{
			var sprite = this.xnaPanel.SelectedSprite;
			if (sprite == null)
				e.Cancel = true;
			else
			{
				SuppressEvents = true;
				this.buttonAppearHalfway.Checked = sprite.Hidden;
				this.buttonImmortal.Checked = sprite.Immortal;
				SuppressEvents = false;
			}
		}

		private void ButtonAppearHalfwayCheckedChanged(object sender, EventArgs e)
		{
			this.xnaPanel.SelectedSprite.Hidden = this.buttonAppearHalfway.Checked;
			this.xnaPanel.Invalidate();
		}

		private void ButtonImmortalCheckedChanged(object sender, EventArgs e)
		{
			this.xnaPanel.SelectedSprite.Immortal = this.buttonImmortal.Checked;
		}

		private void ButtonAutonameClick(object sender, EventArgs e)
		{
			var enemyCounts = new SortedDictionary<int, int>();
			int id;
			foreach (Troop.Member member in this._troop.members)
			{
				id = member.enemy_id;
				if (enemyCounts.ContainsKey(id))
					enemyCounts[id] += 1;
				else
					enemyCounts[id] = 1;
			}
			var names = new string[enemyCounts.Count];
			int count = 0;
			foreach (int i in enemyCounts.Keys.Reverse())
			{
				names[count] = String.Format("{0}*{1}",
					Project.Data.Enemies[i].name, enemyCounts[i]);
				count++;
			}
			this.textBoxName.Text = String.Join(", ", names);
		}

		private void TextBoxNameTextChanged(object sender, EventArgs e)
		{
		    if (SuppressEvents) return;
		    this._troop.name = this.textBoxName.Text;
		    int index = this.dataObjectList.SelectedIndex;
		    this.dataObjectList.Items[index] = this._troop.ToString();
		    this.dataObjectList.Invalidate(this.dataObjectList.GetItemRectangle(index));
		}

		private void ButtonBattleTestClick(object sender, EventArgs e)
		{
			using (var dialog = new BattleTestDialog())
				dialog.ShowDialog();
		}

		private void ListBoxEnemiesMouseDown(object sender, MouseEventArgs e)
		{
			var index = this.listBoxEnemies.IndexFromPoint(e.Location);
			if (index >= 0)
				this.listBoxEnemies.DoDragDrop(Project.Data.Enemies[index + 1], DragDropEffects.Copy);
		}

		private void XnaPanelDragEnter(object sender, DragEventArgs e) 
        {
		    e.Effect = e.Data.GetData(typeof(Enemy)) != null ? 
                DragDropEffects.Copy : DragDropEffects.None;
		}

        private void XnaPanelDragDrop(object sender, DragEventArgs e)
		{
            var enemy = (Enemy)e.Data.GetData(typeof(Enemy));
            var sprite = new EnemySprite(enemy);
			var p = this.xnaPanel.PointToClient(new Point(e.X, e.Y));
			sprite.X = p.X - (sprite.Width / 2);
			sprite.Y = p.Y - (sprite.Height / 2);
			this.xnaPanel.AddSprite(sprite);
        }

        #endregion
    }
}
