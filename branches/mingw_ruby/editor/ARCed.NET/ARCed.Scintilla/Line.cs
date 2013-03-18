#region Using Directives

using System.Collections.Generic;

#endregion

namespace ARCed.Scintilla
{
    public class Line : ScintillaHelperBase
    {
        #region Fields

        private int _number;

        #endregion Fields


        #region Methods

        public MarkerInstance AddMarker(int markerNumber)
        {
            return new MarkerInstance(Scintilla, new Marker(Scintilla, markerNumber), NativeScintilla.MarkerAdd(this._number, markerNumber));
        }


        public MarkerInstance AddMarker(Marker marker)
        {
            return new MarkerInstance(Scintilla, marker, NativeScintilla.MarkerAdd(this._number, marker.Number));
        }


        public Line AddMarkerSet(uint markerMask)
        {
            NativeScintilla.MarkerAddSet(this._number, markerMask);
            return this;
        }


        public Line AddMarkerSet(IEnumerable<Marker> markers)
        {
            AddMarkerSet(Utilities.GetMarkerMask(markers));
            return this;
        }


        public Line AddMarkerSet(IEnumerable<int> markers)
        {
            AddMarkerSet(Utilities.GetMarkerMask(markers));
            return this;
        }


        public Line DeleteAllMarkers()
        {
            this.DeleteMarker(-1);
            return this;
        }


        public Line DeleteMarker(int markerNumber)
        {
            NativeScintilla.MarkerDelete(this._number, markerNumber);
            return this;
        }


        public Line DeleteMarker(Marker marker)
        {
            NativeScintilla.MarkerDelete(this._number, marker.Number);
            return this;
        }


        public Line DeleteMarkerSet(IEnumerable<int> markerNumbers)
        {
            foreach (int markerNumber in markerNumbers)
                NativeScintilla.MarkerDelete(this._number, markerNumber);

            return this;
        }


        public Line DeleteMarkerSet(IEnumerable<Marker> markers)
        {
            foreach (Marker m in markers)
                NativeScintilla.MarkerDelete(this._number, m.Number);

            return this;
        }


        public void EnsureVisible()
        {
            NativeScintilla.EnsureVisible(this._number);
        }


        public override bool Equals(object obj)
        {
            var l = obj as Line;
            if (l == null)
                return false;

            return l.Scintilla == Scintilla && l._number == this._number;
        }


        public Line FindNextMarker(Marker marker)
        {
            return FindNextMarker(marker.Mask);
        }


        public Line FindNextMarker(uint markerMask)
        {
            int foundLine = NativeScintilla.MarkerNext(this._number + 1, markerMask);
            if (foundLine < 0)
                return null;

            return Scintilla.Lines[foundLine];
        }


        public Line FindNextMarker(IEnumerable<int> markers)
        {
            return FindNextMarker(Utilities.GetMarkerMask(markers));
        }


        public Line FindNextMarker(IEnumerable<Marker> markers)
        {
            return FindNextMarker(Utilities.GetMarkerMask(markers));
        }


        public Line FindPreviousMarker(Marker marker)
        {
            return FindPreviousMarker(marker.Mask);
        }


        public Line FindPreviousMarker(uint markerMask)
        {
            int foundLine = NativeScintilla.MarkerPrevious(this._number - 1, markerMask);
            if (foundLine < 0)
                return null;

            return Scintilla.Lines[foundLine];
        }


        public Line FindPreviousMarker(IEnumerable<int> markers)
        {
            return FindPreviousMarker(Utilities.GetMarkerMask(markers));
        }


        public Line FindPreviousMarker(IEnumerable<Marker> markers)
        {
            return FindPreviousMarker(Utilities.GetMarkerMask(markers));
        }


        public override int GetHashCode()
        {
            return base.GetHashCode();
        }


        public Line GetLastFoldChild()
        {
            return this.GetLastFoldChild(-1);
        }


        public Line GetLastFoldChild(int level)
        {
            int num = NativeScintilla.GetLastChild(this._number, level);
            if (num < 0)
                return null;

            return new Line(Scintilla, num);
        }


        public int GetMarkerMask()
        {
            return NativeScintilla.MarkerGet(this._number);
        }


        public List<Marker> GetMarkers()
        {
            var ret = new List<Marker>();
            int mask = this.GetMarkerMask();
            int bit = 1;
            for (int i = 0; i < 32; ++i)
            {
                if ((mask & bit) != 0)
                    ret.Add(new Marker(Scintilla, i));
                bit = bit + bit;
            }

            return ret;
        }


        public void Goto()
        {
            NativeScintilla.GotoLine(this._number);
        }


        public void Select()
        {
            NativeScintilla.SetSel(this.StartPosition, this.EndPosition);
        }


        public void ToggleFoldExpanded()
        {
            NativeScintilla.ToggleFold(this._number);
        }


        public override string ToString()
        {
            return "Line " + this._number.ToString();
        }

        #endregion Methods


