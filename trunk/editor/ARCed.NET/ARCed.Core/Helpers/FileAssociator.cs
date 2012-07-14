using Microsoft.Win32;
using System.Runtime.InteropServices;
using System.Text;
using ARCed.Core.Win32;

namespace ARCed.Helpers
{
	public class FileAssociator
	{
		const string programID = "ARCed.NET";

		// Associate file extension with progID, description, icon and application
		public static void Associate(string extension, string description, string icon, string application)
		{
			Registry.ClassesRoot.CreateSubKey(extension).SetValue("", programID);
			if (programID != null && programID.Length > 0)
				using (RegistryKey key = Registry.ClassesRoot.CreateSubKey(programID))
				{
					if (description != null)
						key.SetValue("", description);
					if (icon != null)
						key.CreateSubKey("DefaultIcon").SetValue("", ToShortPathName(icon));
					if (application != null)
						key.CreateSubKey(@"Shell\Open\Command").SetValue("",
									ToShortPathName(application) + " \"%1\"");
				}
		}

		// Return true if extension already associated in registry
		public static bool IsAssociated(string extension)
		{
			return (Registry.ClassesRoot.OpenSubKey(extension, false) != null);
		}

		// Return short path format of a file name
		private static string ToShortPathName(string longName)
		{
			StringBuilder s = new StringBuilder(1000);
			uint iSize = (uint)s.Capacity;
			uint iRet = NativeMethods.GetShortPathName(longName, s, iSize);
			return s.ToString();
		}
	}
}