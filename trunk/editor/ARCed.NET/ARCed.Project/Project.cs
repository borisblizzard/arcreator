#region Using Directives

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using ARCed.Helpers;
using ARCed.Scripting;
using ARCed.Settings;
using SevenZip;
using RpgObject = RPG.RpgObject;

#endregion

namespace ARCed
{
    /// <summary>
    /// Static class representing the current ARC project.
    /// </summary>
    public static class Project
    {
        #region Private Constants

        // Defines names of ARC folders
        const string BACKUP_FOLDER = "Backups";
        const string SETTINGS_FOLDER = "Settings";
        const string GRAPHICS_FOLDER = "Graphics";
        const string AUDIO_FOLDER = "Audio";
        const string DATA_FOLDER = "Data";
        const string SCRIPT_FOLDER = "Scripts";

        // Defines names of ARCed.NET files
        const string LAYOUT_FILE = "WindowLayout.xml";
        const string PROJECT_SETTINGS_FILE = "ProjectSettings.xml";

        #endregion

        #region Private Fields

        private static string _filename = "";
        private static string _title = "";
        private static List<dynamic> _switches;
        private static List<dynamic> _variables;
        private static GameData _data;
        private static ScriptManager _scriptManager;
        private static ProjectSettings _settings;

        #endregion

        #region Events/Delegates

        /// <summary>
        /// Handler for <see cref="Created"/> events.
        /// </summary>
        /// <param name="e">Event arguments.</param>
        public delegate void OnCreateHandler(EventArgs e);
        /// <summary>
        /// Handler for <see cref="Opened"/> events.
        /// </summary>
        /// <param name="e">Event arguments.</param>
        public delegate void OnOpenHandler(EventArgs e);
        /// <summary>
        /// Handler for <see cref="Closed"/> events.
        /// </summary>
        /// <param name="e">Event arguments.</param>
        public delegate void OnCloseHandler(EventArgs e);
        /// <summary>
        /// Handler for <see cref="Saved"/> events.
        /// </summary>
        /// <param name="e">Event arguments.</param>
        public delegate void OnSavedHandler(EventArgs e);
        /// <summary>
        /// Handler for <see cref="Renamed"/> events.
        /// </summary>
        /// <param name="e">Event arguments.</param>
        public delegate void OnRenamHandler(EventArgs e);

        /// <summary>
        /// Event raised when a project is created.
        /// </summary>
        public static event OnCreateHandler Created;
        /// <summary>
        /// Event raised when a project is opened.
        /// </summary>
        public static event OnOpenHandler Opened;
        /// <summary>
        /// Event raised when a project is closed.
        /// </summary>
        public static event OnCloseHandler Closed;
        /// <summary>
        /// Event raised when a project is saved.
        /// </summary>
        public static event OnSavedHandler Saved;
        /// <summary>
        /// Event raised when a project is renamed.
        /// </summary>
        public static event OnRenamHandler Renamed;

        #endregion

        #region Public Properties

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

        /// <summary>
        /// Gets or sets the project's Battle Test Actors.
        /// </summary>
        public static List<dynamic> BTActors { get; set; }

