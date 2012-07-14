using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml.Serialization;
using System.ComponentModel;
using System.ComponentModel.Design;

namespace ARCed.Settings
{
	public class EquipmentSettings : List<EquipSlotConfiguration>
	{
		public static EquipmentSettings RmxpConfiguration
		{
			get
			{
				string[] labels = new[] { "Weapon", "Shield", "Helmet", "Body Armor", "Accessory" };
				string[] idAttr = new[] { "weapon_id", "armor1_id", "armor2_id", "armor3_id", "armor4_id" };
				string[] fixedAttr = new[] { "weapon_fix", "armor1_fix", "armor2_fix", "armor3_fix", "armor4_fix" };
				int[] kinds = new[] { -1, 0, 1, 2, 3 };
				EquipmentSettings settings = new EquipmentSettings();
				for (int i = 0; i < 5; i++)
				{
					EquipSlotConfiguration config = new EquipSlotConfiguration();
					config.Label = labels[i];
					config.RpgIdProperty = idAttr[i];
					config.RpgFixedProperty = fixedAttr[i];
					config.EquipKind = kinds[i];
					settings.Add(config);
				}
				return settings;
			}
		}
	}

	[TypeConverterAttribute(typeof(ExpandableObjectConverter))]
	public class EquipSlotConfiguration
	{
		[TypeConverterAttribute(typeof(Int32Converter))]
		[Browsable(true), DefaultValue(0), EditorBrowsable(EditorBrowsableState.Always)]
		public int EquipKind { get; set; }

		[TypeConverterAttribute(typeof(StringConverter))]
		[Browsable(true), DefaultValue(""), EditorBrowsable(EditorBrowsableState.Always)]
		public string Label { get; set; }

		[TypeConverterAttribute(typeof(StringConverter))]
		[Browsable(true), DefaultValue(""), EditorBrowsable(EditorBrowsableState.Always)]
		public string RpgIdProperty { get; set; }

		[TypeConverterAttribute(typeof(StringConverter))]
		[Browsable(true), DefaultValue(""), EditorBrowsable(EditorBrowsableState.Always)]
		public string RpgFixedProperty { get; set; }

		public EquipSlotConfiguration()
		{
			EquipKind = 0;
			Label = "";
			RpgIdProperty = "";
			RpgFixedProperty = "";
		}
	}
}
