#region Using Directives

using System;
using System.Collections.Generic;

#endregion

namespace ARCed.Settings
{
	/// <summary>
	/// Class for containing various settings unique to individual projects
	/// </summary>
	[Serializable]
	public class ProjectSettings
	{
        /// <summary>
        /// Gets or sets the settings used for rendering header images
        /// </summary>
        public HeaderSettings HeaderImage { get; set; }
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
        /// <summary>
        /// Gets or sets the max permissable value allowed for Actor max levels.
        /// </summary>
		public int MaxLevel { get; set; }
        /// <summary>
        /// Gets or sets the names of Battler parameters.
        /// </summary>
		public List<string> Parameters { get; set; }
        /// <summary>
        /// Gets or sets the collection of equipment configurations
        /// </summary>
		public EquipmentSettings EquipmentSettings { get; set; }

		/// <summary>
		/// Default constructor
		/// </summary>
		public ProjectSettings()
		{
			OpenScripts = new List<string>();
			ARChiveSettings = new ARChiveSettings();
			Guid = Guid.NewGuid();
			MaxLevel = 99;
			Parameters = new List<string>
			{
				"MaxHP", "MaxSP", "STR", "DEX", "AGI", "INT"
			};
			EquipmentSettings = EquipmentSettings.RmxpConfiguration;
            HeaderImage = new HeaderSettings();
		}

        /// <summary>
        /// Gets the max value for the parameter with the given index.
        /// </summary>
        /// <param name="paramIndex">Index of the parameter</param>
        /// <returns>Maximum value for the parameter.</returns>
		public int GetMaxValue(int paramIndex)
        {
            // TODO: Make this user-defined
            return paramIndex < 2 ? 9999 : 999;
        }
	}
}
