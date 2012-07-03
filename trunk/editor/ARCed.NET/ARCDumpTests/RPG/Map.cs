using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace RPG
{
	public class Map
	{
		public int tileset_id { get; set; }
		public int width { get; set; }
		public int height { get; set; }
		public bool autoplay_bgm { get; set; }
		public AudioFile bgm { get; set; }
		public bool autoplay_bgs { get; set; }
		public AudioFile bgs { get; set; }
		public List<dynamic> encounter_list { get; set; }
		public int encounter_step { get; set; }
		public Table data { get; set; }
		public Dictionary<int, Event> events { get; set; }

		public Map() : this(20, 15) { }

		public Map(int width, int height)
		{
			tileset_id = 0;
			this.width = width;
			this.height = height;
			autoplay_bgm = false;
			bgm = new AudioFile();
			autoplay_bgs = false;
			bgs = new AudioFile("", 80);
			encounter_list = new List<dynamic>();
			encounter_step = 30;
			data = new Table(width, height, 3);
			events = new Dictionary<int, Event>();
		}
	}
}
