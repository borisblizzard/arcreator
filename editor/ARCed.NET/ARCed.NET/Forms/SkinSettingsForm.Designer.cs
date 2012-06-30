namespace ARCed.Forms
{
	partial class SkinSettingsForm
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
			this.groupBoxFontSettings = new ARCed.Controls.CollapsibleGroupBox();
			this.buttonFont = new System.Windows.Forms.Button();
			this.labelFont = new System.Windows.Forms.Label();
			this.groupBoxGradientSettings = new ARCed.Controls.CollapsibleGroupBox();
			this.splitContainer1 = new System.Windows.Forms.SplitContainer();
			this.labelStartColor = new System.Windows.Forms.Label();
			this.panelStartColor = new System.Windows.Forms.Panel();
			this.splitContainer2 = new System.Windows.Forms.SplitContainer();
			this.labelEndColor = new System.Windows.Forms.Label();
			this.panelEndColor = new System.Windows.Forms.Panel();
			this.labelTextColor = new System.Windows.Forms.Label();
			this.panelTextColor = new System.Windows.Forms.Panel();
			this.listBoxGradients = new System.Windows.Forms.ListBox();
			this.labelGradient = new System.Windows.Forms.Label();
			this.comboBoxGradient = new System.Windows.Forms.ComboBox();
			this.groupBoxSkinType = new ARCed.Controls.CollapsibleGroupBox();
			this.splitContainerTypes = new System.Windows.Forms.SplitContainer();
			this.radioDockPanel = new System.Windows.Forms.RadioButton();
			this.radioAutoHide = new System.Windows.Forms.RadioButton();
			this.buttonDefault = new System.Windows.Forms.Button();
			this.buttonApply = new System.Windows.Forms.Button();
			this.toolTip = new System.Windows.Forms.ToolTip(this.components);
			this.groupBoxFontSettings.SuspendLayout();
			this.groupBoxGradientSettings.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).BeginInit();
			this.splitContainer1.Panel1.SuspendLayout();
			this.splitContainer1.Panel2.SuspendLayout();
			this.splitContainer1.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainer2)).BeginInit();
			this.splitContainer2.Panel1.SuspendLayout();
			this.splitContainer2.Panel2.SuspendLayout();
			this.splitContainer2.SuspendLayout();
			this.groupBoxSkinType.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerTypes)).BeginInit();
			this.splitContainerTypes.Panel1.SuspendLayout();
			this.splitContainerTypes.Panel2.SuspendLayout();
			this.splitContainerTypes.SuspendLayout();
			this.SuspendLayout();
			// 
			// groupBoxFontSettings
			// 
			this.groupBoxFontSettings.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxFontSettings.Controls.Add(this.buttonFont);
			this.groupBoxFontSettings.Controls.Add(this.labelFont);
			this.groupBoxFontSettings.Location = new System.Drawing.Point(12, 68);
			this.groupBoxFontSettings.Name = "groupBoxFontSettings";
			this.groupBoxFontSettings.Size = new System.Drawing.Size(238, 48);
			this.groupBoxFontSettings.TabIndex = 9;
			this.groupBoxFontSettings.TabStop = false;
			this.groupBoxFontSettings.Text = "Font Settings";
			this.groupBoxFontSettings.CollapseBoxClickedEvent += new ARCed.Controls.CollapsibleGroupBox.CollapseBoxClickedEventHandler(this.groupBoxFontSettings_CollapseBoxClickedEvent);
			// 
			// buttonFont
			// 
			this.buttonFont.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.buttonFont.Location = new System.Drawing.Point(9, 19);
			this.buttonFont.Name = "buttonFont";
			this.buttonFont.Size = new System.Drawing.Size(77, 23);
			this.buttonFont.TabIndex = 7;
			this.buttonFont.Text = "Font...";
			this.toolTip.SetToolTip(this.buttonFont, "Select the font used for this gradient");
			this.buttonFont.UseVisualStyleBackColor = true;
			this.buttonFont.Click += new System.EventHandler(this.buttonFont_Click);
			// 
			// labelFont
			// 
			this.labelFont.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.labelFont.AutoSize = true;
			this.labelFont.Location = new System.Drawing.Point(92, 24);
			this.labelFont.Name = "labelFont";
			this.labelFont.Size = new System.Drawing.Size(31, 13);
			this.labelFont.TabIndex = 6;
			this.labelFont.Text = "Font:";
			// 
			// groupBoxGradientSettings
			// 
			this.groupBoxGradientSettings.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxGradientSettings.Controls.Add(this.splitContainer1);
			this.groupBoxGradientSettings.Controls.Add(this.listBoxGradients);
			this.groupBoxGradientSettings.Controls.Add(this.labelGradient);
			this.groupBoxGradientSettings.Controls.Add(this.comboBoxGradient);
			this.groupBoxGradientSettings.Location = new System.Drawing.Point(12, 120);
			this.groupBoxGradientSettings.Name = "groupBoxGradientSettings";
			this.groupBoxGradientSettings.Size = new System.Drawing.Size(238, 232);
			this.groupBoxGradientSettings.TabIndex = 0;
			this.groupBoxGradientSettings.TabStop = false;
			this.groupBoxGradientSettings.Text = "Gradient Settings";
			this.groupBoxGradientSettings.CollapseBoxClickedEvent += new ARCed.Controls.CollapsibleGroupBox.CollapseBoxClickedEventHandler(this.groupBoxGradientSettings_CollapseBoxClickedEvent);
			// 
			// splitContainerWeapons
			// 
			this.splitContainer1.Dock = System.Windows.Forms.DockStyle.Top;
			this.splitContainer1.IsSplitterFixed = true;
			this.splitContainer1.Location = new System.Drawing.Point(3, 16);
			this.splitContainer1.Name = "splitContainer1";
			// 
			// splitContainerWeapons.Panel1
			// 
			this.splitContainer1.Panel1.Controls.Add(this.labelStartColor);
			this.splitContainer1.Panel1.Controls.Add(this.panelStartColor);
			// 
			// splitContainerWeapons.Panel2
			// 
			this.splitContainer1.Panel2.Controls.Add(this.splitContainer2);
			this.splitContainer1.Size = new System.Drawing.Size(232, 52);
			this.splitContainer1.SplitterDistance = 71;
			this.splitContainer1.SplitterWidth = 1;
			this.splitContainer1.TabIndex = 11;
			// 
			// labelStartColor
			// 
			this.labelStartColor.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.labelStartColor.AutoSize = true;
			this.labelStartColor.Location = new System.Drawing.Point(3, 0);
			this.labelStartColor.Name = "labelStartColor";
			this.labelStartColor.Size = new System.Drawing.Size(59, 13);
			this.labelStartColor.TabIndex = 0;
			this.labelStartColor.Text = "Start Color:";
			// 
			// panelStartColor
			// 
			this.panelStartColor.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.panelStartColor.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
			this.panelStartColor.Location = new System.Drawing.Point(6, 16);
			this.panelStartColor.Name = "panelStartColor";
			this.panelStartColor.Size = new System.Drawing.Size(62, 30);
			this.panelStartColor.TabIndex = 2;
			this.panelStartColor.Tag = "START";
			this.toolTip.SetToolTip(this.panelStartColor, "Double-click to change the start gradient color");
			this.panelStartColor.DoubleClick += new System.EventHandler(this.panelColor_DoubleClick);
			// 
			// splitContainer2
			// 
			this.splitContainer2.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainer2.IsSplitterFixed = true;
			this.splitContainer2.Location = new System.Drawing.Point(0, 0);
			this.splitContainer2.Name = "splitContainer2";
			// 
			// splitContainer2.Panel1
			// 
			this.splitContainer2.Panel1.Controls.Add(this.labelEndColor);
			this.splitContainer2.Panel1.Controls.Add(this.panelEndColor);
			// 
			// splitContainer2.Panel2
			// 
			this.splitContainer2.Panel2.Controls.Add(this.labelTextColor);
			this.splitContainer2.Panel2.Controls.Add(this.panelTextColor);
			this.splitContainer2.Size = new System.Drawing.Size(160, 52);
			this.splitContainer2.SplitterDistance = 75;
			this.splitContainer2.SplitterWidth = 1;
			this.splitContainer2.TabIndex = 0;
			// 
			// labelEndColor
			// 
			this.labelEndColor.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.labelEndColor.AutoSize = true;
			this.labelEndColor.Location = new System.Drawing.Point(3, 0);
			this.labelEndColor.Name = "labelEndColor";
			this.labelEndColor.Size = new System.Drawing.Size(56, 13);
			this.labelEndColor.TabIndex = 1;
			this.labelEndColor.Text = "End Color:";
			// 
			// panelEndColor
			// 
			this.panelEndColor.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.panelEndColor.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
			this.panelEndColor.Location = new System.Drawing.Point(6, 16);
			this.panelEndColor.Name = "panelEndColor";
			this.panelEndColor.Size = new System.Drawing.Size(66, 30);
			this.panelEndColor.TabIndex = 3;
			this.panelEndColor.Tag = "END";
			this.toolTip.SetToolTip(this.panelEndColor, "Double-click to change the end gradient color");
			this.panelEndColor.DoubleClick += new System.EventHandler(this.panelColor_DoubleClick);
			// 
			// labelTextColor
			// 
			this.labelTextColor.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.labelTextColor.AutoSize = true;
			this.labelTextColor.Location = new System.Drawing.Point(3, 0);
			this.labelTextColor.Name = "labelTextColor";
			this.labelTextColor.Size = new System.Drawing.Size(58, 13);
			this.labelTextColor.TabIndex = 4;
			this.labelTextColor.Text = "Text Color:";
			// 
			// panelTextColor
			// 
			this.panelTextColor.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.panelTextColor.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
			this.panelTextColor.Location = new System.Drawing.Point(6, 16);
			this.panelTextColor.Name = "panelTextColor";
			this.panelTextColor.Size = new System.Drawing.Size(90, 30);
			this.panelTextColor.TabIndex = 5;
			this.panelTextColor.Tag = "TEXT";
			this.toolTip.SetToolTip(this.panelTextColor, "Double-click to change the text color");
			this.panelTextColor.DoubleClick += new System.EventHandler(this.panelColor_DoubleClick);
			// 
			// listBoxGradients
			// 
			this.listBoxGradients.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.listBoxGradients.FormattingEnabled = true;
			this.listBoxGradients.IntegralHeight = false;
			this.listBoxGradients.Location = new System.Drawing.Point(9, 104);
			this.listBoxGradients.Name = "listBoxGradients";
			this.listBoxGradients.Size = new System.Drawing.Size(220, 122);
			this.listBoxGradients.TabIndex = 10;
			this.toolTip.SetToolTip(this.listBoxGradients, "Select the gradient to change");
			this.listBoxGradients.SelectedIndexChanged += new System.EventHandler(this.listBoxGradients_SelectedIndexChanged);
			// 
			// labelGradient
			// 
			this.labelGradient.AutoSize = true;
			this.labelGradient.Location = new System.Drawing.Point(6, 80);
			this.labelGradient.Name = "labelGradient";
			this.labelGradient.Size = new System.Drawing.Size(80, 13);
			this.labelGradient.TabIndex = 9;
			this.labelGradient.Text = "Gradient Mode:";
			// 
			// comboBoxGradient
			// 
			this.comboBoxGradient.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxGradient.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxGradient.FormattingEnabled = true;
			this.comboBoxGradient.Items.AddRange(new object[] {
            "Horizontal",
            "Vertical",
            "Forward Diagonal",
            "Backward Diagonal"});
			this.comboBoxGradient.Location = new System.Drawing.Point(95, 77);
			this.comboBoxGradient.Name = "comboBoxGradient";
			this.comboBoxGradient.Size = new System.Drawing.Size(134, 21);
			this.comboBoxGradient.TabIndex = 8;
			this.toolTip.SetToolTip(this.comboBoxGradient, "Select the mode used to draw the gradient");
			this.comboBoxGradient.SelectedIndexChanged += new System.EventHandler(this.comboBoxGradient_SelectedIndexChanged);
			// 
			// groupBoxSkinType
			// 
			this.groupBoxSkinType.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxSkinType.Controls.Add(this.splitContainerTypes);
			this.groupBoxSkinType.Location = new System.Drawing.Point(12, 12);
			this.groupBoxSkinType.Name = "groupBoxSkinType";
			this.groupBoxSkinType.Size = new System.Drawing.Size(238, 50);
			this.groupBoxSkinType.TabIndex = 8;
			this.groupBoxSkinType.TabStop = false;
			this.groupBoxSkinType.Text = "Skin Type";
			this.toolTip.SetToolTip(this.groupBoxSkinType, "Select the type of panel to change");
			this.groupBoxSkinType.CollapseBoxClickedEvent += new ARCed.Controls.CollapsibleGroupBox.CollapseBoxClickedEventHandler(this.groupBoxSkinType_CollapseBoxClickedEvent);
			// 
			// splitContainerTypes
			// 
			this.splitContainerTypes.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainerTypes.IsSplitterFixed = true;
			this.splitContainerTypes.Location = new System.Drawing.Point(3, 16);
			this.splitContainerTypes.Name = "splitContainerTypes";
			// 
			// splitContainerTypes.Panel1
			// 
			this.splitContainerTypes.Panel1.Controls.Add(this.radioDockPanel);
			// 
			// splitContainerTypes.Panel2
			// 
			this.splitContainerTypes.Panel2.Controls.Add(this.radioAutoHide);
			this.splitContainerTypes.Size = new System.Drawing.Size(232, 31);
			this.splitContainerTypes.SplitterDistance = 106;
			this.splitContainerTypes.SplitterWidth = 1;
			this.splitContainerTypes.TabIndex = 0;
			// 
			// radioDockPanel
			// 
			this.radioDockPanel.AutoSize = true;
			this.radioDockPanel.Checked = true;
			this.radioDockPanel.Location = new System.Drawing.Point(6, 11);
			this.radioDockPanel.Name = "radioDockPanel";
			this.radioDockPanel.Size = new System.Drawing.Size(86, 17);
			this.radioDockPanel.TabIndex = 0;
			this.radioDockPanel.TabStop = true;
			this.radioDockPanel.Text = "Dock Panels";
			this.radioDockPanel.UseVisualStyleBackColor = true;
			this.radioDockPanel.CheckedChanged += new System.EventHandler(this.radioPanel_CheckedChanged);
			// 
			// radioAutoHide
			// 
			this.radioAutoHide.AutoSize = true;
			this.radioAutoHide.Location = new System.Drawing.Point(3, 11);
			this.radioAutoHide.Name = "radioAutoHide";
			this.radioAutoHide.Size = new System.Drawing.Size(101, 17);
			this.radioAutoHide.TabIndex = 1;
			this.radioAutoHide.Text = "Auto-Hide Strips";
			this.radioAutoHide.UseVisualStyleBackColor = true;
			// 
			// buttonDefault
			// 
			this.buttonDefault.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonDefault.Location = new System.Drawing.Point(137, 358);
			this.buttonDefault.Name = "buttonDefault";
			this.buttonDefault.Size = new System.Drawing.Size(111, 23);
			this.buttonDefault.TabIndex = 10;
			this.buttonDefault.Text = "Reset Default";
			this.toolTip.SetToolTip(this.buttonDefault, "Reset all settings to default values.");
			this.buttonDefault.UseVisualStyleBackColor = true;
			this.buttonDefault.Click += new System.EventHandler(this.buttonDefault_Click);
			// 
			// buttonApply
			// 
			this.buttonApply.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonApply.Location = new System.Drawing.Point(58, 358);
			this.buttonApply.Name = "buttonApply";
			this.buttonApply.Size = new System.Drawing.Size(75, 23);
			this.buttonApply.TabIndex = 11;
			this.buttonApply.Text = "Apply";
			this.toolTip.SetToolTip(this.buttonApply, "Apply settings. Changes will take effect next time the window is created.");
			this.buttonApply.UseVisualStyleBackColor = true;
			this.buttonApply.Click += new System.EventHandler(this.buttonApply_Click);
			// 
			// SkinSettingsForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(260, 492);
			this.Controls.Add(this.buttonApply);
			this.Controls.Add(this.buttonDefault);
			this.Controls.Add(this.groupBoxFontSettings);
			this.Controls.Add(this.groupBoxGradientSettings);
			this.Controls.Add(this.groupBoxSkinType);
			this.DefaultFloatSize = new System.Drawing.Size(276, 530);
			this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.Name = "SkinSettingsForm";
			this.ShowHint = ARCed.UI.DockState.DockLeft;
			this.Text = "Skin Settings";
			this.groupBoxFontSettings.ResumeLayout(false);
			this.groupBoxFontSettings.PerformLayout();
			this.groupBoxGradientSettings.ResumeLayout(false);
			this.groupBoxGradientSettings.PerformLayout();
			this.splitContainer1.Panel1.ResumeLayout(false);
			this.splitContainer1.Panel1.PerformLayout();
			this.splitContainer1.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).EndInit();
			this.splitContainer1.ResumeLayout(false);
			this.splitContainer2.Panel1.ResumeLayout(false);
			this.splitContainer2.Panel1.PerformLayout();
			this.splitContainer2.Panel2.ResumeLayout(false);
			this.splitContainer2.Panel2.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainer2)).EndInit();
			this.splitContainer2.ResumeLayout(false);
			this.groupBoxSkinType.ResumeLayout(false);
			this.splitContainerTypes.Panel1.ResumeLayout(false);
			this.splitContainerTypes.Panel1.PerformLayout();
			this.splitContainerTypes.Panel2.ResumeLayout(false);
			this.splitContainerTypes.Panel2.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerTypes)).EndInit();
			this.splitContainerTypes.ResumeLayout(false);
			this.ResumeLayout(false);

		}

		#endregion

		private ARCed.Controls.CollapsibleGroupBox groupBoxGradientSettings;
		private System.Windows.Forms.Label labelGradient;
		private System.Windows.Forms.ComboBox comboBoxGradient;
		private System.Windows.Forms.Button buttonFont;
		private System.Windows.Forms.Label labelFont;
		private System.Windows.Forms.Panel panelTextColor;
		private System.Windows.Forms.Label labelTextColor;
		private System.Windows.Forms.Panel panelEndColor;
		private System.Windows.Forms.Panel panelStartColor;
		private System.Windows.Forms.Label labelEndColor;
		private System.Windows.Forms.Label labelStartColor;
		private System.Windows.Forms.ListBox listBoxGradients;
		private ARCed.Controls.CollapsibleGroupBox groupBoxSkinType;
		private System.Windows.Forms.RadioButton radioAutoHide;
		private System.Windows.Forms.RadioButton radioDockPanel;
		private ARCed.Controls.CollapsibleGroupBox groupBoxFontSettings;
		private System.Windows.Forms.SplitContainer splitContainerTypes;
		private System.Windows.Forms.Button buttonDefault;
		private System.Windows.Forms.SplitContainer splitContainer1;
		private System.Windows.Forms.SplitContainer splitContainer2;
		private System.Windows.Forms.Button buttonApply;
		private System.Windows.Forms.ToolTip toolTip;
	}
}