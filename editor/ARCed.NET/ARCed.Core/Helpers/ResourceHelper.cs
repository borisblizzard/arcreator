#region Using Directives

using System.Collections.Generic;
using System.IO;
using ARCed.Core;

#endregion

namespace ARCed.Helpers
{
    /// <summary>
    /// Static class that handles finding, organizing, and getting resources automatically from 
    /// both ther local directory and installed RTP directory if there is one.
    /// </summary>
	public static class ResourceHelper
	{

		#region Private Fields

		private static FileSystemWatcher _rtpWatcher;
		private static FileSystemWatcher _localWatcher;
		//private static FileSystemWatcher _scriptWatcher;
		private static List<GameResource> _resources;

	    #endregion

		#region Public Properties

        /// <summary>
        /// File watcher for RTP resources.
        /// </summary>
        public static FileSystemWatcher RtpWatcher
        {
            get { return _rtpWatcher; }
        }

        /// <summary>
        /// File watcher for local project resources.
        /// </summary>
        public static FileSystemWatcher LocalWatcher
        {
            get { return _localWatcher; }
        }
		/// <summary>
		/// Gets an array of filters used for searching resources
		/// </summary>
		public static string[] Filters
		{
            get
            {
                string filters = string.Join("|", Constants.IMAGEFILTERS, 
                    Constants.AUDIOFILTERS, Constants.SCRIPTFILTERS);
                return filters.Split('|');
            }
		}
		/// <summary>
		/// Gets a collection of all resources used by the project, both RTP and local, audio and graphics.
		/// </summary>
		public static List<GameResource> AllResources { get { return _resources; } }
		/// <summary>
		/// Gets a collection of all resources found in the RTP directories
		/// </summary>
		public static List<GameResource> RTPResources
		{
			get
			{
				return _resources.FindAll(r => r.Location == Location.RTP);
			}
		}
		/// <summary>
		/// Gets a collection of all resources found in the local directories
		/// </summary>
		public static List<GameResource> LocalResources
		{
			get
			{
				return _resources.FindAll(r => r.Location == Location.Local);
			}
		}
		/// <summary>
		/// Gets a collection of all graphic resources, both local and RTP
		/// </summary>
		public static List<GameResource> AllGraphics
		{
			get
			{
				return _resources.FindAll(r => r.ResourceType == ResourceType.Graphics);
			}
		}
		/// <summary>
		/// Gets a collection of all audio resources, both local and RTP
		/// </summary>
		public static List<GameResource> AllAudio
		{
			get
			{
				return _resources.FindAll(r => r.ResourceType == ResourceType.Audio);
			}
		}
		/// <summary>
		/// Gets a collection of all audio resources located in the local directory
		/// </summary>
		public static List<GameResource> LocalAudio
		{
			get
			{
				return _resources.FindAll(r => r.ResourceType == ResourceType.Audio && r.Location == Location.Local);
			}
		}
		/// <summary>
		/// Gets a collection of all audio resources located in the RTP directory
		/// </summary>
		public static List<GameResource> RTPAudio
		{
			get
			{
				return _resources.FindAll(r => r.ResourceType == ResourceType.Audio && r.Location == Location.RTP);
			}
		}
		/// <summary>
		/// Gets a collection of all graphic resources located in the local directory
		/// </summary>
		public static List<GameResource> LocalGraphics
		{
			get
			{
				return _resources.FindAll(r => r.ResourceType == ResourceType.Graphics && r.Location == Location.Local);
			}
		}
		/// <summary>
		/// Gets a collection of all graphic resources located in the RTP directory
		/// </summary>
		public static List<GameResource> RTPGraphics
		{
			get
			{
				return _resources.FindAll(r => r.ResourceType == ResourceType.Graphics && r.Location == Location.RTP);
			}
		}

		#endregion

		#region Public Methods

		/// <summary>
		/// Initializes the system. Must be called before system can be used.
		/// </summary>
		public static void Initialize()
		{
		    if (IsInitialized) return;
		    _resources = new List<GameResource>();
		    _localWatcher = new FileSystemWatcher(".") {IncludeSubdirectories = true, EnableRaisingEvents = false};
		    //_scriptWatcher = new FileSystemWatcher(".");
		    _localWatcher.Created += FileSystemWatcherCreated;
		    _localWatcher.Deleted += FileSystemWatcherDeleted;
		    _localWatcher.Renamed += FileSystemWatcherRenamed;
		    if (Directory.Exists(Constants.RTPPath))
		    {
		        _rtpWatcher = new FileSystemWatcher(Constants.RTPPath)
		                          { IncludeSubdirectories = true, EnableRaisingEvents = true };
		        _rtpWatcher.Created += FileSystemWatcherCreated;
		        _rtpWatcher.Deleted += FileSystemWatcherDeleted;
		        _rtpWatcher.Renamed += FileSystemWatcherRenamed;
		        RefreshRTP();
		    }
		    IsInitialized = true;
		}

