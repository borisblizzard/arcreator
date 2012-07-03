using System.Collections.Generic;

namespace RPG
{
	public class CommonEvent
	{
		public int id { get; set; }
		public string name { get; set; }
		public int trigger { get; set; }
		public int switch_id { get; set; }
		public List<EventCommand> list { get; set; }

		public CommonEvent()
		{
			id = 0;
			name = "";
			trigger = 0;
			switch_id = 1;
			list = new List<EventCommand>() { new EventCommand() };
		}
	}
}
