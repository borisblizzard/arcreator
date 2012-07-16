#region Using Directives

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Windows.Forms;
using ARCed.Settings;
using RPG;

#endregion

namespace ARCed.Controls
{
	/// <summary>
	/// Control for displaying and setting equipment on an actor.
	/// </summary>
	[Category("ARCed"), Description("Control for displaying and setting equipment on an actor.")]
	public partial class EquipSlot : UserControl
	{

		private EquipSlotConfiguration _configuration;

		#region Events

		public delegate void EquipmentChangedEventHandler(object sender, EquipmentChangedEventArgs e);
		/// <summary>
		/// Event fired when the equipment is changed in the combo box.
		/// </summary>
		[Category("ARCed"), Description("Event fired when the equipment is changed in the combo box.")]
		public event EquipmentChangedEventHandler OnEquipmentChange;

		public delegate void EquipFixChangedEventHandler(object sender, EquipFixChangedEventArgs e);
		/// <summary>
		/// Event fired when the fixed status is changed with the checkbox control.
		/// </summary>
		[Category("ARCed"), Description("Event fired when the fixed status is changed with the checkbox control.")]
		public event EquipFixChangedEventHandler OnEquipFixChange;

		#endregion

		#region Public Properties

		[Browsable(false)]
		public EquipSlotConfiguration Configuration 
		{ 
			get
			{
				if (_configuration == null)
					_configuration = new EquipSlotConfiguration();
				return _configuration;
			}
			set 
			{
				if (value != null)
				{
					_configuration = value;
					labelType.Text = value.Label + ":";
					RefreshItems(null);
				}
			} 
		}

		/// <summary>
		/// Gets or sets the type of items that the equipment slot contains
		/// </summary>
		[Category("ARCed"), Description("Defines the type of items that the equipment slot contains")]
		public int EquipKind 
		{ 
			get { return Configuration.EquipKind; }
			set { Configuration.EquipKind = value; }
		}

		/// <summary>
		/// Gets a collection of the items in the combo control
		/// </summary>
		[Category("ARCed"), Description("Specifies the items in the equipmeny ComboBox.")]
		public ComboBox.ObjectCollection Items
		{
			get { return comboBoxEquipment.Items; }
		}

		/// <summary>
		/// Gets or sets the label of the equipment type. 
		/// </summary>
		[DefaultValue("Equipment")]
		[Category("ARCed"), Description("Defines the label of the equipment type.")]
		public string Label 
		{ 
			get { return Configuration.Label; }
			set { Configuration.Label = value; labelType.Text = value + ":"; }
		}

		/// <summary>
		/// Gets or sets the fixed status of the equipment slot.
		/// </summary>
		[Category("ARCed"), Description("Define the fixed state of the equipment slot.")]
		public bool Fixed
		{
			get { return checkBoxFixed.Checked; }
			set { checkBoxFixed.Checked = value; }
		}

		/// <summary>
		/// Name of the RPG object property the equipment ID value represents.
		/// </summary>
		[DefaultValue("")]
		[Category("ARCed"), Description("Name of the RPG object property the equipment ID value represents.")]
		public string RpgIdAttribute 
		{ 
			get { return Configuration.RpgIdProperty; }
			set { Configuration.RpgIdProperty = value; }
		}

		/// <summary>
		/// Name of the RPG object property the fixed value represents.
		/// </summary>
		[DefaultValue("")]
		[Category("ARCed"), Description("Name of the RPG object property the \"fixed\" value represents.")]
		public string RpgFixedAttribute
		{
			get { return Configuration.RpgFixedProperty; }
			set { Configuration.RpgFixedProperty = value; }
		}

		/// <summary>
		/// Gets or sets the selected index of the equipment combobox
		/// </summary>
		[Browsable(false)]
		public int SelectedIndex
		{
			get { return comboBoxEquipment.SelectedIndex; }
			set { comboBoxEquipment.SelectedIndex = value; }
		}

		#endregion

		#region Constructors

		/// <summary>
		/// Default constructor
		/// </summary>
		public EquipSlot()
		{
			InitializeComponent();
		}

		#endregion

		#region Public Methods

