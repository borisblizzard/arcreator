#region Using Directives

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Linq;
using System.Windows.Forms;
using ARCed.Helpers;
using ARCed.Properties;
using ARCed.Scintilla;
using ARCed.Settings;
using ARCed.UI;

#endregion

namespace ARCed.Scripting
{
	/// <summary>
	/// Form used for editing game scripts. Uses a customizable Ruby lexer for syntax highlighting.
	/// </summary>
	public partial class ScriptEditorForm : DockContent
	{

		#region Private Fields

	    private bool _needSave;
		private string _title;
		private Script _script;
		private static readonly List<char> _braces = new List<char>
		{ '(', ')', '[', ']', '{', '}' };
		private static List<char> _suppressedChars;
		private static List<string> _unindentWords;
	    private static bool _suppressEvents;

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets or sets title of the script and window title
		/// </summary>
		public string Title 
		{ 
			get { return this._title; }
			set { this.SetTitle(value); }
		}
		/// <summary>
		/// Gets the Scintilla object from the window
		/// </summary>
		public Scintilla.Scintilla ScintillaControl
		{
			get { return this._scintilla; }
		}
		/// <summary>
		/// Gets the text from the scintilla control
		/// </summary>
		public string ScriptText { get { return this._scintilla.Text; } }
		/// <summary>
		/// Gets or sets the flag for showing the script has been updated and requires saving
		/// </summary>
		public bool NeedSave 
		{ 
			get { return this._needSave || this.NeedApplyChanges; } 
			set { this._needSave = value; this.UpdateTitle(); } 
		}
		/// <summary>
		/// Gets the flag if changes need applied to the script text
		/// </summary>
		public bool NeedApplyChanges { get { return false; } }//get { return _scintilla.Text != _script.Text; } }
		/// <summary>
        /// Gets or sets the window's associated <see cref="ARCed.Scripting.Script"/> object
		/// </summary>
		public Script Script { get { return this._script; } set { this.ChangeScript(value); } }

		#endregion

		#region Constructors

		/// <summary>
		/// Default constructor
		/// </summary>
		public ScriptEditorForm()
		{
			_unindentWords =
				Resources.UnIndentWords.Split(' ').ToList();
			_suppressedChars = Resources.SuppressedChars.ToCharArray().ToList();
			_suppressedChars.AddRange(new[] { ' ', '\n', '\r', '\t', '\\' });
			this.InitializeComponent();
			Icon = Icon.FromHandle(Resources.Ruby.GetHicon());
			this.InitializeScintilla();
		

			_suppressEvents = true;
			this.buttonToggleAutoComplete.Checked = _settings.AutoComplete;
			this.buttonToggleAutoIndent.Checked = _settings.AutoIndent;
			this.buttonToggleCaret.Checked = _settings.Caret;
			this.buttonToggleFolding.Checked = _settings.CodeFolding;
			this.buttonToggleIndentGuides.Checked = _settings.GuideLines;
			_suppressEvents = false;
		}

		/// <summary>
		/// Constructs and opens a script
		/// </summary>
		/// <param name="script">The script to open</param>
		public ScriptEditorForm(Script script) : this()
		{
			this.SetStyle();
			this.ChangeScript(script);
		}

		#endregion


		/// <summary>
		/// Adds the form to the main editor's script editor list
		/// </summary>
		public void RegisterScript()
		{
			if (Project.IsLoaded && !Windows.ScriptEditors.Contains(this))
				Windows.ScriptEditors.Add(this);
		}

		/// <summary>
		/// Removes the window from the main editor's list of open script editors
		/// </summary>
		public void DeRegisterScript()
		{
			if (Project.IsLoaded && Windows.ScriptEditors.Contains(this))
				Windows.ScriptEditors.Remove(this);
		}

		/// <summary>
        /// Changes the form's associated <see cref="ARCed.Scripting.Script"/> object
		/// </summary>
		/// <param name="script"></param>
		public void ChangeScript(Script script)
		{
			this._script = script;
			this._scintilla.Text = this._script.Text;
			this.SetTitle(this._script.Title);
			this._scintilla.UndoRedo.EmptyUndoBuffer();
		}

