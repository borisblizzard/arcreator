namespace ARCed.Scripting
{
	partial class ScriptEditorForm
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
			this.toolStrip = new System.Windows.Forms.ToolStrip();
			this.cutToolStripButton = new System.Windows.Forms.ToolStripButton();
			this.copyToolStripButton = new System.Windows.Forms.ToolStripButton();
			this.pasteToolStripButton = new System.Windows.Forms.ToolStripButton();
			this.toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
			this.buttonStyle = new System.Windows.Forms.ToolStripButton();
			this.buttonAutoComplete = new System.Windows.Forms.ToolStripButton();
			this.toolStripSeparator2 = new System.Windows.Forms.ToolStripSeparator();
			this.buttonToggleAutoComplete = new System.Windows.Forms.ToolStripButton();
			this.buttonToggleAutoIndent = new System.Windows.Forms.ToolStripButton();
			this.buttonToggleIndentGuides = new System.Windows.Forms.ToolStripButton();
			this.buttonToggleFolding = new System.Windows.Forms.ToolStripButton();
			this.buttonToggleCaret = new System.Windows.Forms.ToolStripButton();
			this.buttonScriptStructure = new System.Windows.Forms.ToolStripButton();
			this.toolStripSeparator3 = new System.Windows.Forms.ToolStripSeparator();
			this.buttonCharMap = new System.Windows.Forms.ToolStripButton();
			this.buttonCalc = new System.Windows.Forms.ToolStripButton();
			this.contextMenu = new System.Windows.Forms.ContextMenuStrip(this.components);
			this.undoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.redoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripSeparator6 = new System.Windows.Forms.ToolStripSeparator();
			this.cutToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.copyToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.pasteToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.deleteToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.selectAllToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripSeparator5 = new System.Windows.Forms.ToolStripSeparator();
			this.incrementalSearchToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.findToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.findNextToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.findPreviousToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.replaceToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.gotoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripSeparator4 = new System.Windows.Forms.ToolStripSeparator();
			this.addToAutoCompleteToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.formatToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.commentToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.structureScriptToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.removeEmptyLinesToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this._scintilla = new ARCed.Scintilla.Scintilla();
			this.toolStrip.SuspendLayout();
			this.contextMenu.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this._scintilla)).BeginInit();
			this.SuspendLayout();
			// 
			// toolStrip
			// 
			this.toolStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.cutToolStripButton,
            this.copyToolStripButton,
            this.pasteToolStripButton,
            this.toolStripSeparator1,
            this.buttonStyle,
            this.buttonAutoComplete,
            this.toolStripSeparator2,
            this.buttonToggleAutoComplete,
            this.buttonToggleAutoIndent,
            this.buttonToggleIndentGuides,
            this.buttonToggleFolding,
            this.buttonToggleCaret,
            this.buttonScriptStructure,
            this.toolStripSeparator3,
            this.buttonCharMap,
            this.buttonCalc});
			this.toolStrip.Location = new System.Drawing.Point(0, 0);
			this.toolStrip.Name = "toolStrip";
			this.toolStrip.Size = new System.Drawing.Size(624, 25);
			this.toolStrip.TabIndex = 0;
			this.toolStrip.Text = "toolStrip1";
			// 
			// cutToolStripButton
			// 
			this.cutToolStripButton.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			this.cutToolStripButton.Image = global::ARCed.Properties.Resources.Cut;
			this.cutToolStripButton.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.cutToolStripButton.Name = "cutToolStripButton";
			this.cutToolStripButton.Size = new System.Drawing.Size(23, 22);
			this.cutToolStripButton.Text = "C&ut";
			this.cutToolStripButton.Click += new System.EventHandler(this.buttonCut_Click);
			// 
			// copyToolStripButton
			// 
			this.copyToolStripButton.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			this.copyToolStripButton.Image = global::ARCed.Properties.Resources.Copy;
			this.copyToolStripButton.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.copyToolStripButton.Name = "copyToolStripButton";
			this.copyToolStripButton.Size = new System.Drawing.Size(23, 22);
			this.copyToolStripButton.Text = "&Copy";
			this.copyToolStripButton.Click += new System.EventHandler(this.buttonCopy_Click);
			// 
			// pasteToolStripButton
			// 
			this.pasteToolStripButton.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			this.pasteToolStripButton.Image = global::ARCed.Properties.Resources.Paste;
			this.pasteToolStripButton.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.pasteToolStripButton.Name = "pasteToolStripButton";
			this.pasteToolStripButton.Size = new System.Drawing.Size(23, 22);
			this.pasteToolStripButton.Text = "&Paste";
			this.pasteToolStripButton.Click += new System.EventHandler(this.buttonPaste_Click);
			// 
			// toolStripSeparator1
			// 
			this.toolStripSeparator1.Name = "toolStripSeparator1";
			this.toolStripSeparator1.Size = new System.Drawing.Size(6, 25);
			// 
			// buttonStyle
			// 
			this.buttonStyle.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			this.buttonStyle.Image = global::ARCed.Properties.Resources.Theme;
			this.buttonStyle.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.buttonStyle.Name = "buttonStyle";
			this.buttonStyle.Size = new System.Drawing.Size(23, 22);
			this.buttonStyle.ToolTipText = "Configure syntax styling";
			this.buttonStyle.Click += new System.EventHandler(this.buttonStyle_Click);
			// 
			// buttonAutoComplete
			// 
			this.buttonAutoComplete.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			this.buttonAutoComplete.Image = global::ARCed.Properties.Resources.Settings;
			this.buttonAutoComplete.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.buttonAutoComplete.Name = "buttonAutoComplete";
			this.buttonAutoComplete.Size = new System.Drawing.Size(23, 22);
			this.buttonAutoComplete.ToolTipText = "Configure auto-complete settings";
			this.buttonAutoComplete.Click += new System.EventHandler(this.buttonAutoComplete_Click);
			// 
			// toolStripSeparator2
			// 
			this.toolStripSeparator2.Name = "toolStripSeparator2";
			this.toolStripSeparator2.Size = new System.Drawing.Size(6, 25);
			// 
			// buttonToggleAutoComplete
			// 
			this.buttonToggleAutoComplete.CheckOnClick = true;
			this.buttonToggleAutoComplete.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			this.buttonToggleAutoComplete.Image = global::ARCed.Properties.Resources.AutoComplete;
			this.buttonToggleAutoComplete.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.buttonToggleAutoComplete.Name = "buttonToggleAutoComplete";
			this.buttonToggleAutoComplete.Size = new System.Drawing.Size(23, 22);
			this.buttonToggleAutoComplete.ToolTipText = "Toggle auto-complete";
			this.buttonToggleAutoComplete.CheckedChanged += new System.EventHandler(this.buttonToggleAutoComplete_Click);
			// 
			// buttonToggleAutoIndent
			// 
			this.buttonToggleAutoIndent.CheckOnClick = true;
			this.buttonToggleAutoIndent.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			this.buttonToggleAutoIndent.Image = global::ARCed.Properties.Resources.Indent;
			this.buttonToggleAutoIndent.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.buttonToggleAutoIndent.Name = "buttonToggleAutoIndent";
			this.buttonToggleAutoIndent.Size = new System.Drawing.Size(23, 22);
			this.buttonToggleAutoIndent.ToolTipText = "Toggle auto-indent";
			this.buttonToggleAutoIndent.CheckedChanged += new System.EventHandler(this.buttonToggleAutoIndent_Click);
			// 
			// buttonToggleIndentGuides
			// 
			this.buttonToggleIndentGuides.CheckOnClick = true;
			this.buttonToggleIndentGuides.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			this.buttonToggleIndentGuides.Image = global::ARCed.Properties.Resources.Ruler;
			this.buttonToggleIndentGuides.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.buttonToggleIndentGuides.Name = "buttonToggleIndentGuides";
			this.buttonToggleIndentGuides.Size = new System.Drawing.Size(23, 22);
			this.buttonToggleIndentGuides.ToolTipText = "Toggle indent guide";
			this.buttonToggleIndentGuides.CheckedChanged += new System.EventHandler(this.buttonToggleIndentGuides_Click);
			// 
			// buttonToggleFolding
			// 
			this.buttonToggleFolding.CheckOnClick = true;
			this.buttonToggleFolding.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			this.buttonToggleFolding.Image = global::ARCed.Properties.Resources.FoldExpand;
			this.buttonToggleFolding.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.buttonToggleFolding.Name = "buttonToggleFolding";
			this.buttonToggleFolding.Size = new System.Drawing.Size(23, 22);
			this.buttonToggleFolding.ToolTipText = "Toggle code-folding";
			this.buttonToggleFolding.CheckedChanged += new System.EventHandler(this.buttonToggleFolding_Click);
			// 
			// buttonToggleCaret
			// 
			this.buttonToggleCaret.CheckOnClick = true;
			this.buttonToggleCaret.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			this.buttonToggleCaret.Image = global::ARCed.Properties.Resources.Highlight;
			this.buttonToggleCaret.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.buttonToggleCaret.Name = "buttonToggleCaret";
			this.buttonToggleCaret.Size = new System.Drawing.Size(23, 22);
			this.buttonToggleCaret.ToolTipText = "Toggle caret";
			this.buttonToggleCaret.CheckedChanged += new System.EventHandler(this.buttonToggleCaret_Click);
			// 
			// buttonScriptStructure
			// 
			this.buttonScriptStructure.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			this.buttonScriptStructure.Image = global::ARCed.Properties.Resources.Indent;
			this.buttonScriptStructure.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.buttonScriptStructure.Name = "buttonScriptStructure";
			this.buttonScriptStructure.Size = new System.Drawing.Size(23, 22);
			this.buttonScriptStructure.ToolTipText = "Automatically fix script indentation";
			this.buttonScriptStructure.Click += new System.EventHandler(this.buttonScriptStructure_Click);
			// 
			// toolStripSeparator3
			// 
			this.toolStripSeparator3.Name = "toolStripSeparator3";
			this.toolStripSeparator3.Size = new System.Drawing.Size(6, 25);
			// 
			// buttonCharMap
			// 
			this.buttonCharMap.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			this.buttonCharMap.Image = global::ARCed.Properties.Resources.CharMap;
			this.buttonCharMap.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.buttonCharMap.Name = "buttonCharMap";
			this.buttonCharMap.Size = new System.Drawing.Size(23, 22);
			this.buttonCharMap.ToolTipText = "Special characters";
			this.buttonCharMap.Click += new System.EventHandler(this.buttonCharMap_Click);
			// 
			// buttonCalc
			// 
			this.buttonCalc.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			this.buttonCalc.Image = global::ARCed.Properties.Resources.Calculator;
			this.buttonCalc.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.buttonCalc.Name = "buttonCalc";
			this.buttonCalc.Size = new System.Drawing.Size(23, 22);
			this.buttonCalc.ToolTipText = "Calculator";
			this.buttonCalc.Click += new System.EventHandler(this.buttonCalc_Click);
			// 
			// contextMenu
			// 
			this.contextMenu.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.undoToolStripMenuItem,
            this.redoToolStripMenuItem,
            this.toolStripSeparator6,
            this.cutToolStripMenuItem,
            this.copyToolStripMenuItem,
            this.pasteToolStripMenuItem,
            this.deleteToolStripMenuItem,
            this.selectAllToolStripMenuItem,
            this.toolStripSeparator5,
            this.incrementalSearchToolStripMenuItem,
            this.findToolStripMenuItem,
            this.findNextToolStripMenuItem,
            this.findPreviousToolStripMenuItem,
            this.replaceToolStripMenuItem,
            this.gotoToolStripMenuItem,
            this.toolStripSeparator4,
            this.addToAutoCompleteToolStripMenuItem,
            this.formatToolStripMenuItem});
			this.contextMenu.Name = "contextMenu";
			this.contextMenu.Size = new System.Drawing.Size(222, 352);
			this.contextMenu.Opening += new System.ComponentModel.CancelEventHandler(this.contextMenu_Opening);
			// 
			// undoToolStripMenuItem
			// 
			this.undoToolStripMenuItem.Image = global::ARCed.Properties.Resources.Undo;
			this.undoToolStripMenuItem.Name = "undoToolStripMenuItem";
			this.undoToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.Z)));
			this.undoToolStripMenuItem.Size = new System.Drawing.Size(221, 22);
			this.undoToolStripMenuItem.Text = "Undo";
			this.undoToolStripMenuItem.Click += new System.EventHandler(this.buttonUndo_Click);
			// 
			// redoToolStripMenuItem
			// 
			this.redoToolStripMenuItem.Image = global::ARCed.Properties.Resources.Redo;
			this.redoToolStripMenuItem.Name = "redoToolStripMenuItem";
			this.redoToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.Y)));
			this.redoToolStripMenuItem.Size = new System.Drawing.Size(221, 22);
			this.redoToolStripMenuItem.Text = "Redo";
			this.redoToolStripMenuItem.Click += new System.EventHandler(this.buttonRedo_Click);
			// 
			// toolStripSeparator6
			// 
			this.toolStripSeparator6.Name = "toolStripSeparator6";
			this.toolStripSeparator6.Size = new System.Drawing.Size(218, 6);
			// 
			// cutToolStripMenuItem
			// 
			this.cutToolStripMenuItem.Image = global::ARCed.Properties.Resources.Cut;
			this.cutToolStripMenuItem.Name = "cutToolStripMenuItem";
			this.cutToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.X)));
			this.cutToolStripMenuItem.Size = new System.Drawing.Size(221, 22);
			this.cutToolStripMenuItem.Text = "Cut";
			this.cutToolStripMenuItem.Click += new System.EventHandler(this.buttonCut_Click);
			// 
			// copyToolStripMenuItem
			// 
			this.copyToolStripMenuItem.Image = global::ARCed.Properties.Resources.Copy;
			this.copyToolStripMenuItem.Name = "copyToolStripMenuItem";
			this.copyToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.C)));
			this.copyToolStripMenuItem.Size = new System.Drawing.Size(221, 22);
			this.copyToolStripMenuItem.Text = "Copy";
			this.copyToolStripMenuItem.Click += new System.EventHandler(this.buttonCopy_Click);
			// 
			// pasteToolStripMenuItem
			// 
			this.pasteToolStripMenuItem.Image = global::ARCed.Properties.Resources.Paste;
			this.pasteToolStripMenuItem.Name = "pasteToolStripMenuItem";
			this.pasteToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.V)));
			this.pasteToolStripMenuItem.Size = new System.Drawing.Size(221, 22);
			this.pasteToolStripMenuItem.Text = "Paste";
			this.pasteToolStripMenuItem.Click += new System.EventHandler(this.buttonPaste_Click);
			// 
			// deleteToolStripMenuItem
			// 
			this.deleteToolStripMenuItem.Image = global::ARCed.Properties.Resources.Delete;
			this.deleteToolStripMenuItem.Name = "deleteToolStripMenuItem";
			this.deleteToolStripMenuItem.ShortcutKeys = System.Windows.Forms.Keys.Delete;
			this.deleteToolStripMenuItem.Size = new System.Drawing.Size(221, 22);
			this.deleteToolStripMenuItem.Text = "Delete";
			this.deleteToolStripMenuItem.Click += new System.EventHandler(this.buttonDelete_Click);
			// 
			// selectAllToolStripMenuItem
			// 
			this.selectAllToolStripMenuItem.Image = global::ARCed.Properties.Resources.SelectAll;
			this.selectAllToolStripMenuItem.Name = "selectAllToolStripMenuItem";
			this.selectAllToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.A)));
			this.selectAllToolStripMenuItem.Size = new System.Drawing.Size(221, 22);
			this.selectAllToolStripMenuItem.Text = "Select All";
			this.selectAllToolStripMenuItem.Click += new System.EventHandler(this.buttonSelectAll_Click);
			// 
			// toolStripSeparator5
			// 
			this.toolStripSeparator5.Name = "toolStripSeparator5";
			this.toolStripSeparator5.Size = new System.Drawing.Size(218, 6);
			// 
			// incrementalSearchToolStripMenuItem
			// 
			this.incrementalSearchToolStripMenuItem.Image = global::ARCed.Properties.Resources.Find2;
			this.incrementalSearchToolStripMenuItem.Name = "incrementalSearchToolStripMenuItem";
			this.incrementalSearchToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.I)));
			this.incrementalSearchToolStripMenuItem.Size = new System.Drawing.Size(221, 22);
			this.incrementalSearchToolStripMenuItem.Text = "Incremental Search...";
			this.incrementalSearchToolStripMenuItem.Click += new System.EventHandler(this.buttonIncrementalSearch_Click);
			// 
			// findToolStripMenuItem
			// 
			this.findToolStripMenuItem.Image = global::ARCed.Properties.Resources.Find1;
			this.findToolStripMenuItem.Name = "findToolStripMenuItem";
			this.findToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.F)));
			this.findToolStripMenuItem.Size = new System.Drawing.Size(221, 22);
			this.findToolStripMenuItem.Text = "Find...";
			this.findToolStripMenuItem.Click += new System.EventHandler(this.buttonFind_Click);
			// 
			// findNextToolStripMenuItem
			// 
			this.findNextToolStripMenuItem.Image = global::ARCed.Properties.Resources.Next;
			this.findNextToolStripMenuItem.Name = "findNextToolStripMenuItem";
			this.findNextToolStripMenuItem.ShortcutKeys = System.Windows.Forms.Keys.F3;
			this.findNextToolStripMenuItem.Size = new System.Drawing.Size(221, 22);
			this.findNextToolStripMenuItem.Text = "Find Next";
			this.findNextToolStripMenuItem.Click += new System.EventHandler(this.buttonFindNext_Click);
			// 
			// findPreviousToolStripMenuItem
			// 
			this.findPreviousToolStripMenuItem.Image = global::ARCed.Properties.Resources.Previous;
			this.findPreviousToolStripMenuItem.Name = "findPreviousToolStripMenuItem";
			this.findPreviousToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Shift | System.Windows.Forms.Keys.F3)));
			this.findPreviousToolStripMenuItem.Size = new System.Drawing.Size(221, 22);
			this.findPreviousToolStripMenuItem.Text = "Find Previous";
			this.findPreviousToolStripMenuItem.Click += new System.EventHandler(this.buttonFindPrevious_Click);
			// 
			// replaceToolStripMenuItem
			// 
			this.replaceToolStripMenuItem.Image = global::ARCed.Properties.Resources.Replace;
			this.replaceToolStripMenuItem.Name = "replaceToolStripMenuItem";
			this.replaceToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.H)));
			this.replaceToolStripMenuItem.Size = new System.Drawing.Size(221, 22);
			this.replaceToolStripMenuItem.Text = "Replace";
			this.replaceToolStripMenuItem.Click += new System.EventHandler(this.buttonReplace_Click);
			// 
			// gotoToolStripMenuItem
			// 
			this.gotoToolStripMenuItem.Image = global::ARCed.Properties.Resources.GoTo;
			this.gotoToolStripMenuItem.Name = "gotoToolStripMenuItem";
			this.gotoToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.G)));
			this.gotoToolStripMenuItem.Size = new System.Drawing.Size(221, 22);
			this.gotoToolStripMenuItem.Text = "Goto...";
			this.gotoToolStripMenuItem.Click += new System.EventHandler(this.buttonGoto_Click);
			// 
			// toolStripSeparator4
			// 
			this.toolStripSeparator4.Name = "toolStripSeparator4";
			this.toolStripSeparator4.Size = new System.Drawing.Size(218, 6);
			// 
			// addToAutoCompleteToolStripMenuItem
			// 
			this.addToAutoCompleteToolStripMenuItem.Image = global::ARCed.Properties.Resources.AutoComplete;
			this.addToAutoCompleteToolStripMenuItem.Name = "addToAutoCompleteToolStripMenuItem";
			this.addToAutoCompleteToolStripMenuItem.Size = new System.Drawing.Size(221, 22);
			this.addToAutoCompleteToolStripMenuItem.Text = "Add to Auto-Complete";
			this.addToAutoCompleteToolStripMenuItem.Click += new System.EventHandler(this.buttonAddToAutocomplete_Click);
			// 
			// formatToolStripMenuItem
			// 
			this.formatToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.commentToolStripMenuItem,
            this.structureScriptToolStripMenuItem,
            this.removeEmptyLinesToolStripMenuItem});
			this.formatToolStripMenuItem.Name = "formatToolStripMenuItem";
			this.formatToolStripMenuItem.Size = new System.Drawing.Size(221, 22);
			this.formatToolStripMenuItem.Text = "Format";
			// 
			// commentToolStripMenuItem
			// 
			this.commentToolStripMenuItem.Image = global::ARCed.Properties.Resources.Comment;
			this.commentToolStripMenuItem.Name = "commentToolStripMenuItem";
			this.commentToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.Q)));
			this.commentToolStripMenuItem.Size = new System.Drawing.Size(184, 22);
			this.commentToolStripMenuItem.Text = "Comment";
			this.commentToolStripMenuItem.Click += new System.EventHandler(this.buttonComment_Click);
			// 
			// structureScriptToolStripMenuItem
			// 
			this.structureScriptToolStripMenuItem.Image = global::ARCed.Properties.Resources.Outline;
			this.structureScriptToolStripMenuItem.Name = "structureScriptToolStripMenuItem";
			this.structureScriptToolStripMenuItem.Size = new System.Drawing.Size(184, 22);
			this.structureScriptToolStripMenuItem.Text = "Structure Script";
			this.structureScriptToolStripMenuItem.Click += new System.EventHandler(this.buttonStructure_Click);
			// 
			// removeEmptyLinesToolStripMenuItem
			// 
			this.removeEmptyLinesToolStripMenuItem.Image = global::ARCed.Properties.Resources.Crop;
			this.removeEmptyLinesToolStripMenuItem.Name = "removeEmptyLinesToolStripMenuItem";
			this.removeEmptyLinesToolStripMenuItem.Size = new System.Drawing.Size(184, 22);
			this.removeEmptyLinesToolStripMenuItem.Text = "Remove Empty Lines";
			this.removeEmptyLinesToolStripMenuItem.Click += new System.EventHandler(this.buttonRemoveEmpty_Click);
			// 
			// _scintilla
			// 
			this._scintilla.AutoComplete.FillUpCharacters = ")]}.";
			this._scintilla.AutoComplete.ListString = "";
			this._scintilla.ConfigurationManager.IsBuiltInEnabled = false;
			this._scintilla.ConfigurationManager.UseXmlReader = false;
			this._scintilla.Dock = System.Windows.Forms.DockStyle.Fill;
			this._scintilla.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F);
			this._scintilla.Indentation.BackspaceUnindents = true;
			this._scintilla.Indentation.IndentWidth = 4;
			this._scintilla.Indentation.ShowGuides = true;
			this._scintilla.Indentation.SmartIndentType = ARCed.Scintilla.SmartIndent.Simple;
			this._scintilla.Indentation.TabWidth = 4;
			this._scintilla.IsBraceMatching = true;
			this._scintilla.Lexing.Lexer = ARCed.Scintilla.Lexer.Ruby;
			this._scintilla.Lexing.LexerName = "ruby";
			this._scintilla.Lexing.LineCommentPrefix = "#~ ";
			this._scintilla.Lexing.StreamCommentPrefix = "=begin";
			this._scintilla.Lexing.StreamCommentSufix = "=end";
			this._scintilla.Location = new System.Drawing.Point(0, 25);
			this._scintilla.LongLines.EdgeColumn = 140;
			this._scintilla.LongLines.EdgeMode = ARCed.Scintilla.EdgeMode.Line;
			this._scintilla.Margins.Margin0.Width = 12;
			this._scintilla.Margins.Margin1.Width = 12;
			this._scintilla.Margins.Margin2.Width = 14;
			this._scintilla.Name = "_scintilla";
			this._scintilla.Size = new System.Drawing.Size(624, 420);
			this._scintilla.TabIndex = 1;
			this._scintilla.CharAdded += new System.EventHandler<ARCed.Scintilla.CharAddedEventArgs>(this.Scintilla_CharAdded);
			this._scintilla.SelectionChanged += new System.EventHandler(this._scintilla_SelectionChanged);
			this._scintilla.TextChanged += new System.EventHandler(this.Scintilla_TextChanged);
			// 
			// ScriptEditorForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(624, 445);
			this.Controls.Add(this._scintilla);
			this.Controls.Add(this.toolStrip);
			this.DefaultFloatSize = new System.Drawing.Size(720, 540);
			this.DoubleBuffered = true;
			this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.Name = "ScriptEditorForm";
			this.ShowHint = ARCed.UI.DockState.Document;
			this.Text = "ScriptEditor";
			this.Activated += new System.EventHandler(this.ScriptEditorForm_Activated);
			this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.ScriptEditorForm_FormClosing);
			this.toolStrip.ResumeLayout(false);
			this.toolStrip.PerformLayout();
			this.contextMenu.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this._scintilla)).EndInit();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.ToolStrip toolStrip;
		private System.Windows.Forms.ToolStripButton cutToolStripButton;
		private System.Windows.Forms.ToolStripButton copyToolStripButton;
		private System.Windows.Forms.ToolStripButton pasteToolStripButton;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator1;
		private System.Windows.Forms.ToolStripButton buttonStyle;
		private System.Windows.Forms.ToolStripButton buttonAutoComplete;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator2;
		private System.Windows.Forms.ToolStripButton buttonToggleAutoComplete;
		private System.Windows.Forms.ToolStripButton buttonToggleAutoIndent;
		private System.Windows.Forms.ToolStripButton buttonToggleIndentGuides;
		private System.Windows.Forms.ToolStripButton buttonToggleFolding;
		private System.Windows.Forms.ToolStripButton buttonToggleCaret;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator3;
		private System.Windows.Forms.ToolStripButton buttonCharMap;
		private System.Windows.Forms.ToolStripButton buttonCalc;
		private System.Windows.Forms.ContextMenuStrip contextMenu;
		private System.Windows.Forms.ToolStripMenuItem undoToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem redoToolStripMenuItem;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator6;
		private System.Windows.Forms.ToolStripMenuItem cutToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem copyToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem pasteToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem deleteToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem selectAllToolStripMenuItem;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator5;
		private System.Windows.Forms.ToolStripMenuItem incrementalSearchToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem findToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem findNextToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem findPreviousToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem replaceToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem gotoToolStripMenuItem;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator4;
		private System.Windows.Forms.ToolStripMenuItem addToAutoCompleteToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem formatToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem commentToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem structureScriptToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem removeEmptyLinesToolStripMenuItem;
		private Scintilla.Scintilla _scintilla;
		private System.Windows.Forms.ToolStripButton buttonScriptStructure;
	}
}