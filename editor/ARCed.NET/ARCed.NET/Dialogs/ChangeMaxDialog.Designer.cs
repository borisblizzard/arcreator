namespace ARCed.Dialogs
{
	partial class ChangeMaxDialog
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(ChangeMaxDialog));
            this.buttonOK = new System.Windows.Forms.Button();
            this.buttonCancel = new System.Windows.Forms.Button();
            this.labelCurrent = new System.Windows.Forms.Label();
            this.labelMax = new System.Windows.Forms.Label();
            this.numericMax = new System.Windows.Forms.NumericUpDown();
            ((System.ComponentModel.ISupportInitialize)(this.numericMax)).BeginInit();
            this.SuspendLayout();
            // 
            // buttonOK
            // 
            resources.ApplyResources(this.buttonOK, "buttonOK");
            this.buttonOK.Name = "buttonOK";
            this.buttonOK.UseVisualStyleBackColor = true;
            this.buttonOK.Click += new System.EventHandler(this.buttonOK_Click);
            // 
            // buttonCancel
            // 
            resources.ApplyResources(this.buttonCancel, "buttonCancel");
            this.buttonCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.buttonCancel.Name = "buttonCancel";
            this.buttonCancel.UseVisualStyleBackColor = true;
            // 
            // labelCurrent
            // 
            resources.ApplyResources(this.labelCurrent, "labelCurrent");
            this.labelCurrent.Name = "labelCurrent";
            // 
            // labelMax
            // 
            resources.ApplyResources(this.labelMax, "labelMax");
            this.labelMax.Name = "labelMax";
            // 
            // numericMax
            // 
            resources.ApplyResources(this.numericMax, "numericMax");
            this.numericMax.Name = "numericMax";
            // 
            // ChangeMaxDialog
            // 
            this.AcceptButton = this.buttonOK;
            resources.ApplyResources(this, "$this");
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.CancelButton = this.buttonCancel;
            this.Controls.Add(this.numericMax);
            this.Controls.Add(this.labelMax);
            this.Controls.Add(this.labelCurrent);
            this.Controls.Add(this.buttonCancel);
            this.Controls.Add(this.buttonOK);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "ChangeMaxDialog";
            this.ShowIcon = false;
            this.ShowInTaskbar = false;
            ((System.ComponentModel.ISupportInitialize)(this.numericMax)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Button buttonOK;
		private System.Windows.Forms.Button buttonCancel;
		private System.Windows.Forms.Label labelCurrent;
		private System.Windows.Forms.Label labelMax;
		private System.Windows.Forms.NumericUpDown numericMax;
	}
}