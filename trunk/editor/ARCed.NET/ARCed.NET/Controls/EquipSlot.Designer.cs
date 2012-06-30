namespace ARCed.Controls
{
	partial class EquipSlot
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

		#region Component Designer generated code

		/// <summary> 
		/// Required method for Designer support - do not modify 
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
			this.labelType = new System.Windows.Forms.Label();
			this.comboBoxEquipment = new System.Windows.Forms.ComboBox();
			this.checkBoxFixed = new System.Windows.Forms.CheckBox();
			this.SuspendLayout();
			// 
			// labelType
			// 
			this.labelType.AutoSize = true;
			this.labelType.Location = new System.Drawing.Point(3, 3);
			this.labelType.Name = "labelType";
			this.labelType.Size = new System.Drawing.Size(79, 13);
			this.labelType.TabIndex = 0;
			this.labelType.Text = "labelEquipment";
			// 
			// comboBoxEquipment
			// 
			this.comboBoxEquipment.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxEquipment.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxEquipment.FormattingEnabled = true;
			this.comboBoxEquipment.Items.AddRange(new object[] {
            "<None>"});
			this.comboBoxEquipment.Location = new System.Drawing.Point(88, 0);
			this.comboBoxEquipment.Name = "comboBoxEquipment";
			this.comboBoxEquipment.Size = new System.Drawing.Size(212, 21);
			this.comboBoxEquipment.TabIndex = 1;
			this.comboBoxEquipment.SelectedIndexChanged += new System.EventHandler(this.comboBoxEquipment_SelectedIndexChanged);
			// 
			// checkBoxFixed
			// 
			this.checkBoxFixed.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.checkBoxFixed.AutoSize = true;
			this.checkBoxFixed.Location = new System.Drawing.Point(306, 2);
			this.checkBoxFixed.Name = "checkBoxFixed";
			this.checkBoxFixed.Size = new System.Drawing.Size(51, 17);
			this.checkBoxFixed.TabIndex = 2;
			this.checkBoxFixed.Text = "Fixed";
			this.checkBoxFixed.UseVisualStyleBackColor = true;
			this.checkBoxFixed.CheckedChanged += new System.EventHandler(this.checkBoxFixed_CheckedChanged);
			// 
			// EquipSlot
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
			this.Controls.Add(this.checkBoxFixed);
			this.Controls.Add(this.comboBoxEquipment);
			this.Controls.Add(this.labelType);
			this.Name = "EquipSlot";
			this.Size = new System.Drawing.Size(360, 21);
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Label labelType;
		private System.Windows.Forms.ComboBox comboBoxEquipment;
		private System.Windows.Forms.CheckBox checkBoxFixed;
	}
}
