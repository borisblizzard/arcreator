using System.Collections.Generic;

namespace RPG
{
	public class Weapon
	{
		public int id { get; set; }
		public string name { get; set; }
		public string icon_name { get; set; }
		public string description { get; set; }
		public int animation1_id { get; set; }
		public int animation2_id { get; set; }
		public int price { get; set; }
		public int atk { get; set; }
		public int pdef { get; set; }
		public int mdef { get; set; }
		public int str_plus { get; set; }
		public int dex_plus { get; set; }
		public int agi_plus { get; set; }
		public int int_plus { get; set; }
		public List<dynamic> element_set { get; set; }
		public List<dynamic> plus_state_set { get; set; }
		public List<dynamic> minus_state_set { get; set; }

		public Weapon()
		{
			id = 0;
			name = "";
			icon_name = "";
			description = "";
			animation1_id = 0;
			animation2_id = 0;
			price = 0;
			atk = 0;
			pdef = 0;
			mdef = 0;
			str_plus = 0;
			dex_plus = 0;
			agi_plus = 0;
			int_plus = 0;
			element_set = new List<dynamic>();
			plus_state_set = new List<dynamic>();
			minus_state_set = new List<dynamic>();
		}
	}
}
