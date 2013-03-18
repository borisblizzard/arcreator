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
			this.components = new System.ComponentModel.Container();
			System.Windows.Forms.TreeNode treeNode2 = new System.Windows.Forms.TreeNode("Node0");
			System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MapEditorMainForm));
			this.panelXnaParent = new System.Windows.Forms.Panel();
			this.panel1 = new System.Windows.Forms.Panel();
			this.toolStrip = new System.Windows.Forms.ToolStrip();
			this.splitContainerControls = new System.Windows.Forms.SplitContainer();
			this.treeViewMaps = new System.Windows.Forms.TreeView();
			this.imageList = new System.Windows.Forms.ImageList(this.components);
			this.mapEditorXnaPanel = new ARCed.Controls.MapEditorXnaPanel();
			this.tilesetSelectionPanel = new ARCed.Controls.MapSourceSelectorPanel();
			this.panelXnaParent.SuspendLayout();
			this.panel1.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerControls)).BeginInit();
			this.splitContainerControls.Panel1.SuspendLayout();
			this.splitContainerControls.Panel2.SuspendLayout();
			this.splitContainerControls.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.tilesetSelectionPanel)).BeginInit();
			this.SuspendLayout();
			// 
			// panelXnaParent
			// 
			this.panelXnaParent.AutoScroll = true;
			this.panelXnaParent.Controls.Add(this.panel1);
			this.panelXnaParent.Controls.Add(this.splitContainerControls);
			this.panelXnaParent.Dock = System.Windows.Forms.DockStyle.Fill;
			this.panelXnaParent.Location = new System.Drawing.Point(0, 0);
			this.panelXnaParent.Name = "panelXnaParent";
			this.panelXnaParent.Size = new System.Drawing.Size(782, 425);
			this.panelXnaParent.TabIndex = 1;
			// 
			// panel1
			// 
			this.panel1.AutoScroll = true;
			this.panel1.BackColor = System.Drawing.SystemColors.AppWorkspace;
			this.panel1.Controls.Add(this.mapEditorXnaPanel);
			this.panel1.Controls.Add(this.toolStrip);
			this.panel1.Dock = System.Windows.Forms.DockStyle.Fill;
			this.panel1.Location = new System.Drawing.Point(273, 0);
			this.panel1.Name = "panel1";
			this.panel1.Size = new System.Drawing.Size(509, 425);
			this.panel1.TabIndex = 3;
			// 
			// toolStrip
			// 
			this.toolStrip.Location = new System.Drawing.Point(0, 0);
			this.toolStrip.Name = "toolStrip";
			this.toolStrip.Size = new System.Drawing.Size(509, 25);
			this.toolStrip.TabIndex = 3;
			this.toolStrip.Text = "toolStrip1";
			// 
			// splitContainerControls
			// 
			this.splitContainerControls.Dock = System.Windows.Forms.DockStyle.Left;
			this.splitContainerControls.Location = new System.Drawing.Point(0, 0);
			this.splitContainerControls.Name = "splitContainerControls";
			this.splitContainerControls.Orientation = System.Windows.Forms.Orientation.Horizontal;
			// 
			// splitContainerControls.Panel1
			// 
			this.splitContainerControls.Panel1.AutoScroll = true;
			this.splitContainerControls.Panel1.Controls.Add(this.tilesetSelectionPanel);
			// 
			// splitContainerControls.Panel2
			// 
			this.splitContainerControls.Panel2.Controls.Add(this.treeViewMaps);
			this.splitContainerControls.Size = new System.Drawing.Size(273, 425);
			this.splitContainerControls.SplitterDistance = 250;
			this.splitContainerControls.TabIndex = 0;
			// 
			// treeViewMaps
			// 
			this.treeViewMaps.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
			this.treeViewMaps.FullRowSelect = true;
			this.treeViewMaps.ImageIndex = 0;
			this.treeViewMaps.ImageList = this.imageList;
			this.treeViewMaps.Location = new System.Drawing.Point(3, 3);
			this.treeViewMaps.Name = "treeViewMaps";
			treeNode2.Name = "RootNode";
			treeNode2.SelectedImageIndex = 0;
			treeNode2.Text = "Node0";
			this.treeViewMaps.Nodes.AddRange(new System.Windows.Forms.TreeNode[] {
            treeNode2});
			this.treeViewMaps.SelectedImageIndex = 0;
			this.treeViewMaps.Size = new System.Drawing.Size(267, 168);
			this.treeViewMaps.TabIndex = 0;
			this.treeViewMaps.AfterSelect += new System.Windows.Forms.TreeViewEventHandler(this.TreeViewMapsAfterSelect);
			// 
			// imageList
			// 
			this.imageList.ImageStream = ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("imageList.ImageStream")));
			this.imageList.TransparentColor = System.Drawing.Color.Transparent;
			this.imageList.Images.SetKeyName(0, "FolderOpen.png");
			this.imageList.Images.SetKeyName(1, "NewDocument.png");
			// 
			// mapEditorXnaPanel
			// 
			this.mapEditorXnaPanel.Location = new System.Drawing.Point(0, 25);
			this.mapEditorXnaPanel.Map = null;
			this.mapEditorXnaPanel.MapInfo = null;
			this.mapEditorXnaPanel.Name = "mapEditorXnaPanel";
			this.mapEditorXnaPanel.SelectionEnabled = true;
			this.mapEditorXnaPanel.Size = new System.Drawing.Size(210, 188);
			this.mapEditorXnaPanel.TabIndex = 2;
			this.mapEditorXnaPanel.Text = "mapEditorXnaPanel";
			// 
			// tilesetSelectionPanel
			// 
			this.tilesetSelectionPanel.Location = new System.Drawing.Point(0, 0);
			this.tilesetSelectionPanel.MinimumSize = new System.Drawing.Size(256, 32);
			this.tilesetSelectionPanel.Name = "tilesetSelectionPanel";
			this.tilesetSelectionPanel.Size = new System.Drawing.Size(256, 244);
			this.tilesetSelectionPanel.TabIndex = 0;
			this.tilesetSelectionPanel.TabStop = false;
			this.tilesetSelectionPanel.Tileset = null;
			// 
			// MapEditorMainForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(782, 425);
			this.Controls.Add(this.panelXnaParent);
			this.DefaultFloatSize = new System.Drawing.Size(800, 600);
			this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.Name = "MapEditorMainForm";
			this.ShowInTaskbar = false;
			this.Text = "Map Editor";
			this.Load += new System.EventHandler(this.MapEditorMainFormLoad);
			this.panelXnaParent.ResumeLayout(false);
			this.panel1.ResumeLayout(false);
			this.panel1.PerformLayout();
			this.splitContainerControls.Panel1.ResumeLayout(false);
			this.splitContainerControls.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerControls)).EndInit();
			this.splitContainerControls.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.tilesetSelectionPanel)).EndInit();
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.Panel panelXnaParent;
		private System.Windows.Forms.SplitContainer splitContainerControls;
		private System.Windows.Forms.TreeView treeViewMaps;
		private System.Windows.Forms.Panel panel1;
		private Controls.MapEditorXnaPanel mapEditorXnaPanel;
		private System.Windows.Forms.ToolStrip toolStrip;
		private System.Windows.Forms.ImageList imageList;
		private Controls.MapSourceSelectorPanel tilesetSelectionPanel;

	}
}