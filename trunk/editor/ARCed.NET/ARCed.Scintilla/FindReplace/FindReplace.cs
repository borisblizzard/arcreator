#region Using Directives

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Drawing.Design;
using System.Text.RegularExpressions;
using ARCed.Scintilla.Design;
using ARCed.UI;

#endregion


namespace ARCed.Scintilla
{
    [TypeConverter(typeof(ExpandableObjectConverter))]
    public class FindReplace : TopLevelHelper
    {
        #region Fields

        private Indicator _indicator;
        private Marker _marker;
        private SearchFlags _flags;
        private FindReplaceDialog _window;
        private IncrementalSearcher _incrementalSearcher;
        private List<Range> _lastReplaceAllMatches = new List<Range>();
        private string _lastReplaceAllReplaceString = "";
        private Range _lastReplaceAllRangeToSearch;
        private int _lastReplaceAllOffset;

        #endregion Fields

        public static DockPanel ParentDock { get; set; }

        #region Methods

        public void ClearAllHighlights()
        {
            Indicator i = Scintilla.FindReplace.Indicator;
            foreach (Range r in i.SearchAll())
            {
                r.ClearIndicator(i);
            }
        }


        public Range Find(int startPos, int endPos, Regex findExpression)
        {
            return Find(new Range(startPos, endPos, Scintilla), findExpression, false);
        }


        public Range Find(int startPos, int endPos, Regex findExpression, bool searchUp)
        {
            return Find(new Range(startPos, endPos, Scintilla), findExpression, searchUp);
        }


        public unsafe Range Find(int startPos, int endPos, string searchString, SearchFlags flags)
        {
            var ttf = new TextToFind
            {
                chrg =
                {
                    cpMin = startPos,
                    cpMax = endPos
                }
            };

            fixed (byte* pb = Scintilla.Encoding.GetBytes(searchString))
            {
                ttf.lpstrText = (IntPtr)pb;
                int pos = NativeScintilla.FindText((int)flags, ref ttf);
                if (pos >= 0)
                {
                    return new Range(pos, pos + searchString.Length, Scintilla);
                }
                else
                {
                    return null;
                }
            }
        }


        public Range Find(Range r, Regex findExpression)
        {
            return Find(r, findExpression, false);
        }


        public Range Find(Range r, Regex findExpression, bool searchUp)
        {
            // Single line and Multi Line in RegExp doesn't really effect
            // whether or not a match will include newline charaters. This 
            // means we can't do a line by line search. We have to search
            // the entire range becuase it could potentially match the 
            // entire range.

            Match m = findExpression.Match(r.Text);

            if (!m.Success)
                return null;

            if (searchUp)
            {
                // Since we can't search backwards with RegExp we
                // have to search the entire string and return the 
                // last match. Not the most efficient way of doing
                // things but it works.
                Range range = null;
                while (m.Success)
                {
                    range = new Range(r.Start + m.Index, r.Start + m.Index + m.Length, Scintilla);
                    m = m.NextMatch();
                }
                return range;
            }

            return new Range(r.Start + m.Index, r.Start + m.Index + m.Length, Scintilla);
        }


        public Range Find(Range rangeToSearch, string searchString)
        {
            return this.Find(rangeToSearch.Start, rangeToSearch.End, searchString, this._flags);
        }


        public Range Find(Range rangeToSearch, string searchString, bool searchUp)
        {
            if (searchUp)
                return this.Find(rangeToSearch.End, rangeToSearch.Start, searchString, this._flags);
            else
                return this.Find(rangeToSearch.Start, rangeToSearch.End, searchString, this._flags);
        }


        public Range Find(Range rangeToSearch, string searchString, SearchFlags searchflags)
        {
            return Find(rangeToSearch.Start, rangeToSearch.End, searchString, searchflags);
        }


        public Range Find(Range rangeToSearch, string searchString, SearchFlags searchflags, bool searchUp)
        {
            if (searchUp)
                return Find(rangeToSearch.End, rangeToSearch.Start, searchString, searchflags);
            else
                return Find(rangeToSearch.Start, rangeToSearch.End, searchString, searchflags);
        }


        public Range Find(Regex findExpression)
        {
            return Find(new Range(0, NativeScintilla.GetTextLength(), Scintilla), findExpression, false);
        }