	    /// <summary>
	    /// Gets the initialized status of the system
	    /// </summary>
	    public static bool IsInitialized { get; private set; }

	    /// <summary>
		/// Recursively searches a directory for filenames using the given filters
		/// </summary>
		/// <param name="rootDir">Root directory to begin search</param>
		/// <param name="filters">Formatted search filters for filenames</param>
		/// <returns>Collection of files found in root directory and all subdirectories that 
		/// matched the given filter(s).</returns>
		public static List<string> DirectorySearch(string rootDir, params string[] filters)
		{
			var fileList = new List<string>();
			foreach (string filter in filters)
				fileList.AddRange(Directory.GetFiles(rootDir, filter));
			foreach (string dir in Directory.GetDirectories(rootDir))
				fileList.AddRange(DirectorySearch(dir, filters));
			return fileList;
		}

		/// <summary>
		/// Refreshes the collection of RTP resources
		/// </summary>
		public static void RefreshRTP()
		{
			_resources.RemoveAll(r => r.Location == Location.RTP);
			var graphics = Path.Combine(Constants.RTPPath, "Graphics");
			var audio = Path.Combine(Constants.RTPPath, "Audio");
			foreach (string filename in DirectorySearch(graphics, Constants.IMAGEFILTERS.Split('|')))
				_resources.Add(new GameResource(filename, Location.RTP, ResourceType.Graphics));
            foreach (string filename in DirectorySearch(audio, Constants.AUDIOFILTERS.Split('|')))
				_resources.Add(new GameResource(filename, Location.RTP, ResourceType.Audio));
		}

		/// <summary>
		/// Refreshes the collection of local resources
		/// </summary>
		public static void RefreshLocal()
		{
			_resources.RemoveAll(r => r.Location == Location.Local);
            foreach (string filename in DirectorySearch("Graphics", Constants.IMAGEFILTERS.Split('|')))
				_resources.Add(new GameResource(filename, Location.Local, ResourceType.Graphics));
            foreach (string filename in DirectorySearch("Audio", Constants.AUDIOFILTERS.Split('|')))
				_resources.Add(new GameResource(filename, Location.Local, ResourceType.Audio));
		}

		/// <summary>
		/// Enables/disables local directory searching
		/// </summary>
		/// <param name="enable">Flag to enable or disable local searching</param>
		public static void EnableLocalDirectory(bool enable)
		{
			_localWatcher.EnableRaisingEvents = enable;
			_localWatcher.Path = Directory.GetCurrentDirectory();
			if (enable)
				RefreshLocal();
			else
				_resources.RemoveAll(r => r.Location == Location.Local);
		}

		/// <summary>
		/// Finds all resources that can be found in the given relative path
		/// </summary>
		/// <param name="folder">Directory that will be searched. This path must be relative to
		/// both the project and the root directory of the RTP</param>
		/// <returns>Collection of found resources</returns>
		public static List<GameResource> GetTypes(string folder)
		{
			var results = _resources.FindAll(r => folder == r.RelativeDirectory);
			results.Sort();
			return results;
		}

		/// <summary>
		/// Gets the full path to a file of the given type using the simple name of the file
		/// </summary>
		/// <param name="folder">Folder name where the file to be found is located.</param>
		/// <param name="name">Simple name of the file, without extension</param>
		/// <returns>Full path to the file</returns>
		public static string GetFullPath(string folder, string name)
		{
			var rsx = _resources.Find(r => r.Name == name && r.RelativeDirectory == folder);
			return rsx != null ? rsx.FullPath : null;
		}

		#endregion

		#region Private Methods

		/// <summary>
		/// Event raised when a file resource file is renamed
		/// </summary>
		/// <param name="sender">Invoker of the event</param>
		/// <param name="e">Event arguments</param>
		private static void FileSystemWatcherRenamed(object sender, RenamedEventArgs e)
		{
			var i = _resources.FindIndex(r => r.FullPath == e.OldFullPath);
			if (i >= 0)
				_resources[i].FileInfo = new FileInfo(e.FullPath);
		}

		/// <summary>
		/// Event raised when a file resource file is deleted
		/// </summary>
		/// <param name="sender">Invoker of the event</param>
		/// <param name="e">Event arguments</param>
		private static void FileSystemWatcherDeleted(object sender, FileSystemEventArgs e)
		{
			_resources.RemoveAll(r => r.FullPath == e.FullPath);
		}

		/// <summary>
		/// Event raised when a file resource file is created
		/// </summary>
		/// <param name="sender">Invoker of the event</param>
		/// <param name="e">Event arguments</param>
		private static void FileSystemWatcherCreated(object sender, FileSystemEventArgs e)
		{
			var location = e.FullPath.Contains(Constants.RTPPath) ? Location.RTP : Location.Local;
			_resources.Add(new GameResource(e.FullPath, location, ResourceType.Unknown));
		}

		#endregion
	}
}
