#region Using Directives

using System.Text;
using ARCed.Core.Win32;
using Microsoft.Win32;

#endregion

namespace ARCed.Helpers
{
    /// <summary>
    /// Static class used for associated ARCed file types with the program and respective icons.
    /// </summary>
	public static class FileAssociator
	{
		private const string PROGRAM_ID = "ARCed.NET";

		/// <summary>
        /// Associate file extension with progID, description, icon and application
		/// </summary>
		/// <param name="extension">Extension to associate</param>
		/// <param name="description">Description of file type</param>
		/// <param name="icon">Path to icon to set for the file type</param>
		/// <param name="application">Path to icon to associate with this file type</param>
		public static void Associate(string extension, string description, string icon, string application)
		{
		    var registryKey = Registry.ClassesRoot.CreateSubKey(extension);
		    if (registryKey != null)
		        registryKey.SetValue("", PROGRAM_ID);
		    if (string.IsNullOrEmpty(PROGRAM_ID)) return;
		    using (var key = Registry.ClassesRoot.CreateSubKey(PROGRAM_ID))
		    {
		        if (key == null) return;
		        if (description != null)
		            key.SetValue("", description);
		        if (icon != null)
		        {
		            var subKey = key.CreateSubKey("DefaultIcon");
		            if (subKey != null)
		                subKey.SetValue("", ToShortPathName(icon));
		        }
		        if (application == null) return;
		        var regKey = key.CreateSubKey(@"Shell\Open\Command");
		        if (regKey != null)
		            regKey.SetValue("", ToShortPathName(application) + " \"%1\"");
		    }
		}

        /// <summary>
        /// Return true if extension already associated in registry
        /// </summary>
        /// <param name="extension">Extension to check</param>
        /// <returns>Flag if extension is already associated or not</returns>
		public static bool IsAssociated(string extension)
		{
			return (Registry.ClassesRoot.OpenSubKey(extension, false) != null);
		}

		/// <summary>
        /// Return short path format of a file name
		/// </summary>
		/// <param name="longName">Long name of file</param>
		/// <returns>Short name of file</returns>
		private static string ToShortPathName(string longName)
		{
			var s = new StringBuilder(1000);
			var iSize = (uint)s.Capacity;
			NativeMethods.GetShortPathName(longName, s, iSize);
			return s.ToString();
		}
	}
}