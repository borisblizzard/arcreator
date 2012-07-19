#region Using Directives

using System.Collections.Generic;

#endregion

namespace RPG
{
    /// <summary>
    /// Data class for class.
    /// </summary>
	public class Class : IRpgObject
	{
        /// <summary>
        /// The class's ID.
        /// </summary>
		public int id { get; set; }
        /// <summary>
        /// The class name.
        /// </summary>
		public string name { get; set; }
        /// <summary>
        /// The class position (0: front, 1: middle, 2: rear).
        /// </summary>
		public int position { get; set; }
        /// <summary>
        /// Collection containing IDs for equippable weapons.
        /// </summary>
		public List<dynamic> weapon_set { get; set; }
        /// <summary>
        /// Collection containing IDs for equippable armor.
        /// </summary>
		public List<dynamic> armor_set { get; set; }
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
        /// Skills to Learn. A collection of <see cref="RPG.Class.Learning"/> objects.
        /// </summary>
		public List<dynamic> learnings { get; set; }

        /// <summary>
        /// Creates a new instance of an RPG.Class.
        /// </summary>
		public Class()
		{
			this.id = 0;
			this.name = "";
			this.position = 0;
			this.weapon_set = new List<dynamic>();
			this.armor_set = new List<dynamic>();
			this.element_ranks = new Table(1);
			this.state_ranks = new Table(1);
			this.learnings = new List<dynamic>();
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
        /// Data class for a [Class's Learned] skills.
        /// </summary>
		public class Learning
		{
            /// <summary>
            /// Skill level.
            /// </summary>
			public int level { get; set; }
            /// <summary>
            /// The learned skill's ID.
            /// </summary>
			public int skill_id { get; set; }

            /// <summary>
            /// Creates a new instance of an RPG.Class.Learning.
            /// </summary>
			public Learning()
			{
				this.level = 1;
				this.skill_id = 1;
			}
		}
	}
}
