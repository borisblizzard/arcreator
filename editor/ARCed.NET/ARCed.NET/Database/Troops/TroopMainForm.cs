#region Using Directives

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Linq;
using System.Windows.Forms;
using ARCed.Controls;
using ARCed.Dialogs;
using ARCed.Helpers;
using RPG;

#endregion

namespace ARCed.Database.Troops
{
	public partial class TroopMainForm : DatabaseWindow
	{
		#region Private Fields

		private string _battleBackName;
		private Troop _troop;

		#endregion

		#region Protected Properties

		/// <summary>
		/// Gets the object list control of this database panel.
		/// </summary>
		protected override DatabaseObjectListBox DataObjectList { get { return dataObjectList; } }

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
			InitializeComponent();
			RefreshEnemies();
			RefreshObjectList();
		}

		#endregion

		public override void NotifyRefresh(RefreshType type)
		{
			if (type.HasFlag(RefreshType.Enemies))
			{

			}
			if (type.HasFlag(RefreshType.Switches))
			{

			}
		}

		public override void RefreshCurrentObject()
		{
			SuppressEvents = true;
			xnaPanel.RemoveAll();
            foreach (Troop.Member member in _troop.members)
            {
                xnaPanel.AddSprite(new EnemySprite(Project.Data.Enemies[member.enemy_id]));
            }
			textBoxName.Text = _troop.name;
			RefreshEvents();
			SuppressEvents = false;
		}

		private void RefreshEnemies()
		{
			ControlHelper.Populate(listBoxEnemies, Project.Data.Enemies, false);
		}

		private void RefreshEvents()
		{
			tabControlEvents.SuspendPainting();
			tabControlEvents.TabPages.Clear();
			int count = 1;
			foreach (var page in _troop.pages)
			{
				var tab = new TabPage(count.ToString());
				var editor = new BattleEventPage();
				tab.Controls.Add(editor);
				editor.Dock = DockStyle.Fill;
				editor.EventPage = page;
				tabControlEvents.TabPages.Add(tab);
				count++;
			}
			tabControlEvents.ResumePainting(true);
		}

		private void TroopMainForm_Load(object sender, EventArgs e)
		{
			var resources = ResourceHelper.GetTypes(@"Graphics\Battlebacks");
			if (resources.Count > 0)
			{
				_battleBackName = resources[0].Name;
				xnaPanel.SetBackground(Cache.Battleback(_battleBackName));
			}
			else
			{
				Image image = new Bitmap(640, 320);
				using (Graphics g = Graphics.FromImage(image))
				{
					g.FillRectangle(Brushes.CornflowerBlue, 0, 0, 640, 320);
					g.DrawString("No background image found!", this.Font, Brushes.White, new PointF(12, 12));
				}
				xnaPanel.SetBackground(image);
			}
			dataObjectList.SelectedIndex = 0;
		}

		private void buttonAddEnemy_Click(object sender, EventArgs e)
		{
			int index = listBoxEnemies.SelectedIndex;
			if (index >= 0)
			{
				var sprite = new EnemySprite(Project.Data.Enemies[index + 1]);
				xnaPanel.AddSprite(sprite);
			}
			if (xnaPanel.Sprites.Count >= 12)
				buttonAddEnemy.Enabled = false;
		}

		private void buttonRemoveEnemy_Click(object sender, EventArgs e)
		{
			xnaPanel.RemoveSelected();
		}

		private void buttonAlignEnemies_Click(object sender, EventArgs e)
		{
			xnaPanel.AutoAlign();
		}

		private void buttonFull_Click(object sender, EventArgs e)
		{

		}

		private void xnaPanel_OnSelectionChanged(object sender, EventArgs e)
		{
			bool enable = false;
			foreach (EnemySprite sprite in xnaPanel.Sprites)
			{
				if (sprite.Selected)
				{
					enable = true;
					break;
				}
			}
			buttonRemoveEnemy.Enabled = enable;
		}

