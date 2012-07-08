using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using ARCed.Helpers;
using ARCed.Scripting;
using ARCed.Settings;
using SevenZip;

namespace ARCed
{
	public static class Project
	{
		// Defines names of ARC folders
		const string BACKUP_FOLDER   = "Backups";
		const string SETTINGS_FOLDER = "Settings";
		const string GRAPHICS_FOLDER = "Graphics";
		const string AUDIO_FOLDER    = "Audio";
		const string DATA_FOLDER     = "Data";
		const string SCRIPT_FOLDER   = "Scripts";

		// Defines names of ARCed.NET files
		const string LAYOUT_FILE           = "WindowLayout.xml";
		const string PROJECT_SETTINGS_FILE = "ProjectSettings.xml";



		private static string _filename = "";
		private static string _title = "";
		private static List<dynamic> _switches;
		private static List<dynamic> _variables;
		private static GameData _data;
		private static ScriptManager _scriptManager;
		private static ProjectSettings _settings;

		public static List<dynamic> BTActors { get; set; }

		public static ProjectSettings Settings
		{
			get { return _settings; }
			set { _settings = value; }
		}

		/// <summary>
		/// Returns the Guid (Globally Unique Identifier) of the project
		/// </summary>
		/// <remarks>This values is used for keeping track of backup files, so 
		/// manually altering it in the .arcproj file will "lose" the directory</remarks>
		public static Guid GUID 
		{
			get { return _settings.Guid; }
		}

		/// <summary>
		/// Gets the status of the editor having a project loaded
		/// </summary>
		public static bool IsLoaded
		{
			get { return _filename != "" && File.Exists(_filename); }
		}

		/// <summary>
		/// Gets the project's variables as a list of generic RPG.GameObjects
		/// </summary>
		public static List<dynamic> Switches
		{
			get
			{
				if (IsLoaded && _switches == null)
				{
					_switches = new List<dynamic>() { null };
					for (int i = 1; i < Data.System.switches.Count; i++)
						_switches.Add(new RPG.RpgObject(Data.System.switches[i], i));
				}
				return _switches;
			}
			set { _switches = value; }
		}

		/// <summary>
		/// Gets the project's variables as a list of generic RPG.GameObjects
		/// </summary>
		public static List<dynamic> Variables
		{
			get
			{
				if (IsLoaded && _variables == null)
				{
					_variables = new List<dynamic>() { null };
					for (int i = 1; i < Data.System.variables.Count; i++)
						_variables.Add(new RPG.RpgObject(Data.System.switches[i], i));
				}
				return _variables;
			}
			set { _variables = value; }
		}

		/// <summary>
		/// Gets or sets the project's associated backup utility
		/// </summary>
		public static ARChiveSettings ARChiveSettings
		{
			get { return _settings.ARChiveSettings; }
			set { _settings.ARChiveSettings = value; }
		}

		/// <summary>
		/// Gets or sets the path of the project.
		/// </summary>
		/// <remarks>The setter does not actually change the path, it
		/// only calls the "Load" function on the passed value.</remarks>
		public static string Filename { get { return _filename; } set { Load(value); } }

		/// <summary>
		/// Gets or sets the project's game data
		/// </summary>
		/// <seealso cref="ARCed.Data.GameData"/>
		public static GameData Data { get { return _data; } set { _data = value; } }

		/// <summary>
		/// Gets or sets the project title
		/// </summary>
		public static string Title 
		{ 
			get { return _title; } 
			set 
			{ 
				_title = value;
				Ini.Load(_filename);
				Ini.Write("Project", "Title", value);
			} 
		}

		/// <summary>
		/// Gets a sorted list of the filenames of all the project's scripts 
		/// </summary>
		public static List<string> ScriptFilenames
		{
			get
			{
				List<string> filenames =
					Directory.GetFiles(ScriptsDirectory, "*.rb").ToList<string>();
				filenames.Sort();
				return filenames;
			}
		}

		/// <summary>
		/// Gets a list of the project's script names, omitting the ordering numbers;
		/// </summary>
		public static List<string> ScriptTitles
		{
			get
			{
				string title;
				List<string> titles = new List<string>();
				foreach (string filename in ScriptFilenames)
				{
					title = Path.GetFileNameWithoutExtension(filename);
					titles.Add(title.Substring(5, title.Length - 5));
				}
				return titles;
			}
		}

		/// <summary>
		/// Gets or sets the project's <paramref name="ARCed.Scripting.ScriptManager"/>
		/// </summary>
		public static ScriptManager ScriptManager
		{
			get { return _scriptManager; }
			set { _scriptManager = value; }
		}

