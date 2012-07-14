using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Windows.Forms;

using Cmd = RPG.EventCommand;

namespace ARCed.EventBuilder
{
	/// <summary>
	/// A compiler bug in VS prevents a simple "using" alias for this, hence the inclusion 
	/// of this class.
	/// </summary>
	public class Params : List<dynamic> { }

	/// <summary>
	/// Static class for building event commands. 
	/// </summary>
	public static class EventCommandEditor 
	{
		private static Cmd EmptyCommand { get { return new Cmd(0, 1, new Params()); } }
		
		/// <summary>
		/// Starts the appropriate dialog, if any, and returns a user-defined command based 
		/// on the specified code and indent level.
		/// </summary>
		/// <param name="code">Event command code to get a command for.</param>
		/// <param name="indent">Current indent level to set for the commands.</param>
		/// <returns>List of user-defined event commands</returns>
		public static List<RPG.EventCommand> CreateCommand(int code, int indent)
		{
			string methodName = String.Format("Command{0}", code);
			MethodInfo info = typeof(EventCommandEditor).GetMethod(methodName, BindingFlags.Static | BindingFlags.NonPublic);
			if (info == null)
			{
				Console.WriteLine("Missing method: \"{0}\"", methodName);
				return null;
			}
			return (List<Cmd>)info.Invoke(null, new object[] { new List<Cmd>() });
		}

		/// <summary>
		/// Begins edit of an existing event command.
		/// </summary>
		/// <param name="command">List of event commands to edit.</param>
		/// <returns>Modified commands, or null if unchanged.</returns>
		public static Cmd EditCommand(List<Cmd> commands)
		{
			string methodName = String.Format("Command{0}", commands[0].code);
			MethodInfo info = typeof(EventCommandEditor).GetMethod(methodName,
				BindingFlags.Static | BindingFlags.NonPublic);
			if (info == null)
			{
				Console.WriteLine("Missing method: \"{0}\"", methodName);
				return null;
			}
			return (RPG.EventCommand)info.Invoke(null, new object[] { commands });
		}

		#region Page 1
	
		/// <summary>
		/// Show Text
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command101(List<Cmd> commands)
		{
			string[] lines = new string[commands.Count];
			for (int i = 0; i < commands.Count; i++)
				lines[i] = commands[i].parameters[0];
			using (CmdShowTextDialog dialog = new CmdShowTextDialog())
			{
				dialog.Lines = lines;
				if (dialog.ShowDialog() == DialogResult.OK)
				{
					commands.Clear();
					lines = dialog.Lines;
					commands.Add(new Cmd(101, 0, new Params { lines[0] }));
					for (int i = 1; i < lines.Length; i++)
						commands.Add(new Cmd(401, 0, new Params { lines[0] }));
					return commands;
				}
			}
			return null;
		}

		/// <summary>
		/// Show Choices
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command102(List<Cmd> commands)
		{
			using (CmdShowChoicesDialog dialog = new CmdShowChoicesDialog())
			{
				if (commands.Count > 0)
				{
					dialog.Choices = commands[0].parameters[0];
					dialog.CancelIndex = commands[0].parameters[1];
				}
				if (dialog.ShowDialog() == DialogResult.OK)
				{
					Params choices = new Params();
					foreach (string choice in dialog.Choices)
						choices.Add(choice);
					if (choices.Count == 0) choices.Add("");
					commands.Clear();
					commands.Add(new Cmd(102, 0, new Params { choices, dialog.CancelIndex }));
					for (int i = 0; i < choices.Count; i++)
					{
						commands.Add(new Cmd(402, 0, new Params { i, choices[i] }));
						commands.Add(EmptyCommand);
					}
					if (dialog.CancelIndex == 5)
					{
						commands.Add(new Cmd(403, 0, new Params()));
						commands.Add(EmptyCommand);
					}
					commands.Add(new Cmd(404, 0, new Params()));
					return commands;
				}
			}
			return null;
		}

		/// <summary>
		/// Input Number
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command103(List<Cmd> commands)
		{
			using (CmdInputNumberDialog dialog = new CmdInputNumberDialog())
			{
				if (commands.Count > 0)
				{
					dialog.VariableId = commands[0].parameters[0];
					dialog.Digits = commands[0].parameters[1];
				}
				if (dialog.ShowDialog() == DialogResult.OK)
				{
					commands.Clear();
					int dgts = dialog.Digits;
					int varId = dialog.VariableId;
					commands.Add(new Cmd(103, 0, new Params { varId, dgts }));
					return commands;
				}
			}
			return null;
		}
		
		/// <summary>
		/// Change Text Options
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command104(List<Cmd> commands)
		{
			using (CmdChangeTextOptionsDialog dialog = new CmdChangeTextOptionsDialog())
			{
				if (commands.Count > 0)
				{
					dialog.Position = commands[0].parameters[0];
					dialog.WindowVisibility = commands[0].parameters[1];
				}
				if (dialog.ShowDialog() == DialogResult.OK)
				{
					commands.Clear();
					commands.Add(new Cmd(104, 0, 
						new Params { dialog.Position, dialog.WindowVisibility }));
					return commands;
				}
			}
			return null;
		}

