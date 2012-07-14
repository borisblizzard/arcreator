namespace ARCed.Controls
{
	partial class EfficiencySlot
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
			this.domainUpDown = new System.Windows.Forms.DomainUpDown();
			this.labelValue = new System.Windows.Forms.Label();
			this.SuspendLayout();
			// 
			// domainUpDown
			// 
			this.domainUpDown.BackColor = System.Drawing.SystemColors.Window;
			this.domainUpDown.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.domainUpDown.Location = new System.Drawing.Point(0, 0);
			this.domainUpDown.Name = "domainUpDown";
			this.domainUpDown.ReadOnly = true;
			this.domainUpDown.Size = new System.Drawing.Size(45, 20);
			this.domainUpDown.TabIndex = 0;
			this.domainUpDown.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			this.domainUpDown.Wrap = true;
			// 
			// labelValue
			// 
			this.labelValue.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.labelValue.Location = new System.Drawing.Point(51, 3);
			this.labelValue.Margin = new System.Windows.Forms.Padding(3);
			this.labelValue.Name = "labelValue";
			this.labelValue.Size = new System.Drawing.Size(87, 14);
			this.labelValue.TabIndex = 1;
			this.labelValue.Text = "label";
			// 
			// EfficiencySlot
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.Controls.Add(this.labelValue);
			this.Controls.Add(this.domainUpDown);
			this.Margin = new System.Windows.Forms.Padding(3, 1, 3, 1);
			this.Name = "EfficiencySlot";
			this.Size = new System.Drawing.Size(141, 20);
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.DomainUpDown domainUpDown;
		private System.Windows.Forms.Label labelValue;
	}
}
