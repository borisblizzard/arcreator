namespace ARCed.Database.Enemies
{
	partial class EditActionDialog
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
			this.groupBox1 = new System.Windows.Forms.GroupBox();
			this.labelOn = new System.Windows.Forms.Label();
			this.numericUpDownTurnX = new System.Windows.Forms.NumericUpDown();
			this.checkBoxSwitch = new System.Windows.Forms.CheckBox();
			this.checkBoxLevel = new System.Windows.Forms.CheckBox();
			this.checkBoxHP = new System.Windows.Forms.CheckBox();
			this.comboBoxSwitch = new System.Windows.Forms.ComboBox();
			this.labelAbove = new System.Windows.Forms.Label();
			this.numericUpDownLevel = new System.Windows.Forms.NumericUpDown();
			this.labelBelow = new System.Windows.Forms.Label();
			this.numericUpDownHP = new System.Windows.Forms.NumericUpDown();
			this.labelTurnPlus = new System.Windows.Forms.Label();
			this.numericUpDownTurn = new System.Windows.Forms.NumericUpDown();
			this.checkBoxTurn = new System.Windows.Forms.CheckBox();
			this.groupBoxAction = new System.Windows.Forms.GroupBox();
			this.radioButtonSkill = new System.Windows.Forms.RadioButton();
			this.radioButtonBasic = new System.Windows.Forms.RadioButton();
			this.comboBoxSkill = new System.Windows.Forms.ComboBox();
			this.comboBoxBasic = new System.Windows.Forms.ComboBox();
			this.buttonCancel = new System.Windows.Forms.Button();
			this.buttonOK = new System.Windows.Forms.Button();
			this.groupBoxRating = new System.Windows.Forms.GroupBox();
			this.numericUpDownRating = new System.Windows.Forms.NumericUpDown();
			this.trackBarRating = new System.Windows.Forms.TrackBar();
			this.groupBox1.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownTurnX)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownLevel)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownHP)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownTurn)).BeginInit();
			this.groupBoxAction.SuspendLayout();
			this.groupBoxRating.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownRating)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.trackBarRating)).BeginInit();
			this.SuspendLayout();
			// 
			// groupBox1
			// 
			this.groupBox1.Controls.Add(this.labelOn);
			this.groupBox1.Controls.Add(this.numericUpDownTurnX);
			this.groupBox1.Controls.Add(this.checkBoxSwitch);
			this.groupBox1.Controls.Add(this.checkBoxLevel);
			this.groupBox1.Controls.Add(this.checkBoxHP);
			this.groupBox1.Controls.Add(this.comboBoxSwitch);
			this.groupBox1.Controls.Add(this.labelAbove);
			this.groupBox1.Controls.Add(this.numericUpDownLevel);
			this.groupBox1.Controls.Add(this.labelBelow);
			this.groupBox1.Controls.Add(this.numericUpDownHP);
			this.groupBox1.Controls.Add(this.labelTurnPlus);
			this.groupBox1.Controls.Add(this.numericUpDownTurn);
			this.groupBox1.Controls.Add(this.checkBoxTurn);
			this.groupBox1.Location = new System.Drawing.Point(12, 12);
			this.groupBox1.Name = "groupBox1";
			this.groupBox1.Size = new System.Drawing.Size(246, 127);
			this.groupBox1.TabIndex = 0;
			this.groupBox1.TabStop = false;
			this.groupBox1.Text = "Conditions";
			// 
			// labelOn
			// 
			this.labelOn.Location = new System.Drawing.Point(200, 95);
			this.labelOn.Name = "labelOn";
			this.labelOn.Size = new System.Drawing.Size(36, 20);
			this.labelOn.TabIndex = 12;
			this.labelOn.Text = "is ON";
			this.labelOn.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
			// 
			// numericUpDownTurnX
			// 
			this.numericUpDownTurnX.Enabled = false;
			this.numericUpDownTurnX.Location = new System.Drawing.Point(166, 20);
			this.numericUpDownTurnX.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
			this.numericUpDownTurnX.Name = "numericUpDownTurnX";
			this.numericUpDownTurnX.Size = new System.Drawing.Size(70, 20);
			this.numericUpDownTurnX.TabIndex = 2;
			// 
			// checkBoxSwitch
			// 
			this.checkBoxSwitch.AutoSize = true;
			this.checkBoxSwitch.Location = new System.Drawing.Point(6, 98);
			this.checkBoxSwitch.Name = "checkBoxSwitch";
			this.checkBoxSwitch.Size = new System.Drawing.Size(58, 17);
			this.checkBoxSwitch.TabIndex = 11;
			this.checkBoxSwitch.Text = "Switch";
			this.checkBoxSwitch.UseVisualStyleBackColor = true;
			this.checkBoxSwitch.CheckedChanged += new System.EventHandler(this.checkBoxSwitch_CheckedChanged);
			// 
			// checkBoxLevel
			// 
			this.checkBoxLevel.AutoSize = true;
			this.checkBoxLevel.Location = new System.Drawing.Point(6, 73);
			this.checkBoxLevel.Name = "checkBoxLevel";
			this.checkBoxLevel.Size = new System.Drawing.Size(52, 17);
			this.checkBoxLevel.TabIndex = 10;
			this.checkBoxLevel.Text = "Level";
			this.checkBoxLevel.UseVisualStyleBackColor = true;
			this.checkBoxLevel.CheckedChanged += new System.EventHandler(this.checkBoxLevel_CheckedChanged);
			// 
			// checkBoxHP
			// 
			this.checkBoxHP.AutoSize = true;
			this.checkBoxHP.Location = new System.Drawing.Point(6, 47);
			this.checkBoxHP.Name = "checkBoxHP";
			this.checkBoxHP.Size = new System.Drawing.Size(41, 17);
			this.checkBoxHP.TabIndex = 9;
			this.checkBoxHP.Text = "HP";
			this.checkBoxHP.UseVisualStyleBackColor = true;
			this.checkBoxHP.CheckedChanged += new System.EventHandler(this.checkBoxHP_CheckedChanged);
			// 
			// comboBoxSwitch
			// 
			this.comboBoxSwitch.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxSwitch.DropDownWidth = 192;
			this.comboBoxSwitch.Enabled = false;
			this.comboBoxSwitch.FormattingEnabled = true;
			this.comboBoxSwitch.Location = new System.Drawing.Point(73, 96);
			this.comboBoxSwitch.Name = "comboBoxSwitch";
			this.comboBoxSwitch.Size = new System.Drawing.Size(121, 21);
			this.comboBoxSwitch.TabIndex = 8;
			// 
			// labelAbove
			// 
			this.labelAbove.Location = new System.Drawing.Point(178, 70);
			this.labelAbove.Name = "labelAbove";
			this.labelAbove.Size = new System.Drawing.Size(58, 20);
			this.labelAbove.TabIndex = 7;
			this.labelAbove.Text = "or above";
			this.labelAbove.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
			// 
			// numericUpDownLevel
			// 
			this.numericUpDownLevel.Enabled = false;
			this.numericUpDownLevel.Location = new System.Drawing.Point(73, 70);
			this.numericUpDownLevel.Maximum = new decimal(new int[] {
            999,
            0,
            0,
            0});
			this.numericUpDownLevel.Minimum = new decimal(new int[] {
            2,
            0,
            0,
            0});
			this.numericUpDownLevel.Name = "numericUpDownLevel";
			this.numericUpDownLevel.Size = new System.Drawing.Size(104, 20);
			this.numericUpDownLevel.TabIndex = 6;
			this.numericUpDownLevel.Value = new decimal(new int[] {
            2,
            0,
            0,
            0});
			// 
			// labelBelow
			// 
			this.labelBelow.Location = new System.Drawing.Point(178, 44);
			this.labelBelow.Name = "labelBelow";
			this.labelBelow.Size = new System.Drawing.Size(58, 20);
			this.labelBelow.TabIndex = 5;
			this.labelBelow.Text = "% or below";
			this.labelBelow.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
			// 
			// numericUpDownHP
			// 
			this.numericUpDownHP.Enabled = false;
			this.numericUpDownHP.Location = new System.Drawing.Point(73, 47);
			this.numericUpDownHP.Maximum = new decimal(new int[] {
            99,
            0,
            0,
            0});
			this.numericUpDownHP.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
			this.numericUpDownHP.Name = "numericUpDownHP";
			this.numericUpDownHP.Size = new System.Drawing.Size(104, 20);
			this.numericUpDownHP.TabIndex = 4;
			this.numericUpDownHP.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
			// 
			// labelTurnPlus
			// 
			this.labelTurnPlus.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.labelTurnPlus.Location = new System.Drawing.Point(147, 20);
			this.labelTurnPlus.Margin = new System.Windows.Forms.Padding(1);
			this.labelTurnPlus.Name = "labelTurnPlus";
			this.labelTurnPlus.Size = new System.Drawing.Size(16, 20);
			this.labelTurnPlus.TabIndex = 3;
			this.labelTurnPlus.Text = "+";
			this.labelTurnPlus.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// numericUpDownTurn
			// 
			this.numericUpDownTurn.Enabled = false;
			this.numericUpDownTurn.Location = new System.Drawing.Point(73, 20);
			this.numericUpDownTurn.Maximum = new decimal(new int[] {
            99999,
            0,
            0,
            0});
			this.numericUpDownTurn.Name = "numericUpDownTurn";
			this.numericUpDownTurn.Size = new System.Drawing.Size(70, 20);
			this.numericUpDownTurn.TabIndex = 1;
			// 
			// checkBoxTurn
			// 
			this.checkBoxTurn.AutoSize = true;
			this.checkBoxTurn.Location = new System.Drawing.Point(6, 19);
			this.checkBoxTurn.Name = "checkBoxTurn";
			this.checkBoxTurn.Size = new System.Drawing.Size(48, 17);
			this.checkBoxTurn.TabIndex = 0;
			this.checkBoxTurn.Text = "Turn";
			this.checkBoxTurn.UseVisualStyleBackColor = true;
			this.checkBoxTurn.CheckedChanged += new System.EventHandler(this.checkBoxTurn_CheckedChanged);
			// 
			// groupBoxAction
			// 
			this.groupBoxAction.Controls.Add(this.radioButtonSkill);
			this.groupBoxAction.Controls.Add(this.radioButtonBasic);
			this.groupBoxAction.Controls.Add(this.comboBoxSkill);
			this.groupBoxAction.Controls.Add(this.comboBoxBasic);
			this.groupBoxAction.Location = new System.Drawing.Point(12, 145);
			this.groupBoxAction.Name = "groupBoxAction";
			this.groupBoxAction.Size = new System.Drawing.Size(246, 79);
			this.groupBoxAction.TabIndex = 1;
			this.groupBoxAction.TabStop = false;
			this.groupBoxAction.Text = "Action";
			// 
			// radioButtonSkill
			// 
			this.radioButtonSkill.AutoSize = true;
			this.radioButtonSkill.Location = new System.Drawing.Point(6, 47);
			this.radioButtonSkill.Name = "radioButtonSkill";
			this.radioButtonSkill.Size = new System.Drawing.Size(44, 17);
			this.radioButtonSkill.TabIndex = 3;
			this.radioButtonSkill.TabStop = true;
			this.radioButtonSkill.Text = "Skill";
			this.radioButtonSkill.UseVisualStyleBackColor = true;
			this.radioButtonSkill.CheckedChanged += new System.EventHandler(this.radioButton_CheckedChanged);
			// 
			// radioButtonBasic
			// 
			this.radioButtonBasic.AutoSize = true;
			this.radioButtonBasic.Location = new System.Drawing.Point(6, 20);
			this.radioButtonBasic.Name = "radioButtonBasic";
			this.radioButtonBasic.Size = new System.Drawing.Size(51, 17);
			this.radioButtonBasic.TabIndex = 2;
			this.radioButtonBasic.TabStop = true;
			this.radioButtonBasic.Text = "Basic";
			this.radioButtonBasic.UseVisualStyleBackColor = true;
			this.radioButtonBasic.CheckedChanged += new System.EventHandler(this.radioButton_CheckedChanged);
			// 
			// comboBoxSkill
			// 
			this.comboBoxSkill.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxSkill.FormattingEnabled = true;
			this.comboBoxSkill.Location = new System.Drawing.Point(73, 46);
			this.comboBoxSkill.Name = "comboBoxSkill";
			this.comboBoxSkill.Size = new System.Drawing.Size(163, 21);
			this.comboBoxSkill.TabIndex = 1;
			// 
			// comboBoxBasic
			// 
			this.comboBoxBasic.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxBasic.FormattingEnabled = true;
			this.comboBoxBasic.Items.AddRange(new object[] {
            "Attack",
            "Defend",
            "Escape",
            "Do Nothing"});
			this.comboBoxBasic.Location = new System.Drawing.Point(73, 19);
			this.comboBoxBasic.Name = "comboBoxBasic";
			this.comboBoxBasic.Size = new System.Drawing.Size(163, 21);
			this.comboBoxBasic.TabIndex = 0;
			// 
			// buttonCancel
			// 
			this.buttonCancel.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
			this.buttonCancel.Location = new System.Drawing.Point(181, 304);
			this.buttonCancel.Name = "buttonCancel";
			this.buttonCancel.Size = new System.Drawing.Size(75, 23);
			this.buttonCancel.TabIndex = 2;
			this.buttonCancel.Text = "Cancel";
			this.buttonCancel.UseVisualStyleBackColor = true;
			// 
			// buttonOK
			// 
			this.buttonOK.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonOK.Location = new System.Drawing.Point(100, 304);
			this.buttonOK.Name = "buttonOK";
			this.buttonOK.Size = new System.Drawing.Size(75, 23);
			this.buttonOK.TabIndex = 3;
			this.buttonOK.Text = "OK";
			this.buttonOK.UseVisualStyleBackColor = true;
			this.buttonOK.Click += new System.EventHandler(this.buttonOK_Click);
			// 
			// groupBoxRating
			// 
			this.groupBoxRating.Controls.Add(this.numericUpDownRating);
			this.groupBoxRating.Controls.Add(this.trackBarRating);
			this.groupBoxRating.Location = new System.Drawing.Point(12, 230);
			this.groupBoxRating.Name = "groupBoxRating";
			this.groupBoxRating.Size = new System.Drawing.Size(246, 53);
			this.groupBoxRating.TabIndex = 4;
			this.groupBoxRating.TabStop = false;
			this.groupBoxRating.Text = "Rating";
			// 
			// numericUpDownRating
			// 
			this.numericUpDownRating.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.numericUpDownRating.Location = new System.Drawing.Point(200, 19);
			this.numericUpDownRating.Maximum = new decimal(new int[] {
            10,
            0,
            0,
            0});
			this.numericUpDownRating.Name = "numericUpDownRating";
			this.numericUpDownRating.Size = new System.Drawing.Size(36, 20);
			this.numericUpDownRating.TabIndex = 1;
			// 
			// trackBarRating
			// 
			this.trackBarRating.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.trackBarRating.AutoSize = false;
			this.trackBarRating.Location = new System.Drawing.Point(6, 19);
			this.trackBarRating.Name = "trackBarRating";
			this.trackBarRating.Size = new System.Drawing.Size(188, 20);
			this.trackBarRating.TabIndex = 0;
			// 
			// EditActionDialog
			// 
			this.AcceptButton = this.buttonOK;
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.CancelButton = this.buttonCancel;
			this.ClientSize = new System.Drawing.Size(268, 336);
			this.Controls.Add(this.groupBoxRating);
			this.Controls.Add(this.buttonOK);
			this.Controls.Add(this.buttonCancel);
			this.Controls.Add(this.groupBoxAction);
			this.Controls.Add(this.groupBox1);
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
			this.MaximizeBox = false;
			this.MinimizeBox = false;
			this.Name = "EditActionDialog";
			this.ShowIcon = false;
			this.ShowInTaskbar = false;
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
			this.Text = "Action";
			this.groupBox1.ResumeLayout(false);
			this.groupBox1.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownTurnX)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownLevel)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownHP)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownTurn)).EndInit();
			this.groupBoxAction.ResumeLayout(false);
			this.groupBoxAction.PerformLayout();
			this.groupBoxRating.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownRating)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.trackBarRating)).EndInit();
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.GroupBox groupBox1;
		private System.Windows.Forms.Label labelOn;
		private System.Windows.Forms.NumericUpDown numericUpDownTurnX;
		private System.Windows.Forms.CheckBox checkBoxSwitch;
		private System.Windows.Forms.CheckBox checkBoxLevel;
		private System.Windows.Forms.CheckBox checkBoxHP;
		private System.Windows.Forms.ComboBox comboBoxSwitch;
		private System.Windows.Forms.Label labelAbove;
		private System.Windows.Forms.NumericUpDown numericUpDownLevel;
		private System.Windows.Forms.Label labelBelow;
		private System.Windows.Forms.NumericUpDown numericUpDownHP;
		private System.Windows.Forms.Label labelTurnPlus;
		private System.Windows.Forms.NumericUpDown numericUpDownTurn;
		private System.Windows.Forms.CheckBox checkBoxTurn;
		private System.Windows.Forms.GroupBox groupBoxAction;
		private System.Windows.Forms.RadioButton radioButtonSkill;
		private System.Windows.Forms.RadioButton radioButtonBasic;
		private System.Windows.Forms.ComboBox comboBoxSkill;
		private System.Windows.Forms.ComboBox comboBoxBasic;
		private System.Windows.Forms.Button buttonCancel;
		private System.Windows.Forms.Button buttonOK;
		private System.Windows.Forms.GroupBox groupBoxRating;
		private System.Windows.Forms.NumericUpDown numericUpDownRating;
		private System.Windows.Forms.TrackBar trackBarRating;
	}
}