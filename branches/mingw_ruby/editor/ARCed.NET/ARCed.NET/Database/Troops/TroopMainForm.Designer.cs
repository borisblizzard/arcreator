namespace ARCed.Database.Troops
{
    sealed partial class TroopMainForm
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
			this.splitContainerMain = new System.Windows.Forms.SplitContainer();
			this.dataObjectList = new ARCed.Controls.DatabaseObjectListBox();
			this.splitContainerRight = new System.Windows.Forms.SplitContainer();
			this.splitContainerTroop = new System.Windows.Forms.SplitContainer();
			this.groupBoxAlignment = new System.Windows.Forms.GroupBox();
			this.panelXnaParent = new System.Windows.Forms.Panel();
			this.xnaPanel = new ARCed.Controls.TroopXnaPanel();
			this.contextMenuStripMember = new System.Windows.Forms.ContextMenuStrip(this.components);
			this.buttonAppearHalfway = new System.Windows.Forms.ToolStripMenuItem();
			this.buttonImmortal = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
			this.removeToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.groupBoxEnemies = new System.Windows.Forms.GroupBox();
			this.buttonClear = new System.Windows.Forms.Button();
			this.buttonFull = new System.Windows.Forms.Button();
			this.buttonAlignEnemies = new System.Windows.Forms.Button();
			this.listBoxEnemies = new System.Windows.Forms.ListBox();
			this.buttonRemoveEnemy = new System.Windows.Forms.Button();
			this.buttonAddEnemy = new System.Windows.Forms.Button();
			this.buttonAutoname = new System.Windows.Forms.Button();
			this.buttonBattleback = new System.Windows.Forms.Button();
			this.buttonBattleTest = new System.Windows.Forms.Button();
			this.textBoxName = new System.Windows.Forms.TextBox();
			this.labelName = new System.Windows.Forms.Label();
			this.splitContainerBottom = new System.Windows.Forms.SplitContainer();
			this.groupBoxEvents = new System.Windows.Forms.GroupBox();
			this.tabControlEvents = new System.Windows.Forms.TabControl();
			this.buttonClearPage = new System.Windows.Forms.Button();
			this.buttonDeletePage = new System.Windows.Forms.Button();
			this.buttonPastePage = new System.Windows.Forms.Button();
			this.buttonCopyPage = new System.Windows.Forms.Button();
			this.buttonNewPage = new System.Windows.Forms.Button();
			this.noteTextBox = new ARCed.Controls.NoteTextBox();
			this.toolTip = new System.Windows.Forms.ToolTip(this.components);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerMain)).BeginInit();
			this.splitContainerMain.Panel1.SuspendLayout();
			this.splitContainerMain.Panel2.SuspendLayout();
			this.splitContainerMain.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerRight)).BeginInit();
			this.splitContainerRight.Panel1.SuspendLayout();
			this.splitContainerRight.Panel2.SuspendLayout();
			this.splitContainerRight.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerTroop)).BeginInit();
			this.splitContainerTroop.Panel1.SuspendLayout();
			this.splitContainerTroop.Panel2.SuspendLayout();
			this.splitContainerTroop.SuspendLayout();
			this.groupBoxAlignment.SuspendLayout();
			this.panelXnaParent.SuspendLayout();
			this.contextMenuStripMember.SuspendLayout();
			this.groupBoxEnemies.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerBottom)).BeginInit();
			this.splitContainerBottom.Panel1.SuspendLayout();
			this.splitContainerBottom.Panel2.SuspendLayout();
			this.splitContainerBottom.SuspendLayout();
			this.groupBoxEvents.SuspendLayout();
			this.SuspendLayout();
			// 
			// splitContainerMain
			// 
			this.splitContainerMain.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainerMain.Location = new System.Drawing.Point(0, 0);
			this.splitContainerMain.Name = "splitContainerMain";
			// 
			// splitContainerMain.Panel1
			// 
			this.splitContainerMain.Panel1.Controls.Add(this.dataObjectList);
			// 
			// splitContainerMain.Panel2
			// 
			this.splitContainerMain.Panel2.Controls.Add(this.splitContainerRight);
			this.splitContainerMain.Size = new System.Drawing.Size(770, 507);
			this.splitContainerMain.SplitterDistance = 199;
			this.splitContainerMain.TabIndex = 0;
			// 
			// dataObjectList
			// 
			this.dataObjectList.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.dataObjectList.HeaderText = "Troops";
			this.dataObjectList.Location = new System.Drawing.Point(3, 3);
			this.dataObjectList.Name = "dataObjectList";
			this.dataObjectList.SelectedIndex = -1;
			this.dataObjectList.Size = new System.Drawing.Size(193, 501);
			this.dataObjectList.TabIndex = 0;
			this.dataObjectList.TabStop = false;
			this.dataObjectList.OnListBoxIndexChanged += new ARCed.Controls.DatabaseObjectListBox.ObjectListIndexChangedEventHandler(this.DataObjectListOnListBoxIndexChanged);
			// 
			// splitContainerRight
			// 
			this.splitContainerRight.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainerRight.Location = new System.Drawing.Point(0, 0);
			this.splitContainerRight.Name = "splitContainerRight";
			this.splitContainerRight.Orientation = System.Windows.Forms.Orientation.Horizontal;
			// 
			// splitContainerRight.Panel1
			// 
			this.splitContainerRight.Panel1.Controls.Add(this.splitContainerTroop);
			this.splitContainerRight.Panel1.Controls.Add(this.buttonAutoname);
			this.splitContainerRight.Panel1.Controls.Add(this.buttonBattleback);
			this.splitContainerRight.Panel1.Controls.Add(this.buttonBattleTest);
			this.splitContainerRight.Panel1.Controls.Add(this.textBoxName);
			this.splitContainerRight.Panel1.Controls.Add(this.labelName);
			// 
			// splitContainerRight.Panel2
			// 
			this.splitContainerRight.Panel2.Controls.Add(this.splitContainerBottom);
			this.splitContainerRight.Size = new System.Drawing.Size(567, 507);
			this.splitContainerRight.SplitterDistance = 317;
			this.splitContainerRight.TabIndex = 0;
			// 
			// splitContainerTroop
			// 
			this.splitContainerTroop.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.splitContainerTroop.Location = new System.Drawing.Point(6, 51);
			this.splitContainerTroop.Name = "splitContainerTroop";
			// 
			// splitContainerTroop.Panel1
			// 
			this.splitContainerTroop.Panel1.Controls.Add(this.groupBoxAlignment);
			// 
			// splitContainerTroop.Panel2
			// 
			this.splitContainerTroop.Panel2.Controls.Add(this.groupBoxEnemies);
			this.splitContainerTroop.Size = new System.Drawing.Size(558, 263);
			this.splitContainerTroop.SplitterDistance = 375;
			this.splitContainerTroop.TabIndex = 5;
			// 
			// groupBoxAlignment
			// 
			this.groupBoxAlignment.Controls.Add(this.panelXnaParent);
			this.groupBoxAlignment.Dock = System.Windows.Forms.DockStyle.Fill;
			this.groupBoxAlignment.Location = new System.Drawing.Point(0, 0);
			this.groupBoxAlignment.Name = "groupBoxAlignment";
			this.groupBoxAlignment.Size = new System.Drawing.Size(375, 263);
			this.groupBoxAlignment.TabIndex = 0;
			this.groupBoxAlignment.TabStop = false;
			this.groupBoxAlignment.Text = "Troop";
			// 
			// panelXnaParent
			// 
			this.panelXnaParent.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.panelXnaParent.AutoScroll = true;
			this.panelXnaParent.BackColor = System.Drawing.SystemColors.ControlDark;
			this.panelXnaParent.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
			this.panelXnaParent.Controls.Add(this.xnaPanel);
			this.panelXnaParent.Location = new System.Drawing.Point(10, 19);
			this.panelXnaParent.Name = "panelXnaParent";
			this.panelXnaParent.Size = new System.Drawing.Size(359, 238);
			this.panelXnaParent.TabIndex = 0;
			// 
			// xnaPanel
			// 
			this.xnaPanel.AllowDrop = true;
			this.xnaPanel.ContextMenuStrip = this.contextMenuStripMember;
			this.xnaPanel.Location = new System.Drawing.Point(0, 0);
			this.xnaPanel.Name = "xnaPanel";
			this.xnaPanel.Size = new System.Drawing.Size(233, 117);
			this.xnaPanel.TabIndex = 0;
			this.toolTip.SetToolTip(this.xnaPanel, "Set troop placement");
			this.xnaPanel.OnSelectionChanged += new ARCed.Controls.TroopXnaPanel.OnSelectHandler(this.XnaPanelOnSelectionChanged);
			this.xnaPanel.OnTroopChanged += new ARCed.Controls.TroopXnaPanel.TroopChangedHandler(this.XnaPanelOnTroopChanged);
			this.xnaPanel.DragDrop += new System.Windows.Forms.DragEventHandler(this.XnaPanelDragDrop);
			this.xnaPanel.DragEnter += new System.Windows.Forms.DragEventHandler(this.XnaPanelDragEnter);
			// 
			// contextMenuStripMember
			// 
			this.contextMenuStripMember.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.buttonAppearHalfway,
            this.buttonImmortal,
            this.toolStripSeparator1,
            this.removeToolStripMenuItem});
			this.contextMenuStripMember.Name = "contextMenuStripMember";
			this.contextMenuStripMember.Size = new System.Drawing.Size(159, 76);
			this.contextMenuStripMember.Opening += new System.ComponentModel.CancelEventHandler(this.ContextMenuStripMemberOpening);
			// 
			// buttonAppearHalfway
			// 
			this.buttonAppearHalfway.CheckOnClick = true;
			this.buttonAppearHalfway.Name = "buttonAppearHalfway";
			this.buttonAppearHalfway.Size = new System.Drawing.Size(158, 22);
			this.buttonAppearHalfway.Text = "Appear Halfway";
			this.buttonAppearHalfway.CheckedChanged += new System.EventHandler(this.ButtonAppearHalfwayCheckedChanged);
			// 
			// buttonImmortal
			// 
			this.buttonImmortal.CheckOnClick = true;
			this.buttonImmortal.Name = "buttonImmortal";
			this.buttonImmortal.Size = new System.Drawing.Size(158, 22);
			this.buttonImmortal.Text = "Immortal";
			this.buttonImmortal.CheckedChanged += new System.EventHandler(this.ButtonImmortalCheckedChanged);
			// 
			// toolStripSeparator1
			// 
			this.toolStripSeparator1.Name = "toolStripSeparator1";
			this.toolStripSeparator1.Size = new System.Drawing.Size(155, 6);
			// 
			// removeToolStripMenuItem
			// 
			this.removeToolStripMenuItem.Image = global::ARCed.Properties.Resources.Delete;
			this.removeToolStripMenuItem.Name = "removeToolStripMenuItem";
			this.removeToolStripMenuItem.Size = new System.Drawing.Size(158, 22);
			this.removeToolStripMenuItem.Text = "Remove";
			this.removeToolStripMenuItem.Click += new System.EventHandler(this.ButtonRemoveEnemyClick);
			// 
			// groupBoxEnemies
			// 
			this.groupBoxEnemies.Controls.Add(this.buttonClear);
			this.groupBoxEnemies.Controls.Add(this.buttonFull);
			this.groupBoxEnemies.Controls.Add(this.buttonAlignEnemies);
			this.groupBoxEnemies.Controls.Add(this.listBoxEnemies);
			this.groupBoxEnemies.Controls.Add(this.buttonRemoveEnemy);
			this.groupBoxEnemies.Controls.Add(this.buttonAddEnemy);
			this.groupBoxEnemies.Dock = System.Windows.Forms.DockStyle.Fill;
			this.groupBoxEnemies.Location = new System.Drawing.Point(0, 0);
			this.groupBoxEnemies.Name = "groupBoxEnemies";
			this.groupBoxEnemies.Size = new System.Drawing.Size(179, 263);
			this.groupBoxEnemies.TabIndex = 0;
			this.groupBoxEnemies.TabStop = false;
			this.groupBoxEnemies.Text = "Enemies";
			// 
			// buttonClear
			// 
			this.buttonClear.Image = global::ARCed.Properties.Resources.Delete;
			this.buttonClear.Location = new System.Drawing.Point(6, 109);
			this.buttonClear.Name = "buttonClear";
			this.buttonClear.Size = new System.Drawing.Size(24, 24);
			this.buttonClear.TabIndex = 7;
			this.toolTip.SetToolTip(this.buttonClear, "Clear all troop members");
			this.buttonClear.UseVisualStyleBackColor = true;
			this.buttonClear.Click += new System.EventHandler(this.ButtonClearClick);
			// 
			// buttonFull
			// 
			this.buttonFull.Image = global::ARCed.Properties.Resources.Edit;
			this.buttonFull.Location = new System.Drawing.Point(6, 139);
			this.buttonFull.Name = "buttonFull";
			this.buttonFull.Size = new System.Drawing.Size(24, 24);
			this.buttonFull.TabIndex = 6;
			this.toolTip.SetToolTip(this.buttonFull, "Full editor");
			this.buttonFull.UseVisualStyleBackColor = true;
			this.buttonFull.Click += new System.EventHandler(this.ButtonFullClick);
			// 
			// buttonAlignEnemies
			// 
			this.buttonAlignEnemies.Image = global::ARCed.Properties.Resources.Ruler;
			this.buttonAlignEnemies.Location = new System.Drawing.Point(6, 79);
			this.buttonAlignEnemies.Name = "buttonAlignEnemies";
			this.buttonAlignEnemies.Size = new System.Drawing.Size(24, 24);
			this.buttonAlignEnemies.TabIndex = 1;
			this.toolTip.SetToolTip(this.buttonAlignEnemies, "Align troop members in a row");
			this.buttonAlignEnemies.UseVisualStyleBackColor = true;
			this.buttonAlignEnemies.Click += new System.EventHandler(this.ButtonAlignEnemiesClick);
			// 
			// listBoxEnemies
			// 
			this.listBoxEnemies.AllowDrop = true;
			this.listBoxEnemies.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.listBoxEnemies.FormattingEnabled = true;
			this.listBoxEnemies.IntegralHeight = false;
			this.listBoxEnemies.Location = new System.Drawing.Point(36, 19);
			this.listBoxEnemies.Name = "listBoxEnemies";
			this.listBoxEnemies.Size = new System.Drawing.Size(134, 238);
			this.listBoxEnemies.TabIndex = 5;
			this.toolTip.SetToolTip(this.listBoxEnemies, "Select an enemy to add to the troop or drag-drop enemy onto panel");
			this.listBoxEnemies.SelectedIndexChanged += new System.EventHandler(this.ListBoxEnemiesSelectedIndexChanged);
			this.listBoxEnemies.MouseDown += new System.Windows.Forms.MouseEventHandler(this.ListBoxEnemiesMouseDown);
			// 
			// buttonRemoveEnemy
			// 
			this.buttonRemoveEnemy.Enabled = false;
			this.buttonRemoveEnemy.Image = global::ARCed.Properties.Resources.Next;
			this.buttonRemoveEnemy.Location = new System.Drawing.Point(6, 49);
			this.buttonRemoveEnemy.Name = "buttonRemoveEnemy";
			this.buttonRemoveEnemy.Size = new System.Drawing.Size(24, 24);
			this.buttonRemoveEnemy.TabIndex = 2;
			this.toolTip.SetToolTip(this.buttonRemoveEnemy, "Remove selected enemy from troop");
			this.buttonRemoveEnemy.UseVisualStyleBackColor = true;
			this.buttonRemoveEnemy.Click += new System.EventHandler(this.ButtonRemoveEnemyClick);
			// 
			// buttonAddEnemy
			// 
			this.buttonAddEnemy.Enabled = false;
			this.buttonAddEnemy.Image = global::ARCed.Properties.Resources.Previous;
			this.buttonAddEnemy.Location = new System.Drawing.Point(6, 19);
			this.buttonAddEnemy.Name = "buttonAddEnemy";
			this.buttonAddEnemy.Size = new System.Drawing.Size(24, 24);
			this.buttonAddEnemy.TabIndex = 0;
			this.toolTip.SetToolTip(this.buttonAddEnemy, "Add selected enemy to troop");
			this.buttonAddEnemy.UseVisualStyleBackColor = true;
			this.buttonAddEnemy.Click += new System.EventHandler(this.ButtonAddEnemyClick);
			// 
			// buttonAutoname
			// 
			this.buttonAutoname.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonAutoname.Location = new System.Drawing.Point(243, 23);
			this.buttonAutoname.Name = "buttonAutoname";
			this.buttonAutoname.Size = new System.Drawing.Size(103, 23);
			this.buttonAutoname.TabIndex = 4;
			this.buttonAutoname.Text = "Autoname";
			this.toolTip.SetToolTip(this.buttonAutoname, "Generate name for troop automatically");
			this.buttonAutoname.UseVisualStyleBackColor = true;
			this.buttonAutoname.Click += new System.EventHandler(this.ButtonAutonameClick);
			// 
			// buttonBattleback
			// 
			this.buttonBattleback.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonBattleback.Location = new System.Drawing.Point(352, 23);
			this.buttonBattleback.Name = "buttonBattleback";
			this.buttonBattleback.Size = new System.Drawing.Size(103, 23);
			this.buttonBattleback.TabIndex = 3;
			this.buttonBattleback.Text = "Battleback...";
			this.toolTip.SetToolTip(this.buttonBattleback, "Change the sample battleback");
			this.buttonBattleback.UseVisualStyleBackColor = true;
			this.buttonBattleback.Click += new System.EventHandler(this.ButtonBattlebackClick);
			// 
			// buttonBattleTest
			// 
			this.buttonBattleTest.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonBattleTest.Location = new System.Drawing.Point(461, 23);
			this.buttonBattleTest.Name = "buttonBattleTest";
			this.buttonBattleTest.Size = new System.Drawing.Size(103, 23);
			this.buttonBattleTest.TabIndex = 2;
			this.buttonBattleTest.Text = "Battle Test...";
			this.toolTip.SetToolTip(this.buttonBattleTest, "Run a test battle with current troop");
			this.buttonBattleTest.UseVisualStyleBackColor = true;
			this.buttonBattleTest.Click += new System.EventHandler(this.ButtonBattleTestClick);
			// 
			// textBoxName
			// 
			this.textBoxName.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBoxName.Location = new System.Drawing.Point(6, 25);
			this.textBoxName.Name = "textBoxName";
			this.textBoxName.Size = new System.Drawing.Size(231, 20);
			this.textBoxName.TabIndex = 1;
			this.toolTip.SetToolTip(this.textBoxName, "Define name of troop");
			this.textBoxName.TextChanged += new System.EventHandler(this.TextBoxNameTextChanged);
			// 
			// labelName
			// 
			this.labelName.AutoSize = true;
			this.labelName.Location = new System.Drawing.Point(3, 9);
			this.labelName.Name = "labelName";
			this.labelName.Size = new System.Drawing.Size(38, 13);
			this.labelName.TabIndex = 0;
			this.labelName.Text = "Name:";
			// 
			// splitContainerBottom
			// 
			this.splitContainerBottom.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainerBottom.Location = new System.Drawing.Point(0, 0);
			this.splitContainerBottom.Name = "splitContainerBottom";
			// 
			// splitContainerBottom.Panel1
			// 
			this.splitContainerBottom.Panel1.Controls.Add(this.groupBoxEvents);
			// 
			// splitContainerBottom.Panel2
			// 
			this.splitContainerBottom.Panel2.Controls.Add(this.noteTextBox);
			this.splitContainerBottom.Size = new System.Drawing.Size(567, 186);
			this.splitContainerBottom.SplitterDistance = 375;
			this.splitContainerBottom.TabIndex = 0;
			// 
			// groupBoxEvents
			// 
			this.groupBoxEvents.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxEvents.Controls.Add(this.tabControlEvents);
			this.groupBoxEvents.Controls.Add(this.buttonClearPage);
			this.groupBoxEvents.Controls.Add(this.buttonDeletePage);
			this.groupBoxEvents.Controls.Add(this.buttonPastePage);
			this.groupBoxEvents.Controls.Add(this.buttonCopyPage);
			this.groupBoxEvents.Controls.Add(this.buttonNewPage);
			this.groupBoxEvents.Location = new System.Drawing.Point(6, 3);
			this.groupBoxEvents.Name = "groupBoxEvents";
			this.groupBoxEvents.Size = new System.Drawing.Size(366, 180);
			this.groupBoxEvents.TabIndex = 0;
			this.groupBoxEvents.TabStop = false;
			this.groupBoxEvents.Text = "Battle Events";
			// 
			// tabControlEvents
			// 
			this.tabControlEvents.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.tabControlEvents.Location = new System.Drawing.Point(45, 19);
			this.tabControlEvents.Name = "tabControlEvents";
			this.tabControlEvents.SelectedIndex = 0;
			this.tabControlEvents.Size = new System.Drawing.Size(315, 155);
			this.tabControlEvents.TabIndex = 5;
			// 
			// buttonClearPage
			// 
			this.buttonClearPage.Location = new System.Drawing.Point(12, 139);
			this.buttonClearPage.Name = "buttonClearPage";
			this.buttonClearPage.Size = new System.Drawing.Size(24, 24);
			this.buttonClearPage.TabIndex = 4;
			this.buttonClearPage.UseVisualStyleBackColor = true;
			// 
			// buttonDeletePage
			// 
			this.buttonDeletePage.Image = global::ARCed.Properties.Resources.Delete;
			this.buttonDeletePage.Location = new System.Drawing.Point(12, 109);
			this.buttonDeletePage.Name = "buttonDeletePage";
			this.buttonDeletePage.Size = new System.Drawing.Size(24, 24);
			this.buttonDeletePage.TabIndex = 3;
			this.buttonDeletePage.UseVisualStyleBackColor = true;
			// 
			// buttonPastePage
			// 
			this.buttonPastePage.Image = global::ARCed.Properties.Resources.Paste;
			this.buttonPastePage.Location = new System.Drawing.Point(12, 79);
			this.buttonPastePage.Name = "buttonPastePage";
			this.buttonPastePage.Size = new System.Drawing.Size(24, 24);
			this.buttonPastePage.TabIndex = 2;
			this.buttonPastePage.UseVisualStyleBackColor = true;
			// 
			// buttonCopyPage
			// 
			this.buttonCopyPage.Image = global::ARCed.Properties.Resources.Copy;
			this.buttonCopyPage.Location = new System.Drawing.Point(12, 49);
			this.buttonCopyPage.Name = "buttonCopyPage";
			this.buttonCopyPage.Size = new System.Drawing.Size(24, 24);
			this.buttonCopyPage.TabIndex = 1;
			this.buttonCopyPage.UseVisualStyleBackColor = true;
			// 
			// buttonNewPage
			// 
			this.buttonNewPage.Image = global::ARCed.Properties.Resources.NewDocument;
			this.buttonNewPage.Location = new System.Drawing.Point(12, 19);
			this.buttonNewPage.Name = "buttonNewPage";
			this.buttonNewPage.Size = new System.Drawing.Size(24, 24);
			this.buttonNewPage.TabIndex = 0;
			this.buttonNewPage.UseVisualStyleBackColor = true;
			// 
			// noteTextBox
			// 
			this.noteTextBox.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.noteTextBox.Location = new System.Drawing.Point(3, 3);
			this.noteTextBox.Name = "noteTextBox";
			this.noteTextBox.NoteText = "";
			this.noteTextBox.Size = new System.Drawing.Size(182, 180);
			this.noteTextBox.TabIndex = 0;
			// 
			// TroopMainForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(770, 507);
			this.Controls.Add(this.splitContainerMain);
			this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.KeyPreview = true;
			this.Name = "TroopMainForm";
			this.RpgTypeName = "RPG.Troop";
			this.Text = "Troops";
			this.Load += new System.EventHandler(this.TroopMainFormLoad);
			this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.FormKeyDown);
			this.splitContainerMain.Panel1.ResumeLayout(false);
			this.splitContainerMain.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerMain)).EndInit();
			this.splitContainerMain.ResumeLayout(false);
			this.splitContainerRight.Panel1.ResumeLayout(false);
			this.splitContainerRight.Panel1.PerformLayout();
			this.splitContainerRight.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerRight)).EndInit();
			this.splitContainerRight.ResumeLayout(false);
			this.splitContainerTroop.Panel1.ResumeLayout(false);
			this.splitContainerTroop.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerTroop)).EndInit();
			this.splitContainerTroop.ResumeLayout(false);
			this.groupBoxAlignment.ResumeLayout(false);
			this.panelXnaParent.ResumeLayout(false);
			this.contextMenuStripMember.ResumeLayout(false);
			this.groupBoxEnemies.ResumeLayout(false);
			this.splitContainerBottom.Panel1.ResumeLayout(false);
			this.splitContainerBottom.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerBottom)).EndInit();
			this.splitContainerBottom.ResumeLayout(false);
			this.groupBoxEvents.ResumeLayout(false);
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.SplitContainer splitContainerMain;
		private Controls.DatabaseObjectListBox dataObjectList;
		private System.Windows.Forms.SplitContainer splitContainerRight;
		private System.Windows.Forms.Button buttonAutoname;
		private System.Windows.Forms.Button buttonBattleback;
		private System.Windows.Forms.Button buttonBattleTest;
		private System.Windows.Forms.TextBox textBoxName;
		private System.Windows.Forms.Label labelName;
		private System.Windows.Forms.SplitContainer splitContainerTroop;
		private System.Windows.Forms.GroupBox groupBoxAlignment;
		private System.Windows.Forms.GroupBox groupBoxEnemies;
		private System.Windows.Forms.GroupBox groupBoxEvents;
		private System.Windows.Forms.ListBox listBoxEnemies;
		private System.Windows.Forms.Button buttonRemoveEnemy;
		private System.Windows.Forms.Button buttonAlignEnemies;
		private System.Windows.Forms.Button buttonAddEnemy;
		private Controls.TroopXnaPanel xnaPanel;
		private System.Windows.Forms.Panel panelXnaParent;
		private System.Windows.Forms.Button buttonFull;
		private System.Windows.Forms.SplitContainer splitContainerBottom;
		private Controls.NoteTextBox noteTextBox;
		private System.Windows.Forms.TabControl tabControlEvents;
		private System.Windows.Forms.Button buttonClearPage;
		private System.Windows.Forms.Button buttonDeletePage;
		private System.Windows.Forms.Button buttonPastePage;
		private System.Windows.Forms.Button buttonCopyPage;
		private System.Windows.Forms.Button buttonNewPage;
		private System.Windows.Forms.Button buttonClear;
		private System.Windows.Forms.ContextMenuStrip contextMenuStripMember;
		private System.Windows.Forms.ToolStripMenuItem buttonAppearHalfway;
		private System.Windows.Forms.ToolStripMenuItem buttonImmortal;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator1;
		private System.Windows.Forms.ToolStripMenuItem removeToolStripMenuItem;
		private System.Windows.Forms.ToolTip toolTip;
	}
}