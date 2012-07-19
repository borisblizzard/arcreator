#region Using Directives

using System.Collections.Generic;

#endregion

namespace RPG
{
    /// <summary>
    /// Data class for skills.
    /// </summary>
	public class Skill : IRpgObject
	{
        /// <summary>
        /// The skill ID.
        /// </summary>
		public int id { get; set; }
        /// <summary>
        /// The skill name.
        /// </summary>
		public string name { get; set; }
        /// <summary>
        /// The skill's icon graphic file name.
        /// </summary>
		public string icon_name { get; set; }
        /// <summary>
        /// The skill description.
        /// </summary>
		public string description { get; set; }
        /// <summary>
        /// Scope of the skill's effects 
        /// (0: none, 1: one enemy, 2: all enemies, 3: one ally, 4: all allies, 5: 1 ally--HP 0, 6: all allies--HP 0, 7: the user).
        /// </summary>
		public int scope { get; set; }
        /// <summary>
        /// When the skill may be used 
        /// (0: always, 1: only in battle, 2: only from the menu, 3: never).
        /// </summary>
		public int occasion { get; set; }
        /// <summary>
        /// The animation ID when using the skill.
        /// </summary>
		public int animation1_id { get; set; }
        /// <summary>
        /// The animation ID when on the receiving end of the skill.
        /// </summary>
		public int animation2_id { get; set; }
        /// <summary>
        /// SE played when skill is used on the menu screen (<see cref="RPG.AudioFile"/>).
        /// </summary>
		public AudioFile menu_se { get; set; }
        /// <summary>
        /// The Common Event ID.
        /// </summary>
		public int common_event_id { get; set; }
        /// <summary>
        /// Number of SP consumed.
        /// </summary>
		public int sp_cost { get; set; }
        /// <summary>
        /// The skill's power.
        /// </summary>
		public int power { get; set; }
        /// <summary>
        /// The skill's attack power F rating.
        /// </summary>
		public int atk_f { get; set; }
        /// <summary>
        /// The skill's evasion F rating.
        /// </summary>
		public int eva_f { get; set; }
        /// <summary>
        /// The skill's strength F rating.
        /// </summary>
		public int str_f { get; set; }
        /// <summary>
        /// The skill's dexterity F rating.
        /// </summary>
		public int dex_f { get; set; }
        /// <summary>
        /// The skill's agility F rating.
        /// </summary>
		public int agi_f { get; set; }
        /// <summary>
        /// The skill's intelligence F rating.
        /// </summary>
		public int int_f { get; set; }
        /// <summary>
        /// The skill's hit probability.
        /// </summary>
		public int hit { get; set; }
        /// <summary>
        /// The skill's physical defense F rating.
        /// </summary>
		public int pdef_f { get; set; }
        /// <summary>
        /// The skill's magic defense F rating.
        /// </summary>
		public int mdef_f { get; set; }
        /// <summary>
        /// The skill's degree of variance.
        /// </summary>
		public int variance { get; set; }
        /// <summary>
        /// The skill's element. An Elemental ID collection.
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
        /// Creates a new instance of an RPG.Skill.
        /// </summary>
		public Skill()
		{
			this.id = 0;
			this.name = "";
			this.icon_name = "";
			this.description = "";
			this.scope = 0;
			this.occasion = 1;
			this.animation1_id = 0;
			this.animation2_id = 0;
			this.menu_se = new AudioFile("", 80);
			this.common_event_id = 0;
			this.sp_cost = 0;
			this.power = 0;
			this.atk_f = 0;
			this.eva_f = 0;
			this.str_f = 0;
			this.dex_f = 0;
			this.agi_f = 0;
			this.int_f = 0;
			this.hit = 0;
			this.pdef_f = 0;
			this.mdef_f = 0;
			this.variance = 15;
			this.element_set = new List<dynamic>();
			this.plus_state_set = new List<dynamic>();
			this.minus_state_set = new List<dynamic>();
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
