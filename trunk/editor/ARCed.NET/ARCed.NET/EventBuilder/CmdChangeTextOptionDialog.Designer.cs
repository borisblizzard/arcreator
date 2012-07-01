namespace ARCed.EventBuilder
{
	partial class CmdChangeTextOptionsDialog
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
			this.buttonCancel = new System.Windows.Forms.Button();
			this.buttonOK = new System.Windows.Forms.Button();
			this.groupBoxPosition = new System.Windows.Forms.GroupBox();
			this.radioButtonBottom = new System.Windows.Forms.RadioButton();
			this.radioButtonMiddle = new System.Windows.Forms.RadioButton();
			this.radioButtonTop = new System.Windows.Forms.RadioButton();
			this.groupBoxWindow = new System.Windows.Forms.GroupBox();
			this.radioButtonHide = new System.Windows.Forms.RadioButton();
			this.radioButtonShow = new System.Windows.Forms.RadioButton();
			this.groupBoxPosition.SuspendLayout();
			this.groupBoxWindow.SuspendLayout();
			this.SuspendLayout();
			// 
			// buttonCancel
			// 
			this.buttonCancel.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
			this.buttonCancel.Location = new System.Drawing.Point(128, 113);
			this.buttonCancel.Name = "buttonCancel";
			this.buttonCancel.Size = new System.Drawing.Size(75, 23);
			this.buttonCancel.TabIndex = 0;
			this.buttonCancel.Text = "Cancel";
			this.buttonCancel.UseVisualStyleBackColor = true;
			// 
			// buttonOK
			// 
			this.buttonOK.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonOK.Location = new System.Drawing.Point(47, 113);
			this.buttonOK.Name = "buttonOK";
			this.buttonOK.Size = new System.Drawing.Size(75, 23);
			this.buttonOK.TabIndex = 1;
			this.buttonOK.Text = "OK";
			this.buttonOK.UseVisualStyleBackColor = true;
			this.buttonOK.Click += new System.EventHandler(this.buttonOK_Click);
			// 
			// groupBoxPosition
			// 
			this.groupBoxPosition.Controls.Add(this.radioButtonBottom);
			this.groupBoxPosition.Controls.Add(this.radioButtonMiddle);
			this.groupBoxPosition.Controls.Add(this.radioButtonTop);
			this.groupBoxPosition.Location = new System.Drawing.Point(12, 12);
			this.groupBoxPosition.Name = "groupBoxPosition";
			this.groupBoxPosition.Size = new System.Drawing.Size(92, 92);
			this.groupBoxPosition.TabIndex = 2;
			this.groupBoxPosition.TabStop = false;
			this.groupBoxPosition.Text = "Position";
			// 
			// radioButtonBottom
			// 
			this.radioButtonBottom.AutoSize = true;
			this.radioButtonBottom.Location = new System.Drawing.Point(6, 65);
			this.radioButtonBottom.Name = "radioButtonBottom";
			this.radioButtonBottom.Size = new System.Drawing.Size(58, 17);
			this.radioButtonBottom.TabIndex = 2;
			this.radioButtonBottom.Text = "Bottom";
			this.radioButtonBottom.UseVisualStyleBackColor = true;
			// 
			// radioButtonMiddle
			// 
			this.radioButtonMiddle.AutoSize = true;
			this.radioButtonMiddle.Checked = true;
			this.radioButtonMiddle.Location = new System.Drawing.Point(6, 42);
			this.radioButtonMiddle.Name = "radioButtonMiddle";
			this.radioButtonMiddle.Size = new System.Drawing.Size(56, 17);
			this.radioButtonMiddle.TabIndex = 1;
			this.radioButtonMiddle.TabStop = true;
			this.radioButtonMiddle.Text = "Middle";
			this.radioButtonMiddle.UseVisualStyleBackColor = true;
			// 
			// radioButtonTop
			// 
			this.radioButtonTop.AutoSize = true;
			this.radioButtonTop.Location = new System.Drawing.Point(6, 19);
			this.radioButtonTop.Name = "radioButtonTop";
			this.radioButtonTop.Size = new System.Drawing.Size(44, 17);
			this.radioButtonTop.TabIndex = 0;
			this.radioButtonTop.Text = "Top";
			this.radioButtonTop.UseVisualStyleBackColor = true;
			// 
			// groupBoxWindow
			// 
			this.groupBoxWindow.Controls.Add(this.radioButtonHide);
			this.groupBoxWindow.Controls.Add(this.radioButtonShow);
			this.groupBoxWindow.Location = new System.Drawing.Point(110, 12);
			this.groupBoxWindow.Name = "groupBoxWindow";
			this.groupBoxWindow.Size = new System.Drawing.Size(92, 92);
			this.groupBoxWindow.TabIndex = 3;
			this.groupBoxWindow.TabStop = false;
			this.groupBoxWindow.Text = "Window";
			// 
			// radioButtonHide
			// 
			this.radioButtonHide.AutoSize = true;
			this.radioButtonHide.Location = new System.Drawing.Point(6, 42);
			this.radioButtonHide.Name = "radioButtonHide";
			this.radioButtonHide.Size = new System.Drawing.Size(47, 17);
			this.radioButtonHide.TabIndex = 1;
			this.radioButtonHide.Text = "Hide";
			this.radioButtonHide.UseVisualStyleBackColor = true;
			// 
			// radioButtonShow
			// 
			this.radioButtonShow.AutoSize = true;
			this.radioButtonShow.Checked = true;
			this.radioButtonShow.Location = new System.Drawing.Point(6, 19);
			this.radioButtonShow.Name = "radioButtonShow";
			this.radioButtonShow.Size = new System.Drawing.Size(52, 17);
			this.radioButtonShow.TabIndex = 0;
			this.radioButtonShow.TabStop = true;
			this.radioButtonShow.Text = "Show";
			this.radioButtonShow.UseVisualStyleBackColor = true;
			// 
			// CmdChangeTextOptionsDialog
			// 
			this.AcceptButton = this.buttonOK;
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.CancelButton = this.buttonCancel;
			this.ClientSize = new System.Drawing.Size(215, 148);
			this.Controls.Add(this.groupBoxWindow);
			this.Controls.Add(this.groupBoxPosition);
			this.Controls.Add(this.buttonOK);
			this.Controls.Add(this.buttonCancel);
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
			this.Name = "CmdChangeTextOptions";
			this.ShowIcon = false;
			this.ShowInTaskbar = false;
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
			this.Text = "Change Text Options";
			this.groupBoxPosition.ResumeLayout(false);
			this.groupBoxPosition.PerformLayout();
			this.groupBoxWindow.ResumeLayout(false);
			this.groupBoxWindow.PerformLayout();
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.Button buttonCancel;
		private System.Windows.Forms.Button buttonOK;
		private System.Windows.Forms.GroupBox groupBoxPosition;
		private System.Windows.Forms.RadioButton radioButtonBottom;
		private System.Windows.Forms.RadioButton radioButtonMiddle;
		private System.Windows.Forms.RadioButton radioButtonTop;
		private System.Windows.Forms.GroupBox groupBoxWindow;
		private System.Windows.Forms.RadioButton radioButtonHide;
		private System.Windows.Forms.RadioButton radioButtonShow;
	}
}