        public Range Find(Regex findExpression, bool searchUp)
        {
            return Find(new Range(0, NativeScintilla.GetTextLength(), Scintilla), findExpression, searchUp);
        }


        public Range Find(string searchString)
        {
            return this.Find(0, NativeScintilla.GetTextLength(), searchString, this._flags);
        }


        public Range Find(string searchString, bool searchUp)
        {
            if (searchUp)
                return this.Find(NativeScintilla.GetTextLength(), 0, searchString, this._flags);
            else
                return this.Find(0, NativeScintilla.GetTextLength(), searchString, this._flags);
        }


        public Range Find(string searchString, SearchFlags searchflags)
        {
            return Find(0, NativeScintilla.GetTextLength(), searchString, searchflags);
        }


        public Range Find(string searchString, SearchFlags searchflags, bool searchUp)
        {
            if (searchUp)
                return Find(NativeScintilla.GetTextLength(), 0, searchString, searchflags);
            else
                return Find(0, NativeScintilla.GetTextLength(), searchString, searchflags);
        }


        public List<Range> FindAll(int startPos, int endPos, Regex findExpression)
        {
            return FindAll(new Range(startPos, endPos, Scintilla), findExpression);
        }


        public List<Range> FindAll(int startPos, int endPos, string searchString, SearchFlags flags)
        {
            var res = new List<Range>();

            while (true)
            {
                Range r = Find(startPos, endPos, searchString, flags);
                if (r == null)
                {
                    break;
                }
                else
                {
                    res.Add(r);
                    startPos = r.End;
                }
            }
            return res;
        }


        public List<Range> FindAll(Range rangeToSearch, Regex findExpression)
        {
            var res = new List<Range>();

            while (true)
            {
                Range r = Find(rangeToSearch, findExpression);
                if (r == null)
                {
                    break;
                }
                else
                {
                    res.Add(r);
                    rangeToSearch = new Range(r.End, rangeToSearch.End, Scintilla);
                }
            }
            return res;
        }


        public List<Range> FindAll(Range rangeToSearch, string searchString)
        {
            return this.FindAll(rangeToSearch.Start, rangeToSearch.End, searchString, this._flags);
        }


        public List<Range> FindAll(Range rangeToSearch, string searchString, SearchFlags flags)
        {
            return this.FindAll(rangeToSearch.Start, rangeToSearch.End, searchString, this._flags);
        }


        public List<Range> FindAll(Regex findExpression)
        {
            return this.FindAll(0, NativeScintilla.GetTextLength(), findExpression);
        }


        public List<Range> FindAll(string searchString)
        {
            return this.FindAll(searchString, this._flags);
        }


        public List<Range> FindAll(string searchString, SearchFlags flags)
        {
            return this.FindAll(0, NativeScintilla.GetTextLength(), searchString, flags);
        }


        public Range FindNext(Regex findExpression)
        {
            return FindNext(findExpression, false);
        }


        public Range FindNext(Regex findExpression, bool wrap)
        {
            Range r = this.Find(NativeScintilla.GetCurrentPos(), NativeScintilla.GetTextLength(), findExpression);
            if (r != null)
                return r;
            else if (wrap)
                return this.Find(0, NativeScintilla.GetCurrentPos(), findExpression);
            else
                return null;
        }


        public Range FindNext(Regex findExpression, bool wrap, Range searchRange)
        {
            int caret = Scintilla.Caret.Position;
            if (!searchRange.PositionInRange(caret))
                return Find(searchRange.Start, searchRange.End, findExpression, false);

            Range r = Find(caret, searchRange.End, findExpression);
            if (r != null)
                return r;
            else if (wrap)
                return Find(searchRange.Start, caret, findExpression);
            else
                return null;
        }


        public Range FindNext(string searchString)
        {
            return this.FindNext(searchString, true, this._flags);
        }


        public Range FindNext(string searchString, bool wrap)
        {
            return this.FindNext(searchString, wrap, this._flags);
        }


        public Range FindNext(string searchString, bool wrap, SearchFlags flags)
        {
            Range r = Find(NativeScintilla.GetCurrentPos(), NativeScintilla.GetTextLength(), searchString, flags);
            if (r != null)
                return r;
            else if (wrap)
                return Find(0, NativeScintilla.GetCurrentPos(), searchString, flags);
            else
                return null;
        }


