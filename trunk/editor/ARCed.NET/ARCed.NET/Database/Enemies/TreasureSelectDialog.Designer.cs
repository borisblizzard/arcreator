namespace ARCed.Database.Enemies
{
	partial class TreasureSelectDialog
	{
		/// <summary>
		/// Required designer variable.
		/// </summary>
		private System.ComponentModel.IContainer components = null;

		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		/// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing && (components != null))
			{
				components.Dispose();
			}
			base.Dispose(disposing);
		}

		#region Windows Form Designer generated code

		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
			this.radioButtonNone = new System.Windows.Forms.RadioButton();
			this.radioButtonItem = new System.Windows.Forms.RadioButton();
			this.radioButtonArmor = new System.Windows.Forms.RadioButton();
			this.radioButtonWeapon = new System.Windows.Forms.RadioButton();
			this.comboBoxItem = new System.Windows.Forms.ComboBox();
			this.comboBoxWeapon = new System.Windows.Forms.ComboBox();
			this.comboBoxArmor = new System.Windows.Forms.ComboBox();
			this.buttonCancel = new System.Windows.Forms.Button();
			this.buttonOK = new System.Windows.Forms.Button();
			this.label1 = new System.Windows.Forms.Label();
			this.numericUpDownPropability = new System.Windows.Forms.NumericUpDown();
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownPropability)).BeginInit();
			this.SuspendLayout();
			// 
			// radioButtonNone
			// 
			this.radioButtonNone.AutoSize = true;
			this.radioButtonNone.Checked = true;
			this.radioButtonNone.Location = new System.Drawing.Point(3, 13);
			this.radioButtonNone.Name = "radioButtonNone";
			this.radioButtonNone.Size = new System.Drawing.Size(51, 17);
			this.radioButtonNone.TabIndex = 0;
			this.radioButtonNone.TabStop = true;
			this.radioButtonNone.Text = "None";
			this.radioButtonNone.UseVisualStyleBackColor = true;
			this.radioButtonNone.CheckedChanged += new System.EventHandler(this.radioButton_CheckChanged);
			// 
			// radioButtonItem
			// 
			this.radioButtonItem.AutoSize = true;
			this.radioButtonItem.Location = new System.Drawing.Point(3, 40);
			this.radioButtonItem.Name = "radioButtonItem";
			this.radioButtonItem.Size = new System.Drawing.Size(45, 17);
			this.radioButtonItem.TabIndex = 1;
			this.radioButtonItem.Text = "Item";
			this.radioButtonItem.UseVisualStyleBackColor = true;
			this.radioButtonItem.CheckedChanged += new System.EventHandler(this.radioButton_CheckChanged);
			// 
			// radioButtonArmor
			// 
			this.radioButtonArmor.AutoSize = true;
			this.radioButtonArmor.Location = new System.Drawing.Point(3, 94);
			this.radioButtonArmor.Name = "radioButtonArmor";
			this.radioButtonArmor.Size = new System.Drawing.Size(52, 17);
			this.radioButtonArmor.TabIndex = 3;
			this.radioButtonArmor.Text = "Armor";
			this.radioButtonArmor.UseVisualStyleBackColor = true;
			this.radioButtonArmor.CheckedChanged += new System.EventHandler(this.radioButton_CheckChanged);
			// 
			// radioButtonWeapon
			// 
			this.radioButtonWeapon.AutoSize = true;
			this.radioButtonWeapon.Location = new System.Drawing.Point(3, 67);
			this.radioButtonWeapon.Name = "radioButtonWeapon";
			this.radioButtonWeapon.Size = new System.Drawing.Size(66, 17);
			this.radioButtonWeapon.TabIndex = 2;
			this.radioButtonWeapon.Text = "Weapon";
			this.radioButtonWeapon.UseVisualStyleBackColor = true;
			this.radioButtonWeapon.CheckedChanged += new System.EventHandler(this.radioButton_CheckChanged);
			// 
			// comboBoxItem
			// 
			this.comboBoxItem.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxItem.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxItem.Enabled = false;
			this.comboBoxItem.FormattingEnabled = true;
			this.comboBoxItem.Location = new System.Drawing.Point(88, 39);
			this.comboBoxItem.Name = "comboBoxItem";
			this.comboBoxItem.Size = new System.Drawing.Size(169, 21);
			this.comboBoxItem.TabIndex = 5;
			// 
			// comboBoxWeapon
			// 
			this.comboBoxWeapon.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxWeapon.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxWeapon.Enabled = false;
			this.comboBoxWeapon.FormattingEnabled = true;
			this.comboBoxWeapon.Location = new System.Drawing.Point(88, 66);
			this.comboBoxWeapon.Name = "comboBoxWeapon";
			this.comboBoxWeapon.Size = new System.Drawing.Size(169, 21);
			this.comboBoxWeapon.TabIndex = 6;
			// 
			// comboBoxArmor
			// 
			this.comboBoxArmor.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxArmor.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxArmor.Enabled = false;
			this.comboBoxArmor.FormattingEnabled = true;
			this.comboBoxArmor.Location = new System.Drawing.Point(88, 93);
			this.comboBoxArmor.Name = "comboBoxArmor";
			this.comboBoxArmor.Size = new System.Drawing.Size(169, 21);
			this.comboBoxArmor.TabIndex = 7;
			// 
			// buttonCancel
			// 
			this.buttonCancel.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
			this.buttonCancel.Location = new System.Drawing.Point(182, 142);
			this.buttonCancel.Name = "buttonCancel";
			this.buttonCancel.Size = new System.Drawing.Size(75, 23);
			this.buttonCancel.TabIndex = 8;
			this.buttonCancel.Text = "Cancel";
			this.buttonCancel.UseVisualStyleBackColor = true;
			// 
			// buttonOK
			// 
			this.buttonOK.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonOK.Location = new System.Drawing.Point(101, 142);
			this.buttonOK.Name = "buttonOK";
			this.buttonOK.Size = new System.Drawing.Size(75, 23);
			this.buttonOK.TabIndex = 9;
			this.buttonOK.Text = "OK";
			this.buttonOK.UseVisualStyleBackColor = true;
			this.buttonOK.Click += new System.EventHandler(this.buttonOK_Click);
			// 
			// label1
			// 
			this.label1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.label1.AutoSize = true;
			this.label1.Location = new System.Drawing.Point(9, 129);
			this.label1.Name = "label1";
			this.label1.Size = new System.Drawing.Size(58, 13);
			this.label1.TabIndex = 10;
			this.label1.Text = "Probability:";
			// 
			// numericUpDownPropability
			// 
			this.numericUpDownPropability.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.numericUpDownPropability.Enabled = false;
			this.numericUpDownPropability.Location = new System.Drawing.Point(12, 145);
			this.numericUpDownPropability.Name = "numericUpDownPropability";
			this.numericUpDownPropability.Size = new System.Drawing.Size(58, 20);
			this.numericUpDownPropability.TabIndex = 11;
			this.numericUpDownPropability.Value = new decimal(new int[] {
            50,
            0,
            0,
            0});
			// 
			// TreasureSelectDialog
			// 
			this.AcceptButton = this.buttonOK;
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.CancelButton = this.buttonCancel;
			this.ClientSize = new System.Drawing.Size(269, 179);
			this.Controls.Add(this.numericUpDownPropability);
			this.Controls.Add(this.label1);
			this.Controls.Add(this.buttonOK);
			this.Controls.Add(this.buttonCancel);
			this.Controls.Add(this.comboBoxArmor);
			this.Controls.Add(this.comboBoxWeapon);
			this.Controls.Add(this.comboBoxItem);
			this.Controls.Add(this.radioButtonArmor);
			this.Controls.Add(this.radioButtonWeapon);
			this.Controls.Add(this.radioButtonItem);
			this.Controls.Add(this.radioButtonNone);
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
			this.MaximizeBox = false;
			this.MinimizeBox = false;
			this.Name = "TreasureSelectDialog";
			this.ShowInTaskbar = false;
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
			this.Text = "Treasure";
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownPropability)).EndInit();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.RadioButton radioButtonNone;
		private System.Windows.Forms.RadioButton radioButtonItem;
		private System.Windows.Forms.RadioButton radioButtonArmor;
		private System.Windows.Forms.RadioButton radioButtonWeapon;
		private System.Windows.Forms.ComboBox comboBoxItem;
		private System.Windows.Forms.ComboBox comboBoxWeapon;
		private System.Windows.Forms.ComboBox comboBoxArmor;
		private System.Windows.Forms.Button buttonCancel;
		private System.Windows.Forms.Button buttonOK;
		private System.Windows.Forms.Label label1;
		private System.Windows.Forms.NumericUpDown numericUpDownPropability;
	}
}