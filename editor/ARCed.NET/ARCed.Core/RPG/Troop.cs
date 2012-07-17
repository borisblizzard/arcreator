#region Using Directives

using System.Collections.Generic;

#endregion

namespace RPG
{
    /// <summary>
    /// Data class for troops.
    /// </summary>
	public class Troop : IRpgObject
	{
        /// <summary>
        /// Troop ID.
        /// </summary>
		public int id { get; set; }
        /// <summary>
        /// Troop name.
        /// </summary>
		public string name { get; set; }
        /// <summary>
        /// Troop members. A collection of <see cref="RPG.Troop.Member"/> objects.
        /// </summary>
		public List<dynamic> members { get; set; }
        /// <summary>
        /// Battle events. A collection of <see cref="RPG.Troop.Page"/> objects.
        /// </summary>
		public List<dynamic> pages{ get; set; }

        /// <summary>
        /// Creates a new instance of an RPG.Troop.
        /// </summary>
		public Troop()
		{
			id = 0;
			name = "";
			members = new List<dynamic>();
			pages = new List<dynamic>
			{ new Page() };
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
        /// Data class for troop members.
        /// </summary>
		public class Member
		{
            /// <summary>
            /// The enemy ID.
            /// </summary>
			public int enemy_id { get; set; }
            /// <summary>
            /// The troop member's X-coordinate.
            /// </summary>
			public int x { get; set; }
            /// <summary>
            /// The troop member's Y-coordinate.
            /// </summary>
			public int y { get; set; }
            /// <summary>
            /// Truth value of the [Appear Midway] option.
            /// </summary>
			public bool hidden { get; set; }
            /// <summary>
            /// Truth value of the [Immortal] option.
            /// </summary>
			public bool immortal { get; set; }

            /// <summary>
            /// Creates a new instance of an RPG.Troop.Member.
            /// </summary>
			public Member()
			{
				enemy_id = 0;
				x = 0;
				y = 0;
				hidden = false;
				immortal = false;
			}
		}

        /// <summary>
        /// Data class for battle events (pages).
        /// </summary>
		public class Page
		{
            /// <summary>
            /// Condition (<see cref="RPG.Troop.Page.Condition"/>).
            /// </summary>
			public Condition condition { get; set; }
            /// <summary>
            /// Span (0: battle, 1: turn, 2: moment).
            /// </summary>
			public int span { get; set; }
            /// <summary>
            /// Program contents. A collection of <see cref="RPG.EventCommand"/> objects.
            /// </summary>
			public List<dynamic> list { get; set; }

            /// <summary>
            /// Creates a new instance of an RPG.Troop.Page.
            /// </summary>
			public Page()
			{
				condition = new Condition();
				span = 0;
				list = new List<dynamic>
				{ new EventCommand() };
			}

            /// <summary>
            /// A database of battle event [Conditions].
            /// </summary>
			public class Condition
			{
                /// <summary>
                /// Truth value for whether the [Turn] condition is valid.
                /// </summary>
				public bool turn_valid { get; set; }
                /// <summary>
                /// Truth value for whether the [Enemy] condition is valid.
                /// </summary>
				public bool enemy_valid { get; set; }
                /// <summary>
                /// Truth value for whether the [Actor] condition is valid.
                /// </summary>
				public bool actor_valid { get; set; }
                /// <summary>
                /// Truth value for whether the [Switch] condition is valid.
                /// </summary>
				public bool switch_valid { get; set; }
                /// <summary>
                /// a and b values specified in the [Turn] condition. 
                /// To be input in the form a + bx.
                /// </summary>
				public int turn_a { get; set; }
                /// <summary>
                /// a and b values specified in the [Turn] condition. 
                /// To be input in the form a + bx.
                /// </summary>
				public int turn_b { get; set; }
                /// <summary>
                /// Troop member index specified in the [Enemy] condition (0..7).
                /// </summary>
				public int enemy_index { get; set; }
                /// <summary>
                /// HP percentage specified in the [Enemy] condition.
                /// </summary>
				public int enemy_hp { get; set; }
                /// <summary>
                /// Actor ID specified in the [Actor] condition.
                /// </summary>
				public int actor_id { get; set; }
                /// <summary>
                /// HP percentage specified in the [Actor] condition.
                /// </summary>
				public int actor_hp { get; set; }
                /// <summary>
                /// Switch ID specified in the [Switch] condition.
                /// </summary>
				public int switch_id { get; set; }

                /// <summary>
                /// Creates a new instance of an RPG.Troop.Page.Condition.
                /// </summary>
				public Condition()
				{
					turn_valid = false;
					enemy_valid = false;
					actor_valid = false;
					switch_valid = false;
					turn_a = 0;
					turn_b = 0;
					enemy_index = 0;
					enemy_hp = 50;
					actor_id = 1;
					actor_hp = 50;
					switch_id = 1;
				}
			}
		}
	}
}
