namespace ARCed.Dialogs
{
	partial class ImageSelectionForm
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
			this.buttonCancel = new System.Windows.Forms.Button();
			this.buttonOK = new System.Windows.Forms.Button();
			this.splitContainer = new System.Windows.Forms.SplitContainer();
			this.listBoxGraphics = new System.Windows.Forms.ListBox();
			this.panelTop = new System.Windows.Forms.Panel();
			this.groupBoxOptions = new System.Windows.Forms.GroupBox();
			this.panelAdvanced = new System.Windows.Forms.Panel();
			this.labelZoom = new System.Windows.Forms.Label();
			this.numericSY = new System.Windows.Forms.NumericUpDown();
			this.labelSY = new System.Windows.Forms.Label();
			this.numericZoom = new System.Windows.Forms.NumericUpDown();
			this.numericSX = new System.Windows.Forms.NumericUpDown();
			this.labelSX = new System.Windows.Forms.Label();
			this.checkAlphaPreview = new System.Windows.Forms.CheckBox();
			this.numericOpacity = new System.Windows.Forms.NumericUpDown();
			this.comboBoxBlend = new System.Windows.Forms.ComboBox();
			this.labelBlending = new System.Windows.Forms.Label();
			this.labelOpacity = new System.Windows.Forms.Label();
			this.groupBoxHue = new System.Windows.Forms.GroupBox();
			this.trackBarHue = new System.Windows.Forms.TrackBar();
			this.labelRtp = new System.Windows.Forms.Label();
			this.labelLocal = new System.Windows.Forms.Label();
			this.buttonOptions = new System.Windows.Forms.Button();
			this.pictureBox = new ARCed.Controls.ImageSelectXnaPanel();
			((System.ComponentModel.ISupportInitialize)(this.splitContainer)).BeginInit();
			this.splitContainer.Panel1.SuspendLayout();
			this.splitContainer.Panel2.SuspendLayout();
			this.splitContainer.SuspendLayout();
			this.panelTop.SuspendLayout();
			this.groupBoxOptions.SuspendLayout();
			this.panelAdvanced.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.numericSY)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.numericZoom)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.numericSX)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.numericOpacity)).BeginInit();
			this.groupBoxHue.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.trackBarHue)).BeginInit();
			this.SuspendLayout();
			// 
			// buttonCancel
			// 
			this.buttonCancel.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
			this.buttonCancel.Location = new System.Drawing.Point(580, 406);
			this.buttonCancel.Name = "buttonCancel";
			this.buttonCancel.Size = new System.Drawing.Size(75, 23);
			this.buttonCancel.TabIndex = 0;
			this.buttonCancel.Text = "Cancel";
			this.buttonCancel.UseVisualStyleBackColor = true;
			// 
			// buttonOK
			// 
			this.buttonOK.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonOK.Location = new System.Drawing.Point(499, 406);
			this.buttonOK.Name = "buttonOK";
			this.buttonOK.Size = new System.Drawing.Size(75, 23);
			this.buttonOK.TabIndex = 1;
			this.buttonOK.Text = "OK";
			this.buttonOK.UseVisualStyleBackColor = true;
			this.buttonOK.Click += new System.EventHandler(this.buttonOK_Click);
			// 
			// splitContainer
			// 
			this.splitContainer.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.splitContainer.Location = new System.Drawing.Point(12, 12);
			this.splitContainer.Name = "splitContainer";
			// 
			// splitContainer.Panel1
			// 
			this.splitContainer.Panel1.Controls.Add(this.listBoxGraphics);
			// 
			// splitContainer.Panel2
			// 
			this.splitContainer.Panel2.Controls.Add(this.panelTop);
			this.splitContainer.Panel2.Controls.Add(this.groupBoxOptions);
			this.splitContainer.Panel2.Controls.Add(this.groupBoxHue);
			this.splitContainer.Size = new System.Drawing.Size(643, 388);
			this.splitContainer.SplitterDistance = 165;
			this.splitContainer.TabIndex = 2;
			// 
			// listBoxGraphics
			// 
			this.listBoxGraphics.Dock = System.Windows.Forms.DockStyle.Fill;
			this.listBoxGraphics.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed;
			this.listBoxGraphics.FormattingEnabled = true;
			this.listBoxGraphics.IntegralHeight = false;
			this.listBoxGraphics.Location = new System.Drawing.Point(0, 0);
			this.listBoxGraphics.Name = "listBoxGraphics";
			this.listBoxGraphics.Size = new System.Drawing.Size(165, 388);
			this.listBoxGraphics.TabIndex = 0;
			this.listBoxGraphics.DrawItem += new System.Windows.Forms.DrawItemEventHandler(this.listBoxGraphics_DrawItem);
			this.listBoxGraphics.SelectedIndexChanged += new System.EventHandler(this.listBoxGraphics_SelectedIndexChanged);
			this.listBoxGraphics.DoubleClick += new System.EventHandler(this.buttonOK_Click);
			// 
			// panelTop
			// 
			this.panelTop.AutoScroll = true;
			this.panelTop.BackColor = System.Drawing.SystemColors.ControlDark;
			this.panelTop.Controls.Add(this.pictureBox);
			this.panelTop.Dock = System.Windows.Forms.DockStyle.Fill;
			this.panelTop.Location = new System.Drawing.Point(0, 0);
			this.panelTop.Name = "panelTop";
			this.panelTop.Size = new System.Drawing.Size(385, 322);
			this.panelTop.TabIndex = 3;
			// 
			// groupBoxOptions
			// 
			this.groupBoxOptions.Controls.Add(this.panelAdvanced);
			this.groupBoxOptions.Controls.Add(this.checkAlphaPreview);
			this.groupBoxOptions.Controls.Add(this.numericOpacity);
			this.groupBoxOptions.Controls.Add(this.comboBoxBlend);
			this.groupBoxOptions.Controls.Add(this.labelBlending);
			this.groupBoxOptions.Controls.Add(this.labelOpacity);
			this.groupBoxOptions.Dock = System.Windows.Forms.DockStyle.Right;
			this.groupBoxOptions.Enabled = false;
			this.groupBoxOptions.Location = new System.Drawing.Point(385, 0);
			this.groupBoxOptions.Name = "groupBoxOptions";
			this.groupBoxOptions.Size = new System.Drawing.Size(89, 322);
			this.groupBoxOptions.TabIndex = 2;
			this.groupBoxOptions.TabStop = false;
			this.groupBoxOptions.Text = "Options";
			// 
			// panelAdvanced
			// 
			this.panelAdvanced.Controls.Add(this.labelZoom);
			this.panelAdvanced.Controls.Add(this.numericSY);
			this.panelAdvanced.Controls.Add(this.labelSY);
			this.panelAdvanced.Controls.Add(this.numericZoom);
			this.panelAdvanced.Controls.Add(this.numericSX);
			this.panelAdvanced.Controls.Add(this.labelSX);
			this.panelAdvanced.Enabled = false;
			this.panelAdvanced.Location = new System.Drawing.Point(9, 116);
			this.panelAdvanced.Name = "panelAdvanced";
			this.panelAdvanced.Size = new System.Drawing.Size(74, 154);
			this.panelAdvanced.TabIndex = 11;
			// 
			// labelZoom
			// 
			this.labelZoom.AutoSize = true;
			this.labelZoom.Location = new System.Drawing.Point(-3, 0);
			this.labelZoom.Name = "labelZoom";
			this.labelZoom.Size = new System.Drawing.Size(48, 13);
			this.labelZoom.TabIndex = 2;
			this.labelZoom.Text = "Zoom %:";
			// 
			// numericSY
			// 
			this.numericSY.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.numericSY.Location = new System.Drawing.Point(0, 112);
			this.numericSY.Maximum = new decimal(new int[] {
            480,
            0,
            0,
            0});
			this.numericSY.Minimum = new decimal(new int[] {
            480,
            0,
            0,
            -2147483648});
			this.numericSY.Name = "numericSY";
			this.numericSY.Size = new System.Drawing.Size(74, 20);
			this.numericSY.TabIndex = 9;
			this.numericSY.ValueChanged += new System.EventHandler(this.imageOption_Changed);
			// 
			// labelSY
			// 
			this.labelSY.AutoSize = true;
			this.labelSY.Location = new System.Drawing.Point(-3, 96);
			this.labelSY.Name = "labelSY";
			this.labelSY.Size = new System.Drawing.Size(46, 13);
			this.labelSY.TabIndex = 4;
			this.labelSY.Text = "Scroll Y:";
			// 
			// numericZoom
			// 
			this.numericZoom.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.numericZoom.Location = new System.Drawing.Point(0, 16);
			this.numericZoom.Maximum = new decimal(new int[] {
            800,
            0,
            0,
            0});
			this.numericZoom.Minimum = new decimal(new int[] {
            100,
            0,
            0,
            0});
			this.numericZoom.Name = "numericZoom";
			this.numericZoom.Size = new System.Drawing.Size(74, 20);
			this.numericZoom.TabIndex = 7;
			this.numericZoom.Value = new decimal(new int[] {
            100,
            0,
            0,
            0});
			this.numericZoom.ValueChanged += new System.EventHandler(this.imageOption_Changed);
			// 
			// numericSX
			// 
			this.numericSX.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.numericSX.Location = new System.Drawing.Point(0, 64);
			this.numericSX.Maximum = new decimal(new int[] {
            480,
            0,
            0,
            0});
			this.numericSX.Minimum = new decimal(new int[] {
            480,
            0,
            0,
            -2147483648});
			this.numericSX.Name = "numericSX";
			this.numericSX.Size = new System.Drawing.Size(74, 20);
			this.numericSX.TabIndex = 8;
			this.numericSX.ValueChanged += new System.EventHandler(this.imageOption_Changed);
			// 
			// labelSX
			// 
			this.labelSX.AutoSize = true;
			this.labelSX.Location = new System.Drawing.Point(-3, 48);
			this.labelSX.Name = "labelSX";
			this.labelSX.Size = new System.Drawing.Size(46, 13);
			this.labelSX.TabIndex = 3;
			this.labelSX.Text = "Scroll X:";
			// 
			// checkAlphaPreview
			// 
			this.checkAlphaPreview.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.checkAlphaPreview.Location = new System.Drawing.Point(9, 276);
			this.checkAlphaPreview.Name = "checkAlphaPreview";
			this.checkAlphaPreview.Size = new System.Drawing.Size(74, 40);
			this.checkAlphaPreview.TabIndex = 10;
			this.checkAlphaPreview.Text = "Alpha Preview";
			this.checkAlphaPreview.UseVisualStyleBackColor = true;
			this.checkAlphaPreview.CheckedChanged += new System.EventHandler(this.checkAlphaPreview_CheckedChanged);
			// 
			// numericOpacity
			// 
			this.numericOpacity.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.numericOpacity.Location = new System.Drawing.Point(9, 41);
			this.numericOpacity.Maximum = new decimal(new int[] {
            255,
            0,
            0,
            0});
			this.numericOpacity.Name = "numericOpacity";
			this.numericOpacity.Size = new System.Drawing.Size(74, 20);
			this.numericOpacity.TabIndex = 6;
			this.numericOpacity.ValueChanged += new System.EventHandler(this.numericOpacity_ValueChanged);
			// 
			// comboBoxBlend
			// 
			this.comboBoxBlend.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxBlend.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxBlend.FormattingEnabled = true;
			this.comboBoxBlend.Items.AddRange(new object[] {
            "Normal",
            "Add",
            "Sub"});
			this.comboBoxBlend.Location = new System.Drawing.Point(9, 89);
			this.comboBoxBlend.Name = "comboBoxBlend";
			this.comboBoxBlend.Size = new System.Drawing.Size(74, 21);
			this.comboBoxBlend.TabIndex = 5;
			this.comboBoxBlend.SelectedIndexChanged += new System.EventHandler(this.imageOption_Changed);
			// 
			// labelBlending
			// 
			this.labelBlending.AutoSize = true;
			this.labelBlending.Location = new System.Drawing.Point(6, 73);
			this.labelBlending.Name = "labelBlending";
			this.labelBlending.Size = new System.Drawing.Size(51, 13);
			this.labelBlending.TabIndex = 1;
			this.labelBlending.Text = "Blending:";
			// 
			// labelOpacity
			// 
			this.labelOpacity.AutoSize = true;
			this.labelOpacity.Location = new System.Drawing.Point(6, 25);
			this.labelOpacity.Name = "labelOpacity";
			this.labelOpacity.Size = new System.Drawing.Size(46, 13);
			this.labelOpacity.TabIndex = 0;
			this.labelOpacity.Text = "Opacity:";
			// 
			// groupBoxHue
			// 
			this.groupBoxHue.Controls.Add(this.trackBarHue);
			this.groupBoxHue.Dock = System.Windows.Forms.DockStyle.Bottom;
			this.groupBoxHue.Enabled = false;
			this.groupBoxHue.Location = new System.Drawing.Point(0, 322);
			this.groupBoxHue.Name = "groupBoxHue";
			this.groupBoxHue.Size = new System.Drawing.Size(474, 66);
			this.groupBoxHue.TabIndex = 0;
			this.groupBoxHue.TabStop = false;
			this.groupBoxHue.Text = "Hue";
			// 
			// trackBarHue
			// 
			this.trackBarHue.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.trackBarHue.Location = new System.Drawing.Point(6, 15);
			this.trackBarHue.Maximum = 359;
			this.trackBarHue.Name = "trackBarHue";
			this.trackBarHue.Size = new System.Drawing.Size(462, 45);
			this.trackBarHue.TabIndex = 0;
			this.trackBarHue.TickFrequency = 8;
			this.trackBarHue.ValueChanged += new System.EventHandler(this.imageOption_Changed);
			// 
			// labelRtp
			// 
			this.labelRtp.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.labelRtp.AutoSize = true;
			this.labelRtp.Image = global::ARCed.Properties.Resources.ResourceRTP;
			this.labelRtp.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
			this.labelRtp.Location = new System.Drawing.Point(86, 411);
			this.labelRtp.Name = "labelRtp";
			this.labelRtp.Size = new System.Drawing.Size(50, 13);
			this.labelRtp.TabIndex = 3;
			this.labelRtp.Text = "     : RTP";
			this.labelRtp.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
			// 
			// labelLocal
			// 
			this.labelLocal.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.labelLocal.AutoSize = true;
			this.labelLocal.Image = global::ARCed.Properties.Resources.ResourceLocal;
			this.labelLocal.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
			this.labelLocal.Location = new System.Drawing.Point(12, 411);
			this.labelLocal.Name = "labelLocal";
			this.labelLocal.Size = new System.Drawing.Size(54, 13);
			this.labelLocal.TabIndex = 4;
			this.labelLocal.Text = "     : Local";
			this.labelLocal.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
			// 
			// buttonOptions
			// 
			this.buttonOptions.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonOptions.Location = new System.Drawing.Point(418, 406);
			this.buttonOptions.Name = "buttonOptions";
			this.buttonOptions.Size = new System.Drawing.Size(75, 23);
			this.buttonOptions.TabIndex = 5;
			this.buttonOptions.Text = "Options...";
			this.buttonOptions.UseVisualStyleBackColor = true;
			// 
			// pictureBox
			// 
			this.pictureBox.AdvancedEnabled = false;
			this.pictureBox.AlphaPreview = false;
			this.pictureBox.BackColor = System.Drawing.SystemColors.ControlDark;
			this.pictureBox.BlendMode = 0;
			this.pictureBox.Image = null;
			this.pictureBox.ImageOpacity = 255;
			this.pictureBox.Location = new System.Drawing.Point(0, 0);
			this.pictureBox.Name = "pictureBox";
			this.pictureBox.ScrollX = 0;
			this.pictureBox.ScrollY = 0;
			this.pictureBox.SelectionEnabled = false;
			this.pictureBox.Size = new System.Drawing.Size(269, 184);
			this.pictureBox.TabIndex = 0;
			this.pictureBox.Text = "pictureBox";
			this.pictureBox.Zoom = 0;
			// 
			// ImageSelectionForm
			// 
			this.AcceptButton = this.buttonOK;
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.CancelButton = this.buttonCancel;
			this.ClientSize = new System.Drawing.Size(667, 441);
			this.Controls.Add(this.buttonOptions);
			this.Controls.Add(this.labelLocal);
			this.Controls.Add(this.labelRtp);
			this.Controls.Add(this.splitContainer);
			this.Controls.Add(this.buttonOK);
			this.Controls.Add(this.buttonCancel);
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.SizableToolWindow;
			this.Name = "ImageSelectionForm";
			this.ShowIcon = false;
			this.ShowInTaskbar = false;
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
			this.Text = "Select Graphic";
			this.Load += new System.EventHandler(this.ImageSelectionForm_Load);
			this.splitContainer.Panel1.ResumeLayout(false);
			this.splitContainer.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainer)).EndInit();
			this.splitContainer.ResumeLayout(false);
			this.panelTop.ResumeLayout(false);
			this.groupBoxOptions.ResumeLayout(false);
			this.groupBoxOptions.PerformLayout();
			this.panelAdvanced.ResumeLayout(false);
			this.panelAdvanced.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.numericSY)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.numericZoom)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.numericSX)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.numericOpacity)).EndInit();
			this.groupBoxHue.ResumeLayout(false);
			this.groupBoxHue.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.trackBarHue)).EndInit();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Button buttonCancel;
		private System.Windows.Forms.Button buttonOK;
		private System.Windows.Forms.SplitContainer splitContainer;
		private System.Windows.Forms.ListBox listBoxGraphics;
		private System.Windows.Forms.GroupBox groupBoxHue;
		private System.Windows.Forms.TrackBar trackBarHue;
		private System.Windows.Forms.Label labelRtp;
		private System.Windows.Forms.Label labelLocal;
		private System.Windows.Forms.GroupBox groupBoxOptions;
		private System.Windows.Forms.Label labelSY;
		private System.Windows.Forms.Label labelSX;
		private System.Windows.Forms.Label labelZoom;
		private System.Windows.Forms.Label labelBlending;
		private System.Windows.Forms.Label labelOpacity;
		private System.Windows.Forms.NumericUpDown numericSY;
		private System.Windows.Forms.NumericUpDown numericSX;
		private System.Windows.Forms.NumericUpDown numericZoom;
		private System.Windows.Forms.NumericUpDown numericOpacity;
		private System.Windows.Forms.ComboBox comboBoxBlend;
		private System.Windows.Forms.Panel panelTop;
		private Controls.ImageSelectXnaPanel pictureBox;
		private System.Windows.Forms.CheckBox checkAlphaPreview;
		private System.Windows.Forms.Button buttonOptions;
		private System.Windows.Forms.Panel panelAdvanced;
	}
}