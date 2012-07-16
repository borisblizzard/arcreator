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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(NoteForm));
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
            resources.ApplyResources(this.buttonCancel, "buttonCancel");
            this.buttonCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
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
            // buttonCopy
            // 
            resources.ApplyResources(this.buttonCopy, "buttonCopy");
            this.buttonCopy.Image = global::ARCed.Properties.Resources.Copy;
            this.buttonCopy.Name = "buttonCopy";
            this.buttonCopy.UseVisualStyleBackColor = true;
            this.buttonCopy.Click += new System.EventHandler(this.buttonCopy_Click);
            // 
            // buttonPaste
            // 
            resources.ApplyResources(this.buttonPaste, "buttonPaste");
            this.buttonPaste.Image = global::ARCed.Properties.Resources.Paste;
            this.buttonPaste.Name = "buttonPaste";
            this.buttonPaste.UseVisualStyleBackColor = true;
            this.buttonPaste.Click += new System.EventHandler(this.buttonPaste_Click);
            // 
            // textBoxNotes
            // 
            this.textBoxNotes.AcceptsReturn = true;
            resources.ApplyResources(this.textBoxNotes, "textBoxNotes");
            this.textBoxNotes.ContextMenuStrip = this.contextMenuNotes;
            this.textBoxNotes.Name = "textBoxNotes";
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
            resources.ApplyResources(this.contextMenuNotes, "contextMenuNotes");
            // 
            // buttonCutContext
            // 
            this.buttonCutContext.Image = global::ARCed.Properties.Resources.Cut;
            this.buttonCutContext.Name = "buttonCutContext";
            resources.ApplyResources(this.buttonCutContext, "buttonCutContext");
            this.buttonCutContext.Click += new System.EventHandler(this.buttonCut_Click);
            // 
            // buttonCopyContext
            // 
            this.buttonCopyContext.Image = global::ARCed.Properties.Resources.Copy;
            this.buttonCopyContext.Name = "buttonCopyContext";
            resources.ApplyResources(this.buttonCopyContext, "buttonCopyContext");
            this.buttonCopyContext.Click += new System.EventHandler(this.buttonCopy_Click);
            // 
            // buttonPasteContext
            // 
            this.buttonPasteContext.Image = global::ARCed.Properties.Resources.Paste;
            this.buttonPasteContext.Name = "buttonPasteContext";
            resources.ApplyResources(this.buttonPasteContext, "buttonPasteContext");
            this.buttonPasteContext.Click += new System.EventHandler(this.buttonPaste_Click);
            // 
            // buttonSelectAllContext
            // 
            this.buttonSelectAllContext.Image = global::ARCed.Properties.Resources.SelectAll;
            this.buttonSelectAllContext.Name = "buttonSelectAllContext";
            resources.ApplyResources(this.buttonSelectAllContext, "buttonSelectAllContext");
            this.buttonSelectAllContext.Click += new System.EventHandler(this.buttonSelectAll_Click);
            // 
            // toolStripSeparator2
            // 
            this.toolStripSeparator2.Name = "toolStripSeparator2";
            resources.ApplyResources(this.toolStripSeparator2, "toolStripSeparator2");
            // 
            // buttonFont
            // 
            this.buttonFont.Image = global::ARCed.Properties.Resources.Font;
            this.buttonFont.Name = "buttonFont";
            resources.ApplyResources(this.buttonFont, "buttonFont");
            this.buttonFont.Click += new System.EventHandler(this.buttonFont_Click);
            // 
            // buttonSelectAll
            // 
            resources.ApplyResources(this.buttonSelectAll, "buttonSelectAll");
            this.buttonSelectAll.Image = global::ARCed.Properties.Resources.SelectAll;
            this.buttonSelectAll.Name = "buttonSelectAll";
            this.buttonSelectAll.UseVisualStyleBackColor = true;
            this.buttonSelectAll.Click += new System.EventHandler(this.buttonSelectAll_Click);
            // 
            // buttonCut
            // 
            resources.ApplyResources(this.buttonCut, "buttonCut");
            this.buttonCut.Image = global::ARCed.Properties.Resources.Cut;
            this.buttonCut.Name = "buttonCut";
            this.buttonCut.UseVisualStyleBackColor = true;
            this.buttonCut.Click += new System.EventHandler(this.buttonCut_Click);
            // 
            // NoteForm
            // 
            this.AcceptButton = this.buttonOK;
            resources.ApplyResources(this, "$this");
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.CancelButton = this.buttonCancel;
            this.Controls.Add(this.textBoxNotes);
            this.Controls.Add(this.buttonOK);
            this.Controls.Add(this.buttonSelectAll);
            this.Controls.Add(this.buttonCut);
            this.Controls.Add(this.buttonCancel);
            this.Controls.Add(this.buttonPaste);
            this.Controls.Add(this.buttonCopy);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.SizableToolWindow;
            this.Name = "NoteForm";
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