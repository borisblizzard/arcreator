using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Windows.Forms;
using ARCed.Scintilla;
using ARCed.UI;

namespace ARCed.Scripting
{
	/// <summary>
	/// Form used for editing game scripts. Uses a customizable Ruby lexer for syntax highlighting.
	/// </summary>
	public partial class ScriptEditorForm : DockContent
	{

		#region Private Fields

		private bool _needSave = false;
		private string _title;
		private Script _script;
		private static List<char> _braces = new List<char>() { '(', ')', '[', ']', '{', '}' };
		private static List<char> _suppressedChars;
		private static List<string> _unindentWords;
		private static bool _suppressEvents = false;

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets or sets title of the script and window title
		/// </summary>
		public string Title 
		{ 
			get { return _title; }
			set { SetTitle(value); }
		}
		/// <summary>
		/// Gets the Scintilla object from the window
		/// </summary>
		public Scintilla.Scintilla ScintillaControl
		{
			get { return _scintilla; }
		}
		/// <summary>
		/// Gets the text from the scintilla control
		/// </summary>
		public string ScriptText { get { return _scintilla.Text; } }
		/// <summary>
		/// Gets or sets the flag for showing the script has been updated and requires saving
		/// </summary>
		public bool NeedSave 
		{ 
			get { return _needSave || NeedApplyChanges; } 
			set { _needSave = value; UpdateTitle(); } 
		}
		/// <summary>
		/// Gets the flag if changes need applied to the script text
		/// </summary>
		public bool NeedApplyChanges { get { return false; } }//get { return _scintilla.Text != _script.Text; } }
		/// <summary>
		/// Gets or sets the window's associated <paramref name="ARCed.Scripting.Script"/> object
		/// </summary>
		public Script Script { get { return _script; } set { ChangeScript(value); } }

		#endregion

		#region Constructors

		/// <summary>
		/// Default constructor
		/// </summary>
		public ScriptEditorForm()
		{
			_unindentWords =
				ARCed.Properties.Resources.UnIndentWords.Split(' ').ToList<string>();
			_suppressedChars = ARCed.Properties.Resources.SuppressedChars.ToCharArray().ToList<char>();
			_suppressedChars.AddRange(new char[] { ' ', '\n', '\r', '\t', '\\' });
			InitializeComponent();
			this.Icon = System.Drawing.Icon.FromHandle(Properties.Resources.Ruby.GetHicon());
			InitializeScintilla();
		

			_suppressEvents = true;
			buttonToggleAutoComplete.Checked = _settings.AutoComplete;
			buttonToggleAutoIndent.Checked = _settings.AutoIndent;
			buttonToggleCaret.Checked = _settings.Caret;
			buttonToggleFolding.Checked = _settings.CodeFolding;
			buttonToggleIndentGuides.Checked = _settings.GuideLines;
			_suppressEvents = false;
		}

