#region Using Directives

using System.ComponentModel;
using System.Drawing;

#endregion


namespace ARCed.Scintilla
{
    [TypeConverter(typeof(ExpandableObjectConverter))]
    public class HeaderInformation : PageInformation
    {
        #region Methods

        private void ResetBorder()
        {
            this.Border = PageInformationBorder.Bottom;
        }


        private void ResetCenter()
        {
            this.Center = InformationType.Nothing;
        }


        private void ResetFont()
        {
            this.Font = DefaultFont;
        }


        private void ResetLeft()
        {
            this.Left = InformationType.DocumentName;
        }


        private void ResetMargin()
        {
            this.Margin = 3;
        }


        private void ResetRight()
        {
            this.Right = InformationType.PageNumber;
        }


        internal bool ShouldSerialize()
        {
            return this.ShouldSerializeBorder() ||
                this.ShouldSerializeCenter() ||
                this.ShouldSerializeFont() ||
                this.ShouldSerializeLeft() ||
                this.ShouldSerializeMargin() ||
                this.ShouldSerializeRight();
        }


        private bool ShouldSerializeBorder()
        {
            return this.Border != PageInformationBorder.Bottom;
        }


        private bool ShouldSerializeCenter()
        {
            return this.Center != InformationType.Nothing;
        }


        private bool ShouldSerializeFont()
        {
            return !DefaultFont.Equals(this.Font);
        }


        private bool ShouldSerializeLeft()
        {
            return this.Left != InformationType.DocumentName;
        }


        private bool ShouldSerializeMargin()
        {
            return this.Margin != 3;
        }


        private bool ShouldSerializeRight()
        {
            return this.Right != InformationType.PageNumber;
        }

        #endregion Methods


        #region Properties

        public override PageInformationBorder Border
        {
            get
            {
                return base.Border;
            }
            set
            {
                base.Border = value;
            }
        }


        public override InformationType Center
        {
            get
            {
                return base.Center;
            }
            set
            {
                base.Center = value;
            }
        }


        public override Font Font
        {
            get
            {
                return base.Font;
            }
            set
            {
                base.Font = value;
            }
        }


        public override InformationType Left
        {
            get
            {
                return base.Left;
            }
            set
            {
                base.Left = value;
            }
        }


        public override int Margin
        {
            get
            {
                return base.Margin;
            }
            set
            {
                base.Margin = value;
            }
        }


        public override InformationType Right
        {
            get
            {
                return base.Right;
            }
            set
            {
                base.Right = value;
            }
        }

        #endregion Properties


        #region Constructors

        /// <summary>
        ///     Default Constructor
        /// </summary>
        public HeaderInformation() : base(PageInformationBorder.None, InformationType.Nothing, InformationType.Nothing, InformationType.Nothing)
        {
        }


        /// <summary>
        ///     Full Constructor
        /// </summary>
        /// <param name="iMargin">Margin to use</param>
        /// <param name="oFont">Font to use </param>
        /// <param name="eBorder">Border style</param>
        /// <param name="eLeft">What to print on the left side of the page</param>
        /// <param name="eCenter">What to print in the center of the page</param>
        /// <param name="eRight">What to print on the right side of the page</param>
        public HeaderInformation(int iMargin, Font oFont, PageInformationBorder eBorder, InformationType eLeft, InformationType eCenter, InformationType eRight) : base(iMargin, oFont, eBorder, eLeft, eCenter, eRight)
        {
        }


        /// <summary>
        ///     Normal Use Constructor
        /// </summary>
        /// <param name="eBorder">Border style</param>
        /// <param name="eLeft">What to print on the left side of the page</param>
        /// <param name="eCenter">What to print in the center of the page</param>
        /// <param name="eRight">What to print on the right side of the page</param>
        public HeaderInformation(PageInformationBorder eBorder, InformationType eLeft, InformationType eCenter, InformationType eRight) : base(3, DefaultFont, eBorder, eLeft, eCenter, eRight)
        {
        }

        #endregion Constructors
    }
}
