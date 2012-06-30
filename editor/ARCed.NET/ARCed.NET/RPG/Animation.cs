using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace RPG
{
	public class Animation : IRpgObject
	{

		public int id { get; set; }
		public string name { get; set; }
		public string animation_name { get; set; }
		public int animation_hue { get; set; }
		public int position { get; set; }
		public int frame_max { get; set; }
		public List<dynamic> frames { get; set; }
		public List<dynamic> timings { get; set; }

		public Animation()
		{
			id = 0;
			name = "";
			animation_name = "";
			animation_hue = 0;
			position = 1;
			frame_max = 1;
			frames = new List<dynamic>() {  };
			timings = new List<dynamic>() {  };
		}

		/// <summary>
		/// Returns a <paramref name="System.String"/> that represents the current object.
		/// </summary>
		/// <returns>String representation of object.</returns>
		public override string ToString()
		{
			return string.Format("{0:d4}: {1}", this.id, this.name);
		}

		public class Frame
		{
			public int cell_max { get; set; }
			public Table cell_data { get; set; }

			public Frame()
			{
				cell_max = 0;
				cell_data = new Table(0, 0);
			}
		}

		public class Timing
		{
			public int frame { get; set; }
			public AudioFile se { get; set; }
			public int flash_scope { get; set; }
			public Color flash_color { get; set; }
			public int flash_duration { get; set; }
			public int condition { get; set; }

			public Timing()
			{
				frame = 0;
				se = new AudioFile("", 80);
				flash_scope = 0;
				flash_color = new Color();
				flash_duration = 5;
				condition = 0;
			}
		}
	}
}
