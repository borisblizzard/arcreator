#region Using Directives

using System.ComponentModel;
using System.Drawing;

#endregion


namespace ARCed.Scintilla
{
    [TypeConverter(typeof(ExpandableObjectConverter))]
    public class Style : ScintillaHelperBase
    {
        #region Fields

        private readonly int _index;

        #endregion Fields


        #region Methods

        public void Apply(int length)
        {
            this.Apply(NativeScintilla.GetCurrentPos(), length);
        }


        public void Apply(int position, int length)
        {
            NativeScintilla.StartStyling(position, 0xff);
            NativeScintilla.SetStyling(length, this._index);
        }


        internal bool BackColorNotSet()
        {
            return !Scintilla.ColorBag.ContainsKey(this + ".BackColor");
        }


        public void CopyTo(Style target)
        {
            target.BackColor = this.BackColor;
            target.Bold = this.Bold;
            target.Case = this.Case;
            target.CharacterSet = this.CharacterSet;
            target.FontName = this.FontName;
            target.ForeColor = this.ForeColor;
            target.IsChangeable = this.IsChangeable;
            target.IsHotspot = this.IsHotspot;
            target.IsSelectionEolFilled = this.IsSelectionEolFilled;
            target.IsVisible = this.IsVisible;
            target.Italic = this.Italic;
            target.Size = this.Size;
            target.Underline = this.Underline;
        }


        public override bool Equals(object obj)
        {
            if (!IsSameHelperFamily(obj))
                return false;

            return ((Style)obj).Index == this.Index;
        }


        internal bool FontNotSet()
        {
            return !Scintilla.PropertyBag.ContainsKey(this + ".FontSet");
        }


        internal bool ForeColorNotSet()
        {
            return !Scintilla.ColorBag.ContainsKey(this + ".ForeColor");
        }


        private Color getDefaultBackColor()
        {
            if (this._index == (int)StylesCommon.CallTip)
                return SystemColors.Info;
            else if (this._index == (int)StylesCommon.LineNumber)
                return SystemColors.Control;

            return Color.FromArgb(0xff, 0xff, 0xff);
        }


        private CharacterSet getDefaultCharacterSet()
        {
            return (CharacterSet)this.getDefaultFont().GdiCharSet;
        }


        private Font getDefaultFont()
        {
            if (this._index == (int)StylesCommon.CallTip)
                return SystemFonts.StatusFont;

            return new Font("Verdana", 8F); 
        }


        private Color getDefaultForeColor()
        {
            if (this._index == (int)StylesCommon.CallTip)
                return SystemColors.InfoText;

            return Color.FromArgb(0, 0, 0);
        }


        public override int GetHashCode()
        {
            return base.GetHashCode();
        }


        public int GetTextWidth(string text)
        {
            return NativeScintilla.TextWidth(this._index, text);
        }


        public void Reset()
        {
            this.ResetBackColor();
            this.ResetBold();
            this.ResetCase();
            this.ResetCharacterSet();
            this.ResetFontName();
            this.ResetForeColor();
            this.ResetIsChangeable();
            this.ResetIsHotspot();
            this.ResetIsSelectionEolFilled();
            this.ResetIsVisible();
            this.ResetItalic();
            this.ResetSize();
            this.ResetUnderline();
        }


        private void ResetBackColor()
        {
            this.BackColor = this.getDefaultBackColor();
        }


        private void ResetBold()
        {
            this.Bold = this.getDefaultFont().Bold;
        }


        private void ResetCase()
        {
            this.Case = StyleCase.Mixed;
        }


        private void ResetCharacterSet()
        {
            this.CharacterSet = this.getDefaultCharacterSet();
        }


        internal void ResetFont()
        {
            this.Font = this.getDefaultFont();
            Scintilla.PropertyBag.Remove(this + ".FontSet");
        }


        private void ResetFontName()
        {
            this.FontName = this.getDefaultFont().Name;
        }


        private void ResetForeColor()
        {
            this.ForeColor = this.getDefaultForeColor();
        }


        private void ResetIsChangeable()
        {
            this.IsChangeable = true;
        }


        private void ResetIsHotspot()
        {
            this.IsHotspot = false;
        }


        private void ResetIsSelectionEolFilled()
        {
            this.IsSelectionEolFilled = false;
        }


        private void ResetIsVisible()
        {
            this.IsVisible = true;
        }


        private void ResetItalic()
        {
            this.Italic = this.getDefaultFont().Italic;
        }


