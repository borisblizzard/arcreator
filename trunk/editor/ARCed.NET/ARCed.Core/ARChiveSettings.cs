#region Using Directives

using System;
using System.ComponentModel;
using System.Xml.Serialization;

#endregion

namespace ARCed.Settings
{
    /// <summary>
    /// Flags used for determining the type of data to backup.
    /// </summary>
	[Serializable, Flags]
	public enum BackupType
	{
        /// <summary>
        /// No data will be backed up.
        /// </summary>
		None = 0x00,
        /// <summary>
        /// Script files will be backed up.
        /// </summary>
		Scripts = 0x01,
        /// <summary>
        /// Map data will be backed up.
        /// </summary>
		Maps = 0x02,
        /// <summary>
        /// All data will be backed up.
        /// </summary>
		AllData = 0xFF
	}

    /// <summary>
    /// Flags for specifying the frequency when data will be backed up.
    /// </summary>
	[Serializable]
	public enum BackupFrequency
	{
        /// <summary>
        /// Backups are not created
        /// </summary>
		None,
        /// <summary>
        /// Each time the project is ran from the editor
        /// </summary>
		Run,
        /// <summary>
        /// Each time the project is ran from the editor in DEBUG mode
        /// </summary>
		Debug,
        /// <summary>
        /// Each time data is saved 
        /// </summary>
		Save,
        /// <summary>
        /// At timed intervals
        /// </summary>
		Timed
	}

    /// <summary>
    /// Class the contains settings on 
    /// </summary>
	[Serializable]
	public class ARChiveSettings
	{
        /// <summary>
        /// Gets or sets the BackupType setting.
        /// </summary>
		[XmlIgnore]
		public BackupType Type { get; set; }

        /// <summary>
        /// Gets or sets the frequency backups are created.
        /// </summary>
		public BackupFrequency Frequency { get; set; }

        /// <summary>
        /// Gets or sets the interval that backups are created when using BackupType.Interval
        /// </summary>
		public int Interval { get; set; }

        /// <summary>
        /// Gets or sets the flag to have the backups copied and compressed on a separate thread.
        /// </summary>
		public bool Threaded { get; set; }

        /// <summary>
        /// Gets or sets the maximum number of backups that will be created before overwriting begins.
        /// </summary>
		public int MaxBackups { get; set; }

        /// <summary>
        /// Gets or sets the BackupType flag as an integer.
        /// </summary>
		[XmlElement("Type")]
		[EditorBrowsable(EditorBrowsableState.Never), Browsable(false)]
		public int TypeToInt32
		{
			get { return (int)this.Type; }
			set { this.Type = (BackupType)value; }
		}

        /// <summary>
        /// Fefault constructor.
        /// </summary>
		public ARChiveSettings()
		{
			this.Type = BackupType.AllData;
			this.Frequency = BackupFrequency.Timed;
			this.Interval = 10;
			this.Threaded = true;
			this.MaxBackups = 5;
		}
	}
}
