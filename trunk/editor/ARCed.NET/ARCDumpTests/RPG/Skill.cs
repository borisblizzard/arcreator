using System.Collections.Generic;

namespace RPG
{
	public class Skill
	{
		public int id { get; set; }
		public string name { get; set; }
		public string icon_name { get; set; }
		public string description { get; set; }
		public int scope { get; set; }
		public int occasion { get; set; }
		public int animation1_id { get; set; }
		public int animation2_id { get; set; }
		public AudioFile menu_se { get; set; }
		public int common_event_id { get; set; }
		public int sp_cost { get; set; }
		public int power { get; set; }
		public int atk_f { get; set; }
		public int eva_f { get; set; }
		public int str_f { get; set; }
		public int dex_f { get; set; }
		public int agi_f { get; set; }
		public int int_f { get; set; }
		public int hit { get; set; }
		public int pdef_f { get; set; }
		public int mdef_f { get; set; }
		public int variance { get; set; }
		public List<dynamic> element_set { get; set; }
		public List<dynamic> plus_state_set { get; set; }
		public List<dynamic> minus_state_set { get; set; }

		public Skill()
		{
			id = 0;
			name = "";
			icon_name = "";
			description = "";
			scope = 0;
			occasion = 1;
			animation1_id = 0;
			animation2_id = 0;
			menu_se = new AudioFile("", 80);
			common_event_id = 0;
			sp_cost = 0;
			power = 0;
			atk_f = 0;
			eva_f = 0;
			str_f = 0;
			dex_f = 0;
			agi_f = 0;
			int_f = 0;
			hit = 0;
			pdef_f = 0;
			mdef_f = 0;
			variance = 15;
			element_set = new List<dynamic>();
			plus_state_set = new List<dynamic>();
			minus_state_set = new List<dynamic>();
		}
	}
}
