#region Using Directives

using System.Collections.Generic;

#endregion

namespace RPG
{
	public class CommonEvent : IRpgObject
	{
		public int id { get; set; }
		public string name { get; set; }
		public int trigger { get; set; }
		public int switch_id { get; set; }
		public List<dynamic> list { get; set; }

		public CommonEvent()
		{
			id = 0;
			name = "";
			trigger = 0;
			switch_id = 1;
			list = new List<dynamic>
			{ new EventCommand() };
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
