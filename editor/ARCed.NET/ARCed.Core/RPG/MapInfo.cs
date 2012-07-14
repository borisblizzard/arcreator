using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace RPG
{
	public class MapInfo
	{
		public string name { get; set; }
		public int parent_id { get; set; }
		public int order { get; set; }
		public bool expanded { get; set; }
		public int scroll_x { get; set; }
		public int scroll_y { get; set; }
		
		public MapInfo()
		{
			name = "";
			parent_id = 0;
			order = 0;
			expanded = false;
			scroll_x = 0;
			scroll_y = 0;
		}
	}
}
