#region Using Directives

using System;
using System.Collections.Generic;
using System.Reflection;
using System.Windows.Forms;
using ARCed.EventBuilder;
using ARCed.Helpers;
using RPG;
using Color = System.Drawing.Color;

#endregion

namespace ARCed.Controls
{
	/// <summary>
	/// Control for parsing and displaying RPG.EventCommands formatted and colorized
	/// </summary>
	public partial class EventTextBox : RichTextBox
	{
		public EventTextBox()
		{
			this.InitializeComponent();
		}

		/// <summary>
		/// Appends the given string and draws it in the specified color
		/// </summary>
		/// <param name="text">String to append to the end of the current text.</param>
		/// <param name="color">Color to use to draw the string.</param>
		public void AppendText(string text, Color color)
		{
			int start = Text.Length;
			base.AppendText(text);
			Select(start, text.Length);
			SelectionColor = color;
		}

		#region Public Methods

		/// <summary>
		/// Converts an array list of RPG.EventCommands and converts it into 
		/// a format that can be displayed in the event editor.
		/// </summary>
		/// <param name="list">Collection of commands</param>
		/// <remarks>Painting of the TextBox is automatically suspended until 
		/// all commands are translated and added to the control.</remarks>
		public void Parse(List<dynamic> list)
		{
			this.SuspendPainting();
			Clear();
			foreach (EventCommand command in list)
				this.Translate(command.code, command.indent, command.parameters);
			this.ResumePainting(true);
		}

		#endregion

		#region Private Methods

		/// <summary>
		/// Translates the specified event code and arguments into a formatted string
		/// </summary>
		/// <param name="code">Event code.</param>
        /// <param name="indent">Indent level</param>
		/// <param name="args">Array of game event parameters.</param>
		/// <returns>Formatted string.</returns>
		private void Translate(int code, int indent, dynamic args)
		{
			AppendText(new string(' ', indent *  4));
			string methodName = String.Format("Command{0}", code);
			MethodInfo info = typeof(EventTextBox).GetMethod(methodName, 
				BindingFlags.NonPublic | BindingFlags.Instance);
			if (info != null)
				info.Invoke(this, new object[] { args });
			else 
				Console.WriteLine("Missing Method: {0}", methodName);
			AppendText("\n");
		}

		/// <summary>
		/// Blank Command
		/// </summary>
		private void Command0(dynamic args)
		{
			AppendText("@>");
		}

		/// <summary>
		/// Show Text
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command101(dynamic args)
		{
			AppendText(String.Format("@>Text: {0}", args[0]));
		}

		/// <summary>
		/// Show Text (Multi-Line)
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command401(dynamic args)
		{
			AppendText(String.Format("      : {0}", args[0]));
		}

		/// <summary>
		/// Show Choices
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command102(dynamic args)
		{
			AppendText(String.Format("@>Show Choices: {0}", String.Join(", ", args[0])));
		}

		/// <summary>
		/// When [**]
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command402(dynamic args)
		{
			AppendText(String.Format(" : When [{0}]", args[1]));
		}

		/// <summary>
		/// When Cancel
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command403(dynamic args)
		{
			AppendText(" : When Cancel");
		}

		/// <summary>
		/// Branch End (Choices)
		/// </summary>
		private void Command404(dynamic args)
		{
			AppendText(" : Branch End");
		}

		/// <summary>
		/// Input Number
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command103(dynamic args)
		{
			AppendText(String.Format("Input Number: [{0}], {1} digit(s)",
				Project.Variables[args[0]].ToString(), args[1]));
		}

		/// <summary>
		/// Change Text Options
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command104(dynamic args)
		{
			AppendText(String.Format("@>Change Text Options: {0}, {1}",
				new[] { "Top", "Middle", "Bottom" }[args[0]], args[1] == 0 ? "Show" : "Hide"));
		}

		/// <summary>
		/// Button Input Processing
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command105(dynamic args)
		{
			AppendText(String.Format("@>Button Input Processing: [{0}]",
				Project.Variables[args[0]].ToString()));
		}

		/// <summary>
		/// Wait
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command106(dynamic args)
		{
			AppendText(String.Format("@>Wait: {0} frame(s)", args[0]));
		}

		/// <summary>
		/// Comment
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command108(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Comment: {0}", args[0]), Color.Green);
		}

		/// <summary>
		/// Comment (Multi-line)
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command408(dynamic args)
		{
			AppendText(" :");
			this.AppendText(String.Format("       : {0}", args[0]), Color.Green);
		}

