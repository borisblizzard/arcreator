#region Using Directives

using System;
using System.IO;

#endregion

namespace ARCed
{
    /// <summary>
    /// Static class for containing constant values used by all assemblies.
    /// </summary>
	public static class Constants
	{
        /// <summary>
        /// Array of strings used for searching supported _srcTexture formats
        /// </summary>
        public const string IMAGEFILTERS = "*.png|.jpg|*.bmp";
        /// <summary>
        /// Array of strings used for searching supported audio formats
        /// </summary>
        public const string AUDIOFILTERS = "*.ogg|*.mid|*.mp3|*.wav";
        /// <summary>
        /// Array of strings used for searching supported script file formats
        /// </summary>
        public const string SCRIPTFILTERS = "*.rb|*.rbw|*.so";

        /// <summary>
        /// Name of the backup folder
        /// </summary>
        public const string BACKUP_FOLDER = "Backups";
        /// <summary>
        /// Name of the settings folder
        /// </summary>
        public const string SETTINGS_FOLDER = "Settings";
        /// <summary>
        /// Name of the graphics folder
        /// </summary>
        public const string GRAPHICS_FOLDER = "Graphics";
        /// <summary>
        /// Name of the audio folder
        /// </summary>
        public const string AUDIO_FOLDER = "Audio";
        /// <summary>
        /// Name of the data folder
        /// </summary>
        public const string DATA_FOLDER = "Data";
        /// <summary>
        /// Name of the scripts folder
        /// </summary>
        public const string SCRIPT_FOLDER = "Scripts";
        /// <summary>
        /// Name of the layout settings file
        /// </summary>
        public const string LAYOUT_FILE = "WindowLayout.xml";
        /// <summary>
        /// Name of the project settings file
        /// </summary>
        public const string PROJECT_SETTINGS_FILE = "ProjectSettings.xml";
        /// <summary>
        /// Frames per second for the game resolution
        /// </summary>
		public const int FRAMERATE = 40;
        /// <summary>
        /// Size in pixels of a map tiles.
        /// </summary>
		public const int TILESIZE = 32;
        /// <summary>
        /// Size in pixels of a tileset graphic
        /// </summary>
		public const int MAXWIDTH = 256;
        /// <summary>
        /// Number of tiles across of a tileset graphic
        /// </summary>
        public const int TILEWIDTH = MAXWIDTH / TILESIZE;
        /// <summary>
        /// Tile IDs reserved for autotiles
        /// </summary>
		public const int AUTO_IDS = 384;
        /// <summary>
        /// Number of autotiles
        /// </summary>
		public const int AUTOTILES = 7;
        /// <summary>
        /// Number of priorities for a tileset
        /// </summary>
		public const int PRIORITIES = 6;
        /// <summary>
        /// Number of terrains for a tileset
        /// </summary>
		public const int TERRAINS = 8;
        /// <summary>
        /// Width and height of a animation source graphic frame
        /// </summary>
		public const int ANIMESIZE = 192;

        private static string _rtpPath;

        /// <summary>
        /// Path to the RTP folder (TEST PURPOSES ONLY)
        /// </summary>
        public static string RTPPath
        {
            get
            {
                if (String.IsNullOrEmpty(_rtpPath))
                {
                    string common = Environment.GetFolderPath(Environment.SpecialFolder.CommonProgramFilesX86);
                    _rtpPath = Path.Combine(common, "Enterbrain", "RGSS", "Standard");
                }
                return _rtpPath;
            }
        }
	}
}
