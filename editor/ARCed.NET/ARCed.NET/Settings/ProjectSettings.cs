using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using ARCed.Settings;
using System.Xml.Serialization;

namespace ARCed.Settings
{
	/// <summary>
	/// Class for containing various settings unique to individual projects
	/// </summary>
	[Serializable]
	public class ProjectSettings
	{
		/// <summary>
		/// Gets or sets the list of relative filenames of open scripts
		/// </summary>
		public List<string> OpenScripts { get; set; }
		/// <summary>
		/// Gets or sets the settings used for creating backups
		/// </summary>
		public ARChiveSettings ARChiveSettings { get; set; }
		/// <summary>
		/// Gets or sets the GUID for the project.
		/// </summary>
		public Guid Guid { get; set; }


		public int MaxLevel { get; set; }

		public List<string> Parameters { get; set; }

		public EquipmentSettings EquipmentSettings { get; set; }

		/// <summary>
		/// Default constructor
		/// </summary>
		public ProjectSettings()
		{
			OpenScripts = new List<string>();
			ARChiveSettings = new ARChiveSettings();
			Guid = System.Guid.NewGuid();
			MaxLevel = 99;
			Parameters = new List<string>()
			{
				"MaxHP", "MaxSP", "STR", "DEX", "AGI", "INT"
			};
			EquipmentSettings = EquipmentSettings.RmxpConfiguration;
		}

		public int GetMaxValue(int paramIndex)
		{
			if (paramIndex < 2)
				return 9999;
			else
				return 999;
		}
	}
}