        public Range FindNext(string searchString, bool wrap, SearchFlags flags, Range searchRange)
        {
            int caret = Scintilla.Caret.Position;
            if (!searchRange.PositionInRange(caret))
                return Find(searchRange.Start, searchRange.End, searchString, flags);

            Range r = Find(caret, searchRange.End, searchString, flags);
            if (r != null)
                return r;
            else if (wrap)
                return Find(searchRange.Start, caret, searchString, flags);
            else
                return null;
        }


        public Range FindNext(string searchString, SearchFlags flags)
        {
            return FindNext(searchString, true, flags);
        }


        public Range FindPrevious(Regex findExpression)
        {
            return FindPrevious(findExpression, false);
        }


        public Range FindPrevious(Regex findExpression, bool wrap)
        {
            Range r = this.Find(0, NativeScintilla.GetAnchor(), findExpression, true);
            if (r != null)
                return r;
            else if (wrap)
                return this.Find(NativeScintilla.GetCurrentPos(), NativeScintilla.GetTextLength(), findExpression, true);
            else
                return null;

        }


        public Range FindPrevious(Regex findExpression, bool wrap, Range searchRange)
        {
            int caret = Scintilla.Caret.Position;
            if (!searchRange.PositionInRange(caret))
                return Find(searchRange.Start, searchRange.End, findExpression, true);

            int anchor = Scintilla.Caret.Anchor;
            if (!searchRange.PositionInRange(anchor))
                anchor = caret;

            Range r = Find(searchRange.Start, anchor, findExpression, true);
            if (r != null)
                return r;
            else if (wrap)
                return Find(anchor, searchRange.End, findExpression, true);
            else
                return null;
        }


        public Range FindPrevious(string searchString)
        {
            return this.FindPrevious(searchString, true, this._flags);
        }


        public Range FindPrevious(string searchString, bool wrap)
        {
            return this.FindPrevious(searchString, wrap, this._flags);
        }


        public Range FindPrevious(string searchString, bool wrap, SearchFlags flags)
        {
            Range r = Find(NativeScintilla.GetAnchor(), 0, searchString, flags);
            if (r != null)
                return r;
            else if (wrap)
                return Find(NativeScintilla.GetTextLength(), NativeScintilla.GetCurrentPos(), searchString, flags);
            else
                return null;
        }


        public Range FindPrevious(string searchString, bool wrap, SearchFlags flags, Range searchRange)
        {
            int caret = Scintilla.Caret.Position;
            if (!searchRange.PositionInRange(caret))
                return Find(searchRange.End, searchRange.Start, searchString, flags);

            int anchor = Scintilla.Caret.Anchor;
            if (!searchRange.PositionInRange(anchor))
                anchor = caret;

            Range r = Find(anchor, searchRange.Start, searchString, flags);
            if (r != null)
                return r;
            else if (wrap)
                return Find(searchRange.End, anchor, searchString, flags);
            else
                return null;
        }


        public Range FindPrevious(string searchString, SearchFlags flags)
        {
            return FindPrevious(searchString, true, flags);
        }


        public void HighlightAll(IList<Range> foundRanges)
        {
            foreach (Range r in foundRanges)
            {
                r.SetIndicator(this.Indicator.Number);
            }
        }


        public void IncrementalSearch()
        {
            this._incrementalSearcher.Show();
        }


        public List<MarkerInstance> MarkAll(IList<Range> foundRanges)
        {
            var ret = new List<MarkerInstance>();

            var lastLine = new Line(Scintilla, -1);
            foreach (Range r in foundRanges)
            {
                //	We can of course have multiple instances of a find on a single
                //	line. We don't want to mark this line more than once.
                Line line = r.StartingLine;
                if (line.Number > lastLine.Number)
                    ret.Add(this.Marker.AddInstanceTo(r.StartingLine));
                lastLine = line;
            }

            return ret;
        }


        public List<Range> ReplaceAll(int startPos, int endPos, Regex findExpression, string replaceString)
        {
            return ReplaceAll(new Range(startPos, endPos, Scintilla), findExpression, replaceString);
        }


