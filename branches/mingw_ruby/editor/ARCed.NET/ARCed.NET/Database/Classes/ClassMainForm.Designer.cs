namespace ARCed.Database.Classes
{
    sealed partial class ClassMainForm
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
			this.splitContainerLeft = new System.Windows.Forms.SplitContainer();
			this.dataObjectList = new ARCed.Controls.DatabaseObjectListBox();
			this.checkGroupWeapons = new ARCed.Controls.CheckGroupBox(this.components);
			this.textBoxName = new System.Windows.Forms.TextBox();
			this.labelName = new System.Windows.Forms.Label();
			this.splitContainerRight = new System.Windows.Forms.SplitContainer();
			this.checkGroupArmor = new ARCed.Controls.CheckGroupBox(this.components);
			this.comboBoxPosition = new System.Windows.Forms.ComboBox();
			this.labelPosition = new System.Windows.Forms.Label();
			this.splitContainerFarRight = new System.Windows.Forms.SplitContainer();
			this.splitContainerEfficiency = new System.Windows.Forms.SplitContainer();
			this.checkedListElements = new ARCed.Controls.MultiStateCheckedListBox();
			this.checkedListStates = new ARCed.Controls.MultiStateCheckedListBox();
			this.splitContainerSkillNotes = new System.Windows.Forms.SplitContainer();
			this.groupBoxSkills = new System.Windows.Forms.GroupBox();
			this.buttonEditSkill = new System.Windows.Forms.Button();
			this.buttonRemoveSkill = new System.Windows.Forms.Button();
			this.buttonAddSkill = new System.Windows.Forms.Button();
			this.listViewSkills = new System.Windows.Forms.ListView();
			this.columnLevel = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
			this.columnId = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
			this.columnSkill = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
			this.contextMenuSkills = new System.Windows.Forms.ContextMenuStrip(this.components);
			this.contextButtonSkillEdit = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
			this.contextButtonSkillAdd = new System.Windows.Forms.ToolStripMenuItem();
			this.contextButtonSkillRemove = new System.Windows.Forms.ToolStripMenuItem();
			this.noteTextBox = new ARCed.Controls.NoteTextBox();
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
			((System.ComponentModel.ISupportInitialize)(this.splitContainerFarRight)).BeginInit();
			this.splitContainerFarRight.Panel1.SuspendLayout();
			this.splitContainerFarRight.Panel2.SuspendLayout();
			this.splitContainerFarRight.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerEfficiency)).BeginInit();
			this.splitContainerEfficiency.Panel1.SuspendLayout();
			this.splitContainerEfficiency.Panel2.SuspendLayout();
			this.splitContainerEfficiency.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerSkillNotes)).BeginInit();
			this.splitContainerSkillNotes.Panel1.SuspendLayout();
			this.splitContainerSkillNotes.Panel2.SuspendLayout();
			this.splitContainerSkillNotes.SuspendLayout();
			this.groupBoxSkills.SuspendLayout();
			this.contextMenuSkills.SuspendLayout();
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
			this.splitContainerMain.Panel1.Controls.Add(this.splitContainerLeft);
			// 
			// splitContainerMain.Panel2
			// 
			this.splitContainerMain.Panel2.Controls.Add(this.splitContainerRight);
			this.splitContainerMain.Size = new System.Drawing.Size(755, 454);
			this.splitContainerMain.SplitterDistance = 317;
			this.splitContainerMain.TabIndex = 0;
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
			this.splitContainerLeft.Panel2.Controls.Add(this.checkGroupWeapons);
			this.splitContainerLeft.Panel2.Controls.Add(this.textBoxName);
			this.splitContainerLeft.Panel2.Controls.Add(this.labelName);
			this.splitContainerLeft.Size = new System.Drawing.Size(317, 454);
			this.splitContainerLeft.SplitterDistance = 162;
			this.splitContainerLeft.TabIndex = 0;
			// 
			// dataObjectList
			// 
			this.dataObjectList.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.dataObjectList.HeaderText = "Classes";
			this.dataObjectList.Location = new System.Drawing.Point(3, 5);
			this.dataObjectList.Name = "dataObjectList";
			this.dataObjectList.SelectedIndex = -1;
			this.dataObjectList.Size = new System.Drawing.Size(156, 443);
			this.dataObjectList.TabIndex = 0;
			this.dataObjectList.TabStop = false;
			this.dataObjectList.OnListBoxIndexChanged += new ARCed.Controls.DatabaseObjectListBox.ObjectListIndexChangedEventHandler(this.ListBoxClassesSelectedIndexChanged);
			// 
			// checkGroupWeapons
			// 
			this.checkGroupWeapons.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.checkGroupWeapons.Location = new System.Drawing.Point(6, 51);
			this.checkGroupWeapons.Name = "checkGroupWeapons";
			this.checkGroupWeapons.SelectedIndex = -1;
			this.checkGroupWeapons.Size = new System.Drawing.Size(142, 397);
			this.checkGroupWeapons.TabIndex = 2;
			this.checkGroupWeapons.TabStop = false;
			this.checkGroupWeapons.Text = "Weapons";
			this.checkGroupWeapons.OnCheckChange += new ARCed.Controls.CheckGroupBox.CheckChangeEventHandler(this.CheckGroupWeaponsOnCheckChange);
			this.checkGroupWeapons.Leave += new System.EventHandler(this.CheckGroupFocusLeave);
			// 
			// textBoxName
			// 
			this.textBoxName.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBoxName.Location = new System.Drawing.Point(6, 25);
			this.textBoxName.Name = "textBoxName";
			this.textBoxName.Size = new System.Drawing.Size(142, 20);
			this.textBoxName.TabIndex = 1;
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
			// splitContainerRight
			// 
			this.splitContainerRight.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainerRight.Location = new System.Drawing.Point(0, 0);
			this.splitContainerRight.Name = "splitContainerRight";
			// 
			// splitContainerRight.Panel1
			// 
			this.splitContainerRight.Panel1.Controls.Add(this.checkGroupArmor);
			this.splitContainerRight.Panel1.Controls.Add(this.comboBoxPosition);
			this.splitContainerRight.Panel1.Controls.Add(this.labelPosition);
			// 
			// splitContainerRight.Panel2
			// 
			this.splitContainerRight.Panel2.Controls.Add(this.splitContainerFarRight);
			this.splitContainerRight.Size = new System.Drawing.Size(434, 454);
			this.splitContainerRight.SplitterDistance = 154;
			this.splitContainerRight.TabIndex = 0;
			// 
			// checkGroupArmor
			// 
			this.checkGroupArmor.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.checkGroupArmor.Location = new System.Drawing.Point(6, 52);
			this.checkGroupArmor.Name = "checkGroupArmor";
			this.checkGroupArmor.SelectedIndex = -1;
			this.checkGroupArmor.Size = new System.Drawing.Size(145, 396);
			this.checkGroupArmor.TabIndex = 2;
			this.checkGroupArmor.TabStop = false;
			this.checkGroupArmor.Text = "Armors";
			this.checkGroupArmor.OnCheckChange += new ARCed.Controls.CheckGroupBox.CheckChangeEventHandler(this.CheckGroupArmorOnCheckChange);
			this.checkGroupArmor.Leave += new System.EventHandler(this.CheckGroupFocusLeave);
			// 
			// comboBoxPosition
			// 
			this.comboBoxPosition.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxPosition.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxPosition.FormattingEnabled = true;
			this.comboBoxPosition.Items.AddRange(new object[] {
            "Front",
            "Middle",
            "Back"});
			this.comboBoxPosition.Location = new System.Drawing.Point(6, 25);
			this.comboBoxPosition.Name = "comboBoxPosition";
			this.comboBoxPosition.Size = new System.Drawing.Size(145, 21);
			this.comboBoxPosition.TabIndex = 1;
			this.comboBoxPosition.SelectedIndexChanged += new System.EventHandler(this.ComboBoxPositionSelectedIndexChanged);
			// 
			// labelPosition
			// 
			this.labelPosition.AutoSize = true;
			this.labelPosition.Location = new System.Drawing.Point(3, 9);
			this.labelPosition.Name = "labelPosition";
			this.labelPosition.Size = new System.Drawing.Size(47, 13);
			this.labelPosition.TabIndex = 0;
			this.labelPosition.Text = "Position:";
			// 
			// splitContainerFarRight
			// 
			this.splitContainerFarRight.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainerFarRight.Location = new System.Drawing.Point(0, 0);
			this.splitContainerFarRight.Name = "splitContainerFarRight";
			this.splitContainerFarRight.Orientation = System.Windows.Forms.Orientation.Horizontal;
			// 
			// splitContainerFarRight.Panel1
			// 
			this.splitContainerFarRight.Panel1.Controls.Add(this.splitContainerEfficiency);
			// 
			// splitContainerFarRight.Panel2
			// 
			this.splitContainerFarRight.Panel2.Controls.Add(this.splitContainerSkillNotes);
			this.splitContainerFarRight.Size = new System.Drawing.Size(276, 454);
			this.splitContainerFarRight.SplitterDistance = 157;
			this.splitContainerFarRight.TabIndex = 0;
			// 
			// splitContainerEfficiency
			// 
			this.splitContainerEfficiency.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainerEfficiency.Location = new System.Drawing.Point(0, 0);
			this.splitContainerEfficiency.Name = "splitContainerEfficiency";
			// 
			// splitContainerEfficiency.Panel1
			// 
			this.splitContainerEfficiency.Panel1.Controls.Add(this.checkedListElements);
			// 
			// splitContainerEfficiency.Panel2
			// 
			this.splitContainerEfficiency.Panel2.Controls.Add(this.checkedListStates);
			this.splitContainerEfficiency.Size = new System.Drawing.Size(276, 157);
			this.splitContainerEfficiency.SplitterDistance = 132;
			this.splitContainerEfficiency.TabIndex = 0;
			// 
			// checkedListElements
			// 
			this.checkedListElements.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.checkedListElements.Colors = new System.Drawing.Color[] {
        System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(0)))), ((int)(((byte)(0))))),
        System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(128)))), ((int)(((byte)(0))))),
        System.Drawing.Color.Gray,
        System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(192)))), ((int)(((byte)(0))))),
        System.Drawing.Color.Blue,
        System.Drawing.Color.Purple};
			this.checkedListElements.Items = new string[] {
        "A",
        "B",
        "C",
        "D",
        "E",
        "F"};
			this.checkedListElements.Location = new System.Drawing.Point(3, 9);
			this.checkedListElements.Name = "efficiencyElements";
			this.checkedListElements.Size = new System.Drawing.Size(126, 142);
			this.checkedListElements.TabIndex = 0;
			this.checkedListElements.TabStop = false;
			this.checkedListElements.Text = "Element Efficiency";
			this.checkedListElements.OnItemChanged += new ARCed.Controls.MultiStateCheckedListBox.ItemValueChangedEventHandler(this.EfficiencyElementsOnItemChanged);
			// 
			// checkedListStates
			// 
			this.checkedListStates.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.checkedListStates.Colors = new System.Drawing.Color[] {
        System.Drawing.Color.Maroon,
        System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(128)))), ((int)(((byte)(0))))),
        System.Drawing.Color.Gray,
        System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(192)))), ((int)(((byte)(0))))),
        System.Drawing.Color.Blue,
        System.Drawing.Color.Purple};
			this.checkedListStates.Items = new string[] {
        "A",
        "B",
        "C",
        "D",
        "E",
        "F"};
			this.checkedListStates.Location = new System.Drawing.Point(3, 9);
			this.checkedListStates.Name = "efficiencyStates";
			this.checkedListStates.Size = new System.Drawing.Size(134, 142);
			this.checkedListStates.TabIndex = 0;
			this.checkedListStates.TabStop = false;
			this.checkedListStates.Text = "State Efficiency";
			this.checkedListStates.OnItemChanged += new ARCed.Controls.MultiStateCheckedListBox.ItemValueChangedEventHandler(this.EfficiencyStatesOnItemChanged);
			// 
			// splitContainerSkillNotes
			// 
			this.splitContainerSkillNotes.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainerSkillNotes.Location = new System.Drawing.Point(0, 0);
			this.splitContainerSkillNotes.Name = "splitContainerSkillNotes";
			this.splitContainerSkillNotes.Orientation = System.Windows.Forms.Orientation.Horizontal;
			// 
			// splitContainerSkillNotes.Panel1
			// 
			this.splitContainerSkillNotes.Panel1.Controls.Add(this.groupBoxSkills);
			// 
			// splitContainerSkillNotes.Panel2
			// 
			this.splitContainerSkillNotes.Panel2.Controls.Add(this.noteTextBox);
			this.splitContainerSkillNotes.Size = new System.Drawing.Size(276, 293);
			this.splitContainerSkillNotes.SplitterDistance = 160;
			this.splitContainerSkillNotes.TabIndex = 0;
			// 
			// groupBoxSkills
			// 
			this.groupBoxSkills.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxSkills.Controls.Add(this.buttonEditSkill);
			this.groupBoxSkills.Controls.Add(this.buttonRemoveSkill);
			this.groupBoxSkills.Controls.Add(this.buttonAddSkill);
			this.groupBoxSkills.Controls.Add(this.listViewSkills);
			this.groupBoxSkills.Location = new System.Drawing.Point(3, 3);
			this.groupBoxSkills.Name = "groupBoxSkills";
			this.groupBoxSkills.Size = new System.Drawing.Size(270, 158);
			this.groupBoxSkills.TabIndex = 0;
			this.groupBoxSkills.TabStop = false;
			this.groupBoxSkills.Text = "Skills";
			// 
			// buttonEditSkill
			// 
			this.buttonEditSkill.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonEditSkill.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
			this.buttonEditSkill.Enabled = false;
			this.buttonEditSkill.Image = global::ARCed.Properties.Resources.Edit;
			this.buttonEditSkill.Location = new System.Drawing.Point(240, 79);
			this.buttonEditSkill.Name = "buttonEditSkill";
			this.buttonEditSkill.Size = new System.Drawing.Size(24, 24);
			this.buttonEditSkill.TabIndex = 3;
			this.buttonEditSkill.UseVisualStyleBackColor = true;
			this.buttonEditSkill.Click += new System.EventHandler(this.ButtonEditSkillClick);
			// 
			// buttonRemoveSkill
			// 
			this.buttonRemoveSkill.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonRemoveSkill.Enabled = false;
			this.buttonRemoveSkill.Image = global::ARCed.Properties.Resources.Delete;
			this.buttonRemoveSkill.Location = new System.Drawing.Point(240, 49);
			this.buttonRemoveSkill.Name = "buttonRemoveSkill";
			this.buttonRemoveSkill.Size = new System.Drawing.Size(24, 24);
			this.buttonRemoveSkill.TabIndex = 2;
			this.buttonRemoveSkill.UseVisualStyleBackColor = true;
			this.buttonRemoveSkill.Click += new System.EventHandler(this.ButtonRemoveSkillClick);
			// 
			// buttonAddSkill
			// 
			this.buttonAddSkill.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonAddSkill.Image = global::ARCed.Properties.Resources.Add;
			this.buttonAddSkill.Location = new System.Drawing.Point(240, 19);
			this.buttonAddSkill.Name = "buttonAddSkill";
			this.buttonAddSkill.Size = new System.Drawing.Size(24, 24);
			this.buttonAddSkill.TabIndex = 1;
			this.buttonAddSkill.UseVisualStyleBackColor = true;
			this.buttonAddSkill.Click += new System.EventHandler(this.ButtonAddSkillClick);
			// 
			// listViewSkills
			// 
			this.listViewSkills.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.listViewSkills.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.columnLevel,
            this.columnId,
            this.columnSkill});
			this.listViewSkills.ContextMenuStrip = this.contextMenuSkills;
			this.listViewSkills.FullRowSelect = true;
			this.listViewSkills.GridLines = true;
			this.listViewSkills.Location = new System.Drawing.Point(6, 19);
			this.listViewSkills.MultiSelect = false;
			this.listViewSkills.Name = "listViewSkills";
			this.listViewSkills.Size = new System.Drawing.Size(228, 133);
			this.listViewSkills.TabIndex = 0;
			this.listViewSkills.UseCompatibleStateImageBehavior = false;
			this.listViewSkills.View = System.Windows.Forms.View.Details;
			this.listViewSkills.ColumnClick += new System.Windows.Forms.ColumnClickEventHandler(this.ListViewSkillsColumnClick);
			this.listViewSkills.SelectedIndexChanged += new System.EventHandler(this.ListViewSkillsSelectedIndexChanged);
			this.listViewSkills.DoubleClick += new System.EventHandler(this.ListViewSkillsDoubleClick);
			// 
			// columnLevel
			// 
			this.columnLevel.Text = "Level";
			this.columnLevel.Width = 48;
			// 
			// columnId
			// 
			this.columnId.Text = "ID";
			this.columnId.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			this.columnId.Width = 48;
			// 
			// columnSkill
			// 
			this.columnSkill.Text = "Skill";
			this.columnSkill.Width = 136;
			// 
			// contextMenuSkills
			// 
			this.contextMenuSkills.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.contextButtonSkillEdit,
            this.toolStripSeparator1,
            this.contextButtonSkillAdd,
            this.contextButtonSkillRemove});
			this.contextMenuSkills.Name = "contextMenuSkills";
			this.contextMenuSkills.Size = new System.Drawing.Size(118, 76);
			// 
			// contextButtonSkillEdit
			// 
			this.contextButtonSkillEdit.Enabled = false;
			this.contextButtonSkillEdit.Image = global::ARCed.Properties.Resources.Settings2;
			this.contextButtonSkillEdit.Name = "contextButtonSkillEdit";
			this.contextButtonSkillEdit.Size = new System.Drawing.Size(117, 22);
			this.contextButtonSkillEdit.Text = "Edit";
			this.contextButtonSkillEdit.Click += new System.EventHandler(this.ButtonEditSkillClick);
			// 
			// toolStripSeparator1
			// 
			this.toolStripSeparator1.Name = "toolStripSeparator1";
			this.toolStripSeparator1.Size = new System.Drawing.Size(114, 6);
			// 
			// contextButtonSkillAdd
			// 
			this.contextButtonSkillAdd.Image = global::ARCed.Properties.Resources.Add;
			this.contextButtonSkillAdd.Name = "contextButtonSkillAdd";
			this.contextButtonSkillAdd.Size = new System.Drawing.Size(117, 22);
			this.contextButtonSkillAdd.Text = "Add";
			this.contextButtonSkillAdd.Click += new System.EventHandler(this.ButtonAddSkillClick);
			// 
			// contextButtonSkillRemove
			// 
			this.contextButtonSkillRemove.Enabled = false;
			this.contextButtonSkillRemove.Image = global::ARCed.Properties.Resources.Delete;
			this.contextButtonSkillRemove.Name = "contextButtonSkillRemove";
			this.contextButtonSkillRemove.Size = new System.Drawing.Size(117, 22);
			this.contextButtonSkillRemove.Text = "Remove";
			this.contextButtonSkillRemove.Click += new System.EventHandler(this.ButtonRemoveSkillClick);
			// 
			// noteTextBox
			// 
			this.noteTextBox.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.noteTextBox.Location = new System.Drawing.Point(3, 3);
			this.noteTextBox.Name = "noteTextBox";
			this.noteTextBox.NoteText = "";
			this.noteTextBox.Size = new System.Drawing.Size(270, 120);
			this.noteTextBox.TabIndex = 0;
			this.noteTextBox.NoteTextChanged += new ARCed.Controls.NoteTextBox.TextChangedEventHandler(this.NoteTextBoxNoteTextChanged);
			// 
			// ClassMainForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(755, 454);
			this.Controls.Add(this.splitContainerMain);
			this.DoubleBuffered = true;
			this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.Name = "ClassMainForm";
			this.RpgTypeName = "RPG.Class";
			this.Text = "Classes";
			this.splitContainerMain.Panel1.ResumeLayout(false);
			this.splitContainerMain.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerMain)).EndInit();
			this.splitContainerMain.ResumeLayout(false);
			this.splitContainerLeft.Panel1.ResumeLayout(false);
			this.splitContainerLeft.Panel2.ResumeLayout(false);
			this.splitContainerLeft.Panel2.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerLeft)).EndInit();
			this.splitContainerLeft.ResumeLayout(false);
			this.splitContainerRight.Panel1.ResumeLayout(false);
			this.splitContainerRight.Panel1.PerformLayout();
			this.splitContainerRight.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerRight)).EndInit();
			this.splitContainerRight.ResumeLayout(false);
			this.splitContainerFarRight.Panel1.ResumeLayout(false);
			this.splitContainerFarRight.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerFarRight)).EndInit();
			this.splitContainerFarRight.ResumeLayout(false);
			this.splitContainerEfficiency.Panel1.ResumeLayout(false);
			this.splitContainerEfficiency.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerEfficiency)).EndInit();
			this.splitContainerEfficiency.ResumeLayout(false);
			this.splitContainerSkillNotes.Panel1.ResumeLayout(false);
			this.splitContainerSkillNotes.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerSkillNotes)).EndInit();
			this.splitContainerSkillNotes.ResumeLayout(false);
			this.groupBoxSkills.ResumeLayout(false);
			this.contextMenuSkills.ResumeLayout(false);
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.SplitContainer splitContainerMain;
		private System.Windows.Forms.SplitContainer splitContainerLeft;
		private System.Windows.Forms.SplitContainer splitContainerRight;
		private Controls.CheckGroupBox checkGroupWeapons;
		private System.Windows.Forms.TextBox textBoxName;
		private System.Windows.Forms.Label labelName;
		private Controls.CheckGroupBox checkGroupArmor;
		private System.Windows.Forms.ComboBox comboBoxPosition;
		private System.Windows.Forms.Label labelPosition;
		private System.Windows.Forms.SplitContainer splitContainerFarRight;
		private System.Windows.Forms.SplitContainer splitContainerEfficiency;
		private System.Windows.Forms.SplitContainer splitContainerSkillNotes;
		private Controls.NoteTextBox noteTextBox;
		private System.Windows.Forms.GroupBox groupBoxSkills;
		private System.Windows.Forms.Button buttonRemoveSkill;
		private System.Windows.Forms.Button buttonAddSkill;
		private System.Windows.Forms.ListView listViewSkills;
		private System.Windows.Forms.ColumnHeader columnLevel;
		private System.Windows.Forms.ColumnHeader columnSkill;
		private System.Windows.Forms.ColumnHeader columnId;
		private System.Windows.Forms.ContextMenuStrip contextMenuSkills;
		private System.Windows.Forms.ToolStripMenuItem contextButtonSkillEdit;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator1;
		private System.Windows.Forms.ToolStripMenuItem contextButtonSkillAdd;
		private System.Windows.Forms.ToolStripMenuItem contextButtonSkillRemove;
		private System.Windows.Forms.Button buttonEditSkill;
		private Controls.MultiStateCheckedListBox checkedListElements;
		private Controls.MultiStateCheckedListBox checkedListStates;
		private Controls.DatabaseObjectListBox dataObjectList;
	}
}