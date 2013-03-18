#region Using Directives



#endregion Using Directives


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Provides data for the StyleChanged event
    /// </summary>
    /// <remarks>
    ///     StyleChangedEventHandler is used for the StyleChanged Event which is also used as 
    ///     a more specific abstraction around the SCN_MODIFIED notification message.
    /// </remarks>
    public class StyleChangedEventArgs : ModifiedEventArgs
    {
        #region Fields

        private readonly int _length;
        private readonly int _position;

        #endregion Fields


        #region Properties

        /// <summary>
        ///     Returns how many characters have changed
        /// </summary>
        public int Length
        {
            get
            {
                return this._length;
            }
        }


        /// <summary>
        ///     Returns the starting document position where the style has been changed
        /// </summary>
        public int Position
        {
            get
            {
                return this._position;
            }
        }

        #endregion Properties


        #region Constructors

        internal StyleChangedEventArgs(int position, int length, int modificationType) : base(modificationType)
        {
            this._position = position;
            this._length = length;
        }

        #endregion Constructors
    }
}
