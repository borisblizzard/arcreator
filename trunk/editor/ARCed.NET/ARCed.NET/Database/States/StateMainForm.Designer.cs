namespace ARCed.Database.States
{
	sealed partial class StateMainForm
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
			this.splitContainer1 = new System.Windows.Forms.SplitContainer();
			this.groupBoxParameters = new System.Windows.Forms.GroupBox();
			this.flowPanelParameters = new System.Windows.Forms.FlowLayoutPanel();
			this.paramBoxRating = new ARCed.Controls.ParamBox();
			this.paramBoxHitRate = new ARCed.Controls.ParamBox();
			this.paramBoxMaxHP = new ARCed.Controls.ParamBox();
			this.paramBoxMaxSP = new ARCed.Controls.ParamBox();
			this.paramBoxStr = new ARCed.Controls.ParamBox();
			this.paramBoxDex = new ARCed.Controls.ParamBox();
			this.paramBoxAgi = new ARCed.Controls.ParamBox();
			this.paramBoxInt = new ARCed.Controls.ParamBox();
			this.paramBoxAtk = new ARCed.Controls.ParamBox();
			this.paramBoxPdef = new ARCed.Controls.ParamBox();
			this.paramBoxMdef = new ARCed.Controls.ParamBox();
			this.paramBoxEva = new ARCed.Controls.ParamBox();
			this.groupBoxReleaseConditions = new System.Windows.Forms.GroupBox();
			this.labelChance2 = new System.Windows.Forms.Label();
			this.numericDamageChance = new System.Windows.Forms.NumericUpDown();
			this.labelPhysDamage = new System.Windows.Forms.Label();
			this.labelChance1 = new System.Windows.Forms.Label();
			this.numericTurnChance = new System.Windows.Forms.NumericUpDown();
			this.labelTurns = new System.Windows.Forms.Label();
			this.labelAfter = new System.Windows.Forms.Label();
			this.numericTurns = new System.Windows.Forms.NumericUpDown();
			this.checkBoxReleaseEndBattle = new System.Windows.Forms.CheckBox();
			this.comboBoxRestriction = new System.Windows.Forms.ComboBox();
			this.comboBoxAnimation = new System.Windows.Forms.ComboBox();
			this.labelRestriction = new System.Windows.Forms.Label();
			this.labelAnimation = new System.Windows.Forms.Label();
			this.groupBoxFlags = new System.Windows.Forms.GroupBox();
			this.checkBoxSlipDamage = new System.Windows.Forms.CheckBox();
			this.checkBoxNoEvade = new System.Windows.Forms.CheckBox();
			this.checkBoxNoExp = new System.Windows.Forms.CheckBox();
			this.checkBoxRegardHp0 = new System.Windows.Forms.CheckBox();
			this.checkBoxNonrestistance = new System.Windows.Forms.CheckBox();
			this.textBoxName = new System.Windows.Forms.TextBox();
			this.labelName = new System.Windows.Forms.Label();
			this.splitContainerNotes = new System.Windows.Forms.SplitContainer();
			this.splitContainerElementsStates = new System.Windows.Forms.SplitContainer();
			this.checkGroupBoxElements = new ARCed.Controls.CheckGroupBox(this.components);
			this.checkedListBoxStates = new ARCed.Controls.MultiStateCheckedListBox();
			this.noteTextBox = new ARCed.Controls.NoteTextBox();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerMain)).BeginInit();
			this.splitContainerMain.Panel1.SuspendLayout();
			this.splitContainerMain.Panel2.SuspendLayout();
			this.splitContainerMain.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).BeginInit();
			this.splitContainer1.Panel1.SuspendLayout();
			this.splitContainer1.Panel2.SuspendLayout();
			this.splitContainer1.SuspendLayout();
			this.groupBoxParameters.SuspendLayout();
			this.flowPanelParameters.SuspendLayout();
			this.groupBoxReleaseConditions.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.numericDamageChance)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.numericTurnChance)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.numericTurns)).BeginInit();
			this.groupBoxFlags.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerNotes)).BeginInit();
			this.splitContainerNotes.Panel1.SuspendLayout();
			this.splitContainerNotes.Panel2.SuspendLayout();
			this.splitContainerNotes.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerElementsStates)).BeginInit();
			this.splitContainerElementsStates.Panel1.SuspendLayout();
			this.splitContainerElementsStates.Panel2.SuspendLayout();
			this.splitContainerElementsStates.SuspendLayout();
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
			this.splitContainerMain.Panel2.Controls.Add(this.splitContainer1);
			this.splitContainerMain.Size = new System.Drawing.Size(784, 562);
			this.splitContainerMain.SplitterDistance = 199;
			this.splitContainerMain.TabIndex = 1;
			// 
			// dataObjectList
			// 
			this.dataObjectList.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.dataObjectList.HeaderText = "States";
			this.dataObjectList.Location = new System.Drawing.Point(3, 3);
			this.dataObjectList.Name = "dataObjectList";
			this.dataObjectList.SelectedIndex = -1;
			this.dataObjectList.Size = new System.Drawing.Size(193, 556);
			this.dataObjectList.TabIndex = 0;
			this.dataObjectList.TabStop = false;
			this.dataObjectList.OnListBoxIndexChanged += new ARCed.Controls.DatabaseObjectListBox.ObjectListIndexChangedEventHandler(this.dataObjectList_OnListBoxIndexChanged);
			// 
			// splitContainer1
			// 
			this.splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainer1.Location = new System.Drawing.Point(0, 0);
			this.splitContainer1.Name = "splitContainer1";
			// 
			// splitContainer1.Panel1
			// 
			this.splitContainer1.Panel1.Controls.Add(this.groupBoxParameters);
			this.splitContainer1.Panel1.Controls.Add(this.groupBoxReleaseConditions);
			this.splitContainer1.Panel1.Controls.Add(this.comboBoxRestriction);
			this.splitContainer1.Panel1.Controls.Add(this.comboBoxAnimation);
			this.splitContainer1.Panel1.Controls.Add(this.labelRestriction);
			this.splitContainer1.Panel1.Controls.Add(this.labelAnimation);
			this.splitContainer1.Panel1.Controls.Add(this.groupBoxFlags);
			this.splitContainer1.Panel1.Controls.Add(this.textBoxName);
			this.splitContainer1.Panel1.Controls.Add(this.labelName);
			// 
			// splitContainer1.Panel2
			// 
			this.splitContainer1.Panel2.Controls.Add(this.splitContainerNotes);
			this.splitContainer1.Size = new System.Drawing.Size(581, 562);
			this.splitContainer1.SplitterDistance = 291;
			this.splitContainer1.TabIndex = 0;
			// 
			// groupBoxParameters
			// 
			this.groupBoxParameters.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxParameters.Controls.Add(this.flowPanelParameters);
			this.groupBoxParameters.Location = new System.Drawing.Point(6, 257);
			this.groupBoxParameters.Name = "groupBoxParameters";
			this.groupBoxParameters.Size = new System.Drawing.Size(282, 302);
			this.groupBoxParameters.TabIndex = 10;
			this.groupBoxParameters.TabStop = false;
			this.groupBoxParameters.Text = "Parameters";
			// 
			// flowPanelParameters
			// 
			this.flowPanelParameters.AutoScroll = true;
			this.flowPanelParameters.Controls.Add(this.paramBoxRating);
			this.flowPanelParameters.Controls.Add(this.paramBoxHitRate);
			this.flowPanelParameters.Controls.Add(this.paramBoxMaxHP);
			this.flowPanelParameters.Controls.Add(this.paramBoxMaxSP);
			this.flowPanelParameters.Controls.Add(this.paramBoxStr);
			this.flowPanelParameters.Controls.Add(this.paramBoxDex);
			this.flowPanelParameters.Controls.Add(this.paramBoxAgi);
			this.flowPanelParameters.Controls.Add(this.paramBoxInt);
			this.flowPanelParameters.Controls.Add(this.paramBoxAtk);
			this.flowPanelParameters.Controls.Add(this.paramBoxPdef);
			this.flowPanelParameters.Controls.Add(this.paramBoxMdef);
			this.flowPanelParameters.Controls.Add(this.paramBoxEva);
			this.flowPanelParameters.Dock = System.Windows.Forms.DockStyle.Fill;
			this.flowPanelParameters.Location = new System.Drawing.Point(3, 16);
			this.flowPanelParameters.Name = "flowPanelParameters";
			this.flowPanelParameters.Size = new System.Drawing.Size(276, 283);
			this.flowPanelParameters.TabIndex = 0;
			// 
			// paramBoxRating
			// 
			this.paramBoxRating.Location = new System.Drawing.Point(3, 3);
			this.paramBoxRating.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
			this.paramBoxRating.Minimum = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxRating.Name = "paramBoxRating";
			this.paramBoxRating.ParameterIndex = 0;
			this.paramBoxRating.ParameterLabel = "Rating:";
			this.paramBoxRating.RpgAttribute = "rating";
			this.paramBoxRating.Size = new System.Drawing.Size(67, 37);
			this.paramBoxRating.TabIndex = 0;
			this.paramBoxRating.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxRating.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.ParamBoxOnValueChanged);
			// 
			// paramBoxHitRate
			// 
			this.paramBoxHitRate.Location = new System.Drawing.Point(76, 3);
			this.paramBoxHitRate.Maximum = new decimal(new int[] {
            200,
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
			this.paramBoxHitRate.ParameterLabel = "Hit Rate %:";
			this.paramBoxHitRate.RpgAttribute = "hit_rate";
			this.paramBoxHitRate.Size = new System.Drawing.Size(67, 37);
			this.paramBoxHitRate.TabIndex = 1;
			this.paramBoxHitRate.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxHitRate.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.ParamBoxOnValueChanged);
			// 
			// paramBoxMaxHP
			// 
			this.paramBoxMaxHP.Location = new System.Drawing.Point(149, 3);
			this.paramBoxMaxHP.Maximum = new decimal(new int[] {
            200,
            0,
            0,
            0});
			this.paramBoxMaxHP.Minimum = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxMaxHP.Name = "paramBoxMaxHP";
			this.paramBoxMaxHP.ParameterIndex = 0;
			this.paramBoxMaxHP.ParameterLabel = "MaxHP %:";
			this.paramBoxMaxHP.RpgAttribute = "maxhp_rate";
			this.paramBoxMaxHP.Size = new System.Drawing.Size(67, 37);
			this.paramBoxMaxHP.TabIndex = 2;
			this.paramBoxMaxHP.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxMaxHP.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.ParamBoxOnValueChanged);
			// 
			// paramBoxMaxSP
			// 
			this.paramBoxMaxSP.Location = new System.Drawing.Point(3, 46);
			this.paramBoxMaxSP.Maximum = new decimal(new int[] {
            200,
            0,
            0,
            0});
			this.paramBoxMaxSP.Minimum = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxMaxSP.Name = "paramBoxMaxSP";
			this.paramBoxMaxSP.ParameterIndex = 0;
			this.paramBoxMaxSP.ParameterLabel = "MaxSP %:";
			this.paramBoxMaxSP.RpgAttribute = "maxsp_rate";
			this.paramBoxMaxSP.Size = new System.Drawing.Size(67, 37);
			this.paramBoxMaxSP.TabIndex = 3;
			this.paramBoxMaxSP.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxMaxSP.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.ParamBoxOnValueChanged);
			// 
			// paramBoxStr
			// 
			this.paramBoxStr.Location = new System.Drawing.Point(76, 46);
			this.paramBoxStr.Maximum = new decimal(new int[] {
            200,
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
			this.paramBoxStr.ParameterLabel = "STR %:";
			this.paramBoxStr.RpgAttribute = "str_rate";
			this.paramBoxStr.Size = new System.Drawing.Size(67, 37);
			this.paramBoxStr.TabIndex = 4;
			this.paramBoxStr.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxStr.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.ParamBoxOnValueChanged);
			// 
			// paramBoxDex
			// 
			this.paramBoxDex.Location = new System.Drawing.Point(149, 46);
			this.paramBoxDex.Maximum = new decimal(new int[] {
            200,
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
			this.paramBoxDex.ParameterLabel = "DEX %:";
			this.paramBoxDex.RpgAttribute = "dex_rate";
			this.paramBoxDex.Size = new System.Drawing.Size(67, 37);
			this.paramBoxDex.TabIndex = 5;
			this.paramBoxDex.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxDex.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.ParamBoxOnValueChanged);
			// 
			// paramBoxAgi
			// 
			this.paramBoxAgi.Location = new System.Drawing.Point(3, 89);
			this.paramBoxAgi.Maximum = new decimal(new int[] {
            200,
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
			this.paramBoxAgi.ParameterLabel = "AGI %:";
			this.paramBoxAgi.RpgAttribute = "agi_rate";
			this.paramBoxAgi.Size = new System.Drawing.Size(67, 37);
			this.paramBoxAgi.TabIndex = 6;
			this.paramBoxAgi.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxAgi.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.ParamBoxOnValueChanged);
			// 
			// paramBoxInt
			// 
			this.paramBoxInt.Location = new System.Drawing.Point(76, 89);
			this.paramBoxInt.Maximum = new decimal(new int[] {
            200,
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
			this.paramBoxInt.ParameterLabel = "INT %:";
			this.paramBoxInt.RpgAttribute = "int_rate";
			this.paramBoxInt.Size = new System.Drawing.Size(67, 37);
			this.paramBoxInt.TabIndex = 7;
			this.paramBoxInt.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxInt.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.ParamBoxOnValueChanged);
			// 
			// paramBoxAtk
			// 
			this.paramBoxAtk.Location = new System.Drawing.Point(149, 89);
			this.paramBoxAtk.Maximum = new decimal(new int[] {
            200,
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
			this.paramBoxAtk.ParameterLabel = "ATK %:";
			this.paramBoxAtk.RpgAttribute = "atk_rate";
			this.paramBoxAtk.Size = new System.Drawing.Size(67, 37);
			this.paramBoxAtk.TabIndex = 8;
			this.paramBoxAtk.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxAtk.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.ParamBoxOnValueChanged);
			// 
			// paramBoxPdef
			// 
			this.paramBoxPdef.Location = new System.Drawing.Point(3, 132);
			this.paramBoxPdef.Maximum = new decimal(new int[] {
            200,
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
			this.paramBoxPdef.ParameterLabel = "PDEF %:";
			this.paramBoxPdef.RpgAttribute = "pdef_rate";
			this.paramBoxPdef.Size = new System.Drawing.Size(67, 37);
			this.paramBoxPdef.TabIndex = 9;
			this.paramBoxPdef.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxPdef.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.ParamBoxOnValueChanged);
			// 
			// paramBoxMdef
			// 
			this.paramBoxMdef.Location = new System.Drawing.Point(76, 132);
			this.paramBoxMdef.Maximum = new decimal(new int[] {
            200,
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
			this.paramBoxMdef.ParameterLabel = "MDEF %:";
			this.paramBoxMdef.RpgAttribute = "mdef__rate";
			this.paramBoxMdef.Size = new System.Drawing.Size(67, 37);
			this.paramBoxMdef.TabIndex = 10;
			this.paramBoxMdef.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxMdef.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.ParamBoxOnValueChanged);
			// 
			// paramBoxEva
			// 
			this.paramBoxEva.Location = new System.Drawing.Point(149, 132);
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
			this.paramBoxEva.ParameterLabel = "EVA:";
			this.paramBoxEva.RpgAttribute = "eva";
			this.paramBoxEva.Size = new System.Drawing.Size(67, 37);
			this.paramBoxEva.TabIndex = 11;
			this.paramBoxEva.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
			this.paramBoxEva.OnValueChanged += new ARCed.Controls.ParamBox.ValueChangedEventHandler(this.ParamBoxOnValueChanged);
			// 
			// groupBoxReleaseConditions
			// 
			this.groupBoxReleaseConditions.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxReleaseConditions.Controls.Add(this.labelChance2);
			this.groupBoxReleaseConditions.Controls.Add(this.numericDamageChance);
			this.groupBoxReleaseConditions.Controls.Add(this.labelPhysDamage);
			this.groupBoxReleaseConditions.Controls.Add(this.labelChance1);
			this.groupBoxReleaseConditions.Controls.Add(this.numericTurnChance);
			this.groupBoxReleaseConditions.Controls.Add(this.labelTurns);
			this.groupBoxReleaseConditions.Controls.Add(this.labelAfter);
			this.groupBoxReleaseConditions.Controls.Add(this.numericTurns);
			this.groupBoxReleaseConditions.Controls.Add(this.checkBoxReleaseEndBattle);
			this.groupBoxReleaseConditions.Location = new System.Drawing.Point(6, 148);
			this.groupBoxReleaseConditions.Name = "groupBoxReleaseConditions";
			this.groupBoxReleaseConditions.Size = new System.Drawing.Size(282, 103);
			this.groupBoxReleaseConditions.TabIndex = 9;
			this.groupBoxReleaseConditions.TabStop = false;
			this.groupBoxReleaseConditions.Text = "Release Conditions";
			// 
			// labelChance2
			// 
			this.labelChance2.Location = new System.Drawing.Point(208, 70);
			this.labelChance2.Name = "labelChance2";
			this.labelChance2.Size = new System.Drawing.Size(67, 20);
			this.labelChance2.TabIndex = 8;
			this.labelChance2.Text = "% chance.";
			this.labelChance2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
			// 
			// numericDamageChance
			// 
			this.numericDamageChance.Location = new System.Drawing.Point(156, 70);
			this.numericDamageChance.Name = "numericDamageChance";
			this.numericDamageChance.Size = new System.Drawing.Size(46, 20);
			this.numericDamageChance.TabIndex = 7;
			this.numericDamageChance.ValueChanged += new System.EventHandler(this.NumericDamageChanceValueChanged);
			// 
			// labelPhysDamage
			// 
			this.labelPhysDamage.Location = new System.Drawing.Point(6, 70);
			this.labelPhysDamage.Name = "labelPhysDamage";
			this.labelPhysDamage.Size = new System.Drawing.Size(144, 20);
			this.labelPhysDamage.TabIndex = 6;
			this.labelPhysDamage.Text = "Each physical damage deal,";
			this.labelPhysDamage.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
			// 
			// labelChance1
			// 
			this.labelChance1.Location = new System.Drawing.Point(208, 44);
			this.labelChance1.Name = "labelChance1";
			this.labelChance1.Size = new System.Drawing.Size(67, 20);
			this.labelChance1.TabIndex = 5;
			this.labelChance1.Text = "% chance.";
			this.labelChance1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
			// 
			// numericTurnChance
			// 
			this.numericTurnChance.Location = new System.Drawing.Point(156, 44);
			this.numericTurnChance.Name = "numericTurnChance";
			this.numericTurnChance.Size = new System.Drawing.Size(46, 20);
			this.numericTurnChance.TabIndex = 4;
			this.numericTurnChance.ValueChanged += new System.EventHandler(this.NumericTurnChanceValueChanged);
			// 
			// labelTurns
			// 
			this.labelTurns.Location = new System.Drawing.Point(115, 44);
			this.labelTurns.Name = "labelTurns";
			this.labelTurns.Size = new System.Drawing.Size(35, 20);
			this.labelTurns.TabIndex = 3;
			this.labelTurns.Text = "turns,";
			this.labelTurns.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// labelAfter
			// 
			this.labelAfter.Location = new System.Drawing.Point(6, 44);
			this.labelAfter.Name = "labelAfter";
			this.labelAfter.Size = new System.Drawing.Size(35, 20);
			this.labelAfter.TabIndex = 2;
			this.labelAfter.Text = "After";
			this.labelAfter.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
			// 
			// numericTurns
			// 
			this.numericTurns.Location = new System.Drawing.Point(47, 44);
			this.numericTurns.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
			this.numericTurns.Name = "numericTurns";
			this.numericTurns.Size = new System.Drawing.Size(62, 20);
			this.numericTurns.TabIndex = 1;
			this.numericTurns.ValueChanged += new System.EventHandler(this.NumericTurnsValueChanged);
			// 
			// checkBoxReleaseEndBattle
			// 
			this.checkBoxReleaseEndBattle.AutoSize = true;
			this.checkBoxReleaseEndBattle.Location = new System.Drawing.Point(6, 19);
			this.checkBoxReleaseEndBattle.Name = "checkBoxReleaseEndBattle";
			this.checkBoxReleaseEndBattle.Size = new System.Drawing.Size(157, 17);
			this.checkBoxReleaseEndBattle.TabIndex = 0;
			this.checkBoxReleaseEndBattle.Text = "Release at the end of battle";
			this.checkBoxReleaseEndBattle.UseVisualStyleBackColor = true;
			// 
			// comboBoxRestriction
			// 
			this.comboBoxRestriction.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxRestriction.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxRestriction.FormattingEnabled = true;
			this.comboBoxRestriction.Items.AddRange(new object[] {
            "<None>",
            "Can\'t use magic",
            "Always attack enemies",
            "Always attack allies",
            "Can\'t Move"});
			this.comboBoxRestriction.Location = new System.Drawing.Point(6, 121);
			this.comboBoxRestriction.Name = "comboBoxRestriction";
			this.comboBoxRestriction.Size = new System.Drawing.Size(161, 21);
			this.comboBoxRestriction.TabIndex = 8;
			this.comboBoxRestriction.SelectedIndexChanged += new System.EventHandler(this.ComboBoxRestrictionSelectedIndexChanged);
			// 
			// comboBoxAnimation
			// 
			this.comboBoxAnimation.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxAnimation.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxAnimation.FormattingEnabled = true;
			this.comboBoxAnimation.Location = new System.Drawing.Point(6, 73);
			this.comboBoxAnimation.Name = "comboBoxAnimation";
			this.comboBoxAnimation.Size = new System.Drawing.Size(161, 21);
			this.comboBoxAnimation.TabIndex = 7;
			this.comboBoxAnimation.SelectedValueChanged += new System.EventHandler(this.ComboBoxAnimationSelectedValueChanged);
			// 
			// labelRestriction
			// 
			this.labelRestriction.AutoSize = true;
			this.labelRestriction.Location = new System.Drawing.Point(3, 105);
			this.labelRestriction.Name = "labelRestriction";
			this.labelRestriction.Size = new System.Drawing.Size(60, 13);
			this.labelRestriction.TabIndex = 6;
			this.labelRestriction.Text = "Restriction:";
			// 
			// labelAnimation
			// 
			this.labelAnimation.AutoSize = true;
			this.labelAnimation.Location = new System.Drawing.Point(3, 57);
			this.labelAnimation.Name = "labelAnimation";
			this.labelAnimation.Size = new System.Drawing.Size(56, 13);
			this.labelAnimation.TabIndex = 5;
			this.labelAnimation.Text = "Animation:";
			// 
			// groupBoxFlags
			// 
			this.groupBoxFlags.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxFlags.Controls.Add(this.checkBoxSlipDamage);
			this.groupBoxFlags.Controls.Add(this.checkBoxNoEvade);
			this.groupBoxFlags.Controls.Add(this.checkBoxNoExp);
			this.groupBoxFlags.Controls.Add(this.checkBoxRegardHp0);
			this.groupBoxFlags.Controls.Add(this.checkBoxNonrestistance);
			this.groupBoxFlags.Location = new System.Drawing.Point(173, 3);
			this.groupBoxFlags.Name = "groupBoxFlags";
			this.groupBoxFlags.Size = new System.Drawing.Size(115, 139);
			this.groupBoxFlags.TabIndex = 4;
			this.groupBoxFlags.TabStop = false;
			// 
			// checkBoxSlipDamage
			// 
			this.checkBoxSlipDamage.AutoSize = true;
			this.checkBoxSlipDamage.Location = new System.Drawing.Point(6, 111);
			this.checkBoxSlipDamage.Name = "checkBoxSlipDamage";
			this.checkBoxSlipDamage.Size = new System.Drawing.Size(86, 17);
			this.checkBoxSlipDamage.TabIndex = 4;
			this.checkBoxSlipDamage.Text = "Slip Damage";
			this.checkBoxSlipDamage.UseVisualStyleBackColor = true;
			// 
			// checkBoxNoEvade
			// 
			this.checkBoxNoEvade.AutoSize = true;
			this.checkBoxNoEvade.Location = new System.Drawing.Point(6, 88);
			this.checkBoxNoEvade.Name = "checkBoxNoEvade";
			this.checkBoxNoEvade.Size = new System.Drawing.Size(84, 17);
			this.checkBoxNoEvade.TabIndex = 3;
			this.checkBoxNoEvade.Text = "Can\'t Evade";
			this.checkBoxNoEvade.UseVisualStyleBackColor = true;
			// 
			// checkBoxNoExp
			// 
			this.checkBoxNoExp.AutoSize = true;
			this.checkBoxNoExp.Location = new System.Drawing.Point(6, 65);
			this.checkBoxNoExp.Name = "checkBoxNoExp";
			this.checkBoxNoExp.Size = new System.Drawing.Size(92, 17);
			this.checkBoxNoExp.TabIndex = 2;
			this.checkBoxNoExp.Text = "Can\'t get EXP";
			this.checkBoxNoExp.UseVisualStyleBackColor = true;
			// 
			// checkBoxRegardHp0
			// 
			this.checkBoxRegardHp0.AutoSize = true;
			this.checkBoxRegardHp0.Location = new System.Drawing.Point(6, 42);
			this.checkBoxRegardHp0.Name = "checkBoxRegardHp0";
			this.checkBoxRegardHp0.Size = new System.Drawing.Size(102, 17);
			this.checkBoxRegardHp0.TabIndex = 1;
			this.checkBoxRegardHp0.Text = "Regard as HP 0";
			this.checkBoxRegardHp0.UseVisualStyleBackColor = true;
			// 
			// checkBoxNonrestistance
			// 
			this.checkBoxNonrestistance.AutoSize = true;
			this.checkBoxNonrestistance.Location = new System.Drawing.Point(6, 19);
			this.checkBoxNonrestistance.Name = "checkBoxNonrestistance";
			this.checkBoxNonrestistance.Size = new System.Drawing.Size(94, 17);
			this.checkBoxNonrestistance.TabIndex = 0;
			this.checkBoxNonrestistance.Text = "Nonresistance";
			this.checkBoxNonrestistance.UseVisualStyleBackColor = true;
			// 
			// textBoxName
			// 
			this.textBoxName.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBoxName.Location = new System.Drawing.Point(6, 25);
			this.textBoxName.Name = "textBoxName";
			this.textBoxName.Size = new System.Drawing.Size(161, 20);
			this.textBoxName.TabIndex = 3;
			this.textBoxName.TextChanged += new System.EventHandler(this.TextBoxNameTextChanged);
			// 
			// labelName
			// 
			this.labelName.AutoSize = true;
			this.labelName.Location = new System.Drawing.Point(3, 9);
			this.labelName.Name = "labelName";
			this.labelName.Size = new System.Drawing.Size(38, 13);
			this.labelName.TabIndex = 2;
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
			this.splitContainerNotes.Panel1.Controls.Add(this.splitContainerElementsStates);
			// 
			// splitContainerNotes.Panel2
			// 
			this.splitContainerNotes.Panel2.Controls.Add(this.noteTextBox);
			this.splitContainerNotes.Size = new System.Drawing.Size(286, 562);
			this.splitContainerNotes.SplitterDistance = 394;
			this.splitContainerNotes.TabIndex = 0;
			// 
			// splitContainerElementsStates
			// 
			this.splitContainerElementsStates.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainerElementsStates.Location = new System.Drawing.Point(0, 0);
			this.splitContainerElementsStates.Name = "splitContainerElementsStates";
			// 
			// splitContainerElementsStates.Panel1
			// 
			this.splitContainerElementsStates.Panel1.Controls.Add(this.checkGroupBoxElements);
			// 
			// splitContainerElementsStates.Panel2
			// 
			this.splitContainerElementsStates.Panel2.Controls.Add(this.checkedListBoxStates);
			this.splitContainerElementsStates.Size = new System.Drawing.Size(286, 394);
			this.splitContainerElementsStates.SplitterDistance = 138;
			this.splitContainerElementsStates.TabIndex = 0;
			// 
			// checkGroupBoxElements
			// 
			this.checkGroupBoxElements.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.checkGroupBoxElements.Location = new System.Drawing.Point(3, 3);
			this.checkGroupBoxElements.Name = "checkGroupBoxElements";
			this.checkGroupBoxElements.SelectedIndex = -1;
			this.checkGroupBoxElements.Size = new System.Drawing.Size(132, 388);
			this.checkGroupBoxElements.TabIndex = 0;
			this.checkGroupBoxElements.TabStop = false;
			this.checkGroupBoxElements.Text = "Element Defense:";
			this.checkGroupBoxElements.OnCheckChange += new ARCed.Controls.CheckGroupBox.CheckChangeEventHandler(this.CheckGroupBoxElementsCheckChanged);
			// 
			// checkedListBoxStates
			// 
			this.checkedListBoxStates.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.checkedListBoxStates.Colors = new System.Drawing.Color[] {
        System.Drawing.Color.Transparent,
        System.Drawing.Color.Red,
        System.Drawing.Color.Blue};
			this.checkedListBoxStates.Items = new string[] {
        " ",
        "+",
        "-"};
			this.checkedListBoxStates.Location = new System.Drawing.Point(3, 3);
			this.checkedListBoxStates.Name = "checkedListBoxStates";
			this.checkedListBoxStates.Size = new System.Drawing.Size(138, 388);
			this.checkedListBoxStates.TabIndex = 0;
			this.checkedListBoxStates.TabStop = false;
			this.checkedListBoxStates.Text = "State Change";
			this.checkedListBoxStates.OnItemChanged += new ARCed.Controls.MultiStateCheckedListBox.ItemValueChangedEventHandler(this.CheckedListBoxStatesItemChanged);
			// 
			// noteTextBox
			// 
			this.noteTextBox.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.noteTextBox.Location = new System.Drawing.Point(3, 3);
			this.noteTextBox.Name = "noteTextBox";
			this.noteTextBox.NoteText = "";
			this.noteTextBox.Size = new System.Drawing.Size(280, 158);
			this.noteTextBox.TabIndex = 0;
			this.noteTextBox.NoteTextChanged += new ARCed.Controls.NoteTextBox.TextChangedEventHandler(this.NoteTextBoxNoteTextChanged);
			// 
			// StateMainForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(784, 562);
			this.Controls.Add(this.splitContainerMain);
			this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.Name = "StateMainForm";
			this.RpgTypeName = "RPG.State";
			this.Text = "States";
			this.splitContainerMain.Panel1.ResumeLayout(false);
			this.splitContainerMain.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerMain)).EndInit();
			this.splitContainerMain.ResumeLayout(false);
			this.splitContainer1.Panel1.ResumeLayout(false);
			this.splitContainer1.Panel1.PerformLayout();
			this.splitContainer1.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).EndInit();
			this.splitContainer1.ResumeLayout(false);
			this.groupBoxParameters.ResumeLayout(false);
			this.flowPanelParameters.ResumeLayout(false);
			this.groupBoxReleaseConditions.ResumeLayout(false);
			this.groupBoxReleaseConditions.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.numericDamageChance)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.numericTurnChance)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.numericTurns)).EndInit();
			this.groupBoxFlags.ResumeLayout(false);
			this.groupBoxFlags.PerformLayout();
			this.splitContainerNotes.Panel1.ResumeLayout(false);
			this.splitContainerNotes.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerNotes)).EndInit();
			this.splitContainerNotes.ResumeLayout(false);
			this.splitContainerElementsStates.Panel1.ResumeLayout(false);
			this.splitContainerElementsStates.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerElementsStates)).EndInit();
			this.splitContainerElementsStates.ResumeLayout(false);
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.SplitContainer splitContainerMain;
		private System.Windows.Forms.SplitContainer splitContainer1;
		private System.Windows.Forms.SplitContainer splitContainerNotes;
		private System.Windows.Forms.SplitContainer splitContainerElementsStates;
		private Controls.MultiStateCheckedListBox checkedListBoxStates;
		private Controls.NoteTextBox noteTextBox;
		private System.Windows.Forms.TextBox textBoxName;
		private System.Windows.Forms.Label labelName;
		private Controls.DatabaseObjectListBox dataObjectList;
		private System.Windows.Forms.GroupBox groupBoxParameters;
		private System.Windows.Forms.GroupBox groupBoxReleaseConditions;
		private System.Windows.Forms.CheckBox checkBoxReleaseEndBattle;
		private System.Windows.Forms.ComboBox comboBoxRestriction;
		private System.Windows.Forms.ComboBox comboBoxAnimation;
		private System.Windows.Forms.Label labelRestriction;
		private System.Windows.Forms.Label labelAnimation;
		private System.Windows.Forms.GroupBox groupBoxFlags;
		private System.Windows.Forms.CheckBox checkBoxSlipDamage;
		private System.Windows.Forms.CheckBox checkBoxNoEvade;
		private System.Windows.Forms.CheckBox checkBoxNoExp;
		private System.Windows.Forms.CheckBox checkBoxRegardHp0;
		private System.Windows.Forms.CheckBox checkBoxNonrestistance;
		private Controls.CheckGroupBox checkGroupBoxElements;
		private System.Windows.Forms.Label labelChance2;
		private System.Windows.Forms.NumericUpDown numericDamageChance;
		private System.Windows.Forms.Label labelPhysDamage;
		private System.Windows.Forms.Label labelChance1;
		private System.Windows.Forms.NumericUpDown numericTurnChance;
		private System.Windows.Forms.Label labelTurns;
		private System.Windows.Forms.Label labelAfter;
		private System.Windows.Forms.NumericUpDown numericTurns;
		private System.Windows.Forms.FlowLayoutPanel flowPanelParameters;
		private Controls.ParamBox paramBoxRating;
		private Controls.ParamBox paramBoxHitRate;
		private Controls.ParamBox paramBoxMaxHP;
		private Controls.ParamBox paramBoxMaxSP;
		private Controls.ParamBox paramBoxStr;
		private Controls.ParamBox paramBoxDex;
		private Controls.ParamBox paramBoxAgi;
		private Controls.ParamBox paramBoxInt;
		private Controls.ParamBox paramBoxAtk;
		private Controls.ParamBox paramBoxPdef;
		private Controls.ParamBox paramBoxMdef;
		private Controls.ParamBox paramBoxEva;
	}
}