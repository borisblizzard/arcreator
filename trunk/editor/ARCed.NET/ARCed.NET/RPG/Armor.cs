using System.Collections;
using System.Collections.Generic;

namespace RPG
{
	public class Armor : IRpgObject
	{
		public int id { get; set; }
		public string name { get; set; }
		public string icon_name { get; set; }
		public string description { get; set; }
		public int kind { get; set; }
		public int auto_state_id { get; set; }
		public int price { get; set; }
		public int pdef { get; set; }
		public int mdef { get; set; }
		public int eva { get; set; }
		public int str_plus { get; set; }
		public int dex_plus { get; set; }
		public int agi_plus { get; set; }
		public int int_plus { get; set; }
		public List<dynamic>  guard_element_set { get; set; }
		public List<dynamic>  guard_state_set { get; set; }

		public Armor()
		{
			id = 0;
			name = "";
			icon_name = "";
			description = "";
			kind = 0;
			auto_state_id = 0;
			price = 0;
			pdef = 0;
			mdef = 0;
			eva = 0;
			str_plus = 0;
			dex_plus = 0;
			agi_plus = 0;
			int_plus = 0;
			guard_element_set = new List<dynamic> ();
			guard_state_set = new List<dynamic> ();
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
