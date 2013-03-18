#region Using Directives

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;

#endregion


namespace ARCed.Scintilla
{
    [TypeConverter(typeof(ExpandableObjectConverter))]
    public class StyleCollection : TopLevelHelper
    {
        #region Methods

        public void ClearAll()
        {
            NativeScintilla.StyleClearAll();
        }


        public void ClearDocumentStyle()
        {
            NativeScintilla.ClearDocumentStyle();
        }


        public int GetEndStyled()
        {
            return NativeScintilla.GetEndStyled();
        }


        public byte GetStyleAt(int position)
        {
            return NativeScintilla.GetStyleAt(position);
        }


        public string GetStyleNameAt(int position)
        {
            int styleNumber = this.GetStyleAt(position);
            foreach (KeyValuePair<string, int> map in Scintilla.Lexing.StyleNameMap)
                if (map.Value == styleNumber)
                    return map.Key;

            return null;
        }


        public void Reset()
        {
            for (int i = 0; i < 32; i++)
                this[i].Reset();
        }


        private void ResetBits()
        {
#pragma warning disable 618
            this.Bits = 7;
#pragma warning restore 618
        }


        public void ResetDefault()
        {
            NativeScintilla.StyleResetDefault();
        }


        internal bool ShouldSerialize()
        {
            return this.ShouldSerializeBits() ||
                this.ShouldSerializeBraceBad() ||
                this.ShouldSerializeBraceLight() ||
                this.ShouldSerializeCallTip() ||
                this.ShouldSerializeControlChar() ||
                this.ShouldSerializeDefault() ||
                this.ShouldSerializeIndentGuide() ||
                this.ShouldSerializeLastPredefined() ||
                this.ShouldSerializeLineNumber() ||
                this.ShouldSerializeMax();
        }


        private bool ShouldSerializeBits()
        {
#pragma warning disable 618
            return this.Bits != 7;
#pragma warning restore 618

        }


        private bool ShouldSerializeBraceBad()
        {
            return this.BraceBad.ShouldSerialize();
        }


        private bool ShouldSerializeBraceLight()
        {
            return this.BraceLight.ShouldSerialize();
        }


        private bool ShouldSerializeCallTip()
        {
            return this.CallTip.ShouldSerialize();
        }


        private bool ShouldSerializeControlChar()
        {
            return this.ControlChar.ShouldSerialize();
        }


        private bool ShouldSerializeDefault()
        {
            return this.BraceBad.ShouldSerialize();
        }


        private bool ShouldSerializeIndentGuide()
        {
            return this.IndentGuide.ShouldSerialize();
        }


        private bool ShouldSerializeLastPredefined()
        {
            return this.LastPredefined.ShouldSerialize();
        }


        private bool ShouldSerializeLineNumber()
        {
            return this.LineNumber.ShouldSerialize();
        }


        private bool ShouldSerializeMax()
        {
            return this.Max.ShouldSerialize();
        }

        #endregion Methods


        #region Properties

        [Obsolete("The modern style indicators make this obsolete, this should always be 7")]
        public int Bits
        {
            get
            {
                return NativeScintilla.GetStyleBits();
            }
            set
            {
                NativeScintilla.SetStyleBits(value);
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public Style BraceBad
        {
            get
            {
                return this[StylesCommon.BraceBad];
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public Style BraceLight
        {
            get
            {
                return this[StylesCommon.BraceLight];
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public Style CallTip
        {
            get
            {
                return this[StylesCommon.CallTip];
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public Style ControlChar
        {
            get
            {
                return this[StylesCommon.ControlChar];
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public Style Default
        {
            get
            {
                return this[StylesCommon.Default];
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public Style IndentGuide
        {
            get
            {
                return this[StylesCommon.IndentGuide];
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public Style LastPredefined
        {
            get
            {
                return this[StylesCommon.LastPredefined];
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public Style LineNumber
        {
            get
            {
                return this[StylesCommon.LineNumber];
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public Style Max
        {
            get
            {
                return this[StylesCommon.Max];
            }
        }

        #endregion Properties


        #region Indexers

        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public Style this[int index]
        {
            get
            {
                return new Style(index, Scintilla);
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public Style this[StylesCommon index]
        {
            get
            {
                return new Style((int)index, Scintilla);
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public Style this[string styleName]
        {
            get
            {
                return new Style(Scintilla.Lexing.StyleNameMap[styleName], Scintilla);
            }
        }

        #endregion Indexers


        #region Constructors

        internal StyleCollection(Scintilla scintilla) : base(scintilla)
        {
#pragma warning disable 618
            this.Bits = 7;
#pragma warning restore 618

            //	Defaulting CallTip Settings to Platform defaults
            Style s = this.CallTip;
            s.ForeColor = SystemColors.InfoText;
            s.BackColor = SystemColors.Info;
            s.Font = SystemFonts.StatusFont;

            //	Making Line Number's BackColor have a named system color
            //	instead of just the value
            this.LineNumber.BackColor = SystemColors.Control;
        }

        #endregion Constructors
    }
}
