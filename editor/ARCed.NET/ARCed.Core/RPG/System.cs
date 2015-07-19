﻿#region Using Directives

using System.Collections.Generic;

#endregion

namespace RPG
{
	/// <summary>
	/// Data class for the system.
	/// </summary>
	public class System
	{
		/// <summary>
		/// Magic number used for update checks. 
		/// Updates changed values every time data is saved in RPGXP.
		/// </summary>
		public int magic_number { get; set; }
		/// <summary>
		/// The initial party. A collection of actor IDs.
		/// </summary>
		public List<dynamic> party_members { get; set; }
		/// <summary>
		/// Element list. 
		/// Text collection using element IDs as subscripts, 
		/// with the element in the 0 position being nil.
		/// </summary>
		public List<dynamic> elements { get; set; }
		/// <summary>
		/// Switch list. 
		/// Text collection using switch IDs as subscripts, 
		/// with the element in the 0 position being nil.
		/// </summary>
		public List<dynamic> switches { get; set; }
		/// <summary>
		/// Variable list. 
		/// Text collection using switch IDs as subscripts, 
		/// with the element in the 0 position being nil.
		/// </summary>
		public List<dynamic> variables { get; set; }
		/// <summary>
		/// The window skin (or "windowskin") graphic file name.
		/// </summary>
		public string windowskin_name { get; set; }
		/// <summary>
		/// The title graphic file name.
		/// </summary>
		public string title_name { get; set; }
		/// <summary>
		/// The "Game Over" graphic file name.
		/// </summary>
		public string gameover_name { get; set; }
		/// <summary>
		/// The file name of the transition graphic, displayed when entering battle.
		/// </summary>
		public string battle_transition { get; set; }
		/// <summary>
		/// The title BGM (<see cref="RPG.AudioFile"/>).
		/// </summary>
		public AudioFile title_bgm { get; set; }
		/// <summary>
		/// The battle BGM (<see cref="RPG.AudioFile"/>).
		/// </summary>
		public AudioFile battle_bgm { get; set; }
		/// <summary>
		/// The battle end ME (<see cref="RPG.AudioFile"/>).
		/// </summary>
		public AudioFile battle_end_me { get; set; }
		/// <summary>
		/// The gameover ME (<see cref="RPG.AudioFile"/>).
		/// </summary>
		public AudioFile gameover_me { get; set; }
		/// <summary>
		/// The cursor SE (<see cref="RPG.AudioFile"/>).
		/// </summary>
		public AudioFile cursor_se { get; set; }
		/// <summary>
		/// The decision SE (<see cref="RPG.AudioFile"/>).
		/// </summary>
		public AudioFile decision_se { get; set; }
		/// <summary>
		/// The cancel SE (<see cref="RPG.AudioFile"/>).
		/// </summary>
		public AudioFile cancel_se { get; set; }
		/// <summary>
		/// The buzzer SE (<see cref="RPG.AudioFile"/>).
		/// </summary>
		public AudioFile buzzer_se { get; set; }
		/// <summary>
		/// The equip SE (<see cref="RPG.AudioFile"/>).
		/// </summary>
		public AudioFile equip_se { get; set; }
		/// <summary>
		/// The shop SE (<see cref="RPG.AudioFile"/>).
		/// </summary>
		public AudioFile shop_se { get; set; }
		/// <summary>
		/// The save SE (<see cref="RPG.AudioFile"/>).
		/// </summary>
		public AudioFile save_se { get; set; }
		/// <summary>
		/// The load SE (<see cref="RPG.AudioFile"/>).
		/// </summary>
		public AudioFile load_se { get; set; }
		/// <summary>
		/// The battle start SE (<see cref="RPG.AudioFile"/>).
		/// </summary>
		public AudioFile battle_start_se { get; set; }
		/// <summary>
		/// The escape SE (<see cref="RPG.AudioFile"/>).
		/// </summary>
		public AudioFile escape_se { get; set; }
		/// <summary>
		/// The actor collapse SE (<see cref="RPG.AudioFile"/>).
		/// </summary>
		public AudioFile actor_collapse_se { get; set; }
		/// <summary>
		/// The enemy collapse SE (<see cref="RPG.AudioFile"/>).
		/// </summary>
		public AudioFile enemy_collapse_se { get; set; }
		/// <summary>
		/// Terms (<see cref="RPG.System.Words"/>).
		/// </summary>
		public Words words { get; set; }
		/// <summary>
		/// The map ID of the player's initial position.
		/// </summary>
		public int start_map_id { get; set; }
		/// <summary>
		/// The map X-coordinate of the player's initial position.
		/// </summary>
		public int start_x { get; set; }
		/// <summary>
		/// The map Y-coordinate of the player's initial position.
		/// </summary>
		public int start_y { get; set; }
		/// <summary>
		/// Party settings for battle tests. 
		/// A collection of <see cref="RPG.System.TestBattler"/> objects.
		/// </summary>
		public List<dynamic> test_battlers { get; set; }
		/// <summary>
		/// The troop ID for battle tests.
		/// </summary>
		public int test_troop_id { get; set; }
		/// <summary>
		/// The battle background graphic file name, for battle tests and internal use.
		/// </summary>
		public string battleback_name { get; set; }
		/// <summary>
		/// The battler graphic file name, for internal use.
		/// </summary>
		public string battler_name { get; set; }
		/// <summary>
		/// The adjustment value for the battler graphic's hue (0..360), for internal use.
		/// </summary>
		public int battler_hue { get; set; }
		/// <summary>
		/// The ID of the map currently being edited, for internal use.
		/// </summary>
		public int edit_map_id { get; set; }

