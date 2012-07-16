#region Using Directives

using System.Collections.Generic;

#endregion

namespace RPG
{
	public class EventCommand
	{
		public int code { get; set; }
		public int indent { get; set; }
		public List<dynamic> parameters { get; set; }

		public EventCommand() : 
			this(0, 0, new List<dynamic>()) { }

		public EventCommand(int code) : 
			this(code, 0, new List<dynamic>()) { }

		public EventCommand(int code, int indent) : 
			this(code, indent, new List<dynamic>()) { }

		public EventCommand(int code, int indent, List<dynamic> parameters)
		{
			this.code = code;
			this.indent = indent;
			this.parameters = parameters;
		}
	}
}
