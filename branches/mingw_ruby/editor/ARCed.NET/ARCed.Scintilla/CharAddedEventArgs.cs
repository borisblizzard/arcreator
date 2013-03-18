#region Using Directives

using System;

#endregion


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Provides data for the CharAdded event
    /// </summary>
    public class CharAddedEventArgs : EventArgs
    {
        #region Fields

        private readonly char _ch;

        #endregion Fields


        #region Properties

        /// <summary>
        ///     Returns the character that was added
        /// </summary>
        public char Ch
        {
            get
            {
                return this._ch;
            }
        }

        #endregion Properties


        #region Constructors

        /// <summary>
        ///     Initializes a new instance of the CharAddedEventArgs class.
        /// </summary>
        /// <param name="ch">The character that was added</param>
        public CharAddedEventArgs(char ch)
        {
            this._ch = ch;
        }

        #endregion Constructors
    }
}
