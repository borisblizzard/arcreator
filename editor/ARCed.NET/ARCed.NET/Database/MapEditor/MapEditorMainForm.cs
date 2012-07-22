#region Using Directives

using System;
using System.Collections.Generic;
using System.Windows.Forms;
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
		public MapEditorMainForm()
		{
			this.InitializeComponent();
		}

		private void MapEditorMainFormLoad(object sender, System.EventArgs e)
		{
			if (DesignMode) return;

			Project.Data.Maps = new Dictionary<int, Map>();
			Map map = Project.LoadArcData<RPG.Map>(@"Data\Map023.arc", Util.RpgTypes);
			xnaPanel.Map = map;
		}
	}
}
