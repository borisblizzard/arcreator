namespace ARCed.Database.Troops
{
	partial class BattleTestDialog
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
			this.labelActors = new System.Windows.Forms.Label();
			this.numericUpDownActors = new System.Windows.Forms.NumericUpDown();
			this.tabControlActors = new System.Windows.Forms.TabControl();
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownActors)).BeginInit();
			this.SuspendLayout();
			// 
			// buttonCancel
			// 
			this.buttonCancel.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
			this.buttonCancel.Location = new System.Drawing.Point(317, 268);
			this.buttonCancel.Name = "buttonCancel";
			this.buttonCancel.Size = new System.Drawing.Size(75, 23);
			this.buttonCancel.TabIndex = 0;
			this.buttonCancel.Text = "Cancel";
			this.buttonCancel.UseVisualStyleBackColor = true;
			// 
			// buttonOK
			// 
			this.buttonOK.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonOK.Location = new System.Drawing.Point(236, 268);
			this.buttonOK.Name = "buttonOK";
			this.buttonOK.Size = new System.Drawing.Size(75, 23);
			this.buttonOK.TabIndex = 1;
			this.buttonOK.Text = "OK";
			this.buttonOK.UseVisualStyleBackColor = true;
			// 
			// labelActors
			// 
			this.labelActors.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.labelActors.AutoSize = true;
			this.labelActors.Location = new System.Drawing.Point(12, 273);
			this.labelActors.Name = "labelActors";
			this.labelActors.Size = new System.Drawing.Size(40, 13);
			this.labelActors.TabIndex = 2;
			this.labelActors.Text = "Actors:";
			// 
			// numericUpDownActors
			// 
			this.numericUpDownActors.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.numericUpDownActors.Location = new System.Drawing.Point(58, 271);
			this.numericUpDownActors.Maximum = new decimal(new int[] {
            12,
            0,
            0,
            0});
			this.numericUpDownActors.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
			this.numericUpDownActors.Name = "numericUpDownActors";
			this.numericUpDownActors.Size = new System.Drawing.Size(43, 20);
			this.numericUpDownActors.TabIndex = 3;
			this.numericUpDownActors.Value = new decimal(new int[] {
            4,
            0,
            0,
            0});
			this.numericUpDownActors.ValueChanged += new System.EventHandler(this.NumericUpDownActorsValueChanged);
			// 
			// tabControlActors
			// 
			this.tabControlActors.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.tabControlActors.Location = new System.Drawing.Point(12, 12);
			this.tabControlActors.Name = "tabControlActors";
			this.tabControlActors.SelectedIndex = 0;
			this.tabControlActors.Size = new System.Drawing.Size(380, 250);
			this.tabControlActors.TabIndex = 4;
			// 
			// BattleTestDialog
			// 
			this.AcceptButton = this.buttonOK;
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.CancelButton = this.buttonCancel;
			this.ClientSize = new System.Drawing.Size(404, 303);
			this.Controls.Add(this.tabControlActors);
			this.Controls.Add(this.numericUpDownActors);
			this.Controls.Add(this.labelActors);
			this.Controls.Add(this.buttonOK);
			this.Controls.Add(this.buttonCancel);
			this.MaximizeBox = false;
			this.MinimizeBox = false;
			this.Name = "BattleTestDialog";
			this.ShowIcon = false;
			this.ShowInTaskbar = false;
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
			this.Text = "BattleTestDialog";
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownActors)).EndInit();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Button buttonCancel;
		private System.Windows.Forms.Button buttonOK;
		private System.Windows.Forms.Label labelActors;
		private System.Windows.Forms.NumericUpDown numericUpDownActors;
		private System.Windows.Forms.TabControl tabControlActors;
	}
}