		/// <summary>
		/// Flag indicating of project has unsaved changes
		/// </summary>
		public static bool NeedSaved { get; set; }

		/// <summary>
		/// Loads an ARC project
		/// </summary>
		/// <param name="filename">The path to the .arcproj</param>
		/// <returns>Truth value successful load</returns>
		public static bool Load(string filename)
		{
			//try
			//{
				_filename = filename;
				Directory.SetCurrentDirectory(ProjectFolder);
				Ini.Load(filename);
				_title = Ini.ReadString("Project", "Title");
				_scriptManager = new ScriptManager(ScriptsDirectory);
				// Load settings
				if (File.Exists(SettingsFile))
					_settings = SystemHelper.LoadXML<ProjectSettings>(SettingsFile); 
				if (_settings == null)
					_settings = new ProjectSettings();
				ResourceHelper.EnableLocalDirectory(true);
				// Load game data
				return LoadGameData();
			//}
			//catch { return false; }
		}

		/// <summary>
		/// Saves the current open project.
		/// </summary>
		/// <returns>Flag if save was successful or not.</returns>
		public static bool Save()
		{
			try
			{
				_settings.OpenScripts.Clear();
				foreach (string filename in Editor.OpenScriptsFiles)
					_settings.OpenScripts.Add(filename);
				SystemHelper.SaveXML<ProjectSettings>(SettingsFile, _settings);

				return true;
			}
			catch { return false; }
		}

		/// <summary>
		/// Unloads the current project
		/// </summary>
		public static void Close()
		{
			_filename = null;
			_scriptManager = null;
			_data = null;
		}

		/// <summary>
		/// Loads the serialized ARC data.
		/// </summary>
		/// <returns>Flag is data was successfully loaded or not.</returns>
		private static bool LoadGameData()
		{
			Editor.MainInstance.Cursor = System.Windows.Forms.Cursors.WaitCursor;
			//try
			//{
				GameData data = new GameData();
				TypeMap map = new TypeMap();

				foreach (Type type in SystemHelper.ARCedAssembly.GetTypes())
					map[type.ToString()] = type;

				//data.Animations = LoadArcData<List<dynamic>>(@"C:\Users\Eric\Desktop\ARC\editor\ARCed\tests\ARC_Data\ARC_imported\Data\Animations.arc", map);
				data.Actors = LoadArcData<List<dynamic>>("Actors.arc", map);
				data.Classes = LoadArcData<List<dynamic>>("Classes.arc", map);
				data.Items = LoadArcData<List<dynamic>>("Items.arc", map);
				data.Weapons = LoadArcData<List<dynamic>>("Weapons.arc", map);
				data.Armors = LoadArcData<List<dynamic>>("Armors.arc", map);
				data.Skills = LoadArcData<List<dynamic>>("Skills.arc", map);
				data.States = LoadArcData<List<dynamic>>("States.arc", map);
				data.CommonEvents = LoadArcData<List<dynamic>>("CommonEvents.arc", map);
				data.System = LoadArcData<RPG.System>("System.arc", map);
				data.Enemies = LoadArcData<List<dynamic>>("Enemies.arc", map);
				data.Troops = LoadArcData<List<dynamic>>("Troops.arc", map);
				data.Tilesets = LoadArcData<List<dynamic>>("Tilesets.arc", map);

				Project.Data = data;
				Editor.MainInstance.Cursor = System.Windows.Forms.Cursors.Default;
				return true;
			//}
			//catch
			//{
				_title = _filename = "";
				return false;
			//}
		}

		/// <summary>
		/// Loads serialized ARC format data from the given path.
		/// </summary>
		/// <typeparam name="T">Specifies the <<paramref name="System.Type"/>type</typeparam> of the 
		/// object that will be returned.
		/// <param name="filename">Filename of the file to load.</param>
		/// <param name="map">Map of reflected types</param>
		/// <returns>Deserialized data.</returns>
		public static T LoadArcData<T>(string filename, TypeMap map = null)
		{
			try
			{
				T data;
				using (Stream s = File.OpenRead(Path.Combine(DataDirectory, filename)))
					data = map == null ? (T)ArcData.load(s) : (T)ArcData.load(s, map);
				return data;
			}
			catch (Exception error) { throw new ARCedException(error.Message); }
		}

