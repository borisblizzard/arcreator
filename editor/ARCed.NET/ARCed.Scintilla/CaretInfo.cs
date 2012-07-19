#region Using Directives

using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;

#endregion


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Manages Caret Settings
    /// </summary>
    /// <remarks>
    ///     The caret is the blinking line that indicates the current document position. This
    ///     is sometimes referred to as cursor.
    /// </remarks>
    [TypeConverter(typeof(ExpandableObjectConverter))]
    public class CaretInfo : TopLevelHelper
    {
        #region Methods

        /// <summary>
        ///     Places the caret somewhere within the document that is displayed in the
        ///     Scintilla Window
        /// </summary>
        /// <remarks>
        ///     If the caret is already visible in the current scrolled view this method does
        ///     nothing.
        /// </remarks>
        public void BringIntoView()
        {
            NativeScintilla.MoveCaretInsideView();
        }


        /// <summary>
        ///     Scintilla remembers the x value of the last position horizontally moved to explicitly by the user and this value is then 
        ///     used when moving vertically such as by using the up and down keys. This method sets the current x position of the caret as 
        ///     the remembered value.
        /// </summary>
        public void ChooseCaretX()
        {
            NativeScintilla.ChooseCaretX();
        }


        /// <summary>
        ///     Scrolls the Scintilla window so that the Caret is visible.
        /// </summary>
        public void EnsureVisible()
        {
            NativeScintilla.ScrollCaret();
        }


        /// <summary>
        ///     Places the caret at the specified document position
        /// </summary>
        /// <param name="position">Position in the document to place the caret</param>
        public void Goto(int position)
        {
            NativeScintilla.GotoPos(position);
        }


        private void ResetBlinkRate()
        {
            this.BlinkRate = SystemInformation.CaretBlinkTime;
        }


        private void ResetColor()
        {
            this.Color = Color.Black;
        }


        private void ResetCurrentLineBackgroundAlpha()
        {
            this.CurrentLineBackgroundAlpha = 256;
        }


        private void ResetCurrentLineBackgroundColor()
        {
            this.CurrentLineBackgroundColor = Color.Yellow;
        }


        private void ResetHighlightCurrentLine()
        {
            this.HighlightCurrentLine = false;
        }


        private void ResetIsSticky()
        {
            this.IsSticky = false;
        }


        private void ResetStyle()
        {
            this.Style = CaretStyle.Line;
        }


        private void ResetWidth()
        {
            this.Width = SystemInformation.CaretWidth;
        }


        protected internal bool ShouldSerialize()
        {
            return this.ShouldSerializeBlinkRate() ||
                    this.ShouldSerializeColor() ||
                    this.ShouldSerializeCurrentLineBackgroundColor() ||
                    this.ShouldSerializeWidth() ||
                    this.ShouldSerializeHighlightCurrentLine() ||
                    this.ShouldSerializeCurrentLineBackgroundAlpha() ||
                    this.ShouldSerializeStyle() ||
                    this.ShouldSerializeIsSticky();
        }


        private bool ShouldSerializeBlinkRate()
        {
            return this.BlinkRate != SystemInformation.CaretBlinkTime;
        }


        private bool ShouldSerializeColor()
        {
            return this.Color != Color.Black;
        }


        private bool ShouldSerializeCurrentLineBackgroundAlpha()
        {
            return this.CurrentLineBackgroundAlpha != 256;
        }


        private bool ShouldSerializeCurrentLineBackgroundColor()
        {
            return this.CurrentLineBackgroundColor != Color.Yellow;
        }


        private bool ShouldSerializeHighlightCurrentLine()
        {
            return this.HighlightCurrentLine;
        }


        private bool ShouldSerializeIsSticky()
        {
            return this.IsSticky;
        }


        private bool ShouldSerializeStyle()
        {
            return this.Style != CaretStyle.Line;
        }


        private bool ShouldSerializeWidth()
        {
            return this.Width != SystemInformation.CaretWidth;
        }


        public override string ToString()
        {
            return this.ShouldSerialize() ? base.ToString() : string.Empty;
        }

        #endregion Methods


        #region Properties

        /// <summary>
        ///     Gets/Sets the current anchor position
        /// </summary>
        /// <remarks>
        ///     If the anchor position is less than the Caret Position it acts as the _start of
        ///     the selection.
        /// </remarks>
        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public int Anchor
        {
            get
            {
                return NativeScintilla.GetAnchor();
            }
            set
            {
                NativeScintilla.SetAnchor(value);
            }
        }


        /// <summary>
        ///     Gets/Sets the time interval in milliseconds that the caret should blink.
        /// </summary>
        /// <remarks>
        ///     This defaults to the system default value.
        /// </remarks>
        public int BlinkRate
        {
            get
            {
                return NativeScintilla.GetCaretPeriod();
            }
            set
            {
                NativeScintilla.SetCaretPeriod(value);
            }
        }


        /// <summary>
        ///     Gets/Sets the color of the Caret.
        /// </summary>
        /// <remarks>Defaults to black</remarks>
        public Color Color
        {
            get
            {
                if (Scintilla.ColorBag.ContainsKey("Caret.Color"))
                    return Scintilla.ColorBag["Caret.Color"];

                Color c = Utilities.RgbToColor(NativeScintilla.GetCaretFore());

                return c == Color.FromArgb(0, 0, 0) ? Color.Black : c;
            }
            set
            {
                if (value == this.Color)
                    return;

                if (value.IsKnownColor)
                {
                    if (this.Color == Color.Black)
                        Scintilla.ColorBag.Remove("Caret.Color");
                    else
                        Scintilla.ColorBag["Caret.Color"] = value;
                }

                NativeScintilla.SetCaretFore(Utilities.ColorToRgb(value));
            }
        }


        /// <summary>
        ///     Gets/Sets the transparency alpha of the CurrentLine Background highlight
        /// </summary>
        /// <remarks>
        ///     Values range from 0 to 256. Default is 256.
        /// </remarks>
        public int CurrentLineBackgroundAlpha
        {
            get
            {
                return NativeScintilla.GetCaretLineBackAlpha();
            }
            set
            {
                NativeScintilla.SetCaretLineBackAlpha(value);
            }
        }


        /// <summary>
        ///     Gets/Sets the color of the document line where the caret currently resides
        /// </summary>
        /// <remarks>
        ///     The <see cref="ARCed.Scintilla.CaretInfo.HighlightCurrentLine"/> property must be set to true in order
        ///     for this to to take effect.
        /// </remarks>
        public Color CurrentLineBackgroundColor
        {
            get
            {
                if (Scintilla.ColorBag.ContainsKey("Caret.CurrentLineBackgroundColor"))
                    return Scintilla.ColorBag["Caret.CurrentLineBackgroundColor"];

                Color c = Utilities.RgbToColor(NativeScintilla.GetCaretLineBack());

                return c.ToArgb() == Color.Yellow.ToArgb() ? Color.Yellow : c;
            }
            set
            {


                if (value == this.Color)
                    return;

                if (value.IsKnownColor)
                {
                    if (this.Color == Color.Yellow)
                        Scintilla.ColorBag.Remove("Caret.CurrentLineBackgroundColor");
                    else
                        Scintilla.ColorBag["Caret.CurrentLineBackgroundColor"] = value;
                }

                NativeScintilla.SetCaretLineBack(Utilities.ColorToRgb(value));
            }
        }


        /// <summary>
        ///     Gets/Sets if the current document line where the caret resides is highlighted.
        /// </summary>
        /// <remarks>
        ///     <see cref="CurrentLineBackgroundColor"/> determines the color. 
        /// </remarks>
        public bool HighlightCurrentLine
        {
            get
            {
                return NativeScintilla.GetCaretLineVisible();
            }
            set
            {
                NativeScintilla.SetCaretLineVisible(value);
            }
        }


        /// <summary>
        ///     Controls when the last position of the caret on the line is saved. When set to true, the position is not saved when you type a character, a tab, paste the clipboard content or press backspace
        /// </summary>
        /// <remarks>
        ///     Defaults to false
        /// </remarks>
        public bool IsSticky
        {
            get
            {
                return NativeScintilla.GetCaretSticky();
            }
            set
            {
                NativeScintilla.SetCaretSticky(value);
            }
        }


        /// <summary>
        ///     Gets/Sets the current Line Number that the caret resides.
        /// </summary>
        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public int LineNumber
        {
            get
            {
                return NativeScintilla.LineFromPosition(NativeScintilla.GetCurrentPos());
            }
            set
            {
                NativeScintilla.GotoLine(value);
            }
        }


        /// <summary>
        ///     Gets/Sets the current document position where the caret resides
        /// </summary>
        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public int Position
        {
            get
            {
                return NativeScintilla.GetCurrentPos();
            }
            set
            {
                NativeScintilla.SetCurrentPos(value);
            }
        }


        /// <summary>
        ///     Gets/Sets the <see cref="CaretStyle"/> displayed.
        /// </summary>
        public CaretStyle Style
        {
            get
            {
                return (CaretStyle)NativeScintilla.GetCaretStyle();
            }
            set
            {
                NativeScintilla.SetCaretStyle((int)value);
            }
        }


        /// <summary>
        ///     Gets/Sets the width in pixels of the Caret
        /// </summary>
        /// <remarks>
        ///     This defaults to the system default.
        /// </remarks>
        public int Width
        {
            get
            {
                return NativeScintilla.GetCaretWidth();
            }
            set
            {
                NativeScintilla.SetCaretWidth(value);
            }
        }

        #endregion Properties


        #region Constructors

        protected internal CaretInfo(Scintilla scintilla)
            : base(scintilla)
        {
            this.BlinkRate = SystemInformation.CaretBlinkTime;
            this.Width = SystemInformation.CaretWidth;
        }

        #endregion Constructors
    }
}
