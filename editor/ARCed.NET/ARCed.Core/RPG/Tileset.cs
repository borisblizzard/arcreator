using System.Collections.Generic;

namespace RPG
{
	public class Tileset : IRpgObject
	{
		public int id { get; set; }
		public string name { get; set; }
		public string tileset_name { get; set; }
		public List<dynamic> autotile_names { get; set; }
		public string panorama_name { get; set; }
		public int panorama_hue { get; set; }
		public string fog_name { get; set; }
		public int fog_hue { get; set; }
		public int fog_opacity { get; set; }
		public int fog_blend_type { get; set; }
		public int fog_zoom { get; set; }
		public int fog_sx { get; set; }
		public int fog_sy { get; set; }
		public string battleback_name { get; set; }
		public Table passages { get; set; }
		public Table priorities { get; set; }
		public Table terrain_tags { get; set; }

		public Tileset()
		{
			id = 0;
			name = "";
			tileset_name = "";
			autotile_names = new List<dynamic>(7);
			panorama_name = "";
			panorama_hue = 0;
			fog_name = "";
			fog_hue = 0;
			fog_opacity = 64;
			fog_blend_type = 0;
			fog_zoom = 200;
			fog_sx = 0;
			fog_sy = 0;
			battleback_name = "";
			passages = new Table(384);
			priorities = new Table(384);
			priorities[0] = 5;
			terrain_tags = new Table(384);
		}

		/// <summary>
		/// Returns a <paramref name="System.String"/> that represents the current object.
		/// </summary>
		/// <returns>String representation of object.</returns>
		public override string ToString()
		{
			return string.Format("{0:d4}: {1}", this.id, this.name);
		}
	}
}
