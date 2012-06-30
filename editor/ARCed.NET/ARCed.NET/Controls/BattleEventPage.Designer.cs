namespace ARCed.Controls
{
	partial class BattleEventPage
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

		#region Component Designer generated code

		/// <summary> 
		/// Required method for Designer support - do not modify 
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
			this.labelCondition = new System.Windows.Forms.Label();
			this.textBoxCondition = new System.Windows.Forms.TextBox();
			this.buttonCondition = new System.Windows.Forms.Button();
			this.comboBoxSpan = new System.Windows.Forms.ComboBox();
			this.labelSpan = new System.Windows.Forms.Label();
			this.eventTextBox = new ARCed.Controls.EventTextBox();
			this.SuspendLayout();
			// 
			// labelCondition
			// 
			this.labelCondition.AutoSize = true;
			this.labelCondition.Location = new System.Drawing.Point(3, 9);
			this.labelCondition.Name = "labelCondition";
			this.labelCondition.Size = new System.Drawing.Size(54, 13);
			this.labelCondition.TabIndex = 0;
			this.labelCondition.Text = "Condition:";
			// 
			// textBoxCondition
			// 
			this.textBoxCondition.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBoxCondition.BackColor = System.Drawing.SystemColors.Window;
			this.textBoxCondition.Location = new System.Drawing.Point(63, 6);
			this.textBoxCondition.Name = "textBoxCondition";
			this.textBoxCondition.ReadOnly = true;
			this.textBoxCondition.Size = new System.Drawing.Size(174, 20);
			this.textBoxCondition.TabIndex = 1;
			// 
			// buttonCondition
			// 
			this.buttonCondition.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonCondition.Image = global::ARCed.Properties.Resources.Edit;
			this.buttonCondition.Location = new System.Drawing.Point(243, 3);
			this.buttonCondition.Name = "buttonCondition";
			this.buttonCondition.Size = new System.Drawing.Size(24, 24);
			this.buttonCondition.TabIndex = 2;
			this.buttonCondition.UseVisualStyleBackColor = true;
			// 
			// comboBoxSpan
			// 
			this.comboBoxSpan.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxSpan.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxSpan.FormattingEnabled = true;
			this.comboBoxSpan.Items.AddRange(new object[] {
            "Battle",
            "Turn",
            "Moment"});
			this.comboBoxSpan.Location = new System.Drawing.Point(333, 6);
			this.comboBoxSpan.Name = "comboBoxSpan";
			this.comboBoxSpan.Size = new System.Drawing.Size(72, 21);
			this.comboBoxSpan.TabIndex = 3;
			this.comboBoxSpan.SelectedIndexChanged += new System.EventHandler(this.comboBoxSpan_SelectedIndexChanged);
			// 
			// labelSpan
			// 
			this.labelSpan.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.labelSpan.AutoSize = true;
			this.labelSpan.Location = new System.Drawing.Point(292, 9);
			this.labelSpan.Name = "labelSpan";
			this.labelSpan.Size = new System.Drawing.Size(35, 13);
			this.labelSpan.TabIndex = 4;
			this.labelSpan.Text = "Span:";
			// 
			// eventTextBox
			// 
			this.eventTextBox.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.eventTextBox.BackColor = System.Drawing.SystemColors.Window;
			this.eventTextBox.Location = new System.Drawing.Point(6, 32);
			this.eventTextBox.Name = "eventTextBox";
			this.eventTextBox.ReadOnly = true;
			this.eventTextBox.Size = new System.Drawing.Size(399, 212);
			this.eventTextBox.TabIndex = 5;
			this.eventTextBox.Text = "";
			// 
			// BattleEventPage
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.BackColor = System.Drawing.SystemColors.Window;
			this.Controls.Add(this.eventTextBox);
			this.Controls.Add(this.labelSpan);
			this.Controls.Add(this.comboBoxSpan);
			this.Controls.Add(this.buttonCondition);
			this.Controls.Add(this.textBoxCondition);
			this.Controls.Add(this.labelCondition);
			this.Name = "BattleEventPage";
			this.Size = new System.Drawing.Size(408, 247);
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Label labelCondition;
		private System.Windows.Forms.TextBox textBoxCondition;
		private System.Windows.Forms.Button buttonCondition;
		private System.Windows.Forms.ComboBox comboBoxSpan;
		private System.Windows.Forms.Label labelSpan;
		private EventTextBox eventTextBox;
	}
}