        private void ResetSize()
        {
            this.Size = this.getDefaultFont().SizeInPoints;
        }


        private void ResetUnderline()
        {
            this.Underline = this.getDefaultFont().Underline;
        }


        internal void SetBackColorInternal(Color value)
        {
            NativeScintilla.StyleSetBack(this._index, Utilities.ColorToRgb(value));
            Scintilla.ColorBag[this + ".BackColor"] = value;

            if (this._index == (int)StylesCommon.CallTip)
                NativeScintilla.CallTipSetBack(Utilities.ColorToRgb(value));
        }


        internal void SetForeColorInternal(Color value)
        {
            Scintilla.ColorBag[this + ".ForeColor"] = value;
            NativeScintilla.StyleSetFore(this._index, Utilities.ColorToRgb(value));

            if (this._index == (int)StylesCommon.CallTip)
                NativeScintilla.CallTipSetFore(Utilities.ColorToRgb(value));
        }


        internal bool ShouldSerialize()
        {
            return this.ShouldSerializeBackColor() ||
                this.ShouldSerializeBold() ||
                this.ShouldSerializeCase() ||
                this.ShouldSerializeCharacterSet() ||
                this.ShouldSerializeFontName() ||
                this.ShouldSerializeForeColor() ||
                this.ShouldSerializeIsChangeable() ||
                this.ShouldSerializeIsHotspot() ||
                this.ShouldSerializeIsSelectionEolFilled() ||
                this.ShouldSerializeIsVisible() ||
                this.ShouldSerializeItalic() ||
                this.ShouldSerializeSize() ||
                this.ShouldSerializeUnderline();
        }


        private bool ShouldSerializeBackColor()
        {
            return this.BackColor != this.getDefaultBackColor();
        }


        private bool ShouldSerializeBold()
        {
            return this.Bold != this.getDefaultFont().Bold;
        }


        private bool ShouldSerializeCase()
        {
            return this.Case != StyleCase.Mixed;
        }


        private bool ShouldSerializeCharacterSet()
        {
            return this.CharacterSet != this.getDefaultCharacterSet();
        }


        private bool ShouldSerializeFont()
        {
            //	We never serialize the font property, we let the component
            //	properties do the work.
            return false;
        }


        private bool ShouldSerializeFontName()
        {
            return this.FontName != this.getDefaultFont().Name;
        }


        private bool ShouldSerializeForeColor()
        {
            return this.ForeColor != this.getDefaultForeColor();
        }


        private bool ShouldSerializeIsChangeable()
        {
            return !this.IsChangeable;
        }


        private bool ShouldSerializeIsHotspot()
        {
            return this.IsHotspot;
        }


        private bool ShouldSerializeIsSelectionEolFilled()
        {
            return this.IsSelectionEolFilled;
        }


        private bool ShouldSerializeIsVisible()
        {
            return !this.IsVisible;
        }


        private bool ShouldSerializeItalic()
        {
            return this.Italic != this.getDefaultFont().Italic;
        }


        private bool ShouldSerializeSize()
        {
            return this.Size != this.getDefaultFont().SizeInPoints;
        }


        private bool ShouldSerializeUnderline()
        {
            return this.Underline != this.getDefaultFont().Underline;
        }


        public override string ToString()
        {
             return "Style" + this._index.ToString();
        }

        #endregion Methods


        #region Properties

        public Color BackColor
        {
            get
            {
                if (Scintilla.ColorBag.ContainsKey(this + ".BackColor"))
                    return Scintilla.ColorBag[this + ".BackColor"];

                return Utilities.RgbToColor(NativeScintilla.StyleGetBack(this._index));
            }
            set
            {
                this.SetBackColorInternal(value);

                if (this._index == (int)StylesCommon.CallTip)
                    Scintilla.CallTip.SetBackColorInternal(value);
            }
        }


        public bool Bold
        {
            get { return NativeScintilla.StyleGetBold(this._index); }
            set
            {
                NativeScintilla.StyleSetBold(this._index, value);
                Scintilla.PropertyBag[this + ".FontSet"] = true;
            }
        }


        public StyleCase Case
        {
            get
            {
                return (StyleCase)NativeScintilla.StyleGetCase(this._index);
            }
            set
            {
                NativeScintilla.StyleSetCase(this._index, (int)value);
            }
        }


        public CharacterSet CharacterSet
        {
            get { return (CharacterSet)NativeScintilla.StyleGetCharacterSet(this._index); }
            set
            {
                NativeScintilla.StyleSetCharacterSet(this._index, (int)value);
                Scintilla.PropertyBag[this + ".FontSet"] = true;
            }
        }


