using System.Collections.Generic;

namespace RPG
{
	public class Enemy
	{
		public int id { get; set; }
		public string name { get; set; }
		public string battler_name { get; set; }
		public int battler_hue { get; set; }
		public int maxhp { get; set; }
		public int maxsp { get; set; }
		public int str { get; set; }
		public int dex { get; set; }
		public int agi { get; set; }
		public int intel { get; set; } 
		public int atk { get; set; }
		public int pdef { get; set; }
		public int mdef { get; set; }
		public int eva { get; set; }
		public int animation1_id { get; set; }
		public int animation2_id { get; set; }
		public Table element_ranks { get; set; }
		public Table state_ranks { get; set; }
		public List<dynamic> actions { get; set; }
		public int exp { get; set; }
		public int gold { get; set; }
		public int item_id { get; set; }
		public int weapon_id { get; set; }
		public int armor_id { get; set; }
		public int treasure_prob { get; set; }

		public Enemy() // Number One
		{
			id = 0;
			name = "";
			battler_name = "";
			battler_hue = 0;
			maxhp = 0;
			maxsp = 0;
			str = 50;
			dex = 50;
			agi = 50;
			intel = 50;
			atk = 100;
			pdef = 100;
			mdef = 100;
			eva = 0;
			animation1_id = 0;
			animation2_id = 0;
			element_ranks = new Table(1);
			state_ranks = new Table(1);
			actions = new List<dynamic>() { new Action() };
			exp = 0;
			gold = 0;
			item_id = 0;
			weapon_id = 0;
			armor_id = 0;
			treasure_prob = 100;
		}


		public class Action
		{
			public int kind { get; set; }
			public int basic { get; set; }
			public int skill_id { get; set; }
			public int condition_turn_a { get; set; }
			public int condition_turn_b { get; set; }
			public int condition_hp { get; set; }
			public int condition_level { get; set; }
			public int condition_switch_id { get; set; }
			public int rating { get; set; }

			public Action()
			{
				kind = 0;
				basic = 0;
				skill_id = 1;
				condition_turn_a = 0;
				condition_turn_b = 1;
				condition_hp = 100;
				condition_level = 1;
				condition_switch_id = 0;
				rating = 5;
			}
		}

	}
}
