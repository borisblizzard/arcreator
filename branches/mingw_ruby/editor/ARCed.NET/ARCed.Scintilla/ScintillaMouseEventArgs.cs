#region Using Directives

using System;

#endregion


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Provides data for Scintilla mouse events
    /// </summary>
    public class ScintillaMouseEventArgs : EventArgs
    {
        #region Fields

        private int _position;
        private int _x;
        private int _y;

        #endregion Fields


        #region Properties

        /// <summary>
        ///     Returns the Document position
        /// </summary>
        public int Position
        {
            get { return this._position; }
            set { this._position = value; }
        }


        /// <summary>
        ///     Returns the X (left) position of mouse in pixels
        /// </summary>
        public int X
        {
            get { return this._x; }
            set { this._x = value; }
        }


        /// <summary>
        ///     Returns the Y (top) position of mouse in pixels
        /// </summary>
        public int Y
        {
            get { return this._y; }
            set { this._y = value; }
        }

        #endregion Properties


        #region Constructors

        /// <summary>
        ///     Initializes a new instance of the ScintillaMouseEventArgs class.
        /// </summary>
        /// <param name="x">X (left) position of mouse in pixels</param>
        /// <param name="y">Y (top) position of mouse in pixels</param>
        /// <param name="position"> Document position</param>
        public ScintillaMouseEventArgs(int x, int y, int position)
        {
            this._x = x;
            this._y = y;
            this._position = position;
        }

        #endregion Constructors
    }
}
