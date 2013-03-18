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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(HeaderSettingsDialog));
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
            resources.ApplyResources(this.labelStartGradient, "labelStartGradient");
            this.labelStartGradient.Name = "labelStartGradient";
            // 
            // panelStartGradient
            // 
            this.panelStartGradient.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            resources.ApplyResources(this.panelStartGradient, "panelStartGradient");
            this.panelStartGradient.Name = "panelStartGradient";
            this.toolTip.SetToolTip(this.panelStartGradient, resources.GetString("panelStartGradient.ToolTip"));
            this.panelStartGradient.DoubleClick += new System.EventHandler(this.panelStartGradient_DoubleClick);
            // 
            // panelEndGradient
            // 
            this.panelEndGradient.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            resources.ApplyResources(this.panelEndGradient, "panelEndGradient");
            this.panelEndGradient.Name = "panelEndGradient";
            this.toolTip.SetToolTip(this.panelEndGradient, resources.GetString("panelEndGradient.ToolTip"));
            this.panelEndGradient.DoubleClick += new System.EventHandler(this.panelEndGradient_DoubleClick);
            // 
            // panelTextColor
            // 
            this.panelTextColor.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            resources.ApplyResources(this.panelTextColor, "panelTextColor");
            this.panelTextColor.Name = "panelTextColor";
            this.toolTip.SetToolTip(this.panelTextColor, resources.GetString("panelTextColor.ToolTip"));
            this.panelTextColor.DoubleClick += new System.EventHandler(this.panelTextColor_DoubleClick);
            // 
            // labelEndGradient
            // 
            resources.ApplyResources(this.labelEndGradient, "labelEndGradient");
            this.labelEndGradient.Name = "labelEndGradient";
            // 
            // labelTextColor
            // 
            resources.ApplyResources(this.labelTextColor, "labelTextColor");
            this.labelTextColor.Name = "labelTextColor";
            // 
            // buttonCancel
            // 
            this.buttonCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            resources.ApplyResources(this.buttonCancel, "buttonCancel");
            this.buttonCancel.Name = "buttonCancel";
            this.buttonCancel.UseVisualStyleBackColor = true;
            // 
            // buttonOK
            // 
            resources.ApplyResources(this.buttonOK, "buttonOK");
            this.buttonOK.Name = "buttonOK";
            this.buttonOK.UseVisualStyleBackColor = true;
            this.buttonOK.Click += new System.EventHandler(this.buttonOK_Click);
            // 
            // fontSelector
            // 
            resources.ApplyResources(this.fontSelector, "fontSelector");
            this.fontSelector.Name = "fontSelector";
            this.fontSelector.OnUserFontChanged += new ARCed.Controls.FontSelector.FontChangedEventHandler(this.fontSelector_OnUserFontChanged);
            // 
            // HeaderSettingsDialog
            // 
            this.AcceptButton = this.buttonOK;
            this.AccessibleRole = System.Windows.Forms.AccessibleRole.Dialog;
            resources.ApplyResources(this, "$this");
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.CancelButton = this.buttonCancel;
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