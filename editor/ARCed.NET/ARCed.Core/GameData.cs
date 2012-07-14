using System.Collections.Generic;

namespace ARCed
{
	/// <summary>
	/// Container for holding all game data used by the editor and engine
	/// </summary>
	public class GameData
	{
		/// <summary>
		/// List of RPG.Actor objects. First element is null.
		/// </summary>
		public List<dynamic> Actors { get; set; }
		/// <summary>
		/// List of RPG.Animation objects. First element is null.
		/// </summary>
		public List<dynamic> Animations { get; set; }
		/// <summary>
		/// List of RPG.Armor objects. First element is null.
		/// </summary>
		public List<dynamic> Armors { get; set; }
		/// <summary>
		/// List of RPG.Class objects. First element is null.
		/// </summary>
		public List<dynamic> Classes { get; set; }
		/// <summary>
		/// List of RPG.CommonEvent objects. First element is null.
		/// </summary>
		public List<dynamic> CommonEvents { get; set; }
		/// <summary>
		/// List of RPG.Enemy objects. First element is null.
		/// </summary>
		public List<dynamic> Enemies { get; set; }
		/// <summary>
		/// List of RPG.Item objects. First element is null.
		/// </summary>
		public List<dynamic> Items { get; set; }
		/// <summary>
		/// List of RPG.MapInfo objects. First element is null.
		/// </summary>
		public List<dynamic> MapInfos { get; set; }
		/// <summary>
		/// List of RPG.Skills objects. First element is null.
		/// </summary>
		public List<dynamic> Skills { get; set; }
		/// <summary>
		/// List of RPG.State objects. First element is null.
		/// </summary>
		public List<dynamic> States { get; set; }
		/// <summary>
		/// RPG.System object.
		/// </summary>
		public RPG.System System { get; set; }
		/// <summary>
		/// List of RPG.Tileset objects. First element is null.
		/// </summary>
		public List<dynamic> Tilesets { get; set; }
		/// <summary>
		/// List of RPG.Troop objects. First element is null.
		/// </summary>
		public List<dynamic> Troops { get; set; }
		/// <summary>
		/// List of RPG.Weapon objects. First element is null.
		/// </summary>
		public List<dynamic> Weapons { get; set; }
		/// <summary>
		/// Dictionary whose key is the map ID and value is an RPG.Map object.
		/// </summary>
		public Dictionary<int, dynamic> Maps { get; set; }
	}
}