		/// <summary>
		/// Button Input Processing
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command105(List<Cmd> commands)
		{
			using (CmdButtonInputDialog dialog = new CmdButtonInputDialog())
			{
				if (commands.Count > 0)
					dialog.VariableId = commands[0].parameters[0];
				if (dialog.ShowDialog() == DialogResult.OK)
				{
					commands.Clear();
					commands.Add(new Cmd(105, 0, new Params { dialog.VariableId }));
					return commands;
				}
			}
			return null;
		}

		/// <summary>
		/// Wait
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command106(List<Cmd> commands)
		{
			using (CmdWaitDialog dialog = new CmdWaitDialog())
			{
				if (commands.Count > 0)
					dialog.Frames = commands[0].parameters[0];
				if (dialog.DialogResult == DialogResult.OK)
				{
					commands.Clear();
					commands.Add(new Cmd(106, 0, new Params { dialog.Frames }));
					return commands;
				}					
			}
			return null;
		}

		/// <summary>
		/// Comment
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command108(List<Cmd> commands)
		{
			string[] lines;
			using (CmdCommentDialog dialog = new CmdCommentDialog())
			{ 
				if (commands.Count > 0)
				{
					lines = new string[commands.Count];
					for (int i = 0; i < commands.Count; i++)
						lines[i] = commands[i].parameters[0];
					dialog.Lines = lines;
				}		
				if (dialog.ShowDialog() == DialogResult.OK)
				{
					commands.Clear();
					lines = dialog.Lines;
					commands.Add(new Cmd(108, 0, new Params { lines[0] }));
					for (int i = 1; i < lines.Length; i++)
						commands.Add(new Cmd(408, 0, new Params { lines[i] }));
					return commands;
				}		
			}
			return null;
		}

		/// <summary>
		/// Conditional Branch
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command111(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Loop
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command112(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Break Loop
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command113(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Exit Event Processing
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command115(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Erase Event
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command116(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Call Common Event
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command117(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Label
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command118(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Jump to Label
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command119(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Control Switches
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command121(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Control Variables
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command122(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Control Self-Switch
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command123(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Control Timer
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command124(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Gold
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command125(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Items
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command126(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Weapons
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command127(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Armors
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command128(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Party Member
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command129(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Windowskin
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command131(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Battle BGM
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command132(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Battle End ME
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command133(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Save Access
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command134(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Menu Access
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command135(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Encounter
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command136(List<Cmd> commands)
		{

			return null;
		}

		#endregion

		#region Page 2

		/// <summary>
		/// Transfer Player
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command201(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Set Event Location
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command202(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Transparency
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command208(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Set Move Route
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command209(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Show Animation
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command207(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Wait for Move's Completion
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command210(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Scroll Map
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command203(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Map Settings
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command204(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Fog Opacity
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command206(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Fog Color Tone
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command205(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Prepare for Transition
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command221(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Execute Transition
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command222(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Screen Color Tone
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command223(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Screen Flash
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command224(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Screen Shake
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command225(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Set Weather Effects
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command236(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Show Picture
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command231(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Move Picture
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command232(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Rotate Picture
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command233(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Picture Color Tone
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command234(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Erase Picture
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command235(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Play BGM
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command241(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Fade Out BGM
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command242(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Play BGS
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command245(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Fade Out BGS
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command246(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Memorize BGM/BGS
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command247(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Restore BGM/BGS
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command248(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Play ME
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command249(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Play SE
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command250(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Stop SE
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command251(List<Cmd> commands)
		{

			return null;
		}

		#endregion

		#region Page 3

		/// <summary>
		/// Battle Processing
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command301(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Shop Processing
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command302(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Name Input Processing
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command303(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Call Menu Screen
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command351(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Call Save Screen
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command352(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Game Over
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command353(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Return to Title Screen
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command354(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Enemy HP
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command331(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Enemy SP
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command332(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Enemy State
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command333(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Enemy Recover All
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command334(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Enemy Appearance
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command335(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Enemy Transform
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command336(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Show Battle Animation
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command337(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Deal Damage
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command338(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Force Action
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command339(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Abort Battle
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command340(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change HP
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command311(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change SP
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command312(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change State
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command313(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Recover All
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command314(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change EXP
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command315(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Level
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command316(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Parameters
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command317(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Skills
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command318(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Equipment
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command319(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Actor Name
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command320(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Actor Class
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command321(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Change Actor Graphic
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command322(List<Cmd> commands)
		{

			return null;
		}

		/// <summary>
		/// Script
		/// </summary>
		/// <param name="commands">List of commands to modify.</param>
		/// <returns>List of user-defined event commands</returns>
		private static List<Cmd> Command355(List<Cmd> commands)
		{

			return null;
		}

		#endregion
	}
}
