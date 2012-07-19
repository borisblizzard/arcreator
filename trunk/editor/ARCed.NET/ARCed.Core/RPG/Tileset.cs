#region Using Directives

using System.Collections.Generic;

#endregion

namespace RPG
{
    /// <summary>
    /// Data class for tilesets.
    /// </summary>
	public class Tileset : IRpgObject
	{
        /// <summary>
        /// The tileset ID.
        /// </summary>
		public int id { get; set; }
        /// <summary>
        /// The tileset name.
        /// </summary>
		public string name { get; set; }
        /// <summary>
        /// The tileset's graphic file name.
        /// </summary>
		public string tileset_name { get; set; }
        /// <summary>
        /// The autotile graphic's file name array ([0]..[6]).
        /// </summary>
		public List<dynamic> autotile_names { get; set; }
        /// <summary>
        /// The panorama graphic file name.
        /// </summary>
		public string panorama_name { get; set; }
        /// <summary>
        /// The adjustment value for the panorama graphic's hue (0..360).
        /// </summary>
		public int panorama_hue { get; set; }
        /// <summary>
        /// The fog graphic's file name.
        /// </summary>
		public string fog_name { get; set; }
        /// <summary>
        /// The adjustment value for the fog graphic's hue (0..360).
        /// </summary>
		public int fog_hue { get; set; }
        /// <summary>
        /// The fog's opacity.
        /// </summary>
		public int fog_opacity { get; set; }
        /// <summary>
        /// The fog's blending mode.
        /// </summary>
		public int fog_blend_type { get; set; }
        /// <summary>
        /// The fog's zoom level.
        /// </summary>
		public int fog_zoom { get; set; }
        /// <summary>
        /// The fog's SX (automatic X-axis scrolling speed).
        /// </summary>
		public int fog_sx { get; set; }
        /// <summary>
        /// The fog's SY (automatic Y-axis scrolling speed).
        /// </summary>
		public int fog_sy { get; set; }
        /// <summary>
        /// The battle background's graphic file name.
        /// </summary>
		public string battleback_name { get; set; }
        /// <summary>
        /// Passage table. A 1-dimensional <see cref="Table"/> containing passage flags, Bush flags, and counter flags.
        /// The tile ID is used as a subscript. 
        /// Each bit is handled as follows:
        ///     0x01: Cannot move down. 
        ///     0x02: Cannot move left. 
        ///     0x04: Cannot move right. 
        ///     0x08: Cannot move up. 
        ///     0x40: Bush flag. 
        ///     0x80: Counter flag. 
        /// </summary>
		public Table passages { get; set; }
        /// <summary>
        /// Priority table. A 1-dimensional <see cref="Table"/> containing priority data.
        /// The tile ID is used as a subscript.
        /// </summary>
		public Table priorities { get; set; }
        /// <summary>
        /// Priority table. A 1-dimensional <see cref="Table"/> containing terrain tag data.
        /// The tile ID is used as a subscript.
        /// </summary>
		public Table terrain_tags { get; set; }

        /// <summary>
        /// Creates a new instance of an RPG.Tileset.
        /// </summary>
		public Tileset()
		{
			this.id = 0;
			this.name = "";
			this.tileset_name = "";
			this.autotile_names = new List<dynamic>(7);
			this.panorama_name = "";
			this.panorama_hue = 0;
			this.fog_name = "";
			this.fog_hue = 0;
			this.fog_opacity = 64;
			this.fog_blend_type = 0;
			this.fog_zoom = 200;
			this.fog_sx = 0;
			this.fog_sy = 0;
			this.battleback_name = "";
			this.passages = new Table(384);
			this.priorities = new Table(384);
			this.priorities[0] = 5;
			this.terrain_tags = new Table(384);
		}

		/// <summary>
        /// Returns a <see langword="string"/> that represents the current object.
		/// </summary>
		/// <returns>String representation of object.</returns>
		public override string ToString()
		{
			return string.Format("{0:d4}: {1}", this.id, this.name);
		}
	}
}
