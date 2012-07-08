namespace ARCed.Database.Animations
{
	partial class AnimationMainForm
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
			this.splitContainerMain = new System.Windows.Forms.SplitContainer();
			this.dataObjectList = new ARCed.Controls.DatabaseObjectListBox();
			this.splitContainerXnaPanels = new System.Windows.Forms.SplitContainer();
			this.panelPreview = new System.Windows.Forms.Panel();
			this.animeXnaPanel = new ARCed.Controls.AnimationXnaPanel();
			this.panel1 = new System.Windows.Forms.Panel();
			this.buttonPlayMiss = new System.Windows.Forms.Button();
			this.buttonPlayHit = new System.Windows.Forms.Button();
			this.buttonEntireSlide = new System.Windows.Forms.Button();
			this.buttonCellBatch = new System.Windows.Forms.Button();
			this.buttonTweening = new System.Windows.Forms.Button();
			this.buttonClear = new System.Windows.Forms.Button();
			this.buttonCopy = new System.Windows.Forms.Button();
			this.buttonPaste = new System.Windows.Forms.Button();
			this.buttonBattler = new System.Windows.Forms.Button();
			this.listBoxFrames = new System.Windows.Forms.ListBox();
			this.buttonFrameNext = new System.Windows.Forms.Button();
			this.buttonFrameBack = new System.Windows.Forms.Button();
			this.splitContainerBottom = new System.Windows.Forms.SplitContainer();
			this.groupBoxGraphics = new System.Windows.Forms.GroupBox();
			this.panelGraphics = new System.Windows.Forms.Panel();
			this.animeSrcXnaPanel = new ARCed.Controls.AnimationSourceXnaPanel();
			this.noteTextBox = new ARCed.Controls.NoteTextBox();
			this.splitContainerTop = new System.Windows.Forms.SplitContainer();
			this.splitContainerPosFrames = new System.Windows.Forms.SplitContainer();
			this.comboBoxPosition = new System.Windows.Forms.ComboBox();
			this.label3 = new System.Windows.Forms.Label();
			this.numericUpDownFrames = new System.Windows.Forms.NumericUpDown();
			this.label4 = new System.Windows.Forms.Label();
			this.textBoxGraphic = new ARCed.Controls.TextBoxButton();
			this.textBoxName = new System.Windows.Forms.TextBox();
			this.label1 = new System.Windows.Forms.Label();
			this.label2 = new System.Windows.Forms.Label();
			this.listViewTiming = new System.Windows.Forms.ListView();
			this.columnFrames = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
			this.columnSE = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
			this.columnFlash = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
			this.columnCondition = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
			((System.ComponentModel.ISupportInitialize)(this.splitContainerMain)).BeginInit();
			this.splitContainerMain.Panel1.SuspendLayout();
			this.splitContainerMain.Panel2.SuspendLayout();
			this.splitContainerMain.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerXnaPanels)).BeginInit();
			this.splitContainerXnaPanels.Panel1.SuspendLayout();
			this.splitContainerXnaPanels.Panel2.SuspendLayout();
			this.splitContainerXnaPanels.SuspendLayout();
			this.panelPreview.SuspendLayout();
			this.panel1.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerBottom)).BeginInit();
			this.splitContainerBottom.Panel1.SuspendLayout();
			this.splitContainerBottom.Panel2.SuspendLayout();
			this.splitContainerBottom.SuspendLayout();
			this.groupBoxGraphics.SuspendLayout();
			this.panelGraphics.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerTop)).BeginInit();
			this.splitContainerTop.Panel1.SuspendLayout();
			this.splitContainerTop.Panel2.SuspendLayout();
			this.splitContainerTop.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerPosFrames)).BeginInit();
			this.splitContainerPosFrames.Panel1.SuspendLayout();
			this.splitContainerPosFrames.Panel2.SuspendLayout();
			this.splitContainerPosFrames.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownFrames)).BeginInit();
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
			this.splitContainerMain.Panel2.Controls.Add(this.splitContainerXnaPanels);
			this.splitContainerMain.Panel2.Controls.Add(this.splitContainerTop);
			this.splitContainerMain.Size = new System.Drawing.Size(784, 562);
			this.splitContainerMain.SplitterDistance = 201;
			this.splitContainerMain.TabIndex = 0;
			// 
			// dataObjectList
			// 
			this.dataObjectList.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.dataObjectList.HeaderText = "Animations";
			this.dataObjectList.Location = new System.Drawing.Point(3, 3);
			this.dataObjectList.Name = "dataObjectList";
			this.dataObjectList.SelectedIndex = -1;
			this.dataObjectList.Size = new System.Drawing.Size(195, 556);
			this.dataObjectList.TabIndex = 1;
			this.dataObjectList.TabStop = false;
			this.dataObjectList.OnListBoxIndexChanged += new ARCed.Controls.DatabaseObjectListBox.ObjectListIndexChangedEventHandler(this.dataObjectList_OnListBoxIndexChanged);
			// 
			// splitContainerXnaPanels
			// 
			this.splitContainerXnaPanels.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.splitContainerXnaPanels.Location = new System.Drawing.Point(3, 145);
			this.splitContainerXnaPanels.Name = "splitContainerXnaPanels";
			this.splitContainerXnaPanels.Orientation = System.Windows.Forms.Orientation.Horizontal;
			// 
			// splitContainerXnaPanels.Panel1
			// 
			this.splitContainerXnaPanels.Panel1.Controls.Add(this.panelPreview);
			this.splitContainerXnaPanels.Panel1.Controls.Add(this.panel1);
			this.splitContainerXnaPanels.Panel1.Controls.Add(this.listBoxFrames);
			this.splitContainerXnaPanels.Panel1.Controls.Add(this.buttonFrameNext);
			this.splitContainerXnaPanels.Panel1.Controls.Add(this.buttonFrameBack);
			// 
			// splitContainerXnaPanels.Panel2
			// 
			this.splitContainerXnaPanels.Panel2.AutoScroll = true;
			this.splitContainerXnaPanels.Panel2.Controls.Add(this.splitContainerBottom);
			this.splitContainerXnaPanels.Panel2MinSize = 160;
			this.splitContainerXnaPanels.Size = new System.Drawing.Size(570, 414);
			this.splitContainerXnaPanels.SplitterDistance = 279;
			this.splitContainerXnaPanels.TabIndex = 5;
			// 
			// panelPreview
			// 
			this.panelPreview.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.panelPreview.BackColor = System.Drawing.SystemColors.ControlDark;
			this.panelPreview.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
			this.panelPreview.Controls.Add(this.animeXnaPanel);
			this.panelPreview.Location = new System.Drawing.Point(62, 9);
			this.panelPreview.Name = "panelPreview";
			this.panelPreview.Size = new System.Drawing.Size(382, 267);
			this.panelPreview.TabIndex = 4;
			// 
			// animeXnaPanel
			// 
			this.animeXnaPanel.Animation = null;
			this.animeXnaPanel.Dock = System.Windows.Forms.DockStyle.Fill;
			this.animeXnaPanel.Location = new System.Drawing.Point(0, 0);
			this.animeXnaPanel.Name = "animeXnaPanel";
			this.animeXnaPanel.Size = new System.Drawing.Size(378, 263);
			this.animeXnaPanel.TabIndex = 0;
			this.animeXnaPanel.Text = "animeXnaPanel";
			// 
			// panel1
			// 
			this.panel1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.panel1.AutoScroll = true;
			this.panel1.Controls.Add(this.buttonPlayMiss);
			this.panel1.Controls.Add(this.buttonPlayHit);
			this.panel1.Controls.Add(this.buttonEntireSlide);
			this.panel1.Controls.Add(this.buttonCellBatch);
			this.panel1.Controls.Add(this.buttonTweening);
			this.panel1.Controls.Add(this.buttonClear);
			this.panel1.Controls.Add(this.buttonCopy);
			this.panel1.Controls.Add(this.buttonPaste);
			this.panel1.Controls.Add(this.buttonBattler);
			this.panel1.Location = new System.Drawing.Point(450, 6);
			this.panel1.Name = "panel1";
			this.panel1.Size = new System.Drawing.Size(114, 270);
			this.panel1.TabIndex = 3;
			// 
			// buttonPlayMiss
			// 
			this.buttonPlayMiss.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.buttonPlayMiss.Location = new System.Drawing.Point(3, 199);
			this.buttonPlayMiss.Margin = new System.Windows.Forms.Padding(3, 0, 3, 3);
			this.buttonPlayMiss.Name = "buttonPlayMiss";
			this.buttonPlayMiss.Size = new System.Drawing.Size(108, 23);
			this.buttonPlayMiss.TabIndex = 8;
			this.buttonPlayMiss.Text = "Play Miss";
			this.buttonPlayMiss.UseVisualStyleBackColor = true;
			// 
			// buttonPlayHit
			// 
			this.buttonPlayHit.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.buttonPlayHit.Location = new System.Drawing.Point(3, 176);
			this.buttonPlayHit.Margin = new System.Windows.Forms.Padding(3, 3, 3, 0);
			this.buttonPlayHit.Name = "buttonPlayHit";
			this.buttonPlayHit.Size = new System.Drawing.Size(108, 23);
			this.buttonPlayHit.TabIndex = 7;
			this.buttonPlayHit.Text = "Play Hit";
			this.buttonPlayHit.UseVisualStyleBackColor = true;
			// 
			// buttonEntireSlide
			// 
			this.buttonEntireSlide.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.buttonEntireSlide.Location = new System.Drawing.Point(3, 147);
			this.buttonEntireSlide.Margin = new System.Windows.Forms.Padding(3, 0, 3, 3);
			this.buttonEntireSlide.Name = "buttonEntireSlide";
			this.buttonEntireSlide.Size = new System.Drawing.Size(108, 23);
			this.buttonEntireSlide.TabIndex = 6;
			this.buttonEntireSlide.Text = "Entire Slide...";
			this.buttonEntireSlide.UseVisualStyleBackColor = true;
			// 
			// buttonCellBatch
			// 
			this.buttonCellBatch.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.buttonCellBatch.Location = new System.Drawing.Point(3, 124);
			this.buttonCellBatch.Margin = new System.Windows.Forms.Padding(3, 0, 3, 0);
			this.buttonCellBatch.Name = "buttonCellBatch";
			this.buttonCellBatch.Size = new System.Drawing.Size(108, 23);
			this.buttonCellBatch.TabIndex = 5;
			this.buttonCellBatch.Text = "Cell Batch...";
			this.buttonCellBatch.UseVisualStyleBackColor = true;
			// 
			// buttonTweening
			// 
			this.buttonTweening.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.buttonTweening.Location = new System.Drawing.Point(3, 101);
			this.buttonTweening.Margin = new System.Windows.Forms.Padding(3, 0, 3, 0);
			this.buttonTweening.Name = "buttonTweening";
			this.buttonTweening.Size = new System.Drawing.Size(108, 23);
			this.buttonTweening.TabIndex = 4;
			this.buttonTweening.Text = "Tweening...";
			this.buttonTweening.UseVisualStyleBackColor = true;
			// 
			// buttonClear
			// 
			this.buttonClear.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.buttonClear.Location = new System.Drawing.Point(3, 78);
			this.buttonClear.Margin = new System.Windows.Forms.Padding(3, 0, 3, 0);
			this.buttonClear.Name = "buttonClear";
			this.buttonClear.Size = new System.Drawing.Size(108, 23);
			this.buttonClear.TabIndex = 3;
			this.buttonClear.Text = "Clear Frames...";
			this.buttonClear.UseVisualStyleBackColor = true;
			// 
			// buttonCopy
			// 
			this.buttonCopy.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.buttonCopy.Location = new System.Drawing.Point(3, 55);
			this.buttonCopy.Margin = new System.Windows.Forms.Padding(3, 0, 3, 0);
			this.buttonCopy.Name = "buttonCopy";
			this.buttonCopy.Size = new System.Drawing.Size(108, 23);
			this.buttonCopy.TabIndex = 2;
			this.buttonCopy.Text = "Copy Frames...";
			this.buttonCopy.UseVisualStyleBackColor = true;
			// 
			// buttonPaste
			// 
			this.buttonPaste.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.buttonPaste.Location = new System.Drawing.Point(3, 32);
			this.buttonPaste.Margin = new System.Windows.Forms.Padding(3, 3, 3, 0);
			this.buttonPaste.Name = "buttonPaste";
			this.buttonPaste.Size = new System.Drawing.Size(108, 23);
			this.buttonPaste.TabIndex = 1;
			this.buttonPaste.Text = "Paste Last";
			this.buttonPaste.UseVisualStyleBackColor = true;
			// 
			// buttonBattler
			// 
			this.buttonBattler.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.buttonBattler.Location = new System.Drawing.Point(3, 3);
			this.buttonBattler.Name = "buttonBattler";
			this.buttonBattler.Size = new System.Drawing.Size(108, 23);
			this.buttonBattler.TabIndex = 0;
			this.buttonBattler.Text = "[ED] Battler...";
			this.buttonBattler.UseVisualStyleBackColor = true;
			// 
			// listBoxFrames
			// 
			this.listBoxFrames.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)));
			this.listBoxFrames.FormattingEnabled = true;
			this.listBoxFrames.IntegralHeight = false;
			this.listBoxFrames.Location = new System.Drawing.Point(6, 35);
			this.listBoxFrames.Name = "listBoxFrames";
			this.listBoxFrames.Size = new System.Drawing.Size(50, 212);
			this.listBoxFrames.TabIndex = 2;
			// 
			// buttonFrameNext
			// 
			this.buttonFrameNext.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.buttonFrameNext.Location = new System.Drawing.Point(6, 253);
			this.buttonFrameNext.Name = "buttonFrameNext";
			this.buttonFrameNext.Size = new System.Drawing.Size(50, 23);
			this.buttonFrameNext.TabIndex = 1;
			this.buttonFrameNext.Text = "Next";
			this.buttonFrameNext.UseVisualStyleBackColor = true;
			// 
			// buttonFrameBack
			// 
			this.buttonFrameBack.Location = new System.Drawing.Point(6, 6);
			this.buttonFrameBack.Name = "buttonFrameBack";
			this.buttonFrameBack.Size = new System.Drawing.Size(50, 23);
			this.buttonFrameBack.TabIndex = 0;
			this.buttonFrameBack.Text = "Back";
			this.buttonFrameBack.UseVisualStyleBackColor = true;
			// 
			// splitContainerBottom
			// 
			this.splitContainerBottom.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainerBottom.Location = new System.Drawing.Point(0, 0);
			this.splitContainerBottom.Name = "splitContainerBottom";
			// 
			// splitContainerBottom.Panel1
			// 
			this.splitContainerBottom.Panel1.Controls.Add(this.groupBoxGraphics);
			// 
			// splitContainerBottom.Panel2
			// 
			this.splitContainerBottom.Panel2.Controls.Add(this.noteTextBox);
			this.splitContainerBottom.Size = new System.Drawing.Size(570, 160);
			this.splitContainerBottom.SplitterDistance = 383;
			this.splitContainerBottom.TabIndex = 0;
			// 
			// groupBoxGraphics
			// 
			this.groupBoxGraphics.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxGraphics.Controls.Add(this.panelGraphics);
			this.groupBoxGraphics.Location = new System.Drawing.Point(6, 6);
			this.groupBoxGraphics.Name = "groupBoxGraphics";
			this.groupBoxGraphics.Size = new System.Drawing.Size(374, 151);
			this.groupBoxGraphics.TabIndex = 1;
			this.groupBoxGraphics.TabStop = false;
			this.groupBoxGraphics.Text = "Graphics";
			// 
			// panelGraphics
			// 
			this.panelGraphics.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.panelGraphics.AutoScroll = true;
			this.panelGraphics.BackColor = System.Drawing.SystemColors.ControlDark;
			this.panelGraphics.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
			this.panelGraphics.Controls.Add(this.animeSrcXnaPanel);
			this.panelGraphics.Location = new System.Drawing.Point(6, 19);
			this.panelGraphics.Name = "panelGraphics";
			this.panelGraphics.Size = new System.Drawing.Size(362, 126);
			this.panelGraphics.TabIndex = 0;
			// 
			// animeSrcXnaPanel
			// 
			this.animeSrcXnaPanel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)));
			this.animeSrcXnaPanel.Animation = null;
			this.animeSrcXnaPanel.Location = new System.Drawing.Point(0, 0);
			this.animeSrcXnaPanel.Name = "animeSrcXnaPanel";
			this.animeSrcXnaPanel.SelectedId = 0;
			this.animeSrcXnaPanel.Size = new System.Drawing.Size(318, 126);
			this.animeSrcXnaPanel.TabIndex = 0;
			this.animeSrcXnaPanel.Text = "animeSrcXnaPanel";
			this.animeSrcXnaPanel.Visible = false;
			// 
			// noteTextBox
			// 
			this.noteTextBox.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.noteTextBox.Location = new System.Drawing.Point(3, 6);
			this.noteTextBox.Name = "noteTextBox";
			this.noteTextBox.NoteText = "";
			this.noteTextBox.Size = new System.Drawing.Size(180, 151);
			this.noteTextBox.TabIndex = 0;
			// 
			// splitContainerTop
			// 
			this.splitContainerTop.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.splitContainerTop.Location = new System.Drawing.Point(3, 3);
			this.splitContainerTop.Name = "splitContainerTop";
			// 
			// splitContainerTop.Panel1
			// 
			this.splitContainerTop.Panel1.Controls.Add(this.splitContainerPosFrames);
			this.splitContainerTop.Panel1.Controls.Add(this.textBoxGraphic);
			this.splitContainerTop.Panel1.Controls.Add(this.textBoxName);
			this.splitContainerTop.Panel1.Controls.Add(this.label1);
			this.splitContainerTop.Panel1.Controls.Add(this.label2);
			// 
			// splitContainerTop.Panel2
			// 
			this.splitContainerTop.Panel2.Controls.Add(this.listViewTiming);
			this.splitContainerTop.Size = new System.Drawing.Size(573, 142);
			this.splitContainerTop.SplitterDistance = 191;
			this.splitContainerTop.TabIndex = 4;
			// 
			// splitContainerPosFrames
			// 
			this.splitContainerPosFrames.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.splitContainerPosFrames.Location = new System.Drawing.Point(6, 96);
			this.splitContainerPosFrames.Name = "splitContainerPosFrames";
			// 
			// splitContainerPosFrames.Panel1
			// 
			this.splitContainerPosFrames.Panel1.Controls.Add(this.comboBoxPosition);
			this.splitContainerPosFrames.Panel1.Controls.Add(this.label3);
			// 
			// splitContainerPosFrames.Panel2
			// 
			this.splitContainerPosFrames.Panel2.Controls.Add(this.numericUpDownFrames);
			this.splitContainerPosFrames.Panel2.Controls.Add(this.label4);
			this.splitContainerPosFrames.Size = new System.Drawing.Size(182, 40);
			this.splitContainerPosFrames.SplitterDistance = 91;
			this.splitContainerPosFrames.TabIndex = 6;
			// 
			// comboBoxPosition
			// 
			this.comboBoxPosition.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxPosition.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxPosition.FormattingEnabled = true;
			this.comboBoxPosition.Items.AddRange(new object[] {
            "Top",
            "Middle",
            "Bottom",
            "Screen"});
			this.comboBoxPosition.Location = new System.Drawing.Point(0, 16);
			this.comboBoxPosition.Name = "comboBoxPosition";
			this.comboBoxPosition.Size = new System.Drawing.Size(89, 21);
			this.comboBoxPosition.TabIndex = 5;
			// 
			// label3
			// 
			this.label3.AutoSize = true;
			this.label3.Location = new System.Drawing.Point(3, 0);
			this.label3.Name = "label3";
			this.label3.Size = new System.Drawing.Size(47, 13);
			this.label3.TabIndex = 2;
			this.label3.Text = "Position:";
			// 
			// numericUpDownFrames
			// 
			this.numericUpDownFrames.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.numericUpDownFrames.Location = new System.Drawing.Point(0, 17);
			this.numericUpDownFrames.Maximum = new decimal(new int[] {
            999,
            0,
            0,
            0});
			this.numericUpDownFrames.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
			this.numericUpDownFrames.Name = "numericUpDownFrames";
			this.numericUpDownFrames.Size = new System.Drawing.Size(87, 20);
			this.numericUpDownFrames.TabIndex = 5;
			this.numericUpDownFrames.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
			this.numericUpDownFrames.ValueChanged += new System.EventHandler(this.numericUpDownFrames_ValueChanged);
			// 
			// label4
			// 
			this.label4.AutoSize = true;
			this.label4.Location = new System.Drawing.Point(0, 0);
			this.label4.Name = "label4";
			this.label4.Size = new System.Drawing.Size(44, 13);
			this.label4.TabIndex = 3;
			this.label4.Text = "Frames:";
			// 
			// textBoxGraphic
			// 
			this.textBoxGraphic.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBoxGraphic.Location = new System.Drawing.Point(6, 70);
			this.textBoxGraphic.MaximumSize = new System.Drawing.Size(1800, 20);
			this.textBoxGraphic.Name = "textBoxGraphic";
			this.textBoxGraphic.Size = new System.Drawing.Size(182, 20);
			this.textBoxGraphic.TabIndex = 5;
			this.textBoxGraphic.OnButtonClick += new ARCed.Controls.TextBoxButton.ButtonClickHandler(this.textBoxGraphic_OnButtonClick);
			// 
			// textBoxName
			// 
			this.textBoxName.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBoxName.Location = new System.Drawing.Point(6, 22);
			this.textBoxName.Name = "textBoxName";
			this.textBoxName.Size = new System.Drawing.Size(182, 20);
			this.textBoxName.TabIndex = 4;
			this.textBoxName.TextChanged += new System.EventHandler(this.textBoxName_TextChanged);
			// 
			// label1
			// 
			this.label1.AutoSize = true;
			this.label1.Location = new System.Drawing.Point(3, 6);
			this.label1.Name = "label1";
			this.label1.Size = new System.Drawing.Size(38, 13);
			this.label1.TabIndex = 0;
			this.label1.Text = "Name:";
			// 
			// label2
			// 
			this.label2.AutoSize = true;
			this.label2.Location = new System.Drawing.Point(3, 54);
			this.label2.Name = "label2";
			this.label2.Size = new System.Drawing.Size(47, 13);
			this.label2.TabIndex = 1;
			this.label2.Text = "Graphic:";
			// 
			// listViewTiming
			// 
			this.listViewTiming.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.listViewTiming.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.columnFrames,
            this.columnSE,
            this.columnFlash,
            this.columnCondition});
			this.listViewTiming.FullRowSelect = true;
			this.listViewTiming.GridLines = true;
			this.listViewTiming.Location = new System.Drawing.Point(3, 3);
			this.listViewTiming.MultiSelect = false;
			this.listViewTiming.Name = "listViewTiming";
			this.listViewTiming.Size = new System.Drawing.Size(372, 133);
			this.listViewTiming.TabIndex = 0;
			this.listViewTiming.UseCompatibleStateImageBehavior = false;
			this.listViewTiming.View = System.Windows.Forms.View.Details;
			this.listViewTiming.ColumnClick += new System.Windows.Forms.ColumnClickEventHandler(this.listViewTiming_ColumnClick);
			this.listViewTiming.MouseDown += new System.Windows.Forms.MouseEventHandler(this.listViewTiming_MouseDown);
			// 
			// columnFrames
			// 
			this.columnFrames.Text = "Frame";
			this.columnFrames.Width = 44;
			// 
			// columnSE
			// 
			this.columnSE.Text = "SE";
			this.columnSE.Width = 96;
			// 
			// columnFlash
			// 
			this.columnFlash.Text = "Flash";
			this.columnFlash.Width = 123;
			// 
			// columnCondition
			// 
			this.columnCondition.Text = "Condition";
			this.columnCondition.Width = 96;
			// 
			// AnimationMainForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(784, 562);
			this.Controls.Add(this.splitContainerMain);
			this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.KeyPreview = true;
			this.Name = "AnimationMainForm";
			this.RpgTypeName = "RPG.Animation";
			this.Text = "Animations";
			this.Load += new System.EventHandler(this.AnimationMainForm_Load);
			this.splitContainerMain.Panel1.ResumeLayout(false);
			this.splitContainerMain.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerMain)).EndInit();
			this.splitContainerMain.ResumeLayout(false);
			this.splitContainerXnaPanels.Panel1.ResumeLayout(false);
			this.splitContainerXnaPanels.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerXnaPanels)).EndInit();
			this.splitContainerXnaPanels.ResumeLayout(false);
			this.panelPreview.ResumeLayout(false);
			this.panel1.ResumeLayout(false);
			this.splitContainerBottom.Panel1.ResumeLayout(false);
			this.splitContainerBottom.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerBottom)).EndInit();
			this.splitContainerBottom.ResumeLayout(false);
			this.groupBoxGraphics.ResumeLayout(false);
			this.panelGraphics.ResumeLayout(false);
			this.splitContainerTop.Panel1.ResumeLayout(false);
			this.splitContainerTop.Panel1.PerformLayout();
			this.splitContainerTop.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerTop)).EndInit();
			this.splitContainerTop.ResumeLayout(false);
			this.splitContainerPosFrames.Panel1.ResumeLayout(false);
			this.splitContainerPosFrames.Panel1.PerformLayout();
			this.splitContainerPosFrames.Panel2.ResumeLayout(false);
			this.splitContainerPosFrames.Panel2.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerPosFrames)).EndInit();
			this.splitContainerPosFrames.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownFrames)).EndInit();
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.SplitContainer splitContainerMain;
		private Controls.DatabaseObjectListBox dataObjectList;
		private System.Windows.Forms.SplitContainer splitContainerTop;
		private System.Windows.Forms.SplitContainer splitContainerPosFrames;
		private System.Windows.Forms.ComboBox comboBoxPosition;
		private System.Windows.Forms.Label label3;
		private System.Windows.Forms.NumericUpDown numericUpDownFrames;
		private System.Windows.Forms.Label label4;
		private Controls.TextBoxButton textBoxGraphic;
		private System.Windows.Forms.TextBox textBoxName;
		private System.Windows.Forms.Label label1;
		private System.Windows.Forms.Label label2;
		private System.Windows.Forms.ListView listViewTiming;
		private System.Windows.Forms.SplitContainer splitContainerXnaPanels;
		private System.Windows.Forms.Panel panel1;
		private System.Windows.Forms.Button buttonPlayMiss;
		private System.Windows.Forms.Button buttonPlayHit;
		private System.Windows.Forms.Button buttonEntireSlide;
		private System.Windows.Forms.Button buttonCellBatch;
		private System.Windows.Forms.Button buttonTweening;
		private System.Windows.Forms.Button buttonClear;
		private System.Windows.Forms.Button buttonCopy;
		private System.Windows.Forms.Button buttonPaste;
		private System.Windows.Forms.Button buttonBattler;
		private System.Windows.Forms.ListBox listBoxFrames;
		private System.Windows.Forms.Button buttonFrameNext;
		private System.Windows.Forms.Button buttonFrameBack;
		private System.Windows.Forms.Panel panelPreview;
		private System.Windows.Forms.SplitContainer splitContainerBottom;
		private System.Windows.Forms.GroupBox groupBoxGraphics;
		private System.Windows.Forms.Panel panelGraphics;
		private Controls.NoteTextBox noteTextBox;
		private Controls.AnimationSourceXnaPanel animeSrcXnaPanel;
		private Controls.AnimationXnaPanel animeXnaPanel;
		private System.Windows.Forms.ColumnHeader columnFrames;
		private System.Windows.Forms.ColumnHeader columnSE;
		private System.Windows.Forms.ColumnHeader columnFlash;
		private System.Windows.Forms.ColumnHeader columnCondition;

	}
}