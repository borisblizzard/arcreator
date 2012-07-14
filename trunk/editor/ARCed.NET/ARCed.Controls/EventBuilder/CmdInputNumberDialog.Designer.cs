namespace ARCed.EventBuilder
{
	partial class CmdInputNumberDialog
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
			this.Cancel = new System.Windows.Forms.Button();
			this.OK = new System.Windows.Forms.Button();
			this.label1 = new System.Windows.Forms.Label();
			this.comboBoxVariable = new System.Windows.Forms.ComboBox();
			this.labelDigits = new System.Windows.Forms.Label();
			this.numericUpDownDigits = new System.Windows.Forms.NumericUpDown();
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownDigits)).BeginInit();
			this.SuspendLayout();
			// 
			// Cancel
			// 
			this.Cancel.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.Cancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
			this.Cancel.Location = new System.Drawing.Point(183, 73);
			this.Cancel.Name = "Cancel";
			this.Cancel.Size = new System.Drawing.Size(75, 23);
			this.Cancel.TabIndex = 0;
			this.Cancel.Text = "Cancel";
			this.Cancel.UseVisualStyleBackColor = true;
			// 
			// OK
			// 
			this.OK.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.OK.Location = new System.Drawing.Point(102, 73);
			this.OK.Name = "OK";
			this.OK.Size = new System.Drawing.Size(75, 23);
			this.OK.TabIndex = 1;
			this.OK.Text = "OK";
			this.OK.UseVisualStyleBackColor = true;
			this.OK.Click += new System.EventHandler(this.OK_Click);
			// 
			// label1
			// 
			this.label1.AutoSize = true;
			this.label1.Location = new System.Drawing.Point(12, 9);
			this.label1.Name = "label1";
			this.label1.Size = new System.Drawing.Size(103, 13);
			this.label1.TabIndex = 2;
			this.label1.Text = "Variable for Number:";
			// 
			// comboBoxVariable
			// 
			this.comboBoxVariable.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxVariable.FormattingEnabled = true;
			this.comboBoxVariable.Location = new System.Drawing.Point(15, 25);
			this.comboBoxVariable.Name = "comboBox1";
			this.comboBoxVariable.Size = new System.Drawing.Size(243, 21);
			this.comboBoxVariable.TabIndex = 3;
			// 
			// labelDigits
			// 
			this.labelDigits.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.labelDigits.AutoSize = true;
			this.labelDigits.Location = new System.Drawing.Point(12, 57);
			this.labelDigits.Name = "labelDigits";
			this.labelDigits.Size = new System.Drawing.Size(36, 13);
			this.labelDigits.TabIndex = 4;
			this.labelDigits.Text = "Digits:";
			// 
			// numericUpDownDigits
			// 
			this.numericUpDownDigits.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.numericUpDownDigits.Location = new System.Drawing.Point(15, 73);
			this.numericUpDownDigits.Maximum = new decimal(new int[] {
            12,
            0,
            0,
            0});
			this.numericUpDownDigits.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
			this.numericUpDownDigits.Name = "numericUpDown1";
			this.numericUpDownDigits.Size = new System.Drawing.Size(57, 20);
			this.numericUpDownDigits.TabIndex = 5;
			this.numericUpDownDigits.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
			// 
			// CmdInputNumberDialog
			// 
			this.AcceptButton = this.OK;
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.CancelButton = this.Cancel;
			this.ClientSize = new System.Drawing.Size(270, 108);
			this.Controls.Add(this.numericUpDownDigits);
			this.Controls.Add(this.labelDigits);
			this.Controls.Add(this.comboBoxVariable);
			this.Controls.Add(this.label1);
			this.Controls.Add(this.OK);
			this.Controls.Add(this.Cancel);
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
			this.Name = "CmdInputNumberDialog";
			this.ShowIcon = false;
			this.ShowInTaskbar = false;
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
			this.Text = "Input Number";
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownDigits)).EndInit();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Button Cancel;
		private System.Windows.Forms.Button OK;
		private System.Windows.Forms.Label label1;
		private System.Windows.Forms.ComboBox comboBoxVariable;
		private System.Windows.Forms.Label labelDigits;
		private System.Windows.Forms.NumericUpDown numericUpDownDigits;
	}
}