		private static ScriptSettings _settings
		{
			get { return Editor.Settings.Scripting; }
		}

		private void InitializeScintilla()
		{
			// Lexer
			this._scintilla.ConfigurationManager.Language = "ruby";
			this._scintilla.Lexing.Lexer = Lexer.Ruby;
			this._scintilla.Lexing.SetKeywords(0, Resources.RubyKeywords);
			//Folding
			this._scintilla.Folding.Flags = FoldFlag.LineAfterContracted;
			this._scintilla.Folding.UseCompactFolding = true;
			this._scintilla.Folding.IsEnabled = true;
			// Indentation
			//_scintilla.Indentation.TabWidth = 2;
			// AutoComplete
			this._scintilla.AutoComplete.DropRestOfWord = false;
			this._scintilla.AutoComplete.CancelAtStart = true;
			this._scintilla.AutoComplete.IsCaseSensitive = false;
			// Margins
			//_scintilla.Margins.Margin0.Width = 20;
			//_scintilla.Margins.Margin1.Width = 2;
			// Edge Line
			//_scintilla.LongLines.EdgeColumn = 80;
			//_scintilla.LongLines.EdgeMode = EdgeMode.Line;


		    this._scintilla.KeyDown += this.Scintilla_KeyDown;

			this._scintilla.NativeInterface.UpdateUI += 
				this.ScintillaNativeInterfaceUpdateUi;
			// Setup
			this._scintilla.SupressControlCharacters = true;
			this._scintilla.ContextMenuStrip = this.contextMenu;
			this._scintilla.Dock = DockStyle.Fill;
			this.UpdateSettings();
		}

		private void ScriptEditorForm_FormClosing(object sender, FormClosingEventArgs e)
		{
			this.DeRegisterScript();
		}

		/// <summary>
		/// Updates the script settings to reflect current settings
		/// </summary>
		public void UpdateSettings()
		{
			if (this._scintilla != null)
			{
				this._scintilla.AutoComplete.FillUpCharacters = _settings.FillUpCharacters;
				this._scintilla.Indentation.ShowGuides = _settings.GuideLines;
				this._scintilla.Margins.Margin1.Scintilla.Font = FontHelper.MonoFont;
				this._scintilla.Margins.Margin2.Width = _settings.CodeFolding ? 16 : 0;
				this._scintilla.Caret.CurrentLineBackgroundColor = _settings.CaretColor;
				this._scintilla.Caret.CurrentLineBackgroundAlpha = _settings.CaretColor.A;
				this._scintilla.Caret.HighlightCurrentLine = _settings.Caret;
				this._scintilla.Indentation.SmartIndentType = _settings.AutoIndent ? SmartIndent.None : SmartIndent.Simple;
				if (!_settings.CodeFolding)
					this.UnfoldAllLines();
			}
		}

		/// <summary>
		/// Sets the styles used for the script editor
		/// </summary>
		/// <param name="styles">An array of script styles</param>
		public void SetStyle(ScriptStyle[] styles)
		{
			if (this._scintilla != null)
			{
				for (int i = 0; i < 19; i++)
				{
					if (i == 1)
						continue;
					this._scintilla.Styles[i].ForeColor = styles[i].ForeColor;
					this._scintilla.Styles[i].BackColor = styles[i].BackColor;
					this._scintilla.Styles[i].Font = styles[i].Font;
				}
				// demoted keywords style
				this._scintilla.Styles[29].ForeColor = this._scintilla.Styles[5].ForeColor;
				this._scintilla.Styles[29].BackColor = this._scintilla.Styles[5].BackColor;
				this._scintilla.Styles[29].Font = this._scintilla.Styles[5].Font;
				// braces style
				this._scintilla.Styles.BraceLight.ForeColor = styles[1].ForeColor;
				this._scintilla.Styles.BraceLight.BackColor = styles[1].BackColor;
				this._scintilla.Styles.BraceLight.Font = styles[1].Font;
				this._scintilla.Styles.BraceBad.ForeColor = styles[1].BackColor;
				this._scintilla.Styles.BraceBad.BackColor = styles[1].ForeColor;
				this._scintilla.Styles.BraceBad.Font = styles[1].Font;
				// left margin style
				this._scintilla.Styles.LineNumber.ForeColor = styles[19].ForeColor;
				this._scintilla.Styles.LineNumber.BackColor = styles[19].BackColor;
				this._scintilla.Styles.LineNumber.Font = styles[19].Font;
				this._scintilla.Margins.FoldMarginColor = styles[19].BackColor;
			}
		}

