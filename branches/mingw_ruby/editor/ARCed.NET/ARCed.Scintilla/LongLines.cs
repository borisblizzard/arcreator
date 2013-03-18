#region Using Directives

using System.ComponentModel;
using System.Drawing;

#endregion


namespace ARCed.Scintilla
{
    [TypeConverter(typeof(ExpandableObjectConverter))]
    public class LongLines : TopLevelHelper
    {
        #region Methods

        private void ResetEdgeColor()
        {
            this.EdgeColor = Color.Silver;
        }


        private void ResetEdgeColumn()
        {
            this.EdgeColumn = 0;
        }


        private void ResetEdgeMode()
        {
            this.EdgeMode = EdgeMode.None;
        }


        internal bool ShouldSerialize()
        {
            return this.ShouldSerializeEdgeColor() ||
                this.ShouldSerializeEdgeColumn() ||
                this.ShouldSerializeEdgeMode();
        }


        private bool ShouldSerializeEdgeColor()
        {
            return this.EdgeColor != Color.Silver;
        }


        private bool ShouldSerializeEdgeColumn()
        {
            return this.EdgeColumn != 0;
        }


        private bool ShouldSerializeEdgeMode()
        {
            return this.EdgeMode != EdgeMode.None;
        }

        #endregion Methods


        #region Properties

        public Color EdgeColor
        {
            get
            {
                if (Scintilla.ColorBag.ContainsKey("LongLines.EdgeColor"))
                    return Scintilla.ColorBag["LongLines.EdgeColor"];

                return Color.Silver;
            }
            set
            {
                if (value == Color.Silver)
                    Scintilla.ColorBag.Remove("LongLines.EdgeColor");

                Scintilla.ColorBag["LongLines.EdgeColor"] = value;
                NativeScintilla.SetEdgeColour(Utilities.ColorToRgb(value));
            }
        }


        public int EdgeColumn
        {
            get
            {
                return NativeScintilla.GetEdgeColumn();
            }
            set
            {
                NativeScintilla.SetEdgeColumn(value);
            }
        }


        public EdgeMode EdgeMode
        {
            get
            {
                return (EdgeMode)NativeScintilla.GetEdgeMode();
            }
            set
            {
                NativeScintilla.SetEdgeMode((int)value);
            }
        }

        #endregion Properties


        #region Constructors

        internal LongLines(Scintilla scintilla) : base(scintilla) { }

        #endregion Constructors
    }
}
