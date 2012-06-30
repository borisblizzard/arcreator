namespace ARCed.Database.Skills
{
	partial class SkillMainForm
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
			System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(SkillMainForm));
			this.splitContainerMain = new System.Windows.Forms.SplitContainer();
			this.dataObjectList = new ARCed.Controls.DatabaseObjectListBox();
			this.splitContainerRight = new System.Windows.Forms.SplitContainer();
			this.groupBoxParameters = new System.Windows.Forms.GroupBox();
			this.flowPanel = new System.Windows.Forms.FlowLayoutPanel();
			this.paramBoxSpCost = new ARCed.Controls.ParamBox();
			this.paramBoxPower = new ARCed.Controls.ParamBox();
			this.paramBoxHitRate = new ARCed.Controls.ParamBox();
			this.paramBoxVariance = new ARCed.Controls.ParamBox();
			this.paramBoxAtk = new ARCed.Controls.ParamBox();
			this.paramBoxEva = new ARCed.Controls.ParamBox();
			this.paramBoxPdef = new ARCed.Controls.ParamBox();
			this.paramBoxMdef = new ARCed.Controls.ParamBox();
			this.paramBoxStr = new ARCed.Controls.ParamBox();
			this.paramBoxDex = new ARCed.Controls.ParamBox();
			this.paramBoxAgi = new ARCed.Controls.ParamBox();
			this.paramBoxInt = new ARCed.Controls.ParamBox();
			this.buttonPlay = new System.Windows.Forms.Button();
			this.button1 = new System.Windows.Forms.Button();
			this.labelMenuSE = new System.Windows.Forms.Label();
			this.splitContainerScopeAnimation = new System.Windows.Forms.SplitContainer();
			this.comboBoxCommonEvent = new System.Windows.Forms.ComboBox();
			this.labelCommonEvent = new System.Windows.Forms.Label();
			this.comboBoxUserAnimation = new System.Windows.Forms.ComboBox();
			this.label3 = new System.Windows.Forms.Label();
			this.comboBoxScope = new System.Windows.Forms.ComboBox();
			this.labelScope = new System.Windows.Forms.Label();
			this.comboBoxTargetAnimation = new System.Windows.Forms.ComboBox();
			this.label4 = new System.Windows.Forms.Label();
			this.comboBoxOccasion = new System.Windows.Forms.ComboBox();
			this.labelOccasion = new System.Windows.Forms.Label();
			this.textBoxMenuSe = new System.Windows.Forms.TextBox();
			this.buttonIcon = new System.Windows.Forms.Button();
			this.pictureBoxIcon = new System.Windows.Forms.PictureBox();
			this.textBoxIcon = new System.Windows.Forms.TextBox();
			this.labelIcon = new System.Windows.Forms.Label();
			this.textBoxDescription = new System.Windows.Forms.TextBox();
			this.labelDescription = new System.Windows.Forms.Label();
			this.textBoxName = new System.Windows.Forms.TextBox();
			this.labelName = new System.Windows.Forms.Label();
			this.splitContainerNotes = new System.Windows.Forms.SplitContainer();
			this.splitContainerStateElements = new System.Windows.Forms.SplitContainer();
			this.checkGroupBoxElements = new ARCed.Controls.CheckGroupBox(this.components);
			this.checkedListBoxStates = new ARCed.Controls.MultiStateCheckedListBox();
			this.noteTextBox = new ARCed.Controls.NoteTextBox();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerMain)).BeginInit();
			this.splitContainerMain.Panel1.SuspendLayout();
			this.splitContainerMain.Panel2.SuspendLayout();
			this.splitContainerMain.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerRight)).BeginInit();
			this.splitContainerRight.Panel1.SuspendLayout();
			this.splitContainerRight.Panel2.SuspendLayout();
			this.splitContainerRight.SuspendLayout();
			this.groupBoxParameters.SuspendLayout();
			this.flowPanel.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerScopeAnimation)).BeginInit();
			this.splitContainerScopeAnimation.Panel1.SuspendLayout();
			this.splitContainerScopeAnimation.Panel2.SuspendLayout();
			this.splitContainerScopeAnimation.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.pictureBoxIcon)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerNotes)).BeginInit();
			this.splitContainerNotes.Panel1.SuspendLayout();
			this.splitContainerNotes.Panel2.SuspendLayout();
			this.splitContainerNotes.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerStateElements)).BeginInit();
			this.splitContainerStateElements.Panel1.SuspendLayout();
			this.splitContainerStateElements.Panel2.SuspendLayout();
			this.splitContainerStateElements.SuspendLayout();
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
			this.splitContainerMain.Size = new System.Drawing.Size(708, 490);
			this.splitContainerMain.SplitterDistance = 174;
			this.splitContainerMain.TabIndex = 0;
			// 
			// dataObjectList
			// 
			this.dataObjectList.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.dataObjectList.HeaderText = "Skills";
			this.dataObjectList.Location = new System.Drawing.Point(6, 3);
			this.dataObjectList.Name = "dataObjectList";
			this.dataObjectList.SelectedIndex = -1;
			this.dataObjectList.Size = new System.Drawing.Size(165, 484);
			this.dataObjectList.TabIndex = 0;
			this.dataObjectList.TabStop = false;
			this.dataObjectList.OnListBoxIndexChanged += new ARCed.Controls.DatabaseObjectListBox.ObjectListIndexChangedEventHandler(this.listBoxSkills_OnListBoxIndexChanged);
			// 
			// splitContainerRight
			// 
			this.splitContainerRight.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainerRight.Location = new System.Drawing.Point(0, 0);
			this.splitContainerRight.Name = "splitContainerRight";
			// 
			// splitContainerRight.Panel1
			// 
			this.splitContainerRight.Panel1.Controls.Add(this.groupBoxParameters);
			this.splitContainerRight.Panel1.Controls.Add(this.buttonPlay);
			this.splitContainerRight.Panel1.Controls.Add(this.button1);
			this.splitContainerRight.Panel1.Controls.Add(this.labelMenuSE);
			this.splitContainerRight.Panel1.Controls.Add(this.splitContainerScopeAnimation);
			this.splitContainerRight.Panel1.Controls.Add(this.textBoxMenuSe);
			this.splitContainerRight.Panel1.Controls.Add(this.buttonIcon);
			this.splitContainerRight.Panel1.Controls.Add(this.pictureBoxIcon);
			this.splitContainerRight.Panel1.Controls.Add(this.textBoxIcon);
			this.splitContainerRight.Panel1.Controls.Add(this.labelIcon);
			this.splitContainerRight.Panel1.Controls.Add(this.textBoxDescription);
			this.splitContainerRight.Panel1.Controls.Add(this.labelDescription);
			this.splitContainerRight.Panel1.Controls.Add(this.textBoxName);
			this.splitContainerRight.Panel1.Controls.Add(this.labelName);
			// 
			// splitContainerRight.Panel2
			// 
			this.splitContainerRight.Panel2.Controls.Add(this.splitContainerNotes);
			this.splitContainerRight.Size = new System.Drawing.Size(530, 490);
			this.splitContainerRight.SplitterDistance = 239;
			this.splitContainerRight.TabIndex = 0;
			// 
			// groupBoxParameters
			// 
			this.groupBoxParameters.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxParameters.Controls.Add(this.flowPanel);
			this.groupBoxParameters.Location = new System.Drawing.Point(6, 300);
			this.groupBoxParameters.Name = "groupBoxParameters";
			this.groupBoxParameters.Size = new System.Drawing.Size(230, 178);
			this.groupBoxParameters.TabIndex = 28;
			this.groupBoxParameters.TabStop = false;
			this.groupBoxParameters.Text = "Parameters";
			// 
			// flowPanel
			// 
			this.flowPanel.AutoScroll = true;
			this.flowPanel.Controls.Add(this.paramBoxSpCost);
			this.flowPanel.Controls.Add(this.paramBoxPower);
			this.flowPanel.Controls.Add(this.paramBoxHitRate);
			this.flowPanel.Controls.Add(this.paramBoxVariance);
			this.flowPanel.Controls.Add(this.paramBoxAtk);
			this.flowPanel.Controls.Add(this.paramBoxEva);
			this.flowPanel.Controls.Add(this.paramBoxPdef);
			this.flowPanel.Controls.Add(this.paramBoxMdef);
			this.flowPanel.Controls.Add(this.paramBoxStr);
			this.flowPanel.Controls.Add(this.paramBoxDex);
			this.flowPanel.Controls.Add(this.paramBoxAgi);
			this.flowPanel.Controls.Add(this.paramBoxInt);
			this.flowPanel.Dock = System.Windows.Forms.DockStyle.Fill;
			this.flowPanel.Location = new System.Drawing.Point(3, 16);
			this.flowPanel.Name = "flowPanel";
			this.flowPanel.Size = new System.Drawing.Size(224, 159);
			this.flowPanel.TabIndex = 0;
			// 
			// paramBoxSpCost
			// 
			this.paramBoxSpCost.Location = new System.Drawing.Point(3, 3);
			this.paramBoxSpCost.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
			this.paramBoxSpCost.Minimum = new decimal(new int[] {
            99999,
            0,
            0,
            -2147483648});
			this.paramBoxSpCost.Name = "paramBoxSpCost";
			this.paramBoxSpCost.ParameterIndex = 0;
			this.paramBoxSpCost.ParameterLabel = "SP Cost:";
			this.paramBoxSpCost.RpgAttribute = "sp_cost";
			this.paramBoxSpCost.Size = new System.Drawing.Size(63, 37);
			this.paramBoxSpCost.TabIndex = 0;
			this.paramBoxSpCost.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxSpCost.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.paramBox_OnValueChanged);
			// 
			// paramBoxPower
			// 
			this.paramBoxPower.Location = new System.Drawing.Point(72, 3);
			this.paramBoxPower.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
			this.paramBoxPower.Minimum = new decimal(new int[] {
            99999,
            0,
            0,
            -2147483648});
			this.paramBoxPower.Name = "paramBoxPower";
			this.paramBoxPower.ParameterIndex = 0;
			this.paramBoxPower.ParameterLabel = "Power:";
			this.paramBoxPower.RpgAttribute = "power";
			this.paramBoxPower.Size = new System.Drawing.Size(63, 37);
			this.paramBoxPower.TabIndex = 1;
			this.paramBoxPower.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxPower.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.paramBox_OnValueChanged);
			// 
			// paramBoxHitRate
			// 
			this.paramBoxHitRate.Location = new System.Drawing.Point(141, 3);
			this.paramBoxHitRate.Maximum = new decimal(new int[] {
            100,
            0,
            0,
            0});
			this.paramBoxHitRate.Minimum = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxHitRate.Name = "paramBoxHitRate";
			this.paramBoxHitRate.ParameterIndex = 0;
			this.paramBoxHitRate.ParameterLabel = "Hit Rate:";
			this.paramBoxHitRate.RpgAttribute = "hit";
			this.paramBoxHitRate.Size = new System.Drawing.Size(63, 37);
			this.paramBoxHitRate.TabIndex = 2;
			this.paramBoxHitRate.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxHitRate.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.paramBox_OnValueChanged);
			// 
			// paramBoxVariance
			// 
			this.paramBoxVariance.Location = new System.Drawing.Point(3, 46);
			this.paramBoxVariance.Maximum = new decimal(new int[] {
            100,
            0,
            0,
            0});
			this.paramBoxVariance.Minimum = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxVariance.Name = "paramBoxVariance";
			this.paramBoxVariance.ParameterIndex = 0;
			this.paramBoxVariance.ParameterLabel = "Variance:";
			this.paramBoxVariance.RpgAttribute = "variance";
			this.paramBoxVariance.Size = new System.Drawing.Size(63, 37);
			this.paramBoxVariance.TabIndex = 3;
			this.paramBoxVariance.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxVariance.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.paramBox_OnValueChanged);
			// 
			// paramBoxAtk
			// 
			this.paramBoxAtk.Location = new System.Drawing.Point(72, 46);
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
			this.paramBoxAtk.ParameterLabel = "ATK-F:";
			this.paramBoxAtk.RpgAttribute = "atk_f";
			this.paramBoxAtk.Size = new System.Drawing.Size(63, 37);
			this.paramBoxAtk.TabIndex = 4;
			this.paramBoxAtk.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxAtk.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.paramBox_OnValueChanged);
			// 
			// paramBoxEva
			// 
			this.paramBoxEva.Location = new System.Drawing.Point(141, 46);
			this.paramBoxEva.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
			this.paramBoxEva.Minimum = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxEva.Name = "paramBoxEva";
			this.paramBoxEva.ParameterIndex = 0;
			this.paramBoxEva.ParameterLabel = "EVA-F:";
			this.paramBoxEva.RpgAttribute = "eva_f";
			this.paramBoxEva.Size = new System.Drawing.Size(63, 37);
			this.paramBoxEva.TabIndex = 5;
			this.paramBoxEva.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxEva.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.paramBox_OnValueChanged);
			// 
			// paramBoxPdef
			// 
			this.paramBoxPdef.Location = new System.Drawing.Point(3, 89);
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
			this.paramBoxPdef.ParameterLabel = "PDEF-F:";
			this.paramBoxPdef.RpgAttribute = "pdef_f";
			this.paramBoxPdef.Size = new System.Drawing.Size(63, 37);
			this.paramBoxPdef.TabIndex = 6;
			this.paramBoxPdef.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxPdef.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.paramBox_OnValueChanged);
			// 
			// paramBoxMdef
			// 
			this.paramBoxMdef.Location = new System.Drawing.Point(72, 89);
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
			this.paramBoxMdef.ParameterLabel = "MDEF-F:";
			this.paramBoxMdef.RpgAttribute = "mdef_f";
			this.paramBoxMdef.Size = new System.Drawing.Size(63, 37);
			this.paramBoxMdef.TabIndex = 7;
			this.paramBoxMdef.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxMdef.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.paramBox_OnValueChanged);
			// 
			// paramBoxStr
			// 
			this.paramBoxStr.Location = new System.Drawing.Point(141, 89);
			this.paramBoxStr.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
			this.paramBoxStr.Minimum = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxStr.Name = "paramBoxStr";
			this.paramBoxStr.ParameterIndex = 0;
			this.paramBoxStr.ParameterLabel = "STR-F:";
			this.paramBoxStr.RpgAttribute = "str_f";
			this.paramBoxStr.Size = new System.Drawing.Size(63, 37);
			this.paramBoxStr.TabIndex = 8;
			this.paramBoxStr.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxStr.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.paramBox_OnValueChanged);
			// 
			// paramBoxDex
			// 
			this.paramBoxDex.Location = new System.Drawing.Point(3, 132);
			this.paramBoxDex.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
			this.paramBoxDex.Minimum = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxDex.Name = "paramBoxDex";
			this.paramBoxDex.ParameterIndex = 0;
			this.paramBoxDex.ParameterLabel = "DEX-F:";
			this.paramBoxDex.RpgAttribute = "dex_f";
			this.paramBoxDex.Size = new System.Drawing.Size(63, 37);
			this.paramBoxDex.TabIndex = 9;
			this.paramBoxDex.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxDex.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.paramBox_OnValueChanged);
			// 
			// paramBoxAgi
			// 
			this.paramBoxAgi.Location = new System.Drawing.Point(72, 132);
			this.paramBoxAgi.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
			this.paramBoxAgi.Minimum = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxAgi.Name = "paramBoxAgi";
			this.paramBoxAgi.ParameterIndex = 0;
			this.paramBoxAgi.ParameterLabel = "AGI-F:";
			this.paramBoxAgi.RpgAttribute = "agi_f";
			this.paramBoxAgi.Size = new System.Drawing.Size(63, 37);
			this.paramBoxAgi.TabIndex = 10;
			this.paramBoxAgi.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxAgi.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.paramBox_OnValueChanged);
			// 
			// paramBoxInt
			// 
			this.paramBoxInt.Location = new System.Drawing.Point(141, 132);
			this.paramBoxInt.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
			this.paramBoxInt.Minimum = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxInt.Name = "paramBoxInt";
			this.paramBoxInt.ParameterIndex = 0;
			this.paramBoxInt.ParameterLabel = "INT-F:";
			this.paramBoxInt.RpgAttribute = "int_f";
			this.paramBoxInt.Size = new System.Drawing.Size(63, 37);
			this.paramBoxInt.TabIndex = 11;
			this.paramBoxInt.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxInt.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.paramBox_OnValueChanged);
			// 
			// buttonPlay
			// 
			this.buttonPlay.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonPlay.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
			this.buttonPlay.Image = global::ARCed.Properties.Resources.Play;
			this.buttonPlay.Location = new System.Drawing.Point(182, 143);
			this.buttonPlay.Name = "buttonPlay";
			this.buttonPlay.Size = new System.Drawing.Size(24, 24);
			this.buttonPlay.TabIndex = 27;
			this.buttonPlay.UseVisualStyleBackColor = true;
			// 
			// button1
			// 
			this.button1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.button1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
			this.button1.Image = global::ARCed.Properties.Resources.Edit;
			this.button1.Location = new System.Drawing.Point(212, 143);
			this.button1.Name = "button1";
			this.button1.Size = new System.Drawing.Size(24, 24);
			this.button1.TabIndex = 26;
			this.button1.UseVisualStyleBackColor = true;
			// 
			// labelMenuSE
			// 
			this.labelMenuSE.AutoSize = true;
			this.labelMenuSE.Location = new System.Drawing.Point(3, 130);
			this.labelMenuSE.Name = "labelMenuSE";
			this.labelMenuSE.Size = new System.Drawing.Size(76, 13);
			this.labelMenuSE.TabIndex = 5;
			this.labelMenuSE.Text = "Menu Use SE:";
			// 
			// splitContainerScopeAnimation
			// 
			this.splitContainerScopeAnimation.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.splitContainerScopeAnimation.Location = new System.Drawing.Point(0, 173);
			this.splitContainerScopeAnimation.Name = "splitContainerScopeAnimation";
			// 
			// splitContainerScopeAnimation.Panel1
			// 
			this.splitContainerScopeAnimation.Panel1.Controls.Add(this.comboBoxCommonEvent);
			this.splitContainerScopeAnimation.Panel1.Controls.Add(this.labelCommonEvent);
			this.splitContainerScopeAnimation.Panel1.Controls.Add(this.comboBoxUserAnimation);
			this.splitContainerScopeAnimation.Panel1.Controls.Add(this.label3);
			this.splitContainerScopeAnimation.Panel1.Controls.Add(this.comboBoxScope);
			this.splitContainerScopeAnimation.Panel1.Controls.Add(this.labelScope);
			// 
			// splitContainerScopeAnimation.Panel2
			// 
			this.splitContainerScopeAnimation.Panel2.Controls.Add(this.comboBoxTargetAnimation);
			this.splitContainerScopeAnimation.Panel2.Controls.Add(this.label4);
			this.splitContainerScopeAnimation.Panel2.Controls.Add(this.comboBoxOccasion);
			this.splitContainerScopeAnimation.Panel2.Controls.Add(this.labelOccasion);
			this.splitContainerScopeAnimation.Size = new System.Drawing.Size(240, 121);
			this.splitContainerScopeAnimation.SplitterDistance = 119;
			this.splitContainerScopeAnimation.TabIndex = 25;
			// 
			// comboBoxCommonEvent
			// 
			this.comboBoxCommonEvent.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxCommonEvent.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxCommonEvent.FormattingEnabled = true;
			this.comboBoxCommonEvent.Location = new System.Drawing.Point(6, 96);
			this.comboBoxCommonEvent.Name = "comboBoxCommonEvent";
			this.comboBoxCommonEvent.Size = new System.Drawing.Size(110, 21);
			this.comboBoxCommonEvent.TabIndex = 5;
			this.comboBoxCommonEvent.SelectedIndexChanged += new System.EventHandler(this.comboBoxCommonEvent_SelectedIndexChanged);
			// 
			// labelCommonEvent
			// 
			this.labelCommonEvent.AutoSize = true;
			this.labelCommonEvent.Location = new System.Drawing.Point(3, 80);
			this.labelCommonEvent.Name = "labelCommonEvent";
			this.labelCommonEvent.Size = new System.Drawing.Size(82, 13);
			this.labelCommonEvent.TabIndex = 6;
			this.labelCommonEvent.Text = "Common Event:";
			// 
			// comboBoxUserAnimation
			// 
			this.comboBoxUserAnimation.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxUserAnimation.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxUserAnimation.FormattingEnabled = true;
			this.comboBoxUserAnimation.Location = new System.Drawing.Point(6, 56);
			this.comboBoxUserAnimation.Name = "comboBoxUserAnimation";
			this.comboBoxUserAnimation.Size = new System.Drawing.Size(110, 21);
			this.comboBoxUserAnimation.TabIndex = 3;
			this.comboBoxUserAnimation.SelectedIndexChanged += new System.EventHandler(this.comboBoxUserAnimation_SelectedIndexChanged);
			// 
			// label3
			// 
			this.label3.AutoSize = true;
			this.label3.Location = new System.Drawing.Point(3, 40);
			this.label3.Name = "label3";
			this.label3.Size = new System.Drawing.Size(81, 13);
			this.label3.TabIndex = 2;
			this.label3.Text = "User Animation:";
			// 
			// comboBoxScope
			// 
			this.comboBoxScope.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxScope.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxScope.FormattingEnabled = true;
			this.comboBoxScope.Items.AddRange(new object[] {
            "None",
            "One Enemy",
            "All Enemies",
            "One Ally",
            "All Allies",
            "One Ally (HP 0)",
            "All Allies (HP 0)",
            "User"});
			this.comboBoxScope.Location = new System.Drawing.Point(6, 16);
			this.comboBoxScope.Name = "comboBoxScope";
			this.comboBoxScope.Size = new System.Drawing.Size(110, 21);
			this.comboBoxScope.TabIndex = 1;
			this.comboBoxScope.SelectedIndexChanged += new System.EventHandler(this.comboBoxScope_SelectedIndexChanged);
			// 
			// labelScope
			// 
			this.labelScope.AutoSize = true;
			this.labelScope.Location = new System.Drawing.Point(3, 0);
			this.labelScope.Name = "labelScope";
			this.labelScope.Size = new System.Drawing.Size(41, 13);
			this.labelScope.TabIndex = 0;
			this.labelScope.Text = "Scope:";
			// 
			// comboBoxTargetAnimation
			// 
			this.comboBoxTargetAnimation.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxTargetAnimation.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxTargetAnimation.FormattingEnabled = true;
			this.comboBoxTargetAnimation.Location = new System.Drawing.Point(6, 56);
			this.comboBoxTargetAnimation.Name = "comboBoxTargetAnimation";
			this.comboBoxTargetAnimation.Size = new System.Drawing.Size(107, 21);
			this.comboBoxTargetAnimation.TabIndex = 4;
			this.comboBoxTargetAnimation.SelectedIndexChanged += new System.EventHandler(this.comboBoxTargetAnimation_SelectedIndexChanged);
			// 
			// label4
			// 
			this.label4.AutoSize = true;
			this.label4.Location = new System.Drawing.Point(3, 40);
			this.label4.Name = "label4";
			this.label4.Size = new System.Drawing.Size(90, 13);
			this.label4.TabIndex = 3;
			this.label4.Text = "Target Animation:";
			// 
			// comboBoxOccasion
			// 
			this.comboBoxOccasion.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxOccasion.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxOccasion.FormattingEnabled = true;
			this.comboBoxOccasion.Items.AddRange(new object[] {
            "Always",
            "Only in Battle",
            "Only in Menu",
            "Never"});
			this.comboBoxOccasion.Location = new System.Drawing.Point(6, 16);
			this.comboBoxOccasion.Name = "comboBoxOccasion";
			this.comboBoxOccasion.Size = new System.Drawing.Size(107, 21);
			this.comboBoxOccasion.TabIndex = 2;
			this.comboBoxOccasion.SelectedIndexChanged += new System.EventHandler(this.comboBoxOccasion_SelectedIndexChanged);
			// 
			// labelOccasion
			// 
			this.labelOccasion.AutoSize = true;
			this.labelOccasion.Location = new System.Drawing.Point(3, 0);
			this.labelOccasion.Name = "labelOccasion";
			this.labelOccasion.Size = new System.Drawing.Size(55, 13);
			this.labelOccasion.TabIndex = 0;
			this.labelOccasion.Text = "Occasion:";
			// 
			// textBoxMenuSe
			// 
			this.textBoxMenuSe.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBoxMenuSe.BackColor = System.Drawing.SystemColors.Window;
			this.textBoxMenuSe.Location = new System.Drawing.Point(6, 146);
			this.textBoxMenuSe.Name = "textBoxMenuSe";
			this.textBoxMenuSe.ReadOnly = true;
			this.textBoxMenuSe.Size = new System.Drawing.Size(170, 20);
			this.textBoxMenuSe.TabIndex = 4;
			this.textBoxMenuSe.WordWrap = false;
			// 
			// buttonIcon
			// 
			this.buttonIcon.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonIcon.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
			this.buttonIcon.Image = global::ARCed.Properties.Resources.Edit;
			this.buttonIcon.Location = new System.Drawing.Point(212, 104);
			this.buttonIcon.Name = "buttonIcon";
			this.buttonIcon.Size = new System.Drawing.Size(24, 24);
			this.buttonIcon.TabIndex = 24;
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
			this.pictureBoxIcon.TabIndex = 23;
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
			this.textBoxIcon.Size = new System.Drawing.Size(155, 20);
			this.textBoxIcon.TabIndex = 22;
			// 
			// labelIcon
			// 
			this.labelIcon.AutoSize = true;
			this.labelIcon.Location = new System.Drawing.Point(48, 91);
			this.labelIcon.Name = "labelIcon";
			this.labelIcon.Size = new System.Drawing.Size(31, 13);
			this.labelIcon.TabIndex = 4;
			this.labelIcon.Text = "Icon:";
			// 
			// textBoxDescription
			// 
			this.textBoxDescription.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBoxDescription.Location = new System.Drawing.Point(6, 64);
			this.textBoxDescription.Name = "textBoxDescription";
			this.textBoxDescription.Size = new System.Drawing.Size(230, 20);
			this.textBoxDescription.TabIndex = 3;
			this.textBoxDescription.TextChanged += new System.EventHandler(this.textBoxDescription_TextChanged);
			// 
			// labelDescription
			// 
			this.labelDescription.AutoSize = true;
			this.labelDescription.Location = new System.Drawing.Point(3, 48);
			this.labelDescription.Name = "labelDescription";
			this.labelDescription.Size = new System.Drawing.Size(63, 13);
			this.labelDescription.TabIndex = 2;
			this.labelDescription.Text = "Description:";
			// 
			// textBoxName
			// 
			this.textBoxName.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBoxName.Location = new System.Drawing.Point(6, 25);
			this.textBoxName.Name = "textBoxName";
			this.textBoxName.Size = new System.Drawing.Size(230, 20);
			this.textBoxName.TabIndex = 1;
			this.textBoxName.TextChanged += new System.EventHandler(this.textBoxName_TextChanged);
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
			// splitContainerNotes
			// 
			this.splitContainerNotes.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainerNotes.Location = new System.Drawing.Point(0, 0);
			this.splitContainerNotes.Name = "splitContainerNotes";
			this.splitContainerNotes.Orientation = System.Windows.Forms.Orientation.Horizontal;
			// 
			// splitContainerNotes.Panel1
			// 
			this.splitContainerNotes.Panel1.Controls.Add(this.splitContainerStateElements);
			// 
			// splitContainerNotes.Panel2
			// 
			this.splitContainerNotes.Panel2.Controls.Add(this.noteTextBox);
			this.splitContainerNotes.Size = new System.Drawing.Size(287, 490);
			this.splitContainerNotes.SplitterDistance = 316;
			this.splitContainerNotes.TabIndex = 0;
			// 
			// splitContainerStateElements
			// 
			this.splitContainerStateElements.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainerStateElements.Location = new System.Drawing.Point(0, 0);
			this.splitContainerStateElements.Name = "splitContainerStateElements";
			// 
			// splitContainerStateElements.Panel1
			// 
			this.splitContainerStateElements.Panel1.Controls.Add(this.checkGroupBoxElements);
			// 
			// splitContainerStateElements.Panel2
			// 
			this.splitContainerStateElements.Panel2.Controls.Add(this.checkedListBoxStates);
			this.splitContainerStateElements.Size = new System.Drawing.Size(287, 316);
			this.splitContainerStateElements.SplitterDistance = 143;
			this.splitContainerStateElements.TabIndex = 0;
			// 
			// checkGroupBoxElements
			// 
			this.checkGroupBoxElements.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.checkGroupBoxElements.Location = new System.Drawing.Point(3, 9);
			this.checkGroupBoxElements.Name = "checkGroupBoxElements";
			this.checkGroupBoxElements.SelectedIndex = -1;
			this.checkGroupBoxElements.Size = new System.Drawing.Size(137, 304);
			this.checkGroupBoxElements.TabIndex = 0;
			this.checkGroupBoxElements.TabStop = false;
			this.checkGroupBoxElements.Text = "Elements";
			this.checkGroupBoxElements.OnCheckChange += new ARCed.Controls.CheckGroupBox.CheckChangeEventHandler(this.checkGroupBoxElements_OnCheckChange);
			this.checkGroupBoxElements.Leave += new System.EventHandler(this.checkGroup_FocusLeave);
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
			this.checkedListBoxStates.Location = new System.Drawing.Point(3, 9);
			this.checkedListBoxStates.Name = "checkedListBoxStates";
			this.checkedListBoxStates.Size = new System.Drawing.Size(134, 304);
			this.checkedListBoxStates.TabIndex = 0;
			this.checkedListBoxStates.TabStop = false;
			this.checkedListBoxStates.Text = "States";
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
			this.noteTextBox.Size = new System.Drawing.Size(281, 164);
			this.noteTextBox.TabIndex = 0;
			this.noteTextBox.NoteTextChanged += new ARCed.Controls.NoteTextBox.TextChangedEventHandler(this.noteTextBox_NoteTextChanged);
			// 
			// SkillMainForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(708, 490);
			this.Controls.Add(this.splitContainerMain);
			this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
			this.Name = "SkillMainForm";
			this.RpgTypeName = "RPG.Skill";
			this.Text = "Skills";
			this.splitContainerMain.Panel1.ResumeLayout(false);
			this.splitContainerMain.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerMain)).EndInit();
			this.splitContainerMain.ResumeLayout(false);
			this.splitContainerRight.Panel1.ResumeLayout(false);
			this.splitContainerRight.Panel1.PerformLayout();
			this.splitContainerRight.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerRight)).EndInit();
			this.splitContainerRight.ResumeLayout(false);
			this.groupBoxParameters.ResumeLayout(false);
			this.flowPanel.ResumeLayout(false);
			this.splitContainerScopeAnimation.Panel1.ResumeLayout(false);
			this.splitContainerScopeAnimation.Panel1.PerformLayout();
			this.splitContainerScopeAnimation.Panel2.ResumeLayout(false);
			this.splitContainerScopeAnimation.Panel2.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerScopeAnimation)).EndInit();
			this.splitContainerScopeAnimation.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.pictureBoxIcon)).EndInit();
			this.splitContainerNotes.Panel1.ResumeLayout(false);
			this.splitContainerNotes.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerNotes)).EndInit();
			this.splitContainerNotes.ResumeLayout(false);
			this.splitContainerStateElements.Panel1.ResumeLayout(false);
			this.splitContainerStateElements.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerStateElements)).EndInit();
			this.splitContainerStateElements.ResumeLayout(false);
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.SplitContainer splitContainerMain;
		private System.Windows.Forms.SplitContainer splitContainerRight;
		private Controls.DatabaseObjectListBox dataObjectList;
		private System.Windows.Forms.Label labelName;
		private System.Windows.Forms.TextBox textBoxDescription;
		private System.Windows.Forms.Label labelDescription;
		private System.Windows.Forms.TextBox textBoxName;
		private System.Windows.Forms.Label labelIcon;
		private System.Windows.Forms.PictureBox pictureBoxIcon;
		private System.Windows.Forms.TextBox textBoxIcon;
		private System.Windows.Forms.SplitContainer splitContainerNotes;
		private Controls.NoteTextBox noteTextBox;
		private System.Windows.Forms.SplitContainer splitContainerStateElements;
		private Controls.CheckGroupBox checkGroupBoxElements;
		private System.Windows.Forms.Button buttonIcon;
		private System.Windows.Forms.SplitContainer splitContainerScopeAnimation;
		private System.Windows.Forms.ComboBox comboBoxUserAnimation;
		private System.Windows.Forms.Label label3;
		private System.Windows.Forms.ComboBox comboBoxScope;
		private System.Windows.Forms.Label labelScope;
		private System.Windows.Forms.ComboBox comboBoxTargetAnimation;
		private System.Windows.Forms.Label label4;
		private System.Windows.Forms.ComboBox comboBoxOccasion;
		private System.Windows.Forms.Label labelOccasion;
		private System.Windows.Forms.Label labelMenuSE;
		private System.Windows.Forms.TextBox textBoxMenuSe;
		private System.Windows.Forms.Label labelCommonEvent;
		private System.Windows.Forms.ComboBox comboBoxCommonEvent;
		private System.Windows.Forms.Button buttonPlay;
		private System.Windows.Forms.Button button1;
		private System.Windows.Forms.GroupBox groupBoxParameters;
		private System.Windows.Forms.FlowLayoutPanel flowPanel;
		private Controls.ParamBox paramBoxSpCost;
		private Controls.ParamBox paramBoxPower;
		private Controls.ParamBox paramBoxHitRate;
		private Controls.ParamBox paramBoxVariance;
		private Controls.ParamBox paramBoxAtk;
		private Controls.ParamBox paramBoxEva;
		private Controls.ParamBox paramBoxPdef;
		private Controls.ParamBox paramBoxMdef;
		private Controls.ParamBox paramBoxStr;
		private Controls.ParamBox paramBoxDex;
		private Controls.ParamBox paramBoxAgi;
		private Controls.ParamBox paramBoxInt;
		private Controls.MultiStateCheckedListBox checkedListBoxStates;

	}
}