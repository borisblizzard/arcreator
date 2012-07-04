namespace ARCed.Database.MapEditor
{
	partial class MapTilesetForm
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
			System.Windows.Forms.TreeNode treeNode1 = new System.Windows.Forms.TreeNode("ARCed Project Name");
			this.splitContainer = new System.Windows.Forms.SplitContainer();
			this.treeViewMaps = new System.Windows.Forms.TreeView();
			((System.ComponentModel.ISupportInitialize)(this.splitContainer)).BeginInit();
			this.splitContainer.Panel2.SuspendLayout();
			this.splitContainer.SuspendLayout();
			this.SuspendLayout();
			// 
			// splitContainer
			// 
			this.splitContainer.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainer.Location = new System.Drawing.Point(0, 0);
			this.splitContainer.Name = "splitContainer";
			this.splitContainer.Orientation = System.Windows.Forms.Orientation.Horizontal;
			// 
			// splitContainer.Panel2
			// 
			this.splitContainer.Panel2.Controls.Add(this.treeViewMaps);
			this.splitContainer.Size = new System.Drawing.Size(264, 497);
			this.splitContainer.SplitterDistance = 326;
			this.splitContainer.TabIndex = 0;
			// 
			// treeViewMaps
			// 
			this.treeViewMaps.Dock = System.Windows.Forms.DockStyle.Fill;
			this.treeViewMaps.Location = new System.Drawing.Point(0, 0);
			this.treeViewMaps.Name = "treeViewMaps";
			treeNode1.Name = "NodeRoot";
			treeNode1.Text = "ARCed Project Name";
			this.treeViewMaps.Nodes.AddRange(new System.Windows.Forms.TreeNode[] {
            treeNode1});
			this.treeViewMaps.Size = new System.Drawing.Size(264, 167);
			this.treeViewMaps.TabIndex = 0;
			// 
			// MapTilesetForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(264, 497);
			this.Controls.Add(this.splitContainer);
			this.DefaultFloatSize = new System.Drawing.Size(256, 360);
			this.DockAreas = ((ARCed.UI.DockAreas)(((((ARCed.UI.DockAreas.Float | ARCed.UI.DockAreas.DockLeft)
						| ARCed.UI.DockAreas.DockRight)
						| ARCed.UI.DockAreas.DockTop)
						| ARCed.UI.DockAreas.DockBottom)));
			this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.SizableToolWindow;
			this.Name = "MapTilesetForm";
			this.ShowHint = ARCed.UI.DockState.DockLeft;
			this.Text = "MapTreeForm";
			this.splitContainer.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainer)).EndInit();
			this.splitContainer.ResumeLayout(false);
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.SplitContainer splitContainer;
		private System.Windows.Forms.TreeView treeViewMaps;
	}
}