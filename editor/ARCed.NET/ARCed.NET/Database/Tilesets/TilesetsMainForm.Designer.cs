﻿namespace ARCed.Database.Tilesets
{
	partial class TilesetsMainForm
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
            this.splitContainer = new System.Windows.Forms.SplitContainer();
            this.dataObjectList = new ARCed.Controls.DatabaseObjectListBox();
            this.splitContainerAutotileNote = new System.Windows.Forms.SplitContainer();
            this.groupBoxAutotiles = new System.Windows.Forms.GroupBox();
            this.panelAutotiles = new System.Windows.Forms.Panel();
            this.noteTextBox = new ARCed.Controls.NoteTextBox();
            this.checkBoxIcons = new System.Windows.Forms.CheckBox();
            this.checkBoxBatch = new System.Windows.Forms.CheckBox();
            this.radioTerrain = new System.Windows.Forms.RadioButton();
            this.radioCounter = new System.Windows.Forms.RadioButton();
            this.radioBush = new System.Windows.Forms.RadioButton();
            this.radioPriority = new System.Windows.Forms.RadioButton();
            this.radioPassage4Dir = new System.Windows.Forms.RadioButton();
            this.radioPassage = new System.Windows.Forms.RadioButton();
            this.checkBoxGrid = new System.Windows.Forms.CheckBox();
            this.buttonColors = new System.Windows.Forms.Button();
            this.panelTileset = new System.Windows.Forms.Panel();
            this.tilesetXnaPanel = new ARCed.Controls.TilesetXnaPanel();
            this.textBoxBattleback = new ARCed.Controls.TextBoxButton();
            this.textBoxFog = new ARCed.Controls.TextBoxButton();
            this.textBoxPanorama = new ARCed.Controls.TextBoxButton();
            this.textBoxTileset = new ARCed.Controls.TextBoxButton();
            this.textBoxName = new System.Windows.Forms.TextBox();
            this.labelBattlebackGraphic = new System.Windows.Forms.Label();
            this.labelFogGraphic = new System.Windows.Forms.Label();
            this.labelPanoramaGraphic = new System.Windows.Forms.Label();
            this.labelTilesetGraphic = new System.Windows.Forms.Label();
            this.labelName = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer)).BeginInit();
            this.splitContainer.Panel1.SuspendLayout();
            this.splitContainer.Panel2.SuspendLayout();
            this.splitContainer.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainerAutotileNote)).BeginInit();
            this.splitContainerAutotileNote.Panel1.SuspendLayout();
            this.splitContainerAutotileNote.Panel2.SuspendLayout();
            this.splitContainerAutotileNote.SuspendLayout();
            this.groupBoxAutotiles.SuspendLayout();
            this.panelTileset.SuspendLayout();
            this.SuspendLayout();
            // 
            // splitContainer
            // 
            this.splitContainer.Dock = System.Windows.Forms.DockStyle.Fill;
            this.splitContainer.Location = new System.Drawing.Point(0, 0);
            this.splitContainer.Name = "splitContainer";
            // 
            // splitContainer.Panel1
            // 
            this.splitContainer.Panel1.Controls.Add(this.dataObjectList);
            // 
            // splitContainer.Panel2
            // 
            this.splitContainer.Panel2.Controls.Add(this.splitContainerAutotileNote);
            this.splitContainer.Panel2.Controls.Add(this.checkBoxIcons);
            this.splitContainer.Panel2.Controls.Add(this.checkBoxBatch);
            this.splitContainer.Panel2.Controls.Add(this.radioTerrain);
            this.splitContainer.Panel2.Controls.Add(this.radioCounter);
            this.splitContainer.Panel2.Controls.Add(this.radioBush);
            this.splitContainer.Panel2.Controls.Add(this.radioPriority);
            this.splitContainer.Panel2.Controls.Add(this.radioPassage4Dir);
            this.splitContainer.Panel2.Controls.Add(this.radioPassage);
            this.splitContainer.Panel2.Controls.Add(this.checkBoxGrid);
            this.splitContainer.Panel2.Controls.Add(this.buttonColors);
            this.splitContainer.Panel2.Controls.Add(this.panelTileset);
            this.splitContainer.Panel2.Controls.Add(this.textBoxBattleback);
            this.splitContainer.Panel2.Controls.Add(this.textBoxFog);
            this.splitContainer.Panel2.Controls.Add(this.textBoxPanorama);
            this.splitContainer.Panel2.Controls.Add(this.textBoxTileset);
            this.splitContainer.Panel2.Controls.Add(this.textBoxName);
            this.splitContainer.Panel2.Controls.Add(this.labelBattlebackGraphic);
            this.splitContainer.Panel2.Controls.Add(this.labelFogGraphic);
            this.splitContainer.Panel2.Controls.Add(this.labelPanoramaGraphic);
            this.splitContainer.Panel2.Controls.Add(this.labelTilesetGraphic);
            this.splitContainer.Panel2.Controls.Add(this.labelName);
            this.splitContainer.Size = new System.Drawing.Size(784, 562);
            this.splitContainer.SplitterDistance = 201;
            this.splitContainer.TabIndex = 0;
            // 
            // dataObjectList
            // 
            this.dataObjectList.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.dataObjectList.HeaderText = "Tilesets";
            this.dataObjectList.Location = new System.Drawing.Point(3, 3);
            this.dataObjectList.Name = "dataObjectList";
            this.dataObjectList.SelectedIndex = -1;
            this.dataObjectList.Size = new System.Drawing.Size(195, 556);
            this.dataObjectList.TabIndex = 0;
            this.dataObjectList.TabStop = false;
            this.dataObjectList.OnButtonMaxClick += new ARCed.Controls.DatabaseObjectListBox.ButtonMaxClickEventHandler(this.dataObjectList_OnButtonMaxClick);
            this.dataObjectList.OnListBoxIndexChanged += new ARCed.Controls.DatabaseObjectListBox.ObjectListIndexChangedEventHandler(this.DataObjectListOnListBoxIndexChanged);
            // 
            // splitContainerAutotileNote
            // 
            this.splitContainerAutotileNote.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.splitContainerAutotileNote.Location = new System.Drawing.Point(6, 211);
            this.splitContainerAutotileNote.Name = "splitContainerAutotileNote";
            this.splitContainerAutotileNote.Orientation = System.Windows.Forms.Orientation.Horizontal;
            // 
            // splitContainerAutotileNote.Panel1
            // 
            this.splitContainerAutotileNote.Panel1.Controls.Add(this.groupBoxAutotiles);
            // 
            // splitContainerAutotileNote.Panel2
            // 
            this.splitContainerAutotileNote.Panel2.Controls.Add(this.noteTextBox);
            this.splitContainerAutotileNote.Size = new System.Drawing.Size(215, 307);
            this.splitContainerAutotileNote.SplitterDistance = 153;
            this.splitContainerAutotileNote.TabIndex = 33;
            // 
            // groupBoxAutotiles
            // 
            this.groupBoxAutotiles.Controls.Add(this.panelAutotiles);
            this.groupBoxAutotiles.Dock = System.Windows.Forms.DockStyle.Fill;
            this.groupBoxAutotiles.Location = new System.Drawing.Point(0, 0);
            this.groupBoxAutotiles.Name = "groupBoxAutotiles";
            this.groupBoxAutotiles.Size = new System.Drawing.Size(215, 153);
            this.groupBoxAutotiles.TabIndex = 9;
            this.groupBoxAutotiles.TabStop = false;
            this.groupBoxAutotiles.Text = "Autotiles";
            // 
            // panelAutotiles
            // 
            this.panelAutotiles.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.panelAutotiles.AutoScroll = true;
            this.panelAutotiles.Location = new System.Drawing.Point(7, 19);
            this.panelAutotiles.Name = "panelAutotiles";
            this.panelAutotiles.Size = new System.Drawing.Size(202, 128);
            this.panelAutotiles.TabIndex = 0;
            // 
            // noteTextBox
            // 
            this.noteTextBox.Dock = System.Windows.Forms.DockStyle.Fill;
            this.noteTextBox.Location = new System.Drawing.Point(0, 0);
            this.noteTextBox.Name = "noteTextBox";
            this.noteTextBox.NoteText = "";
            this.noteTextBox.Size = new System.Drawing.Size(215, 150);
            this.noteTextBox.TabIndex = 0;
            this.noteTextBox.NoteTextChanged += new ARCed.Controls.NoteTextBox.TextChangedEventHandler(this.NoteTextBoxNoteTextChanged);
            // 
            // checkBoxIcons
            // 
            this.checkBoxIcons.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.checkBoxIcons.AutoSize = true;
            this.checkBoxIcons.Checked = true;
            this.checkBoxIcons.CheckState = System.Windows.Forms.CheckState.Checked;
            this.checkBoxIcons.Location = new System.Drawing.Point(163, 528);
            this.checkBoxIcons.Name = "checkBoxIcons";
            this.checkBoxIcons.Size = new System.Drawing.Size(52, 17);
            this.checkBoxIcons.TabIndex = 32;
            this.checkBoxIcons.Text = "Icons";
            this.checkBoxIcons.UseVisualStyleBackColor = true;
            this.checkBoxIcons.CheckedChanged += new System.EventHandler(this.CheckBoxIconsCheckedChanged);
            // 
            // checkBoxBatch
            // 
            this.checkBoxBatch.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.checkBoxBatch.Appearance = System.Windows.Forms.Appearance.Button;
            this.checkBoxBatch.Location = new System.Drawing.Point(508, 510);
            this.checkBoxBatch.Name = "checkBoxBatch";
            this.checkBoxBatch.Size = new System.Drawing.Size(59, 40);
            this.checkBoxBatch.TabIndex = 31;
            this.checkBoxBatch.Text = "Batch Select";
            this.checkBoxBatch.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.checkBoxBatch.UseVisualStyleBackColor = true;
            this.checkBoxBatch.CheckedChanged += new System.EventHandler(this.CheckBoxBatchCheckedChanged);
            // 
            // radioTerrain
            // 
            this.radioTerrain.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.radioTerrain.Appearance = System.Windows.Forms.Appearance.Button;
            this.radioTerrain.Location = new System.Drawing.Point(508, 243);
            this.radioTerrain.Name = "radioTerrain";
            this.radioTerrain.Size = new System.Drawing.Size(59, 40);
            this.radioTerrain.TabIndex = 30;
            this.radioTerrain.Tag = "5";
            this.radioTerrain.Text = "Terrain Tag";
            this.radioTerrain.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.radioTerrain.UseVisualStyleBackColor = true;
            this.radioTerrain.Click += new System.EventHandler(this.RadioModeClicked);
            // 
            // radioCounter
            // 
            this.radioCounter.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.radioCounter.Appearance = System.Windows.Forms.Appearance.Button;
            this.radioCounter.Location = new System.Drawing.Point(508, 197);
            this.radioCounter.Name = "radioCounter";
            this.radioCounter.Size = new System.Drawing.Size(59, 40);
            this.radioCounter.TabIndex = 29;
            this.radioCounter.Tag = "4";
            this.radioCounter.Text = "Counter Flag";
            this.radioCounter.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.radioCounter.UseVisualStyleBackColor = true;
            this.radioCounter.Click += new System.EventHandler(this.RadioModeClicked);
            // 
            // radioBush
            // 
            this.radioBush.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.radioBush.Appearance = System.Windows.Forms.Appearance.Button;
            this.radioBush.Location = new System.Drawing.Point(508, 151);
            this.radioBush.Name = "radioBush";
            this.radioBush.Size = new System.Drawing.Size(59, 40);
            this.radioBush.TabIndex = 28;
            this.radioBush.Tag = "3";
            this.radioBush.Text = "Bush Flag";
            this.radioBush.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.radioBush.UseVisualStyleBackColor = true;
            this.radioBush.Click += new System.EventHandler(this.RadioModeClicked);
            // 
            // radioPriority
            // 
            this.radioPriority.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.radioPriority.Appearance = System.Windows.Forms.Appearance.Button;
            this.radioPriority.Location = new System.Drawing.Point(508, 105);
            this.radioPriority.Name = "radioPriority";
            this.radioPriority.Size = new System.Drawing.Size(59, 40);
            this.radioPriority.TabIndex = 27;
            this.radioPriority.Tag = "2";
            this.radioPriority.Text = "Priority";
            this.radioPriority.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.radioPriority.UseVisualStyleBackColor = true;
            this.radioPriority.Click += new System.EventHandler(this.RadioModeClicked);
            // 
            // radioPassage4Dir
            // 
            this.radioPassage4Dir.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.radioPassage4Dir.Appearance = System.Windows.Forms.Appearance.Button;
            this.radioPassage4Dir.Location = new System.Drawing.Point(508, 58);
            this.radioPassage4Dir.Name = "radioPassage4Dir";
            this.radioPassage4Dir.Size = new System.Drawing.Size(59, 40);
            this.radioPassage4Dir.TabIndex = 26;
            this.radioPassage4Dir.Tag = "1";
            this.radioPassage4Dir.Text = "Passage (4 Dir)";
            this.radioPassage4Dir.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.radioPassage4Dir.UseVisualStyleBackColor = true;
            this.radioPassage4Dir.Click += new System.EventHandler(this.RadioModeClicked);
            // 
            // radioPassage
            // 
            this.radioPassage.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.radioPassage.Appearance = System.Windows.Forms.Appearance.Button;
            this.radioPassage.Checked = true;
            this.radioPassage.Location = new System.Drawing.Point(508, 12);
            this.radioPassage.Name = "radioPassage";
            this.radioPassage.Size = new System.Drawing.Size(59, 40);
            this.radioPassage.TabIndex = 25;
            this.radioPassage.TabStop = true;
            this.radioPassage.Tag = "0";
            this.radioPassage.Text = "Passage";
            this.radioPassage.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.radioPassage.UseVisualStyleBackColor = true;
            this.radioPassage.Click += new System.EventHandler(this.RadioModeClicked);
            // 
            // checkBoxGrid
            // 
            this.checkBoxGrid.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.checkBoxGrid.AutoSize = true;
            this.checkBoxGrid.Checked = true;
            this.checkBoxGrid.CheckState = System.Windows.Forms.CheckState.Checked;
            this.checkBoxGrid.Location = new System.Drawing.Point(114, 528);
            this.checkBoxGrid.Name = "checkBoxGrid";
            this.checkBoxGrid.Size = new System.Drawing.Size(45, 17);
            this.checkBoxGrid.TabIndex = 23;
            this.checkBoxGrid.Text = "Grid";
            this.checkBoxGrid.UseVisualStyleBackColor = true;
            this.checkBoxGrid.CheckedChanged += new System.EventHandler(this.CheckBoxGridCheckedChanged);
            // 
            // buttonColors
            // 
            this.buttonColors.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.buttonColors.Location = new System.Drawing.Point(12, 524);
            this.buttonColors.Name = "buttonColors";
            this.buttonColors.Size = new System.Drawing.Size(96, 23);
            this.buttonColors.TabIndex = 22;
            this.buttonColors.Text = "Edit Colors...";
            this.buttonColors.UseVisualStyleBackColor = true;
            this.buttonColors.Click += new System.EventHandler(this.ButtonColorsClick);
            // 
            // panelTileset
            // 
            this.panelTileset.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.panelTileset.AutoScroll = true;
            this.panelTileset.BackColor = System.Drawing.Color.White;
            this.panelTileset.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.panelTileset.Controls.Add(this.tilesetXnaPanel);
            this.panelTileset.Location = new System.Drawing.Point(227, 12);
            this.panelTileset.Name = "panelTileset";
            this.panelTileset.Size = new System.Drawing.Size(275, 538);
            this.panelTileset.TabIndex = 17;
            // 
            // tilesetXnaPanel
            // 
            this.tilesetXnaPanel.DisplayIcons = false;
            this.tilesetXnaPanel.Location = new System.Drawing.Point(0, 0);
            this.tilesetXnaPanel.Name = "tilesetXnaPanel";
            this.tilesetXnaPanel.SelectionEnabled = false;
            this.tilesetXnaPanel.Size = new System.Drawing.Size(256, 533);
            this.tilesetXnaPanel.TabIndex = 0;
            this.tilesetXnaPanel.Text = "tilesetXnaPanel";
            this.tilesetXnaPanel.Tileset = null;
            this.tilesetXnaPanel.TilesetMode = ARCed.Controls.TilesetMode.Passage;
            // 
            // textBoxBattleback
            // 
            this.textBoxBattleback.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.textBoxBattleback.Location = new System.Drawing.Point(6, 185);
            this.textBoxBattleback.MaximumSize = new System.Drawing.Size(1800, 20);
            this.textBoxBattleback.Name = "textBoxBattleback";
            this.textBoxBattleback.Size = new System.Drawing.Size(215, 20);
            this.textBoxBattleback.TabIndex = 16;
            this.textBoxBattleback.OnButtonClick += new ARCed.Controls.TextBoxButton.ButtonClickHandler(this.TextBoxBattlebackOnButtonClick);
            // 
            // textBoxFog
            // 
            this.textBoxFog.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.textBoxFog.Location = new System.Drawing.Point(6, 145);
            this.textBoxFog.MaximumSize = new System.Drawing.Size(1800, 20);
            this.textBoxFog.Name = "textBoxFog";
            this.textBoxFog.Size = new System.Drawing.Size(215, 20);
            this.textBoxFog.TabIndex = 15;
            this.textBoxFog.OnButtonClick += new ARCed.Controls.TextBoxButton.ButtonClickHandler(this.TextBoxFogOnTextBoxFogOnButtonClick);
            // 
            // textBoxPanorama
            // 
            this.textBoxPanorama.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.textBoxPanorama.Location = new System.Drawing.Point(6, 105);
            this.textBoxPanorama.MaximumSize = new System.Drawing.Size(1800, 20);
            this.textBoxPanorama.Name = "textBoxPanorama";
            this.textBoxPanorama.Size = new System.Drawing.Size(215, 20);
            this.textBoxPanorama.TabIndex = 14;
            this.textBoxPanorama.OnButtonClick += new ARCed.Controls.TextBoxButton.ButtonClickHandler(this.TextBoxPanoramaOnButtonClick);
            // 
            // textBoxTileset
            // 
            this.textBoxTileset.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.textBoxTileset.Location = new System.Drawing.Point(6, 65);
            this.textBoxTileset.MaximumSize = new System.Drawing.Size(1800, 20);
            this.textBoxTileset.Name = "textBoxTileset";
            this.textBoxTileset.Size = new System.Drawing.Size(215, 20);
            this.textBoxTileset.TabIndex = 13;
            this.textBoxTileset.OnButtonClick += new ARCed.Controls.TextBoxButton.ButtonClickHandler(this.TextBoxTilesetOnButtonClick);
            // 
            // textBoxName
            // 
            this.textBoxName.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.textBoxName.Location = new System.Drawing.Point(6, 25);
            this.textBoxName.Name = "textBoxName";
            this.textBoxName.Size = new System.Drawing.Size(215, 20);
            this.textBoxName.TabIndex = 10;
            this.textBoxName.TextChanged += new System.EventHandler(this.TextBoxNameTextChanged);
            // 
            // labelBattlebackGraphic
            // 
            this.labelBattlebackGraphic.AutoSize = true;
            this.labelBattlebackGraphic.Location = new System.Drawing.Point(3, 169);
            this.labelBattlebackGraphic.Name = "labelBattlebackGraphic";
            this.labelBattlebackGraphic.Size = new System.Drawing.Size(101, 13);
            this.labelBattlebackGraphic.TabIndex = 7;
            this.labelBattlebackGraphic.Text = "Battleback Graphic:";
            // 
            // labelFogGraphic
            // 
            this.labelFogGraphic.AutoSize = true;
            this.labelFogGraphic.Location = new System.Drawing.Point(3, 129);
            this.labelFogGraphic.Name = "labelFogGraphic";
            this.labelFogGraphic.Size = new System.Drawing.Size(68, 13);
            this.labelFogGraphic.TabIndex = 6;
            this.labelFogGraphic.Text = "Fog Graphic:";
            // 
            // labelPanoramaGraphic
            // 
            this.labelPanoramaGraphic.AutoSize = true;
            this.labelPanoramaGraphic.Location = new System.Drawing.Point(3, 89);
            this.labelPanoramaGraphic.Name = "labelPanoramaGraphic";
            this.labelPanoramaGraphic.Size = new System.Drawing.Size(98, 13);
            this.labelPanoramaGraphic.TabIndex = 5;
            this.labelPanoramaGraphic.Text = "Panorama Graphic:";
            // 
            // labelTilesetGraphic
            // 
            this.labelTilesetGraphic.AutoSize = true;
            this.labelTilesetGraphic.Location = new System.Drawing.Point(3, 49);
            this.labelTilesetGraphic.Name = "labelTilesetGraphic";
            this.labelTilesetGraphic.Size = new System.Drawing.Size(81, 13);
            this.labelTilesetGraphic.TabIndex = 4;
            this.labelTilesetGraphic.Text = "Tileset Graphic:";
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
            // TilesetsMainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(784, 562);
            this.Controls.Add(this.splitContainer);
            this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.KeyPreview = true;
            this.Name = "TilesetsMainForm";
            this.RpgTypeName = "RPG.Tileset";
            this.Text = "Tilesets";
            this.Load += new System.EventHandler(this.TilesetsMainFormLoad);
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.TilesetsMainFormKeyDown);
            this.splitContainer.Panel1.ResumeLayout(false);
            this.splitContainer.Panel2.ResumeLayout(false);
            this.splitContainer.Panel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer)).EndInit();
            this.splitContainer.ResumeLayout(false);
            this.splitContainerAutotileNote.Panel1.ResumeLayout(false);
            this.splitContainerAutotileNote.Panel2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.splitContainerAutotileNote)).EndInit();
            this.splitContainerAutotileNote.ResumeLayout(false);
            this.groupBoxAutotiles.ResumeLayout(false);
            this.panelTileset.ResumeLayout(false);
            this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.SplitContainer splitContainer;
		private Controls.DatabaseObjectListBox dataObjectList;
		private System.Windows.Forms.TextBox textBoxName;
		private System.Windows.Forms.GroupBox groupBoxAutotiles;
		private System.Windows.Forms.Label labelBattlebackGraphic;
		private System.Windows.Forms.Label labelFogGraphic;
		private System.Windows.Forms.Label labelPanoramaGraphic;
		private System.Windows.Forms.Label labelTilesetGraphic;
		private System.Windows.Forms.Label labelName;
		private Controls.TextBoxButton textBoxTileset;
		private Controls.TextBoxButton textBoxBattleback;
		private Controls.TextBoxButton textBoxFog;
		private Controls.TextBoxButton textBoxPanorama;
		private System.Windows.Forms.Panel panelTileset;
		private Controls.TilesetXnaPanel tilesetXnaPanel;
		private System.Windows.Forms.Button buttonColors;
		private System.Windows.Forms.CheckBox checkBoxGrid;
		private System.Windows.Forms.RadioButton radioTerrain;
		private System.Windows.Forms.RadioButton radioCounter;
		private System.Windows.Forms.RadioButton radioBush;
		private System.Windows.Forms.RadioButton radioPriority;
		private System.Windows.Forms.RadioButton radioPassage4Dir;
		private System.Windows.Forms.RadioButton radioPassage;
		private System.Windows.Forms.Panel panelAutotiles;
		private System.Windows.Forms.CheckBox checkBoxBatch;
		private System.Windows.Forms.CheckBox checkBoxIcons;
		private System.Windows.Forms.SplitContainer splitContainerAutotileNote;
		private Controls.NoteTextBox noteTextBox;
	}
}