		/// <summary>
		/// Creates a new instance of an RPG.System.
		/// </summary>
		public System()
		{
			this.magic_number = 0;
			this.party_members = new List<dynamic> { 1 };
			this.elements = new List<dynamic> { null, "" };
			this.switches = new List<dynamic> { null, "" };
			this.variables = new List<dynamic> { null, "" };
			this.windowskin_name = "";
			this.title_name = "";
			this.gameover_name = "";
			this.battle_transition = "";
			this.title_bgm = new AudioFile();
			this.battle_bgm = new AudioFile();
			this.battle_end_me = new AudioFile();
			this.gameover_me = new AudioFile();
			this.cursor_se = new AudioFile("", 80);
			this.decision_se = new AudioFile("", 80);
			this.cancel_se = new AudioFile("", 80);
			this.buzzer_se = new AudioFile("", 80);
			this.equip_se = new AudioFile("", 80);
			this.shop_se = new AudioFile("", 80);
			this.save_se = new AudioFile("", 80);
			this.load_se = new AudioFile("", 80);
			this.battle_start_se = new AudioFile("", 80);
			this.escape_se = new AudioFile("", 80);
			this.actor_collapse_se = new AudioFile("", 80);
			this.enemy_collapse_se = new AudioFile("", 80);
			this.words = new Words();
			this.test_battlers = new List<dynamic> { };
			this.test_troop_id = 1;
			this.start_map_id = 1;
			this.start_x = 0;
			this.start_y = 0;
			this.battleback_name = "";
			this.battler_name = "";
			this.battler_hue = 0;
			this.edit_map_id = 1;
		}

		/// <summary>
		/// Data class for the battlers used in battle tests.
		/// </summary>
		public class TestBattler
		{
			/// <summary>
			/// The actor ID.
			/// </summary>
			public int actor_id { get; set; }
			/// <summary>
			/// The actor's level.
			/// </summary>
			public int level { get; set; }
			/// <summary>
			/// The actor's weapon ID.
			/// </summary>
			public int weapon_id { get; set; }
			/// <summary>
			/// The actor's shield ID.
			/// </summary>
			public int armor1_id { get; set; }
			/// <summary>
			/// The actor's helmet ID.
			/// </summary>
			public int armor2_id { get; set; }
			/// <summary>
			/// The actor's body armor ID.
			/// </summary>
			public int armor3_id { get; set; }
			/// <summary>
			/// The actor's accessory ID.
			/// </summary>
			public int armor4_id { get; set; }

			/// <summary>
			/// Creates a new instance of an RPG.System.TestBattler.
			/// </summary>
			public TestBattler()
			{
				this.actor_id = 0;
				this.level = 0;
				this.weapon_id = 0;
				this.armor1_id = 0;
				this.armor2_id = 0;
				this.armor3_id = 0;
				this.armor4_id = 0;
			}
		}

		/// <summary>
		/// Data class for terminology.
		/// </summary>
		public class Words
		{
			/// <summary>
			/// The term "G" (the unit of currency).
			/// </summary>
			public string gold { get; set; }
			/// <summary>
			/// The term "HP" (hit points).
			/// </summary>
			public string hp { get; set; }
			/// <summary>
			/// The term "SP" (skill points).
			/// </summary>
			public string sp { get; set; }
			/// <summary>
			/// The term "Strength".
			/// </summary>
			public string str { get; set; }
			/// <summary>
			/// The term "Dexterity".
			/// </summary>
			public string dex { get; set; }
			/// <summary>
			/// The term "Agility".
			/// </summary>
			public string agi { get; set; }
			/// <summary>
			/// The term "Intelligence".
			/// </summary>
			public string @int { get; set; }
			/// <summary>
			/// The term "Attack Power".
			/// </summary>
			public string atk { get; set; }
			/// <summary>
			/// The term "Physical Defense".
			/// </summary>
			public string pdef { get; set; }
			/// <summary>
			/// The term "Magic Defense".
			/// </summary>
			public string mdef { get; set; }
			/// <summary>
			/// The term "Weapon".
			/// </summary>
			public string weapon { get; set; }
			/// <summary>
			/// The term "Shield".
			/// </summary>
			public string armor1 { get; set; }
			/// <summary>
			/// The term "Helmet".
			/// </summary>
			public string armor2 { get; set; }
			/// <summary>
			/// The term "Body armor".
			/// </summary>
			public string armor3 { get; set; }
			/// <summary>
			/// The term "Accessory".
			/// </summary>
			public string armor4 { get; set; }
			/// <summary>
			/// The term "Attack".
			/// </summary>
			public string attack { get; set; }
			/// <summary>
			/// The term "Skill".
			/// </summary>
			public string skill { get; set; }
			/// <summary>
			/// The term "Defense".
			/// </summary>
			public string guard { get; set; }
			/// <summary>
			/// The term "Item".
			/// </summary>
			public string item { get; set; }
			/// <summary>
			/// The term "Equip".
			/// </summary>
			public string equip { get; set; }

			/// <summary>
			/// Creates a new instance of an RPG.System.Words.
			/// </summary>
			public Words()
			{
				this.gold = "";
				this.hp = "";
				this.sp = "";
				this.str = "";
				this.dex = "";
				this.agi = "";
				this.@int = "";
				this.atk = "";
				this.pdef = "";
				this.mdef = "";
				this.weapon = "";
				this.armor1 = "";
				this.armor2 = "";
				this.armor3 = "";
				this.armor4 = "";
				this.attack = "";
				this.skill = "";
				this.guard = "";
				this.item = "";
				this.equip = "";
			}
		}
	}
}
