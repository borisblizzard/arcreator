
namespace RPG
{
	/// <summary>
	/// Data class for actors.
	/// </summary>
	public class Actor : IRpgObject
	{
		/// <summary>
		/// Actor id
		/// </summary>
		public int id { get; set; }
		/// <summary>
		/// Actor name
		/// </summary>
		public string name { get; set; }
		/// <summary>
		/// Actor class id
		/// </summary>
		public int class_id { get; set; }
		/// <summary>
		/// Actor's initial level
		/// </summary>
		public int initial_level { get; set; }
		/// <summary>
		/// Actor's final level
		/// </summary>
		public int final_level { get; set; }
		/// <summary>
		/// The value on which the experience curve is based (10..50).
		/// </summary>
		public int exp_basis { get; set; }
		/// <summary>
		/// The amount of experience curve inflation (10..50).
		/// </summary>
		public int exp_inflation { get; set; }
		/// <summary>
		/// The _actor's character graphic file name.
		/// </summary>
		public string character_name { get; set; }
		/// <summary>
		/// The adjustment value for the character graphic's hue (0..360).
		/// </summary>
		public int character_hue { get; set; }
		/// <summary>
		/// The _actor's battler graphic file name.
		/// </summary>
		public string battler_name { get; set; }
		/// <summary>
		/// The adjustment value for the battler graphic's hue (0..360).
		/// </summary>
		public int battler_hue { get; set; }
		/// <summary>
		/// 2-dimensional array containing base parameters for each level.
		/// Generally takes the form parameters[kind, level].
		/// Kind indicates the parameter type (0: max HP, 1: max SP, 2: strength, 3: dexterity, 4: agility, 5: intelligence).
		/// </summary>
		/// <seealso cref="Table"/>
		public Table parameters { get; set; }
		/// <summary>
		/// ID of the _actor's initially equipped weapon.
		/// </summary>
		public int weapon_id { get; set; }
		/// <summary>
		/// ID of the _actor's initially equipped shield.
		/// </summary>
		public int armor1_id { get; set; }
		/// <summary>
		/// ID of the _actor's initially equipped helmet.
		/// </summary>
		public int armor2_id { get; set; }
		/// <summary>
		/// ID of the _actor's initially equipped body armor.
		/// </summary>
		public int armor3_id { get; set; }
		/// <summary>
		/// ID of the _actor's initially equipped accessory.
		/// </summary>
		public int armor4_id { get; set; }
		/// <summary>
		/// Flag making the _actor's weapon unremovable.
		/// </summary>
		public bool weapon_fix { get; set; }
		/// <summary>
		/// Flag making the _actor's shield unremovable.
		/// </summary>
		public bool armor1_fix { get; set; }
		/// <summary>
		/// Flag making the _actor's helmet unremovable.
		/// </summary>
		public bool armor2_fix { get; set; }
		/// <summary>
		/// Flag making the _actor's body armor unremovable.
		/// </summary>
		public bool armor3_fix { get; set; }
		/// <summary>
		/// Flag making the _actor's accessory unremovable.
		/// </summary>
		public bool armor4_fix { get; set; }

		/// <summary>
		/// Default constructor
		/// </summary>
		public Actor()
		{
			id = 0;
			name = "";
			class_id = 1;
			initial_level = 1;
			final_level = 99;
			exp_basis = 30;
			exp_inflation = 30;
			character_name = "";
			character_hue = 0;
			battler_name = "";
			battler_hue = 0;
			parameters = new Table(6, 100);
			for (int i = 0; i < 100; i++)
			{
				parameters[0, i] = 500 + i * 50;
				parameters[1, i] = 500 + i * 50;
				parameters[2, i] = 50 + i * 5;
				parameters[3, i] = 50 + i * 5;
				parameters[4, i] = 50 + i * 5;
				parameters[5, i] = 50 + i * 5;
			}
			weapon_id = armor1_id = armor2_id = armor3_id = armor4_id = 0;
			weapon_fix = armor1_fix = armor2_fix = armor3_fix = armor4_fix = false;
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
