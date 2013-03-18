#region Using Directives

using System.ComponentModel;
using System.Drawing;

#endregion


namespace ARCed.Scintilla
{
    [TypeConverter(typeof(ExpandableObjectConverter))]
    public class Margin : ScintillaHelperBase
    {
        #region Fields

        private int _autoToggleMarkerNumber = -1;
        private readonly int _number;

        #endregion Fields


        #region Methods

        public override bool Equals(object obj)
        {
            if (!IsSameHelperFamily(obj))
                return false;

            return this.Number == ((Margin)obj).Number;
        }


        public Rectangle GetClientRectangle()
        {
            int left = 0;
            for (int i = 0; i < this._number; i++)
                left += NativeScintilla.GetMarginWidthN(i);

            return new Rectangle(left, 0, this.Width, Scintilla.ClientSize.Height);
        }


        public override int GetHashCode()
        {
            return base.GetHashCode();
        }


        public void Reset()
        {
            this.ResetAutoToggleMarkerNumber();
            this.ResetIsClickable();
            this.ResetIsFoldMargin();
            this.ResetIsMarkerMargin();
            this.ResetType();
            this.ResetWidth();
        }


        private void ResetAutoToggleMarkerNumber()
        {
            this._autoToggleMarkerNumber = -1;
        }


        internal void ResetIsClickable()
        {
            if (this._number == 2)
                this.IsClickable = true;
            else
                this.IsClickable = false;
        }


        internal void ResetIsFoldMargin()
        {
            if (this._number == 2)
                this.IsFoldMargin = true;
            else
                this.IsFoldMargin = false;
        }


        internal void ResetIsMarkerMargin()
        {
            if (this._number == 1)
                this.IsMarkerMargin = true;
            else
                this.IsMarkerMargin = false;
        }


        internal void ResetType()
        {
            if (this._number == 0)
                this.Type = MarginType.Number;
            else
                this.Type = MarginType.Symbol;
        }


        internal void ResetWidth()
        {
            if (this._number == 1)
                this.Width = 16;
            else
                this.Width = 0;
        }


        internal bool ShouldSerialize()
        {
            return this.ShouldSerializeIsFoldMargin() ||
                this.ShouldSerializeIsClickable() ||
                this.ShouldSerializeType() ||
                this.ShouldSerializeWidth() ||
                this.ShouldSerializeAutoToggleMarkerNumber() ||
                this.ShouldSerializeIsMarkerMargin();
        }


        private bool ShouldSerializeAutoToggleMarkerNumber()
        {
            return this._autoToggleMarkerNumber != -1;
        }


        private bool ShouldSerializeIsClickable()
        {
            if (this._number == 2)
                return !this.IsClickable;

            return this.IsClickable;
        }


        private bool ShouldSerializeIsFoldMargin()
        {
            if (this._number == 2)
                return !this.IsFoldMargin;

            return this.IsFoldMargin;
        }


        private bool ShouldSerializeIsMarkerMargin()
        {
            if (this._number == 1)
                return !this.IsMarkerMargin;
            else
                return this.IsMarkerMargin;
        }


        private bool ShouldSerializeType()
        {
            // Margin 0 defaults to Number, all the rest
            // default to Symbol
            if (this._number == 0)
                return this.Type != MarginType.Number;

            return this.Type != MarginType.Symbol;
        }


        private bool ShouldSerializeWidth()
        {
            // Margin 1 defaults to 16, all the rest
            // default to 0
            if (this._number == 1)
                return this.Width != 16;

            return this.Width != 0;
        }


        public override string ToString()
        {
            if (this._number == 0)
                return "(Default Line Numbers)";
            else if (this._number == 1)
                return "(Default Markers)";
            else if (this._number == 2)
                return "(Default Folds)";

            return base.ToString();
        }

        #endregion Methods


        #region Properties

        public int AutoToggleMarkerNumber
        {
            get
            {
                return this._autoToggleMarkerNumber;
            }
            set
            {
                this._autoToggleMarkerNumber = value;
            }
        }


        public bool IsClickable
        {
            get
            {
                return NativeScintilla.GetMarginSensitiveN(this._number);
            }
            set
            {
                NativeScintilla.SetMarginSensitiveN(this._number, value);
            }
        }


        public bool IsFoldMargin
        {
            get
            {
                return (this.Mask & Constants.SC_MASK_FOLDERS) == Constants.SC_MASK_FOLDERS;
            }
            set
            {
                if (value)
                    this.Mask |= Constants.SC_MASK_FOLDERS;
                else
                    this.Mask &= ~Constants.SC_MASK_FOLDERS;
            }
        }


        public bool IsMarkerMargin
        {
            // As best as I can divine, this value is like SC_MASK_FOLDERS but applies
            // instead to regular markers. I can't seem to find it in any of the documentation
            // or even a constant defined for it though.
            get
            {
                return (this.Mask & 0x1FFFFFF) == 0x1FFFFFF;
            }

            set
            {
                if (value)
                    this.Mask |= 0x1FFFFFF;
                else
                    this.Mask &= ~0x1FFFFFF;
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public int Mask
        {
            get
            {
                return NativeScintilla.GetMarginMaskN(this._number);
            }
            set
            {
                NativeScintilla.SetMarginMaskN(this._number, value);
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public int Number
        {
            get
            {
                return this._number;
            }
        }


        public MarginType Type
        {
            get
            {
                return (MarginType)NativeScintilla.GetMarginTypeN(this._number);
            }
            set
            {
                NativeScintilla.SetMarginTypeN(this._number, (int)value);
            }
        }


        public int Width
        {
            get
            {
                return NativeScintilla.GetMarginWidthN(this._number);
            }
            set
            {
                NativeScintilla.SetMarginWidthN(this._number, value);
            }
        }

        #endregion Properties


        #region Constructors

        protected internal Margin(Scintilla scintilla, int number) : base(scintilla)
        {
            this._number = number;
        }

        #endregion Constructors
    }
}
