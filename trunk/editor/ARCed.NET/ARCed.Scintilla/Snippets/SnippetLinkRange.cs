#region Using Directives

using System.Collections.Generic;

#endregion


namespace ARCed.Scintilla
{
    public class SnippetLinkRange : ManagedRange
    {
        #region Fields

        private bool _active;
        private string _key;
        private List<SnippetLinkRange> _parent;

        #endregion Fields


        #region Methods

        public override void Dispose()
        {
            if (!IsDisposed)
            {
                this._parent.Remove(this);
                base.Dispose();
            }
        }


        internal void Init()
        {
            Scintilla.ManagedRanges.Add(this);
        }

        #endregion Methods


        #region Properties

        public bool Active
        {
            get
            {
                return this._active;
            }
            set
            {
                this._active = value;

                if (value)
                {
                    ClearIndicator(Scintilla.Snippets.InactiveSnippetIndicator);
                    SetIndicator(Scintilla.Snippets.ActiveSnippetIndicator);
                }
                else
                {
                    SetIndicator(Scintilla.Snippets.InactiveSnippetIndicator);
                    ClearIndicator(Scintilla.Snippets.ActiveSnippetIndicator);
                }
            }
        }


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


        public List<SnippetLinkRange> Parent
        {
            get
            {
                return this._parent;
            }
            set
            {
                this._parent = value;
            }
        }

        #endregion Properties


        #region Constructors

        public SnippetLinkRange(int start, int end, Scintilla scintilla, string key)
        {
            Scintilla = scintilla;
            Start = start;
            End = end;
            this._key = key;
        }

        #endregion Constructors
    }
}
