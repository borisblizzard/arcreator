
namespace RPG
{
	/// <summary>
	/// A generic container for a basic game object
	/// </summary>
	public class RpgObject
	{
		/// <summary>
		/// Gets or sets the name of the object
		/// </summary>
		public virtual string name { get; set; }
		/// <summary>
		/// Gets or sets the ID of the object
		/// </summary>
		public virtual int id { get; set; }

		/// <summary>
		/// Default constructor
		/// </summary>
		public RpgObject()
		{
			name = "";
			id = 0;
		}

		/// <summary>
		/// Default constructor
		/// </summary>
		/// <param name="name">Name of the object</param>
		/// <param name="id">ID of the object</param>
		public RpgObject(string name, int id)
		{
			this.name = name;
			this.id = id;
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
