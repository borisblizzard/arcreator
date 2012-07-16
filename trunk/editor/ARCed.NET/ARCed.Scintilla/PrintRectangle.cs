﻿#region Using Directives

using System.Runtime.InteropServices;

#endregion


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Struct used for specifying the printing bounds
    /// </summary>
    [StructLayout(LayoutKind.Sequential)]
    public struct PrintRectangle
    {
        #region Fields

        /// <summary>
        ///  Left X Bounds Coordinate
        /// </summary>
        public int Left;

        /// <summary>
        ///     Top Y Bounds Coordinate
        /// </summary>
        public int Top;

        /// <summary>
        ///     Right X Bounds Coordinate
        /// </summary>
        public int Right;

        /// <summary>
        ///     FixedY Y Bounds Coordinate
        /// </summary>
        public int Bottom;

        #endregion Fields


        #region Constructors

        public PrintRectangle(int iLeft, int iTop, int iRight, int iBottom)
        {
            Left = iLeft;
            Top = iTop;
            Right = iRight;
            Bottom = iBottom;
        }

        #endregion Constructors
    }
}