		/// <summary>
		/// Conditional Branch
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command111(dynamic args)
		{
			this.AppendText("@>Conditional Branch: ", Color.Blue);
			string text = "";
			int code = args[0];
			switch (code)
			{
				case 0: // Switch
				{
					text = String.Format("Switch [{0}] == {1}",
						Project.Switches[args[1]].ToString(), args[2] == 0 ? "ON" : "OFF");
					break;
				}
				case 1: // Variable
				{
					string varName = Project.Variables[args[1]].ToString();
					string oper = new[] { "==", ">=", "<=", ">", "<", "!=" }[args[4]];
					if (args[2] == 0) // Constant
					{
						text = String.Format("Variable [{0}] {1} {2}", varName, oper, args[3]);
					}
					else // Variable
					{
						text = String.Format("Variable [{0}] {1} Variable: [{2}]",
							varName, oper, Project.Variables[args[3]].ToString());
					}
					break;
				}
				case 2: // Self-Switch
				{
					text = String.Format("Self Switch {0} == {1}", "ABCD"[args[1]], args[2] == 0 ? "ON" : "OFF");
					break;
				}
				case 3: // Timer
				{
					int secs = args[1];
					text = String.Format("Timer {0} min {1} sec or {2}",
						secs / 60, secs % 60, args[2] == 0 ? "more" : "less");
					break;
				}
				case 4: // Actor
				{
					string actorName = Project.Data.Actors[args[1]].ToString();
					int oper = args[2];
					switch (oper)
					{
						case 0: // In Party
						{
							text = String.Format("[{0}] is in party", actorName);
							break;
						}
						case 1: // Name Applied
						{
							text = String.Format("[{0}] is name '{1}' applied", actorName, args[3]);
							break;
						}
						case 2: // Skill Learned
						{
							text = String.Format("[{0}] is [{1}] learned", actorName,
								Project.Data.Skills[args[3]].ToString());
							break;
						}
						case 3: // Weapon Equipped
						{
							text = String.Format("[{0}] is [{1}] equipped", actorName,
								Project.Data.Weapons[args[3]].ToString());
							break;
						}
						case 4: // Armor Equipped
						{
							text = String.Format("[{0}] is [{1}] equipped", actorName,
								Project.Data.Armors[args[3]].ToString());
							break;
						}
						case 5: // State Inflicted
						{
							text = String.Format("[{0}] is [{1}] inflicted", actorName,
								Project.Data.States[args[3]].ToString());
							break;
						}
					}
					break;
				}
				case 5: // Enemy
				{
					// TODO: Implement once event builder is complete for easier testing
					break;
				}
				case 6: // Character
				{
					// TODO: Implement once event builder is complete for easier testing
					break;
				}
				case 7: // Gold
				{
					text = String.Format("Gold {0} or {1}", args[1],
						args[2] == 0 ? "more" : "less");
					break;
				}
				case 8: // Item in Inventory
				{
					text = String.Format("[{0}] in inventory",
						Project.Data.Items[args[1]].ToString());
					break;
				}
				case 9: // Weapon in Inventory
				{
					text = String.Format("[{0}] in inventory",
						Project.Data.Weapons[args[1]].ToString());
					break;
				}
				case 10: // Armor in Inventory
				{
					text = String.Format("[{0}] in inventory",
						Project.Data.Armors[args[1]].ToString());
					break;
				}
				case 11: // Button
				{
					var buttons = new[] { "", "", "Down", "", "Left", "", "Right", 
						"", "Up", "", "", "A", "B", "C", "X", "Y", "Z", "L", "R" };
					text = String.Format("The {0} button is being pressed", buttons[args[1]]);
					break;
				}
				case 12: // Script
				{
					text = String.Format("Script: {0}", args[1]);
					break;
				}
			}
			if (!String.IsNullOrEmpty(text))
				this.AppendText(text, Color.Blue);
		}

		/// <summary>
		/// Else
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command411(dynamic args)
		{
			AppendText(" : ");
			this.AppendText("Else", Color.Blue);
		}

		/// <summary>
		/// Branch End (Conditional Branch)
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command412(dynamic args)
		{
			AppendText(" : ");
			this.AppendText("Branch End", Color.Blue);
		}

		/// <summary>
		/// Loop
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command112(dynamic args)
		{
			AppendText("@>");
			this.AppendText("Loop", Color.Blue);
		}

		/// <summary>
		/// End Loop
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command413(dynamic args)
		{
			AppendText(" : ");
			this.AppendText("Repeat Above", Color.Blue);
		}

		/// <summary>
		/// Break Loop
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command113(dynamic args)
		{
			AppendText("@>");
			this.AppendText("Break Loop", Color.Blue);
		}

		/// <summary>
		/// Exit Event Processing
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command115(dynamic args)
		{
			AppendText("@>");
			this.AppendText("Exit Event Processing", Color.Blue);
		}

		/// <summary>
		/// Erase Event
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command116(dynamic args)
		{
			AppendText("@>");
			this.AppendText("Erase Event", Color.Blue);
		}