		/// <summary>
		/// Sets the styles used for the script editor to match the currently defined
		/// </summary>
		public void SetStyle()
		{
			this.SetStyle(_settings.ScriptStyles);
		}

		private void SetTitle(string title)
		{
			this._title = title;
			this.UpdateTitle();
		}

		/// <summary>
		/// Normalizes indentation of the script according to standard Ruby conventions
		/// </summary>
		/// <returns>Return true if changes have been applied</returns>
		public void StructureScript()
		{
			this._scintilla.UndoRedo.BeginUndoAction();
			foreach (Line line in this._scintilla.Lines)
			{
				int indent = this.GetLineIndent(line);
				if (indent != -1)
				{
					line.Indentation = 0; // so even if the indent is the same thereafter it will replace "  " by "\t"
					line.Indentation = indent * this._scintilla.Indentation.TabWidth;
				}
			}
			this._scintilla.UndoRedo.EndUndoAction();
		}

		/// <summary>
		/// Make the script shorter by deleting all unneeded lines
		/// </summary>
		/// <returns>Return true if changes have been applied</returns>
		public void RemoveEmptyLines()
		{
			this._scintilla.UndoRedo.BeginUndoAction();
			for (int i = this._scintilla.Lines.Count - 1; i >= 0; i--)
				if (this._scintilla.Lines[i].Text.Trim().Length == 0)
				{
					this._scintilla.CurrentPos = this._scintilla.Lines[i].StartPosition;
					this._scintilla.Commands.Execute(BindableCommand.LineDelete);
				}
			Line lastLine = this._scintilla.Lines[this._scintilla.Lines.Count - 1];
			if (lastLine.Text.Length == 0)
			{
				this._scintilla.CurrentPos = lastLine.StartPosition;
				this._scintilla.Commands.Execute(BindableCommand.DeleteBack);
			}
			this._scintilla.UndoRedo.EndUndoAction();
		}

		/// <summary>
		/// Expands all code folding
		/// </summary>
		public void UnfoldAllLines()
		{
			if (this._scintilla != null)
				foreach (Line line in this._scintilla.Lines)
					if (!line.FoldExpanded)
						line.ToggleFoldExpanded();
		}

		/// <summary>
		/// Return the required indent for this line or -1 if the line is a multiline comment or string
		/// </summary>
		private int GetLineIndent(Line line)
		{
			int pos = line.StartPosition - 1;
			this._scintilla.NativeInterface.Colourise(pos, pos + 1); // styles are used to determine indent so we must load them before proceeding
			int style = this._scintilla.Styles.GetStyleAt(pos);
			if (style == 3 || style == 6 || style == 7 || style == 12 || style == 18 || line.Text.StartsWith("=begin"))
				return -1;
			int indent = line.FoldLevel - 1024;
			string w1 = this._scintilla.GetWordFromPosition(line.IndentPosition);
			string w2 = this._scintilla.CharAt(line.IndentPosition).ToString();
			if (_unindentWords.Contains(w1) || _unindentWords.Contains(w2))
				indent--;
			return indent;
		}

		private bool IsBrace(int pos)
		{
			return this._scintilla != null && _braces.Contains(this._scintilla.CharAt(pos)) && this._scintilla.Styles.GetStyleAt(pos) == 10;
		}


		public void ApplyChanges()
		{
			if (this.NeedApplyChanges)
			{
				this.NeedSave = true;
			}
		}

		private void UpdateTitle()
		{
			Text = this.NeedSave ? "* " + this.Title : this.Title;
		}

		#region Scintilla Events

