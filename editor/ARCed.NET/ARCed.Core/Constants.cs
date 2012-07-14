using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ARCed
{
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

        // Defines names of ARC folders
        public const string BACKUP_FOLDER = "Backups";
        public const string SETTINGS_FOLDER = "Settings";
        public const string GRAPHICS_FOLDER = "Graphics";
        public const string AUDIO_FOLDER = "Audio";
        public const string DATA_FOLDER = "Data";
        public const string SCRIPT_FOLDER = "Scripts";

        // Defines names of ARCed.NET files
        public const string LAYOUT_FILE = "WindowLayout.xml";
        public const string PROJECT_SETTINGS_FILE = "ProjectSettings.xml";

		public const int FRAMERATE = 40;
		public const int TILESIZE = 32;
		public const int MAXWIDTH = 256;
		public const int TILEWIDTH = 8;
		public const int AUTO_IDS = 384;
		public const int AUTOTILES = 7;
		public const int PRIORITIES = 6;
		public const int TERRAINS = 8;
		public const int ANIMESIZE = 192;

		public const string RTP_PATH = @"C:\Program Files (x86)\Common Files\Enterbrain\RGSS\Standard";
	}
}
