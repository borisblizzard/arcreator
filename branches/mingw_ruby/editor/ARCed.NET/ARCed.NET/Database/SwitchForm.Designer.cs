namespace ARCed.Database
{
    sealed partial class SwitchForm
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
			this.dataObjectList = new ARCed.Controls.DatabaseObjectListBox();
			this.labelName = new System.Windows.Forms.Label();
			this.textBoxName = new System.Windows.Forms.TextBox();
			this.SuspendLayout();
			// 
			// dataObjectList
			// 
			this.dataObjectList.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.dataObjectList.HeaderText = "Switches";
			this.dataObjectList.Location = new System.Drawing.Point(1, 2);
			this.dataObjectList.Name = "dataObjectList";
			this.dataObjectList.SelectedIndex = -1;
			this.dataObjectList.Size = new System.Drawing.Size(173, 380);
			this.dataObjectList.TabIndex = 1;
			this.dataObjectList.TabStop = false;
			this.dataObjectList.OnButtonMaxClick += new ARCed.Controls.DatabaseObjectListBox.ButtonMaxClickEventHandler(this.dataObjectList_OnButtonMaxClick);
			this.dataObjectList.OnListBoxIndexChanged += new ARCed.Controls.DatabaseObjectListBox.ObjectListIndexChangedEventHandler(this.dataObjectList_OnListBoxIndexChanged);
			// 
			// labelName
			// 
			this.labelName.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.labelName.AutoSize = true;
			this.labelName.Location = new System.Drawing.Point(9, 394);
			this.labelName.Name = "labelName";
			this.labelName.Size = new System.Drawing.Size(38, 13);
			this.labelName.TabIndex = 2;
			this.labelName.Text = "Name:";
			// 
			// textBoxName
			// 
			this.textBoxName.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBoxName.Location = new System.Drawing.Point(12, 410);
			this.textBoxName.Name = "textBoxName";
			this.textBoxName.Size = new System.Drawing.Size(152, 20);
			this.textBoxName.TabIndex = 3;
			this.textBoxName.TextChanged += new System.EventHandler(this.textBoxName_TextChanged);
			// 
			// SwitchForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(176, 442);
			this.Controls.Add(this.textBoxName);
			this.Controls.Add(this.labelName);
			this.Controls.Add(this.dataObjectList);
			this.DefaultFloatSize = new System.Drawing.Size(192, 480);
			this.DockAreas = ((ARCed.UI.DockAreas)(((ARCed.UI.DockAreas.Float | ARCed.UI.DockAreas.DockLeft)
						| ARCed.UI.DockAreas.DockRight)));
			this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.SizableToolWindow;
			this.Name = "SwitchForm";
			this.RpgTypeName = "RPG.RpgObject";
			this.ShowHint = ARCed.UI.DockState.DockRight;
			this.ShowIcon = false;
			this.ShowInTaskbar = false;
			this.Text = "SwitchVariableDialog";
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private Controls.DatabaseObjectListBox dataObjectList;
		private System.Windows.Forms.Label labelName;
		private System.Windows.Forms.TextBox textBoxName;

	}
}