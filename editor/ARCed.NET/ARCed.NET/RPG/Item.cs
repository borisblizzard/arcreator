using System.Collections.Generic;

namespace RPG
{
	public class Item : IRpgObject
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
		public int price { get; set; }
		public bool consumable { get; set; }
		public int parameter_type { get; set; }
		public int parameter_points { get; set; }
		public int recover_hp_rate { get; set; }
		public int recover_hp { get; set; }
		public int recover_sp_rate { get; set; }
		public int recover_sp { get; set; }
		public int hit { get; set; }
		public int pdef_f { get; set; }
		public int mdef_f { get; set; }
		public int variance { get; set; }
		public List<dynamic> element_set { get; set; }
		public List<dynamic> plus_state_set { get; set; }
		public List<dynamic> minus_state_set { get; set; }

		public Item()
		{
			id = 0;
			name = "";
			icon_name = "";
			description = "";
			scope = 0;
			occasion = 0;
			animation1_id = 0;
			animation2_id = 0;
			menu_se = new AudioFile("", 80);
			common_event_id = 0;
			price = 0;
			consumable = false;
			parameter_type = 0;
			parameter_points = 0;
			recover_hp_rate = 0;
			recover_hp = 0;
			recover_sp_rate = 0;
			recover_sp = 0;
			hit = 100;
			pdef_f = 0;
			mdef_f = 0;
			variance = 0;
			element_set = new List<dynamic>();
			plus_state_set = new List<dynamic>();
			minus_state_set = new List<dynamic>();
		}

		/// <summary>
		/// Returns a <paramref name="System.String"/> that represents the current object.
		/// </summary>
		/// <returns>String representation of object.</returns>
		public override string ToString()
		{
			return string.Format("{0:d4}: {1}", this.id, this.name);
		}
	}
}
