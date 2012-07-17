#region Using Directives

using System.Collections.Generic;

#endregion

namespace RPG
{
    /// <summary>
    /// Data class for the Move command.
    /// </summary>
	public class MoveCommand
	{
        /// <summary>
        /// Move command code.
        /// </summary>
		public int code { get; set; }
        /// <summary>
        /// Array containing the Move command arguments. 
        /// The contents vary for each command.
        /// </summary>
		public List<dynamic> parameters { get; set; }

        /// <summary>
        /// Creates a new instance of an RPG.MoveCommand.
        /// </summary>
		public MoveCommand() : 
			this(0, new List<dynamic>()) { }

        /// <summary>
        /// Creates a new instance of an RPG.MoveCommand.
        /// </summary>
        /// <param name="code">Move command code.</param>
		public MoveCommand(int code) : 
			this(code, new List<dynamic>()) { }

        /// <summary>
        /// Creates a new instance of an RPG.MoveCommand.
        /// </summary>
        /// <param name="code">Move command code.</param>
        /// <param name="parameters">Move command arguments.</param>
		public MoveCommand(int code, List<dynamic> parameters)
		{
			this.code = code;
			this.parameters = parameters;
		}
	}
}
