namespace ARCed.Dialogs
{
	partial class NoteForm
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
			this.buttonCancel = new System.Windows.Forms.Button();
			this.buttonOK = new System.Windows.Forms.Button();
			this.buttonCopy = new System.Windows.Forms.Button();
			this.buttonPaste = new System.Windows.Forms.Button();
			this.textBoxNotes = new System.Windows.Forms.TextBox();
			this.contextMenuNotes = new System.Windows.Forms.ContextMenuStrip(this.components);
			this.buttonCutContext = new System.Windows.Forms.ToolStripMenuItem();
			this.buttonCopyContext = new System.Windows.Forms.ToolStripMenuItem();
			this.buttonPasteContext = new System.Windows.Forms.ToolStripMenuItem();
			this.buttonSelectAllContext = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripSeparator2 = new System.Windows.Forms.ToolStripSeparator();
			this.buttonFont = new System.Windows.Forms.ToolStripMenuItem();
			this.buttonSelectAll = new System.Windows.Forms.Button();
			this.buttonCut = new System.Windows.Forms.Button();
			this.contextMenuNotes.SuspendLayout();
			this.SuspendLayout();
			// 
			// buttonCancel
			// 
			this.buttonCancel.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
			this.buttonCancel.Location = new System.Drawing.Point(366, 334);
			this.buttonCancel.Name = "buttonCancel";
			this.buttonCancel.Size = new System.Drawing.Size(75, 23);
			this.buttonCancel.TabIndex = 0;
			this.buttonCancel.Text = "Cancel";
			this.buttonCancel.UseVisualStyleBackColor = true;
			// 
			// buttonOK
			// 
			this.buttonOK.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonOK.Location = new System.Drawing.Point(285, 334);
			this.buttonOK.Name = "buttonOK";
			this.buttonOK.Size = new System.Drawing.Size(75, 23);
			this.buttonOK.TabIndex = 1;
			this.buttonOK.Text = "OK";
			this.buttonOK.UseVisualStyleBackColor = true;
			this.buttonOK.Click += new System.EventHandler(this.buttonOK_Click);
			// 
			// buttonCopy
			// 
			this.buttonCopy.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.buttonCopy.Image = global::ARCed.Properties.Resources.Copy;
			this.buttonCopy.Location = new System.Drawing.Point(41, 334);
			this.buttonCopy.Name = "buttonCopy";
			this.buttonCopy.Size = new System.Drawing.Size(23, 23);
			this.buttonCopy.TabIndex = 2;
			this.buttonCopy.UseVisualStyleBackColor = true;
			this.buttonCopy.Click += new System.EventHandler(this.buttonCopy_Click);
			// 
			// buttonPaste
			// 
			this.buttonPaste.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.buttonPaste.Image = global::ARCed.Properties.Resources.Paste;
			this.buttonPaste.Location = new System.Drawing.Point(70, 334);
			this.buttonPaste.Name = "buttonPaste";
			this.buttonPaste.Size = new System.Drawing.Size(23, 23);
			this.buttonPaste.TabIndex = 3;
			this.buttonPaste.UseVisualStyleBackColor = true;
			this.buttonPaste.Click += new System.EventHandler(this.buttonPaste_Click);
			// 
			// textBoxNotes
			// 
			this.textBoxNotes.AcceptsReturn = true;
			this.textBoxNotes.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBoxNotes.ContextMenuStrip = this.contextMenuNotes;
			this.textBoxNotes.Location = new System.Drawing.Point(12, 12);
			this.textBoxNotes.Multiline = true;
			this.textBoxNotes.Name = "textBoxNotes";
			this.textBoxNotes.Size = new System.Drawing.Size(429, 316);
			this.textBoxNotes.TabIndex = 4;
			// 
			// contextMenuNotes
			// 
			this.contextMenuNotes.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.buttonCutContext,
            this.buttonCopyContext,
            this.buttonPasteContext,
            this.buttonSelectAllContext,
            this.toolStripSeparator2,
            this.buttonFont});
			this.contextMenuNotes.Name = "contextMenuNotes";
			this.contextMenuNotes.Size = new System.Drawing.Size(165, 142);
			// 
			// buttonCutContext
			// 
			this.buttonCutContext.Image = global::ARCed.Properties.Resources.Cut;
			this.buttonCutContext.Name = "buttonCutContext";
			this.buttonCutContext.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.X)));
			this.buttonCutContext.Size = new System.Drawing.Size(164, 22);
			this.buttonCutContext.Text = "Cut";
			this.buttonCutContext.Click += new System.EventHandler(this.buttonCut_Click);
			// 
			// buttonCopyContext
			// 
			this.buttonCopyContext.Image = global::ARCed.Properties.Resources.Copy;
			this.buttonCopyContext.Name = "buttonCopyContext";
			this.buttonCopyContext.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.C)));
			this.buttonCopyContext.Size = new System.Drawing.Size(164, 22);
			this.buttonCopyContext.Text = "Copy";
			this.buttonCopyContext.Click += new System.EventHandler(this.buttonCopy_Click);
			// 
			// buttonPasteContext
			// 
			this.buttonPasteContext.Image = global::ARCed.Properties.Resources.Paste;
			this.buttonPasteContext.Name = "buttonPasteContext";
			this.buttonPasteContext.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.V)));
			this.buttonPasteContext.Size = new System.Drawing.Size(164, 22);
			this.buttonPasteContext.Text = "Paste";
			this.buttonPasteContext.Click += new System.EventHandler(this.buttonPaste_Click);
			// 
			// buttonSelectAllContext
			// 
			this.buttonSelectAllContext.Image = global::ARCed.Properties.Resources.SelectAll;
			this.buttonSelectAllContext.Name = "buttonSelectAllContext";
			this.buttonSelectAllContext.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.A)));
			this.buttonSelectAllContext.Size = new System.Drawing.Size(164, 22);
			this.buttonSelectAllContext.Text = "Select All";
			this.buttonSelectAllContext.Click += new System.EventHandler(this.buttonSelectAll_Click);
			// 
			// toolStripSeparator2
			// 
			this.toolStripSeparator2.Name = "toolStripSeparator2";
			this.toolStripSeparator2.Size = new System.Drawing.Size(161, 6);
			// 
			// buttonFont
			// 
			this.buttonFont.Image = global::ARCed.Properties.Resources.Font;
			this.buttonFont.Name = "buttonFont";
			this.buttonFont.Size = new System.Drawing.Size(164, 22);
			this.buttonFont.Text = "Font...";
			this.buttonFont.ToolTipText = "Select the font of the textbox";
			this.buttonFont.Click += new System.EventHandler(this.buttonFont_Click);
			// 
			// buttonSelectAll
			// 
			this.buttonSelectAll.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.buttonSelectAll.Image = global::ARCed.Properties.Resources.SelectAll;
			this.buttonSelectAll.Location = new System.Drawing.Point(99, 334);
			this.buttonSelectAll.Name = "buttonSelectAll";
			this.buttonSelectAll.Size = new System.Drawing.Size(23, 23);
			this.buttonSelectAll.TabIndex = 5;
			this.buttonSelectAll.UseVisualStyleBackColor = true;
			this.buttonSelectAll.Click += new System.EventHandler(this.buttonSelectAll_Click);
			// 
			// buttonCut
			// 
			this.buttonCut.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.buttonCut.Image = global::ARCed.Properties.Resources.Cut;
			this.buttonCut.Location = new System.Drawing.Point(12, 334);
			this.buttonCut.Name = "buttonCut";
			this.buttonCut.Size = new System.Drawing.Size(23, 23);
			this.buttonCut.TabIndex = 7;
			this.buttonCut.UseVisualStyleBackColor = true;
			this.buttonCut.Click += new System.EventHandler(this.buttonCut_Click);
			// 
			// NoteForm
			// 
			this.AcceptButton = this.buttonOK;
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.CancelButton = this.buttonCancel;
			this.ClientSize = new System.Drawing.Size(453, 369);
			this.Controls.Add(this.textBoxNotes);
			this.Controls.Add(this.buttonOK);
			this.Controls.Add(this.buttonSelectAll);
			this.Controls.Add(this.buttonCut);
			this.Controls.Add(this.buttonCancel);
			this.Controls.Add(this.buttonPaste);
			this.Controls.Add(this.buttonCopy);
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.SizableToolWindow;
			this.Name = "NoteForm";
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
			this.Text = "Edit Note";
			this.contextMenuNotes.ResumeLayout(false);
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Button buttonCancel;
		private System.Windows.Forms.Button buttonOK;
		private System.Windows.Forms.Button buttonCopy;
		private System.Windows.Forms.Button buttonPaste;
		private System.Windows.Forms.TextBox textBoxNotes;
		private System.Windows.Forms.Button buttonSelectAll;
		private System.Windows.Forms.ContextMenuStrip contextMenuNotes;
		private System.Windows.Forms.ToolStripMenuItem buttonCutContext;
		private System.Windows.Forms.ToolStripMenuItem buttonCopyContext;
		private System.Windows.Forms.ToolStripMenuItem buttonPasteContext;
		private System.Windows.Forms.ToolStripMenuItem buttonSelectAllContext;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator2;
		private System.Windows.Forms.ToolStripMenuItem buttonFont;
		private System.Windows.Forms.Button buttonCut;
	}
}