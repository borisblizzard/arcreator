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
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(ImageSelectionForm));
            this.buttonCancel = new System.Windows.Forms.Button();
            this.buttonOK = new System.Windows.Forms.Button();
            this.splitContainer = new System.Windows.Forms.SplitContainer();
            this.listBoxGraphics = new System.Windows.Forms.ListBox();
            this.panelTop = new System.Windows.Forms.Panel();
            this.pictureBox = new ARCed.Controls.ImageSelectXnaPanel();
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
            this.buttonColor = new System.Windows.Forms.Button();
            this.toolTip = new System.Windows.Forms.ToolTip(this.components);
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
            resources.ApplyResources(this.buttonCancel, "buttonCancel");
            this.buttonCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.buttonCancel.Name = "buttonCancel";
            this.toolTip.SetToolTip(this.buttonCancel, resources.GetString("buttonCancel.ToolTip"));
            this.buttonCancel.UseVisualStyleBackColor = true;
            // 
            // buttonOK
            // 
            resources.ApplyResources(this.buttonOK, "buttonOK");
            this.buttonOK.Name = "buttonOK";
            this.toolTip.SetToolTip(this.buttonOK, resources.GetString("buttonOK.ToolTip"));
            this.buttonOK.UseVisualStyleBackColor = true;
            this.buttonOK.Click += new System.EventHandler(this.buttonOK_Click);
            // 
            // splitContainer
            // 
            resources.ApplyResources(this.splitContainer, "splitContainer");
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
            // 
            // listBoxGraphics
            // 
            resources.ApplyResources(this.listBoxGraphics, "listBoxGraphics");
            this.listBoxGraphics.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed;
            this.listBoxGraphics.FormattingEnabled = true;
            this.listBoxGraphics.Name = "listBoxGraphics";
            this.listBoxGraphics.DrawItem += new System.Windows.Forms.DrawItemEventHandler(this.listBoxGraphics_DrawItem);
            this.listBoxGraphics.SelectedIndexChanged += new System.EventHandler(this.listBoxGraphics_SelectedIndexChanged);
            this.listBoxGraphics.DoubleClick += new System.EventHandler(this.buttonOK_Click);
            // 
            // panelTop
            // 
            resources.ApplyResources(this.panelTop, "panelTop");
            this.panelTop.BackColor = System.Drawing.SystemColors.ControlDark;
            this.panelTop.Controls.Add(this.pictureBox);
            this.panelTop.Name = "panelTop";
            // 
            // pictureBox
            // 
            this.pictureBox.AdvancedEnabled = false;
            this.pictureBox.AlphaPreview = false;
            this.pictureBox.BackColor = System.Drawing.SystemColors.ControlDark;
            this.pictureBox.BlendMode = 0;
            this.pictureBox.Image = null;
            this.pictureBox.ImageBackColor = new Microsoft.Xna.Framework.Color(((int)(((byte)(0)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))));
            this.pictureBox.ImageOpacity = 255;
            resources.ApplyResources(this.pictureBox, "pictureBox");
            this.pictureBox.Name = "pictureBox";
            this.pictureBox.ScrollX = 0;
            this.pictureBox.ScrollY = 0;
            this.pictureBox.SelectionEnabled = false;
            this.pictureBox.Zoom = 0;
            // 
            // groupBoxOptions
            // 
            this.groupBoxOptions.Controls.Add(this.panelAdvanced);
            this.groupBoxOptions.Controls.Add(this.checkAlphaPreview);
            this.groupBoxOptions.Controls.Add(this.numericOpacity);
            this.groupBoxOptions.Controls.Add(this.comboBoxBlend);
            this.groupBoxOptions.Controls.Add(this.labelBlending);
            this.groupBoxOptions.Controls.Add(this.labelOpacity);
            resources.ApplyResources(this.groupBoxOptions, "groupBoxOptions");
            this.groupBoxOptions.Name = "groupBoxOptions";
            this.groupBoxOptions.TabStop = false;
            // 
            // panelAdvanced
            // 
            this.panelAdvanced.Controls.Add(this.labelZoom);
            this.panelAdvanced.Controls.Add(this.numericSY);
            this.panelAdvanced.Controls.Add(this.labelSY);
            this.panelAdvanced.Controls.Add(this.numericZoom);
            this.panelAdvanced.Controls.Add(this.numericSX);
            this.panelAdvanced.Controls.Add(this.labelSX);
            resources.ApplyResources(this.panelAdvanced, "panelAdvanced");
            this.panelAdvanced.Name = "panelAdvanced";
            // 
            // labelZoom
            // 
            resources.ApplyResources(this.labelZoom, "labelZoom");
            this.labelZoom.Name = "labelZoom";
            // 
            // numericSY
            // 
            resources.ApplyResources(this.numericSY, "numericSY");
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
            this.toolTip.SetToolTip(this.numericSY, resources.GetString("numericSY.ToolTip"));
            this.numericSY.ValueChanged += new System.EventHandler(this.imageOption_Changed);
            // 
            // labelSY
            // 
            resources.ApplyResources(this.labelSY, "labelSY");
            this.labelSY.Name = "labelSY";
            // 
            // numericZoom
            // 
            resources.ApplyResources(this.numericZoom, "numericZoom");
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
            this.toolTip.SetToolTip(this.numericZoom, resources.GetString("numericZoom.ToolTip"));
            this.numericZoom.Value = new decimal(new int[] {
            100,
            0,
            0,
            0});
            this.numericZoom.ValueChanged += new System.EventHandler(this.imageOption_Changed);
            // 
            // numericSX
            // 
            resources.ApplyResources(this.numericSX, "numericSX");
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
            this.toolTip.SetToolTip(this.numericSX, resources.GetString("numericSX.ToolTip"));
            this.numericSX.ValueChanged += new System.EventHandler(this.imageOption_Changed);
            // 
            // labelSX
            // 
            resources.ApplyResources(this.labelSX, "labelSX");
            this.labelSX.Name = "labelSX";
            // 
            // checkAlphaPreview
            // 
            resources.ApplyResources(this.checkAlphaPreview, "checkAlphaPreview");
            this.checkAlphaPreview.Name = "checkAlphaPreview";
            this.toolTip.SetToolTip(this.checkAlphaPreview, resources.GetString("checkAlphaPreview.ToolTip"));
            this.checkAlphaPreview.UseVisualStyleBackColor = true;
            this.checkAlphaPreview.CheckedChanged += new System.EventHandler(this.checkAlphaPreview_CheckedChanged);
            // 
            // numericOpacity
            // 
            resources.ApplyResources(this.numericOpacity, "numericOpacity");
            this.numericOpacity.Maximum = new decimal(new int[] {
            255,
            0,
            0,
            0});
            this.numericOpacity.Name = "numericOpacity";
            this.toolTip.SetToolTip(this.numericOpacity, resources.GetString("numericOpacity.ToolTip"));
            this.numericOpacity.ValueChanged += new System.EventHandler(this.numericOpacity_ValueChanged);
            // 
            // comboBoxBlend
            // 
            resources.ApplyResources(this.comboBoxBlend, "comboBoxBlend");
            this.comboBoxBlend.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.comboBoxBlend.FormattingEnabled = true;
            this.comboBoxBlend.Items.AddRange(new object[] {
            resources.GetString("comboBoxBlend.Items"),
            resources.GetString("comboBoxBlend.Items1"),
            resources.GetString("comboBoxBlend.Items2")});
            this.comboBoxBlend.Name = "comboBoxBlend";
            this.toolTip.SetToolTip(this.comboBoxBlend, resources.GetString("comboBoxBlend.ToolTip"));
            this.comboBoxBlend.SelectedIndexChanged += new System.EventHandler(this.imageOption_Changed);
            // 
            // labelBlending
            // 
            resources.ApplyResources(this.labelBlending, "labelBlending");
            this.labelBlending.Name = "labelBlending";
            // 
            // labelOpacity
            // 
            resources.ApplyResources(this.labelOpacity, "labelOpacity");
            this.labelOpacity.Name = "labelOpacity";
            // 
            // groupBoxHue
            // 
            this.groupBoxHue.Controls.Add(this.trackBarHue);
            resources.ApplyResources(this.groupBoxHue, "groupBoxHue");
            this.groupBoxHue.Name = "groupBoxHue";
            this.groupBoxHue.TabStop = false;
            // 
            // trackBarHue
            // 
            resources.ApplyResources(this.trackBarHue, "trackBarHue");
            this.trackBarHue.Maximum = 359;
            this.trackBarHue.Name = "trackBarHue";
            this.trackBarHue.TickFrequency = 8;
            this.toolTip.SetToolTip(this.trackBarHue, resources.GetString("trackBarHue.ToolTip"));
            this.trackBarHue.ValueChanged += new System.EventHandler(this.imageOption_Changed);
            // 
            // labelRtp
            // 
            resources.ApplyResources(this.labelRtp, "labelRtp");
            this.labelRtp.Image = global::ARCed.Properties.Resources.ResourceRTP;
            this.labelRtp.Name = "labelRtp";
            // 
            // labelLocal
            // 
            resources.ApplyResources(this.labelLocal, "labelLocal");
            this.labelLocal.Image = global::ARCed.Properties.Resources.ResourceLocal;
            this.labelLocal.Name = "labelLocal";
            // 
            // buttonColor
            // 
            resources.ApplyResources(this.buttonColor, "buttonColor");
            this.buttonColor.Name = "buttonColor";
            this.toolTip.SetToolTip(this.buttonColor, resources.GetString("buttonColor.ToolTip"));
            this.buttonColor.UseVisualStyleBackColor = true;
            this.buttonColor.Click += new System.EventHandler(this.buttonColor_Click);
            // 
            // ImageSelectionForm
            // 
            this.AcceptButton = this.buttonOK;
            resources.ApplyResources(this, "$this");
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.CancelButton = this.buttonCancel;
            this.Controls.Add(this.buttonColor);
            this.Controls.Add(this.labelLocal);
            this.Controls.Add(this.labelRtp);
            this.Controls.Add(this.splitContainer);
            this.Controls.Add(this.buttonOK);
            this.Controls.Add(this.buttonCancel);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.SizableToolWindow;
            this.Name = "ImageSelectionForm";
            this.ShowIcon = false;
            this.ShowInTaskbar = false;
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
		private System.Windows.Forms.Button buttonColor;
		private System.Windows.Forms.Panel panelAdvanced;
		private System.Windows.Forms.ToolTip toolTip;
	}
}