namespace ARCed.Controls
{
	partial class NoteTextBox
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

		#region Component Designer generated code

		/// <summary> 
		/// Required method for Designer support - do not modify 
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
			this.components = new System.ComponentModel.Container();
			this.textBoxNotes = new System.Windows.Forms.TextBox();
			this.contextMenuNotes = new System.Windows.Forms.ContextMenuStrip(this.components);
			this.buttonCut = new System.Windows.Forms.ToolStripMenuItem();
			this.buttonCopy = new System.Windows.Forms.ToolStripMenuItem();
			this.buttonPaste = new System.Windows.Forms.ToolStripMenuItem();
			this.buttonSelectAll = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripSeparator2 = new System.Windows.Forms.ToolStripSeparator();
			this.buttonFont = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
			this.buttonEditor = new System.Windows.Forms.ToolStripMenuItem();
			this.groupBoxNotes = new System.Windows.Forms.GroupBox();
			this.contextMenuNotes.SuspendLayout();
			this.groupBoxNotes.SuspendLayout();
			this.SuspendLayout();
			// 
			// textBoxNotes
			// 
			this.textBoxNotes.AcceptsReturn = true;
			this.textBoxNotes.AcceptsTab = true;
			this.textBoxNotes.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBoxNotes.ContextMenuStrip = this.contextMenuNotes;
			this.textBoxNotes.Location = new System.Drawing.Point(6, 19);
			this.textBoxNotes.Multiline = true;
			this.textBoxNotes.Name = "textBoxNotes";
			this.textBoxNotes.Size = new System.Drawing.Size(246, 204);
			this.textBoxNotes.TabIndex = 0;
			this.textBoxNotes.WordWrap = false;
			this.textBoxNotes.ClientSizeChanged += new System.EventHandler(this.textBoxNotes_ClientSizeChanged);
			this.textBoxNotes.TextChanged += new System.EventHandler(this.textBoxNotes_ClientSizeChanged);
			this.textBoxNotes.DoubleClick += new System.EventHandler(this.buttonEditor_Click);
			// 
			// contextMenuNotes
			// 
			this.contextMenuNotes.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.buttonCut,
            this.buttonCopy,
            this.buttonPaste,
            this.buttonSelectAll,
            this.toolStripSeparator2,
            this.buttonFont,
            this.toolStripSeparator1,
            this.buttonEditor});
			this.contextMenuNotes.Name = "contextMenuNotes";
			this.contextMenuNotes.Size = new System.Drawing.Size(165, 148);
			// 
			// buttonCut
			// 
			this.buttonCut.Image = global::ARCed.Properties.Resources.Cut;
			this.buttonCut.Name = "buttonCut";
			this.buttonCut.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.X)));
			this.buttonCut.Size = new System.Drawing.Size(164, 22);
			this.buttonCut.Text = "Cut";
			this.buttonCut.Click += new System.EventHandler(this.buttonCut_Click);
			// 
			// buttonCopy
			// 
			this.buttonCopy.Image = global::ARCed.Properties.Resources.Copy;
			this.buttonCopy.Name = "buttonCopy";
			this.buttonCopy.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.C)));
			this.buttonCopy.Size = new System.Drawing.Size(164, 22);
			this.buttonCopy.Text = "Copy";
			this.buttonCopy.Click += new System.EventHandler(this.buttonCopy_Click);
			// 
			// buttonPaste
			// 
			this.buttonPaste.Image = global::ARCed.Properties.Resources.Paste;
			this.buttonPaste.Name = "buttonPaste";
			this.buttonPaste.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.V)));
			this.buttonPaste.Size = new System.Drawing.Size(164, 22);
			this.buttonPaste.Text = "Paste";
			this.buttonPaste.Click += new System.EventHandler(this.buttonPaste_Click);
			// 
			// buttonSelectAll
			// 
			this.buttonSelectAll.Image = global::ARCed.Properties.Resources.SelectAll;
			this.buttonSelectAll.Name = "buttonSelectAll";
			this.buttonSelectAll.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.A)));
			this.buttonSelectAll.Size = new System.Drawing.Size(164, 22);
			this.buttonSelectAll.Text = "Select All";
			this.buttonSelectAll.Click += new System.EventHandler(this.buttonSelectAll_Click);
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
			// toolStripSeparator1
			// 
			this.toolStripSeparator1.Name = "toolStripSeparator1";
			this.toolStripSeparator1.Size = new System.Drawing.Size(161, 6);
			// 
			// buttonEditor
			// 
			this.buttonEditor.Image = global::ARCed.Properties.Resources.NoteText;
			this.buttonEditor.Name = "buttonEditor";
			this.buttonEditor.Size = new System.Drawing.Size(164, 22);
			this.buttonEditor.Text = "Full Editor...";
			this.buttonEditor.ToolTipText = "Open the full editor";
			this.buttonEditor.Click += new System.EventHandler(this.buttonEditor_Click);
			// 
			// groupBoxNotes
			// 
			this.groupBoxNotes.Controls.Add(this.textBoxNotes);
			this.groupBoxNotes.Dock = System.Windows.Forms.DockStyle.Fill;
			this.groupBoxNotes.Location = new System.Drawing.Point(0, 0);
			this.groupBoxNotes.Name = "groupBoxNotes";
			this.groupBoxNotes.Size = new System.Drawing.Size(258, 229);
			this.groupBoxNotes.TabIndex = 1;
			this.groupBoxNotes.TabStop = false;
			this.groupBoxNotes.Text = "Notes";
			// 
			// NoteTextBox
			// 
			this.Controls.Add(this.groupBoxNotes);
			this.Name = "NoteTextBox";
			this.Size = new System.Drawing.Size(258, 229);
			this.Load += new System.EventHandler(this.NoteTextBox_Load);
			this.contextMenuNotes.ResumeLayout(false);
			this.groupBoxNotes.ResumeLayout(false);
			this.groupBoxNotes.PerformLayout();
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.TextBox textBoxNotes;
		private System.Windows.Forms.ContextMenuStrip contextMenuNotes;
		private System.Windows.Forms.ToolStripMenuItem buttonFont;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator1;
		private System.Windows.Forms.ToolStripMenuItem buttonEditor;
		private System.Windows.Forms.ToolStripMenuItem buttonCut;
		private System.Windows.Forms.ToolStripMenuItem buttonCopy;
		private System.Windows.Forms.ToolStripMenuItem buttonPaste;
		private System.Windows.Forms.ToolStripMenuItem buttonSelectAll;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator2;
		private System.Windows.Forms.GroupBox groupBoxNotes;
	}
}
