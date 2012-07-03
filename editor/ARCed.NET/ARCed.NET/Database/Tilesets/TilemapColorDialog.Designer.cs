namespace ARCed.Database.Tilesets
{
	partial class TilemapColorDialog
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
			this.label1 = new System.Windows.Forms.Label();
			this.panelBackground = new System.Windows.Forms.Panel();
			this.panelSelector = new System.Windows.Forms.Panel();
			this.label2 = new System.Windows.Forms.Label();
			this.panelGrid = new System.Windows.Forms.Panel();
			this.label3 = new System.Windows.Forms.Label();
			this.buttonCancel = new System.Windows.Forms.Button();
			this.buttonOK = new System.Windows.Forms.Button();
			this.toolTip = new System.Windows.Forms.ToolTip(this.components);
			this.SuspendLayout();
			// 
			// label1
			// 
			this.label1.AutoSize = true;
			this.label1.Location = new System.Drawing.Point(12, 9);
			this.label1.Name = "label1";
			this.label1.Size = new System.Drawing.Size(68, 13);
			this.label1.TabIndex = 0;
			this.label1.Text = "Background:";
			// 
			// panelBackground
			// 
			this.panelBackground.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
			this.panelBackground.Location = new System.Drawing.Point(15, 25);
			this.panelBackground.Name = "panelBackground";
			this.panelBackground.Size = new System.Drawing.Size(66, 31);
			this.panelBackground.TabIndex = 1;
			this.toolTip.SetToolTip(this.panelBackground, "Double-click to edit");
			this.panelBackground.Click += new System.EventHandler(this.panelBackgroundColor_DoubleClick);
			// 
			// panelSelector
			// 
			this.panelSelector.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
			this.panelSelector.Location = new System.Drawing.Point(87, 25);
			this.panelSelector.Name = "panelSelector";
			this.panelSelector.Size = new System.Drawing.Size(65, 31);
			this.panelSelector.TabIndex = 3;
			this.toolTip.SetToolTip(this.panelSelector, "Double-click to edit");
			this.panelSelector.Click += new System.EventHandler(this.panelSelectorColor_DoubleClick);
			// 
			// label2
			// 
			this.label2.AutoSize = true;
			this.label2.Location = new System.Drawing.Point(84, 9);
			this.label2.Name = "label2";
			this.label2.Size = new System.Drawing.Size(49, 13);
			this.label2.TabIndex = 2;
			this.label2.Text = "Selector:";
			// 
			// panelGrid
			// 
			this.panelGrid.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
			this.panelGrid.Location = new System.Drawing.Point(158, 25);
			this.panelGrid.Name = "panelGrid";
			this.panelGrid.Size = new System.Drawing.Size(65, 31);
			this.panelGrid.TabIndex = 5;
			this.toolTip.SetToolTip(this.panelGrid, "Double-click to edit");
			this.panelGrid.Click += new System.EventHandler(this.panelGridColor_DoubleClick);
			// 
			// label3
			// 
			this.label3.AutoSize = true;
			this.label3.Location = new System.Drawing.Point(155, 9);
			this.label3.Name = "label3";
			this.label3.Size = new System.Drawing.Size(57, 13);
			this.label3.TabIndex = 4;
			this.label3.Text = "Grid Lines:";
			// 
			// buttonCancel
			// 
			this.buttonCancel.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
			this.buttonCancel.Location = new System.Drawing.Point(148, 66);
			this.buttonCancel.Name = "buttonCancel";
			this.buttonCancel.Size = new System.Drawing.Size(75, 23);
			this.buttonCancel.TabIndex = 6;
			this.buttonCancel.Text = "Cancel";
			this.buttonCancel.UseVisualStyleBackColor = true;
			// 
			// buttonOK
			// 
			this.buttonOK.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonOK.Location = new System.Drawing.Point(67, 66);
			this.buttonOK.Name = "buttonOK";
			this.buttonOK.Size = new System.Drawing.Size(75, 23);
			this.buttonOK.TabIndex = 7;
			this.buttonOK.Text = "OK";
			this.buttonOK.UseVisualStyleBackColor = true;
			this.buttonOK.Click += new System.EventHandler(this.buttonOK_Click);
			// 
			// TilemapColorDialog
			// 
			this.AcceptButton = this.buttonOK;
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.CancelButton = this.buttonCancel;
			this.ClientSize = new System.Drawing.Size(238, 101);
			this.Controls.Add(this.buttonOK);
			this.Controls.Add(this.buttonCancel);
			this.Controls.Add(this.panelGrid);
			this.Controls.Add(this.label3);
			this.Controls.Add(this.panelSelector);
			this.Controls.Add(this.label2);
			this.Controls.Add(this.panelBackground);
			this.Controls.Add(this.label1);
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
			this.Name = "TilemapColorDialog";
			this.ShowIcon = false;
			this.ShowInTaskbar = false;
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
			this.Text = "Tileset Colors";
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Label label1;
		private System.Windows.Forms.Panel panelBackground;
		private System.Windows.Forms.Panel panelSelector;
		private System.Windows.Forms.Label label2;
		private System.Windows.Forms.Panel panelGrid;
		private System.Windows.Forms.Label label3;
		private System.Windows.Forms.Button buttonCancel;
		private System.Windows.Forms.Button buttonOK;
		private System.Windows.Forms.ToolTip toolTip;
	}
}