		/// <summary>
		/// Checks key input for the hotkeys
		/// </summary>
		private void Scintilla_KeyDown(object sender, KeyEventArgs e)
		{
			if (e.Control)
			{
				var scintilla = (Scintilla.Scintilla)sender;
				if (e.KeyCode == Keys.NumPad0 || e.KeyCode == Keys.D0)
					scintilla.Zoom = 0;
				// Just for GG, we add the Ctrl button for dropping autocomplete :)
				if (scintilla.AutoComplete.IsActive)
					scintilla.AutoComplete.Accept();
			}
		}

		/// <summary>
		/// Registers characters added to the control for controlling auto-indentation and autocomplete 
		/// </summary>
		private void Scintilla_CharAdded(object sender, CharAddedEventArgs e)
		{
			// Update AutoIndent depending on words typed
			if (_settings.AutoIndent && e.Ch == '\n')
			{
				// Correct previous line indent
				string prevText = this._scintilla.Lines.Current.Previous.Text.Trim();
				int prevIndent = -1;
				if (prevText == "=begin" || prevText == "=end")
					this._scintilla.Lines.Current.Previous.Indentation = 0;
				else
					prevIndent = this.GetLineIndent(this._scintilla.Lines.Current.Previous);
				if (prevIndent != -1)
					this._scintilla.Lines.Current.Previous.Indentation = prevIndent * this._scintilla.Indentation.TabWidth;
				// Indent new line
				string indentStr = "";
				int indent = this.GetLineIndent(this._scintilla.Lines.Current);
				for (int i = 0; i < indent; i++)
					indentStr += "\t";
				this._scintilla.InsertText(indentStr);
			}
			// Update AutoComplete depending on the words typed
			if (_settings.AutoComplete)
			{
				int pos = this._scintilla.CurrentPos;
				// Prevents auto-complete for comments and strings
				int style = this._scintilla.Styles.GetStyleAt(pos - 2);
				if (style == 2 || style == 3 || style == 6 || style == 7 || style == 12 || style == 18)
					return;
				// Prevents certain characters from raising the auto-complete window
				string word = this._scintilla.GetWordFromPosition(pos).ToLower();
				if (_suppressedChars.Contains(e.Ch) || word.Length < _settings.AutoCompleteLength)
					return;
				// Select the matched words (we assume that Settings.AutoCompleteWords is already sorted)
				this._scintilla.AutoComplete.List = _settings.AutoCompleteWords.FindAll(
				    listWord => (listWord.ToLower().Contains(word)));
				if (this._scintilla.AutoComplete.List.Count > 0)
					this._scintilla.AutoComplete.Show();
				else
					this._scintilla.AutoComplete.Cancel();
			}
		}

		/// <summary>
		/// Ensures the margin is sized correctly to allow display of the line numbers
		/// </summary>
		private void Scintilla_TextChanged(object sender, EventArgs e)
		{
			int lineNumber = this._scintilla.Lines.Count;
			if (lineNumber < 100)
				this._scintilla.Margins.Margin0.Width = 20;
			else if (lineNumber < 1000)
				this._scintilla.Margins.Margin0.Width = 30;
			else if (lineNumber < 10000)
				this._scintilla.Margins.Margin0.Width = 40;
			else if (lineNumber < 100000)
				this._scintilla.Margins.Margin0.Width = 50;
			else
				this._scintilla.Margins.Margin0.Width = 60;
			this.UpdateTitle();
			this.UpdateScriptStatus();
		}

		/// <summary>
		/// Check if cursor is on a brace or not, highlighting if necessary
        /// </summary>
        #pragma warning disable 612, 618
        private void ScintillaNativeInterfaceUpdateUi(object sender, NativeScintillaEventArgs e)
		{
			var scintilla = (Scintilla.Scintilla)sender;
			int pos = scintilla.CurrentPos;
			if (this.IsBrace(pos) || this.IsBrace(--pos))
			{
				int match = scintilla.NativeInterface.BraceMatch(pos, 0);
				if (match != -1)
					scintilla.NativeInterface.BraceHighlight(pos, match);
				else
					scintilla.NativeInterface.BraceBadLight(pos);
			}
			else
				scintilla.NativeInterface.BraceHighlight(-1, -1);
			Editor.StatusBar.Items[2].Text =
				String.Format("Current Position: {0}", this._scintilla.CurrentPos);
		}
        #pragma warning restore 612, 618

