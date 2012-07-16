#region Using Directives

using System.Collections.Generic;

#endregion

namespace RPG
{
	public class State : IRpgObject
	{
		public int id { get; set; }
		public string name { get; set; }
		public int animation_id { get; set; }
		public int restriction { get; set; }
		public bool nonresistance { get; set; }
		public bool zero_hp { get; set; }
		public bool cant_get_exp { get; set; }
		public bool cant_evade { get; set; }
		public bool slip_damage { get; set; }
		public int rating { get; set; }
		public int hit_rate { get; set; }
		public int maxhp_rate { get; set; }
		public int maxsp_rate { get; set; }
		public int str_rate { get; set; }
		public int dex_rate { get; set; }
		public int agi_rate { get; set; }
		public int int_rate { get; set; }
		public int atk_rate { get; set; }
		public int pdef_rate { get; set; }
		public int mdef_rate { get; set; }
		public int eva { get; set; }
		public bool battle_only { get; set; }
		public int hold_turn { get; set; }
		public int auto_release_prob { get; set; }
		public int shock_release_prob { get; set; }
		public List<dynamic> guard_element_set { get; set; }
		public List<dynamic> plus_state_set { get; set; }
		public List<dynamic> minus_state_set { get; set; }

		public State()
		{
			id = 0;
			name = "";
			animation_id = 0;
			restriction = 0;
			nonresistance = false;
			zero_hp = false;
			cant_get_exp = false;
			cant_evade = false;
			slip_damage = false;
			rating = 5;
			hit_rate = 100;
			maxhp_rate = 100;
			maxsp_rate = 100;
			str_rate = 100;
			dex_rate = 100;
			agi_rate = 100;
			int_rate = 100;
			atk_rate = 100;
			pdef_rate = 100;
			mdef_rate = 100;
			eva = 0;
			battle_only = true;
			hold_turn = 0;
			auto_release_prob = 0;
			shock_release_prob = 0;
			guard_element_set = new List<dynamic>();
			plus_state_set = new List<dynamic>();
			minus_state_set = new List<dynamic>();
		}

		/// <summary>
        /// Returns a <see langword="string"/> that represents the current object.
		/// </summary>
		/// <returns>String representation of object.</returns>
		public override string ToString()
		{
			return string.Format("{0:d4}: {1}", this.id, this.name);
		}
	}
}
