#region Using Directives

using System.Collections.Generic;

#endregion

namespace RPG
{
	public class Event : IRpgObject
	{
		public int id { get; set; }
		public string name { get; set; }
		public int x { get; set; }
		public int y { get; set; }
        public List<dynamic> pages { get; set; }

		public Event() : this(0, 0) { }

		public Event(int x, int y)
		{
			id = 0;
			name = "";
			this.x = x;
			this.y = y;
            pages = new List<dynamic>
            { new Page() };
		}

		/// <summary>
        /// Returns a <see langword="string"/> that represents the current object.
		/// </summary>
		/// <returns>String representation of object.</returns>
		public override string ToString()
		{
			return string.Format("{0:d4}: {1}", this.id, this.name);
		}

		public class Page
		{
			public Condition condition { get; set; }
			public Graphic graphic { get; set; }
			public int move_type { get; set; }
			public int move_speed { get; set; }
			public int move_frequency { get; set; }
			public MoveRoute move_route { get; set; }
			public bool walk_anime { get; set; }
			public bool step_anime { get; set; }
			public bool direction_fix { get; set; }
			public bool through { get; set; }
			public bool always_on_top { get; set; }
			public int trigger { get; set; }
			public List<dynamic> list { get; set; }

			public Page()
			{
				condition = new Condition();
				graphic = new Graphic();
				move_type = 0;
				move_speed = 3;
				move_frequency = 3;
				move_route = new MoveRoute();
				walk_anime = true;
				step_anime = false;
				direction_fix = false;
				through = false;
				always_on_top = false;
				trigger = 0;
                list = new List<dynamic>
                { new EventCommand() };
			}

			public class Condition
			{
				public bool switch1_valid { get; set; }
				public bool switch2_valid { get; set; }
				public bool variable_valid { get; set; }
				public bool self_switch_valid { get; set; }
				public int switch1_id { get; set; }
				public int switch2_id { get; set; }
				public int variable_id { get; set; }
				public int variable_value { get; set; }
				public char self_switch_ch { get; set; }

				public Condition()
				{
					switch1_valid = false;
					switch2_valid = false;
					variable_valid = false;
					self_switch_valid = false;
					switch1_id = 1;
					switch2_id = 1;
					variable_id = 1;
					variable_value = 0;
					self_switch_ch = 'A';
				}
			}

			public class Graphic
			{
				public int tile_id { get; set; }
				public string character_name { get; set; }
				public int character_hue { get; set; }
				public int direction { get; set; }
				public int pattern { get; set; }
				public int opacity { get; set; }
				public int blend_type { get; set; }

				public Graphic()
				{
					tile_id = 0;
					character_name = "";
					character_hue = 0;
					direction = 2;
					pattern = 0;
					opacity = 255;
					blend_type = 0;
				}
			}
		}
	}
}
