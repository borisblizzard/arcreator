namespace ARCed.Controls
{
	partial class DatabaseObjectListBox
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
			this.pictureBoxHeader = new System.Windows.Forms.PictureBox();
			this.contextMenuHeader = new System.Windows.Forms.ContextMenuStrip(this.components);
			this.toolStripMenuItemEdit = new System.Windows.Forms.ToolStripMenuItem();
			this.listBoxObjects = new System.Windows.Forms.ListBox();
			this.buttonMaximum = new System.Windows.Forms.Button();
			this.toolTip = new System.Windows.Forms.ToolTip(this.components);
			((System.ComponentModel.ISupportInitialize)(this.pictureBoxHeader)).BeginInit();
			this.contextMenuHeader.SuspendLayout();
			this.SuspendLayout();
			// 
			// pictureBoxHeader
			// 
			this.pictureBoxHeader.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.pictureBoxHeader.BackColor = System.Drawing.SystemColors.ControlDark;
			this.pictureBoxHeader.ContextMenuStrip = this.contextMenuHeader;
			this.pictureBoxHeader.Location = new System.Drawing.Point(10, 16);
			this.pictureBoxHeader.Margin = new System.Windows.Forms.Padding(3, 3, 3, 0);
			this.pictureBoxHeader.Name = "pictureBoxHeader";
			this.pictureBoxHeader.Size = new System.Drawing.Size(146, 29);
			this.pictureBoxHeader.TabIndex = 2;
			this.pictureBoxHeader.TabStop = false;
			this.pictureBoxHeader.SizeChanged += new System.EventHandler(this.PictureBoxHeaderResize);
			this.pictureBoxHeader.DoubleClick += new System.EventHandler(this.PictureBoxHeaderDoubleClick);
			// 
			// contextMenuHeader
			// 
			this.contextMenuHeader.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripMenuItemEdit});
			this.contextMenuHeader.Name = "contextMenuHeader";
			this.contextMenuHeader.Size = new System.Drawing.Size(170, 26);
			// 
			// toolStripMenuItemEdit
			// 
			this.toolStripMenuItemEdit.Name = "toolStripMenuItemEdit";
			this.toolStripMenuItemEdit.Size = new System.Drawing.Size(169, 22);
			this.toolStripMenuItemEdit.Text = "Edit Appearance...";
			// 
			// listBoxObjects
			// 
			this.listBoxObjects.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.listBoxObjects.IntegralHeight = false;
			this.listBoxObjects.Location = new System.Drawing.Point(10, 45);
			this.listBoxObjects.Margin = new System.Windows.Forms.Padding(3, 0, 3, 3);
			this.listBoxObjects.Name = "listBoxObjects";
			this.listBoxObjects.Size = new System.Drawing.Size(146, 372);
			this.listBoxObjects.TabIndex = 1;
			this.toolTip.SetToolTip(this.listBoxObjects, "Select object to edit");
			this.listBoxObjects.SelectedIndexChanged += new System.EventHandler(this.ListBoxObjectsSelectedIndexChanged);
			// 
			// buttonMaximum
			// 
			this.buttonMaximum.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.buttonMaximum.Location = new System.Drawing.Point(10, 423);
			this.buttonMaximum.Name = "buttonMaximum";
			this.buttonMaximum.Size = new System.Drawing.Size(146, 23);
			this.buttonMaximum.TabIndex = 0;
			this.buttonMaximum.Text = "Change Maximum...";
			this.toolTip.SetToolTip(this.buttonMaximum, "Change maximum amount of items");
			this.buttonMaximum.UseVisualStyleBackColor = true;
			this.buttonMaximum.Click += new System.EventHandler(this.ButtonMaximumClick);
			// 
			// DatabaseObjectListBox
			// 
			this.Controls.Add(this.pictureBoxHeader);
			this.Controls.Add(this.listBoxObjects);
			this.Controls.Add(this.buttonMaximum);
			this.Size = new System.Drawing.Size(166, 452);
			((System.ComponentModel.ISupportInitialize)(this.pictureBoxHeader)).EndInit();
			this.contextMenuHeader.ResumeLayout(false);
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.PictureBox pictureBoxHeader;
		private System.Windows.Forms.ListBox listBoxObjects;
		private System.Windows.Forms.Button buttonMaximum;
		private System.Windows.Forms.ToolTip toolTip;
		private System.Windows.Forms.ContextMenuStrip contextMenuHeader;
		private System.Windows.Forms.ToolStripMenuItem toolStripMenuItemEdit;
	}
}
