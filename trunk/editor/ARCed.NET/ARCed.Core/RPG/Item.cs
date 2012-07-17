#region Using Directives

using System.Collections.Generic;

#endregion

namespace RPG
{
    /// <summary>
    /// Data class for items.
    /// </summary>
	public class Item : IRpgObject
	{
        /// <summary>
        /// The item ID.
        /// </summary>
		public int id { get; set; }
        /// <summary>
        /// The item name.
        /// </summary>
		public string name { get; set; }
        /// <summary>
        /// The item's icon graphic file name.
        /// </summary>
		public string icon_name { get; set; }
        /// <summary>
        /// The item description.
        /// </summary>
		public string description { get; set; }
        /// <summary>
        /// Scope of the item's effects 
        /// (0: none, 1: one enemy, 2: all enemies, 3: one ally, 4: all allies, 5: 1 ally--HP 0, 6: all allies--HP 0, 7: the user).
        /// </summary>
		public int scope { get; set; }
        /// <summary>
        /// When the item may be used 
        /// (0: always, 1: only in battle, 2: only from the menu, 3: never).
        /// </summary>
		public int occasion { get; set; }
        /// <summary>
        /// The animation ID when using the item.
        /// </summary>
		public int animation1_id { get; set; }
        /// <summary>
        /// The animation ID when on the receiving end of the item.
        /// </summary>
		public int animation2_id { get; set; }
        /// <summary>
        /// SE played when item is used on the menu screen (<see cref="RPG.AudioFile"/>).
        /// </summary>
		public AudioFile menu_se { get; set; }
        /// <summary>
        /// The Common Event ID.
        /// </summary>
		public int common_event_id { get; set; }
        /// <summary>
        /// The item price.
        /// </summary>
		public int price { get; set; }
        /// <summary>
        /// Truth value of whether the item disappears when used.
        /// </summary>
		public bool consumable { get; set; }
        /// <summary>
        /// Parameter affected 
        /// (0: none, 1: max HP, 2: max SP, 3: strength, 4: dexterity, 5: agility, 6: intelligence).
        /// </summary>
		public int parameter_type { get; set; }
        /// <summary>
        /// Amount by which parameter increases.
        /// </summary>
		public int parameter_points { get; set; }
        /// <summary>
        /// HP recovery rate.
        /// </summary>
		public int recover_hp_rate { get; set; }
        /// <summary>
        /// HP recovery amount.
        /// </summary>
		public int recover_hp { get; set; }
        /// <summary>
        /// SP recovery rate.
        /// </summary>
		public int recover_sp_rate { get; set; }
        /// <summary>
        /// SP recovery amount.
        /// </summary>
		public int recover_sp { get; set; }
        /// <summary>
        /// The item's hit probability.
        /// </summary>
		public int hit { get; set; }
        /// <summary>
        /// The item's physical defense F rating.
        /// </summary>
		public int pdef_f { get; set; }
        /// <summary>
        /// The item's magic defense F rating.
        /// </summary>
		public int mdef_f { get; set; }
        /// <summary>
        /// The item's degree of variance.
        /// </summary>
		public int variance { get; set; }
        /// <summary>
        /// The item's element. An Elemental ID collection.
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
        /// Creates a new instance of an RPG.Item.
        /// </summary>
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
        /// Returns a <see langword="string"/> that represents the current object.
		/// </summary>
		/// <returns>String representation of object.</returns>
		public override string ToString()
		{
			return string.Format("{0:d4}: {1}", this.id, this.name);
		}
	}
}