        #region Properties

        public int EndPosition
        {
            get
            {
                return NativeScintilla.GetLineEndPosition(this._number);
            }
        }


        public bool FoldExpanded
        {
            get
            {
                return NativeScintilla.GetFoldExpanded(this._number);
            }
            set
            {
                NativeScintilla.SetFoldExpanded(this._number, value);
            }
        }


        public int FoldLevel
        {
            get
            {
                return (int)(NativeScintilla.GetFoldLevel(this._number) & Constants.SC_FOLDLEVELNUMBERMASK);
            }
            set
            {
                uint flags = NativeScintilla.GetFoldLevel(this._number) & (Constants.SC_FOLDLEVELHEADERFLAG | Constants.SC_FOLDLEVELWHITEFLAG);
                NativeScintilla.SetFoldLevel(this._number, (uint)value | flags);
            }
        }


        public Line FoldParent
        {
            get
            {
                int num = NativeScintilla.GetFoldParent(this._number);
                if (num < 0)
                    return null;

                return new Line(Scintilla, num);
            }
        }


        public int Height
        {
            get
            {
                return NativeScintilla.TextHeight(this._number);
            }
        }


        public int Indentation
        {
            get
            {
                return NativeScintilla.GetLineIndentation(this._number);
            }
            set
            {
                NativeScintilla.SetLineIndentation(this._number, value);
            }
        }


        public int IndentPosition
        {
            get
            {
                return NativeScintilla.GetLineIndentPosition(this._number);
            }
        }


        public bool IsFoldPoint
        {
            get
            {
                return (NativeScintilla.GetFoldLevel(this._number) & Constants.SC_FOLDLEVELHEADERFLAG) == Constants.SC_FOLDLEVELHEADERFLAG;
            }
            set
            {
                if (value)
                    NativeScintilla.SetFoldLevel(this._number, NativeScintilla.GetFoldLevel(this._number) | Constants.SC_FOLDLEVELHEADERFLAG);
                else
                    NativeScintilla.SetFoldLevel(this._number, NativeScintilla.GetFoldLevel(this._number) & ~Constants.SC_FOLDLEVELHEADERFLAG);
            }
        }


        public bool IsFoldWhitespace
        {
            get
            {
                return (NativeScintilla.GetFoldLevel(this._number) & Constants.SC_FOLDLEVELWHITEFLAG) == Constants.SC_FOLDLEVELWHITEFLAG;
            }
            set
            {
                if (value)
                    NativeScintilla.SetFoldLevel(this._number, NativeScintilla.GetFoldLevel(this._number) | Constants.SC_FOLDLEVELWHITEFLAG);
                else
                    NativeScintilla.SetFoldLevel(this._number, NativeScintilla.GetFoldLevel(this._number) & ~Constants.SC_FOLDLEVELWHITEFLAG);
            }
        }


        public bool IsVisible
        {
            get
            {
                return NativeScintilla.GetLineVisible(this._number);
            }
            set
            {
                if (value)
                    NativeScintilla.ShowLines(this._number, this._number);
                else
                    NativeScintilla.HideLines(this._number, this._number);
            }
        }


        public int Length
        {
            get
            {
                return NativeScintilla.LineLength(this._number);
            }
        }


        public int LineState
        {
            get
            {
                return NativeScintilla.GetLineState(this._number);
            }
            set
            {
                NativeScintilla.SetLineState(this._number, value);
            }
        }


        public Line Next
        {
            get
            {
                return new Line(Scintilla, this._number + 1);
            }
        }


        public int Number
        {
            get
            {
                return this._number;
            }
            set
            {
                this._number = value;
            }
        }


        public Line Previous
        {
            get
            {
                return new Line(Scintilla, this._number - 1);
            }
        }


        public Range Range
        {
            get
            {
                return Scintilla.GetRange(this.StartPosition, this.EndPosition);
            }
        }


        public int SelectionEndPosition
        {
            get
            {
                return NativeScintilla.GetLineSelEndPosition(this._number);
            }
        }


        public int SelectionStartPosition
        {
            get
            {
                return NativeScintilla.GetLineSelStartPosition(this._number);
            }
        }


        public int StartPosition
        {
            get
            {
                return NativeScintilla.PositionFromLine(this._number);
            }
        }


        public string Text
        {
            get
            {
                string s;
                NativeScintilla.GetLine(this._number, out s);
                return s;
            }
            set
            {
                NativeScintilla.SetTargetStart(this.StartPosition);
                NativeScintilla.SetTargetEnd(this.EndPosition);
                NativeScintilla.ReplaceTarget(-1, value);
            }
        }


        public int VisibleLineNumber
        {
            get
            {
                return NativeScintilla.VisibleFromDocLine(this._number);
            }
        }

        #endregion Properties


        #region Constructors

        protected internal Line(Scintilla scintilla, int number) : base(scintilla)
        {
            this._number = number;
        }

        #endregion Constructors
    }
}
