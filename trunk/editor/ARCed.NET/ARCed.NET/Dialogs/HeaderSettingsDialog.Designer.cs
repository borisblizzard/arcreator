namespace ARCed.Dialogs
{
	partial class HeaderSettingsDialog
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
			this.labelStartGradient = new System.Windows.Forms.Label();
			this.panelStartGradient = new System.Windows.Forms.Panel();
			this.toolTip = new System.Windows.Forms.ToolTip(this.components);
			this.panelEndGradient = new System.Windows.Forms.Panel();
			this.panelTextColor = new System.Windows.Forms.Panel();
			this.labelEndGradient = new System.Windows.Forms.Label();
			this.labelTextColor = new System.Windows.Forms.Label();
			this.buttonCancel = new System.Windows.Forms.Button();
			this.buttonOK = new System.Windows.Forms.Button();
			this.fontSelector = new ARCed.Controls.FontSelector();
			this.SuspendLayout();
			// 
			// labelStartGradient
			// 
			this.labelStartGradient.AutoSize = true;
			this.labelStartGradient.Location = new System.Drawing.Point(12, 9);
			this.labelStartGradient.Name = "labelStartGradient";
			this.labelStartGradient.Size = new System.Drawing.Size(75, 13);
			this.labelStartGradient.TabIndex = 0;
			this.labelStartGradient.Text = "Start Gradient:";
			// 
			// panelStartGradient
			// 
			this.panelStartGradient.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
			this.panelStartGradient.Location = new System.Drawing.Point(15, 25);
			this.panelStartGradient.Name = "panelStartGradient";
			this.panelStartGradient.Size = new System.Drawing.Size(72, 28);
			this.panelStartGradient.TabIndex = 1;
			this.toolTip.SetToolTip(this.panelStartGradient, "Double-click to edit");
			this.panelStartGradient.DoubleClick += new System.EventHandler(this.panelStartGradient_DoubleClick);
			// 
			// panelEndGradient
			// 
			this.panelEndGradient.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
			this.panelEndGradient.Location = new System.Drawing.Point(96, 25);
			this.panelEndGradient.Name = "panelEndGradient";
			this.panelEndGradient.Size = new System.Drawing.Size(72, 28);
			this.panelEndGradient.TabIndex = 3;
			this.toolTip.SetToolTip(this.panelEndGradient, "Double-click to edit");
			this.panelEndGradient.DoubleClick += new System.EventHandler(this.panelEndGradient_DoubleClick);
			// 
			// panelTextColor
			// 
			this.panelTextColor.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
			this.panelTextColor.Location = new System.Drawing.Point(174, 25);
			this.panelTextColor.Name = "panelTextColor";
			this.panelTextColor.Size = new System.Drawing.Size(72, 28);
			this.panelTextColor.TabIndex = 5;
			this.toolTip.SetToolTip(this.panelTextColor, "Double-click to edit");
			this.panelTextColor.DoubleClick += new System.EventHandler(this.panelTextColor_DoubleClick);
			// 
			// labelEndGradient
			// 
			this.labelEndGradient.AutoSize = true;
			this.labelEndGradient.Location = new System.Drawing.Point(93, 9);
			this.labelEndGradient.Name = "labelEndGradient";
			this.labelEndGradient.Size = new System.Drawing.Size(72, 13);
			this.labelEndGradient.TabIndex = 2;
			this.labelEndGradient.Text = "End Gradient:";
			// 
			// labelTextColor
			// 
			this.labelTextColor.AutoSize = true;
			this.labelTextColor.Location = new System.Drawing.Point(171, 9);
			this.labelTextColor.Name = "labelTextColor";
			this.labelTextColor.Size = new System.Drawing.Size(58, 13);
			this.labelTextColor.TabIndex = 4;
			this.labelTextColor.Text = "Text Color:";
			// 
			// buttonCancel
			// 
			this.buttonCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
			this.buttonCancel.Location = new System.Drawing.Point(173, 207);
			this.buttonCancel.Name = "buttonCancel";
			this.buttonCancel.Size = new System.Drawing.Size(75, 23);
			this.buttonCancel.TabIndex = 9;
			this.buttonCancel.Text = "Cancel";
			this.buttonCancel.UseVisualStyleBackColor = true;
			// 
			// buttonOK
			// 
			this.buttonOK.Location = new System.Drawing.Point(93, 207);
			this.buttonOK.Name = "buttonOK";
			this.buttonOK.Size = new System.Drawing.Size(75, 23);
			this.buttonOK.TabIndex = 10;
			this.buttonOK.Text = "OK";
			this.buttonOK.UseVisualStyleBackColor = true;
			this.buttonOK.Click += new System.EventHandler(this.buttonOK_Click);
			// 
			// fontSelector
			// 
			this.fontSelector.Location = new System.Drawing.Point(15, 59);
			this.fontSelector.Name = "fontSelector";
			this.fontSelector.Size = new System.Drawing.Size(231, 142);
			this.fontSelector.TabIndex = 13;
			this.fontSelector.OnUserFontChanged += new ARCed.Controls.FontSelector.FontChangedEventHandler(this.fontSelector_OnUserFontChanged);
			// 
			// HeaderSettingsDialog
			// 
			this.AcceptButton = this.buttonOK;
			this.AccessibleRole = System.Windows.Forms.AccessibleRole.Dialog;
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.CancelButton = this.buttonCancel;
			this.ClientSize = new System.Drawing.Size(261, 241);
			this.Controls.Add(this.fontSelector);
			this.Controls.Add(this.buttonOK);
			this.Controls.Add(this.buttonCancel);
			this.Controls.Add(this.panelTextColor);
			this.Controls.Add(this.labelTextColor);
			this.Controls.Add(this.panelEndGradient);
			this.Controls.Add(this.labelEndGradient);
			this.Controls.Add(this.panelStartGradient);
			this.Controls.Add(this.labelStartGradient);
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
			this.MaximizeBox = false;
			this.MinimizeBox = false;
			this.Name = "HeaderSettingsDialog";
			this.ShowIcon = false;
			this.ShowInTaskbar = false;
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
			this.Text = "Edit Appearance";
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Label labelStartGradient;
		private System.Windows.Forms.Panel panelStartGradient;
		private System.Windows.Forms.ToolTip toolTip;
		private System.Windows.Forms.Panel panelEndGradient;
		private System.Windows.Forms.Label labelEndGradient;
		private System.Windows.Forms.Panel panelTextColor;
		private System.Windows.Forms.Label labelTextColor;
		private System.Windows.Forms.Button buttonCancel;
		private System.Windows.Forms.Button buttonOK;
		private Controls.FontSelector fontSelector;
	}
}