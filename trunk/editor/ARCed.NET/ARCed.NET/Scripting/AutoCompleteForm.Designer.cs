namespace ARCed.Scripting
{
	partial class AutoCompleteForm
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
			this.listBoxWords = new System.Windows.Forms.ListBox();
			this.contextMenuStrip = new System.Windows.Forms.ContextMenuStrip(this.components);
			this.removeSelectedToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.textBoxWords = new System.Windows.Forms.TextBox();
			this.labelAuto1 = new System.Windows.Forms.Label();
			this.numericAutoLength = new System.Windows.Forms.NumericUpDown();
			this.labelAuto2 = new System.Windows.Forms.Label();
			this.buttonAdd = new System.Windows.Forms.Button();
			this.buttonClear = new System.Windows.Forms.Button();
			this.splitContainerWords = new System.Windows.Forms.SplitContainer();
			this.toolTip = new System.Windows.Forms.ToolTip(this.components);
			this.textBoxFillUp = new System.Windows.Forms.TextBox();
			this.buttonPaste = new System.Windows.Forms.Button();
			this.labelFillUp = new System.Windows.Forms.Label();
			this.contextMenuStrip.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.numericAutoLength)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerWords)).BeginInit();
			this.splitContainerWords.Panel1.SuspendLayout();
			this.splitContainerWords.Panel2.SuspendLayout();
			this.splitContainerWords.SuspendLayout();
			this.SuspendLayout();
			// 
			// listBoxWords
			// 
			this.listBoxWords.ContextMenuStrip = this.contextMenuStrip;
			this.listBoxWords.Dock = System.Windows.Forms.DockStyle.Fill;
			this.listBoxWords.FormattingEnabled = true;
			this.listBoxWords.IntegralHeight = false;
			this.listBoxWords.Location = new System.Drawing.Point(0, 0);
			this.listBoxWords.Name = "listBoxWords";
			this.listBoxWords.SelectionMode = System.Windows.Forms.SelectionMode.MultiExtended;
			this.listBoxWords.Size = new System.Drawing.Size(207, 199);
			this.listBoxWords.Sorted = true;
			this.listBoxWords.TabIndex = 0;
			this.toolTip.SetToolTip(this.listBoxWords, "List of current words");
			this.listBoxWords.KeyDown += new System.Windows.Forms.KeyEventHandler(this.listBoxWords_KeyDown);
			// 
			// contextMenuStrip
			// 
			this.contextMenuStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.removeSelectedToolStripMenuItem});
			this.contextMenuStrip.Name = "contextMenuStrip";
			this.contextMenuStrip.Size = new System.Drawing.Size(165, 26);
			// 
			// removeSelectedToolStripMenuItem
			// 
			this.removeSelectedToolStripMenuItem.Name = "removeSelectedToolStripMenuItem";
			this.removeSelectedToolStripMenuItem.Size = new System.Drawing.Size(164, 22);
			this.removeSelectedToolStripMenuItem.Text = "Remove Selected";
			this.removeSelectedToolStripMenuItem.Click += new System.EventHandler(this.removeSelectedToolStripMenuItem_Click);
			// 
			// textBoxWords
			// 
			this.textBoxWords.Dock = System.Windows.Forms.DockStyle.Fill;
			this.textBoxWords.Location = new System.Drawing.Point(0, 0);
			this.textBoxWords.Multiline = true;
			this.textBoxWords.Name = "textBoxWords";
			this.textBoxWords.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
			this.textBoxWords.Size = new System.Drawing.Size(414, 199);
			this.textBoxWords.TabIndex = 1;
			this.toolTip.SetToolTip(this.textBoxWords, "Type/paste words here to add to control");
			// 
			// labelAuto1
			// 
			this.labelAuto1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.labelAuto1.AutoSize = true;
			this.labelAuto1.Location = new System.Drawing.Point(12, 222);
			this.labelAuto1.Name = "labelAuto1";
			this.labelAuto1.Size = new System.Drawing.Size(58, 13);
			this.labelAuto1.TabIndex = 5;
			this.labelAuto1.Text = "Begin after";
			// 
			// numericAutoLength
			// 
			this.numericAutoLength.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.numericAutoLength.Location = new System.Drawing.Point(76, 220);
			this.numericAutoLength.Maximum = new decimal(new int[] {
            10,
            0,
            0,
            0});
			this.numericAutoLength.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
			this.numericAutoLength.Name = "numericAutoLength";
			this.numericAutoLength.Size = new System.Drawing.Size(35, 20);
			this.numericAutoLength.TabIndex = 6;
			this.toolTip.SetToolTip(this.numericAutoLength, "Number of characters needed to enable autocomplate");
			this.numericAutoLength.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
			this.numericAutoLength.ValueChanged += new System.EventHandler(this.numericAutoLength_ValueChanged);
			// 
			// labelAuto2
			// 
			this.labelAuto2.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.labelAuto2.AutoSize = true;
			this.labelAuto2.Location = new System.Drawing.Point(117, 222);
			this.labelAuto2.Name = "labelAuto2";
			this.labelAuto2.Size = new System.Drawing.Size(60, 13);
			this.labelAuto2.TabIndex = 7;
			this.labelAuto2.Text = "characters.";
			// 
			// buttonAdd
			// 
			this.buttonAdd.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonAdd.Image = global::ARCed.Properties.Resources.Add;
			this.buttonAdd.Location = new System.Drawing.Point(583, 215);
			this.buttonAdd.Name = "buttonAdd";
			this.buttonAdd.Size = new System.Drawing.Size(24, 24);
			this.buttonAdd.TabIndex = 8;
			this.toolTip.SetToolTip(this.buttonAdd, "Parses and adds the words to the word list");
			this.buttonAdd.UseVisualStyleBackColor = true;
			this.buttonAdd.Click += new System.EventHandler(this.buttonAdd_Click);
			// 
			// buttonClear
			// 
			this.buttonClear.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonClear.Image = global::ARCed.Properties.Resources.Delete;
			this.buttonClear.Location = new System.Drawing.Point(613, 215);
			this.buttonClear.Name = "buttonClear";
			this.buttonClear.Size = new System.Drawing.Size(24, 24);
			this.buttonClear.TabIndex = 9;
			this.toolTip.SetToolTip(this.buttonClear, "Clears the text box");
			this.buttonClear.UseVisualStyleBackColor = true;
			this.buttonClear.Click += new System.EventHandler(this.buttonClear_Click);
			// 
			// splitContainerWords
			// 
			this.splitContainerWords.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.splitContainerWords.Location = new System.Drawing.Point(12, 12);
			this.splitContainerWords.Name = "splitContainerWords";
			// 
			// splitContainerWords.Panel1
			// 
			this.splitContainerWords.Panel1.Controls.Add(this.listBoxWords);
			// 
			// splitContainerWords.Panel2
			// 
			this.splitContainerWords.Panel2.Controls.Add(this.textBoxWords);
			this.splitContainerWords.Size = new System.Drawing.Size(625, 199);
			this.splitContainerWords.SplitterDistance = 207;
			this.splitContainerWords.TabIndex = 10;
			// 
			// textBoxFillUp
			// 
			this.textBoxFillUp.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.textBoxFillUp.Location = new System.Drawing.Point(317, 219);
			this.textBoxFillUp.Name = "textBoxFillUp";
			this.textBoxFillUp.Size = new System.Drawing.Size(117, 20);
			this.textBoxFillUp.TabIndex = 12;
			this.toolTip.SetToolTip(this.textBoxFillUp, "Characters that will drop an autocomplete word when pressed");
			this.textBoxFillUp.TextChanged += new System.EventHandler(this.textBoxFillUp_TextChanged);
			// 
			// buttonPaste
			// 
			this.buttonPaste.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonPaste.Image = global::ARCed.Properties.Resources.Paste;
			this.buttonPaste.Location = new System.Drawing.Point(553, 215);
			this.buttonPaste.Name = "buttonPaste";
			this.buttonPaste.Size = new System.Drawing.Size(24, 24);
			this.buttonPaste.TabIndex = 13;
			this.toolTip.SetToolTip(this.buttonPaste, "Paste clipboard contents");
			this.buttonPaste.UseVisualStyleBackColor = true;
			this.buttonPaste.Click += new System.EventHandler(this.buttonPaste_Click);
			// 
			// labelFillUp
			// 
			this.labelFillUp.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.labelFillUp.AutoSize = true;
			this.labelFillUp.Location = new System.Drawing.Point(220, 222);
			this.labelFillUp.Name = "labelFillUp";
			this.labelFillUp.Size = new System.Drawing.Size(91, 13);
			this.labelFillUp.TabIndex = 11;
			this.labelFillUp.Text = "Fill-up Characters:";
			// 
			// AutoCompleteForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(649, 249);
			this.Controls.Add(this.buttonPaste);
			this.Controls.Add(this.textBoxFillUp);
			this.Controls.Add(this.labelFillUp);
			this.Controls.Add(this.splitContainerWords);
			this.Controls.Add(this.buttonClear);
			this.Controls.Add(this.buttonAdd);
			this.Controls.Add(this.labelAuto1);
			this.Controls.Add(this.numericAutoLength);
			this.Controls.Add(this.labelAuto2);
			this.DefaultFloatSize = new System.Drawing.Size(640, 288);
			this.DockAreas = ((ARCed.UI.DockAreas)((((ARCed.UI.DockAreas.Float | ARCed.UI.DockAreas.DockTop)
						| ARCed.UI.DockAreas.DockBottom)
						| ARCed.UI.DockAreas.Document)));
			this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.Name = "AutoCompleteForm";
			this.ShowHint = ARCed.UI.DockState.DockBottom;
			this.Text = "Auto-Complete Settings";
			this.contextMenuStrip.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.numericAutoLength)).EndInit();
			this.splitContainerWords.Panel1.ResumeLayout(false);
			this.splitContainerWords.Panel2.ResumeLayout(false);
			this.splitContainerWords.Panel2.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerWords)).EndInit();
			this.splitContainerWords.ResumeLayout(false);
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.ListBox listBoxWords;
		private System.Windows.Forms.TextBox textBoxWords;
		private System.Windows.Forms.Label labelAuto1;
		private System.Windows.Forms.NumericUpDown numericAutoLength;
		private System.Windows.Forms.Label labelAuto2;
		private System.Windows.Forms.Button buttonAdd;
		private System.Windows.Forms.Button buttonClear;
		private System.Windows.Forms.SplitContainer splitContainerWords;
		private System.Windows.Forms.ContextMenuStrip contextMenuStrip;
		private System.Windows.Forms.ToolStripMenuItem removeSelectedToolStripMenuItem;
		private System.Windows.Forms.ToolTip toolTip;
		private System.Windows.Forms.Label labelFillUp;
		private System.Windows.Forms.TextBox textBoxFillUp;
		private System.Windows.Forms.Button buttonPaste;
	}
}