		/// <summary>
		/// Constructs and opens a script
		/// </summary>
		/// <param name="script">The script to open</param>
		public ScriptEditorForm(Script script) : this()
		{
			SetStyle();
			ChangeScript(script);
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
		/// Changes the form's associated <paramref name="ARCed.Scripting.Script"/> object
		/// </summary>
		/// <param name="script"></param>
		public void ChangeScript(Script script)
		{
			_script = script;
			_scintilla.Text = _script.Text;
			SetTitle(_script.Title);
			_scintilla.UndoRedo.EmptyUndoBuffer();
		}

		private ARCed.Settings.ScriptSettings _settings
		{
			get { return Editor.Settings.Scripting; }
		}

		private void InitializeScintilla()
		{
			// Lexer
			_scintilla.ConfigurationManager.Language = "ruby";
			_scintilla.Lexing.Lexer = Lexer.Ruby;
			_scintilla.Lexing.SetKeywords(0, ARCed.Properties.Resources.RubyKeywords);
			//Folding
			_scintilla.Folding.Flags = FoldFlag.LineAfterContracted;
			_scintilla.Folding.UseCompactFolding = true;
			_scintilla.Folding.IsEnabled = true;
			// Indentation
			//_scintilla.Indentation.TabWidth = 2;
			// AutoComplete
			_scintilla.AutoComplete.DropRestOfWord = false;
			_scintilla.AutoComplete.CancelAtStart = true;
			_scintilla.AutoComplete.IsCaseSensitive = false;
			// Margins
			//_scintilla.Margins.Margin0.Width = 20;
			//_scintilla.Margins.Margin1.Width = 2;
			// Edge Line
			//_scintilla.LongLines.EdgeColumn = 80;
			//_scintilla.LongLines.EdgeMode = EdgeMode.Line;




			_scintilla.NativeInterface.UpdateUI += 
				new EventHandler<NativeScintillaEventArgs>(Scintilla_NativeInterface_UpdateUI);
			// Setup
			_scintilla.SupressControlCharacters = true;
			_scintilla.ContextMenuStrip = contextMenu;
			_scintilla.Dock = DockStyle.Fill;
			UpdateSettings();
		}

		private void ScriptEditorForm_FormClosing(object sender, FormClosingEventArgs e)
		{
			DeRegisterScript();
		}

		/// <summary>
		/// Updates the script settings to reflect current settings
		/// </summary>
		public void UpdateSettings()
		{
			if (_scintilla != null)
			{
				_scintilla.AutoComplete.FillUpCharacters = _settings.FillUpCharacters;
				_scintilla.Indentation.ShowGuides = _settings.GuideLines;
				_scintilla.Margins.Margin1.Scintilla.Font = Helpers.FontHelper.MonoFont;
				_scintilla.Margins.Margin2.Width = _settings.CodeFolding ? 16 : 0;
				_scintilla.Caret.CurrentLineBackgroundColor = _settings.CaretColor;
				_scintilla.Caret.CurrentLineBackgroundAlpha = _settings.CaretColor.A;
				_scintilla.Caret.HighlightCurrentLine = _settings.Caret;
				_scintilla.Indentation.SmartIndentType = _settings.AutoIndent ? SmartIndent.None : SmartIndent.Simple;
				if (!_settings.CodeFolding)
					UnfoldAllLines();
			}
		}

		/// <summary>
		/// Sets the styles used for the script editor
		/// </summary>
		/// <param name="styles">An array of script styles</param>
		public void SetStyle(ScriptStyle[] styles)
		{
			if (_scintilla != null)
			{
				for (int i = 0; i < 19; i++)
				{
					if (i == 1)
						continue;
					_scintilla.Styles[i].ForeColor = styles[i].ForeColor;
					_scintilla.Styles[i].BackColor = styles[i].BackColor;
					_scintilla.Styles[i].Font = styles[i].Font;
				}
				// demoted keywords style
				_scintilla.Styles[29].ForeColor = _scintilla.Styles[5].ForeColor;
				_scintilla.Styles[29].BackColor = _scintilla.Styles[5].BackColor;
				_scintilla.Styles[29].Font = _scintilla.Styles[5].Font;
				// braces style
				_scintilla.Styles.BraceLight.ForeColor = styles[1].ForeColor;
				_scintilla.Styles.BraceLight.BackColor = styles[1].BackColor;
				_scintilla.Styles.BraceLight.Font = styles[1].Font;
				_scintilla.Styles.BraceBad.ForeColor = styles[1].BackColor;
				_scintilla.Styles.BraceBad.BackColor = styles[1].ForeColor;
				_scintilla.Styles.BraceBad.Font = styles[1].Font;
				// left margin style
				_scintilla.Styles.LineNumber.ForeColor = styles[19].ForeColor;
				_scintilla.Styles.LineNumber.BackColor = styles[19].BackColor;
				_scintilla.Styles.LineNumber.Font = styles[19].Font;
				_scintilla.Margins.FoldMarginColor = styles[19].BackColor;
			}
		}

		/// <summary>
		/// Sets the styles used for the script editor to match the currently defined
		/// </summary>
		public void SetStyle()
		{
			SetStyle(_settings.ScriptStyles);
		}

		private void SetTitle(string title)
		{
			_title = title;
			UpdateTitle();
		}

		/// <summary>
		/// Normalizes indentation of the script according to standard Ruby conventions
		/// </summary>
		/// <returns>Return true if changes have been applied</returns>
		public void StructureScript()
		{
			_scintilla.UndoRedo.BeginUndoAction();
			foreach (Line line in _scintilla.Lines)
			{
				int indent = GetLineIndent(line);
				if (indent != -1)
				{
					line.Indentation = 0; // so even if the indent is the same thereafter it will replace "  " by "\t"
					line.Indentation = indent * _scintilla.Indentation.TabWidth;
				}
			}
			_scintilla.UndoRedo.EndUndoAction();
		}

		/// <summary>
		/// Make the script shorter by deleting all unneeded lines
		/// </summary>
		/// <returns>Return true if changes have been applied</returns>
		public void RemoveEmptyLines()
		{
			_scintilla.UndoRedo.BeginUndoAction();
			for (int i = _scintilla.Lines.Count - 1; i >= 0; i--)
				if (_scintilla.Lines[i].Text.Trim().Length == 0)
				{
					_scintilla.CurrentPos = _scintilla.Lines[i].StartPosition;
					_scintilla.Commands.Execute(BindableCommand.LineDelete);
				}
			Line lastLine = _scintilla.Lines[_scintilla.Lines.Count - 1];
			if (lastLine.Text.Length == 0)
			{
				_scintilla.CurrentPos = lastLine.StartPosition;
				_scintilla.Commands.Execute(BindableCommand.DeleteBack);
			}
			_scintilla.UndoRedo.EndUndoAction();
		}

		/// <summary>
		/// Expands all code folding
		/// </summary>
		public void UnfoldAllLines()
		{
			if (_scintilla != null)
				foreach (Line line in _scintilla.Lines)
					if (!line.FoldExpanded)
						line.ToggleFoldExpanded();
		}

		/// <summary>
		/// Return the required indent for this line or -1 if the line is a multiline comment or string
		/// </summary>
		private int GetLineIndent(Line line)
		{
			int pos = line.StartPosition - 1;
			_scintilla.NativeInterface.Colourise(pos, pos + 1); // styles are used to determine indent so we must load them before proceeding
			int style = _scintilla.Styles.GetStyleAt(pos);
			if (style == 3 || style == 6 || style == 7 || style == 12 || style == 18 || line.Text.StartsWith("=begin"))
				return -1;
			int indent = line.FoldLevel - 1024;
			string w1 = _scintilla.GetWordFromPosition(line.IndentPosition);
			string w2 = _scintilla.CharAt(line.IndentPosition).ToString();
			if (_unindentWords.Contains(w1) || _unindentWords.Contains(w2))
				indent--;
			return indent;
		}

		private bool IsBrace(int pos)
		{
			return _scintilla != null && _braces.Contains(_scintilla.CharAt(pos)) && _scintilla.Styles.GetStyleAt(pos) == 10;
		}


		public void ApplyChanges()
		{
			if (NeedApplyChanges)
			{
				NeedSave = true;
			}
		}

		private void UpdateTitle()
		{
			this.Text = NeedSave ? "* " + Title : Title;
		}

		#region Scintilla Events

		/// <summary>
		/// Checks key input for the hotkeys
		/// </summary>
		private void Scintilla_KeyDown(object sender, KeyEventArgs e)
		{
			if (e.Control)
			{
				Scintilla.Scintilla scintilla = (ARCed.Scintilla.Scintilla)sender;
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
				string prevText = _scintilla.Lines.Current.Previous.Text.Trim();
				int prevIndent = -1;
				if (prevText == "=begin" || prevText == "=end")
					_scintilla.Lines.Current.Previous.Indentation = 0;
				else
					prevIndent = GetLineIndent(_scintilla.Lines.Current.Previous);
				if (prevIndent != -1)
					_scintilla.Lines.Current.Previous.Indentation = prevIndent * _scintilla.Indentation.TabWidth;
				// Indent new line
				string indentStr = "";
				int indent = GetLineIndent(_scintilla.Lines.Current);
				for (int i = 0; i < indent; i++)
					indentStr += "\t";
				_scintilla.InsertText(indentStr);
			}
			// Update AutoComplete depending on the words typed
			if (_settings.AutoComplete)
			{
				int pos = _scintilla.CurrentPos;
				// Prevents auto-complete for comments and strings
				int style = _scintilla.Styles.GetStyleAt(pos - 2);
				if (style == 2 || style == 3 || style == 6 || style == 7 || style == 12 || style == 18)
					return;
				// Prevents certain characters from raising the auto-complete window
				string word = _scintilla.GetWordFromPosition(pos).ToLower();
				if (_suppressedChars.Contains(e.Ch) || word.Length < _settings.AutoCompleteLength)
					return;
				// Select the matched words (we assume that Settings.AutoCompleteWords is already sorted)
				_scintilla.AutoComplete.List = _settings.AutoCompleteWords.FindAll(
					delegate(string listWord) { return (listWord.ToLower().Contains(word)); });
				if (_scintilla.AutoComplete.List.Count > 0)
					_scintilla.AutoComplete.Show();
				else
					_scintilla.AutoComplete.Cancel();
			}
		}

		/// <summary>
		/// Ensures the margin is sized correctly to allow display of the line numbers
		/// </summary>
		private void Scintilla_TextChanged(object sender, EventArgs e)
		{
			int lineNumber = _scintilla.Lines.Count;
			if (lineNumber < 100)
				_scintilla.Margins.Margin0.Width = 20;
			else if (lineNumber < 1000)
				_scintilla.Margins.Margin0.Width = 30;
			else if (lineNumber < 10000)
				_scintilla.Margins.Margin0.Width = 40;
			else if (lineNumber < 100000)
				_scintilla.Margins.Margin0.Width = 50;
			else
				_scintilla.Margins.Margin0.Width = 60;
			UpdateTitle();
			UpdateScriptStatus();
		}

		/// <summary>
		/// Check if cursor is on a brace or not, highlighting if necessary
		/// </summary>
		private void Scintilla_NativeInterface_UpdateUI(object sender, NativeScintillaEventArgs e)
		{
			ARCed.Scintilla.Scintilla scintilla = (ARCed.Scintilla.Scintilla)sender;
			int pos = scintilla.CurrentPos;
			if (IsBrace(pos) || IsBrace(--pos))
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
				String.Format("Current Position: {0}", _scintilla.CurrentPos);
		}

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
				_settings.AutoComplete = buttonToggleAutoComplete.Checked;
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
				_settings.AutoIndent = buttonToggleAutoIndent.Checked;
				foreach (ScriptEditorForm form in Windows.ScriptEditors)
					form.buttonToggleAutoIndent.Checked = _settings.AutoIndent;
				_suppressEvents = false;
			}
		}

