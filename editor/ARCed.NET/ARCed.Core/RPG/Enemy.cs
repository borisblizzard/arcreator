#region Using Directives

using System.Collections.Generic;

#endregion

namespace RPG
{
    /// <summary>
    /// Data class for enemies.
    /// </summary>
	public class Enemy : IRpgObject
	{
        /// <summary>
        /// The enemy ID.
        /// </summary>
		public int id { get; set; }
        /// <summary>
        /// The enemy name.
        /// </summary>
		public string name { get; set; }
        /// <summary>
        /// The enemy's battler graphic file name.
        /// </summary>
		public string battler_name { get; set; }
        /// <summary>
        /// The adjustment value for the battler graphic's hue (0..360).
        /// </summary>
		public int battler_hue { get; set; }
        /// <summary>
        /// The enemy's max HP.
        /// </summary>
		public int maxhp { get; set; }
        /// <summary>
        /// The enemy's max SP.
        /// </summary>
		public int maxsp { get; set; }
        /// <summary>
        /// The enemy's strength.
        /// </summary>
		public int str { get; set; }
        /// <summary>
        /// The enemy's dexterity.
        /// </summary>
		public int dex { get; set; }
        /// <summary>
        /// The enemy's agility.
        /// </summary>
		public int agi { get; set; }
        /// <summary>
        /// The enemy's intelligence.
        /// </summary>
		public int @int { get; set; }
        /// <summary>
        /// The enemy's attack power.
        /// </summary>
		public int atk { get; set; }
        /// <summary>
        /// The enemy's physical defense rating.
        /// </summary>
		public int pdef { get; set; }
        /// <summary>
        /// The enemy's magic defense rating.
        /// </summary>
		public int mdef { get; set; }
        /// <summary>
        /// The enemy's evasion rating.
        /// </summary>
		public int eva { get; set; }
        /// <summary>
        /// The battle animation ID.
        /// </summary>
		public int animation1_id { get; set; }
        /// <summary>
        /// The target animation ID.
        /// </summary>
		public int animation2_id { get; set; }
        /// <summary>
        /// Level of elemental effectiveness. 
        /// 1-dimensional <see cref="Table"/> using element IDs as subscripts, 
        /// with 6 levels (0: A, 1: B, 2: C, 3: D, 4: E, 5: F).
        /// </summary>
		public Table element_ranks { get; set; }
        /// <summary>
        /// Level of status effectiveness. 
        /// 1-dimensional <see cref="Table"/> using status IDs as subscripts, 
        /// with 6 levels (0: A, 1: B, 2: C, 3: D, 4: E, 5: F).
        /// </summary>
		public Table state_ranks { get; set; }
        /// <summary>
        /// The enemy's actions. A collection of <see cref="RPG.Enemy.Action"/> objects.
        /// </summary>
		public List<dynamic> actions { get; set; }
        /// <summary>
        /// The enemy's experience.
        /// </summary>
		public int exp { get; set; }
        /// <summary>
        /// The enemy's gold.
        /// </summary>
		public int gold { get; set; }
        /// <summary>
        /// The ID of the item used as treasure.
        /// </summary>
		public int item_id { get; set; }
        /// <summary>
        /// The ID of the weapon used as treasure.
        /// </summary>
		public int weapon_id { get; set; }
        /// <summary>
        /// The ID of the armor used as treasure.
        /// </summary>
		public int armor_id { get; set; }
        /// <summary>
        /// The probability of treasure being left behind.
        /// </summary>
		public int treasure_prob { get; set; }

        /// <summary>
        /// Creates a new instance of an RPG.Enemy.
        /// </summary>
		public Enemy() // Number One
		{
			id = 0;
			name = "";
			battler_name = "";
			battler_hue = 0;
			maxhp = 0;
			maxsp = 0;
			str = 50;
			dex = 50;
			agi = 50;
			@int = 50;
			atk = 100;
			pdef = 100;
			mdef = 100;
			eva = 0;
			animation1_id = 0;
			animation2_id = 0;
			element_ranks = new Table(1);
			state_ranks = new Table(1);
			actions = new List<dynamic>
			{ new Action() };
			exp = 0;
			gold = 0;
			item_id = 0;
			weapon_id = 0;
			armor_id = 0;
			treasure_prob = 100;
		}

		/// <summary>
        /// Returns a <see langword="string"/> that represents the current object.
		/// </summary>
		/// <returns>String representation of object.</returns>
		public override string ToString()
		{
			return string.Format("{0:d4}: {1}", this.id, this.name);
		}

        /// <summary>
        /// Data class for enemy [Actions].
        /// </summary>
		public class Action
		{
            /// <summary>
            /// Type of action (0: basic, 1: skill).
            /// </summary>
			public int kind { get; set; }
            /// <summary>
            /// When set to a [Basic] action, defines it further 
            /// (0: attack, 1: defend, 2: escape, 3: do nothing).
            /// </summary>
			public int basic { get; set; }
            /// <summary>
            /// When set to a [Skill], the ID of that skill.
            /// </summary>
			public int skill_id { get; set; }
            /// <summary>
            /// a and b values specified in the [Turn] condition. 
            /// To be input in the form a + bx.
            /// When the turn is not specified as a condition, a = 0 and b = 1.
            /// </summary>
			public int condition_turn_a { get; set; }
            /// <summary>
            /// a and b values specified in the [Turn] condition. 
            /// To be input in the form a + bx.
            /// When the turn is not specified as a condition, a = 0 and b = 1.
            /// </summary>
			public int condition_turn_b { get; set; }
            /// <summary>
            /// Percentage specified in the [HP] condition.
            /// When HP is not specified as a condition, this value is set to 100.
            /// </summary>
			public int condition_hp { get; set; }
            /// <summary>
            /// Standard level specified in the [Level] condition.
            /// When the level is not specified as a condition, this value is set to 1.
            /// </summary>
			public int condition_level { get; set; }
            /// <summary>
            /// Switch ID specified in the [Switch] condition.
            /// When the switch ID is not specified as a condition, this value is set to 0. 
            /// Consequently, it is essential to check whether this value is 0.
            /// </summary>
			public int condition_switch_id { get; set; }
            /// <summary>
            /// The action's rating (1..10).
            /// </summary>
			public int rating { get; set; }

            /// <summary>
            /// Creates a new instance of an RPG.Enemy.Action.
            /// </summary>
			public Action()
			{
				kind = 0;
				basic = 0;
				skill_id = 1;
				condition_turn_a = 0;
				condition_turn_b = 1;
				condition_hp = 100;
				condition_level = 1;
				condition_switch_id = 0;
				rating = 5;
			}
		}

	}
}
