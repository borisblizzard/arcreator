#region Using Directives

using System.Collections.Generic;

#endregion

namespace RPG
{
    /// <summary>
    /// Data class for the Event command.
    /// </summary>
	public class EventCommand
	{
        /// <summary>
        /// The event code.
        /// </summary>
		public int code { get; set; }
        /// <summary>
        /// The indent depth. 
        /// Usually 0; the [Conditional Branch] command, among others, 
        /// adds 1 with every step deeper.
        /// </summary>
		public int indent { get; set; }
        /// <summary>
        /// Collection containing the Move command arguments. 
        /// The contents vary for each command.
        /// </summary>
		public List<dynamic> parameters { get; set; }

        /// <summary>
        /// Creates a new instance of an RPG.EventCommand.
        /// </summary>
		public EventCommand() : 
			this(0, 0, new List<dynamic>()) { }

        /// <summary>
        /// Creates a new instance of an RPG.EventCommand.
        /// </summary>
        /// <param name="code">The event code.</param>
		public EventCommand(int code) : 
			this(code, 0, new List<dynamic>()) { }

        /// <summary>
        /// Creates a new instance of an RPG.EventCommand.
        /// </summary>
        /// <param name="code">The event code.</param>
        /// <param name="indent">The indent depth.</param>
		public EventCommand(int code, int indent) : 
			this(code, indent, new List<dynamic>()) { }

        /// <summary>
        /// Creates a new instance of an RPG.EventCommand.
        /// </summary>
        /// <param name="code">The event code.</param>
        /// <param name="indent">The indent depth.</param>
        /// <param name="parameters">Command arguments.</param>
		public EventCommand(int code, int indent, List<dynamic> parameters)
		{
			this.code = code;
			this.indent = indent;
			this.parameters = parameters;
		}
	}
}