        #endregion

        private void buttonStyle_Click(object sender, EventArgs e)
		{
			Windows.ScriptStyleMenu.Show(Editor.MainDock);
		}

		private void buttonAutoComplete_Click(object sender, EventArgs e)
		{
			Windows.AutoCompleteWindow.Show(Editor.MainDock);
		}

		private void buttonToggleAutoComplete_Click(object sender, EventArgs e)
		{
			if (!_suppressEvents)
			{
				_suppressEvents = true;
				_settings.AutoComplete = this.buttonToggleAutoComplete.Checked;
				foreach (ScriptEditorForm form in Windows.ScriptEditors)
					form.buttonToggleAutoComplete.Checked = _settings.AutoComplete;
				_suppressEvents = false;
			}
		}

		private void buttonToggleAutoIndent_Click(object sender, EventArgs e)
		{
			if (!_suppressEvents)
			{
				_suppressEvents = true;
				_settings.AutoIndent = this.buttonToggleAutoIndent.Checked;
				foreach (ScriptEditorForm form in Windows.ScriptEditors)
					form.buttonToggleAutoIndent.Checked = _settings.AutoIndent;
				_suppressEvents = false;
			}
		}

		private void buttonToggleIndentGuides_Click(object sender, EventArgs e)
		{
			_settings.GuideLines = this.buttonToggleIndentGuides.Checked;
		}

		private void buttonToggleFolding_Click(object sender, EventArgs e)
		{
			_settings.CodeFolding = this.buttonToggleFolding.Checked;
		}

		private void buttonToggleCaret_Click(object sender, EventArgs e)
		{
			if (!_suppressEvents)
			{
				_suppressEvents = true;
				_settings.Caret = this.buttonToggleCaret.Checked;
				foreach (ScriptEditorForm form in Windows.ScriptEditors)
				{
					form.ScintillaControl.Caret.Style = _settings.Caret ? 
						CaretStyle.Line : CaretStyle.Invisible;
				}
				_suppressEvents = false;
			}
		}

		private void buttonCharMap_Click(object sender, EventArgs e)
		{
			Editor.AttachProcess("charmap.exe");
		}

		private void buttonCalc_Click(object sender, EventArgs e)
		{
			Windows.CalculatorWindow.Show();
			Windows.CalculatorWindow.Activate();
		}

		#region Context Menu

		private void buttonCut_Click(object sender, EventArgs e)
		{
			if (this._scintilla.Clipboard.CanCut)
				this._scintilla.Clipboard.Cut();
		}

		private void buttonCopy_Click(object sender, EventArgs e)
		{
			if (this._scintilla.Clipboard.CanCopy)
				this._scintilla.Clipboard.Copy();
		}

		private void buttonPaste_Click(object sender, EventArgs e)
		{
			if (this._scintilla.Clipboard.CanPaste)
				this._scintilla.Clipboard.Paste();
		}

		private void buttonUndo_Click(object sender, EventArgs e)
		{
			if (this._scintilla.UndoRedo.CanUndo)
				this._scintilla.UndoRedo.Undo();
		}

		private void buttonRedo_Click(object sender, EventArgs e)
		{
			if (this._scintilla.UndoRedo.CanRedo)
				this._scintilla.UndoRedo.Redo();
		}

		private void buttonDelete_Click(object sender, EventArgs e)
		{
			this._scintilla.Commands.Execute(BindableCommand.DeleteBack);
		}

		private void buttonSelectAll_Click(object sender, EventArgs e)
		{
			this._scintilla.Commands.Execute(BindableCommand.SelectAll);
		}

		private void buttonIncrementalSearch_Click(object sender, EventArgs e)
		{
			this._scintilla.Commands.Execute(BindableCommand.IncrementalSearch);
			Point p = this._scintilla.PointToClient(MousePosition);
			if (this._scintilla.Bounds.Contains(p))
				this._scintilla.FindReplace.IncrementalSearcher.Location = p;
		}