        public Font Font
        {
            get
            {
                var fs = FontStyle.Regular;
                if (this.Bold) fs |= FontStyle.Bold;
                if (this.Italic) fs |= FontStyle.Italic;
                if (this.Underline) fs |= FontStyle.Underline;

                return new Font(this.FontName, this.Size, fs, GraphicsUnit.Point, (byte)this.CharacterSet);
            }
            set
            {
                this.CharacterSet = (CharacterSet)value.GdiCharSet;
                this.FontName = value.Name;
                this.Size = value.SizeInPoints;
                this.Bold = value.Bold;
                this.Italic = value.Italic;
                this.Underline = value.Underline;
            }
        }


        public string FontName
        {
            get
            {
                //	Scintilla has trouble returning some font names, especially those
                //	with spaces in it. They get truncated. So we're storing ourselves.
                //	Oh yeah I wrote the code for SCI_STYLEGETFONT in Scintilla so what 
                //	does that tell you?
                if (!Scintilla.PropertyBag.ContainsKey(this + ".FontName"))
                {
                    string fontName;
                    NativeScintilla.StyleGetFont(this._index, out fontName);
                    return fontName;
                }

                return Scintilla.PropertyBag[this + ".FontName"].ToString();
            }
            set
            {
                NativeScintilla.StyleSetFont(this._index, value);
                Scintilla.PropertyBag[this + ".FontName"] = value;
                Scintilla.PropertyBag[this + ".FontSet"] = true;

            }
        }


        public Color ForeColor
        {
            get
            {
                if (Scintilla.ColorBag.ContainsKey(this + ".ForeColor"))
                    return Scintilla.ColorBag[this + ".ForeColor"];

                return Utilities.RgbToColor(NativeScintilla.StyleGetFore(this._index));
            }
            set
            {
                this.SetForeColorInternal(value);

                if (this._index == (int)StylesCommon.CallTip)
                    Scintilla.CallTip.SetForeColorInternal(value);
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public int Index
        {
            get
            {
                return this._index;
            }
        }


        public bool IsChangeable
        {
            get
            {
                return NativeScintilla.StyleGetChangeable(this._index); 
            }
            set
            {
                NativeScintilla.StyleSetChangeable(this._index, value);
            }
        }


        public bool IsHotspot
        {
            get
            {
                return NativeScintilla.StyleGetHotspot(this._index);
            }
            set
            {
                NativeScintilla.StyleSetHotspot(this._index, value);
            }
        }


        public bool IsSelectionEolFilled
        {
            get
            {
                return NativeScintilla.StyleGetEOLFilled(this._index);
            }
            set
            {
                NativeScintilla.StyleSetEOLFilled(this._index, value);
            }
        }


        public bool IsVisible
        {
            get
            {
                return NativeScintilla.StyleGetVisible(this._index);
            }
            set
            {
                NativeScintilla.StyleSetVisible(this._index, value);
            }
        }


        public bool Italic
        {
            get { return NativeScintilla.StyleGetItalic(this._index); }
            set
            {
                NativeScintilla.StyleSetItalic(this._index, value);
                Scintilla.PropertyBag[this + ".FontSet"] = true;
            }
        }


         //	There are 2 problems with Font Sizes, first Scintilla seems to
        //	accept them just fine, but always returns 8. Also it only supports
        //	integer font sizes, and .NET tends to use non integer values like 8.5
        //	which means that it would always be serialized. The solution? store our
        //	own value.
        public float Size
        {
            get
            {
                if (!Scintilla.PropertyBag.ContainsKey(this + ".Size"))
                    return NativeScintilla.StyleGetSize(this._index);

                return (float)Scintilla.PropertyBag[this + ".Size"];
            }
            set
            {
                NativeScintilla.StyleSetSize(this._index, (int)value);
                Scintilla.PropertyBag[this + ".Size"] = value;
                Scintilla.PropertyBag[this + ".FontSet"] = true;
            }
        }


        public bool Underline
        {
            get { return NativeScintilla.StyleGetUnderline(this._index); }
            set
            {
                NativeScintilla.StyleSetUnderline(this._index, value);
                Scintilla.PropertyBag[this + ".FontSet"] = true;
            }
        }

        #endregion Properties


        #region Constructors

         internal Style(int index, Scintilla scintilla) : base(scintilla)
         {
             this._index = index;
         }

        #endregion Constructors
    }
}
