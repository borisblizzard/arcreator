#region Using Directives

using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;

#endregion


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Defines a marker's appearance in a <see cref="Scintilla"/> control.
    /// </summary>
    [TypeConverter(typeof(ExpandableObjectConverter))]
    public class Marker : ScintillaHelperBase
    {
        #region Fields

        private int _number;

        #endregion Fields


        #region Methods

        public MarkerInstance AddInstanceTo(int line)
        {
            return new MarkerInstance(Scintilla, this, NativeScintilla.MarkerAdd(line, this._number));
        }


        public MarkerInstance AddInstanceTo(Line line)
        {
            return AddInstanceTo(line.Number);
        }


        public override bool Equals(object obj)
        {
            if (!IsSameHelperFamily(obj))
                return false;

            return ((Marker)obj).Number == this.Number;
            
        }


        public override int GetHashCode()
        {
            return base.GetHashCode();
        }


        public void Reset()
        {
            this.ResetAlpha();
            this.ResetBackColor();
            this.ResetForeColor();
            this.ResetSymbol();
        }


        private void ResetAlpha()
        {
            this.Alpha = 0xff;
        }


        private void ResetBackColor()
        {
            this.BackColor = Color.White;
        }


        private void ResetForeColor()
        {
            this.ForeColor = Color.Black;
        }


        private void ResetSymbol()
        {
            this.Symbol = MarkerSymbol.Circle;
        }


        internal void SetBackColorInternal(Color value)
        {
            Scintilla.ColorBag[this + ".BackColor"] = value;
            NativeScintilla.MarkerSetBack(this._number, Utilities.ColorToRgb(value));
        }


        internal void SetForeColorInternal(Color value)
        {
            Scintilla.ColorBag[this + ".ForeColor"] = value;
            NativeScintilla.MarkerSetFore(this._number, Utilities.ColorToRgb(value));
        }


        public void SetImage(string xpmImage)
        {
            NativeScintilla.MarkerDefinePixmap(this._number, xpmImage);
        }


        public void SetImage(Bitmap image)
        {
            NativeScintilla.MarkerDefinePixmap(this._number, XpmConverter.ConvertToXPM(image));
        }


        public void SetImage(Bitmap image, Color transparentColor)
        {
            NativeScintilla.MarkerDefinePixmap(this._number, XpmConverter.ConvertToXPM(image, Utilities.ColorToHtml(transparentColor)));
        }


        internal void SetSymbolInternal(MarkerSymbol value)
        {
            Scintilla.PropertyBag[this + ".Symbol"] = value;
            NativeScintilla.MarkerDefine(this._number, (int)value);
        }


        internal bool ShouldSerialize()
        {
            return this.ShouldSerializeAlpha() ||
                this.ShouldSerializeBackColor() ||
                this.ShouldSerializeForeColor() ||
                this.ShouldSerializeSymbol();
        }


        private bool ShouldSerializeAlpha()
        {
            return this.Alpha != 0xff;
        }


        private bool ShouldSerializeBackColor()
        {
            if (Scintilla.Folding.MarkerScheme == FoldMarkerScheme.Custom)
                return this.BackColor != Color.White;

            return false;
        }


        private bool ShouldSerializeForeColor()
        {
            if (Scintilla.Folding.MarkerScheme == FoldMarkerScheme.Custom)
                return this.ForeColor != Color.Black;

            return false;
        }


        private bool ShouldSerializeSymbol()
        {
            if (Scintilla.Folding.MarkerScheme == FoldMarkerScheme.Custom)
                return this.Symbol != MarkerSymbol.Circle;

            return false;
        }


        public override string ToString()
        {
            return "MarkerNumber" + this._number;
        }

        #endregion Methods


        #region Properties

        public int Alpha
        {
            get
            {

                try
                {
                    if (Scintilla.PropertyBag.ContainsKey(this + ".Alpha"))
                        return (int)Scintilla.PropertyBag[this + ".Alpha"];

                    return 0xff;
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.ToString());
                    return 0xff;
                }
            }
            set
            {
                Scintilla.PropertyBag[this + ".Alpha"] = value;
                NativeScintilla.MarkerSetAlpha(this._number, value);
            }
        }


        public Color BackColor
        {
            get
            {
                if (Scintilla.ColorBag.ContainsKey(this + ".BackColor"))
                    return Scintilla.ColorBag[this + ".BackColor"];

                return Color.White;
            }
            set
            {
                this.SetBackColorInternal(value);
                Scintilla.Folding.MarkerScheme = FoldMarkerScheme.Custom;
            }
        }


        public Color ForeColor
        {
            get
            {
                if (Scintilla.ColorBag.ContainsKey(this + ".ForeColor"))
                    return Scintilla.ColorBag[this + ".ForeColor"];

                return Color.Black;
            }
            set
            {
                this.SetForeColorInternal(value);
                Scintilla.Folding.MarkerScheme = FoldMarkerScheme.Custom;
            }
        }


        public uint Mask
        {
            get
            {
                uint result = ((uint)1) << this.Number;
                return result;
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


        /// <summary>
        ///     Gets or sets the marker symbol.
        /// </summary>
        /// <returns>One of the <see cref="MarkerSymbol" /> values. The default is <see cref="MarkerSymbol.Circle" />.</returns>
        /// <exception cref="InvalidEnumArgumentException">
        ///     The value assigned is not one of the <see cref="MarkerSymbol" /> values.
        /// </exception>
        public MarkerSymbol Symbol
        {
            get
            {
                if (Scintilla.PropertyBag.ContainsKey(this + ".Symbol"))
                    return (MarkerSymbol)Scintilla.PropertyBag[this + ".Symbol"];

                return MarkerSymbol.Circle;
            }
            set
            {
                if (!Enum.IsDefined(typeof(MarkerSymbol), value))
                    throw new InvalidEnumArgumentException("value", (int)value, typeof(MarkerSymbol));

                if (value != this.Symbol)
                {
                    this.SetSymbolInternal(value);
                    Scintilla.Folding.MarkerScheme = FoldMarkerScheme.Custom;
                }
            }
        }

        #endregion Properties


        #region Constructors

        internal Marker(Scintilla scintilla, int number) : base(scintilla)
        {
            this._number = number;
        }

        #endregion Constructors
    }
}