		/// <summary>
		/// Refreshes the list of items/equipment in the combo box control
		/// </summary>
		/// <param name="ids"></param>
		public void RefreshItems(List<dynamic> ids)
		{
			comboBoxEquipment.BeginUpdate();
			comboBoxEquipment.Items.Clear();
			comboBoxEquipment.Items.Add("<None>");
			if (ids == null)
			{
				comboBoxEquipment.EndUpdate();
				return;
			}
			Armor armor;
			foreach (int id in ids)
			{
				if (EquipKind < 0) // Weapon
					comboBoxEquipment.Items.Add(Project.Data.Weapons[id].ToString());
				else // Armor
				{
					armor = Project.Data.Armors[id];
					if (armor.kind == EquipKind)
						comboBoxEquipment.Items.Add(armor.ToString());
				}
			}
			comboBoxEquipment.EndUpdate();
		}

		/// <summary>
		/// Returns the ID of the selected piece of equipment.
		/// </summary>
		/// <returns>ID of the selected equipment</returns>
		public int GetItemId()
		{
			string[] text = comboBoxEquipment.Text.Split(':');
			if (text.Length <= 1)
				return 0;
			return Convert.ToInt32(text[0]);
		}

		/// <summary>
		/// Sets the equipment that has the given ID as the current item.
		/// </summary>
		/// <param name="id">ID of the equipement to set.</param>
		public void SetItemId(int id)
		{
			int itemId;
			string subString;
			for (int i = 1; i < comboBoxEquipment.Items.Count; i++)
			{
				subString = comboBoxEquipment.Items[i].ToString();
				itemId = Convert.ToInt32(subString.Substring(0, 4));
				if (itemId == id)
				{
					comboBoxEquipment.SelectedIndex = i;
					return;
				}
			}
			comboBoxEquipment.SelectedIndex = 0;
		}

		/// <summary>
		/// Maintains performance while items are added to the control's 
		/// ComboBox one at a time by preventing painting until EndUpdate() is called.
		/// </summary>
		public void BeginUpdate()
		{
			comboBoxEquipment.BeginUpdate();
		}

		/// <summary>
		/// Resumes painting of the control's ComboBox after painting is suspended from calling BeginUpdate().
		/// </summary>
		public void EndUpdate()
		{
			comboBoxEquipment.EndUpdate();
		}

		#endregion

		#region Private Methods

		private void checkBoxFixed_CheckedChanged(object sender, EventArgs e)
		{
			if (OnEquipFixChange != null)
				OnEquipFixChange(this, new EquipFixChangedEventArgs(checkBoxFixed.Checked, RpgFixedAttribute));
		}

		private void comboBoxEquipment_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (OnEquipmentChange != null)
				OnEquipmentChange(this,
					new EquipmentChangedEventArgs(comboBoxEquipment.SelectedIndex, GetItemId(), RpgIdAttribute));
		}

		#endregion
	}

	/// <summary>
	/// Event arguments used for changing equipment events
	/// </summary>
	public class EquipmentChangedEventArgs
	{
		/// <summary>
		/// Gets the index of the item
		/// </summary>
		public int Index { get; private set; }
		/// <summary>
		/// Gets the ID of the item's selected equipment
		/// </summary>
		public int EquipmentId { get; private set; }
		/// <summary>
		/// Name of the RPG object property this value represents
		/// </summary>
		public string PropertyName { get; private set; }

		/// <summary>
		/// Default constructor
		/// </summary>
		/// <param name="index">Index of the item</param>
		/// <param name="equipmentId">ID of the item's selected equipment</param>
		/// <param name="propertyName">Name of the RPG object property this value represents</param>
		public EquipmentChangedEventArgs(int index, int equipmentId, string propertyName)
		{
			Index = index;
			EquipmentId = equipmentId;
			PropertyName = propertyName;
		}
	}

	/// <summary>
	/// Event arguments for used for changing fixed status events
	/// </summary>
	public class EquipFixChangedEventArgs
	{
		/// <summary>
		/// Gets the value indicating the fixed status of the slot
		/// </summary>
		public bool Fixed { get; private set; }

		/// <summary>
		/// Name of the RPG object property this value represents
		/// </summary>
		public string PropertyName { get; private set; }

		/// <summary>
		/// Default constructor
		/// </summary>
		/// <param name="value">Value indicating the fixed status of the slot</param>
		/// <param name="propertyName">Name of the RPG object property this value represents</param>
		public EquipFixChangedEventArgs(bool value, string propertyName)
		{
			Fixed = value;
			PropertyName = propertyName;
		}
	}
}
