namespace ARCed.Database.Actors
{
	partial class ParamGenerateCurveDialog
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
			this.labelInitial = new System.Windows.Forms.Label();
			this.numericInitial = new System.Windows.Forms.NumericUpDown();
			this.numericFinal = new System.Windows.Forms.NumericUpDown();
			this.labelFinal = new System.Windows.Forms.Label();
			this.trackBarSpeed = new System.Windows.Forms.TrackBar();
			this.label2 = new System.Windows.Forms.Label();
			this.label3 = new System.Windows.Forms.Label();
			this.label1 = new System.Windows.Forms.Label();
			((System.ComponentModel.ISupportInitialize)(this.numericInitial)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.numericFinal)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.trackBarSpeed)).BeginInit();
			this.SuspendLayout();
			// 
			// buttonCancel
			// 
			this.buttonCancel.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
			this.buttonCancel.Location = new System.Drawing.Point(163, 41);
			this.buttonCancel.Name = "buttonCancel";
			this.buttonCancel.Size = new System.Drawing.Size(75, 23);
			this.buttonCancel.TabIndex = 0;
			this.buttonCancel.Text = "Cancel";
			this.buttonCancel.UseVisualStyleBackColor = true;
			// 
			// buttonOK
			// 
			this.buttonOK.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonOK.Location = new System.Drawing.Point(163, 12);
			this.buttonOK.Name = "buttonOK";
			this.buttonOK.Size = new System.Drawing.Size(75, 23);
			this.buttonOK.TabIndex = 1;
			this.buttonOK.Text = "OK";
			this.buttonOK.UseVisualStyleBackColor = true;
			this.buttonOK.Click += new System.EventHandler(this.ButtonOkClick);
			// 
			// labelInitial
			// 
			this.labelInitial.AutoSize = true;
			this.labelInitial.Location = new System.Drawing.Point(12, 9);
			this.labelInitial.Name = "labelInitial";
			this.labelInitial.Size = new System.Drawing.Size(63, 13);
			this.labelInitial.TabIndex = 2;
			this.labelInitial.Text = "Initial Level:";
			// 
			// numericInitial
			// 
			this.numericInitial.Location = new System.Drawing.Point(15, 25);
			this.numericInitial.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
			this.numericInitial.Name = "numericInitial";
			this.numericInitial.Size = new System.Drawing.Size(66, 20);
			this.numericInitial.TabIndex = 3;
			this.numericInitial.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
			this.numericInitial.ValueChanged += new System.EventHandler(this.NumericValueChanged);
			// 
			// numericFinal
			// 
			this.numericFinal.Location = new System.Drawing.Point(87, 25);
			this.numericFinal.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
			this.numericFinal.Name = "numericFinal";
			this.numericFinal.Size = new System.Drawing.Size(66, 20);
			this.numericFinal.TabIndex = 4;
			this.numericFinal.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
			this.numericFinal.ValueChanged += new System.EventHandler(this.NumericValueChanged);
			// 
			// labelFinal
			// 
			this.labelFinal.AutoSize = true;
			this.labelFinal.Location = new System.Drawing.Point(84, 9);
			this.labelFinal.Name = "labelFinal";
			this.labelFinal.Size = new System.Drawing.Size(61, 13);
			this.labelFinal.TabIndex = 5;
			this.labelFinal.Text = "Final Level:";
			// 
			// trackBarSpeed
			// 
			this.trackBarSpeed.Location = new System.Drawing.Point(12, 51);
			this.trackBarSpeed.Minimum = -10;
			this.trackBarSpeed.Name = "trackBarSpeed";
			this.trackBarSpeed.Size = new System.Drawing.Size(141, 45);
			this.trackBarSpeed.TabIndex = 6;
			this.trackBarSpeed.TickFrequency = 10;
			// 
			// label2
			// 
			this.label2.AutoSize = true;
			this.label2.Location = new System.Drawing.Point(126, 84);
			this.label2.Name = "label2";
			this.label2.Size = new System.Drawing.Size(27, 13);
			this.label2.TabIndex = 8;
			this.label2.Text = "Fast";
			// 
			// label3
			// 
			this.label3.AutoSize = true;
			this.label3.Location = new System.Drawing.Point(12, 83);
			this.label3.Name = "label3";
			this.label3.Size = new System.Drawing.Size(30, 13);
			this.label3.TabIndex = 9;
			this.label3.Text = "Slow";
			// 
			// label1
			// 
			this.label1.AutoSize = true;
			this.label1.Location = new System.Drawing.Point(64, 83);
			this.label1.Name = "label1";
			this.label1.Size = new System.Drawing.Size(38, 13);
			this.label1.TabIndex = 10;
			this.label1.Text = "Middle";
			// 
			// ParamGenerateCurveDialog
			// 
			this.AcceptButton = this.buttonOK;
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.CancelButton = this.buttonCancel;
			this.ClientSize = new System.Drawing.Size(250, 106);
			this.Controls.Add(this.label1);
			this.Controls.Add(this.label3);
			this.Controls.Add(this.label2);
			this.Controls.Add(this.trackBarSpeed);
			this.Controls.Add(this.labelFinal);
			this.Controls.Add(this.numericFinal);
			this.Controls.Add(this.numericInitial);
			this.Controls.Add(this.labelInitial);
			this.Controls.Add(this.buttonOK);
			this.Controls.Add(this.buttonCancel);
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
			this.MaximizeBox = false;
			this.MinimizeBox = false;
			this.Name = "ParamGenerateCurveDialog";
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
			this.Text = "Generate Curve";
			((System.ComponentModel.ISupportInitialize)(this.numericInitial)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.numericFinal)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.trackBarSpeed)).EndInit();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Button buttonCancel;
		private System.Windows.Forms.Button buttonOK;
		private System.Windows.Forms.Label labelInitial;
		private System.Windows.Forms.NumericUpDown numericInitial;
		private System.Windows.Forms.NumericUpDown numericFinal;
		private System.Windows.Forms.Label labelFinal;
		private System.Windows.Forms.TrackBar trackBarSpeed;
		private System.Windows.Forms.Label label2;
		private System.Windows.Forms.Label label3;
		private System.Windows.Forms.Label label1;
	}
}