using System.Collections.Generic;

namespace RPG
{
	public class MoveRoute
	{
		public bool repeat { get; set; }
		public bool skippable { get; set; }
		public List<dynamic> list { get; set; }

		public MoveRoute()
		{
			repeat = true;
			skippable = false;
			list = new List<dynamic>() { new MoveCommand() };
		}
	}
}
