using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Xml.Serialization;
using System.ComponentModel;
using System.Windows.Forms;

namespace ARCed.Settings
{
	[Serializable]
	public enum BackupType
	{
		None = 0x00,
		Scripts = 0x01,
		Maps = 0x02,
		AllData = 0xFF
	}

	[Serializable]
	public enum BackupFrequency
	{
		None,
		Run,
		Debug,
		Save,
		Timed
	}

	[Serializable]
	public class ARChiveSettings
	{
		[XmlIgnore]
		public BackupType Type { get; set; }
		public BackupFrequency Frequency { get; set; }
		public int Interval { get; set; }
		public bool Threaded { get; set; }
		public int MaxBackups { get; set; }

		[XmlElement("Type")]
		[EditorBrowsable(EditorBrowsableState.Never), Browsable(false)]
		public int TypeToInt32
		{
			get { return (int)Type; }
			set { Type = (BackupType)value; }
		}

		public ARChiveSettings()
		{
			Type = BackupType.AllData;
			Frequency = BackupFrequency.Timed;
			Interval = 10;
			Threaded = true;
			MaxBackups = 5;
		}

		/// <summary>
		/// Deletes backup files when the number of files exceeds the maximum allowed
		/// </summary>
		/// <remarks>The "Creation Time" attribute of the file is used to delete 
		/// the files in order of the oldest first.</remarks>
		public void TrimExcess()
		{
			List<FileInfo> infos;
			infos = new DirectoryInfo(Project.BackupDirectory).GetFiles("*.7z").ToList();
			infos.Sort(delegate(FileInfo a, FileInfo b) { 
				return b.CreationTime.CompareTo(a.CreationTime); });
			for (int i = MaxBackups; i < infos.Count; i++)
			{
				try { File.Delete(infos[i].FullName); }
				catch (IOException)
				{
					MessageBox.Show("Failed to remove old ARChive.\nFile is locked by another process.",
						"Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
				}
			}
		}
	}
}
