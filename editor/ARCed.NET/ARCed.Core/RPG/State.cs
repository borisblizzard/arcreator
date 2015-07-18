﻿#region Using Directives

using System.Collections.Generic;

#endregion

namespace RPG
{
	/// <summary>
	/// Data class for state.
	/// </summary>
	public class State : IRpgObject
	{
		/// <summary>
		/// State ID.
		/// </summary>
		public int id { get; set; }
		/// <summary>
		/// State name.
		/// </summary>
		public string name { get; set; }
		/// <summary>
		/// The state's animation ID.
		/// </summary>
		public int animation_id { get; set; }
		/// <summary>
		/// Sets restrictions 
		/// (0: none, 1: can't use magic, 2: always attack enemies, 3: always attack allies, 4: can't move).
		/// </summary>
		public int restriction { get; set; }
		/// <summary>
		/// Truth value of the [Nonresistance] option.
		/// </summary>
		public bool nonresistance { get; set; }
		/// <summary>
		/// Truth value of the [Regard as HP 0] option.
		/// </summary>
		public bool zero_hp { get; set; }
		/// <summary>
		/// Truth value of the [Can't Get EXP] option.
		/// </summary>
		public bool cant_get_exp { get; set; }
		/// <summary>
		/// Truth value of the [Can't Evade] option.
		/// </summary>
		public bool cant_evade { get; set; }
		/// <summary>
		/// Truth value of the [Slip Damage] option.
		/// </summary>
		public bool slip_damage { get; set; }
		/// <summary>
		/// State rating (0..10).
		/// </summary>
		public int rating { get; set; }
		/// <summary>
		/// Hit percentage.
		/// </summary>
		public int hit_rate { get; set; }
		/// <summary>
		/// Maximum HP percentage.
		/// </summary>
		public int maxhp_rate { get; set; }
		/// <summary>
		/// Maximum SP percentage.
		/// </summary>
		public int maxsp_rate { get; set; }
		/// <summary>
		/// Strength percentage.
		/// </summary>
		public int str_rate { get; set; }
		/// <summary>
		/// Dexterity percentage.
		/// </summary>
		public int dex_rate { get; set; }
		/// <summary>
		/// Agility percentage.
		/// </summary>
		public int agi_rate { get; set; }
		/// <summary>
		/// Intelligence percentage.
		/// </summary>
		public int int_rate { get; set; }
		/// <summary>
		/// Attack percentage.
		/// </summary>
		public int atk_rate { get; set; }
		/// <summary>
		/// Physical defense percentage.
		/// </summary>
		public int pdef_rate { get; set; }
		/// <summary>
		/// Magic defense percentage.
		/// </summary>
		public int mdef_rate { get; set; }
		/// <summary>
		/// Evasion correction.
		/// </summary>
		public int eva { get; set; }
		/// <summary>
		/// Truth value of whether the state wears off at battle end.
		/// </summary>
		public bool battle_only { get; set; }
		/// <summary>
		/// Minumum number of turns before state has chance of releasing.
		/// </summary>
		public int hold_turn { get; set; }
		/// <summary>
		/// Percent probability of wearing off after the number of turns in hold_turn have passed.
		/// </summary>
		public int auto_release_prob { get; set; }
		/// <summary>
		/// Percent probability of wearing off after receiving physical damage.
		/// </summary>
		public int shock_release_prob { get; set; }
		/// <summary>
		/// Elemental defense. An Elemental ID collection.
		/// </summary>
		public List<dynamic> guard_element_set { get; set; }
		/// <summary>
		/// States to add. A State ID collection.
		/// </summary>
		public List<dynamic> plus_state_set { get; set; }
		/// <summary>
		/// States to cancel. A State ID collection.
		/// </summary>
		public List<dynamic> minus_state_set { get; set; }

		/// <summary>
		/// Creates a new instance of an RPG.State.
		/// </summary>
		public State()
		{
			this.id = 0;
			this.name = "";
			this.animation_id = 0;
			this.restriction = 0;
			this.nonresistance = false;
			this.zero_hp = false;
			this.cant_get_exp = false;
			this.cant_evade = false;
			this.slip_damage = false;
			this.rating = 5;
			this.hit_rate = 100;
			this.maxhp_rate = 100;
			this.maxsp_rate = 100;
			this.str_rate = 100;
			this.dex_rate = 100;
			this.agi_rate = 100;
			this.int_rate = 100;
			this.atk_rate = 100;
			this.pdef_rate = 100;
			this.mdef_rate = 100;
			this.eva = 0;
			this.battle_only = true;
			this.hold_turn = 0;
			this.auto_release_prob = 0;
			this.shock_release_prob = 0;
			this.guard_element_set = new List<dynamic>();
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
