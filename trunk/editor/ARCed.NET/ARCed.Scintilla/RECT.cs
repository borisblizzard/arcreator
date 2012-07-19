#region Using Directives

using System;
using System.Drawing;
using System.Runtime.InteropServices;

#endregion


namespace ARCed.Scintilla
{
    [Serializable, StructLayout(LayoutKind.Sequential)]
    public struct RECT
    {
        #region Fields

        public int Left;
        public int Top;
        public int Right;
        public int Bottom;

        #endregion Fields


        #region Properties

        public int Height { get { return this.Bottom - this.Top; } }
        public Point Location { get { return new Point(this.Left, this.Top); } }
        public Size Size { get { return new Size(this.Width, this.Height); } }
        public int Width { get { return this.Right - this.Left; } }

        #endregion Properties


        #region Methods

        public static RECT FromRectangle(Rectangle rectangle)
        {
            return new RECT(rectangle.Left, rectangle.Top, rectangle.Right, rectangle.Bottom);
        }


        public override int GetHashCode()
        {
            return this.Left ^ ((this.Top << 13) | (this.Top >> 0x13))
              ^ ((this.Width << 0x1a) | (this.Width >> 6))
              ^ ((this.Height << 7) | (this.Height >> 0x19));
        }


        // Handy method for converting to a System.Drawing.Rectangle
        public Rectangle ToRectangle()
        {
            return Rectangle.FromLTRB(this.Left, this.Top, this.Right, this.Bottom);
        }

        #endregion Methods


        #region Operators

        public static implicit operator RECT(Rectangle rect)
        {
            return FromRectangle(rect);
        }


        public static implicit operator Rectangle(RECT rect)
        {
            return rect.ToRectangle();
        }

        #endregion Operators


        #region Constructors

        public RECT(int left_, int top_, int right_, int bottom_)
        {
            this.Left = left_;
            this.Top = top_;
            this.Right = right_;
            this.Bottom = bottom_;
        }

        #endregion Constructors
    } 
}
