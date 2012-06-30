namespace ARCed.Database.Actors
{
	partial class ActorMainForm
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
			this.pictureCharacter = new System.Windows.Forms.PictureBox();
			this.contextMenuImages = new System.Windows.Forms.ContextMenuStrip(this.components);
			this.contextImageNormal = new System.Windows.Forms.ToolStripMenuItem();
			this.contextImageStretch = new System.Windows.Forms.ToolStripMenuItem();
			this.contextImageCenter = new System.Windows.Forms.ToolStripMenuItem();
			this.contextImageZoom = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
			this.changeToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.pictureBattler = new System.Windows.Forms.PictureBox();
			this.groupBoxEquipment = new System.Windows.Forms.GroupBox();
			this.panelEquipment = new System.Windows.Forms.Panel();
			this.groupBoxGeneral = new System.Windows.Forms.GroupBox();
			this.buttonExperience = new System.Windows.Forms.Button();
			this.textBoxExpCurve = new System.Windows.Forms.TextBox();
			this.groupBoxGraphics = new System.Windows.Forms.GroupBox();
			this.tabControlImages = new System.Windows.Forms.TabControl();
			this.tabPageCharacter = new System.Windows.Forms.TabPage();
			this.tabPageBattler = new System.Windows.Forms.TabPage();
			this.labelName = new System.Windows.Forms.Label();
			this.comboClass = new System.Windows.Forms.ComboBox();
			this.textBoxName = new System.Windows.Forms.TextBox();
			this.splitContainerCombos = new System.Windows.Forms.SplitContainer();
			this.numericLevelInit = new System.Windows.Forms.NumericUpDown();
			this.labelLevelInit = new System.Windows.Forms.Label();
			this.numericLevelFinal = new System.Windows.Forms.NumericUpDown();
			this.labelLevelFinal = new System.Windows.Forms.Label();
			this.labelExpCurve = new System.Windows.Forms.Label();
			this.labelClass = new System.Windows.Forms.Label();
			this.noteTextBox = new ARCed.Controls.NoteTextBox();
			this.splitContainerMain = new System.Windows.Forms.SplitContainer();
			this.splitContainerLeft = new System.Windows.Forms.SplitContainer();
			this.dataObjectList = new ARCed.Controls.DatabaseObjectListBox();
			this.splitContainerRight = new System.Windows.Forms.SplitContainer();
			this.groupBoxParameters = new System.Windows.Forms.GroupBox();
			this.tableLayoutPanel = new System.Windows.Forms.TableLayoutPanel();
			this.splitContainerBottomRight = new System.Windows.Forms.SplitContainer();
			((System.ComponentModel.ISupportInitialize)(this.pictureCharacter)).BeginInit();
			this.contextMenuImages.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.pictureBattler)).BeginInit();
			this.groupBoxEquipment.SuspendLayout();
			this.groupBoxGeneral.SuspendLayout();
			this.groupBoxGraphics.SuspendLayout();
			this.tabControlImages.SuspendLayout();
			this.tabPageCharacter.SuspendLayout();
			this.tabPageBattler.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerCombos)).BeginInit();
			this.splitContainerCombos.Panel1.SuspendLayout();
			this.splitContainerCombos.Panel2.SuspendLayout();
			this.splitContainerCombos.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.numericLevelInit)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.numericLevelFinal)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerMain)).BeginInit();
			this.splitContainerMain.Panel1.SuspendLayout();
			this.splitContainerMain.Panel2.SuspendLayout();
			this.splitContainerMain.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerLeft)).BeginInit();
			this.splitContainerLeft.Panel1.SuspendLayout();
			this.splitContainerLeft.Panel2.SuspendLayout();
			this.splitContainerLeft.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerRight)).BeginInit();
			this.splitContainerRight.Panel1.SuspendLayout();
			this.splitContainerRight.Panel2.SuspendLayout();
			this.splitContainerRight.SuspendLayout();
			this.groupBoxParameters.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerBottomRight)).BeginInit();
			this.splitContainerBottomRight.Panel1.SuspendLayout();
			this.splitContainerBottomRight.Panel2.SuspendLayout();
			this.splitContainerBottomRight.SuspendLayout();
			this.SuspendLayout();
			// 
			// pictureCharacter
			// 
			this.pictureCharacter.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
			this.pictureCharacter.ContextMenuStrip = this.contextMenuImages;
			this.pictureCharacter.Dock = System.Windows.Forms.DockStyle.Fill;
			this.pictureCharacter.Location = new System.Drawing.Point(3, 3);
			this.pictureCharacter.Name = "pictureCharacter";
			this.pictureCharacter.Size = new System.Drawing.Size(148, 194);
			this.pictureCharacter.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage;
			this.pictureCharacter.TabIndex = 1;
			this.pictureCharacter.TabStop = false;
			this.pictureCharacter.DoubleClick += new System.EventHandler(this.pictureCharacter_DoubleClick);
			// 
			// contextMenuImages
			// 
			this.contextMenuImages.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.contextImageNormal,
            this.contextImageStretch,
            this.contextImageCenter,
            this.contextImageZoom,
            this.toolStripSeparator1,
            this.changeToolStripMenuItem});
			this.contextMenuImages.Name = "contextMenuImages";
			this.contextMenuImages.Size = new System.Drawing.Size(125, 120);
			this.contextMenuImages.Opening += new System.ComponentModel.CancelEventHandler(this.contextMenuImages_Opening);
			// 
			// contextImageNormal
			// 
			this.contextImageNormal.Name = "contextImageNormal";
			this.contextImageNormal.Size = new System.Drawing.Size(124, 22);
			this.contextImageNormal.Tag = "0";
			this.contextImageNormal.Text = "Normal";
			this.contextImageNormal.Click += new System.EventHandler(this.contextImagesSizeMode_Clicked);
			// 
			// contextImageStretch
			// 
			this.contextImageStretch.Name = "contextImageStretch";
			this.contextImageStretch.Size = new System.Drawing.Size(124, 22);
			this.contextImageStretch.Tag = "1";
			this.contextImageStretch.Text = "Stretch";
			this.contextImageStretch.Click += new System.EventHandler(this.contextImagesSizeMode_Clicked);
			// 
			// contextImageCenter
			// 
			this.contextImageCenter.Name = "contextImageCenter";
			this.contextImageCenter.Size = new System.Drawing.Size(124, 22);
			this.contextImageCenter.Tag = "3";
			this.contextImageCenter.Text = "Center";
			this.contextImageCenter.Click += new System.EventHandler(this.contextImagesSizeMode_Clicked);
			// 
			// contextImageZoom
			// 
			this.contextImageZoom.Name = "contextImageZoom";
			this.contextImageZoom.Size = new System.Drawing.Size(124, 22);
			this.contextImageZoom.Tag = "4";
			this.contextImageZoom.Text = "Zoom";
			this.contextImageZoom.Click += new System.EventHandler(this.contextImagesSizeMode_Clicked);
			// 
			// toolStripSeparator1
			// 
			this.toolStripSeparator1.Name = "toolStripSeparator1";
			this.toolStripSeparator1.Size = new System.Drawing.Size(121, 6);
			// 
			// changeToolStripMenuItem
			// 
			this.changeToolStripMenuItem.Name = "changeToolStripMenuItem";
			this.changeToolStripMenuItem.Size = new System.Drawing.Size(124, 22);
			this.changeToolStripMenuItem.Text = "Change...";
			// 
			// pictureBattler
			// 
			this.pictureBattler.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
			this.pictureBattler.ContextMenuStrip = this.contextMenuImages;
			this.pictureBattler.Dock = System.Windows.Forms.DockStyle.Fill;
			this.pictureBattler.Location = new System.Drawing.Point(3, 3);
			this.pictureBattler.Name = "pictureBattler";
			this.pictureBattler.Size = new System.Drawing.Size(148, 194);
			this.pictureBattler.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage;
			this.pictureBattler.TabIndex = 1;
			this.pictureBattler.TabStop = false;
			this.pictureBattler.DoubleClick += new System.EventHandler(this.pictureBattler_DoubleClick);
			// 
			// groupBoxEquipment
			// 
			this.groupBoxEquipment.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxEquipment.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
			this.groupBoxEquipment.Controls.Add(this.panelEquipment);
			this.groupBoxEquipment.Location = new System.Drawing.Point(3, 3);
			this.groupBoxEquipment.Name = "groupBoxEquipment";
			this.groupBoxEquipment.Size = new System.Drawing.Size(313, 168);
			this.groupBoxEquipment.TabIndex = 0;
			this.groupBoxEquipment.TabStop = false;
			this.groupBoxEquipment.Text = "Equipment";
			// 
			// panelEquipment
			// 
			this.panelEquipment.AutoScroll = true;
			this.panelEquipment.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
			this.panelEquipment.Dock = System.Windows.Forms.DockStyle.Fill;
			this.panelEquipment.Location = new System.Drawing.Point(3, 16);
			this.panelEquipment.Name = "panelEquipment";
			this.panelEquipment.Size = new System.Drawing.Size(307, 149);
			this.panelEquipment.TabIndex = 0;
			// 
			// groupBoxGeneral
			// 
			this.groupBoxGeneral.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxGeneral.Controls.Add(this.buttonExperience);
			this.groupBoxGeneral.Controls.Add(this.textBoxExpCurve);
			this.groupBoxGeneral.Controls.Add(this.groupBoxGraphics);
			this.groupBoxGeneral.Controls.Add(this.labelName);
			this.groupBoxGeneral.Controls.Add(this.comboClass);
			this.groupBoxGeneral.Controls.Add(this.textBoxName);
			this.groupBoxGeneral.Controls.Add(this.splitContainerCombos);
			this.groupBoxGeneral.Controls.Add(this.labelExpCurve);
			this.groupBoxGeneral.Controls.Add(this.labelClass);
			this.groupBoxGeneral.Location = new System.Drawing.Point(3, 3);
			this.groupBoxGeneral.Name = "groupBoxGeneral";
			this.groupBoxGeneral.Size = new System.Drawing.Size(186, 452);
			this.groupBoxGeneral.TabIndex = 0;
			this.groupBoxGeneral.TabStop = false;
			this.groupBoxGeneral.Text = "General";
			// 
			// buttonExperience
			// 
			this.buttonExperience.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonExperience.BackgroundImage = global::ARCed.Properties.Resources.Settings2;
			this.buttonExperience.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
			this.buttonExperience.Location = new System.Drawing.Point(150, 169);
			this.buttonExperience.Name = "buttonExperience";
			this.buttonExperience.Size = new System.Drawing.Size(24, 24);
			this.buttonExperience.TabIndex = 22;
			this.buttonExperience.UseVisualStyleBackColor = true;
			this.buttonExperience.Click += new System.EventHandler(this.buttonExperience_Click);
			// 
			// textBoxExpCurve
			// 
			this.textBoxExpCurve.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBoxExpCurve.BackColor = System.Drawing.SystemColors.Window;
			this.textBoxExpCurve.Location = new System.Drawing.Point(9, 172);
			this.textBoxExpCurve.Name = "textBoxExpCurve";
			this.textBoxExpCurve.ReadOnly = true;
			this.textBoxExpCurve.Size = new System.Drawing.Size(135, 20);
			this.textBoxExpCurve.TabIndex = 21;
			// 
			// groupBoxGraphics
			// 
			this.groupBoxGraphics.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxGraphics.Controls.Add(this.tabControlImages);
			this.groupBoxGraphics.Location = new System.Drawing.Point(9, 198);
			this.groupBoxGraphics.Name = "groupBoxGraphics";
			this.groupBoxGraphics.Size = new System.Drawing.Size(168, 248);
			this.groupBoxGraphics.TabIndex = 0;
			this.groupBoxGraphics.TabStop = false;
			this.groupBoxGraphics.Text = "Graphics";
			// 
			// tabControlImages
			// 
			this.tabControlImages.Appearance = System.Windows.Forms.TabAppearance.Buttons;
			this.tabControlImages.Controls.Add(this.tabPageCharacter);
			this.tabControlImages.Controls.Add(this.tabPageBattler);
			this.tabControlImages.Dock = System.Windows.Forms.DockStyle.Fill;
			this.tabControlImages.Location = new System.Drawing.Point(3, 16);
			this.tabControlImages.Name = "tabControlImages";
			this.tabControlImages.SelectedIndex = 0;
			this.tabControlImages.Size = new System.Drawing.Size(162, 229);
			this.tabControlImages.SizeMode = System.Windows.Forms.TabSizeMode.FillToRight;
			this.tabControlImages.TabIndex = 0;
			// 
			// tabPageCharacter
			// 
			this.tabPageCharacter.BackColor = System.Drawing.SystemColors.Control;
			this.tabPageCharacter.Controls.Add(this.pictureCharacter);
			this.tabPageCharacter.Location = new System.Drawing.Point(4, 25);
			this.tabPageCharacter.Name = "tabPageCharacter";
			this.tabPageCharacter.Padding = new System.Windows.Forms.Padding(3);
			this.tabPageCharacter.Size = new System.Drawing.Size(154, 200);
			this.tabPageCharacter.TabIndex = 0;
			this.tabPageCharacter.Text = "Character";
			// 
			// tabPageBattler
			// 
			this.tabPageBattler.Controls.Add(this.pictureBattler);
			this.tabPageBattler.Location = new System.Drawing.Point(4, 25);
			this.tabPageBattler.Name = "tabPageBattler";
			this.tabPageBattler.Padding = new System.Windows.Forms.Padding(3);
			this.tabPageBattler.Size = new System.Drawing.Size(154, 200);
			this.tabPageBattler.TabIndex = 1;
			this.tabPageBattler.Text = "Battler";
			this.tabPageBattler.UseVisualStyleBackColor = true;
			// 
			// labelName
			// 
			this.labelName.AutoSize = true;
			this.labelName.Location = new System.Drawing.Point(6, 19);
			this.labelName.Name = "labelName";
			this.labelName.Size = new System.Drawing.Size(38, 13);
			this.labelName.TabIndex = 14;
			this.labelName.Text = "Name:";
			// 
			// comboClass
			// 
			this.comboClass.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboClass.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboClass.FormattingEnabled = true;
			this.comboClass.Location = new System.Drawing.Point(9, 80);
			this.comboClass.Name = "comboClass";
			this.comboClass.Size = new System.Drawing.Size(168, 21);
			this.comboClass.TabIndex = 17;
			this.comboClass.SelectedIndexChanged += new System.EventHandler(this.comboClass_SelectedIndexChanged);
			// 
			// textBoxName
			// 
			this.textBoxName.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBoxName.Location = new System.Drawing.Point(9, 35);
			this.textBoxName.Name = "textBoxName";
			this.textBoxName.Size = new System.Drawing.Size(168, 20);
			this.textBoxName.TabIndex = 15;
			this.textBoxName.TextChanged += new System.EventHandler(this.textBoxName_TextChanged);
			// 
			// splitContainerCombos
			// 
			this.splitContainerCombos.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.splitContainerCombos.Location = new System.Drawing.Point(9, 109);
			this.splitContainerCombos.Name = "splitContainerCombos";
			// 
			// splitContainerCombos.Panel1
			// 
			this.splitContainerCombos.Panel1.Controls.Add(this.numericLevelInit);
			this.splitContainerCombos.Panel1.Controls.Add(this.labelLevelInit);
			// 
			// splitContainerCombos.Panel2
			// 
			this.splitContainerCombos.Panel2.Controls.Add(this.numericLevelFinal);
			this.splitContainerCombos.Panel2.Controls.Add(this.labelLevelFinal);
			this.splitContainerCombos.Size = new System.Drawing.Size(168, 39);
			this.splitContainerCombos.SplitterDistance = 80;
			this.splitContainerCombos.TabIndex = 18;
			// 
			// numericLevelInit
			// 
			this.numericLevelInit.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.numericLevelInit.Location = new System.Drawing.Point(0, 16);
			this.numericLevelInit.Name = "numericLevelInit";
			this.numericLevelInit.Size = new System.Drawing.Size(74, 20);
			this.numericLevelInit.TabIndex = 1;
			this.numericLevelInit.ValueChanged += new System.EventHandler(this.numericLevelInit_ValueChanged);
			// 
			// labelLevelInit
			// 
			this.labelLevelInit.AutoSize = true;
			this.labelLevelInit.Location = new System.Drawing.Point(-3, 0);
			this.labelLevelInit.Name = "labelLevelInit";
			this.labelLevelInit.Size = new System.Drawing.Size(63, 13);
			this.labelLevelInit.TabIndex = 0;
			this.labelLevelInit.Text = "Initial Level:";
			// 
			// numericLevelFinal
			// 
			this.numericLevelFinal.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.numericLevelFinal.Location = new System.Drawing.Point(3, 16);
			this.numericLevelFinal.Maximum = new decimal(new int[] {
            999,
            0,
            0,
            0});
			this.numericLevelFinal.Name = "numericLevelFinal";
			this.numericLevelFinal.Size = new System.Drawing.Size(78, 20);
			this.numericLevelFinal.TabIndex = 1;
			this.numericLevelFinal.ValueChanged += new System.EventHandler(this.numericLevelFinal_ValueChanged);
			// 
			// labelLevelFinal
			// 
			this.labelLevelFinal.AutoSize = true;
			this.labelLevelFinal.Location = new System.Drawing.Point(0, 0);
			this.labelLevelFinal.Name = "labelLevelFinal";
			this.labelLevelFinal.Size = new System.Drawing.Size(61, 13);
			this.labelLevelFinal.TabIndex = 0;
			this.labelLevelFinal.Text = "Final Level:";
			// 
			// labelExpCurve
			// 
			this.labelExpCurve.AutoSize = true;
			this.labelExpCurve.Location = new System.Drawing.Point(6, 155);
			this.labelExpCurve.Name = "labelExpCurve";
			this.labelExpCurve.Size = new System.Drawing.Size(94, 13);
			this.labelExpCurve.TabIndex = 19;
			this.labelExpCurve.Text = "Experience Curve:";
			// 
			// labelClass
			// 
			this.labelClass.AutoSize = true;
			this.labelClass.Location = new System.Drawing.Point(6, 64);
			this.labelClass.Name = "labelClass";
			this.labelClass.Size = new System.Drawing.Size(35, 13);
			this.labelClass.TabIndex = 16;
			this.labelClass.Text = "Class:";
			// 
			// noteTextBox
			// 
			this.noteTextBox.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.noteTextBox.Location = new System.Drawing.Point(3, 3);
			this.noteTextBox.Name = "noteTextBox";
			this.noteTextBox.NoteText = "";
			this.noteTextBox.Size = new System.Drawing.Size(111, 168);
			this.noteTextBox.TabIndex = 21;
			// 
			// splitContainerMain
			// 
			this.splitContainerMain.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainerMain.Location = new System.Drawing.Point(0, 0);
			this.splitContainerMain.Name = "splitContainerMain";
			// 
			// splitContainerMain.Panel1
			// 
			this.splitContainerMain.Panel1.Controls.Add(this.splitContainerLeft);
			// 
			// splitContainerMain.Panel2
			// 
			this.splitContainerMain.Panel2.Controls.Add(this.splitContainerRight);
			this.splitContainerMain.Size = new System.Drawing.Size(810, 461);
			this.splitContainerMain.SplitterDistance = 367;
			this.splitContainerMain.TabIndex = 12;
			// 
			// splitContainerLeft
			// 
			this.splitContainerLeft.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainerLeft.Location = new System.Drawing.Point(0, 0);
			this.splitContainerLeft.Name = "splitContainerLeft";
			// 
			// splitContainerLeft.Panel1
			// 
			this.splitContainerLeft.Panel1.Controls.Add(this.dataObjectList);
			// 
			// splitContainerLeft.Panel2
			// 
			this.splitContainerLeft.Panel2.Controls.Add(this.groupBoxGeneral);
			this.splitContainerLeft.Size = new System.Drawing.Size(367, 461);
			this.splitContainerLeft.SplitterDistance = 171;
			this.splitContainerLeft.TabIndex = 0;
			// 
			// dataObjectList
			// 
			this.dataObjectList.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.dataObjectList.HeaderText = "Actors";
			this.dataObjectList.Location = new System.Drawing.Point(3, 3);
			this.dataObjectList.Name = "dataObjectList";
			this.dataObjectList.SelectedIndex = -1;
			this.dataObjectList.Size = new System.Drawing.Size(165, 452);
			this.dataObjectList.TabIndex = 0;
			this.dataObjectList.TabStop = false;
			this.dataObjectList.OnListBoxIndexChanged += new ARCed.Controls.DatabaseObjectListBox.ObjectListIndexChangedEventHandler(this.listBoxActors_SelectedIndexChanged);
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
			this.splitContainerRight.Panel1.Controls.Add(this.groupBoxParameters);
			// 
			// splitContainerRight.Panel2
			// 
			this.splitContainerRight.Panel2.Controls.Add(this.splitContainerBottomRight);
			this.splitContainerRight.Size = new System.Drawing.Size(439, 461);
			this.splitContainerRight.SplitterDistance = 280;
			this.splitContainerRight.TabIndex = 0;
			// 
			// groupBoxParameters
			// 
			this.groupBoxParameters.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxParameters.Controls.Add(this.tableLayoutPanel);
			this.groupBoxParameters.Location = new System.Drawing.Point(3, 3);
			this.groupBoxParameters.Name = "groupBoxParameters";
			this.groupBoxParameters.Size = new System.Drawing.Size(433, 274);
			this.groupBoxParameters.TabIndex = 0;
			this.groupBoxParameters.TabStop = false;
			this.groupBoxParameters.Text = "Parameters";
			// 
			// tableLayoutPanel
			// 
			this.tableLayoutPanel.ColumnCount = 2;
			this.tableLayoutPanel.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
			this.tableLayoutPanel.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
			this.tableLayoutPanel.Dock = System.Windows.Forms.DockStyle.Fill;
			this.tableLayoutPanel.Location = new System.Drawing.Point(3, 16);
			this.tableLayoutPanel.Name = "tableLayoutPanel";
			this.tableLayoutPanel.RowCount = 3;
			this.tableLayoutPanel.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 33.33333F));
			this.tableLayoutPanel.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 33.33333F));
			this.tableLayoutPanel.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 33.33333F));
			this.tableLayoutPanel.Size = new System.Drawing.Size(427, 255);
			this.tableLayoutPanel.TabIndex = 0;
			// 
			// splitContainerBottomRight
			// 
			this.splitContainerBottomRight.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainerBottomRight.Location = new System.Drawing.Point(0, 0);
			this.splitContainerBottomRight.Name = "splitContainerBottomRight";
			// 
			// splitContainerBottomRight.Panel1
			// 
			this.splitContainerBottomRight.Panel1.Controls.Add(this.groupBoxEquipment);
			// 
			// splitContainerBottomRight.Panel2
			// 
			this.splitContainerBottomRight.Panel2.Controls.Add(this.noteTextBox);
			this.splitContainerBottomRight.Size = new System.Drawing.Size(439, 177);
			this.splitContainerBottomRight.SplitterDistance = 315;
			this.splitContainerBottomRight.TabIndex = 0;
			// 
			// ActorMainForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(810, 461);
			this.Controls.Add(this.splitContainerMain);
			this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.Name = "ActorMainForm";
			this.RpgTypeName = "RPG.Actor";
			this.Text = "Actors";
			((System.ComponentModel.ISupportInitialize)(this.pictureCharacter)).EndInit();
			this.contextMenuImages.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.pictureBattler)).EndInit();
			this.groupBoxEquipment.ResumeLayout(false);
			this.groupBoxGeneral.ResumeLayout(false);
			this.groupBoxGeneral.PerformLayout();
			this.groupBoxGraphics.ResumeLayout(false);
			this.tabControlImages.ResumeLayout(false);
			this.tabPageCharacter.ResumeLayout(false);
			this.tabPageBattler.ResumeLayout(false);
			this.splitContainerCombos.Panel1.ResumeLayout(false);
			this.splitContainerCombos.Panel1.PerformLayout();
			this.splitContainerCombos.Panel2.ResumeLayout(false);
			this.splitContainerCombos.Panel2.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerCombos)).EndInit();
			this.splitContainerCombos.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.numericLevelInit)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.numericLevelFinal)).EndInit();
			this.splitContainerMain.Panel1.ResumeLayout(false);
			this.splitContainerMain.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerMain)).EndInit();
			this.splitContainerMain.ResumeLayout(false);
			this.splitContainerLeft.Panel1.ResumeLayout(false);
			this.splitContainerLeft.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerLeft)).EndInit();
			this.splitContainerLeft.ResumeLayout(false);
			this.splitContainerRight.Panel1.ResumeLayout(false);
			this.splitContainerRight.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerRight)).EndInit();
			this.splitContainerRight.ResumeLayout(false);
			this.groupBoxParameters.ResumeLayout(false);
			this.splitContainerBottomRight.Panel1.ResumeLayout(false);
			this.splitContainerBottomRight.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerBottomRight)).EndInit();
			this.splitContainerBottomRight.ResumeLayout(false);
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.PictureBox pictureCharacter;
		private System.Windows.Forms.PictureBox pictureBattler;
		private System.Windows.Forms.GroupBox groupBoxEquipment;
		private System.Windows.Forms.GroupBox groupBoxGeneral;
		private System.Windows.Forms.Label labelName;
		private System.Windows.Forms.ComboBox comboClass;
		private System.Windows.Forms.TextBox textBoxName;
		private System.Windows.Forms.SplitContainer splitContainerCombos;
		private System.Windows.Forms.NumericUpDown numericLevelInit;
		private System.Windows.Forms.Label labelLevelInit;
		private System.Windows.Forms.NumericUpDown numericLevelFinal;
		private System.Windows.Forms.Label labelLevelFinal;
		private System.Windows.Forms.Label labelExpCurve;
		private System.Windows.Forms.Label labelClass;
		private System.Windows.Forms.ContextMenuStrip contextMenuImages;
		private System.Windows.Forms.ToolStripMenuItem contextImageNormal;
		private System.Windows.Forms.ToolStripMenuItem contextImageStretch;
		private System.Windows.Forms.ToolStripMenuItem contextImageCenter;
		private System.Windows.Forms.ToolStripMenuItem contextImageZoom;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator1;
		private System.Windows.Forms.ToolStripMenuItem changeToolStripMenuItem;
		private System.Windows.Forms.SplitContainer splitContainerMain;
		private System.Windows.Forms.SplitContainer splitContainerLeft;
		private Controls.NoteTextBox noteTextBox;
		private System.Windows.Forms.GroupBox groupBoxGraphics;
		private System.Windows.Forms.TabControl tabControlImages;
		private System.Windows.Forms.TabPage tabPageCharacter;
		private System.Windows.Forms.TabPage tabPageBattler;
		private System.Windows.Forms.Button buttonExperience;
		private System.Windows.Forms.TextBox textBoxExpCurve;
		private System.Windows.Forms.SplitContainer splitContainerRight;
		private System.Windows.Forms.SplitContainer splitContainerBottomRight;
		private System.Windows.Forms.GroupBox groupBoxParameters;
		private System.Windows.Forms.TableLayoutPanel tableLayoutPanel;
		private Controls.DatabaseObjectListBox dataObjectList;
		private System.Windows.Forms.Panel panelEquipment;

	}
}