namespace ARCed.Scripting
{
	partial class ScriptMenuForm
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
			this.contextMenu = new System.Windows.Forms.ContextMenuStrip(this.components);
			this.contextButtonInsert = new System.Windows.Forms.ToolStripMenuItem();
			this.contextButtonDelete = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripSeparator4 = new System.Windows.Forms.ToolStripSeparator();
			this.contextButtonMoveUp = new System.Windows.Forms.ToolStripMenuItem();
			this.contextButtonMoveDown = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripSeparator5 = new System.Windows.Forms.ToolStripSeparator();
			this.contextButtonFind = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripSeparator6 = new System.Windows.Forms.ToolStripSeparator();
			this.buttonTemplate = new System.Windows.Forms.ToolStripMenuItem();
			this.labelName = new System.Windows.Forms.Label();
			this.textBoxName = new System.Windows.Forms.TextBox();
			this.toolStrip = new System.Windows.Forms.ToolStrip();
			this.buttonImport = new System.Windows.Forms.ToolStripButton();
			this.buttonAdd = new System.Windows.Forms.ToolStripButton();
			this.buttonOpen = new System.Windows.Forms.ToolStripButton();
			this.toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
			this.buttonMoveUp = new System.Windows.Forms.ToolStripButton();
			this.buttonMoveDown = new System.Windows.Forms.ToolStripButton();
			this.toolStripSeparator2 = new System.Windows.Forms.ToolStripSeparator();
			this.buttonSaveAll = new System.Windows.Forms.ToolStripButton();
			this.buttonDelete = new System.Windows.Forms.ToolStripButton();
			this.toolStripSeparator3 = new System.Windows.Forms.ToolStripSeparator();
			this.buttonFind = new System.Windows.Forms.ToolStripButton();
			this.fileSystemWatcher = new System.IO.FileSystemWatcher();
			this.listBoxScripts = new ARCed.Controls.DoubleBufferedListBox();
			this.pictureHeader = new System.Windows.Forms.PictureBox();
			this.contextMenu.SuspendLayout();
			this.toolStrip.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.fileSystemWatcher)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.pictureHeader)).BeginInit();
			this.SuspendLayout();
			// 
			// contextMenu
			// 
			this.contextMenu.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.contextButtonInsert,
            this.contextButtonDelete,
            this.toolStripSeparator4,
            this.contextButtonMoveUp,
            this.contextButtonMoveDown,
            this.toolStripSeparator5,
            this.contextButtonFind,
            this.toolStripSeparator6,
            this.buttonTemplate});
			this.contextMenu.Name = "contextMenu";
			this.contextMenu.Size = new System.Drawing.Size(200, 154);
			// 
			// contextButtonInsert
			// 
			this.contextButtonInsert.Image = global::ARCed.Properties.Resources.NewDocument;
			this.contextButtonInsert.Name = "contextButtonInsert";
			this.contextButtonInsert.ShortcutKeys = System.Windows.Forms.Keys.Insert;
			this.contextButtonInsert.Size = new System.Drawing.Size(199, 22);
			this.contextButtonInsert.Text = "Insert...";
			this.contextButtonInsert.Click += new System.EventHandler(this.buttonInsert_Click);
			// 
			// contextButtonDelete
			// 
			this.contextButtonDelete.Image = global::ARCed.Properties.Resources.Delete;
			this.contextButtonDelete.Name = "contextButtonDelete";
			this.contextButtonDelete.ShortcutKeys = System.Windows.Forms.Keys.Delete;
			this.contextButtonDelete.Size = new System.Drawing.Size(199, 22);
			this.contextButtonDelete.Text = "Delete";
			this.contextButtonDelete.Click += new System.EventHandler(this.buttonDelete_Click);
			// 
			// toolStripSeparator4
			// 
			this.toolStripSeparator4.Name = "toolStripSeparator4";
			this.toolStripSeparator4.Size = new System.Drawing.Size(196, 6);
			// 
			// contextButtonMoveUp
			// 
			this.contextButtonMoveUp.Image = global::ARCed.Properties.Resources.Up;
			this.contextButtonMoveUp.Name = "contextButtonMoveUp";
			this.contextButtonMoveUp.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Alt | System.Windows.Forms.Keys.Up)));
			this.contextButtonMoveUp.Size = new System.Drawing.Size(199, 22);
			this.contextButtonMoveUp.Text = "Move Up";
			// 
			// contextButtonMoveDown
			// 
			this.contextButtonMoveDown.Image = global::ARCed.Properties.Resources.Down;
			this.contextButtonMoveDown.Name = "contextButtonMoveDown";
			this.contextButtonMoveDown.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Alt | System.Windows.Forms.Keys.Down)));
			this.contextButtonMoveDown.Size = new System.Drawing.Size(199, 22);
			this.contextButtonMoveDown.Text = "Move Down";
			// 
			// toolStripSeparator5
			// 
			this.toolStripSeparator5.Name = "toolStripSeparator5";
			this.toolStripSeparator5.Size = new System.Drawing.Size(196, 6);
			// 
			// contextButtonFind
			// 
			this.contextButtonFind.Image = global::ARCed.Properties.Resources.Find1;
			this.contextButtonFind.Name = "contextButtonFind";
			this.contextButtonFind.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.F)));
			this.contextButtonFind.Size = new System.Drawing.Size(199, 22);
			this.contextButtonFind.Text = "Find...";
			// 
			// toolStripSeparator6
			// 
			this.toolStripSeparator6.Name = "toolStripSeparator6";
			this.toolStripSeparator6.Size = new System.Drawing.Size(196, 6);
			// 
			// buttonTemplate
			// 
			this.buttonTemplate.Image = global::ARCed.Properties.Resources.SaveTemplate;
			this.buttonTemplate.Name = "buttonTemplate";
			this.buttonTemplate.Size = new System.Drawing.Size(199, 22);
			this.buttonTemplate.Text = "Save as Template...";
			this.buttonTemplate.Click += new System.EventHandler(this.buttonTemplate_Click);
			// 
			// labelName
			// 
			this.labelName.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.labelName.AutoSize = true;
			this.labelName.Location = new System.Drawing.Point(9, 399);
			this.labelName.Name = "labelName";
			this.labelName.Size = new System.Drawing.Size(38, 13);
			this.labelName.TabIndex = 6;
			this.labelName.Text = "Name:";
			// 
			// textBoxName
			// 
			this.textBoxName.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBoxName.Location = new System.Drawing.Point(53, 396);
			this.textBoxName.Name = "textBoxName";
			this.textBoxName.Size = new System.Drawing.Size(153, 20);
			this.textBoxName.TabIndex = 7;
			this.textBoxName.TextChanged += new System.EventHandler(this.textBoxName_TextChanged);
			// 
			// toolStrip
			// 
			this.toolStrip.Dock = System.Windows.Forms.DockStyle.Bottom;
			this.toolStrip.GripStyle = System.Windows.Forms.ToolStripGripStyle.Hidden;
			this.toolStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.buttonImport,
            this.buttonAdd,
            this.buttonOpen,
            this.toolStripSeparator1,
            this.buttonMoveUp,
            this.buttonMoveDown,
            this.toolStripSeparator2,
            this.buttonSaveAll,
            this.buttonDelete,
            this.toolStripSeparator3,
            this.buttonFind});
			this.toolStrip.Location = new System.Drawing.Point(0, 423);
			this.toolStrip.Name = "toolStrip";
			this.toolStrip.Size = new System.Drawing.Size(218, 25);
			this.toolStrip.TabIndex = 8;
			this.toolStrip.Text = "toolStrip";
			// 
			// buttonImport
			// 
			this.buttonImport.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			this.buttonImport.Image = global::ARCed.Properties.Resources.FolderOpen;
			this.buttonImport.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.buttonImport.Name = "buttonImport";
			this.buttonImport.Size = new System.Drawing.Size(23, 22);
			this.buttonImport.Text = "Import Script";
			this.buttonImport.Click += new System.EventHandler(this.buttonImport_Click);
			// 
			// buttonAdd
			// 
			this.buttonAdd.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			this.buttonAdd.Image = global::ARCed.Properties.Resources.Add;
			this.buttonAdd.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.buttonAdd.Name = "buttonAdd";
			this.buttonAdd.Size = new System.Drawing.Size(23, 22);
			this.buttonAdd.Text = "Add Script";
			this.buttonAdd.Click += new System.EventHandler(this.buttonAdd_Click);
			// 
			// buttonOpen
			// 
			this.buttonOpen.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			this.buttonOpen.Enabled = false;
			this.buttonOpen.Image = global::ARCed.Properties.Resources.NewDocument;
			this.buttonOpen.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.buttonOpen.Name = "buttonOpen";
			this.buttonOpen.Size = new System.Drawing.Size(23, 22);
			this.buttonOpen.Text = "Open Script";
			this.buttonOpen.Click += new System.EventHandler(this.buttonOpen_Click);
			// 
			// toolStripSeparator1
			// 
			this.toolStripSeparator1.Name = "toolStripSeparator1";
			this.toolStripSeparator1.Size = new System.Drawing.Size(6, 25);
			// 
			// buttonMoveUp
			// 
			this.buttonMoveUp.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			this.buttonMoveUp.Enabled = false;
			this.buttonMoveUp.Image = global::ARCed.Properties.Resources.Up;
			this.buttonMoveUp.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.buttonMoveUp.Name = "buttonMoveUp";
			this.buttonMoveUp.Size = new System.Drawing.Size(23, 22);
			this.buttonMoveUp.Text = "Move Up";
			this.buttonMoveUp.Click += new System.EventHandler(this.buttonMoveUp_Click);
			// 
			// buttonMoveDown
			// 
			this.buttonMoveDown.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			this.buttonMoveDown.Enabled = false;
			this.buttonMoveDown.Image = global::ARCed.Properties.Resources.Down;
			this.buttonMoveDown.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.buttonMoveDown.Name = "buttonMoveDown";
			this.buttonMoveDown.Size = new System.Drawing.Size(23, 22);
			this.buttonMoveDown.Text = "Move Down";
			this.buttonMoveDown.Click += new System.EventHandler(this.buttonMoveDown_Click);
			// 
			// toolStripSeparator2
			// 
			this.toolStripSeparator2.Name = "toolStripSeparator2";
			this.toolStripSeparator2.Size = new System.Drawing.Size(6, 25);
			// 
			// buttonSaveAll
			// 
			this.buttonSaveAll.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			this.buttonSaveAll.Image = global::ARCed.Properties.Resources.SaveAll;
			this.buttonSaveAll.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.buttonSaveAll.Name = "buttonSaveAll";
			this.buttonSaveAll.Size = new System.Drawing.Size(23, 22);
			this.buttonSaveAll.Text = "Save All";
			this.buttonSaveAll.Click += new System.EventHandler(this.buttonSaveAll_Click);
			// 
			// buttonDelete
			// 
			this.buttonDelete.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			this.buttonDelete.Enabled = false;
			this.buttonDelete.Image = global::ARCed.Properties.Resources.Delete;
			this.buttonDelete.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.buttonDelete.Name = "buttonDelete";
			this.buttonDelete.Size = new System.Drawing.Size(23, 22);
			this.buttonDelete.Text = "Delete";
			this.buttonDelete.Click += new System.EventHandler(this.buttonDelete_Click);
			// 
			// toolStripSeparator3
			// 
			this.toolStripSeparator3.Name = "toolStripSeparator3";
			this.toolStripSeparator3.Size = new System.Drawing.Size(6, 25);
			// 
			// buttonFind
			// 
			this.buttonFind.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			this.buttonFind.Image = global::ARCed.Properties.Resources.Find1;
			this.buttonFind.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.buttonFind.Name = "buttonFind";
			this.buttonFind.Size = new System.Drawing.Size(23, 22);
			this.buttonFind.Text = "Find in scripts...";
			this.buttonFind.Click += new System.EventHandler(this.buttonFind_Click);
			// 
			// fileSystemWatcher
			// 
			this.fileSystemWatcher.EnableRaisingEvents = true;
			this.fileSystemWatcher.Filter = "*.rb";
			this.fileSystemWatcher.NotifyFilter = System.IO.NotifyFilters.FileName;
			this.fileSystemWatcher.SynchronizingObject = this;
			this.fileSystemWatcher.Created += new System.IO.FileSystemEventHandler(this.fileSystemWatcher_CreatedorDeleted);
			this.fileSystemWatcher.Deleted += new System.IO.FileSystemEventHandler(this.fileSystemWatcher_CreatedorDeleted);
			// 
			// listBoxScripts
			// 
			this.listBoxScripts.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.listBoxScripts.ContextMenuStrip = this.contextMenu;
			this.listBoxScripts.DisplayMember = "Title";
			this.listBoxScripts.FormattingEnabled = true;
			this.listBoxScripts.IntegralHeight = false;
			this.listBoxScripts.Location = new System.Drawing.Point(0, 29);
			this.listBoxScripts.Name = "listBoxScripts";
			this.listBoxScripts.Size = new System.Drawing.Size(218, 355);
			this.listBoxScripts.TabIndex = 9;
			this.listBoxScripts.ValueMember = "Filename";
			this.listBoxScripts.SelectedIndexChanged += new System.EventHandler(this.listBoxScripts_SelectedIndexChanged);
			this.listBoxScripts.DoubleClick += new System.EventHandler(this.buttonOpen_Click);
			this.listBoxScripts.MouseDown += new System.Windows.Forms.MouseEventHandler(this.listBoxScripts_MouseDown);
			// 
			// pictureHeader
			// 
			this.pictureHeader.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.pictureHeader.Location = new System.Drawing.Point(0, 0);
			this.pictureHeader.Name = "pictureHeader";
			this.pictureHeader.Size = new System.Drawing.Size(218, 29);
			this.pictureHeader.TabIndex = 10;
			this.pictureHeader.TabStop = false;
			this.pictureHeader.SizeChanged += new System.EventHandler(this.pictureHeader_SizeChanged);
			this.pictureHeader.DoubleClick += new System.EventHandler(this.pictureHeader_DoubleClick);
			// 
			// ScriptMenuForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(218, 448);
			this.Controls.Add(this.pictureHeader);
			this.Controls.Add(this.listBoxScripts);
			this.Controls.Add(this.toolStrip);
			this.Controls.Add(this.textBoxName);
			this.Controls.Add(this.labelName);
			this.DefaultFloatSize = new System.Drawing.Size(228, 480);
			this.DockAreas = ((ARCed.UI.DockAreas)(((((ARCed.UI.DockAreas.Float | ARCed.UI.DockAreas.DockLeft)
						| ARCed.UI.DockAreas.DockRight)
						| ARCed.UI.DockAreas.DockTop)
						| ARCed.UI.DockAreas.DockBottom)));
			this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.SizableToolWindow;
			this.Name = "ScriptMenuForm";
			this.ShowHint = ARCed.UI.DockState.DockLeft;
			this.Text = "Scripts";
			this.contextMenu.ResumeLayout(false);
			this.toolStrip.ResumeLayout(false);
			this.toolStrip.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.fileSystemWatcher)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.pictureHeader)).EndInit();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Label labelName;
		private System.Windows.Forms.TextBox textBoxName;
		private System.Windows.Forms.ToolStrip toolStrip;
		private System.Windows.Forms.ToolStripButton buttonImport;
		private System.Windows.Forms.ToolStripButton buttonOpen;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator1;
		private System.Windows.Forms.ToolStripButton buttonMoveUp;
		private System.Windows.Forms.ToolStripButton buttonMoveDown;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator2;
		private System.Windows.Forms.ToolStripButton buttonDelete;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator3;
		private System.Windows.Forms.ToolStripButton buttonFind;
		private System.Windows.Forms.ContextMenuStrip contextMenu;
		private System.Windows.Forms.ToolStripMenuItem contextButtonInsert;
		private System.Windows.Forms.ToolStripMenuItem contextButtonDelete;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator4;
		private System.Windows.Forms.ToolStripMenuItem contextButtonMoveUp;
		private System.Windows.Forms.ToolStripMenuItem contextButtonMoveDown;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator5;
		private System.Windows.Forms.ToolStripMenuItem contextButtonFind;
		private System.Windows.Forms.ToolStripButton buttonAdd;
		private System.Windows.Forms.ToolStripButton buttonSaveAll;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator6;
		private System.Windows.Forms.ToolStripMenuItem buttonTemplate;
		private System.IO.FileSystemWatcher fileSystemWatcher;
		private Controls.DoubleBufferedListBox listBoxScripts;
		private System.Windows.Forms.PictureBox pictureHeader;
	}
}