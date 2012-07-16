#region Using Directives

using System.Collections.Generic;

#endregion

namespace ARCed.Settings
{
    /// <summary>
    /// Class containing settings for equipment slots. 
    /// </summary>
    /// <remarks>This class is a wrapper for a standard List of EquipSlotConfiguration objects</remarks>
	public class EquipmentSettings : List<EquipSlotConfiguration>
	{
        /// <summary>
        /// Gets the default configuration used for a converted RMXP project.
        /// </summary>
		public static EquipmentSettings RmxpConfiguration
		{
			get
			{
				var labels = new[] { "Weapon", "Shield", "Helmet", "Body Armor", "Accessory" };
				var idAttr = new[] { "weapon_id", "armor1_id", "armor2_id", "armor3_id", "armor4_id" };
				var fixedAttr = new[] { "weapon_fix", "armor1_fix", "armor2_fix", "armor3_fix", "armor4_fix" };
				var kinds = new[] { -1, 0, 1, 2, 3 };
				var settings = new EquipmentSettings();
				for (var i = 0; i < 5; i++)
				{
					var config = new EquipSlotConfiguration
					{
					    Label = labels[i],
					    RpgIdProperty = idAttr[i],
					    RpgFixedProperty = fixedAttr[i],
					    EquipKind = kinds[i]
					};
				    settings.Add(config);
				}
				return settings;
			}
		}
	}

    /// <summary>
    /// Contains settings determining the name, properties and types of equipment for an equipment slot.
    /// </summary>
	public class EquipSlotConfiguration
	{
        /// <summary>
        /// Gets or sets the kind of equipment this slot contains.
        /// </summary>
		public int EquipKind { get; set; }
        /// <summary>
        /// Gets or sets the associated label for the equipment slot.
        /// </summary>
		public string Label { get; set; }
        /// <summary>
        /// Gets or sets the associated property name of the RPG class to modify
        /// </summary>
		public string RpgIdProperty { get; set; }
        /// <summary>
        /// Gets or sets the fixed flag indicating equipment can be changed.
        /// </summary>
		public string RpgFixedProperty { get; set; }

        /// <summary>
        /// Default constructor
        /// </summary>
		public EquipSlotConfiguration()
		{
			EquipKind = 0;
			Label = "";
			RpgIdProperty = "";
			RpgFixedProperty = "";
		}
	}
}
