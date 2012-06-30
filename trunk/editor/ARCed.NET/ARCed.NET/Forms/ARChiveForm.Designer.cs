namespace ARCed.Forms
{
	partial class ARChiveForm
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
			System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(ARChiveForm));
			this.groupBoxType = new System.Windows.Forms.GroupBox();
			this.checkBoxTypeScripts = new System.Windows.Forms.CheckBox();
			this.checkBoxTypeMaps = new System.Windows.Forms.CheckBox();
			this.checkBoxTypeAllData = new System.Windows.Forms.CheckBox();
			this.groupBoxFrequency = new System.Windows.Forms.GroupBox();
			this.radioButtonInterval = new System.Windows.Forms.RadioButton();
			this.radioButtonSave = new System.Windows.Forms.RadioButton();
			this.radioButtonDebug = new System.Windows.Forms.RadioButton();
			this.radioButtonRun = new System.Windows.Forms.RadioButton();
			this.radioButtonNone = new System.Windows.Forms.RadioButton();
			this.checkBoxThreaded = new System.Windows.Forms.CheckBox();
			this.labelMinutes = new System.Windows.Forms.Label();
			this.numericInterval = new System.Windows.Forms.NumericUpDown();
			this.toolTip = new System.Windows.Forms.ToolTip(this.components);
			this.buttonRemove = new System.Windows.Forms.Button();
			this.buttonCreateNew = new System.Windows.Forms.Button();
			this.buttonRestore = new System.Windows.Forms.Button();
			this.labelMaxBackups = new System.Windows.Forms.Label();
			this.numericMaxBackups = new System.Windows.Forms.NumericUpDown();
			this.listViewARChives = new System.Windows.Forms.ListView();
			this.columnCreated = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
			this.columnSize = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
			this.columnName = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
			this.contextMenuStrip = new System.Windows.Forms.ContextMenuStrip(this.components);
			this.restoreToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.removeToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripSeparator2 = new System.Windows.Forms.ToolStripSeparator();
			this.openFileLocationToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.shellOpenToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.imageList = new System.Windows.Forms.ImageList(this.components);
			this.fileSystemWatcher = new System.IO.FileSystemWatcher();
			this.groupBoxSettings = new ARCed.Controls.CollapsibleGroupBox();
			this.splitContainer1 = new System.Windows.Forms.SplitContainer();
			this.splitContainer2 = new System.Windows.Forms.SplitContainer();
			this.groupBoxType.SuspendLayout();
			this.groupBoxFrequency.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.numericInterval)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.numericMaxBackups)).BeginInit();
			this.contextMenuStrip.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.fileSystemWatcher)).BeginInit();
			this.groupBoxSettings.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).BeginInit();
			this.splitContainer1.Panel1.SuspendLayout();
			this.splitContainer1.Panel2.SuspendLayout();
			this.splitContainer1.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainer2)).BeginInit();
			this.splitContainer2.Panel1.SuspendLayout();
			this.splitContainer2.Panel2.SuspendLayout();
			this.splitContainer2.SuspendLayout();
			this.SuspendLayout();
			// 
			// groupBoxType
			// 
			this.groupBoxType.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxType.Controls.Add(this.checkBoxTypeScripts);
			this.groupBoxType.Controls.Add(this.checkBoxTypeMaps);
			this.groupBoxType.Controls.Add(this.checkBoxTypeAllData);
			this.groupBoxType.Location = new System.Drawing.Point(7, 3);
			this.groupBoxType.Name = "groupBoxType";
			this.groupBoxType.Size = new System.Drawing.Size(105, 91);
			this.groupBoxType.TabIndex = 0;
			this.groupBoxType.TabStop = false;
			this.groupBoxType.Text = "Backup Type";
			// 
			// checkBoxTypeScripts
			// 
			this.checkBoxTypeScripts.AutoSize = true;
			this.checkBoxTypeScripts.Location = new System.Drawing.Point(6, 41);
			this.checkBoxTypeScripts.Name = "checkBoxTypeScripts";
			this.checkBoxTypeScripts.Size = new System.Drawing.Size(58, 17);
			this.checkBoxTypeScripts.TabIndex = 2;
			this.checkBoxTypeScripts.Text = "Scripts";
			this.toolTip.SetToolTip(this.checkBoxTypeScripts, "Backs up the project\'s \"Scripts\" folder");
			this.checkBoxTypeScripts.UseVisualStyleBackColor = true;
			this.checkBoxTypeScripts.CheckedChanged += new System.EventHandler(this.checkBoxType_CheckChanged);
			// 
			// checkBoxTypeMaps
			// 
			this.checkBoxTypeMaps.AutoSize = true;
			this.checkBoxTypeMaps.Checked = true;
			this.checkBoxTypeMaps.CheckState = System.Windows.Forms.CheckState.Checked;
			this.checkBoxTypeMaps.Location = new System.Drawing.Point(6, 64);
			this.checkBoxTypeMaps.Name = "checkBoxTypeMaps";
			this.checkBoxTypeMaps.Size = new System.Drawing.Size(52, 17);
			this.checkBoxTypeMaps.TabIndex = 1;
			this.checkBoxTypeMaps.Text = "Maps";
			this.toolTip.SetToolTip(this.checkBoxTypeMaps, "Backs up the project\'s Map files");
			this.checkBoxTypeMaps.UseVisualStyleBackColor = true;
			this.checkBoxTypeMaps.CheckedChanged += new System.EventHandler(this.checkBoxType_CheckChanged);
			// 
			// checkBoxTypeAllData
			// 
			this.checkBoxTypeAllData.AutoSize = true;
			this.checkBoxTypeAllData.Location = new System.Drawing.Point(6, 19);
			this.checkBoxTypeAllData.Name = "checkBoxTypeAllData";
			this.checkBoxTypeAllData.Size = new System.Drawing.Size(63, 17);
			this.checkBoxTypeAllData.TabIndex = 0;
			this.checkBoxTypeAllData.Text = "All Data";
			this.toolTip.SetToolTip(this.checkBoxTypeAllData, "Full backup of projects Data folder");
			this.checkBoxTypeAllData.UseVisualStyleBackColor = true;
			this.checkBoxTypeAllData.CheckedChanged += new System.EventHandler(this.checkBoxTypeAll_CheckedChanged);
			// 
			// groupBoxFrequency
			// 
			this.groupBoxFrequency.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxFrequency.Controls.Add(this.radioButtonInterval);
			this.groupBoxFrequency.Controls.Add(this.radioButtonSave);
			this.groupBoxFrequency.Controls.Add(this.radioButtonDebug);
			this.groupBoxFrequency.Controls.Add(this.radioButtonRun);
			this.groupBoxFrequency.Controls.Add(this.radioButtonNone);
			this.groupBoxFrequency.Location = new System.Drawing.Point(3, 3);
			this.groupBoxFrequency.Name = "groupBoxFrequency";
			this.groupBoxFrequency.Size = new System.Drawing.Size(102, 138);
			this.groupBoxFrequency.TabIndex = 1;
			this.groupBoxFrequency.TabStop = false;
			this.groupBoxFrequency.Text = "Frequency";
			// 
			// radioButtonInterval
			// 
			this.radioButtonInterval.AutoSize = true;
			this.radioButtonInterval.Location = new System.Drawing.Point(6, 110);
			this.radioButtonInterval.Name = "radioButtonInterval";
			this.radioButtonInterval.Size = new System.Drawing.Size(60, 17);
			this.radioButtonInterval.TabIndex = 4;
			this.radioButtonInterval.Text = "Interval";
			this.toolTip.SetToolTip(this.radioButtonInterval, "Create backup every so many minutes (define below)");
			this.radioButtonInterval.UseVisualStyleBackColor = true;
			this.radioButtonInterval.Click += new System.EventHandler(this.radioButtonFrequency_Click);
			// 
			// radioButtonSave
			// 
			this.radioButtonSave.AutoSize = true;
			this.radioButtonSave.Location = new System.Drawing.Point(6, 88);
			this.radioButtonSave.Name = "radioButtonSave";
			this.radioButtonSave.Size = new System.Drawing.Size(50, 17);
			this.radioButtonSave.TabIndex = 3;
			this.radioButtonSave.Text = "Save";
			this.toolTip.SetToolTip(this.radioButtonSave, "Create backup each time the game is saved");
			this.radioButtonSave.UseVisualStyleBackColor = true;
			this.radioButtonSave.Click += new System.EventHandler(this.radioButtonFrequency_Click);
			// 
			// radioButtonDebug
			// 
			this.radioButtonDebug.AutoSize = true;
			this.radioButtonDebug.Location = new System.Drawing.Point(6, 64);
			this.radioButtonDebug.Name = "radioButtonDebug";
			this.radioButtonDebug.Size = new System.Drawing.Size(80, 17);
			this.radioButtonDebug.TabIndex = 2;
			this.radioButtonDebug.Text = "Debug Run";
			this.toolTip.SetToolTip(this.radioButtonDebug, "Create backup each time the game is ran in DEBUG mode");
			this.radioButtonDebug.UseVisualStyleBackColor = true;
			this.radioButtonDebug.Click += new System.EventHandler(this.radioButtonFrequency_Click);
			// 
			// radioButtonRun
			// 
			this.radioButtonRun.AutoSize = true;
			this.radioButtonRun.Location = new System.Drawing.Point(6, 42);
			this.radioButtonRun.Name = "radioButtonRun";
			this.radioButtonRun.Size = new System.Drawing.Size(45, 17);
			this.radioButtonRun.TabIndex = 1;
			this.radioButtonRun.Text = "Run";
			this.toolTip.SetToolTip(this.radioButtonRun, "Create backup each time the game is ran");
			this.radioButtonRun.UseVisualStyleBackColor = true;
			this.radioButtonRun.Click += new System.EventHandler(this.radioButtonFrequency_Click);
			// 
			// radioButtonNone
			// 
			this.radioButtonNone.AutoSize = true;
			this.radioButtonNone.Checked = true;
			this.radioButtonNone.Location = new System.Drawing.Point(6, 19);
			this.radioButtonNone.Name = "radioButtonNone";
			this.radioButtonNone.Size = new System.Drawing.Size(51, 17);
			this.radioButtonNone.TabIndex = 0;
			this.radioButtonNone.TabStop = true;
			this.radioButtonNone.Text = "None";
			this.toolTip.SetToolTip(this.radioButtonNone, "Disable backup creation");
			this.radioButtonNone.UseVisualStyleBackColor = true;
			this.radioButtonNone.Click += new System.EventHandler(this.radioButtonFrequency_Click);
			// 
			// checkBoxThreaded
			// 
			this.checkBoxThreaded.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.checkBoxThreaded.AutoSize = true;
			this.checkBoxThreaded.Checked = true;
			this.checkBoxThreaded.CheckState = System.Windows.Forms.CheckState.Checked;
			this.checkBoxThreaded.Location = new System.Drawing.Point(9, 163);
			this.checkBoxThreaded.Name = "checkBoxThreaded";
			this.checkBoxThreaded.Size = new System.Drawing.Size(72, 17);
			this.checkBoxThreaded.TabIndex = 2;
			this.checkBoxThreaded.Text = "Threaded";
			this.toolTip.SetToolTip(this.checkBoxThreaded, "Run backup on separate thread to prevent lag on editor");
			this.checkBoxThreaded.UseVisualStyleBackColor = true;
			// 
			// labelMinutes
			// 
			this.labelMinutes.AutoSize = true;
			this.labelMinutes.Location = new System.Drawing.Point(9, 105);
			this.labelMinutes.Name = "labelMinutes";
			this.labelMinutes.Size = new System.Drawing.Size(90, 13);
			this.labelMinutes.TabIndex = 5;
			this.labelMinutes.Text = "Interval (minutes):";
			// 
			// numericInterval
			// 
			this.numericInterval.Location = new System.Drawing.Point(12, 121);
			this.numericInterval.Maximum = new decimal(new int[] {
            120,
            0,
            0,
            0});
			this.numericInterval.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
			this.numericInterval.Name = "numericInterval";
			this.numericInterval.Size = new System.Drawing.Size(58, 20);
			this.numericInterval.TabIndex = 6;
			this.toolTip.SetToolTip(this.numericInterval, "The interval, in minutes, between backup creation");
			this.numericInterval.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
			// 
			// buttonRemove
			// 
			this.buttonRemove.Enabled = false;
			this.buttonRemove.Location = new System.Drawing.Point(161, 3);
			this.buttonRemove.Name = "buttonRemove";
			this.buttonRemove.Size = new System.Drawing.Size(73, 48);
			this.buttonRemove.TabIndex = 9;
			this.buttonRemove.Text = "Remove ARChive";
			this.toolTip.SetToolTip(this.buttonRemove, "Remove selected backup");
			this.buttonRemove.UseVisualStyleBackColor = true;
			this.buttonRemove.Click += new System.EventHandler(this.buttonRemove_Click);
			// 
			// buttonCreateNew
			// 
			this.buttonCreateNew.Location = new System.Drawing.Point(-1, 3);
			this.buttonCreateNew.Name = "buttonCreateNew";
			this.buttonCreateNew.Size = new System.Drawing.Size(75, 48);
			this.buttonCreateNew.TabIndex = 11;
			this.buttonCreateNew.Text = "Create New ARChive";
			this.toolTip.SetToolTip(this.buttonCreateNew, "Create backup of project in its current state");
			this.buttonCreateNew.UseVisualStyleBackColor = true;
			this.buttonCreateNew.Click += new System.EventHandler(this.buttonCreateNew_Click);
			// 
			// buttonRestore
			// 
			this.buttonRestore.Enabled = false;
			this.buttonRestore.Location = new System.Drawing.Point(80, 3);
			this.buttonRestore.Name = "buttonRestore";
			this.buttonRestore.Size = new System.Drawing.Size(75, 48);
			this.buttonRestore.TabIndex = 12;
			this.buttonRestore.Text = "Restore ARChive";
			this.toolTip.SetToolTip(this.buttonRestore, "Unpackage the selected backup");
			this.buttonRestore.UseVisualStyleBackColor = true;
			this.buttonRestore.Click += new System.EventHandler(this.buttonRestore_Click);
			// 
			// labelMaxBackups
			// 
			this.labelMaxBackups.AutoSize = true;
			this.labelMaxBackups.Location = new System.Drawing.Point(10, 147);
			this.labelMaxBackups.Name = "labelMaxBackups";
			this.labelMaxBackups.Size = new System.Drawing.Size(75, 13);
			this.labelMaxBackups.TabIndex = 8;
			this.labelMaxBackups.Text = "Max Backups:";
			// 
			// numericMaxBackups
			// 
			this.numericMaxBackups.Location = new System.Drawing.Point(12, 163);
			this.numericMaxBackups.Maximum = new decimal(new int[] {
            20,
            0,
            0,
            0});
			this.numericMaxBackups.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
			this.numericMaxBackups.Name = "numericMaxBackups";
			this.numericMaxBackups.Size = new System.Drawing.Size(59, 20);
			this.numericMaxBackups.TabIndex = 7;
			this.numericMaxBackups.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
			// 
			// listViewARChives
			// 
			this.listViewARChives.AllowColumnReorder = true;
			this.listViewARChives.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.columnCreated,
            this.columnSize,
            this.columnName});
			this.listViewARChives.ContextMenuStrip = this.contextMenuStrip;
			this.listViewARChives.Dock = System.Windows.Forms.DockStyle.Fill;
			this.listViewARChives.FullRowSelect = true;
			this.listViewARChives.GridLines = true;
			this.listViewARChives.HeaderStyle = System.Windows.Forms.ColumnHeaderStyle.Nonclickable;
			this.listViewARChives.HideSelection = false;
			this.listViewARChives.Location = new System.Drawing.Point(0, 0);
			this.listViewARChives.MinimumSize = new System.Drawing.Size(235, 4);
			this.listViewARChives.MultiSelect = false;
			this.listViewARChives.Name = "listViewARChives";
			this.listViewARChives.ShowItemToolTips = true;
			this.listViewARChives.Size = new System.Drawing.Size(236, 192);
			this.listViewARChives.SmallImageList = this.imageList;
			this.listViewARChives.TabIndex = 8;
			this.listViewARChives.UseCompatibleStateImageBehavior = false;
			this.listViewARChives.View = System.Windows.Forms.View.Details;
			this.listViewARChives.SelectedIndexChanged += new System.EventHandler(this.listViewARChives_SelectedIndexChanged);
			this.listViewARChives.DoubleClick += new System.EventHandler(this.listViewARChives_DoubleClick);
			this.listViewARChives.MouseDown += new System.Windows.Forms.MouseEventHandler(this.listViewARChives_MouseDown);
			// 
			// columnCreated
			// 
			this.columnCreated.Text = "Created";
			this.columnCreated.Width = 156;
			// 
			// columnSize
			// 
			this.columnSize.Text = "Size (KBs)";
			this.columnSize.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			this.columnSize.Width = 71;
			// 
			// columnName
			// 
			this.columnName.Text = "Filename (GUID)";
			this.columnName.Width = 256;
			// 
			// contextMenuStrip
			// 
			this.contextMenuStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.restoreToolStripMenuItem,
            this.removeToolStripMenuItem,
            this.toolStripSeparator2,
            this.openFileLocationToolStripMenuItem,
            this.shellOpenToolStripMenuItem});
			this.contextMenuStrip.Name = "contextMenuStrip";
			this.contextMenuStrip.Size = new System.Drawing.Size(178, 98);
			this.contextMenuStrip.Opened += new System.EventHandler(this.contextMenuStrip_Opened);
			// 
			// restoreToolStripMenuItem
			// 
			this.restoreToolStripMenuItem.Name = "restoreToolStripMenuItem";
			this.restoreToolStripMenuItem.Size = new System.Drawing.Size(177, 22);
			this.restoreToolStripMenuItem.Text = "Restore...";
			this.restoreToolStripMenuItem.ToolTipText = "Unpackage the selected backup";
			this.restoreToolStripMenuItem.Click += new System.EventHandler(this.buttonRestore_Click);
			// 
			// contextButtonActionRemove
			// 
			this.removeToolStripMenuItem.Name = "removeToolStripMenuItem";
			this.removeToolStripMenuItem.ShortcutKeys = System.Windows.Forms.Keys.Delete;
			this.removeToolStripMenuItem.Size = new System.Drawing.Size(177, 22);
			this.removeToolStripMenuItem.Text = "Remove";
			this.removeToolStripMenuItem.ToolTipText = "Remove selected backup";
			this.removeToolStripMenuItem.Click += new System.EventHandler(this.buttonRemove_Click);
			// 
			// toolStripSeparator2
			// 
			this.toolStripSeparator2.Name = "toolStripSeparator2";
			this.toolStripSeparator2.Size = new System.Drawing.Size(174, 6);
			// 
			// openFileLocationToolStripMenuItem
			// 
			this.openFileLocationToolStripMenuItem.Name = "openFileLocationToolStripMenuItem";
			this.openFileLocationToolStripMenuItem.Size = new System.Drawing.Size(177, 22);
			this.openFileLocationToolStripMenuItem.Text = "Open file location...";
			this.openFileLocationToolStripMenuItem.ToolTipText = "Open the containing folder in Explorer";
			this.openFileLocationToolStripMenuItem.Click += new System.EventHandler(this.openFileLocationToolStripMenuItem_Click);
			// 
			// shellOpenToolStripMenuItem
			// 
			this.shellOpenToolStripMenuItem.Name = "shellOpenToolStripMenuItem";
			this.shellOpenToolStripMenuItem.Size = new System.Drawing.Size(177, 22);
			this.shellOpenToolStripMenuItem.Text = "Open with Shell32";
			this.shellOpenToolStripMenuItem.ToolTipText = "Open the file using the Windows Shell";
			this.shellOpenToolStripMenuItem.Click += new System.EventHandler(this.shellOpenToolStripMenuItem_Click);
			// 
			// imageList
			// 
			this.imageList.ImageStream = ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("imageList.ImageStream")));
			this.imageList.TransparentColor = System.Drawing.Color.Transparent;
			this.imageList.Images.SetKeyName(0, "sevenZip.png");
			// 
			// fileSystemWatcher
			// 
			this.fileSystemWatcher.EnableRaisingEvents = true;
			this.fileSystemWatcher.Filter = "*.7z";
			this.fileSystemWatcher.NotifyFilter = System.IO.NotifyFilters.FileName;
			this.fileSystemWatcher.SynchronizingObject = this;
			this.fileSystemWatcher.Created += new System.IO.FileSystemEventHandler(this.fileSystemWatcher_AnyChange);
			this.fileSystemWatcher.Deleted += new System.IO.FileSystemEventHandler(this.fileSystemWatcher_AnyChange);
			// 
			// groupBoxSettings
			// 
			this.groupBoxSettings.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxSettings.Controls.Add(this.splitContainer1);
			this.groupBoxSettings.Location = new System.Drawing.Point(12, 12);
			this.groupBoxSettings.MinimumSize = new System.Drawing.Size(235, 0);
			this.groupBoxSettings.Name = "groupBoxSettings";
			this.groupBoxSettings.Size = new System.Drawing.Size(236, 217);
			this.groupBoxSettings.TabIndex = 13;
			this.groupBoxSettings.TabStop = false;
			this.groupBoxSettings.Text = "Settings";
			this.groupBoxSettings.CollapseBoxClickedEvent += new ARCed.Controls.CollapsibleGroupBox.CollapseBoxClickedEventHandler(this.groupBoxSettings_CollapseBoxClickedEvent);
			// 
			// splitContainerWeapons
			// 
			this.splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainer1.Location = new System.Drawing.Point(3, 16);
			this.splitContainer1.Name = "splitContainer1";
			// 
			// splitContainerWeapons.Panel1
			// 
			this.splitContainer1.Panel1.Controls.Add(this.labelMaxBackups);
			this.splitContainer1.Panel1.Controls.Add(this.groupBoxType);
			this.splitContainer1.Panel1.Controls.Add(this.numericInterval);
			this.splitContainer1.Panel1.Controls.Add(this.numericMaxBackups);
			this.splitContainer1.Panel1.Controls.Add(this.labelMinutes);
			// 
			// splitContainerWeapons.Panel2
			// 
			this.splitContainer1.Panel2.Controls.Add(this.groupBoxFrequency);
			this.splitContainer1.Panel2.Controls.Add(this.checkBoxThreaded);
			this.splitContainer1.Size = new System.Drawing.Size(230, 198);
			this.splitContainer1.SplitterDistance = 118;
			this.splitContainer1.TabIndex = 0;
			// 
			// splitContainer2
			// 
			this.splitContainer2.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.splitContainer2.Location = new System.Drawing.Point(12, 235);
			this.splitContainer2.Name = "splitContainer2";
			this.splitContainer2.Orientation = System.Windows.Forms.Orientation.Horizontal;
			// 
			// splitContainer2.Panel1
			// 
			this.splitContainer2.Panel1.Controls.Add(this.listViewARChives);
			// 
			// splitContainer2.Panel2
			// 
			this.splitContainer2.Panel2.Controls.Add(this.buttonRestore);
			this.splitContainer2.Panel2.Controls.Add(this.buttonCreateNew);
			this.splitContainer2.Panel2.Controls.Add(this.buttonRemove);
			this.splitContainer2.Panel2MinSize = 54;
			this.splitContainer2.Size = new System.Drawing.Size(236, 255);
			this.splitContainer2.SplitterDistance = 192;
			this.splitContainer2.TabIndex = 14;
			// 
			// ARChiveForm
			// 
			this.AutoHidePortion = 262D;
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.AutoScroll = true;
			this.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
			this.ClientSize = new System.Drawing.Size(260, 502);
			this.Controls.Add(this.splitContainer2);
			this.Controls.Add(this.groupBoxSettings);
			this.DefaultFloatSize = new System.Drawing.Size(433, 536);
			this.DockAreas = ((ARCed.UI.DockAreas)((((ARCed.UI.DockAreas.Float | ARCed.UI.DockAreas.DockLeft)
						| ARCed.UI.DockAreas.DockRight)
						| ARCed.UI.DockAreas.Document)));
			this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.SizableToolWindow;
			this.MaximizeBox = false;
			this.MinimizeBox = false;
			this.Name = "ARChiveForm";
			this.ShowHint = ARCed.UI.DockState.DockRight;
			this.ShowIcon = false;
			this.ShowInTaskbar = false;
			this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
			this.StartPosition = System.Windows.Forms.FormStartPosition.Manual;
			this.Text = "ARChive Utility";
			this.groupBoxType.ResumeLayout(false);
			this.groupBoxType.PerformLayout();
			this.groupBoxFrequency.ResumeLayout(false);
			this.groupBoxFrequency.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.numericInterval)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.numericMaxBackups)).EndInit();
			this.contextMenuStrip.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.fileSystemWatcher)).EndInit();
			this.groupBoxSettings.ResumeLayout(false);
			this.splitContainer1.Panel1.ResumeLayout(false);
			this.splitContainer1.Panel1.PerformLayout();
			this.splitContainer1.Panel2.ResumeLayout(false);
			this.splitContainer1.Panel2.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).EndInit();
			this.splitContainer1.ResumeLayout(false);
			this.splitContainer2.Panel1.ResumeLayout(false);
			this.splitContainer2.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainer2)).EndInit();
			this.splitContainer2.ResumeLayout(false);
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.GroupBox groupBoxType;
		private System.Windows.Forms.CheckBox checkBoxTypeScripts;
		private System.Windows.Forms.CheckBox checkBoxTypeMaps;
		private System.Windows.Forms.CheckBox checkBoxTypeAllData;
		private System.Windows.Forms.GroupBox groupBoxFrequency;
		private System.Windows.Forms.RadioButton radioButtonInterval;
		private System.Windows.Forms.RadioButton radioButtonSave;
		private System.Windows.Forms.RadioButton radioButtonDebug;
		private System.Windows.Forms.RadioButton radioButtonRun;
		private System.Windows.Forms.RadioButton radioButtonNone;
		private System.Windows.Forms.CheckBox checkBoxThreaded;
		private System.Windows.Forms.Label labelMinutes;
		private System.Windows.Forms.NumericUpDown numericInterval;
		private System.Windows.Forms.ToolTip toolTip;
		private System.Windows.Forms.Label labelMaxBackups;
		private System.Windows.Forms.NumericUpDown numericMaxBackups;
		private System.Windows.Forms.ListView listViewARChives;
		private System.Windows.Forms.Button buttonRemove;
		private System.Windows.Forms.Button buttonCreateNew;
		private System.Windows.Forms.Button buttonRestore;
		private System.Windows.Forms.ColumnHeader columnName;
		private System.Windows.Forms.ColumnHeader columnCreated;
		private System.Windows.Forms.ColumnHeader columnSize;
		private System.Windows.Forms.ImageList imageList;
		private System.IO.FileSystemWatcher fileSystemWatcher;
		private ARCed.Controls.CollapsibleGroupBox groupBoxSettings;
		private System.Windows.Forms.SplitContainer splitContainer1;
		private System.Windows.Forms.SplitContainer splitContainer2;
		private System.Windows.Forms.ContextMenuStrip contextMenuStrip;
		private System.Windows.Forms.ToolStripMenuItem openFileLocationToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem restoreToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem removeToolStripMenuItem;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator2;
		private System.Windows.Forms.ToolStripMenuItem shellOpenToolStripMenuItem;
	}
}