		private void xnaPanel_OnTroopChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
			{
				_troop.members.Clear();
				foreach (EnemySprite sprite in xnaPanel.Sprites)
					_troop.members.Add(sprite.TroopMember);
			}
		}

		private void form_KeyDown(object sender, KeyEventArgs e)
		{
			if (e.KeyCode == Keys.Delete)
			{
				buttonRemoveEnemy_Click(null, null);
				e.Handled = true;
			}
		}

		private void listBoxEnemies_SelectedIndexChanged(object sender, EventArgs e)
		{
			buttonAddEnemy.Enabled = listBoxEnemies.SelectedIndex >= 0;
		}

		private void buttonBattleback_Click(object sender, EventArgs e)
		{
			using (var dialog = new ImageSelectionForm(@"Battlebacks", _battleBackName))
			{
				dialog.Width = 800;
				dialog.SelectionEnabled = false;
				dialog.HueEnabled = false;
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					_battleBackName = dialog.ImageName;
					xnaPanel.SetBackground(Cache.Battleback(_battleBackName));
				}
			}
		}

		private void dataObjectList_OnListBoxIndexChanged(object sender, EventArgs e)
		{
			int index = dataObjectList.SelectedIndex;
			if (index >= 0)
			{
				_troop = Data[index + 1];
				RefreshCurrentObject();
			}
		}

		private void buttonClear_Click(object sender, EventArgs e)
		{
			xnaPanel.RemoveAll();
		}

		private void contextMenuStripMember_Opening(object sender, CancelEventArgs e)
		{
			EnemySprite sprite = xnaPanel.SelectedSprite;
			if (sprite == null)
				e.Cancel = true;
			else
			{
				SuppressEvents = true;
				buttonAppearHalfway.Checked = sprite.Hidden;
				buttonImmortal.Checked = sprite.Immortal;
				SuppressEvents = false;
			}
		}

		private void buttonAppearHalfway_CheckedChanged(object sender, EventArgs e)
		{
			xnaPanel.SelectedSprite.Hidden = buttonAppearHalfway.Checked;
			xnaPanel.Invalidate();
		}

		private void buttonImmortal_CheckedChanged(object sender, EventArgs e)
		{
			xnaPanel.SelectedSprite.Immortal = buttonImmortal.Checked;
		}

		private void buttonAutoname_Click(object sender, EventArgs e)
		{
			var enemyCounts = new SortedDictionary<int, int>();
			int id;
			foreach (Troop.Member member in _troop.members)
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
			textBoxName.Text = String.Join(", ", names);
		}

		private void textBoxName_TextChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
			{
				_troop.name = textBoxName.Text;
				int index = dataObjectList.SelectedIndex;
				dataObjectList.Items[index] = _troop.ToString();
				dataObjectList.Invalidate(dataObjectList.GetItemRectangle(index));
			}
		}

		private void buttonBattleTest_Click(object sender, EventArgs e)
		{
			using (var dialog = new BattleTestDialog())
			{
				dialog.ShowDialog();
			}
		}

		private void listBoxEnemies_MouseDown(object sender, MouseEventArgs e)
		{
			int index = listBoxEnemies.IndexFromPoint(e.Location);
			if (index >= 0)
				listBoxEnemies.DoDragDrop(Project.Data.Enemies[index + 1], DragDropEffects.Copy);
		}

		private void xnaPanel_DragEnter(object sender, DragEventArgs e)
		{

			if (e.Data.GetData(typeof(Enemy)) != null)
				e.Effect = DragDropEffects.Copy;
			else
				e.Effect = DragDropEffects.None;
		}

		private void xnaPanel_DragDrop(object sender, DragEventArgs e)
		{
            var enemy = (Enemy)e.Data.GetData(typeof(Enemy));
            var sprite = new EnemySprite(enemy);
			Point p = xnaPanel.PointToClient(new Point(e.X, e.Y));
			sprite.X = p.X - (sprite.Width / 2);
			sprite.Y = p.Y - (sprite.Height / 2);
			xnaPanel.AddSprite(sprite);
		}
	}
}
