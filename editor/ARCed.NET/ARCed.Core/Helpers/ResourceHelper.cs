using System.Collections.Generic;
using System.IO;
using System.Linq;
using ARCed.Core;

namespace ARCed.Helpers
{
	public static class ResourceHelper
	{

		public static FileSystemWatcher RtpWatcher
		{
			get { return _rtpWatcher; }
		}

		public static FileSystemWatcher LocalWatcher
		{
			get { return _localWatcher; }
		}

		#region Private Fields

		private static FileSystemWatcher _rtpWatcher;
		private static FileSystemWatcher _localWatcher;
		private static FileSystemWatcher _scriptWatcher;
		private static List<GameResource> _resources;
		private static bool _initialized;

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets an array of filters used for searching resources
		/// </summary>
		public static string[] Filters
		{
            get
            {
                string f = string.Join("|", Constants.IMAGEFILTERS, Constants.AUDIOFILTERS, Constants.SCRIPTFILTERS);
                return f.Split('|');
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
				return _resources.FindAll(delegate(GameResource r)
				{
					return r.Location == Location.RTP;
				});
			}
		}
		/// <summary>
		/// Gets a collection of all resources found in the local directories
		/// </summary>
		public static List<GameResource> LocalResources
		{
			get
			{
				return _resources.FindAll(delegate(GameResource r)
				{
					return r.Location == Location.Local;
				});
			}
		}
		/// <summary>
		/// Gets a collection of all graphic resources, both local and RTP
		/// </summary>
		public static List<GameResource> AllGraphics
		{
			get
			{
				return _resources.FindAll(delegate(GameResource r)
				{
					return r.ResourceType == ResourceType.Graphics;
				});
			}
		}
		/// <summary>
		/// Gets a collection of all audio resources, both local and RTP
		/// </summary>
		public static List<GameResource> AllAudio
		{
			get
			{
				return _resources.FindAll(delegate(GameResource r)
				{
					return r.ResourceType == ResourceType.Audio;
				});
			}
		}
		/// <summary>
		/// Gets a collection of all audio resources located in the local directory
		/// </summary>
		public static List<GameResource> LocalAudio
		{
			get
			{
				return _resources.FindAll(delegate(GameResource r)
				{
					return r.ResourceType == ResourceType.Audio && r.Location == Location.Local;
				});
			}
		}
		/// <summary>
		/// Gets a collection of all audio resources located in the RTP directory
		/// </summary>
		public static List<GameResource> RTPAudio
		{
			get
			{
				return _resources.FindAll(delegate(GameResource r)
				{
					return r.ResourceType == ResourceType.Audio && r.Location == Location.RTP;
				});
			}
		}
		/// <summary>
		/// Gets a collection of all graphic resources located in the local directory
		/// </summary>
		public static List<GameResource> LocalGraphics
		{
			get
			{
				return _resources.FindAll(delegate(GameResource r)
				{
					return r.ResourceType == ResourceType.Graphics && r.Location == Location.Local;
				});
			}
		}
		/// <summary>
		/// Gets a collection of all graphic resources located in the RTP directory
		/// </summary>
		public static List<GameResource> RTPGraphics
		{
			get
			{
				return _resources.FindAll(delegate(GameResource r)
				{
					return r.ResourceType == ResourceType.Graphics && r.Location == Location.RTP;
				});
			}
		}

		#endregion

		#region Public Methods

		/// <summary>
		/// Initializes the system. Must be called before system can be used.
		/// </summary>
		public static void Initialize()
		{
			if (!_initialized)
			{
				_resources = new List<GameResource>();
				_rtpWatcher = new FileSystemWatcher(Constants.RTP_PATH);
				_localWatcher = new FileSystemWatcher(".");
				//_scriptWatcher = new FileSystemWatcher(".");
				_rtpWatcher.IncludeSubdirectories = true;
				_rtpWatcher.EnableRaisingEvents = true;
				_localWatcher.IncludeSubdirectories = true;
				_localWatcher.EnableRaisingEvents = false;
				_rtpWatcher.Created += new FileSystemEventHandler(fileSystemWatcher_Created);
				_rtpWatcher.Deleted += new FileSystemEventHandler(fileSystemWatcher_Deleted);
				_rtpWatcher.Renamed += new RenamedEventHandler(fileSystemWatcher_Renamed);
				_localWatcher.Created += new FileSystemEventHandler(fileSystemWatcher_Created);
				_localWatcher.Deleted += new FileSystemEventHandler(fileSystemWatcher_Deleted);
				_localWatcher.Renamed += new RenamedEventHandler(fileSystemWatcher_Renamed);
				_initialized = true;
				RefreshRTP();
			}
		}