		/// <summary>
		/// Call Common Event
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command117(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Call Common Event: [{0}]",
				Project.Data.CommonEvents[args[0]].ToString()), Color.Blue);
		}

		/// <summary>
		/// Label
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command118(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Label: {0}", args[0]), Color.Blue);
		}

		/// <summary>
		/// Jump to Label
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command119(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("JumpToLabel: {0}", args[0]), Color.Blue);
		}

		/// <summary>
		/// Control Switches
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command121(dynamic args)
		{
			int id1 = args[0];
			int id2 = args[1];
			string oper = args[2] == 0 ? "ON" : "OFF";
			AppendText("@>");
			if (id1 == id2)
			{
				this.AppendText(String.Format("Control Switches: [{0}] = {1}",
					Project.Switches[id1].ToString(), oper), Color.Red);
			}
			else
			{
				this.AppendText(String.Format("Control Switches: [{0}..{1}] = {2}",
					id1, id2, oper), Color.Red);
			}
		}

		/// <summary>
		/// Control Variables
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command122(dynamic args)
		{
			AppendText("@>");
			int id1 = args[0];
			int id2 = args[1];
			int operCode = args[3];
			string var;
			if (id1 == id2)
				var = String.Format("Control Variables: [{0}]", Project.Variables[id1].ToString());
			else
				var = String.Format("Control Variables: [{0:d4}..{1:d4}]", id1, id2);
			string oper = new[] { "=", "+=", "-=", "*=", "/=", "%=" }[args[2]];
			string operand = "";
			switch (operCode)
			{
				case 0: // Constant
				operand = args[4].ToString(); break;
				case 1: // Variable
				operand = String.Format("Variable [{0}]", Project.Variables[args[4]].ToString());
				break;
				case 2: // Random
				operand = String.Format("Random No. ({0}..{1}", args[4], args[5]);
				break;
				case 3: // Item
				operand = String.Format("[{0}] In Inventory", Project.Data.Items[args[4]].ToString());
				break;
				case 4: // Actor
				string actor = Project.Data.Actors[args[4]].ToString();
				string param = new[] { "Level", "EXP", "HP", "SP", "MaxHP", "MaxSP",
						"STR", "DEX", "AGI", "INT", "ATK", "PDEF", "MDEF", "EVA" }[args[5]];
				operand = String.Format("[{0}]'s {1}", actor, param);
				break;
				case 5: // Enemy
				// TODO: Implement
				break;
				case 6: // Character
				// TODO: Implement
				break;
				case 7: // Other
				operand = new[] { "Map ID", "Party Members", "Gold", "Steps",
						"Play Time", "Timer", "Save Count" }[args[4]];
				break;
			}
			this.AppendText(String.Format("{0} {1} {2}", var, oper, operand), Color.Red);
		}

		/// <summary>
		/// Control Self-Switch
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command123(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Control Self Switch: {0} = {1}",
				args[0], args[1] == 0 ? "ON" : "OFF"), Color.Red);
		}

		/// <summary>
		/// Control Timer
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command124(dynamic args)
		{
			AppendText("@>");
			if (args[0] == 0)
			{
				int secs = args[1];
				this.AppendText(String.Format("Control Timer: Startup ({0} min. {1} sec.)",
					secs / 60, secs % 60), Color.Red);
			}
			else
				this.AppendText("Control Timer: Stop", Color.Red);
		}

		/// <summary>
		/// Change Gold
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command125(dynamic args)
		{
			AppendText("@>");
			string oper = args[0] == 0 ? "+" : "-";
			if (args[1] == 0) // Constant
			{
				this.AppendText(String.Format("Change Gold: {0}{1}", oper, args[2]), Color.Red);
			}
			else // Variable
			{
				this.AppendText(String.Format("Change Gold: {0}Variable [{1}]",
					oper, Project.Variables[args[2]].ToString()), Color.Red);
			}
		}

		/// <summary>
		/// Change Items
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command126(dynamic args)
		{
			AppendText("@>");
			string name = Project.Data.Items[args[0]].ToString();
			string oper = args[1] == 0 ? "+" : "-";
			if (args[2] == 0) // Constant
			{
				this.AppendText(String.Format("Change Items: [{0}], {1}{2}",
					name, oper, args[3]), Color.Red);
			}
			else // Variable
			{
				this.AppendText(String.Format("Change Items: [{0}], {1}Variable [{2}]",
					name, oper, Project.Variables[args[3]].ToString()), Color.Red);
			}
		}

		/// <summary>
		/// Change Weapons
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command127(dynamic args)
		{
			AppendText("@>");
			string name = Project.Data.Weapons[args[0]].ToString();
			string oper = args[1] == 0 ? "+" : "-";
			if (args[2] == 0) // Constant
			{
				this.AppendText(String.Format("Change Weapons: [{0}], {1}{2}",
					name, oper, args[3]), Color.Red);
			}
			else // Variable
			{
				this.AppendText(String.Format("Change Weapons: [{0}], {1}Variable [{2}]",
					name, oper, Project.Variables[args[3]].ToString()), Color.Red);
			}
		}

		/// <summary>
		/// Change Armors
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command128(dynamic args)
		{
			AppendText("@>");
			string name = Project.Data.Armors[args[0]].ToString();
			string oper = args[1] == 0 ? "+" : "-";
			if (args[2] == 0) // Constant
			{
				this.AppendText(String.Format("Change Armors: [{0}], {1}{2}",
					name, oper, args[3]), Color.Red);
			}
			else // Variable
			{
				this.AppendText(String.Format("Change Armors: [{0}], {1}Variable [{2}]",
					name, oper, Project.Variables[args[3]].ToString()), Color.Red);
			}
		}

		/// <summary>
		/// Change Party Member
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command129(dynamic args)
		{
			AppendText("@>");
			string actorName = Project.Data.Actors[args[0]].ToString();
			if (args[1] == 0) // Add
			{
				this.AppendText(String.Format("Change Party Member: Add [{0}]{1}",
					actorName, args[2] == 0 ? ", Initialize" : ""), Color.Red);
			}
			else // Remove
			{
				this.AppendText(String.Format("Change Party Member: Remove [{0}]",
					actorName), Color.Red);
			}
		}

		/// <summary>
		/// Change Windowskin
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command131(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Change Windowskin: '{0}'", args[0]), Color.Magenta);
		}

		/// <summary>
		/// Change Battle BGM
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command132(dynamic args)
		{
			AppendText("@>");
			AudioFile bgm = args[0];
			this.AppendText(String.Format("Change Battle BGM: '{0}', {1}, {2}",
				bgm.name, bgm.volume, bgm.pitch), Color.Magenta);
		}

		/// <summary>
		/// Change Battle End ME
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command133(dynamic args)
		{
			AppendText("@>");
			AudioFile me = args[0];
			this.AppendText(String.Format("Change Battle End ME: '{0}', {1}, {2}",
				me.name, me.volume, me.pitch), Color.Magenta);
		}

		/// <summary>
		/// Change Save Access
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command134(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Change Save Access: {0}",
				args[0] == 0 ? "Disable" : "Enable"), Color.Magenta);
		}

		/// <summary>
		/// Change Menu Access
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command135(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Change Menu Access: {0}",
				args[0] == 0 ? "Disable" : "Enable"), Color.Magenta);
		}

		/// <summary>
		/// Change Encounter
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command136(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Change Encounter: {0}",
				args[0] == 0 ? "Disable" : "Enable"), Color.Magenta);
		}

		/// <summary>
		/// Transfer Player
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command201(dynamic args)
		{
			AppendText("@>");
			string text;
			int mapId = args[1];
			int mapX = args[2];
			int mapY = args[3];
			string dir = new[] { "", ", Down", ", Left", ", Right", ", Up" }[args[4] / 2];
			string fade = args[5] == 0 ? "" : ", No Fade";
			if (args[0] == 0) // Direct Appointment
			{
				text = String.Format("Transfer Player:[{0}], ({1:d3}, {2:d3}){3}{4}",
					ControlHelper.GetMapLabel(mapId), mapX, mapY, dir, fade);
			}
			else // Appoint with Variables
			{
				text = String.Format("Transfer Player:Variable [{0}][{1}][{2}]{3}{4}",
					Project.Variables[mapId], Project.Variables[mapX],
					Project.Variables[mapY], dir, fade);
			}
			this.AppendText(text, Color.Brown);
		}

		/// <summary>
		/// Set Event Location
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command202(dynamic args)
		{
			// TODO: Implement
		}

		/// <summary>
		/// Scroll Map
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command203(dynamic args)
		{
			AppendText("@>");
			string dir = new[] { "", "Down", "Left", "Right", "Up" }[args[0]];
			this.AppendText(String.Format("Scroll Map: {0}, {1}, {2}",
				dir, args[1], args[2]), Color.Brown);
		}

		/// <summary>
		/// Change Map Settings
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command204(dynamic args)
		{
			AppendText("@>");
			int code = args[0];
			string text = "Change Map Settings: ";
			switch (code)
			{
				case 0: // Panorama
				text += String.Format("Panorama = '{0}', {1}", args[1], args[2]);
				break;
				case 1: // Fog
				string blend = new[] { "Normal", "Add", "Sub" }[args[4]];
				text += String.Format("Fog = {0}, {1}, {2}, {3}, {4}, {5}, {6}",
					args[1], args[2], args[3], blend, args[5], args[6], args[7]);
				break;
				case 2: // Battleback
				text += String.Format("Battleback = '{0}'", args[1]);
				break;
			}
			this.AppendText(text, Color.Brown);
		}

		/// <summary>
		/// Change Fog Color Tone
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command205(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Change Fog Color Tone: {0}, @{1}",
				args[0], args[1]), Color.Brown);
		}

		/// <summary>
		/// Change Fog Opacity
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command206(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Change Fog Opacity: {0}, @{1}",
				args[0], args[1]), Color.Brown);
		}

		/// <summary>
		/// Show Animation
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command207(dynamic args)
		{
			AppendText("@>");
			int id = args[0];
			// TODO: Implement getting map event names
			string name = (id == -1 ? "Player" : (id == 0 ? "This Event" : "[IMPLEMENT]"));
			this.AppendText(String.Format("Show Animation: {0}, [{1}]", name,
				Project.Data.Animations[args[1]]), Color.Brown);
		}

		/// <summary>
		/// Change Transparent Flag
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command208(dynamic args)
		{
			this.AppendText(String.Format("Change Transparent Flag: {0}",
				args[0] == 0 ? "Transparency" : "Normal"), Color.Brown);
		}

		/// <summary>
		/// Set Move Route
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command209(dynamic args)
		{
			AppendText("@>");
			int id = args[0];
			MoveRoute route = args[1];
			// TODO: Implement getting map event names
			string name = (id == -1 ? "Player" : (id == 0 ? "This Event" : "[IMPLEMENT]"));
			if (route.repeat || route.skippable)
			{
				string repeat = route.repeat ? "Repeat" : "";
				string skip = route.skippable ? ", Ignore If Can't Move" : "";
				this.AppendText(String.Format("Set Move Route: {0} ({1}{2})",
					name, repeat, skip), Color.Brown);
			}
			else
				this.AppendText(String.Format("Set Move Route: {0}", name), Color.Brown);
		}

		/// <summary>
		/// Move Command
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command509(dynamic args)
		{
			AppendText(" :");
			this.AppendText(String.Format("              :$>{0}",
				TranslateMove(args[0])), Color.Brown);
		}

		/// <summary>
		/// Wait for Move's Completion
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command210(dynamic args)
		{
			AppendText("@>Wait for Move's Completion");
		}

		/// <summary>
		/// Prepare for Transition
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command221(dynamic args)
		{
			AppendText("@>");
			this.AppendText("Prepare for Transition", Color.YellowGreen);
		}

		/// <summary>
		/// Execute Transition
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command222(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Execute Transition: '{0}'", args[0]), Color.YellowGreen);
		}

		/// <summary>
		/// Change Screen Color Tone
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command223(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Change Screen Color Tone: ({0}), @{1}",
				args[0], args[1]), Color.YellowGreen);
		}

		/// <summary>
		/// Screen Flash
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command224(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Screen Flash: ({0}), @{1}",
				args[0], args[1]), Color.YellowGreen);
		}

		/// <summary>
		/// Screen Shake
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command225(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Screen Shake: {0}, {1}, @{2}",
				args[0], args[1]), Color.YellowGreen);
		}

		/// <summary>
		/// Show Picture
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command231(dynamic args)
		{
			AppendText("@>");
			string text;
			int picNum = args[0];
			string name = args[1];
			string origin = args[2] == 0 ? "Upper Left" : "Center";
			int x = args[4];
			int y = args[5];
			int zoomX = args[6];
			int zoomY = args[7];
			int opacity = args[8];
			string blend = new[] { "Normal", "Add", "Sub" }[args[9]];
			if (args[3] == 0) // Constant
			{
				text = String.Format("Show Picture: {0}, '{1}', {2} ({3}, {4}), ({5}%, {6}%), {7}, {8}",
					picNum, name, origin, x, y, zoomX, zoomY, opacity, blend);
			}
			else // Variable
			{
				text = String.Format("Show Picture: {0}, '{1}', {2} (Variable [{3:d4}][{4:d4}]), ({5}%, {6}%), {7}, {8}",
					picNum, name, origin, x, y, zoomX, zoomY, opacity, blend);
			}
			this.AppendText(text, Color.Purple);
		}

		/// <summary>
		/// Move Picture
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command232(dynamic args)
		{
			AppendText("@>");
			string text;
			int picNum = args[0];
			string frames = args[1];
			string origin = args[2] == 0 ? "Upper Left" : "Center";
			int x = args[4];
			int y = args[5];
			int zoomX = args[6];
			int zoomY = args[7];
			int opacity = args[8];
			string blend = new[] { "Normal", "Add", "Sub" }[args[9]];
			if (args[3] == 0) // Constant
			{
				text = String.Format("Move Picture: {0}, @{1}, {2} ({3}, {4}), ({5}%, {6}%), {7}, {8}",
					picNum, frames, origin, x, y, zoomX, zoomY, opacity, blend);
			}
			else // Variable
			{
				text = String.Format("Move Picture: {0}, @{1}, {2} (Variable [{3:d4}][{4:d4}]), ({5}%, {6}%), {7}, {8}",
					picNum, frames, origin, x, y, zoomX, zoomY, opacity, blend);
			}
			this.AppendText(text, Color.Purple);
		}

		/// <summary>
		/// Rotate Picture
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command233(dynamic args)
		{
			AppendText("@>");
			string oper = args[1] >= 0 ? "+" : "";
			this.AppendText(String.Format("Rotate Picture: {0}, {1}{2}",
				args[0], oper, args[1]), Color.Purple);
		}

		/// <summary>
		/// Change Picture Color Tone
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command234(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Change Picture Color Tone: {0}, ({1}), @{2}",
				args[0], args[1], args[2]), Color.Purple);
		}

		/// <summary>
		/// Erase Picture
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command235(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Erase Picture: {0}", args[0]), Color.Purple);
		}

		/// <summary>
		/// Set Weather Effects
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command236(dynamic args)
		{
			AppendText("@>");
			string type = new[] { "None", "Rain", "Storm", "Snow" }[args[0]];
			int power = args[0] == 0 ? "" : ", " + args[1];
			this.AppendText(String.Format("Set Weather Effects: {0}{1}, @{2}",
				args[0], power, args[2]), Color.Purple);
		}

		/// <summary>
		/// Play BGM
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command241(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Play BGM: {0}", args[0]), Color.Teal);
		}

		/// <summary>
		/// Fade Out BGM
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command242(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Fade Out BGM: {0} sec.", args[0]), Color.Teal);
		}

		/// <summary>
		/// Play BGS
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command245(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Play BGS: {0}", args[0]), Color.Teal);
		}

		/// <summary>
		/// Fade Out BGS
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command246(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Fade Out BGS: {0} sec.", args[0]), Color.Teal);
		}

		/// <summary>
		/// Memorize BGM/BGS
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command247(dynamic args)
		{
			AppendText("@>");
			this.AppendText("Memorize BGM/BGS", Color.Teal);
		}

		/// <summary>
		/// Restore BGM/BGS
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command248(dynamic args)
		{
			AppendText("@>");
			this.AppendText("Restore BGM/BGS", Color.Teal);
		}

		/// <summary>
		/// Play ME
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command249(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Play ME: {0}", args[0]), Color.Teal);
		}

		/// <summary>
		/// Play SE
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command250(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Play SE: {0}", args[0]), Color.Teal);
		}

		/// <summary>
		/// Stop SE
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command251(dynamic args)
		{
			AppendText("@>");
			this.AppendText("Stop SE", Color.Teal);
		}

		/// <summary>
		/// Battle Processing
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command301(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Battle Processing: {0}",
				Project.Data.Troops[args[0]].name), Color.Orange);
		}

		/// <summary>
		/// If Win
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command601(dynamic args)
		{
			AppendText(" : ");
			this.AppendText("If Win", Color.Orange);
		}

		/// <summary>
		/// If Escape
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command602(dynamic args)
		{
			AppendText(" : ");
			this.AppendText("If Escape", Color.Orange);
		}

		/// <summary>
		/// If Lose
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command603(dynamic args)
		{
			AppendText(" : ");
			this.AppendText("If Lose", Color.Orange);
		}

		/// <summary>
		/// End Branch (Battle Processing)
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command604(dynamic args)
		{
			AppendText(" : ");
			this.AppendText("Branch End", Color.Orange);
		}

		/// <summary>
		/// Shop Processing
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command302(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Shop Processing: [{0}]",
				GetItemName(args[0], args[1])), Color.Orange);
		}

		/// <summary>
		/// Shop Good
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command605(dynamic args)
		{
			AppendText(" :");
			this.AppendText(String.Format("               : [{0}]",
				GetItemName(args[0], args[1])), Color.Orange);
		}

		/// <summary>
		/// Name Input Processing
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command303(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Name Input Processing: [{0}], {1} characters",
				Project.Data.Actors[args[0]], args[1]), Color.Orange);
		}

		/// <summary>
		/// Change HP
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command311(dynamic args)
		{
			AppendText("@>");
			int id = args[0];
			string name = id == 0 ? "Entire Party" :
				String.Format("[{0}]", Project.Data.Actors[id].ToString());
			string oper = args[1] == 0 ? "+" : "-";
			string value;
			if (args[2] == 0) // Constant
				value = Math.Abs(args[3]).ToString();
			else // Variable
				value = String.Format("Variable [{0}]", Project.Variables[args[3]]);
			this.AppendText(String.Format("Change HP: {0}, {1}{2}",
				name, oper, value), Color.DeepSkyBlue);
		}

		/// <summary>
		/// Change SP
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command312(dynamic args)
		{
			AppendText("@>");
			int id = args[0];
			string name = id == 0 ? "Entire Party" :
				String.Format("[{0}]", Project.Data.Actors[id].ToString());
			string oper = args[1] == 0 ? "+" : "-";
			string value;
			if (args[2] == 0) // Constant
				value = Math.Abs(args[3]).ToString();
			else // Variable
				value = String.Format("Variable [{0}]", Project.Variables[args[3]]);
			this.AppendText(String.Format("Change SP: {0}, {1}{2}",
				name, oper, value), Color.DeepSkyBlue);
		}

		/// <summary>
		/// Change State
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command313(dynamic args)
		{
			AppendText("@>");
			string name = args[0] == 0 ? "Entire Party" :
				String.Format("[{0}]", Project.Data.Actors[args[0]]);
			string oper = args[1] == 0 ? "+" : "-";
			this.AppendText(String.Format("Change State: {0}, {1}[{2}]",
				name, oper, Project.Data.States[args[2]]), Color.DeepSkyBlue);
		}

		/// <summary>
		/// Recover All
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command314(dynamic args)
		{
			AppendText("@>");
			string text = args[0] == 0 ? "Recover All: Entire Party" :
				String.Format("Recover All: [{0}]", Project.Data.Actors[args[0]]);
			this.AppendText(text, Color.DeepSkyBlue);
		}

		/// <summary>
		/// Change Experience
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command315(dynamic args)
		{
			AppendText("@>");
			int id = args[0];
			string name = id == 0 ? "Entire Party" :
				String.Format("[{0}]", Project.Data.Actors[id].ToString());
			string oper = args[1] == 0 ? "+" : "-";
			string value;
			if (args[2] == 0) // Constant
				value = Math.Abs(args[3]).ToString();
			else // Variable
				value = String.Format("Variable [{0}]", Project.Variables[args[3]]);
			this.AppendText(String.Format("Change EXP: {0}, {1}{2}",
				name, oper, value), Color.DeepSkyBlue);
		}

		/// <summary>
		/// Change Level
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command316(dynamic args)
		{
			AppendText("@>");
			int id = args[0];
			string name = id == 0 ? "Entire Party" :
				String.Format("[{0}]", Project.Data.Actors[id].ToString());
			string oper = args[1] == 0 ? "+" : "-";
			string value;
			if (args[2] == 0) // Constant
				value = Math.Abs(args[3]).ToString();
			else // Variable
				value = String.Format("Variable [{0}]", Project.Variables[args[3]]);
			this.AppendText(String.Format("Change Level: {0}, {1}{2}",
				name, oper, value), Color.DeepSkyBlue);
		}

		/// <summary>
		/// Change Parameters
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command317(dynamic args)
		{
			AppendText("@>");
			string name = Project.Data.Actors[args[0]].ToString();
			string param = new[] { "MaxHP", "MaxSP", "STR", "DEX", "AGI", "INT" }[args[1]];
			string oper = args[2] == 0 ? "+" : "-";
			string value;
			if (args[3] == 0) // Constant
				value = Math.Abs(args[4]).ToString();
			else
				value = String.Format("Variable [{0}]", Project.Variables[args[4]]);
			this.AppendText(String.Format("Change Parameters: [{0}], {1} {2}{3}",
				name, param, oper, value), Color.DeepSkyBlue);
		}

		/// <summary>
		/// Change Skills
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command318(dynamic args)
		{
			AppendText("@>");
			string name = Project.Data.Actors[args[0]].ToString();
			string oper = args[1] == 0 ? "+" : "-";
			string skill = Project.Data.Skills[args[2]].ToString();
			this.AppendText(String.Format("Change Skills: [{0}], {1}[{2}]",
				name, oper, skill), Color.DeepSkyBlue);
		}

		/// <summary>
		/// Change Equipment
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command319(dynamic args)
		{
			AppendText("@>");
			string name = Project.Data.Actors[args[0]].ToString();
			string equip;
			if (args[1] == 0)
				equip = Project.Data.Weapons[args[2]].ToString();
			else
				equip = Project.Data.Armors[args[2]].ToString();
			string type = new[] { "Weapon", "Shield", "Helmet", "Body Armor", "Accessory" }[args[1]];
			this.AppendText(String.Format("Change Equipment: [{0}], {1} = [{2}]",
				name, type, equip), Color.DeepSkyBlue);
		}

		/// <summary>
		/// Change Actor Name
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command320(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Change Actor Name: [{0}], '{1}'",
				Project.Data.Actors[args[0]], args[1]), Color.DeepSkyBlue);
		}

		/// <summary>
		/// Change Actor Class
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command321(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Change Actor Class: [{0}], [{1}]",
				Project.Data.Actors[args[0]], Project.Data.Classes[args[1]]), Color.DeepSkyBlue);
		}

		/// <summary>
		/// Change Actor Graphic
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command322(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Change Actor Graphic: [{0}], '{1}', {2}, '{3}', {4}",
				Project.Data.Actors[args[0]], args[1], args[2], args[3], args[4]), Color.DeepSkyBlue);
		}

		/// <summary>
		/// Change Enemy HP
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command331(dynamic args)
		{
			AppendText("@>");
			int id = args[0];
			string name = id == -1 ? "Entire Troop" :
				String.Format("[{0}]", "IMPLEMENT"); // TODO: Implement
			string oper = args[1] == 0 ? "+" : "-";
			string value;
			if (args[2] == 0) // Constant
				value = Math.Abs(args[3]).ToString();
			else // Variable
				value = String.Format("Variable [{0}]", Project.Variables[args[3]]);
			this.AppendText(String.Format("Change Enemy HP: {0}, {1}{2}",
				name, oper, value), Color.DarkViolet);
		}

		/// <summary>
		/// Change Enemy SP
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command332(dynamic args)
		{
			AppendText("@>");
			int id = args[0];
			string name = id == -1 ? "Entire Troop" :
				String.Format("[{0}]", "IMPLEMENT"); // TODO: Implement
			string oper = args[1] == 0 ? "+" : "-";
			string value;
			if (args[2] == 0) // Constant
				value = Math.Abs(args[3]).ToString();
			else // Variable
				value = String.Format("Variable [{0}]", Project.Variables[args[3]]);
			this.AppendText(String.Format("Change Enemy SP: {0}, {1}{2}",
				name, oper, value), Color.DarkViolet);
		}

		/// <summary>
		/// Change Enemy State
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command333(dynamic args)
		{
			AppendText("@>");
			string name = args[0] == -1 ? "Entire Troop" :
				String.Format("[{0}]", "IMPLEMENT"); // TODO: Implement
			string oper = args[1] == 0 ? "+" : "-";
			this.AppendText(String.Format("Change State: {0}, {1}[{2}]",
				name, oper, Project.Data.States[args[2]]), Color.DarkViolet);
		}

		/// <summary>
		/// Enemy Recover All
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command334(dynamic args)
		{
			AppendText("@>");
			string text = args[0] == 0 ? "Enemy Recover All: Entire Troop" :
				String.Format("Enemy Recover All: [{0}]", "IMPLEMENT"); // TODO: Implement
			this.AppendText(text, Color.DarkViolet);
		}

		/// <summary>
		/// Enemy Appearance
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command335(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Enemy Appearance: [{0}. {1}]",
				args[0] + 1, "IMPLEMENT"), Color.DarkViolet);
		}

		/// <summary>
		/// Enemy Transform
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command336(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Enemy Transform: [{0}. {1}], [{2}]",
				args[0] + 1, "IMPLEMENT", Project.Data.Enemies[args[1]]), Color.DarkViolet);
		}

		/// <summary>
		/// Show Battle Animation
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command337(dynamic args)
		{
			AppendText("@>");
			string name;
			if (args[0] == 0) // Enemy
			{
				name = args[1] == -1 ? "Entire Troop" :
					String.Format("[{0}. {1}]", args[1] + 1, "IMPLEMENT"); // TODO: Implement
			}
			else // Actor
				name = String.Format("Actor No. {0}", args[1] + 1);
			string anime = Project.Data.Animations[args[2]].ToString();
			this.AppendText(String.Format("Show Battle Animation: {0}, [{1}]",
				name, anime), Color.DarkViolet);
		}

		/// <summary>
		/// Deal Damage
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command338(dynamic args)
		{
			AppendText("@>");
			string name, value;
			if (args[0] == 0) // Enemy
			{
				name = args[1] == -1 ? "Entire Troop" :
					String.Format("[{0}. {1}]", args[1] + 1, "IMPLEMENT"); // TODO: Implement
			}
			else // Actor
				name = name = args[1] == -1 ? "Entire Party" :
					String.Format("Actor No. {0}", args[1] + 1);
			if (args[2] == 0) // Constant
				value = args[3];
			else // Variable
				value = String.Format("Variable [{0}]", Project.Variables[args[3]]);
			this.AppendText(String.Format("Deal Damage: {0}, {1}",
				name, value), Color.DarkViolet);
		}

		/// <summary>
		/// Force Action
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command339(dynamic args)
		{
			AppendText("@>");
			string name, cmd;
			if (args[0] == 0) // Enemy
				name = String.Format("[{0}. {1}", args[1] + 1, "IMPLEMENT"); // TODO: Implement
			else // Actor
				name = String.Format("Actor No. {0}", args[1] + 1);
			if (args[2] == 0) // Basic
				cmd = new[] { "Attack", "Defend", "Escape", "Do Nothing" }[args[3]];
			else // Skill
				cmd = String.Format("[{0}]", Project.Data.Skills[args[3]]);
			string target = args[4] == -1 ? "Random" : "Index " + args[4].ToString();
			string seq = args[5] == 0 ? "" : ", Execute Now";
			string text = String.Format("Force Action: {0}, {1}, {2}{3}", name, cmd, target, seq);
			this.AppendText(text, Color.DarkViolet);
		}

		/// <summary>
		/// Abort Battle
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command340(dynamic args)
		{
			AppendText("@>");
			this.AppendText("Abort Battle", Color.DarkViolet);
		}

		/// <summary>
		/// Call Menu Screen
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command351(dynamic args)
		{
			AppendText("@>");
			this.AppendText("Call Menu Screen", Color.DarkGray);
		}

		/// <summary>
		/// Call Save Screen
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command352(dynamic args)
		{
			AppendText("@>");
			this.AppendText("Call Save Screen", Color.DarkGray);
		}

		/// <summary>
		/// Gameover
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command353(dynamic args)
		{
			AppendText("@>");
			this.AppendText("Game Over", Color.DarkGray);
		}

		/// <summary>
		/// Return to Title Screen
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command354(dynamic args)
		{
			AppendText("@>");
			this.AppendText("Return to Title Screen", Color.DarkGray);
		}

		/// <summary>
		/// Script
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command355(dynamic args)
		{
			AppendText("@>");
			this.AppendText(String.Format("Script: {0}", args[0]), Color.DarkGray);
		}

		/// <summary>
		/// Script (Multi-Line)
		/// </summary>
		/// <param name="args">Array of game event parameters</param>
		private void Command655(dynamic args)
		{
			AppendText(" :");
			this.AppendText(String.Format("      : {0}", args[0]), Color.DarkGray);
		}

		/// <summary>
		/// Translates an RPG.MoveCommand into a string to display in the editor.
		/// </summary>
		/// <param name="cmd">RPG.MoveCommand to translate</param>
		/// <returns>String representation of command and parameters</returns>
		private static string TranslateMove(MoveCommand cmd)
		{
			switch (cmd.code)
			{
				case 1: return "Move Down";
				case 2: return "Move Left";
				case 3: return "Move Right";
				case 4: return "Move Up";
				case 5: return "Move Lower Left";
				case 6: return "Move Lower Right";
				case 7: return "Move Upper Left";
				case 8: return "Move Upper Right";
				case 9: return "Move at Random";
				case 10: return "Move toward Player";
				case 11: return "Move away from Player";
				case 12: return "1 Step Forward";
				case 13: return "1 Step Backward";
				case 14:
				int x = cmd.parameters[0];
				int y = cmd.parameters[1];
				string oper1 = x >= 0 ? "+" : "";
				string oper2 = y >= 0 ? "+" : "";
				return String.Format("Jump: {0}{1}, {2}{3}", oper1, x, oper2, y);
				case 15: return String.Format("Wait: {0} frame(s)", cmd.parameters[0]);
				case 16: return "Turn Down";
				case 17: return "Turn Left";
				case 18: return "Turn Right";
				case 19: return "Turn Up";
				case 20: return "Turn 90° Right";
				case 21: return "Turn 90° Left";
				case 22: return "Turn 180°";
				case 23: return "Turn 90° Right or Left";
				case 24: return "Turn at Random";
				case 25: return "Turn toward Player";
				case 26: return "Turn away from Player";
				case 27: return String.Format("Switch ON: [{0}]", Project.Switches[cmd.parameters[0]]);
				case 28: return String.Format("Switch OFF: [{0}]", Project.Switches[cmd.parameters[0]]);
				case 29: return String.Format("Change Speed: {0}", cmd.parameters[0]);
				case 30: return String.Format("Change Frequency: {0}", cmd.parameters[0]);
				case 31: return "Move Animation ON";
				case 32: return "Move Animation OFF";
				case 33: return "Stop Animation ON";
				case 34: return "Stop Animation OFF";
				case 35: return "Direction Fix ON";
				case 36: return "Direction Fix OFF";
				case 37: return "Through ON";
				case 38: return "Through OFF";
				case 39: return "Always on Top ON";
				case 40: return "Always on Top OFF";
				case 41:
				var p = cmd.parameters;
				return String.Format("Graphic: '{0}', {1}, {2}, {3}", p[0], p[1], p[2], p[3]);
				case 42: return String.Format("Change Opacity: {0}", cmd.parameters[0]);
				case 43: return String.Format("Change Blending: {0}", new[] { "Normal", "Add", "Sub" }[cmd.parameters[0]]);
				case 44: return String.Format("SE: {0}", cmd.parameters[0]);
				case 45: return String.Format("Script: {0}", cmd.parameters[0]);
				default: return "";
			}
		}

		/// <summary>
		/// Gets an item by ID and integer type
		/// </summary>
		/// <param name="type">Type of item: 0 = Item, 1 = Weapon, 2 = Armor</param>
		/// <param name="id">ID of the item</param>
		/// <returns>Formatted name of item</returns>
		private static string GetItemName(int type, int id)
		{
		    switch (type)
		    {
		        case 0:
		            return Project.Data.Items[id].ToString();
		        case 1:
		            return Project.Data.Weapons[id].ToString();
		        case 2:
		            return Project.Data.Armors[id].ToString();
                default:
		            return "";
		    }
		}

	    #endregion

		private void EventTextBox_Click(object sender, EventArgs e)
		{

		}

		private void EventTextBox_DoubleClick(object sender, EventArgs e)
		{
			var form = new EventBuilderMainForm();
			form.ShowDialog();
		}

		private void EventTextBox_KeyDown(object sender, KeyEventArgs e)
		{

		}
	}
}
