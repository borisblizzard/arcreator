using System.Collections.Generic;

namespace RPG
{
	public class Class
	{
		public int id { get; set; }
		public string name { get; set; }
		public int position { get; set; }
		public List<int> weapon_set { get; set; }
		public List<int> armor_set { get; set; }
		public Table element_ranks { get; set; }
		public Table state_ranks { get; set; }
		public List<Learning> learnings { get; set; }

		public Class()
		{
			id = 0;
			name = "";
			position = 0;
			weapon_set = new List<int>();
			armor_set = new List<int>();
			element_ranks = new Table(1);
			state_ranks = new Table(1);
			learnings = new List<Learning>();
		}

		public class Learning
		{
			public int level { get; set; }
			public int skill_id { get; set; }

			public Learning()
			{
				level = 1;
				skill_id = 1;
			}
		}
	}
}
