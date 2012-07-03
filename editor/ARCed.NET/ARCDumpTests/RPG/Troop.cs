using System.Collections.Generic;

namespace RPG
{
	public class Troop
	{
		public int id { get; set; }
		public string name { get; set; }
		public List<dynamic> members { get; set; }
		public List<dynamic> pages{ get; set; }

		public Troop()
		{
			id = 0;
			name = "";
			members = new List<dynamic>();
			pages = new List<dynamic>() { new Page() };
		}

		public class Member
		{
			public int enemy_id { get; set; }
			public int x { get; set; }
			public int y { get; set; }
			public bool hidden { get; set; }
			public bool immortal { get; set; }

			public Member()
			{
				enemy_id = 0;
				x = 0;
				y = 0;
				hidden = false;
				immortal = false;
			}
		}

		public class Page
		{

			public Condition condition { get; set; }
			public int span { get; set; }
			public List<dynamic> list { get; set; }

			public Page()
			{
				condition = new Condition();
				span = 0;
				list = new List<dynamic>() { new EventCommand() };
			}

			public class Condition
			{
				public bool turn_valid { get; set; }
				public bool enemy_valid { get; set; }
				public bool actor_valid { get; set; }
				public bool switch_valid { get; set; }
				public int turn_a { get; set; }
				public int turn_b { get; set; }
				public int enemy_index { get; set; }
				public int enemy_hp { get; set; }
				public int actor_id { get; set; }
				public int actor_hp { get; set; }
				public int switch_id { get; set; }

				public Condition()
				{
					turn_valid = false;
					enemy_valid = false;
					actor_valid = false;
					switch_valid = false;
					turn_a = 0;
					turn_b = 0;
					enemy_index = 0;
					enemy_hp = 50;
					actor_id = 1;
					actor_hp = 50;
					switch_id = 1;
				}
			}
		}
	}
}
