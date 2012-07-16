#region Using Directives

using System;
using System.IO;

#endregion

namespace ARCed.Helpers
{
    /// <summary>
    /// Static class for getting paths to files/folders used by ARCed.
    /// </summary>
	public static class PathHelper
	{
		// Names for folders
		const string ARC_PROJECT_FOLDER      = "ARC";
		const string EDITOR_SETTINGS_FOLDER  = "Settings";
		const string PLUGIN_FOLDER           = "Plugins";
		const string TEMPLATES_FOLDER        = "Templates";
		const string SCRIPT_TEMPLATE_FOLDER  = "Scripts";
		const string PROJECT_TEMPLATE_FOLDER = "Projects";
		// Names for files
		const string EDITOR_SETTINGS_FILE = "EditorSettings.xml";
		const string SCRIPT_SETTINGS_FILE = "ScriptSettings.xml";
		const string SKIN_SETTINGS_FILE   = "WindowskinSettings.xml";

		const string X86_FOLDER = "x86";
		const string X64_FOLDER = "x64";
		const string SEVENZIP_32 = "7z.dll";
		const string SEVENZIP_64 = "7z64.dll";
		const string SCILEXER_32 = "SciLexer.dll";
		const string SCILEXER_64 = "SciLexer64.dll";

        const string ASSEMBLY_DIRECTORY = "Assemblies";
        const string PORTABLE_DIRECTORY = "AppData";

		private static string _appDataDir;

		/// <summary>
		/// Gets the path to ARCed.NET's AppData directory
		/// </summary>
		public static string ApplicationData
		{
			get
			{
				if (_appDataDir == null)
				{
                    if (Runtime.Portable)
                        _appDataDir = Path.Combine(EditorDirectory, PORTABLE_DIRECTORY);
                    else
                    {
                        string appdata = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
                        _appDataDir = Path.Combine(appdata, "ARCed.NET");
                    }
				}
				if (!Directory.Exists(_appDataDir))
					Directory.CreateDirectory(_appDataDir);
				return _appDataDir;
			}
		}

		/// <summary>
		/// Gets the full path to the current application
		/// </summary>
        public static string EditorPath { get; set; }

        /// <summary>
        /// Gets the full path to the directory of the editor
        /// </summary>
        public static string EditorDirectory
        {
            get { return Path.GetDirectoryName(EditorPath); }
        }

        /// <summary>
        /// Gets the path to the folder containing the application's assemblies.
        /// </summary>
        public static string AssemblyDir
        {
            get { return Path.Combine(EditorDirectory, ASSEMBLY_DIRECTORY); }
        }

		/// <summary>
		/// Gets the path to the plugins directory
		/// </summary>
		public static string PluginDirectory
		{
			get 
			{ 
				string path = Path.Combine(EditorDirectory, PLUGIN_FOLDER);
				if (!Directory.Exists(path))
					Directory.CreateDirectory(path);
				return path;
			}
		}

		/// <summary>
		/// Gets the path to the template directory
		/// </summary>
		public static string TemplateDirectory
		{
			get
			{
                string path = Path.Combine(ApplicationData, TEMPLATES_FOLDER);
				if (!Directory.Exists(path))
					Directory.CreateDirectory(path);
				return path;
			}
		}

		/// <summary>
		/// Gets the path to the templates directory
		/// </summary>
		public static string ProjectTemplateDirectory
		{
			get 
			{ 
				string path = Path.Combine(TemplateDirectory, PROJECT_TEMPLATE_FOLDER);
				if (!Directory.Exists(path))
					Directory.CreateDirectory(path);
				return path;
			}
		}

		/// <summary>
		/// Gets the path to the script template directory
		/// </summary>
		public static string ScriptTemplateDirectory
		{
			get 
			{
				string path = Path.Combine(TemplateDirectory, SCRIPT_TEMPLATE_FOLDER);
				if (!Directory.Exists(path))
					Directory.CreateDirectory(path);
				return path;
			}
		}

		/// <summary>
		/// Gets the path to the editor's settings folder
		/// </summary>
		public static string SettingsDirectory
		{
			get
			{
				string path = Path.Combine(ApplicationData, EDITOR_SETTINGS_FOLDER);
				if (!Directory.Exists(path))
					Directory.CreateDirectory(path);
				return path;
			}
		}

		/// <summary>
		/// Gets the path to ARCed.NET's settings file
		/// </summary>
		public static string EditorSettings
		{
			get { return Path.Combine(SettingsDirectory, EDITOR_SETTINGS_FILE); }
		}

		/// <summary>
		/// Gets the path to ARCed.NET's skin settings file
		/// </summary>
		public static string SkinSettings
		{
			get { return Path.Combine(SettingsDirectory, SKIN_SETTINGS_FILE); }
		}

		/// <summary>
		/// Gets the path to ARCed.NET's script setting file
		/// </summary>
		public static string ScriptSettings
		{
			get { return Path.Combine(SettingsDirectory, SCRIPT_SETTINGS_FILE); }
		}
		
		/// <summary>
		/// Gets the default directory where projects are saved
		/// </summary>
		public static string DefaultSaveDirectory
		{
			get
			{
				string path = Path.Combine(
					Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments), ARC_PROJECT_FOLDER);
				if (!Directory.Exists(path))
					Directory.CreateDirectory(path);
				return path;
			}
		}

        /// <summary>
        /// Gets the path to the native 7zip library appropriate for the host machines CPU architecture.
        /// </summary>
		public static string SevenZipLibrary
		{
			get 
            {
			    return IntPtr.Size == 8 ? Path.Combine(EditorDirectory, X64_FOLDER, SEVENZIP_64) : 
                    Path.Combine(EditorDirectory, X86_FOLDER, SEVENZIP_32);
			}
		}

        /// <summary>
        /// Gets the path to the native Scintilla library appropriate for the host machines CPU architecture.
        /// </summary>
		public static string SciLexerLibrary
		{
			get 
            {
			    return IntPtr.Size == 8 ? Path.Combine(EditorDirectory, X64_FOLDER, SCILEXER_64) : 
                    Path.Combine(EditorDirectory, X86_FOLDER, SCILEXER_32);
			}
		}
	}
}
