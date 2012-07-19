#region Using Directives

using System.Collections.Generic;

#endregion


namespace ARCed.Scintilla
{
    public class SnippetLink
    {
        #region Fields

        private string _key;
        private List<SnippetLinkRange> _ranges = new List<SnippetLinkRange>();

        #endregion Fields


        #region Properties

        public string Key
        {
            get
            {
                return this._key;
            }
            set
            {
                this._key = value;
            }
        }


        public List<SnippetLinkRange> Ranges
        {
            get
            {
                return this._ranges;
            }
            set
            {
                this._ranges = value;
            }
        }

        #endregion Properties


        #region Constructors

        public SnippetLink(string key)
        {
            this._key = key;
        }

        #endregion Constructors
    }
}