        public List<Range> ReplaceAll(int startPos, int endPos, string searchString, string replaceString, SearchFlags flags)
        {
            var ret = new List<Range>();

            Scintilla.UndoRedo.BeginUndoAction();

            int diff = replaceString.Length - searchString.Length;
            while (true)
            {
                Range r = Find(startPos, endPos, searchString, flags);
                if (r == null)
                {
                    break;
                }
                else
                {
                    r.Text = replaceString;
                    r.End = startPos = r.Start + replaceString.Length;
                    endPos += diff;

                    ret.Add(r);
                }
            }

            Scintilla.UndoRedo.EndUndoAction();
            return ret;
        }


        public List<Range> ReplaceAll(Range rangeToSearch, Regex findExpression, string replaceString)
        {
            Scintilla.UndoRedo.BeginUndoAction();

            //	I tried using an anonymous delegate for this but it didn't work too well.
            //	It's too bad because it was a lot cleaner than using member variables as
            //	psuedo globals.
            this._lastReplaceAllMatches = new List<Range>();
            this._lastReplaceAllReplaceString = replaceString;
            this._lastReplaceAllRangeToSearch = rangeToSearch;
            this._lastReplaceAllOffset = 0;

            findExpression.Replace(rangeToSearch.Text, this.ReplaceAllEvaluator);

            Scintilla.UndoRedo.EndUndoAction();

            //	No use having these values hanging around wasting memory :)
            List<Range> ret = this._lastReplaceAllMatches;
            this._lastReplaceAllMatches = null;
            this._lastReplaceAllReplaceString = null;
            this._lastReplaceAllRangeToSearch = null;

            return ret;
        }


        public List<Range> ReplaceAll(Range rangeToSearch, string searchString, string replaceString)
        {
            return this.ReplaceAll(rangeToSearch.Start, rangeToSearch.End, searchString, replaceString, this._flags);
        }


        public List<Range> ReplaceAll(Range rangeToSearch, string searchString, string replaceString, SearchFlags flags)
        {
            return this.ReplaceAll(rangeToSearch.Start, rangeToSearch.End, searchString, replaceString, this._flags);
        }


        public List<Range> ReplaceAll(Regex findExpression, string replaceString)
        {
            return this.ReplaceAll(0, NativeScintilla.GetTextLength(), findExpression, replaceString);
        }


        public List<Range> ReplaceAll(string searchString, string replaceString)
        {
            return this.ReplaceAll(searchString, replaceString, this._flags);
        }


        public List<Range> ReplaceAll(string searchString, string replaceString, SearchFlags flags)
        {
            return this.ReplaceAll(0, NativeScintilla.GetTextLength(), searchString, replaceString, flags);
        }


        private string ReplaceAllEvaluator(Match m)
        {
            //	So this method is called for every match

            //	We make a replacement in the range based upon
            //	the match range.
            string replacement = m.Result(this._lastReplaceAllReplaceString);
            int start = this._lastReplaceAllRangeToSearch.Start + m.Index + this._lastReplaceAllOffset;
            int end = start + m.Length;

            var r = new Range(start, end, Scintilla);
            this._lastReplaceAllMatches.Add(r);
            r.Text = replacement;

            //	But because we've modified the document, the RegEx
            //	match ranges are going to be different from the
            //	document ranges. We need to compensate
            this._lastReplaceAllOffset += replacement.Length - m.Value.Length;
            return replacement;
        }


        public Range ReplaceNext(string searchString, string replaceString)
        {
            return this.ReplaceNext(searchString, replaceString, true, this._flags);
        }


        public Range ReplaceNext(string searchString, string replaceString, bool wrap)
        {
            return this.ReplaceNext(searchString, replaceString, wrap, this._flags);
        }


        public Range ReplaceNext(string searchString, string replaceString, bool wrap, SearchFlags flags)
        {
            Range r = FindNext(searchString, wrap, flags);

            if (r != null)
            {
                r.Text = replaceString;
                r.End = r.Start + replaceString.Length;
            }

            return r;
        }


        public Range ReplaceNext(string searchString, string replaceString, SearchFlags flags)
        {
            return this.ReplaceNext(searchString, replaceString, true, flags);
        }


        public Range ReplacePrevious(string searchString, string replaceString)
        {
            return this.ReplacePrevious(searchString, replaceString, true, this._flags);
        }


        public Range ReplacePrevious(string searchString, string replaceString, bool wrap)
        {
            return this.ReplacePrevious(searchString, replaceString, wrap, this._flags);
        }


