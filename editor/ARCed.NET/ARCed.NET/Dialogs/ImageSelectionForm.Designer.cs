namespace ARCed.Dialogs
{
	partial class ImageSelectionForm
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
			this.splitContainer1 = new System.Windows.Forms.SplitContainer();
			this.listBoxGraphics = new System.Windows.Forms.ListBox();
			this.groupBoxHue = new System.Windows.Forms.GroupBox();
			this.trackBarHue = new System.Windows.Forms.TrackBar();
			this.label1 = new System.Windows.Forms.Label();
			this.label2 = new System.Windows.Forms.Label();
			this.pictureBox = new ARCed.Controls.CharSelectionControl();
			((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).BeginInit();
			this.splitContainer1.Panel1.SuspendLayout();
			this.splitContainer1.Panel2.SuspendLayout();
			this.splitContainer1.SuspendLayout();
			this.groupBoxHue.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.trackBarHue)).BeginInit();
			this.SuspendLayout();
			// 
			// buttonCancel
			// 
			this.buttonCancel.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
			this.buttonCancel.Location = new System.Drawing.Point(496, 406);
			this.buttonCancel.Name = "buttonCancel";
			this.buttonCancel.Size = new System.Drawing.Size(75, 23);
			this.buttonCancel.TabIndex = 0;
			this.buttonCancel.Text = "Cancel";
			this.buttonCancel.UseVisualStyleBackColor = true;
			// 
			// buttonOK
			// 
			this.buttonOK.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonOK.Location = new System.Drawing.Point(415, 406);
			this.buttonOK.Name = "buttonOK";
			this.buttonOK.Size = new System.Drawing.Size(75, 23);
			this.buttonOK.TabIndex = 1;
			this.buttonOK.Text = "OK";
			this.buttonOK.UseVisualStyleBackColor = true;
			this.buttonOK.Click += new System.EventHandler(this.buttonOK_Click);
			// 
			// splitContainerWeapons
			// 
			this.splitContainer1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.splitContainer1.Location = new System.Drawing.Point(12, 12);
			this.splitContainer1.Name = "splitContainer1";
			// 
			// splitContainerWeapons.Panel1
			// 
			this.splitContainer1.Panel1.Controls.Add(this.listBoxGraphics);
			// 
			// splitContainerWeapons.Panel2
			// 
			this.splitContainer1.Panel2.Controls.Add(this.pictureBox);
			this.splitContainer1.Panel2.Controls.Add(this.groupBoxHue);
			this.splitContainer1.Size = new System.Drawing.Size(559, 388);
			this.splitContainer1.SplitterDistance = 144;
			this.splitContainer1.TabIndex = 2;
			// 
			// listBoxGraphics
			// 
			this.listBoxGraphics.Dock = System.Windows.Forms.DockStyle.Fill;
			this.listBoxGraphics.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed;
			this.listBoxGraphics.FormattingEnabled = true;
			this.listBoxGraphics.IntegralHeight = false;
			this.listBoxGraphics.Location = new System.Drawing.Point(0, 0);
			this.listBoxGraphics.Name = "listBoxGraphics";
			this.listBoxGraphics.Size = new System.Drawing.Size(144, 388);
			this.listBoxGraphics.TabIndex = 0;
			this.listBoxGraphics.DrawItem += new System.Windows.Forms.DrawItemEventHandler(this.listBoxGraphics_DrawItem);
			this.listBoxGraphics.SelectedIndexChanged += new System.EventHandler(this.listBoxGraphics_SelectedIndexChanged);
			this.listBoxGraphics.DoubleClick += new System.EventHandler(this.buttonOK_Click);
			// 
			// groupBoxHue
			// 
			this.groupBoxHue.Controls.Add(this.trackBarHue);
			this.groupBoxHue.Dock = System.Windows.Forms.DockStyle.Bottom;
			this.groupBoxHue.Location = new System.Drawing.Point(0, 322);
			this.groupBoxHue.Name = "groupBoxHue";
			this.groupBoxHue.Size = new System.Drawing.Size(411, 66);
			this.groupBoxHue.TabIndex = 0;
			this.groupBoxHue.TabStop = false;
			this.groupBoxHue.Text = "Hue";
			// 
			// trackBarHue
			// 
			this.trackBarHue.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.trackBarHue.Location = new System.Drawing.Point(6, 15);
			this.trackBarHue.Maximum = 359;
			this.trackBarHue.Name = "trackBarHue";
			this.trackBarHue.Size = new System.Drawing.Size(399, 45);
			this.trackBarHue.TabIndex = 0;
			this.trackBarHue.TickFrequency = 8;
			this.trackBarHue.ValueChanged += new System.EventHandler(this.trackBarHue_ValueChanged);
			// 
			// label1
			// 
			this.label1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.label1.AutoSize = true;
			this.label1.Image = global::ARCed.Properties.Resources.ResourceRTP;
			this.label1.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
			this.label1.Location = new System.Drawing.Point(86, 411);
			this.label1.Name = "label1";
			this.label1.Size = new System.Drawing.Size(50, 13);
			this.label1.TabIndex = 3;
			this.label1.Text = "     : RTP";
			this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
			// 
			// label2
			// 
			this.label2.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.label2.AutoSize = true;
			this.label2.Image = global::ARCed.Properties.Resources.ResourceLocal;
			this.label2.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
			this.label2.Location = new System.Drawing.Point(12, 411);
			this.label2.Name = "label2";
			this.label2.Size = new System.Drawing.Size(54, 13);
			this.label2.TabIndex = 4;
			this.label2.Text = "     : Local";
			this.label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
			// 
			// pictureBox
			// 
			this.pictureBox.AutoScroll = true;
			this.pictureBox.AutoSize = true;
			this.pictureBox.BackColor = System.Drawing.SystemColors.ControlDark;
			this.pictureBox.Dock = System.Windows.Forms.DockStyle.Fill;
			this.pictureBox.Image = null;
			this.pictureBox.ImageBackColor = System.Drawing.SystemColors.ControlLight;
			this.pictureBox.Location = new System.Drawing.Point(0, 0);
			this.pictureBox.Name = "pictureBox";
			this.pictureBox.Size = new System.Drawing.Size(411, 322);
			this.pictureBox.TabIndex = 1;
			// 
			// ImageSelectionForm
			// 
			this.AcceptButton = this.buttonOK;
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.CancelButton = this.buttonCancel;
			this.ClientSize = new System.Drawing.Size(583, 441);
			this.Controls.Add(this.label2);
			this.Controls.Add(this.label1);
			this.Controls.Add(this.splitContainer1);
			this.Controls.Add(this.buttonOK);
			this.Controls.Add(this.buttonCancel);
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.SizableToolWindow;
			this.Name = "ImageSelectionForm";
			this.ShowInTaskbar = false;
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
			this.Text = "Select Graphic";
			this.splitContainer1.Panel1.ResumeLayout(false);
			this.splitContainer1.Panel2.ResumeLayout(false);
			this.splitContainer1.Panel2.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).EndInit();
			this.splitContainer1.ResumeLayout(false);
			this.groupBoxHue.ResumeLayout(false);
			this.groupBoxHue.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.trackBarHue)).EndInit();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Button buttonCancel;
		private System.Windows.Forms.Button buttonOK;
		private System.Windows.Forms.SplitContainer splitContainer1;
		private System.Windows.Forms.ListBox listBoxGraphics;
		private System.Windows.Forms.GroupBox groupBoxHue;
		private System.Windows.Forms.TrackBar trackBarHue;
		private ARCed.Controls.CharSelectionControl pictureBox;
		private System.Windows.Forms.Label label1;
		private System.Windows.Forms.Label label2;
	}
}