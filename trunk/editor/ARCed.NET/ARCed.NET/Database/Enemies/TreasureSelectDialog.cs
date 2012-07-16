#region Using Directives

using System;
using System.Windows.Forms;
using ARCed.Helpers;

#endregion

namespace ARCed.Database.Enemies
{
	/// <summary>
	/// Dialog for selecting possible treasure to be obtained after defeating enemies.
	/// </summary>
	public partial class TreasureSelectDialog : Form
	{
		#region Public Properties

        /// <summary>
        /// Gets the ID of the <see cref="RPG.Item"/> defined in the dialog
        /// </summary>
		public int ItemId
		{
			get
			{
				if (radioButtonItem.Checked)
					return comboBoxItem.SelectedIndex + 1;
				return 0;
			}
		}

		/// <summary>
		/// Gets the ID of the <see cref="RPG.Weapon"/> defined in the dialog
		/// </summary>
		public int WeaponId
		{
			get
			{
				if (radioButtonWeapon.Checked)
					return comboBoxWeapon.SelectedIndex + 1;
				return 0;
			}
		}

        /// <summary>
        /// Gets the ID of the <see cref="RPG.Armor"/> defined in the dialog
        /// </summary>
		public int ArmorId
		{
			get
			{
				if (radioButtonArmor.Checked)
					return comboBoxArmor.SelectedIndex + 1;
				return 0;
			}
		}

		/// <summary>
		/// Gets the probablity defined in the dialog
		/// </summary>
		public int TreasureProbablity
		{
			get { return (int)numericUpDownPropability.Value; } 
		}

		#endregion

		#region Constructor

		/// <summary>
		/// Default constructor
		/// </summary>
		public TreasureSelectDialog()
		{
			InitializeComponent();
			ControlHelper.Populate(comboBoxItem, Project.Data.Items, false);
			ControlHelper.Populate(comboBoxWeapon, Project.Data.Weapons, false);
			ControlHelper.Populate(comboBoxArmor, Project.Data.Armors, false);
		}

		#endregion

		#region Public Methods

		/// <summary>
		/// Sets the values of the control based on current settings
		/// </summary>
		/// <param name="prob">Probablity of obtaining treasure</param>
		/// <param name="itemId">ID of item to be obtained</param>
		/// <param name="weaponId">ID of weapon to be obtained</param>
		/// <param name="armorId">ID of armor to be obtained</param>
		public void SetTreasure(int prob, int itemId, int weaponId, int armorId)
		{
			numericUpDownPropability.Value = prob;
			if (itemId > 0 && itemId < comboBoxItem.Items.Count)
			{
				radioButtonItem.Checked = true;
				comboBoxItem.SelectedIndex = itemId - 1;
			}
			else if (weaponId > 0 && weaponId < comboBoxWeapon.Items.Count)
			{
				radioButtonWeapon.Checked = true;
				comboBoxWeapon.SelectedIndex = weaponId - 1;
			}
			else if (armorId > 0 && armorId < comboBoxArmor.Items.Count)
			{
				radioButtonArmor.Checked = true;
				comboBoxArmor.SelectedIndex = armorId - 1;
			}
		}

		#endregion

		#region Private Methods

		private void ButtonOkClick(object sender, EventArgs e)
		{
			DialogResult = DialogResult.OK;
			Close();
		}

		private void RadioButtonCheckChanged(object sender, EventArgs e)
		{
			bool disableAll = radioButtonNone.Checked;
			comboBoxItem.Enabled = radioButtonItem.Checked && !disableAll;
			comboBoxWeapon.Enabled = radioButtonWeapon.Checked && !disableAll;
			comboBoxArmor.Enabled = radioButtonArmor.Checked && !disableAll;
			numericUpDownPropability.Enabled = !disableAll;
			foreach (ComboBox box in new[] { comboBoxItem, comboBoxWeapon, comboBoxArmor })
			{
				if (box.Enabled && box.SelectedIndex < 0)
					box.SelectedIndex = 0;
				else if (!box.Enabled)
					box.SelectedIndex = -1;
			}
		}

		#endregion
	}
}