        /// <summary>
        /// Gets or sets the project's settings.
        /// </summary>
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
                    _switches = new List<dynamic>
                    { null };
                    for (int i = 1; i < Data.System.switches.Count; i++)
                        _switches.Add(new RpgObject(Data.System.switches[i], i));
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
                    _variables = new List<dynamic>
                    { null };
                    for (int i = 1; i < Data.System.variables.Count; i++)
                        _variables.Add(new RpgObject(Data.System.switches[i], i));
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
        /// Gets or sets the project's <see cref="GameData"/>.
        /// </summary>
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
                if (Renamed != null)
                    Renamed(new EventArgs());
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
                    Directory.GetFiles(ScriptsDirectory, "*.rb").ToList();
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
                var titles = new List<string>();
                foreach (var filename in ScriptFilenames)
                {
                    title = Path.GetFileNameWithoutExtension(filename);
                    if (!String.IsNullOrEmpty(title))
                        titles.Add(title.Substring(5, title.Length - 5));
                }
                return titles;
            }
        }

        /// <summary>
        /// Gets or sets the project's <see cref="ARCed.Scripting.ScriptManager"/>
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

        #endregion

        /// <summary>
        /// Loads an ARC project
        /// </summary>
        /// <param name="filename">The path to the .arcproj</param>
        /// <returns>Truth value successful load</returns>
        public static bool Load(string filename)
        {
            try
            {
                _filename = filename;
                Directory.SetCurrentDirectory(ProjectFolder);
                Ini.Load(filename);
                _title = Ini.ReadString("Project", "Title");
                _scriptManager = new ScriptManager(ScriptsDirectory);
                // Load settings
                if (File.Exists(SettingsFile))
                    _settings = Util.LoadXML<ProjectSettings>(SettingsFile);
                if (_settings == null)
                    _settings = new ProjectSettings();
                ResourceHelper.EnableLocalDirectory(true);
                // Load game data
                if (Opened != null)
                    Opened(new EventArgs());
                return LoadGameData();
            }
            catch { return false; }
        }

        /// <summary>
        /// Saves the current open project.
        /// </summary>
        /// <returns>Flag if save was successful or not.</returns>
        public static bool Save()
        {
            try
            {
                Util.SaveXML(SettingsFile, _settings);
                if (Saved != null)
                    Saved(new EventArgs());
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
            if (Closed != null)
                Closed(new EventArgs());
        }

        /// <summary>
        /// Loads the serialized ARC data.
        /// </summary>
        /// <returns>Flag is data was successfully loaded or not.</returns>
        private static bool LoadGameData()
        {
            try
            {
                Data = new GameData();
                TypeMap map = Util.RpgTypes;
				Data.Tilesets = LoadArcData<List<dynamic>>(@"Data\Tilesets.arc", map);
                Data.Items = LoadArcData<List<dynamic>>(@"Data\Items.arc", map);
                Data.Animations = LoadArcData<List<dynamic>>(@"Data\Animations.arc", map);
                Data.Actors = LoadArcData<List<dynamic>>(@"Data\Actors.arc", map);
                Data.Classes = LoadArcData<List<dynamic>>(@"Data\Classes.arc", map);
                Data.Weapons = LoadArcData<List<dynamic>>(@"Data\Weapons.arc", map);
                Data.Armors = LoadArcData<List<dynamic>>(@"Data\Armors.arc", map);
                Data.Skills = LoadArcData<List<dynamic>>(@"Data\Skills.arc", map);
                Data.States = LoadArcData<List<dynamic>>(@"Data\States.arc", map);
                Data.CommonEvents = LoadArcData<List<dynamic>>(@"Data\CommonEvents.arc", map);
                Data.System = LoadArcData<RPG.System>(@"Data\System.arc", map);
                Data.Enemies = LoadArcData<List<dynamic>>(@"Data\Enemies.arc", map);
                Data.Troops = LoadArcData<List<dynamic>>(@"Data\Troops.arc", map);

                return true;
            }
            catch
            {
                _title = _filename = "";
                //Data = null;
                return false;
            }
        }

        /// <summary>
        /// Loads serialized ARC format data from the given path.
        /// </summary>
        /// <typeparam name="T">Specifies the <see cref="System.Type"/> of the 
        /// object that will be returned.</typeparam>
        /// <param name="filename">Filename of the file to load.</param>
        /// <param name="map">Map of reflected types</param>
        /// <returns>Deserialized data.</returns>
        public static T LoadArcData<T>(string filename, TypeMap map = null)
        {
            try
            {
                T data;
                using (Stream s = File.OpenRead(filename))
                    data = (T)ArcData.Load(s, map);
                return data;
            }
            catch (Exception error) { throw new ARCedException(error.Message); }
        }

        /// <summary>
        /// Creates a new ARC project.
        /// </summary>
        /// <param name="library">Path to native library to use for extraction.</param>
        /// <param name="directory">Path to the directory to create project in.</param>
        /// <param name="title">Title of the project.</param>
        /// <param name="template">Template name of the project.</param>
        /// <returns>Path to the created project file to load.</returns>
        public static string CreateProject(string library, string directory, string title, string template)
        {
            SevenZipBase.SetLibraryPath(library);
            var extractor = new SevenZipExtractor(template)
            {
                EventSynchronization = EventSynchronizationStrategy.AlwaysSynchronous
            };
            if (!Directory.Exists(directory))
                Directory.CreateDirectory(directory);
            extractor.ExtractArchive(directory);
            foreach (string arcProj in Directory.GetFiles(directory, "*.arcproj"))
                File.Delete(arcProj);
            if (Created != null)
                Created(new EventArgs());
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
                var projUri = new Uri(_filename);
                var absUri = new Uri(absolutePath);
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

        #endregion

        /// <summary>
        /// Deletes backup files when the number of files exceeds the maximum allowed
        /// </summary>
        /// <returns>Flag if all files were successfully removed or not.</returns>
        /// <remarks>The "Creation Time" attribute of the file is used to delete 
        /// the files in order of the oldest first.</remarks>
        public static bool CleanARChives()
        {
            var result = true;
            var max = _settings.ARChiveSettings.MaxBackups;
            var infos = new DirectoryInfo(BackupDirectory).GetFiles("*.7z").ToList();
            infos.Sort((a, b) => b.CreationTime.CompareTo(a.CreationTime));
            for (var i = max; i < infos.Count; i++)
            {
                try { File.Delete(infos[i].FullName); }
                catch (IOException) { result = false; }
            }
            return result;
        }
    }
}