		private void buttonToggleIndentGuides_Click(object sender, EventArgs e)
		{
			_settings.GuideLines = buttonToggleIndentGuides.Checked;
		}

		private void buttonToggleFolding_Click(object sender, EventArgs e)
		{
			_settings.CodeFolding = buttonToggleFolding.Checked;
		}

		private void buttonToggleCaret_Click(object sender, EventArgs e)
		{
			if (!_suppressEvents)
			{
				_suppressEvents = true;
				_settings.Caret = buttonToggleCaret.Checked;
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
			if (_scintilla.Clipboard.CanCut)
				_scintilla.Clipboard.Cut();
		}

		private void buttonCopy_Click(object sender, EventArgs e)
		{
			if (_scintilla.Clipboard.CanCopy)
				_scintilla.Clipboard.Copy();
		}

		private void buttonPaste_Click(object sender, EventArgs e)
		{
			if (_scintilla.Clipboard.CanPaste)
				_scintilla.Clipboard.Paste();
		}

		private void buttonUndo_Click(object sender, EventArgs e)
		{
			if (_scintilla.UndoRedo.CanUndo)
				_scintilla.UndoRedo.Undo();
		}

		private void buttonRedo_Click(object sender, EventArgs e)
		{
			if (_scintilla.UndoRedo.CanRedo)
				_scintilla.UndoRedo.Redo();
		}

		private void buttonDelete_Click(object sender, EventArgs e)
		{
			_scintilla.Commands.Execute(BindableCommand.DeleteBack);
		}

		private void buttonSelectAll_Click(object sender, EventArgs e)
		{
			_scintilla.Commands.Execute(BindableCommand.SelectAll);
		}

		private void buttonIncrementalSearch_Click(object sender, EventArgs e)
		{
			_scintilla.Commands.Execute(BindableCommand.IncrementalSearch);
			Point p = _scintilla.PointToClient(MousePosition);
			if (_scintilla.Bounds.Contains(p))
				_scintilla.FindReplace.IncrementalSearcher.Location = p;
		}

		private void buttonFind_Click(object sender, EventArgs e)
		{
			_scintilla.Commands.Execute(BindableCommand.ShowFind);
			Point p = _scintilla.PointToClient(MousePosition);
			if (_scintilla.Bounds.Contains(p))
				_scintilla.FindReplace.Window.Location = p;
		}

		private void buttonFindNext_Click(object sender, EventArgs e)
		{
			_scintilla.Commands.Execute(BindableCommand.FindNext);
		}

		private void buttonFindPrevious_Click(object sender, EventArgs e)
		{
			_scintilla.Commands.Execute(BindableCommand.FindPrevious);
		}

		private void buttonReplace_Click(object sender, EventArgs e)
		{
			_scintilla.Commands.Execute(BindableCommand.ShowReplace);
			Point p = _scintilla.PointToClient(MousePosition);
			if (_scintilla.Bounds.Contains(p))
				_scintilla.FindReplace.Window.Location = p;
		}

		private void buttonGoto_Click(object sender, EventArgs e)
		{
			_scintilla.Commands.Execute(BindableCommand.ShowGoTo);
		}

		private void buttonAddToAutocomplete_Click(object sender, EventArgs e)
		{
			Windows.AutoCompleteWindow.AddToAutocomplete(_scintilla.Selection.Text);
		}

		private void buttonComment_Click(object sender, EventArgs e)
		{
			_scintilla.Commands.Execute(BindableCommand.ToggleLineComment);
		}

		private void buttonStructure_Click(object sender, EventArgs e)
		{
			StructureScript();
		}

		private void buttonRemoveEmpty_Click(object sender, EventArgs e)
		{
			RemoveEmptyLines();
		}

		#endregion

		private void SaveChanges()
		{
			_script.Text = _scintilla.Text;
			_script.Save();
			_needSave = false;
			UpdateTitle();
		}

		private void UpdateScriptStatus()
		{
			Editor.StatusBar.Items[0].Text = 
				String.Format("Lines: {0}  Characters: {1}", _scintilla.Lines.Count, _scintilla.TextLength);
			Editor.StatusBar.Items[1].Text = _scintilla.Selection.Length == 0 ? "" :
				String.Format("Selection Length: {0}", _scintilla.Selection.Length);
			Editor.StatusBar.Items[2].Text = 
				String.Format("Current Position: {0}", _scintilla.CurrentPos);
		}

		private void ScriptEditorForm_Activated(object sender, EventArgs e)
		{
			_scintilla.FindReplace.Window = Windows.ScintillaFindReplace;
			Windows.ScintillaFindReplace.Scintilla = _scintilla;
			UpdateScriptStatus();
			if (this.Pane != null && this.Pane.ContextMenuStrip == null)
				this.Pane.ContextMenuStrip = Windows.ScriptTabContextMenu;
		}

		private void _scintilla_SelectionChanged(object sender, EventArgs e)
		{
			bool enable = _scintilla.Selection.Length > 0;
			copyToolStripButton.Enabled = _scintilla.Clipboard.CanCopy;
			cutToolStripMenuItem.Enabled = _scintilla.Clipboard.CanCut;
			pasteToolStripButton.Enabled = _scintilla.Clipboard.CanPaste;
			Editor.StatusBar.Items[1].Text = _scintilla.Selection.Length == 0 ? "" :
				String.Format("Selection Length: {0}", _scintilla.Selection.Length);
		}

		void contextMenu_Opening(object sender, System.ComponentModel.CancelEventArgs e)
		{
			bool enable = _scintilla.Selection.Length > 0;
			copyToolStripMenuItem.Enabled = enable;
			cutToolStripMenuItem.Enabled = enable;
			deleteToolStripMenuItem.Enabled = enable;
			commentToolStripMenuItem.Enabled = enable;
			addToAutoCompleteToolStripMenuItem.Enabled = enable;
		}

		private void buttonScriptStructure_Click(object sender, EventArgs e)
		{
			StructureScript();
		}
	}
}
