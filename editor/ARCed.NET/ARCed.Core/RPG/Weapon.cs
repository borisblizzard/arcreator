#region Using Directives

using System.Collections.Generic;

#endregion

namespace RPG
{
    /// <summary>
    /// Data class for weapons.
    /// </summary>
	public class Weapon : IRpgObject
	{
        /// <summary>
        /// The weapon ID.
        /// </summary>
		public int id { get; set; }
        /// <summary>
        /// The weapon name.
        /// </summary>
		public string name { get; set; }
        /// <summary>
        /// The weapon's icon graphic file name.
        /// </summary>
		public string icon_name { get; set; }
        /// <summary>
        /// The weapon description.
        /// </summary>
		public string description { get; set; }
        /// <summary>
        /// The animation ID when using the weapon.
        /// </summary>
		public int animation1_id { get; set; }
        /// <summary>
        /// The animation ID when on the receiving end of the weapon.
        /// </summary>
		public int animation2_id { get; set; }
        /// <summary>
        /// The weapon's price.
        /// </summary>
		public int price { get; set; }
        /// <summary>
        /// The weapon's attack power.
        /// </summary>
		public int atk { get; set; }
        /// <summary>
        /// The weapon's physical defense rating.
        /// </summary>
		public int pdef { get; set; }
        /// <summary>
        /// The weapon's magic defense rating.
        /// </summary>
		public int mdef { get; set; }
        /// <summary>
        /// The weapon's strength bonus.
        /// </summary>
		public int str_plus { get; set; }
        /// <summary>
        /// The weapon's dexterity bonus.
        /// </summary>
		public int dex_plus { get; set; }
        /// <summary>
        /// The weapon's agility bonus.
        /// </summary>
		public int agi_plus { get; set; }
        /// <summary>
        /// The weapon's intelligence bonus.
        /// </summary>
		public int int_plus { get; set; }
        /// <summary>
        /// The weapon's element. An Elemental ID array.
        /// </summary>
		public List<dynamic> element_set { get; set; }
        /// <summary>
        /// States to add. A State ID collection.
        /// </summary>
		public List<dynamic> plus_state_set { get; set; }
        /// <summary>
        /// States to cancel. A State ID collection.
        /// </summary>
		public List<dynamic> minus_state_set { get; set; }

        /// <summary>
        /// Creates a new instance of an RPG.Weapon.
        /// </summary>
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
