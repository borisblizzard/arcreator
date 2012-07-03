using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Text;
using ARCed;

namespace ARCDumpTests
{
	class Program
	{
		static void Main(string[] args)
		{
			/*
			var ass = System.Reflection.Assembly.GetExecutingAssembly();
			var types = ass.GetTypes();
			foreach (var t in types)
				Console.WriteLine(t);
			*/
			string path = @"C:\Users\Eric\Desktop\ARC_Data\TEST.arc";
			string path2 = @"C:\Users\Eric\Desktop\ARC\engine\Data\Animations.arc";

			dynamic data;
			using (Stream stream = File.Open(path2, FileMode.Open))
				data = ArcData.load(stream);




			Console.WriteLine();
			
			


		}
	}
}
