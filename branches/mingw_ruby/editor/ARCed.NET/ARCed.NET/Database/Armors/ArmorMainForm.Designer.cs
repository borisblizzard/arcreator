namespace ARCed.Database.Armors
{
    sealed partial class ArmorMainForm
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
			System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(ArmorMainForm));
			this.splitContainerMain = new System.Windows.Forms.SplitContainer();
			this.dataObjectList = new ARCed.Controls.DatabaseObjectListBox();
			this.splitContainerWeapons = new System.Windows.Forms.SplitContainer();
			this.splitContainerKind = new System.Windows.Forms.SplitContainer();
			this.comboBoxKind = new System.Windows.Forms.ComboBox();
			this.labelKind = new System.Windows.Forms.Label();
			this.comboBoxAutoState = new System.Windows.Forms.ComboBox();
			this.labelAutoState = new System.Windows.Forms.Label();
			this.groupBoxParameters = new System.Windows.Forms.GroupBox();
			this.flowPanel = new System.Windows.Forms.FlowLayoutPanel();
			this.paramBoxPrice = new ARCed.Controls.ParamBox();
			this.paramBoxPdef = new ARCed.Controls.ParamBox();
			this.paramBoxMdef = new ARCed.Controls.ParamBox();
			this.paramBoxEva = new ARCed.Controls.ParamBox();
			this.paramBoxStrPlus = new ARCed.Controls.ParamBox();
			this.paramBoxDexPlus = new ARCed.Controls.ParamBox();
			this.paramBoxAgiPlus = new ARCed.Controls.ParamBox();
			this.paramBoxIntPlus = new ARCed.Controls.ParamBox();
			this.pictureBoxIcon = new System.Windows.Forms.PictureBox();
			this.labelIcon = new System.Windows.Forms.Label();
			this.textBoxDescription = new System.Windows.Forms.TextBox();
			this.labelDescription = new System.Windows.Forms.Label();
			this.textBoxName = new System.Windows.Forms.TextBox();
			this.labelName = new System.Windows.Forms.Label();
			this.splitContainerRight = new System.Windows.Forms.SplitContainer();
			this.splitContainerElementState = new System.Windows.Forms.SplitContainer();
			this.checkGroupBoxElements = new ARCed.Controls.CheckGroupBox(this.components);
			this.checkGroupBoxStates = new ARCed.Controls.CheckGroupBox(this.components);
			this.noteTextBox = new ARCed.Controls.NoteTextBox();
			this.textBoxIcon = new ARCed.Controls.TextBoxButton();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerMain)).BeginInit();
			this.splitContainerMain.Panel1.SuspendLayout();
			this.splitContainerMain.Panel2.SuspendLayout();
			this.splitContainerMain.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerWeapons)).BeginInit();
			this.splitContainerWeapons.Panel1.SuspendLayout();
			this.splitContainerWeapons.Panel2.SuspendLayout();
			this.splitContainerWeapons.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerKind)).BeginInit();
			this.splitContainerKind.Panel1.SuspendLayout();
			this.splitContainerKind.Panel2.SuspendLayout();
			this.splitContainerKind.SuspendLayout();
			this.groupBoxParameters.SuspendLayout();
			this.flowPanel.SuspendLayout();
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
			this.dataObjectList.HeaderText = "Armors";
			this.dataObjectList.Location = new System.Drawing.Point(3, 3);
			this.dataObjectList.Name = "dataObjectList";
			this.dataObjectList.SelectedIndex = -1;
			this.dataObjectList.Size = new System.Drawing.Size(182, 482);
			this.dataObjectList.TabIndex = 0;
			this.dataObjectList.TabStop = false;
			this.dataObjectList.OnListBoxIndexChanged += new ARCed.Controls.DatabaseObjectListBox.ObjectListIndexChangedEventHandler(this.ListBoxArmorsOnListBoxIndexChanged);
			// 
			// splitContainerWeapons
			// 
			this.splitContainerWeapons.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainerWeapons.Location = new System.Drawing.Point(0, 0);
			this.splitContainerWeapons.Name = "splitContainerWeapons";
			// 
			// splitContainerWeapons.Panel1
			// 
			this.splitContainerWeapons.Panel1.Controls.Add(this.textBoxIcon);
			this.splitContainerWeapons.Panel1.Controls.Add(this.splitContainerKind);
			this.splitContainerWeapons.Panel1.Controls.Add(this.groupBoxParameters);
			this.splitContainerWeapons.Panel1.Controls.Add(this.pictureBoxIcon);
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
			// splitContainerKind
			// 
			this.splitContainerKind.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.splitContainerKind.Location = new System.Drawing.Point(0, 134);
			this.splitContainerKind.Name = "splitContainerKind";
			// 
			// splitContainerKind.Panel1
			// 
			this.splitContainerKind.Panel1.Controls.Add(this.comboBoxKind);
			this.splitContainerKind.Panel1.Controls.Add(this.labelKind);
			// 
			// splitContainerKind.Panel2
			// 
			this.splitContainerKind.Panel2.Controls.Add(this.comboBoxAutoState);
			this.splitContainerKind.Panel2.Controls.Add(this.labelAutoState);
			this.splitContainerKind.Size = new System.Drawing.Size(277, 39);
			this.splitContainerKind.SplitterDistance = 136;
			this.splitContainerKind.TabIndex = 40;
			// 
			// comboBoxKind
			// 
			this.comboBoxKind.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxKind.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxKind.FormattingEnabled = true;
			this.comboBoxKind.Items.AddRange(new object[] {
            "Shield",
            "Helmet",
            "Body Armor",
            "Accessory"});
			this.comboBoxKind.Location = new System.Drawing.Point(6, 16);
			this.comboBoxKind.Name = "comboBoxKind";
			this.comboBoxKind.Size = new System.Drawing.Size(124, 21);
			this.comboBoxKind.TabIndex = 3;
			this.comboBoxKind.SelectedIndexChanged += new System.EventHandler(this.ComboBoxKindSelectedIndexChanged);
			// 
			// labelKind
			// 
			this.labelKind.AutoSize = true;
			this.labelKind.Location = new System.Drawing.Point(3, 0);
			this.labelKind.Name = "labelKind";
			this.labelKind.Size = new System.Drawing.Size(31, 13);
			this.labelKind.TabIndex = 2;
			this.labelKind.Text = "Kind:";
			// 
			// comboBoxAutoState
			// 
			this.comboBoxAutoState.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxAutoState.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxAutoState.FormattingEnabled = true;
			this.comboBoxAutoState.Items.AddRange(new object[] {
            "<None>"});
			this.comboBoxAutoState.Location = new System.Drawing.Point(6, 16);
			this.comboBoxAutoState.Name = "comboBoxAutoState";
			this.comboBoxAutoState.Size = new System.Drawing.Size(128, 21);
			this.comboBoxAutoState.TabIndex = 4;
			this.comboBoxAutoState.SelectedIndexChanged += new System.EventHandler(this.ComboBoxAutoStateSelectedIndexChanged);
			// 
			// labelAutoState
			// 
			this.labelAutoState.AutoSize = true;
			this.labelAutoState.Location = new System.Drawing.Point(3, 0);
			this.labelAutoState.Name = "labelAutoState";
			this.labelAutoState.Size = new System.Drawing.Size(60, 13);
			this.labelAutoState.TabIndex = 3;
			this.labelAutoState.Text = "Auto-State:";
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
			this.flowPanel.Controls.Add(this.paramBoxPdef);
			this.flowPanel.Controls.Add(this.paramBoxMdef);
			this.flowPanel.Controls.Add(this.paramBoxEva);
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
			this.paramBoxPrice.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.ParamBoxOnValueChanged);
			// 
			// paramBoxPdef
			// 
			this.paramBoxPdef.Location = new System.Drawing.Point(76, 3);
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
			this.paramBoxPdef.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.ParamBoxOnValueChanged);
			// 
			// paramBoxMdef
			// 
			this.paramBoxMdef.Location = new System.Drawing.Point(149, 3);
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
			this.paramBoxMdef.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.ParamBoxOnValueChanged);
			// 
			// paramBoxEva
			// 
			this.paramBoxEva.Location = new System.Drawing.Point(3, 46);
			this.paramBoxEva.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
			this.paramBoxEva.Minimum = new decimal(new int[] {
            99999,
            0,
            0,
            -2147483648});
			this.paramBoxEva.Name = "paramBoxEva";
			this.paramBoxEva.ParameterIndex = 0;
			this.paramBoxEva.ParameterLabel = "EVA:";
			this.paramBoxEva.RpgAttribute = "eva";
			this.paramBoxEva.Size = new System.Drawing.Size(67, 37);
			this.paramBoxEva.TabIndex = 4;
			this.paramBoxEva.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxEva.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.ParamBoxOnValueChanged);
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
			this.paramBoxStrPlus.TabIndex = 8;
			this.paramBoxStrPlus.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxStrPlus.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.ParamBoxOnValueChanged);
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
			this.paramBoxDexPlus.TabIndex = 9;
			this.paramBoxDexPlus.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxDexPlus.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.ParamBoxOnValueChanged);
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
			this.paramBoxAgiPlus.TabIndex = 10;
			this.paramBoxAgiPlus.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxAgiPlus.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.ParamBoxOnValueChanged);
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
			this.paramBoxIntPlus.TabIndex = 11;
			this.paramBoxIntPlus.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxIntPlus.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.ParamBoxOnValueChanged);
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
			this.textBoxDescription.TextChanged += new System.EventHandler(this.TextBoxDescriptionTextChanged);
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
			this.textBoxName.TextChanged += new System.EventHandler(this.TextBoxNameTextChanged);
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
			this.splitContainerElementState.Panel2.Controls.Add(this.checkGroupBoxStates);
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
			this.checkGroupBoxElements.Text = "Element Defense";
			this.checkGroupBoxElements.OnCheckChange += new ARCed.Controls.CheckGroupBox.CheckChangeEventHandler(this.CheckGroupBoxElementsOnCheckChange);
			// 
			// checkGroupBoxStates
			// 
			this.checkGroupBoxStates.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.checkGroupBoxStates.Location = new System.Drawing.Point(3, 3);
			this.checkGroupBoxStates.Name = "checkGroupBoxStates";
			this.checkGroupBoxStates.SelectedIndex = -1;
			this.checkGroupBoxStates.Size = new System.Drawing.Size(145, 307);
			this.checkGroupBoxStates.TabIndex = 0;
			this.checkGroupBoxStates.TabStop = false;
			this.checkGroupBoxStates.Text = "State Defense";
			this.checkGroupBoxStates.OnCheckChange += new ARCed.Controls.CheckGroupBox.CheckChangeEventHandler(this.CheckGroupBoxStatesOnCheckChange);
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
			this.noteTextBox.NoteTextChanged += new ARCed.Controls.NoteTextBox.TextChangedEventHandler(this.NoteTextBoxNoteTextChanged);
			// 
			// textBoxIcon
			// 
			this.textBoxIcon.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBoxIcon.Location = new System.Drawing.Point(51, 107);
			this.textBoxIcon.MaximumSize = new System.Drawing.Size(1800, 20);
			this.textBoxIcon.Name = "textBoxIcon";
			this.textBoxIcon.Size = new System.Drawing.Size(223, 20);
			this.textBoxIcon.TabIndex = 41;
			this.textBoxIcon.OnButtonClick += new ARCed.Controls.TextBoxButton.ButtonClickHandler(this.ButtonIconClick);
			// 
			// ArmorMainForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(775, 491);
			this.Controls.Add(this.splitContainerMain);
			this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
			this.Name = "ArmorMainForm";
			this.RpgTypeName = "RPG.Armor";
			this.Text = "Armors";
			this.splitContainerMain.Panel1.ResumeLayout(false);
			this.splitContainerMain.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerMain)).EndInit();
			this.splitContainerMain.ResumeLayout(false);
			this.splitContainerWeapons.Panel1.ResumeLayout(false);
			this.splitContainerWeapons.Panel1.PerformLayout();
			this.splitContainerWeapons.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerWeapons)).EndInit();
			this.splitContainerWeapons.ResumeLayout(false);
			this.splitContainerKind.Panel1.ResumeLayout(false);
			this.splitContainerKind.Panel1.PerformLayout();
			this.splitContainerKind.Panel2.ResumeLayout(false);
			this.splitContainerKind.Panel2.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerKind)).EndInit();
			this.splitContainerKind.ResumeLayout(false);
			this.groupBoxParameters.ResumeLayout(false);
			this.flowPanel.ResumeLayout(false);
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
		private System.Windows.Forms.PictureBox pictureBoxIcon;
		private System.Windows.Forms.Label labelIcon;
		private System.Windows.Forms.TextBox textBoxDescription;
		private System.Windows.Forms.Label labelDescription;
		private System.Windows.Forms.TextBox textBoxName;
		private System.Windows.Forms.Label labelName;
		private System.Windows.Forms.GroupBox groupBoxParameters;
		private System.Windows.Forms.FlowLayoutPanel flowPanel;
		private Controls.ParamBox paramBoxPrice;
		private Controls.ParamBox paramBoxPdef;
		private Controls.ParamBox paramBoxMdef;
		private System.Windows.Forms.SplitContainer splitContainerRight;
		private System.Windows.Forms.SplitContainer splitContainerElementState;
		private Controls.CheckGroupBox checkGroupBoxElements;
		private Controls.NoteTextBox noteTextBox;
		private Controls.CheckGroupBox checkGroupBoxStates;
		private System.Windows.Forms.SplitContainer splitContainerKind;
		private System.Windows.Forms.ComboBox comboBoxKind;
		private System.Windows.Forms.Label labelKind;
		private System.Windows.Forms.ComboBox comboBoxAutoState;
		private System.Windows.Forms.Label labelAutoState;
		private Controls.ParamBox paramBoxEva;
		private Controls.ParamBox paramBoxStrPlus;
		private Controls.ParamBox paramBoxDexPlus;
		private Controls.ParamBox paramBoxAgiPlus;
		private Controls.ParamBox paramBoxIntPlus;
		private Controls.TextBoxButton textBoxIcon;
	}
}