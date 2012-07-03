namespace ARCed.Controls
{
	partial class TextBoxButton
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
			this.components = new System.ComponentModel.Container();
			this.toolTip = new System.Windows.Forms.ToolTip(this.components);
			this.textBox = new System.Windows.Forms.Label();
			this.button = new System.Windows.Forms.Button();
			this.SuspendLayout();
			// 
			// textBox
			// 
			this.textBox.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBox.BackColor = System.Drawing.SystemColors.Window;
			this.textBox.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
			this.textBox.Location = new System.Drawing.Point(0, 0);
			this.textBox.Margin = new System.Windows.Forms.Padding(0);
			this.textBox.Name = "textBox";
			this.textBox.Size = new System.Drawing.Size(198, 20);
			this.textBox.TabIndex = 1;
			this.textBox.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
			this.textBox.TextChanged += new System.EventHandler(this.textBox_TextChanged);
			// 
			// button
			// 
			this.button.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.button.BackColor = System.Drawing.SystemColors.Control;
			this.button.Font = new System.Drawing.Font("Microsoft Sans Serif", 8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Pixel, ((byte)(0)));
			this.button.Location = new System.Drawing.Point(174, 1);
			this.button.Margin = new System.Windows.Forms.Padding(1);
			this.button.Name = "button";
			this.button.Size = new System.Drawing.Size(24, 18);
			this.button.TabIndex = 2;
			this.button.Text = "...";
			this.button.TextAlign = System.Drawing.ContentAlignment.TopCenter;
			this.toolTip.SetToolTip(this.button, "Edit");
			this.button.UseVisualStyleBackColor = false;
			this.button.Click += new System.EventHandler(this.button_Click);
			// 
			// TextBoxButton
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.Controls.Add(this.button);
			this.Controls.Add(this.textBox);
			this.MaximumSize = new System.Drawing.Size(1800, 20);
			this.Name = "TextBoxButton";
			this.Size = new System.Drawing.Size(198, 20);
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.ToolTip toolTip;
		private System.Windows.Forms.Label textBox;
		private System.Windows.Forms.Button button;
	}
}
