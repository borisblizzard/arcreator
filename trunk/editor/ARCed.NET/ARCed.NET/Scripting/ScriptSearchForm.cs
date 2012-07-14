using System;
using System.Collections.Generic;
using System.Drawing;
using ARCed.Scintilla;
using ARCed.UI;

namespace ARCed.Scripting
{
	/// <summary>
	/// Class for displaying search results found across multiple script files
	/// </summary>
	public partial class ScriptSearchForm : DockContent
	{
		private List<SearchResult> results;

		/// <summary>
		/// Default constructor
		/// </summary>
		public ScriptSearchForm()
		{
			InitializeComponent();
			this.Icon = Icon.FromHandle(Properties.Resources.Find3.GetHicon());
			results = new List<SearchResult>();
			searchControl.buttonSearch.Click += new EventHandler(buttonSearch_Click);
			searchControl.listViewResults.DoubleClick += new EventHandler(listViewResults_DoubleClick);
			searchControl.listViewResults.Font = Helpers.FontHelper.MonoFont;
		}

		private void listViewResults_DoubleClick(object sender, EventArgs e)
		{
			Point p = searchControl.listViewResults.PointToClient(MousePosition);
			int index = searchControl.listViewResults.GetItemAt(p.X, p.Y).Index;
			if (index >= 0)
			{
				Script script = results[index].Script;
				ScriptEditorForm page = new ScriptEditorForm(script);
				page.Show(Editor.MainDock);
				page.ScintillaControl.Lines[results[index].Line].Select();
			}
		}

		private void buttonSearch_Click(object sender, EventArgs e)
		{
			results.Clear();
			// Create list of scripts to search
			List<Script> searchScripts = new List<Script>();
			if (searchControl.toolStripComboBox_Scope.SelectedIndex == 0) // Open
			{
				foreach (ScriptEditorForm form in Windows.ScriptEditors)
					searchScripts.Add(form.Script);
			}
			else // All
				searchScripts = Project.ScriptManager.Scripts;
			string searchString = searchControl.textBoxSearch.Text;
			// Set flags
			SearchFlags flag = SearchFlags.Empty;
			if (searchControl.toolStripMenuItem_MatchCase.Checked) flag |= SearchFlags.MatchCase;
			if (searchControl.toolStripMenuItem_RegExp.Checked) flag |= SearchFlags.RegExp;
			if (searchControl.toolStripMenuItem_WholeWord.Checked) flag |= SearchFlags.WholeWord;
			if (searchControl.toolStripMenuItem_WordStart.Checked) flag |= SearchFlags.WordStart;
			// Perform search using SciLexer's unmanaged library for improved perfomance
			using (var scintilla = new Scintilla.Scintilla())
			{
				foreach (Script script in searchScripts)
				{
					scintilla.Text = script.Text;
					foreach (Range r in scintilla.FindReplace.FindAll(searchString, flag))
					{
						results.Add(new SearchResult(script, script.Title,
							r.StartingLine.Number, r.StartingLine.Text));
					}
				}
			}
			RefreshResults();
		}

		private void RefreshResults()
		{
			searchControl.listViewResults.BeginUpdate();
			searchControl.listViewResults.Items.Clear();
			foreach (SearchResult result in results)
				searchControl.listViewResults.Items.Add(result);
			searchControl.listViewResults.EndUpdate();
		}
	}
}
