#region Using Directives

using System;

#endregion


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Provides data for the LinesNeedShown event
    /// </summary>
    public class LinesNeedShownEventArgs : EventArgs
    {
        #region Fields

        private readonly int _firstLine;
        private int _lastLine;

        #endregion Fields


        #region Properties

        /// <summary>
        ///     Returns the first (top) line that needs to be shown
        /// </summary>
        public int FirstLine
        {
            get { return this._firstLine; }
        }


        /// <summary>
        ///     Returns the last (bottom) line that needs to be shown
        /// </summary>
        public int LastLine
        {
            get { return this._lastLine; }
            set { this._lastLine = value; }
        }

        #endregion Properties


        #region Constructors

        /// <summary>
        ///     Initializes a new instance of the LinesNeedShownEventArgs class.
        /// </summary>
        /// <param name="startLine">the first (top) line that needs to be shown</param>
        /// <param name="endLine">the last (bottom) line that needs to be shown</param>
        public LinesNeedShownEventArgs(int startLine, int endLine)
        {
            this._firstLine = startLine;
            this._lastLine = endLine;
        }

        #endregion Constructors
    }
}
