namespace ARCed.Database.Actors
{
	partial class ExperienceCurveForm
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
			this.groupBoxBasis = new System.Windows.Forms.GroupBox();
			this.numericBasis = new System.Windows.Forms.NumericUpDown();
			this.trackBarBasis = new System.Windows.Forms.TrackBar();
			this.groupBoxInflation = new System.Windows.Forms.GroupBox();
			this.numericInflation = new System.Windows.Forms.NumericUpDown();
			this.trackBarInflation = new System.Windows.Forms.TrackBar();
			this.groupBox1 = new System.Windows.Forms.GroupBox();
			this.radioButtonTotal = new System.Windows.Forms.RadioButton();
			this.radioButtonNext = new System.Windows.Forms.RadioButton();
			this.buttonCancel = new System.Windows.Forms.Button();
			this.buttonApply = new System.Windows.Forms.Button();
			this.listBoxExperience = new System.Windows.Forms.ListBox();
			this.groupBoxBasis.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.numericBasis)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.trackBarBasis)).BeginInit();
			this.groupBoxInflation.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.numericInflation)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.trackBarInflation)).BeginInit();
			this.groupBox1.SuspendLayout();
			this.SuspendLayout();
			// 
			// groupBoxBasis
			// 
			this.groupBoxBasis.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxBasis.Controls.Add(this.numericBasis);
			this.groupBoxBasis.Controls.Add(this.trackBarBasis);
			this.groupBoxBasis.Location = new System.Drawing.Point(12, 310);
			this.groupBoxBasis.Name = "groupBoxBasis";
			this.groupBoxBasis.Size = new System.Drawing.Size(252, 65);
			this.groupBoxBasis.TabIndex = 0;
			this.groupBoxBasis.TabStop = false;
			this.groupBoxBasis.Text = "Basis";
			// 
			// numericBasis
			// 
			this.numericBasis.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.numericBasis.Location = new System.Drawing.Point(190, 28);
			this.numericBasis.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
			this.numericBasis.Name = "numericBasis";
			this.numericBasis.Size = new System.Drawing.Size(56, 20);
			this.numericBasis.TabIndex = 1;
			this.numericBasis.Value = new decimal(new int[] {
            5,
            0,
            0,
            0});
			this.numericBasis.ValueChanged += new System.EventHandler(this.NumericBasisValueChanged);
			// 
			// trackBarBasis
			// 
			this.trackBarBasis.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.trackBarBasis.Location = new System.Drawing.Point(6, 19);
			this.trackBarBasis.Maximum = 100;
			this.trackBarBasis.Minimum = 1;
			this.trackBarBasis.Name = "trackBarBasis";
			this.trackBarBasis.Size = new System.Drawing.Size(178, 45);
			this.trackBarBasis.TabIndex = 0;
			this.trackBarBasis.TickFrequency = 10;
			this.trackBarBasis.Value = 1;
			// 
			// groupBoxInflation
			// 
			this.groupBoxInflation.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxInflation.Controls.Add(this.numericInflation);
			this.groupBoxInflation.Controls.Add(this.trackBarInflation);
			this.groupBoxInflation.Location = new System.Drawing.Point(12, 381);
			this.groupBoxInflation.Name = "groupBoxInflation";
			this.groupBoxInflation.Size = new System.Drawing.Size(252, 65);
			this.groupBoxInflation.TabIndex = 1;
			this.groupBoxInflation.TabStop = false;
			this.groupBoxInflation.Text = "Inflation";
			// 
			// numericInflation
			// 
			this.numericInflation.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.numericInflation.Location = new System.Drawing.Point(190, 28);
			this.numericInflation.Name = "numericInflation";
			this.numericInflation.Size = new System.Drawing.Size(56, 20);
			this.numericInflation.TabIndex = 1;
			this.numericInflation.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
			this.numericInflation.ValueChanged += new System.EventHandler(this.NumericInflationValueChanged);
			// 
			// trackBarInflation
			// 
			this.trackBarInflation.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.trackBarInflation.Location = new System.Drawing.Point(6, 19);
			this.trackBarInflation.Maximum = 100;
			this.trackBarInflation.Minimum = 1;
			this.trackBarInflation.Name = "trackBarInflation";
			this.trackBarInflation.Size = new System.Drawing.Size(178, 45);
			this.trackBarInflation.TabIndex = 0;
			this.trackBarInflation.TickFrequency = 10;
			this.trackBarInflation.Value = 1;
			// 
			// groupBox1
			// 
			this.groupBox1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.groupBox1.Controls.Add(this.radioButtonTotal);
			this.groupBox1.Controls.Add(this.radioButtonNext);
			this.groupBox1.Location = new System.Drawing.Point(270, 310);
			this.groupBox1.Name = "groupBox1";
			this.groupBox1.Size = new System.Drawing.Size(129, 65);
			this.groupBox1.TabIndex = 2;
			this.groupBox1.TabStop = false;
			this.groupBox1.Text = "Display Mode";
			// 
			// radioButtonTotal
			// 
			this.radioButtonTotal.AutoSize = true;
			this.radioButtonTotal.Location = new System.Drawing.Point(6, 42);
			this.radioButtonTotal.Name = "radioButtonTotal";
			this.radioButtonTotal.Size = new System.Drawing.Size(49, 17);
			this.radioButtonTotal.TabIndex = 1;
			this.radioButtonTotal.Text = "Total";
			this.radioButtonTotal.UseVisualStyleBackColor = true;
			// 
			// radioButtonNext
			// 
			this.radioButtonNext.AutoSize = true;
			this.radioButtonNext.Checked = true;
			this.radioButtonNext.Location = new System.Drawing.Point(6, 19);
			this.radioButtonNext.Name = "radioButtonNext";
			this.radioButtonNext.Size = new System.Drawing.Size(92, 17);
			this.radioButtonNext.TabIndex = 0;
			this.radioButtonNext.TabStop = true;
			this.radioButtonNext.Text = "To Next Level";
			this.radioButtonNext.UseVisualStyleBackColor = true;
			this.radioButtonNext.CheckedChanged += new System.EventHandler(this.RadioButtonCheckedChanged);
			// 
			// buttonCancel
			// 
			this.buttonCancel.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
			this.buttonCancel.Location = new System.Drawing.Point(324, 421);
			this.buttonCancel.Name = "buttonCancel";
			this.buttonCancel.Size = new System.Drawing.Size(75, 23);
			this.buttonCancel.TabIndex = 3;
			this.buttonCancel.Text = "Reset";
			this.buttonCancel.UseVisualStyleBackColor = true;
			this.buttonCancel.Click += new System.EventHandler(this.ButtonCancelClick);
			// 
			// buttonApply
			// 
			this.buttonApply.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonApply.Location = new System.Drawing.Point(325, 392);
			this.buttonApply.Name = "buttonApply";
			this.buttonApply.Size = new System.Drawing.Size(75, 23);
			this.buttonApply.TabIndex = 4;
			this.buttonApply.Text = "Apply";
			this.buttonApply.UseVisualStyleBackColor = true;
			this.buttonApply.Click += new System.EventHandler(this.ButtonApplyClick);
			// 
			// listBoxExperience
			// 
			this.listBoxExperience.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.listBoxExperience.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed;
			this.listBoxExperience.Location = new System.Drawing.Point(12, 12);
			this.listBoxExperience.MultiColumn = true;
			this.listBoxExperience.Name = "listBoxExperience";
			this.listBoxExperience.SelectionMode = System.Windows.Forms.SelectionMode.None;
			this.listBoxExperience.Size = new System.Drawing.Size(387, 277);
			this.listBoxExperience.TabIndex = 5;
			this.listBoxExperience.DrawItem += new System.Windows.Forms.DrawItemEventHandler(this.ListBoxExperienceDrawItem);
			// 
			// ExperienceCurveForm
			// 
			this.AcceptButton = this.buttonApply;
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.CancelButton = this.buttonCancel;
			this.ClientSize = new System.Drawing.Size(412, 456);
			this.Controls.Add(this.listBoxExperience);
			this.Controls.Add(this.buttonApply);
			this.Controls.Add(this.buttonCancel);
			this.Controls.Add(this.groupBox1);
			this.Controls.Add(this.groupBoxInflation);
			this.Controls.Add(this.groupBoxBasis);
			this.DefaultFloatSize = new System.Drawing.Size(428, 490);
			this.DockAreas = ((ARCed.UI.DockAreas)((((ARCed.UI.DockAreas.Float | ARCed.UI.DockAreas.DockLeft)
						| ARCed.UI.DockAreas.DockRight)
						| ARCed.UI.DockAreas.Document)));
			this.DoubleBuffered = true;
			this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.SizableToolWindow;
			this.MaximizeBox = false;
			this.MinimizeBox = false;
			this.MinimumSize = new System.Drawing.Size(90, 56);
			this.Name = "ExperienceCurveForm";
			this.ShowHint = ARCed.UI.DockState.Float;
			this.ShowIcon = false;
			this.ShowInTaskbar = false;
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
			this.Text = "Experience Curve";
			this.groupBoxBasis.ResumeLayout(false);
			this.groupBoxBasis.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.numericBasis)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.trackBarBasis)).EndInit();
			this.groupBoxInflation.ResumeLayout(false);
			this.groupBoxInflation.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.numericInflation)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.trackBarInflation)).EndInit();
			this.groupBox1.ResumeLayout(false);
			this.groupBox1.PerformLayout();
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.GroupBox groupBoxBasis;
		private System.Windows.Forms.NumericUpDown numericBasis;
		private System.Windows.Forms.TrackBar trackBarBasis;
		private System.Windows.Forms.GroupBox groupBoxInflation;
		private System.Windows.Forms.NumericUpDown numericInflation;
		private System.Windows.Forms.TrackBar trackBarInflation;
		private System.Windows.Forms.GroupBox groupBox1;
		private System.Windows.Forms.RadioButton radioButtonTotal;
		private System.Windows.Forms.RadioButton radioButtonNext;
		private System.Windows.Forms.Button buttonCancel;
		private System.Windows.Forms.Button buttonApply;
		private System.Windows.Forms.ListBox listBoxExperience;
	}
}