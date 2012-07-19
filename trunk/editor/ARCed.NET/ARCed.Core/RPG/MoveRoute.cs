#region Using Directives

using System.Collections.Generic;

#endregion

namespace RPG
{
    /// <summary>
    /// Data class for the move route (movement route).
    /// </summary>
	public class MoveRoute
	{
        /// <summary>
        /// Truth value of the [Repeat Action] option.
        /// </summary>
		public bool repeat { get; set; }
        /// <summary>
        /// Truth value of the [Ignore if Can't Move] option.
        /// </summary>
		public bool skippable { get; set; }
        /// <summary>
        /// Program contents. A collection of <see cref="RPG.MoveCommand"/> objects.
        /// </summary>
		public List<dynamic> list { get; set; }

        /// <summary>
        /// Creates a new instance of an RPG.MoveRoute.
        /// </summary>
		public MoveRoute()
		{
			this.repeat = true;
			this.skippable = false;
			this.list = new List<dynamic>
			{ new MoveCommand() };
		}
	}
}
