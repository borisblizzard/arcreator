#region Using Directives

using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;
using ARCed.Core.Win32;
using ARCed.Helpers;

#endregion

namespace ARCed
{
	static class Program
	{

		/// <summary>
		/// The main entry point for the application.
		/// </summary>
		[STAThread]
		static void Main(string[] arguments)
		{
			List<string> args = arguments.ToList();
			Runtime.Debug = args.Contains("-d") || args.Contains("-debug");
			Runtime.Logging = args.Contains("-l") || args.Contains("-logging");
			Runtime.Legacy = args.Contains("-x") || args.Contains("-legacy");
            Runtime.Portable = args.Contains("-p") || args.Contains("-portable");
			if (Runtime.Debug)
			{
				NativeMethods.AllocConsole();
				Console.Title = "ARCed.NET Debug";
				Console.ForegroundColor = ConsoleColor.DarkGreen;
				Console.WriteLine("ARCed.NET [Version {0}]", Application.ProductVersion);
				Console.WriteLine("Copyright (c) 2012 ARC Development Team.  All rights reserved.");
				Console.ForegroundColor = ConsoleColor.Gray;
				Console.WriteLine();
			}
			string filename = args.Count > 0 ? args[0] : null;
            PathHelper.EditorPath = Application.ExecutablePath;
			Application.EnableVisualStyles();
			Application.SetCompatibleTextRenderingDefault(false);
			Application.Run(new Editor(filename));
		}
	}
}