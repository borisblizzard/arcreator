namespace ARCed.Controls
{
	partial class ParamBox
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
			this.labelParameter = new System.Windows.Forms.Label();
			this.numericParameter = new System.Windows.Forms.NumericUpDown();
			((System.ComponentModel.ISupportInitialize)(this.numericParameter)).BeginInit();
			this.SuspendLayout();
			// 
			// labelParameter
			// 
			this.labelParameter.AutoSize = true;
			this.labelParameter.Location = new System.Drawing.Point(-3, 0);
			this.labelParameter.Name = "labelParameter";
			this.labelParameter.Size = new System.Drawing.Size(29, 13);
			this.labelParameter.TabIndex = 0;
			this.labelParameter.Text = "label";
			// 
			// numericParameter
			// 
			this.numericParameter.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.numericParameter.Location = new System.Drawing.Point(0, 16);
			this.numericParameter.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
			this.numericParameter.Name = "numericParameter";
			this.numericParameter.Size = new System.Drawing.Size(67, 20);
			this.numericParameter.TabIndex = 1;
			this.numericParameter.ValueChanged += new System.EventHandler(this.numericParameter_ValueChanged);
			// 
			// ParamBox
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.Controls.Add(this.numericParameter);
			this.Controls.Add(this.labelParameter);
			this.Name = "ParamBox";
			this.Size = new System.Drawing.Size(67, 37);
			((System.ComponentModel.ISupportInitialize)(this.numericParameter)).EndInit();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Label labelParameter;
		private System.Windows.Forms.NumericUpDown numericParameter;
	}
}
