#region Using Directives

using System.Windows.Forms;

#endregion


namespace ARCed.Scintilla
{
    public class ToolStripIncrementalSearcher : ToolStripControlHost
    {
        #region Properties

        public Scintilla Scintilla
        {
            get { return this.Searcher.Scintilla; }
            set { this.Searcher.Scintilla = value; }
        }


        public IncrementalSearcher Searcher
        {
            get { return Control as IncrementalSearcher; }
        }

        #endregion Properties


        #region Constructors

        public ToolStripIncrementalSearcher() : base(new IncrementalSearcher(true))
        {
        }

        #endregion Constructors
    }
}
