using System.Collections.Generic;

namespace RPG
{
	public class MoveCommand
	{
		public int code { get; set; }
		public List<dynamic> parameters { get; set; }

		public MoveCommand() : 
			this(0, new List<dynamic>()) { }

		public MoveCommand(int code) : 
			this(code, new List<dynamic>()) { }

		public MoveCommand(int code, List<dynamic> parameters)
		{
			this.code = code;
			this.parameters = parameters;
		}
	}
}
