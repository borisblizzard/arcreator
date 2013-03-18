namespace ARCed.Database.Actors
{
	partial class ChartSettingsForm
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
			this.checkBox3D = new System.Windows.Forms.CheckBox();
			this.numericDepth = new System.Windows.Forms.NumericUpDown();
			this.labelDepth = new System.Windows.Forms.Label();
			this.numericPerspective = new System.Windows.Forms.NumericUpDown();
			this.numericRotation = new System.Windows.Forms.NumericUpDown();
			this.numericInclination = new System.Windows.Forms.NumericUpDown();
			this.labelPerspective = new System.Windows.Forms.Label();
			this.labelRotation = new System.Windows.Forms.Label();
			this.labelInclination = new System.Windows.Forms.Label();
			this.checkBoxMarkerLines = new System.Windows.Forms.CheckBox();
			this.comboBoxLighting = new System.Windows.Forms.ComboBox();
			this.labelLighting = new System.Windows.Forms.Label();
			this.numericTension = new System.Windows.Forms.NumericUpDown();
			this.labelTension = new System.Windows.Forms.Label();
			this.comboBoxType = new System.Windows.Forms.ComboBox();
			this.labelType = new System.Windows.Forms.Label();
			this.splitContainer = new System.Windows.Forms.SplitContainer();
			this.collapsibleGroupBox1 = new ARCed.Controls.CollapsibleGroupBox();
			this.buttonDefaultColors = new System.Windows.Forms.Button();
			this.buttonDown = new System.Windows.Forms.Button();
			this.buttonUp = new System.Windows.Forms.Button();
			this.buttonRemove = new System.Windows.Forms.Button();
			this.buttonAdd = new System.Windows.Forms.Button();
			this.listBoxColors = new System.Windows.Forms.ListBox();
			this.toolTip = new System.Windows.Forms.ToolTip(this.components);
			((System.ComponentModel.ISupportInitialize)(this.numericDepth)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.numericPerspective)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.numericRotation)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.numericInclination)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.numericTension)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.splitContainer)).BeginInit();
			this.splitContainer.Panel1.SuspendLayout();
			this.splitContainer.Panel2.SuspendLayout();
			this.splitContainer.SuspendLayout();
			this.collapsibleGroupBox1.SuspendLayout();
			this.SuspendLayout();
			// 
			// checkBox3D
			// 
			this.checkBox3D.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.checkBox3D.AutoSize = true;
			this.checkBox3D.Checked = true;
			this.checkBox3D.CheckState = System.Windows.Forms.CheckState.Checked;
			this.checkBox3D.Location = new System.Drawing.Point(6, 150);
			this.checkBox3D.Name = "checkBox3D";
			this.checkBox3D.Size = new System.Drawing.Size(92, 17);
			this.checkBox3D.TabIndex = 22;
			this.checkBox3D.Text = "3-Dimensional";
			this.toolTip.SetToolTip(this.checkBox3D, "Enable/Disable three-dimensional view of chart");
			this.checkBox3D.UseVisualStyleBackColor = true;
			this.checkBox3D.CheckedChanged += new System.EventHandler(this.CheckBox3DCheckedChanged);
			// 
			// numericDepth
			// 
			this.numericDepth.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.numericDepth.Location = new System.Drawing.Point(12, 160);
			this.numericDepth.Maximum = new decimal(new int[] {
            500,
            0,
            0,
            0});
			this.numericDepth.Minimum = new decimal(new int[] {
            5,
            0,
            0,
            0});
			this.numericDepth.Name = "numericDepth";
			this.numericDepth.Size = new System.Drawing.Size(92, 20);
			this.numericDepth.TabIndex = 21;
			this.toolTip.SetToolTip(this.numericDepth, "Depth of the chart (3D only)");
			this.numericDepth.Value = new decimal(new int[] {
            5,
            0,
            0,
            0});
			this.numericDepth.ValueChanged += new System.EventHandler(this.NumericDepthValueChanged);
			// 
			// labelDepth
			// 
			this.labelDepth.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.labelDepth.AutoSize = true;
			this.labelDepth.Location = new System.Drawing.Point(9, 144);
			this.labelDepth.Name = "labelDepth";
			this.labelDepth.Size = new System.Drawing.Size(39, 13);
			this.labelDepth.TabIndex = 20;
			this.labelDepth.Text = "Depth:";
			// 
			// numericPerspective
			// 
			this.numericPerspective.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.numericPerspective.Location = new System.Drawing.Point(6, 70);
			this.numericPerspective.Name = "numericPerspective";
			this.numericPerspective.Size = new System.Drawing.Size(89, 20);
			this.numericPerspective.TabIndex = 19;
			this.toolTip.SetToolTip(this.numericPerspective, "Perspective of the chart (3D only)");
			this.numericPerspective.ValueChanged += new System.EventHandler(this.NumericPerspectiveValueChanged);
			// 
			// numericRotation
			// 
			this.numericRotation.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.numericRotation.Location = new System.Drawing.Point(6, 115);
			this.numericRotation.Maximum = new decimal(new int[] {
            90,
            0,
            0,
            0});
			this.numericRotation.Minimum = new decimal(new int[] {
            90,
            0,
            0,
            -2147483648});
			this.numericRotation.Name = "numericRotation";
			this.numericRotation.Size = new System.Drawing.Size(89, 20);
			this.numericRotation.TabIndex = 18;
			this.toolTip.SetToolTip(this.numericRotation, "Rotation of the chart (3D only)");
			this.numericRotation.ValueChanged += new System.EventHandler(this.NumericRotationValueChanged);
			// 
			// numericInclination
			// 
			this.numericInclination.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.numericInclination.Location = new System.Drawing.Point(12, 115);
			this.numericInclination.Maximum = new decimal(new int[] {
            90,
            0,
            0,
            0});
			this.numericInclination.Minimum = new decimal(new int[] {
            90,
            0,
            0,
            -2147483648});
			this.numericInclination.Name = "numericInclination";
			this.numericInclination.Size = new System.Drawing.Size(92, 20);
			this.numericInclination.TabIndex = 17;
			this.toolTip.SetToolTip(this.numericInclination, "Inclination of the chart (3D only)");
			this.numericInclination.ValueChanged += new System.EventHandler(this.NumericInclinationValueChanged);
			// 
			// labelPerspective
			// 
			this.labelPerspective.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.labelPerspective.AutoSize = true;
			this.labelPerspective.Location = new System.Drawing.Point(3, 54);
			this.labelPerspective.Name = "labelPerspective";
			this.labelPerspective.Size = new System.Drawing.Size(66, 13);
			this.labelPerspective.TabIndex = 16;
			this.labelPerspective.Text = "Perspective:";
			// 
			// labelRotation
			// 
			this.labelRotation.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.labelRotation.AutoSize = true;
			this.labelRotation.Location = new System.Drawing.Point(3, 99);
			this.labelRotation.Name = "labelRotation";
			this.labelRotation.Size = new System.Drawing.Size(50, 13);
			this.labelRotation.TabIndex = 15;
			this.labelRotation.Text = "Rotation:";
			// 
			// labelInclination
			// 
			this.labelInclination.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.labelInclination.AutoSize = true;
			this.labelInclination.Location = new System.Drawing.Point(9, 99);
			this.labelInclination.Name = "labelInclination";
			this.labelInclination.Size = new System.Drawing.Size(58, 13);
			this.labelInclination.TabIndex = 14;
			this.labelInclination.Text = "Inclination:";
			// 
			// checkBoxMarkerLines
			// 
			this.checkBoxMarkerLines.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.checkBoxMarkerLines.AutoSize = true;
			this.checkBoxMarkerLines.Location = new System.Drawing.Point(6, 173);
			this.checkBoxMarkerLines.Name = "checkBoxMarkerLines";
			this.checkBoxMarkerLines.Size = new System.Drawing.Size(87, 17);
			this.checkBoxMarkerLines.TabIndex = 13;
			this.checkBoxMarkerLines.Text = "Marker Lines";
			this.toolTip.SetToolTip(this.checkBoxMarkerLines, "Toggle marker line display");
			this.checkBoxMarkerLines.UseVisualStyleBackColor = true;
			this.checkBoxMarkerLines.CheckStateChanged += new System.EventHandler(this.CheckBoxMarkerLinesCheckedChanged);
			// 
			// comboBoxLighting
			// 
			this.comboBoxLighting.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxLighting.FormattingEnabled = true;
			this.comboBoxLighting.Items.AddRange(new object[] {
            "None",
            "Simplistic",
            "Realistic"});
			this.comboBoxLighting.Location = new System.Drawing.Point(6, 25);
			this.comboBoxLighting.Name = "comboBoxLighting";
			this.comboBoxLighting.Size = new System.Drawing.Size(89, 21);
			this.comboBoxLighting.TabIndex = 12;
			this.toolTip.SetToolTip(this.comboBoxLighting, "Lighting effects applied to the chart");
			this.comboBoxLighting.SelectedIndexChanged += new System.EventHandler(this.ComboBoxLightingSelectedIndexChanged);
			// 
			// labelLighting
			// 
			this.labelLighting.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.labelLighting.AutoSize = true;
			this.labelLighting.Location = new System.Drawing.Point(3, 9);
			this.labelLighting.Name = "labelLighting";
			this.labelLighting.Size = new System.Drawing.Size(44, 13);
			this.labelLighting.TabIndex = 11;
			this.labelLighting.Text = "Lighting";
			// 
			// numericTension
			// 
			this.numericTension.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.numericTension.DecimalPlaces = 1;
			this.numericTension.Increment = new decimal(new int[] {
            1,
            0,
            0,
            65536});
			this.numericTension.Location = new System.Drawing.Point(12, 70);
			this.numericTension.Maximum = new decimal(new int[] {
            2,
            0,
            0,
            0});
			this.numericTension.Name = "numericTension";
			this.numericTension.Size = new System.Drawing.Size(92, 20);
			this.numericTension.TabIndex = 10;
			this.toolTip.SetToolTip(this.numericTension, "Tension of the line across the splines");
			this.numericTension.ValueChanged += new System.EventHandler(this.NumericTensionValueChanged);
			// 
			// labelTension
			// 
			this.labelTension.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.labelTension.AutoSize = true;
			this.labelTension.Location = new System.Drawing.Point(9, 54);
			this.labelTension.Name = "labelTension";
			this.labelTension.Size = new System.Drawing.Size(80, 13);
			this.labelTension.TabIndex = 9;
			this.labelTension.Text = "Spline Tension:";
			// 
			// comboBoxType
			// 
			this.comboBoxType.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxType.FormattingEnabled = true;
			this.comboBoxType.Items.AddRange(new object[] {
            "Spline Range",
            "Spline Area",
            "Spline",
            "Step Line",
            "Range Column",
            "Points"});
			this.comboBoxType.Location = new System.Drawing.Point(12, 25);
			this.comboBoxType.Name = "comboBoxType";
			this.comboBoxType.Size = new System.Drawing.Size(92, 21);
			this.comboBoxType.TabIndex = 8;
			this.toolTip.SetToolTip(this.comboBoxType, "Display type of the charts");
			this.comboBoxType.SelectedIndexChanged += new System.EventHandler(this.ComboBoxTypeSelectedIndexChanged);
			// 
			// labelType
			// 
			this.labelType.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.labelType.AutoSize = true;
			this.labelType.Location = new System.Drawing.Point(9, 9);
			this.labelType.Name = "labelType";
			this.labelType.Size = new System.Drawing.Size(62, 13);
			this.labelType.TabIndex = 7;
			this.labelType.Text = "Chart Type:";
			// 
			// splitContainer
			// 
			this.splitContainer.Dock = System.Windows.Forms.DockStyle.Top;
			this.splitContainer.Location = new System.Drawing.Point(0, 0);
			this.splitContainer.Name = "splitContainer";
			// 
			// splitContainer.Panel1
			// 
			this.splitContainer.Panel1.Controls.Add(this.labelType);
			this.splitContainer.Panel1.Controls.Add(this.labelInclination);
			this.splitContainer.Panel1.Controls.Add(this.labelDepth);
			this.splitContainer.Panel1.Controls.Add(this.comboBoxType);
			this.splitContainer.Panel1.Controls.Add(this.labelTension);
			this.splitContainer.Panel1.Controls.Add(this.numericDepth);
			this.splitContainer.Panel1.Controls.Add(this.numericInclination);
			this.splitContainer.Panel1.Controls.Add(this.numericTension);
			// 
			// splitContainer.Panel2
			// 
			this.splitContainer.Panel2.Controls.Add(this.labelLighting);
			this.splitContainer.Panel2.Controls.Add(this.labelRotation);
			this.splitContainer.Panel2.Controls.Add(this.numericPerspective);
			this.splitContainer.Panel2.Controls.Add(this.checkBoxMarkerLines);
			this.splitContainer.Panel2.Controls.Add(this.checkBox3D);
			this.splitContainer.Panel2.Controls.Add(this.numericRotation);
			this.splitContainer.Panel2.Controls.Add(this.labelPerspective);
			this.splitContainer.Panel2.Controls.Add(this.comboBoxLighting);
			this.splitContainer.Size = new System.Drawing.Size(218, 205);
			this.splitContainer.SplitterDistance = 107;
			this.splitContainer.TabIndex = 24;
			// 
			// collapsibleGroupBox1
			// 
			this.collapsibleGroupBox1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.collapsibleGroupBox1.Controls.Add(this.buttonDefaultColors);
			this.collapsibleGroupBox1.Controls.Add(this.buttonDown);
			this.collapsibleGroupBox1.Controls.Add(this.buttonUp);
			this.collapsibleGroupBox1.Controls.Add(this.buttonRemove);
			this.collapsibleGroupBox1.Controls.Add(this.buttonAdd);
			this.collapsibleGroupBox1.Controls.Add(this.listBoxColors);
			this.collapsibleGroupBox1.Location = new System.Drawing.Point(9, 211);
			this.collapsibleGroupBox1.Name = "collapsibleGroupBox1";
			this.collapsibleGroupBox1.Size = new System.Drawing.Size(200, 173);
			this.collapsibleGroupBox1.TabIndex = 25;
			this.collapsibleGroupBox1.TabStop = false;
			this.collapsibleGroupBox1.Text = "Colors";
			// 
			// buttonDefaultColors
			// 
			this.buttonDefaultColors.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonDefaultColors.Image = global::ARCed.Properties.Resources.Update;
			this.buttonDefaultColors.Location = new System.Drawing.Point(170, 139);
			this.buttonDefaultColors.Name = "buttonDefaultColors";
			this.buttonDefaultColors.Size = new System.Drawing.Size(24, 24);
			this.buttonDefaultColors.TabIndex = 5;
			this.toolTip.SetToolTip(this.buttonDefaultColors, "Reset default colors");
			this.buttonDefaultColors.UseVisualStyleBackColor = true;
			this.buttonDefaultColors.Click += new System.EventHandler(this.ButtonDefaultColorsClick);
			// 
			// buttonDown
			// 
			this.buttonDown.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonDown.Enabled = false;
			this.buttonDown.Image = global::ARCed.Properties.Resources.Down;
			this.buttonDown.Location = new System.Drawing.Point(170, 109);
			this.buttonDown.Name = "buttonDown";
			this.buttonDown.Size = new System.Drawing.Size(24, 24);
			this.buttonDown.TabIndex = 4;
			this.toolTip.SetToolTip(this.buttonDown, "Move selected color down");
			this.buttonDown.UseVisualStyleBackColor = true;
			this.buttonDown.Click += new System.EventHandler(this.ButtonDownClick);
			// 
			// buttonUp
			// 
			this.buttonUp.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonUp.Enabled = false;
			this.buttonUp.Image = global::ARCed.Properties.Resources.Up;
			this.buttonUp.Location = new System.Drawing.Point(170, 79);
			this.buttonUp.Name = "buttonUp";
			this.buttonUp.Size = new System.Drawing.Size(24, 24);
			this.buttonUp.TabIndex = 3;
			this.toolTip.SetToolTip(this.buttonUp, "Move selected color up");
			this.buttonUp.UseVisualStyleBackColor = true;
			this.buttonUp.Click += new System.EventHandler(this.ButtonUpClick);
			// 
			// buttonRemove
			// 
			this.buttonRemove.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonRemove.Enabled = false;
			this.buttonRemove.Image = global::ARCed.Properties.Resources.Delete;
			this.buttonRemove.Location = new System.Drawing.Point(170, 49);
			this.buttonRemove.Name = "buttonRemove";
			this.buttonRemove.Size = new System.Drawing.Size(24, 24);
			this.buttonRemove.TabIndex = 2;
			this.toolTip.SetToolTip(this.buttonRemove, "Remove selected color");
			this.buttonRemove.UseVisualStyleBackColor = true;
			this.buttonRemove.Click += new System.EventHandler(this.ButtonRemoveClick);
			// 
			// buttonAdd
			// 
			this.buttonAdd.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonAdd.Image = global::ARCed.Properties.Resources.Add;
			this.buttonAdd.Location = new System.Drawing.Point(170, 19);
			this.buttonAdd.Name = "buttonAdd";
			this.buttonAdd.Size = new System.Drawing.Size(24, 24);
			this.buttonAdd.TabIndex = 1;
			this.toolTip.SetToolTip(this.buttonAdd, "Add a new color");
			this.buttonAdd.UseVisualStyleBackColor = true;
			this.buttonAdd.Click += new System.EventHandler(this.ButtonAddClick);
			// 
			// listBoxColors
			// 
			this.listBoxColors.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.listBoxColors.FormattingEnabled = true;
			this.listBoxColors.IntegralHeight = false;
			this.listBoxColors.Location = new System.Drawing.Point(6, 19);
			this.listBoxColors.Name = "listBoxColors";
			this.listBoxColors.Size = new System.Drawing.Size(158, 144);
			this.listBoxColors.TabIndex = 0;
			this.toolTip.SetToolTip(this.listBoxColors, "Double-click to edit");
			this.listBoxColors.SelectedIndexChanged += new System.EventHandler(this.ListBoxColorsSelectedIndexChanged);
			this.listBoxColors.DoubleClick += new System.EventHandler(this.ListBoxColorsDoubleClick);
			// 
			// ChartSettingsForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.AutoScroll = true;
			this.ClientSize = new System.Drawing.Size(218, 418);
			this.Controls.Add(this.collapsibleGroupBox1);
			this.Controls.Add(this.splitContainer);
			this.DefaultFloatSize = new System.Drawing.Size(224, 442);
			this.DockAreas = ((ARCed.UI.DockAreas)(((ARCed.UI.DockAreas.Float | ARCed.UI.DockAreas.DockLeft)
						| ARCed.UI.DockAreas.DockRight)));
			this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
			this.MinimumSize = new System.Drawing.Size(224, 239);
			this.Name = "ChartSettingsForm";
			this.ShowHint = ARCed.UI.DockState.DockRight;
			this.ShowIcon = false;
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
			this.Text = "Chart Settings";
			((System.ComponentModel.ISupportInitialize)(this.numericDepth)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.numericPerspective)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.numericRotation)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.numericInclination)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.numericTension)).EndInit();
			this.splitContainer.Panel1.ResumeLayout(false);
			this.splitContainer.Panel1.PerformLayout();
			this.splitContainer.Panel2.ResumeLayout(false);
			this.splitContainer.Panel2.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainer)).EndInit();
			this.splitContainer.ResumeLayout(false);
			this.collapsibleGroupBox1.ResumeLayout(false);
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.CheckBox checkBox3D;
		private System.Windows.Forms.NumericUpDown numericDepth;
		private System.Windows.Forms.Label labelDepth;
		private System.Windows.Forms.NumericUpDown numericPerspective;
		private System.Windows.Forms.NumericUpDown numericRotation;
		private System.Windows.Forms.NumericUpDown numericInclination;
		private System.Windows.Forms.Label labelPerspective;
		private System.Windows.Forms.Label labelRotation;
		private System.Windows.Forms.Label labelInclination;
		private System.Windows.Forms.CheckBox checkBoxMarkerLines;
		private System.Windows.Forms.ComboBox comboBoxLighting;
		private System.Windows.Forms.Label labelLighting;
		private System.Windows.Forms.NumericUpDown numericTension;
		private System.Windows.Forms.Label labelTension;
		private System.Windows.Forms.ComboBox comboBoxType;
		private System.Windows.Forms.Label labelType;
		private System.Windows.Forms.SplitContainer splitContainer;
		private ARCed.Controls.CollapsibleGroupBox collapsibleGroupBox1;
		private System.Windows.Forms.Button buttonDown;
		private System.Windows.Forms.Button buttonUp;
		private System.Windows.Forms.Button buttonRemove;
		private System.Windows.Forms.Button buttonAdd;
		private System.Windows.Forms.ListBox listBoxColors;
		private System.Windows.Forms.ToolTip toolTip;
		private System.Windows.Forms.Button buttonDefaultColors;
	}
}