		/// <summary>
		/// Gets the initialized status of the system
		/// </summary>
		public static bool IsInitialized { get { return _initialized; } }

		/// <summary>
		/// Recursively searches a directory for filenames using the given filters
		/// </summary>
		/// <param _frames="rootDir">Root directory to begin search</param>
		/// <param _frames="filters">Formatted search filters for filenames</param>
		/// <returns>Collection of files found in root directory and all subdirectories that 
		/// matched the given filter(s).</returns>
		public static List<string> DirectorySearch(string rootDir, params string[] filters)
		{
			List<string> fileList = new List<string>();
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
			_resources.RemoveAll(delegate(GameResource r) { return r.Location == Location.RTP; });
			string graphics = Path.Combine(Constants.RTP_PATH, "Graphics");
			string audio = Path.Combine(Constants.RTP_PATH, "Audio");
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
			_resources.RemoveAll(delegate(GameResource r) { return r.Location == Location.Local; });
            foreach (string filename in DirectorySearch("Graphics", Constants.IMAGEFILTERS.Split('|')))
				_resources.Add(new GameResource(filename, Location.Local, ResourceType.Graphics));
            foreach (string filename in DirectorySearch("Audio", Constants.AUDIOFILTERS.Split('|')))
				_resources.Add(new GameResource(filename, Location.Local, ResourceType.Audio));
		}

		/// <summary>
		/// Enables/disables local directory searching
		/// </summary>
		/// <param _frames="enable">Flag to enable or disable local searching</param>
		public static void EnableLocalDirectory(bool enable)
		{
			_localWatcher.EnableRaisingEvents = enable;
			_localWatcher.Path = Directory.GetCurrentDirectory();
			if (enable)
				RefreshLocal();
			else
				_resources.RemoveAll(delegate(GameResource r) { return r.Location == Location.Local; });
		}

		/// <summary>
		/// Finds all resources that can be found in the given relative path
		/// </summary>
		/// <param _frames="folder">Directory that will be searched. This path must be relative to
		/// both the project and the root directory of the RTP</param>
		/// <returns>Collection of found resources</returns>
		public static List<GameResource> GetTypes(string folder)
		{
			var results = _resources.FindAll(delegate(GameResource r) {
				return folder == r.RelativeDirectory; });
			results.Sort();
			return results;
		}

		/// <summary>
		/// Gets the full path to a file of the given type using the simple _frames of the file
		/// </summary>
		/// <param _frames="type">Detailed type of the file to find</param>
		/// <param _frames="_frames">Simple _frames of the file, without extension</param>
		/// <returns>Full path to the file</returns>
		public static string GetFullPath(string folder, string name)
		{
			GameResource rsx = _resources.Find(delegate(GameResource r) { 
				return r.Name == name && r.RelativeDirectory == folder; });
			if (rsx != null)
				return rsx.FullPath;
			return null;
		}

		#endregion

		#region Private Methods

		/// <summary>
		/// Event raised when a file resource file is renamed
		/// </summary>
		/// <param _frames="sender">Invoker of the event</param>
		/// <param _frames="e">Event arguments</param>
		private static void fileSystemWatcher_Renamed(object sender, RenamedEventArgs e)
		{
			int i = _resources.FindIndex(delegate(GameResource r) { return r.FullPath == e.OldFullPath; });
			if (i >= 0)
				_resources[i].FileInfo = new FileInfo(e.FullPath);
		}

		/// <summary>
		/// Event raised when a file resource file is deleted
		/// </summary>
		/// <param _frames="sender">Invoker of the event</param>
		/// <param _frames="e">Event arguments</param>
		private static void fileSystemWatcher_Deleted(object sender, FileSystemEventArgs e)
		{
			_resources.RemoveAll(delegate(GameResource r) { return r.FullPath == e.FullPath; });
		}

		/// <summary>
		/// Event raised when a file resource file is created
		/// </summary>
		/// <param _frames="sender">Invoker of the event</param>
		/// <param _frames="e">Event arguments</param>
		private static void fileSystemWatcher_Created(object sender, FileSystemEventArgs e)
		{
			Location location = e.FullPath.Contains(Constants.RTP_PATH) ? Location.RTP : Location.Local;
			_resources.Add(new GameResource(e.FullPath, location, ResourceType.Unknown));
		}

		#endregion
	}
}
