namespace ARCed.Controls
{
	partial class FontSelector
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
			this.groupBoxFont = new System.Windows.Forms.GroupBox();
			this.panelSample = new System.Windows.Forms.Panel();
			this.labelSample = new System.Windows.Forms.Label();
			this.numericSize = new System.Windows.Forms.NumericUpDown();
			this.labelSize = new System.Windows.Forms.Label();
			this.groupBoxStyle = new System.Windows.Forms.GroupBox();
			this.checkBoxUnderline = new System.Windows.Forms.CheckBox();
			this.checkBoxItalic = new System.Windows.Forms.CheckBox();
			this.checkBoxBold = new System.Windows.Forms.CheckBox();
			this.fontComboBox = new ARCed.Controls.FontComboBox();
			this.groupBoxFont.SuspendLayout();
			this.panelSample.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.numericSize)).BeginInit();
			this.groupBoxStyle.SuspendLayout();
			this.SuspendLayout();
			// 
			// groupBoxFont
			// 
			this.groupBoxFont.Controls.Add(this.panelSample);
			this.groupBoxFont.Controls.Add(this.numericSize);
			this.groupBoxFont.Controls.Add(this.labelSize);
			this.groupBoxFont.Controls.Add(this.groupBoxStyle);
			this.groupBoxFont.Controls.Add(this.fontComboBox);
			this.groupBoxFont.Dock = System.Windows.Forms.DockStyle.Fill;
			this.groupBoxFont.Location = new System.Drawing.Point(0, 0);
			this.groupBoxFont.Name = "groupBoxFont";
			this.groupBoxFont.Size = new System.Drawing.Size(262, 141);
			this.groupBoxFont.TabIndex = 0;
			this.groupBoxFont.TabStop = false;
			this.groupBoxFont.Text = "Font";
			// 
			// panelSample
			// 
			this.panelSample.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.panelSample.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
			this.panelSample.Controls.Add(this.labelSample);
			this.panelSample.Location = new System.Drawing.Point(116, 90);
			this.panelSample.Name = "panelSample";
			this.panelSample.Size = new System.Drawing.Size(140, 44);
			this.panelSample.TabIndex = 4;
			// 
			// labelSample
			// 
			this.labelSample.Dock = System.Windows.Forms.DockStyle.Fill;
			this.labelSample.Location = new System.Drawing.Point(0, 0);
			this.labelSample.Name = "labelSample";
			this.labelSample.Size = new System.Drawing.Size(136, 40);
			this.labelSample.TabIndex = 0;
			this.labelSample.Text = "ABC abc 123";
			this.labelSample.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// numericSize
			// 
			this.numericSize.DecimalPlaces = 2;
			this.numericSize.Increment = new decimal(new int[] {
            25,
            0,
            0,
            131072});
			this.numericSize.Location = new System.Drawing.Point(116, 59);
			this.numericSize.Maximum = new decimal(new int[] {
            72,
            0,
            0,
            0});
			this.numericSize.Minimum = new decimal(new int[] {
            4,
            0,
            0,
            0});
			this.numericSize.Name = "numericSize";
			this.numericSize.Size = new System.Drawing.Size(58, 20);
			this.numericSize.TabIndex = 3;
			this.numericSize.Value = new decimal(new int[] {
            85,
            0,
            0,
            65536});
			this.numericSize.ValueChanged += new System.EventHandler(this.FontSetting_Changed);
			// 
			// labelSize
			// 
			this.labelSize.AutoSize = true;
			this.labelSize.Location = new System.Drawing.Point(113, 43);
			this.labelSize.Name = "labelSize";
			this.labelSize.Size = new System.Drawing.Size(30, 13);
			this.labelSize.TabIndex = 2;
			this.labelSize.Text = "Size:";
			this.labelSize.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
			// 
			// groupBoxStyle
			// 
			this.groupBoxStyle.Controls.Add(this.checkBoxUnderline);
			this.groupBoxStyle.Controls.Add(this.checkBoxItalic);
			this.groupBoxStyle.Controls.Add(this.checkBoxBold);
			this.groupBoxStyle.Location = new System.Drawing.Point(6, 46);
			this.groupBoxStyle.Name = "groupBoxStyle";
			this.groupBoxStyle.Size = new System.Drawing.Size(101, 88);
			this.groupBoxStyle.TabIndex = 1;
			this.groupBoxStyle.TabStop = false;
			this.groupBoxStyle.Text = "Style";
			// 
			// checkBoxUnderline
			// 
			this.checkBoxUnderline.AutoSize = true;
			this.checkBoxUnderline.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Underline, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.checkBoxUnderline.Location = new System.Drawing.Point(6, 65);
			this.checkBoxUnderline.Name = "checkBoxUnderline";
			this.checkBoxUnderline.Size = new System.Drawing.Size(71, 17);
			this.checkBoxUnderline.TabIndex = 2;
			this.checkBoxUnderline.Text = "Underline";
			this.checkBoxUnderline.UseVisualStyleBackColor = true;
			this.checkBoxUnderline.CheckedChanged += new System.EventHandler(this.FontSetting_Changed);
			// 
			// checkBoxItalic
			// 
			this.checkBoxItalic.AutoSize = true;
			this.checkBoxItalic.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.checkBoxItalic.Location = new System.Drawing.Point(6, 42);
			this.checkBoxItalic.Name = "checkBoxItalic";
			this.checkBoxItalic.Size = new System.Drawing.Size(48, 17);
			this.checkBoxItalic.TabIndex = 1;
			this.checkBoxItalic.Text = "Italic";
			this.checkBoxItalic.UseVisualStyleBackColor = true;
			this.checkBoxItalic.CheckedChanged += new System.EventHandler(this.FontSetting_Changed);
			// 
			// checkBoxBold
			// 
			this.checkBoxBold.AutoSize = true;
			this.checkBoxBold.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.checkBoxBold.Location = new System.Drawing.Point(6, 19);
			this.checkBoxBold.Name = "checkBoxBold";
			this.checkBoxBold.Size = new System.Drawing.Size(51, 17);
			this.checkBoxBold.TabIndex = 0;
			this.checkBoxBold.Text = "Bold";
			this.checkBoxBold.UseVisualStyleBackColor = true;
			this.checkBoxBold.CheckedChanged += new System.EventHandler(this.FontSetting_Changed);
			// 
			// fontComboBox
			// 
			this.fontComboBox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.fontComboBox.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawVariable;
			this.fontComboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.fontComboBox.FormattingEnabled = true;
			this.fontComboBox.IntegralHeight = false;
			this.fontComboBox.Location = new System.Drawing.Point(6, 19);
			this.fontComboBox.MaxDropDownItems = 20;
			this.fontComboBox.Name = "fontComboBox";
			this.fontComboBox.Size = new System.Drawing.Size(250, 21);
			this.fontComboBox.TabIndex = 0;
			this.fontComboBox.SelectedIndexChanged += new System.EventHandler(this.FontSetting_Changed);
			// 
			// FontSelector
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.Controls.Add(this.groupBoxFont);
			this.Name = "FontSelector";
			this.Size = new System.Drawing.Size(262, 141);
			this.groupBoxFont.ResumeLayout(false);
			this.groupBoxFont.PerformLayout();
			this.panelSample.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.numericSize)).EndInit();
			this.groupBoxStyle.ResumeLayout(false);
			this.groupBoxStyle.PerformLayout();
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.GroupBox groupBoxFont;
		private ARCed.Controls.FontComboBox fontComboBox;
		private System.Windows.Forms.Panel panelSample;
		private System.Windows.Forms.NumericUpDown numericSize;
		private System.Windows.Forms.Label labelSize;
		private System.Windows.Forms.GroupBox groupBoxStyle;
		private System.Windows.Forms.CheckBox checkBoxUnderline;
		private System.Windows.Forms.CheckBox checkBoxItalic;
		private System.Windows.Forms.CheckBox checkBoxBold;
		private System.Windows.Forms.Label labelSample;
	}
}
