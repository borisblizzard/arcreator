#region Using Directives

using System;
using System.ComponentModel;

#endregion


namespace ARCed.Scintilla
{
    [TypeConverter(typeof(ExpandableObjectConverter))]
    public class Indentation : TopLevelHelper
    {
        #region Fields

        /// <summary>
        ///     Enables the Smart Indenter so that On enter, it indents the next line.
        /// </summary>
        private SmartIndent _smartIndentType = SmartIndent.None;

        /// <summary>
        ///     For Custom Smart Indenting, assign a handler to this delegate property.
        /// </summary>
        public EventHandler<CharAddedEventArgs> SmartIndentCustomAction;

        #endregion Fields


        #region Methods

        /// <summary>
        ///     If Smart Indenting is enabled, this delegate will be added to the CharAdded multicast event.
        /// </summary>
        internal void CheckSmartIndent(char ch)
        {
            char newline = (Scintilla.EndOfLine.Mode == EndOfLineMode.CR) ? '\r' : '\n';

            switch (this.SmartIndentType)
            {
                case SmartIndent.None:
                    return;
                case SmartIndent.Simple:
                    if (ch == newline)
                    {
                        Line curLine = Scintilla.Lines.Current;
                        curLine.Indentation = curLine.Previous.Indentation;
                        Scintilla.CurrentPos = curLine.IndentPosition;
                    }
                    break;
                case SmartIndent.CPP:
                case SmartIndent.CPP2:
                    if (ch == newline)
                    {
                        Line curLine = Scintilla.Lines.Current;
                        Line tempLine = curLine;
                        int previousIndent;
                        string tempText;

                        do
                        {
                            tempLine = tempLine.Previous;
                            previousIndent = tempLine.Indentation;
                            tempText = tempLine.Text.Trim();
                            if (tempText.Length == 0) previousIndent = -1;
                        }
                        while ((tempLine.Number > 1) && (previousIndent < 0));

                        if (tempText.EndsWith("{"))
                        {
                            int bracePos = Scintilla.CurrentPos - 1;
                            while (bracePos > 0 && Scintilla.CharAt(bracePos) != '{') bracePos--;
                            if (bracePos > 0 && Scintilla.Styles.GetStyleAt(bracePos) == 10)
                                previousIndent += this.TabWidth;
                        }
                        curLine.Indentation = previousIndent;
                        Scintilla.CurrentPos =  curLine.IndentPosition;
                    }
                    else if (ch == '}')
                    {
                        int position = Scintilla.CurrentPos;
                        Line curLine = Scintilla.Lines.Current;
                        int previousIndent = curLine.Previous.Indentation;
                        int match = Scintilla.SafeBraceMatch(position - 1);
                        if (match != -1)
                        {
                            previousIndent = Scintilla.Lines.FromPosition(match).Indentation;
                            curLine.Indentation =  previousIndent;
                        }
                    }
                    break;
            }
        }


        /// <summary>
        ///     Smart Indenting helper method
        /// </summary>
        private void IndentLine(int line, int indent)
        {
            if (indent < 0)
            {
                return;
            }

            int selStart = Scintilla.Selection.Start;
            int selEnd = Scintilla.Selection.End;

            Line l = Scintilla.Lines[line];
            int posBefore = l.IndentPosition;
            l.Indentation = indent;

            int posAfter = l.IndentPosition;
            int posDifference = posAfter - posBefore;

            if (posAfter > posBefore)
            {
                // Move selection on
                if (selStart >= posBefore)
                {
                    selStart += posDifference;
                }

                if (selEnd >= posBefore)
                {
                    selEnd += posDifference;
                }
            }
            else if (posAfter < posBefore)
            {
                // Move selection back
                if (selStart >= posAfter)
                {
                    if (selStart >= posBefore)
                        selStart += posDifference;
                    else
                        selStart = posAfter;
                }
                if (selEnd >= posAfter)
                {
                    if (selEnd >= posBefore)
                        selEnd += posDifference;
                    else
                        selEnd = posAfter;
                }
            }

            Scintilla.Selection.Start = selStart;
            Scintilla.Selection.End = selEnd;
        }


        private void ResetBackspaceUnindents()
        {
            this.BackspaceUnindents = false;
        }


        private void ResetIndentWidth()
        {
            this.IndentWidth = 0;
        }


        private void ResetShowGuides()
        {
            this.ShowGuides = false;
        }


        private void ResetSmartIndentType()
        {
            this._smartIndentType = SmartIndent.None;
        }


        private void ResetTabIndents()
        {
            this.TabIndents = false;
        }


        private void ResetTabWidth()
        {
            this.TabWidth = 8;
        }


        private void ResetUseTabs()
        {
            this.UseTabs = true;
        }


        internal bool ShouldSerialize()
        {
            return this.ShouldSerializeBackspaceUnindents() ||
                this.ShouldSerializeIndentWidth() ||
                this.ShouldSerializeShowGuides() || 
                this.ShouldSerializeTabIndents() ||
                this.ShouldSerializeTabWidth() ||
                this.ShouldSerializeUseTabs();
        }


        private bool ShouldSerializeBackspaceUnindents()
        {
            return this.BackspaceUnindents;

        }


        private bool ShouldSerializeIndentWidth()
        {
            return this.IndentWidth != 0;
        }


        private bool ShouldSerializeShowGuides()
        {
            return this.ShowGuides;
        }


        private bool ShouldSerializeSmartIndentType()
        {
            return this._smartIndentType != SmartIndent.None;
        }


        private bool ShouldSerializeTabIndents()
        {
            return !this.TabIndents;
        }


        private bool ShouldSerializeTabWidth()
        {
            return this.TabWidth != 8;
        }


        private bool ShouldSerializeUseTabs()
        {
            return !this.UseTabs;
        }

        #endregion Methods


        #region Properties

        public bool BackspaceUnindents
        {
            get
            {
                return NativeScintilla.GetBackSpaceUnIndents();
            }
            set
            {
                NativeScintilla.SetBackSpaceUnIndents(value);
            }
        }


        public int IndentWidth
        {
            get
            {
                return NativeScintilla.GetIndent();
            }
            set
            {
                NativeScintilla.SetIndent(value);
            }
        }


        public bool ShowGuides
        {
            get
            {
                return NativeScintilla.GetIndentationGuides();
            }
            set
            {
                NativeScintilla.SetIndentationGuides(value);
            }
        }


        public SmartIndent SmartIndentType
        {
            get { return this._smartIndentType; }
            set
            {
                this._smartIndentType = value;
            }
        }


        public bool TabIndents
        {
            get
            {
                return NativeScintilla.GetTabIndents();
            }
            set
            {
                NativeScintilla.SetTabIndents(value);
            }
        }


        public int TabWidth
        {
            get
            {
                return NativeScintilla.GetTabWidth();
            }
            set
            {
                NativeScintilla.SetTabWidth(value);
            }
        }


        public bool UseTabs
        {
            get
            {
                return NativeScintilla.GetUseTabs();
            }
            set
            {
                NativeScintilla.SetUseTabs(value);
            }
        }

        #endregion Properties


        #region Constructors

        internal Indentation(Scintilla scintilla) : base(scintilla) { }

        #endregion Constructors
    }
}
