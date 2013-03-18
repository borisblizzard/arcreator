
namespace RPG
{
	/// <summary>
	/// Generic interface for database objects
	/// </summary>
	public interface IRpgObject
	{
		/// <summary>
		/// Gets or sets the name of the object.
		/// </summary>
		string name { get; set; }
		/// <summary>
		/// Gets or sets the ID of the object.
		/// </summary>
		int id { get; set; }
	}
}