        public Range ReplacePrevious(string searchString, string replaceString, bool wrap, SearchFlags flags)
        {
            Range r = FindPrevious(searchString, wrap, flags);

            if (r != null)
            {
                r.Text = replaceString;
                r.End = r.Start + replaceString.Length;
            }

            return r;
        }


        public Range ReplacePrevious(string searchString, string replaceString, SearchFlags flags)
        {
            return this.ReplacePrevious(searchString, replaceString, true, flags);
        }


        private void ResetFlags()
        {
            this._flags = SearchFlags.Empty;
        }


        private void ResetIndicator()
        {
            this._indicator.Reset();
        }


        private void ResetMarker()
        {
            this._marker.Reset();
            this._marker.Number = 10;
        }


        internal bool ShouldSerialize()
        {
            return this.ShouldSerializeFlags() ||
                this.ShouldSerializeIndicator() ||
                this.ShouldSerializeMarker();
        }


        private bool ShouldSerializeFlags()
        {
            return this._flags != SearchFlags.Empty;
        }


        private bool ShouldSerializeIndicator()
        {
            return this._indicator.Number != 16 || this._indicator.Color != Color.Purple || this._indicator.IsDrawnUnder;
        }


        private bool ShouldSerializeMarker()
        {
            return this._marker.Number != 10 || this._marker.ForeColor != Color.White || this._marker.BackColor != Color.Black || this._marker.Symbol != MarkerSymbol.Arrows;
        }


        public void ShowFind()
        {
            if (!this._window.Visible)
                //_window.Show(Scintilla.FindForm());
                if (ParentDock == null)
                    return;
				this._window.Show(ParentDock);
            this._window.tabAll.SelectedTab = this._window.tabAll.TabPages["tpgFind"];

            Range selRange = Scintilla.Selection.Range;
            if (selRange.IsMultiLine)
            {
                this._window.chkSearchSelectionF.Checked = true;
            }
            else if (selRange.Length > 0)
            {
                this._window.cboFindF.Text = selRange.Text;
            }

            this._window.cboFindF.Select();
            this._window.cboFindF.SelectAll();
        }


        public void ShowReplace()
        {
            if (!this._window.Visible)
                if (ParentDock == null)
                    return;
				this._window.Show(ParentDock);
                //_window.Show(Scintilla.FindForm());
            this._window.tabAll.SelectedTab = this._window.tabAll.TabPages["tpgReplace"];

            Range selRange = Scintilla.Selection.Range;
            if (selRange.IsMultiLine)
            {
                this._window.chkSearchSelectionR.Checked = true;
            }
            else if (selRange.Length > 0)
            {
                this._window.cboFindR.Text = selRange.Text;
            }

            this._window.cboFindR.Select();
            this._window.cboFindR.SelectAll();
        }

        #endregion Methods


        #region Properties

        [Editor(typeof(FlagEnumUIEditor), typeof(UITypeEditor))]
        public SearchFlags Flags
        {
            get
            {
                return this._flags;
            }
            set
            {
                this._flags = value;
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public IncrementalSearcher IncrementalSearcher
        {
            get
            {
                return this._incrementalSearcher;
            }
            set
            {
                this._incrementalSearcher = value;
            }
        }


        public Indicator Indicator
        {
            get
            {
                return this._indicator;
            }
            set
            {
                this._indicator = value;
            }
        }


        public Marker Marker
        {
            get
            {
                return this._marker;
            }
            set
            {
                this._marker = value;
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public FindReplaceDialog Window
        {
            get
            {
                return this._window;
            }
            set
            {
                this._window = value;
            }
        }

        #endregion Properties


        #region Constructors

        internal FindReplace(Scintilla scintilla) : base(scintilla) 
        {
            this._marker = scintilla.Markers[10];
            this._marker.SetSymbolInternal(MarkerSymbol.Arrows);
            this._indicator = scintilla.Indicators[16];
            this._indicator.Color = Color.Purple;
            this._indicator.Style = IndicatorStyle.RoundBox;


            this._window = new FindReplaceDialog
            {
                Scintilla = scintilla
            };

            this._incrementalSearcher = new IncrementalSearcher
            {
                Scintilla = scintilla,
                Visible = false
            };
            scintilla.Controls.Add(this._incrementalSearcher);
        }

        #endregion Constructors
    }
}

