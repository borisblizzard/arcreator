namespace ARCed.Database.MapEditor
{
	partial class MapEditorMainForm
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
			this.xnaPanel = new ARCed.Controls.MapEditorXnaPanel();
			this.panelXnaParent = new System.Windows.Forms.Panel();
			this.panelXnaParent.SuspendLayout();
			this.SuspendLayout();
			// 
			// xnaPanel
			// 
			this.xnaPanel.Location = new System.Drawing.Point(0, 0);
			this.xnaPanel.Map = null;
			this.xnaPanel.MapInfo = null;
			this.xnaPanel.Name = "xnaPanel";
			this.xnaPanel.Size = new System.Drawing.Size(226, 172);
			this.xnaPanel.TabIndex = 0;
			this.xnaPanel.Text = "MapEditor";
			// 
			// panelXnaParent
			// 
			this.panelXnaParent.AutoScroll = true;
			this.panelXnaParent.Controls.Add(this.xnaPanel);
			this.panelXnaParent.Dock = System.Windows.Forms.DockStyle.Fill;
			this.panelXnaParent.Location = new System.Drawing.Point(0, 0);
			this.panelXnaParent.Name = "panelXnaParent";
			this.panelXnaParent.Size = new System.Drawing.Size(690, 425);
			this.panelXnaParent.TabIndex = 1;
			// 
			// MapEditorMainForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(690, 425);
			this.Controls.Add(this.panelXnaParent);
			this.DefaultFloatSize = new System.Drawing.Size(800, 600);
			this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.Name = "MapEditorMainForm";
			this.ShowInTaskbar = false;
			this.Text = "Map Editor";
			this.Load += new System.EventHandler(this.MapEditorMainFormLoad);
			this.panelXnaParent.ResumeLayout(false);
			this.ResumeLayout(false);

		}

		#endregion

		private Controls.MapEditorXnaPanel xnaPanel;
		private System.Windows.Forms.Panel panelXnaParent;

	}
}