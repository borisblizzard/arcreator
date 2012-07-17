#region Using Directives

using System.Collections.Generic;

#endregion

namespace RPG
{
    /// <summary>
    /// Data class for animation.
    /// </summary>
	public class Animation : IRpgObject
	{
        /// <summary>
        /// The animation ID.
        /// </summary>
		public int id { get; set; }
        /// <summary>
        /// The animation name.
        /// </summary>
		public string name { get; set; }
        /// <summary>
        /// The animation's graphic file name.
        /// </summary>
		public string animation_name { get; set; }
        /// <summary>
        /// The adjustment value for the animation graphic's hue (0..360).
        /// </summary>
		public int animation_hue { get; set; }
        /// <summary>
        /// The animation's position (0: top, 1: middle, 2: bottom, 3: screen).
        /// </summary>
		public int position { get; set; }
        /// <summary>
        /// Number of frames.
        /// </summary>
		public int frame_max { get; set; }
        /// <summary>
        /// Frame contents. An <see cref="RPG.Animation.Frame"/> collection.
        /// </summary>
		public List<dynamic> frames { get; set; }
        /// <summary>
        /// Timing for SE and flash effects. An <see cref="RPG.Animation.Timing"/> collection.
        /// </summary>
		public List<dynamic> timings { get; set; }

        /// <summary>
        /// Creates a new instance of an RPG.Animation.
        /// </summary>
		public Animation()
		{
			id = 0;
			name = "";
			animation_name = "";
			animation_hue = 0;
			position = 1;
			frame_max = 1;
			frames = new List<dynamic>
			{ new Frame() };
			timings = new List<dynamic>
			{  };
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
        /// Data class for animation frames.
        /// </summary>
		public class Frame
		{
            /// <summary>
            /// Number of cells. Equivalent to the largest cell number in the frame set.
            /// </summary>
			public int cell_max { get; set; }
            /// <summary>
            /// 2-dimensional <see cref="Table"/> containing cell contents.
            /// Generally takes the form <c>cell_data[cell_index, data_index]</c>.
            /// <c>data_index</c> ranges from 0 to 7 and denotes various information 
            /// about a cell. 
            /// (0: pattern, 1: X-coordinate, 2: Y-coordinate, 3: zoom level, 4: angle of rotation, 5: horizontal flip, 6: opacity, 7: blending mode). 
            /// Patterns are 1 less than the number displayed in RPGXP; -1 indicates that that cell is not in use.
            /// </summary>
			public Table cell_data { get; set; }

            /// <summary>
            /// Creates a new instance of an RPG.Animation.Frame.
            /// </summary>
			public Frame()
			{
				cell_max = 0;
				cell_data = new Table(0, 0);
			}
		}

        /// <summary>
        /// Data class for the timing of an animation's SE and flash effects.
        /// </summary>
		public class Timing
		{
            /// <summary>
            /// Frame number. 1 less than the number displayed in RPGXP.
            /// </summary>
			public int frame { get; set; }
            /// <summary>
            /// SE, or sound effect (<see cref="RPG.AudioFile"/>).
            /// </summary>
			public AudioFile se { get; set; }
            /// <summary>
            /// Flash area (0: none, 1: target, 2: screen; 3: delete target).
            /// </summary>
			public int flash_scope { get; set; }
            /// <summary>
            /// Flash color (<see cref="RPG.Color"/>).
            /// </summary>
			public Color flash_color { get; set; }
            /// <summary>
            /// Flash duration.
            /// </summary>
			public int flash_duration { get; set; }
            /// <summary>
            /// Condition of the effect (0: none, 1: hit, 2: miss).
            /// </summary>
			public int condition { get; set; }

            /// <summary>
            /// Creates a new instance of an RPG.Animation.Timing.
            /// </summary>
			public Timing()
			{
				frame = 0;
				se = new AudioFile("", 80);
				flash_scope = 0;
				flash_color = new Color();
				flash_duration = 5;
				condition = 0;
			}
		}
	}
}
