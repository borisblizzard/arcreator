namespace ARCed.Forms.Splash
{
	partial class SplashScreenForm
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
			this.labelStatus = new System.Windows.Forms.Label();
			this.pictureBoxSplash = new System.Windows.Forms.PictureBox();
			((System.ComponentModel.ISupportInitialize)(this.pictureBoxSplash)).BeginInit();
			this.SuspendLayout();
			// 
			// labelStatus
			// 
			this.labelStatus.AutoSize = true;
			this.labelStatus.BackColor = System.Drawing.Color.Transparent;
			this.labelStatus.Font = new System.Drawing.Font("Tahoma", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.labelStatus.ForeColor = System.Drawing.Color.AntiqueWhite;
			this.labelStatus.Location = new System.Drawing.Point(270, 383);
			this.labelStatus.Name = "labelStatus";
			this.labelStatus.Size = new System.Drawing.Size(107, 19);
			this.labelStatus.TabIndex = 1;
			this.labelStatus.Text = "Status Update";
			// 
			// pictureBoxSplash
			// 
			this.pictureBoxSplash.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None;
			this.pictureBoxSplash.Cursor = System.Windows.Forms.Cursors.WaitCursor;
			this.pictureBoxSplash.Dock = System.Windows.Forms.DockStyle.Fill;
			this.pictureBoxSplash.Image = global::ARCed.Properties.Resources.ARCedSplash;
			this.pictureBoxSplash.InitialImage = global::ARCed.Properties.Resources.ARCedSplash;
			this.pictureBoxSplash.Location = new System.Drawing.Point(0, 0);
			this.pictureBoxSplash.Name = "pictureBoxSplash";
			this.pictureBoxSplash.Size = new System.Drawing.Size(640, 480);
			this.pictureBoxSplash.TabIndex = 2;
			this.pictureBoxSplash.TabStop = false;
			// 
			// SplashScreenForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.BackColor = System.Drawing.Color.Magenta;
			this.ClientSize = new System.Drawing.Size(640, 480);
			this.Controls.Add(this.labelStatus);
			this.Controls.Add(this.pictureBoxSplash);
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
			this.Name = "SplashScreenForm";
			this.ShowInTaskbar = false;
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
			this.Text = "SplashForm";
			this.TopMost = true;
			this.TransparencyKey = System.Drawing.Color.Magenta;
			this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.SplashForm_FormClosing);
			((System.ComponentModel.ISupportInitialize)(this.pictureBoxSplash)).EndInit();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Label labelStatus;
		private System.Windows.Forms.PictureBox pictureBoxSplash;
	}
}