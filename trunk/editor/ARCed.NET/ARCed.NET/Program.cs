using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Windows.Forms;


namespace ARCed
{
	static class Program
	{
		public static bool DEBUG_MODE;
		public static bool LOGGING;
		public static bool LEGACY;

		/// <summary>
		/// The main entry point for the application.
		/// </summary>
		[STAThread]
		static void Main(string[] arguments)
		{
			Application.SetCompatibleTextRenderingDefault(true);
			List<string> args = arguments.ToList<string>();
			DEBUG_MODE = args.Contains("-d") || args.Contains("-debug");
			LOGGING = args.Contains("-l") || args.Contains("-logging");
			LEGACY = args.Contains("-x") || args.Contains("-legacy");
			if (DEBUG_MODE)
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
			Application.EnableVisualStyles();
			Application.SetCompatibleTextRenderingDefault(false);
			Application.Run(new Editor(filename));
		}
	}
}