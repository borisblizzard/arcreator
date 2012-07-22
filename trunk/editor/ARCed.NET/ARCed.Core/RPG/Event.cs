#region Using Directives

using System.Collections.Generic;

#endregion

namespace RPG
{
    /// <summary>
    /// Data class for map events.
    /// </summary>
	public class Event : IRpgObject
	{
        /// <summary>
        /// The event ID.
        /// </summary>
		public int id { get; set; }
        /// <summary>
        /// The event name.
        /// </summary>
		public string name { get; set; }
        /// <summary>
        /// The event's X-coordinate on the map.
        /// </summary>
		public int x { get; set; }
        /// <summary>
        /// The event's Y-coordinate on the map.
        /// </summary>
		public int y { get; set; }
        /// <summary>
        /// The Events pages. A collection of <see cref="RPG.Event.Page"/> objects.
        /// </summary>
        public List<dynamic> pages { get; set; }

		/// <summary>
		/// Creates a new instance of an RPG.Event.
		/// </summary>
		public Event() : this(0, 0) { }

	    /// <summary>
        /// Creates a new instance of an RPG.Event.
        /// </summary>
        /// <param name="x">The event's X-coordinate on the map.</param>
        /// <param name="y">The event's Y-coordinate on the map.</param>
		public Event(int x = 0, int y = 0)
		{
			this.id = 0;
			this.name = "";
			this.x = x;
			this.y = y;
            this.pages = new List<dynamic>
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
        /// Data class for the event page.
        /// </summary>
		public class Page
		{
            /// <summary>
            /// The event condition.
            /// </summary>
			public Condition condition { get; set; }
            /// <summary>
            /// The event graphic.
            /// </summary>
			public Graphic graphic { get; set; }
            /// <summary>
            /// Type of movement (0: fixed, 1: random, 2: approach, 3: custom).
            /// </summary>
			public int move_type { get; set; }
            /// <summary>
            /// Movement speed (1: slowest, 2: slower, 3: slow, 4: fast, 5: faster, 6: fastest).
            /// </summary>
			public int move_speed { get; set; }
            /// <summary>
            /// Movement frequency (1: lowest, 2: lower, 3: low ,4: high, 5: higher, 6: highest).
            /// </summary>
			public int move_frequency { get; set; }
            /// <summary>
            /// Movement route. 
            /// Referenced only when the movement type is set to Custom.
            /// </summary>
			public MoveRoute move_route { get; set; }
            /// <summary>
            /// Truth value of the [Moving Animation] option.
            /// </summary>
			public bool walk_anime { get; set; }
            /// <summary>
            /// Truth value of the [Stopped Animation] option.
            /// </summary>
			public bool step_anime { get; set; }
            /// <summary>
            /// Truth value of the [Fixed Direction] option.
            /// </summary>
			public bool direction_fix { get; set; }
            /// <summary>
            /// Truth value of the [Move Through] option.
            /// </summary>
			public bool through { get; set; }
            /// <summary>
            /// Truth value of the [Always On Top] option.
            /// </summary>
			public bool always_on_top { get; set; }
            /// <summary>
            /// Event trigger.
            /// (0: action button, 1: contact with player, 2: contact with event, 3: autorun, 4: parallel processing).
            /// </summary>
			public int trigger { get; set; }
            /// <summary>
            /// Program contents. A collection of <see cref="RPG.EventCommand"/> objects.
            /// </summary>
			public List<dynamic> list { get; set; }

            /// <summary>
            /// Creates a new instance of an RPG.Event.Page.
            /// </summary>
			public Page()
			{
				this.condition = new Condition();
				this.graphic = new Graphic();
				this.move_type = 0;
				this.move_speed = 3;
				this.move_frequency = 3;
				this.move_route = new MoveRoute();
				this.walk_anime = true;
				this.step_anime = false;
				this.direction_fix = false;
				this.through = false;
				this.always_on_top = false;
				this.trigger = 0;
                this.list = new List<dynamic>
                { new EventCommand() };
			}

            /// <summary>
            /// Data class for event page conditions.
            /// </summary>
			public class Condition
			{
                /// <summary>
                /// Truth value for whether the first [Switch] condition is valid.
                /// </summary>
				public bool switch1_valid { get; set; }
                /// <summary>
                /// Truth value for whether the second [Switch] condition is valid.
                /// </summary>
				public bool switch2_valid { get; set; }
                /// <summary>
                /// Truth value for whether the [Variable] condition is valid.
                /// </summary>
				public bool variable_valid { get; set; }
                /// <summary>
                /// Truth value for whether the [Self Switch] condition is valid.
                /// </summary>
				public bool self_switch_valid { get; set; }
                /// <summary>
                /// If the first [Switch] condition is valid, the ID of that switch.
                /// </summary>
				public int switch1_id { get; set; }
                /// <summary>
                /// If the second [Switch] condition is valid, the ID of that switch.
                /// </summary>
				public int switch2_id { get; set; }
                /// <summary>
                /// If the [Variable] condition is valid, the ID of that variable.
                /// </summary>
				public int variable_id { get; set; }
                /// <summary>
                /// If the [Variable] condition is valid, the standard value of that variable (x and greater).
                /// </summary>
				public int variable_value { get; set; }
                /// <summary>
                /// If the [Self Switch] condition is valid, the letter of that self switch ("A".."D").
                /// </summary>
				public string self_switch_ch { get; set; }

                /// <summary>
                /// Creates a new instance of an RPG.Event.Page.Condition.
                /// </summary>
				public Condition()
				{
					this.switch1_valid = false;
					this.switch2_valid = false;
					this.variable_valid = false;
					this.self_switch_valid = false;
					this.switch1_id = 1;
					this.switch2_id = 1;
					this.variable_id = 1;
					this.variable_value = 0;
					this.self_switch_ch = "A";
				}
			}

            /// <summary>
            /// Data class for the Event page [Graphics].
            /// </summary>
			public class Graphic
			{
                /// <summary>
                /// The tile ID. If the specified graphic is not a tile, this value is 0.
                /// </summary>
				public int tile_id { get; set; }
                /// <summary>
                /// The character's graphic file name.
                /// </summary>
				public string character_name { get; set; }
                /// <summary>
                /// The adjustment value for the character graphic's hue (0..360).
                /// </summary>
				public int character_hue { get; set; }
                /// <summary>
                /// The direction in which the character is facing (2: down, 4: left, 6: right, 8: up).
                /// </summary>
				public int direction { get; set; }
                /// <summary>
                /// The character's pattern (0..3).
                /// </summary>
				public int pattern { get; set; }
                /// <summary>
                /// The character's opacity.
                /// </summary>
				public int opacity { get; set; }
                /// <summary>
                /// The character's blending mode.
                /// </summary>
				public int blend_type { get; set; }

                /// <summary>
                /// Creates a new instance of an RPG.Event.Graphic.
                /// </summary>
				public Graphic()
				{
					this.tile_id = 0;
					this.character_name = "";
					this.character_hue = 0;
					this.direction = 2;
					this.pattern = 0;
					this.opacity = 255;
					this.blend_type = 0;
				}
			}
		}
	}
}
