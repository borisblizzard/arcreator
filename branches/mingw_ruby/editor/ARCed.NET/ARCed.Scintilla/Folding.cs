#region Using Directives

using System.ComponentModel;
using System.Drawing;
using System.Drawing.Design;
using ARCed.Scintilla.Design;

#endregion


namespace ARCed.Scintilla
{
    [TypeConverter(typeof(ExpandableObjectConverter))]
    public class Folding : TopLevelHelper
    {
        #region Fields

        private FoldFlag _flags;
        private FoldMarkerScheme _markerScheme;

        #endregion Fields


        #region Methods

        private void ResetFlags()
        {
            this.Flags = 0;
        }


        private void ResetIsEnabled()
        {
            this.IsEnabled = true;
        }


        private void ResetMarkerScheme()
        {
            this.MarkerScheme = FoldMarkerScheme.BoxPlusMinus;
        }


        private void ResetUseCompactFolding()
        {
            this.UseCompactFolding = false;
        }


        internal bool ShouldSerialize()
        {
            return this.ShouldSerializeFlags() ||
                this.ShouldSerializeIsEnabled() ||
                this.ShouldSerializeMarkerScheme() ||
                this.ShouldSerializeUseCompactFolding();
        }


        private bool ShouldSerializeFlags()
        {
            return (int)this.Flags != 0;
        }


        private bool ShouldSerializeIsEnabled()
        {
            return !this.IsEnabled;
        }


        private bool ShouldSerializeMarkerScheme()
        {
            return this._markerScheme != FoldMarkerScheme.BoxPlusMinus;
        }


        private bool ShouldSerializeUseCompactFolding()
        {
            return this.UseCompactFolding;
        }

        #endregion Methods


        #region Properties

        /// <summary>
        ///     Read or change the Flags associated with a fold. The default value is 0.
        /// </summary>
        [Editor(typeof(FlagEnumUIEditor), typeof(UITypeEditor)), Category("Appearance")]
        public FoldFlag Flags
        {
            get
            {
                return this._flags;
            }
            set
            {
                this._flags = value;
                NativeScintilla.SetFoldFlags((int)value);
            }
        }


        public bool IsEnabled
        {
            get
            {
                return Scintilla.Lexing.GetProperty("fold") == "1";
            }
            set
            {
                string s;
                if (value)
                    s = "1";
                else
                    s = "0";

                Scintilla.Lexing.SetProperty("fold", s);
                Scintilla.Lexing.SetProperty("fold.html", s);
            }
        }