		private void buttonFind_Click(object sender, EventArgs e)
		{
			this._scintilla.Commands.Execute(BindableCommand.ShowFind);
			Point p = this._scintilla.PointToClient(MousePosition);
			if (this._scintilla.Bounds.Contains(p))
				this._scintilla.FindReplace.Window.Location = p;
		}

		private void buttonFindNext_Click(object sender, EventArgs e)
		{
			this._scintilla.Commands.Execute(BindableCommand.FindNext);
		}

		private void buttonFindPrevious_Click(object sender, EventArgs e)
		{
			this._scintilla.Commands.Execute(BindableCommand.FindPrevious);
		}

		private void buttonReplace_Click(object sender, EventArgs e)
		{
			this._scintilla.Commands.Execute(BindableCommand.ShowReplace);
			Point p = this._scintilla.PointToClient(MousePosition);
			if (this._scintilla.Bounds.Contains(p))
				this._scintilla.FindReplace.Window.Location = p;
		}

		private void buttonGoto_Click(object sender, EventArgs e)
		{
			this._scintilla.Commands.Execute(BindableCommand.ShowGoTo);
		}

		private void buttonAddToAutocomplete_Click(object sender, EventArgs e)
		{
			Windows.AutoCompleteWindow.AddToAutocomplete(this._scintilla.Selection.Text);
		}

		private void buttonComment_Click(object sender, EventArgs e)
		{
			this._scintilla.Commands.Execute(BindableCommand.ToggleLineComment);
		}

		private void buttonStructure_Click(object sender, EventArgs e)
		{
			this.StructureScript();
		}

		private void buttonRemoveEmpty_Click(object sender, EventArgs e)
		{
			this.RemoveEmptyLines();
		}

		#endregion

		private void SaveChanges()
		{
			this._script.Text = this._scintilla.Text;
			this._script.Save();
			this._needSave = false;
			this.UpdateTitle();
		}

		private void UpdateScriptStatus()
		{
			Editor.StatusBar.Items[0].Text = 
				String.Format("Lines: {0}  Characters: {1}", this._scintilla.Lines.Count, this._scintilla.TextLength);
			Editor.StatusBar.Items[1].Text = this._scintilla.Selection.Length == 0 ? "" :
				String.Format("Selection Length: {0}", this._scintilla.Selection.Length);
			Editor.StatusBar.Items[2].Text = 
				String.Format("Current Position: {0}", this._scintilla.CurrentPos);
		}

		private void ScriptEditorForm_Activated(object sender, EventArgs e)
		{
			this._scintilla.FindReplace.Window = Windows.ScintillaFindReplace;
			Windows.ScintillaFindReplace.Scintilla = this._scintilla;
			this.UpdateScriptStatus();
			if (Pane != null && Pane.ContextMenuStrip == null)
				Pane.ContextMenuStrip = Windows.ScriptTabContextMenu;
		}

		private void _scintilla_SelectionChanged(object sender, EventArgs e)
		{
			this.copyToolStripButton.Enabled = this._scintilla.Clipboard.CanCopy;
			this.cutToolStripMenuItem.Enabled = this._scintilla.Clipboard.CanCut;
			this.pasteToolStripButton.Enabled = this._scintilla.Clipboard.CanPaste;
			Editor.StatusBar.Items[1].Text = this._scintilla.Selection.Length == 0 ? "" :
				String.Format("Selection Length: {0}", this._scintilla.Selection.Length);
		}

		void contextMenu_Opening(object sender, CancelEventArgs e)
		{
			bool enable = this._scintilla.Selection.Length > 0;
			this.copyToolStripMenuItem.Enabled = enable;
			this.cutToolStripMenuItem.Enabled = enable;
			this.deleteToolStripMenuItem.Enabled = enable;
			this.commentToolStripMenuItem.Enabled = enable;
			this.addToAutoCompleteToolStripMenuItem.Enabled = enable;
		}

		private void buttonScriptStructure_Click(object sender, EventArgs e)
		{
			this.StructureScript();
		}
	}
}
