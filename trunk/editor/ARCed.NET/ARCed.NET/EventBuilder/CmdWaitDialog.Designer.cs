namespace ARCed.EventBuilder
{
	partial class CmdWaitDialog
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
			this.labelTime = new System.Windows.Forms.Label();
			this.numericUpDownFrames = new System.Windows.Forms.NumericUpDown();
			this.labelFames = new System.Windows.Forms.Label();
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownFrames)).BeginInit();
			this.SuspendLayout();
			// 
			// buttonCancel
			// 
			this.buttonCancel.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
			this.buttonCancel.Location = new System.Drawing.Point(96, 53);
			this.buttonCancel.Name = "buttonCancel";
			this.buttonCancel.Size = new System.Drawing.Size(75, 23);
			this.buttonCancel.TabIndex = 0;
			this.buttonCancel.Text = "Cancel";
			this.buttonCancel.UseVisualStyleBackColor = true;
			// 
			// buttonOK
			// 
			this.buttonOK.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonOK.Location = new System.Drawing.Point(15, 53);
			this.buttonOK.Name = "buttonOK";
			this.buttonOK.Size = new System.Drawing.Size(75, 23);
			this.buttonOK.TabIndex = 1;
			this.buttonOK.Text = "OK";
			this.buttonOK.UseVisualStyleBackColor = true;
			this.buttonOK.Click += new System.EventHandler(this.buttonOK_Click);
			// 
			// labelTime
			// 
			this.labelTime.AutoSize = true;
			this.labelTime.Location = new System.Drawing.Point(12, 9);
			this.labelTime.Name = "labelTime";
			this.labelTime.Size = new System.Drawing.Size(33, 13);
			this.labelTime.TabIndex = 2;
			this.labelTime.Text = "Time:";
			// 
			// numericUpDownFrames
			// 
			this.numericUpDownFrames.Location = new System.Drawing.Point(15, 25);
			this.numericUpDownFrames.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
			this.numericUpDownFrames.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
			this.numericUpDownFrames.Name = "numericUpDown1";
			this.numericUpDownFrames.Size = new System.Drawing.Size(62, 20);
			this.numericUpDownFrames.TabIndex = 3;
			this.numericUpDownFrames.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
			// 
			// labelFames
			// 
			this.labelFames.AutoSize = true;
			this.labelFames.Location = new System.Drawing.Point(83, 27);
			this.labelFames.Name = "labelFames";
			this.labelFames.Size = new System.Drawing.Size(41, 13);
			this.labelFames.TabIndex = 4;
			this.labelFames.Text = "Frames";
			// 
			// CmdWaitDialog
			// 
			this.AcceptButton = this.buttonOK;
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.CancelButton = this.buttonCancel;
			this.ClientSize = new System.Drawing.Size(183, 88);
			this.Controls.Add(this.labelFames);
			this.Controls.Add(this.numericUpDownFrames);
			this.Controls.Add(this.labelTime);
			this.Controls.Add(this.buttonOK);
			this.Controls.Add(this.buttonCancel);
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
			this.Name = "CmdWaitDialog";
			this.ShowIcon = false;
			this.ShowInTaskbar = false;
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
			this.Text = "Wait";
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownFrames)).EndInit();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Button buttonCancel;
		private System.Windows.Forms.Button buttonOK;
		private System.Windows.Forms.Label labelTime;
		private System.Windows.Forms.NumericUpDown numericUpDownFrames;
		private System.Windows.Forms.Label labelFames;
	}
}