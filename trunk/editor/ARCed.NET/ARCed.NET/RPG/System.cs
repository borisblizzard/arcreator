using System.Collections.Generic;

namespace RPG
{
	public class System
	{
		public int magic_number { get; set; }
		public List<dynamic> party_members { get; set; }
		public List<dynamic> elements { get; set; }
		public List<dynamic> switches { get; set; }
		public List<dynamic> variables { get; set; }
		public string windowskin_name { get; set; }
		public string title_name { get; set; }
		public string gameover_name { get; set; }
		public string battle_transition { get; set; }
		public AudioFile title_bgm { get; set; }
		public AudioFile battle_bgm { get; set; }
		public AudioFile battle_end_me { get; set; }
		public AudioFile gameover_me { get; set; }
		public AudioFile cursor_se { get; set; }
		public AudioFile decision_se { get; set; }
		public AudioFile cancel_se { get; set; }
		public AudioFile buzzer_se { get; set; }
		public AudioFile equip_se { get; set; }
		public AudioFile shop_se { get; set; }
		public AudioFile save_se { get; set; }
		public AudioFile load_se { get; set; }
		public AudioFile battle_start_se { get; set; }
		public AudioFile escape_se { get; set; }
		public AudioFile actor_collapse_se { get; set; }
		public AudioFile enemy_collapse_se { get; set; }
		public Words words { get; set; }
		public int start_map_id { get; set; }
		public int start_x { get; set; }
		public int start_y { get; set; }
		public List<dynamic> test_battlers { get; set; }
		public int test_troop_id { get; set; }
		public string battleback_name { get; set; }
		public string battler_name { get; set; }
		public int battler_hue { get; set; }
		public int edit_map_id { get; set; }

		public System()
		{
			magic_number = 0;
			party_members = new List<dynamic>() { 1 };
			elements = new List<dynamic>() { null, "" };
			switches = new List<dynamic>() { null, "" };
			variables = new List<dynamic>() { null, "" };
			windowskin_name = "";
			title_name = "";
			gameover_name = "";
			battle_transition = "";
			title_bgm = new AudioFile();
			battle_bgm = new AudioFile();
			battle_end_me = new AudioFile();
			gameover_me = new AudioFile();
			cursor_se = new AudioFile("", 80);
			decision_se = new AudioFile("", 80);
			cancel_se = new AudioFile("", 80);
			buzzer_se = new AudioFile("", 80);
			equip_se = new AudioFile("", 80);
			shop_se = new AudioFile("", 80);
			save_se = new AudioFile("", 80);
			load_se = new AudioFile("", 80);
			battle_start_se = new AudioFile("", 80);
			escape_se = new AudioFile("", 80);
			actor_collapse_se = new AudioFile("", 80);
			enemy_collapse_se = new AudioFile("", 80);
			words = new Words();
			test_battlers = new List<dynamic>() {};
			test_troop_id = 1;
			start_map_id = 1;
			start_x = 0;
			start_y = 0;
			battleback_name = "";
			battler_name = "";
			battler_hue = 0;
			edit_map_id = 1;
		}

		public class TestBattler
		{
			public int actor_id { get; set; }
			public int level { get; set; }
			public int weapon_id { get; set; }
			public int armor1_id { get; set; }
			public int armor2_id { get; set; }
			public int armor3_id { get; set; }
			public int armor4_id { get; set; }

			public TestBattler()
			{
				actor_id = 0;
				level = 0;
				weapon_id = 0;
				armor1_id = 0;
				armor2_id = 0;
				armor3_id = 0;
				armor4_id = 0;
			}
		}

		public class Words
		{
			public string gold { get; set; }
			public string hp { get; set; }
			public string sp { get; set; }
			public string str { get; set; }
			public string dex { get; set; }
			public string agi { get; set; }
			public string @int { get; set; }
			public string atk { get; set; }
			public string pdef { get; set; }
			public string mdef { get; set; }
			public string weapon { get; set; }
			public string armor1 { get; set; }
			public string armor2 { get; set; }
			public string armor3 { get; set; }
			public string armor4 { get; set; }
			public string attack { get; set; }
			public string skill { get; set; }
			public string guard { get; set; }
			public string item { get; set; }
			public string equip { get; set; }

			public Words()
			{
				gold = "";
				hp = "";
				sp = "";
				str = "";
				dex = "";
				agi = "";
				@int = "";
				atk = "";
				pdef = "";
				mdef = "";
				weapon = "";
				armor1 = "";
				armor2 = "";
				armor3 = "";
				armor4 = "";
				attack = "";
				skill = "";
				guard = "";
				item = "";
				equip = "";
			}
		}
	}
}