        /// <summary>
        ///     Read or change the Fold Marker Scheme. This changes the way Scintilla displays folds
        ///     in the control. The default is BoxPlusMinus and the value Custom can be used to disable
        ///     ARCed.Scintilla changing selections made directly using MarkerCollection.FolderXX methods. 
        /// </summary>
        public FoldMarkerScheme MarkerScheme
        {
            get
            {
                return this._markerScheme;
            }
            set
            {
                this._markerScheme = value;

                if (value == FoldMarkerScheme.Custom)
                    return;

                MarkerCollection mc = Scintilla.Markers;

                mc.Folder.SetBackColorInternal(Color.Gray);
                mc.FolderEnd.SetBackColorInternal(Color.Gray);
                mc.FolderOpen.SetBackColorInternal(Color.Gray);
                mc.FolderOpenMid.SetBackColorInternal(Color.Gray);
                mc.FolderOpenMidTail.SetBackColorInternal(Color.Gray);
                mc.FolderSub.SetBackColorInternal(Color.Gray);
                mc.FolderTail.SetBackColorInternal(Color.Gray);

                mc.Folder.SetForeColorInternal(Color.White);
                mc.FolderEnd.SetForeColorInternal(Color.White);
                mc.FolderOpen.SetForeColorInternal(Color.White);
                mc.FolderOpenMid.SetForeColorInternal(Color.White);
                mc.FolderOpenMidTail.SetForeColorInternal(Color.White);
                mc.FolderSub.SetForeColorInternal(Color.White);
                mc.FolderTail.SetForeColorInternal(Color.White);

                switch (value)
                {
                    case FoldMarkerScheme.Arrow:
                        mc.Folder.SetSymbolInternal(MarkerSymbol.Arrow);
                        mc.FolderEnd.SetSymbolInternal(MarkerSymbol.Empty);
                        mc.FolderOpen.SetSymbolInternal(MarkerSymbol.ArrowDown);
                        mc.FolderOpenMid.SetSymbolInternal(MarkerSymbol.Empty);
                        mc.FolderOpenMidTail.SetSymbolInternal(MarkerSymbol.Empty);
                        mc.FolderSub.SetSymbolInternal(MarkerSymbol.Empty);
                        mc.FolderTail.SetSymbolInternal(MarkerSymbol.Empty);
                        break;
                    case FoldMarkerScheme.BoxPlusMinus:
                        mc.Folder.SetSymbolInternal(MarkerSymbol.BoxPlus);
                        mc.FolderEnd.SetSymbolInternal(MarkerSymbol.BoxPlusConnected);
                        mc.FolderOpen.SetSymbolInternal(MarkerSymbol.BoxMinus);
                        mc.FolderOpenMid.SetSymbolInternal(MarkerSymbol.BoxMinusConnected);
                        mc.FolderOpenMidTail.SetSymbolInternal(MarkerSymbol.TCorner);
                        mc.FolderSub.SetSymbolInternal(MarkerSymbol.VLine);
                        mc.FolderTail.SetSymbolInternal(MarkerSymbol.LCorner);
                        break;
                    case FoldMarkerScheme.CirclePlusMinus:
                        mc.Folder.SetSymbolInternal(MarkerSymbol.CirclePlus);
                        mc.FolderEnd.SetSymbolInternal(MarkerSymbol.CirclePlusConnected);
                        mc.FolderOpen.SetSymbolInternal(MarkerSymbol.CircleMinus);
                        mc.FolderOpenMid.SetSymbolInternal(MarkerSymbol.CircleMinusConnected);
                        mc.FolderOpenMidTail.SetSymbolInternal(MarkerSymbol.TCornerCurve);
                        mc.FolderSub.SetSymbolInternal(MarkerSymbol.VLine);
                        mc.FolderTail.SetSymbolInternal(MarkerSymbol.LCornerCurve);
                        break;
                    case FoldMarkerScheme.PlusMinus:
                        mc.Folder.SetSymbolInternal(MarkerSymbol.Plus);
                        mc.FolderEnd.SetSymbolInternal(MarkerSymbol.Empty);
                        mc.FolderOpen.SetSymbolInternal(MarkerSymbol.Minus);
                        mc.FolderOpenMid.SetSymbolInternal(MarkerSymbol.Empty);
                        mc.FolderOpenMidTail.SetSymbolInternal(MarkerSymbol.Empty);
                        mc.FolderSub.SetSymbolInternal(MarkerSymbol.Empty);
                        mc.FolderTail.SetSymbolInternal(MarkerSymbol.Empty);
                        break;
                }
            }
        }


        /// <summary>
        ///     Read or change the value controlling whether to use compact folding from the lexer.
        /// </summary>
        /// <remarks>This tracks the property "fold.compact"</remarks>
        public bool UseCompactFolding
        {
            get
            {
                return Scintilla.Lexing.GetProperty("fold.compact") == "1";
            }
            set
            {
                string val = "0";

                if (value)
                    val = "1";

                Scintilla.Lexing.SetProperty("fold.compact", val);
            }
        }

        #endregion Properties


        #region Constructors

        internal Folding(Scintilla scintilla) : base(scintilla) 
        {
            this.IsEnabled = true;
            this.UseCompactFolding = false;
            this.MarkerScheme = FoldMarkerScheme.BoxPlusMinus;
        }

        #endregion Constructors
    }

}
