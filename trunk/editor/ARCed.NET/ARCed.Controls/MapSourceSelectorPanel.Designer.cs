﻿namespace ARCed.Controls
{
	sealed partial class MapSourceSelectorPanel
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
			((System.ComponentModel.ISupportInitialize)(this)).BeginInit();
			this.SuspendLayout();
			// 
			// MapSourceSelectorPanel
			// 
			this.MinimumSize = new System.Drawing.Size(256, 32);
			this.Size = new System.Drawing.Size(279, 426);
			this.MouseDown += new System.Windows.Forms.MouseEventHandler(this.PictureBoxTilesetMouseDown);
			this.MouseMove += new System.Windows.Forms.MouseEventHandler(this.PictureBoxTilesetMouseMove);
			this.MouseUp += new System.Windows.Forms.MouseEventHandler(this.PictureBoxTilesetMouseUp);
			((System.ComponentModel.ISupportInitialize)(this)).EndInit();
			this.ResumeLayout(false);

		}

		#endregion

	}
}
