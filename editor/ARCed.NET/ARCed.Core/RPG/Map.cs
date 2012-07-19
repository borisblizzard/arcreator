#region Using Directives

using System.Collections.Generic;

#endregion

namespace RPG
{
    /// <summary>
    /// Data class for maps.
    /// </summary>
	public class Map
	{
        /// <summary>
        /// Tileset ID to be used in the map.
        /// </summary>
		public int tileset_id { get; set; }
        /// <summary>
        /// The map width.
        /// </summary>
		public int width { get; set; }
        /// <summary>
        /// The map height.
        /// </summary>
		public int height { get; set; }
        /// <summary>
        /// Truth-value of whether BGM autoswitching is enabled.
        /// </summary>
		public bool autoplay_bgm { get; set; }
        /// <summary>
        /// If BGM autoswitching is enabled, the name of that BGM (<see cref="RPG.AudioFile"/>).
        /// </summary>
		public AudioFile bgm { get; set; }
        /// <summary>
        /// Truth-value of whether BGS autoswitching is enabled.
        /// </summary>
		public bool autoplay_bgs { get; set; }
        /// <summary>
        /// If BGS autoswitching is enabled, the name of that BGS (<see cref="RPG.AudioFile"/>).
        /// </summary>
		public AudioFile bgs { get; set; }
        /// <summary>
        /// Encounter list. A troop ID collection.
        /// </summary>
		public List<dynamic> encounter_list { get; set; }
        /// <summary>
        /// Encounter list. A troop ID array.
        /// </summary>
		public int encounter_step { get; set; }
        /// <summary>
        /// The map data. A 3-dimensional tile ID <see cref="Table"/>.
        /// </summary>
		public Table data { get; set; }
        /// <summary>
        /// Map events. A dictionary that represents RPG.Event instances as 
        /// values, using event IDs as the keys.
        /// </summary>
		public Dictionary<int, Event> events { get; set; }

        /// <summary>
        /// Creates a new instance of an RPG.Map.
        /// </summary>
        /// <param name="width">The map width.</param>
        /// <param name="height">The map height.</param>
		public Map(int width = 20, int height = 15)
		{
			this.tileset_id = 0;
			this.width = width;
			this.height = height;
			this.autoplay_bgm = false;
			this.bgm = new AudioFile();
			this.autoplay_bgs = false;
			this.bgs = new AudioFile("", 80);
			this.encounter_list = new List<dynamic>();
			this.encounter_step = 30;
			this.data = new Table(width, height, 3);
			this.events = new Dictionary<int, Event>();
		}
	}
}
