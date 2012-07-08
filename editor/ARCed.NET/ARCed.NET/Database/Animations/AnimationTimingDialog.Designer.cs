namespace ARCed.Database.Animations
{
	partial class AnimationTimingDialog
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
			this.buttonCancel = new System.Windows.Forms.Button();
			this.buttonOK = new System.Windows.Forms.Button();
			this.labelFrame = new System.Windows.Forms.Label();
			this.labelSE = new System.Windows.Forms.Label();
			this.numericUpDownFrame = new System.Windows.Forms.NumericUpDown();
			this.labelCondition = new System.Windows.Forms.Label();
			this.comboBoxCondition = new System.Windows.Forms.ComboBox();
			this.textBoxSE = new ARCed.Controls.TextBoxButton();
			this.groupBoxFlash = new System.Windows.Forms.GroupBox();
			this.trackBarStrength = new System.Windows.Forms.TrackBar();
			this.numericUpDownStrength = new System.Windows.Forms.NumericUpDown();
			this.labelStrength = new System.Windows.Forms.Label();
			this.numericUpDownDuration = new System.Windows.Forms.NumericUpDown();
			this.labelDuration = new System.Windows.Forms.Label();
			this.labelColor = new System.Windows.Forms.Label();
			this.radioHide = new System.Windows.Forms.RadioButton();
			this.radioScreen = new System.Windows.Forms.RadioButton();
			this.radioTarget = new System.Windows.Forms.RadioButton();
			this.radioNone = new System.Windows.Forms.RadioButton();
			this.panelColor = new System.Windows.Forms.Panel();
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownFrame)).BeginInit();
			this.groupBoxFlash.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.trackBarStrength)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownStrength)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownDuration)).BeginInit();
			this.SuspendLayout();
			// 
			// buttonCancel
			// 
			this.buttonCancel.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
			this.buttonCancel.Location = new System.Drawing.Point(133, 281);
			this.buttonCancel.Name = "buttonCancel";
			this.buttonCancel.Size = new System.Drawing.Size(75, 23);
			this.buttonCancel.TabIndex = 0;
			this.buttonCancel.Text = "Cancel";
			this.buttonCancel.UseVisualStyleBackColor = true;
			// 
			// buttonOK
			// 
			this.buttonOK.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonOK.Location = new System.Drawing.Point(52, 281);
			this.buttonOK.Name = "buttonOK";
			this.buttonOK.Size = new System.Drawing.Size(75, 23);
			this.buttonOK.TabIndex = 1;
			this.buttonOK.Text = "OK";
			this.buttonOK.UseVisualStyleBackColor = true;
			this.buttonOK.Click += new System.EventHandler(this.buttonOK_Click);
			// 
			// labelFrame
			// 
			this.labelFrame.AutoSize = true;
			this.labelFrame.Location = new System.Drawing.Point(12, 9);
			this.labelFrame.Name = "labelFrame";
			this.labelFrame.Size = new System.Drawing.Size(39, 13);
			this.labelFrame.TabIndex = 2;
			this.labelFrame.Text = "Frame:";
			// 
			// labelSE
			// 
			this.labelSE.AutoSize = true;
			this.labelSE.Location = new System.Drawing.Point(12, 57);
			this.labelSE.Name = "labelSE";
			this.labelSE.Size = new System.Drawing.Size(24, 13);
			this.labelSE.TabIndex = 3;
			this.labelSE.Text = "SE:";
			// 
			// numericUpDownFrame
			// 
			this.numericUpDownFrame.Location = new System.Drawing.Point(15, 25);
			this.numericUpDownFrame.Maximum = new decimal(new int[] {
            999,
            0,
            0,
            0});
			this.numericUpDownFrame.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
			this.numericUpDownFrame.Name = "numericUpDownFrame";
			this.numericUpDownFrame.Size = new System.Drawing.Size(69, 20);
			this.numericUpDownFrame.TabIndex = 4;
			this.numericUpDownFrame.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
			// 
			// labelCondition
			// 
			this.labelCondition.AutoSize = true;
			this.labelCondition.Location = new System.Drawing.Point(100, 9);
			this.labelCondition.Name = "labelCondition";
			this.labelCondition.Size = new System.Drawing.Size(54, 13);
			this.labelCondition.TabIndex = 5;
			this.labelCondition.Text = "Condition:";
			// 
			// comboBoxCondition
			// 
			this.comboBoxCondition.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxCondition.FormattingEnabled = true;
			this.comboBoxCondition.Items.AddRange(new object[] {
            "None",
            "Hit",
            "Miss"});
			this.comboBoxCondition.Location = new System.Drawing.Point(103, 25);
			this.comboBoxCondition.Name = "comboBoxCondition";
			this.comboBoxCondition.Size = new System.Drawing.Size(86, 21);
			this.comboBoxCondition.TabIndex = 6;
			// 
			// textBoxSE
			// 
			this.textBoxSE.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBoxSE.Location = new System.Drawing.Point(15, 73);
			this.textBoxSE.MaximumSize = new System.Drawing.Size(1800, 20);
			this.textBoxSE.Name = "textBoxSE";
			this.textBoxSE.Size = new System.Drawing.Size(193, 20);
			this.textBoxSE.TabIndex = 7;
			// 
			// groupBoxFlash
			// 
			this.groupBoxFlash.Controls.Add(this.trackBarStrength);
			this.groupBoxFlash.Controls.Add(this.numericUpDownStrength);
			this.groupBoxFlash.Controls.Add(this.labelStrength);
			this.groupBoxFlash.Controls.Add(this.numericUpDownDuration);
			this.groupBoxFlash.Controls.Add(this.labelDuration);
			this.groupBoxFlash.Controls.Add(this.labelColor);
			this.groupBoxFlash.Controls.Add(this.radioHide);
			this.groupBoxFlash.Controls.Add(this.radioScreen);
			this.groupBoxFlash.Controls.Add(this.radioTarget);
			this.groupBoxFlash.Controls.Add(this.radioNone);
			this.groupBoxFlash.Controls.Add(this.panelColor);
			this.groupBoxFlash.Location = new System.Drawing.Point(15, 99);
			this.groupBoxFlash.Name = "groupBoxFlash";
			this.groupBoxFlash.Size = new System.Drawing.Size(193, 176);
			this.groupBoxFlash.TabIndex = 8;
			this.groupBoxFlash.TabStop = false;
			this.groupBoxFlash.Text = "Flash";
			// 
			// trackBarStrength
			// 
			this.trackBarStrength.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.trackBarStrength.AutoSize = false;
			this.trackBarStrength.Location = new System.Drawing.Point(8, 136);
			this.trackBarStrength.Maximum = 255;
			this.trackBarStrength.Name = "trackBarStrength";
			this.trackBarStrength.Size = new System.Drawing.Size(131, 34);
			this.trackBarStrength.TabIndex = 10;
			this.trackBarStrength.TickFrequency = 16;
			// 
			// numericUpDownStrength
			// 
			this.numericUpDownStrength.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.numericUpDownStrength.Location = new System.Drawing.Point(147, 136);
			this.numericUpDownStrength.Maximum = new decimal(new int[] {
            255,
            0,
            0,
            0});
			this.numericUpDownStrength.Name = "numericUpDownStrength";
			this.numericUpDownStrength.Size = new System.Drawing.Size(40, 20);
			this.numericUpDownStrength.TabIndex = 9;
			// 
			// labelStrength
			// 
			this.labelStrength.AutoSize = true;
			this.labelStrength.Location = new System.Drawing.Point(6, 120);
			this.labelStrength.Name = "labelStrength";
			this.labelStrength.Size = new System.Drawing.Size(50, 13);
			this.labelStrength.TabIndex = 8;
			this.labelStrength.Text = "Strength:";
			// 
			// numericUpDownDuration
			// 
			this.numericUpDownDuration.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.numericUpDownDuration.Location = new System.Drawing.Point(106, 88);
			this.numericUpDownDuration.Maximum = new decimal(new int[] {
            999,
            0,
            0,
            0});
			this.numericUpDownDuration.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
			this.numericUpDownDuration.Name = "numericUpDownDuration";
			this.numericUpDownDuration.Size = new System.Drawing.Size(63, 20);
			this.numericUpDownDuration.TabIndex = 7;
			this.numericUpDownDuration.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
			// 
			// labelDuration
			// 
			this.labelDuration.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.labelDuration.AutoSize = true;
			this.labelDuration.Location = new System.Drawing.Point(103, 72);
			this.labelDuration.Name = "labelDuration";
			this.labelDuration.Size = new System.Drawing.Size(50, 13);
			this.labelDuration.TabIndex = 6;
			this.labelDuration.Text = "Duration:";
			// 
			// labelColor
			// 
			this.labelColor.AutoSize = true;
			this.labelColor.Location = new System.Drawing.Point(6, 72);
			this.labelColor.Name = "labelColor";
			this.labelColor.Size = new System.Drawing.Size(34, 13);
			this.labelColor.TabIndex = 5;
			this.labelColor.Text = "Color:";
			// 
			// radioHide
			// 
			this.radioHide.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.radioHide.AutoSize = true;
			this.radioHide.Location = new System.Drawing.Point(106, 42);
			this.radioHide.Name = "radioHide";
			this.radioHide.Size = new System.Drawing.Size(81, 17);
			this.radioHide.TabIndex = 4;
			this.radioHide.Text = "Hide Target";
			this.radioHide.UseVisualStyleBackColor = true;
			// 
			// radioScreen
			// 
			this.radioScreen.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.radioScreen.AutoSize = true;
			this.radioScreen.Location = new System.Drawing.Point(106, 19);
			this.radioScreen.Name = "radioScreen";
			this.radioScreen.Size = new System.Drawing.Size(59, 17);
			this.radioScreen.TabIndex = 3;
			this.radioScreen.Text = "Screen";
			this.radioScreen.UseVisualStyleBackColor = true;
			// 
			// radioTarget
			// 
			this.radioTarget.AutoSize = true;
			this.radioTarget.Location = new System.Drawing.Point(8, 42);
			this.radioTarget.Name = "radioTarget";
			this.radioTarget.Size = new System.Drawing.Size(56, 17);
			this.radioTarget.TabIndex = 2;
			this.radioTarget.Text = "Target";
			this.radioTarget.UseVisualStyleBackColor = true;
			// 
			// radioNone
			// 
			this.radioNone.AutoSize = true;
			this.radioNone.Checked = true;
			this.radioNone.Location = new System.Drawing.Point(8, 19);
			this.radioNone.Name = "radioNone";
			this.radioNone.Size = new System.Drawing.Size(51, 17);
			this.radioNone.TabIndex = 1;
			this.radioNone.TabStop = true;
			this.radioNone.Text = "None";
			this.radioNone.UseVisualStyleBackColor = true;
			// 
			// panelColor
			// 
			this.panelColor.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
			this.panelColor.Location = new System.Drawing.Point(9, 88);
			this.panelColor.Name = "panelColor";
			this.panelColor.Size = new System.Drawing.Size(63, 20);
			this.panelColor.TabIndex = 0;
			this.panelColor.DoubleClick += new System.EventHandler(this.panelColor_DoubleClick);
			// 
			// AnimationTimingDialog
			// 
			this.AcceptButton = this.buttonOK;
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.CancelButton = this.buttonCancel;
			this.ClientSize = new System.Drawing.Size(220, 316);
			this.Controls.Add(this.groupBoxFlash);
			this.Controls.Add(this.textBoxSE);
			this.Controls.Add(this.comboBoxCondition);
			this.Controls.Add(this.labelCondition);
			this.Controls.Add(this.numericUpDownFrame);
			this.Controls.Add(this.labelSE);
			this.Controls.Add(this.labelFrame);
			this.Controls.Add(this.buttonOK);
			this.Controls.Add(this.buttonCancel);
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
			this.Name = "AnimationTimingDialog";
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
			this.Text = "SE and Flash Timing";
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownFrame)).EndInit();
			this.groupBoxFlash.ResumeLayout(false);
			this.groupBoxFlash.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.trackBarStrength)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownStrength)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownDuration)).EndInit();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Button buttonCancel;
		private System.Windows.Forms.Button buttonOK;
		private System.Windows.Forms.Label labelFrame;
		private System.Windows.Forms.Label labelSE;
		private System.Windows.Forms.NumericUpDown numericUpDownFrame;
		private System.Windows.Forms.Label labelCondition;
		private System.Windows.Forms.ComboBox comboBoxCondition;
		private Controls.TextBoxButton textBoxSE;
		private System.Windows.Forms.GroupBox groupBoxFlash;
		private System.Windows.Forms.NumericUpDown numericUpDownDuration;
		private System.Windows.Forms.Label labelDuration;
		private System.Windows.Forms.Label labelColor;
		private System.Windows.Forms.RadioButton radioHide;
		private System.Windows.Forms.RadioButton radioScreen;
		private System.Windows.Forms.RadioButton radioTarget;
		private System.Windows.Forms.RadioButton radioNone;
		private System.Windows.Forms.Panel panelColor;
		private System.Windows.Forms.TrackBar trackBarStrength;
		private System.Windows.Forms.NumericUpDown numericUpDownStrength;
		private System.Windows.Forms.Label labelStrength;
	}
}