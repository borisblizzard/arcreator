namespace ARCed.Database.Classes
{
	partial class EditSkillDialog
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
			this.buttonOK = new System.Windows.Forms.Button();
			this.buttonCancel = new System.Windows.Forms.Button();
			this.labelLevel = new System.Windows.Forms.Label();
			this.labelSkill = new System.Windows.Forms.Label();
			this.numericLevel = new System.Windows.Forms.NumericUpDown();
			this.comboBoxSkill = new System.Windows.Forms.ComboBox();
			this.toolTip = new System.Windows.Forms.ToolTip(this.components);
			((System.ComponentModel.ISupportInitialize)(this.numericLevel)).BeginInit();
			this.SuspendLayout();
			// 
			// buttonOK
			// 
			this.buttonOK.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonOK.Location = new System.Drawing.Point(115, 59);
			this.buttonOK.Name = "buttonOK";
			this.buttonOK.Size = new System.Drawing.Size(75, 23);
			this.buttonOK.TabIndex = 0;
			this.buttonOK.Text = "OK";
			this.toolTip.SetToolTip(this.buttonOK, "Confirm ");
			this.buttonOK.UseVisualStyleBackColor = true;
			this.buttonOK.Click += new System.EventHandler(this.buttonOK_Click);
			// 
			// buttonCancel
			// 
			this.buttonCancel.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
			this.buttonCancel.Location = new System.Drawing.Point(196, 59);
			this.buttonCancel.Name = "buttonCancel";
			this.buttonCancel.Size = new System.Drawing.Size(75, 23);
			this.buttonCancel.TabIndex = 1;
			this.buttonCancel.Text = "Cancel";
			this.toolTip.SetToolTip(this.buttonCancel, "Cancel and return");
			this.buttonCancel.UseVisualStyleBackColor = true;
			// 
			// labelLevel
			// 
			this.labelLevel.AutoSize = true;
			this.labelLevel.Location = new System.Drawing.Point(12, 12);
			this.labelLevel.Name = "labelLevel";
			this.labelLevel.Size = new System.Drawing.Size(36, 13);
			this.labelLevel.TabIndex = 2;
			this.labelLevel.Text = "Level:";
			// 
			// labelSkill
			// 
			this.labelSkill.AutoSize = true;
			this.labelSkill.Location = new System.Drawing.Point(72, 12);
			this.labelSkill.Name = "labelSkill";
			this.labelSkill.Size = new System.Drawing.Size(29, 13);
			this.labelSkill.TabIndex = 3;
			this.labelSkill.Text = "Skill:";
			// 
			// numericLevel
			// 
			this.numericLevel.Location = new System.Drawing.Point(15, 28);
			this.numericLevel.Maximum = new decimal(new int[] {
            999,
            0,
            0,
            0});
			this.numericLevel.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
			this.numericLevel.Name = "numericLevel";
			this.numericLevel.Size = new System.Drawing.Size(54, 20);
			this.numericLevel.TabIndex = 4;
			this.toolTip.SetToolTip(this.numericLevel, "Level when skill is learned");
			this.numericLevel.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
			// 
			// comboBoxSkill
			// 
			this.comboBoxSkill.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxSkill.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxSkill.FormattingEnabled = true;
			this.comboBoxSkill.Location = new System.Drawing.Point(75, 28);
			this.comboBoxSkill.Name = "comboBoxSkill";
			this.comboBoxSkill.Size = new System.Drawing.Size(196, 21);
			this.comboBoxSkill.TabIndex = 5;
			this.toolTip.SetToolTip(this.comboBoxSkill, "Skill to learn");
			// 
			// EditSkillDialog
			// 
			this.AcceptButton = this.buttonOK;
			this.AccessibleRole = System.Windows.Forms.AccessibleRole.Dialog;
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.CancelButton = this.buttonCancel;
			this.ClientSize = new System.Drawing.Size(283, 94);
			this.Controls.Add(this.comboBoxSkill);
			this.Controls.Add(this.numericLevel);
			this.Controls.Add(this.labelSkill);
			this.Controls.Add(this.labelLevel);
			this.Controls.Add(this.buttonCancel);
			this.Controls.Add(this.buttonOK);
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.SizableToolWindow;
			this.MaximizeBox = false;
			this.MinimizeBox = false;
			this.Name = "EditSkillDialog";
			this.ShowIcon = false;
			this.ShowInTaskbar = false;
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
			this.Text = "Skill";
			((System.ComponentModel.ISupportInitialize)(this.numericLevel)).EndInit();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Button buttonOK;
		private System.Windows.Forms.ToolTip toolTip;
		private System.Windows.Forms.Button buttonCancel;
		private System.Windows.Forms.Label labelLevel;
		private System.Windows.Forms.Label labelSkill;
		private System.Windows.Forms.NumericUpDown numericLevel;
		private System.Windows.Forms.ComboBox comboBoxSkill;
	}
}