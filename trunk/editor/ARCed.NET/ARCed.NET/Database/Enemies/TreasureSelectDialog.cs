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
				if (this.radioButtonItem.Checked)
					return this.comboBoxItem.SelectedIndex + 1;
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
				if (this.radioButtonWeapon.Checked)
					return this.comboBoxWeapon.SelectedIndex + 1;
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
				if (this.radioButtonArmor.Checked)
					return this.comboBoxArmor.SelectedIndex + 1;
				return 0;
			}
		}

		/// <summary>
		/// Gets the probablity defined in the dialog
		/// </summary>
		public int TreasureProbablity
		{
			get { return (int)this.numericUpDownPropability.Value; } 
		}

		#endregion

		#region Constructor

		/// <summary>
		/// Default constructor
		/// </summary>
		public TreasureSelectDialog()
		{
			this.InitializeComponent();
			ControlHelper.Populate(this.comboBoxItem, Project.Data.Items, false);
			ControlHelper.Populate(this.comboBoxWeapon, Project.Data.Weapons, false);
			ControlHelper.Populate(this.comboBoxArmor, Project.Data.Armors, false);
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
			this.numericUpDownPropability.Value = prob;
			if (itemId > 0 && itemId < this.comboBoxItem.Items.Count)
			{
				this.radioButtonItem.Checked = true;
				this.comboBoxItem.SelectedIndex = itemId - 1;
			}
			else if (weaponId > 0 && weaponId < this.comboBoxWeapon.Items.Count)
			{
				this.radioButtonWeapon.Checked = true;
				this.comboBoxWeapon.SelectedIndex = weaponId - 1;
			}
			else if (armorId > 0 && armorId < this.comboBoxArmor.Items.Count)
			{
				this.radioButtonArmor.Checked = true;
				this.comboBoxArmor.SelectedIndex = armorId - 1;
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
			bool disableAll = this.radioButtonNone.Checked;
			this.comboBoxItem.Enabled = this.radioButtonItem.Checked && !disableAll;
			this.comboBoxWeapon.Enabled = this.radioButtonWeapon.Checked && !disableAll;
			this.comboBoxArmor.Enabled = this.radioButtonArmor.Checked && !disableAll;
			this.numericUpDownPropability.Enabled = !disableAll;
			foreach (ComboBox box in new[] { this.comboBoxItem, this.comboBoxWeapon, this.comboBoxArmor })
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
