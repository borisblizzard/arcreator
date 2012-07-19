#region Using Directives

using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using ARCed.Helpers;
using ARCed.Properties;
using ARCed.Scintilla;
using ARCed.UI;

#endregion

namespace ARCed.Scripting
{
	/// <summary>
	/// Class for displaying search results found across multiple script files
	/// </summary>
	public partial class ScriptSearchForm : DockContent
	{
		private readonly List<SearchResult> results;

		/// <summary>
		/// Default constructor
		/// </summary>
		public ScriptSearchForm()
		{
			this.InitializeComponent();
			Icon = Icon.FromHandle(Resources.Find3.GetHicon());
			this.results = new List<SearchResult>();
			this.searchControl.buttonSearch.Click += this.buttonSearch_Click;
			this.searchControl.listViewResults.DoubleClick += this.listViewResults_DoubleClick;
			this.searchControl.listViewResults.Font = FontHelper.MonoFont;
		}

		private void listViewResults_DoubleClick(object sender, EventArgs e)
		{
			Point p = this.searchControl.listViewResults.PointToClient(MousePosition);
			int index = this.searchControl.listViewResults.GetItemAt(p.X, p.Y).Index;
			if (index >= 0)
			{
				Script script = this.results[index].Script;
				var page = new ScriptEditorForm(script);
				page.Show(Editor.MainDock);
				page.ScintillaControl.Lines[this.results[index].Line].Select();
			}
		}

		private void buttonSearch_Click(object sender, EventArgs e)
		{
			this.results.Clear();
			// Create list of scripts to search
			var searchScripts = new List<Script>();
			if (this.searchControl.toolStripComboBox_Scope.SelectedIndex == 0) // Open
			{
			    searchScripts.AddRange(Windows.ScriptEditors.Select(form => form.Script));
			}
			else // All
				searchScripts = Project.ScriptManager.Scripts;
			string searchString = this.searchControl.textBoxSearch.Text;
			// Set flags
			var flag = SearchFlags.Empty;
			if (this.searchControl.toolStripMenuItem_MatchCase.Checked) flag |= SearchFlags.MatchCase;
			if (this.searchControl.toolStripMenuItem_RegExp.Checked) flag |= SearchFlags.RegExp;
			if (this.searchControl.toolStripMenuItem_WholeWord.Checked) flag |= SearchFlags.WholeWord;
			if (this.searchControl.toolStripMenuItem_WordStart.Checked) flag |= SearchFlags.WordStart;
			// Perform search using SciLexer's unmanaged library for improved perfomance
			using (var scintilla = new Scintilla.Scintilla())
			{
				foreach (Script script in searchScripts)
				{
					scintilla.Text = script.Text;
					foreach (Range r in scintilla.FindReplace.FindAll(searchString, flag))
					{
						this.results.Add(new SearchResult(script, script.Title,
							r.StartingLine.Number, r.StartingLine.Text));
					}
				}
			}
			this.RefreshResults();
		}

		private void RefreshResults()
		{
			this.searchControl.listViewResults.BeginUpdate();
			this.searchControl.listViewResults.Items.Clear();
			foreach (SearchResult result in this.results)
				this.searchControl.listViewResults.Items.Add(result);
			this.searchControl.listViewResults.EndUpdate();
		}
	}
}
