namespace ARCed.Database.Weapons
{
	partial class WeaponMainForm
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
			System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(WeaponMainForm));
			this.splitContainerMain = new System.Windows.Forms.SplitContainer();
			this.dataObjectList = new ARCed.Controls.DatabaseObjectListBox();
			this.splitContainerWeapons = new System.Windows.Forms.SplitContainer();
			this.groupBoxParameters = new System.Windows.Forms.GroupBox();
			this.flowPanel = new System.Windows.Forms.FlowLayoutPanel();
			this.paramBoxPrice = new ARCed.Controls.ParamBox();
			this.paramBoxAtk = new ARCed.Controls.ParamBox();
			this.paramBoxPdef = new ARCed.Controls.ParamBox();
			this.paramBoxMdef = new ARCed.Controls.ParamBox();
			this.paramBoxStrPlus = new ARCed.Controls.ParamBox();
			this.paramBoxDexPlus = new ARCed.Controls.ParamBox();
			this.paramBoxAgiPlus = new ARCed.Controls.ParamBox();
			this.paramBoxIntPlus = new ARCed.Controls.ParamBox();
			this.splitContainerAnimation = new System.Windows.Forms.SplitContainer();
			this.comboBoxUserAnimation = new System.Windows.Forms.ComboBox();
			this.label3 = new System.Windows.Forms.Label();
			this.comboBoxTargetAnimation = new System.Windows.Forms.ComboBox();
			this.label4 = new System.Windows.Forms.Label();
			this.buttonIcon = new System.Windows.Forms.Button();
			this.pictureBoxIcon = new System.Windows.Forms.PictureBox();
			this.textBoxIcon = new System.Windows.Forms.TextBox();
			this.labelIcon = new System.Windows.Forms.Label();
			this.textBoxDescription = new System.Windows.Forms.TextBox();
			this.labelDescription = new System.Windows.Forms.Label();
			this.textBoxName = new System.Windows.Forms.TextBox();
			this.labelName = new System.Windows.Forms.Label();
			this.splitContainerRight = new System.Windows.Forms.SplitContainer();
			this.splitContainerElementState = new System.Windows.Forms.SplitContainer();
			this.checkGroupBoxElements = new ARCed.Controls.CheckGroupBox(this.components);
			this.checkedListBoxStates = new ARCed.Controls.MultiStateCheckedListBox();
			this.noteTextBox = new ARCed.Controls.NoteTextBox();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerMain)).BeginInit();
			this.splitContainerMain.Panel1.SuspendLayout();
			this.splitContainerMain.Panel2.SuspendLayout();
			this.splitContainerMain.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerWeapons)).BeginInit();
			this.splitContainerWeapons.Panel1.SuspendLayout();
			this.splitContainerWeapons.Panel2.SuspendLayout();
			this.splitContainerWeapons.SuspendLayout();
			this.groupBoxParameters.SuspendLayout();
			this.flowPanel.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerAnimation)).BeginInit();
			this.splitContainerAnimation.Panel1.SuspendLayout();
			this.splitContainerAnimation.Panel2.SuspendLayout();
			this.splitContainerAnimation.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.pictureBoxIcon)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerRight)).BeginInit();
			this.splitContainerRight.Panel1.SuspendLayout();
			this.splitContainerRight.Panel2.SuspendLayout();
			this.splitContainerRight.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerElementState)).BeginInit();
			this.splitContainerElementState.Panel1.SuspendLayout();
			this.splitContainerElementState.Panel2.SuspendLayout();
			this.splitContainerElementState.SuspendLayout();
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
			this.splitContainerMain.Panel2.Controls.Add(this.splitContainerWeapons);
			this.splitContainerMain.Size = new System.Drawing.Size(775, 491);
			this.splitContainerMain.SplitterDistance = 188;
			this.splitContainerMain.TabIndex = 0;
			// 
			// dataObjectList
			// 
			this.dataObjectList.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.dataObjectList.HeaderText = "Weapons";
			this.dataObjectList.Location = new System.Drawing.Point(3, 3);
			this.dataObjectList.Name = "dataObjectList";
			this.dataObjectList.SelectedIndex = -1;
			this.dataObjectList.Size = new System.Drawing.Size(182, 482);
			this.dataObjectList.TabIndex = 0;
			this.dataObjectList.TabStop = false;
			this.dataObjectList.OnListBoxIndexChanged += new ARCed.Controls.DatabaseObjectListBox.ObjectListIndexChangedEventHandler(this.listBoxWeapons_OnListBoxIndexChanged);
			// 
			// splitContainerWeapons
			// 
			this.splitContainerWeapons.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainerWeapons.Location = new System.Drawing.Point(0, 0);
			this.splitContainerWeapons.Name = "splitContainerWeapons";
			// 
			// splitContainerWeapons.Panel1
			// 
			this.splitContainerWeapons.Panel1.Controls.Add(this.groupBoxParameters);
			this.splitContainerWeapons.Panel1.Controls.Add(this.splitContainerAnimation);
			this.splitContainerWeapons.Panel1.Controls.Add(this.buttonIcon);
			this.splitContainerWeapons.Panel1.Controls.Add(this.pictureBoxIcon);
			this.splitContainerWeapons.Panel1.Controls.Add(this.textBoxIcon);
			this.splitContainerWeapons.Panel1.Controls.Add(this.labelIcon);
			this.splitContainerWeapons.Panel1.Controls.Add(this.textBoxDescription);
			this.splitContainerWeapons.Panel1.Controls.Add(this.labelDescription);
			this.splitContainerWeapons.Panel1.Controls.Add(this.textBoxName);
			this.splitContainerWeapons.Panel1.Controls.Add(this.labelName);
			// 
			// splitContainerWeapons.Panel2
			// 
			this.splitContainerWeapons.Panel2.Controls.Add(this.splitContainerRight);
			this.splitContainerWeapons.Size = new System.Drawing.Size(583, 491);
			this.splitContainerWeapons.SplitterDistance = 280;
			this.splitContainerWeapons.TabIndex = 0;
			// 
			// groupBoxParameters
			// 
			this.groupBoxParameters.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxParameters.Controls.Add(this.flowPanel);
			this.groupBoxParameters.Location = new System.Drawing.Point(6, 178);
			this.groupBoxParameters.Name = "groupBoxParameters";
			this.groupBoxParameters.Size = new System.Drawing.Size(271, 310);
			this.groupBoxParameters.TabIndex = 39;
			this.groupBoxParameters.TabStop = false;
			this.groupBoxParameters.Text = "Parameters";
			// 
			// flowPanel
			// 
			this.flowPanel.AutoScroll = true;
			this.flowPanel.Controls.Add(this.paramBoxPrice);
			this.flowPanel.Controls.Add(this.paramBoxAtk);
			this.flowPanel.Controls.Add(this.paramBoxPdef);
			this.flowPanel.Controls.Add(this.paramBoxMdef);
			this.flowPanel.Controls.Add(this.paramBoxStrPlus);
			this.flowPanel.Controls.Add(this.paramBoxDexPlus);
			this.flowPanel.Controls.Add(this.paramBoxAgiPlus);
			this.flowPanel.Controls.Add(this.paramBoxIntPlus);
			this.flowPanel.Dock = System.Windows.Forms.DockStyle.Fill;
			this.flowPanel.Location = new System.Drawing.Point(3, 16);
			this.flowPanel.Name = "flowPanel";
			this.flowPanel.Size = new System.Drawing.Size(265, 291);
			this.flowPanel.TabIndex = 0;
			// 
			// paramBoxPrice
			// 
			this.paramBoxPrice.Location = new System.Drawing.Point(3, 3);
			this.paramBoxPrice.Maximum = new decimal(new int[] {
            99999999,
            0,
            0,
            0});
			this.paramBoxPrice.Minimum = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxPrice.Name = "paramBoxPrice";
			this.paramBoxPrice.ParameterIndex = 0;
			this.paramBoxPrice.ParameterLabel = "Price:";
			this.paramBoxPrice.RpgAttribute = "price";
			this.paramBoxPrice.Size = new System.Drawing.Size(67, 37);
			this.paramBoxPrice.TabIndex = 0;
			this.paramBoxPrice.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxPrice.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.paramBox_OnValueChanged);
			// 
			// paramBoxAtk
			// 
			this.paramBoxAtk.Location = new System.Drawing.Point(76, 3);
			this.paramBoxAtk.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
			this.paramBoxAtk.Minimum = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxAtk.Name = "paramBoxAtk";
			this.paramBoxAtk.ParameterIndex = 0;
			this.paramBoxAtk.ParameterLabel = "ATK:";
			this.paramBoxAtk.RpgAttribute = "atk";
			this.paramBoxAtk.Size = new System.Drawing.Size(67, 37);
			this.paramBoxAtk.TabIndex = 1;
			this.paramBoxAtk.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxAtk.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.paramBox_OnValueChanged);
			// 
			// paramBoxPdef
			// 
			this.paramBoxPdef.Location = new System.Drawing.Point(149, 3);
			this.paramBoxPdef.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
			this.paramBoxPdef.Minimum = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxPdef.Name = "paramBoxPdef";
			this.paramBoxPdef.ParameterIndex = 0;
			this.paramBoxPdef.ParameterLabel = "PDEF:";
			this.paramBoxPdef.RpgAttribute = "pdef";
			this.paramBoxPdef.Size = new System.Drawing.Size(67, 37);
			this.paramBoxPdef.TabIndex = 2;
			this.paramBoxPdef.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxPdef.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.paramBox_OnValueChanged);
			// 
			// paramBoxMdef
			// 
			this.paramBoxMdef.Location = new System.Drawing.Point(3, 46);
			this.paramBoxMdef.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
			this.paramBoxMdef.Minimum = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxMdef.Name = "paramBoxMdef";
			this.paramBoxMdef.ParameterIndex = 0;
			this.paramBoxMdef.ParameterLabel = "MDEF:";
			this.paramBoxMdef.RpgAttribute = "mdef";
			this.paramBoxMdef.Size = new System.Drawing.Size(67, 37);
			this.paramBoxMdef.TabIndex = 3;
			this.paramBoxMdef.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxMdef.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.paramBox_OnValueChanged);
			// 
			// paramBoxStrPlus
			// 
			this.paramBoxStrPlus.Location = new System.Drawing.Point(76, 46);
			this.paramBoxStrPlus.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
			this.paramBoxStrPlus.Minimum = new decimal(new int[] {
            99999,
            0,
            0,
            -2147483648});
			this.paramBoxStrPlus.Name = "paramBoxStrPlus";
			this.paramBoxStrPlus.ParameterIndex = 0;
			this.paramBoxStrPlus.ParameterLabel = "STR+:";
			this.paramBoxStrPlus.RpgAttribute = "str_plus";
			this.paramBoxStrPlus.Size = new System.Drawing.Size(67, 37);
			this.paramBoxStrPlus.TabIndex = 4;
			this.paramBoxStrPlus.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxStrPlus.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.paramBox_OnValueChanged);
			// 
			// paramBoxDexPlus
			// 
			this.paramBoxDexPlus.Location = new System.Drawing.Point(149, 46);
			this.paramBoxDexPlus.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
			this.paramBoxDexPlus.Minimum = new decimal(new int[] {
            99999,
            0,
            0,
            -2147483648});
			this.paramBoxDexPlus.Name = "paramBoxDexPlus";
			this.paramBoxDexPlus.ParameterIndex = 0;
			this.paramBoxDexPlus.ParameterLabel = "DEX+:";
			this.paramBoxDexPlus.RpgAttribute = "dex_plus";
			this.paramBoxDexPlus.Size = new System.Drawing.Size(67, 37);
			this.paramBoxDexPlus.TabIndex = 5;
			this.paramBoxDexPlus.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxDexPlus.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.paramBox_OnValueChanged);
			// 
			// paramBoxAgiPlus
			// 
			this.paramBoxAgiPlus.Location = new System.Drawing.Point(3, 89);
			this.paramBoxAgiPlus.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
			this.paramBoxAgiPlus.Minimum = new decimal(new int[] {
            99999,
            0,
            0,
            -2147483648});
			this.paramBoxAgiPlus.Name = "paramBoxAgiPlus";
			this.paramBoxAgiPlus.ParameterIndex = 0;
			this.paramBoxAgiPlus.ParameterLabel = "AGI+:";
			this.paramBoxAgiPlus.RpgAttribute = "agi_plus";
			this.paramBoxAgiPlus.Size = new System.Drawing.Size(67, 37);
			this.paramBoxAgiPlus.TabIndex = 6;
			this.paramBoxAgiPlus.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxAgiPlus.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.paramBox_OnValueChanged);
			// 
			// paramBoxIntPlus
			// 
			this.paramBoxIntPlus.Location = new System.Drawing.Point(76, 89);
			this.paramBoxIntPlus.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
			this.paramBoxIntPlus.Minimum = new decimal(new int[] {
            99999,
            0,
            0,
            -2147483648});
			this.paramBoxIntPlus.Name = "paramBoxIntPlus";
			this.paramBoxIntPlus.ParameterIndex = 0;
			this.paramBoxIntPlus.ParameterLabel = "INT+:";
			this.paramBoxIntPlus.RpgAttribute = "int_plus";
			this.paramBoxIntPlus.Size = new System.Drawing.Size(67, 37);
			this.paramBoxIntPlus.TabIndex = 7;
			this.paramBoxIntPlus.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxIntPlus.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.paramBox_OnValueChanged);
			// 
			// splitContainerAnimation
			// 
			this.splitContainerAnimation.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.splitContainerAnimation.Location = new System.Drawing.Point(0, 133);
			this.splitContainerAnimation.Name = "splitContainerAnimation";
			// 
			// splitContainerAnimation.Panel1
			// 
			this.splitContainerAnimation.Panel1.Controls.Add(this.comboBoxUserAnimation);
			this.splitContainerAnimation.Panel1.Controls.Add(this.label3);
			// 
			// splitContainerAnimation.Panel2
			// 
			this.splitContainerAnimation.Panel2.Controls.Add(this.comboBoxTargetAnimation);
			this.splitContainerAnimation.Panel2.Controls.Add(this.label4);
			this.splitContainerAnimation.Size = new System.Drawing.Size(277, 39);
			this.splitContainerAnimation.SplitterDistance = 137;
			this.splitContainerAnimation.TabIndex = 38;
			// 
			// comboBoxUserAnimation
			// 
			this.comboBoxUserAnimation.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxUserAnimation.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxUserAnimation.FormattingEnabled = true;
			this.comboBoxUserAnimation.Items.AddRange(new object[] {
            "<None>"});
			this.comboBoxUserAnimation.Location = new System.Drawing.Point(6, 16);
			this.comboBoxUserAnimation.Name = "comboBoxUserAnimation";
			this.comboBoxUserAnimation.Size = new System.Drawing.Size(128, 21);
			this.comboBoxUserAnimation.TabIndex = 3;
			this.comboBoxUserAnimation.SelectedIndexChanged += new System.EventHandler(this.comboBoxUserAnimation_SelectedIndexChanged);
			// 
			// label3
			// 
			this.label3.AutoSize = true;
			this.label3.Location = new System.Drawing.Point(3, 0);
			this.label3.Name = "label3";
			this.label3.Size = new System.Drawing.Size(81, 13);
			this.label3.TabIndex = 2;
			this.label3.Text = "User Animation:";
			// 
			// comboBoxTargetAnimation
			// 
			this.comboBoxTargetAnimation.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxTargetAnimation.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxTargetAnimation.FormattingEnabled = true;
			this.comboBoxTargetAnimation.Items.AddRange(new object[] {
            "<None>"});
			this.comboBoxTargetAnimation.Location = new System.Drawing.Point(6, 16);
			this.comboBoxTargetAnimation.Name = "comboBoxTargetAnimation";
			this.comboBoxTargetAnimation.Size = new System.Drawing.Size(130, 21);
			this.comboBoxTargetAnimation.TabIndex = 4;
			this.comboBoxTargetAnimation.SelectedIndexChanged += new System.EventHandler(this.comboBoxTargetAnimation_SelectedIndexChanged);
			// 
			// label4
			// 
			this.label4.AutoSize = true;
			this.label4.Location = new System.Drawing.Point(3, 0);
			this.label4.Name = "label4";
			this.label4.Size = new System.Drawing.Size(90, 13);
			this.label4.TabIndex = 3;
			this.label4.Text = "Target Animation:";
			// 
			// buttonIcon
			// 
			this.buttonIcon.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonIcon.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
			this.buttonIcon.Image = global::ARCed.Properties.Resources.Edit;
			this.buttonIcon.Location = new System.Drawing.Point(253, 104);
			this.buttonIcon.Name = "buttonIcon";
			this.buttonIcon.Size = new System.Drawing.Size(24, 24);
			this.buttonIcon.TabIndex = 37;
			this.buttonIcon.UseVisualStyleBackColor = true;
			this.buttonIcon.Click += new System.EventHandler(this.buttonIcon_Click);
			// 
			// pictureBoxIcon
			// 
			this.pictureBoxIcon.BackColor = System.Drawing.SystemColors.Window;
			this.pictureBoxIcon.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
			this.pictureBoxIcon.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
			this.pictureBoxIcon.Location = new System.Drawing.Point(6, 91);
			this.pictureBoxIcon.Name = "pictureBoxIcon";
			this.pictureBoxIcon.Size = new System.Drawing.Size(36, 36);
			this.pictureBoxIcon.TabIndex = 36;
			this.pictureBoxIcon.TabStop = false;
			// 
			// textBoxIcon
			// 
			this.textBoxIcon.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBoxIcon.BackColor = System.Drawing.SystemColors.Window;
			this.textBoxIcon.Location = new System.Drawing.Point(51, 107);
			this.textBoxIcon.Name = "textBoxIcon";
			this.textBoxIcon.ReadOnly = true;
			this.textBoxIcon.Size = new System.Drawing.Size(196, 20);
			this.textBoxIcon.TabIndex = 35;
			// 
			// labelIcon
			// 
			this.labelIcon.AutoSize = true;
			this.labelIcon.Location = new System.Drawing.Point(48, 91);
			this.labelIcon.Name = "labelIcon";
			this.labelIcon.Size = new System.Drawing.Size(31, 13);
			this.labelIcon.TabIndex = 32;
			this.labelIcon.Text = "Icon:";
			// 
			// textBoxDescription
			// 
			this.textBoxDescription.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBoxDescription.Location = new System.Drawing.Point(6, 64);
			this.textBoxDescription.Name = "textBoxDescription";
			this.textBoxDescription.Size = new System.Drawing.Size(271, 20);
			this.textBoxDescription.TabIndex = 31;
			this.textBoxDescription.TextChanged += new System.EventHandler(this.textBoxDescription_TextChanged);
			// 
			// labelDescription
			// 
			this.labelDescription.AutoSize = true;
			this.labelDescription.Location = new System.Drawing.Point(3, 48);
			this.labelDescription.Name = "labelDescription";
			this.labelDescription.Size = new System.Drawing.Size(63, 13);
			this.labelDescription.TabIndex = 30;
			this.labelDescription.Text = "Description:";
			// 
			// textBoxName
			// 
			this.textBoxName.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBoxName.Location = new System.Drawing.Point(6, 25);
			this.textBoxName.Name = "textBoxName";
			this.textBoxName.Size = new System.Drawing.Size(271, 20);
			this.textBoxName.TabIndex = 29;
			this.textBoxName.TextChanged += new System.EventHandler(this.textBoxName_TextChanged);
			// 
			// labelName
			// 
			this.labelName.AutoSize = true;
			this.labelName.Location = new System.Drawing.Point(3, 9);
			this.labelName.Name = "labelName";
			this.labelName.Size = new System.Drawing.Size(38, 13);
			this.labelName.TabIndex = 28;
			this.labelName.Text = "Name:";
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
			this.splitContainerRight.Panel1.Controls.Add(this.splitContainerElementState);
			// 
			// splitContainerRight.Panel2
			// 
			this.splitContainerRight.Panel2.Controls.Add(this.noteTextBox);
			this.splitContainerRight.Size = new System.Drawing.Size(299, 491);
			this.splitContainerRight.SplitterDistance = 313;
			this.splitContainerRight.TabIndex = 0;
			// 
			// splitContainerElementState
			// 
			this.splitContainerElementState.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainerElementState.Location = new System.Drawing.Point(0, 0);
			this.splitContainerElementState.Name = "splitContainerElementState";
			// 
			// splitContainerElementState.Panel1
			// 
			this.splitContainerElementState.Panel1.Controls.Add(this.checkGroupBoxElements);
			// 
			// splitContainerElementState.Panel2
			// 
			this.splitContainerElementState.Panel2.Controls.Add(this.checkedListBoxStates);
			this.splitContainerElementState.Size = new System.Drawing.Size(299, 313);
			this.splitContainerElementState.SplitterDistance = 144;
			this.splitContainerElementState.TabIndex = 0;
			// 
			// checkGroupBoxElements
			// 
			this.checkGroupBoxElements.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.checkGroupBoxElements.Location = new System.Drawing.Point(3, 3);
			this.checkGroupBoxElements.Name = "checkGroupBoxElements";
			this.checkGroupBoxElements.SelectedIndex = -1;
			this.checkGroupBoxElements.Size = new System.Drawing.Size(138, 307);
			this.checkGroupBoxElements.TabIndex = 0;
			this.checkGroupBoxElements.TabStop = false;
			this.checkGroupBoxElements.Text = "Elements";
			this.checkGroupBoxElements.OnCheckChange += new ARCed.Controls.CheckGroupBox.CheckChangeEventHandler(this.checkGroupBoxElements_OnCheckChange);
			// 
			// checkedListBoxStates
			// 
			this.checkedListBoxStates.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.checkedListBoxStates.Colors = new System.Drawing.Color[] {
        System.Drawing.Color.Empty,
        System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(0)))), ((int)(((byte)(0))))),
        System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(0)))), ((int)(((byte)(192)))))};
			this.checkedListBoxStates.Items = new string[] {
        "",
        "+",
        "-"};
			this.checkedListBoxStates.Location = new System.Drawing.Point(3, 3);
			this.checkedListBoxStates.Name = "checkedListBoxStates";
			this.checkedListBoxStates.Size = new System.Drawing.Size(145, 307);
			this.checkedListBoxStates.TabIndex = 0;
			this.checkedListBoxStates.TabStop = false;
			this.checkedListBoxStates.Text = "State Change";
			this.checkedListBoxStates.OnItemChanged += new ARCed.Controls.MultiStateCheckedListBox.ItemValueChangedEventHandler(this.checkedListBoxStates_OnItemChanged);
			// 
			// noteTextBox
			// 
			this.noteTextBox.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.noteTextBox.Location = new System.Drawing.Point(3, 3);
			this.noteTextBox.Name = "noteTextBox";
			this.noteTextBox.NoteText = "";
			this.noteTextBox.Size = new System.Drawing.Size(293, 168);
			this.noteTextBox.TabIndex = 0;
			this.noteTextBox.NoteTextChanged += new ARCed.Controls.NoteTextBox.TextChangedEventHandler(this.noteTextBox_NoteTextChanged);
			// 
			// WeaponMainForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(775, 491);
			this.Controls.Add(this.splitContainerMain);
			this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
			this.Name = "WeaponMainForm";
			this.RpgTypeName = "RPG.Weapon";
			this.Text = "Weapons";
			this.splitContainerMain.Panel1.ResumeLayout(false);
			this.splitContainerMain.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerMain)).EndInit();
			this.splitContainerMain.ResumeLayout(false);
			this.splitContainerWeapons.Panel1.ResumeLayout(false);
			this.splitContainerWeapons.Panel1.PerformLayout();
			this.splitContainerWeapons.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerWeapons)).EndInit();
			this.splitContainerWeapons.ResumeLayout(false);
			this.groupBoxParameters.ResumeLayout(false);
			this.flowPanel.ResumeLayout(false);
			this.splitContainerAnimation.Panel1.ResumeLayout(false);
			this.splitContainerAnimation.Panel1.PerformLayout();
			this.splitContainerAnimation.Panel2.ResumeLayout(false);
			this.splitContainerAnimation.Panel2.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerAnimation)).EndInit();
			this.splitContainerAnimation.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.pictureBoxIcon)).EndInit();
			this.splitContainerRight.Panel1.ResumeLayout(false);
			this.splitContainerRight.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerRight)).EndInit();
			this.splitContainerRight.ResumeLayout(false);
			this.splitContainerElementState.Panel1.ResumeLayout(false);
			this.splitContainerElementState.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerElementState)).EndInit();
			this.splitContainerElementState.ResumeLayout(false);
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.SplitContainer splitContainerMain;
		private System.Windows.Forms.SplitContainer splitContainerWeapons;
		private Controls.DatabaseObjectListBox dataObjectList;
		private System.Windows.Forms.Button buttonIcon;
		private System.Windows.Forms.PictureBox pictureBoxIcon;
		private System.Windows.Forms.TextBox textBoxIcon;
		private System.Windows.Forms.Label labelIcon;
		private System.Windows.Forms.TextBox textBoxDescription;
		private System.Windows.Forms.Label labelDescription;
		private System.Windows.Forms.TextBox textBoxName;
		private System.Windows.Forms.Label labelName;
		private System.Windows.Forms.GroupBox groupBoxParameters;
		private System.Windows.Forms.SplitContainer splitContainerAnimation;
		private System.Windows.Forms.ComboBox comboBoxUserAnimation;
		private System.Windows.Forms.Label label3;
		private System.Windows.Forms.ComboBox comboBoxTargetAnimation;
		private System.Windows.Forms.Label label4;
		private System.Windows.Forms.FlowLayoutPanel flowPanel;
		private Controls.ParamBox paramBoxPrice;
		private Controls.ParamBox paramBoxAtk;
		private Controls.ParamBox paramBoxPdef;
		private Controls.ParamBox paramBoxMdef;
		private Controls.ParamBox paramBoxStrPlus;
		private Controls.ParamBox paramBoxDexPlus;
		private Controls.ParamBox paramBoxAgiPlus;
		private Controls.ParamBox paramBoxIntPlus;
		private System.Windows.Forms.SplitContainer splitContainerRight;
		private System.Windows.Forms.SplitContainer splitContainerElementState;
		private Controls.CheckGroupBox checkGroupBoxElements;
		private Controls.MultiStateCheckedListBox checkedListBoxStates;
		private Controls.NoteTextBox noteTextBox;
	}
}