#region Using Directives

using System.Collections.Generic;

#endregion

namespace RPG
{
    /// <summary>
    /// Data class for common events.
    /// </summary>
	public class CommonEvent : IRpgObject
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
        /// The event trigger (0: none, 1: autorun; 2: parallel).
        /// </summary>
		public int trigger { get; set; }
        /// <summary>
        /// The condition switch ID.
        /// </summary>
		public int switch_id { get; set; }
        /// <summary>
        /// List of event commands. A collection of <see cref="RPG.EventCommand"/> pbjects.
        /// </summary>
		public List<dynamic> list { get; set; }

        /// <summary>
        /// Creates a new instance of an RPG.CommonEvent.
        /// </summary>
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
