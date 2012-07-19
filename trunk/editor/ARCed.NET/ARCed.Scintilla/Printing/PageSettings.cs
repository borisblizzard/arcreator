#region Using Directives

using System.ComponentModel;
using System.Drawing;
using System.Drawing.Printing;

#endregion


namespace ARCed.Scintilla
{
    /// <summary>
    ///     ARCed.Scintilla derived class for handling printed page settings.  It holds information 
    ///     on how and what to print in the header and footer of pages.
    /// </summary>
    [TypeConverter(typeof(ExpandableObjectConverter))]
    public class PageSettings : System.Drawing.Printing.PageSettings
    {
        #region Fields

        private readonly bool _baseColor;

        /// <summary>
        /// Default footer style used when no footer is provided.
        /// </summary>
        public static readonly PageInformation DefaultFooter = new PageInformation(PageInformationBorder.Top, InformationType.Nothing, InformationType.Nothing, InformationType.Nothing);

        /// <summary>
        /// Default header style used when no header is provided.
        /// </summary>
        public static readonly PageInformation DefaultHeader = new PageInformation(PageInformationBorder.Bottom, InformationType.DocumentName, InformationType.Nothing, InformationType.PageNumber);

        private PrintColorMode _eColorMode;
        private FooterInformation _oFooter;
        private HeaderInformation _oHeader;
        private short _sFontMagnification;

        #endregion Fields


        #region Methods

        private void ResetColor()
        {
            this.Color = this._baseColor;
        }


        private void ResetColorMode()
        {
            this._eColorMode = PrintColorMode.Normal;
        }


        private void ResetFontMagnification()
        {
            this._sFontMagnification = 0;
        }


        private void ResetLandscape()
        {
            this.Landscape = false;
        }


        private void ResetMargins()
        {
            this.Margins = new Margins(50,50,50,50);
        }


        internal bool ShouldSerialize()
        {
            return this.ShouldSerializeColor() ||
                this.ShouldSerializeColorMode() ||
                this.ShouldSerializeFontMagnification() ||
                this.ShouldSerializeFooter() ||
                this.ShouldSerializeHeader() ||
                this.ShouldSerializeLandscape() ||
                this.ShouldSerializeMargins();
        }


        private bool ShouldSerializeColor()
        {
            return this.Color != this._baseColor;
        }


        private bool ShouldSerializeColorMode()
        {
            return this._eColorMode != PrintColorMode.Normal;
        }


        private bool ShouldSerializeFontMagnification()
        {
            return this._sFontMagnification != 0;
        }


        private bool ShouldSerializeFooter()
        {
            return this._oFooter.ShouldSerialize();
        }


        private bool ShouldSerializeHeader()
        {
            return this._oHeader.ShouldSerialize();
        }


        private bool ShouldSerializeLandscape()
        {
            return this.Landscape;
        }


        private bool ShouldSerializeMargins()
        {
            return this.Margins.Bottom != 50 ||this.Margins.Left != 50 || this.Margins.Right != 50 || this.Margins.Bottom != 50;
        }

        #endregion Methods


        #region Properties

        // All these properties below merely call into their base class.
        // So why have new versions of these? The PageSettings class
        // isn't designer friendly.
        [Browsable(false)]
        public new Rectangle Bounds
        {
            get
            {
                return base.Bounds;
            }
        }


        public new bool Color
        {
            get
            {
                return base.Color;
            }
            set
            {
                base.Color = value;
            }
        }


        /// <summary>
        ///     Method used to render colored text on a printer
        /// </summary>
        public PrintColorMode ColorMode
        {
            get { return this._eColorMode; }
            set { this._eColorMode = value; }
        }


        /// <summary>
        ///     Number of points to add or subtract to the size of each screen font during printing
        /// </summary>
        public short FontMagnification
        {
            get { return this._sFontMagnification; }
            set { this._sFontMagnification = value; }
        }


        /// <summary>
        ///     Page Information printed in the footer of the page
        /// </summary>
        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public FooterInformation Footer
        {
            get { return this._oFooter; }
            set { this._oFooter = value; }
        }


        [Browsable(false)]
        public new float HardMarginX
        {
            get
            {
                return base.HardMarginX;
            }
        }


        [Browsable(false)]
        public new float HardMarginY
        {
            get
            {
                return base.HardMarginY;
            }
        }


        /// <summary>
        ///     Page Information printed in header of the page
        /// </summary>
        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public HeaderInformation Header
        {
            get { return this._oHeader; }
            set { this._oHeader = value; }
        }


        public new bool Landscape
        {
            get
            {
                return base.Landscape;
            }
            set
            {
                base.Landscape = value;
            }
        }


        public new Margins Margins
        {
            get
            {
                return base.Margins;
            }
            set
            {
                base.Margins = value;
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public new PaperSize PaperSize
        {
            get
            {
                return base.PaperSize;
            }
            set
            {
                base.PaperSize  = value;
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public new PaperSource PaperSource
        {
            get
            {
                return base.PaperSource;
            }
            set
            {
                base.PaperSource = value;
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public new RectangleF PrintableArea
        {
            get
            {
                return base.PrintableArea;
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public new PrinterResolution PrinterResolution
        {
            get
            {
                return base.PrinterResolution;
            }
            set
            {
                base.PrinterResolution = value;
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public new PrinterSettings PrinterSettings
        {
            get
            {
                return base.PrinterSettings;
            }
            set
            {
                base.PrinterSettings = value;
            }
        }

        #endregion Properties


        #region Constructors

        /// <summary>
        ///     Default constructor
        /// </summary>
        public PageSettings()
        {
            // Keep track of the base color for designer serialization. This is a workaround that should
            // last until the PageSettings can be redesigned.
            this._baseColor = base.Color;


            this._oHeader = new HeaderInformation(PageInformationBorder.Bottom, InformationType.DocumentName, InformationType.Nothing, InformationType.PageNumber);
            this._oFooter = new FooterInformation(PageInformationBorder.Top, InformationType.Nothing, InformationType.Nothing, InformationType.Nothing);
            this._sFontMagnification = 0;
            this._eColorMode = PrintColorMode.Normal;

            // Set default margins to 1/2 inch (50/100ths)
            base.Margins.Top = 50;
            base.Margins.Left = 50;
            base.Margins.Right = 50;
            base.Margins.Bottom = 50;
        }

        #endregion Constructors
    }
}