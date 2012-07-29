#region Using Directives

using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
using System.Linq;
using ARCed.Helpers;
using ARCed.UI;
using RPG;

#endregion

namespace ARCed.Database.MapEditor
{
    /// <summary>
    /// Main form for configuring Project <see cref="RPG.Map"/> data.
    /// </summary>
	public partial class MapEditorMainForm : DockContent
    {
	    private List<int> _skipIds;


		public MapEditorMainForm()
		{
			this.InitializeComponent();
			splitContainerControls.MinimumSize = new Size(tilesetSelectionPanel.Width, 32);
			this.RefreshMapList();
		}

		private void MapEditorMainFormLoad(object sender, System.EventArgs e)
		{
			if (DesignMode) return;

			Project.Data.Maps = new Dictionary<int, Map>();
			Map map = Project.LoadArcData<RPG.Map>(@"Data\Map017.arc", Util.RpgTypes);
			tilesetSelectionPanel.Tileset = Project.Data.Tilesets[map.tileset_id];
			mapEditorXnaPanel.Map = map;
		}

		private void RefreshMapList()
		{
			treeViewMaps.BeginUpdate();
			treeViewMaps.Nodes.Clear();
			TreeNode root = new TreeNode(Project.Title, 0, 0);
			_skipIds = new List<int>();
			List<dynamic> values = Project.Data.MapInfos.Values.ToList();
			values.Sort((v1, v2) => (v1 as MapInfo).order.CompareTo((v2 as MapInfo).order));

			foreach (MapInfo value in values)
			{
				int id = Project.Data.MapInfos.GetKey(value);
				if (!_skipIds.Contains(id))
					root.Nodes.Add(this.RecurrsiveSearch(id));
			}
			treeViewMaps.Nodes.Add(root);
			root.Expand();
			treeViewMaps.EndUpdate();
		}

		private TreeNode RecurrsiveSearch(int id)
		{
			Hash source = Project.Data.MapInfos;
			var mapInfo = source[id] as MapInfo;
			if (mapInfo != null)
			{
				var node = new TreeNode
				{
					Name = id.ToString(),
					ImageIndex = 1,
					SelectedImageIndex = 1,
					Text = mapInfo.name,
					Tag = mapInfo
				};
				foreach (MapInfo info in source.Values)
				{
					int childId = source.GetKey(info);
					if (info.parent_id == id && !_skipIds.Contains(childId))
					{
						_skipIds.Add(childId);
						node.Nodes.Add(RecurrsiveSearch(childId));
					}
				}
				return node;
			}
			return null;
		}

		private void TreeViewMapsAfterSelect(object sender, TreeViewEventArgs e)
		{
			MapInfo info = e.Node.Tag as MapInfo;
			if (info != null)
			{
				int id = Project.Data.MapInfos.GetKey(info);
				string file = String.Format(@"Data\Map{0:d3}.arc", id);
				Map map = Project.LoadArcData<RPG.Map>(file, Util.RpgTypes);

				mapEditorXnaPanel.Map = map;
			}
		}
	}
}
