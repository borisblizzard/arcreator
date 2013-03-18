namespace ARCed.Database.Actors
{
	partial class ActorParametersForm
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
            this.buttonGenerate = new System.Windows.Forms.Button();
            this.tabControlParameters = new System.Windows.Forms.TabControl();
            this.labelLevel = new System.Windows.Forms.Label();
            this.labelValue = new System.Windows.Forms.Label();
            this.numericLevel = new System.Windows.Forms.NumericUpDown();
            this.numericValue = new System.Windows.Forms.NumericUpDown();
            this.groupBoxQuickSettings = new System.Windows.Forms.GroupBox();
            this.buttonQuickE = new System.Windows.Forms.Button();
            this.buttonQuickC = new System.Windows.Forms.Button();
            this.buttonQuickB = new System.Windows.Forms.Button();
            this.buttonQuickD = new System.Windows.Forms.Button();
            this.buttonQuickA = new System.Windows.Forms.Button();
            this.labelCoordX = new System.Windows.Forms.Label();
            this.labelCoordY = new System.Windows.Forms.Label();
            this.buttonSettings = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.numericLevel)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericValue)).BeginInit();
            this.groupBoxQuickSettings.SuspendLayout();
            this.SuspendLayout();
            // 
            // buttonGenerate
            // 
            this.buttonGenerate.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.buttonGenerate.Location = new System.Drawing.Point(452, 257);
            this.buttonGenerate.Name = "buttonGenerate";
            this.buttonGenerate.Size = new System.Drawing.Size(93, 23);
            this.buttonGenerate.TabIndex = 0;
            this.buttonGenerate.Text = "Generate...";
            this.buttonGenerate.UseVisualStyleBackColor = true;
            this.buttonGenerate.Click += new System.EventHandler(this.ButtonGenerateClick);
            // 
            // tabControlParameters
            // 
            this.tabControlParameters.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.tabControlParameters.Location = new System.Drawing.Point(12, 12);
            this.tabControlParameters.Name = "tabControlParameters";
            this.tabControlParameters.SelectedIndex = 0;
            this.tabControlParameters.Size = new System.Drawing.Size(431, 268);
            this.tabControlParameters.TabIndex = 2;
            this.tabControlParameters.SelectedIndexChanged += new System.EventHandler(this.TabControlParametersSelectedIndexChanged);
            // 
            // labelLevel
            // 
            this.labelLevel.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.labelLevel.AutoSize = true;
            this.labelLevel.Location = new System.Drawing.Point(449, 96);
            this.labelLevel.Name = "labelLevel";
            this.labelLevel.Size = new System.Drawing.Size(36, 13);
            this.labelLevel.TabIndex = 7;
            this.labelLevel.Text = "Level:";
            // 
            // labelValue
            // 
            this.labelValue.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.labelValue.AutoSize = true;
            this.labelValue.Location = new System.Drawing.Point(449, 141);
            this.labelValue.Name = "labelValue";
            this.labelValue.Size = new System.Drawing.Size(34, 13);
            this.labelValue.TabIndex = 8;
            this.labelValue.Text = "Value";
            // 
            // numericLevel
            // 
            this.numericLevel.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.numericLevel.Location = new System.Drawing.Point(452, 112);
            this.numericLevel.Name = "numericLevel";
            this.numericLevel.Size = new System.Drawing.Size(93, 20);
            this.numericLevel.TabIndex = 9;
            this.numericLevel.ValueChanged += new System.EventHandler(this.NumericLevelValueChanged);
            // 
            // numericValue
            // 
            this.numericValue.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.numericValue.Location = new System.Drawing.Point(452, 157);
            this.numericValue.Name = "numericValue";
            this.numericValue.Size = new System.Drawing.Size(93, 20);
            this.numericValue.TabIndex = 10;
            this.numericValue.ValueChanged += new System.EventHandler(this.NumericValueValueChanged);
            // 
            // groupBoxQuickSettings
            // 
            this.groupBoxQuickSettings.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.groupBoxQuickSettings.Controls.Add(this.buttonQuickE);
            this.groupBoxQuickSettings.Controls.Add(this.buttonQuickC);
            this.groupBoxQuickSettings.Controls.Add(this.buttonQuickB);
            this.groupBoxQuickSettings.Controls.Add(this.buttonQuickD);
            this.groupBoxQuickSettings.Controls.Add(this.buttonQuickA);
            this.groupBoxQuickSettings.Location = new System.Drawing.Point(452, 12);
            this.groupBoxQuickSettings.Name = "groupBoxQuickSettings";
            this.groupBoxQuickSettings.Size = new System.Drawing.Size(93, 81);
            this.groupBoxQuickSettings.TabIndex = 11;
            this.groupBoxQuickSettings.TabStop = false;
            this.groupBoxQuickSettings.Text = "Quick Curve";
            // 
            // buttonQuickE
            // 
            this.buttonQuickE.Location = new System.Drawing.Point(51, 48);
            this.buttonQuickE.Name = "buttonQuickE";
            this.buttonQuickE.Size = new System.Drawing.Size(23, 23);
            this.buttonQuickE.TabIndex = 4;
            this.buttonQuickE.Tag = "10";
            this.buttonQuickE.Text = "E";
            this.buttonQuickE.UseVisualStyleBackColor = true;
            this.buttonQuickE.Click += new System.EventHandler(this.ButtonQuickCurveClick);
            // 
            // buttonQuickC
            // 
            this.buttonQuickC.Location = new System.Drawing.Point(64, 19);
            this.buttonQuickC.Name = "buttonQuickC";
            this.buttonQuickC.Size = new System.Drawing.Size(23, 23);
            this.buttonQuickC.TabIndex = 3;
            this.buttonQuickC.Tag = "0";
            this.buttonQuickC.Text = "C";
            this.buttonQuickC.UseVisualStyleBackColor = true;
            this.buttonQuickC.Click += new System.EventHandler(this.ButtonQuickCurveClick);
            // 
            // buttonQuickB
            // 
            this.buttonQuickB.Location = new System.Drawing.Point(35, 19);
            this.buttonQuickB.Name = "buttonQuickB";
            this.buttonQuickB.Size = new System.Drawing.Size(23, 23);
            this.buttonQuickB.TabIndex = 2;
            this.buttonQuickB.Tag = "-5";
            this.buttonQuickB.Text = "B";
            this.buttonQuickB.UseVisualStyleBackColor = true;
            this.buttonQuickB.Click += new System.EventHandler(this.ButtonQuickCurveClick);
            // 
            // buttonQuickD
            // 
            this.buttonQuickD.Location = new System.Drawing.Point(22, 48);
            this.buttonQuickD.Name = "buttonQuickD";
            this.buttonQuickD.Size = new System.Drawing.Size(23, 23);
            this.buttonQuickD.TabIndex = 1;
            this.buttonQuickD.Tag = "5";
            this.buttonQuickD.Text = "D";
            this.buttonQuickD.UseVisualStyleBackColor = true;
            this.buttonQuickD.Click += new System.EventHandler(this.ButtonQuickCurveClick);
            // 
            // buttonQuickA
            // 
            this.buttonQuickA.Location = new System.Drawing.Point(6, 19);
            this.buttonQuickA.Name = "buttonQuickA";
            this.buttonQuickA.Size = new System.Drawing.Size(23, 23);
            this.buttonQuickA.TabIndex = 0;
            this.buttonQuickA.Tag = "-10";
            this.buttonQuickA.Text = "A";
            this.buttonQuickA.UseVisualStyleBackColor = true;
            this.buttonQuickA.Click += new System.EventHandler(this.ButtonQuickCurveClick);
            // 
            // labelCoordX
            // 
            this.labelCoordX.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.labelCoordX.AutoSize = true;
            this.labelCoordX.Location = new System.Drawing.Point(455, 190);
            this.labelCoordX.Name = "labelCoordX";
            this.labelCoordX.Size = new System.Drawing.Size(17, 13);
            this.labelCoordX.TabIndex = 12;
            this.labelCoordX.Text = "X:";
            // 
            // labelCoordY
            // 
            this.labelCoordY.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.labelCoordY.AutoSize = true;
            this.labelCoordY.Location = new System.Drawing.Point(455, 203);
            this.labelCoordY.Name = "labelCoordY";
            this.labelCoordY.Size = new System.Drawing.Size(17, 13);
            this.labelCoordY.TabIndex = 13;
            this.labelCoordY.Text = "Y:";
            // 
            // buttonSettings
            // 
            this.buttonSettings.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.buttonSettings.Location = new System.Drawing.Point(451, 228);
            this.buttonSettings.Name = "buttonSettings";
            this.buttonSettings.Size = new System.Drawing.Size(94, 23);
            this.buttonSettings.TabIndex = 14;
            this.buttonSettings.Text = "Settings...";
            this.buttonSettings.UseVisualStyleBackColor = true;
            this.buttonSettings.Click += new System.EventHandler(this.ButtonSettingsClick);
            // 
            // ActorParametersForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(557, 292);
            this.Controls.Add(this.buttonSettings);
            this.Controls.Add(this.labelCoordY);
            this.Controls.Add(this.labelCoordX);
            this.Controls.Add(this.groupBoxQuickSettings);
            this.Controls.Add(this.numericValue);
            this.Controls.Add(this.numericLevel);
            this.Controls.Add(this.labelValue);
            this.Controls.Add(this.labelLevel);
            this.Controls.Add(this.tabControlParameters);
            this.Controls.Add(this.buttonGenerate);
            this.DefaultFloatSize = new System.Drawing.Size(573, 330);
            this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.MinimumSize = new System.Drawing.Size(300, 330);
            this.Name = "ActorParametersForm";
            this.Text = "Actor Parameters";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.ActorParametersFormFormClosing);
            this.Load += new System.EventHandler(this.ActorParametersFormLoad);
            ((System.ComponentModel.ISupportInitialize)(this.numericLevel)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericValue)).EndInit();
            this.groupBoxQuickSettings.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Button buttonGenerate;
		private System.Windows.Forms.TabControl tabControlParameters;
		private System.Windows.Forms.Label labelLevel;
		private System.Windows.Forms.Label labelValue;
		private System.Windows.Forms.NumericUpDown numericLevel;
		private System.Windows.Forms.NumericUpDown numericValue;
		private System.Windows.Forms.GroupBox groupBoxQuickSettings;
		private System.Windows.Forms.Button buttonQuickE;
		private System.Windows.Forms.Button buttonQuickC;
		private System.Windows.Forms.Button buttonQuickB;
		private System.Windows.Forms.Button buttonQuickD;
		private System.Windows.Forms.Button buttonQuickA;
		private System.Windows.Forms.Label labelCoordX;
		private System.Windows.Forms.Label labelCoordY;
		private System.Windows.Forms.Button buttonSettings;
	}
}