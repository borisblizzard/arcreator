namespace ARCed.Scripting
{
	partial class ScriptStyleForm
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
			this.groupBoxStyle = new System.Windows.Forms.GroupBox();
			this.listBoxStyles = new System.Windows.Forms.ListBox();
			this.groupBoxColors = new System.Windows.Forms.GroupBox();
			this.splitContainer1 = new System.Windows.Forms.SplitContainer();
			this.labelCaret = new System.Windows.Forms.Label();
			this.panelCaretColor = new System.Windows.Forms.Panel();
			this.splitContainer2 = new System.Windows.Forms.SplitContainer();
			this.labelColorFore = new System.Windows.Forms.Label();
			this.panelColorFore = new System.Windows.Forms.Panel();
			this.labelBackColor = new System.Windows.Forms.Label();
			this.panelColorBack = new System.Windows.Forms.Panel();
			this.buttonDefault = new System.Windows.Forms.Button();
			this.toolTip = new System.Windows.Forms.ToolTip(this.components);
			this.fontSelector = new ARCed.Controls.FontSelector();
			this.groupBoxStyle.SuspendLayout();
			this.groupBoxColors.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).BeginInit();
			this.splitContainer1.Panel1.SuspendLayout();
			this.splitContainer1.Panel2.SuspendLayout();
			this.splitContainer1.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainer2)).BeginInit();
			this.splitContainer2.Panel1.SuspendLayout();
			this.splitContainer2.Panel2.SuspendLayout();
			this.splitContainer2.SuspendLayout();
			this.SuspendLayout();
			// 
			// groupBoxStyle
			// 
			this.groupBoxStyle.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxStyle.Controls.Add(this.listBoxStyles);
			this.groupBoxStyle.Location = new System.Drawing.Point(12, 12);
			this.groupBoxStyle.Name = "groupBoxStyle";
			this.groupBoxStyle.Size = new System.Drawing.Size(232, 158);
			this.groupBoxStyle.TabIndex = 0;
			this.groupBoxStyle.TabStop = false;
			this.groupBoxStyle.Text = "Style";
			// 
			// listBoxStyles
			// 
			this.listBoxStyles.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.listBoxStyles.FormattingEnabled = true;
			this.listBoxStyles.Location = new System.Drawing.Point(6, 19);
			this.listBoxStyles.Name = "listBoxStyles";
			this.listBoxStyles.Size = new System.Drawing.Size(220, 134);
			this.listBoxStyles.TabIndex = 0;
			this.toolTip.SetToolTip(this.listBoxStyles, "Select style to edit");
			this.listBoxStyles.SelectedIndexChanged += new System.EventHandler(this.listBoxStyles_SelectedIndexChanged);
			// 
			// groupBoxColors
			// 
			this.groupBoxColors.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxColors.Controls.Add(this.splitContainer1);
			this.groupBoxColors.Location = new System.Drawing.Point(15, 322);
			this.groupBoxColors.Name = "groupBoxColors";
			this.groupBoxColors.Size = new System.Drawing.Size(229, 75);
			this.groupBoxColors.TabIndex = 4;
			this.groupBoxColors.TabStop = false;
			this.groupBoxColors.Text = "Colors";
			// 
			// splitContainer1
			// 
			this.splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainer1.Location = new System.Drawing.Point(3, 16);
			this.splitContainer1.Name = "splitContainer1";
			// 
			// splitContainer1.Panel1
			// 
			this.splitContainer1.Panel1.Controls.Add(this.labelCaret);
			this.splitContainer1.Panel1.Controls.Add(this.panelCaretColor);
			// 
			// splitContainer1.Panel2
			// 
			this.splitContainer1.Panel2.Controls.Add(this.splitContainer2);
			this.splitContainer1.Size = new System.Drawing.Size(223, 56);
			this.splitContainer1.SplitterDistance = 73;
			this.splitContainer1.TabIndex = 0;
			// 
			// labelCaret
			// 
			this.labelCaret.AutoSize = true;
			this.labelCaret.Location = new System.Drawing.Point(3, 0);
			this.labelCaret.Name = "labelCaret";
			this.labelCaret.Size = new System.Drawing.Size(32, 13);
			this.labelCaret.TabIndex = 7;
			this.labelCaret.Text = "Caret";
			// 
			// panelCaretColor
			// 
			this.panelCaretColor.BackgroundImage = global::ARCed.Properties.Resources.Alpha;
			this.panelCaretColor.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
			this.panelCaretColor.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
			this.panelCaretColor.Location = new System.Drawing.Point(3, 16);
			this.panelCaretColor.Name = "panelCaretColor";
			this.panelCaretColor.Size = new System.Drawing.Size(67, 37);
			this.panelCaretColor.TabIndex = 6;
			this.toolTip.SetToolTip(this.panelCaretColor, "Caret color. Double-Click to edit.");
			this.panelCaretColor.Paint += new System.Windows.Forms.PaintEventHandler(this.panelColor_OnPaint);
			this.panelCaretColor.DoubleClick += new System.EventHandler(this.panelCaretColor_DoubleClick);
			// 
			// splitContainer2
			// 
			this.splitContainer2.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainer2.Location = new System.Drawing.Point(0, 0);
			this.splitContainer2.Name = "splitContainer2";
			// 
			// splitContainer2.Panel1
			// 
			this.splitContainer2.Panel1.Controls.Add(this.labelColorFore);
			this.splitContainer2.Panel1.Controls.Add(this.panelColorFore);
			// 
			// splitContainer2.Panel2
			// 
			this.splitContainer2.Panel2.Controls.Add(this.labelBackColor);
			this.splitContainer2.Panel2.Controls.Add(this.panelColorBack);
			this.splitContainer2.Size = new System.Drawing.Size(146, 56);
			this.splitContainer2.SplitterDistance = 71;
			this.splitContainer2.TabIndex = 0;
			// 
			// labelColorFore
			// 
			this.labelColorFore.AutoSize = true;
			this.labelColorFore.Location = new System.Drawing.Point(3, 0);
			this.labelColorFore.Name = "labelColorFore";
			this.labelColorFore.Size = new System.Drawing.Size(31, 13);
			this.labelColorFore.TabIndex = 2;
			this.labelColorFore.Text = "Fore:";
			// 
			// panelColorFore
			// 
			this.panelColorFore.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.panelColorFore.BackgroundImage = global::ARCed.Properties.Resources.Alpha;
			this.panelColorFore.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
			this.panelColorFore.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
			this.panelColorFore.Location = new System.Drawing.Point(3, 16);
			this.panelColorFore.Name = "panelColorFore";
			this.panelColorFore.Size = new System.Drawing.Size(65, 37);
			this.panelColorFore.TabIndex = 0;
			this.toolTip.SetToolTip(this.panelColorFore, "Foreground color. Double-Click to edit");
			this.panelColorFore.Paint += new System.Windows.Forms.PaintEventHandler(this.panelColor_OnPaint);
			this.panelColorFore.DoubleClick += new System.EventHandler(this.panelColorFore_DoubleClick);
			// 
			// labelBackColor
			// 
			this.labelBackColor.AutoSize = true;
			this.labelBackColor.Location = new System.Drawing.Point(3, 0);
			this.labelBackColor.Name = "labelBackColor";
			this.labelBackColor.Size = new System.Drawing.Size(35, 13);
			this.labelBackColor.TabIndex = 4;
			this.labelBackColor.Text = "Back:";
			// 
			// panelColorBack
			// 
			this.panelColorBack.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.panelColorBack.BackgroundImage = global::ARCed.Properties.Resources.Alpha;
			this.panelColorBack.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
			this.panelColorBack.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
			this.panelColorBack.Location = new System.Drawing.Point(3, 16);
			this.panelColorBack.Name = "panelColorBack";
			this.panelColorBack.Size = new System.Drawing.Size(65, 37);
			this.panelColorBack.TabIndex = 3;
			this.toolTip.SetToolTip(this.panelColorBack, "Background color. Double-Click to edit");
			this.panelColorBack.Paint += new System.Windows.Forms.PaintEventHandler(this.panelColor_OnPaint);
			this.panelColorBack.DoubleClick += new System.EventHandler(this.panelColorBack_DoubleClick);
			// 
			// buttonDefault
			// 
			this.buttonDefault.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonDefault.Location = new System.Drawing.Point(133, 403);
			this.buttonDefault.Name = "buttonDefault";
			this.buttonDefault.Size = new System.Drawing.Size(111, 23);
			this.buttonDefault.TabIndex = 5;
			this.buttonDefault.Text = "Reset Default";
			this.toolTip.SetToolTip(this.buttonDefault, "Reset style to default");
			this.buttonDefault.UseVisualStyleBackColor = true;
			this.buttonDefault.Click += new System.EventHandler(this.buttonDefault_Click);
			// 
			// fontSelector
			// 
			this.fontSelector.Location = new System.Drawing.Point(15, 176);
			this.fontSelector.Name = "fontSelector";
			this.fontSelector.Size = new System.Drawing.Size(229, 140);
			this.fontSelector.TabIndex = 8;
			this.fontSelector.OnUserFontChanged += new ARCed.Controls.FontSelector.FontChangedEventHandler(this.UpdateFont);
			// 
			// ScriptStyleForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(256, 437);
			this.Controls.Add(this.fontSelector);
			this.Controls.Add(this.buttonDefault);
			this.Controls.Add(this.groupBoxColors);
			this.Controls.Add(this.groupBoxStyle);
			this.DefaultFloatSize = new System.Drawing.Size(272, 405);
			this.DockAreas = ((ARCed.UI.DockAreas)((ARCed.UI.DockAreas.DockLeft | ARCed.UI.DockAreas.DockRight)));
			this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.SizableToolWindow;
			this.Name = "ScriptStyleForm";
			this.ShowHint = ARCed.UI.DockState.DockRight;
			this.Text = "Syntax Styling";
			this.groupBoxStyle.ResumeLayout(false);
			this.groupBoxColors.ResumeLayout(false);
			this.splitContainer1.Panel1.ResumeLayout(false);
			this.splitContainer1.Panel1.PerformLayout();
			this.splitContainer1.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).EndInit();
			this.splitContainer1.ResumeLayout(false);
			this.splitContainer2.Panel1.ResumeLayout(false);
			this.splitContainer2.Panel1.PerformLayout();
			this.splitContainer2.Panel2.ResumeLayout(false);
			this.splitContainer2.Panel2.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainer2)).EndInit();
			this.splitContainer2.ResumeLayout(false);
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.GroupBox groupBoxStyle;
		private System.Windows.Forms.ListBox listBoxStyles;
		private System.Windows.Forms.GroupBox groupBoxColors;
		private System.Windows.Forms.SplitContainer splitContainer1;
		private System.Windows.Forms.Label labelColorFore;
		private System.Windows.Forms.Panel panelColorFore;
		private System.Windows.Forms.Label labelBackColor;
		private System.Windows.Forms.Panel panelColorBack;
		private System.Windows.Forms.Button buttonDefault;
		private System.Windows.Forms.Panel panelCaretColor;
		private System.Windows.Forms.Label labelCaret;
		private System.Windows.Forms.ToolTip toolTip;
		private System.Windows.Forms.SplitContainer splitContainer2;
		private Controls.FontSelector fontSelector;
	}
}