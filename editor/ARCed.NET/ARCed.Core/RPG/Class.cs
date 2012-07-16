#region Using Directives

using System.Collections.Generic;

#endregion

namespace RPG
{
	public class Class : IRpgObject
	{
		public int id { get; set; }
		public string name { get; set; }
		public int position { get; set; }
		public List<dynamic> weapon_set { get; set; }
		public List<dynamic> armor_set { get; set; }
		public Table element_ranks { get; set; }
		public Table state_ranks { get; set; }
		public List<dynamic> learnings { get; set; }

		public Class()
		{
			id = 0;
			name = "";
			position = 0;
			weapon_set = new List<dynamic>();
			armor_set = new List<dynamic>();
			element_ranks = new Table(1);
			state_ranks = new Table(1);
			learnings = new List<dynamic>();
		}

		/// <summary>
        /// Returns a <see langword="string"/> that represents the current object.
		/// </summary>
		/// <returns>String representation of object.</returns>
		public override string ToString()
		{
			return string.Format("{0:d4}: {1}", this.id, this.name);
		}

		public class Learning
		{
			public int level { get; set; }
			public int skill_id { get; set; }

			public Learning()
			{
				level = 1;
				skill_id = 1;
			}
		}
	}
}
