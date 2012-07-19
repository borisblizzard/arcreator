#region Using Directives

using System;
using System.Collections.Generic;
using System.ComponentModel;

#endregion


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Represents a collection of <see cref="Marker" /> objects and options in a <see cref="Scintilla" /> control.
    /// </summary>
    [TypeConverter(typeof(ExpandableObjectConverter))]
    public class MarkerCollection : TopLevelHelper
    {
        #region Methods

        public void AddInstanceSet(int line, uint markerMask)
        {
            NativeScintilla.MarkerAddSet(line, markerMask);
        }


        public void AddInstanceSet(Line line, uint markerMask)
        {
            AddInstanceSet(line.Number, markerMask);
        }


        public void AddInstanceSet(Line line, IEnumerable<Marker> markers)
        {
            AddInstanceSet(line, Utilities.GetMarkerMask(markers));
        }


        public void DeleteAll()
        {
            NativeScintilla.MarkerDeleteAll(-1);
        }


        public void DeleteAll(int marker)
        {
            NativeScintilla.MarkerDeleteAll(marker);
        }


        public void DeleteAll(Marker marker)
        {
            NativeScintilla.MarkerDeleteAll(marker.Number);
        }


        public void DeleteInstance(int line, int markerNumber)
        {
            NativeScintilla.MarkerDelete(line, markerNumber);
        }


        public void DeleteInstance(int line, Marker marker)
        {
            DeleteInstance(line, marker.Number);
        }


        public Line FindNextMarker()
        {
            unchecked
            {
                return this.FindNextMarker(this.NextLine(), UInt32.MaxValue);
            }
        }


        public Line FindNextMarker(Marker marker)
        {
            return this.FindNextMarker(this.NextLine(), (uint)marker.Number);
        }


        public Line FindNextMarker(uint markerMask)
        {
            return FindNextMarker(this.NextLine(), markerMask);
        }


        public Line FindNextMarker(IEnumerable<int> markers)
        {
            return FindNextMarker(this.NextLine(), Utilities.GetMarkerMask(markers));
        }


        public Line FindNextMarker(IEnumerable<Marker> markers)
        {
            return FindNextMarker(this.NextLine(), Utilities.GetMarkerMask(markers));
        }


        public Line FindNextMarker(int line)
        {
            return FindNextMarker(line, UInt32.MaxValue);
        }


        public Line FindNextMarker(Line line)
        {
            return FindNextMarker(line.Number, UInt32.MaxValue);
        }


        public Line FindNextMarker(int line, uint markerMask)
        {
            int foundLine = NativeScintilla.MarkerNext(line, markerMask);
            if (foundLine < 0)
                return null;

            return new Line(Scintilla, foundLine);
        }


        public Line FindNextMarker(Line line, uint markerMask)
        {
            return FindNextMarker(line.Number, markerMask);
        }


        public Line FindNextMarker(Line line, Marker marker)
        {
            return FindNextMarker(line.Number, (uint)marker.Number);
        }


        public Line FindNextMarker(Line line, IEnumerable<int> markers)
        {
            return FindNextMarker(line.Number, Utilities.GetMarkerMask(markers));
        }


        public Line FindNextMarker(Line line, IEnumerable<Marker> markers)
        {
            return FindNextMarker(line.Number, Utilities.GetMarkerMask(markers));
        }


        public Line FindNextMarker(int line, Marker marker)
        {
            return FindNextMarker(line, (uint)marker.Number);
        }


        public Line FindPreviousMarker()
        {
            return this.FindPreviousMarker(this.PrevLine(), UInt32.MaxValue);
        }


        public Line FindPreviousMarker(Marker marker)
        {
            return this.FindPreviousMarker(this.PrevLine(), (uint)marker.Number);
        }


        public Line FindPreviousMarker(uint markerMask)
        {
            return FindPreviousMarker(this.PrevLine(), markerMask);
        }


        public Line FindPreviousMarker(int line)
        {
            return FindPreviousMarker(line, UInt32.MaxValue);
        }


        public Line FindPreviousMarker(IEnumerable<int> markers)
        {
            return FindPreviousMarker(this.PrevLine(), Utilities.GetMarkerMask(markers));
        }


        public Line FindPreviousMarker(IEnumerable<Marker> markers)
        {
            return FindPreviousMarker(this.NextLine(), Utilities.GetMarkerMask(markers));
        }


        public Line FindPreviousMarker(Line line)
        {
            return FindPreviousMarker(line.Number, UInt32.MaxValue);
        }


        public Line FindPreviousMarker(int line, uint markerMask)
        {
            int lineNo = NativeScintilla.MarkerPrevious(line, markerMask);
            if (lineNo < 0)
                return null;

            return new Line(Scintilla, lineNo);
        }


        public Line FindPreviousMarker(Line line, uint markerMask)
        {
            return FindPreviousMarker(line.Number, markerMask);
        }


        public Line FindPreviousMarker(Line line, Marker marker)
        {
            return FindPreviousMarker(line.Number, (uint)marker.Number);
        }


        public Line FindPreviousMarker(Line line, IEnumerable<int> markers)
        {
            return FindPreviousMarker(line.Number, Utilities.GetMarkerMask(markers));
        }


        public Line FindPreviousMarker(Line line, IEnumerable<Marker> markers)
        {
            return FindPreviousMarker(line.Number, Utilities.GetMarkerMask(markers));
        }


        public Line FindPreviousMarker(int line, Marker marker)
        {
            return FindPreviousMarker(line, (uint)marker.Number);
        }


        public int GetMarkerMask(int line)
        {
            return NativeScintilla.MarkerGet(line);
        }


        public int GetMarkerMask(Line line)
        {
            return NativeScintilla.MarkerGet(line.Number);
        }


        public List<Marker> GetMarkers(Line line)
        {
            return GetMarkers(line.Number);
        }


        public List<Marker> GetMarkers(int line)
        {
            var ret = new List<Marker>();
            int mask = GetMarkerMask(line);
            for (int i = 0; i < 32; i++)
                if ((mask & i) == i)
                    ret.Add(new Marker(Scintilla, i));

            return ret;
        }


        private int NextLine()
        {
            return NativeScintilla.LineFromPosition(NativeScintilla.GetCurrentPos()) + 1;
        }


        private int PrevLine()
        {
            return NativeScintilla.LineFromPosition(NativeScintilla.GetCurrentPos()) - 1;
        }


        public void Reset()
        {
            for (int i = 0; i < 32; i++)
                this[i].Reset();
        }


        internal bool ShouldSerialize()
        {
            return this.ShouldSerializeFolder() ||
                this.ShouldSerializeFolderEnd() ||
                this.ShouldSerializeFolderOpen() ||
                this.ShouldSerializeFolderOpenMid() ||
                this.ShouldSerializeFolderOpenMidTail() ||
                this.ShouldSerializeFolderSub() ||
                this.ShouldSerializeFolderTail();
        }


        private bool ShouldSerializeFolder()
        {
            return this.Folder.ShouldSerialize();
        }


        private bool ShouldSerializeFolderEnd()
        {
            return this.FolderEnd.ShouldSerialize();
        }


        private bool ShouldSerializeFolderOpen()
        {
            return this.FolderOpen.ShouldSerialize();
        }


        private bool ShouldSerializeFolderOpenMid()
        {
            return this.FolderOpenMid.ShouldSerialize();
        }


        private bool ShouldSerializeFolderOpenMidTail()
        {
            return this.FolderOpenMidTail.ShouldSerialize();
        }


        private bool ShouldSerializeFolderSub()
        {
            return this.FolderSub.ShouldSerialize();
        }


        private bool ShouldSerializeFolderTail()
        {
            return this.FolderTail.ShouldSerialize();
        }

        #endregion Methods


        #region Properties

        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public Marker Folder
        {
            get
            {
                return new Marker(Scintilla, Constants.SC_MARKNUM_FOLDER);
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public Marker FolderEnd
        {
            get
            {
                return new Marker(Scintilla, Constants.SC_MARKNUM_FOLDEREND);
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public Marker FolderOpen
        {
            get
            {
                return new Marker(Scintilla, Constants.SC_MARKNUM_FOLDEROPEN);
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public Marker FolderOpenMid
        {
            get
            {
                return new Marker(Scintilla, Constants.SC_MARKNUM_FOLDEROPENMID);
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public Marker FolderOpenMidTail
        {
            get
            {
                return new Marker(Scintilla, Constants.SC_MARKNUM_FOLDERMIDTAIL);
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public Marker FolderSub
        {
            get
            {
                return new Marker(Scintilla, Constants.SC_MARKNUM_FOLDERSUB);
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public Marker FolderTail
        {
            get
            {
                return new Marker(Scintilla, Constants.SC_MARKNUM_FOLDERTAIL);
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public Marker this[int markerNumber]
        {
            get
            {
                return new Marker(Scintilla, markerNumber);
            }
        }

        #endregion Properties


        #region Constructors

        internal MarkerCollection(Scintilla scintilla) : base(scintilla) { }

        #endregion Constructors
    }
}