		/// <summary>
		/// Creates a new ARC project.
		/// </summary>
		/// <param name="directory">Path to the directory to create project in.</param>
		/// <param name="title">Title of the project.</param>
		/// <param name="template">Template name of the project.</param>
		/// <returns>Path to the created project file to load.</returns>
		public static string CreateProject(string directory, string title, string template)
		{
			SevenZipExtractor.SetLibraryPath(Editor.Is64bit ? 
				Path.Combine(PathHelper.EditorDirectory, @"x64\7z64.dll") : 
				Path.Combine(PathHelper.EditorDirectory, @"x86\7z.dll"));
			var extractor = new SevenZipExtractor(template);
			extractor.EventSynchronization = EventSynchronizationStrategy.AlwaysSynchronous;
			if (!Directory.Exists(directory))
				Directory.CreateDirectory(directory);
			extractor.ExtractArchive(directory);
			foreach (string arcProj in Directory.GetFiles(directory, "*.arcproj"))
				File.Delete(arcProj);
			return CreateArcProj(directory, title);
		}

		/// <summary>
		/// Creates the .arcproj file for a project.
		/// </summary>
		/// <param name="dir">Directory where file will be saved.</param>
		/// <param name="title">Title of the project.</param>
		/// <returns>Path to the created file.</returns>
		private static string CreateArcProj(string dir, string title)
		{
			string file = Path.Combine(dir, String.Format("{0}.arcproj", title));
			string text = String.Format("[Project]\nTitle={0}", title);
			File.WriteAllText(file, text);
			return file;
		}

		#region Project PathHelper

		/// <summary>
		/// Gets the relative path of the given path to the project folder
		/// </summary>
		/// <param name="absolutePath">The full system path</param>
		/// <returns>The relative path</returns>
		public static string GetRelativePath(string absolutePath)
		{
			try
			{
				Uri projUri = new Uri(_filename);
				Uri absUri = new Uri(absolutePath);
				string filename = Uri.UnescapeDataString(projUri.MakeRelativeUri(absUri).ToString());
				return filename.Replace('/', '\\');
			}
			catch (UriFormatException) { return absolutePath; }
		}

		/// <summary>
		/// Appends the project's directory to the given relative path and returns it
		/// </summary>
		/// <param name="relativePath">The relative path to the game folder</param>
		/// <returns>The full system path</returns>
		public static string GetAbsolutePath(string relativePath)
		{
			return Path.Combine(ProjectFolder, relativePath);
		}

		/// <summary>
		/// Gets the directory of of the project
		/// </summary>
		public static string ProjectFolder { get { return Path.GetDirectoryName(_filename); } }

		/// <summary>
		/// Gets the the path to the project's graphics directory
		/// </summary>
		public static string GraphicsDirectory
		{
			get { return EnsureDirectoryExist(GRAPHICS_FOLDER); }
		}

		/// <summary>
		/// Gets the the path to the project's audio directory
		/// </summary>
		public static string AudioDirectory
		{
			get { return EnsureDirectoryExist(AUDIO_FOLDER); }
		}

		/// <summary>
		/// Gets the the path to the project's data directory
		/// </summary>
		public static string DataDirectory
		{
			get { return EnsureDirectoryExist(DATA_FOLDER); }
		}

		/// <summary>
		/// Gets the the path to the project's script directory
		/// </summary>
		public static string ScriptsDirectory
		{
			get
			{
				string path = Path.Combine(DATA_FOLDER, SCRIPT_FOLDER);
				return EnsureDirectoryExist(path); 
			}
		}

		/// <summary>
		/// Gets the path to this project's backups directory
		/// </summary>
		public static string BackupDirectory
		{
			get { return EnsureDirectoryExist(BACKUP_FOLDER); }
		}

		/// <summary>
		/// Gets the path to the project's settings directory
		/// </summary>
		public static string SettingsDirectory
		{
			get { return EnsureDirectoryExist(SETTINGS_FOLDER); }
		}

		/// <summary>
		/// Checks if a directory exists, creating it if not, then returns it
		/// </summary>
		/// <param name="directory">The directory to check</param>
		/// <returns>The directory</returns>
		public static string EnsureDirectoryExist(string directory)
		{
			if (!Directory.Exists(directory))
				Directory.CreateDirectory(directory);
			return directory;
		}

		/// <summary>
		/// Gets the path to the project's window layout configuration
		/// </summary>
		public static string LayoutSettings
		{
			get { return Path.Combine(SettingsDirectory, LAYOUT_FILE); }
		}

		/// <summary>
		/// Gets the path to the project's settings file
		/// </summary>
		public static string SettingsFile
		{
			get { return Path.Combine(SettingsDirectory, PROJECT_SETTINGS_FILE); }
		}

		#endregion
	}
}
