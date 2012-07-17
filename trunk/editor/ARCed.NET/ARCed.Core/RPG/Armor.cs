﻿#region Using Directives

using System.Collections.Generic;

#endregion

namespace RPG
{
    /// <summary>
    /// Data class for armor.
    /// </summary>
	public class Armor : IRpgObject
	{
        /// <summary>
        /// The armor ID.
        /// </summary>
		public int id { get; set; }
        /// <summary>
        /// The armor name.
        /// </summary>
		public string name { get; set; }
        /// <summary>
        /// The armor's icon graphic file name.
        /// </summary>
		public string icon_name { get; set; }
        /// <summary>
        /// The armor description.
        /// </summary>
		public string description { get; set; }
        /// <summary>
        /// Type of armor (0: shield, 1: helmet, 2: body armor, 3: accessory).
        /// </summary>
		public int kind { get; set; }
        /// <summary>
        /// The auto state ID.
        /// </summary>
		public int auto_state_id { get; set; }
        /// <summary>
        /// The armor's price.
        /// </summary>
		public int price { get; set; }
        /// <summary>
        /// The armor's physical defense rating.
        /// </summary>
		public int pdef { get; set; }
        /// <summary>
        /// The armor's magic defense rating.
        /// </summary>
		public int mdef { get; set; }
        /// <summary>
        /// The armor's evasion correction.
        /// </summary>
		public int eva { get; set; }
        /// <summary>
        /// The armor's strength bonus.
        /// </summary>
		public int str_plus { get; set; }
        /// <summary>
        /// The armor's dexterity bonus.
        /// </summary>
		public int dex_plus { get; set; }
        /// <summary>
        /// The armor's agility bonus.
        /// </summary>
		public int agi_plus { get; set; }
        /// <summary>
        /// The armor's intelligence bonus.
        /// </summary>
		public int int_plus { get; set; }
        /// <summary>
        /// The armor's elemental defense rating. An elemental ID collection.
        /// </summary>
		public List<dynamic>  guard_element_set { get; set; }
        /// <summary>
        /// The armor's state defense rating. A state ID collection.
        /// </summary>
		public List<dynamic>  guard_state_set { get; set; }

        /// <summary>
        /// Creates a new instance of an RPG.Armor.
        /// </summary>
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
        /// Returns a <see langword="string"/> that represents the current object.
		/// </summary>
		/// <returns>String representation of object.</returns>
		public override string ToString()
		{
			return string.Format("{0:d4}: {1}", this.id, this.name);
		}
	}
}
