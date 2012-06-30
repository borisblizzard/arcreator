using System.Windows.Forms;

namespace ARCed.Scripting
{
	/// <summary>
	/// Represents a script search result
	/// </summary>
	public class SearchResult : ListViewItem
	{
		/// <summary>
		/// Gets or sets the script the result is found in
		/// </summary>
		public Script Script { get; set; }
		/// <summary>
		/// Gets or sets the line number of the result
		/// </summary>
		public int Line { get; set; }

		/// <summary>
		/// Constructs a new instance
		/// </summary>
		/// <param name="script">The <paramref name="ARCed.Scripting.Script"/> the result is found in</param>
		/// <param name="scriptTitle">Title of the script</param>
		/// <param name="lineNumber">The line number the in the script the result is found on</param>
		/// <param name="lineText">The text of the line</param>
		public SearchResult(Script script, string scriptTitle, int lineNumber, string lineText)
			: base(new string[] { scriptTitle, (lineNumber + 1).ToString(), lineText })
		{
			Script = script;
			Line = lineNumber;
		}
	}
}
